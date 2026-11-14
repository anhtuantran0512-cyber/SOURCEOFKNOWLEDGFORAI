---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/css-gradient-card-with-hover-lift/"
title: "CSS Gradient Card with Hover Lift"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A three-card feature row where each card owns a distinct gradient identity — on hover it lifts with a hue-matched shadow (via color-mix), its gradient…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Card with Hover Lift
Source: https://codefronts.com/design-styles/css-gradient-ui/css-gradient-card-with-hover-lift/

A three-card feature row where each card owns a distinct gradient identity — on hover it lifts with a hue-matched shadow (via color-mix), its gradient drifts, and the CTA arrow slides. The whole card is a single link hit-target.
## HTML
```html
<div class="cgu-02-group">
<section class="cgu-02" aria-label="CSS gradient card hover lift demos">
  <div class="cgu-02__inner">
    <header class="cgu-02__head">
      <p class="cgu-02__eyebrow">02 · Gradient cards</p>
      <h2 class="cgu-02__title">One <code>--tint</code>, a whole card theme</h2>
      <p class="cgu-02__sub">Hover a card: hue-matched lift shadow, gradient drift and a sliding arrow — all derived from a single custom property.</p>
    </header>
    <div class="cgu-02__grid">
      <article class="cgu-02__card cgu-02__card--violet">
        <span class="cgu-02__chip" aria-hidden="true">◈</span>
        <h3 class="cgu-02__name">Design tokens</h3>
        <p class="cgu-02__body">Ship one palette that themes every surface, state and shadow automatically.</p>
        <a class="cgu-02__cta" href="#tokens">Explore tokens <span class="cgu-02__arrow" aria-hidden="true">→</span></a>
      </article>
      <article class="cgu-02__card cgu-02__card--cyan">
        <span class="cgu-02__chip" aria-hidden="true">◎</span>
        <h3 class="cgu-02__name">Live previews</h3>
        <p class="cgu-02__body">Every component renders in an isolated sandbox with real props and real data.</p>
        <a class="cgu-02__cta" href="#previews">See it live <span class="cgu-02__arrow" aria-hidden="true">→</span></a>
      </article>
      <article class="cgu-02__card cgu-02__card--amber">
        <span class="cgu-02__chip" aria-hidden="true">✦</span>
        <h3 class="cgu-02__name">Zero-config export</h3>
        <p class="cgu-02__body">Copy production CSS with fallbacks, reduced-motion and focus states included.</p>
        <a class="cgu-02__cta" href="#export">Copy the CSS <span class="cgu-02__arrow" aria-hidden="true">→</span></a>
      </article>
    </div>
    <p class="cgu-02__foot">Cards are full-card links via the stretched-link <code>::after</code> pattern — one clean <code>&lt;a&gt;</code> per card.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-02-group {
  display: block;
  width: 100%;
}

.cgu-02,
.cgu-02 *,
.cgu-02 *::before,
.cgu-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-02 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: #0c0e17;
}

.cgu-02__inner {
  width: min(1080px,100%);
  display: grid;
  gap: 42px;
}

.cgu-02__head {
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cgu-02__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #67e8f9;
}

.cgu-02__title {
  font-size: clamp(28px,4.2vw,48px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.08;
  text-wrap: balance;
}

.cgu-02__title code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .82em;
  color: #8be9fd;
  background: rgba(103,232,249,.1);
  padding: 2px 10px;
  border-radius: 10px;
}

.cgu-02__sub {
  max-width: 56ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
  text-wrap: pretty;
}

.cgu-02__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(260px,1fr));
  gap: 22px;
}

.cgu-02__card {
  --tint: oklch(0.62 0.22 275);
  position: relative;
  isolation: isolate;
  display: grid;
  gap: 14px;
  align-content: start;
  padding: 30px 28px 26px;
  border-radius: 22px;
  border: 1px solid color-mix(in oklab,var(--tint) 28%,transparent);
  background: linear-gradient(160deg,color-mix(in oklab,var(--tint) 30%,#12131f) 0%,#12131f 65%);
  background-size: 150% 150%;
  background-position: 0% 0%;
  box-shadow: 0 14px 30px -22px color-mix(in oklab,var(--tint) 35%,transparent);
  transition: transform .38s cubic-bezier(.2,.9,.3,1.15),box-shadow .38s,background-position .5s;
}

.cgu-02__card--violet {
  --tint: oklch(0.6 0.24 295);
}

.cgu-02__card--cyan {
  --tint: oklch(0.72 0.15 210);
}

.cgu-02__card--amber {
  --tint: oklch(0.75 0.16 70);
}

.cgu-02__card:hover,
.cgu-02__card:focus-within {
  transform: translateY(-8px);
  background-position: 80% 60%;
  box-shadow: 0 26px 50px -22px color-mix(in oklab,var(--tint) 55%,transparent);
}

.cgu-02__chip {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 13px;
  font-size: 19px;
  color: #fff;
  background: linear-gradient(140deg,color-mix(in oklab,var(--tint) 85%,white),var(--tint));
}

.cgu-02__name {
  font-size: 19px;
  font-weight: 750;
}

.cgu-02__body {
  font-size: 14px;
  line-height: 1.62;
  color: #b6bad4;
  text-wrap: pretty;
}

.cgu-02__cta {
  margin-top: 6px;
  font-size: 14px;
  font-weight: 700;
  color: color-mix(in oklab,var(--tint) 60%,white);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 7px;
}

.cgu-02__cta::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
}

.cgu-02__cta:focus-visible {
  outline: none;
}

.cgu-02__card:has(.cgu-02__cta:focus-visible) {
  outline: 3px solid color-mix(in oklab,var(--tint) 70%,white);
  outline-offset: 3px;
}

.cgu-02__arrow {
  display: inline-block;
  transition: transform .3s cubic-bezier(.2,.9,.3,1.4);
}

.cgu-02__card:hover .cgu-02__arrow,
.cgu-02__card:focus-within .cgu-02__arrow {
  transform: translateX(6px);
}

.cgu-02__foot {
  text-align: center;
  font-size: 13px;
  color: #7c81a3;
}

.cgu-02__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: #8be9fd;
}

@media (prefers-reduced-motion: reduce) {
  .cgu-02__card,
    .cgu-02__arrow {
    transition: box-shadow .2s;
  }

  .cgu-02__card:hover,
    .cgu-02__card:focus-within {
    transform: none;
    background-position: 0% 0%;
  }
}
```

## JavaScript
```js
/* No JavaScript — lift is transform-only, shadow and theme derive from one --tint custom property via color-mix(). */
```
