---
name: gtm-market-icp-persona
description: Step 3 of the GTM flow and CHECKPOINT 2 (Market -> ICP -> Persona). Build the ICP top-down in three levels for an IT agency cold-audit — first propose the 3 best target markets the client could pursue (stage 0-1 clients do not yet know where to knock), then 3 account tiers (Tier 1/2/3 = A/B/C, where 1/A is the largest), then the buyer personas (decision-maker + champion/user) with JTBD, buying process, buying context and triggers, plus an Anti-ICP. Stage-adaptive depth; personas go deeper from stage 2+. Use when the user asks обери ринок, цільові ринки, побудуй ICP, ідеальний клієнт, персона, who to target, or right after the stage gate. Writes to Notion in Ukrainian.
argument-hint: "(reads Snapshot + Stage from the client's Notion page)"
---

# 03 · Market → ICP → Persona (GATE 2)

Третій крок і **другий чекпоінт**. ICP будуємо **зверху вниз у 3 рівні**. Головна ідея: на Стадії 0-1
агенція **ще не знає, куди стукатись** — тому крок 1 не «опиши клієнта», а **«обери ринок»**.
Cold audit → це гіпотеза з offer + мови клієнта + тех-сигналу, яку **підтверджуємо на discovery**.

Прочитай `reference/agency-stages.md`. Вхід — Snapshot (01) + Stage (02) з Notion.
**GTM enrichment** (`reference/gtm-frameworks.md` §1-2): **ECP-first** (кого
монетизуємо за 1-2 кв) vs ICP · beachhead-критерії (winnable ≤18 міс, ~100 компаній, 30-50%, painkiller) ·
**Market-Problem Map** (Pain × Ease-of-sale × Ease-of-impl) · GTM-сегментація (JTBD/pains/alternatives/values) ·
**DMU** + **Anti-persona** · validation confidence-ladder (interviews→presale).
Формат полів персон — за ICP-шаблоном Viktor'а (Ideal Company / DM / User / Anti-ICP).
(Окремого кроку для персон немає: персони — рівень 3 тут.)

## Реюз
- `icp-builder` (outbound-engine-skills) / `account-dossier` (account-management-skills) для синтезу;
  `market-research-edp` (цей пак) / `niche-data-finder` (outbound-engine-skills) — для оцінки ринків і розміру.
  Усе — якщо встановлено. Named-списки акаунтів — пізніше у `data-research` / `account-sourcing`
  (outbound-engine-skills), не тут.

## Рівень 1 · Цільові ринки (СПЕРШУ)
Не стрибай одразу до «3 ринків» — спершу покажи, **як вони потрапили в список**:

**1a · Клин + необхідні умови (pre-criteria, ДО скорингу).** Витягни зі Snapshot реальний клин агенції
(сильна сторона + тех-сигнал, не маркетингові claim'и). Сформулюй 5-7 **обов'язкових умов-гейтів**,
які ринок-кандидат МУСИТЬ мати, щоб клин давав очевидний ROI (приклади: високий обсяг повторюваних
phone/intake/workflow задач · вже є системи для інтеграції · фрагментований ринок із багатьма
SMB/mid операторами · чіткий вимірюваний $-біль · досяжний owner/ops-DM · потрібне гео · можна
запустити пілот без регуляторного блоку). Це **гейти кваліфікації, не бали**.

**1b · Лонгліст.** 8-12 вертикалей, що проходять гейти.

**1c · Шортліст → 3.** Обери 3, що найкраще проходять умови + найточніше лягають під клин; поясни
**чому саме ці 3 і чому відсіялись інші** (рядок на відсіяний). І лише тоді — скоринг.

**Скоринг шортлиста (3 ринки) 1-5 за 6 критеріями:**
- **Fit** — наскільки лягає під сильну сторону/офер агенції.
- **Pain/Demand** — гострота й частота болю в ринку.
- **Accessibility** — чи легко зробити список і дістатись (reachable, визначуваний).
- **Deal $** — бюджет/розмір чека.
- **Competition** — наскільки перенасичено (менше = краще; вищий бал = менше конкуренції).
- **Size** — розмір ринку / TAM (скільки таргетованих акаунтів існує).

Σ-бал (макс 30) → **рекомендуй 1 primary-ринок** + 1-2 рядки «чому саме він під цю стадію» (Стадія 0 →
обирай той, що дає **найшвидші перші 3-5 угод** для кейс-матеріалу: коротший цикл, простіший
комітет, прямий $-наратив).

## Рівень 2 · Тіри акаунтів
У межах primary-ринку — **3 тіри: Tier 1 / 2 / 3 (= A / B / C), де Tier 1 (A) — найбільший**, Tier 3 (C)
— найменший. На кожен: профіль, розмір (employees + revenue), pilot-чек, цикл, DM, зусилля. Поля з
«Ideal Company» шаблону (size, revenue, geo, tech stack, deal size). **Признач стартовий тір під стадію**
(0-1 → зазвичай **Tier 2-3 (B/C)** для швидких угод; **Tier 1 (A) відклади** — повільний комітет).

## Рівень 3 · Персони
Для **стартового тіру** опиши персони за шаблоном:
- **Decision-Maker** (обов'язково) і **Champion/User** (мін. стисло). Поля:
  Persona profile (titles, dept, success metrics) · **Transformation/JTBD** (jobs → existing way →
  ideal solution → pains → implications → success criteria) · **Buying process** (awareness /
  consideration / conversion) · **Buying context** (buying committee · checklist · preferred channels ·
  хто продає компліментарне) · **Triggers** (3).
- **Глибина за стадією:** Стадія 0-1 — DM (за шаблоном) + champion (стисло). **Від Стадії 2 включно** —
  повний шаблон обох персон + **Consumption behaviour** (top-5 сайти/розсилки/спільноти/події/influencers).
  Не вигадуй фейкові top-5 на ранніх стадіях — познач «уточнити на discovery».
- **Anti-ICP:** 3-5 disqualification criteria.

## Stage-adaptive глибина
- **Стадія 0-1:** 3 ринки → 1 primary → 3 тіри (старт Tier 2-3) → 1 DM + 1 champion (стисло) + Anti-ICP.
  Hypothesis-grade, явно «перевірити на discovery».
- **Стадія 2:** 1-2 валідовані ринки; **повні персони (DM + User) за повним шаблоном + consumption**.
- **Стадія 3-4:** мульти-ринок, per-segment персони + TAM-натяки (зв'язок із market-sizing).

## GATE 2 — чекпоінт
Поверни оркестратору: топ-3 ринки (зі Σ) + рекомендований primary + стартовий тір + DM-персона +
впевненість. Оркестратор покаже користувачу й чекатиме підтвердження/правок. Не починай VP/offers,
доки ринок+ICP не підтверджено.

## Вихід (Notion)
Під-сторінка **«03 · Market → ICP → Persona»**: Рівень 1 (таблиця 3 ринків зі скорингом 6 критеріїв +
рекомендація) · Рівень 2 (таблиця Tier 1/2/3 + стартовий) · Рівень 3 (персони за шаблоном) ·
Anti-ICP · блок «Джерела / припущення». Українською; titles/verbatim — мовою оригіналу.

## Definition of Done
- Зафіксовано **клин + умови-гейти (pre-criteria)**, **лонгліст 8-12** і **чому шортліст саме ці 3** (з відсіяними).
- **3 ринки** оцінені за 6 критеріями (вкл. Size) + рекомендований primary з обґрунтуванням під стадію.
- **3 тіри** (Tier 1/2/3, де 1/A — найбільший) із розміром/чеком/циклом + признач стартовий.
- **DM-персона** за шаблоном (JTBD + buying process + triggers); champion — мін. стисло.
- **Anti-ICP** ≥ 3 disqualifiers.
- Болі прив'язані до verbatim зі Snapshot; впевненість + discovery-питання зафіксовані.
- Notion-сторінка створена; summary повернено оркестратору.
