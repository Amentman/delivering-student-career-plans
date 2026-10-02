import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_skill_name_matches_repository(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^name:\s*delivering-student-career-plans$")

    def test_markdown_references_are_local_and_resolvable(self):
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
        for markdown in ROOT.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for target in link_pattern.findall(text):
                if target.startswith(("http://", "https://")):
                    continue
                self.assertFalse(target.startswith("/"), f"absolute link in {markdown}: {target}")
                self.assertTrue(
                    (markdown.parent / target).resolve().is_file(),
                    f"missing link in {markdown}: {target}",
                )

    def test_bundled_visual_validator_is_present(self):
        validator = ROOT / "scripts" / "vendor" / "validate_visual_manifest.py"
        self.assertTrue(validator.is_file())

    def test_repository_has_no_private_targets_or_absolute_user_paths(self):
        text_suffixes = {".md", ".py", ".yaml", ".yml", ".json", ".toml", ".txt"}
        corpus = "\n".join(
            path.read_text(encoding="utf-8")
            for path in ROOT.rglob("*")
            if path.is_file() and ".git" not in path.parts and path.suffix in text_suffixes
        )
        forbidden = (
            "/" + "Users" + "/",
            r"space_id`?:\s*`?\d{10,}",
            r"https://[^\s)]+(?:feishu\.cn|larksuite\.com)/(?:wiki|docx|docs|base|drive)/[^\s)]+",
            r"sk-[A-Za-z0-9_-]{16,}",
            r"AKIA[0-9A-Z]{16}",
            r"gh[pousr]_[A-Za-z0-9]{20,}",
            r"Bearer\s+[A-Za-z0-9._-]{20,}",
        )
        for pattern in forbidden:
            self.assertIsNone(re.search(pattern, corpus, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()
