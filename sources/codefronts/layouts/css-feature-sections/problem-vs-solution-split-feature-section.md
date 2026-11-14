---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/problem-vs-solution-split-feature-section/"
title: "Problem vs Solution Split Feature Section"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "The before-and-after argument, laid out as two columns with a centred divider: pain points on the left in a muted red wash, the matching wins on the right in…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Problem vs Solution Split Feature Section
Source: https://codefronts.com/layouts/css-feature-sections/problem-vs-solution-split-feature-section/

The before-and-after argument, laid out as two columns with a centred divider: pain points on the left in a muted red wash, the matching wins on the right in green, paired line for line so the eye reads across. Tints are generated with color-mix in oklab from two seed hues, which means one variable swap re-themes the whole comparison without hand-mixing a dozen backgrounds.
## HTML
```html
<section class="fs-04" aria-labelledby="fs-04-heading">
  <div class="fs-04__hero" aria-hidden="true">
    <span class="fs-04__wordmark">VALE</span>
    <span class="fs-04__heronav">Platform / Connectors / Docs</span>
  </div>

  <div class="fs-04__stage">
    <div class="fs-04__head">
      <p class="fs-04__eyebrow">The switch</p>
      <h2 class="fs-04__heading" id="fs-04-heading">Hand-rolled pipelines, or pipelines you stop thinking about</h2>
      <p class="fs-04__sub">Four things every data team we talk to is doing manually, and what Vale does with them instead.</p>
    </div>

    <div class="fs-04__split">
      <div class="fs-04__col fs-04__col--bad">
        <h3 class="fs-04__colhead"><span class="fs-04__tag">Today</span> Running it yourself</h3>
        <ul class="fs-04__list">
          <li class="fs-04__item"><span class="fs-04__glyph" aria-hidden="true">✕</span><b>Manual data pipes</b><span>Someone owns a cron job, a bash script and a folder of one-off backfills nobody else can read.</span></li>
          <li class="fs-04__item"><span class="fs-04__glyph" aria-hidden="true">✕</span><b>Silent failures</b><span>A source changes a column type on Friday, the dashboard is wrong all weekend, and finance finds it first.</span></li>
          <li class="fs-04__item"><span class="fs-04__glyph" aria-hidden="true">✕</span><b>Schema drift by surprise</b><span>Every new field is a migration ticket, and the staging warehouse is three schemas behind production.</span></li>
          <li class="fs-04__item"><span class="fs-04__glyph" aria-hidden="true">✕</span><b>Backfills that take the night</b><span>Reprocessing a quarter means blocking the warehouse and telling analysts to come back tomorrow.</span></li>
        </ul>
      </div>

      <div class="fs-04__divider" aria-hidden="true">
        <span class="fs-04__badge">
          <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 10h13M11 5l5 5-5 5"/></svg>
        </span>
      </div>

      <div class="fs-04__col fs-04__col--good">
        <h3 class="fs-04__colhead"><span class="fs-04__tag">With Vale</span> Managed by contract</h3>
        <ul class="fs-04__list">
          <li class="fs-04__item"><span class="fs-04__glyph" aria-hidden="true">✓</span><b>Declared sources</b><span>Every pipe is a versioned declaration in your repo, reviewed like code and reproducible from empty.</span></li>
          <li class="fs-04__item"><span class="fs-04__glyph" aria-hidden="true">✓</span><b>Loud, owned alerts</b><span>A type change pages the dataset owner in ninety seconds with the offending rows attached.</span></li>
          <li class="fs-04__item"><span class="fs-04__glyph" aria-hidden="true">✓</span><b>Auto-detected schemas</b><span>New fields land typed and nullable, with a diff to approve — no migration ticket, no drift.</span></li>
          <li class="fs-04__item"><span class="fs-04__glyph" aria-hidden="true">✓</span><b>Backfills off the hot path</b><span>Reprocess a quarter into a shadow table and swap it in when it matches. Analysts never notice.</span></li>
        </ul>
      </div>
    </div>

    <p class="fs-04__foot">Migrating from an in-house loader? <a class="fs-04__link" href="#fs-04-heading">Read the two-week cutover plan</a></p>
  </div>

  <div class="fs-04__below" aria-hidden="true">Compare plans · Talk to an engineer</div>
</section>
```
## CSS
```css
.fs-04 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --surface: #ffffff;
  --page: #f4f5f7;
  --page: oklch(0.965 0.003 260);
  --ink: #14181f;
  --ink: oklch(0.21 0.012 260);
  --muted: #5d6674;
  --muted: oklch(0.51 0.017 260);
  --rule: #d9dde4;
  --rule: oklch(0.88 0.008 260);
  --bad: #c2372f;
  --bad: oklch(0.53 0.18 27);
  --good: #1d7a4c;
  --good: oklch(0.5 0.13 155);
  --tint: 7%;
  --divider: 1px;
  --font-display: "Avenir Next Condensed", "Haettenschweiler", "Arial Narrow", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-04 *,
.fs-04 *::before,
.fs-04 *::after {
  box-sizing: border-box;
}

.fs-04__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 16px 20px;
  background: var(--surface);
  border-block-end: 1px solid var(--rule);
}

.fs-04__wordmark {
  font: 700 15px/1 var(--font-display);
  letter-spacing: 0.14em;
}

.fs-04__heronav {
  font-size: 12px;
  color: var(--muted);
}

.fs-04__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 6vw, 64px) 16px;
}

.fs-04__head {
  inline-size: 100%;
  max-inline-size: 68rem;
  min-inline-size: 0;
  margin: 0 0 clamp(24px, 4vw, 40px);
}

.fs-04__eyebrow {
  margin: 0 0 10px;
  font: 700 11px/1 var(--font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
}

.fs-04__heading {
  margin: 0 0 10px;
  max-inline-size: 34ch;
  font: 700 clamp(27px, 5.2vw, 44px)/1.05 var(--font-display);
  letter-spacing: 0.005em;
  text-wrap: balance;
}

.fs-04__sub {
  margin: 0;
  max-inline-size: 56ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-04__split {
  inline-size: 100%;
  max-inline-size: 68rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr);
  gap: clamp(14px, 2.6vw, 30px);
  background: var(--surface);
  border: 1px solid var(--rule);
  padding: clamp(16px, 3vw, 30px);
}

.fs-04__col {
  min-inline-size: 0;
}

.fs-04__colhead {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 8px;
  margin: 0 0 16px;
  padding-block-end: 12px;
  border-block-end: 1px solid var(--rule);
  font: 700 clamp(15px, 2vw, 18px)/1.2 var(--font-display);
  letter-spacing: 0.02em;
}

.fs-04__tag {
  padding: 3px 8px;
  font: 700 10px/1.3 system-ui, sans-serif;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  border-radius: 2px;
}

.fs-04__col--bad .fs-04__tag {
  color: #8d2620;
  color: color-mix(in oklab, var(--bad) 78%, black);
  background: #f7e4e2;
  background: color-mix(in oklab, var(--bad) 12%, var(--surface));
}

.fs-04__col--good .fs-04__tag {
  color: #145636;
  color: color-mix(in oklab, var(--good) 78%, black);
  background: #e2f1e9;
  background: color-mix(in oklab, var(--good) 12%, var(--surface));
}

.fs-04__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 10px;
}

.fs-04__item {
  display: grid;
  grid-template-columns: 22px minmax(0, 1fr);
  gap: 4px 10px;
  align-items: start;
  min-block-size: 92px;
  padding: 13px 14px;
  border-inline-start: 3px solid;
}

.fs-04__item b {
  grid-column: 2;
  font-size: 14px;
  font-weight: 650;
  letter-spacing: -0.01em;
}

.fs-04__item span:last-child {
  grid-column: 2;
  font-size: 13px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-04__glyph {
  grid-row: span 2;
  font-size: 15px;
  font-weight: 700;
  line-height: 1.2;
}

.fs-04__col--bad .fs-04__item {
  background: #fbf1f0;
  background: color-mix(in oklab, var(--bad) var(--tint), var(--surface));
  border-color: #d9756c;
  border-color: color-mix(in oklab, var(--bad) 45%, var(--surface));
}

.fs-04__col--bad .fs-04__glyph {
  color: #a92e26;
  color: color-mix(in oklab, var(--bad) 85%, black);
}

.fs-04__col--good .fs-04__item {
  background: #eef7f2;
  background: color-mix(in oklab, var(--good) var(--tint), var(--surface));
  border-color: #6bad8c;
  border-color: color-mix(in oklab, var(--good) 45%, var(--surface));
}

.fs-04__col--good .fs-04__glyph {
  color: #166540;
  color: color-mix(in oklab, var(--good) 85%, black);
}

.fs-04__divider {
  position: relative;
  inline-size: var(--divider);
  background: linear-gradient(180deg, transparent, var(--rule) 12%, var(--rule) 88%, transparent);
  display: grid;
  place-items: center;
}

.fs-04__badge {
  position: sticky;
  inset-block-start: 50%;
  display: grid;
  place-items: center;
  inline-size: 38px;
  block-size: 38px;
  border-radius: 50%;
  color: var(--surface);
  background: var(--ink);
  border: 3px solid var(--surface);
}

.fs-04__foot {
  inline-size: 100%;
  max-inline-size: 68rem;
  margin: 18px 0 0;
  font-size: 13.5px;
  color: var(--muted);
}

.fs-04__link {
  color: var(--good);
  color: color-mix(in oklab, var(--good) 88%, black);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
}

.fs-04__link:hover {
  color: var(--ink);
}

.fs-04__link:focus-visible {
  outline: 2px solid var(--good);
  outline-offset: 3px;
  border-radius: 2px;
}

.fs-04__below {
  padding: 16px 20px;
  background: var(--surface);
  border-block-start: 1px solid var(--rule);
  font-size: 12px;
  color: var(--muted);
}

@media (max-width: 780px) {
  .fs-04__split {
    grid-template-columns: minmax(0, 1fr);
  }

  .fs-04__divider {
    inline-size: auto;
    block-size: var(--divider);
    background: linear-gradient(90deg, transparent, var(--rule) 12%, var(--rule) 88%, transparent);
  }

  .fs-04__badge {
    position: static;
    transform: rotate(90deg);
  }

  .fs-04__item {
    min-block-size: 0;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-04 {
    --surface: #171b21;
    --page: #101318;
    --ink: #eef1f5;
    --muted: #97a1b0;
    --rule: #2a2f38;
    --bad: #f08c82;
    --good: #6fd39f;
    --tint: 12%;
  }

  .fs-04__badge {
    color: #101318;
    background: var(--ink);
    border-color: var(--surface);
  }

  .fs-04__col--bad .fs-04__glyph,
    .fs-04__col--good .fs-04__glyph,
    .fs-04__link {
    color: inherit;
  }

  .fs-04__col--bad .fs-04__glyph {
    color: var(--bad);
  }

  .fs-04__col--good .fs-04__glyph {
    color: var(--good);
  }

  .fs-04__link {
    color: var(--good);
  }

  .fs-04__col--bad .fs-04__tag {
    color: #ffd9d3;
    background: color-mix(in oklab, var(--bad) 22%, var(--surface));
  }

  .fs-04__col--good .fs-04__tag {
    color: #d5f6e4;
    background: color-mix(in oklab, var(--good) 22%, var(--surface));
  }
}

[data-theme="dark"] .fs-04 {
  --surface: #171b21;
  --page: #101318;
  --ink: #eef1f5;
  --muted: #97a1b0;
  --rule: #2a2f38;
  --bad: #f08c82;
  --good: #6fd39f;
  --tint: 12%;
}

[data-theme="dark"] .fs-04 .fs-04__badge {
  color: #101318;
  background: var(--ink);
  border-color: var(--surface);
}

[data-theme="dark"] .fs-04 .fs-04__link {
  color: var(--good);
}
```
