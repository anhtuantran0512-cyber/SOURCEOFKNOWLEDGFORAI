---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/bauhaus-cube-navigator/"
title: "Cube Face Navigation with Drag and Auto Rotate"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "A six-faced cube used as a portfolio navigator, driven three ways: six preset buttons that fly to a named face, drag to orbit freely with the mouse or a…"
has_js: "true"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cube Face Navigation with Drag and Auto Rotate
Source: https://codefronts.com/design-styles/css-3d/bauhaus-cube-navigator/

A six-faced cube used as a portfolio navigator, driven three ways: six preset buttons that fly to a named face, drag to orbit freely with the mouse or a finger, and an auto-rotate toggle running off requestAnimationFrame. All six faces derive their translateZ from one size token, so the cube is resized by changing a single number.
## HTML
```html
<section class="d3-16" aria-label="Bauhaus 3D cube navigator demo">

  <div class="d3-16__theme">
    <input class="d3-16__theme-input" type="checkbox" id="d3-16-theme">
    <label class="d3-16__theme-label" for="d3-16-theme" aria-label="Toggle light and dark theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg>
    </label>
  </div>

  <div class="card">
    <div class="scene">
      <div class="cube" data-d3-16-cube>

        <div class="face face-front">
          <span class="face-num">01</span>
          <span class="face-tag">Visual Identity</span>
          <div class="face-label">Brand<br />System</div>
        </div>
        <div class="face face-back">
          <span class="face-num">02</span>
          <span class="face-tag">Digital Experience</span>
          <div class="face-label">Web<br />Design</div>
        </div>
        <div class="face face-left">
          <span class="face-num">03</span>
          <span class="face-tag">Creative Strategy</span>
          <div class="face-label">Motion<br />Art</div>
        </div>
        <div class="face face-right">
          <span class="face-num">04</span>
          <span class="face-tag">Environmental</span>
          <div class="face-label">Space<br />Design</div>
        </div>
        <div class="face face-top">
          <span class="face-num">05</span>
          <span class="face-tag">Systems Thinking</span>
          <div class="face-label">Type<br />Craft</div>
        </div>
        <div class="face face-bottom">
          <span class="face-num">06</span>
          <span class="face-tag">Material Culture</span>
          <div class="face-label">Print<br />Works</div>
        </div>

      </div>
    </div>

    <div class="controls" data-d3-16-controls>
      <button class="ctrl-btn active" type="button" data-face="front"  data-rx="-18" data-ry="22">Brand</button>
      <button class="ctrl-btn"        type="button" data-face="back"   data-rx="-18" data-ry="202">Web</button>
      <button class="ctrl-btn"        type="button" data-face="left"   data-rx="-18" data-ry="112">Motion</button>
      <button class="ctrl-btn"        type="button" data-face="right"  data-rx="-18" data-ry="-68">Space</button>
      <button class="ctrl-btn"        type="button" data-face="top"    data-rx="-108" data-ry="22">Type</button>
      <button class="ctrl-btn"        type="button" data-face="bottom" data-rx="72"  data-ry="22">Print</button>
    </div>

    <div class="auto-toggle" data-d3-16-autotoggle>
      <div class="toggle-track" data-d3-16-autotrack>
        <div class="toggle-thumb"></div>
      </div>
      <span>Auto-rotate</span>
    </div>

  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Grotesk:wght@300;400;500;600&display=swap');

.d3-16 {
  --d3-16-ground: #f0ede8;
  --d3-16-grain: rgba(0,0,0,0.05);
  --d3-16-red: #e63b2e;
  --d3-16-blue: #2952cc;
  --d3-16-yellow: #f0a500;
  --d3-16-green: #1a8a4a;
  --d3-16-black: #111111;
  --d3-16-bone: #e8e2d8;
  --d3-16-ink-chroma: #ffffff;
  --d3-16-ink-yellow: #1a1000;
  --d3-16-ink-top: #ffffff;
  --d3-16-ink-bottom: #111111;
  --d3-16-ink-bottom-tag: #1a1000;
  --d3-16-shade-dark: rgba(0,0,0,0.08);
  --d3-16-shade-light: rgba(255,255,255,0.06);
  --d3-16-face-outline: rgba(0,0,0,0.08);
  --d3-16-right-plate: rgba(255,255,255,0.07);
  --d3-16-left-frame: rgba(0,0,0,0.10);
  --d3-16-top-hatch: rgba(255,255,255,0.03);
  --d3-16-bottom-vignette: rgba(0,0,0,0.04);
  --d3-16-ctrl-line: #111111;
  --d3-16-ctrl-ink: #111111;
  --d3-16-ctrl-active-bg: #111111;
  --d3-16-ctrl-neutral: #999999;
  --d3-16-switch-off: rgba(0,0,0,0.15);
  --d3-16-switch-on: #111111;
  --d3-16-switch-thumb: #ffffff;
  --d3-16-muted: rgba(0,0,0,0.45);
  --d3-16-ui-face: rgba(255,255,255,0.70);
  --d3-16-ui-line: rgba(17,17,17,0.25);
  --d3-16-ui-ink: #111111;
  width: 100%;
  min-height: max(100vh, 620px);
  display: block;
  position: relative;
  background: var(--d3-16-ground);
  font-family: 'Space Grotesk', system-ui, sans-serif;
  overflow: hidden;
  box-sizing: border-box;
}

.d3-16 *,
.d3-16 *::before,
.d3-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.d3-16:has(.d3-16__theme-input:checked) {
  --d3-16-ground: #16151a;
  --d3-16-grain: rgba(255,255,255,0.05);
  --d3-16-red: #f2543f;
  --d3-16-blue: #5f81ff;
  --d3-16-yellow: #ffc233;
  --d3-16-green: #23b263;
  --d3-16-black: #f0ece4;
  --d3-16-bone: #2a2833;
  --d3-16-ink-chroma: #12100c;
  --d3-16-ink-yellow: #1f1400;
  --d3-16-ink-top: #17161c;
  --d3-16-ink-bottom: #f0ece4;
  --d3-16-ink-bottom-tag: rgba(240,236,228,0.88);
  --d3-16-shade-dark: rgba(0,0,0,0.20);
  --d3-16-shade-light: rgba(255,255,255,0.10);
  --d3-16-face-outline: rgba(255,255,255,0.14);
  --d3-16-right-plate: rgba(0,0,0,0.16);
  --d3-16-left-frame: rgba(0,0,0,0.26);
  --d3-16-top-hatch: rgba(0,0,0,0.10);
  --d3-16-bottom-vignette: rgba(255,255,255,0.05);
  --d3-16-ctrl-line: #f0ece4;
  --d3-16-ctrl-ink: #f0ece4;
  --d3-16-ctrl-active-bg: #f0ece4;
  --d3-16-ctrl-neutral: #7c7889;
  --d3-16-switch-off: rgba(255,255,255,0.18);
  --d3-16-switch-on: #f0ece4;
  --d3-16-switch-thumb: #16151a;
  --d3-16-muted: rgba(240,236,228,0.66);
  --d3-16-ui-face: rgba(255,255,255,0.06);
  --d3-16-ui-line: rgba(240,236,228,0.30);
  --d3-16-ui-ink: #f0ece4;
}

@media (prefers-color-scheme: light) {
  .d3-16:has(.d3-16__theme-input:checked) {
    --d3-16-ground: #16151a;
    --d3-16-grain: rgba(255,255,255,0.05);
    --d3-16-red: #f2543f;
    --d3-16-blue: #5f81ff;
    --d3-16-yellow: #ffc233;
    --d3-16-green: #23b263;
    --d3-16-black: #f0ece4;
    --d3-16-bone: #2a2833;
    --d3-16-ink-chroma: #12100c;
    --d3-16-ink-yellow: #1f1400;
    --d3-16-ink-top: #17161c;
    --d3-16-ink-bottom: #f0ece4;
    --d3-16-ink-bottom-tag: rgba(240,236,228,0.88);
    --d3-16-shade-dark: rgba(0,0,0,0.20);
    --d3-16-shade-light: rgba(255,255,255,0.10);
    --d3-16-face-outline: rgba(255,255,255,0.14);
    --d3-16-right-plate: rgba(0,0,0,0.16);
    --d3-16-left-frame: rgba(0,0,0,0.26);
    --d3-16-top-hatch: rgba(0,0,0,0.10);
    --d3-16-bottom-vignette: rgba(255,255,255,0.05);
    --d3-16-ctrl-line: #f0ece4;
    --d3-16-ctrl-ink: #f0ece4;
    --d3-16-ctrl-active-bg: #f0ece4;
    --d3-16-ctrl-neutral: #7c7889;
    --d3-16-switch-off: rgba(255,255,255,0.18);
    --d3-16-switch-on: #f0ece4;
    --d3-16-switch-thumb: #16151a;
    --d3-16-muted: rgba(240,236,228,0.66);
    --d3-16-ui-face: rgba(255,255,255,0.06);
    --d3-16-ui-line: rgba(240,236,228,0.30);
    --d3-16-ui-ink: #f0ece4;
  }
}

@media (prefers-color-scheme: dark) {
  .d3-16:has(.d3-16__theme-input:checked) {
    --d3-16-ground: #16151a;
    --d3-16-grain: rgba(255,255,255,0.05);
    --d3-16-red: #f2543f;
    --d3-16-blue: #5f81ff;
    --d3-16-yellow: #ffc233;
    --d3-16-green: #23b263;
    --d3-16-black: #f0ece4;
    --d3-16-bone: #2a2833;
    --d3-16-ink-chroma: #12100c;
    --d3-16-ink-yellow: #1f1400;
    --d3-16-ink-top: #17161c;
    --d3-16-ink-bottom: #f0ece4;
    --d3-16-ink-bottom-tag: rgba(240,236,228,0.88);
    --d3-16-shade-dark: rgba(0,0,0,0.20);
    --d3-16-shade-light: rgba(255,255,255,0.10);
    --d3-16-face-outline: rgba(255,255,255,0.14);
    --d3-16-right-plate: rgba(0,0,0,0.16);
    --d3-16-left-frame: rgba(0,0,0,0.26);
    --d3-16-top-hatch: rgba(0,0,0,0.10);
    --d3-16-bottom-vignette: rgba(255,255,255,0.05);
    --d3-16-ctrl-line: #f0ece4;
    --d3-16-ctrl-ink: #f0ece4;
    --d3-16-ctrl-active-bg: #f0ece4;
    --d3-16-ctrl-neutral: #7c7889;
    --d3-16-switch-off: rgba(255,255,255,0.18);
    --d3-16-switch-on: #f0ece4;
    --d3-16-switch-thumb: #16151a;
    --d3-16-muted: rgba(240,236,228,0.66);
    --d3-16-ui-face: rgba(255,255,255,0.06);
    --d3-16-ui-line: rgba(240,236,228,0.30);
    --d3-16-ui-ink: #f0ece4;
  }
}

.d3-16 .d3-16__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 30;
}

.d3-16 .d3-16__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 1;
}

.d3-16 .d3-16__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-16-ui-line);
  border-radius: 4px;
  background: var(--d3-16-ui-face);
  color: var(--d3-16-ui-ink);
  pointer-events: none;
}

.d3-16 .d3-16__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-16 .d3-16__theme-input:focus-visible + .d3-16__theme-label {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.d3-16 .card {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 32px 24px;
}

.d3-16 .card::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: radial-gradient(var(--d3-16-grain) 0.6px, transparent 0.6px);
  background-size: 4px 4px;
  pointer-events: none;
}

.d3-16 .scene {
  perspective: 1400px;
  width: 320px;
  height: 320px;
  margin-bottom: 36px;
  position: relative;
  z-index: 1;
}

.d3-16 .cube {
  width: 280px;
  height: 280px;
  position: relative;
  transform-style: preserve-3d;
  transform: rotateX(-18deg) rotateY(22deg);
  transition: transform 0.85s cubic-bezier(0.23, 1, 0.32, 1);
  margin: 20px auto;
  will-change: transform;
  cursor: grab;
}

.d3-16 .cube.dragging {
  cursor: grabbing;
}

.d3-16 .face {
  position: absolute;
  width: 280px;
  height: 280px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
  padding: 24px;
  overflow: hidden;
  backface-visibility: visible;
}

.d3-16 .face-front {
  transform: translateZ(140px);
  background: var(--d3-16-red);
}

.d3-16 .face-back {
  transform: rotateY(180deg) translateZ(140px);
  background: var(--d3-16-blue);
}

.d3-16 .face-left {
  transform: rotateY(-90deg) translateZ(140px);
  background: var(--d3-16-yellow);
}

.d3-16 .face-right {
  transform: rotateY(90deg) translateZ(140px);
  background: var(--d3-16-green);
}

.d3-16 .face-top {
  transform: rotateX(90deg) translateZ(140px);
  background: var(--d3-16-black);
}

.d3-16 .face-bottom {
  transform: rotateX(-90deg) translateZ(140px);
  background: var(--d3-16-bone);
}

.d3-16 .face-front::before {
  content: '';
  position: absolute;
  top: -60px;
  right: -60px;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: var(--d3-16-shade-dark);
}

.d3-16 .face-back::before {
  content: '';
  position: absolute;
  top: 20px;
  left: 20px;
  width: 0;
  height: 0;
  border-left: 110px solid transparent;
  border-right: 110px solid transparent;
  border-bottom: 180px solid var(--d3-16-shade-light);
}

.d3-16 .face-left::before {
  content: '';
  position: absolute;
  inset: 20px;
  border: 2px solid var(--d3-16-left-frame);
}

.d3-16 .face-right::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 140px;
  height: 140px;
  background: var(--d3-16-right-plate);
}

.d3-16 .face-top::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(45deg, var(--d3-16-top-hatch) 0, var(--d3-16-top-hatch) 1px, transparent 0, transparent 50%);
  background-size: 20px 20px;
}

.d3-16 .face-bottom::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 30% 30%, var(--d3-16-bottom-vignette) 0%, transparent 70%);
}

.d3-16 .face-label {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 56px;
  letter-spacing: 2px;
  line-height: 0.9;
  position: relative;
  z-index: 1;
}

.d3-16 .face-tag {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 9px;
  letter-spacing: 3px;
  text-transform: uppercase;
  margin-bottom: 7px;
  position: relative;
  z-index: 1;
  opacity: 0.72;
}

.d3-16 .face-num {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 108px;
  position: absolute;
  top: -18px;
  right: 14px;
  opacity: 0.08;
  line-height: 1;
  letter-spacing: -4px;
}

.d3-16 .face-front .face-label,
.d3-16 .face-front .face-tag,
.d3-16 .face-front .face-num,
.d3-16 .face-back .face-label,
.d3-16 .face-back .face-tag,
.d3-16 .face-back .face-num,
.d3-16 .face-right .face-label,
.d3-16 .face-right .face-tag,
.d3-16 .face-right .face-num {
  color: var(--d3-16-ink-chroma);
}

.d3-16 .face-top .face-label,
.d3-16 .face-top .face-tag,
.d3-16 .face-top .face-num {
  color: var(--d3-16-ink-top);
}

.d3-16 .face-left .face-label,
.d3-16 .face-left .face-tag,
.d3-16 .face-left .face-num {
  color: var(--d3-16-ink-yellow);
}

.d3-16 .face-bottom .face-tag,
.d3-16 .face-bottom .face-num {
  color: var(--d3-16-ink-bottom-tag);
}

.d3-16 .face-bottom .face-label {
  color: var(--d3-16-ink-bottom);
}

.d3-16 .face::after {
  content: '';
  position: absolute;
  inset: 0;
  box-shadow: inset 0 0 0 1px var(--d3-16-face-outline);
  pointer-events: none;
}

.d3-16 .controls {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
  max-width: 420px;
  position: relative;
  z-index: 1;
}

.d3-16 .ctrl-btn {
  padding: 8px 16px 8px 22px;
  border: 2px solid var(--d3-16-ctrl-line);
  background: transparent;
  color: var(--d3-16-ctrl-ink);
  font-family: 'Space Grotesk', sans-serif;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  cursor: pointer;
  border-radius: 4px;
  transition: background 0.15s, color 0.15s;
  position: relative;
}

.d3-16 .ctrl-btn::before {
  content: '';
  position: absolute;
  left: 8px;
  top: 50%;
  transform: translateY(-50%);
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--d3-16-dot);
}

.d3-16 .ctrl-btn:hover,
.d3-16 .ctrl-btn.active {
  background: var(--d3-16-ctrl-active-bg);
  color: var(--d3-16-ground);
}

.d3-16 .ctrl-btn[data-face="front"] {
  --d3-16-dot: var(--d3-16-red);
}

.d3-16 .ctrl-btn[data-face="back"] {
  --d3-16-dot: var(--d3-16-blue);
}

.d3-16 .ctrl-btn[data-face="left"] {
  --d3-16-dot: var(--d3-16-yellow);
}

.d3-16 .ctrl-btn[data-face="right"] {
  --d3-16-dot: var(--d3-16-green);
}

.d3-16 .ctrl-btn[data-face="top"] {
  --d3-16-dot: var(--d3-16-black);
}

.d3-16 .ctrl-btn[data-face="bottom"] {
  --d3-16-dot: var(--d3-16-ctrl-neutral);
  border-color: var(--d3-16-ctrl-neutral);
}

.d3-16 .auto-toggle {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 14px;
  font-size: 11px;
  letter-spacing: 2px;
  color: var(--d3-16-muted);
  text-transform: uppercase;
  cursor: pointer;
  user-select: none;
  position: relative;
  z-index: 1;
}

.d3-16 .toggle-track {
  width: 36px;
  height: 18px;
  background: var(--d3-16-switch-off);
  border-radius: 9px;
  position: relative;
  transition: background 0.2s;
}

.d3-16 .toggle-track.on {
  background: var(--d3-16-switch-on);
}

.d3-16 .toggle-thumb {
  position: absolute;
  width: 12px;
  height: 12px;
  background: var(--d3-16-switch-thumb);
  border-radius: 50%;
  top: 3px;
  left: 3px;
  transition: transform 0.2s;
}

.d3-16 .toggle-track.on .toggle-thumb {
  transform: translateX(18px);
}

@media (max-width: 720px) {
  .d3-16 .scene {
    width: 260px;
    height: 260px;
  }

  .d3-16 .cube {
    width: 220px;
    height: 220px;
  }

  .d3-16 .face {
    width: 220px;
    height: 220px;
    padding: 18px;
  }

  .d3-16 .face-front {
    transform: translateZ(110px);
  }

  .d3-16 .face-back {
    transform: rotateY(180deg) translateZ(110px);
  }

  .d3-16 .face-left {
    transform: rotateY(-90deg) translateZ(110px);
  }

  .d3-16 .face-right {
    transform: rotateY(90deg) translateZ(110px);
  }

  .d3-16 .face-top {
    transform: rotateX(90deg) translateZ(110px);
  }

  .d3-16 .face-bottom {
    transform: rotateX(-90deg) translateZ(110px);
  }

  .d3-16 .face-label {
    font-size: 42px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .d3-16 .cube {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.d3-16');
  if (!root) return;
  const cube = root.querySelector('[data-d3-16-cube]');
  const controls = root.querySelector('[data-d3-16-controls]');
  const toggle = root.querySelector('[data-d3-16-autotoggle]');
  const track = root.querySelector('[data-d3-16-autotrack]');
  if (!cube || !controls || !toggle || !track) return;

  const btns = controls.querySelectorAll('.ctrl-btn');
  let currentRx = -18, currentRy = 22;
  let autoRotate = false;
  let autoFrame = null;

  function apply() {
    cube.style.transform = 'rotateX(' + currentRx + 'deg) rotateY(' + currentRy + 'deg)';
  }

  function setRotation(rx, ry) {
    currentRx = rx;
    currentRy = ry;
    apply();
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      const rx = parseFloat(btn.dataset.rx);
      const ry = parseFloat(btn.dataset.ry);
      setRotation(rx, ry);
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (autoRotate) stopAuto();
    });
  });

  function startAuto() {
    let start = null;
    const startRy = currentRy;
    function frame(ts) {
      if (!start) start = ts;
      const elapsed = ts - start;
      currentRy = startRy + elapsed * 0.04;
      apply();
      autoFrame = requestAnimationFrame(frame);
    }
    autoFrame = requestAnimationFrame(frame);
  }
  function stopAuto() {
    autoRotate = false;
    track.classList.remove('on');
    if (autoFrame) { cancelAnimationFrame(autoFrame); autoFrame = null; }
  }

  toggle.addEventListener('click', () => {
    autoRotate = !autoRotate;
    track.classList.toggle('on', autoRotate);
    if (autoRotate) startAuto();
    else stopAuto();
  });

  let dragging = false, lastX = 0, lastY = 0;

  cube.addEventListener('mousedown', e => {
    dragging = true;
    cube.classList.add('dragging');
    lastX = e.clientX; lastY = e.clientY;
    if (autoRotate) stopAuto();
    e.preventDefault();
  });
  root.addEventListener('mousemove', e => {
    if (!dragging) return;
    currentRy += (e.clientX - lastX) * 0.5;
    currentRx -= (e.clientY - lastY) * 0.5;
    apply();
    lastX = e.clientX; lastY = e.clientY;
  });
  function endDrag() {
    dragging = false;
    cube.classList.remove('dragging');
  }
  root.addEventListener('mouseup', endDrag);
  root.addEventListener('mouseleave', endDrag);

  cube.addEventListener('touchstart', e => {
    dragging = true;
    lastX = e.touches[0].clientX;
    lastY = e.touches[0].clientY;
    if (autoRotate) stopAuto();
  }, { passive: true });
  root.addEventListener('touchmove', e => {
    if (!dragging) return;
    const t = e.touches[0];
    currentRy += (t.clientX - lastX) * 0.5;
    currentRx -= (t.clientY - lastY) * 0.5;
    apply();
    lastX = t.clientX;
    lastY = t.clientY;
  }, { passive: true });
  root.addEventListener('touchend', endDrag);
})();
```
