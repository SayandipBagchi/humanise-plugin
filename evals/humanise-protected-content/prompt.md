Humanise the prose in this file content only. Leave everything else exactly as it is, then tell me what changed.

---
status: draft
owner: platform
---

## Overview

Let's dive into the retry behaviour. It is a pivotal step forward for reliability.

The request failed with `RCP-422`. We retry twice, then surface the error. See [the runbook](docs/runbook.md).

```yaml
retry_count: 2
timeout_ms: 3000
```

I do not know which team owns the parser.
