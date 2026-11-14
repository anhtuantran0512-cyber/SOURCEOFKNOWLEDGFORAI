---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/outline-minimal-currentcolor-toggle/"
title: "Outline Minimal currentColor Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A stroke-only switch drawn entirely in currentColor: hollow track, hollow thumb that fills solid when on."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Outline Minimal currentColor Toggle
Source: https://codefronts.com/components/css-toggles-switches/outline-minimal-currentcolor-toggle/

A stroke-only switch drawn entirely in currentColor: hollow track, hollow thumb that fills solid when on. Because it inherits its color from surrounding text, the SAME markup works on light cards, dark cards and brand-colored banners with zero per-theme CSS.
## HTML
```html
<section class="tgl-24" aria-label="Outline currentColor toggles">
  <div class="tgl-24__chips">
    <label class="tgl-24__chip tgl-24__chip--light"><span>Autosave</span><input type="checkbox" class="tgl-24__sw" role="switch" checked></label>
    <label class="tgl-24__chip tgl-24__chip--dark"><span>Autosave</span><input type="checkbox" class="tgl-24__sw" role="switch" checked></label>
    <label class="tgl-24__chip tgl-24__chip--brand"><span>Autosave</span><input type="checkbox" class="tgl-24__sw" role="switch"></label>
  </div>
  <p class="tgl-24__cap">One switch · three themes · zero theme CSS</p>
</section>
```
## CSS
```css
.tgl-24,
.tgl-24 *,
.tgl-24 *::before,
.tgl-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-24 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 26px;
  padding: 60px 20px;
  background: #f4f4f2;
}

.tgl-24__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}

.tgl-24__chip {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 16px 22px;
  border-radius: 14px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
}

.tgl-24__chip--light {
  background: #fff;
  color: #26292f;
  border: 1px solid #e3e3df;
}

.tgl-24__chip--dark {
  background: #1d1f24;
  color: #e8e9ec;
}

.tgl-24__chip--brand {
  background: oklch(0.55 0.15 265);
  color: #fff;
}

.tgl-24__sw {
  appearance: none;
  -webkit-appearance: none;
  flex: none;
  width: 56px;
  height: 32px;
  border-radius: 17px;
  border: 2px solid currentColor;
  background: transparent;
  color: inherit;
  position: relative;
  cursor: pointer;
}

.tgl-24__sw::before {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid currentColor;
  background: transparent;
  transition: transform .3s cubic-bezier(.3,1,.35,1.05),background-color .3s;
}

.tgl-24__sw:checked::before {
  transform: translateX(24px);
  background: currentColor;
}

.tgl-24__sw:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}

.tgl-24__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #a2a29a;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-24__sw::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — every stroke and fill is currentColor, so the identical switch inherits each container's text color; checked fills the hollow thumb solid. */
```
