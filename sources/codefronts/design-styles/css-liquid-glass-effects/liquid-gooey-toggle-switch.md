---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-gooey-toggle-switch/"
title: "Liquid (Gooey) Toggle Switch"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A toggle where the handle behaves like liquid metal: as it slides from off to on it stretches and the drop 'merges' with the track before snapping into place…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid (Gooey) Toggle Switch
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-gooey-toggle-switch/

A toggle where the handle behaves like liquid metal: as it slides from off to on it stretches and the drop 'merges' with the track before snapping into place — the classic gooey-filter trick applied to a glass switch. Driven entirely by a native checkbox, so it's fully accessible.
## HTML
```html
<section class="lg-04" aria-label="Liquid gooey toggle switch">
  <svg width="0" height="0" aria-hidden="true" focusable="false" style="position:absolute">
    <filter id="lg-04-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9" result="goo"/><feBlend in="SourceGraphic" in2="goo"/></filter>
  </svg>
  <label class="lg-04__switch">
    <input class="lg-04__input" type="checkbox" checked>
    <span class="lg-04__track" aria-hidden="true"><span class="lg-04__goo"><span class="lg-04__blob lg-04__blob--fixed"></span><span class="lg-04__blob lg-04__blob--handle"></span></span></span>
    <span class="lg-04__label">Liquid mode</span>
  </label>
</section>
```
## CSS
```css
.lg-04,
.lg-04 *,
.lg-04 *::before,
.lg-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-04 {
  --on: oklch(0.7 0.17 165);
  --off: oklch(0.55 0.03 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(circle at 30% 20%,#2a2740,#12101d);
}

.lg-04__switch {
  font-size: 22px;
  display: inline-flex;
  align-items: center;
  gap: .9em;
  cursor: pointer;
  color: #eceaf5;
}

.lg-04__input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.lg-04__track {
  position: relative;
  width: 3.4em;
  height: 1.7em;
  border-radius: 999px;
  background: var(--off);
  border: 1px solid rgba(255,255,255,.25);
  box-shadow: inset 0 2px 8px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.25);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  transition: background .35s;
}

.lg-04__goo {
  position: absolute;
  inset: 0;
  filter: url(#lg-04-goo);
}

.lg-04__blob {
  position: absolute;
  top: 50%;
  border-radius: 50%;
  background: #fff;
  transform: translateY(-50%);
}

.lg-04__blob--fixed {
  left: .28em;
  width: 1.14em;
  height: 1.14em;
  opacity: .9;
  transition: opacity .3s ease .18s;
}

.lg-04__input:checked+.lg-04__track .lg-04__blob--fixed {
  opacity: 0;
}

.lg-04__blob--handle {
  left: .28em;
  width: 1.14em;
  height: 1.14em;
  box-shadow: 0 2px 6px rgba(0,0,0,.35);
  transition: left .4s cubic-bezier(.6,-.4,.4,1.4),transform .4s;
}

.lg-04__input:checked+.lg-04__track {
  background: var(--on);
}

.lg-04__input:checked+.lg-04__track .lg-04__blob--handle {
  left: 2.0em;
  animation: lg-04-stretch .4s ease;
}

.lg-04__input:not(:checked)+.lg-04__track .lg-04__blob--handle {
  animation: lg-04-stretch .4s ease;
}

.lg-04__input:focus-visible+.lg-04__track {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-04__label {
  font-size: .85em;
  font-weight: 600;
}

@keyframes lg-04-stretch {
  0% {
    transform: translateY(-50%) scaleX(1);
  }

  45% {
    transform: translateY(-50%) scaleX(1.55);
  }

  100% {
    transform: translateY(-50%) scaleX(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-04__blob--handle {
    transition: left .2s;
  }

  .lg-04__input:checked+.lg-04__track .lg-04__blob--handle,
    .lg-04__input:not(:checked)+.lg-04__track .lg-04__blob--handle {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a native checkbox drives :checked, the handle slides via CSS transition, and an SVG feGaussianBlur+feColorMatrix goo filter fuses the blobs so the handle reads as liquid. */
```
