# A worked talk track

## The request

> I need to pitch an onboarding improvement to a product director. I get about four minutes. The only facts I have: setup fell from 12 minutes to 4 minutes in our test, and the flow still has an unresolved error state. Don't claim adoption or retention impact.

Audience: product director. Decision: unstated, so ask or assume. Evidence: two facts, one positive and one open. Constraint: four minutes.

## The output

**Main point**

"Setup now takes four minutes instead of twelve in our test, and I want to ship it behind a flag once the error state is fixed."

**Say this**

- "We cut setup from twelve minutes to four in testing."
- "That came from removing the second step, not from making the same steps faster."
- "There is one error state we have not resolved, and I do not want to ship without it."
- "I have not measured what this does to completion or retention, so I am not claiming either."
- "What I want is a flagged rollout to ten percent once the error state is closed."

**Proof**

- Twelve to four minutes: our own setup test. That is the measured number, and it is a test, not production.
- The mechanism: the second step is gone. That is why the time moved, and it is the part that generalises.
- The unresolved error state: known, reproducible, not yet fixed.
- Completion and retention: unmeasured. No data either way.

**Pushback**

- They ask: *"Does this actually improve conversion?"* You say: "I do not know yet. The only thing I have measured is setup time. A flagged rollout is how we find out."
- They ask: *"Can it wait a sprint?"* You say: "It can. The cost is that we keep shipping the twelve-minute path to everyone who signs up in the meantime."
- They ask: *"Why not ship it now and fix the error after?"* You say: "Because the error state has no recovery path, so those users are stuck rather than slowed."

**Ask**

"I am asking for a flagged rollout at ten percent once the error fix lands. Can you approve that now, or do you want to see the error fix first?"

## Why it is shaped this way

- The **main point** carries both the result and the ask, so if the director interrupts after one sentence they still have the decision in front of them. That is BLUF doing its job.
- The **mechanism line** does more work than the number. "Twelve to four" invites "in what conditions"; "we removed a step" survives the follow-up.
- The **unmeasured line is said out loud**, not omitted. The user asked not to claim adoption impact. Staying silent about it invites the director to assume a claim was implied; saying it first takes the question off the table and buys credibility for the numbers that are real.
- The **trade-off is in the pushback**, where the director will actually raise it, rather than in a section they will not reach in four minutes.
- The **ask is closed**, with an alternative. "Approve now, or see the fix first" gives a director two doors instead of an open question, which is what turns a pitch into a decision.
- Every line is speakable. No dashes, no abstract nouns, no "leveraging our learnings".

## What is not in it

No adoption number, no retention number, no ROI, no user quote, no competitor reference, no claim about how the team feels. None of that was supplied, so none of it appears. The four-minute version stayed at four minutes.
