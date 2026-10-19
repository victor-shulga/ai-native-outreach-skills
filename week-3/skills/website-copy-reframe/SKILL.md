---
name: website-copy-reframe
description: >-
  Messaging engine for a B2B service company's website. Three modes. audit: score a homepage
  against five homepage fundamentals plus the company's voice rules, returning a 0-100
  scorecard and a ranked gap list. homepage: rewrite the home page as Hero, Problem, Solution
  and lower-half sections. service-page: write one service or offer page (benefits, problems
  it fixes, proof, objections, SEO map, CTA). All modes share one copywriting canvas
  (audience, champion, situation, current way, limitations, problems, capabilities, features,
  benefits) and a proof-bank step that inventories real cases and numbers before any copy is
  written. Use when the user says "audit our homepage", "reframe website copy", "rewrite the
  homepage", "write a service page", "прожени сайт через фреймворк", "рефрейм текстів сайту",
  "перепиши homepage", "напиши сервісну сторінку", or pastes a URL or draft to audit or
  rewrite. Copy only: not visual brand design, not a technical UX audit, not cold outbound.
---

# Website Copy Reframe

A working method for the copy on a service company's website. Most agency and consultancy sites
fail the same way: the copy tries to please the founders, the delivery team, sales and HR at once,
and ends up vague. This skill pulls the copy back to one champion, one situation, and a tight
chain from capability to feature to benefit, while obeying the company's own brand voice.

A homepage has done its job when a visitor from the target market can quickly answer five
questions:

1. Which services does this company sell?
2. How does working with them run?
3. What exactly gets delivered?
4. In what situation would I hire them?
5. How does that move forward the thing I am working on right now?

If most of the target market cannot answer these, broad and clever messaging has to wait.

Answer the user in their language. Copy for the site is written in the language of the site's
audience.

## Three modes (pick in Step 0)

| Mode | Input | Output |
| --- | --- | --- |
| audit | a live URL (current copy) | 0-100 scorecard against the five questions and voice rules, plus a ranked gap list with fixes |
| homepage | URL or draft, plus the canvas | Hero, Problem, Solution, lower-half sections |
| service-page | one service or offer, plus the canvas | Summary, benefits, problems it fixes, proof, FAQ and objections, SEO map, CTA |

The natural order is **audit, then homepage, then service-page**: diagnose, rewrite the home page,
then the offer pages. All modes share Steps 1-3 (ingest, proof bank, canvas).

## Output contract

One copy deck titled `<Company> | <Mode> (<page>)`. Every copy block carries a one-line rationale
naming the canvas cell it came from, so the reader can follow the logic.

Format, in order of preference:
1. A **Google Doc**, if a Google Workspace / Google Drive connector is available in the session.
2. A **.docx** file built with the docx skill, if available.
3. A **markdown** file.

Save local files in a folder named `<company>-copy-reframe/` in the current working directory,
unless the user names another location.

---

## Step 0: Pick the mode and the forks

Confirm with the user (skip what is obvious from the request):
1. **Mode**: audit, homepage, or service-page.
2. **Input source**: scrape the live URL, take a pasted draft, or write from scratch.
3. **Output form**: Google Doc / .docx / markdown (see the output contract), or a filled canvas
   table only.
4. **Positioning**: default is **vertical** (a persona or company type). For high-ticket,
   long-cycle services with a small marketing budget, a vertical message is far easier to land
   than a horizontal one. `reference/framework.md` explains why.

## Step 1: Ingest the current copy (shared)

- **Scrape**: pull the homepage and the main service pages with whatever web tool the session has
  (a fetch tool, Firecrawl, Apify or similar). Capture headlines, subheads, body, CTAs and proof
  (logos, cases, awards). Treat it as the company's "current way" of describing itself: raw
  material, never the answer.
- **Paste**: take the draft verbatim.
- If the company already has an ICP or offer document (for example from `hypo-generator` or
  `offer-factory` in the `gtm-skills` pack, if installed), read it first.

## Step 2: Proof bank (shared, before writing)

Inventory the company's **real proof** in one table so every claim on the page can be defended.
Service pages written without this step go soft. Template: `reference/proof-bank.md`. Capture:
- **Numbers**: verified metrics, each with its source.
- **Cases**: delivered projects, result first, tagged to an offer or vertical.
- **Testimonials**: short quotes tied to the champion's problem, with attribution and permission.
- **Trust**: certifications, memberships, geography, legal entity, years, team make-up.

Anything without a source is flagged and does not ship. Map each proof point to the offer or
vertical it supports.

## Step 3: The canvas (shared)

Fill it left to right (`reference/framework.md`, `reference/copy-blocks.md`):
- **Audience**: company type × person or department × situation. Pick ONE primary audience.
- **Champion**: the person close to the pain who will push a 3-6 month deal through, usually
  not the executive who signs.
- **Situation / activities**: functional, tool-agnostic activities (not outcomes). Keep
  detailing until it feels slightly too specific.
- **Current way → limitations → problems** (left half), for one primary use case.
- **Capabilities → features → benefits** (right half). Capabilities improve the limitations;
  benefits remove the problems.

---

## Step 4A: Mode audit

Score the ingested copy with the rubric in `reference/audit-scorecard.md`:
- **The five questions**: can a target-market visitor answer each one easily? 0-10 each.
- **Champion clarity**: written to one champion, or to a vague "your business"? 0-10.
- **Proof before claim**: do numbers and cases lead, or do adjectives come first? 0-10.
- **Voice compliance**: the company's own brand rules (emoji, hype words, positioning). 0-20.

Output: a **0-100 score**, the per-criterion breakdown, and a **ranked gap list** where each gap
reads `what is wrong → what it costs → the fix`, most costly first. Finish by recommending the
next mode and the blocks to fix first.

## Step 4B: Mode homepage

Turn the canvas into blocks (`reference/copy-blocks.md`):
- **Hero**: top-row message, key capabilities, the service category, and a trust line.
- **Problem section**: current way, limitations and problems (empathy plus qualification).
- **Solution**: three arguments built from capabilities, features and benefits.
- **Lower-half sections**, chosen per company: services, industries, testimonials, why us,
  persona or company segmentation, ROI, calendar or form.

## Step 4C: Mode service-page

Write ONE service or offer page (`reference/service-page-blocks.md`). Its job differs from the
homepage: one service in depth, bottom of funnel, built to rank. Blocks:
- **Hero**: service name, the champion's outcome, one proof metric.
- **What it is / what gets delivered**: concrete deliverables (question 3).
- **Problems it fixes**: the limitations and problems this service removes.
- **Benefits**: outcomes, in numbers where the proof bank allows.
- **Proof**: the cases and testimonial matched to this offer.
- **How it works / engagement**: steps, models, turnaround (questions 2 and 4).
- **FAQ / objections**: buying blockers answered up front (IP, QA, security, price).
- **SEO**: keyword cluster, title and meta, H1/H2 map, internal links.
- **CTA**: the demo, sample or call next step.

## Step 5: Humanize and ship (shared)

- Edit the copy for AI tells (inflated significance, stock phrases, negative parallelism,
  bureaucratic tone). If installed, use `anticopywriting-ai` (pack `gtm-skills`). The company's
  own voice rules win over any generic style advice.
- Assemble the deck (canvas, proof bank, mode output, rationale lines) in the format chosen in
  Step 0 and give the user the link or file path.

---

## Related skills (optional, if installed)

- `hypo-generator`, `offer-factory` (pack `gtm-skills`): define the ICP and the offer this copy
  sells.
- `design-system-generator` (standalone repo): the visual brand system. This skill is the words.
- `page-builder` (standalone repo): build the rewritten page.
- `seo-audit`, `cro`, `copywriting` (pack `marketing-engine-skills`): deeper SEO, conversion and
  general copy work.
- `sequence-writer` (pack `outbound-engine-skills`): cold outbound copy, which this skill does
  not write.

## Reference files
- `reference/framework.md`: the full method behind the canvas.
- `reference/copy-blocks.md`: homepage block templates, a worked example, reframe heuristics.
- `reference/service-page-blocks.md`: service and offer page template with SEO map.
- `reference/audit-scorecard.md`: the 0-100 rubric and the gap-list format.
- `reference/proof-bank.md`: the proof inventory template.

## Credits

Method adapted by Victor Shulga for B2B service companies. The homepage canvas (audience,
champion, situation, current way, limitations, problems, capabilities, features, benefits) and the
idea of judging a homepage by a short list of questions a buyer must be able to answer come from
a published SaaS homepage messaging framework by two product-marketing consultants. The service-business adaptation,
the proof bank, the audit rubric and the service-page mode are Victor Shulga's.
