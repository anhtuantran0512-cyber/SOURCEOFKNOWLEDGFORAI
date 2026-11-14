---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/3d-neumorphic-pill-toggle/"
title: "3D Neumorphic Pill Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A tactile soft-UI switch for modern immersive dashboards: the track is carved INTO the surface with inset shadows while the knob extrudes OUT of it — and…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Neumorphic Pill Toggle
Source: https://codefronts.com/components/css-toggles-switches/3d-neumorphic-pill-toggle/

A tactile soft-UI switch for modern immersive dashboards: the track is carved INTO the surface with inset shadows while the knob extrudes OUT of it — and pressing gives a physical push-down before the knob glides across and an accent ring wakes up.
## HTML
```html
<section class="tgl-03" aria-label="Neumorphic pill toggle">
  <label class="tgl-03__row" for="tgl-03-sw">
    <span class="tgl-03__lbl">Focus mode</span>
    <input type="checkbox" id="tgl-03-sw" class="tgl-03__sw" role="switch">
  </label>
  <p class="tgl-03__cap">Press it — it pushes back</p>
</section>
```
## CSS
```css
.tgl-03,
.tgl-03 *,
.tgl-03 *::before,
.tgl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-03 {
  --surface: #e0e5ec;
  --shade: #b8bec9;
  --light: #ffffff;
  --accent: oklch(0.62 0.17 264);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 26px;
  padding: 60px 20px;
  background: var(--surface);
}

.tgl-03__row {
  display: flex;
  align-items: center;
  gap: 34px;
  cursor: pointer;
  padding: 26px 34px;
  border-radius: 24px;
  background: var(--surface);
  box-shadow: 9px 9px 20px var(--shade),-9px -9px 20px var(--light);
}

.tgl-03__lbl {
  font-size: 16px;
  font-weight: 600;
  color: #5b6472;
  letter-spacing: .01em;
}

.tgl-03__sw {
  appearance: none;
  -webkit-appearance: none;
  flex: none;
  width: 78px;
  height: 42px;
  border-radius: 24px;
  background: var(--surface);
  position: relative;
  cursor: pointer;
  box-shadow: inset 5px 5px 10px var(--shade),inset -5px -5px 10px var(--light);
  transition: box-shadow .35s;
}

.tgl-03__sw:checked {
  box-shadow: inset 5px 5px 10px var(--shade),inset -5px -5px 10px var(--light),inset 0 0 14px 2px color-mix(in oklab,var(--accent) 45%,transparent);
}

.tgl-03__sw::before {
  content: "";
  position: absolute;
  top: 5px;
  left: 5px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(145deg,#f0f3f8,#d3d9e3);
  box-shadow: 4px 4px 9px var(--shade),-4px -4px 9px var(--light);
  transition: transform .35s cubic-bezier(.3,1.1,.4,1),box-shadow .2s;
}

.tgl-03__sw:checked::before {
  transform: translateX(36px);
  background: linear-gradient(145deg,color-mix(in oklab,var(--accent) 85%,#fff),var(--accent));
}

.tgl-03__sw:active::before {
  transform: scale(.9);
  box-shadow: 2px 2px 4px var(--shade),-2px -2px 4px var(--light);
}

.tgl-03__sw:checked:active::before {
  transform: translateX(36px) scale(.9);
}

.tgl-03__sw:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

.tgl-03__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #9aa3b2;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-03__sw,
    .tgl-03__sw::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — dual-source inset shadows deboss the track, outset shadows emboss the knob, and :active collapses them for a physical push-down. */
```
