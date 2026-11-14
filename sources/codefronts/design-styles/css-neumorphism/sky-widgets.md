---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/sky-widgets/"
title: "Soft UI Dashboard Widgets"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The hardest test of soft UI: dense data, where every widget competing for depth turns the screen to mush."
has_js: "true"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Soft UI Dashboard Widgets
Source: https://codefronts.com/design-styles/css-neumorphism/sky-widgets/

The hardest test of soft UI: dense data, where every widget competing for depth turns the screen to mush. Five widgets — stat, bar chart, sparkline, gauge, list — on a strict depth budget, with a density toggle showing the same data comfortable and compact. The rule that saves it: data lives in wells, chrome is raised, and nothing else gets a shadow.
## HTML
```html
<section class="nm-21" aria-labelledby="nm-21-heading">
      <input type="checkbox" id="nm-21-theme" class="nm-21__themeinput">
      <label for="nm-21-theme" class="nm-21__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-21__stage" data-density="comfortable">
    <header class="nm-21__head">
      <div class="nm-21__headtext">
        <p class="nm-21__kicker">Application</p>
        <h2 class="nm-21__heading" id="nm-21-heading">Dense data on a depth budget</h2>
        <p class="nm-21__sub">Two levels only: bodies raised, data inset. Rows get a dotted rule, never a shadow.</p>
      </div>
      <button class="nm-21__density" type="button" aria-pressed="false">Compact density</button>
    </header>

    <div class="nm-21__grid">
      <article class="nm-21__w nm-21__w--stat">
        <p class="nm-21__wlabel">Monthly recurring</p>
        <p class="nm-21__stat">£48,210</p>
        <p class="nm-21__delta">+6.4% against May</p>
      </article>

      <article class="nm-21__w nm-21__w--chart">
        <p class="nm-21__wlabel">Invoices raised, by week</p>
        <div class="nm-21__well nm-21__bars">
          <span class="nm-21__bar" style="--h:38%"></span>
          <span class="nm-21__bar" style="--h:56%"></span>
          <span class="nm-21__bar" style="--h:44%"></span>
          <span class="nm-21__bar" style="--h:72%"></span>
          <span class="nm-21__bar" style="--h:61%"></span>
          <span class="nm-21__bar nm-21__bar--now" style="--h:88%"></span>
        </div>
        <div class="nm-21__axis"><span>W18</span><span>W23</span></div>
      </article>

      <article class="nm-21__w">
        <p class="nm-21__wlabel">Cash position</p>
        <div class="nm-21__well nm-21__spark"><span class="nm-21__sparkline"></span></div>
        <p class="nm-21__delta">£112,940 · 90-day trend</p>
      </article>

      <article class="nm-21__w nm-21__w--list">
        <p class="nm-21__wlabel">Awaiting action</p>
        <ul class="nm-21__list">
          <li class="nm-21__row"><span>Halden Rivers</span><b>£2,720</b></li>
          <li class="nm-21__row"><span>Corvid Press</span><b>£1,140</b></li>
          <li class="nm-21__row"><span>Meridian Labs</span><b>£860</b></li>
          <li class="nm-21__row"><span>Aster Studio</span><b>£410</b></li>
        </ul>
      </article>

      <article class="nm-21__w">
        <p class="nm-21__wlabel">Collection rate</p>
        <div class="nm-21__well nm-21__meter"><span class="nm-21__meterfill" style="width:81%"></span></div>
        <div class="nm-21__meterrow"><span>81% within terms</span><b>target 85%</b></div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-21 {
  position: relative;
  --nm-21-surface: #e6e8e9;
  --nm-21-dark: rgba(170,175,178,0.62);
  --nm-21-light: rgba(255,255,255,0.94);
  --nm-21-ink: #232729;
  --nm-21-muted: #565c60;
  --nm-21-border: #969b9f;
  --nm-21-accent: #2f6b6f;
  --nm-21-accent2: #7a5a2e;
  --nm-21-dist: 8px;
  --nm-21-pad: 22px;
  --nm-21-statsize: 2.1rem;
  --nm-21-font-display: "Söhne", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-21-surface);
  color: var(--nm-21-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 200)) {
  .nm-21 {
    --nm-21-surface: oklch(0.918 0.005 205);
    --nm-21-ink: oklch(0.26 0.011 220);
    --nm-21-muted: oklch(0.45 0.012 220);
    --nm-21-accent: oklch(0.47 0.07 195);
    --nm-21-accent2: oklch(0.48 0.08 70);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-21 {
    --nm-21-dark: color-mix(in oklab, var(--nm-21-surface), #000 19%);
    --nm-21-light: color-mix(in oklab, var(--nm-21-surface), #fff 92%);
    --nm-21-border: color-mix(in oklab, var(--nm-21-surface), var(--nm-21-ink) 33%);
  }
}

.nm-21 *,
.nm-21 *::before,
.nm-21 *::after {
  box-sizing: border-box;
}

.nm-21__stage {
  max-width: 1080px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 54px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(20px, 3.2vw, 30px);
}

.nm-21__stage[data-density="compact"] {
  --nm-21-pad: 14px;
  --nm-21-dist: 5px;
  --nm-21-statsize: 1.6rem;
}

.nm-21__head {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  align-items: flex-end;
  justify-content: space-between;
}

.nm-21__headtext {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-inline-size: 0;
}

.nm-21__kicker {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-21-muted);
}

.nm-21__heading {
  margin: 0;
  font-family: var(--nm-21-font-display);
  font-size: clamp(1.45rem, 4vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-21__sub {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--nm-21-muted);
  text-wrap: pretty;
}

.nm-21__density {
  min-height: 44px;
  padding: 0 18px;
  border-radius: 12px;
  border: 1px solid var(--nm-21-border);
  background: var(--nm-21-surface);
  color: var(--nm-21-muted);
  font: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 5px 5px 11px var(--nm-21-dark), -5px -5px 11px var(--nm-21-light);
}

.nm-21__density[aria-pressed="true"] {
  color: var(--nm-21-accent);
  border-color: var(--nm-21-accent);
  box-shadow: inset 4px 4px 9px var(--nm-21-dark), inset -4px -4px 9px var(--nm-21-light);
}

.nm-21__density:focus-visible {
  outline: 2px solid var(--nm-21-accent);
  outline-offset: 3px;
}

.nm-21__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr));
  gap: clamp(14px, 2.4vw, 22px);
  align-items: start;
}

.nm-21__w {
  border-radius: 20px;
  padding: var(--nm-21-pad);
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-inline-size: 0;
  background: var(--nm-21-surface);
  border: 1px solid var(--nm-21-border);
  box-shadow: var(--nm-21-dist) var(--nm-21-dist) calc(var(--nm-21-dist) * 2.1) var(--nm-21-dark), calc(var(--nm-21-dist) * -1) calc(var(--nm-21-dist) * -1) calc(var(--nm-21-dist) * 2.1) var(--nm-21-light);
}

.nm-21__w--chart,
.nm-21__w--list {
  grid-column: span 1;
}

@media (min-width: 780px) {
  .nm-21__w--chart {
    grid-column: span 2;
  }
}

.nm-21__wlabel {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--nm-21-muted);
  font-weight: 600;
}

.nm-21__stat {
  margin: 0;
  font-family: var(--nm-21-font-display);
  font-size: var(--nm-21-statsize);
  font-weight: 650;
  letter-spacing: -0.03em;
  font-variant-numeric: tabular-nums;
  line-height: 1.05;
}

.nm-21__delta {
  margin: 0;
  font-size: 0.78rem;
  color: var(--nm-21-accent);
  font-weight: 600;
}

.nm-21__well {
  border-radius: 14px;
  padding: 12px;
  background: var(--nm-21-surface);
  box-shadow: inset 4px 4px 9px var(--nm-21-dark), inset -4px -4px 9px var(--nm-21-light);
}

.nm-21__bars {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  gap: 10px;
  align-items: end;
  height: 118px;
}

.nm-21__bar {
  height: var(--h);
  border-radius: 6px 6px 3px 3px;
  background: var(--nm-21-accent);
  opacity: 0.72;
}

.nm-21__bar--now {
  opacity: 1;
  background: var(--nm-21-accent2);
}

.nm-21__axis {
  display: flex;
  justify-content: space-between;
  font-size: 0.68rem;
  color: var(--nm-21-muted);
  font-variant-numeric: tabular-nums;
}

.nm-21__spark {
  height: 88px;
  display: grid;
  align-items: stretch;
}

.nm-21__sparkline {
  display: block;
  height: 100%;
  background: linear-gradient(180deg, var(--nm-21-accent), rgba(0,0,0,0));
  opacity: 0.85;
  clip-path: polygon(0 78%, 12% 66%, 24% 72%, 36% 48%, 48% 56%, 60% 34%, 72% 42%, 84% 22%, 100% 30%, 100% 100%, 0 100%);
}

.nm-21__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 9px;
}

.nm-21__row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-size: 0.83rem;
  padding-bottom: 9px;
  border-bottom: 1px dotted var(--nm-21-border);
  min-inline-size: 0;
}

.nm-21__row:last-child {
  border-bottom: 0;
  padding-bottom: 0;
}

.nm-21__row b {
  font-variant-numeric: tabular-nums;
}

.nm-21__meter {
  padding: 0;
  height: 16px;
  border-radius: 999px;
  overflow: hidden;
}

.nm-21__meterfill {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: var(--nm-21-accent);
}

.nm-21__meterrow {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-size: 0.76rem;
  color: var(--nm-21-muted);
  min-inline-size: 0;
}

.nm-21__meterrow b {
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

@media (prefers-color-scheme: dark) {
  .nm-21 {
    --nm-21-surface: #262a2b;
    --nm-21-dark: rgba(11,12,13,0.72);
    --nm-21-light: rgba(88,93,96,0.44);
    --nm-21-ink: #e7eaeb;
    --nm-21-muted: #9aa0a3;
    --nm-21-border: #858b8f;
    --nm-21-accent: #6fbdc0;
    --nm-21-accent2: #d0a367;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-21 {
      --nm-21-dark: color-mix(in oklab, var(--nm-21-surface), #000 55%);
      --nm-21-light: color-mix(in oklab, var(--nm-21-surface), #fff 14%);
    }
  }
}

.nm-21[data-theme="dark"] {
  --nm-21-surface: #262a2b;
  --nm-21-dark: rgba(11,12,13,0.72);
  --nm-21-light: rgba(88,93,96,0.44);
  --nm-21-ink: #e7eaeb;
  --nm-21-muted: #9aa0a3;
  --nm-21-border: #858b8f;
  --nm-21-accent: #6fbdc0;
  --nm-21-accent2: #d0a367;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-21[data-theme="dark"] {
    --nm-21-dark: color-mix(in oklab, var(--nm-21-surface), #000 55%);
    --nm-21-light: color-mix(in oklab, var(--nm-21-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-21__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-21__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-21-surface);
  color: var(--nm-21-ink);
  border: 1px solid var(--nm-21-line);
  font: 600 11px/1 var(--nm-21-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-21-distance, 6px) var(--nm-21-distance, 6px) var(--nm-21-blur, 14px) var(--nm-21-dark), calc(-1 * var(--nm-21-distance, 6px)) calc(-1 * var(--nm-21-distance, 6px)) var(--nm-21-blur, 14px) var(--nm-21-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-21__themebtn:hover {
  color: var(--nm-21-ink);
}

.nm-21__themeinput:focus-visible + .nm-21__themebtn {
  outline: 2px solid var(--nm-21-ink);
  outline-offset: 3px;
}

.nm-21:has(#nm-21-theme:checked) .nm-21__themebtn {
  box-shadow: inset var(--nm-21-distance, 6px) var(--nm-21-distance, 6px) var(--nm-21-blur, 14px) var(--nm-21-dark), inset calc(-1 * var(--nm-21-distance, 6px)) calc(-1 * var(--nm-21-distance, 6px)) var(--nm-21-blur, 14px) var(--nm-21-light);
}

.nm-21__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-21:has(#nm-21-theme:checked) {
  --nm-21-surface: #262a2b;
  --nm-21-dark: rgba(11,12,13,0.72);
  --nm-21-light: rgba(88,93,96,0.44);
  --nm-21-ink: #e7eaeb;
  --nm-21-muted: #9aa0a3;
  --nm-21-border: #858b8f;
  --nm-21-accent: #6fbdc0;
  --nm-21-accent2: #d0a367;
}

@media (prefers-color-scheme: light) {
  .nm-21:has(#nm-21-theme:checked) {
    --nm-21-surface: #262a2b;
    --nm-21-dark: rgba(11,12,13,0.72);
    --nm-21-light: rgba(88,93,96,0.44);
    --nm-21-ink: #e7eaeb;
    --nm-21-muted: #9aa0a3;
    --nm-21-border: #858b8f;
    --nm-21-accent: #6fbdc0;
    --nm-21-accent2: #d0a367;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-21:has(#nm-21-theme:checked) {
    --nm-21-surface: #e6e8e9;
    --nm-21-dark: rgba(170,175,178,0.62);
    --nm-21-light: rgba(255,255,255,0.94);
    --nm-21-ink: #232729;
    --nm-21-muted: #565c60;
    --nm-21-border: #969b9f;
    --nm-21-accent: #2f6b6f;
    --nm-21-accent2: #7a5a2e;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-21__themebtn {
    transition: none;
  }
}
```

## JavaScript
```js
const d = document.querySelector('.nm-21');
if (d) {
  const stage = d.querySelector('.nm-21__stage'), btn = d.querySelector('.nm-21__density');
  btn.addEventListener('click', () => {
    const on = btn.getAttribute('aria-pressed') === 'true';
    btn.setAttribute('aria-pressed', String(!on));
    stage.dataset.density = on ? 'comfortable' : 'compact';
    btn.textContent = on ? 'Compact density' : 'Comfortable density';
  });
}
```
