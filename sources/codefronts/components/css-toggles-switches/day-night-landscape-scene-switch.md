---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/day-night-landscape-scene-switch/"
title: "Day / Night Landscape Scene Switch"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A wide cinematic toggle that IS a landscape: the sun arcs across a gradient sky and sets behind silhouetted mountains as a moon rises, stars pepper the dark,…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Day / Night Landscape Scene Switch
Source: https://codefronts.com/components/css-toggles-switches/day-night-landscape-scene-switch/

A wide cinematic toggle that IS a landscape: the sun arcs across a gradient sky and sets behind silhouetted mountains as a moon rises, stars pepper the dark, and the surrounding page follows the scene into night. The most shareable switch in the collection.
## HTML
```html
<section class="tgl-18" aria-label="Day night landscape scene switch">
  <label class="tgl-18__wrap" for="tgl-18-sw">
    <span class="tgl-18__scene">
      <input type="checkbox" id="tgl-18-sw" class="tgl-18__sw" role="switch" aria-label="Night mode">
      <span class="tgl-18__stars" aria-hidden="true"></span>
      <span class="tgl-18__moon" aria-hidden="true"></span>
      <span class="tgl-18__ridge tgl-18__ridge--far" aria-hidden="true"></span>
      <span class="tgl-18__ridge tgl-18__ridge--near" aria-hidden="true"></span>
    </span>
    <span class="tgl-18__lbl">Night mode</span>
  </label>
</section>
```
## CSS
```css
.tgl-18,
.tgl-18 *,
.tgl-18 *::before,
.tgl-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-18 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #dfeaf2;
  transition: background-color .7s;
}

.tgl-18:has(.tgl-18__sw:checked) {
  background: #0b1020;
}

.tgl-18__wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  cursor: pointer;
}

.tgl-18__scene {
  position: relative;
  display: block;
  width: 220px;
  height: 100px;
  border-radius: 50px;
  overflow: hidden;
  box-shadow: 0 18px 40px -18px rgba(10,20,50,.6),inset 0 0 0 1px rgba(255,255,255,.25);
}

.tgl-18__sw {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  cursor: pointer;
  background: linear-gradient(180deg,#69b7e8,#b8dff5 70%,#ffd9a0);
  transition: background-color .7s,filter .7s;
  z-index: 1;
}

.tgl-18__sw:checked {
  background: linear-gradient(180deg,#0d1b3d,#22355e 75%,#3a4a72);
  filter: saturate(.9);
}

.tgl-18__sw::before {
  content: "";
  position: absolute;
  top: 14px;
  left: 26px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,#fff3c0,#ffcf4d);
  box-shadow: 0 0 22px rgba(255,200,80,.9);
  transition: transform .7s cubic-bezier(.5,0,.6,1);
}

.tgl-18__sw:checked::before {
  transform: translate(60px,95px);
}

.tgl-18__moon {
  position: absolute;
  top: 14px;
  right: 30px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #f1eee2;
  box-shadow: inset -6px -4px 0 rgba(150,150,140,.35),0 0 14px rgba(230,235,255,.5);
  transform: translate(-40px,95px);
  transition: transform .7s cubic-bezier(.4,0,.5,1);
  z-index: 2;
  pointer-events: none;
}

.tgl-18__sw:checked ~ .tgl-18__moon {
  transform: translate(0,0);
}

.tgl-18__stars {
  position: absolute;
  top: 12px;
  left: 30px;
  width: 2px;
  height: 2px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 24px 8px 0 #fff,58px 2px 0 0 #cfd8ff,96px 14px 0 #fff,130px 5px 0 0 #cfd8ff,74px 26px 0 #fff,150px 22px 0 0 #cfd8ff;
  opacity: 0;
  transition: opacity .7s;
  z-index: 2;
  pointer-events: none;
}

.tgl-18__sw:checked ~ .tgl-18__stars {
  opacity: .95;
}

.tgl-18__ridge {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 44px;
  z-index: 3;
  pointer-events: none;
  transition: filter .7s;
}

.tgl-18__ridge--far {
  clip-path: polygon(0 100%,0 55%,18% 20%,34% 62%,52% 10%,70% 58%,86% 30%,100% 65%,100% 100%);
  background: #5d7c66;
}

.tgl-18__ridge--near {
  height: 32px;
  clip-path: polygon(0 100%,0 70%,14% 35%,30% 75%,48% 25%,66% 70%,84% 40%,100% 72%,100% 100%);
  background: #3f5a48;
}

.tgl-18:has(.tgl-18__sw:checked) .tgl-18__ridge {
  filter: brightness(.35) saturate(.6);
}

.tgl-18__lbl {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .06em;
  color: #39506b;
  transition: color .7s;
}

.tgl-18:has(.tgl-18__sw:checked) .tgl-18__lbl {
  color: #aab6d4;
}

.tgl-18__sw:focus-visible {
  outline: 3px solid #6ea8ff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-18,
    .tgl-18__sw,
    .tgl-18__sw::before,
    .tgl-18__moon,
    .tgl-18__stars,
    .tgl-18__ridge,
    .tgl-18__lbl {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — sun and moon swap along mirrored diagonal transforms inside an overflow-hidden scene while the sky crossfades and :has() re-themes the page. */
```
