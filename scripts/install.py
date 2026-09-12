#!/usr/bin/env python3
"""Install the UI/UX workflow using only the Python standard library."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys


START = b"<!-- ui-ux-workflow:start -->"
END = b"<!-- ui-ux-workflow:end -->"
SKILLS = ("ui-ux", "ui-ux-style", "ui-ux-prototype", "ui-ux-plan", "ui-ux-build", "ui-ux-review")
BLOCK_KEYS = {"project-rules/AGENTS.md", "project-rules/CLAUDE.md", "codex-rules/AGENTS.md", "claude-rules/CLAUDE.md"}
ROOT_KEYS = {"project-rules", "codex-rules", "claude-rules", "codex-skills", "claude-skills"}


class Conflict(Exception):
    """A preflight finding that must be resolved without overwriting local work."""


def digest(content):
    return hashlib.sha256(content).hexdigest()


def valid_relative(key):
    parts = key.split("/")
    return all(part and part not in (".", "..") and not part.endswith((".", " "))
               and not re.search(r'[\\:<>"|?*\x00-\x1f]', part)
               and not re.fullmatch(r"(?i)(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?", part)
               for part in parts)


def check_path(path, expect_file=False):
    """Reject redirects and incompatible types before reading or writing a target."""
    for current in reversed((path, *path.parents)):
        try:
            info = current.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 1024):
            raise Conflict(f"Symbolic link, junction, or reparse point is not supported: {current}")
        should_be_file = current == path and expect_file
        if (should_be_file and not stat.S_ISREG(info.st_mode)) or (not should_be_file and not stat.S_ISDIR(info.st_mode)):
            raise Conflict(f"Unexpected file or directory type: {current}")


def read_source(package):
    contents = {}

    def visit(directory):
        check_path(directory)
        for source in sorted(directory.iterdir()):
            check_path(source, expect_file=not source.is_dir())
            if source.is_dir():
                visit(source)
            else:
                relative = source.relative_to(package / "skills").as_posix()
                if not valid_relative(relative):
                    raise Conflict(f"Unsafe package file name: {source}")
                contents[relative] = source.read_bytes()

    for name in SKILLS:
        required = package / "skills" / name / "SKILL.md"
        check_path(required, expect_file=True)
        if not required.is_file():
            raise Conflict(f"Missing required skill: {name}")
        visit(required.parent)
    return contents


def load_manifest(path, scope):
    if not path.exists():
        return {"schema": 1, "scope": scope, "platforms": {}, "roots": {}, "files": {}, "blocks": {}}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict) or set(value) != {"schema", "scope", "platforms", "roots", "files", "blocks"} or value["schema"] != 1 or value["scope"] != scope:
            raise ValueError
        if any(not isinstance(value[field], dict) for field in ("platforms", "roots", "files", "blocks")):
            raise ValueError
        if not set(value["platforms"]).issubset({"codex", "claude"}) or not all(isinstance(version, str) for version in value["platforms"].values()):
            raise ValueError
        if not set(value["roots"]).issubset(ROOT_KEYS) or not all(isinstance(root, str) for root in value["roots"].values()):
            raise ValueError
        for key, checksum in value["files"].items():
            parts = key.split("/")
            if not valid_relative(key) or len(parts) < 3 or parts[0] not in ("codex-skills", "claude-skills") or parts[1] not in SKILLS:
                raise ValueError
            if not isinstance(checksum, str) or not re.fullmatch("[a-f0-9]{64}", checksum):
                raise ValueError
        for key, checksum in value["blocks"].items():
            if key not in BLOCK_KEYS or not isinstance(checksum, str) or not re.fullmatch("[a-f0-9]{64}", checksum):
                raise ValueError
        return value
    except (ValueError, UnicodeError, TypeError, AttributeError):
        raise Conflict(f"Invalid ownership manifest: {path}") from None


def managed_block(existing, path):
    if START not in existing and END not in existing:
        return None
    if existing.count(START) != 1 or existing.count(END) != 1 or existing.index(START) > existing.index(END):
        raise Conflict(f"Malformed managed markers in {path}")
    return existing[existing.index(START):existing.index(END) + len(END)]


def update_rules(existing, body, version, path):
    newline = b"\r\n" if b"\r\n" in existing else b"\n"
    block = newline.join((START, f"Installed UI/UX workflow version: {version}".encode(), body.strip().replace(b"\r\n", b"\n").replace(b"\n", newline), END))
    previous = managed_block(existing, path)
    if previous is not None:
        start = existing.index(START)
        return existing[:start] + block + existing[start + len(previous):], block
    separator = b"" if not existing else (newline if existing.endswith(newline) else newline * 2)
    return existing + separator + block + newline, block


def has_claude_import(content):
    """Recognize an existing prose import while ignoring Markdown code examples."""
    fence = None
    for line in content.splitlines():
        marker = re.match(rb"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[:1] == fence[:1] and len(token) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        prose = re.sub(rb"(`+).*?\1", b"", line)
        if re.search(rb"(?<![\w@\\])@(?:\./)?AGENTS\.md(?=$|[\s,;:)])", prose):
            return True
    return False


def install(args, package):
    base = (args.project_dir if args.scope == "project" else Path.home()).absolute()
    check_path(base)
    for required in (package / "VERSION", package / "adapters" / "rules.md"):
        check_path(required, expect_file=True)
        if not required.is_file():
            raise Conflict(f"Missing package metadata: {required.name}")
    source_files = read_source(package)
    version = (package / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:[-+][0-9A-Za-z.-]+)?", version):
        raise Conflict("VERSION must contain a single semantic version")
    platforms = ("codex", "claude") if args.platform == "both" else (args.platform,)
    roots = {
        "codex-skills": base / ".agents" / "skills",
        "claude-skills": base / ".claude" / "skills",
        "project-rules": base,
        "codex-rules": Path(os.environ.get("CODEX_HOME", base / ".codex")).absolute(),
        "claude-rules": base / ".claude",
    }
    manifest_path = base / ".ui-ux-workflow" / "install.json"
    check_path(manifest_path, expect_file=True)
    manifest = load_manifest(manifest_path, args.scope)
    installed_platforms = manifest["platforms"]
    if (args.scope == "project" and args.platform != "both"
            and len(set(installed_platforms) | set(platforms)) > 1
            and any(installed_version != version for installed_version in installed_platforms.values())):
        raise Conflict("Project platforms share AGENTS.md; use --platform both to upgrade their versions together")
    writes = {}
    desired = {}
    for platform in platforms:
        for relative, content in source_files.items():
            if platform == "claude" and relative.endswith("/agents/openai.yaml"):
                continue
            desired[f"{platform}-skills/{relative}"] = content
    rules = (package / "adapters" / "rules.md").read_bytes()
    rule_bodies = {}
    if args.scope == "project" or "codex" in platforms:
        rule_bodies[("project-rules" if args.scope == "project" else "codex-rules") + "/AGENTS.md"] = rules
    if "claude" in platforms:
        rule_bodies[("project-rules" if args.scope == "project" else "claude-rules") + "/CLAUDE.md"] = b"@AGENTS.md" if args.scope == "project" else rules

    def destination(key):
        root_name, relative = key.split("/", 1)
        root = roots[root_name]
        old_root = manifest["roots"].get(root_name)
        if args.scope == "user" and old_root is not None and old_root != str(root):
            raise Conflict(f"Install location changed for {root_name}; resolve the previous installation first")
        # Project destinations always come from these fixed mappings, so a
        # checkout may move without retaining machine-specific absolute roots.
        manifest["roots"][root_name] = root.relative_to(base).as_posix() if args.scope == "project" else str(root)
        target = root / relative
        check_path(target, expect_file=True)
        return target

    for key, content in desired.items():
        target = destination(key)
        current = target.read_bytes() if target.exists() else None
        owned = manifest["files"].get(key)
        if owned is not None:
            if current is None or digest(current) != owned:
                raise Conflict(f"Locally changed or missing installed file: {target}")
        elif current is not None:
            raise Conflict(f"Existing file is not owned by this installer: {target}")
        writes[target] = content
        manifest["files"][key] = digest(content)
    removals = []
    for key, owned in list(manifest["files"].items()):
        if key.split("/", 1)[0] in {f"{platform}-skills" for platform in platforms} and key not in desired:
            target = destination(key)
            if not target.is_file() or digest(target.read_bytes()) != owned:
                raise Conflict(f"Locally changed or missing stale installed file: {target}")
            removals.append(target)
            del manifest["files"][key]
    for key, body in rule_bodies.items():
        target = destination(key)
        current = target.read_bytes() if target.exists() else b""
        previous = managed_block(current, target)
        owned = manifest["blocks"].get(key)
        if owned is not None:
            if previous is None or digest(previous) != owned:
                raise Conflict(f"Locally changed or missing managed rules: {target}")
        elif previous is not None:
            raise Conflict(f"Existing managed block is not owned by this installer: {target}")
        external_import = key == "project-rules/CLAUDE.md" and previous is None and has_claude_import(current)
        if not external_import:
            content, block = update_rules(current, body, version, target)
            writes[target] = content
            manifest["blocks"][key] = digest(block)
    for platform in platforms:
        manifest["platforms"][platform] = version
    writes[manifest_path] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
    changes = {target: content for target, content in writes.items() if not target.exists() or target.read_bytes() != content}
    if args.dry_run:
        print(f"Dry run: UI/UX workflow {version}")
        for target in changes:
            print(f"Would write {target}")
        for target in removals:
            print(f"Would remove {target}")
        return 0
    for target in removals:
        target.unlink()
    for target, content in changes.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    print(f"Installed UI/UX workflow {version} ({args.scope}, {args.platform}); {len(changes)} files changed.")
    return 0


def main(argv=None, package_root=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=("user", "project"), required=True)
    parser.add_argument("--platform", choices=("codex", "claude", "both"), required=True)
    parser.add_argument("--project-dir", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    package = Path(package_root) if package_root else Path(__file__).resolve().parents[1]
    try:
        return install(args, package)
    except Conflict as error:
        print(f"Conflict: {error}. No files were changed.")
        return 1


if __name__ == "__main__":
    # A legacy Windows console may not represent an otherwise valid file path.
    # Escape only unrepresentable console characters; installed bytes stay exact.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="backslashreplace")
    raise SystemExit(main())
