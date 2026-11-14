---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/haptic-mechanical-keycap-toggles/"
title: "Haptic Mechanical Keycap Toggles"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A bank of mechanical keyboard keycaps that toggle settings: each cap physically travels down into its socket on press, latches with a backlit glow when on —…"
has_js: "true"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Haptic Mechanical Keycap Toggles
Source: https://codefronts.com/components/css-toggles-switches/haptic-mechanical-keycap-toggles/

A bank of mechanical keyboard keycaps that toggle settings: each cap physically travels down into its socket on press, latches with a backlit glow when on — and fires a real haptic pulse through the Vibration API on supporting devices.
## HTML
```html
<section class="tgl-08" aria-label="Mechanical keycap toggles">
  <div class="tgl-08__board" id="tgl-08-board">
    <label class="tgl-08__key" style="--glow:oklch(0.75 0.16 220)"><input type="checkbox" class="tgl-08__sw" role="switch" checked><span class="tgl-08__cap">MIC</span></label>
    <label class="tgl-08__key" style="--glow:oklch(0.78 0.16 150)"><input type="checkbox" class="tgl-08__sw" role="switch"><span class="tgl-08__cap">CAM</span></label>
    <label class="tgl-08__key" style="--glow:oklch(0.75 0.17 20)"><input type="checkbox" class="tgl-08__sw" role="switch"><span class="tgl-08__cap">REC</span></label>
  </div>
  <p class="tgl-08__cap-note">Latching keys · haptic tick on supported devices</p>
</section>
```
## CSS
```css
.tgl-08,
.tgl-08 *,
.tgl-08 *::before,
.tgl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-08 {
  font-family: ui-monospace,'SF Mono',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 30px;
  padding: 60px 20px;
  background: #191b1f;
}

.tgl-08__board {
  display: flex;
  gap: 18px;
  padding: 22px 26px;
  border-radius: 18px;
  background: linear-gradient(160deg,#23262c,#1c1e23);
  box-shadow: 0 24px 50px -26px #000,inset 0 1px 0 rgba(255,255,255,.06);
}

.tgl-08__key {
  position: relative;
  display: block;
  width: 76px;
  height: 76px;
  cursor: pointer;
}

.tgl-08__sw {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
  inset: -4px;
  cursor: pointer;
  z-index: 2;
  border-radius: 12px;
}

.tgl-08__cap {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background: linear-gradient(180deg,#3a3e46,#2b2e35);
  color: #8b919d;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .12em;
  box-shadow: 0 7px 0 #15161a,0 12px 18px -6px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.1);
  transition: transform .09s ease-out,box-shadow .09s ease-out,color .2s,text-shadow .2s;
}

.tgl-08__key:active .tgl-08__cap {
  transform: translateY(5px);
  box-shadow: 0 2px 0 #15161a,0 5px 10px -4px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.08);
}

.tgl-08__sw:checked ~ .tgl-08__cap {
  transform: translateY(3px);
  box-shadow: 0 4px 0 #15161a,0 8px 14px -6px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.08);
  color: var(--glow);
  text-shadow: 0 0 10px var(--glow),0 0 26px color-mix(in oklab,var(--glow) 55%,transparent);
}

.tgl-08__sw:checked:active ~ .tgl-08__cap,
.tgl-08__key:has(.tgl-08__sw:checked):active .tgl-08__cap {
  transform: translateY(5px);
}

.tgl-08__sw:focus-visible ~ .tgl-08__cap {
  outline: 3px solid #6ea8ff;
  outline-offset: 4px;
}

.tgl-08__cap-note {
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #565b66;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-08__cap {
    transition: color .2s,text-shadow .2s;
  }
}
```

## JavaScript
```js
(() => {
  // Haptic tick: an 8ms vibration pulse per toggle, on hardware that supports it.
  const board = document.querySelector('#tgl-08-board');
  board.addEventListener('change', () => {
    if (navigator.vibrate) navigator.vibrate(8);
  });
})();
```
