---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/glass-tint-overlay-variants/"
title: "Glass Tint Overlay Variants"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "Six glass panels over one background, each tinted with color-mix(in oklab, …) so the tint carries meaning — info, success, warning, danger, neutral and brand."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Tint Overlay Variants
Source: https://codefronts.com/design-styles/css-glassmorphism/glass-tint-overlay-variants/

Six glass panels over one background, each tinted with color-mix(in oklab, …) so the tint carries meaning — info, success, warning, danger, neutral and brand. Because the mix happens in oklab, every hue lands at the same perceived lightness, which is what keeps a semantic set looking like a set instead of six unrelated colours.
## HTML
```html
<div class="gm-04">
  <input class="gm-04__sr" type="checkbox" id="gm-04-theme">
  <label class="gm-04__theme" for="gm-04-theme" title="Switch theme">
    <svg class="gm-04__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-04__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-04__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-04__stage">
    <section class="gm-04__wrap" aria-labelledby="gm-04-h">
      <header class="gm-04__head">
        <p class="gm-04__eyebrow">color-mix(in oklab, …)</p>
        <h2 class="gm-04__h" id="gm-04-h">Tint that carries meaning</h2>
        <p class="gm-04__sub">Six semantic states, one glass recipe, one mix percentage. Perceptual mixing keeps every hue at the same visual weight.</p>
      </header>

      <ul class="gm-04__grid">
        <li class="gm-04__panel gm-04__panel--info">
          <span class="gm-04__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M12 10.6v6M12 7.4h.01" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>
          <h3 class="gm-04__label">Info</h3>
          <p class="gm-04__mix">oklch(.72 .16 240) 26%</p>
          <p class="gm-04__copy">Build 4.12 is rolling out to the EU edge region.</p>
        </li>
        <li class="gm-04__panel gm-04__panel--success">
          <span class="gm-04__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M8 12.4l2.8 2.7L16 9.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <h3 class="gm-04__label">Success</h3>
          <p class="gm-04__mix">oklch(.76 .17 150) 26%</p>
          <p class="gm-04__copy">All 214 visual snapshots matched the baseline.</p>
        </li>
        <li class="gm-04__panel gm-04__panel--warn">
          <span class="gm-04__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M12 4.2 21 19.4H3L12 4.2Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M12 10v4.1M12 16.7h.01" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>
          <h3 class="gm-04__label">Warning</h3>
          <p class="gm-04__mix">oklch(.84 .16 85) 26%</p>
          <p class="gm-04__copy">Bundle grew 42 kB — over the 180 kB budget.</p>
        </li>
        <li class="gm-04__panel gm-04__panel--danger">
          <span class="gm-04__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M9 9l6 6M15 9l-6 6" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>
          <h3 class="gm-04__label">Danger</h3>
          <p class="gm-04__mix">oklch(.66 .21 22) 26%</p>
          <p class="gm-04__copy">Payment webhook failed 3× — retries exhausted.</p>
        </li>
        <li class="gm-04__panel gm-04__panel--neutral">
          <span class="gm-04__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><rect x="4" y="6" width="16" height="12" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M4 10.5h16" stroke="currentColor" stroke-width="1.7"/></svg></span>
          <h3 class="gm-04__label">Neutral</h3>
          <p class="gm-04__mix">oklch(.72 .02 265) 26%</p>
          <p class="gm-04__copy">Draft saved locally. Nothing published yet.</p>
        </li>
        <li class="gm-04__panel gm-04__panel--brand">
          <span class="gm-04__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M12 3.6l2.6 5.5 6 .8-4.4 4.2 1.1 6-5.3-2.9-5.3 2.9 1.1-6L3.4 9.9l6-.8L12 3.6Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
          <h3 class="gm-04__label">Brand</h3>
          <p class="gm-04__mix">oklch(.65 .2 285) 26%</p>
          <p class="gm-04__copy">Priya Sharma invited you to the Atlas workspace.</p>
        </li>
      </ul>

      <p class="gm-04__foot">Every panel pairs tint with an icon and a word — colour is reinforcement, never the only signal.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-04 {
  --a1: rgba(125,211,252,.5);
  --a2: rgba(196,181,253,.55);
  --a3: rgba(253,164,175,.45);
  --a4: rgba(110,231,183,.45);
  --base: #f0f3fa;
  --base2: #e2e8fb;
  --ink: #101322;
  --muted: rgba(16,19,34,.66);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(16,19,34,.1);
  --info: #60a5fa;
  --success: #34d399;
  --warn: #fbbf24;
  --danger: #fb7185;
  --neutral: #64748b;
  --brand: #a78bfa;
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
  background: radial-gradient(50% 42% at 10% 18%, var(--a1) 0%, transparent 60%), radial-gradient(54% 46% at 88% 20%, var(--a2) 0%, transparent 62%), radial-gradient(48% 42% at 74% 88%, var(--a3) 0%, transparent 60%), radial-gradient(46% 40% at 18% 92%, var(--a4) 0%, transparent 60%), linear-gradient(158deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-04 *,
.gm-04 *::before,
.gm-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-04 {
    --a1: oklch(0.78 0.16 220 / .52);
    --a2: oklch(0.68 0.24 305 / .56);
    --a3: oklch(0.72 0.19 15 / .46);
    --a4: oklch(0.8 0.15 165 / .42);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
    --info: oklch(0.72 0.16 240);
    --success: oklch(0.76 0.17 150);
    --warn: oklch(0.84 0.16 85);
    --danger: oklch(0.66 0.21 22);
    --neutral: oklch(0.72 0.02 265);
    --brand: oklch(0.65 0.2 285);
  }
}

.gm-04__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-04__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 6;
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

.gm-04__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-04__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-04__theme:hover {
  scale: 1.06;
}

.gm-04__sr:focus-visible + .gm-04__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-04__moon {
  display: none;
}

.gm-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-04__wrap {
  inline-size: min(74rem,100%);
}

.gm-04__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 44rem;
  margin-block-end: clamp(1.5rem,3.5vw,2.5rem);
}

.gm-04__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-04__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-04__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-04__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(.9rem,1.8vw,1.3rem);
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
}

.gm-04__panel {
  --hue: #94a3b8;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .35rem .75rem;
  align-items: center;
  padding: clamp(1rem,1.7vw,1.35rem);
  border-radius: 1.15rem;
  background: rgba(148,163,184,.26);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 22px 50px -26px rgba(0,0,0,.6);
  transition: translate .22s cubic-bezier(.2,.7,.3,1);
}

@supports (background: color-mix(in oklab, red 10%, transparent)) {
  .gm-04__panel {
    background: color-mix(in oklab, var(--hue) 26%, transparent);
    border-color: color-mix(in oklab, var(--hue) 45%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-04__panel {
    -webkit-backdrop-filter: blur(22px) saturate(165%);
    backdrop-filter: blur(22px) saturate(165%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-04__panel {
    background: rgba(20,16,50,.86);
  }
}

.gm-04__panel--info {
  --hue: var(--info);
}

.gm-04__panel--success {
  --hue: var(--success);
}

.gm-04__panel--warn {
  --hue: var(--warn);
}

.gm-04__panel--danger {
  --hue: var(--danger);
}

.gm-04__panel--neutral {
  --hue: var(--neutral);
}

.gm-04__panel--brand {
  --hue: var(--brand);
}

.gm-04__panel:hover {
  translate: 0 -3px;
}

.gm-04__ico {
  grid-row: span 2;
  display: grid;
  place-items: center;
  inline-size: 2.4rem;
  block-size: 2.4rem;
  border-radius: .8rem;
  background: rgba(255,255,255,.18);
  border: 1px solid var(--rim2);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-04__ico svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.gm-04__label {
  margin: 0;
  align-self: end;
  font-size: 1.02rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.gm-04__mix {
  margin: 0;
  align-self: start;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .02em;
  color: var(--muted);
}

.gm-04__copy {
  grid-column: 1 / -1;
  margin: .4rem 0 0;
  padding-block-start: .7rem;
  border-block-start: 1px solid var(--rim2);
  font-size: .9rem;
  line-height: 1.5;
  color: var(--ink);
  text-wrap: pretty;
}

.gm-04__foot {
  margin: clamp(1.1rem,2vw,1.6rem) 0 0;
  font-size: .9rem;
  color: var(--muted);
}

.gm-04[data-theme="light"],
.gm-04:has(#gm-04-theme:checked) {
  --a1: rgba(56,189,248,.5);
  --a2: rgba(168,85,247,.55);
  --a3: rgba(251,113,133,.45);
  --a4: rgba(52,211,153,.4);
  --base: #070a16;
  --base2: #141033;
  --ink: #f8fafd;
  --muted: rgba(248,250,253,.7);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.18);
  --neutral: #a5b4cf;
}

.gm-04:has(#gm-04-theme:checked) .gm-04__sun {
  display: none;
}

.gm-04:has(#gm-04-theme:checked) .gm-04__moon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .gm-04 *,
    .gm-04 *::before,
    .gm-04 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-04__panel,
    .gm-04__theme,
    .gm-04__ico {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
