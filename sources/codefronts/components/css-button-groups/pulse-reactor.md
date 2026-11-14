---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/pulse-reactor/"
title: "CSS Action Button Row with Radar Shockwave Click Feedback (Ripple Pulse)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "An action button row that answers every click with a radar shockwave — concentric rings burst from the button and a reactor core pulses, giving weighty,…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Action Button Row with Radar Shockwave Click Feedback (Ripple Pulse)
Source: https://codefronts.com/components/css-button-groups/pulse-reactor/

An action button row that answers every click with a radar shockwave — concentric rings burst from the button and a reactor core pulses, giving weighty, satisfying tactile feedback. The impactful 'CSS radar shockwave click feedback button group' (a next-gen ripple) for confirm bars, tool palettes and control panels.
## HTML
```html
<section class="btn-24" aria-label="Radar shockwave action row demo">
  <div class="btn-24__wrap">
    <p class="btn-24__label">Reactor controls — click a button</p>
    <div class="btn-24__row" role="group" aria-label="Reactor controls">
      <button type="button" class="btn-24__btn btn-24__btn--core" style="--c:#37f5c5">Engage</button>
      <button type="button" class="btn-24__btn" style="--c:#5cc8ff">Scan</button>
      <button type="button" class="btn-24__btn" style="--c:#ffb84d">Vent</button>
      <button type="button" class="btn-24__btn btn-24__btn--danger" style="--c:#ff5470">Abort</button>
    </div>
  </div>
</section>
```
## CSS
```css
@property --btn-24-g {
  syntax: "<length>";
  inherits: false;
  initial-value: 0px;
}

.btn-24,
.btn-24 *,
.btn-24 *::before,
.btn-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-24 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 50% 40%,#06201c,#03100e);
  padding: 44px 20px;
}

.btn-24__wrap {
  width: min(600px,100%);
}

.btn-24__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #4fd6b8;
  margin: 0 0 16px 2px;
}

.btn-24__row {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}

.btn-24__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  border: 1.5px solid color-mix(in oklab,var(--c) 55%,#0a1a17);
  background: #0a1a17;
  color: var(--c);
  height: 54px;
  padding: 0 26px;
  border-radius: 14px;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .02em;
  cursor: pointer;
  transition: color .18s,background .18s;
}

.btn-24__btn:hover {
  background: color-mix(in oklab,var(--c) 16%,#0a1a17);
  color: #eafffa;
}

.btn-24__btn::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 120%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle,color-mix(in oklab,var(--c) 70%,transparent) 0 40%,transparent 60%);
  translate: -50% -50%;
  scale: 0;
  opacity: 0;
  z-index: -1;
  pointer-events: none;
}

.btn-24__btn:active::after {
  animation: btn-24-wave .6s ease-out;
}

@keyframes btn-24-wave {
  0% {
    scale: 0;
    opacity: .65;
  }

  100% {
    scale: 2.6;
    opacity: 0;
  }
}

.btn-24__btn:active {
  background: color-mix(in oklab,var(--c) 26%,#0a1a17);
}

.btn-24__btn--core {
  box-shadow: 0 0 var(--btn-24-g) -2px var(--c);
  animation: btn-24-breathe 2.6s ease-in-out infinite;
}

@keyframes btn-24-breathe {
  0%,
    100% {
    --btn-24-g: 14px;
  }

  50% {
    --btn-24-g: 34px;
  }
}

.btn-24__btn--danger {
  color: #ff8098;
}

.btn-24__btn:focus-visible {
  outline: 3px solid var(--c);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-24__btn--core {
    animation: none;
  }

  .btn-24__btn:active::after {
    animation: none;
  }
}
```
