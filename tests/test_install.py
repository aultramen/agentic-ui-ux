"""Behavioral tests exercise the installer against disposable homes and projects."""

import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import subprocess
import shutil
import sys
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install.py"
SKILLS = ("ui-ux", "ui-ux-style", "ui-ux-prototype", "ui-ux-plan", "ui-ux-build", "ui-ux-review")


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = self.root / "package"
        self.project = self.root / "project with spaces é"
        self.home = self.root / "home"
        self.project.mkdir()
        self.home.mkdir()
        (self.package / "adapters").mkdir(parents=True)
        (self.package / "VERSION").write_text("0.1.0\n", encoding="utf-8")
        (self.package / "adapters" / "rules.md").write_text("Use ui-ux for frontend work.\n", encoding="utf-8")
        for name in SKILLS:
            folder = self.package / "skills" / name
            (folder / "agents").mkdir(parents=True)
            (folder / "references").mkdir()
            (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Test\n---\nRead references/workflow.md.\n", encoding="utf-8")
            (folder / "references" / "workflow.md").write_text("Follow the approved workflow.\n", encoding="utf-8")
            (folder / "agents" / "openai.yaml").write_text("interface: {}\n", encoding="utf-8")
        self.environment = patch.dict(os.environ, {"USERPROFILE": str(self.home), "HOME": str(self.home)})
        self.environment.start()
        self.addCleanup(self.environment.stop)
        os.environ.pop("CODEX_HOME", None)

    def run_install(self, *args):
        self.assertTrue(SCRIPT.is_file(), "The standalone installer has not been implemented")
        spec = importlib.util.spec_from_file_location("ui_ux_installer_test", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            try:
                result = module.main(list(args), package_root=self.package)
            except SystemExit as error:
                result = error.code
        return result, output.getvalue()

    def install_project(self, *extra):
        return self.run_install("--scope", "project", "--platform", "codex", "--project-dir", str(self.project), *extra)

    def snapshot(self, directory):
        return {path.relative_to(directory).as_posix(): path.read_bytes() if path.is_file() else None for path in directory.rglob("*")}

    def test_installs_all_six_project_codex_skills(self):
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        for name in SKILLS:
            target = self.project / ".agents" / "skills" / name
            self.assertEqual((target / "SKILL.md").read_bytes(), (self.package / "skills" / name / "SKILL.md").read_bytes())
            self.assertTrue((target / "references" / "workflow.md").is_file())
            self.assertTrue((target / "agents" / "openai.yaml").is_file())

    def test_platform_and_scope_routes_skills_and_preserves_rule_content(self):
        existing = b"# Existing instructions\r\nKeep my configuration.\r\n"
        for scope in ("project", "user"):
            for platform in ("codex", "claude", "both"):
                with self.subTest(scope=scope, platform=platform):
                    destination = self.root / f"{scope}-{platform}"
                    destination.mkdir()
                    codex_home = destination / "custom-codex-config"
                    agents = destination / "AGENTS.md" if scope == "project" else codex_home / "AGENTS.md"
                    claude = destination / "CLAUDE.md" if scope == "project" else destination / ".claude" / "CLAUDE.md"
                    for rule in (agents, claude):
                        rule.parent.mkdir(parents=True, exist_ok=True)
                        rule.write_bytes(existing)
                    with patch.dict(os.environ, {"USERPROFILE": str(destination), "HOME": str(destination), "CODEX_HOME": str(codex_home)}):
                        result, output = self.run_install("--scope", scope, "--platform", platform, "--project-dir", str(destination))
                    self.assertEqual(result, 0, output)
                    for selected, directory in (("codex", ".agents"), ("claude", ".claude")):
                        skill_base = destination / directory / "skills"
                        self.assertEqual(skill_base.exists(), platform in (selected, "both"))
                        if skill_base.exists():
                            for name in SKILLS:
                                self.assertTrue((skill_base / name / "SKILL.md").is_file())
                                self.assertEqual((skill_base / name / "agents" / "openai.yaml").exists(), selected == "codex")
                    for rule in (agents, claude):
                        self.assertTrue(rule.read_bytes().startswith(existing))
                    if scope == "project" or platform in ("codex", "both"):
                        self.assertIn(b"Use ui-ux for frontend work.", agents.read_bytes())
                        self.assertIn(b"0.1.0", agents.read_bytes())
                    if platform in ("claude", "both"):
                        expected = b"@AGENTS.md" if scope == "project" else b"Use ui-ux for frontend work."
                        self.assertIn(expected, claude.read_bytes())

    def test_dry_run_creates_no_files_or_directories_and_reports_actions(self):
        for scope, directory in (("project", self.project), ("user", self.home)):
            with self.subTest(scope=scope):
                before = self.snapshot(directory)
                result, output = self.run_install("--scope", scope, "--platform", "both", "--project-dir", str(self.project), "--dry-run")
                self.assertEqual(result, 0, output)
                self.assertEqual(self.snapshot(directory), before)
                self.assertIn("Dry run", output)
                self.assertIn("SKILL.md", output)

    def test_cli_requires_scope_and_platform_and_rejects_unknown_choices(self):
        for args in ((), ("--scope", "project"), ("--platform", "codex"), ("--scope", "all", "--platform", "codex"), ("--scope", "user", "--platform", "unknown")):
            with self.subTest(args=args):
                result, output = self.run_install(*args)
                self.assertEqual(result, 2, output)
                self.assertIn("usage:", output)
                self.assertEqual(self.snapshot(self.project), {})
                self.assertEqual(self.snapshot(self.home), {})

    def test_reinstall_is_idempotent_and_keeps_existing_claude_import(self):
        existing = b"# Team rules\r\n@AGENTS.md\r\nKeep these rules."
        (self.project / "CLAUDE.md").write_bytes(existing)
        for unused in range(2):
            result, output = self.run_install("--scope", "project", "--platform", "both", "--project-dir", str(self.project))
            self.assertEqual(result, 0, output)
            self.assertEqual((self.project / "CLAUDE.md").read_bytes(), existing)
        before = self.snapshot(self.project)
        times = {str(path): path.stat().st_mtime_ns for path in self.project.rglob("*") if path.is_file()}
        result, output = self.run_install("--scope", "project", "--platform", "both", "--project-dir", str(self.project))
        self.assertEqual(result, 0, output)
        self.assertEqual(self.snapshot(self.project), before)
        self.assertEqual({str(path): path.stat().st_mtime_ns for path in self.project.rglob("*") if path.is_file()}, times)
        self.assertEqual((self.project / "AGENTS.md").read_bytes().count(b"<!-- ui-ux-workflow:start -->"), 1)

    def test_manifest_tracks_version_and_reinstall_rejects_edited_skill_before_any_write(self):
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        manifest = self.project / ".ui-ux-workflow" / "install.json"
        self.assertTrue(manifest.is_file(), "An installation needs an ownership manifest")
        self.assertIn("0.1.0", manifest.read_text(encoding="utf-8"))
        changed = self.project / ".agents" / "skills" / "ui-ux-review" / "SKILL.md"
        secret = "LOCAL-SECRET-not-for-output"
        changed.write_text(secret, encoding="utf-8")
        (self.package / "skills" / "ui-ux" / "SKILL.md").write_text("New source version", encoding="utf-8")
        before = self.snapshot(self.project)
        for extra in ((), ("--dry-run",)):
            result, output = self.install_project(*extra)
            self.assertNotEqual(result, 0)
            self.assertIn("Conflict", output)
            self.assertNotIn(secret, output)
            self.assertEqual(self.snapshot(self.project), before)

    def test_unowned_existing_skill_is_never_overwritten(self):
        target = self.project / ".agents" / "skills" / "ui-ux-review" / "SKILL.md"
        target.parent.mkdir(parents=True)
        target.write_text("My preexisting skill", encoding="utf-8")
        before = self.snapshot(self.project)
        result, output = self.install_project()
        self.assertNotEqual(result, 0)
        self.assertIn("Conflict", output)
        self.assertEqual(self.snapshot(self.project), before)

    def test_edited_managed_rules_abort_but_unmanaged_edits_are_preserved(self):
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        rules = self.project / "AGENTS.md"
        rules.write_bytes(b"My new instructions\r\n" + rules.read_bytes() + b"\r\nMore user instructions.")
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        self.assertTrue(rules.read_bytes().startswith(b"My new instructions\r\n"))
        self.assertTrue(rules.read_bytes().endswith(b"More user instructions."))
        rules.write_bytes(rules.read_bytes().replace(b"Use ui-ux for frontend work.", b"Local managed-block change."))
        before = self.snapshot(self.project)
        result, output = self.install_project()
        self.assertNotEqual(result, 0)
        self.assertIn("Conflict", output)
        self.assertEqual(self.snapshot(self.project), before)

    def test_user_upgrade_removes_only_unchanged_owned_stale_files_and_preserves_other_platform(self):
        result, output = self.run_install("--scope", "user", "--platform", "both")
        self.assertEqual(result, 0, output)
        codex = self.home / ".agents" / "skills" / "ui-ux"
        claude = self.home / ".claude" / "skills" / "ui-ux"
        local = codex / "my-notes.txt"
        local.write_text("Keep these unrelated notes", encoding="utf-8")
        source = self.package / "skills" / "ui-ux"
        (source / "references" / "workflow.md").unlink()
        (source / "references" / "new.md").write_text("Revised workflow", encoding="utf-8")
        (self.package / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        before = self.snapshot(self.home)
        result, output = self.run_install("--scope", "user", "--platform", "codex", "--dry-run")
        self.assertEqual(result, 0, output)
        self.assertIn("Would remove", output)
        self.assertEqual(self.snapshot(self.home), before)
        result, output = self.run_install("--scope", "user", "--platform", "codex")
        self.assertEqual(result, 0, output)
        self.assertFalse((codex / "references" / "workflow.md").exists())
        self.assertTrue((codex / "references" / "new.md").is_file())
        self.assertEqual(local.read_text(encoding="utf-8"), "Keep these unrelated notes")
        self.assertTrue((claude / "references" / "workflow.md").is_file())
        self.assertFalse((claude / "references" / "new.md").exists())
        manifest = json.loads((self.home / ".ui-ux-workflow" / "install.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["platforms"], {"codex": "0.2.0", "claude": "0.1.0"})
        self.assertIn(b"0.2.0", (self.home / ".codex" / "AGENTS.md").read_bytes())

    def test_upgrade_aborts_if_stale_owned_file_was_edited(self):
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        (self.project / ".agents" / "skills" / "ui-ux" / "references" / "workflow.md").write_text("Local customization", encoding="utf-8")
        (self.package / "skills" / "ui-ux" / "references" / "workflow.md").unlink()
        (self.package / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        before = self.snapshot(self.project)
        result, output = self.install_project()
        self.assertNotEqual(result, 0)
        self.assertIn("Conflict", output)
        self.assertEqual(self.snapshot(self.project), before)

    def test_hostile_manifest_cannot_delete_a_file_outside_owned_skill_paths(self):
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        victim = self.root / "outside.txt"
        victim.write_text("Must survive", encoding="utf-8")
        manifest_path = self.project / ".ui-ux-workflow" / "install.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["files"]["codex-skills/../../../outside.txt"] = hashlib.sha256(victim.read_bytes()).hexdigest()
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        before = self.snapshot(self.project)
        result, output = self.install_project()
        self.assertNotEqual(result, 0)
        self.assertIn("Conflict", output)
        self.assertTrue(victim.is_file())
        self.assertEqual(self.snapshot(self.project), before)

    def directory_link(self, link, target):
        if os.name == "nt":
            process = subprocess.run(["cmd.exe", "/c", "mklink", "/J", str(link), str(target)], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            if process.returncode:
                self.skipTest("Windows junction creation unavailable")
        else:
            link.symlink_to(target, target_is_directory=True)

    def test_destination_junction_or_symlink_cannot_escape_install_root(self):
        outside = self.root / "outside-directory"
        outside.mkdir()
        self.directory_link(self.project / ".agents", outside)
        before = self.snapshot(outside)
        result, output = self.install_project()
        self.assertNotEqual(result, 0)
        self.assertIn("Conflict", output)
        self.assertEqual(self.snapshot(outside), before)
        self.assertFalse((self.project / "AGENTS.md").exists())

    def test_missing_required_skill_aborts_before_any_destination_change(self):
        (self.package / "skills" / "ui-ux-review" / "SKILL.md").unlink()
        result, output = self.install_project()
        self.assertNotEqual(result, 0)
        self.assertIn("Conflict", output)
        self.assertEqual(self.snapshot(self.project), {})

    def test_invalid_package_version_is_rejected_without_echoing_content(self):
        secret = "PRIVATE-package-content\nUnexpected instruction"
        (self.package / "VERSION").write_text(secret, encoding="utf-8")
        result, output = self.install_project()
        self.assertNotEqual(result, 0)
        self.assertIn("Conflict", output)
        self.assertNotIn(secret, output)
        self.assertNotIn("PRIVATE-package-content", output)
        self.assertEqual(self.snapshot(self.project), {})

    def test_missing_package_metadata_returns_controlled_error_without_writes(self):
        (self.package / "VERSION").unlink()
        try:
            result, output = self.install_project()
        except OSError:
            self.fail("Missing package metadata must return a controlled error, not raise an OS exception")
        self.assertNotEqual(result, 0)
        self.assertIn("Conflict", output)
        self.assertEqual(self.snapshot(self.project), {})

    def test_claude_import_examples_do_not_count_as_active_imports(self):
        examples = b"# Documentation\n```markdown\n@AGENTS.md\n```\nAn inline example: `@AGENTS.md`.\n"
        claude = self.project / "CLAUDE.md"
        claude.write_bytes(examples)
        result, output = self.run_install("--scope", "project", "--platform", "claude", "--project-dir", str(self.project))
        self.assertEqual(result, 0, output)
        self.assertTrue(claude.read_bytes().startswith(examples))
        self.assertIn(b"<!-- ui-ux-workflow:start -->", claude.read_bytes())

    def test_existing_inline_claude_import_is_not_duplicated(self):
        existing = b"# Team rules\nRead @AGENTS.md for the shared project rules.\n"
        claude = self.project / "CLAUDE.md"
        claude.write_bytes(existing)
        result, output = self.run_install("--scope", "project", "--platform", "claude", "--project-dir", str(self.project))
        self.assertEqual(result, 0, output)
        self.assertEqual(claude.read_bytes(), existing)

    def test_project_install_can_be_renamed_and_upgraded(self):
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        renamed = self.root / "renamed project"
        self.assertTrue(self.project.resolve().is_relative_to(self.root.resolve()))
        self.assertTrue(renamed.resolve().is_relative_to(self.root.resolve()))
        self.project.rename(renamed)
        self.project = renamed
        (self.package / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        self.assertIn(b"0.2.0", (renamed / "AGENTS.md").read_bytes())

    def test_project_with_both_platforms_requires_coordinated_version_upgrade(self):
        result, output = self.run_install("--scope", "project", "--platform", "both", "--project-dir", str(self.project))
        self.assertEqual(result, 0, output)
        (self.package / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        before = self.snapshot(self.project)
        for platform in ("codex", "claude"):
            for extra in ((), ("--dry-run",)):
                result, output = self.run_install("--scope", "project", "--platform", platform, "--project-dir", str(self.project), *extra)
                self.assertNotEqual(result, 0)
                self.assertIn("--platform both", output)
                self.assertEqual(self.snapshot(self.project), before)
        result, output = self.run_install("--scope", "project", "--platform", "both", "--project-dir", str(self.project))
        self.assertEqual(result, 0, output)
        manifest = json.loads((self.project / ".ui-ux-workflow" / "install.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["platforms"], {"codex": "0.2.0", "claude": "0.2.0"})

    def test_adding_second_project_platform_with_newer_version_requires_both(self):
        result, output = self.install_project()
        self.assertEqual(result, 0, output)
        (self.package / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        before = self.snapshot(self.project)
        result, output = self.run_install("--scope", "project", "--platform", "claude", "--project-dir", str(self.project))
        self.assertNotEqual(result, 0)
        self.assertIn("--platform both", output)
        self.assertEqual(self.snapshot(self.project), before)

    def test_native_cli_supports_unicode_paths_with_ascii_console_encoding(self):
        scripts = self.package / "scripts"
        scripts.mkdir()
        script = scripts / "install.py"
        shutil.copyfile(SCRIPT, script)
        project = self.root / "project \u4e2d\u6587"
        project.mkdir()
        environment = dict(os.environ, PYTHONIOENCODING="ascii")
        command = [sys.executable, str(script), "--scope", "project", "--platform", "codex", "--project-dir", str(project)]
        preview = subprocess.run([*command, "--dry-run"], capture_output=True, env=environment)
        self.assertEqual(preview.returncode, 0, preview.stderr.decode("ascii", errors="replace"))
        self.assertIn(b"Dry run", preview.stdout)
        self.assertIn(b"\\u4e2d\\u6587", preview.stdout)
        self.assertEqual(self.snapshot(project), {})
        local = project / ".agents" / "skills" / "ui-ux" / "SKILL.md"
        local.parent.mkdir(parents=True)
        local.write_text("Preserve this local skill", encoding="utf-8")
        before = self.snapshot(project)
        conflict = subprocess.run(command, capture_output=True, env=environment)
        self.assertEqual(conflict.returncode, 1, conflict.stderr.decode("ascii", errors="replace"))
        self.assertIn(b"Conflict", conflict.stdout)
        self.assertNotIn(b"UnicodeEncodeError", conflict.stderr)
        self.assertEqual(self.snapshot(project), before)


if __name__ == "__main__":
    unittest.main()
