---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/orion-constellation-chart/"
title: "Orion Constellation Chart"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A starfield rendering of the Orion constellation with six labeled star hotspots — Rigel, Betelgeuse, Bellatrix, Alnilam, Saiph, Meissa."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Orion Constellation Chart
Source: https://codefronts.com/snippets/css-tooltips/orion-constellation-chart/

A starfield rendering of the Orion constellation with six labeled star hotspots — Rigel, Betelgeuse, Bellatrix, Alnilam, Saiph, Meissa. Each star pops a card with real astronomical data: Bayer designation, distance, magnitude, luminosity, and a five-star brightness gauge.
## HTML
```html
<div class="tp-15">
  <div class="tp-15__chart">
    <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
      <circle cx="22" cy="18" r="0.6" fill="rgba(200,220,255,0.35)"/>
      <circle cx="80" cy="10" r="0.7" fill="rgba(200,220,255,0.45)"/>
      <circle cx="140" cy="22" r="0.4" fill="rgba(200,220,255,0.25)"/>
      <circle cx="170" cy="38" r="0.6" fill="rgba(200,220,255,0.35)"/>
      <circle cx="265" cy="18" r="0.7" fill="rgba(200,220,255,0.4)"/>
      <circle cx="330" cy="22" r="0.4" fill="rgba(200,220,255,0.22)"/>
      <circle cx="360" cy="55" r="0.6" fill="rgba(200,220,255,0.38)"/>
      <circle cx="30" cy="80" r="0.4" fill="rgba(200,220,255,0.2)"/>
      <circle cx="320" cy="75" r="0.6" fill="rgba(200,220,255,0.32)"/>
      <circle cx="55" cy="145" r="0.5" fill="rgba(200,220,255,0.28)"/>
      <circle cx="360" cy="150" r="0.5" fill="rgba(200,220,255,0.28)"/>
      <circle cx="35" cy="260" r="0.5" fill="rgba(200,220,255,0.3)"/>
      <circle cx="380" cy="260" r="0.5" fill="rgba(200,220,255,0.28)"/>
      <circle cx="58" cy="360" r="0.4" fill="rgba(200,220,255,0.2)"/>
      <circle cx="90" cy="380" r="0.5" fill="rgba(200,220,255,0.28)"/>
      <circle cx="340" cy="355" r="0.5" fill="rgba(200,220,255,0.3)"/>
      <circle cx="392" cy="360" r="0.6" fill="rgba(200,220,255,0.35)"/>
      <line x1="200" y1="48" x2="148" y2="155" stroke="rgba(140,160,255,0.18)" stroke-width="0.8"/>
      <line x1="200" y1="48" x2="262" y2="142" stroke="rgba(140,160,255,0.18)" stroke-width="0.8"/>
      <line x1="148" y1="155" x2="168" y2="228" stroke="rgba(140,160,255,0.18)" stroke-width="0.8"/>
      <line x1="262" y1="142" x2="232" y2="224" stroke="rgba(140,160,255,0.18)" stroke-width="0.8"/>
      <line x1="168" y1="228" x2="200" y2="230" stroke="rgba(140,160,255,0.22)" stroke-width="0.8"/>
      <line x1="200" y1="230" x2="232" y2="224" stroke="rgba(140,160,255,0.22)" stroke-width="0.8"/>
      <line x1="168" y1="228" x2="136" y2="342" stroke="rgba(140,160,255,0.18)" stroke-width="0.8"/>
      <line x1="232" y1="224" x2="278" y2="330" stroke="rgba(140,160,255,0.18)" stroke-width="0.8"/>
      <circle cx="200" cy="48" r="6" fill="rgba(160,180,255,0.08)"/>
      <circle cx="200" cy="48" r="2.5" fill="#d0daff" opacity="0.85"/>
      <circle cx="148" cy="155" r="10" fill="rgba(255,120,60,0.06)"/>
      <circle cx="148" cy="155" r="5" fill="#ffb890" opacity="0.9"/>
      <circle cx="262" cy="142" r="6" fill="rgba(160,200,255,0.06)"/>
      <circle cx="262" cy="142" r="3" fill="#c0d8ff" opacity="0.85"/>
      <circle cx="168" cy="228" r="5" fill="rgba(160,180,255,0.06)"/>
      <circle cx="168" cy="228" r="2.8" fill="#d0daff" opacity="0.85"/>
      <circle cx="200" cy="230" r="5" fill="rgba(160,180,255,0.06)"/>
      <circle cx="200" cy="230" r="3" fill="#d0daff" opacity="0.85"/>
      <circle cx="232" cy="224" r="5" fill="rgba(160,200,255,0.06)"/>
      <circle cx="232" cy="224" r="2.5" fill="#c8d8ff" opacity="0.85"/>
      <circle cx="136" cy="342" r="5" fill="rgba(160,200,255,0.06)"/>
      <circle cx="136" cy="342" r="2.5" fill="#c0d4ff" opacity="0.8"/>
      <circle cx="278" cy="330" r="14" fill="rgba(160,200,255,0.05)"/>
      <circle cx="278" cy="330" r="6" fill="#dce8ff" opacity="0.95"/>
    </svg>
    <div class="tp-15__spot" style="left:37%;top:38.75%"><div class="tp-15__hit"></div>
      <div class="tp-15__card">
        <div class="tp-15__top"><div class="tp-15__bayer">α Orionis</div><div class="tp-15__name">Betelgeuse</div><div class="tp-15__const">Orion · Upper left shoulder</div><span class="tp-15__pill">M1–2 Iaab · Red Supergiant</span></div>
        <div class="tp-15__data">
          <div class="tp-15__row"><span class="tp-15__key">Distance</span><span class="tp-15__val">700 ly</span></div>
          <div class="tp-15__row"><span class="tp-15__key">App. mag</span><span class="tp-15__val">0.42 (variable)</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Luminosity</span><span class="tp-15__val">~126,000 L☉</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Radius</span><span class="tp-15__val">~700 R☉</span></div>
          <div class="tp-15__mag"><span class="tp-15__mag-label">Brightness</span><span class="tp-15__mag-stars"><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star tp-15__mag-dim">★</span></span></div>
        </div>
      </div>
    </div>
    <div class="tp-15__spot" style="left:69.5%;top:82.5%"><div class="tp-15__hit"></div>
      <div class="tp-15__card tp-15__card-left">
        <div class="tp-15__top"><div class="tp-15__bayer">β Orionis</div><div class="tp-15__name">Rigel</div><div class="tp-15__const">Orion · Lower right</div><span class="tp-15__pill">B8 Ia · Blue Supergiant</span></div>
        <div class="tp-15__data">
          <div class="tp-15__row"><span class="tp-15__key">Distance</span><span class="tp-15__val">860 ly</span></div>
          <div class="tp-15__row"><span class="tp-15__key">App. mag</span><span class="tp-15__val">0.13 (brightest)</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Luminosity</span><span class="tp-15__val">~120,000 L☉</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Temp</span><span class="tp-15__val">12,100 K</span></div>
          <div class="tp-15__mag"><span class="tp-15__mag-label">Brightness</span><span class="tp-15__mag-stars"><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span></span></div>
        </div>
      </div>
    </div>
    <div class="tp-15__spot" style="left:65.5%;top:35.5%"><div class="tp-15__hit"></div>
      <div class="tp-15__card tp-15__card-left">
        <div class="tp-15__top"><div class="tp-15__bayer">γ Orionis</div><div class="tp-15__name">Bellatrix</div><div class="tp-15__const">Orion · Upper right shoulder</div><span class="tp-15__pill">B2 III · Blue Giant</span></div>
        <div class="tp-15__data">
          <div class="tp-15__row"><span class="tp-15__key">Distance</span><span class="tp-15__val">250 ly</span></div>
          <div class="tp-15__row"><span class="tp-15__key">App. mag</span><span class="tp-15__val">1.64</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Luminosity</span><span class="tp-15__val">~6,400 L☉</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Temp</span><span class="tp-15__val">22,000 K</span></div>
          <div class="tp-15__mag"><span class="tp-15__mag-label">Brightness</span><span class="tp-15__mag-stars"><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star">★</span><span class="tp-15__mag-star tp-15__mag-dim">★</span><span class="tp-15__mag-star tp-15__mag-dim">★</span></span></div>
        </div>
      </div>
    </div>
    <div class="tp-15__spot" style="left:50%;top:57.5%"><div class="tp-15__hit"></div>
      <div class="tp-15__card">
        <div class="tp-15__top"><div class="tp-15__bayer">ε Orionis</div><div class="tp-15__name">Alnilam</div><div class="tp-15__const">Orion · Belt, central star</div><span class="tp-15__pill">B0 Ia · Blue Supergiant</span></div>
        <div class="tp-15__data">
          <div class="tp-15__row"><span class="tp-15__key">Distance</span><span class="tp-15__val">2,000 ly</span></div>
          <div class="tp-15__row"><span class="tp-15__key">App. mag</span><span class="tp-15__val">1.69</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Luminosity</span><span class="tp-15__val">~375,000 L☉</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Temp</span><span class="tp-15__val">27,500 K</span></div>
        </div>
      </div>
    </div>
    <div class="tp-15__spot" style="left:50%;top:12%"><div class="tp-15__hit"></div>
      <div class="tp-15__card">
        <div class="tp-15__top"><div class="tp-15__bayer">λ Orionis</div><div class="tp-15__name">Meissa</div><div class="tp-15__const">Orion · Head</div><span class="tp-15__pill">O8 III · Blue-White Giant</span></div>
        <div class="tp-15__data">
          <div class="tp-15__row"><span class="tp-15__key">Distance</span><span class="tp-15__val">1,100 ly</span></div>
          <div class="tp-15__row"><span class="tp-15__key">App. mag</span><span class="tp-15__val">3.39</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Luminosity</span><span class="tp-15__val">~28,000 L☉</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Temp</span><span class="tp-15__val">35,000 K</span></div>
        </div>
      </div>
    </div>
    <div class="tp-15__spot" style="left:34%;top:85.5%"><div class="tp-15__hit"></div>
      <div class="tp-15__card">
        <div class="tp-15__top"><div class="tp-15__bayer">κ Orionis</div><div class="tp-15__name">Saiph</div><div class="tp-15__const">Orion · Lower left</div><span class="tp-15__pill">B0.5 Ia · Blue Supergiant</span></div>
        <div class="tp-15__data">
          <div class="tp-15__row"><span class="tp-15__key">Distance</span><span class="tp-15__val">720 ly</span></div>
          <div class="tp-15__row"><span class="tp-15__key">App. mag</span><span class="tp-15__val">2.07</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Luminosity</span><span class="tp-15__val">~57,500 L☉</span></div>
          <div class="tp-15__row"><span class="tp-15__key">Temp</span><span class="tp-15__val">26,500 K</span></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-15 {
  width: 100%;
  min-height: 100vh;
  background: #04060e;
  /* Side room — star cards pop to the right (Betelgeuse, Alnilam,
       Meissa, Saiph) or left (Rigel, Bellatrix). 260px each side. */
  padding: 40px 280px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tp-15__chart {
  position: relative;
  width: 400px;
  height: 400px;
  flex-shrink: 0;
}

.tp-15__chart svg {
  width: 100%;
  height: 100%;
  display: block;
}

.tp-15__spot {
  position: absolute;
  transform: translate(-50%, -50%);
  cursor: help;
  z-index: 10;
}

.tp-15__hit {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  position: relative;
}

.tp-15__hit::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: rgba(180, 200, 255, 0);
  transition: background .2s;
}

.tp-15__spot:hover .tp-15__hit::after {
  background: rgba(180, 200, 255, 0.08);
  box-shadow: 0 0 18px 6px rgba(160, 180, 255, 0.12);
}

.tp-15__card {
  position: absolute;
  left: calc(100% + 14px);
  top: 50%;
  transform: translateY(-50%) translateX(6px);
  z-index: 200;
  width: 230px;
  background: rgba(8, 12, 28, 0.96);
  border: 1px solid rgba(100, 120, 200, 0.2);
  border-radius: 8px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  box-shadow: 0 12px 38px rgba(0, 0, 0, 0.9), 0 0 0 1px rgba(100, 120, 200, 0.06);
  overflow: hidden;
  text-align: left;
}

.tp-15__spot:hover .tp-15__card {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(0);
  transition-delay: 0s;
}

.tp-15__card-left {
  left: auto;
  right: calc(100% + 14px);
  transform: translateY(-50%) translateX(-6px);
}

.tp-15__spot:hover .tp-15__card-left {
  transform: translateY(-50%) translateX(0);
}

.tp-15__top {
  padding: 12px 13px 10px;
  border-bottom: 1px solid rgba(100, 120, 200, 0.1);
}

.tp-15__bayer {
  font-size: 9px;
  color: rgba(140, 160, 255, 0.4);
  letter-spacing: 0.1em;
  margin-bottom: 3px;
}

.tp-15__name {
  font-size: 15px;
  font-weight: 500;
  color: rgba(220, 230, 255, 0.92);
  margin-bottom: 1px;
}

.tp-15__const {
  font-size: 9.5px;
  color: rgba(100, 120, 180, 0.6);
}

.tp-15__pill {
  display: inline-block;
  font-size: 8.5px;
  padding: 2px 7px;
  border-radius: 3px;
  margin-top: 6px;
  letter-spacing: 0.06em;
  border: 1px solid rgba(100, 120, 200, 0.2);
  color: rgba(140, 160, 220, 0.7);
}

.tp-15__data {
  padding: 10px 13px;
}

.tp-15__row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.tp-15__key {
  font-size: 8.5px;
  color: rgba(60, 80, 140, 0.7);
  letter-spacing: 0.08em;
}

.tp-15__val {
  font-size: 9.5px;
  color: rgba(160, 180, 240, 0.75);
}

.tp-15__mag {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px solid rgba(100, 120, 200, 0.06);
}

.tp-15__mag-label {
  font-size: 7.5px;
  color: rgba(60, 80, 140, 0.5);
  letter-spacing: 0.08em;
}

.tp-15__mag-stars {
  display: flex;
  gap: 2px;
}

.tp-15__mag-star {
  font-size: 9.5px;
  color: rgba(255, 220, 80, 0.7);
}

.tp-15__mag-dim {
  color: rgba(60, 80, 140, 0.3);
}
```
