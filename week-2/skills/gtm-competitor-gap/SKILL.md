---
name: gtm-competitor-gap
description: Step 5 of the GTM flow (right after market sizing, BEFORE positioning and offers). Map direct and indirect competitors (incl. platform/CRM-native, incumbent/human answering, DIY build, and do-nothing) into a matrix, then run a GAP analysis — where the agency wins, is at parity, or is behind — and surface positioning whitespace the agency can own. Informs positioning (06) and offers (08) so they are built from the gap with no rework. Stage-adaptive. Use when the user asks конкуренти, competitor analysis, gap analysis, battlecards, how do we differentiate, alternatives, whitespace, red ocean. Writes to Notion in Ukrainian.
argument-hint: "(reads market/ICP + sizing from steps 3-4 in Notion)"
---

# 05 · Competitor + GAP analysis

П'ятий крок (одразу після market-sizing, **ДО** positioning і offers). Positioning живе в порівнянні —
тому конкурентів аналізуємо ПЕРЕД VP (метод Dunford). Зібрати конкурентів (прямих + непрямих), знайти,
**де ми реально виграємо / на парі / програємо**, і головне — **whitespace** (незайняте позиціонування,
яке агенція може зайняти). Без гейту: **whitespace одразу живить 06 (positioning) → далі 07 (VP) і 08 (offers)** — без
рерайту; за потреби може звузити ринок (03, рідко).

Вхід — 03 (ринок/ICP), 04 (sizing). Прочитай
`${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md`.

## Реюз
`competitor-finder` (цей пак, якщо встановлений) + `WebSearch` (реальні гравці, ціни, відгуки G2/Clutch). Кожен конкурент — з
посиланням/джерелом.

## Кластери (не забувай непрямих — найчастіша помилка)
- **Direct** — ті, хто продає те саме тій самій персоні.
- **Platform / native** — платформи/CRM, що додають цю функцію нативно (часто найбільша загроза, бо вже
  «в стеку» клієнта).
- **Incumbent / human** — старі рішення (агенції/сервіси/люди), що закривають той самий job.
- **DIY / build** — клієнт будує сам (для агенцій — in-house team / no-code платформи).
- **Do nothing / status quo** — найчастіша «альтернатива».

## Матриця (атрибути на конкурента)
Type · Positioning · Target tier · Pricing model · Strengths · **Weakness / gap для покупця** · Channel.

## Battle angles
На топ-конкурентів — 1 рядок «як позиціонуватись проти» (для sales/outreach).

## GAP analysis
- **Win** — де ми об'єктивно кращі (з evidence).
- **Parity** — де однаково (це вже table-stakes, не диференціатор).
- **Behind** — де програємо (чесно: бренд/проф/ціна/дані/scale).
- **Whitespace** — 1-3 незайняті позиції, які ми можемо зайняти (перетин наших сил × дір ринку).
- **Strategic implication** — якщо «answer+book» уже table-stakes/контестно → це **задає positioning у 06**
  (обрати whitespace, не воювати в лоб) і/або **вужчий beachhead у 03** (рідко). Тепер це наперед, не рерайт.

## Stage-adaptive глибина
- **Стадія 0-1:** 3 direct + кластери непрямих + GAP + **1 whitespace-рекомендація**. Чесно про «red ocean».
- **Стадія 2:** + battlecards на топ-3 (strengths/weaknesses/how-to-win) + win/loss зачіпки.
- **Стадія 3-4:** + emerging entrants + adjacent categories + quarterly refresh.

## Вихід (Notion)
Під-сторінка **«05 · Competitor + GAP»**: матриця (таблиця по кластерах) · battle angles · GAP
(win/parity/behind) · whitespace · strategic implication (+ чи треба правити 05/03) · «Джерела».
Українською; назви/ціни — як є.

## Definition of Done
- ≥3 direct + усі релевантні непрямі кластери (вкл. platform-native, DIY, do-nothing).
- Матриця з weakness/gap для покупця на кожного; battle angle на топ-3.
- GAP: win/parity/behind + **≥1 whitespace** + явна strategic implication.
- Якщо ніша контестна — whitespace передано у 06 (positioning) і за потреби звужено 03. Джерела на кожного. Notion створено.
