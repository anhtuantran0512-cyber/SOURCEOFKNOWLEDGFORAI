---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/particle-burst/"
title: "Particle Burst Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A confetti-cannon dismiss: pressing the button detonates eight particles that fly outward on individual vectors, shrink, and fade — every particle is a…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Particle Burst Close Button
Source: https://codefronts.com/components/css-close-buttons/particle-burst/

A confetti-cannon dismiss: pressing the button detonates eight particles that fly outward on individual vectors, shrink, and fade — every particle is a box-shadow point on ONE pseudo-element, so the whole explosion costs a single node and a single keyframe. The classic checkbox-burst trick, weaponised for close buttons.
## HTML
```html
<section class="ccb-19" aria-label="Particle burst close button demo">
  <button class="ccb-19__close" type="button" aria-label="Close">
    <span class="ccb-19__x" aria-hidden="true"></span>
    <span class="ccb-19__burst" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
.ccb-19,
.ccb-19 *,
.ccb-19 *::before,
.ccb-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-19 {
  --p1: oklch(0.75 0.18 60);
  --p2: oklch(0.65 0.22 330);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.2 0.03 300),oklch(0.15 0.02 290));
}

.ccb-19 .ccb-19__close {
  position: relative;
  display: grid;
  place-items: center;
  width: 64px;
  height: 64px;
  border: 1.5px solid oklch(0.75 0.18 60 / .4);
  border-radius: 50%;
  background: oklch(0.24 0.035 300);
  cursor: pointer;
  transition: border-color .2s ease;
  box-shadow: 0 16px 36px -18px rgba(0,0,0,.8);
}

.ccb-19 .ccb-19__close:hover {
  border-color: var(--p1);
}

.ccb-19 .ccb-19__x {
  position: relative;
  width: 20px;
  height: 20px;
  transition: transform .2s ease;
}

.ccb-19 .ccb-19__x::before,
.ccb-19 .ccb-19__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 2.5px;
  border-radius: 2px;
  background: oklch(0.95 0.02 60);
}

.ccb-19 .ccb-19__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-19 .ccb-19__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-19 .ccb-19__burst {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 6px;
  height: 6px;
  margin: -3px;
  border-radius: 50%;
  background: transparent;
  pointer-events: none;
}

.ccb-19 .ccb-19__close:active .ccb-19__burst {
  animation: ccb-19-boom .55s cubic-bezier(.2,.7,.3,1) forwards;
}

.ccb-19 .ccb-19__close:active .ccb-19__x {
  animation: ccb-19-pop .55s cubic-bezier(.34,1.56,.64,1) forwards;
}

@keyframes ccb-19-boom {
  0% {
    background: var(--p1);
    box-shadow: 0 0 0 0 var(--p1),0 0 0 0 var(--p2),0 0 0 0 var(--p1),0 0 0 0 var(--p2),0 0 0 0 var(--p1),0 0 0 0 var(--p2),0 0 0 0 var(--p1),0 0 0 0 var(--p2);
  }

  100% {
    background: transparent;
    box-shadow: 26px 0 0 -3px transparent,18px -18px 0 -3px transparent,0 -26px 0 -3px transparent,-18px -18px 0 -3px transparent,-26px 0 0 -3px transparent,-18px 18px 0 -3px transparent,0 26px 0 -3px transparent,18px 18px 0 -3px transparent;
  }

  60% {
    background: transparent;
    box-shadow: 22px 0 0 0 var(--p1),15px -15px 0 0 var(--p2),0 -22px 0 0 var(--p1),-15px -15px 0 0 var(--p2),-22px 0 0 0 var(--p1),-15px 15px 0 0 var(--p2),0 22px 0 0 var(--p1),15px 15px 0 0 var(--p2);
  }
}

@keyframes ccb-19-pop {
  0% {
    transform: scale(1);
  }

  30% {
    transform: scale(.8);
  }

  70% {
    transform: scale(1.12);
  }

  100% {
    transform: scale(1);
  }
}

.ccb-19 .ccb-19__close:focus-visible {
  outline: 3px solid var(--p1);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-19 .ccb-19__close:active .ccb-19__burst,
    .ccb-19 .ccb-19__close:active .ccb-19__x {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — eight box-shadow copies of one 6px dot ARE the particles; a single keyframe flings them outward and shrinks them. */
```
