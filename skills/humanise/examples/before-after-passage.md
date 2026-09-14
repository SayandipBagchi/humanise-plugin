# A full passage, before and after

Sentence-level examples teach sentence-level patching, and patching is how a rewrite ends up with the same skeleton wearing new words. This example shows the whole move.

## Input

> ## Unlocking Seamless Onboarding: Key Highlights ✨
>
> Let's dive into what we shipped. The new onboarding flow is not just faster, it's a fundamental rethink of how users experience their first session.
>
> - **Speed:** Setup time dropped from 12 minutes to 4 minutes in testing.
> - **Clarity:** Users no longer encounter the ambiguous second step.
> - **Reliability:** The flow completes without the previous timeout.
>
> ---
>
> This represents a pivotal moment for the team, underscoring our commitment to user-centric design. While challenges remain, particularly around the unresolved error state, the future looks bright.
>
> That's the real win.

## Pattern inventory

Eleven tells, which puts this at **standard** intensity and close to heavy.

| Pattern | Where |
|---|---|
| 4. Staged run-up | "Let's dive into what we shipped." |
| 1. Not X but Y | "not just faster, it's a fundamental rethink" |
| 18. Decorative headings | title case, emoji, horizontal rule |
| 17. Bold as decoration | Speed / Clarity / Reliability labels |
| 6. Forced triad | three items shaped to match rather than to inform |
| 12. Inflated significance | "pivotal moment", "underscoring our commitment", "the future looks bright" |
| 11. Overused model words | pivotal, underscoring, seamless, unlocking |
| 13. Sales language | "user-centric design" |
| 12. Inflated significance, stock section | "While challenges remain..." |
| 2. Restating instead of continuing | "That's the real win." |
| 21. Writing about the previous version | "no longer encounter", "the previous timeout" |

## The wrong rewrite: patching

> ## Onboarding improvements
>
> Here is what we shipped. The new onboarding flow is faster and rethinks the first session.
>
> - **Speed:** Setup time dropped from 12 minutes to 4 minutes in testing.
> - **Clarity:** Users do not encounter the ambiguous second step.
> - **Reliability:** The flow completes without the timeout.
>
> This is an important moment for the team and shows our focus on users. The error state is still unresolved.

Every flagged phrase was replaced and the passage is still generated. The skeleton survived: staged opener, three parallel bold labels, a significance sentence, an outlook. "Here is what we shipped" traded one run-up for another, and "an important moment" traded one inflation for a quieter one. Facts also drifted: "rethinks the first session" is an unsupported claim carried over from the contrast that was supposedly removed.

## The rewrite

> ## Onboarding
>
> Setup now takes about 4 minutes, down from 12 in testing. The second step no longer asks the ambiguous question, and the flow completes without timing out.
>
> The error state is still unresolved. We have not tested whether the shorter setup changes completion rates.

What happened, and why:

- The passage was rebuilt around its point (setup is faster and two specific problems went away) instead of around its original shape.
- The three bold labels became one sentence, because the labels carried no information the sentence does not. The three facts all survived.
- The significance sentence, the outlook, and the closer were cut. The passage ends on the last concrete fact.
- "We have not tested whether..." was added, and it is the one addition allowed: it states an absence in the supplied material rather than a new fact. Nothing else new appears.
- Length went from 104 words to 62. That is outside the 85 to 115 percent band, so it gets a mention: the cut is entirely staging and decoration, and every fact survived. Say so in one line rather than expanding the prose to hit a number.
- No dash, no contrast, no triad, no closer, no decorative bold. The final gate passes.

## What did not change

The heading stayed (renamed to sentence case, not deleted). The numbers, the units, the word "testing", and the unresolved error state all carried through exactly. The writer's position, that this shipped and it is an improvement, is intact. The rewrite did not become sceptical, and it did not become more enthusiastic.
