---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/vinyl-record/"
title: "Retro Vinyl Record Rotating Menu"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A turntable you can browse with: the record's grooves are one repeating-radial-gradient, four track chips sit around the platter, and choosing a track drops…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Vinyl Record Rotating Menu
Source: https://codefronts.com/navigation/css-circular-menus/vinyl-record/

A turntable you can browse with: the record's grooves are one repeating-radial-gradient, four track chips sit around the platter, and choosing a track drops the tonearm onto the vinyl and starts the spin. Selecting a track is the play action — navigation and player state collapse into one gorgeous object.
## HTML
```html
<section class="ccm-21" aria-label="Vinyl record menu demo">
  <div class="ccm-21__stage">
    <div class="ccm-21__deck">
      <div class="ccm-21__platter" aria-hidden="true">
        <div class="ccm-21__vinyl"><span class="ccm-21__labelface"><b>MIDNIGHT</b><i>SIDE A</i></span></div>
      </div>
      <div class="ccm-21__arm" aria-hidden="true"><i class="ccm-21__weight"></i><i class="ccm-21__head"></i></div>
      <fieldset class="ccm-21__tracks"><legend class="ccm-21__sr">Choose a track</legend>
        <div><input type="radio" name="ccm21" id="ccm21-a" value="Neon Rain"><label for="ccm21-a"><b>01</b>Neon Rain<span>3:42</span></label></div>
        <div><input type="radio" name="ccm21" id="ccm21-b" value="Slow Motion"><label for="ccm21-b"><b>02</b>Slow Motion<span>4:18</span></label></div>
        <div><input type="radio" name="ccm21" id="ccm21-c" value="Afterglow"><label for="ccm21-c"><b>03</b>Afterglow<span>3:05</span></label></div>
        <div><input type="radio" name="ccm21" id="ccm21-d" value="Daybreak"><label for="ccm21-d"><b>04</b>Daybreak<span>5:01</span></label></div>
      </fieldset>
      <p class="ccm-21__now" aria-live="polite">Select a track to drop the needle</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ccm-21,
.ccm-21 *,
.ccm-21 *::before,
.ccm-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-21 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,oklch(0.27 0.03 50),oklch(0.2 0.025 45));
  --wood: oklch(0.32 0.04 55);
  --label: oklch(0.62 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.92 0.01 55);
}

.ccm-21__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(180deg,oklch(0.27 0.03 50),oklch(0.2 0.025 45));
  overflow: hidden;
  padding: 28px;
}

.ccm-21__deck {
  position: relative;
  display: grid;
  grid-template-columns: auto 200px;
  gap: 26px;
  align-items: center;
  padding: 26px;
  border-radius: 22px;
  background: linear-gradient(160deg,var(--wood),oklch(0.26 0.035 50));
  box-shadow: 0 30px 70px -30px oklch(0 0 0 / .8),inset 0 1px 0 oklch(1 0 0 / .08);
}

@media (max-width: 560px) {
  .ccm-21__deck {
    grid-template-columns: 1fr;
  }
}

.ccm-21__platter {
  position: relative;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: oklch(0.14 0 0);
  box-shadow: 0 12px 30px -10px oklch(0 0 0 / .8),inset 0 0 0 6px oklch(0.2 0 0);
}

.ccm-21__vinyl {
  position: absolute;
  inset: 10px;
  border-radius: 50%;
  background: conic-gradient(from 40deg,transparent 0 8%,oklch(1 0 0 / .05) 10%,transparent 13% 48%,oklch(1 0 0 / .05) 51%,transparent 54%),radial-gradient(circle,var(--label) 0 24%,transparent 24.5%),repeating-radial-gradient(circle,oklch(0.23 0 0) 0 2px,oklch(0.17 0 0) 2px 4px);
  display: grid;
  place-items: center;
  animation: ccm21-spin 1.8s linear infinite;
  animation-play-state: paused;
}

.ccm-21__deck.is-playing .ccm-21__vinyl {
  animation-play-state: running;
}

.ccm-21__labelface {
  display: grid;
  place-items: center;
  gap: 1px;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  text-align: center;
}

.ccm-21__labelface b {
  font-size: 14px;
  letter-spacing: .18em;
}

.ccm-21__labelface i {
  font-style: normal;
  font-size: 9.5px;
  letter-spacing: .3em;
  opacity: .8;
}

.ccm-21__labelface::after {
  content: "";
  position: absolute;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: oklch(0.9 0.01 55);
  box-shadow: inset 0 1px 2px oklch(0 0 0 / .6);
}

.ccm-21__arm {
  position: absolute;
  left: 266px;
  top: 30px;
  width: 16px;
  height: 190px;
  rotate: -24deg;
  transform-origin: 8px 22px;
  transition: rotate .8s cubic-bezier(.4,0,.3,1);
  z-index: 2;
  filter: drop-shadow(0 8px 14px oklch(0 0 0 / .6));
}

.ccm-21__deck.is-playing .ccm-21__arm {
  rotate: 0deg;
}

.ccm-21__arm::before {
  content: "";
  position: absolute;
  left: 6px;
  top: 20px;
  width: 4px;
  height: 150px;
  border-radius: 2px;
  background: linear-gradient(90deg,oklch(0.78 0.01 80),oklch(0.6 0.01 80));
}

.ccm-21__weight {
  position: absolute;
  left: 0;
  top: 0;
  width: 16px;
  height: 26px;
  border-radius: 5px;
  background: oklch(0.5 0.02 80);
}

.ccm-21__head {
  position: absolute;
  left: 2px;
  bottom: 6px;
  width: 12px;
  height: 22px;
  border-radius: 3px;
  background: oklch(0.72 0.12 80);
}

.ccm-21__tracks {
  border: none;
  display: grid;
  gap: 9px;
}

.ccm-21__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-21__tracks input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.ccm-21__tracks label {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 11px 14px;
  border-radius: 12px;
  background: oklch(1 0 0 / .06);
  border: 1px solid oklch(1 0 0 / .12);
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  transition: background .2s,border-color .2s;
}

.ccm-21__tracks label:hover {
  background: oklch(1 0 0 / .12);
}

.ccm-21__tracks :checked + label {
  background: color-mix(in oklab,var(--label) 30%,transparent);
  border-color: var(--label);
}

.ccm-21__tracks :focus-visible + label {
  outline: 3px solid var(--label);
  outline-offset: 2px;
}

.ccm-21__tracks b {
  font-size: 11px;
  color: oklch(0.75 0.1 30);
  font-variant-numeric: tabular-nums;
}

.ccm-21__tracks span {
  margin-left: auto;
  font-size: 11.5px;
  opacity: .6;
  font-variant-numeric: tabular-nums;
}

.ccm-21__now {
  position: absolute;
  bottom: 8px;
  left: 26px;
  font-size: 11.5px;
  letter-spacing: .06em;
  color: oklch(0.7 0.04 55 / .8);
}

@keyframes ccm21-spin {
  to {
    rotate: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccm-21__vinyl {
    animation: none;
  }

  .ccm-21 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const deck = document.querySelector('.ccm-21__deck');
  const now = deck.querySelector('.ccm-21__now');
  deck.addEventListener('change', (e) => {
    if (e.target.name !== 'ccm21') return;
    deck.classList.add('is-playing');
    now.textContent = '▶ Now playing — ' + e.target.value;
  });
})();
```
