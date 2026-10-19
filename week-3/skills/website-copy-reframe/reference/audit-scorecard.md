# Audit scorecard: 0-100 messaging rubric

Output of mode `audit`. Score the CURRENT copy (scraped or pasted) against the method. This is
the diagnosis that comes before any rewrite.

## Scoring (100 total)

### A. The five questions (50 points, 10 each)
Can a visitor from the target market answer each one easily?
1. **Which services?** Is the offer readable in five seconds, or buried under a list of industries?
2. **How does it run?** Is the engagement or process shown, or only implied?
3. **What gets delivered?** Are concrete deliverables named, or vague "solutions"?
4. **When would I hire them?** Is the trigger situation clear?
5. **How does it help me progress?** Tied to the champion's work, or generic "efficiency"?

Score each 0-10: 0 = missing or misleading, 5 = present but vague, 10 = specific and written to
the champion.

### B. Champion clarity (10 points)
Is the copy addressed to the champion close to the pain (for example a BIM coordinator, a GIS
manager, a CTO), or to an abstract "your business" or the executive buyer?
0 = no persona, 10 = one clear champion.

### C. Proof before claim (10 points)
Do numbers and cases lead, with the capability following? Or do adjectives make claims that the
page then cannot back? 0 = adjectives only, 10 = every claim carries a number or a case.

### D. Voice compliance (20 points), against the company's OWN brand rules
Start at 20 and deduct per violation (floor 0). A common rule set:
- Emoji where the brand rules forbid them: -4
- Hype words ("cutting-edge", "top-tier", "world-class", "revolutionising"): -3
- "Free pilot" or "free trial" where the brand offers a demo dataset or sample instead: -3
- Broken or placeholder stats ("0+ years", "0+ projects" from an unloaded counter): -4
- A horizontal spread across unrelated industries when the strategy is vertical: -3
- Missing domain vocabulary the buyer expects (for geospatial work, terms like CRS or LOD): -3

Replace this list with the company's actual rules when they exist.

## Output format

```
<Company> homepage | Messaging audit | Score XX/100

A. Five questions          __/50   (1:_ 2:_ 3:_ 4:_ 5:_)
B. Champion clarity        __/10
C. Proof before claim      __/10
D. Voice compliance        __/20
                           ─────
                           XX/100  ·  <one-line verdict>

Ranked gaps (most costly first):
1. <what is wrong> → <why it costs a lead> → <the fix>
2. ...
```

## Reading the score
- **80-100**: solid. Tighten, do not rebuild.
- **55-79**: real leaks. Run mode homepage on Hero, Problem and Solution.
- **Below 55**: the copy is working against the strategy. Full reframe and a new structure.

Always end with the recommended next mode (homepage or service-page) and the blocks to fix first.

Typical profile of a sub-55 site: emoji in headings, counters showing "0+", eight unrelated
industries on the homepage, "free pilot" language, and the strongest service buried below the
fold.
