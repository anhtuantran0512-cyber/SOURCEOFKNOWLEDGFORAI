---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-toolbox-latch-spotlight-button/"
title: "Tailwind Toolbox Latch Spotlight Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A steel toolbox latch under a work lamp: a spotlight tracks your pointer across the brushed plate, and clicking throws the latch — the hasp swings up over…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Toolbox Latch Spotlight Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-toolbox-latch-spotlight-button/

A steel toolbox latch under a work lamp: a spotlight tracks your pointer across the brushed plate, and clicking throws the latch — the hasp swings up over the keeper and the button reports its state through aria-pressed, not just its look.
## HTML
```html
<div class="tb-48 w-full min-h-svh grid place-items-center font-tb48-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" aria-pressed="false" class="tb-48__plate group relative overflow-hidden cursor-pointer grid place-items-center w-68 min-h-22 pl-22 pr-4 border border-tb48-edge rounded-lg text-base font-extrabold tracking-[-0.01em] text-tb48-ink [text-shadow:0_1px_0_#ffffff73] shadow-[inset_0_1px_0_#ffffff80,inset_0_-2px_5px_#00000059,0_16px_26px_-14px_#000000cc] transition-[translate,box-shadow] duration-200 ease-tb48-out touch-manipulation [-webkit-tap-highlight-color:transparent] hover:-translate-y-0.5 active:translate-y-px active:shadow-[inset_0_2px_6px_#00000073] aria-pressed:shadow-[inset_0_2px_6px_#00000066,0_8px_16px_-12px_#000000cc] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb48-lamp motion-reduce:transition-none">
    <span aria-hidden="true" class="tb-48__light absolute inset-0 z-30 pointer-events-none"></span>
    <span aria-hidden="true" class="tb-48__rivet absolute z-20 top-2 right-2.5 size-2 rounded-full"></span>
    <span aria-hidden="true" class="tb-48__rivet absolute z-20 bottom-2 right-2.5 size-2 rounded-full"></span>
    <span aria-hidden="true" class="tb-48__keeper absolute z-10 left-4 top-1/2 -mt-[1.15rem] size-9.5 rounded-[0.2rem] shadow-[inset_0_1px_0_#ffffff47,0_2px_4px_#00000080]"></span>
    <span aria-hidden="true" class="tb-48__hasp absolute z-20 left-[2.4rem] top-1/2 -mt-[0.55rem] w-10 h-[1.1rem] rounded-[0.2rem] shadow-[inset_0_1px_0_#ffffff99,0_2px_5px_#00000080] [transform-origin:calc(100%-0.55rem)_50%] transition-[rotate] duration-500 ease-tb48-out group-aria-pressed:-rotate-[58deg] motion-reduce:transition-none">
      <span class="tb-48__pin absolute right-[0.28rem] top-1/2 size-[0.55rem] -mt-[0.275rem] rounded-full shadow-[inset_0_-1px_1px_#00000080]"></span>
    </span>
    <span class="relative z-40">Latch the case</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb48-bg: #191b1d;
  --color-tb48-bg: oklch(0.21 0.006 240);
  --color-tb48-steel: #9ba3aa;
  --color-tb48-steel: oklch(0.7 0.008 240);
  --color-tb48-steel-hi: #d3d9de;
  --color-tb48-steel-hi: oklch(0.87 0.008 240);
  --color-tb48-steel-lo: #5f676d;
  --color-tb48-steel-lo: oklch(0.48 0.01 240);
  --color-tb48-edge: #2a2f33;
  --color-tb48-edge: oklch(0.28 0.008 240);
  --color-tb48-ink: #1b1f22;
  --color-tb48-ink: oklch(0.22 0.008 240);
  --color-tb48-lamp: #fff6d6;
  --color-tb48-lamp: oklch(0.97 0.05 95);
  --font-tb48-sans: "Archivo", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb48-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-48 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(30rem 18rem at 50% 30%, #24282b, transparent 72%), var(--color-tb48-bg);
}
/* Pointer defaults: with no pointer (touch, keyboard) the plate keeps a static
   top-light rather than going dead. */

.tb-48__plate {
  --mx: 50%;
  --my: 0%;
  background-color: var(--color-tb48-steel);
  background-image: repeating-linear-gradient(90deg, rgba(255,255,255,.1) 0 1px, transparent 1px 2px, rgba(0,0,0,.06) 2px 3px, transparent 3px 6px), linear-gradient(170deg, var(--color-tb48-steel-hi), var(--color-tb48-steel) 45%, var(--color-tb48-steel-lo));
}

.tb-48__light {
  mix-blend-mode: screen;
  background: radial-gradient(7rem 7rem at var(--mx) var(--my), rgba(255,246,214,.34), rgba(255,246,214,.09) 42%, transparent 68%);
}

.tb-48__keeper {
  background: linear-gradient(160deg, var(--color-tb48-steel-lo), #3d4348);
}

.tb-48__keeper::after {
  content: '';
  position: absolute;
  inset: 32% 22%;
  border-radius: .1rem;
  background: #15181a;
  box-shadow: inset 0 1px 2px rgba(0,0,0,.9);
}

.tb-48__hasp {
  background: linear-gradient(180deg, var(--color-tb48-steel-hi), var(--color-tb48-steel) 55%, var(--color-tb48-steel-lo));
}

.tb-48__hasp::after {
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

.tb-48__pin {
  background: radial-gradient(circle at 34% 30%, #eef2f5, #6d757b 62%, #3f4649);
}

.tb-48__rivet {
  background: radial-gradient(circle at 34% 30%, #f2f5f7, #7d858b 60%, #4a5155);
  box-shadow: inset 0 -1px 1px rgba(0,0,0,.45), 0 1px 0 rgba(255,255,255,.3);
}

@media (prefers-color-scheme: light) {
  .tb-48:not([data-theme="dark"]) {
    --color-tb48-bg: oklch(0.25 0.006 240);
  }
}

.tb-48[data-theme="light"] {
  --color-tb48-bg: oklch(0.25 0.006 240);
}

@media (forced-colors: active) {
  .tb-48__plate {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
    text-shadow: none;
  }

  .tb-48__light,
    .tb-48__rivet,
    .tb-48__pin {
    display: none;
  }

  .tb-48__hasp,
    .tb-48__keeper {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-48__plate');
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
  // The ONLY state the controller owns is the attribute. CSS reads it from there.
  btn.addEventListener('click', () => {
    const on = btn.getAttribute('aria-pressed') === 'true';
    btn.setAttribute('aria-pressed', String(!on));
  });
})();
```
