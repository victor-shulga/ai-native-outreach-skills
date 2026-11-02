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

## Terms and plain-language output

<!-- glossary:start terms=account-tiers,decision-maker,day-to-day-owner,jtbd,anti-icp,trigger,market-score,beachhead,ecp,buying-committee,awareness-stages,checkpoint,hypothesis-confidence,tam-sam-som,paid-pilot -->
Rules for every document a client or their team will read (review, roast, canvas, offer cards, instruction):

1. **Open with «Словник цього документа»**: only the terms that actually appear in it, at most 10, each as «термін: що це простими словами». Like the definitions section of a contract.
2. **No internal codes or letter scales in the text** (A/B/C, D L T E, BLEND numbers without words, Own/Shared/Generic, Z1.4, GATE 2.5, T1–T6). Write the meaning instead: «є цифра з клієнтом», not «A».
3. **Use the plain form from the table below.** English stays only for tool names and for copy that ships in English (promises, hooks, subject lines). If the document is in another language, translate the plain form, never the internal term.
4. **Do not score what cannot exist yet.** A block that depends on work not done (signal catalog, case studies, a previous step) gets «пропущено: спершу потрібно <що саме>», not a score.
5. **Every section of a review opens with one concrete action** («до наступного дзвінка: …»), then at most five lines of why. No paragraph that only restates the framework.


| Internal term (this skill) | Write for the reader | What it means |
|---|---|---|
| Tier 1 / 2 / 3 (= A / B / C) | групи компаній: великі · середні · малі | ділимо ринок за розміром, бо чек, цикл угоди і хто вирішує в кожній групі різні; літер A/B/C у документі не пишемо. |
| decision maker | ОПР (особа, що приймає рішення) | той, хто підписує: власник, операційний директор, керівник напряму |
| day-to-day owner, champion | той, хто працюватиме з вами щодня | керівник проєкту, BIM-менеджер, керівник розробки; йому важливе інше, ніж ОПР |
| JTBD | задача клієнта | що людина намагається зробити, коли шукає рішення: «коли…, хочу…, щоб…» |
| Anti-ICP, disqualifiers | кому не продаємо | ознаки компаній, з якими не працюємо, щоб не витрачати на них час. |
| trigger, business trigger, account trigger, TRIGGER | подія-поштовх | подія в компанії покупця (нове керівництво, великий проєкт, втрата людини), після якої він починає шукати рішення. |
| Fit · Pain/Demand · Accessibility · Deal $ · Competition · Size | оцінка ринку: збіг із вашою сильною стороною · гострота болю · чи легко дістатися · чек · конкуренція · розмір | шість оцінок від 1 до 5, за сумою обираємо головний ринок. |
| beachhead | перша вузька ніша | один сегмент, де вас найлегше вибрати; звідти розширюємося |
| ECP, Early Customer Profile | перші клієнти, яких реально закрити за 1–2 квартали | вужча група за ICP: з неї беремо перші угоди і кейси. |
| DMU, buying committee, buying process | хто бере участь у рішенні і як воно ухвалюється | люди з боку клієнта, які впливають на покупку, і кроки, через які проходить угода. |
| Problem unaware → business trigger → problem aware → solution aware → alternatives → objections → consideration → decision → onboarding → expansion | етапи шляху покупця: не бачить проблеми · подія-поштовх · бачить проблему · шукає рішення · порівнює · обирає · перший результат · допродаж | де зараз покупець у голові і що йому потрібно почути саме на цьому етапі. |
| GATE 2.5, checkpoint | точка погодження з вами | місце, де зупиняємося і питаємо «підтверджуєте чи міняємо?»; код у документ не пишемо |
| propose-by-default, hypothesis · confidence low/med/high | наш варіант з рівнем упевненості | там, де ви ще не назвали відповідь, пропонуємо свою і пишемо, наскільки впевнені і на чому вона базується |
| TAM / SAM / SOM | весь ринок · ваша досяжна частина · реальна ціль на 1–3 роки | скільки грошей витрачають на вашу послугу; рахуємо витрати на послугу, розмір галузі клієнтів сюди не входить. |
| entry (paid pilot) | платний пілот | невелика робота з фіксованим обсягом, ціною і строком, яка доводить результат до великого договору |
<!-- glossary:end -->

## Вихід (Notion)
Під-сторінка **«03 · Market → ICP → Persona»**: Рівень 1 (таблиця 3 ринків зі скорингом 6 критеріїв +
рекомендація) · Рівень 2 (table of the three company groups named in words: large / mid / small, no Tier numbers or A/B/C letters + стартовий) · Рівень 3 (персони за шаблоном) ·
Anti-ICP · блок «Джерела / припущення». Українською; titles/verbatim — мовою оригіналу.

## Definition of Done
- Зафіксовано **клин + умови-гейти (pre-criteria)**, **лонгліст 8-12** і **чому шортліст саме ці 3** (з відсіяними).
- **3 ринки** оцінені за 6 критеріями (вкл. Size) + рекомендований primary з обґрунтуванням під стадію.
- **3 тіри** (Tier 1/2/3, де 1/A — найбільший) із розміром/чеком/циклом + признач стартовий.
- **DM-персона** за шаблоном (JTBD + buying process + triggers); champion — мін. стисло.
- **Anti-ICP** ≥ 3 disqualifiers.
- Болі прив'язані до verbatim зі Snapshot; впевненість + discovery-питання зафіксовані.
- Notion-сторінка створена; summary повернено оркестратору.
