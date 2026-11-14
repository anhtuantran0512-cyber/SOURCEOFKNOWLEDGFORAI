---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/gooey-liquid-morphing-switch/"
title: "Gooey Liquid Morphing Switch"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A high-impact micro-interaction: the thumb is a blob of liquid that stretches, necks and snaps to the far side of the track like plasma — built with an…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gooey Liquid Morphing Switch
Source: https://codefronts.com/components/css-toggles-switches/gooey-liquid-morphing-switch/

A high-impact micro-interaction: the thumb is a blob of liquid that stretches, necks and snaps to the far side of the track like plasma — built with an inline SVG filter (feGaussianBlur + feColorMatrix) and two staggered CSS transitions. No JavaScript, no canvas.
## HTML
```html
<section class="tgl-04" aria-label="Gooey liquid morphing switch">
  <svg width="0" height="0" aria-hidden="true" style="position:absolute">
    <defs><filter id="tgl-04-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="g"/><feComposite in="SourceGraphic" in2="g" operator="atop"/></filter></defs>
  </svg>
  <label class="tgl-04__row" for="tgl-04-sw">
    <span class="tgl-04__lbl">Liquid mode</span>
    <span class="tgl-04__track">
      <span class="tgl-04__goo" aria-hidden="true"><i class="tgl-04__blob"></i><i class="tgl-04__echo"></i></span>
      <input type="checkbox" id="tgl-04-sw" class="tgl-04__sw" role="switch">
    </span>
  </label>
  <p class="tgl-04__cap">Watch the drop neck &amp; snap</p>
</section>
```
## CSS
```css
.tgl-04,
.tgl-04 *,
.tgl-04 *::before,
.tgl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-04 {
  --goo: oklch(0.72 0.19 340);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 60px 20px;
  background: #171222;
}

.tgl-04__row {
  display: flex;
  align-items: center;
  gap: 30px;
  cursor: pointer;
}

.tgl-04__lbl {
  font-size: 16px;
  font-weight: 600;
  color: #cfc6e4;
}

.tgl-04__track {
  position: relative;
  width: 96px;
  height: 48px;
  border-radius: 26px;
  background: #241b38;
  box-shadow: inset 0 3px 8px rgba(0,0,0,.55);
}

.tgl-04__goo {
  position: absolute;
  inset: 0;
  filter: url(#tgl-04-goo);
  pointer-events: none;
}

.tgl-04__blob,
.tgl-04__echo {
  position: absolute;
  top: 8px;
  left: 8px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--goo);
}

.tgl-04__blob {
  transition: transform .5s cubic-bezier(.65,0,.35,1);
}

.tgl-04__echo {
  transition: transform .5s cubic-bezier(.65,0,.35,1) .09s;
  transform: scale(.86);
}

.tgl-04__sw {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border-radius: 26px;
  cursor: pointer;
  background: transparent;
}

.tgl-04__sw:checked ~ * .tgl-04__blob {
}

.tgl-04__track:has(.tgl-04__sw:checked) .tgl-04__blob {
  transform: translateX(48px);
}

.tgl-04__track:has(.tgl-04__sw:checked) .tgl-04__echo {
  transform: translateX(48px) scale(.86);
}

.tgl-04__sw:focus-visible {
  outline: 3px solid var(--goo);
  outline-offset: 4px;
}

.tgl-04__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #6f6588;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-04__blob,
    .tgl-04__echo {
    transition: transform .2s;
  }

  .tgl-04__echo {
    transition-delay: 0s;
  }
}
```

## JavaScript
```js
/* No JavaScript — an SVG feGaussianBlur + feColorMatrix filter fuses a thumb blob with a delayed echo blob, drawing a liquid neck as they separate mid-slide. */
```
