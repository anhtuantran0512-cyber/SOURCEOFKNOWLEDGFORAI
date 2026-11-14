---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-toolbox-latch-spotlight-button/"
title: "CSS Toolbox Latch Spotlight Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A steel toolbox latch under a work lamp: a spotlight tracks your pointer across the brushed plate, and clicking throws the latch — the hasp swings up over…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Toolbox Latch Spotlight Button
Source: https://codefronts.com/components/css-buttons/css-toolbox-latch-spotlight-button/

A steel toolbox latch under a work lamp: a spotlight tracks your pointer across the brushed plate, and clicking throws the latch — the hasp swings up over the keeper and the button reports its state through aria-pressed, not just its look.
## HTML
```html
<div class="cb-48">
  <div class="cb-48__stage">
    <button class="cb-48__btn" type="button" aria-pressed="false">
      <span class="cb-48__light" aria-hidden="true"></span>
      <span class="cb-48__rivet cb-48__rivet--a" aria-hidden="true"></span>
      <span class="cb-48__rivet cb-48__rivet--b" aria-hidden="true"></span>
      <span class="cb-48__keeper" aria-hidden="true"></span>
      <span class="cb-48__hasp" aria-hidden="true"><span class="cb-48__pin"></span></span>
      <span class="cb-48__label">Latch the case</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&display=swap');

.cb-48 {
  --bg: #191b1d;
  --steel: #9ba3aa;
  --steel-hi: #d3d9de;
  --steel-lo: #5f676d;
  --ink: #1b1f22;
  --lamp: #fff6d6;
  --radius: .5rem;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(30rem 18rem at 50% 30%, #24282b, transparent 72%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-48 {
    --steel: oklch(70% .008 240);
    --steel-hi: oklch(87% .008 240);
    --steel-lo: oklch(48% .01 240);
  }
}

@media (prefers-color-scheme: light) {
  .cb-48:not([data-theme="dark"]) {
    --bg: #232629;
  }
}

.cb-48[data-theme="light"] {
  --bg: #232629;
}

.cb-48,
.cb-48 *,
.cb-48 *::before,
.cb-48 *::after {
  box-sizing: border-box;
}

.cb-48__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-48__btn {
  --mx: 50%;
  --my: 0%;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  display: grid;
  place-items: center;
  width: 17rem;
  min-height: 5.5rem;
  padding: 0 1rem 0 5.5rem;
  border: 1px solid #2a2f33;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--ink);
  background-color: var(--steel);
  background-image: repeating-linear-gradient(90deg, rgba(255,255,255,.1) 0 1px, transparent 1px 2px, rgba(0,0,0,.06) 2px 3px, transparent 3px 6px), linear-gradient(170deg, var(--steel-hi), var(--steel) 45%, var(--steel-lo));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), inset 0 -2px 5px rgba(0,0,0,.35), 0 16px 26px -14px rgba(0,0,0,.8);
  text-shadow: 0 1px 0 rgba(255,255,255,.45);
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .25s ease;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.cb-48__label {
  position: relative;
  z-index: 4;
}

.cb-48__light {
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
  mix-blend-mode: screen;
  background: radial-gradient(7rem 7rem at var(--mx) var(--my), rgba(255,246,214,.34), rgba(255,246,214,.09) 42%, transparent 68%);
}

.cb-48__keeper {
  position: absolute;
  z-index: 1;
  left: 1rem;
  top: 50%;
  margin-top: -1.15rem;
  width: 2.3rem;
  height: 2.3rem;
  border-radius: .2rem;
  background: linear-gradient(160deg, var(--steel-lo), #3d4348);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.28), 0 2px 4px rgba(0,0,0,.5);
}

.cb-48__keeper::after {
  content: '';
  position: absolute;
  inset: 32% 22%;
  border-radius: .1rem;
  background: #15181a;
  box-shadow: inset 0 1px 2px rgba(0,0,0,.9);
}

.cb-48__hasp {
  position: absolute;
  z-index: 2;
  left: 2.4rem;
  top: 50%;
  margin-top: -.55rem;
  width: 2.5rem;
  height: 1.1rem;
  border-radius: .2rem;
  background: linear-gradient(180deg, var(--steel-hi), var(--steel) 55%, var(--steel-lo));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6), 0 2px 5px rgba(0,0,0,.5);
  transform-origin: calc(100% - .55rem) 50%;
  transition: rotate .5s cubic-bezier(.16,1,.3,1);
}

.cb-48__hasp::after {
  content: '';
  position: absolute;
  left: .35rem;
  top: .3rem;
  width: 1.1rem;
  height: .5rem;
  border-radius: .1rem;
  background: #15181a;
  box-shadow: inset 0 1px 2px rgba(0,0,0,.8);
}

.cb-48__pin {
  position: absolute;
  right: .28rem;
  top: 50%;
  width: .55rem;
  height: .55rem;
  margin-top: -.275rem;
  border-radius: 50%;
  background: radial-gradient(circle at 34% 30%, #eef2f5, #6d757b 62%, #3f4649);
  box-shadow: inset 0 -1px 1px rgba(0,0,0,.5);
}

.cb-48__rivet {
  position: absolute;
  z-index: 2;
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: radial-gradient(circle at 34% 30%, #f2f5f7, #7d858b 60%, #4a5155);
  box-shadow: inset 0 -1px 1px rgba(0,0,0,.45), 0 1px 0 rgba(255,255,255,.3);
}

.cb-48__rivet--a {
  top: .55rem;
  right: .6rem;
}

.cb-48__rivet--b {
  bottom: .55rem;
  right: .6rem;
}

.cb-48__btn:hover {
  translate: 0 -2px;
}

.cb-48__btn:active {
  translate: 0 1px;
  box-shadow: inset 0 2px 6px rgba(0,0,0,.45);
}

.cb-48__btn:focus-visible {
  outline: 2px solid var(--lamp);
  outline-offset: 4px;
}

.cb-48__btn[aria-pressed="true"] .cb-48__hasp {
  rotate: -58deg;
}

.cb-48__btn[aria-pressed="true"] {
  box-shadow: inset 0 2px 6px rgba(0,0,0,.4), 0 8px 16px -12px rgba(0,0,0,.8);
}

@media (prefers-reduced-motion: reduce) {
  .cb-48__btn,
    .cb-48__hasp {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-48__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
    text-shadow: none;
  }

  .cb-48__light {
    display: none;
  }

  .cb-48__hasp,
    .cb-48__keeper {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-48__rivet,
    .cb-48__pin {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-48__btn');
  if (!btn) return;
  let box = null;
  btn.addEventListener('pointerenter', () => { box = btn.getBoundingClientRect(); });
  btn.addEventListener('pointermove', (e) => {
    box = box || btn.getBoundingClientRect();
    btn.style.setProperty('--mx', (((e.clientX - box.left) / box.width) * 100).toFixed(1) + '%');
    btn.style.setProperty('--my', (((e.clientY - box.top) / box.height) * 100).toFixed(1) + '%');
  });
  btn.addEventListener('pointerleave', () => {
    box = null;
    btn.style.setProperty('--mx', '50%');
    btn.style.setProperty('--my', '0%');
  });
  btn.addEventListener('click', () => {
    const on = btn.getAttribute('aria-pressed') === 'true';
    btn.setAttribute('aria-pressed', String(!on));
  });
})();
```
