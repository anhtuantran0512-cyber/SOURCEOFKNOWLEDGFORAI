---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-neon-plasma-burst-button/"
title: "CSS Neon Plasma Burst Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A neon tube that idles at low current, floods with plasma on hover, and fires an expanding shock ring on press."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Plasma Burst Button
Source: https://codefronts.com/components/css-buttons/css-neon-plasma-burst-button/

A neon tube that idles at low current, floods with plasma on hover, and fires an expanding shock ring on press. The glow is layered text-shadow and box-shadow rather than a blur filter, so it stays crisp at any zoom, and the plasma is a registered-angle conic gradient under a blur.
## HTML
```html
<div class="cb-17">
  <div class="cb-17__stage">
    <button class="cb-17__btn" type="button">
      <span class="cb-17__plasma" aria-hidden="true"></span>
      <span class="cb-17__burst" aria-hidden="true"></span>
      <span class="cb-17__label">Initiate sequence</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&display=swap');

@property --cb-17-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.cb-17 {
  --bg: #05060a;
  --shell: #0b0d16;
  --tube: #22d3ee;
  --c1: #22d3ee;
  --c2: #a855f7;
  --c3: #f472b6;
  --radius: .6rem;
  --sans: "Chakra Petch",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(44rem 26rem at 50% 50%, color-mix(in oklab,var(--c2) 12%,transparent), transparent 72%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-17 {
    --tube: oklch(82% .14 200);
    --c1: oklch(82% .14 200);
    --c2: oklch(64% .24 305);
    --c3: oklch(74% .17 349);
  }
}

@media (prefers-color-scheme: light) {
  .cb-17:not([data-theme="dark"]) {
    --bg: #0a0b12;
    --shell: #0e1120;
  }
}

.cb-17[data-theme="light"] {
  --bg: #0a0b12;
  --shell: #0e1120;
}

.cb-17,
.cb-17 *,
.cb-17 *::before,
.cb-17 *::after {
  box-sizing: border-box;
}

.cb-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-17__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  min-height: 3.5rem;
  padding: 0 2.1rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: .9375rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .14em;
  color: var(--tube);
  background: var(--shell);
  text-shadow: 0 0 4px color-mix(in oklab,var(--tube) 90%,transparent), 0 0 12px color-mix(in oklab,var(--tube) 55%,transparent), 0 0 34px color-mix(in oklab,var(--tube) 30%,transparent);
  box-shadow: inset 0 0 14px color-mix(in oklab,var(--tube) 20%,transparent), 0 0 0 1px color-mix(in oklab,var(--tube) 50%,transparent), 0 0 30px -8px color-mix(in oklab,var(--tube) 40%,transparent);
  transition: box-shadow .35s ease, color .3s ease, scale .2s cubic-bezier(.16,1,.3,1);
  animation: cb-17-flicker 6s ease-in-out infinite;
}

.cb-17__label {
  position: relative;
  z-index: 2;
}

@keyframes cb-17-flicker {
  0%,
    100% {
    opacity: 1;
  }

  48% {
    opacity: .94;
  }

  50% {
    opacity: .82;
  }

  52% {
    opacity: .97;
  }
}

.cb-17__plasma {
  position: absolute;
  inset: -40%;
  z-index: 1;
  opacity: .3;
  pointer-events: none;
  background: conic-gradient(from var(--cb-17-a),var(--c1),var(--c2),var(--c3),var(--c1));
  filter: blur(16px) saturate(1.5);
  animation: cb-17-spin 7s linear infinite;
  transition: opacity .4s ease;
}

@keyframes cb-17-spin {
  to {
    --cb-17-a: 360deg;
  }
}

.cb-17__btn:is(:hover,:focus-visible) {
  color: #f4feff;
  box-shadow: inset 0 0 22px color-mix(in oklab,var(--tube) 32%,transparent), 0 0 0 1px color-mix(in oklab,var(--tube) 80%,transparent), 0 0 46px -6px color-mix(in oklab,var(--c2) 60%,transparent);
}

.cb-17__btn:is(:hover,:focus-visible) .cb-17__plasma {
  opacity: .62;
  animation-duration: 3.2s;
}

.cb-17__btn:focus-visible {
  outline: 2px solid var(--c1);
  outline-offset: 5px;
}

.cb-17__btn:active {
  scale: .97;
}

.cb-17__burst {
  position: absolute;
  z-index: 1;
  top: 50%;
  left: 50%;
  width: 6rem;
  height: 6rem;
  margin: -3rem 0 0 -3rem;
  border-radius: 50%;
  border: 2px solid var(--c1);
  opacity: 0;
  pointer-events: none;
}

.cb-17__btn:active .cb-17__burst {
  animation: cb-17-burst .62s cubic-bezier(.16,1,.3,1);
}

@keyframes cb-17-burst {
  0% {
    opacity: .9;
    scale: .15;
  }

  100% {
    opacity: 0;
    scale: 3;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-17__btn {
    animation: none;
    transition: none;
  }

  .cb-17__plasma {
    animation: none;
  }

  .cb-17__burst {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-17__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
    text-shadow: none;
  }

  .cb-17__plasma,
    .cb-17__burst {
    display: none;
  }
}
```
