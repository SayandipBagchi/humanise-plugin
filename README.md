# Humanise

Two skills and four commands, for the last pass before something goes out.

**`humanise`** takes prose that reads like a language model wrote it and rewrites it so it reads like the person who asked. Every supported fact, number, quote, citation, and technical term survives. Nothing new gets invented. It works from a catalogue of 21 named patterns across five families, and it only acts on a weak pattern when several appear in the same passage.

**`meeting-talk`** turns a pitch, an update, a stakeholder conversation, or a pushback moment into sentences you can say in the room. Answer first, evidence under the reason it supports, trade-off named, concrete ask at the end. It keeps what the evidence shows separate from what you are inferring, and says so when something is unmeasured.

**Use it if** you have a draft that already says the right things in the wrong voice, or a position you have to say out loud, and you need every fact in it to survive the edit.

**Not for you if** you want new material. Nothing here invents a fact, a number or a quote, and it reports which patterns it found rather than deciding for you which draft is the right one.

Status: maintained, v2.0.0. Markdown only, so there is nothing to break between Claude Code releases.

## How the evals work, and why they came first

Eleven cases under `evals/`, each a prompt plus two graders. The cases were written while the pattern catalogue was being specified, not after the skill worked, and that ordering is the reason several of them exist. `humanise-clean-draft-no-harm` and `humanise-ignores-unrelated` are the ones that matter most: they check that the skill leaves alone writing that was already fine. A case like that is easy to write from a specification and almost impossible to think of once you have a working rewriter in front of you, because everything you test it on is something you already wanted it to change.

The graders are an LLM-as-judge setup held to a narrow question. `skill-fired.md` asks one binary thing, whether the right skill engaged. `criteria.md` checks named properties of the output against a written rubric rather than asking for an overall quality score, because a judge asked "is this good writing" returns an opinion, and a judge asked "does every number in the source appear in the output" returns a fact. Both rubrics are version-controlled next to the case, so a change to what counts as passing is a reviewable diff.

The skill leans the same way in use. It reports which patterns it found and why, and the decision to act stays with the writer. Knowing which of two drafts is the right one is the part that does not automate, and it is faster than editing from scratch only if you can make that call quickly.

## Install

From this repository, in Claude Code:

```
/plugin marketplace add sayandip1987/humanise-plugin
/plugin install humanise@humanise
```

Or clone it and add the folder as a local marketplace:

```
git clone https://github.com/sayandip1987/humanise-plugin.git humanise
```
Clone into a folder named `humanise` so `scripts/validate_skill.py` passes: it checks that the folder name matches the plugin name.
```
/plugin marketplace add ./humanise
/plugin install humanise@humanise
```

You can also drop a packaged `.plugin` file into Claude and accept it.

## Use

Claude picks the right skill up on its own from phrases like "make this sound human", "this reads like AI wrote it", "make it sound like me", "how do I pitch this to the director", or "they're going to push back, what do I say". Name one directly with the commands above.

`humanise` has three output modes: **pasted text** (the default, rewrite first, no preamble), **file mode** (name a file, prose changes only, short summary afterwards), and **embedded mode** (another task calls it for a commit message or a document section, only the final text comes back).

Ask for `light` or `heavy` to change how hard it edits. Standard is the default, and it is chosen from how many tells the text actually has.

For the boundaries, what it refuses to do, and how it handles pasted instructions, see the `Input boundary` section of `skills/humanise/SKILL.md` and `Boundaries` in `skills/meeting-talk/SKILL.md`.

## Why the skill is split across files

`SKILL.md` holds the workflow, the intensity rules, the gates and the routing. The 21-pattern catalogue, the channel register and the portability notes sit in `references/`, and the worked before-and-after passage sits in `examples/`. That split is a context decision, not a filing one.

A skill's own text competes for the same window as the draft it is rewriting. Loading the full pattern catalogue on every invocation would spend thousands of tokens describing tells that a given passage does not contain, and it would do it before the model has seen the passage. So `SKILL.md` stays small enough to always load, and the catalogue is read during step 1 of a rewrite, once there is a reason to read it.

The same logic sets the working unit. The skill acts on a passage rather than a whole document, because a pattern like repeated sentence openings or a forced triad is only visible against its neighbours, and because the weak-alone rule needs to know what else shares the passage. Too small a unit and the co-occurrence test cannot run; too large and the rewrite drifts.

## The package

`.claude-plugin/` holds plugin.json, the single source of truth for name, version and author, and marketplace.json, which makes this repo installable as a marketplace. `commands/` holds the four commands: `/humanise:humanise` to rewrite a draft, `/humanise:talk-track` for lines for a meeting, `/humanise:pushback` to handle an objection, and `/humanise:audit` to name the patterns without a rewrite. `skills/humanise/` holds its `SKILL.md` for workflow, intensity, gates and routing, its `references/` for the pattern catalogue, channel register and portability, its `examples/` for the full-passage before/after and the change-report format, and its `templates/` for the voice profile. `skills/meeting-talk/` holds its `SKILL.md` for the output contract and evidence discipline, `references/meeting-pack.md` for the pyramid, stakeholder shapes, pushback and time boxes, and `examples/` for a worked talk track.

Alongside them sit `hosts/openai.yaml` for optional UI metadata on OpenAI hosts, `scripts/validate_skill.py` for the structural validator, `evals/` with 11 cases, each with prompt and graders, and README.md, CHANGELOG.md and LICENSE. No `.mcp.json`, no `hooks/`, no `settings.json`, no `bin/`. Nothing here needs a connector, a hook, or a binary.

```bash
python3 scripts/validate_skill.py
```

Python 3.9 or later, nothing else. It checks the manifest, both skills' frontmatter and behaviour markers, that neither skill duplicates the other's content, relative links, the 21-pattern count, command wiring, that version and author are declared exactly once, that the skill's own prose contains no dashes, and the shape of every eval case.

Everything is plain Markdown with relative references. No tool call, shell, package, network connection, or vendor-specific variable, so the same folders run under Codex, ChatGPT, or any other Agent Skills host. Per-host notes in `skills/humanise/references/portability.md`.

## Licence

Proprietary; see [LICENSE](LICENSE). Author: Sayandip Bagchi. Version lives in `.claude-plugin/plugin.json`.
