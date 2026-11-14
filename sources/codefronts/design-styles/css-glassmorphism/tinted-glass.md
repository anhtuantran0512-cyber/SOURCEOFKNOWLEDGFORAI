---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/tinted-glass/"
title: "Tinted Frosted Glass Panel"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "One brand hue — oklch(0.65 0.2 285) — carried through a single large panel at three labelled intensities, so you can see exactly how much tint your surface…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tinted Frosted Glass Panel
Source: https://codefronts.com/design-styles/css-glassmorphism/tinted-glass/

One brand hue — oklch(0.65 0.2 285) — carried through a single large panel at three labelled intensities, so you can see exactly how much tint your surface can take before the copy on it stops being readable. This is the single-hue depth reference; demo 04 is the multi-hue semantic set.
## HTML
```html
<div class="gm-21">
  <input class="gm-21__sr" type="checkbox" id="gm-21-theme">
  <label class="gm-21__theme" for="gm-21-theme" title="Switch theme">
    <svg class="gm-21__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-21__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-21__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-21__stage">
    <section class="gm-21__panel" aria-labelledby="gm-21-h">
      <header class="gm-21__head">
        <p class="gm-21__eyebrow">brand tint · oklch(0.65 0.2 285)</p>
        <h2 class="gm-21__h" id="gm-21-h">How much brand can glass carry?</h2>
        <p class="gm-21__sub">One hue, three mix percentages, one blur. The answer is: more than you think for chrome, less than you hope for body copy.</p>
      </header>

      <div class="gm-21__ramp">
        <article class="gm-21__band gm-21__band--soft">
          <div class="gm-21__btop">
            <p class="gm-21__pct">14%</p>
            <p class="gm-21__blabel">Ambient</p>
          </div>
          <p class="gm-21__bcopy">Barely-there brand presence. Safe for long-form copy, sidebars and anything a user reads for more than a few seconds.</p>
          <p class="gm-21__bnote">contrast: comfortable · body text OK</p>
        </article>

        <article class="gm-21__band gm-21__band--mid">
          <div class="gm-21__btop">
            <p class="gm-21__pct">28%</p>
            <p class="gm-21__blabel">Product</p>
          </div>
          <p class="gm-21__bcopy">The default brand surface. Clearly tinted, still transparent enough that the backdrop mesh reads through it as movement and colour.</p>
          <p class="gm-21__bnote">contrast: verify per backdrop · UI copy OK</p>
        </article>

        <article class="gm-21__band gm-21__band--deep">
          <div class="gm-21__btop">
            <p class="gm-21__pct">42%</p>
            <p class="gm-21__blabel">Chrome</p>
          </div>
          <p class="gm-21__bcopy">Heavily branded. Use for headers, badges and call-out chrome — at this depth paragraph text over a bright backdrop starts failing 4.5:1.</p>
          <p class="gm-21__bnote">contrast: headings only · avoid paragraphs</p>
        </article>
      </div>

      <footer class="gm-21__foot">
        <p class="gm-21__fcopy">Rim and border are mixed from the same hue, so the edge stays on-brand instead of reading as a white outline stuck on top of a coloured box.</p>
        <code class="gm-21__snip">background: color-mix(in oklab, var(--brand) 28%, transparent)</code>
      </footer>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-21 {
  --brand: #8b5cf6;
  --a1: rgba(196,181,253,.6);
  --a2: rgba(125,211,252,.5);
  --a3: rgba(249,168,212,.5);
  --a4: rgba(254,240,138,.45);
  --base: #f2f1fb;
  --base2: #e6e2fc;
  --ink: #120f22;
  --muted: rgba(18,15,34,.68);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(18,15,34,.12);
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
  background: radial-gradient(54% 46% at 12% 14%, var(--a1) 0%, transparent 62%), radial-gradient(48% 42% at 88% 18%, var(--a2) 0%, transparent 58%), radial-gradient(50% 44% at 80% 88%, var(--a3) 0%, transparent 60%), radial-gradient(40% 34% at 16% 90%, var(--a4) 0%, transparent 56%), linear-gradient(162deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-21 *,
.gm-21 *::before,
.gm-21 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-21 {
    --brand: oklch(0.65 0.2 285);
    --a1: oklch(0.62 0.24 295 / .62);
    --a2: oklch(0.78 0.16 220 / .52);
    --a3: oklch(0.7 0.24 350 / .46);
    --a4: oklch(0.88 0.16 95 / .32);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
  }
}

.gm-21__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-21__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-21__theme {
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

.gm-21__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-21__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-21__theme:hover {
  scale: 1.06;
}

.gm-21__sr:focus-visible + .gm-21__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-21__moon {
  display: none;
}

.gm-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-21__panel {
  inline-size: min(62rem,100%);
  display: grid;
  gap: clamp(1.1rem,2.4vw,1.75rem);
  padding: clamp(1.4rem,3vw,2.25rem);
  border-radius: 1.9rem;
  background: rgba(139,92,246,.18);
  border: 1px solid rgba(196,181,253,.4);
  -webkit-backdrop-filter: blur(26px) saturate(170%);
  backdrop-filter: blur(26px) saturate(170%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), inset 0 -1px 0 var(--rim2), 0 38px 84px -34px rgba(0,0,0,.75);
}

@supports (background: color-mix(in oklab, red 10%, transparent)) {
  .gm-21__panel {
    background: color-mix(in oklab, var(--brand) 18%, transparent);
    border-color: color-mix(in oklab, var(--brand) 40%, white 25%);
    box-shadow: inset 0 1px 0 color-mix(in oklab, white 65%, var(--brand)), inset 0 -1px 0 var(--rim2), 0 38px 84px -34px rgba(0,0,0,.75);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-21__panel {
    background: rgba(48,26,92,.94);
  }
}

.gm-21__head {
  display: grid;
  gap: .5rem;
  max-inline-size: 44rem;
}

.gm-21__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-21__h {
  margin: 0;
  font-size: clamp(1.75rem,4.2vw,2.7rem);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1.06;
  text-wrap: balance;
}

.gm-21__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.6;
  color: var(--ink);
  opacity: .84;
  text-wrap: pretty;
}

.gm-21__ramp {
  display: grid;
  gap: clamp(.85rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
}

.gm-21__band {
  --pct: 28%;
  display: flex;
  flex-direction: column;
  gap: .55rem;
  padding: clamp(1.05rem,1.9vw,1.4rem);
  border-radius: 1.35rem;
  background: rgba(139,92,246,.28);
  border: 1px solid rgba(196,181,253,.4);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  backdrop-filter: blur(20px) saturate(170%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45), inset 0 -1px 0 var(--rim2);
}

@supports (background: color-mix(in oklab, red 10%, transparent)) {
  .gm-21__band {
    background: color-mix(in oklab, var(--brand) var(--pct), transparent);
    border-color: color-mix(in oklab, var(--brand) 45%, white 30%);
    box-shadow: inset 0 1px 0 color-mix(in oklab, white 60%, var(--brand)), inset 0 -1px 0 var(--rim2);
  }
}

.gm-21__band--soft {
  --pct: 14%;
  background: rgba(139,92,246,.14);
}

.gm-21__band--mid {
  --pct: 28%;
  background: rgba(139,92,246,.28);
}

.gm-21__band--deep {
  --pct: 42%;
  background: rgba(139,92,246,.42);
}

@supports (background: color-mix(in oklab, red 10%, transparent)) {
  .gm-21__band--soft,
    .gm-21__band--mid,
    .gm-21__band--deep {
    background: color-mix(in oklab, var(--brand) var(--pct), transparent);
  }
}

.gm-21__btop {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: .8rem;
}

.gm-21__pct {
  margin: 0;
  font-family: var(--mono);
  font-size: 1.5rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.02em;
}

.gm-21__blabel {
  margin: 0;
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-21__bcopy {
  margin: 0;
  font-size: .92rem;
  line-height: 1.55;
  color: var(--ink);
  opacity: .9;
  text-wrap: pretty;
}

.gm-21__bnote {
  margin: auto 0 0;
  padding-block-start: .75rem;
  border-block-start: 1px solid var(--rim2);
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.gm-21__foot {
  display: grid;
  gap: .6rem;
  padding-block-start: clamp(.9rem,1.8vw,1.25rem);
  border-block-start: 1px solid var(--rim2);
}

.gm-21__fcopy {
  margin: 0;
  max-inline-size: 46rem;
  font-size: .9rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-21__snip {
  display: block;
  justify-self: start;
  padding: .55rem .8rem;
  border-radius: .65rem;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--ink);
  background: rgba(0,0,0,.3);
  border: 1px solid var(--rim2);
  overflow-wrap: anywhere;
}

.gm-21[data-theme="light"],
.gm-21:has(#gm-21-theme:checked) {
  --a1: rgba(139,92,246,.6);
  --a2: rgba(56,189,248,.5);
  --a3: rgba(236,72,153,.45);
  --a4: rgba(250,204,21,.3);
  --base: #06060f;
  --base2: #150f33;
  --ink: #f9f8fe;
  --muted: rgba(249,248,254,.7);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.15);
  --edge: rgba(255,255,255,.2);
}

.gm-21:has(#gm-21-theme:checked) .gm-21__sun {
  display: none;
}

.gm-21:has(#gm-21-theme:checked) .gm-21__moon {
  display: block;
}

.gm-21[data-theme="light"] .gm-21__snip,
.gm-21:has(#gm-21-theme:checked) .gm-21__snip {
  background: rgba(255,255,255,.6);
  border-color: rgba(18,15,34,.12);
}

.gm-21[data-theme="light"] .gm-21__band--deep,
.gm-21:has(#gm-21-theme:checked) .gm-21__band--deep {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .gm-21 *,
    .gm-21 *::before,
    .gm-21 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-21__panel,
    .gm-21__band,
    .gm-21__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
    color: CanvasText;
  }
}
```
