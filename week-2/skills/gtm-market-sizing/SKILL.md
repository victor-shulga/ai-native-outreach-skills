---
name: gtm-market-sizing
description: Step 4 of the GTM flow. Size the market the client chose in step 3 using Viktor's TAM-SAM-SOM framework — computed BOTH top-down (public market data, cut to the relevant slice) and bottom-up (target accounts x annual spend on the agency's service), then reconciled. Sizes by account tier (1/2/3 from step 3) and notes growth. The TAM is spend on the AGENCY'S service (e.g. AI automation), not the size of the client's end-market. Stage-adaptive depth. Use when the user asks TAM SAM SOM, market sizing, розмір ринку, скільки грошей у ніші, market research, or right after market/ICP selection. Writes to Notion in Ukrainian.
argument-hint: "(reads the recommended market + tiers from the step-3 Notion page)"
---

# 04 · Market Sizing — TAM / SAM / SOM

Четвертий крок. Кількісно оцінити **обраний у кроці 3 ринок** (і за потреби — топ-3 для звірки
критерію Size). Реалізує **TAM-SAM-SOM фреймворк Viktor'а**: рахуємо **і top-down, і bottom-up**,
тоді звіряємо. Без гейту.

Прочитай `reference/agency-stages.md` (TAM розділ). Вхід — крок 03 (ринок + тіри +
ICP) з Notion.

## ⚠️ Головне правило
**TAM = спенд на ПОСЛУГУ агенції** (напр. на AI-автоматизацію/voice), **а НЕ розмір кінцевого ринку
клієнтів.** Помилка: брати «$600B home services» як TAM. Правильно: `# target firms × річний спенд на
наш тип рішення`.

## Реюз
- `market-research-edp` (цей пак) / `niche-data-finder` (outbound-engine-skills), якщо встановлені, + `WebSearch` для джерел (к-сть фірм,
  market reports, ARPU). Кожне число — з посиланням; де нема — позначити «оцінка, перевірити».
- Опційно заповнити Google-шаблон Viktor'а (TAM_SAM_SOM_Template) копією — за запитом.

## Два методи (рахуй обидва)
**Top-down:** взяти публічні дані ринку → відрізати нерелевантне фільтрами (гео, розмір, % що купують
наш тип рішення, % serviceable, % obtainable). Джерела: IBISWorld / Census CBP / Statista / галузеві звіти.
**Bottom-up:** `# таргет-акаунтів × річний чек` (із тірів кроку 3). SOM — з реальної capacity
(скільки угод закриє команда стадії за 1-3 роки × ACV).

Порядок: top-down від TAM вниз; bottom-up від SOM вгору. Потім **звірити пари** й пояснити розбіжності
(bottom-up зазвичай скромніший).

## Розбивка по тірах
SAM/SOM рахуй **по Tier 1/2/3** (із кроку 3), бо ACV і % obtainable різні per тір. Для Стадії 0-1
концентруй SOM у стартових тірах (2-3), Tier 1 — поза near-term SOM.

## Stage-adaptive глибина
- **Стадія 0:** lite — bottom-up sanity-check (чи ринок узагалі достатній: `#firms × ACV`) + грубий
  SOM = реалістична ціль 1 року. TAM/SAM — одним рядком. Не закопуйся.
- **Стадія 1:** повний top-down + bottom-up TAM/SAM/SOM, звірка.
- **Стадія 2:** + розбивка по розмірних бендах/тірах (модель просунутого шаблону) + кілька джерел (середнє).
- **Стадія 3-4:** + мульти-гео + 3-5y growth-проєкція (CAGR) + intent-data шар.

## Вихід (Notion)
Під-сторінка **«04 · Market Sizing (TAM-SAM-SOM)»**: таблиця TAM/SAM/SOM × (top-down | bottom-up) +
розбивка по тірах + припущення/фільтри з джерелами + висновок «чи ринок достатній + куди фокус».
Блок «Джерела / припущення». Українською.

## Definition of Done
- TAM/SAM/SOM пораховано **двома методами** і звірено (різниця пояснена).
- TAM = спенд на послугу агенції (не кінцевий ринок) — перевірено.
- SAM/SOM розкладено по тірах; SOM-фокус відповідає стадії.
- Кожен ключовий вхід має джерело або явну позначку «оцінка, перевірити».
- Висновок: ринок достатній для цілей? куди концентрувати SOM? Notion-сторінка створена.
