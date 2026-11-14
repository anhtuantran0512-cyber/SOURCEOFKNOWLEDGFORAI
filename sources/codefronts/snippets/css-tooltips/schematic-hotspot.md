---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/schematic-hotspot/"
title: "Schematic Hotspot"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "For product diagrams and exploded views."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Schematic Hotspot
Source: https://codefronts.com/snippets/css-tooltips/schematic-hotspot/

For product diagrams and exploded views. Four pulsing red dots dot a wireframe drawing; hover any one and a leader line draws itself to a numbered callout box with part name, description, and a tiny spec table. The whole annotation reads like a CAD title block.
## HTML
```html
<div class="tp-01">
  <div class="tp-01__paper">
    <span class="tp-01__corner tp-01__tl"></span>
    <span class="tp-01__corner tp-01__tr"></span>
    <span class="tp-01__corner tp-01__bl"></span>
    <span class="tp-01__corner tp-01__br"></span>
    <div class="tp-01__meta">
      <span>DWG-0142-A · CAMERA / EXPLODED VIEW</span>
      <span class="tp-01__right">SCALE 1:1 · REV 04<br>14.MAY.2026</span>
    </div>
    <div class="tp-01__object">
      <svg class="tp-01__svg" viewBox="0 0 800 460" preserveAspectRatio="xMidYMid meet">
        <rect x="200" y="160" width="400" height="200" stroke="#1c2330" stroke-width="1.5" fill="none"/>
        <rect x="340" y="130" width="80" height="30" stroke="#1c2330" stroke-width="1.5" fill="none"/>
        <rect x="355" y="120" width="50" height="10" stroke="#1c2330" stroke-width="1" fill="none"/>
        <path d="M200 160 L160 180 L160 340 L200 360 Z" stroke="#1c2330" stroke-width="1.5" fill="none"/>
        <circle cx="450" cy="260" r="90" stroke="#1c2330" stroke-width="1.5" fill="none"/>
        <circle cx="450" cy="260" r="68" stroke="#1c2330" stroke-width="1" fill="none"/>
        <circle cx="450" cy="260" r="46" stroke="#1c2330" stroke-width="0.8" fill="none"/>
        <circle cx="450" cy="260" r="24" stroke="#1c2330" stroke-width="0.6" fill="none"/>
        <circle cx="260" cy="200" r="22" stroke="#1c2330" stroke-width="1" fill="none"/>
        <circle cx="260" cy="200" r="3" fill="#1c2330"/>
        <circle cx="540" cy="200" r="18" stroke="#1c2330" stroke-width="1" fill="none"/>
        <rect x="320" y="190" width="40" height="28" stroke="#1c2330" stroke-width="0.8" fill="none"/>
        <line x1="200" y1="380" x2="600" y2="380" stroke="#1c2330" stroke-width="0.5" stroke-dasharray="4,4"/>
        <text x="400" y="398" text-anchor="middle" font-family="IBM Plex Mono" font-size="10" fill="#1c2330">142mm</text>
      </svg>
      <div class="tp-01__hot tp-01__hot-1"></div>
      <svg class="tp-01__leader tp-01__leader-1"><line x1="0" y1="100" x2="180" y2="0" stroke="#1c2330" stroke-width="1"/></svg>
      <div class="tp-01__note tp-01__note-1">
        <div class="tp-01__num">01</div>
        <div class="tp-01__label">— Optical Assembly</div>
        <div class="tp-01__part">35mm <em>f/1.4</em> prime</div>
        <div class="tp-01__desc">Twelve-element design across nine groups. Aspherical front and rear, two ED elements mid-stack.</div>
        <div class="tp-01__spec">
          <span class="tp-01__k">Glass</span><span class="tp-01__v">12 / 9</span>
          <span class="tp-01__k">Coating</span><span class="tp-01__v">Nano-V</span>
          <span class="tp-01__k">Weight</span><span class="tp-01__v">410g</span>
        </div>
      </div>
      <div class="tp-01__hot tp-01__hot-2"></div>
      <svg class="tp-01__leader tp-01__leader-2"><line x1="160" y1="80" x2="0" y2="0" stroke="#1c2330" stroke-width="1"/></svg>
      <div class="tp-01__note tp-01__note-2">
        <div class="tp-01__num">02</div>
        <div class="tp-01__label">— Shutter Dial</div>
        <div class="tp-01__part">Mechanical <em>command</em> dial</div>
        <div class="tp-01__desc">Detented brass with knurled edge. Range 1/8000s to 30s plus bulb. Locks with a quarter-press.</div>
        <div class="tp-01__spec">
          <span class="tp-01__k">Steps</span><span class="tp-01__v">1/3 EV</span>
          <span class="tp-01__k">Travel</span><span class="tp-01__v">300°</span>
          <span class="tp-01__k">Cycles</span><span class="tp-01__v">500k</span>
        </div>
      </div>
      <div class="tp-01__hot tp-01__hot-3"></div>
      <svg class="tp-01__leader tp-01__leader-3"><line x1="0" y1="120" x2="80" y2="0" stroke="#1c2330" stroke-width="1"/></svg>
      <div class="tp-01__note tp-01__note-3">
        <div class="tp-01__num">03</div>
        <div class="tp-01__label">— Accessory Port</div>
        <div class="tp-01__part">ISO 518 <em>hot shoe</em></div>
        <div class="tp-01__desc">Standard mount with X-sync at 1/250s. Center pin plus four data contacts for TTL flash control.</div>
        <div class="tp-01__spec">
          <span class="tp-01__k">Sync</span><span class="tp-01__v">1/250s</span>
          <span class="tp-01__k">Pins</span><span class="tp-01__v">1+4</span>
          <span class="tp-01__k">Hot</span><span class="tp-01__v">12V</span>
        </div>
      </div>
      <div class="tp-01__hot tp-01__hot-4"></div>
      <svg class="tp-01__leader tp-01__leader-4"><line x1="160" y1="0" x2="0" y2="80" stroke="#1c2330" stroke-width="1"/></svg>
      <div class="tp-01__note tp-01__note-4">
        <div class="tp-01__num">04</div>
        <div class="tp-01__label">— Hand Grip</div>
        <div class="tp-01__part">Magnesium <em>undergrip</em></div>
        <div class="tp-01__desc">Cast magnesium core wrapped in pressed cowhide. Conceals battery, card slot, and focus-recall trigger.</div>
        <div class="tp-01__spec">
          <span class="tp-01__k">Wrap</span><span class="tp-01__v">Cowhide</span>
          <span class="tp-01__k">Core</span><span class="tp-01__v">MgAl</span>
          <span class="tp-01__k">Battery</span><span class="tp-01__v">7.4 Wh</span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-01 {
  min-height: 100vh;
  background: #f4f3ee;
  padding: 32px 24px;
  background-image: linear-gradient(rgba(28, 35, 48, 0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(28, 35, 48, 0.06) 1px, transparent 1px);
  background-size: 24px 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Inter', system-ui, sans-serif;
  color: #1c2330;
  /* Force full width of the stage. .cf-stage uses align-items: center
       which collapses children to their content-min-width when they
       don't declare an explicit width. Without this, .tp-01__paper's
       width: 100% resolves against a collapsed parent and produces the
       tiny-square + content-overflow we saw. */
  width: 100%;
  box-sizing: border-box;
}

.tp-01__paper {
  position: relative;
  width: 100%;
  max-width: 760px;
  aspect-ratio: 16 / 10;
  background: #fbfaf6;
  border: 1px solid rgba(28, 35, 48, 0.2);
  overflow: visible;
}

.tp-01__paper::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(28, 35, 48, 0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(28, 35, 48, 0.05) 1px, transparent 1px);
  background-size: 18px 18px;
  pointer-events: none;
}

.tp-01__meta {
  position: absolute;
  top: 12px;
  left: 16px;
  right: 16px;
  display: flex;
  justify-content: space-between;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9.5px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: rgba(28, 35, 48, 0.55);
  z-index: 2;
}

.tp-01__right {
  text-align: right;
  line-height: 1.6;
}

.tp-01__corner {
  position: absolute;
  width: 12px;
  height: 12px;
  border: 1px solid rgba(28, 35, 48, 0.4);
}

.tp-01__tl {
  top: 6px;
  left: 6px;
  border-right: none;
  border-bottom: none;
}

.tp-01__tr {
  top: 6px;
  right: 6px;
  border-left: none;
  border-bottom: none;
}

.tp-01__bl {
  bottom: 6px;
  left: 6px;
  border-right: none;
  border-top: none;
}

.tp-01__br {
  bottom: 6px;
  right: 6px;
  border-left: none;
  border-top: none;
}

.tp-01__object {
  position: absolute;
  inset: 50px 60px 50px 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tp-01__svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}

.tp-01__hot {
  position: absolute;
  width: 16px;
  height: 16px;
  margin: -8px;
  border-radius: 50%;
  cursor: help;
  z-index: 5;
}

.tp-01__hot::before {
  content: '';
  position: absolute;
  inset: 5px;
  background: #c1422c;
  border-radius: 50%;
}

.tp-01__hot::after {
  content: '';
  position: absolute;
  inset: 0;
  border: 1px solid #c1422c;
  border-radius: 50%;
  animation: tp-01-pulse 2.4s ease-out infinite;
}

@keyframes tp-01-pulse {
  0% {
    transform: scale(0.6);
    opacity: 0.8;
  }

  100% {
    transform: scale(2);
    opacity: 0;
  }
}

.tp-01__hot-1 {
  top: 56%;
  left: 56.25%;
}

.tp-01__hot-2 {
  top: 25%;
  left: 32.5%;
}

.tp-01__hot-3 {
  top: 30%;
  left: 47.5%;
}

.tp-01__hot-4 {
  top: 56%;
  left: 22.5%;
}
/* Leader lines hidden — they were stylish but only worked with the
   original off-paper annotation positions. Now that notes are clamped
   to the paper's four corners (so .cf-stage doesn't clip them), drawing
   a line from each hotspot to its corner would require per-hotspot
   trig that's not worth the complexity. Keeping the SVG markup in
   place so the adjacent-sibling selector chain
   (.tp-01__hot:hover + .tp-01__leader + .tp-01__note) still resolves. */

.tp-01__leader {
  display: none;
}

.tp-01__note {
  position: absolute;
  width: 190px;
  background: #fbfaf6;
  border: 1px solid #1c2330;
  padding: 11px 13px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  line-height: 1.6;
  color: #1c2330;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s, visibility 0s linear 0.3s;
  pointer-events: none;
  z-index: 10;
  box-shadow: 4px 4px 0 rgba(28, 35, 48, 0.08);
}

.tp-01__hot:hover + .tp-01__leader + .tp-01__note {
  opacity: 1;
  visibility: visible;
  transition-delay: 0.12s;
}
/* Annotations positioned in each corner of the schematic object's
   coordinate space — kept inside the paper bounds so they don't get
   clipped by .cf-stage's overflow:hidden. Hotspot 1 (lens) lower-right,
   note in upper-right; hotspot 2 (top dial) upper-left, note upper-left;
   hotspot 3 (hot shoe) top-center, note top-right; hotspot 4 (grip)
   lower-left, note lower-left. */

.tp-01__note-1 {
  top: 4%;
  right: 0;
  left: auto;
}

.tp-01__note-2 {
  top: 4%;
  left: 0;
}

.tp-01__note-3 {
  top: 4%;
  left: 50%;
}

.tp-01__note-4 {
  bottom: 4%;
  left: 0;
  top: auto;
}

.tp-01__num {
  display: inline-block;
  font-family: Georgia, serif;
  font-weight: 500;
  font-style: italic;
  color: #c1422c;
  font-size: 20px;
  line-height: 1;
  margin-bottom: 3px;
}

.tp-01__label {
  font-size: 9.5px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: rgba(28, 35, 48, 0.6);
  margin-bottom: 6px;
}

.tp-01__part {
  font-family: Georgia, serif;
  font-size: 15px;
  font-weight: 500;
  line-height: 1.2;
  margin-bottom: 6px;
  color: #1c2330;
}

.tp-01__part em {
  font-style: italic;
  color: #c1422c;
}

.tp-01__desc {
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 10.5px;
  color: rgba(28, 35, 48, 0.75);
  line-height: 1.5;
}

.tp-01__spec {
  margin-top: 8px;
  padding-top: 6px;
  border-top: 1px dashed rgba(28, 35, 48, 0.3);
  display: grid;
  grid-template-columns: 54px 1fr;
  gap: 3px 8px;
  font-size: 9.5px;
}

.tp-01__k {
  color: rgba(28, 35, 48, 0.5);
}

.tp-01__v {
  color: #c1422c;
}
```
