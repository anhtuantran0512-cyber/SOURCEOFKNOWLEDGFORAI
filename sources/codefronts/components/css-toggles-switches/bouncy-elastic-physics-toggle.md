---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/bouncy-elastic-physics-toggle/"
title: "Bouncy Elastic Physics Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "Premium landing-page motion in one line of CSS: an overshooting cubic-bezier makes the thumb wind up backwards, shoot across the track, and bounce gently off…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncy Elastic Physics Toggle
Source: https://codefronts.com/components/css-toggles-switches/bouncy-elastic-physics-toggle/

Premium landing-page motion in one line of CSS: an overshooting cubic-bezier makes the thumb wind up backwards, shoot across the track, and bounce gently off the far wall — playful, physics-driven, and still just a checkbox with a transition.
## HTML
```html
<section class="tgl-05" aria-label="Bouncy elastic physics toggle">
  <label class="tgl-05__row" for="tgl-05-sw">
    <span class="tgl-05__lbl">Confetti on publish</span>
    <input type="checkbox" id="tgl-05-sw" class="tgl-05__sw" role="switch">
  </label>
  <p class="tgl-05__cap">cubic-bezier(0.4, −0.3, 0.6, 1.3)</p>
</section>
```
## CSS
```css
.tgl-05,
.tgl-05 *,
.tgl-05 *::before,
.tgl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-05 {
  --on: oklch(0.7 0.17 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 60px 20px;
  background: #fdf8ef;
}

.tgl-05__row {
  display: flex;
  align-items: center;
  gap: 34px;
  cursor: pointer;
  background: #fff;
  border: 1px solid #eee3cf;
  border-radius: 18px;
  padding: 20px 26px;
  box-shadow: 0 10px 26px -18px rgba(120,90,20,.35);
}

.tgl-05__lbl {
  font-size: 16px;
  font-weight: 600;
  color: #4a4132;
}

.tgl-05__sw {
  appearance: none;
  -webkit-appearance: none;
  flex: none;
  width: 76px;
  height: 40px;
  border-radius: 22px;
  background: #e8e0d0;
  position: relative;
  cursor: pointer;
  transition: background-color .45s ease;
}

.tgl-05__sw:checked {
  background: var(--on);
}

.tgl-05__sw::before {
  content: "";
  position: absolute;
  top: 4px;
  left: 4px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 3px 7px rgba(80,60,20,.3);
  transition: transform .55s cubic-bezier(0.4,-0.3,0.6,1.3);
}

.tgl-05__sw:checked::before {
  transform: translateX(36px);
}

.tgl-05__sw:active::before {
  transform: scale(.92);
}

.tgl-05__sw:checked:active::before {
  transform: translateX(36px) scale(.92);
}

.tgl-05__sw:focus-visible {
  outline: 3px solid var(--on);
  outline-offset: 4px;
}

.tgl-05__cap {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: #b0a58d;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-05__sw::before {
    transition: transform .2s ease;
  }
}
```

## JavaScript
```js
/* No JavaScript — a single overshooting cubic-bezier on the thumb's transform creates the wind-up, launch and wall-bounce. */
```
