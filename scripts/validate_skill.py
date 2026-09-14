#!/usr/bin/env python3
"""Validate the humanise plugin package. No third-party dependencies.

Run from anywhere:  python3 scripts/validate_skill.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FRONTMATTER_KEYS = {"name", "description", "metadata", "allowed-tools", "license"}

# Version and author are declared once, in .claude-plugin/plugin.json.
# Nothing else in the package restates them, so a bump is a one-line edit.
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"

SKILLS = {
    "humanise": {
        "required": [
            "references/pattern-catalogue.md",
            "references/channel-register.md",
            "references/portability.md",
            "examples/before-after-passage.md",
            "examples/change-report.md",
            "templates/voice-profile.md",
        ],
        "markers": [
            "How hard to edit",
            "Do no harm",
            "Final gate",
            "Protected content",
            "Long documents",
            "85",  # length band
            "meeting-talk",  # hand-off to the sibling skill
        ],
        "anti_markers": [
            "Pyramid Principle",  # belongs to meeting-talk now, not here
        ],
    },
    "meeting-talk": {
        "required": [
            "references/meeting-pack.md",
            "examples/sample-talk-track.md",
        ],
        "markers": [
            "Pyramid Principle",
            "BLUF",
            "SCQ",
            "Three to five",
            "evidence gap",
            "humanise",  # hand-off to the sibling skill
        ],
        "anti_markers": [
            "pattern catalogue",  # belongs to humanise, not here
        ],
    },
}

REFERENCE_MARKERS = {
    "skills/humanise/references/pattern-catalogue.md": [
        "Not X but Y",
        "weak alone",
        "Dashes as the universal connector",
    ],
    "skills/humanise/references/channel-register.md": [
        "Slack",
        "PRD",
        "Commit message",
        "Executive update",
    ],
    "skills/humanise/references/portability.md": [
        "Codex",
        "ChatGPT",
        "Claude",
        ".agents/skills/humanise",
        "$humanise",
        "@humanise",
        "/humanise",
    ],
    "skills/meeting-talk/references/meeting-pack.md": [
        "Claim -> proof -> implication -> ask",
        "Handle pushback",
        "30 seconds",
        "2 minutes",
        "5 minutes",
    ],
}

COMMANDS = ("humanise.md", "talk-track.md", "pushback.md", "audit.md")

ROOT_FILES = ("README.md", "CHANGELOG.md", "LICENSE", ".gitignore")

EXPECTED_PATTERN_COUNT = 21

# Em dash, en dash, double hyphen, and spaced hyphen used as a dash.
DASH_RE = re.compile(r"[—–]|(?<=\s)--(?=\s)|(?<=\w)--(?=\w)|(?<=\s)-(?=\s)")

PROSE_GLOBS = ("skills/**/*.md", "commands/*.md", "README.md", "CHANGELOG.md")


def parse_frontmatter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if not text.startswith("---\n"):
        errors.append(f"{rel}: must start with YAML frontmatter")
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"{rel}: frontmatter must close with ---")
        return {}, text

    values: dict[str, str] = {}
    for number, line in enumerate(text[4:end].splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#") or line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            errors.append(f"{rel}: frontmatter line {number} is not a key/value pair")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key not in FRONTMATTER_KEYS:
            errors.append(f"{rel}: unsupported core frontmatter key: {key}")
        if value[:1] in {'"', "'"} and value.endswith(value[:1]):
            value = value[1:-1]
        values[key] = value
    return values, text[end + len("\n---\n"):]


def check_manifest(errors: list[str]) -> dict:
    if not MANIFEST.is_file():
        errors.append("missing .claude-plugin/plugin.json")
        return {}
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"plugin.json is not valid JSON: {exc}")
        return {}
    for key in ("name", "version", "description", "author"):
        if not data.get(key):
            errors.append(f"plugin.json is missing {key}")
    if data.get("name") != ROOT.name:
        errors.append(f"plugin.json name must match the folder name: {ROOT.name}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(data.get("version", ""))):
        errors.append("plugin.json version must be semver, for example 2.0.0")
    return data


def check_skill(slug: str, spec: dict, author: str, errors: list[str]) -> None:
    base = ROOT / "skills" / slug
    skill_md = base / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"missing skills/{slug}/SKILL.md")
        return

    frontmatter, body = parse_frontmatter(skill_md, errors)

    name = frontmatter.get("name", "")
    if name != slug:
        errors.append(f"skills/{slug}: frontmatter name must match the folder name")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"skills/{slug}: name must be lowercase with single hyphens")

    description = frontmatter.get("description", "").strip()
    if not description:
        errors.append(f"skills/{slug}: description must be non-empty")
    if len(description) > 1024:
        errors.append(f"skills/{slug}: description exceeds 1024 characters")
    if "Do not use" not in description and "do not use" not in description:
        errors.append(f"skills/{slug}: description should state when NOT to trigger")
    if "disable-model-invocation" in frontmatter:
        errors.append(f"skills/{slug}: no provider-specific invocation controls in portable frontmatter")

    head = skill_md.read_text(encoding="utf-8").split("\n---\n", 1)[0]
    if f"author: {author}" not in head:
        errors.append(f"skills/{slug}: frontmatter metadata must name the author: {author}")
    if re.search(r"^\s*version:", head, re.MULTILINE):
        errors.append(f"skills/{slug}: version must live only in plugin.json, not in skill frontmatter")

    line_count = len(body.splitlines())
    if line_count > 500:
        errors.append(f"skills/{slug}: SKILL.md body is {line_count} lines, over the 500-line target")

    for marker in spec["markers"]:
        if marker not in body:
            errors.append(f"skills/{slug}: SKILL.md is missing behaviour marker: {marker}")
    for marker in spec["anti_markers"]:
        if marker in body:
            errors.append(f"skills/{slug}: SKILL.md duplicates content that belongs elsewhere: {marker}")

    for relative in spec["required"]:
        if not (base / relative).is_file():
            errors.append(f"missing skills/{slug}/{relative}")

    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill_md.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        resolved = (base / target).resolve()
        if base.resolve() not in resolved.parents:
            errors.append(f"skills/{slug}: link escapes the skill root: {target}")
        elif not resolved.is_file():
            errors.append(f"skills/{slug}: link target does not exist: {target}")


def check_references(errors: list[str]) -> None:
    for relative, markers in REFERENCE_MARKERS.items():
        path = ROOT / relative
        if not path.is_file():
            continue  # the per-skill required-file check already reported it
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{relative} is missing marker: {marker}")

    catalogue = ROOT / "skills/humanise/references/pattern-catalogue.md"
    if catalogue.is_file():
        found = len(re.findall(r"^### \d+\. ", catalogue.read_text(encoding="utf-8"), re.MULTILINE))
        if found != EXPECTED_PATTERN_COUNT:
            errors.append(
                f"pattern catalogue must hold {EXPECTED_PATTERN_COUNT} numbered patterns (found {found})"
            )


def check_commands(errors: list[str]) -> None:
    for filename in COMMANDS:
        path = ROOT / "commands" / filename
        if not path.is_file():
            errors.append(f"missing commands/{filename}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"commands/{filename}: must start with frontmatter")
        if "description:" not in text.split("\n---\n", 1)[0]:
            errors.append(f"commands/{filename}: frontmatter needs a description")
        if "$ARGUMENTS" not in text:
            errors.append(f"commands/{filename}: must pass $ARGUMENTS through to the skill")


def check_dashes(errors: list[str]) -> None:
    """The skill bans dashes in its output, so its own prose should not use them."""
    for pattern in PROSE_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            rel = path.relative_to(ROOT)
            in_fence = False
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
                if line.lstrip().startswith("```"):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                stripped = re.sub(r"`[^`]*`", "", line)
                # Drop blockquote markers, then list markers, so "> - item" is not
                # read as a spaced hyphen. Quoted example text is still checked:
                # a sample output that uses a dash teaches the dash.
                stripped = re.sub(r"^(\s*>)+\s*", "", stripped)
                stripped = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", stripped)
                if stripped.strip() in {"---", "***", "___"}:
                    continue
                if DASH_RE.search(stripped):
                    errors.append(f"{rel}:{number}: dash in skill prose, which the skill itself forbids")


def check_evals(errors: list[str]) -> tuple[int, list[str]]:
    base = ROOT / "evals"
    if not base.is_dir():
        errors.append("missing evals/")
        return 0, []
    names = sorted(
        p.name for p in base.iterdir() if p.is_dir() and p.name not in {"results", "mocks"}
    )
    if not names:
        errors.append("evals/ holds no cases")
        return 0, []
    for name in names:
        case = base / name
        if not (case / "prompt.md").is_file():
            errors.append(f"evals/{name}: missing prompt.md")
        elif not (case / "prompt.md").read_text(encoding="utf-8").strip():
            errors.append(f"evals/{name}: prompt.md is empty")
        graders = case / "graders"
        if not graders.is_dir():
            errors.append(f"evals/{name}: missing graders/")
            continue
        for grader in ("criteria.md", "skill-fired.md"):
            path = graders / grader
            if not path.is_file():
                errors.append(f"evals/{name}: missing graders/{grader}")
            elif "- [ ]" not in path.read_text(encoding="utf-8"):
                errors.append(f"evals/{name}: graders/{grader} has no checkable items")
        case_yaml = case / "case.yaml"
        if case_yaml.is_file():
            text = case_yaml.read_text(encoding="utf-8")
            if not text.lstrip().startswith("context:"):
                errors.append(f"evals/{name}: case.yaml may only carry context.*")
    return len(names), names


def check_root_files(errors: list[str]) -> None:
    for filename in ROOT_FILES:
        if not (ROOT / filename).is_file():
            errors.append(f"missing {filename}")
    stray = ROOT / "agents"
    if stray.is_dir():
        errors.append("agents/ at the package root means subagents; host metadata belongs in hosts/")


def main() -> int:
    errors: list[str] = []
    manifest = check_manifest(errors)
    author = (manifest.get("author") or {}).get("name", "")

    for slug, spec in SKILLS.items():
        check_skill(slug, spec, author, errors)
    check_references(errors)
    check_commands(errors)
    check_root_files(errors)
    check_dashes(errors)
    case_count, case_names = check_evals(errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"\n{len(errors)} problem(s) found.")
        return 1

    version = manifest.get("version", "?")
    print(f"PASS: {ROOT.name} v{version} is structurally valid")
    print(f"PASS: {len(SKILLS)} skills, {len(COMMANDS)} commands, references and links resolve")
    print(f"PASS: pattern catalogue holds {EXPECTED_PATTERN_COUNT} patterns")
    print("PASS: no dashes in skill prose")
    print(f"PASS: version and author declared once, author is {author}")
    print(f"PASS: {case_count} eval cases with graders")
    for name in case_names:
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
