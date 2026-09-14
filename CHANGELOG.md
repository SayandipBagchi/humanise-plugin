# Changelog

## 2.0.0

Restructure. Same editing philosophy, less context per invocation, and a second skill instead of a second job bolted onto the first.

### Breaking

- Split into two skills. `humanise` rewrites prose; `meeting-talk` produces spoken lines. The meeting route is no longer a section inside `humanise`, and `meeting-pack.md` moved to `skills/meeting-talk/references/`.
- `agents/openai.yaml` moved to `hosts/openai.yaml`. In Claude plugin format `agents/` means subagents, so the old location was a naming collision.
- `evals/evals.json` replaced by per-case directories at the package root, each with `prompt.md`, `case.yaml`, and `graders/`. The suite is now scoreable instead of prose-only.
- Version and author are declared once, in `.claude-plugin/plugin.json`. Removed from skill frontmatter bodies, references, and the validator's hardcoded constant.

### Added

- Four slash commands: `/humanise:humanise`, `/humanise:talk-track`, `/humanise:pushback`, `/humanise:audit`.
- Edit-intensity dial (light, standard, heavy) with standard as the default, selected by tell count or by the user.
- Do-no-harm stop rule. Under two tells, the text comes back substantially unchanged, and trading one tell for another counts as a failed edit.
- Length contract. Output stays within 85 to 115 percent of input unless the user asked otherwise; large cuts are surfaced rather than made silently.
- Channel register reference: Slack, email, PRD, Jira, Confluence, release note, commit and pull request, executive update.
- Long-document route with stable headings, anchors, cross-references, and per-section fact checking.
- Specified "what changed" report format, which was referenced but never defined.
- Voice-profile template, replacing one-shot sample handling.
- Full-passage before-and-after example, including the patched rewrite that fails, and a worked talk track.
- Protected-content section now names legal, regulatory, and mandated wording, and locks the source's spelling convention so British copy does not drift American.

### Changed

- Pattern catalogue moved out of `SKILL.md` into `references/pattern-catalogue.md`. `SKILL.md` drops from 278 to roughly 150 lines; the catalogue loads only during a rewrite.
- The five most persistent tells promoted into a final gate in `SKILL.md`, dash rule first, so the common checks need no file read.
- 25 patterns deduped to 21 with no loss of coverage: heading-repeat merged into restating, `-ing` riders into inflated significance, curly quotes into decorative formatting, and vague connection merged with avoided plain verbs. Overlapping vocabulary consolidated into one shared word list.
- Assistant-wrapper removal stated once, in the output section, instead of three times.
- Skill descriptions rewritten for triggering, with explicit negative cases.
- Validator rewritten for the two-skill layout, the new eval format, and single-source versioning.

## 1.1.0

- Single `humanise` skill with a 25-pattern catalogue, a meeting reference, portability notes, 20 prose evals, and a structural validator.
