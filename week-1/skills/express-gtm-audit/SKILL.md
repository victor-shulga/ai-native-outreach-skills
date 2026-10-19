---
name: express-gtm-audit
description: Express audit of a B2B service company's GTM system from public data only (site, cases, review platforms, LinkedIn, search, AI answers, DNS). Scores 6 blocks of the GTM system (strategy, team, lead generation, sales, account management, processes) on 24 criteria, scale 1-5, «?» for what is not visible from outside; block score = mean of scored criteria. Output is one single-file HTML page in a fixed order - header with overall score and thesis, dashboard of 6 blocks with 3 headline findings, then block by block, each ending with a verdict, a «what to do» box and 2-3 questions for the call. Use when the user says express audit, експрес-аудит, оціни нашу агенцію ззовні, аудит перед дзвінком, audit this agency from the outside, score our GTM in 6 blocks, or when a course/homework asks for the 6-block self-audit. Not the weighted 23-criteria maturity audit (that is gtm-audit) and not a website UX audit.
argument-hint: "[company URL] (+ optional: competitor URLs, target market, anything already known)"
---

# Express GTM audit: 6 blocks, scale 1–5, public data only

One document a buyer or a founder can read in ten minutes. Built from what anyone can see from
outside: the website, the cases, review platforms, LinkedIn, search results, AI-assistant answers,
DNS records. Whatever cannot be seen becomes a question, never a guess.

Two uses:
- **Before a first call with a prospect**: the audit is the call plan.
- **Self-audit by an agency founder** (course homework): the founder scores their own company the
  way a stranger would, then picks the three things to close first.

Language of the document = language of the user. Company, tool and competitor names stay Latin.

## Hard rules

- **No evidence, no score.** A criterion that cannot be seen from outside gets `?`, is excluded
  from the block mean, and turns into a call question. Never infer a score from "they probably
  have it".
- **Torn between two scores: take the lower one.**
- **Results first.** The page opens with the overall score and a 4–5 line thesis, then the
  dashboard. Methodology never comes first.
- **Every number has a source line** (page URL, review count and date, DNS record, post count
  and period). Anything derived is tagged as a conclusion.
- **Confidentiality.** Never mention the author's other clients or their cases. Competitors of the
  audited company may be named: they are public.
- **One next step** at the end (a call link or the homework hand-in), never two CTAs.
- Ukrainian text: no em dashes (use `?` as the "not visible" marker, en dash only between
  numbers), decimal comma (2,7), plain words, block names in the user's language.

## Scale (same for every criterion)

| Score | Meaning |
|---|---|
| 1 | absent, or present but brings no buyers |
| 2 | weak |
| 3 | exists, but it is not a system |
| 4 | strong |
| 5 | best in class, visibly better than the neighbours |
| `?` | not visible from outside; not scored, becomes a call question |

Block score = mean of its scored criteria, one decimal. Overall = mean of all scored criteria.
Card colour: below 2,5 red · 2,5–3,4 amber · 3,5 and above green. Show the formula next to any
composite number and say how many criteria were scored ("середнє по 20 критеріях").

## The 6 blocks and 24 criteria

Full checklists, tables and sources are in `references/rubric.md`. Read it before scoring.

| # | Block | Criteria |
|---|---|---|
| 01 | GTM strategy (foundation) | ICP (3 components) · positioning · offer · delivery process (8-point checklist) · lead magnets · case depth (5 cases × 7 features) |
| 02 | Team (foundation) | GTM roles · owners of announced markets · `?` sales hiring and development |
| 03 | Lead generation (pipeline) | SEO · AI visibility · LinkedIn and content · events · outreach infrastructure · inbound capture |
| 04 | Sales (pipeline) | path to the first meeting · buyer materials · `?` first call and proposal |
| 05 | Account management (pipeline) | retention · reviews and referrals · `?` account expansion |
| 06 | Processes (foundation) | tracking and analytics · forms-to-CRM link · `?` metrics and rhythms |

Criteria marked `?` are almost never visible from outside. Keep them in the table, score them
only when the user supplies inside evidence (answers, exports, call notes).

## Procedure

1. **Collect** (60–90 minutes of agent time for a prospect; 2–3 hours for a founder doing it by
   hand). Site crawl: menu, service pages, cases, pricing, how-we-work, about, blog. Review
   platforms: count, dates, client sizes and industries. LinkedIn: company page and the two most
   visible people, 12 months of posts. Search: brand and category queries in the main market.
   AI assistants: 2–4 topics × 3–4 unbranded prompts, note who gets named instead. DNS: MX,
   SPF, DKIM selectors, DMARC policy, separate sending domains.
2. **Score** every criterion with 2–4 evidence bullets and a one-line verdict, using the tables
   in `references/rubric.md` (ICP, delivery process, case anatomy are mandatory tables).
3. **Write the page** by copying `references/example-audit.html` (a finished, anonymised audit of a
   software company, September 2026): keep its HTML, CSS and section order, replace every piece of
   data with the audited company's. Do not redesign and do not start from a blank page. Then run
   the self-check list.
4. **Deliver** as a single HTML file built on the page order below, with the user's design
   tokens or neutral ones; a `<meta name="viewport">` tag and tables that scroll inside their
   block on phones.

## Example (read before writing)

`references/example-audit.html` is the etalon: a complete audit of a real software company with the
company name removed (its neighbours stay named, they are public). Overall 2,7 / 5 across 20 scored
criteria, 4 marked `?`. It shows what "enough evidence" looks like: the ICP table with three
components, the 8-row delivery-process table, the 5-case anatomy table, a positioning map against five
neighbours, an H2 per block that carries the conclusion with a number, and a call-questions box under
every block. The same page is live at https://vs-express-audit-example.shoulga-v.workers.dev. A blank
version for a founder filling the audit by hand, with block means computed on the fly, is at
https://vs-express-audit-template.shoulga-v.workers.dev; this skill produces the filled page, not the
blank one.

## Page order (fixed)

1. Header: company, date, "prepared from public data only", overall score, 4–5 line thesis that
   names the weakest block and the first thing to fix.
2. Dashboard: 6 block cards with scores and criteria pills, plus 3 headline findings with
   numbers.
3. Bridge: why strategy decides the rest (6 block scores as bars, strategy highlighted).
4. Blocks 01–06. Each block: H2 = its conclusion with a number, criterion rows (score · evidence
   · verdict), the mandatory tables where they belong, a "Що зробити" box, a "Не видно ззовні ·
   питання на дзвінок" box with 2–3 questions.
5. Next step: one link or one hand-in instruction.
6. Sources: every URL and record used.

## Self-check before delivering

- Every score has evidence; every `?` has a question.
- No block H2 is a bare block name; each carries its conclusion.
- Headline numbers appear at most twice (thesis and its block).
- Reviews are counted as reviews, not as clients.
- Every "since", "years", "average" has a dated source or is removed.
- No client names of the author, no em dashes in Ukrainian, decimal comma.
- The page has `<meta name="viewport">` and does not scroll sideways on a phone.
