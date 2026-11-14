---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/css-gradient-border-card/"
title: "CSS Gradient Border Card"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "The three canonical ways to draw a gradient border that respects border-radius — the double-background trick, the mask-composite ring, and a rotating conic…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Border Card
Source: https://codefronts.com/design-styles/css-gradient-ui/css-gradient-border-card/

The three canonical ways to draw a gradient border that respects border-radius — the double-background trick, the mask-composite ring, and a rotating conic tracer — each on its own labelled card so you can compare the techniques side by side.
## HTML
```html
<div class="cgu-03-group">
<section class="cgu-03" aria-label="CSS gradient border card technique demos">
  <div class="cgu-03__inner">
    <header class="cgu-03__head">
      <p class="cgu-03__eyebrow">03 · Gradient borders</p>
      <h2 class="cgu-03__title">Gradient borders that respect <code>border-radius</code></h2>
      <p class="cgu-03__sub">border-image can't do rounded corners — these three patterns can. Hover each card to see its border react.</p>
    </header>
    <div class="cgu-03__grid">
      <article class="cgu-03__card cgu-03__card--double">
        <p class="cgu-03__tech">Technique A</p>
        <h3 class="cgu-03__name">Double background</h3>
        <p class="cgu-03__body">Opaque fill on <code>padding-box</code> over a gradient on <code>border-box</code>. One declaration, zero pseudo-elements.</p>
        <p class="cgu-03__meta">Best for: solid cards, inputs, buttons</p>
      </article>
      <article class="cgu-03__card cgu-03__card--mask">
        <p class="cgu-03__tech">Technique B</p>
        <h3 class="cgu-03__name">Mask-composite ring</h3>
        <p class="cgu-03__body">A gradient pseudo-element hollowed with <code>mask-composite: exclude</code> — the middle stays fully transparent.</p>
        <p class="cgu-03__meta">Best for: glass cards, image overlays</p>
      </article>
      <article class="cgu-03__card cgu-03__card--orbit">
        <p class="cgu-03__tech">Technique C</p>
        <h3 class="cgu-03__name">Conic orbit tracer</h3>
        <p class="cgu-03__body">Technique B with a <code>conic-gradient</code> fill whose <code>@property</code> angle rotates forever — an orbiting light.</p>
        <p class="cgu-03__meta">Best for: featured plans, AI surfaces</p>
      </article>
    </div>
    <p class="cgu-03__foot">Card B sits on a photo strip on purpose — notice its centre stays see-through.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-03-group {
  display: block;
  width: 100%;
}

.cgu-03,
.cgu-03 *,
.cgu-03 *::before,
.cgu-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --cgu03-a {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.cgu-03 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: linear-gradient(180deg,#0a0c14 0%,#10121f 100%);
}

.cgu-03__inner {
  width: min(1080px,100%);
  display: grid;
  gap: 42px;
}

.cgu-03__head {
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cgu-03__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #e879f9;
}

.cgu-03__title {
  font-size: clamp(27px,4vw,46px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  text-wrap: balance;
}

.cgu-03__title code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .8em;
  color: #f0abfc;
  background: rgba(232,121,249,.1);
  padding: 2px 10px;
  border-radius: 10px;
}

.cgu-03__sub {
  max-width: 58ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
  text-wrap: pretty;
}

.cgu-03__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(270px,1fr));
  gap: 24px;
}

.cgu-03__card {
  position: relative;
  isolation: isolate;
  display: grid;
  gap: 12px;
  align-content: start;
  padding: 30px 28px;
  border-radius: 22px;
  min-height: 230px;
}

.cgu-03__tech {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: #8b90b0;
}

.cgu-03__name {
  font-size: 20px;
  font-weight: 750;
}

.cgu-03__body {
  font-size: 14px;
  line-height: 1.62;
  color: #b6bad4;
  text-wrap: pretty;
}

.cgu-03__body code,
.cgu-03__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: #8be9fd;
  background: rgba(103,232,249,.08);
  padding: 1px 5px;
  border-radius: 5px;
}

.cgu-03__meta {
  margin-top: auto;
  font-size: 12.5px;
  font-weight: 600;
  color: #7c81a3;
}

.cgu-03__card--double {
  border: 2px solid transparent;
  background: linear-gradient(#141626,#141626) padding-box,linear-gradient(135deg,#22d3ee,#818cf8,#e879f9) border-box;
  transition: box-shadow .35s;
}

.cgu-03__card--double:hover {
  box-shadow: 0 18px 44px -20px rgba(129,140,248,.5);
}

.cgu-03__card--mask {
  background: linear-gradient(120deg,rgba(34,211,238,.12),rgba(232,121,249,.12)) ,repeating-linear-gradient(45deg,rgba(255,255,255,.045) 0 12px,transparent 12px 24px);
}

.cgu-03__card--mask::before {
  content: "";
  position: absolute;
  inset: 0;
  padding: 2px;
  border-radius: inherit;
  background: linear-gradient(200deg,#34d399,#22d3ee,#818cf8);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  transition: padding .3s;
}

.cgu-03__card--mask:hover::before {
  padding: 4px;
}

.cgu-03__card--orbit {
  background: #12142a;
}

.cgu-03__card--orbit::before {
  content: "";
  position: absolute;
  inset: 0;
  padding: 2px;
  border-radius: inherit;
  background: conic-gradient(from var(--cgu03-a),transparent 0 18%,#f472b6 28%,#fbbf24 36%,transparent 46%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: cgu03-orbit 3.2s linear infinite;
}

.cgu-03__card--orbit::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  box-shadow: inset 0 0 0 1px rgba(244,114,182,.18);
  z-index: -1;
}

.cgu-03__card--orbit:hover::before {
  animation-duration: 1.4s;
}

.cgu-03__foot {
  text-align: center;
  font-size: 13px;
  color: #7c81a3;
}

@keyframes cgu03-orbit {
  to {
    --cgu03-a: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-03__card--orbit::before {
    animation: none;
    background: conic-gradient(from 210deg,transparent 0 18%,#f472b6 28%,#fbbf24 36%,transparent 46%);
  }
}
```

## JavaScript
```js
/* No JavaScript — three border techniques: padding-box/border-box double background, mask-composite ring, and a @property-animated conic tracer. */
```
