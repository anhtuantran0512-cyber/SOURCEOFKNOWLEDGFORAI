---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/chronometer/"
title: "Clockface Chronometer Circular Selector"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A chronometer-styled hour picker, the Material-timepicker pattern rebuilt in plain HTML/CSS/JS: twelve hour stops on a steel bezel, a hand that sweeps to…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clockface Chronometer Circular Selector
Source: https://codefronts.com/navigation/css-circular-menus/chronometer/

A chronometer-styled hour picker, the Material-timepicker pattern rebuilt in plain HTML/CSS/JS: twelve hour stops on a steel bezel, a hand that sweeps to your choice (shortest way around), and a digital complication that confirms it. The 12-stop clock dial doubles as a general 12-item selector — months, zodiac, table seats.
## HTML
```html
<section class="ccm-25" aria-label="Clockface hour selector demo">
  <div class="ccm-25__stage">
    <fieldset class="ccm-25__watch"><legend class="ccm-25__sr">Pick a delivery hour</legend>
      <div class="ccm-25__dial">
        <span class="ccm-25__ticks" aria-hidden="true"></span>
        <div class="ccm-25__stops"></div>
        <span class="ccm-25__hand" aria-hidden="true"></span>
        <span class="ccm-25__pin" aria-hidden="true"></span>
        <p class="ccm-25__window"><output class="ccm-25__digital">12:00</output><em>delivery</em></p>
      </div>
    </fieldset>
    <p class="ccm-25__hint">Twelve stops · the hand takes the short way round</p>
  </div>
</section>
```
## CSS
```css
.ccm-25,
.ccm-25 *,
.ccm-25 *::before,
.ccm-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-25 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(175deg,oklch(0.96 0.005 250),oklch(0.9 0.01 250));
  --brand: oklch(0.6 0.19 25);
  --steel: oklch(0.85 0.005 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.25 0.01 250);
}

.ccm-25__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  border-radius: 20px;
  background: linear-gradient(175deg,oklch(0.96 0.005 250),oklch(0.9 0.01 250));
  border: 1px solid oklch(0.88 0.008 250);
}

.ccm-25__watch {
  border: none;
}

.ccm-25__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-25__dial {
  position: relative;
  width: 330px;
  height: 330px;
  border-radius: 50%;
  background: radial-gradient(circle at 40% 30%,#fff,var(--steel));
  box-shadow: 0 0 0 10px oklch(0.75 0.008 250),0 0 0 12px oklch(0.55 0.01 250),0 30px 60px -25px oklch(0.4 0.02 250 / .6),inset 0 2px 8px oklch(1 0 0 / .9),inset 0 -10px 24px oklch(0.6 0.01 250 / .3);
  display: grid;
  place-items: center;
}

.ccm-25__ticks {
  position: absolute;
  inset: 12px;
  border-radius: 50%;
  background: repeating-conic-gradient(oklch(0.45 0.01 250) 0 .5deg,transparent .5deg 6deg);
  mask: radial-gradient(circle,transparent 82%,black 83%);
}

.ccm-25__stops {
  position: absolute;
  inset: 0;
}

.ccm-25__stop {
  position: absolute;
  left: 50%;
  top: 50%;
  --a: calc(var(--h) * 30deg - 90deg);
  translate: calc(cos(var(--a)) * 118px - 50%) calc(sin(var(--a)) * 118px - 50%);
}

.ccm-25__stop input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.ccm-25__stop label {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  font-size: 15px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .2s,color .2s,scale .2s;
}

.ccm-25__stop label:hover {
  background: oklch(0.6 0.19 25 / .12);
}

.ccm-25__stop :checked + label {
  background: var(--brand);
  color: #fff;
  scale: 1.12;
  box-shadow: 0 6px 16px -6px oklch(0.5 0.18 25 / .7);
}

.ccm-25__stop:has(:focus-visible) label {
  outline: 3px solid var(--brand);
  outline-offset: 2px;
}

.ccm-25__hand {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 6px;
  height: 96px;
  margin-left: -3px;
  border-radius: 3px 3px 0 0;
  background: linear-gradient(180deg,var(--brand),oklch(0.45 0.16 25));
  transform-origin: 50% 100%;
  translate: 0 -100%;
  rotate: var(--rot,0deg);
  transition: rotate .7s cubic-bezier(.3,1.35,.4,1);
  pointer-events: none;
}

.ccm-25__hand::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -26px;
  translate: -50% 0;
  width: 6px;
  height: 26px;
  border-radius: 0 0 3px 3px;
  background: oklch(0.45 0.02 250);
}

.ccm-25__pin {
  position: absolute;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,#fff,oklch(0.6 0.01 250));
  box-shadow: 0 1px 3px oklch(0 0 0 / .35);
  pointer-events: none;
}

.ccm-25__window {
  position: absolute;
  left: 50%;
  top: 64%;
  translate: -50% 0;
  display: grid;
  justify-items: center;
  gap: 1px;
  padding: 7px 14px;
  border-radius: 9px;
  background: oklch(0.22 0.01 250);
  color: #fff;
  pointer-events: none;
}

.ccm-25__digital {
  font: 700 17px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .06em;
}

.ccm-25__window em {
  font-style: normal;
  font-size: 8.5px;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: oklch(0.7 0.03 250);
}

.ccm-25__hint {
  font-size: 13px;
  color: oklch(0.5 0.015 250);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-25 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const watch = document.querySelector('.ccm-25__watch');
  const stops = watch.querySelector('.ccm-25__stops');
  const hand = watch.querySelector('.ccm-25__hand');
  const digital = watch.querySelector('.ccm-25__digital');
  for (let h = 1; h <= 12; h++) {
    const d = document.createElement('div');
    d.className = 'ccm-25__stop';
    d.style.setProperty('--h', h);
    d.innerHTML = '<input type="radio" name="ccm25" id="ccm25-' + h + '" value="' + h + '"' + (h === 12 ? ' checked' : '') + '>' +
      '<label for="ccm25-' + h + '">' + h + '</label>';
    stops.append(d);
  }
  let rot = 0;
  watch.addEventListener('change', (e) => {
    if (e.target.name !== 'ccm25') return;
    const target = (Number(e.target.value) % 12) * 30; // 12 → 0° (top)
    let delta = ((target - ((rot % 360) + 360) % 360) % 360 + 540) % 360 - 180;
    rot += delta;
    hand.style.setProperty('--rot', rot + 'deg');
    digital.textContent = e.target.value + ':00';
  });
})();
```
