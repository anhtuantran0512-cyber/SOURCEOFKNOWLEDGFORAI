---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/organic-dividers/"
title: "Organic Leaf & Vine SVG Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "A botanical divider that draws itself: a single SVG vine whose stroke is animated with the dash-offset technique, with leaves fading in on staggered delays…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Organic Leaf & Vine SVG Divider CSS
Source: https://codefronts.com/snippets/css-dividers/organic-dividers/

A botanical divider that draws itself: a single SVG vine whose stroke is animated with the dash-offset technique, with leaves fading in on staggered delays so the plant appears to grow rather than appear. Everything is stroke-based and uses currentColor, so the vine inherits your text colour and scales to any width without pixelation — ideal for wellness, organic-product and editorial nature pages.
## HTML
```html
<section class="div-12" aria-label="Organic leaf and vine SVG divider demo">
  <div class="div-12__stage">
    <p class="div-12__eyebrow">stroke-dashoffset · staggered sprout</p>
    <h2 class="div-12__title">Grown, not drawn</h2>
    <div class="div-12__vine" aria-hidden="true">
      <svg viewBox="0 0 520 60" fill="none" focusable="false">
        <path class="div-12__stem" d="M8 30 C90 4, 150 56, 232 30 C314 4, 372 56, 452 30 L512 30" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        <path class="div-12__leaf" d="M96 20 C104 6, 124 6, 128 14 C120 26, 104 28, 96 20Z" fill="currentColor"/>
        <path class="div-12__leaf" d="M168 40 C176 54, 196 54, 200 46 C192 34, 176 32, 168 40Z" fill="currentColor"/>
        <path class="div-12__leaf" d="M320 20 C328 6, 348 6, 352 14 C344 26, 328 28, 320 20Z" fill="currentColor"/>
        <path class="div-12__leaf" d="M392 40 C400 54, 420 54, 424 46 C416 34, 400 32, 392 40Z" fill="currentColor"/>
        <circle class="div-12__bud" cx="260" cy="30" r="5" fill="currentColor"/>
      </svg>
    </div>
    <p class="div-12__sub">Sourced, grown and bottled within forty miles of the press that printed this label.</p>
    <div class="div-12__photo" aria-hidden="true"></div>
    <p class="div-12__chip">transform-box:fill-box · currentColor · vector-effect</p>
  </div>
</section>
```
## CSS
```css
.div-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-12-bg);
  --div-12-bg: oklch(0.965 0.022 130);
  --div-12-ink: oklch(0.3 0.045 145);
  --div-12-mut: oklch(0.52 0.04 145);
  --div-12-acc: oklch(0.52 0.11 148);
  --div-12-len: 760;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-12-ink);
}

.div-12 *,
.div-12 *::before,
.div-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-12__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(14px,2.6vw,24px);
  text-align: center;
  padding: clamp(30px,6vw,72px) clamp(20px,5vw,56px);
  background: radial-gradient(90% 70% at 50% 10%,oklch(0.99 0.012 130),transparent);
}

.div-12__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-12-acc);
}

.div-12__title {
  font-family: Georgia,'Iowan Old Style',serif;
  font-size: clamp(30px,6vw,58px);
  line-height: 1.04;
  letter-spacing: -.02em;
  font-weight: 400;
}

.div-12__vine {
  width: min(92vw,520px);
  color: var(--div-12-acc);
  line-height: 0;
}

.div-12__vine svg {
  width: 100%;
  height: auto;
  display: block;
  overflow: visible;
}

.div-12__stem {
  vector-effect: non-scaling-stroke;
  stroke-dasharray: var(--div-12-len);
  stroke-dashoffset: var(--div-12-len);
  animation: div-12-draw 2.6s cubic-bezier(.22,.61,.36,1) forwards;
}

@keyframes div-12-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.div-12__leaf,
.div-12__bud {
  opacity: 0;
  transform-box: fill-box;
  transform-origin: 0% 50%;
  animation: div-12-sprout .55s cubic-bezier(.34,1.4,.64,1) forwards;
}

.div-12__leaf:nth-of-type(2) {
  animation-delay: .75s;
}

.div-12__leaf:nth-of-type(3) {
  animation-delay: 1.05s;
}

.div-12__leaf:nth-of-type(4) {
  animation-delay: 1.75s;
}

.div-12__leaf:nth-of-type(5) {
  animation-delay: 2.05s;
}

.div-12__bud {
  transform-origin: 50% 50%;
  animation-delay: 1.4s;
}

@keyframes div-12-sprout {
  from {
    opacity: 0;
    scale: .2 .5;
  }

  to {
    opacity: 1;
    scale: 1 1;
  }
}

.div-12__sub {
  max-width: 44ch;
  font-size: clamp(14px,1.8vw,17px);
  line-height: 1.62;
  color: var(--div-12-mut);
  text-wrap: pretty;
}

.div-12__photo {
  width: min(86vw,420px);
  aspect-ratio: 16/6;
  border-radius: 200px 200px 12px 12px;
  background: linear-gradient(160deg,oklch(0.6 0.09 148),oklch(0.42 0.07 160)),url("https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?q=80&w=1200&auto=format&fit=crop") center/cover no-repeat;
  background-blend-mode: soft-light,normal;
  box-shadow: 0 14px 34px oklch(0.3 0.045 145/.22);
}

.div-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-12-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.3 0.045 145/.18);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .div-12__stem {
    animation: none;
    stroke-dashoffset: 0;
  }

  .div-12__leaf,
    .div-12__bud {
    animation: none;
    opacity: 1;
  }
}
```
