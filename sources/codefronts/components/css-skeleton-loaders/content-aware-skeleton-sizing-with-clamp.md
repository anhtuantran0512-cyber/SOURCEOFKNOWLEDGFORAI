---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/content-aware-skeleton-sizing-with-clamp/"
title: "Content-Aware Skeleton Sizing with clamp"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "A skeleton line sized width: 320px is a promise your real paragraph will not keep."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Content-Aware Skeleton Sizing with clamp
Source: https://codefronts.com/components/css-skeleton-loaders/content-aware-skeleton-sizing-with-clamp/

A skeleton line sized width: 320px is a promise your real paragraph will not keep. Sizing bars with clamp() and ch units makes them track the measure of the text that replaces them at every viewport — drag the resize handle on either panel and watch the fixed-width version break while the clamped one holds.
## HTML
```html
<div class="sk-06">
  <div class="sk-06__stage">
    <section class="sk-06__wrap" aria-labelledby="sk-06-h">
      <header class="sk-06__head">
        <p class="sk-06__eyebrow">clamp() · ch units</p>
        <h2 class="sk-06__h" id="sk-06-h">Size the bar like the sentence it replaces</h2>
        <p class="sk-06__sub">Drag the handle in either panel's bottom-right corner. The fixed-width bars overflow and strand; the clamped ones keep a believable measure at every width.</p>
      </header>

      <div class="sk-06__cols">
        <article class="sk-06__panel sk-06__panel--good">
          <header class="sk-06__phead">
            <p class="sk-06__label sk-06__label--on">clamp(60%, 46ch, 95%)</p>
            <p class="sk-06__ptitle">Content-aware</p>
          </header>
          <div class="sk-06__resizer">
            <div class="sk-06__lines sk-06__lines--clamp" role="status" aria-live="polite">
              <span class="sk-06__vh">Loading article body…</span>
              <span class="sk-06__bar" aria-hidden="true"></span>
              <span class="sk-06__bar" aria-hidden="true"></span>
              <span class="sk-06__bar" aria-hidden="true"></span>
              <span class="sk-06__bar" aria-hidden="true"></span>
              <span class="sk-06__bar sk-06__bar--last" aria-hidden="true"></span>
            </div>
            <p class="sk-06__handle" aria-hidden="true">drag →</p>
          </div>
          <p class="sk-06__note">Bars stay between 60% and 95% of the container, aiming for a 46-character measure — the same shape the real paragraph will take.</p>
        </article>

        <article class="sk-06__panel sk-06__panel--bad">
          <header class="sk-06__phead">
            <p class="sk-06__label">width: 320px</p>
            <p class="sk-06__ptitle">Fixed width</p>
          </header>
          <div class="sk-06__resizer">
            <div class="sk-06__lines sk-06__lines--fixed" role="status" aria-live="polite">
              <span class="sk-06__vh">Loading article body…</span>
              <span class="sk-06__bar" aria-hidden="true"></span>
              <span class="sk-06__bar" aria-hidden="true"></span>
              <span class="sk-06__bar" aria-hidden="true"></span>
              <span class="sk-06__bar" aria-hidden="true"></span>
              <span class="sk-06__bar sk-06__bar--last" aria-hidden="true"></span>
            </div>
            <p class="sk-06__handle" aria-hidden="true">drag →</p>
          </div>
          <p class="sk-06__note">Same 320px at every viewport. Narrow: it overflows the column. Wide: it sits marooned, then the real text reflows past it.</p>
        </article>
      </div>

      <article class="sk-06__real">
        <p class="sk-06__label">the copy these bars stand in for</p>
        <p class="sk-06__copy">Jordan Lee moved the activity feed to route-level skeletons last sprint. The measure here is roughly forty-six characters per line, which is exactly what the clamped placeholder above is shaped to imitate — so when this paragraph arrives, not a single line of it moves.</p>
      </article>

      <aside class="sk-06__spec" aria-label="Recipe">
        <p class="sk-06__srow"><span class="sk-06__skey">line</span><span class="sk-06__sval">inline-size: clamp(60%, 46ch, 95%)</span></p>
        <p class="sk-06__srow"><span class="sk-06__skey">last</span><span class="sk-06__sval">inline-size: clamp(30%, 24ch, 62%) — always shorter, like real prose</span></p>
        <p class="sk-06__srow"><span class="sk-06__skey">unit</span><span class="sk-06__sval">ch tracks the loaded font; px goes stale on zoom and font swap</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-06 {
  --bg: #ffffff;
  --bg2: #f4f6f4;
  --surface: #fbfcfb;
  --line: rgba(10,20,12,.12);
  --ink: #0b1410;
  --muted: rgba(11,20,16,.64);
  --faint: rgba(11,20,16,.45);
  --accent: #116b3a;
  --warn: #a4442a;
  --sk: rgba(11,20,16,.09);
  --sheen: rgba(11,20,16,.16);
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
  background: radial-gradient(60% 40% at 88% -8%, rgba(17,107,58,.09) 0%, transparent 60%), linear-gradient(178deg,#fff 0%,var(--bg2) 100%);
}

.sk-06 *,
.sk-06 *::before,
.sk-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 150)) {
  .sk-06 {
    --ink: oklch(0.18 0.02 155);
    --muted: oklch(0.18 0.02 155 / .64);
    --faint: oklch(0.18 0.02 155 / .45);
    --accent: oklch(0.48 0.12 152);
    --warn: oklch(0.5 0.13 35);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-06 {
    --sk: color-mix(in oklab, currentColor 9%, transparent);
    --sheen: color-mix(in oklab, currentColor 16%, transparent);
  }
}

.sk-06__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-06__wrap {
  inline-size: min(74rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-06__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
}

.sk-06__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-06__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-06__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-06__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(18rem,1fr));
  align-items: start;
}

.sk-06__panel {
  display: grid;
  gap: .9rem;
  padding: clamp(1.05rem,2vw,1.45rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
  box-shadow: 0 20px 44px -34px rgba(10,20,12,.4);
}

.sk-06__panel--good {
  border-color: rgba(17,107,58,.35);
}

.sk-06__panel--bad {
  border-color: rgba(164,68,42,.3);
}

.sk-06__phead {
  display: grid;
  gap: .3rem;
}

.sk-06__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .04em;
  color: var(--warn);
}

.sk-06__label--on {
  color: var(--accent);
}

.sk-06__ptitle {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 500;
  letter-spacing: -.015em;
}

.sk-06__resizer {
  position: relative;
  resize: horizontal;
  overflow: hidden;
  min-inline-size: 11rem;
  max-inline-size: 100%;
  inline-size: 100%;
  padding: 1rem 1rem 1.9rem;
  border: 1px dashed var(--line);
  border-radius: .8rem;
  background: #fff;
}

.sk-06__handle {
  position: absolute;
  inset-block-end: .45rem;
  inset-inline-end: 1.4rem;
  margin: 0;
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-06__lines {
  display: grid;
  gap: .65rem;
  position: relative;
}

.sk-06__note {
  margin: 0;
  font-size: .85rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-06__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .78rem;
  border-radius: 6px;
  background: var(--sk);
}

.sk-06__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-06-sheen 1.4s linear infinite;
}

@keyframes sk-06-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-06__lines--clamp > .sk-06__bar {
  inline-size: clamp(60%,46ch,95%);
}

.sk-06__lines--clamp > .sk-06__bar:nth-child(3) {
  inline-size: clamp(55%,42ch,88%);
}

.sk-06__lines--clamp > .sk-06__bar:nth-child(4) {
  inline-size: clamp(52%,38ch,84%);
}

.sk-06__lines--clamp > .sk-06__bar--last {
  inline-size: clamp(30%,24ch,62%);
}

.sk-06__lines--fixed > .sk-06__bar {
  inline-size: 320px;
  max-inline-size: none;
}

.sk-06__lines--fixed > .sk-06__bar--last {
  inline-size: 200px;
}

.sk-06__lines--fixed {
  overflow: hidden;
}

.sk-06__real {
  padding: clamp(1.05rem,2vw,1.45rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
  display: grid;
  gap: .55rem;
}

.sk-06__real .sk-06__label {
  color: var(--faint);
  text-transform: uppercase;
  letter-spacing: .11em;
  font-size: .66rem;
}

.sk-06__copy {
  margin: 0;
  max-inline-size: 46ch;
  font-size: 1rem;
  line-height: 1.65;
  color: var(--ink);
  text-wrap: pretty;
}

.sk-06__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-06__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-06__skey {
  min-inline-size: 3.2rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-06__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-06[data-theme="dark"] {
  --bg: #080b09;
  --bg2: #0e130f;
  --surface: rgba(255,255,255,.03);
  --line: rgba(255,255,255,.11);
  --ink: #eff5f0;
  --muted: rgba(239,245,240,.62);
  --faint: rgba(239,245,240,.42);
  --accent: #4ade80;
  --warn: #fb923c;
  background: linear-gradient(178deg,#0e130f 0%,#080b09 100%);
}

.sk-06[data-theme="dark"] .sk-06__resizer {
  background: rgba(255,255,255,.02);
}

@media (prefers-color-scheme: dark) {
  .sk-06:not([data-theme="light"]) {
    --bg: #080b09;
    --bg2: #0e130f;
    --surface: rgba(255,255,255,.03);
    --line: rgba(255,255,255,.11);
    --ink: #eff5f0;
    --muted: rgba(239,245,240,.62);
    --faint: rgba(239,245,240,.42);
    --accent: #4ade80;
    --warn: #fb923c;
    background: linear-gradient(178deg,#0e130f 0%,#080b09 100%);
  }

  .sk-06:not([data-theme="light"]) .sk-06__resizer {
    background: rgba(255,255,255,.02);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-06__bar::after {
    animation: none;
    background: none;
  }

  .sk-06__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-06__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-06__bar::after {
    animation: none;
    background: none;
  }

  .sk-06__panel,
    .sk-06__spec,
    .sk-06__real,
    .sk-06__resizer {
    border-color: CanvasText;
  }
}
```
