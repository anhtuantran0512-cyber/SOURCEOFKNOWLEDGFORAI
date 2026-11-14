---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/inkwell-ripple/"
title: "Inkwell Ripple Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The Material Design ink burst, implemented the modern way: a clipped ::after disc expands from the exact tap point (not just the centre) from scale(0) to…"
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inkwell Ripple Close Button
Source: https://codefronts.com/components/css-close-buttons/inkwell-ripple/

The Material Design ink burst, implemented the modern way: a clipped ::after disc expands from the exact tap point (not just the centre) from scale(0) to scale(2.5) while fading — coordinates fed by four lines of JS into CSS custom properties, with a pure-CSS centre-ripple fallback for keyboard activation.
## HTML
```html
<section class="ccb-18" aria-label="Material ripple close button demo">
  <div class="ccb-18__sheet">
    <span class="ccb-18__label">Tap anywhere on the button</span>
    <button class="ccb-18__close" id="ccb-18-btn" type="button" aria-label="Close">
      <span class="ccb-18__x" aria-hidden="true"></span>
    </button>
  </div>
</section>
```
## CSS
```css
.ccb-18,
.ccb-18 *,
.ccb-18 *::before,
.ccb-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-18 {
  --ink: oklch(0.55 0.2 285 / .35);
  font-family: Roboto,'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.95 0.01 285);
}

.ccb-18 .ccb-18__sheet {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
}

.ccb-18 .ccb-18__label {
  font-size: 12.5px;
  color: oklch(0.5 0.03 285);
}

.ccb-18 .ccb-18__close {
  --rx: 50%;
  --ry: 50%;
  position: relative;
  display: grid;
  place-items: center;
  width: 56px;
  height: 56px;
  border: none;
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 3px 10px -2px oklch(0.4 0.06 285 / .4),0 12px 28px -14px oklch(0.4 0.08 285 / .5);
  transition: box-shadow .2s ease;
}

.ccb-18 .ccb-18__close:hover {
  box-shadow: 0 5px 14px -2px oklch(0.4 0.08 285 / .45),0 16px 34px -14px oklch(0.4 0.1 285 / .55);
}

.ccb-18 .ccb-18__close::after {
  content: "";
  position: absolute;
  top: var(--ry);
  left: var(--rx);
  width: 56px;
  height: 56px;
  margin: -28px 0 0 -28px;
  border-radius: 50%;
  background: var(--ink);
  transform: scale(0);
  opacity: 0;
  pointer-events: none;
}

.ccb-18 .ccb-18__close.is-rippling::after {
  animation: ccb-18-ink .45s cubic-bezier(.2,.6,.4,1) forwards;
}

@keyframes ccb-18-ink {
  0% {
    transform: scale(0);
    opacity: 1;
  }

  100% {
    transform: scale(2.5);
    opacity: 0;
  }
}

.ccb-18 .ccb-18__x {
  position: relative;
  width: 18px;
  height: 18px;
}

.ccb-18 .ccb-18__x::before,
.ccb-18 .ccb-18__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: oklch(0.4 0.03 285);
}

.ccb-18 .ccb-18__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-18 .ccb-18__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-18 .ccb-18__close:focus-visible {
  outline: 3px solid oklch(0.55 0.2 285);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-18 .ccb-18__close.is-rippling::after {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('ccb-18-btn'); if (!btn) return;
  const ripple = (x, y) => {
    if (x != null) {
      const r = btn.getBoundingClientRect();
      btn.style.setProperty('--rx', (x - r.left) + 'px');
      btn.style.setProperty('--ry', (y - r.top) + 'px');
    } else { btn.style.setProperty('--rx', '50%'); btn.style.setProperty('--ry', '50%'); }
    btn.classList.remove('is-rippling');
    requestAnimationFrame(() => requestAnimationFrame(() => btn.classList.add('is-rippling')));
  };
  btn.addEventListener('pointerdown', (e) => ripple(e.clientX, e.clientY));
  btn.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') ripple(); });
})();
```
