---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/plus-minus-morph/"
title: "Plus / Minus Morph Accordion — CSS-Drawn Icon Animation"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The beloved plus-to-minus toggle done right: the icon is two CSS-drawn bars (no icon font, no SVG request) where the vertical bar rotates 90° into the…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Plus / Minus Morph Accordion — CSS-Drawn Icon Animation
Source: https://codefronts.com/navigation/css-accordions/plus-minus-morph/

The beloved plus-to-minus toggle done right: the icon is two CSS-drawn bars (no icon font, no SVG request) where the vertical bar rotates 90° into the horizontal on open — so plus visually MORPHS into minus instead of swapping. Wrapped in a warm two-tone card list for product marketing FAQ sections.
## HTML
```html
<section class="acc-09" aria-label="Plus minus morph accordion demo">
  <div class="acc-09__wrap">
    <h3 class="acc-09__title">Everything about pricing</h3>
    <details class="acc-09__item" open>
      <summary class="acc-09__sum">Is there a free tier?<span class="acc-09__pm"></span></summary>
      <div class="acc-09__body"><p>Yes — up to 3 projects and 2 collaborators, forever. No credit card, no trial clock. You upgrade only when your team does.</p></div>
    </details>
    <details class="acc-09__item">
      <summary class="acc-09__sum">What happens when my trial ends?<span class="acc-09__pm"></span></summary>
      <div class="acc-09__body"><p>Your workspace becomes read-only — nothing is deleted. Export everything anytime, or upgrade to pick up exactly where you left off.</p></div>
    </details>
    <details class="acc-09__item">
      <summary class="acc-09__sum">Do you offer nonprofit discounts?<span class="acc-09__pm"></span></summary>
      <div class="acc-09__body"><p>Registered nonprofits and accredited classrooms get 50% off every plan. Apply from settings with your registration number — approval takes about a day.</p></div>
    </details>
    <details class="acc-09__item">
      <summary class="acc-09__sum">Can I switch plans mid-cycle?<span class="acc-09__pm"></span></summary>
      <div class="acc-09__body"><p>Anytime. Upgrades prorate instantly; downgrades apply at the next renewal so you never lose paid time.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-09,
.acc-09 *,
.acc-09 *::before,
.acc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-09 {
  --accent: oklch(0.55 0.16 160);
  --ico: 22px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eff5f1;
  padding: 40px 20px;
}

.acc-09__wrap {
  width: min(580px,100%);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.acc-09__title {
  font-size: 25px;
  font-weight: 800;
  color: #16281f;
  letter-spacing: -.02em;
  margin-bottom: 8px;
}

.acc-09__item {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 10px 30px -22px rgba(20,60,40,.4);
  transition: background .25s;
}

.acc-09__item[open] {
  background: oklch(0.55 0.16 160 / .06);
}

.acc-09__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: 60px;
  padding: 8px 20px;
  font-size: 16px;
  font-weight: 650;
  color: #1d3428;
  cursor: pointer;
  transition: color .2s;
}

.acc-09__sum::-webkit-details-marker {
  display: none;
}

.acc-09__sum::marker {
  content: "";
}

.acc-09__sum:hover {
  color: var(--accent);
}

.acc-09__item[open] .acc-09__sum {
  color: var(--accent);
}

.acc-09__pm {
  margin-left: auto;
  position: relative;
  width: var(--ico);
  height: var(--ico);
  flex: none;
  transition: transform .4s cubic-bezier(.3,1.4,.4,1);
}

.acc-09__pm::before,
.acc-09__pm::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  background: currentColor;
  border-radius: 3px;
  transition: transform .4s cubic-bezier(.3,1.4,.4,1);
}

.acc-09__pm::before {
  width: 100%;
  height: 3px;
}

.acc-09__pm::after {
  width: 3px;
  height: 100%;
}

.acc-09__item[open] .acc-09__pm {
  transform: rotate(180deg);
}

.acc-09__item[open] .acc-09__pm::after {
  transform: rotate(90deg);
}

.acc-09__body {
  padding: 0 56px 20px 20px;
  font-size: 14.5px;
  line-height: 1.65;
  color: #41564b;
}

.acc-09__item[open] .acc-09__body {
  animation: acc-09-in .35s cubic-bezier(.2,.7,.3,1);
}

@keyframes acc-09-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-09__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-09__pm,
    .acc-09__pm::before,
    .acc-09__pm::after {
    transition: none;
  }

  .acc-09__item[open] .acc-09__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the plus icon is two pseudo-element bars; details[open] rotates the vertical bar 90° so plus folds into minus, while the whole icon spins 180° for overshoot. */
```
