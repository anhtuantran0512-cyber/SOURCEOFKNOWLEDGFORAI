---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/lock-tumble/"
title: "Lock Tumble Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A safe-cracking dismiss: a brass-ringed dial whose × sits inside a notched bezel."
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Lock Tumble Close Button
Source: https://codefronts.com/components/css-close-buttons/lock-tumble/

A safe-cracking dismiss: a brass-ringed dial whose × sits inside a notched bezel. Hover triggers a mechanical combination — the cross ratchets left, further left, then snaps right past centre and settles — driven by one steps()-flavoured keyframe sequence, while the bezel's notch markings counter-rotate like a tumbler wheel.
## HTML
```html
<section class="ccb-12" aria-label="Lock tumbler close button demo">
  <button class="ccb-12__close" type="button" aria-label="Close">
    <span class="ccb-12__ticks" aria-hidden="true"></span>
    <span class="ccb-12__x" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
@property --ccb-12-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.ccb-12,
.ccb-12 *,
.ccb-12 *::before,
.ccb-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-12 {
  --brass-a: oklch(0.78 0.1 85);
  --brass-b: oklch(0.55 0.09 75);
  --spin: 2.4s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 120% at 50% 0%,oklch(0.32 0.04 60),oklch(0.2 0.02 50));
}

.ccb-12 .ccb-12__close {
  position: relative;
  width: 84px;
  height: 84px;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  background: conic-gradient(from 210deg,var(--brass-a),var(--brass-b) 30%,var(--brass-a) 52%,var(--brass-b) 78%,var(--brass-a));
  box-shadow: 0 18px 40px -16px rgba(0,0,0,.75),inset 0 2px 3px rgba(255,255,255,.45),inset 0 -3px 6px rgba(0,0,0,.4);
}

.ccb-12 .ccb-12__close::before {
  content: "";
  position: absolute;
  inset: 10px;
  border-radius: 50%;
  background: radial-gradient(circle at 32% 28%,oklch(0.42 0.05 70),oklch(0.26 0.03 60) 70%);
  box-shadow: inset 0 2px 6px rgba(0,0,0,.6);
}

.ccb-12 .ccb-12__ticks {
  position: absolute;
  inset: 2px;
  border-radius: 50%;
  background: repeating-conic-gradient(from var(--ccb-12-a),transparent 0 8deg,oklch(0.3 0.03 60 / .9) 8deg 10deg);
  -webkit-mask: radial-gradient(circle,transparent 62%,#000 63%,#000 74%,transparent 75%);
  mask: radial-gradient(circle,transparent 62%,#000 63%,#000 74%,transparent 75%);
}

.ccb-12 .ccb-12__x {
  position: absolute;
  inset: 0;
  display: block;
}

.ccb-12 .ccb-12__x::before,
.ccb-12 .ccb-12__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 26px;
  height: 3.5px;
  border-radius: 2px;
  background: linear-gradient(180deg,oklch(0.92 0.06 85),oklch(0.7 0.08 80));
  box-shadow: 0 1px 2px rgba(0,0,0,.5);
}

.ccb-12 .ccb-12__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-12 .ccb-12__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-12 .ccb-12__close:hover .ccb-12__x {
  animation: ccb-12-tumble 1.1s cubic-bezier(.3,0,.2,1) 1 both;
}

.ccb-12 .ccb-12__close:hover .ccb-12__ticks {
  animation: ccb-12-ring var(--spin) linear infinite;
}

@keyframes ccb-12-tumble {
  0% {
    transform: rotate(0);
  }

  14%,
    26% {
    transform: rotate(-20deg);
  }

  40%,
    52% {
    transform: rotate(-38deg);
  }

  68%,
    78% {
    transform: rotate(18deg);
  }

  100% {
    transform: rotate(0);
  }
}

@keyframes ccb-12-ring {
  to {
    --ccb-12-a: -360deg;
  }
}

.ccb-12 .ccb-12__close:active {
  transform: scale(.94);
}

.ccb-12 .ccb-12__close:focus-visible {
  outline: 3px solid var(--brass-a);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-12 .ccb-12__close:hover .ccb-12__x,
    .ccb-12 .ccb-12__close:hover .ccb-12__ticks {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hold-heavy keyframe ratchets the × like tumbler clicks; @property spins the masked tick ring the other way. */
```
