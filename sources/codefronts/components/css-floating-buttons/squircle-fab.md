---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/squircle-fab/"
title: "Apple Squircle Superellipse Floating Button CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "The shape Apple uses for every app icon and every large control: a superellipse, where the curve flows into the straight edge instead of meeting it at a…"
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Apple Squircle Superellipse Floating Button CSS
Source: https://codefronts.com/components/css-floating-buttons/squircle-fab/

The shape Apple uses for every app icon and every large control: a superellipse, where the curve flows into the straight edge instead of meeting it at a tangent break. CSS finally has it natively — corner-shape: squircle — and this demo shows it beside a plain border-radius at the same value, plus an SVG-mask fallback for engines that have not shipped it.
## HTML
```html
<section class="fb-15" aria-label="Squircle superellipse floating button demo">
  <div class="fb-15__stage">
    <p class="fb-15__eyebrow">corner-shape: squircle</p>
    <h2 class="fb-15__title">The corner that never breaks tangent</h2>
    <p class="fb-15__sub">Same 28px radius on both. The left one arcs; the right one ramps its curvature into the edge — that is the whole difference, and you can feel it before you can name it.</p>
    <div class="fb-15__row">
      <div class="fb-15__cell">
        <button class="fb-15__fab fb-15__fab--plain" type="button" aria-label="Create, circular corners">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
        <span class="fb-15__cap">border-radius</span>
      </div>
      <div class="fb-15__cell">
        <button class="fb-15__fab fb-15__fab--sq" type="button" aria-label="Create, squircle corners">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
        <span class="fb-15__cap">+ squircle</span>
      </div>
      <div class="fb-15__cell">
        <button class="fb-15__fab fb-15__fab--bevel" type="button" aria-label="Create, bevelled corners">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
        <span class="fb-15__cap">+ bevel</span>
      </div>
      <div class="fb-15__cell">
        <button class="fb-15__fab fb-15__fab--scoop" type="button" aria-label="Create, scooped corners">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
        <span class="fb-15__cap">+ scoop</span>
      </div>
    </div>
    <div class="fb-15__overlay" aria-hidden="true">
      <span class="fb-15__ghost fb-15__ghost--plain"></span>
      <span class="fb-15__ghost fb-15__ghost--sq"></span>
      <span class="fb-15__ovLab">overlaid outlines · the flat spot is on the arc</span>
    </div>
    <p class="fb-15__chip" id="fb-15-support">superellipse curvature · @supports fallback to mask-image</p>
  </div>
</section>
```
## CSS
```css
.fb-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-15-bg);
  --fb-15-bg: oklch(0.95 0.008 250);
  --fb-15-ink: oklch(0.22 0.02 255);
  --fb-15-mut: oklch(0.53 0.015 255);
  --fb-15-brand: oklch(0.58 0.17 258);
  --fb-15-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M50 0C88 0 100 12 100 50s-12 50-50 50S0 88 0 50 12 0 50 0z" fill="black"/></svg>');
  font-family: -apple-system,'SF Pro Display','Segoe UI',system-ui,sans-serif;
  color: var(--fb-15-ink);
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
}

.fb-15 *,
.fb-15 *::before,
.fb-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-15__stage {
  width: min(100%,60ch);
  display: grid;
  gap: clamp(18px,3vw,28px);
  justify-items: center;
  text-align: center;
}

.fb-15__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-15-brand);
}

.fb-15__title {
  font-size: clamp(25px,4.4vw,42px);
  line-height: 1.06;
  letter-spacing: -.035em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-15__sub {
  max-width: 52ch;
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-15-mut);
  text-wrap: pretty;
}

.fb-15__row {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(18px,5vw,42px);
  justify-content: center;
}

.fb-15__cell {
  display: grid;
  gap: 11px;
  justify-items: center;
}

.fb-15__cap {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .06em;
  color: var(--fb-15-mut);
}

.fb-15__fab {
  display: grid;
  place-items: center;
  inline-size: 76px;
  block-size: 76px;
  border: 0;
  border-radius: 28px;
  cursor: pointer;
  color: oklch(0.99 0.01 258);
  background: linear-gradient(155deg,oklch(0.68 0.16 250),oklch(0.46 0.18 265));
  box-shadow: 0 14px 32px -14px oklch(0.4 0.14 258/.9),0 2px 5px oklch(0.3 0.06 258/.22);
  transition: transform .3s cubic-bezier(.2,1.25,.4,1),box-shadow .3s ease;
}

.fb-15__fab svg {
  width: 29px;
  height: 29px;
}

.fb-15__fab:hover {
  transform: translateY(-3px);
  box-shadow: 0 20px 42px -14px oklch(0.4 0.14 258/.95);
}

.fb-15__fab:active {
  transform: scale(.94);
}

.fb-15__fab:focus-visible {
  outline: 3px solid oklch(0.46 0.18 265);
  outline-offset: 4px;
}

.fb-15__fab--sq {
  -webkit-mask-image: var(--fb-15-mask);
  mask-image: var(--fb-15-mask);
  -webkit-mask-size: 100% 100%;
  mask-size: 100% 100%;
  box-shadow: none;
  filter: drop-shadow(0 12px 22px oklch(0.4 0.14 258/.45));
}

@supports (corner-shape: squircle) {
  .fb-15__fab--sq {
    -webkit-mask-image: none;
    mask-image: none;
    corner-shape: squircle;
    filter: none;
    box-shadow: 0 14px 32px -14px oklch(0.4 0.14 258/.9),0 2px 5px oklch(0.3 0.06 258/.22);
  }

  .fb-15__fab--bevel {
    corner-shape: bevel;
  }

  .fb-15__fab--scoop {
    corner-shape: scoop;
    border-radius: 22px;
  }
}

.fb-15__fab--bevel {
  background: linear-gradient(155deg,oklch(0.78 0.14 190),oklch(0.5 0.13 205));
}

.fb-15__fab--scoop {
  background: linear-gradient(155deg,oklch(0.8 0.14 90),oklch(0.6 0.16 45));
}

.fb-15__overlay {
  position: relative;
  width: min(100%,320px);
  height: 120px;
  display: grid;
  place-items: center;
}

.fb-15__ghost {
  position: absolute;
  width: 96px;
  height: 96px;
  border-radius: 34px;
}

.fb-15__ghost--plain {
  border: 2px dashed oklch(0.55 0.02 255/.55);
}

.fb-15__ghost--sq {
  border: 2px solid var(--fb-15-brand);
  -webkit-mask-image: none;
  mask-image: none;
}

@supports (corner-shape: squircle) {
  .fb-15__ghost--sq {
    corner-shape: squircle;
  }
}

.fb-15__ovLab {
  position: absolute;
  bottom: 0;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  color: var(--fb-15-mut);
}

.fb-15__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-15-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.22 0.02 255/.14);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .fb-15__fab {
    transition: none;
  }
}
```
