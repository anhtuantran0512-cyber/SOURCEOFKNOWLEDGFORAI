---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-bakelite-radio-dial-toggle-button/"
title: "CSS Bakelite Radio Dial Toggle Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A bakelite rotary switch that turns 132° from OFF to ON, with a knurled grip, a chamfered pointer, engraved tick marks around the bezel, and a warm indicator…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Bakelite Radio Dial Toggle Button
Source: https://codefronts.com/components/css-buttons/css-bakelite-radio-dial-toggle-button/

A bakelite rotary switch that turns 132° from OFF to ON, with a knurled grip, a chamfered pointer, engraved tick marks around the bezel, and a warm indicator lamp that fades up as the contact closes. Pure CSS: a checkbox holds the state and :has() drives the rotation.
## HTML
```html
<div class="cb-44">
  <div class="cb-44__stage">
    <label class="cb-44__switch">
      <input type="checkbox" role="switch" aria-label="Power">
      <span class="cb-44__plate" aria-hidden="true">
        <span class="cb-44__ticks"></span>
        <span class="cb-44__legend cb-44__legend--off">Off</span>
        <span class="cb-44__legend cb-44__legend--on">On</span>
        <span class="cb-44__lamp"></span>
        <span class="cb-44__knob">
          <span class="cb-44__knurl"></span>
          <span class="cb-44__pointer"></span>
        </span>
      </span>
    </label>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&display=swap');

.cb-44 {
  --bg: #1b1512;
  --plate: #241c17;
  --bake: #3a2418;
  --bake-hi: #5a3a26;
  --bake-lo: #1d120b;
  --tick: #c9b48d;
  --ink: #e6d7b8;
  --lamp: #ff9f43;
  --size: 9.5rem;
  --spring: linear(0,.36 7%,.8 15%,1.05 23%,1.09 29%,1.02 39%,1 54%,1);
  --sans: "Oswald",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(30rem 20rem at 50% 44%, #2b211a, transparent 74%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-44 {
    --bake: oklch(30% .05 50);
    --bake-hi: oklch(40% .06 52);
    --bake-lo: oklch(18% .03 48);
    --lamp: oklch(78% .16 62);
  }
}

@media (prefers-color-scheme: light) {
  .cb-44:not([data-theme="dark"]) {
    --bg: #26201b;
  }
}

.cb-44[data-theme="light"] {
  --bg: #26201b;
}

.cb-44,
.cb-44 *,
.cb-44 *::before,
.cb-44 *::after {
  box-sizing: border-box;
}

.cb-44__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-44__switch {
  position: relative;
  display: block;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.cb-44__switch input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-44__plate {
  position: relative;
  display: grid;
  place-items: center;
  width: var(--size);
  height: var(--size);
  border-radius: 50%;
  background: radial-gradient(circle at 40% 30%, rgba(255,255,255,.08), transparent 60%), linear-gradient(160deg, #2e241d, var(--plate));
  box-shadow: inset 0 2px 4px rgba(255,255,255,.1), inset 0 -3px 8px rgba(0,0,0,.7), 0 16px 26px -12px rgba(0,0,0,.85);
}

.cb-44__ticks {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: repeating-conic-gradient(from -66deg, var(--tick) 0 .9deg, transparent .9deg 11deg);
  -webkit-mask: radial-gradient(farthest-side, transparent 76%, #000 78%);
  mask: radial-gradient(farthest-side, transparent 76%, #000 78%);
  opacity: .65;
}

.cb-44__legend {
  position: absolute;
  font-size: .6875rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--ink);
  opacity: .6;
  transition: opacity .3s ease, color .3s ease;
}

.cb-44__legend--off {
  left: .35rem;
  bottom: 1.5rem;
  rotate: -24deg;
}

.cb-44__legend--on {
  right: .35rem;
  bottom: 1.5rem;
  rotate: 24deg;
}

.cb-44__lamp {
  position: absolute;
  top: .85rem;
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--lamp);
  opacity: .18;
  box-shadow: 0 0 6px var(--lamp), 0 0 14px color-mix(in oklab,var(--lamp) 55%,transparent);
  transition: opacity .35s ease;
}

.cb-44__knob {
  position: relative;
  width: 62%;
  height: 62%;
  border-radius: 50%;
  background: radial-gradient(circle at 36% 28%, var(--bake-hi), transparent 58%), radial-gradient(1.4rem 1rem at 70% 74%, rgba(0,0,0,.4), transparent 70%), linear-gradient(155deg, var(--bake), var(--bake-lo));
  box-shadow: inset 0 2px 3px rgba(255,255,255,.22), inset 0 -3px 6px rgba(0,0,0,.6), 0 6px 12px -4px rgba(0,0,0,.8);
  rotate: -66deg;
  transition: rotate .55s cubic-bezier(.16,1,.3,1);
}

@supports (transition-timing-function: linear(0,1)) {
  .cb-44__knob {
    transition: rotate .7s var(--spring);
  }
}

.cb-44__knurl {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: repeating-conic-gradient(from 0deg, rgba(255,255,255,.14) 0 1.6deg, rgba(0,0,0,.22) 1.6deg 3.4deg);
  -webkit-mask: radial-gradient(farthest-side, transparent 78%, #000 80%);
  mask: radial-gradient(farthest-side, transparent 78%, #000 80%);
}

.cb-44__pointer {
  position: absolute;
  top: 9%;
  left: 50%;
  width: .28rem;
  height: 34%;
  margin-left: -.14rem;
  border-radius: 999px;
  background: linear-gradient(180deg, var(--tick), color-mix(in oklab,var(--tick) 60%,black));
  box-shadow: 0 0 4px rgba(0,0,0,.6);
}

.cb-44__switch:hover .cb-44__knob {
  filter: brightness(1.08);
}

.cb-44__switch:has(input:focus-visible) .cb-44__plate {
  outline: 2px solid var(--lamp);
  outline-offset: 5px;
}

.cb-44__switch:has(input:checked) .cb-44__knob {
  rotate: 66deg;
}

.cb-44__switch:has(input:checked) .cb-44__lamp {
  opacity: 1;
}

.cb-44__switch:has(input:checked) .cb-44__legend--on {
  opacity: 1;
  color: var(--lamp);
}

.cb-44__switch:not(:has(input:checked)) .cb-44__legend--off {
  opacity: 1;
}

.cb-44__switch:active .cb-44__knob {
  scale: .97;
}

@media (prefers-reduced-motion: reduce) {
  .cb-44__knob,
    .cb-44__lamp,
    .cb-44__legend {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-44__plate,
    .cb-44__knob {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-44__ticks,
    .cb-44__knurl {
    display: none;
  }

  .cb-44__pointer {
    background: ButtonText;
  }

  .cb-44__lamp {
    background: GrayText;
    box-shadow: none;
  }

  .cb-44__switch:has(input:checked) .cb-44__lamp {
    background: Highlight;
  }
}
```
