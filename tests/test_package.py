"""Distribution contracts: discoverability and relocatable skill references."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("ui-ux", "ui-ux-style", "ui-ux-prototype", "ui-ux-plan", "ui-ux-build", "ui-ux-review")


class PackageTests(unittest.TestCase):
    def test_every_entrypoint_links_the_shared_model_routing_contract(self):
        policy = (ROOT / "skills" / "ui-ux" / "references" / "model-routing.md").resolve()
        self.assertTrue(policy.is_file(), "The shared routing contract must be distributed")
        for name in SKILLS:
            entry = ROOT / "skills" / name / "SKILL.md"
            targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)", entry.read_text(encoding="utf-8"))
            local_targets = {
                (entry.parent / target.split("#", 1)[0]).resolve()
                for target in targets if "://" not in target and not target.startswith("#")
            }
            with self.subTest(skill=name):
                self.assertIn(policy, local_targets, "Direct skill invocation must reach the shared routing contract")

    def test_every_phase_is_discoverable_and_small(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                entry = ROOT / "skills" / name / "SKILL.md"
                self.assertTrue(entry.is_file(), f"Missing discoverable entrypoint: {entry}")
                content = entry.read_text(encoding="utf-8")
                self.assertTrue(content.startswith("---\n"), "YAML frontmatter must start the file")
                parts = content.split("---", 2)
                self.assertEqual(len(parts), 3)
                metadata = dict(re.findall(r"^([\w-]+):\s*(.*?)\s*$", parts[1], re.M))
                self.assertEqual(metadata.get("name", "").strip('"'), name)
                description = metadata.get("description", "").strip('"')
                self.assertTrue(description.startswith("Use when"))
                self.assertLessEqual(len(description), 1024)
                self.assertLess(len(content.split()), 500)
                self.assertNotIn("disable-model-invocation: true", content)

    def test_local_skill_links_survive_installation_of_the_skill_bundle(self):
        skill_root = ROOT / "skills"
        documents = list(skill_root.rglob("*.md"))
        self.assertTrue(documents, "The bundle must contain skill documents")
        for document in documents:
            content = document.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
                if "://" in target or target.startswith("#"):
                    continue
                relative = target.split("#", 1)[0]
                if not relative:
                    continue
                resolved = (document.parent / relative).resolve()
                with self.subTest(document=document, target=target):
                    self.assertTrue(resolved.is_relative_to(skill_root.resolve()), "Installed references must stay inside the skill bundle")
                    self.assertTrue(resolved.is_file(), "Referenced file must be distributed")

    def test_codex_metadata_keeps_implicit_invocation_available(self):
        for name in SKILLS:
            metadata = ROOT / "skills" / name / "agents" / "openai.yaml"
            with self.subTest(skill=name):
                self.assertTrue(metadata.is_file())
                content = metadata.read_text(encoding="utf-8")
                self.assertRegex(content, r"allow_implicit_invocation:\s*true")
                self.assertIn(f"${name}", content)


if __name__ == "__main__":
    unittest.main()
