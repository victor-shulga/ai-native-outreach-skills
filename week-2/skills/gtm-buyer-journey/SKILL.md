---
name: gtm-buyer-journey
description: Step 9 of the GTM flow. Map the buyer's journey for the chosen persona — stages from unaware to advocacy (unaware -> problem-aware -> solution-aware -> vendor consideration -> decision/pilot -> onboarding -> expansion) with, per stage, the buyer mindset/questions, the trigger that advances them, the main objection, the touchpoint/content that fits, and the channel. Feeds materials (10) and channels (11). Stage-adaptive. Use when the user asks buyer journey, customer journey, шлях покупця, awareness consideration decision, funnel stages, touchpoints. Writes to Notion in Ukrainian.
argument-hint: "(reads persona + positioning + VP + competitor + offers from steps 3-8 in Notion)"
---

# 09 · Buyer's Journey

Дев'ятий крок. Карта шляху покупця для обраної персони — від «не усвідомлює» до «адвокат». На кожній
стадії: що думає/питає, що тригерить перехід далі, головне заперечення, доречний тачпоінт/контент, канал.
Це **міст до 10 (матеріали) і 11 (канали)** — їх будуємо проти цієї карти. Без гейту.

Вхід — 03 (персона/JTBD), 06 (позиціонування), 07 (VP, dream outcome, objections), 05 (alternatives), 08 (offers/ladder).
Прочитай `reference/agency-stages.md`.

## Реюз
`deep-company-analyser` (customer language per стадія) · buying-process поля з VP-канвасу (07).

## Стадії (адаптуй назви під ринок)
1. **Problem unaware** — не бачить проблеми («так і працюємо»).
2. **Business trigger** — внутрішня/зовнішня подія, що запускає пошук (пік-сезон, падіння revenue,
   скарги, нове керівництво). Часто саме її чіпляє outbound — окрема, важлива стадія.
3. **Problem aware** — усвідомив біль, ще не шукає рішення.
4. **Solution aware** — шукає життєздатні рішення (вкл. наше); часто скептик.
5. **Alternatives** — розглядає інші способи вирішити (вкл. do-nothing / in-house; деталі — 05).
6. **Objections** — причини НЕ купувати таке рішення, як ваше.
7. **Consideration** — що змушує розглянути саме вас (ціни, tailored proposal, гарантія, легкий старт).
8. **Decision** — що змушує обрати саме вашу компанію (business case, references, low-ticket offer).
9. **Onboarding / first value** — від контракту до першого результату.
10. **Expansion / advocacy** — апсел/реферал.

**Buying process (поглинається з персони 03).** awareness = 1-3 → consideration = 4-7 → decision = 8 →
post-sale = 9-10. У 03 buying process лишається стисло (на рівні персони); повна карта — тут.

## На кожну стадію — 6 полів
- **Mindset / питання** (що думає, що гуглить, що питає — customer language).
- **Trigger to advance** (що штовхає на наступну стадію).
- **Головне заперечення / гальмо**.
- **Тачпоінт / контент** (що тут доречно — годує крок 10).
- **Канал** (де відбувається — годує крок 11).
- **Хто веде** (роль: outbound/marketing/sales/AM).

## Принципи
- **Старт із реального рівня обізнаності.** На Стадії 0-1 outbound часто стартує покупця ще на 1-2
  (ми самі тригеримо awareness) — не вигадуй «inbound-шлях клієнта», якого ще нема.
- Контент/канали — **наслідок** шлях клієнта, не навпаки (інакше «шарашимо навмання»).
- Заперечення беруться з 07 (VP) і реальних альтернатив (05).

## Journey example (наратив)
Окрім таблиці — **конкретний touch-by-touch приклад**, як реальний покупець проходить шлях від
business trigger до decision (із реальними тачпоінтами/повідомленнями). Робить шлях клієнта відчутним і
перевіряє логіку переходів (як приклад-наратив у content-plan документі Viktor'а).

## Stage-adaptive глибина
- **Стадія 0-1:** 1 персона; фокус на стадіях 1-5 (outbound-driven); 6-7 — стисло.
- **Стадія 2:** повна шлях клієнта + мапа контенту per стадія (inbound вмикається).
- **Стадія 3-4:** per-segment шлях клієнта + attribution + lifecycle/expansion деталізація.

## Terms and plain-language output

<!-- glossary:start terms=awareness-stages,trigger,touchpoint,jtbd,dream-outcome,competitor-lanes,low-ticket,agency-stage -->
Rules for every document a client or their team will read (review, roast, canvas, offer cards, instruction):

1. **Open with «Словник цього документа»**: only the terms that actually appear in it, at most 10, each as «термін: що це простими словами». Like the definitions section of a contract.
2. **No internal codes or letter scales in the text** (A/B/C, D L T E, BLEND numbers without words, Own/Shared/Generic, Z1.4, GATE 2.5, T1–T6). Write the meaning instead: «є цифра з клієнтом», not «A».
3. **Use the plain form from the table below.** English stays only for tool names and for copy that ships in English (promises, hooks, subject lines). If the document is in another language, translate the plain form, never the internal term.
4. **Do not score what cannot exist yet.** A block that depends on work not done (signal catalog, case studies, a previous step) gets «пропущено: спершу потрібно <що саме>», not a score.
5. **Every section of a review opens with one concrete action** («до наступного дзвінка: …»), then at most five lines of why. No paragraph that only restates the framework.


| Internal term (this skill) | Write for the reader | What it means |
|---|---|---|
| Problem unaware → business trigger → problem aware → solution aware → alternatives → objections → consideration → decision → onboarding → expansion | етапи шляху покупця: не бачить проблеми · подія-поштовх · бачить проблему · шукає рішення · порівнює · обирає · перший результат · допродаж | де зараз покупець у голові і що йому потрібно почути саме на цьому етапі. |
| trigger, business trigger, account trigger, TRIGGER | подія-поштовх | подія в компанії покупця (нове керівництво, великий проєкт, втрата людини), після якої він починає шукати рішення. |
| touchpoint | точка контакту | місце чи матеріал, де покупець стикається з вами: лист, сторінка, дзвінок, пост. |
| JTBD | задача клієнта | що людина намагається зробити, коли шукає рішення: «коли…, хочу…, щоб…» |
| dream outcome | бажаний результат клієнта | як виглядає ситуація клієнта, коли проблему вирішено, його ж словами |
| lanes / clusters: direct, marketplace, adjacent, in-house, platform-native, incumbent, DIY, do nothing | типи альтернатив: прямі конкуренти · фрилансери з маркетплейсів · сусідні послуги · свій найм · платформи · старий постачальник · зробити самим · нічого не робити | з усім цим покупець вас порівнює, тому дивимось ширше за прямих конкурентів. |
| low-ticket | недорогий офер | готові інструкції й шаблони, які клієнт застосовує сам |
| Stage 0–5, стадія агенції | стадія розвитку компанії (0–5) | шість щаблів від «CEO робить усе» до «портфель напрямів»; від стадії залежить, що доречно робити зараз. |
<!-- glossary:end -->

## Вихід (Notion)
Під-сторінка **«09 · Buyer's Journey»**: таблиця стадій × 6 полів + примітка, що годує 10/11 +
блок «Джерела / припущення». Українською; customer-language фрази — як є.

## Definition of Done
- Усі релевантні стадії (для Стадії 0-1 фокус 2-8: від business trigger до decision) з 6 полями.
- Mindset/заперечення — у customer language (з 07/05), не вигадані.
- Явно позначено реальний стартовий рівень обізнаності (де вмикається outbound).
- Є **Journey example** (touch-by-touch наратив) для головної персони.
- Тачпоінти/канали позначені як вхід для 10/11. Notion-сторінка створена.
