---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/backdrop-filter-fallback-recipe/"
title: "Backdrop Filter Fallback Recipe"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "Glass is an enhancement, never a requirement."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Backdrop Filter Fallback Recipe
Source: https://codefronts.com/design-styles/css-glassmorphism/backdrop-filter-fallback-recipe/

Glass is an enhancement, never a requirement. Two panels sit side by side — the left one gets real backdrop-filter, the right one is deliberately built as if the browser had none — so you can see exactly what your fallback users see. The recipe: declare the opaque version first, upgrade inside @supports, and fake the depth with a rim plus an inner shadow.
## HTML
```html
<div class="gm-09">
  <input class="gm-09__sr" type="checkbox" id="gm-09-theme">
  <label class="gm-09__theme" for="gm-09-theme" title="Switch theme">
    <svg class="gm-09__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-09__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-09__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-09__stage">
    <section class="gm-09__wrap" aria-labelledby="gm-09-h">
      <header class="gm-09__head">
        <p class="gm-09__eyebrow">@supports · progressive enhancement</p>
        <h2 class="gm-09__h" id="gm-09-h">What your fallback users actually see</h2>
        <p class="gm-09__sub">Left: the browser can blur. Right: the same component built as if it could not. Both are legible, both look deliberate.</p>
        <div class="gm-09__pills">
          <span class="gm-09__sp">Chrome 76+</span>
          <span class="gm-09__sp">Safari 9+ <em>-webkit-</em></span>
          <span class="gm-09__sp">Firefox 103+</span>
        </div>
      </header>

      <div class="gm-09__compare">
        <article class="gm-09__panel gm-09__panel--glass">
          <div class="gm-09__ptop">
            <span class="gm-09__state gm-09__state--on" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M5 12.6l4.4 4.2L19 7.4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <h3 class="gm-09__title">Supported</h3>
          </div>
          <p class="gm-09__copy">The upgrade rule lands: 22px blur, 165% saturate, 14% white film. The mesh reads through the panel and the rim catches light.</p>
          <code class="gm-09__snip">@supports (backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))</code>
          <dl class="gm-09__kv">
            <div><dt>fill</dt><dd>white 14%</dd></div>
            <div><dt>blur</dt><dd>22px</dd></div>
          </dl>
        </article>

        <article class="gm-09__panel gm-09__panel--fallback">
          <div class="gm-09__ptop">
            <span class="gm-09__state gm-09__state--off" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M8 8l8 8M16 8l-8 8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
            <h3 class="gm-09__title">Not supported</h3>
          </div>
          <p class="gm-09__copy">No filter, so depth comes from material instead: 92% opaque fill, a bright top rim and an inner top shadow that reads as panel thickness.</p>
          <code class="gm-09__snip">@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px)))</code>
          <dl class="gm-09__kv">
            <div><dt>fill</dt><dd>solid 92%</dd></div>
            <div><dt>depth</dt><dd>inset shadow</dd></div>
          </dl>
        </article>
      </div>

      <p class="gm-09__foot">Author the opaque rule <em>first</em>. If the enhancement never arrives, the worst case is a solid panel — not white text on a transparent hole.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-09 {
  --a1: rgba(110,231,183,.5);
  --a2: rgba(165,180,252,.55);
  --a3: rgba(253,164,175,.5);
  --a4: rgba(125,211,252,.5);
  --base: #eff3fa;
  --base2: #e0e8fb;
  --ink: #0e1220;
  --muted: rgba(14,18,32,.68);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(14,18,32,.12);
  --solid: rgba(255,255,255,.94);
  --ok: #047857;
  --no: #be123c;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(50% 42% at 10% 20%, var(--a1) 0%, transparent 60%), radial-gradient(54% 46% at 88% 16%, var(--a2) 0%, transparent 62%), radial-gradient(46% 40% at 76% 90%, var(--a3) 0%, transparent 58%), radial-gradient(46% 40% at 18% 88%, var(--a4) 0%, transparent 58%), linear-gradient(158deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-09 *,
.gm-09 *::before,
.gm-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-09 {
    --a1: oklch(0.8 0.15 165 / .52);
    --a2: oklch(0.62 0.22 275 / .56);
    --a3: oklch(0.72 0.19 15 / .46);
    --a4: oklch(0.78 0.16 220 / .46);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
    --ok: oklch(0.86 0.13 175);
    --no: oklch(0.78 0.14 15);
  }
}

.gm-09__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-09__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 8;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(10px) saturate(160%);
  backdrop-filter: blur(10px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), 0 10px 24px -14px rgba(0,0,0,.7);
  transition: scale .18s ease;
}

.gm-09__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-09__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-09__theme:hover {
  scale: 1.06;
}

.gm-09__sr:focus-visible + .gm-09__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-09__moon {
  display: none;
}

.gm-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-09__wrap {
  inline-size: min(70rem,100%);
}

.gm-09__head {
  display: grid;
  gap: .7rem;
  max-inline-size: 44rem;
  margin-block-end: clamp(1.5rem,3.5vw,2.5rem);
}

.gm-09__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-09__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-09__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-09__pills {
  display: flex;
  flex-wrap: wrap;
  gap: .45rem;
  margin-block-start: .25rem;
}

.gm-09__sp {
  padding: .34rem .6rem;
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .02em;
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-09__sp em {
  font-style: normal;
  opacity: .7;
}

.gm-09__compare {
  display: grid;
  gap: clamp(1rem,2vw,1.5rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.gm-09__panel {
  display: flex;
  flex-direction: column;
  gap: .7rem;
  padding: clamp(1.2rem,2.1vw,1.65rem);
  border-radius: 1.4rem;
  border: 1px solid var(--edge);
  background: var(--solid);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3), inset 0 2px 10px rgba(0,0,0,.4), 0 26px 58px -28px rgba(0,0,0,.6);
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-09__panel--glass {
    background: rgba(255,255,255,.14);
    -webkit-backdrop-filter: blur(22px) saturate(165%);
    backdrop-filter: blur(22px) saturate(165%);
    box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 26px 58px -28px rgba(0,0,0,.62);
  }
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  @supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
    .gm-09__panel--glass {
      background: color-mix(in oklab, var(--tint) 14%, transparent);
    }
  }
}

.gm-09__ptop {
  display: flex;
  align-items: center;
  gap: .6rem;
}

.gm-09__state {
  display: grid;
  place-items: center;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  border-radius: 999px;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.12);
}

.gm-09__state svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.gm-09__state--on {
  color: var(--ok);
}

.gm-09__state--off {
  color: var(--no);
}

.gm-09__title {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.gm-09__copy {
  margin: 0;
  font-size: .94rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-09__snip {
  display: block;
  padding: .6rem .7rem;
  border-radius: .6rem;
  font-family: var(--mono);
  font-size: .68rem;
  line-height: 1.5;
  color: var(--ink);
  background: rgba(0,0,0,.3);
  border: 1px solid var(--rim2);
  overflow-wrap: anywhere;
}

.gm-09__kv {
  margin: auto 0 0;
  padding-block-start: .85rem;
  border-block-start: 1px solid var(--rim2);
  display: flex;
  gap: 1.6rem;
}

.gm-09__kv div {
  display: grid;
  gap: .15rem;
}

.gm-09__kv dt {
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-09__kv dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .85rem;
  font-variant-numeric: tabular-nums;
}

.gm-09__foot {
  margin: clamp(1.1rem,2vw,1.6rem) 0 0;
  max-inline-size: 46rem;
  font-size: .9rem;
  line-height: 1.55;
  color: var(--muted);
}

.gm-09[data-theme="light"],
.gm-09:has(#gm-09-theme:checked) {
  --a1: rgba(52,211,153,.5);
  --a2: rgba(99,102,241,.55);
  --a3: rgba(251,113,133,.45);
  --a4: rgba(56,189,248,.45);
  --base: #060a12;
  --base2: #101a34;
  --ink: #f8fbfe;
  --muted: rgba(248,251,254,.7);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.2);
  --solid: rgba(16,20,44,.92);
  --ok: #5eead4;
  --no: #fda4af;
}

.gm-09:has(#gm-09-theme:checked) .gm-09__sun {
  display: none;
}

.gm-09:has(#gm-09-theme:checked) .gm-09__moon {
  display: block;
}

.gm-09[data-theme="light"] .gm-09__snip,
.gm-09:has(#gm-09-theme:checked) .gm-09__snip {
  background: rgba(14,18,32,.06);
  color: #0e1220;
}

.gm-09[data-theme="light"] .gm-09__panel,
.gm-09:has(#gm-09-theme:checked) .gm-09__panel {
  box-shadow: inset 0 1px 0 rgba(255,255,255,.9), inset 0 2px 8px rgba(20,20,50,.12), 0 22px 48px -30px rgba(24,20,60,.4);
}

@media (prefers-reduced-motion: reduce) {
  .gm-09 *,
    .gm-09 *::before,
    .gm-09 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-09__panel,
    .gm-09__theme,
    .gm-09__sp,
    .gm-09__state {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
