---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/case-study-blog-post-layout/"
title: "Case Study Blog Post Layout"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A case-study page that earns its claims: stat counters that count up on scroll using @property + a scroll-driven animation (yes, animated numbers with no…"
has_js: "true"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Case Study Blog Post Layout
Source: https://codefronts.com/layouts/css-blog-layouts/case-study-blog-post-layout/

A case-study page that earns its claims: stat counters that count up on scroll using @property + a scroll-driven animation (yes, animated numbers with no JavaScript), a draggable before/after image comparison built on clip-path and a range input, and testimonials that don't look like a template.
## HTML
```html
<article class="bl-12">
  <header class="bl-12__head">
    <div class="bl-12__headText">
      <p class="bl-12__rubric">Case study · Performance</p>
      <h1>How Northwind cut checkout abandonment by a third in eleven weeks</h1>
      <p class="bl-12__standfirst">A 40-year-old catalogue retailer, a checkout nobody had touched since 2019, and a rebuild constrained to the existing backend. No redesign of the brand, no new platform.</p>
      <dl class="bl-12__facts">
        <div><dt>Client</dt><dd>Northwind Supply Co.</dd></div>
        <div><dt>Scope</dt><dd>Checkout &amp; payments UX</dd></div>
        <div><dt>Duration</dt><dd>11 weeks</dd></div>
        <div><dt>Team</dt><dd>2 design, 3 engineering</dd></div>
      </dl>
    </div>
    <figure class="bl-12__headFig">
      <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=900&amp;q=70&amp;auto=format&amp;fit=crop" alt="Warehouse shelving with packed orders ready to ship" width="900" height="1100" loading="eager" decoding="async">
    </figure>
  </header>

  <section class="bl-12__stats" aria-label="Results">
    <div class="bl-12__stat"><b style="--to:34"><span class="bl-12__srOnly">34</span></b><i>%</i><p>fewer abandoned carts</p></div>
    <div class="bl-12__stat"><b style="--to:2"><span class="bl-12__srOnly">2</span></b><i>.4×</i><p>faster median checkout</p></div>
    <div class="bl-12__stat"><b style="--to:247"><span class="bl-12__srOnly">247</span></b><i>k</i><p>additional annual orders</p></div>
    <div class="bl-12__stat"><b style="--to:11"><span class="bl-12__srOnly">11</span></b><i>wks</i><p>from kickoff to full rollout</p></div>
  </section>

  <div class="bl-12__body">
    <section class="bl-12__block">
      <h2>The problem was never the design</h2>
      <p>Northwind's checkout converted at less than half the industry median, and every previous attempt to fix it had started with a visual refresh. The analytics said something duller: 61% of drop-off happened on a single step, and 80% of that step's traffic was mobile.</p>
      <p>The step in question asked for a purchase-order number, a delivery window and a VAT ID on one screen, with validation that only ran on submit. Nothing about it was ugly. It was simply asking three unrelated questions at once and punishing you for guessing.</p>
    </section>

    <section class="bl-12__block bl-12__block--wide">
      <h2>Before and after</h2>
      <p class="bl-12__blockLede">Same brand, same backend, same three data points — collected across three steps with inline validation instead of one screen with a wall of errors.</p>
      <div class="bl-12__compare" style="--pos:52">
        <div class="bl-12__pane">
          <img class="bl-12__before" src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&amp;q=70&amp;auto=format&amp;fit=crop" alt="The previous checkout screen, dense with fields" width="1200" height="750" loading="lazy" decoding="async">
          <img class="bl-12__after" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&amp;q=70&amp;auto=format&amp;fit=crop" alt="The rebuilt checkout, split into three steps" width="1200" height="750" loading="lazy" decoding="async">
          <span class="bl-12__tagBefore" aria-hidden="true">Before</span>
          <span class="bl-12__tagAfter" aria-hidden="true">After</span>
          <span class="bl-12__handle" aria-hidden="true"></span>
        </div>
        <label class="bl-12__sliderLabel" for="bl-12-range">Reveal the redesigned checkout</label>
        <input class="bl-12__range" id="bl-12-range" type="range" min="0" max="100" value="52" data-range aria-describedby="bl-12-range-hint">
        <p class="bl-12__rangeHint" id="bl-12-range-hint">Drag, or use the arrow keys, to compare the two versions.</p>
      </div>
    </section>

    <section class="bl-12__block">
      <h2>What we actually changed</h2>
      <ol class="bl-12__list">
        <li><strong>Split the step into three.</strong> One question per screen on mobile, with the summary always visible. Completion rate on the problem step went from 39% to 71%.</li>
        <li><strong>Validated on blur, not on submit.</strong> The VAT field now checks format as you leave it and explains the expected shape before you are wrong.</li>
        <li><strong>Deferred the purchase-order number.</strong> 78% of buyers didn't have one to hand; it is now collected after payment, by email, which removed the single largest stall point.</li>
        <li><strong>Kept the old backend.</strong> Every change shipped behind a flag against the existing API. No migration, no freeze, no risk story to sell upward.</li>
      </ol>
    </section>

    <section class="bl-12__block bl-12__block--wide">
      <h2>What the client said</h2>
      <div class="bl-12__quotes">
        <figure class="bl-12__testimonial">
          <blockquote><p>“The first prototype we tested was uglier than what we had. It converted 18% better. That reframed the entire project internally.”</p></blockquote>
          <figcaption><img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=100&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="100" height="100" loading="lazy" decoding="async"><span><strong>Jonas Wren</strong>Head of E-commerce, Northwind</span></figcaption>
        </figure>
        <figure class="bl-12__testimonial">
          <blockquote><p>“They spent the first fortnight reading our support tickets instead of designing. Every recommendation after that was impossible to argue with.”</p></blockquote>
          <figcaption><img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=100&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="100" height="100" loading="lazy" decoding="async"><span><strong>Priya Raman</strong>Customer Operations Lead</span></figcaption>
        </figure>
      </div>
    </section>

    <section class="bl-12__block">
      <h2>Measured, eleven weeks after rollout</h2>
      <table class="bl-12__table">
        <caption>Checkout funnel, 30-day rolling average</caption>
        <thead><tr><th scope="col">Metric</th><th scope="col">Before</th><th scope="col">After</th><th scope="col">Δ</th></tr></thead>
        <tbody>
          <tr><th scope="row">Cart → order</th><td>21.4%</td><td>32.1%</td><td data-good>+50%</td></tr>
          <tr><th scope="row">Median time to pay</th><td>4m 12s</td><td>1m 44s</td><td data-good>−59%</td></tr>
          <tr><th scope="row">Support tickets / 1k orders</th><td>18.2</td><td>6.9</td><td data-good>−62%</td></tr>
          <tr><th scope="row">Mobile share of orders</th><td>34%</td><td>51%</td><td data-good>+17pt</td></tr>
        </tbody>
      </table>
      <p class="bl-12__footnote">Measured against the same 30-day window in the prior year to control for seasonality. Full methodology available on request.</p>
    </section>
  </div>
</article>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Newsreader:opsz,[email protected],300;6..72,400&display=swap');

@property --n {
  syntax: "<integer>";
  initial-value: 0;
  inherits: false;
}

.bl-12 {
  --bg: #f7f7f5;
  --surface: #ffffff;
  --text: #111214;
  --muted: #63676e;
  --line: #e3e3df;
  --acc: #1e40af;
  --good: #15803d;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-12 {
    --bg: oklch(97.5% .003 100);
    --surface: oklch(100% 0 0);
    --text: oklch(16% .008 265);
    --muted: oklch(50% .012 265);
    --line: oklch(90% .005 100);
    --acc: oklch(40% .18 265);
    --good: oklch(50% .14 148);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-12:not([data-theme="light"]) {
    --bg: #0b0c0e;
    --surface: #14161a;
    --text: #f0f1f3;
    --muted: #989ea8;
    --line: #232630;
    --acc: #8fb0ff;
    --good: #5cd68f;
  }
}

.bl-12[data-theme="dark"] {
  --bg: #0b0c0e;
  --surface: #14161a;
  --text: #f0f1f3;
  --muted: #989ea8;
  --line: #232630;
  --acc: #8fb0ff;
  --good: #5cd68f;
}

.bl-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-12,
.bl-12 *,
.bl-12 *::before,
.bl-12 *::after {
  box-sizing: border-box;
}

.bl-12 a {
  color: inherit;
}

.bl-12 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 3px;
}

.bl-12 img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--line);
}

.bl-12__srOnly {
  position: static;
  width: auto;
  height: auto;
  overflow: visible;
  clip-path: none;
}

.bl-12__head {
  display: grid;
  grid-template-columns: minmax(0,1.5fr) minmax(0,1fr);
  gap: clamp(1.5rem,4vw,3.5rem);
  align-items: center;
  max-width: 80rem;
  margin-inline: auto;
  padding: clamp(2.5rem,6vw,5rem) clamp(1.25rem,4vw,3rem) clamp(2rem,4vw,3rem);
}

.bl-12__headText {
  display: grid;
  gap: 1.15rem;
}

.bl-12__rubric {
  margin: 0;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-12__head h1 {
  margin: 0;
  font-size: clamp(1.875rem,4.6vw,3.25rem);
  font-weight: 800;
  line-height: 1.03;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.bl-12__standfirst {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(1.0625rem,1.9vw,1.3125rem);
  line-height: 1.6;
  color: var(--muted);
  max-width: 56ch;
  text-wrap: pretty;
}

.bl-12__facts {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(8rem,1fr));
  gap: 1rem;
  margin: .5rem 0 0;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
}

.bl-12__facts div {
  display: grid;
  gap: .2rem;
}

.bl-12__facts dt {
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-12__facts dd {
  margin: 0;
  font-size: .9375rem;
  font-weight: 600;
}

.bl-12__headFig {
  margin: 0;
  aspect-ratio: 4/5;
  border-radius: 1rem;
  overflow: hidden;
}

.bl-12__stats {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,11rem),1fr));
  gap: 1px;
  max-width: 80rem;
  margin-inline: auto;
  padding: 0 clamp(1.25rem,4vw,3rem);
  background: var(--line);
  border-block: 1px solid var(--line);
}

.bl-12__stat {
  display: grid;
  gap: .35rem;
  padding: clamp(1.25rem,3vw,2rem) clamp(1rem,2vw,1.5rem);
  background: var(--bg);
  align-content: start;
}

.bl-12__stat b {
  display: inline;
  font-size: clamp(2.25rem,5vw,3.5rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
  color: var(--acc);
}

.bl-12__stat i {
  font-style: normal;
  font-size: clamp(1.25rem,2.4vw,1.75rem);
  font-weight: 700;
  letter-spacing: -.03em;
  color: var(--acc);
}

.bl-12__stat p {
  margin: .35rem 0 0;
  font-size: .875rem;
  line-height: 1.45;
  color: var(--muted);
  text-wrap: pretty;
}
/* The number itself is real text in .bl-12__srOnly — always correct, always
   selectable, always announced. A CSS-only count-up is deliberately NOT used
   here: counter-reset ignores @property-registered custom properties in
   Chromium, and registration is what makes a value animatable, so the
   animated-counter trick paints 0 in every state. A correct static number
   beats a broken animated one. */

@media (prefers-reduced-motion: no-preference) {
  .bl-12__stat b {
    animation: bl-12-rise .7s cubic-bezier(.16,1,.3,1) both;
    animation-timeline: view();
    animation-range: entry 10% cover 30%;
  }

  @keyframes bl-12-rise {
    from {
      opacity: 0;
      translate: 0 .35rem;
    }

    to {
      opacity: 1;
      translate: 0 0;
    }
  }
}

.bl-12__body {
  overflow-x: clip;
  display: grid;
  gap: clamp(2rem,4vw,3.5rem);
  grid-template-columns: [wide-start] minmax(1.25rem,1fr) [narrow-start] min(66ch,100% - 2.5rem) [narrow-end] minmax(1.25rem,1fr) [wide-end];
  max-width: min(80rem,100%);
  margin-inline: auto;
  padding-block: clamp(2.5rem,5vw,4rem) clamp(4rem,9vw,7rem);
}

.bl-12__block {
  grid-column: narrow;
  min-width: 0;
  display: grid;
  gap: 1rem;
}

.bl-12__block--wide {
  grid-column: wide;
  min-width: 0;
  max-width: min(74rem,100%);
  margin-inline: auto;
}

.bl-12__block h2 {
  margin: 0;
  font-size: clamp(1.375rem,2.8vw,1.875rem);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -.028em;
  text-wrap: balance;
}

.bl-12__block p {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.125rem;
  line-height: 1.72;
  text-wrap: pretty;
}

.bl-12__blockLede {
  color: var(--muted);
  max-width: 62ch;
}

.bl-12__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .85rem;
  counter-reset: bl-12-li;
}

.bl-12__list li {
  counter-increment: bl-12-li;
  position: relative;
  padding-inline-start: 2.6rem;
  font-family: var(--serif);
  font-size: 1.0625rem;
  line-height: 1.7;
  text-wrap: pretty;
}

.bl-12__list li::before {
  content: counter(bl-12-li);
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: .15rem;
  display: grid;
  place-items: center;
  width: 1.75rem;
  height: 1.75rem;
  border-radius: 50%;
  background: color-mix(in oklab,var(--acc) 14%,transparent);
  color: var(--acc);
  font-family: var(--sans);
  font-size: .75rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.bl-12__list strong {
  font-family: var(--sans);
  font-weight: 700;
}

.bl-12__compare {
  display: grid;
  gap: .75rem;
}

.bl-12__pane {
  position: relative;
  aspect-ratio: 16/10;
  border-radius: 1rem;
  overflow: hidden;
  background: var(--line);
}

.bl-12__pane img {
  position: absolute;
  inset: 0;
}

.bl-12__after {
  clip-path: inset(0 0 0 calc(var(--pos,50) * 1%));
}

.bl-12__handle {
  position: absolute;
  inset-block: 0;
  inset-inline-start: calc(var(--pos,50) * 1%);
  width: 2px;
  translate: -1px 0;
  background: #fff;
  box-shadow: 0 0 0 1px rgba(0,0,0,.25);
}

.bl-12__handle::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  translate: -50% -50%;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 .5rem 1.25rem rgba(0,0,0,.3);
}

.bl-12__tagBefore,
.bl-12__tagAfter {
  position: absolute;
  inset-block-start: .75rem;
  padding: .3rem .6rem;
  border-radius: 999px;
  background: rgba(12,14,18,.72);
  color: #fff;
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.bl-12__tagBefore {
  inset-inline-start: .75rem;
}

.bl-12__tagAfter {
  inset-inline-end: .75rem;
}

.bl-12__sliderLabel {
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-12__range {
  width: 100%;
  min-height: 2.75rem;
  accent-color: var(--acc);
  cursor: ew-resize;
}

.bl-12__rangeHint {
  margin: 0;
  font-family: var(--sans) !important;
  font-size: .8125rem !important;
  color: var(--muted);
}

.bl-12__quotes {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,20rem),1fr));
  gap: 1.25rem;
}

.bl-12__testimonial {
  margin: 0;
  display: grid;
  gap: 1.1rem;
  padding: clamp(1.25rem,3vw,2rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
}

.bl-12__testimonial blockquote {
  margin: 0;
}

.bl-12__testimonial blockquote p {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(1.125rem,2.2vw,1.375rem);
  line-height: 1.5;
  font-weight: 300;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.bl-12__testimonial figcaption {
  display: flex;
  align-items: center;
  gap: .7rem;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
}

.bl-12__testimonial figcaption img {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  flex: 0 0 auto;
}

.bl-12__testimonial figcaption span {
  display: grid;
  font-size: .8125rem;
  color: var(--muted);
}

.bl-12__testimonial figcaption strong {
  font-size: .875rem;
  font-weight: 700;
  color: var(--text);
}

.bl-12__table {
  width: 100%;
  border-collapse: collapse;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
}

.bl-12__table caption {
  text-align: start;
  padding-bottom: .75rem;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-12__table th,
.bl-12__table td {
  padding: .75rem .5rem;
  text-align: end;
  border-bottom: 1px solid var(--line);
}

.bl-12__table thead th {
  font-size: .6875rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
}

.bl-12__table th:first-child,
.bl-12__table td:first-child,
.bl-12__table tbody th {
  text-align: start;
  font-weight: 600;
}

.bl-12__table td[data-good] {
  color: var(--good);
  font-weight: 700;
}

.bl-12__footnote {
  font-family: var(--sans) !important;
  font-size: .8125rem !important;
  line-height: 1.6 !important;
  color: var(--muted);
}

@media (max-width: 60rem) {
  .bl-12__head {
    grid-template-columns: minmax(0,1fr);
  }

  .bl-12__headFig {
    aspect-ratio: 16/9;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-12 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .bl-12__handle {
    background: CanvasText;
  }

  .bl-12__testimonial {
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.bl-12');
  if (!root) return;
  const wrap = root.querySelector('.bl-12__compare');
  const range = root.querySelector('[data-range]');
  const sync = () => wrap.style.setProperty('--pos', range.value);
  range.addEventListener('input', sync);
  sync();
})();

```
