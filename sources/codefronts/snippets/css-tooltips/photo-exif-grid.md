---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/photo-exif-grid/"
title: "Photo EXIF Grid"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A dark contact-sheet grid of eight gradient photographs."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Photo EXIF Grid
Source: https://codefronts.com/snippets/css-tooltips/photo-exif-grid/

A dark contact-sheet grid of eight gradient photographs. Hover any cell to lift a developer-tools-style card with full EXIF metadata — camera body, lens, aperture, shutter, ISO, focal length, white balance, and location. For photo portfolios and stock catalogs.
## HTML
```html
<div class="tp-17">
  <div class="tp-17__grid">
    <div class="tp-17__cell">
      <div class="tp-17__img" style="background:linear-gradient(160deg,#c86020 0%,#e8a030 40%,#f0c060 70%,#a04010 100%)"></div>
      <div class="tp-17__tip">
        <div class="tp-17__tip-head"><div><div class="tp-17__camera">Sony A7 IV</div><div class="tp-17__lens">FE 24-70mm f/2.8 GM</div></div><div class="tp-17__date">Mar 14, 2024</div></div>
        <div class="tp-17__settings">
          <div class="tp-17__set"><div class="tp-17__key">Aperture</div><div class="tp-17__val">f/8.0</div></div>
          <div class="tp-17__set"><div class="tp-17__key">Shutter</div><div class="tp-17__val">1/250s</div></div>
          <div class="tp-17__set"><div class="tp-17__key">ISO</div><div class="tp-17__val">100</div></div>
        </div>
        <div class="tp-17__extra"><span>Focal: <strong>35mm</strong></span><span>WB: <strong>Daylight</strong></span><span>Malibu, CA</span></div>
      </div>
    </div>
    <div class="tp-17__cell">
      <div class="tp-17__img" style="background:linear-gradient(145deg,#1a1218 0%,#2c1828 50%,#180c14 100%)"></div>
      <div class="tp-17__tip">
        <div class="tp-17__tip-head"><div><div class="tp-17__camera">Nikon Z6 III</div><div class="tp-17__lens">NIKKOR Z 85mm f/1.8 S</div></div><div class="tp-17__date">Jan 8, 2024</div></div>
        <div class="tp-17__settings">
          <div class="tp-17__set"><div class="tp-17__key">Aperture</div><div class="tp-17__val">f/1.8</div></div>
          <div class="tp-17__set"><div class="tp-17__key">Shutter</div><div class="tp-17__val">1/160s</div></div>
          <div class="tp-17__set"><div class="tp-17__key">ISO</div><div class="tp-17__val">800</div></div>
        </div>
        <div class="tp-17__extra"><span>Focal: <strong>85mm</strong></span><span>WB: <strong>Tungsten</strong></span><span>Flash: <strong>Off</strong></span></div>
      </div>
    </div>
    <div class="tp-17__cell">
      <div class="tp-17__img" style="background:linear-gradient(180deg,#082840 0%,#0c4060 35%,#1060a0 70%,#082040 100%)"></div>
      <div class="tp-17__tip">
        <div class="tp-17__tip-head"><div><div class="tp-17__camera">Fujifilm X-T5</div><div class="tp-17__lens">XF 16-80mm f/4 R</div></div><div class="tp-17__date">Feb 22, 2024</div></div>
        <div class="tp-17__settings">
          <div class="tp-17__set"><div class="tp-17__key">Aperture</div><div class="tp-17__val">f/11</div></div>
          <div class="tp-17__set"><div class="tp-17__key">Shutter</div><div class="tp-17__val">1/500s</div></div>
          <div class="tp-17__set"><div class="tp-17__key">ISO</div><div class="tp-17__val">200</div></div>
        </div>
        <div class="tp-17__extra"><span>Focal: <strong>16mm</strong></span><span>WB: <strong>Cloudy</strong></span><span>Big Sur, CA</span></div>
      </div>
    </div>
    <div class="tp-17__cell">
      <div class="tp-17__img" style="background:linear-gradient(135deg,#0c1e10 0%,#1a3818 40%,#2a5a28 70%,#0c2010 100%)"></div>
      <div class="tp-17__tip">
        <div class="tp-17__tip-head"><div><div class="tp-17__camera">Canon EOS R5</div><div class="tp-17__lens">RF 24-105mm f/4L IS</div></div><div class="tp-17__date">Apr 5, 2024</div></div>
        <div class="tp-17__settings">
          <div class="tp-17__set"><div class="tp-17__key">Aperture</div><div class="tp-17__val">f/5.6</div></div>
          <div class="tp-17__set"><div class="tp-17__key">Shutter</div><div class="tp-17__val">1/60s</div></div>
          <div class="tp-17__set"><div class="tp-17__key">ISO</div><div class="tp-17__val">400</div></div>
        </div>
        <div class="tp-17__extra"><span>Focal: <strong>50mm</strong></span><span>WB: <strong>Shade</strong></span><span>Olympic NP</span></div>
      </div>
    </div>
    <div class="tp-17__cell">
      <div class="tp-17__img" style="background:linear-gradient(160deg,#080c18 0%,#101428 40%,#181c30 70%,#0c0e20 100%)"></div>
      <div class="tp-17__tip">
        <div class="tp-17__tip-head"><div><div class="tp-17__camera">Sony A7 IV</div><div class="tp-17__lens">FE 50mm f/1.4 GM</div></div><div class="tp-17__date">Dec 18, 2023</div></div>
        <div class="tp-17__settings">
          <div class="tp-17__set"><div class="tp-17__key">Aperture</div><div class="tp-17__val">f/2.0</div></div>
          <div class="tp-17__set"><div class="tp-17__key">Shutter</div><div class="tp-17__val">1/30s</div></div>
          <div class="tp-17__set"><div class="tp-17__key">ISO</div><div class="tp-17__val">3200</div></div>
        </div>
        <div class="tp-17__extra"><span>Focal: <strong>50mm</strong></span><span>WB: <strong>Auto</strong></span><span>Tokyo, JP</span></div>
      </div>
    </div>
    <div class="tp-17__cell">
      <div class="tp-17__img" style="background:linear-gradient(155deg,#604020 0%,#d09050 40%,#f0c880 70%,#806030 100%)"></div>
      <div class="tp-17__tip">
        <div class="tp-17__tip-head"><div><div class="tp-17__camera">Hasselblad X2D</div><div class="tp-17__lens">XCD 45mm f/3.5</div></div><div class="tp-17__date">Nov 3, 2023</div></div>
        <div class="tp-17__settings">
          <div class="tp-17__set"><div class="tp-17__key">Aperture</div><div class="tp-17__val">f/16</div></div>
          <div class="tp-17__set"><div class="tp-17__key">Shutter</div><div class="tp-17__val">1/1000s</div></div>
          <div class="tp-17__set"><div class="tp-17__key">ISO</div><div class="tp-17__val">64</div></div>
        </div>
        <div class="tp-17__extra"><span>Focal: <strong>45mm</strong></span><span>WB: <strong>Daylight</strong></span><span>Sahara, Morocco</span></div>
      </div>
    </div>
    <div class="tp-17__cell">
      <div class="tp-17__img" style="background:linear-gradient(170deg,#c8c8cc 0%,#a8a8b0 40%,#d0d0d4 70%,#b0b0b8 100%)"></div>
      <div class="tp-17__tip">
        <div class="tp-17__tip-head"><div><div class="tp-17__camera">Leica M11</div><div class="tp-17__lens">Summicron 50mm f/2</div></div><div class="tp-17__date">Oct 14, 2023</div></div>
        <div class="tp-17__settings">
          <div class="tp-17__set"><div class="tp-17__key">Aperture</div><div class="tp-17__val">f/4.0</div></div>
          <div class="tp-17__set"><div class="tp-17__key">Shutter</div><div class="tp-17__val">1/125s</div></div>
          <div class="tp-17__set"><div class="tp-17__key">ISO</div><div class="tp-17__val">200</div></div>
        </div>
        <div class="tp-17__extra"><span>Focal: <strong>50mm</strong></span><span>WB: <strong>Cloudy</strong></span><span>Highlands, UK</span></div>
      </div>
    </div>
    <div class="tp-17__cell">
      <div class="tp-17__img" style="background:linear-gradient(150deg,#200830 0%,#401060 40%,#602080 65%,#100420 100%)"></div>
      <div class="tp-17__tip">
        <div class="tp-17__tip-head"><div><div class="tp-17__camera">Nikon Z6 III</div><div class="tp-17__lens">NIKKOR Z 14-30mm f/4 S</div></div><div class="tp-17__date">Sep 27, 2023</div></div>
        <div class="tp-17__settings">
          <div class="tp-17__set"><div class="tp-17__key">Aperture</div><div class="tp-17__val">f/2.8</div></div>
          <div class="tp-17__set"><div class="tp-17__key">Shutter</div><div class="tp-17__val">20s</div></div>
          <div class="tp-17__set"><div class="tp-17__key">ISO</div><div class="tp-17__val">1600</div></div>
        </div>
        <div class="tp-17__extra"><span>Focal: <strong>14mm</strong></span><span>WB: <strong>3200K</strong></span><span>Iceland</span></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-17 {
  min-height: 100vh;
  background: #080808;
  /* Top room — EXIF cards pop UP from each photo, ~180px tall. */
  padding: 220px 28px 40px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  /* Force full width of the .cf-stage flex parent. Without this, the
       stage collapses to its content's min-width and the 4-column grid
       inside resolves each 1fr track to ~0px, stacking all 8 photos as
       one thin vertical strip. */
  width: 100%;
  box-sizing: border-box;
}

.tp-17__grid {
  max-width: 600px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 3px;
}

.tp-17__cell {
  position: relative;
  aspect-ratio: 3 / 2;
  cursor: help;
}

.tp-17__img {
  width: 100%;
  height: 100%;
  display: block;
  transition: filter .2s;
}

.tp-17__cell:hover .tp-17__img {
  filter: brightness(1.1);
}

.tp-17__tip {
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(-6px);
  z-index: 100;
  width: 230px;
  background: #111;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 6px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  box-shadow: 0 16px 44px rgba(0, 0, 0, 0.98);
  overflow: hidden;
  text-align: left;
}

.tp-17__cell:hover .tp-17__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-17__tip-head {
  padding: 11px 13px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.tp-17__camera {
  font-size: 10.5px;
  color: rgba(255, 255, 255, 0.7);
}

.tp-17__lens {
  font-size: 8.5px;
  color: rgba(255, 255, 255, 0.2);
  margin-top: 2px;
}

.tp-17__date {
  font-size: 8.5px;
  color: rgba(255, 255, 255, 0.2);
}

.tp-17__settings {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.tp-17__set {
  padding: 9px 13px;
  border-right: 1px solid rgba(255, 255, 255, 0.04);
}

.tp-17__set:last-child {
  border-right: none;
}

.tp-17__key {
  font-size: 6.5px;
  color: rgba(255, 255, 255, 0.2);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 2px;
}

.tp-17__val {
  font-size: 10.5px;
  color: rgba(255, 255, 255, 0.65);
}

.tp-17__extra {
  display: flex;
  justify-content: space-between;
  padding: 8px 13px;
  font-size: 8.5px;
  color: rgba(255, 255, 255, 0.25);
  gap: 6px;
}

.tp-17__extra strong {
  color: rgba(255, 255, 255, 0.45);
  font-weight: 500;
}
```
