---
name: competitor-finder
description: >-
  Builds an evidence-backed competitor map for a B2B service company (agency, dev or IT
  outsourcing, AEC/BIM outsourcing, consultancy). Finds who the buyer really compares you
  with: direct service firms, marketplace freelancers, adjacent providers, an in-house hire,
  and doing nothing. Per player: positioning claim in their words, proof, price signal, and
  a weakness backed by reviews (Clutch, GoodFirms, G2, Upwork), each with a source URL,
  unknowns marked. Ends with differentiation angles for outbound copy and "we already work
  with X" objections.
  Use for "who are our competitors", "competitor map", "battlecard", "how do we beat X",
  "alternatives to us", "конкуренти", "хто наші конкуренти", "карта конкурентів",
  "баттлкард", "чим ми відрізняємось". Feeds gtm-competitor-gap and gtm-positioning.
  NOT for gap scoring and whitespace (gtm-competitor-gap), NOT for the positioning
  statement (gtm-positioning), NOT for SaaS feature comparisons.
---

# Competitor Finder

A service buyer rarely compares you with one rival agency. They compare you with the vendor they already have, with a freelancer they found on a marketplace, with hiring one more person, and with leaving the problem alone for another quarter. This skill maps all of those options with evidence, so positioning and outbound copy are built on what buyers actually see.

Answer in the user's language. Every factual line carries a source URL or the label `unknown`.

## Where it sits

- **gtm-competitor-gap** calls this skill to collect the players, prices and reviews, then does the gap scoring and whitespace itself.
- **gtm-positioning** reads the artifact this skill produced (through 05). If a map from the last 90 days exists, reuse it and only refresh what changed.

## Inputs (ask once, in one message)

1. Company website, plus one line on the service sold and to whom (segment, geo, deal type: project, retainer, white-label, staff augmentation).
2. Competitors the team already knows, and deals lost in the last 12 months with the reason given (CRM lost-reason field if it exists).
3. Scope: the full map, or a focused battlecard against one or two named rivals.

If the user cannot answer 2, continue and say the map is built from outside-in sources only.

## Step 1. Define the job the buyer hires for

Write one sentence: "When [trigger], a [buyer role] at a [company type] needs [outcome], and today they get it from ___." The blank is the competitor set. Example for a BIM outsourcing firm: "When a UK MEP contractor wins more projects than the in-house modelling team can carry, the BIM manager needs coordinated models on time, and today they get it from ___."

## Step 2. Fill five lanes

| Lane | What to look for in service markets |
|---|---|
| Direct firms | Same service, same buyer, similar delivery model (nearshore or offshore team, white-label) |
| Marketplace talent | Upwork or Toptal agencies and freelancers selling the same deliverable by the hour |
| Adjacent providers | A firm that sells a neighbouring service and adds yours as an upsell (a design agency doing dev, an engineering consultancy doing BIM) |
| In-house | Hiring a person or a team; check the buyer segment's job posts for the same role |
| Do nothing | Delay, overtime for the current team, cutting scope, turning down projects |

Aim for 5 to 8 direct firms and at least one named example in each other lane. A lane with no evidence stays in the map with `no evidence found` and the queries you ran.

**Where to search**

- Clutch, GoodFirms, DesignRush category pages filtered by service, geo and min project size
- Upwork agency profiles for the service keyword (rates and job success are public)
- Google: `[service] outsourcing [geo]`, `[service] company for [vertical]`, `[rival] vs`, `[rival] alternative`
- LinkedIn company pages (headcount trend, open roles), conference sponsor and exhibitor lists for the vertical
- The rival's own site: case studies, pricing or engagement pages, "how we work" pages

## Step 3. Build one evidence card per player

For each direct firm and the strongest example in other lanes:

```
### [Player] · lane: [direct / marketplace / adjacent / in-house / do nothing]
Site: [URL]
Claim (their words): "[headline or tagline, quoted]" [URL]
Who they serve: [segment, geo, company size] [URL or unknown]
Proof they show: [named case types, certifications, standards, logos count] [URL]
Price signal: [Clutch min project / hourly band, Upwork rate, published package] [URL or unknown]
Team and geo: [headcount range, delivery locations] [URL]
Weakness from reviews: [pattern] [review URL 1] [review URL 2]
They win when: [buyer situation where they are the right choice]
```

Rules for this step:
- Quote the claim as written. Paraphrase only in a separate note.
- A weakness needs two independent reviews, or one review plus another public signal (a hiring spike for the same role, a complaint thread). One review alone goes in as `single review, weak`.
- Price signals are ranges with a source. If nothing is published, write `unknown`; do not estimate.

## Step 4. Read the reviews for failure patterns

Pull the 3 to 4 star and the negative reviews first, they carry the useful detail. Tag each complaint with one of these service failure patterns (add your own if the data shows another):

- Seniority swap (senior people sold, juniors delivered)
- Communication lag, time-zone friction
- Missed deadlines, slow ramp-up
- Scope creep and change-order disputes
- Quality rework (standards not followed, for AEC: LOD, naming conventions, clash detection gaps)
- Team turnover mid-project
- Account management disappears after signing

Count how many reviews per rival fall into each pattern. The pattern that repeats across several rivals is a market-wide weakness and the strongest base for an angle.

## Step 5. Turn gaps into differentiation angles

An angle is valid only when three things line up: a weakness the buyer has felt (from Step 4), proof that you behave differently (a case, a process, a guarantee you can show), and a sentence a buyer would repeat. For each angle write:

- **Gap:** the failure pattern and how often it showed up
- **Our proof:** the asset that backs it, or `proof missing` (then it is a hypothesis, not an angle)
- **Outbound line:** one sentence, buyer language, no superlatives
- **When they say "we already work with [rival]":** a two-line reply that respects the incumbent and asks one question about the known gap

Also write where you lose. If a rival is cheaper, larger or has a reference you lack, say so, and note the deal situations where you should walk away early.

## Output template

```
# Competitor map: [company] · [date]
Scope: [full map / battlecard vs X] · Sources checked: [N] · Lost-deal data: [yes / no]

## 1. The buyer's job
[one sentence from Step 1]

## 2. Map by lane
| Player | Lane | Claim (quoted) | Price signal | Main weakness | Source |
|---|---|---|---|---|---|

## 3. Evidence cards
[one card per player, Step 3 format]

## 4. Failure patterns across the market
| Pattern | Rivals affected | Review count | Example URL |

## 5. Differentiation angles
[angle blocks from Step 5]

## 6. Where we lose
[honest list + walk-away situations]

## 7. Unknowns and next checks
[what could not be verified and how to verify it: discovery question, lost-deal call, mystery inquiry]
```

## Quality gate (all must pass before handing over)

- [ ] All five lanes present, empty lanes explained
- [ ] Every claim, price and weakness has a URL or `unknown`
- [ ] No weakness rests on one review without the `weak` label
- [ ] Each angle has proof, or is labelled a hypothesis
- [ ] "Where we lose" is filled in
- [ ] No invented numbers: market shares, win rates and prices only with a source

## Hand-offs

- Gap scoring and whitespace: `gtm-competitor-gap` (this pack)
- Positioning statement and enemy angle: `gtm-positioning` (this pack)
- Objection replies in live threads: if installed, `reply-objection-handler` (pack `outbound-engine-skills`)
- Cold copy built on the angles: if installed, `sequence-writer` (pack `outbound-engine-skills`) or `angle-finder` (pack `outbound-engine-skills`)
- Deeper profile of one rival: if installed, `competitor-profiling` (pack `marketing-engine-skills`)

## Credits

Idea adapted from a public outbound-skills collection; rewritten for B2B service companies.
