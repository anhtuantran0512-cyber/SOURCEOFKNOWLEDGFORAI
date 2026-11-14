---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/toast-dismiss/"
title: "Toast Dismiss Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The notification-toast pattern done to spec: a compact × whose tap target is extended with padding + negative margin so it fills the toast's corner without…"
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Toast Dismiss Close Button
Source: https://codefronts.com/components/css-close-buttons/toast-dismiss/

The notification-toast pattern done to spec: a compact × whose tap target is extended with padding + negative margin so it fills the toast's corner without inflating the layout, an auto-dismiss progress bar that PAUSES while hovered (the detail every toast library gets asked for), and a slide-out exit on transform.
## HTML
```html
<section class="ccb-25" aria-label="Toast dismiss close button demo">
  <div class="ccb-25__toast" id="ccb-25-toast" role="status">
    <span class="ccb-25__icon" aria-hidden="true">✓</span>
    <div class="ccb-25__body">
      <strong class="ccb-25__title">Changes saved</strong>
      <span class="ccb-25__sub">Hover me to pause the countdown</span>
    </div>
    <button class="ccb-25__close" id="ccb-25-close" type="button" aria-label="Dismiss notification">
      <span class="ccb-25__x" aria-hidden="true"></span>
    </button>
    <span class="ccb-25__bar" id="ccb-25-bar" aria-hidden="true"></span>
  </div>
  <button class="ccb-25__reset" id="ccb-25-reset" type="button" hidden>Show toast again</button>
</section>
```
## CSS
```css
.ccb-25,
.ccb-25 *,
.ccb-25 *::before,
.ccb-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-25 {
  --edge: oklch(0.72 0.15 160);
  --life: 5s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.23 0.02 250),oklch(0.17 0.015 250));
}

.ccb-25 .ccb-25__toast {
  position: relative;
  width: min(360px,100%);
  display: flex;
  align-items: center;
  gap: 12px;
  background: oklch(0.28 0.02 250);
  border: 1px solid oklch(0.4 0.02 250 / .6);
  border-radius: 14px;
  padding: 14px 16px;
  overflow: hidden;
  box-shadow: 0 20px 46px -24px rgba(0,0,0,.85);
  transition: transform .3s ease,opacity .3s ease;
}

.ccb-25 .ccb-25__toast.is-leaving {
  transform: translateX(24px);
  opacity: 0;
}

.ccb-25 .ccb-25__icon {
  display: grid;
  place-items: center;
  width: 26px;
  height: 26px;
  flex-shrink: 0;
  border-radius: 50%;
  background: color-mix(in oklab,var(--edge) 25%,transparent);
  color: var(--edge);
  font-size: 13px;
  font-weight: 700;
}

.ccb-25 .ccb-25__body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.ccb-25 .ccb-25__title {
  font-size: 13.5px;
  color: oklch(0.93 0.01 250);
}

.ccb-25 .ccb-25__sub {
  font-size: 11.5px;
  color: oklch(0.65 0.02 250);
}

.ccb-25 .ccb-25__close {
  position: relative;
  flex-shrink: 0;
  padding: 12px;
  margin: -8px -8px -8px auto;
  border: none;
  background: transparent;
  border-radius: 10px;
  cursor: pointer;
  transition: background .15s ease;
}

.ccb-25 .ccb-25__close:hover {
  background: rgba(255,255,255,.08);
}

.ccb-25 .ccb-25__close:focus-visible {
  outline: 2.5px solid var(--edge);
  outline-offset: -2px;
}

.ccb-25 .ccb-25__x {
  position: relative;
  display: block;
  width: 16px;
  height: 16px;
}

.ccb-25 .ccb-25__x::before,
.ccb-25 .ccb-25__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 16px;
  height: 2px;
  border-radius: 2px;
  background: oklch(0.75 0.02 250);
}

.ccb-25 .ccb-25__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-25 .ccb-25__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-25 .ccb-25__bar {
  position: absolute;
  inset-inline: 0;
  bottom: 0;
  height: 3px;
  background: var(--edge);
  transform-origin: left;
  animation: ccb-25-life var(--life) linear forwards;
}

.ccb-25 .ccb-25__toast:hover .ccb-25__bar {
  animation-play-state: paused;
}

@keyframes ccb-25-life {
  from {
    transform: scaleX(1);
  }

  to {
    transform: scaleX(0);
  }
}

.ccb-25 .ccb-25__reset {
  font: 500 12px/1 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.7 0.05 250);
  background: none;
  border: none;
  border-bottom: 1px dashed currentColor;
  cursor: pointer;
  padding: 2px 0;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-25 .ccb-25__bar {
    animation-duration: 20s;
  }
}
```

## JavaScript
```js
(() => {
  const toast = document.getElementById('ccb-25-toast'); if (!toast) return;
  const bar = document.getElementById('ccb-25-bar');
  const reset = document.getElementById('ccb-25-reset');
  const leave = () => {
    toast.classList.add('is-leaving');
    setTimeout(() => { toast.style.display = 'none'; reset.hidden = false; reset.focus(); }, 300);
  };
  bar.addEventListener('animationend', leave);              // countdown owns the clock — no duplicate timer
  document.getElementById('ccb-25-close').addEventListener('click', leave);
  reset.addEventListener('click', () => {
    toast.style.display = ''; toast.classList.remove('is-leaving'); reset.hidden = true;
    bar.style.animation = 'none';                            // restart the countdown
    requestAnimationFrame(() => { bar.style.animation = ''; });
  });
})();
```
