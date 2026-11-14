---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/gradient-flow/"
title: "CSS Multi-Action Button Group with Gradient Flow Progress (Animated CTA Bar)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A multi-action button bar — Save / Publish / Share — where the primary action carries a perpetually flowing gradient that reads as live momentum, and a…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Multi-Action Button Group with Gradient Flow Progress (Animated CTA Bar)
Source: https://codefronts.com/components/css-button-groups/gradient-flow/

A multi-action button bar — Save / Publish / Share — where the primary action carries a perpetually flowing gradient that reads as live momentum, and a determinate progress fill sweeps across on activation. The eye-catching 'CSS multi-action button group gradient flow progress' for CTA bars, wizards and deploy panels.
## HTML
```html
<section class="btn-18" aria-label="Gradient flow multi-action button group demo">
  <div class="btn-18__wrap">
    <p class="btn-18__label">Ready to ship</p>
    <div class="btn-18__bar" role="group" aria-label="Publish actions">
      <button type="button" class="btn-18__primary">Publish now</button>
      <button type="button" class="btn-18__ghost">Save draft</button>
      <button type="button" class="btn-18__ghost">Share link</button>
    </div>
  </div>
</section>
```
## CSS
```css
@property --btn-18-p {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}

.btn-18,
.btn-18 *,
.btn-18 *::before,
.btn-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-18 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 80% 0%,#13182a,#080a14);
  padding: 44px 20px;
}

.btn-18__wrap {
  width: min(560px,100%);
}

.btn-18__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #8ea0ff;
  margin: 0 0 14px 2px;
}

.btn-18__bar {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.btn-18__primary {
  position: relative;
  border: none;
  height: 54px;
  padding: 0 30px;
  border-radius: 14px;
  font-size: 16px;
  font-weight: 800;
  color: #0a0e1c;
  cursor: pointer;
  overflow: hidden;
  background: linear-gradient(90deg,#4d7cff,#c04dff,#ff5db8,#4d7cff);
  background-size: 250% 100%;
  animation: btn-18-flow 4s linear infinite;
  box-shadow: 0 14px 34px -14px rgba(120,90,255,.8);
}

@keyframes btn-18-flow {
  to {
    background-position: 250% 0;
  }
}

.btn-18__primary::after {
  content: "";
  position: absolute;
  inset: 0;
  width: var(--btn-18-p);
  background: rgba(255,255,255,.28);
  border-right: 2px solid rgba(255,255,255,.7);
  transition: none;
}

.btn-18__primary:active {
  animation-play-state: paused;
}

.btn-18__primary:active::after {
  animation: btn-18-fill 1.4s cubic-bezier(.4,0,.2,1) forwards;
}

@keyframes btn-18-fill {
  from {
    --btn-18-p: 0%;
  }

  to {
    --btn-18-p: 100%;
  }
}

.btn-18__primary:hover {
  filter: brightness(1.08);
}

.btn-18__ghost {
  border: 1.5px solid #2b3452;
  background: rgba(255,255,255,.03);
  height: 54px;
  padding: 0 24px;
  border-radius: 14px;
  font-size: 15px;
  font-weight: 700;
  color: #c5d0f0;
  cursor: pointer;
  transition: border-color .18s,background .18s;
}

.btn-18__ghost:hover {
  border-color: #4a5a88;
  background: rgba(255,255,255,.06);
}

.btn-18__primary:focus-visible,
.btn-18__ghost:focus-visible {
  outline: 3px solid #8ea0ff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-18__primary {
    animation: none;
    background-position: 0 0;
  }

  .btn-18__primary:active::after {
    animation: none;
    width: 100%;
  }
}
```
