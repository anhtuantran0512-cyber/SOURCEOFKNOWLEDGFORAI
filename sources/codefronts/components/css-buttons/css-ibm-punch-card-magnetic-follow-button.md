---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-ibm-punch-card-magnetic-follow-button/"
title: "CSS IBM Punch Card Magnetic Follow Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "An 80-column punch card that tilts toward your cursor in real 3D and drifts a few pixels with it: rows of rectangular holes cut by a mask grid, a clipped…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS IBM Punch Card Magnetic Follow Button
Source: https://codefronts.com/components/css-buttons/css-ibm-punch-card-magnetic-follow-button/

An 80-column punch card that tilts toward your cursor in real 3D and drifts a few pixels with it: rows of rectangular holes cut by a mask grid, a clipped corner, faded index printing, and a sheen that tracks the light across the card stock.
## HTML
```html
<div class="cb-50">
  <div class="cb-50__stage">
    <button class="cb-50__btn" type="button">
      <span class="cb-50__sheen" aria-hidden="true"></span>
      <span class="cb-50__holes" aria-hidden="true"></span>
      <span class="cb-50__top">
        <span class="cb-50__seq">0042</span>
        <span class="cb-50__cols">001 · 080</span>
      </span>
      <span class="cb-50__label">RUN JOB — COMPILE</span>
      <span class="cb-50__foot">IBM 5081 · FORTRAN IV</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap');

.cb-50 {
  --bg: #15171a;
  --card: #efe6cd;
  --card-lo: #ddd2b4;
  --ink: #2b2a22;
  --print: #6d8f86;
  --accent: #b4562f;
  --tilt-max: 9deg;
  --mono: "IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(32rem 20rem at 50% 40%, #1f2226, transparent 74%), var(--bg);
  font-family: var(--mono);
}

@supports (color: oklch(50% 0 0)) {
  .cb-50 {
    --card: oklch(92% .03 88);
    --card-lo: oklch(86% .035 86);
    --print: oklch(62% .05 175);
  }
}

@media (prefers-color-scheme: light) {
  .cb-50:not([data-theme="dark"]) {
    --bg: #1c1f22;
  }
}

.cb-50[data-theme="light"] {
  --bg: #1c1f22;
}

.cb-50,
.cb-50 *,
.cb-50 *::before,
.cb-50 *::after {
  box-sizing: border-box;
}

.cb-50__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-50__btn {
  --tx: 0;
  --ty: 0;
  --tilt: 0deg;
  --mx: 50%;
  --my: 50%;
  position: relative;
  cursor: pointer;
  display: grid;
  gap: .55rem;
  align-content: space-between;
  width: min(100%,26rem);
  min-height: 9.5rem;
  padding: .9rem 1.1rem 1rem;
  border: 0;
  border-radius: .15rem;
  text-align: left;
  font: inherit;
  font-size: .8125rem;
  color: var(--ink);
  clip-path: polygon(0 0, calc(100% - 1.1rem) 0, 100% 1.1rem, 100% 100%, 0 100%);
  background-color: var(--card);
  background-image: repeating-linear-gradient(0deg, rgba(109,143,134,.14) 0 1px, transparent 1px 1.05rem), linear-gradient(168deg, var(--card), var(--card-lo));
  filter: drop-shadow(0 14px 22px rgba(0,0,0,.55));
  transform: perspective(760px) rotate3d(var(--ty),var(--tx),0,var(--tilt)) translate3d(calc(var(--tx) * 6px), calc(var(--ty) * -6px), 0);
  transition: transform .4s cubic-bezier(.16,1,.3,1), filter .35s ease;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.cb-50__holes {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

@supports ((mask-composite: intersect) or (-webkit-mask-composite: source-in)) {
  .cb-50__holes {
    background: linear-gradient(180deg, rgba(0,0,0,.55), rgba(0,0,0,.4));
    -webkit-mask: repeating-linear-gradient(90deg, #000 0 .3rem, transparent .3rem .62rem) 0 0/100% 100%, repeating-linear-gradient(180deg, transparent 0 3.2rem, #000 3.2rem 3.75rem, transparent 3.75rem 4.9rem, #000 4.9rem 5.45rem, transparent 5.45rem 100%) 0 0/100% 100%;
    mask: repeating-linear-gradient(90deg, #000 0 .3rem, transparent .3rem .62rem) 0 0/100% 100%, repeating-linear-gradient(180deg, transparent 0 3.2rem, #000 3.2rem 3.75rem, transparent 3.75rem 4.9rem, #000 4.9rem 5.45rem, transparent 5.45rem 100%) 0 0/100% 100%;
    -webkit-mask-composite: source-in;
    mask-composite: intersect;
  }
}

.cb-50__sheen {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: .65;
  background: radial-gradient(12rem 8rem at var(--mx) var(--my), rgba(255,255,255,.5), transparent 66%);
  transition: opacity .35s ease;
}

.cb-50__top {
  position: relative;
  z-index: 3;
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  color: var(--print);
  font-size: .6875rem;
  letter-spacing: .14em;
  font-variant-numeric: tabular-nums;
}

.cb-50__label {
  position: relative;
  z-index: 3;
  font-size: 1.0625rem;
  font-weight: 600;
  letter-spacing: .06em;
}

.cb-50__foot {
  position: relative;
  z-index: 3;
  font-size: .625rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.cb-50__seq {
  font-weight: 600;
}

.cb-50__btn:hover {
  filter: drop-shadow(0 22px 30px rgba(0,0,0,.6));
}

.cb-50__btn:hover .cb-50__sheen {
  opacity: 1;
}

.cb-50__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 5px;
}

.cb-50__btn:active {
  filter: drop-shadow(0 6px 12px rgba(0,0,0,.55));
}

.cb-50__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.6);
  opacity: .75;
}

@media (prefers-reduced-motion: reduce) {
  .cb-50__btn {
    transform: none;
    transition: none;
  }

  .cb-50__sheen {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-50__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    filter: none;
    transform: none;
    clip-path: none;
  }

  .cb-50__holes,
    .cb-50__sheen {
    display: none;
  }

  .cb-50__top,
    .cb-50__foot {
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-50__btn');
  if (!btn) return;
  const max = 9;
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
    btn.style.setProperty('--tx', '0');
    btn.style.setProperty('--ty', '0');
    btn.style.setProperty('--mx', '50%');
    btn.style.setProperty('--my', '50%');
  });
})();
```
