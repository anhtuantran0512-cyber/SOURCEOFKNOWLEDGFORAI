---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/add-to-cart-ripple-glass-button/"
title: "Add-to-Cart Ripple Glass Button"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A Liquid Glass 'Add to Cart' CTA that ripples like a disturbed pool of liquid on hover and click — a real SVG displacement map animates outward from the…"
has_js: "true"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Add-to-Cart Ripple Glass Button
Source: https://codefronts.com/motion/css-button-hover-effects/add-to-cart-ripple-glass-button/

A Liquid Glass 'Add to Cart' CTA that ripples like a disturbed pool of liquid on hover and click — a real SVG displacement map animates outward from the pointer, warping the button's frosted surface, then settles. Includes a success morph where the label swaps to a checkmark with a spring.
## HTML
```html
<section class="bhe-36" aria-label="Add to cart ripple glass button demo">
  <svg class="bhe-36__defs" aria-hidden="true" width="0" height="0"><filter id="bhe-36-ripple"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="3" result="n"><animate attributeName="baseFrequency" dur="6s" values="0.02;0.035;0.02" repeatCount="indefinite"/></feTurbulence><feDisplacementMap id="bhe-36-disp" in="SourceGraphic" in2="n" scale="0" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
  <div class="bhe-36__stage" data-perf="high">
    <button class="bhe-36__btn" id="bhe-36-btn" type="button">
      <span class="bhe-36__glass" aria-hidden="true"></span>
      <span class="bhe-36__lbl"><span class="bhe-36__ic" aria-hidden="true">🛒</span>Add to Cart · $89</span>
    </button>
    <p class="bhe-36__status" id="bhe-36-status" aria-live="polite"></p>
    <label class="bhe-36__perf"><input type="checkbox" id="bhe-36-perf"> High-Performance Mode (CSS ripple)</label>
  </div>
</section>
```
## CSS
```css
.bhe-36,
.bhe-36 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-36 {
  --accent: oklch(0.68 0.18 155);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 200deg at 40% 60%,#0ea5e9,#6366f1,#ec4899,#0ea5e9);
  background-size: 220% 220%;
  animation: bhe-36-bg 20s ease-in-out infinite;
}

@keyframes bhe-36-bg {
  50% {
    background-position: 100% 100%;
  }
}

.bhe-36__stage {
  display: grid;
  justify-items: center;
  gap: 16px;
}

.bhe-36__btn {
  position: relative;
  min-height: 52px;
  padding: 0 30px;
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  color: #fff;
  font: 700 16px 'Segoe UI',system-ui,sans-serif;
  --mx: 50%;
  --my: 50%;
  background: color-mix(in oklab,white 16%,transparent);
  border: 1px solid rgba(255,255,255,.45);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6),0 18px 40px -18px rgba(0,0,0,.7);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
}

.bhe-36__glass {
  position: absolute;
  inset: 0;
  background: radial-gradient(140px 140px at var(--mx) var(--my),rgba(255,255,255,.4),transparent 60%);
}

.bhe-36__stage[data-perf=high] .bhe-36__glass {
  filter: url(#bhe-36-ripple);
}

.bhe-36__lbl {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  transition: opacity .25s,transform .3s;
}

.bhe-36__ic {
  font-size: 17px;
}

.bhe-36__btn:hover {
  box-shadow: inset 0 1px 0 rgba(255,255,255,.7),0 22px 46px -18px rgba(0,0,0,.7);
}

.bhe-36__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.bhe-36__btn.is-done {
  background: color-mix(in oklab,var(--accent) 70%,transparent);
  border-color: transparent;
}

.bhe-36__btn.is-done .bhe-36__lbl {
  transform: scale(1.04);
}

.bhe-36__stage:not([data-perf=high]) .bhe-36__btn.is-ripple .bhe-36__glass {
  animation: bhe-36-css .6s ease-out;
}

@keyframes bhe-36-css {
  0% {
    transform: scale(.3);
    opacity: .9;
  }

  100% {
    transform: scale(2.4);
    opacity: 0;
  }
}

.bhe-36__status {
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  min-height: 1.2em;
  text-shadow: 0 1px 6px rgba(0,0,0,.3);
}

.bhe-36__perf {
  color: rgba(255,255,255,.85);
  font-size: 12.5px;
  display: flex;
  align-items: center;
  gap: 7px;
  cursor: pointer;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-36 {
    animation: none;
  }

  .bhe-36__stage[data-perf=high] .bhe-36__glass {
    filter: none;
  }
}
```

## JavaScript
```js
(() => {
  const stage = document.querySelector('.bhe-36__stage');
  const btn = document.querySelector('#bhe-36-btn');
  const disp = document.querySelector('#bhe-36-disp');
  const status = document.querySelector('#bhe-36-status');
  const perf = document.querySelector('#bhe-36-perf');
  if (!btn) return;
  perf.addEventListener('change', () => stage.dataset.perf = perf.checked ? 'css' : 'high');
  const setPos = (e) => {
    const r = btn.getBoundingClientRect();
    btn.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    btn.style.setProperty('--my', (e.clientY - r.top) + 'px');
  };
  btn.addEventListener('pointermove', setPos);
  let raf;
  const rippleSVG = () => {
    let s = 26, dir = -1;
    cancelAnimationFrame(raf);
    const step = () => { s += dir * 1.6; if (s <= 0) { disp.setAttribute('scale', 0); return; } disp.setAttribute('scale', s); raf = requestAnimationFrame(step); };
    step();
  };
  btn.addEventListener('click', (e) => {
    setPos(e);
    if (stage.dataset.perf === 'high') rippleSVG();
    else { btn.classList.remove('is-ripple'); void btn.offsetWidth; btn.classList.add('is-ripple'); }
    btn.classList.add('is-done');
    btn.querySelector('.bhe-36__lbl').innerHTML = '<span aria-hidden="true">✓</span> Added to Cart';
    status.textContent = 'Added to cart — 1 item';
    setTimeout(() => { btn.classList.remove('is-done'); btn.querySelector('.bhe-36__lbl').innerHTML = '<span class="bhe-36__ic" aria-hidden="true">🛒</span>Add to Cart · $89'; }, 1600);
  });
})();
```
