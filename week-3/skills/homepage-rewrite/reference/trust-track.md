# Trust track: the second pass of a homepage rewrite

The clarity track makes a visitor understand **what, for whom, and what result** in 5 seconds.
The trust track makes them **believe it**. A clear page with unbacked claims reads as a pitch;
a page full of proof with no clear offer reads as a portfolio. The homepage needs both.

`website-audit` only counts whether trust markers exist (testimonials, cases, logos).
This track judges whether they are **real, specific, and placed next to the promise they back**.

Input: the proof bank from Step 2 (`proof-bank.md`). If the bank is thin, the rewrite says so
and leaves the slot out. It never invents a case, a number, a quote or a logo.

## The 6 trust rules

### T1. Named cases with a number
Every case on the homepage = **who** (named client or a precise descriptor if under NDA) +
**result as a number** + **timeframe**.
- weak: "We helped a fintech company grow."
- strong (fictional): "Payments startup, 40 → 140 demo calls a quarter in 6 months."
If the client allows the name, use it; an NDA descriptor must still be specific
(segment + size + geo). A case without a number goes to the case page only.

### T2. Logos and testimonials: real only
- Logo strip = clients who actually paid, with permission. No tool/vendor logos posing as
  clients, no "as seen in" without a link to the mention.
- Testimonial = quote + full name + role + company (+ photo or a profile link). An anonymous
  quote signed only "CEO, SaaS company" counts as zero.
- Independent review links beat on-site quotes: Clutch, G2, Trustpilot, LinkedIn
  recommendations (`linkedin.com/in/<id>/details/recommendations`). Link at least one if it
  exists.

### T3. No placeholders
Delete before shipping: "coming soon", "soon", empty cards, `0+` counters, lorem ipsum, a nav
link to an empty section, a blog with one post from two years ago, a "Case studies" page with
no cases. Each one tells the visitor the company is not finished. A missing block costs less
than a visible gap.

### T4. Proof next to the promise
Each promise gets its proof **in the same block**, within one scroll:
- Hero promise → trust line under the CTA (number of clients, one named result, or a review
  score with a link).
- Each Solution argument → one matching case or number.
- Pricing / offer → a guarantee or a named result at that tier.
A proof section at the bottom of the page does not back a hero claim at the top.

### T5. Every promise has an address
Each claim on the page must lead somewhere the visitor can check it: a case page, a review
link, a public demo, a downloadable sample. Click through every link before calling the
rewrite done. A "see our cases" link that lands on a list of three logos fails.

### T6. Voice that sounds like a person
Adjectives in place of proof are a trust leak (see the buzzword kill-list in
`copy-blocks.md`). Edit the final copy for AI tells (with `anticopywriting-ai`, if installed): no negative parallelism,
no rule-of-three punch lines, no em-dash cascades, no "cutting-edge / world-class".

## Diagnosis table (trust half)

Score each rule 0-2 (0 = broken, 1 = partial, 2 = solid). Max 12.

| Rule | Score | Evidence on the current page | Fix |
| --- | --- | --- | --- |
| T1 Named cases with a number | | | |
| T2 Real logos and testimonials | | | |
| T3 No placeholders | | | |
| T4 Proof next to the promise | | | |
| T5 Every promise has an address | | | |
| T6 Human voice | | | |

## Worked example (neutral)

Current hero on a fictional dev shop:
> "Innovative software solutions for forward-thinking businesses. Trusted by industry leaders."
> Logo strip: stripe.com and linear.app logos (tools the team uses, presented as clients).
> Below: "Case studies: coming soon".

Diagnosis: T1 0 (no case), T2 0 (tool logos as clients), T3 0 ("coming soon"), T4 0 (the
"trusted by" claim has no proof), T5 0 (nothing to click), T6 0 ("innovative",
"forward-thinking").

Rewrite:
> Category: Product engineering for B2B SaaS
> H1: Ship the roadmap your sales team already promised
> Sub: A senior squad joins your sprint in 2 weeks and owns delivery end to end.
> CTA: Get a delivery estimate
> Trust line: Series A analytics platform: release cycle 6 → 2 weeks · 4.9 on Clutch (link)

Where the trust line comes from (all fictional, like the rest of the example): Step 1 followed
the links off the homepage and found both items on inner pages the homepage never used.
- Proof bank row 2: the case page `/cases/analytics-platform`, release cycle 6 → 2 weeks.
- Proof bank row 5: the Clutch profile linked from the footer, 4.9.

The client count is left out: nothing on the site states it, so it goes to the questions list
("How many SaaS clients have you shipped for, and may we say so?"). Tool logos removed. The
"coming soon" block is gone until two real cases exist.
