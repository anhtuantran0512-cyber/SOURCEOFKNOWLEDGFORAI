---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/material-design-3-switch/"
title: "Material Design 3 Switch"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A faithful Material 3 switch, CSS-only: the small outlined thumb grows as it slides, a checkmark fades in on the handle, a state-layer halo blooms on hover…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design 3 Switch
Source: https://codefronts.com/components/css-toggles-switches/material-design-3-switch/

A faithful Material 3 switch, CSS-only: the small outlined thumb grows as it slides, a checkmark fades in on the handle, a state-layer halo blooms on hover and press — every spec detail (52×32 track, 2px outline, 16→24→28dp thumb) without the Material library.
## HTML
```html
<section class="tgl-14" aria-label="Material Design 3 switch">
  <label class="tgl-14__row" for="tgl-14-sw">
    <span class="tgl-14__txt"><b>Sync over Wi-Fi only</b><small>Pause large uploads on mobile data</small></span>
    <input type="checkbox" id="tgl-14-sw" class="tgl-14__sw" role="switch" checked>
  </label>
  <p class="tgl-14__cap">M3 spec: growing thumb + state layer</p>
</section>
```
## CSS
```css
.tgl-14,
.tgl-14 *,
.tgl-14 *::before,
.tgl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-14 {
  --m3-primary: #6750a4;
  --m3-on-primary: #ffffff;
  --m3-outline: #79747e;
  --m3-track-off: #e6e0e9;
  font-family: Roboto,'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 60px 20px;
  background: #fef7ff;
}

.tgl-14__row {
  display: flex;
  align-items: center;
  gap: 34px;
  cursor: pointer;
  background: #fff;
  border: 1px solid #e7e0ec;
  border-radius: 16px;
  padding: 18px 22px;
  width: min(360px,100%);
}

.tgl-14__txt {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.tgl-14__txt b {
  font-size: 15px;
  font-weight: 500;
  color: #1d1b20;
}

.tgl-14__txt small {
  font-size: 12.5px;
  color: #79747e;
}

.tgl-14__sw {
  appearance: none;
  -webkit-appearance: none;
  flex: none;
  width: 52px;
  height: 32px;
  border-radius: 16px;
  background: var(--m3-track-off);
  border: 2px solid var(--m3-outline);
  position: relative;
  cursor: pointer;
  transition: background-color .25s,border-color .25s;
}

.tgl-14__sw:checked {
  background: var(--m3-primary);
  border-color: var(--m3-primary);
}

.tgl-14__sw::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--m3-outline);
  transform: scale(.5715);
  transition: transform .25s cubic-bezier(.2,0,0,1),background-color .25s,box-shadow .2s;
}

.tgl-14__sw:checked::before {
  background: var(--m3-on-primary);
  transform: translateX(20px) scale(.857);
}

.tgl-14__sw:hover::before {
  box-shadow: 0 0 0 10px rgba(103,80,164,.08);
}

.tgl-14__sw:active::before {
  transform: scale(1);
}

.tgl-14__sw:checked:active::before {
  transform: translateX(20px) scale(1);
}

.tgl-14__sw::after {
  content: "";
  position: absolute;
  top: 6px;
  left: 6px;
  width: 16px;
  height: 16px;
  background: var(--m3-primary);
  -webkit-mask: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill="none" stroke="black" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" d="M3 8.5l3.2 3.2L13 5"/></svg>') center/contain no-repeat;
  mask: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill="none" stroke="black" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" d="M3 8.5l3.2 3.2L13 5"/></svg>') center/contain no-repeat;
  opacity: 0;
  transform: translateX(20px) scale(.5);
  transition: opacity .2s .05s,transform .25s cubic-bezier(.2,0,0,1);
}

.tgl-14__sw:checked::after {
  opacity: 1;
  transform: translateX(20px) scale(1);
}

.tgl-14__sw:focus-visible {
  outline: 3px solid var(--m3-primary);
  outline-offset: 3px;
}

.tgl-14__cap {
  font-size: 12px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: #a49daf;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-14__sw,
    .tgl-14__sw::before,
    .tgl-14__sw::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the M3 thumb grows/slides via transform:scale()+translateX(), the checkmark is a masked data-URI SVG, and the state layer is a translucent box-shadow halo. */
```
