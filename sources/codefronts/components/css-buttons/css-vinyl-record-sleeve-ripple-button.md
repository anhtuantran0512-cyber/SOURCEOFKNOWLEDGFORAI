---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-vinyl-record-sleeve-ripple-button/"
title: "CSS Vinyl Record Sleeve Ripple Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A record slides half out of its sleeve on hover and starts turning; press it and concentric ripples run out through the grooves like a needle drop."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Vinyl Record Sleeve Ripple Button
Source: https://codefronts.com/components/css-buttons/css-vinyl-record-sleeve-ripple-button/

A record slides half out of its sleeve on hover and starts turning; press it and concentric ripples run out through the grooves like a needle drop. The disc's grooves and label are pure gradients, and the sleeve carries real cover art with a flat fallback.
## HTML
```html
<div class="cb-39">
  <div class="cb-39__stage">
    <button class="cb-39__btn" type="button">
      <span class="cb-39__disc" aria-hidden="true">
        <span class="cb-39__ring"></span>
        <span class="cb-39__ring"></span>
      </span>
      <span class="cb-39__sleeve">
        <img class="cb-39__art" src="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="700" height="700" loading="lazy" decoding="async">
        <span class="cb-39__spine" aria-hidden="true"></span>
        <span class="cb-39__label">Play side one</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&display=swap');

.cb-39 {
  --bg: #131316;
  --sleeve: #e9e4d8;
  --sleeve-lo: #c9c2b2;
  --ink: #1a1712;
  --label: #d8483b;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 22rem at 50% 44%, #1e1e24, transparent 74%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-39 {
    --sleeve: oklch(91% .015 90);
    --label: oklch(58% .19 30);
  }
}

@media (prefers-color-scheme: light) {
  .cb-39:not([data-theme="dark"]) {
    --bg: #1c1c21;
  }
}

.cb-39[data-theme="light"] {
  --bg: #1c1c21;
}

.cb-39,
.cb-39 *,
.cb-39 *::before,
.cb-39 *::after {
  box-sizing: border-box;
}

.cb-39__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-39__btn {
  position: relative;
  isolation: isolate;
  cursor: pointer;
  border: 0;
  background: transparent;
  padding: 0;
  width: 11.5rem;
  height: 11.5rem;
  font: inherit;
  -webkit-tap-highlight-color: transparent;
}

.cb-39__disc {
  position: absolute;
  z-index: 1;
  inset: .4rem;
  border-radius: 50%;
  background: repeating-radial-gradient(circle at 50% 50%, rgba(255,255,255,.055) 0 1px, transparent 1px 3px), conic-gradient(from 210deg, rgba(255,255,255,.14), transparent 26%, rgba(255,255,255,.1) 56%, transparent 82%), radial-gradient(circle, var(--label) 0 25%, #1a1a1a 26%, #0b0b0b 100%);
  box-shadow: 0 8px 18px -6px rgba(0,0,0,.8), inset 0 0 0 1px rgba(255,255,255,.06);
  translate: 0 0;
  transition: translate .55s cubic-bezier(.16,1,.3,1);
}

.cb-39__disc::after {
  content: '';
  position: absolute;
  inset: 47.5%;
  border-radius: 50%;
  background: var(--bg);
  box-shadow: 0 0 0 1px rgba(0,0,0,.6);
}

@keyframes cb-39-spin {
  to {
    rotate: 1turn;
  }
}

.cb-39__sleeve {
  position: absolute;
  z-index: 2;
  inset: 0;
  overflow: hidden;
  display: grid;
  align-content: end;
  border-radius: .25rem;
  background: linear-gradient(150deg, var(--sleeve), var(--sleeve-lo));
  box-shadow: 0 20px 34px -16px rgba(0,0,0,.85), inset 0 0 0 1px rgba(0,0,0,.18);
}

.cb-39__art {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--sleeve-lo);
  filter: saturate(1.05) contrast(1.05);
}

.cb-39__spine {
  position: absolute;
  inset: 0 auto 0 0;
  width: .5rem;
  background: linear-gradient(90deg, rgba(0,0,0,.4), transparent);
}

.cb-39__label {
  position: relative;
  z-index: 3;
  margin: .7rem;
  padding: .5rem .75rem;
  border-radius: .25rem;
  font-size: .8125rem;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--sleeve);
  background: rgba(12,12,14,.72);
  backdrop-filter: blur(3px);
}

.cb-39__btn:is(:hover,:focus-visible) .cb-39__disc {
  translate: 56% 0;
  animation: cb-39-spin 3.4s linear infinite;
}

.cb-39__btn:focus-visible {
  outline: 2px solid var(--label);
  outline-offset: 5px;
  border-radius: .35rem;
}

.cb-39__ring {
  position: absolute;
  inset: 20%;
  border-radius: 50%;
  border: 2px solid rgba(255,255,255,.6);
  opacity: 0;
}

.cb-39__ring:last-child {
  animation-delay: .12s;
}

.cb-39__btn:active .cb-39__ring {
  animation: cb-39-ripple .7s cubic-bezier(.16,1,.3,1);
}

@keyframes cb-39-ripple {
  0% {
    opacity: .7;
    scale: .3;
  }

  100% {
    opacity: 0;
    scale: 1.9;
  }
}

.cb-39__btn:active .cb-39__sleeve {
  scale: .99;
}

.cb-39__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.7);
}

@media (prefers-reduced-motion: reduce) {
  .cb-39__disc {
    transition: none;
  }

  .cb-39__btn:is(:hover,:focus-visible) .cb-39__disc {
    animation: none;
    translate: 56% 0;
  }

  .cb-39__ring {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-39__sleeve {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-39__label {
    background: ButtonFace;
    color: ButtonText;
  }

  .cb-39__disc,
    .cb-39__ring {
    display: none;
  }
}
```
