---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-company-timeline-tooltip-alternating-event-cards/"
title: "Tailwind Company Timeline Tooltip with Alternating Event Cards"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A seven-stop company timeline whose events alternate above and below the track, each opening a card with quarter, headline, badge, narrative and one impact…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Company Timeline Tooltip with Alternating Event Cards
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-company-timeline-tooltip-alternating-event-cards/

A seven-stop company timeline whose events alternate above and below the track, each opening a card with quarter, headline, badge, narrative and one impact figure. The alternation is the port's interesting case: odd:flex-col-reverse and odd:*:bottom-[calc(100%+10px)] keep an nth-child rule as a variant instead of a separate selector.
## HTML
```html
<section class="ttp-19 relative w-full min-h-svh overflow-hidden bg-ttp19-bg px-6 py-[240px] font-ttp19-sans before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:bg-[radial-gradient(ellipse_60%_50%_at_50%_50%,rgba(80,40,120,0.08)_0%,transparent_70%)]">
  <div class="relative mx-auto max-w-[760px] py-10 before:content-[''] before:absolute before:inset-x-0 before:top-1/2 before:h-px before:-translate-y-1/2 before:bg-[linear-gradient(to_right,transparent,rgba(120,80,200,0.35)_10%,rgba(120,80,200,0.35)_90%,transparent)]">
    <div class="relative flex items-center justify-between">

      <div class="ttp19-ev group"><span class="ttp19-label">Seed Round</span><button type="button" aria-describedby="ttp19-e1" aria-label="2018, seed funding closed" class="ttp19-dot"></button><span class="ttp19-year">2018</span>
        <div id="ttp19-e1" role="tooltip" class="ttp19-card">
          <div class="ttp19-ctop"><div class="ttp19-cq">Q3 · 2018</div><div class="ttp19-ct">Seed Funding Closed</div><span class="ttp19-badge border-ttp19-mile/30 bg-ttp19-mile/15 text-ttp19-mile">Milestone</span></div>
          <p class="ttp19-body">$2.4M raised from 12 angel investors. The round was led by two former founders from the enterprise SaaS sector, providing both capital and key industry connections.</p>
          <div class="ttp19-impact"><span class="text-ttp19-dim">Runway</span><span class="text-ttp19-val">18 months secured</span></div>
        </div>
      </div>

      <div class="ttp19-ev group"><span class="ttp19-label">Public Beta</span><button type="button" aria-describedby="ttp19-e2" aria-label="2019, public beta launch" class="ttp19-dot"></button><span class="ttp19-year">2019</span>
        <div id="ttp19-e2" role="tooltip" class="ttp19-card">
          <div class="ttp19-ctop"><div class="ttp19-cq">Q1 · 2019</div><div class="ttp19-ct">Public Beta Launch</div><span class="ttp19-badge border-ttp19-prod/30 bg-ttp19-prod/15 text-ttp19-prod">Product</span></div>
          <p class="ttp19-body">First 1,000 paying customers acquired within 90 days. Net Promoter Score of 72 in initial surveys. Product-market fit validated across legal, healthcare and fintech.</p>
          <div class="ttp19-impact"><span class="text-ttp19-dim">ARR at launch</span><span class="text-ttp19-val">$480K</span></div>
        </div>
      </div>

      <div class="ttp19-ev group"><span class="ttp19-label">Series A</span><button type="button" aria-describedby="ttp19-e3" aria-label="2020, Series A" class="ttp19-dot"></button><span class="ttp19-year">2020</span>
        <div id="ttp19-e3" role="tooltip" class="ttp19-card">
          <div class="ttp19-ctop"><div class="ttp19-cq">Q2 · 2020</div><div class="ttp19-ct">Series A — $12M</div><span class="ttp19-badge border-ttp19-mile/30 bg-ttp19-mile/15 text-ttp19-mile">Milestone</span></div>
          <p class="ttp19-body">$12M Series A led by a top-tier growth fund. The round closed despite pandemic uncertainty, reflecting strong retention. Funds used to double engineering headcount.</p>
          <div class="ttp19-impact"><span class="text-ttp19-dim">Post-money</span><span class="text-ttp19-val">$68M</span></div>
        </div>
      </div>

      <div class="ttp19-ev group"><span class="ttp19-label">EU Expansion</span><button type="button" aria-describedby="ttp19-e4" aria-label="2021, EU launch" class="ttp19-dot"></button><span class="ttp19-year">2021</span>
        <div id="ttp19-e4" role="tooltip" class="ttp19-card">
          <div class="ttp19-ctop"><div class="ttp19-cq">Q3 · 2021</div><div class="ttp19-ct">100K Users · EU Launch</div><span class="ttp19-badge border-ttp19-prod/30 bg-ttp19-prod/15 text-ttp19-prod">Growth</span></div>
          <p class="ttp19-body">Crossed 100,000 active users and launched GDPR-compliant EU data centres in Frankfurt and Dublin. Opened a London office with 24 hires. MRR surpassed $1M.</p>
          <div class="ttp19-impact"><span class="text-ttp19-dim">EU share</span><span class="text-ttp19-val">31% of new ARR</span></div>
        </div>
      </div>

      <div class="ttp19-ev group"><span class="ttp19-label">Series B</span><button type="button" aria-describedby="ttp19-e5" aria-label="2022, Series B" class="ttp19-dot"></button><span class="ttp19-year">2022</span>
        <div id="ttp19-e5" role="tooltip" class="ttp19-card">
          <div class="ttp19-ctop"><div class="ttp19-cq">Q1 · 2022</div><div class="ttp19-ct">Series B — $45M · Profitable</div><span class="ttp19-badge border-ttp19-mile/30 bg-ttp19-mile/15 text-ttp19-mile">Milestone</span></div>
          <p class="ttp19-body">$45M Series B led by a multi-stage venture firm. Achieved the first profitable quarter ahead of schedule. Capital allocated to enterprise sales infrastructure.</p>
          <div class="ttp19-impact"><span class="text-ttp19-dim">Valuation</span><span class="text-ttp19-val">$320M post-money</span></div>
        </div>
      </div>

      <div class="ttp19-ev group"><span class="ttp19-label">Acquisition</span><button type="button" aria-describedby="ttp19-e6" aria-label="2023, acquisition" class="ttp19-dot"></button><span class="ttp19-year">2023</span>
        <div id="ttp19-e6" role="tooltip" class="ttp19-card">
          <div class="ttp19-ctop"><div class="ttp19-cq">Q2 · 2023</div><div class="ttp19-ct">Acquired Synapse Labs</div><span class="ttp19-badge border-ttp19-acq/30 bg-ttp19-acq/15 text-ttp19-acq">M&amp;A</span></div>
          <p class="ttp19-body">Acquired Synapse Labs, a 22-person AI workflow automation startup, for $280M. The deal added Synapse's orchestration layer, accelerating the roadmap by an estimated 18 months.</p>
          <div class="ttp19-impact"><span class="text-ttp19-dim">ARR added</span><span class="text-ttp19-val">$8.4M</span></div>
        </div>
      </div>

      <div class="ttp19-ev group"><span class="ttp19-label">IPO Filed</span><button type="button" aria-describedby="ttp19-e7" aria-label="2024, IPO filed" class="ttp19-dot"></button><span class="ttp19-year">2024</span>
        <div id="ttp19-e7" role="tooltip" class="ttp19-card">
          <div class="ttp19-ctop"><div class="ttp19-cq">Q3 · 2024</div><div class="ttp19-ct">S-1 Filed · NASDAQ</div><span class="ttp19-badge border-ttp19-ipo/30 bg-ttp19-ipo/15 text-ttp19-ipo">Public Markets</span></div>
          <p class="ttp19-body">Filed the S-1 registration with the SEC. The IPO priced at $18 per share, valuing the company at $1.2B; shares closed up 38% on day one.</p>
          <div class="ttp19-impact"><span class="text-ttp19-dim">Market cap</span><span class="text-ttp19-val">$1.65B (day 1)</span></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp19-bg: #0e0c14;
  --color-ttp19-bg: oklch(0.16 0.02 300);
  --color-ttp19-acc: #9a6ee8;
  --color-ttp19-acc: oklch(0.65 0.16 295);
  --color-ttp19-val: #cba8ff;
  --color-ttp19-val: oklch(0.8 0.12 295);
  --color-ttp19-dim: #9b8bc0;
  --color-ttp19-dim: oklch(0.67 0.06 295);
  --color-ttp19-ink: #ded9ea;
  --color-ttp19-ink: oklch(0.89 0.02 295);
  --color-ttp19-mile: #7cd07c;
  --color-ttp19-mile: oklch(0.79 0.15 145);
  --color-ttp19-prod: #86b4f5;
  --color-ttp19-prod: oklch(0.76 0.12 255);
  --color-ttp19-acq: #f0a44f;
  --color-ttp19-acq: oklch(0.77 0.14 65);
  --color-ttp19-ipo: #d08af0;
  --color-ttp19-ipo: oklch(0.74 0.16 315);
  --font-ttp19-sans: 'Inter', system-ui, sans-serif;
  --font-ttp19-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttp19-serif: Georgia, 'Times New Roman', serif;
}

.ttp-19 {
  width: 100%;
  min-height: 100svh;
}
/* Seven events, one card. The odd/even flip is genuinely structural,
   so it stays as two nth-child rules rather than a contorted variant. */

.ttp-19 .ttp19-ev {
  @apply relative flex cursor-help flex-col items-center odd:flex-col-reverse;
}

.ttp-19 .ttp19-label {
  @apply my-2.75 text-center font-ttp19-mono text-[9.5px] tracking-[0.08em] text-ttp19-dim;
}

.ttp-19 .ttp19-year {
  @apply my-2.75 text-center font-ttp19-mono text-[11px] font-bold tracking-[0.04em] text-ttp19-val;
}

.ttp-19 .ttp19-dot {
  @apply relative z-2 h-2.75 w-2.75 shrink-0 cursor-help rounded-full border-2 border-ttp19-acc/40 bg-ttp19-acc/70 p-0 transition-[background,box-shadow,transform] duration-150 group-hover:scale-130 group-hover:bg-ttp19-acc group-hover:shadow-[0_0_14px_4px_rgba(120,80,200,0.25)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ttp19-acc;
}

.ttp-19 .ttp19-card {
  @apply pointer-events-none invisible absolute left-1/2 z-50 w-[250px] max-w-[calc(100vw-48px)] -translate-x-1/2 -translate-y-1.5 overflow-hidden rounded-[10px] border border-ttp19-acc/25 bg-ttp19-bg/97 text-left opacity-0 shadow-[0_16px_44px_rgba(0,0,0,0.9),0_0_0_1px_rgba(120,80,200,0.08)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100;
}

.ttp-19 .ttp19-ev:nth-child(odd) .ttp19-card {
  bottom: calc(100% + 10px);
  top: auto;
}

.ttp-19 .ttp19-ev:nth-child(even) .ttp19-card {
  top: calc(100% + 10px);
  bottom: auto;
}
/* The rail's outer two events sit at the section edges, so a centred
   250px card would hang ~125px past them. Anchor them to their own
   edge instead; --tw-translate-x is nulled rather than the whole
   translate property, so the reveal's y-shift still animates. */

.ttp-19 .ttp19-ev:first-child .ttp19-card {
  left: 0;
  --tw-translate-x: 0;
}

.ttp-19 .ttp19-ev:last-child .ttp19-card {
  left: auto;
  right: 0;
  --tw-translate-x: 0;
}

.ttp-19 .ttp19-ctop {
  @apply border-b border-ttp19-acc/15 px-3.25 pt-3 pb-2.5;
}

.ttp-19 .ttp19-cq {
  @apply mb-1 font-ttp19-mono text-[9.5px] tracking-[0.1em] text-ttp19-dim;
}

.ttp-19 .ttp19-ct {
  @apply font-ttp19-serif text-[13px] leading-snug text-ttp19-ink;
}

.ttp-19 .ttp19-badge {
  @apply mt-1.75 inline-block rounded-[3px] border px-1.75 py-0.5 font-ttp19-mono text-[8.5px] uppercase tracking-[0.07em];
}

.ttp-19 .ttp19-body {
  @apply m-0 border-b border-ttp19-acc/10 px-3.25 py-2.25 font-ttp19-serif text-[11.5px] italic leading-[1.55] text-ttp19-ink/85;
}

.ttp-19 .ttp19-impact {
  @apply flex justify-between gap-2 px-3.25 py-2.25 font-ttp19-mono text-[10px];
}
```
