---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-double-diagonal-section-both-edges/"
title: "CSS Double Diagonal Section Both Edges"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "A parallelogram band: both edges cut at the same angle in the same direction, so the section reads as a slice taken clean through the page rather than a join…"
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Double Diagonal Section Both Edges
Source: https://codefronts.com/layouts/css-diagonal-sections/css-double-diagonal-section-both-edges/

A parallelogram band: both edges cut at the same angle in the same direction, so the section reads as a slice taken clean through the page rather than a join between two colours. Four polygon points, one --cut token, and flat neighbours above and below to prove the slice — plus the padding maths that keeps content off both diagonals at once.
## HTML
```html
<div class="dgs-05">
  <input class="dgs-05__sronly" type="checkbox" id="dgs-05-dark">
  <label class="dgs-05__theme" for="dgs-05-dark">
    <svg class="dgs-05__i dgs-05__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-05__i dgs-05__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-05__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-05__ctl">
    <legend class="dgs-05__vh">Ribbon controls</legend>
    <input class="dgs-05__sr" type="radio" name="dgs-05-e" id="dgs-05-e1" checked><label for="dgs-05-e1">Parallel</label>
    <input class="dgs-05__sr" type="radio" name="dgs-05-e" id="dgs-05-e2"><label for="dgs-05-e2">Chevron</label>
    <input class="dgs-05__sr" type="radio" name="dgs-05-e" id="dgs-05-e3"><label for="dgs-05-e3">Wedge</label>
  </fieldset>

  <div class="dgs-05__stage">
    <section class="dgs-05__top" aria-labelledby="dgs-05-a">
      <div class="dgs-05__wrap">
        <p class="dgs-05__eyebrow">Ledger API</p>
        <h2 class="dgs-05__display" id="dgs-05-a">Settle in seven currencies from one balance</h2>
        <p class="dgs-05__lede">Double-entry accounts, idempotent transfers and a webhook you can replay. Sandbox keys are live the moment you sign up.</p>
        <dl class="dgs-05__kpi">
          <div><dt>p99 authorisation</dt><dd>84<span>ms</span></dd></div>
          <div><dt>Uptime, 12 mo</dt><dd>99.995<span>%</span></dd></div>
          <div><dt>Settlement</dt><dd>T+0</dd></div>
        </dl>
      </div>
    </section>

    <section class="dgs-05__ribbon" aria-labelledby="dgs-05-b">
      <div class="dgs-05__wrap dgs-05__split">
        <div>
          <p class="dgs-05__eyebrow dgs-05__eyebrow--on">Both edges cut</p>
          <h2 class="dgs-05__h2" id="dgs-05-b">A ribbon reads as a slice through the page</h2>
          <p class="dgs-05__body">Two coordinates in the same <code class="dgs-05__code">polygon()</code> handle the top and bottom edge. Cut them the same direction and the band reads as a parallel ribbon; cut them opposite and it becomes a chevron or a wedge — geometry only, no extra markup.</p>
          <p class="dgs-05__mono" aria-hidden="true">polygon(0 var(--cut), 100% 0, 100% calc(100% - var(--cut)), 0 100%)</p>
        </div>
        <figure class="dgs-05__code-card">
          <figcaption><span class="dgs-05__dot"></span>transfer.create</figcaption>
          <pre><code><span class="dgs-05__kw">POST</span> /v2/transfers
{
  <span class="dgs-05__str">"amount"</span>: 48250,
  <span class="dgs-05__str">"currency"</span>: <span class="dgs-05__val">"CAD"</span>,
  <span class="dgs-05__str">"source"</span>: <span class="dgs-05__val">"acct_9fK2"</span>,
  <span class="dgs-05__str">"idempotency_key"</span>: <span class="dgs-05__val">"inv_88214"</span>
}
<span class="dgs-05__ok">201 Created &middot; 84ms</span></code></pre>
        </figure>
      </div>
    </section>

    <section class="dgs-05__bottom" aria-labelledby="dgs-05-c">
      <div class="dgs-05__wrap">
        <h2 class="dgs-05__h3" id="dgs-05-c">Flat page resumes</h2>
        <p class="dgs-05__body dgs-05__body--dark">Because both edges are cut, the ribbon needs a negative margin at the top <em>and</em> the bottom — otherwise you get a wedge of page colour above and below the slice.</p>
        <ul class="dgs-05__list">
          <li><strong>Symmetric pull</strong><span>margin-block: calc(var(--cut) * -1 - 1px)</span></li>
          <li><strong>Symmetric padding</strong><span>padding-block: calc(var(--cut) + 5rem)</span></li>
          <li><strong>Stacking</strong><span>position: relative; z-index: 1</span></li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

.dgs-05 {
  --cut: clamp(1.75rem, 5.5vw, 7rem);
  --edge: polygon(0 var(--cut), 100% 0, 100% calc(100% - var(--cut)), 0 100%);
  --page: #ffffff;
  --page2: #f3f5f9;
  --ink: #0d1220;
  --muted: #576078;
  --line: #e2e6ef;
  --navy: #0b1230;
  --navy2: #131c46;
  --on-navy: #eef2ff;
  --blue: #3b6dff;
  --cyan: #4fd1e0;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'IBM Plex Sans', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-05 *,
.dgs-05 *::before,
.dgs-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.6 0.2 262)) {
  .dgs-05 {
    --page: oklch(1 0 0);
    --page2: oklch(0.966 0.006 262);
    --ink: oklch(0.19 0.03 265);
    --muted: oklch(0.51 0.03 265);
    --line: oklch(0.915 0.01 262);
    --navy: oklch(0.21 0.075 268);
    --navy2: oklch(0.29 0.1 268);
    --on-navy: oklch(0.96 0.015 265);
    --blue: oklch(0.62 0.19 264);
    --cyan: oklch(0.82 0.11 205);
  }
}

.dgs-05__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-05__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: .25rem;
  display: flex;
  gap: .2rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255,255,255,.9);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  box-shadow: 0 1px 2px rgba(13,18,32,.06);
}

.dgs-05__ctl label {
  min-inline-size: 3rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .75rem;
  border-radius: 6px;
  font-size: .76rem;
  font-weight: 500;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.dgs-05__ctl label:hover {
  color: var(--ink);
  background: var(--page2);
}

.dgs-05__sr:checked + label {
  background: var(--navy);
  color: var(--on-navy);
}

.dgs-05__sr:focus-visible + label {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

.dgs-05__stage {
  display: flow-root;
}

.dgs-05__wrap {
  inline-size: min(74rem, 100%);
  margin-inline: auto;
}

.dgs-05__top {
  padding: clamp(4rem, 9vw, 6.5rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(2.5rem, 6vw, 4.5rem));
}

.dgs-05__eyebrow {
  margin: 0 0 .9rem;
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  font-family: 'IBM Plex Mono', monospace;
  font-size: .74rem;
  font-weight: 500;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--blue);
}

.dgs-05__eyebrow--on {
  color: var(--cyan);
}

.dgs-05__display {
  margin: 0 0 1rem;
  max-inline-size: 25ch;
  font-size: clamp(2.1rem, 6.5vw, 4rem);
  font-weight: 600;
  line-height: 1.03;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-05__lede {
  margin: 0 0 clamp(2rem, 5vw, 3rem);
  max-inline-size: 48ch;
  font-size: clamp(1rem, 2vw, 1.18rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-05__kpi {
  margin: 0;
  display: grid;
  gap: 1.25rem clamp(1.5rem, 5vw, 3.5rem);
  grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr));
}

.dgs-05__kpi > div {
  padding-block-start: .8rem;
  border-block-start: 2px solid var(--blue);
}

.dgs-05__kpi dt {
  font-size: .74rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.dgs-05__kpi dd {
  margin: .3rem 0 0;
  font-size: clamp(1.6rem, 4.5vw, 2.3rem);
  font-weight: 600;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.dgs-05__kpi span {
  font-size: .8rem;
  font-weight: 500;
  color: var(--muted);
  margin-inline-start: .15rem;
}

.dgs-05__ribbon {
  position: relative;
  z-index: 1;
  color: var(--on-navy);
  background: linear-gradient(118deg, var(--navy) 0%, var(--navy2) 62%, var(--navy) 100%);
  clip-path: var(--edge);
  margin-block: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem);
}

.dgs-05__split {
  display: grid;
  gap: clamp(2rem, 5vw, 3.5rem);
  grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
  align-items: center;
}

.dgs-05__h2 {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-size: clamp(1.6rem, 4.4vw, 2.6rem);
  font-weight: 600;
  line-height: 1.06;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.dgs-05__body {
  margin: 0 0 1.25rem;
  max-inline-size: 52ch;
  color: rgba(238,242,255,.76);
  text-wrap: pretty;
}

.dgs-05__body--dark {
  color: var(--muted);
}

.dgs-05__code {
  font-family: 'IBM Plex Mono', monospace;
  font-size: .86em;
  padding: .1em .35em;
  border-radius: 4px;
  background: rgba(255,255,255,.12);
}

.dgs-05__mono {
  margin: 0;
  font-family: 'IBM Plex Mono', monospace;
  font-size: clamp(.6rem, 1.4vw, .74rem);
  color: var(--cyan);
  overflow-wrap: anywhere;
}

.dgs-05__code-card {
  margin: 0;
  border: 1px solid rgba(238,242,255,.18);
  border-radius: 12px;
  overflow: clip;
  background: rgba(4,8,26,.55);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.dgs-05__code-card figcaption {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: .65rem .9rem;
  border-block-end: 1px solid rgba(238,242,255,.14);
  font-family: 'IBM Plex Mono', monospace;
  font-size: .74rem;
  color: rgba(238,242,255,.72);
}

.dgs-05__dot {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 999px;
  background: var(--cyan);
  box-shadow: 0 0 0 3px rgba(79,209,224,.18);
}

.dgs-05__code-card pre {
  margin: 0;
  padding: 1rem 1.1rem 1.2rem;
  overflow-x: auto;
}

.dgs-05__code-card code {
  font-family: 'IBM Plex Mono', monospace;
  font-size: clamp(.68rem, 1.5vw, .82rem);
  line-height: 1.75;
  color: rgba(238,242,255,.86);
  white-space: pre;
}

.dgs-05__kw {
  color: var(--cyan);
  font-weight: 500;
}

.dgs-05__str {
  color: #9db4ff;
}

.dgs-05__val {
  color: #ffd8a8;
}

.dgs-05__ok {
  display: inline-block;
  margin-block-start: .6rem;
  color: #7ee3a5;
}

.dgs-05__bottom {
  background: var(--page2);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-05__h3 {
  margin: 0 0 .8rem;
  font-size: clamp(1.35rem, 3.6vw, 2rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.dgs-05__list {
  list-style: none;
  margin: 1.5rem 0 0;
  padding: 0;
  display: grid;
  gap: 1px;
  background: var(--line);
  border: 1px solid var(--line);
  border-radius: 10px;
  overflow: clip;
}

.dgs-05__list li {
  display: flex;
  flex-wrap: wrap;
  gap: .3rem 1rem;
  justify-content: space-between;
  align-items: baseline;
  padding: .9rem 1.1rem;
  background: var(--page);
}

.dgs-05__list strong {
  font-weight: 600;
}

.dgs-05__list span {
  font-family: 'IBM Plex Mono', monospace;
  font-size: .76rem;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.dgs-05:has(#dgs-05-e2:checked) {
  --edge: polygon(0 var(--cut), 100% 0, 100% 100%, 0 calc(100% - var(--cut)));
}

.dgs-05:has(#dgs-05-e3:checked) {
  --edge: polygon(0 0, 100% var(--cut), 100% calc(100% - var(--cut)), 0 100%);
}

@media (prefers-color-scheme: dark) {
  .dgs-05 {
    --page: #070a14;
    --page2: #0c1020;
    --ink: #eef2ff;
    --muted: #98a2c0;
    --line: #1d2338;
  }
}

@media (prefers-reduced-motion: reduce) {
  .dgs-05 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-05__ribbon {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
  }

  .dgs-05__code-card,
    .dgs-05__list,
    .dgs-05__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-05__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-05__sronly,
.dgs-05__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-05__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-05__theme:hover {
  translate: 0 -1px;
}

.dgs-05__sronly:focus-visible + .dgs-05__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-05__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-05__i--sun {
  display: none;
}

.dgs-05:has(#dgs-05-dark:checked) .dgs-05__i--moon {
  display: none;
}

.dgs-05:has(#dgs-05-dark:checked) .dgs-05__i--sun {
  display: block;
}

.dgs-05:has(#dgs-05-dark:checked) {
  --page: #070a14;
  --page2: #0c1020;
  --ink: #eef2ff;
  --muted: #98a2c0;
  --line: #1d2338;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-05__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-05__theme {
    border-color: CanvasText;
  }
}
```
