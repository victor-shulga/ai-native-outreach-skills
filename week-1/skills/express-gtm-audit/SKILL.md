---
name: express-gtm-audit
description: Express audit of a B2B service company's GTM system from public data only (site, cases, review platforms, LinkedIn, search, AI answers, DNS). Scores 6 blocks of the GTM system (strategy, team, lead generation, sales, account management, processes) on 24 criteria, scale 1-5, «?» for what is not visible from outside; block score = mean of scored criteria. Output is one single-file HTML page in a fixed order - a diagnosis header (which block is the main problem, big coloured score), 4 verdict tiles, a bowtie dashboard of the funnel with a donut per stage over the foundation tiles, then block by block in tables, each ending with a «what to do» line and questions for the call. Use when the user says express audit, експрес-аудит, оціни нашу агенцію ззовні, аудит перед дзвінком, audit this agency from the outside, score our GTM in 6 blocks, or when a course/homework asks for the 6-block self-audit. Not the weighted 23-criteria maturity audit (that is gtm-audit) and not a website UX audit.
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
- **Results first, as a diagnosis.** H1 = «<Company>: головна проблема в <weakest block>», never a
  topic and never a row of coloured numbers. Methodology never comes first.
- **Less text.** Tables, tiles and charts over paragraphs. A tile's big text says what the fact
  means («Офер готовий до продажу», «Кейси не відкриваються»); the numbers go in its caption.
  A bare number in a tile says nothing.
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
Overall label (same buckets as the self-assessment tool): below 2 «Системи ще немає» · 2–2,9
«Тримається на фаундері» (red) · 3–3,9 «Працює нерівно» (amber) · 4+ «Система працює» (green).
Dashboard percentages = score ÷ 5 × 100: 90–100% норма · 80–89% майже норма · 50–79% увага ·
below 50% проблема · grey «?» = not visible. Show the formula next to any
composite number and say how many criteria were scored ("середнє по 20 критеріях").

## The 6 blocks and 24 criteria

Full checklists, tables and sources are in `references/rubric.md`. Read it before scoring.

| # | Block | Criteria |
|---|---|---|
| 01 | GTM strategy (foundation) | ICP (3 components) · positioning · offer · delivery process (8-point checklist) · lead magnets · case depth (5 cases × 8 features) |
| 02 | Team (foundation) | GTM roles · owners of announced markets · `?` sales hiring and development |
| 03 | Lead generation (pipeline) | SEO · AI visibility · LinkedIn and content · events · outreach infrastructure · inbound capture |
| 04 | Sales (pipeline) | path to the first meeting · buyer materials · `?` first call and proposal |
| 05 | Account management (pipeline) | retention · reviews and referrals · `?` account expansion |
| 06 | Processes (foundation) | tracking and analytics · forms-to-CRM link · `?` metrics and rhythms |

Criteria marked `?` are almost never visible from outside. Keep them in the table, score them
only when the user supplies inside evidence (answers, exports, call notes).

Plus one **separate track, «Довіра до сайту» (site trust), 0–100**: 8 weighted criteria
(independent ratings 15 · verifiable testimonials 15 · named cases 15 · faces 15 · consistent numbers 15 ·
legal entity and reachability 10 · certificates and partnerships 10 · pulse 5), score 1–5 each,
trust = Σ(score ÷ 5 × weight). It never enters the 24-criteria overall. Rubric, verification path
and number-drift rule in `references/rubric.md`.

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

`references/example-audit.html` is the etalon (since 23.10.2026): a complete audit of a real 3D and
motion studio for CleanTech, anonymised as «Studio X» (company, people, clients, cities, prices and one
headline figure changed). Overall 3,1 / 5 «Працює нерівно» across 16 scored criteria, 8 marked `?`,
site trust 57/100. It shows the diagnosis header, the verdict tiles, the bowtie dashboard, the
«Розклад на складові» cards (Offer 6 · Value Proposition 4 · ICP 3), the delivery-process table, the
case anatomy table, the trust track with its verification path, and a call-questions box under every
block. Copy its HTML and CSS; the bowtie SVG and the cards are plain markup you fill with your numbers.
The same page is live at https://vs-express-audit-example.shoulga-v.workers.dev. A blank version for a
founder filling the audit by hand, with everything computed on the fly, is at
https://vs-express-audit-template.shoulga-v.workers.dev; this skill produces the filled page, not the
blank one.

## Page order (fixed)

1. **Diagnosis header**: H1 «<Company>: головна проблема в <weakest block>»; under it one line
   «Найслабші блоки: …, N з 5» plus 1–2 sentences of facts; the overall score large and coloured by
   its bucket, with the bucket label as a pill; «prepared from public data only».
2. **4 verdict tiles**: big text = what it means, caption = the numbers (two strengths, two gaps
   is typical), then one line «Перший крок: …».
3. **Bowtie dashboard «GTM-система: де губляться клієнти»**: funnel Формування попиту (SEO, AI,
   LinkedIn, events) → Захоплення попиту (outreach, inbound) → Продажі → knot «Угода» → Утримання →
   Відгуки → Розширення, a donut with % on every stage; under it the foundation as coloured tiles:
   01 strategy (its 6 criteria + Value Proposition), 02 team, 06 processes, each group with its
   donut; the legend. On phones the funnel becomes a vertical list.
4. **Bars of the 6 block scores**, H2 «Оцінки 6 блоків: N з 6 нижче 3».
5. **Blocks 01–06.** Block 01 opens with «Розклад на складові»: Offer (entry product, price, term,
   what the buyer holds, risk reversal, next step), Value Proposition (dream outcome, proof, time to
   result, client effort), ICP (3 components 1–5); each row ✓ / ~ / ✕ in green / amber / red, a
   «X з N» count and a segmented bar. Every block: H2 = a fact with a number, criteria in a table
   (score · what is visible), mandatory tables where they belong, one «Що зробити» line, a
   «Питання на дзвінок» box.
6. **Trust track «Довіра до сайту»**: H2 with the 0–100 score, table of 8 criteria (weight · score ·
   what is visible), the formula line, a number-drift table, a «Шлях перевірки» table
   (clicked → opened → ✓/✕), «Що зробити».
7. **Next step**: one link or one hand-in instruction.
8. **Sources**: every URL and record used.

## Self-check before delivering

- Every score has evidence; every `?` has a question.
- H1 names the weakest block; no block H2 is a bare block name; each carries a fact with a number.
- No tile shows a bare number as its big text.
- Headline numbers appear at most twice (thesis and its block).
- Reviews are counted as reviews, not as clients.
- Trust track: every repeated number (team, years, projects, clients) checked on home, About,
  meta description, LinkedIn and review platform; one drift caps «Чесні й узгоджені цифри» at 2.
- Trust track never changes the overall GTM score.
- Every "since", "years", "average" has a dated source or is removed.
- No client names of the author, no em dashes in Ukrainian, decimal comma.
- The page has `<meta name="viewport">` and does not scroll sideways on a phone.

## Terms and plain-language output

<!-- glossary:start terms=value-equation,dream-outcome,risk-reversal,free-hook,inbound-outbound,spf-dkim,ai-visibility,bowtie,expand,referral,cold-audit -->
Rules for every document a client or their team will read (review, roast, canvas, offer cards, instruction):

1. **Open with «Словник цього документа»**: only the terms that actually appear in it, at most 10, each as «термін: що це простими словами». Like the definitions section of a contract.
2. **No internal codes or letter scales in the text** (A/B/C, D L T E, BLEND numbers without words, Own/Shared/Generic, Z1.4, GATE 2.5, T1–T6). Write the meaning instead: «є цифра з клієнтом», not «A».
3. **Use the plain form from the table below.** English stays only for tool names and for copy that ships in English (promises, hooks, subject lines). If the document is in another language, translate the plain form, never the internal term.
4. **Do not score what cannot exist yet.** A block that depends on work not done (signal catalog, case studies, a previous step) gets «пропущено: спершу потрібно <що саме>», not a score.
5. **Every section of a review opens with one concrete action** («до наступного дзвінка: …»), then at most five lines of why. No paragraph that only restates the framework.


| Internal term (this skill) | Write for the reader | What it means |
|---|---|---|
| Value Proposition X/4: Dream Outcome, perceived likelihood, Time Delay, Effort & Sacrifice | ціннісна пропозиція: бажаний результат · віра, що вийде · час до результату · зусилля клієнта | чим більший результат і віра в нього, і чим менше часу та зусиль, тим цінніша пропозиція. |
| dream outcome | бажаний результат клієнта | як виглядає ситуація клієнта, коли проблему вирішено, його ж словами |
| risk reversal, guarantee | гарантія, що знімає ризик | що клієнт отримає, якщо результату не буде: повернення грошей, безкоштовне продовження, оплата за етапами |
| hook / free offer, lead magnet | безкоштовний вхід | аудит, розрахунок втрат або розбір, що показує проблему і веде до розмови |
| inbound / outbound, inbound capture | вхідні заявки · холодні звернення | клієнт приходить сам через сайт і контент, або ви пишете йому першим. |
| SPF, DKIM, DMARC, sending domains | SPF, DKIM, DMARC (записи, що підтверджують вашу пошту) | без них листи потрапляють у спам; для розсилок потрібні ще й окремі домени. |
| AI visibility | видимість у відповідях AI-асистентів | чи називають вас ChatGPT, Gemini, Perplexity, коли покупець питає про вашу послугу. |
| bowtie dashboard | схема «GTM-система: де губляться клієнти» | шлях від першого контакту до угоди і далі до утримання й допродажу, з оцінкою кожного етапу. |
| expand, land-and-expand | допродаж після першої роботи | дорожчі сходинки не пропонуємо холодним людям, їх продаємо клієнту, який уже отримав результат на вхідному офері |
| referral | рекомендації | клієнти приводять інших клієнтів. |
| cold audit | огляд ззовні за публічними даними | оцінка лише з того, що бачить сторонній: сайт, LinkedIn, відгуки; внутрішніх даних ще немає. |
<!-- glossary:end -->
