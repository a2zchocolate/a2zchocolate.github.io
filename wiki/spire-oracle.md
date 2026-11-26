---
title: Spire Oracle
category: Projects
summary: Ask anything, answered with a Slay the Spire 2 card, relic, potion or event.
infobox_title: Spire Oracle（问问尖塔）
infobox:
  - [Type, Bilingual fortune-telling game]
  - [Languages, English and Simplified Chinese]
  - [Launched, November 2026]
  - [Website, "[sts2tarot.uk](https://sts2tarot.uk)"]
  - [Hosting, Cloudflare Workers (free plan)]
  - [AI, Cloudflare Workers AI; DeepSeek for overflow]
  - [Item data, 1,155 official names via Spire Codex]
---
**Spire Oracle** (Chinese: 问问尖塔) is a bilingual fortune-telling game that answers any question with a single item from the roguelike deck-builder *[Slay the Spire 2](https://store.steampowered.com/app/2868840/)*: a card, relic, potion or event. The item is chosen so that its *name*, read literally, works as the reply, a pun, a punchline or a deadpan verdict. A one- or two-sentence "reading" then connects the name to the question and gives a piece of real advice.

Asked *"他还爱我吗"* ("Does he still love me?"), for example, it once answered **相信着你** (*Believe in You*), with the reading that the question is less about whether he believes in you than whether you believe in yourself.

## Origin
The idea came from a Xiaohongshu post in which a Slay the Spire player answered commenters' questions by hand, each time with the name of a card. The replies worked because they were puns: an exam tomorrow got **末日降临** (*End of Days*); "dad or mum?" got **双持** (*Dual Wield*). Spire Oracle tries to do the same thing automatically, for any question.

## How it works
Each question is answered by the first source that can:

1. **Approved library**: hand-reviewed answers for common questions.
2. **Answer cache**: a question asked before, in the same language, gets the same reading back.
3. **AI pick**: a language model receives the question and the full item list, first shortlists five candidates of different types, then picks the one whose name lands best and writes the reading.

The AI step runs on Cloudflare's free daily allowance; once that is used up, it switches to DeepSeek on a small prepaid balance, so the running cost has a hard ceiling.

## Development
- **Version 1** picked an item by hashing the question, free, instant and arbitrary. Testers found the answers meaningless.
- **Version 2** let a language model choose, using the Xiaohongshu replies as examples. This produced the first answers that felt like the original post.
- **Official names.** Early Chinese names were borrowed from the first game's translation; they were replaced with the official *Slay the Spire 2* names from [Spire Codex](https://spire-codex.com), which matter because the puns depend on exact wording.
- **Variety.** Friends testing it on Discord got the same answer (满屋芝士, *Room Full of Cheese*) again and again. Shuffling the item list, requiring a five-item shortlist and avoiding recent answers fixed most of the repetition.
- **Cost.** The free AI allowance ran out on the first evening of real use. A more compact item list, an answer cache and a prepaid fallback brought the cost per question to a fraction of a cent.

## See also
- [Splatoon Weapon Guesser](/wiki/splatoon-weapon-guesser/), an earlier fan game
- [Spire Codex](https://spire-codex.com), the community database the item names come from

<small>Fan project, not affiliated with Mega Crit. Slay the Spire and all item names belong to Mega Crit.</small>
