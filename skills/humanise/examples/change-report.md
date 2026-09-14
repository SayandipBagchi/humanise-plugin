# The change report

Produce this only when the user asks for a comparison, an audit, a "what changed" report, or a diff. The default output is the rewrite alone.

Keep it short enough to read faster than the text itself. The point is to let the writer accept or reject edits, not to document the process.

## Format

```
[the rewrite]

---

Changed
- <what moved>. <which pattern, by name>
- ...

Kept deliberately
- <what looked like a tell and is not>. <why>

Facts
- All preserved. / <what was dropped, and why a pattern required it>

Length: <in> → <out> words (<percent>)
```

`Changed` is grouped by what moved, not by sentence. Four to eight lines for a normal passage. If the list runs past ten, the edit was heavier than the user asked for.

`Kept deliberately` is the more useful half. It tells the writer you saw the thing and left it, which is what stops them re-adding it next draft.

`Facts` is a one-liner unless something was dropped. Anything dropped is named, with the pattern that required it.

## Example

> Setup now takes about 4 minutes, down from 12 in testing. The second step no longer asks the ambiguous question, and the flow completes without timing out.
>
> The error state is still unresolved. We have not tested whether the shorter setup changes completion rates.
>
> ---
>
> **Changed**
> - Cut the opener "Let's dive into what we shipped". Staged run-up (4).
> - Removed "not just faster, it's a fundamental rethink" and stated the speed change directly. Not X but Y (1).
> - Collapsed the three bold-labelled bullets into one sentence; the labels carried no information. Bold as decoration (17), forced triad (6).
> - Cut "pivotal moment", "underscoring our commitment", and "the future looks bright". Inflated significance (12).
> - Cut the closer "That's the real win". Restating instead of continuing (2).
> - Heading to sentence case, emoji and horizontal rule removed. Decorative headings (18).
>
> **Kept deliberately**
> - The heading itself. Removing it would break the document's navigation.
> - "in testing". It bounds the claim, and dropping it would make the number sound like production data.
>
> **Facts**
> - All preserved. Added one statement of absence: completion-rate effect is untested. Nothing else added.
>
> Length: 104 → 62 words (60%). The cut is staging and decoration only.

## For long documents

Report at section granularity. One line per section saying what class of change it took, then a single document-level list for tells that only appear at scale: a repeated closer, every section opening the same way, a triad of sections.
