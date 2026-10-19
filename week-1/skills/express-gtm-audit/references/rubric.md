# Express GTM audit: rubric, tables and sources

Scale per criterion: 1 absent / brings no buyers · 2 weak · 3 exists, not a system · 4 strong ·
5 best in class · `?` not visible from outside (not scored, becomes a call question).
Block score = mean of scored criteria (1 decimal). Overall = mean of all scored criteria.

## 01 · GTM strategy (foundation)

| Criterion | What to check | Where |
|---|---|---|
| ICP | three components, each 1–5, ICP = their mean (table below) | menu, industry pages, "who it's for" on service pages, cases, review platforms |
| Positioning | H1 and claim vs 4–6 peers: do the neighbours use the same words; what AI assistants say about the brand | homepages, review platforms, branded AI answers |
| Offer | entry products, duration, price, how findable; minimum project | service pages, pricing, review platforms |
| Delivery process | how the buyer's project runs phase by phase and what they hold after each phase (8-point checklist below) | how-we-work, approach, service pages, FAQ, pricing |
| Lead magnets | what is useful before the first call; for which segment; gated or not; any instant-result tool (calculator, self-assessment) | site crawl, blog, LinkedIn |
| Case depth | depth, not count (anatomy table below) | cases |

**ICP = 3 components** (mandatory table: what the site says · what the evidence shows · score):

1. **Target markets**: countries or regions the company sells to. Stated on the site vs office
   locations vs the geography of ALL cases (count by client country) vs review-platform
   locations. A market named only by an office address, with cases pointing elsewhere, caps at 3.
2. **Company type**: industry, size (revenue or headcount), stage, business model. Count the
   industries on the site and the review-platform split; is there a leading type? 10+ industries
   with equal weight caps at 2.
3. **Persona**: the buyer's job titles and what they own. Read "who it's for" on the main
   service pages, CTA wording, roles in case quotes. Generic roles ("leaders", "teams") = 2; one
   named title per service with its pain = 4.

**Delivery process ≠ internal process.** Delivery process = what the buyer gets and when:
phases, deliverables, stop point, what the client must provide. Internal rituals, roles and tools
are not scored here.

**Delivery process checklist** (mandatory table; ✓ = 1, ~ = 0,5):
1. one page for the MAIN service
2. 3–5 phases with weeks or days (a bare "Discovery → Design → Development → QA" caps at 2)
3. what the buyer holds after each phase
4. a stop point with its own price
5. what the client must give (owner, hours a week, access)
6. how progress is shown (format, cadence)
7. what happens when things go wrong (missed date, person replaced, scope change)
8. timelines and price tied to a baseline scenario and consistent with other pages and cases

Points → score: 0–1 → 1 · 1,5–3 → 2 · 3,5–5 → 3 · 5,5–7 → 4 · 7,5–8 and visible in the cases → 5.
Read the service pages in full; never judge from headings.

**Case anatomy** (mandatory table, 5 cases: the flagship, the newest, one per top segment, the
best-looking one). Mark ✓ / ~ / ✕ on 7 features: problem with a number · how the work went
(phases, weeks, rituals) · team (roles, size, both sides) · timeline · engagement model or budget
· result with a measurement basis · client quote with job title. Also scan ALL cases for the
share with a "how we worked" section. Score 2 if the reader cannot picture how their own project
would run, even with 30+ cases.

## 02 · Team (foundation)

| Criterion | What to check | Where |
|---|---|---|
| GTM roles | sales leadership, AE, SDR/BDR, marketing, presales: who is visibly in place | LinkedIn people search by company, About page |
| Owners of new markets | a named owner per announced market or office | LinkedIn, About, press |
| `?` Sales hiring and development | only from inside evidence | call |

## 03 · Lead generation (pipeline)

| Criterion | What to check | Where |
|---|---|---|
| SEO | organic traffic and keywords in the main market; share of traffic from the top page; do service pages get traffic; 2 peers for comparison | any SEO data tool, search results |
| AI visibility | 2–4 topics × 3–4 unbranded prompts across 3 assistants: mention share, citations, topics with zero, who gets named instead | AI assistants, run by hand or by script |
| LinkedIn and content | company page + CEO + sales lead: posts in 12 months, median reactions, topics | LinkedIn |
| Events | conferences, roadshows, webinars in 12 months; speaker or exhibitor roles | site, LinkedIn, event sites |
| Outreach infrastructure | MX, SPF, DKIM selectors, DMARC policy; separate sending domains that resolve; sender profiles | DNS lookup, LinkedIn |
| Inbound capture | tag container contents, visitor identification, lead-magnet gating, response promise | page source, forms |

## 04 · Sales (pipeline)

| Criterion | What to check | Where |
|---|---|---|
| Path to the first meeting | every CTA → where it lands → calendar or form → promised response time; does the calendar work | site, click through every CTA |
| Buyer materials | FAQ, pricing, engagement models, security page, contradictions between pages | site |
| `?` First call and proposal | only from inside evidence | call |

## 05 · Account management (pipeline)

| Criterion | What to check | Where |
|---|---|---|
| Retention | "client since" in cases, tenure named in quotes, repeat clients across cases | cases, reviews |
| Reviews and referrals | count, date of the latest review, platforms, share with job titles | review platforms |
| `?` Account expansion | only from inside evidence | call |

## 06 · Processes (foundation)

| Criterion | What to check | Where |
|---|---|---|
| Tracking and analytics | tags present in the container: analytics, ads, heatmaps, CRM scripts | page source |
| Forms-to-CRM link | form technology vs CRM tracking script; auto-reply after submit | page source, test submit |
| `?` Metrics and rhythms | only from inside evidence | call |

## Call questions

Each block ends with 2–3 questions for what is `?` or inferred. Questions ask about the last 12
months in concrete terms ("which title actually bought", "how many proposals went out in Q3"),
never about budget, authority, need or timing as a checklist.

## Writing lessons (from scored audits)

- H1 and every block H2 carry the finding with a number, not the topic.
- One scale legend everywhere: "1 = немає або не дає покупців"; bar caption "повна ширина = 5".
- Count reviews as reviews, never as clients.
- Date every "since" claim with its source.
- One reading per fact: the same quote cannot be a copy error in one block and loyalty in another.
- Repetition costs points: each headline number at most in the thesis and its own block.
- ICP rounding is always questioned: state "у підсумок блоку йде округлене 3".
- Dark mode: chips with `color:#fff` on `var(--ink)` vanish; use `color:var(--bg)`.
