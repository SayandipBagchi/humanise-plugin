# Register by channel

Read this when the destination of the text is named or obvious. Skip it otherwise; a generic register is better than the wrong specific one.

"Human" pulls in a different direction in each channel. A Slack message that reads like a PRD is as wrong as a PRD that reads like a Slack message. What never changes: the facts, the protected content, and the writer's position.

## Slack, Teams, chat

Short sentences. Contractions. One idea per message. Lead with the ask or the answer; context follows if the reader needs it. Threads carry the detail.

Drop: headings, bold labels on every line, bullet lists under four items, sign-offs, "Hi team" when the channel already names the audience.

Keep: @-mentions, links, code formatting, emoji the writer actually uses.

## Email

A subject line that states the ask or the outcome. First sentence gives the point. Paragraphs of two or three sentences. One clear action at the end with an owner and a date if there is one.

Drop: throat-clearing openers ("Hope this finds you well", "I wanted to reach out"), nested bullet hierarchies, bold labels.

Keep: the greeting and sign-off the writer normally uses. These predate chat assistants and are not tells.

## PRD, spec, design doc

Neutral and plain. Present tense for how the system behaves, and precise verbs. Requirements stay unambiguous, so a hedge is removed or made explicit, never softened into ambiguity.

Drop: motivational framing, significance claims, "this unlocks", benefit language that belongs in a pitch.

Keep: numbered requirements and their numbering, acceptance criteria wording, defined terms used consistently, explicit non-goals, open questions marked as open.

## Jira, ticket, bug report

Title states the observable problem or the change. Body separates what happens, what should happen, and how to reproduce. No narrative.

Drop: adjectives about severity that a field already carries, apology, speculation about cause presented as fact.

Keep: exact error strings, IDs, environments, versions, steps in order, links to logs.

## Confluence, wiki, runbook

Written for someone arriving cold in six months. Second person for instructions. Each step does one thing and says how you know it worked.

Drop: "as discussed", references to a meeting the reader did not attend, status that will be stale next week unless the page is explicitly a status page.

Keep: heading structure and anchors, table structure, the order of steps, warnings and prerequisites.

## Release note, changelog

Reader-facing outcome first, mechanism second, and only if it affects them. One entry per change. Past tense for what shipped.

Drop: internal ticket language, team credit unless the writer wants it, "we're excited to", significance claims.

Keep: version numbers, dates, breaking-change flags, migration instructions verbatim.

## Commit message, pull request

Subject line in the imperative, under about seventy characters, saying what the change does. Body says why, and what a reviewer should look at. No marketing.

Drop: "this commit", "various fixes", significance claims, offers to continue.

Keep: issue references, breaking-change markers, co-author trailers, exact identifiers.

## Executive update

Answer first, in one sentence. Then what changed, what it means, what is still unknown, and what you need. Bounded claims: an unmeasured outcome is stated as unmeasured.

Drop: process narrative, activity lists that stand in for outcomes, confidence used to cover a missing basis.

Keep: numbers with their denominators and dates, named risks, named owners, the ask.

When the request is for lines to *say* in a meeting rather than text to read, that is the **meeting-talk** skill, not this one.
