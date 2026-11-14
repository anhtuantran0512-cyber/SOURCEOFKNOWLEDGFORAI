---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/inner-text-on-off-switch/"
title: "Inner Text ON / OFF Switch"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The space-saving form control PMs ask for: a wider track carries 'ON' and 'OFF' nested inside it, and the sliding thumb covers the inactive word while the…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inner Text ON / OFF Switch
Source: https://codefronts.com/components/css-toggles-switches/inner-text-on-off-switch/

The space-saving form control PMs ask for: a wider track carries 'ON' and 'OFF' nested inside it, and the sliding thumb covers the inactive word while the active one fades in — state is spelled out, never inferred from color alone.
## HTML
```html
<section class="tgl-06" aria-label="Text labeled ON OFF switch">
  <div class="tgl-06__row">
    <span class="tgl-06__lbl" id="tgl-06-l">Maintenance mode</span>
    <input type="checkbox" id="tgl-06-sw" class="tgl-06__sw" role="switch" aria-labelledby="tgl-06-l">
    <label class="tgl-06__track" for="tgl-06-sw" aria-hidden="true">
      <span class="tgl-06__on">ON</span>
      <span class="tgl-06__off">OFF</span>
      <span class="tgl-06__thumb"></span>
    </label>
  </div>
  <p class="tgl-06__cap">State in words, not just color</p>
</section>
```
## CSS
```css
.tgl-06,
.tgl-06 *,
.tgl-06 *::before,
.tgl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-06 {
  --on: oklch(0.68 0.16 150);
  --off: #7c8494;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 60px 20px;
  background: #f4f5f8;
}

.tgl-06__row {
  display: flex;
  align-items: center;
  gap: 30px;
  background: #fff;
  border-radius: 16px;
  padding: 20px 26px;
  box-shadow: 0 8px 24px -18px rgba(30,40,70,.4);
}

.tgl-06__lbl {
  font-size: 16px;
  font-weight: 600;
  color: #2b3140;
}

.tgl-06__sw {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.tgl-06__track {
  position: relative;
  flex: none;
  width: 92px;
  height: 38px;
  border-radius: 20px;
  background: var(--off);
  cursor: pointer;
  transition: background-color .35s;
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: .08em;
  color: #fff;
}

.tgl-06__sw:checked ~ .tgl-06__track {
  background: var(--on);
}

.tgl-06__on,
.tgl-06__off {
  position: absolute;
  top: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  transition: opacity .3s,transform .3s;
}

.tgl-06__on {
  left: 14px;
  opacity: 0;
  transform: translateX(-6px);
}

.tgl-06__off {
  right: 12px;
  opacity: 1;
  transform: translateX(0);
}

.tgl-06__sw:checked ~ .tgl-06__track .tgl-06__on {
  opacity: 1;
  transform: translateX(0);
}

.tgl-06__sw:checked ~ .tgl-06__track .tgl-06__off {
  opacity: 0;
  transform: translateX(6px);
}

.tgl-06__thumb {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(20,30,60,.35);
  transition: transform .35s cubic-bezier(.25,.9,.3,1.1);
}

.tgl-06__sw:checked ~ .tgl-06__track .tgl-06__thumb {
  transform: translateX(54px);
}

.tgl-06__sw:focus-visible ~ .tgl-06__track {
  outline: 3px solid oklch(0.6 0.17 250);
  outline-offset: 3px;
}

.tgl-06__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #a3a9b7;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-06__track,
    .tgl-06__thumb,
    .tgl-06__on,
    .tgl-06__off {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an sr-only checkbox drives a labeled track; the thumb slides on transform while ON/OFF crossfade with opacity so the covered word slips out of view. */
```
