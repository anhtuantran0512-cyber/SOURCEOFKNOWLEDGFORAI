---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/editorial-restaurant/"
title: "Editorial Restaurant"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Editorial restaurant menu — cream paper, olive-green typography, burgundy accents."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Restaurant
Source: https://codefronts.com/layouts/css-split-screen/editorial-restaurant/

Editorial restaurant menu — cream paper, olive-green typography, burgundy accents. Classic 50/50 split with food photography on the left (CSS-painted plate) and the menu on the right. Serif headlines, dotted-leader pricing, the printed-menu aesthetic.
## HTML
```html
<section class="ss-edt" aria-label="Restaurant menu">
  <aside class="ss-edt-visual" aria-hidden="true">
    <div class="ss-edt-plate">
      <div class="ss-edt-food"></div>
      <span class="ss-edt-fork"></span>
      <span class="ss-edt-knife"></span>
    </div>
    <span class="ss-edt-stamp">No. 47 · Spring</span>
  </aside>
  <article class="ss-edt-menu">
    <header>
      <span class="ss-edt-eye">— La Maison Verte</span>
      <h2>The Spring<br /><em>tasting menu.</em></h2>
      <p>Five courses, paired with natural wines, served family-style. Reservations required.</p>
    </header>
    <dl class="ss-edt-courses">
      <div>
        <dt>Asparagus &amp; truffle</dt>
        <dd>18</dd>
      </div>
      <div>
        <dt>Pea soup, mint oil</dt>
        <dd>14</dd>
      </div>
      <div>
        <dt>Hand-rolled cavatelli</dt>
        <dd>26</dd>
      </div>
      <div>
        <dt>Lamb shoulder, jus</dt>
        <dd>34</dd>
      </div>
      <div>
        <dt>Olive oil cake</dt>
        <dd>12</dd>
      </div>
    </dl>
    <footer>
      <span>5-course · 104 per guest</span>
      <button type="button" class="ss-edt-cta">Reserve a table →</button>
    </footer>
  </article>
</section>
```
## CSS
```css
.ss-edt {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  background: #f4ede0;
  color: #2a3325;
  border-radius: 0;
  overflow: hidden;
  border: 1px solid #2a3325;
}

.ss-edt-visual {
  position: relative;
  background: radial-gradient(60% 80% at 50% 40%, #efe4cf 0%, #d8c8a8 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid #2a3325;
}

.ss-edt-plate {
  position: relative;
  width: 240px;
  height: 240px;
  border-radius: 50%;
  background: linear-gradient(135deg, #fff 0%, #f0e8d4 100%);
  box-shadow: inset 0 0 0 14px rgba(0,0,0,0.04), inset 0 0 0 16px rgba(122,86,40,0.18), 0 18px 40px rgba(60,40,20,0.18);
}

.ss-edt-food {
  position: absolute;
  inset: 30%;
  border-radius: 50%;
  background: radial-gradient(ellipse at 35% 30%, #6d8c3c 0%, #4a6b25 60%, transparent 75%), radial-gradient(circle at 70% 60%, #c43a2c 0%, #8a1f1c 30%, transparent 50%), radial-gradient(circle at 50% 75%, #e8b04a 0%, #b8924a 40%, transparent 60%);
}

.ss-edt-fork,
.ss-edt-knife {
  position: absolute;
  width: 4px;
  height: 80px;
  background: linear-gradient(180deg, #c0bcb0 0%, #888477 100%);
  border-radius: 2px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}

.ss-edt-fork {
  top: 50%;
  left: 8%;
  transform: translateY(-50%) rotate(8deg);
}

.ss-edt-knife {
  top: 50%;
  right: 8%;
  transform: translateY(-50%) rotate(-8deg);
}

.ss-edt-fork::before {
  content: '';
  position: absolute;
  top: -10px;
  left: -6px;
  width: 16px;
  height: 24px;
  background: repeating-linear-gradient(90deg, transparent 0 3px, #c0bcb0 3px 4px);
}

.ss-edt-knife::before {
  content: '';
  position: absolute;
  top: -10px;
  left: -3px;
  width: 10px;
  height: 30px;
  background: linear-gradient(180deg, #c0bcb0 0%, #888477 100%);
  border-radius: 2px 4px 0 0;
  transform: skewX(-8deg);
}

.ss-edt-stamp {
  position: absolute;
  top: 24px;
  left: 24px;
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #5a3825;
  border: 1.5px solid #5a3825;
  padding: 6px 12px;
  transform: rotate(-4deg);
  background: rgba(244,237,224,0.4);
}

.ss-edt-menu {
  padding: 40px 44px;
  display: flex;
  flex-direction: column;
  gap: 22px;
  background: radial-gradient(60% 60% at 100% 0%, #fdf8eb 0%, transparent 60%), #f9f1de;
}

.ss-edt-eye {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #6e1f1c;
}

.ss-edt-menu h2 {
  margin: 6px 0 0;
  font-size: clamp(34px, 4.5vw, 54px);
  font-weight: 500;
  line-height: 0.95;
  color: #2a3325;
  letter-spacing: -0.02em;
}

.ss-edt-menu h2 em {
  font-style: italic;
  color: #6e1f1c;
}

.ss-edt-menu header p {
  margin: 4px 0 0;
  font-size: 16px;
  color: #5a4a35;
  line-height: 1.55;
  max-width: 440px;
}

.ss-edt-courses {
  margin: 0;
  padding: 18px 0;
  border-top: 1px solid #c8b896;
  border-bottom: 1px solid #c8b896;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ss-edt-courses div {
  display: flex;
  align-items: baseline;
  gap: 8px;
  font-size: 18px;
}

.ss-edt-courses dt {
  color: #2a3325;
  font-style: italic;
  flex-shrink: 0;
}

.ss-edt-courses dt::after {
  content: '';
  display: inline-block;
  width: 100%;
  margin: 0 8px 4px;
  border-bottom: 1.5px dotted #b89668;
  vertical-align: bottom;
}

.ss-edt-courses dd {
  margin: 0;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: #6e1f1c;
}

.ss-edt-menu footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
}

.ss-edt-menu footer span {
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: #5a4a35;
}

.ss-edt-cta {
  padding: 12px 22px;
  background: #2a3325;
  color: #f4ede0;
  border: 0;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  transition: background 0.16s, transform 0.12s;
}

.ss-edt-cta:hover {
  background: #6e1f1c;
}

.ss-edt-cta:active {
  transform: translateY(1px);
}

@media (max-width: 720px) {
  .ss-edt {
    grid-template-columns: 1fr;
  }

  .ss-edt-visual {
    min-height: 280px;
    border-right: 0;
    border-bottom: 1px solid #2a3325;
  }
}
```
