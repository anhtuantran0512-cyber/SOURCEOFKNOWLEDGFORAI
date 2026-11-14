---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/neon-etch/"
title: "Neon Etch Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A gas-tube × on midnight glass: layered drop-shadow() filters build the inner-glow-plus-halo of real neon, and hovering powers the tube on with a flickering…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Etch Close Button
Source: https://codefronts.com/components/css-close-buttons/neon-etch/

A gas-tube × on midnight glass: layered drop-shadow() filters build the inner-glow-plus-halo of real neon, and hovering powers the tube on with a flickering strike sequence — two dim pre-flashes, then full brightness — exactly like fluorescent tubes igniting. One custom property carries the entire glow color.
## HTML
```html
<section class="ccb-21" aria-label="Neon close button demo">
  <button class="ccb-21__close" type="button" aria-label="Close">
    <span class="ccb-21__x" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
.ccb-21,
.ccb-21 *,
.ccb-21 *::before,
.ccb-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-21 {
  --neon: oklch(0.78 0.2 330);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 120% at 50% 10%,oklch(0.2 0.03 300),oklch(0.12 0.015 290));
}

.ccb-21 .ccb-21__close {
  position: relative;
  display: grid;
  place-items: center;
  width: 84px;
  height: 84px;
  border: 1px solid oklch(0.78 0.2 330 / .22);
  border-radius: 18px;
  background: linear-gradient(160deg,rgba(255,255,255,.05),rgba(255,255,255,.01));
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  cursor: pointer;
  transition: border-color .25s ease;
  box-shadow: 0 20px 44px -22px rgba(0,0,0,.9),inset 0 1px 0 rgba(255,255,255,.07);
}

.ccb-21 .ccb-21__close::after {
  content: "";
  position: absolute;
  inset: auto 14px 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--neon);
  filter: blur(14px);
  opacity: .12;
  transition: opacity .3s ease;
}

.ccb-21 .ccb-21__x {
  position: relative;
  width: 28px;
  height: 28px;
  opacity: .35;
  filter: drop-shadow(0 0 2px var(--neon));
  transition: opacity .2s ease;
}

.ccb-21 .ccb-21__x::before,
.ccb-21 .ccb-21__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 28px;
  height: 3px;
  border-radius: 3px;
  background: color-mix(in oklab,var(--neon) 60%,white);
}

.ccb-21 .ccb-21__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-21 .ccb-21__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-21 .ccb-21__close:hover .ccb-21__x {
  animation: ccb-21-strike .9s ease-out forwards;
}

.ccb-21 .ccb-21__close:hover::after {
  opacity: .4;
}

.ccb-21 .ccb-21__close:hover {
  border-color: oklch(0.78 0.2 330 / .5);
}

@keyframes ccb-21-strike {
  0% {
    opacity: .35;
    filter: drop-shadow(0 0 2px var(--neon));
  }

  8% {
    opacity: .7;
  }

  11%,
    18% {
    opacity: .35;
  }

  21% {
    opacity: .8;
  }

  24%,
    30% {
    opacity: .4;
  }

  55%,
    100% {
    opacity: 1;
    filter: drop-shadow(0 0 2px var(--neon)) drop-shadow(0 0 6px var(--neon)) drop-shadow(0 0 14px var(--neon));
  }
}

.ccb-21 .ccb-21__close:active {
  transform: scale(.95);
}

.ccb-21 .ccb-21__close:focus-visible {
  outline: 2.5px solid var(--neon);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-21 .ccb-21__close:hover .ccb-21__x {
    animation: none;
    opacity: 1;
    filter: drop-shadow(0 0 2px var(--neon)) drop-shadow(0 0 6px var(--neon)) drop-shadow(0 0 14px var(--neon));
  }
}
```

## JavaScript
```js
/* No JavaScript — three stacked drop-shadow shells build the tube glow; a ballast-misfire keyframe strikes the light on hover. */
```
