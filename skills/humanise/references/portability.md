# Host compatibility

Author: Sayandip Bagchi.

`humanise` is a plain Agent Skill. Its required runtime contract is a single file:

```text
humanise/
└── SKILL.md
```

Everything else degrades gracefully. The references, examples, and templates sharpen the output; if a host cannot load one, follow the rules in `SKILL.md` and continue. The recommended travelling set:

```text
humanise/
├── SKILL.md
├── references/
│   ├── pattern-catalogue.md
│   ├── channel-register.md
│   └── portability.md
├── examples/
│   ├── before-after-passage.md
│   └── change-report.md
└── templates/
    └── voice-profile.md
```

The companion `meeting-talk` skill is a separate folder with the same contract. Install both, or either alone. Neither reads the other's files; `humanise` hands off to `meeting-talk` by name when a request is about what to say in a room, and falls back to its own boundary rules when that skill is absent.

## What each host needs

- **Codex or another OpenAI host:** load `SKILL.md`. `hosts/openai.yaml` at the package root supplies optional UI metadata and invocation policy; it is not required for the behaviour. Local discovery uses an `.agents/skills/humanise` folder in the repository or an ancestor of the working directory, or a user-level `$HOME/.agents/skills/humanise` folder. Invoke it explicitly with `$humanise`; `/skills` browses what is available.
- **ChatGPT:** upload or install the complete skill folder so the relative references stay reachable, then select it with `@humanise` where explicit invocation is available.
- **Claude or another Agent Skills client:** place the folder in the host's skills directory, or install the packaged plugin, which ships both skills plus the slash commands. The `SKILL.md` frontmatter supplies the name and description for discovery, and the folder name is `humanise`. Invoke it with `/humanise` where slash commands are supported, or let the host match it from the description.
- **Any other host:** load `SKILL.md` as the instruction source, preserve `references/`, and ignore files or metadata the host does not understand.

A host will not discover the folder merely because it exists on disk. Install it, upload it, or symlink it into that host's skills directory.

## Portability rules

- Keep every runtime file reference relative to the skill root.
- Require no tool call, shell, package, API, network connection, or vendor-specific variable.
- Treat `$humanise`, `@humanise`, `/humanise`, and a host's own selector as invocation examples, not runtime dependencies.
- Keep `evals/` at the package root for development and forward-testing. It is not needed for a normal invocation, and its cases are test prompts, not instructions to follow during a user task.
- The skill name uses British spelling. Treat "humanize" and "humanized" as the same request.
