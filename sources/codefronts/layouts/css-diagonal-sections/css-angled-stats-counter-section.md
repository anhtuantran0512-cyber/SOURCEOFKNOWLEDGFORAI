---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-angled-stats-counter-section/"
title: "CSS Angled Stats Counter Section"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "Four KPI figures in an angled band, counting up the first time the section scrolls into view."
has_js: "true"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Angled Stats Counter Section
Source: https://codefronts.com/layouts/css-diagonal-sections/css-angled-stats-counter-section/

Four KPI figures in an angled band, counting up the first time the section scrolls into view. The final values are in the HTML, so with JavaScript disabled — or before the observer fires — the numbers are already correct; the script only animates from a lower start. Under prefers-reduced-motion nothing counts at all.
## HTML
```html
<div class="dgs-15" data-dgs-15>
  <input class="dgs-15__sronly" type="checkbox" id="dgs-15-dark">
  <label class="dgs-15__theme" for="dgs-15-dark">
    <svg class="dgs-15__i dgs-15__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-15__i dgs-15__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-15__srtext">Toggle dark theme</span>
  </label>
  <div class="dgs-15__stage">
    <section class="dgs-15__top" aria-labelledby="dgs-15-a">
      <div class="dgs-15__wrap">
        <p class="dgs-15__eyebrow">Terrace &mdash; matchday analytics</p>
        <h2 class="dgs-15__display" id="dgs-15-a">Ninety minutes of a stadium, measured</h2>
        <p class="dgs-15__lede">Turnstile flow, concession queues and away-end density, from one feed the safety officer already trusts.</p>
      </div>
    </section>

    <section class="dgs-15__band" aria-labelledby="dgs-15-b">
      <div class="dgs-15__wrap">
        <div class="dgs-15__head">
          <h2 class="dgs-15__h2" id="dgs-15-b">Season to date</h2>
          <p class="dgs-15__live"><span class="dgs-15__pulse" aria-hidden="true"></span>Updated 6 minutes ago</p>
        </div>
        <dl class="dgs-15__counters">
          <div>
            <dd><span class="dgs-15__num" data-dgs-15-to="1284000" data-dgs-15-fmt="compact">0</span></dd>
            <dt>Admissions scanned</dt>
          </div>
          <div>
            <dd><span class="dgs-15__num" data-dgs-15-to="96.4" data-dgs-15-dec="1">0</span><em>%</em></dd>
            <dt>Gates open on time</dt>
          </div>
          <div>
            <dd><span class="dgs-15__num" data-dgs-15-to="212">0</span><em>s</em></dd>
            <dt>Median queue, kiosk</dt>
          </div>
          <div>
            <dd><span class="dgs-15__num" data-dgs-15-to="38">0</span></dd>
            <dt>Venues live</dt>
          </div>
        </dl>
        <p class="dgs-15__foot">Figures aggregate 38 venues across four leagues, refreshed every five minutes on matchdays.</p>
      </div>
    </section>

    <section class="dgs-15__after" aria-labelledby="dgs-15-c">
      <div class="dgs-15__wrap dgs-15__cols">
        <h2 class="dgs-15__h3" id="dgs-15-c">Counting, done politely</h2>
        <p class="dgs-15__note">An <code class="dgs-15__code">IntersectionObserver</code> starts the count once, when the band is actually on screen, and <code class="dgs-15__code">prefers-reduced-motion</code> skips straight to the final figure. The numbers live in an <code class="dgs-15__code">aria-live</code> region so a screen reader hears the result, not every frame.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.dgs-15 {
  --cut: clamp(2rem, 6.5vw, 8rem);
  --black: #0a0a0a;
  --black2: #121212;
  --on: #f5f6f2;
  --dim: #8e918a;
  --volt: #d8ff2e;
  --line: rgba(245,246,242,.16);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--black);
  color: var(--on);
  font-family: 'Barlow Condensed', 'Archivo Narrow', system-ui, sans-serif;
  font-size: 17px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

.dgs-15 *,
.dgs-15 *::before,
.dgs-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.95 0.2 115)) {
  .dgs-15 {
    --black: oklch(0.145 0 0);
    --black2: oklch(0.2 0 0);
    --on: oklch(0.965 0.005 110);
    --dim: oklch(0.7 0.008 110);
    --volt: oklch(0.93 0.21 116);
  }
}

.dgs-15__stage {
  display: flow-root;
}

.dgs-15__wrap {
  inline-size: min(76rem, 100%);
  margin-inline: auto;
}

.dgs-15__top {
  padding: clamp(3.5rem, 8vw, 6rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-15__eyebrow {
  margin: 0 0 1rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .72rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--volt);
}

.dgs-15__display {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-size: clamp(2.6rem, 9vw, 5.6rem);
  font-weight: 700;
  line-height: .95;
  letter-spacing: -.02em;
  text-transform: uppercase;
  text-wrap: balance;
}

.dgs-15__lede {
  margin: 0;
  max-inline-size: 52ch;
  font-size: clamp(1.05rem, 2.2vw, 1.3rem);
  color: var(--dim);
  text-wrap: pretty;
}

.dgs-15__band {
  position: relative;
  z-index: 1;
  background: var(--volt);
  color: #0a0a0a;
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(2.5rem, 6vw, 4rem)) clamp(1.25rem, 5vw, 4rem) clamp(3rem, 7vw, 4.5rem);
}

.dgs-15__head {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.5rem;
  align-items: baseline;
  justify-content: space-between;
  padding-block-end: 1rem;
  border-block-end: 2px solid #0a0a0a;
}

.dgs-15__h2 {
  margin: 0;
  font-size: clamp(1.5rem, 4.5vw, 2.4rem);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: -.01em;
}

.dgs-15__live {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.dgs-15__pulse {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 999px;
  background: #0a0a0a;
  animation: dgs-15-blink 2s steps(1) infinite;
}

@keyframes dgs-15-blink {
  50% {
    opacity: .25;
  }
}

.dgs-15__counters {
  margin: 0;
  display: grid;
  gap: 1.5rem clamp(1.5rem, 4vw, 3rem);
  grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr));
  padding-block: clamp(1.75rem, 4vw, 2.5rem);
}

.dgs-15__counters > div {
  display: grid;
  gap: .2rem;
}

.dgs-15__counters dd {
  margin: 0;
  display: flex;
  align-items: baseline;
  font-size: clamp(2.6rem, 8vw, 4.6rem);
  font-weight: 700;
  line-height: .9;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.dgs-15__counters em {
  font-style: normal;
  font-size: .45em;
  font-weight: 600;
  margin-inline-start: .1em;
}

.dgs-15__counters dt {
  font-family: 'JetBrains Mono', monospace;
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(10,10,10,.7);
}

.dgs-15__foot {
  margin: 0;
  padding-block-start: 1rem;
  border-block-start: 1px solid rgba(10,10,10,.25);
  font-size: .9rem;
  color: rgba(10,10,10,.75);
  max-inline-size: 62ch;
}

.dgs-15__after {
  background: var(--black2);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-15__cols {
  display: grid;
  gap: 1rem clamp(2rem, 6vw, 4rem);
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  align-items: start;
}

.dgs-15__h3 {
  margin: 0;
  font-size: clamp(1.4rem, 3.6vw, 2rem);
  font-weight: 700;
  text-transform: uppercase;
}

.dgs-15__note {
  margin: 0;
  max-inline-size: 60ch;
  color: var(--dim);
  font-size: 1.02rem;
  text-wrap: pretty;
}

.dgs-15__code {
  font-family: 'JetBrains Mono', monospace;
  font-size: .82em;
  padding: .1em .35em;
  background: rgba(245,246,242,.1);
  color: var(--volt);
}

@media (prefers-reduced-motion: reduce) {
  .dgs-15 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-15__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-15__sronly,
.dgs-15__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-15__theme {
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

.dgs-15__theme:hover {
  translate: 0 -1px;
}

.dgs-15__sronly:focus-visible + .dgs-15__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-15__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-15__i--sun {
  display: none;
}

.dgs-15:has(#dgs-15-dark:checked) .dgs-15__i--moon {
  display: none;
}

.dgs-15:has(#dgs-15-dark:checked) .dgs-15__i--sun {
  display: block;
}

.dgs-15:has(#dgs-15-dark:checked) {
  --black: #f4f5f7;
  --ink: #0c0f14;
  --muted: #5b616b;
  --line: rgba(12,15,20,.15);
}

@media (prefers-reduced-motion: reduce) {
  .dgs-15__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-15__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-dgs-15]');
  if (!root) return;
  const nums = [...root.querySelectorAll('[data-dgs-15-to]')];
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = (el, v) => {
    // NB: a data-* name whose dash is followed by a DIGIT is not camel-cased
    // into the dataset map — only a dash followed by a letter is. So this
    // attribute is unreachable via dot access and Number() would yield NaN.
    // getAttribute sidesteps the mapping rule entirely.
    const dec = Number(el.getAttribute('data-dgs-15-dec') || 0);
    if (el.getAttribute('data-dgs-15-fmt') === 'compact') {
      return v >= 1e6 ? (v / 1e6).toFixed(2) + 'M' : Math.round(v).toLocaleString('en-US');
    }
    return v.toFixed(dec);
  };
  const run = (el) => {
    const to = Number(el.getAttribute('data-dgs-15-to'));
    if (still) { el.textContent = fmt(el, to); return; }
    const dur = 1400, t0 = performance.now();
    const tick = (t) => {
      const p = Math.min(1, (t - t0) / dur);
      const e = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(el, to * e);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  const band = root.querySelector('.dgs-15__counters');
  band.setAttribute('aria-live', 'polite');
  if (!('IntersectionObserver' in window)) { nums.forEach(run); return; }
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      io.unobserve(entry.target);
      nums.forEach(run);
    });
  }, { threshold: 0.35 });
  io.observe(band);
})();
```
