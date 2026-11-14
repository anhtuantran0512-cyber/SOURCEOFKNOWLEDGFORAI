---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-border-button/"
title: "CSS Gradient Border Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "Transparent-body buttons with multi-color gradient outlines via the double-background background-clip trick, including an orbiting conic variant animated…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Border Button
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-border-button/

Transparent-body buttons with multi-color gradient outlines via the double-background background-clip trick, including an orbiting conic variant animated through @property.
## HTML
```html
<div class="gb-04">
  <div class="gb-04__panel">
    <h3 class="gb-04__h">Gradient borders, zero images</h3>
    <p class="gb-04__p">Transparent-body buttons with a multi-colour outline — the classic <em>background-clip</em> trick, plus an orbiting conic variant.</p>
    <div class="gb-04__row">
      <button class="gb-04__btn" type="button">Static border</button>
      <button class="gb-04__btn gb-04__btn--orbit" type="button">Orbiting border</button>
    </div>
    <p class="gb-04__foot">Hover the orbit button — the conic angle accelerates</p>
  </div>
</div>
```
## CSS
```css
.gb-04,
.gb-04 *,
.gb-04 *::before,
.gb-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-04 ::selection {
  background: #22d3ee;
  color: #0b1020;
}

@property --gb-04-angle {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: false;
}

.gb-04 {
  --cyan: #22d3ee;
  --violet: #a78bfa;
  --pink: #f472b6;
  --bg: #0b1020;
  --panel: #111832;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(800px 400px at 80% -10%,rgba(167,139,250,.12),transparent 60%), radial-gradient(700px 400px at 10% 110%,rgba(34,211,238,.1),transparent 60%), var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-04__panel {
  width: 100%;
  max-width: 440px;
  background: var(--panel);
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 20px;
  padding: 40px 36px;
  text-align: center;
}

.gb-04__h {
  color: #e7ecff;
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -.3px;
  margin-bottom: 8px;
}

.gb-04__p {
  color: #8b93b8;
  font-size: 14px;
  line-height: 1.6;
  margin-bottom: 30px;
}

.gb-04__row {
  display: flex;
  gap: 18px;
  justify-content: center;
  flex-wrap: wrap;
}
/* Technique A — double background + background-clip:
   layer 1 (padding-box) paints the dark fill, layer 2 (border-box)
   paints the gradient that shows through the transparent border. */

.gb-04__btn {
  padding: 15px 30px;
  border: 2px solid transparent;
  border-radius: 14px;
  font-family: inherit;
  font-size: 15px;
  font-weight: 700;
  color: #e7ecff;
  cursor: pointer;
  background: linear-gradient(var(--panel),var(--panel)) padding-box, linear-gradient(120deg,var(--cyan),var(--violet) 55%,var(--pink)) border-box;
  transition: color .3s ease,box-shadow .35s ease,transform .25s ease;
  -webkit-tap-highlight-color: transparent;
}

.gb-04__btn:hover {
  color: #fff;
  transform: translateY(-2px);
  box-shadow: 0 12px 30px -12px rgba(167,139,250,.55);
}

.gb-04__btn:active {
  transform: translateY(0);
}

.gb-04__btn:focus-visible {
  outline: 3px solid var(--cyan);
  outline-offset: 3px;
}
/* Technique B — animated conic border driven by @property so the
   angle itself interpolates and the gradient orbits the button. */

.gb-04__btn--orbit {
  background: linear-gradient(var(--panel),var(--panel)) padding-box, conic-gradient(from var(--gb-04-angle),var(--cyan),var(--violet),var(--pink),var(--cyan)) border-box;
  animation: gb-04-spin 3.5s linear infinite;
}

@keyframes gb-04-spin {
  to {
    --gb-04-angle: 360deg;
  }
}

.gb-04__btn--orbit:hover {
  animation-duration: 1.2s;
  box-shadow: 0 12px 34px -10px rgba(244,114,182,.55);
}

.gb-04__foot {
  margin-top: 24px;
  font-size: 12.5px;
  color: #5d6690;
}

@media (prefers-reduced-motion: reduce) {
  .gb-04__btn {
    transition: none;
  }

  .gb-04__btn--orbit {
    animation: none;
  }

  .gb-04__btn:hover {
    transform: none;
  }
}
```
