---
name: homepage-rewrite
description: >-
  Rewrites the homepage of a B2B service company (agency, outsourcing, consulting) on two tracks.
  Clarity: a visitor from the target market understands what is sold, to whom and with what
  result within five seconds of the first screen. Trust: they believe it, because every promise
  has a named case with a number, real logos and attributed testimonials, no "coming soon"
  placeholders, and proof in the same block as the claim. Builds a proof bank before writing and
  never invents a case, number, quote or logo. Output: a diagnosis (clarity 0-50, trust 0-12, the
  three costliest gaps), new copy per block, a remove list, a pre-ship checklist and open
  questions. Use when the user says "rewrite the homepage",
  "homepage rewrite", "fix our homepage", "why doesn't our homepage convert", "перепиши головну",
  "рерайт хоумпейджа", "перепиши хоумпейдж", or pastes a site URL and asks for a new homepage.
  NOT a technical audit (website-audit), NOT service or industry pages (page-builder), NOT a
  visual design system.
---

# homepage-rewrite

A homepage has two jobs and most service-company homepages do one of them. Some are clear and
read like a pitch nobody can verify. Others are a portfolio of logos with no offer on top. This
skill runs both tracks over the same page and returns copy you can paste into the site.

- **Clarity track.** A visitor from the target market can answer five questions quickly: which
  services, how working together runs, what exactly gets delivered, in what situation they
  would hire you, and how it moves forward the thing they are working on right now.
- **Trust track.** Each promise carries proof the visitor can check, placed next to it.

Answer the user in their language. Write the site copy in the language of the site's audience.

## Inputs

- **URL** of the current homepage, or a pasted draft. Ask if neither is given.
- **Target market** if the company has one written down (ICP or offer document). Read it first.
- **Brand voice rules** if they exist. They win over any generic style advice here.

## Step 1. Ingest the current page

Pull the homepage text with whatever web tool the session has (a fetch tool, Firecrawl or
similar). Capture every headline, subhead, CTA, stat, logo, testimonial and link. Follow the
links behind cases and testimonials: proof that sits on an inner page counts as proof the
homepage could use. Treat the current copy as raw material for the rewrite.

## Step 2. Proof bank (before writing anything)

Fill `reference/proof-bank.md`: numbers with their source, named cases (who, result as a number,
timeframe), testimonials with name, role and company, independent review links (Clutch, G2,
LinkedIn recommendations), certifications, years, geography. Mark every item verified or not.
Unverified items do not go into the new copy; they go into the questions list.

## Step 3. Canvas

Fill the canvas table in `reference/copy-blocks.md` (the reasoning behind each cell is in
`reference/framework.md`) for ONE primary audience: audience, champion (the person close to the pain who pushes the deal), situation,
current way, limitations, problems, then capabilities, features, benefits. Capabilities improve
the limitations; benefits remove the problems. Default to a vertical position.

## Step 4. Diagnosis

Two tables.

**Clarity, 0-50.** Score the five questions 0-10 each with section A of
`reference/audit-scorecard.md`. Then run the 5-second test: read only the first screen and write
down what is sold, to whom, and the result. Any blank means the hero fails.

**Trust, 0-12.** Score rules T1-T6 from `reference/trust-track.md`, 0-2 each, with the evidence
from the page and the fix.

Close with the **three costliest gaps** across both tracks, each as
`what is wrong → what it costs → the fix`.

## Step 5. New copy per block

Templates in `reference/copy-blocks.md`. Every block gets a one-line rationale naming the canvas
cell (clarity) and the proof-bank row (trust) it uses.

- **Hero**: the hero template in `reference/copy-blocks.md`, ending with a trust line (rule T4).
- **Logos**: paying clients only, with permission.
- **Problem**: current way, limitations, problems. Keep what already works.
- **Solution**: three arguments, each with its own matching case or number from the proof bank.
- **Lower-half sections**, chosen per company: cases, testimonials, services, industries,
  why us, pricing, FAQ, calendar or form. A section with no real content is cut.

If the current page already passes a block, say "keep" and move on. Do not rewrite for the sake
of it.

## Step 6. Remove list, checklist, questions

- **Remove list**: every placeholder, unverified logo, anonymous quote, number without a source
  and link to an empty page.
- **Pre-ship checklist**, with a "now" and "after the rewrite" column:
  - [ ] First screen alone answers what, for whom and what result
  - [ ] H1 names a capability and an audience
  - [ ] Every case has a name (or a specific NDA descriptor), a number and a timeframe
  - [ ] Every logo is a paying client; every quote has name, role and company
  - [ ] At least one independent review link, if one exists
  - [ ] Zero "coming soon", empty cards, `0+` counters, links to empty pages
  - [ ] Hero and each Solution argument carry proof in the same block
  - [ ] Every claim links to a page where it can be checked; all links clicked
  - [ ] Nothing in the copy came from outside the proof bank
  - [ ] Copy passed an anti-AI-tell edit and the company's voice rules
- **Questions for the company**: what only they can confirm (permission for a logo, the source
  of a number, a missing timeframe).

## Step 7. Humanise and hand over

Edit the copy for AI tells: negative parallelism ("not X but Y"), rule-of-three punch lines,
em-dash cascades, hype words. Use `anticopywriting-ai` if installed. Then save one markdown file
`<company>-homepage-rewrite-<date>.md` in the current folder with these sections in order: proof
bank, canvas, diagnosis, new copy, remove list, checklist, questions. The proof bank and canvas
sections are what `page-builder` reuses for inner pages. Give the user the scores, the three gaps, the new hero and the path.
Do not publish anything to the live site yourself.

## Rules

- Never invent proof. If the bank is thin, the copy says less and the questions list grows.
- A number on the page without a source is a gap, even if it is probably true.
- The company's brand voice rules outrank this skill's style rules.
- Score the current page honestly. A homepage that already works gets "keep" on most blocks.

## Related skills (optional, if installed)

- `website-audit`: technical and mobile audit of the same site. Run it after the rewrite ships.
- `page-builder`: service, industry and case pages built from the same canvas and proof bank.
- `website-copy-reframe` (pack `marketing-engine-skills`): messaging audit and service pages.
- `website` (pack `marketing-engine-skills`): one flow from a baseline audit through this
  skill and page-builder to a second audit.

## Reference files

- `reference/framework.md`: the method behind the canvas
- `reference/copy-blocks.md`: block templates and reframe heuristics
- `reference/proof-bank.md`: the proof inventory template
- `reference/audit-scorecard.md`: clarity scoring (section A) and the gap format
- `reference/trust-track.md`: trust rules T1-T6, the diagnosis table, a neutral worked example

## Credits

Method by Victor Shulga (victorshulga.com) for B2B service companies. The homepage canvas and the
idea of judging a homepage by the questions a buyer must be able to answer come from a published
SaaS homepage messaging framework by two product-marketing consultants. The trust track, the proof
bank and the service-business adaptation are Victor Shulga's.
