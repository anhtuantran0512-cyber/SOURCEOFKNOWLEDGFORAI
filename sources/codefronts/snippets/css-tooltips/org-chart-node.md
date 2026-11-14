---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/org-chart-node/"
title: "Org Chart Node"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A three-tier org chart with CEO → C-suite → leads."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Org Chart Node
Source: https://codefronts.com/snippets/css-tooltips/org-chart-node/

A three-tier org chart with CEO → C-suite → leads. Hover any node to lift a profile card with gradient hero, avatar monogram, role + department pill, three stats (reports/org size/tenure), and a footer with email + timezone. For team directories, succession-planning UIs, internal wikis.
## HTML
```html
<div class="tp-18">
  <div class="tp-18__tree">
    <div class="tp-18__level">
      <div class="tp-18__node">
        <div class="tp-18__box tp-18__box-ceo">
          <div class="tp-18__av" style="background:linear-gradient(135deg,#6028a0,#9060d0)">SL</div>
          <div class="tp-18__bname">Sarah Lindqvist</div>
          <div class="tp-18__btitle">Chief Executive Officer</div>
          <div class="tp-18__bdept">Executive</div>
        </div>
        <div class="tp-18__card tp-18__card-left">
          <div class="tp-18__hero" style="background:linear-gradient(135deg,#4a1880,#8050c0)"></div>
          <div class="tp-18__photo" style="background:linear-gradient(135deg,#6028a0,#9060d0)">SL</div>
          <div class="tp-18__body">
            <div class="tp-18__name">Sarah Lindqvist</div>
            <div class="tp-18__title">Chief Executive Officer</div>
            <span class="tp-18__pill">Executive · Board</span>
            <div class="tp-18__stats">
              <div class="tp-18__stat"><div class="tp-18__stat-n">2</div><div class="tp-18__stat-l">Reports</div></div>
              <div class="tp-18__stat"><div class="tp-18__stat-n">214</div><div class="tp-18__stat-l">Org Size</div></div>
              <div class="tp-18__stat"><div class="tp-18__stat-n">8yr</div><div class="tp-18__stat-l">Tenure</div></div>
            </div>
          </div>
          <div class="tp-18__foot"><span>[email protected]</span><span>NYC · EST</span></div>
        </div>
      </div>
    </div>
    <div class="tp-18__conn"></div>
    <div class="tp-18__level">
      <div class="tp-18__node">
        <div class="tp-18__box">
          <div class="tp-18__av" style="background:linear-gradient(135deg,#204080,#4070c0)">MW</div>
          <div class="tp-18__bname">Marcus Webb</div>
          <div class="tp-18__btitle">Chief Technology Officer</div>
          <div class="tp-18__bdept">Engineering</div>
        </div>
        <div class="tp-18__card tp-18__card-left">
          <div class="tp-18__hero" style="background:linear-gradient(135deg,#102060,#3060a0)"></div>
          <div class="tp-18__photo" style="background:linear-gradient(135deg,#204080,#4070c0)">MW</div>
          <div class="tp-18__body">
            <div class="tp-18__name">Marcus Webb</div>
            <div class="tp-18__title">Chief Technology Officer</div>
            <span class="tp-18__pill">Engineering · Platform</span>
            <div class="tp-18__stats">
              <div class="tp-18__stat"><div class="tp-18__stat-n">2</div><div class="tp-18__stat-l">Reports</div></div>
              <div class="tp-18__stat"><div class="tp-18__stat-n">96</div><div class="tp-18__stat-l">Org Size</div></div>
              <div class="tp-18__stat"><div class="tp-18__stat-n">5yr</div><div class="tp-18__stat-l">Tenure</div></div>
            </div>
          </div>
          <div class="tp-18__foot"><span>[email protected]</span><span>SF · PST</span></div>
        </div>
      </div>
      <div class="tp-18__node">
        <div class="tp-18__box">
          <div class="tp-18__av" style="background:linear-gradient(135deg,#0a6050,#1aa080)">ER</div>
          <div class="tp-18__bname">Elena Russo</div>
          <div class="tp-18__btitle">Chief Marketing Officer</div>
          <div class="tp-18__bdept">Marketing</div>
        </div>
        <div class="tp-18__card">
          <div class="tp-18__hero" style="background:linear-gradient(135deg,#054030,#108060)"></div>
          <div class="tp-18__photo" style="background:linear-gradient(135deg,#0a6050,#1aa080)">ER</div>
          <div class="tp-18__body">
            <div class="tp-18__name">Elena Russo</div>
            <div class="tp-18__title">Chief Marketing Officer</div>
            <span class="tp-18__pill">Marketing · Growth</span>
            <div class="tp-18__stats">
              <div class="tp-18__stat"><div class="tp-18__stat-n">2</div><div class="tp-18__stat-l">Reports</div></div>
              <div class="tp-18__stat"><div class="tp-18__stat-n">68</div><div class="tp-18__stat-l">Org Size</div></div>
              <div class="tp-18__stat"><div class="tp-18__stat-n">3yr</div><div class="tp-18__stat-l">Tenure</div></div>
            </div>
          </div>
          <div class="tp-18__foot"><span>[email protected]</span><span>London · GMT</span></div>
        </div>
      </div>
      <div class="tp-18__node">
        <div class="tp-18__box">
          <div class="tp-18__av" style="background:linear-gradient(135deg,#804010,#c07030)">AT</div>
          <div class="tp-18__bname">Amir Tahir</div>
          <div class="tp-18__btitle">Chief Financial Officer</div>
          <div class="tp-18__bdept">Finance</div>
        </div>
        <div class="tp-18__card">
          <div class="tp-18__hero" style="background:linear-gradient(135deg,#603008,#a06020)"></div>
          <div class="tp-18__photo" style="background:linear-gradient(135deg,#804010,#c07030)">AT</div>
          <div class="tp-18__body">
            <div class="tp-18__name">Amir Tahir</div>
            <div class="tp-18__title">Chief Financial Officer</div>
            <span class="tp-18__pill">Finance · Strategy</span>
            <div class="tp-18__stats">
              <div class="tp-18__stat"><div class="tp-18__stat-n">2</div><div class="tp-18__stat-l">Reports</div></div>
              <div class="tp-18__stat"><div class="tp-18__stat-n">50</div><div class="tp-18__stat-l">Org Size</div></div>
              <div class="tp-18__stat"><div class="tp-18__stat-n">2yr</div><div class="tp-18__stat-l">Tenure</div></div>
            </div>
          </div>
          <div class="tp-18__foot"><span>[email protected]</span><span>Dubai · GST</span></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-18 {
  width: 100%;
  min-height: 100vh;
  background: #f7f7f9;
  /* Side room — org cards pop to the right (CMO/CFO) or left (CEO/CTO). */
  padding: 40px 280px;
  font-family: 'Inter', system-ui, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tp-18__tree {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}

.tp-18__level {
  display: flex;
  justify-content: center;
  gap: 18px;
  position: relative;
}

.tp-18__conn {
  width: 1px;
  height: 24px;
  background: #d0d0d8;
  margin: 0 auto;
}

.tp-18__node {
  position: relative;
  cursor: help;
}

.tp-18__box {
  background: #fff;
  border: 1px solid #e0e0e8;
  border-radius: 8px;
  padding: 9px 12px;
  width: 130px;
  text-align: center;
  transition: border-color .15s, box-shadow .15s;
}

.tp-18__node:hover .tp-18__box {
  border-color: #a0a0c0;
  box-shadow: 0 4px 16px rgba(0, 0, 40, 0.08);
}

.tp-18__box-ceo {
  border-color: #c0b0e0;
  background: linear-gradient(135deg, #faf9ff, #fff);
}

.tp-18__av {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin: 0 auto 7px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10.5px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.92);
  letter-spacing: 0.03em;
}

.tp-18__bname {
  font-size: 10.5px;
  font-weight: 600;
  color: #1a1a2e;
}

.tp-18__btitle {
  font-size: 8.5px;
  color: #909098;
  margin-top: 2px;
  letter-spacing: 0.04em;
}

.tp-18__bdept {
  font-size: 7.5px;
  color: #c0c0cc;
  margin-top: 1px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.tp-18__card {
  position: absolute;
  left: calc(100% + 12px);
  top: 50%;
  transform: translateY(-50%) translateX(6px);
  z-index: 200;
  width: 230px;
  background: #fff;
  border: 1px solid #e4e4ee;
  border-radius: 10px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  box-shadow: 0 8px 30px rgba(0, 0, 40, 0.12), 0 2px 8px rgba(0, 0, 40, 0.06);
  overflow: hidden;
  text-align: left;
}

.tp-18__node:hover .tp-18__card {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(0);
  transition-delay: 0s;
}

.tp-18__card-left {
  left: auto;
  right: calc(100% + 12px);
  transform: translateY(-50%) translateX(-6px);
}

.tp-18__node:hover .tp-18__card-left {
  transform: translateY(-50%) translateX(0);
}

.tp-18__hero {
  height: 50px;
  position: relative;
}

.tp-18__photo {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 3px solid #fff;
  position: absolute;
  left: 14px;
  bottom: -14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.92);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.tp-18__body {
  padding: 20px 14px 11px;
}

.tp-18__name {
  font-size: 14px;
  font-weight: 600;
  color: #1a1a2e;
}

.tp-18__title {
  font-size: 10.5px;
  color: #6060a0;
  margin-top: 1px;
}

.tp-18__pill {
  display: inline-block;
  font-size: 8.5px;
  padding: 2px 7px;
  border-radius: 4px;
  background: #f0f0f8;
  color: #8080b0;
  margin-top: 6px;
  border: 1px solid #e4e4f0;
  letter-spacing: 0.04em;
}

.tp-18__stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  margin-top: 11px;
  padding-top: 10px;
  border-top: 1px solid #f0f0f8;
}

.tp-18__stat {
  text-align: center;
}

.tp-18__stat-n {
  font-size: 14px;
  font-weight: 600;
  color: #2a2a4e;
}

.tp-18__stat-l {
  font-size: 7.5px;
  color: #c0c0cc;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 2px;
}

.tp-18__foot {
  padding: 9px 14px;
  border-top: 1px solid #f4f4fc;
  font-size: 9.5px;
  color: #b0b0c8;
  display: flex;
  justify-content: space-between;
}
```
