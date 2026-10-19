# AI-native аутріч для агенцій · скіли по тижнях

Скіли для Claude, якими ми працюємо на курсі [«AI-native аутріч для агенцій»](https://victorshulga.com/ai-native-outreach/) Віктора Шульги. Одна тека = один тиждень курсу, у кожній лише ті скіли, які знадобляться на цьому тижні.

| Тиждень | Тема | Скілів | Встановити |
|---|---|---|---|
| [week-1](week-1/) | Попит та інфраструктура | 5 | `npx skills add victor-shulga/ai-native-outreach-skills/week-1` |
| [week-2](week-2/) | Стратегія проспектингу | 5 | `npx skills add victor-shulga/ai-native-outreach-skills/week-2` |
| [week-3](week-3/) | Підготовка до запуску | 7 | `npx skills add victor-shulga/ai-native-outreach-skills/week-3` |
| [week-4](week-4/) | Гіпотези й радари | 12 | `npx skills add victor-shulga/ai-native-outreach-skills/week-4` |
| [week-5](week-5/) | Запуск кампанії | 8 | `npx skills add victor-shulga/ai-native-outreach-skills/week-5` |
| [week-6](week-6/) | Відповіді й аналітика | 7 | `npx skills add victor-shulga/ai-native-outreach-skills/week-6` |

Почніть з першого тижня: у ньому є `max`, оркестратор, який підкаже, який скіл запускати далі.

## Як встановити

| У вас є | Що зробити |
|---|---|
| термінал (Claude Code) | команда з таблиці вище в теці, де ви працюєте; оновлення = та сама команда ще раз |
| Claude Desktop або claude.ai без терміналу | відкрийте теку тижня → `skills/<скіл>` → завантажте як ZIP → Settings → Capabilities → Skills → Upload a skill |

Якщо у вас уже встановлені основні паки (`gtm-strategy-skills`, `outbound-engine-skills` та інші), ці скіли там уже є: ставити тиждень окремо не треба.

## Звідки скіли

Це копії з основного стеку скілів Віктора: повний каталог з описами живе тут: https://github.com/victor-shulga/max/blob/main/CATALOG.md. Оновлення спершу виходять в основних паках, сюди їх переносить `sync.py` за списком у `weeks.json`.

## Requirements & integrations

| Integration | Used for | Required? | Auth/setup |
|---|---|---|---|
| Claude (Pro або Max) | запуск скілів | так | акаунт Claude |
| Claude Code або Claude Desktop | встановлення скілів | так | один з двох |
| Node.js 18+ | команда `npx skills add` | лише для встановлення з терміналу | `node -v` |
| Інструменти курсу (Apify, Instantly, Twenty тощо) | дані, розсилка, CRM у конкретних скілах | ні, залежить від скіла | описано в SKILL.md кожного скіла |

## Ліцензія

Скіли поширюються на тих самих умовах, що й у їхніх основних паках (LICENSE усередині паків). Сторонні методики позначені в теках скілів, де вони використані.
