---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/css-gradient-button-with-hover-animation/"
title: "CSS Gradient Button with Hover Animation"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "Six production-ready gradient CTA buttons on one screen — background-position shift, shine sweep, spinning conic ring, glow lift, ghost fill and an oklch…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Button with Hover Animation
Source: https://codefronts.com/design-styles/css-gradient-ui/css-gradient-button-with-hover-animation/

Six production-ready gradient CTA buttons on one screen — background-position shift, shine sweep, spinning conic ring, glow lift, ghost fill and an oklch hue-drift — every hover animates on the compositor, no JavaScript, no repaint jank.
## HTML
```html
<div class="cgu-01-group">
<section class="cgu-01" aria-label="CSS gradient button hover animation demos">
  <div class="cgu-01__inner">
    <header class="cgu-01__head">
      <p class="cgu-01__eyebrow">01 · Gradient buttons</p>
      <h2 class="cgu-01__title">Hover every button.<br>Zero JavaScript.</h2>
      <p class="cgu-01__sub">Six compositor-only gradient hover animations — shift, sweep, spin, glow, fill and hue-drift.</p>
    </header>
    <div class="cgu-01__grid">
      <div class="cgu-01__cell"><button class="cgu-01__btn cgu-01__btn--shift" type="button">Get started free</button><p class="cgu-01__cap">Position shift · <code>background-position</code></p></div>
      <div class="cgu-01__cell"><button class="cgu-01__btn cgu-01__btn--sweep" type="button">Start building</button><p class="cgu-01__cap">Shine sweep · skewed <code>::after</code></p></div>
      <div class="cgu-01__cell"><button class="cgu-01__btn cgu-01__btn--ring" type="button">Upgrade to Pro</button><p class="cgu-01__cap">Conic ring spin · <code>@property</code> angle</p></div>
      <div class="cgu-01__cell"><button class="cgu-01__btn cgu-01__btn--glow" type="button">Deploy now</button><p class="cgu-01__cap">Glow lift · blurred <code>::before</code> twin</p></div>
      <div class="cgu-01__cell"><button class="cgu-01__btn cgu-01__btn--ghost" type="button">View pricing</button><p class="cgu-01__cap">Ghost fill · gradient border → solid</p></div>
      <div class="cgu-01__cell"><button class="cgu-01__btn cgu-01__btn--hue" type="button">Join waitlist</button><p class="cgu-01__cap">Hue drift · animated <code>oklch()</code> hue</p></div>
    </div>
    <p class="cgu-01__foot">Tab through the buttons — every effect also fires on <code>:focus-visible</code>.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-01-group {
  display: block;
  width: 100%;
}

.cgu-01,
.cgu-01 *,
.cgu-01 *::before,
.cgu-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --cgu01-a {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@property --cgu01-h {
  syntax: '<number>';
  initial-value: 290;
  inherits: false;
}

.cgu-01 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: radial-gradient(120% 90% at 50% -10%,#1b1440 0%,#0b0d16 55%,#07080e 100%);
}

.cgu-01__inner {
  width: min(1060px,100%);
  display: grid;
  gap: 44px;
}

.cgu-01__head {
  text-align: center;
  display: grid;
  gap: 14px;
  justify-items: center;
}

.cgu-01__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #8f7bff;
}

.cgu-01__title {
  font-size: clamp(30px,4.6vw,54px);
  line-height: 1.06;
  font-weight: 800;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.cgu-01__sub {
  max-width: 52ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
  text-wrap: pretty;
}

.cgu-01__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(280px,1fr));
  gap: 22px;
}

.cgu-01__cell {
  display: grid;
  gap: 14px;
  justify-items: center;
  align-content: center;
  padding: 38px 22px;
  border-radius: 20px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.07);
}

.cgu-01__cap {
  font-size: 12.5px;
  color: #8b90b0;
}

.cgu-01__cap code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  color: #b9beff;
  background: rgba(139,123,255,.12);
  padding: 1px 5px;
  border-radius: 5px;
}

.cgu-01__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font: inherit;
  font-size: 15.5px;
  font-weight: 700;
  color: #fff;
  padding: 15px 34px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
}

.cgu-01__btn:focus-visible {
  outline: 3px solid #cdd2ff;
  outline-offset: 3px;
}

.cgu-01__btn--shift {
  background: linear-gradient(120deg,#7c3aed,#ec4899,#f97316);
  background-size: 220% 100%;
  background-position: 0 0;
  transition: background-position .5s ease,box-shadow .3s;
  box-shadow: 0 14px 30px -14px rgba(236,72,153,.55);
}

.cgu-01__btn--shift:hover,
.cgu-01__btn--shift:focus-visible {
  background-position: 100% 0;
  box-shadow: 0 18px 36px -14px rgba(249,115,22,.6);
}

.cgu-01__btn--sweep {
  background: linear-gradient(135deg,oklch(0.55 0.22 265),oklch(0.6 0.24 305));
}

.cgu-01__btn--sweep::after {
  content: "";
  position: absolute;
  inset: 0 auto 0 -70%;
  width: 45%;
  background: linear-gradient(105deg,transparent,rgba(255,255,255,.55),transparent);
  transform: skewX(-18deg);
  transition: left .55s ease;
}

.cgu-01__btn--sweep:hover::after,
.cgu-01__btn--sweep:focus-visible::after {
  left: 125%;
}

.cgu-01__btn--ring {
  background: #12142a;
  border-radius: 14px;
}

.cgu-01__btn--ring::before {
  content: "";
  position: absolute;
  inset: 0;
  padding: 2px;
  border-radius: inherit;
  background: conic-gradient(from var(--cgu01-a),#22d3ee,#818cf8,#e879f9,#22d3ee);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  z-index: -1;
}

.cgu-01__btn--ring:hover::before,
.cgu-01__btn--ring:focus-visible::before {
  animation: cgu01-spin 1.6s linear infinite;
}

.cgu-01__btn--glow {
  background: linear-gradient(120deg,#06b6d4,#3b82f6);
  transition: transform .3s cubic-bezier(.2,.9,.3,1.4);
}

.cgu-01__btn--glow::before {
  content: "";
  position: absolute;
  inset: -6px;
  border-radius: inherit;
  background: inherit;
  filter: blur(18px);
  opacity: 0;
  transition: opacity .35s;
  z-index: -1;
}

.cgu-01__btn--glow:hover,
.cgu-01__btn--glow:focus-visible {
  transform: translateY(-3px);
}

.cgu-01__btn--glow:hover::before,
.cgu-01__btn--glow:focus-visible::before {
  opacity: .85;
}

.cgu-01__btn--ghost {
  background: transparent;
  border-radius: 14px;
  color: #e9d5ff;
  transition: color .35s;
}

.cgu-01__btn--ghost::before {
  content: "";
  position: absolute;
  inset: 0;
  padding: 2px;
  border-radius: inherit;
  background: linear-gradient(120deg,#a855f7,#ec4899);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}

.cgu-01__btn--ghost::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(120deg,#a855f7,#ec4899);
  opacity: 0;
  transition: opacity .35s;
  z-index: -1;
}

.cgu-01__btn--ghost:hover,
.cgu-01__btn--ghost:focus-visible {
  color: #fff;
}

.cgu-01__btn--ghost:hover::after,
.cgu-01__btn--ghost:focus-visible::after {
  opacity: 1;
}

.cgu-01__btn--hue {
  background: linear-gradient(130deg,oklch(0.55 0.24 calc(var(--cgu01-h) * 1deg)),oklch(0.68 0.2 calc((var(--cgu01-h) + 60) * 1deg)));
}

.cgu-01__btn--hue:hover,
.cgu-01__btn--hue:focus-visible {
  animation: cgu01-hue 2.4s linear infinite;
}

.cgu-01__foot {
  text-align: center;
  font-size: 13px;
  color: #7c81a3;
}

.cgu-01__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: #b9beff;
}

@keyframes cgu01-spin {
  to {
    --cgu01-a: 360deg;
  }
}

@keyframes cgu01-hue {
  to {
    --cgu01-h: 650;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-01 * {
    transition-duration: .01s!important;
    animation: none!important;
  }

  .cgu-01__btn--glow:hover::before {
    opacity: .85;
  }
}
```

## JavaScript
```js
/* No JavaScript — all six hover animations run on background-position, transform, opacity and @property-registered angle/hue custom properties. */
```
