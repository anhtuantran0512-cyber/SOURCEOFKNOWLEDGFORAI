---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/skeleton-timing-and-duration-recipe/"
title: "Skeleton Timing and Duration Recipe"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "800ms feels frantic, 2400ms feels broken, and 1400ms is the value GitHub, Linear and Notion all converged on."
has_js: "true"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeleton Timing and Duration Recipe
Source: https://codefronts.com/components/css-skeleton-loaders/skeleton-timing-and-duration-recipe/

800ms feels frantic, 2400ms feels broken, and 1400ms is the value GitHub, Linear and Notion all converged on. Three panels run those durations simultaneously so the difference is impossible to miss — then a live slider lets you dial any value from 600ms to 3000ms and compare linear against cubic-bezier(.4, 0, .6, 1).
## HTML
```html
<div class="sk-09">
  <div class="sk-09__stage">
    <section class="sk-09__wrap" aria-labelledby="sk-09-h">
      <header class="sk-09__head">
        <p class="sk-09__eyebrow">timing · 1400ms</p>
        <h2 class="sk-09__h" id="sk-09-h">The sweet spot is 1400ms. Here's why.</h2>
        <p class="sk-09__sub">All three panels animate at once, so you judge them against each other rather than from memory. Then dial your own value and watch the seam.</p>
      </header>

      <div class="sk-09__cols">
        <article class="sk-09__panel sk-09__panel--fast" role="status" aria-live="off">
          <p class="sk-09__dur">800ms</p>
          <p class="sk-09__verdict">Frenetic</p>
          <div class="sk-09__bars" aria-hidden="true">
            <span class="sk-09__bar sk-09__bar--block"></span>
            <span class="sk-09__bar"></span><span class="sk-09__bar" style="inline-size:74%"></span><span class="sk-09__bar" style="inline-size:52%"></span>
          </div>
          <p class="sk-09__why">The sweep reads as flicker and competes for attention with everything else on the page.</p>
        </article>

        <article class="sk-09__panel sk-09__panel--good" role="status" aria-live="off">
          <p class="sk-09__dur">1400ms</p>
          <p class="sk-09__verdict sk-09__verdict--on">Sweet spot
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12.6 9.6 17 19 7.5" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </p>
          <div class="sk-09__bars" aria-hidden="true">
            <span class="sk-09__bar sk-09__bar--block"></span>
            <span class="sk-09__bar"></span><span class="sk-09__bar" style="inline-size:74%"></span><span class="sk-09__bar" style="inline-size:52%"></span>
          </div>
          <p class="sk-09__why">One calm pass per beat. Reads as "working" without pulling the eye. GitHub, Linear and Notion all sit within 200ms of this.</p>
        </article>

        <article class="sk-09__panel sk-09__panel--slow" role="status" aria-live="off">
          <p class="sk-09__dur">2400ms</p>
          <p class="sk-09__verdict">Stalled</p>
          <div class="sk-09__bars" aria-hidden="true">
            <span class="sk-09__bar sk-09__bar--block"></span>
            <span class="sk-09__bar"></span><span class="sk-09__bar" style="inline-size:74%"></span><span class="sk-09__bar" style="inline-size:52%"></span>
          </div>
          <p class="sk-09__why">Long enough between passes that users start to believe the request has died.</p>
        </article>
      </div>

      <div class="sk-09__tuner">
        <div class="sk-09__tunehead">
          <label class="sk-09__tunelabel" for="sk-09-range">Tune the duration</label>
          <output class="sk-09__out" id="sk-09-out" role="status" aria-live="polite">1400ms · linear</output>
        </div>
        <input class="sk-09__range" id="sk-09-range" type="range" min="600" max="3000" step="50" value="1400" aria-describedby="sk-09-out">
        <div class="sk-09__tunebars" id="sk-09-live" aria-hidden="true">
          <span class="sk-09__bar sk-09__bar--tall"></span>
          <span class="sk-09__bar sk-09__bar--tall"></span>
          <span class="sk-09__bar sk-09__bar--tall"></span>
          <span class="sk-09__bar sk-09__bar--tall"></span>
          <span class="sk-09__bar sk-09__bar--tall"></span>
          <span class="sk-09__bar sk-09__bar--tall"></span>
        </div>
        <div class="sk-09__eases">
          <button class="sk-09__ease is-on" type="button" data-ease="linear" aria-pressed="true">linear — travelling sheen</button>
          <button class="sk-09__ease" type="button" data-ease="cubic-bezier(.4,0,.6,1)" aria-pressed="false">cubic-bezier(.4,0,.6,1) — pulse</button>
        </div>
      </div>

      <aside class="sk-09__spec" aria-label="Recipe">
        <p class="sk-09__srow"><span class="sk-09__skey">sheen</span><span class="sk-09__sval">animation: sheen 1400ms linear infinite — keep travelling motion linear</span></p>
        <p class="sk-09__srow"><span class="sk-09__skey">pulse</span><span class="sk-09__sval">animation: pulse 1800ms cubic-bezier(.4,0,.6,1) infinite — dwells at both ends</span></p>
        <p class="sk-09__srow"><span class="sk-09__skey">stagger</span><span class="sk-09__sval">negative animation-delay per row, then add ~200ms to the base</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-09 {
  --bg: #0b0705;
  --bg2: #170e08;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #fdf4ee;
  --muted: rgba(253,244,238,.62);
  --faint: rgba(253,244,238,.42);
  --accent: #fb923c;
  --good: #5eead4;
  --sk: rgba(253,244,238,.1);
  --sheen: rgba(253,244,238,.18);
  --dur: 1400ms;
  --ease: linear;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(60% 42% at 12% -6%, rgba(251,146,60,.15) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-09 *,
.sk-09 *::before,
.sk-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 50)) {
  .sk-09 {
    --ink: oklch(0.97 0.012 60);
    --muted: oklch(0.97 0.012 60 / .62);
    --faint: oklch(0.97 0.012 60 / .42);
    --accent: oklch(0.78 0.15 55);
    --good: oklch(0.85 0.12 178);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-09 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 18%, transparent);
  }
}

.sk-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-09__wrap {
  inline-size: min(78rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-09__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
}

.sk-09__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-09__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-09__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-09__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
}

.sk-09__panel {
  display: grid;
  gap: .6rem;
  align-content: start;
  padding: clamp(1rem,1.9vw,1.4rem);
  border: 1px solid var(--line);
  border-radius: 1.05rem;
  background: var(--surface);
}

.sk-09__panel--fast {
  --dur: 800ms;
}

.sk-09__panel--good {
  --dur: 1400ms;
  border-color: rgba(94,234,212,.35);
  box-shadow: 0 26px 62px -40px rgba(0,0,0,.9);
}

.sk-09__panel--slow {
  --dur: 2400ms;
}

.sk-09__dur {
  margin: 0;
  font-family: var(--mono);
  font-size: 1.5rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.02em;
}

.sk-09__verdict {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .4rem;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-09__verdict--on {
  color: var(--good);
}

.sk-09__verdict svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.sk-09__bars {
  display: grid;
  gap: .6rem;
  margin-block: .5rem;
}

.sk-09__why {
  margin: auto 0 0;
  padding-block-start: .75rem;
  border-block-start: 1px solid var(--line);
  font-size: .85rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-09__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-09__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-09-sheen var(--dur) var(--ease) infinite;
}

@keyframes sk-09-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-09__bar--block {
  block-size: auto;
  aspect-ratio: 16/7;
  border-radius: 9px;
}

.sk-09__bar--tall {
  block-size: clamp(3rem,7vw,4.5rem);
  border-radius: 9px;
}

.sk-09__tuner {
  padding: clamp(1.05rem,2vw,1.5rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
  display: grid;
  gap: .9rem;
}

.sk-09__tunehead {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.sk-09__tunelabel {
  font-size: 1rem;
  font-weight: 500;
}

.sk-09__out {
  font-family: var(--mono);
  font-size: .9rem;
  font-variant-numeric: tabular-nums;
  color: var(--accent);
}

.sk-09__range {
  inline-size: 100%;
  min-block-size: 2.75rem;
  accent-color: var(--accent);
  cursor: pointer;
}

.sk-09__range:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.sk-09__tunebars {
  display: grid;
  gap: .55rem;
  grid-template-columns: repeat(auto-fit,minmax(7rem,1fr));
}

.sk-09__eases {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
}

.sk-09__ease {
  min-block-size: 2.75rem;
  padding: .55rem 1rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--muted);
  background: transparent;
  border: 1px solid var(--line);
  transition: background .18s ease, color .18s ease;
}

.sk-09__ease:hover {
  background: rgba(255,255,255,.06);
  color: var(--ink);
}

.sk-09__ease:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.sk-09__ease.is-on {
  background: var(--accent);
  border-color: var(--accent);
  color: #21100a;
}

.sk-09__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-09__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-09__skey {
  min-inline-size: 4rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-09__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-09[data-theme="light"] {
  --bg: #fdf9f5;
  --bg2: #fff;
  --surface: rgba(24,12,4,.028);
  --line: rgba(24,12,4,.11);
  --ink: #180c04;
  --muted: rgba(24,12,4,.62);
  --faint: rgba(24,12,4,.44);
  --accent: #b4530a;
  --good: #0f766e;
  background: linear-gradient(178deg,#fff 0%,#f7efe6 100%);
}

@media (prefers-color-scheme: light) {
  .sk-09:not([data-theme="dark"]) {
    --bg: #fdf9f5;
    --bg2: #fff;
    --surface: rgba(24,12,4,.028);
    --line: rgba(24,12,4,.11);
    --ink: #180c04;
    --muted: rgba(24,12,4,.62);
    --faint: rgba(24,12,4,.44);
    --accent: #b4530a;
    --good: #0f766e;
    background: linear-gradient(178deg,#fff 0%,#f7efe6 100%);
  }

  .sk-09:not([data-theme="dark"]) .sk-09__ease.is-on {
    color: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-09__bar::after {
    animation: none;
    background: none;
  }

  .sk-09__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }

  .sk-09__ease {
    transition: none;
  }
}

@media (forced-colors: active) {
  .sk-09__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-09__bar::after {
    animation: none;
    background: none;
  }

  .sk-09__panel,
    .sk-09__tuner,
    .sk-09__spec,
    .sk-09__ease {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sk-09');
const range = document.getElementById('sk-09-range');
const out = document.getElementById('sk-09-out');
const live = document.getElementById('sk-09-live');
const eases = [...root.querySelectorAll('.sk-09__ease')];
let easeName = 'linear';

const paint = () => {
  live.style.setProperty('--dur', range.value + 'ms');
  live.style.setProperty('--ease', easeName);
  out.textContent = range.value + 'ms · ' + (easeName === 'linear' ? 'linear' : 'cubic-bezier(.4,0,.6,1)');
};

range.addEventListener('input', paint);
eases.forEach((b) => b.addEventListener('click', () => {
  easeName = b.dataset.ease;
  eases.forEach((o) => { o.classList.toggle('is-on', o === b); o.setAttribute('aria-pressed', String(o === b)); });
  paint();
}));
paint();
```
