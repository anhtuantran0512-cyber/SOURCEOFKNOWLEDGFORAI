---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-holographic-foil-sticker-button/"
title: "CSS Holographic Foil Sticker Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A die-cut vinyl sticker whose holographic laminate shifts with the pointer: the rainbow sweep, the specular sheen and a 3D tilt all read from two pointer…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Holographic Foil Sticker Button
Source: https://codefronts.com/components/css-buttons/css-holographic-foil-sticker-button/

A die-cut vinyl sticker whose holographic laminate shifts with the pointer: the rainbow sweep, the specular sheen and a 3D tilt all read from two pointer variables, and the corner peels up as you approach — the effect trading-card collectors call "cracked ice".
## HTML
```html
<div class="cb-29">
  <div class="cb-29__stage">
    <button class="cb-29__btn" type="button">
      <span class="cb-29__holo" aria-hidden="true"></span>
      <span class="cb-29__peel" aria-hidden="true"></span>
      <span class="cb-29__plate">
        <span class="cb-29__label">Limited drop</span>
        <span class="cb-29__sub">01 / 250</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&display=swap');

.cb-29 {
  --bg: #0a0a0f;
  --cut: #fbfbfd;
  --plate: #111119;
  --ink: #f6f6fb;
  --muted: #9b9bb0;
  --tilt-max: 8deg;
  --radius: 1.35rem;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(40rem 24rem at 50% 45%, #1b1b28, transparent 72%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: light) {
  .cb-29:not([data-theme="dark"]) {
    --bg: #e9e9ef;
  }
}

.cb-29[data-theme="light"] {
  --bg: #e9e9ef;
}

.cb-29,
.cb-29 *,
.cb-29 *::before,
.cb-29 *::after {
  box-sizing: border-box;
}

.cb-29__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-29__btn {
  --mx: 50%;
  --my: 50%;
  --tx: 0;
  --ty: 0;
  --tilt: 0deg;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  padding: .5rem;
  border: .32rem solid var(--cut);
  border-radius: var(--radius);
  background: var(--plate);
  color: var(--ink);
  filter: drop-shadow(0 16px 26px rgba(0,0,0,.55));
  transform: perspective(700px) rotate3d(var(--ty),var(--tx),0,var(--tilt));
  transition: transform .35s cubic-bezier(.16,1,.3,1), filter .35s ease;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.cb-29__holo {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  opacity: .55;
  mix-blend-mode: color-dodge;
  background-image: repeating-linear-gradient(102deg, #ff5f6d 0 12%, #ffc371 18%, #47e5bc 30%, #4facfe 42%, #b06ab3 54%, #ff5f6d 66%), conic-gradient(from 210deg at var(--mx) var(--my), rgba(255,255,255,.55), transparent 28%, rgba(255,255,255,.4) 62%, transparent 88%);
  background-size: 340% 340%, 100% 100%;
  background-position: var(--mx) var(--my), 0 0;
  transition: opacity .35s ease;
}

.cb-29__plate {
  position: relative;
  z-index: 1;
  display: grid;
  gap: .15rem;
  justify-items: start;
  min-height: 3.1rem;
  padding: .7rem 1.5rem;
  border-radius: calc(var(--radius) - .5rem);
  background: linear-gradient(180deg, color-mix(in oklab,var(--plate) 80%,white 5%), var(--plate));
}

.cb-29__label {
  font-size: 1.0625rem;
  font-weight: 800;
  letter-spacing: -.02em;
}

.cb-29__sub {
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cb-29__peel {
  position: absolute;
  z-index: 3;
  top: -.05rem;
  right: -.05rem;
  width: 1.6rem;
  height: 1.6rem;
  pointer-events: none;
  background: linear-gradient(225deg, #ffffff, #cfd2dc 55%, #9aa0b0);
  clip-path: polygon(100% 0,100% 100%,0 0);
  filter: drop-shadow(-2px 3px 3px rgba(0,0,0,.4));
  scale: 0;
  transform-origin: 100% 0;
  transition: scale .4s cubic-bezier(.16,1,.3,1);
}

.cb-29__btn:is(:hover,:focus-visible) .cb-29__holo {
  opacity: .95;
}

.cb-29__btn:is(:hover,:focus-visible) .cb-29__peel {
  scale: 1;
}

.cb-29__btn:focus-visible {
  outline: 2px solid #4facfe;
  outline-offset: 5px;
}

.cb-29__btn:active {
  scale: .98;
}

@media (prefers-reduced-motion: reduce) {
  .cb-29__btn,
    .cb-29__holo,
    .cb-29__peel {
    transition: none;
  }

  .cb-29__btn {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cb-29__btn {
    background: ButtonFace;
    border-color: ButtonText;
    filter: none;
  }

  .cb-29__holo,
    .cb-29__peel {
    display: none;
  }

  .cb-29__plate {
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-29__btn');
  if (!btn) return;
  const max = 8;
  let box = null;
  btn.addEventListener('pointerenter', () => { box = btn.getBoundingClientRect(); });
  btn.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    box = box || btn.getBoundingClientRect();
    const nx = (e.clientX - box.left) / box.width;
    const ny = (e.clientY - box.top) / box.height;
    btn.style.setProperty('--mx', (nx * 100).toFixed(1) + '%');
    btn.style.setProperty('--my', (ny * 100).toFixed(1) + '%');
    btn.style.setProperty('--tx', (nx - 0.5).toFixed(3));
    btn.style.setProperty('--ty', (0.5 - ny).toFixed(3));
    btn.style.setProperty('--tilt', (Math.hypot(nx - 0.5, ny - 0.5) * 2 * max).toFixed(2) + 'deg');
  });
  btn.addEventListener('pointerleave', () => {
    box = null;
    btn.style.setProperty('--tilt', '0deg');
    btn.style.setProperty('--mx', '50%');
    btn.style.setProperty('--my', '50%');
  });
})();
```
