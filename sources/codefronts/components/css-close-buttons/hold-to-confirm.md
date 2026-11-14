---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/hold-to-confirm/"
title: "Hold to Confirm Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "Destructive-action protection: closing requires pressing and HOLDING for 900ms while a conic-gradient ring fills clockwise around the button."
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hold to Confirm Close Button
Source: https://codefronts.com/components/css-close-buttons/hold-to-confirm/

Destructive-action protection: closing requires pressing and HOLDING for 900ms while a conic-gradient ring fills clockwise around the button. Release early and the ring rewinds; hold to completion and the dismissal fires. The fill is one CSS custom property animated by @property — JS only starts, cancels, and listens for completion.
## HTML
```html
<section class="ccb-24" aria-label="Hold to confirm close button demo">
  <div class="ccb-24__wrap">
    <button class="ccb-24__close" id="ccb-24-btn" type="button" aria-label="Hold to close">
      <span class="ccb-24__x" aria-hidden="true"></span>
    </button>
    <span class="ccb-24__hint" id="ccb-24-hint">Press &amp; hold to close</span>
  </div>
</section>
```
## CSS
```css
@property --ccb-24-p {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}

.ccb-24,
.ccb-24 *,
.ccb-24 *::before,
.ccb-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-24 {
  --accent: oklch(0.62 0.21 25);
  --hold: 900ms;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.2 0.02 25),oklch(0.14 0.015 20));
}

.ccb-24 .ccb-24__wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.ccb-24 .ccb-24__close {
  --ccb-24-p: 0%;
  position: relative;
  display: grid;
  place-items: center;
  width: 76px;
  height: 76px;
  border: none;
  border-radius: 50%;
  background: oklch(0.25 0.03 25);
  cursor: pointer;
  transition: --ccb-24-p .3s ease-out,transform .15s ease;
  box-shadow: 0 18px 40px -20px rgba(0,0,0,.9);
}

.ccb-24 .ccb-24__close::before {
  content: "";
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  background: conic-gradient(var(--accent) var(--ccb-24-p),oklch(0.35 0.03 25 / .5) 0);
  -webkit-mask: radial-gradient(circle,transparent 66%,#000 67%);
  mask: radial-gradient(circle,transparent 66%,#000 67%);
}

.ccb-24 .ccb-24__close.is-holding {
  --ccb-24-p: 100%;
  transition: --ccb-24-p var(--hold) linear,transform .15s ease;
  transform: scale(.96);
}

.ccb-24 .ccb-24__close.is-done {
  background: var(--accent);
}

.ccb-24 .ccb-24__x {
  position: relative;
  width: 24px;
  height: 24px;
}

.ccb-24 .ccb-24__x::before,
.ccb-24 .ccb-24__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 24px;
  height: 3px;
  border-radius: 2px;
  background: oklch(0.95 0.02 25);
}

.ccb-24 .ccb-24__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-24 .ccb-24__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-24 .ccb-24__close:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 5px;
}

.ccb-24 .ccb-24__hint {
  font-size: 12px;
  letter-spacing: .04em;
  color: oklch(0.65 0.03 25);
}

@media (prefers-reduced-motion: reduce) {
  .ccb-24 .ccb-24__close {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('ccb-24-btn'); if (!btn) return;
  const hint = document.getElementById('ccb-24-hint');
  const HOLD = 900; let timer = null;
  const start = () => {
    if (btn.classList.contains('is-done')) return;
    btn.classList.add('is-holding');
    timer = setTimeout(complete, HOLD);           // completion by timer — robust even if transitionend is missed
  };
  const cancel = () => { clearTimeout(timer); btn.classList.remove('is-holding'); };
  const complete = () => {
    btn.classList.add('is-done'); btn.classList.remove('is-holding');
    hint.textContent = 'Closed ✓ (click to reset)';
    navigator.vibrate?.(10);
  };
  btn.addEventListener('pointerdown', start);
  btn.addEventListener('pointerup', cancel);
  btn.addEventListener('pointerleave', cancel);
  btn.addEventListener('keydown', (e) => { if ((e.key === 'Enter' || e.key === ' ') && !e.repeat) { e.preventDefault(); start(); } });
  btn.addEventListener('keyup', (e) => { if (e.key === 'Enter' || e.key === ' ') cancel(); });
  btn.addEventListener('click', () => {           // reset for the demo
    if (btn.classList.contains('is-done')) { btn.classList.remove('is-done'); hint.textContent = 'Press & hold to close'; }
  });
})();
```
