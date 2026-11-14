---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/gradient-border/"
title: "Gradient Border Card Radio"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Dark glass cards wrapped in a living gradient border: at rest a faint ring, on selection a vivid violet-to-cyan gradient that slowly rotates around the…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Border Card Radio
Source: https://codefronts.com/components/css-radio-buttons/gradient-border/

Dark glass cards wrapped in a living gradient border: at rest a faint ring, on selection a vivid violet-to-cyan gradient that slowly rotates around the card's perimeter like circulating energy. The premium checked-state treatment for AI products, crypto dashboards and feature pickers.
## HTML
```html
<div class="crb-20-group">
<section class="crb-20a" aria-label="Gradient border card radio">
  <fieldset class="crb-20a__group">
    <legend class="crb-20a__legend">Choose your model</legend>
    <div class="crb-20a__row">
      <label class="crb-20a__card">
        <input class="crb-20a__input" type="radio" name="crb-20a" value="lite">
        <span class="crb-20a__panel"><span class="crb-20a__name">Nova Lite</span><span class="crb-20a__meta">Fast drafts &amp; chat</span><span class="crb-20a__stat">128k context</span></span>
      </label>
      <label class="crb-20a__card">
        <input class="crb-20a__input" type="radio" name="crb-20a" value="pro" checked>
        <span class="crb-20a__panel"><span class="crb-20a__name">Nova Pro</span><span class="crb-20a__meta">Deep reasoning</span><span class="crb-20a__stat">1M context</span></span>
      </label>
      <label class="crb-20a__card">
        <input class="crb-20a__input" type="radio" name="crb-20a" value="vision">
        <span class="crb-20a__panel"><span class="crb-20a__name">Nova Vision</span><span class="crb-20a__meta">Image + video in</span><span class="crb-20a__stat">Multimodal</span></span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-20-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-20-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

@property --crb20a-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.crb-20a,
.crb-20a *,
.crb-20a *::before,
.crb-20a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-20a {
  --g1: oklch(0.6 0.24 300);
  --g2: oklch(0.75 0.14 195);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0b0c12;
}

.crb-20a__group {
  border: none;
}

.crb-20a__legend {
  font-size: 24px;
  font-weight: 750;
  color: #edeffa;
  letter-spacing: -.02em;
  text-align: center;
}

.crb-20a__row {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  margin-top: 28px;
}

.crb-20a__card {
  position: relative;
  border-radius: 18px;
  padding: 1.5px;
  background: conic-gradient(from var(--crb20a-angle),rgba(255,255,255,.14),rgba(255,255,255,.05),rgba(255,255,255,.14));
  cursor: pointer;
  transition: transform .3s;
}

.crb-20a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-20a__panel {
  display: grid;
  gap: 4px;
  width: 196px;
  padding: 24px 20px;
  border-radius: 16.5px;
  background: linear-gradient(170deg,#171927,#101119);
}

.crb-20a__name {
  font-size: 17px;
  font-weight: 750;
  color: #fff;
  letter-spacing: -.01em;
}

.crb-20a__meta {
  font-size: 13px;
  color: #8b91ad;
}

.crb-20a__stat {
  margin-top: 12px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #6a7194;
}

.crb-20a__card:hover {
  transform: translateY(-2px);
}

.crb-20a__card:has(.crb-20a__input:checked) {
  background: conic-gradient(from var(--crb20a-angle),var(--g1),var(--g2),var(--g1));
  animation: crb-20a-rotate 5s linear infinite;
}

.crb-20a__card:has(.crb-20a__input:checked) .crb-20a__stat {
  color: var(--g2);
}

.crb-20a__card:has(.crb-20a__input:focus-visible) {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@keyframes crb-20a-rotate {
  to {
    --crb20a-angle: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .crb-20a__card:has(.crb-20a__input:checked) {
    animation: none;
  }

  .crb-20a__card:hover {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the border is a conic-gradient underlayer showing through a 1.5px padding rim; @property lets the gradient's from-angle animate, so the checked rim circulates. */
```
