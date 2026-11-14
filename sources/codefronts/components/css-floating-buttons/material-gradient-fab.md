---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/material-gradient-fab/"
title: "Material Gradient Floating Action Button CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A gradient FAB that actually animates, because @property makes the gradient angle a typed, interpolatable value."
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Gradient Floating Action Button CSS
Source: https://codefronts.com/components/css-floating-buttons/material-gradient-fab/

A gradient FAB that actually animates, because @property makes the gradient angle a typed, interpolatable value. Includes the two-layer construction — a conic gradient ring rotating behind a solid core — plus the detail that sells it: a coloured shadow sampled from the gradient itself, so the button appears to light the surface under it.
## HTML
```html
<section class="fb-09" aria-label="Gradient floating action button demo">
  <div class="fb-09__stage">
    <p class="fb-09__eyebrow">@property &lt;angle&gt; · conic-gradient</p>
    <h2 class="fb-09__title">A border that sweeps, not spins</h2>
    <p class="fb-09__sub">The ring geometry never moves — only the colour phase advances, so the edge stays razor sharp at every size.</p>
    <div class="fb-09__row">
      <div class="fb-09__cell">
        <button class="fb-09__fab" type="button" aria-label="Create, gradient ring style">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
        <span class="fb-09__cap">ring</span>
      </div>
      <div class="fb-09__cell">
        <button class="fb-09__fab fb-09__fab--fill" type="button" aria-label="Create, gradient fill style">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
        <span class="fb-09__cap">fill</span>
      </div>
      <div class="fb-09__cell">
        <button class="fb-09__fab fb-09__fab--calm" type="button" aria-label="Create, hover activated gradient">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
        <span class="fb-09__cap">on hover</span>
      </div>
    </div>
    <p class="fb-09__chip">hue-matched shadow · blurred glow twin · 5s sweep</p>
  </div>
</section>
```
## CSS
```css
@property --fb-09-ang {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.fb-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-09-bg);
  --fb-09-bg: radial-gradient(120% 90% at 50% 0%,oklch(0.26 0.05 300),oklch(0.15 0.02 285) 70%);
  --fb-09-grad: conic-gradient(from var(--fb-09-ang),oklch(0.7 0.21 12),oklch(0.62 0.24 300),oklch(0.78 0.15 200),oklch(0.82 0.17 95),oklch(0.7 0.21 12));
  --fb-09-ink: oklch(0.97 0.01 300);
  --fb-09-mut: oklch(0.76 0.02 300);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-09-ink);
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
}

.fb-09 *,
.fb-09 *::before,
.fb-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-09__stage {
  width: min(100%,58ch);
  display: grid;
  gap: clamp(18px,3vw,28px);
  justify-items: center;
  text-align: center;
}

.fb-09__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.78 0.15 330);
}

.fb-09__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-09__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-09-mut);
  text-wrap: pretty;
  max-width: 46ch;
}

.fb-09__row {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(24px,6vw,54px);
  justify-content: center;
  padding: 8px 0;
}

.fb-09__cell {
  display: grid;
  gap: 12px;
  justify-items: center;
}

.fb-09__cap {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--fb-09-mut);
}

.fb-09__fab {
  position: relative;
  isolation: isolate;
  display: grid;
  place-items: center;
  inline-size: 68px;
  block-size: 68px;
  border: 0;
  border-radius: 22px;
  cursor: pointer;
  color: var(--fb-09-ink);
  background: linear-gradient(oklch(0.2 0.03 290),oklch(0.16 0.02 290));
  box-shadow: 0 16px 38px -12px oklch(0.62 0.24 300/.55),0 3px 8px oklch(0.1 0.02 290/.6);
  transition: transform .3s cubic-bezier(.2,1.25,.4,1),box-shadow .3s ease;
}

.fb-09__fab svg {
  width: 28px;
  height: 28px;
  position: relative;
  z-index: 2;
}

.fb-09__fab::before {
  content: "";
  position: absolute;
  inset: -2.5px;
  border-radius: inherit;
  background: var(--fb-09-grad);
  animation: fb-09-spin 5s linear infinite;
  z-index: -2;
}

.fb-09__fab::after {
  content: "";
  position: absolute;
  inset: -2.5px;
  border-radius: inherit;
  background: var(--fb-09-grad);
  filter: blur(16px);
  opacity: .55;
  animation: fb-09-spin 5s linear infinite;
  z-index: -3;
}

@keyframes fb-09-spin {
  to {
    --fb-09-ang: 360deg;
  }
}

.fb-09__fab:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 22px 46px -12px oklch(0.62 0.24 300/.7),0 3px 8px oklch(0.1 0.02 290/.6);
}

.fb-09__fab:active {
  transform: scale(.94);
}

.fb-09__fab:focus-visible {
  outline: 3px solid oklch(0.9 0.06 300);
  outline-offset: 5px;
}

.fb-09__fab--fill {
  background: var(--fb-09-grad);
  animation: fb-09-spin 5s linear infinite;
  color: oklch(0.16 0.03 290);
}

.fb-09__fab--fill::before {
  inset: 2px;
  background: none;
  box-shadow: inset 0 1px 0 oklch(1 0 0/.35);
  animation: none;
}

.fb-09__fab--calm::before,
.fb-09__fab--calm::after {
  animation-play-state: paused;
}

.fb-09__fab--calm::after {
  opacity: 0;
  transition: opacity .4s ease;
}

.fb-09__fab--calm:is(:hover,:focus-visible)::before,
.fb-09__fab--calm:is(:hover,:focus-visible)::after {
  animation-play-state: running;
}

.fb-09__fab--calm:is(:hover,:focus-visible)::after {
  opacity: .6;
}

.fb-09__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-09-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .fb-09__fab,
    .fb-09__fab::before,
    .fb-09__fab::after {
    animation: none !important;
    transition: none !important;
  }
}
```
