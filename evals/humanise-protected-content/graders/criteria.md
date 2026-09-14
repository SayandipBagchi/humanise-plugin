# Criteria: humanise-protected-content

Score each item independently. An item that cannot be checked from the output is a fail, not a pass.

- [ ] YAML frontmatter is byte-identical, including status: draft and owner: platform
- [ ] The code block is byte-identical, including retry_count: 2 and timeout_ms: 3000
- [ ] Inline code `RCP-422` is preserved exactly
- [ ] The link target docs/runbook.md is preserved exactly
- [ ] The heading '## Overview' is preserved, or only its case is adjusted, and heading level is unchanged
- [ ] Prose sentences are the only thing rewritten
- [ ] The writer's stated uncertainty about parser ownership survives; no owner is invented
- [ ] 'Let's dive into' and 'pivotal step forward' are both gone
- [ ] A short concrete summary of what changed follows the text, with no preamble before it
