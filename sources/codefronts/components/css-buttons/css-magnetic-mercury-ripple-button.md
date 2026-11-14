---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-magnetic-mercury-ripple-button/"
title: "CSS Magnetic Mercury Ripple Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "The button leans toward your cursor like it is magnetised, a liquid mercury highlight tracks the pointer across its surface, and clicks send a ripple out…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Magnetic Mercury Ripple Button
Source: https://codefronts.com/components/css-buttons/css-magnetic-mercury-ripple-button/

The button leans toward your cursor like it is magnetised, a liquid mercury highlight tracks the pointer across its surface, and clicks send a ripple out from the exact point of contact. Fourteen lines of JavaScript write two custom properties — every visual is CSS.
## HTML
```html
<div class="cb-15">
  <div class="cb-15__stage">
    <button class="cb-15__btn" type="button">
      <span class="cb-15__mercury" aria-hidden="true"></span>
      <span class="cb-15__ripple" aria-hidden="true"></span>
      <span class="cb-15__label">Explore the system</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap');

.cb-15 {
  --bg: #08090c;
  --btn: #101319;
  --line: #262b36;
  --ink: #f2f5fa;
  --accent: #a3e635;
  --ripple: #a3e635;
  --pull: 13px;
  --radius: 1.15rem;
  --spring: linear(0,.35 6%,.78 14%,1.05 22%,1.09 27%,1.03 36%,1 50%,1);
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(38rem 24rem at 50% 50%, color-mix(in oklab,var(--accent) 8%,transparent), transparent 70%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-15 {
    --accent: oklch(87% .19 124);
    --btn: oklch(20% .015 260);
    --line: oklch(31% .02 260);
  }
}

@media (prefers-color-scheme: light) {
  .cb-15:not([data-theme="dark"]) {
    --bg: #f2f3f5;
    --btn: #111318;
    --line: #2a2f3a;
  }
}

.cb-15[data-theme="light"] {
  --bg: #f2f3f5;
  --btn: #111318;
  --line: #2a2f3a;
}

.cb-15,
.cb-15 *,
.cb-15 *::before,
.cb-15 *::after {
  box-sizing: border-box;
}

.cb-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-15__btn {
  --mx: 50%;
  --my: 50%;
  --dx: 0;
  --dy: 0;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  min-height: 3.75rem;
  padding: 0 2.2rem;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.01em;
  color: var(--ink);
  background: linear-gradient(180deg,color-mix(in oklab,var(--btn) 82%,white 5%),var(--btn));
  box-shadow: 0 20px 44px -24px color-mix(in oklab,black 90%,transparent), inset 0 1px 0 color-mix(in oklab,white 12%,transparent);
  translate: calc(var(--dx) * var(--pull)) calc(var(--dy) * var(--pull) * .6);
  transition: translate .45s var(--spring), border-color .3s ease, box-shadow .3s ease;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.cb-15__label {
  position: relative;
  z-index: 2;
  display: inline-block;
  transition: translate .5s var(--spring);
}

.cb-15__btn:hover .cb-15__label {
  translate: calc(var(--dx) * 4px) calc(var(--dy) * 3px);
}

.cb-15__mercury {
  position: absolute;
  inset: -1px;
  z-index: 1;
  border-radius: inherit;
  opacity: 0;
  background: radial-gradient(9rem 6rem at var(--mx) var(--my), color-mix(in oklab,var(--accent) 55%,transparent), transparent 62%), radial-gradient(3.2rem 3.2rem at var(--mx) var(--my), color-mix(in oklab,white 55%,transparent), transparent 70%);
  filter: blur(2px) saturate(1.2);
  transition: opacity .35s ease;
}

.cb-15__btn:hover {
  border-color: color-mix(in oklab,var(--accent) 45%,var(--line));
}

.cb-15__btn:hover .cb-15__mercury {
  opacity: .9;
}

.cb-15__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.cb-15__btn:active {
  scale: .985;
}

.cb-15__ripple {
  position: absolute;
  z-index: 1;
  top: var(--my);
  left: var(--mx);
  width: 1rem;
  height: 1rem;
  margin: -.5rem 0 0 -.5rem;
  border-radius: 50%;
  pointer-events: none;
  opacity: 0;
  background: radial-gradient(circle, color-mix(in oklab,var(--ripple) 70%,transparent), transparent 70%);
}

.cb-15__btn.is-rippling .cb-15__ripple {
  animation: cb-15-ripple .62s cubic-bezier(.16,1,.3,1) forwards;
}

@keyframes cb-15-ripple {
  0% {
    opacity: .85;
    scale: 0;
  }

  100% {
    opacity: 0;
    scale: 22;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-15__btn {
    translate: 0 0 !important;
    transition: none;
  }

  .cb-15__label {
    transition: none;
    translate: 0 0 !important;
  }

  .cb-15__ripple {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-15__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .cb-15__mercury,
    .cb-15__ripple {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-15__btn');
  if (!btn) return;
  let box = null;
  btn.addEventListener('pointerenter', () => { box = btn.getBoundingClientRect(); });
  btn.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    box = box || btn.getBoundingClientRect();
    const nx = (e.clientX - box.left) / box.width;
    const ny = (e.clientY - box.top) / box.height;
    btn.style.setProperty('--mx', (nx * 100).toFixed(2) + '%');
    btn.style.setProperty('--my', (ny * 100).toFixed(2) + '%');
    btn.style.setProperty('--dx', (nx - 0.5).toFixed(3));
    btn.style.setProperty('--dy', (ny - 0.5).toFixed(3));
  });
  btn.addEventListener('pointerleave', () => {
    box = null;
    btn.style.setProperty('--dx', '0');
    btn.style.setProperty('--dy', '0');
  });
  btn.addEventListener('click', () => {
    btn.classList.remove('is-rippling');
    void btn.offsetWidth; // restart the keyframes
    btn.classList.add('is-rippling');
  });
})();
```
