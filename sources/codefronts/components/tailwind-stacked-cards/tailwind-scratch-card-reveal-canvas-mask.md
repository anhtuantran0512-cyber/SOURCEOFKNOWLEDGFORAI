---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-scratch-card-reveal-canvas-mask/"
title: "Tailwind Scratch Card Reveal Canvas Mask"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A foil coating you scratch away with a finger."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scratch Card Reveal Canvas Mask
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-scratch-card-reveal-canvas-mask/

A foil coating you scratch away with a finger. The interesting boundary here is that Tailwind styles the frame and the canvas owns the pixels: the coating, the brush and the erase are Canvas 2D with destination-out, while the layout, the prize card, the crosshair cursor and the data-[done=true]:opacity-0 fade are all utilities. Knowing which side of that line a problem is on is most of the work.
## HTML
```html
<section class="stk-27 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk27-sans bg-stk27-bg" aria-label="Scratch card">
  <div class="relative w-75">
    <div class="relative flex h-45 flex-col items-center justify-center gap-1.5 rounded-[18px] bg-linear-[150deg,var(--color-stk27-p1),var(--color-stk27-p2)] text-stk27-ink shadow-[0_20px_44px_-22px_rgba(0,0,0,0.7)]">
      <p class="m-0 font-stk27-mono text-xs font-medium tracking-[0.16em] uppercase opacity-80">You won</p>
      <b class="text-[34px] font-black tracking-[0.05em]">LUCKY-40</b>
      <p class="m-0 text-[13px] opacity-85">40% off your next pack</p>
    </div>
    <canvas class="absolute left-0 top-0 w-75 h-45 rounded-[18px] cursor-crosshair [touch-action:none] transition-opacity duration-500 data-[done=true]:opacity-0 data-[done=true]:pointer-events-none motion-reduce:duration-200" id="stk-27-canvas" width="300" height="180" role="img" aria-label="Scratch-off coating hiding a promo code. Use the Reveal button if you prefer not to scratch."></canvas>
    <div class="mt-4 flex gap-2.5">
      <button class="flex-1 rounded-[11px] border border-stk27-line bg-stk27-btn px-4 py-2.5 text-[13px] font-bold text-white cursor-pointer transition-colors duration-200 hover:bg-stk27-btnh focus-visible:outline-3 focus-visible:outline-stk27-ring focus-visible:outline-offset-2" id="stk-27-reveal" type="button">Reveal</button>
      <button class="flex-1 rounded-[11px] border border-stk27-line bg-stk27-btn px-4 py-2.5 text-[13px] font-bold text-white cursor-pointer transition-colors duration-200 hover:bg-stk27-btnh focus-visible:outline-3 focus-visible:outline-stk27-ring focus-visible:outline-offset-2" id="stk-27-reset" type="button">Reset</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk27-bg: #141019;
  --color-stk27-bg: oklch(0.19 0.020 300);
  --color-stk27-p1: #e8b53f;
  --color-stk27-p1: oklch(0.80 0.15 90);
  --color-stk27-p2: #e08a3c;
  --color-stk27-p2: oklch(0.70 0.16 55);
  --color-stk27-ink: #3a1f00;
  --color-stk27-ink: oklch(0.30 0.070 65);
  --color-stk27-btn: #20232f;
  --color-stk27-btn: oklch(0.26 0.016 275);
  --color-stk27-btnh: #2b2f3e;
  --color-stk27-btnh: oklch(0.32 0.018 275);
  --color-stk27-line: #333a4e;
  --color-stk27-line: oklch(0.36 0.020 275);
  --color-stk27-ring: #e8a83f;
  --color-stk27-ring: oklch(0.76 0.15 70);
  --font-stk27-sans: 'Archivo', system-ui, sans-serif;
  --font-stk27-mono: 'JetBrains Mono', ui-monospace, monospace;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.stk-27');
  if (!root) return;
  const canvas = root.querySelector('#stk-27-canvas');
  const ctx = canvas.getContext('2d');
  const W = 300, H = 180;

  /* Sized to devicePixelRatio and laid out at CSS size by w-75 h-45 — without
     this the scratched edge is visibly soft on any retina display. */
  function coat() {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.globalCompositeOperation = 'source-over';
    const g = ctx.createLinearGradient(0, 0, W, H);
    g.addColorStop(0, '#9aa0b4');
    g.addColorStop(1, '#6b7186');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = 'rgba(255,255,255,0.16)';
    ctx.font = 'bold 15px Archivo, system-ui, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('SCRATCH HERE', W / 2, H / 2 + 5);
    delete canvas.dataset.done;
  }

  /* destination-out erases pixels. Painting a colour over the foil looks
     similar and breaks the moment the prize behind it changes. */
  function scratch(x, y) {
    ctx.globalCompositeOperation = 'destination-out';
    ctx.beginPath();
    ctx.arc(x, y, 18, 0, Math.PI * 2);
    ctx.fill();
  }

  const pos = (e) => {
    const r = canvas.getBoundingClientRect();
    return [(e.clientX - r.left) * (W / r.width), (e.clientY - r.top) * (H / r.height)];
  };

  /* Sampled, not scanned: every 40th pixel is plenty to decide "half gone". */
  function cleared() {
    const d = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    let clear = 0, seen = 0;
    for (let i = 3; i < d.length; i += 4 * 40) { seen++; if (d[i] === 0) clear++; }
    return seen ? clear / seen : 0;
  }

  let drawing = false;
  canvas.addEventListener('pointerdown', (e) => {
    drawing = true;
    canvas.setPointerCapture(e.pointerId);
    scratch(...pos(e));
  });
  canvas.addEventListener('pointermove', (e) => { if (drawing) scratch(...pos(e)); });
  canvas.addEventListener('pointerup', () => {
    drawing = false;
    if (cleared() > 0.5) reveal();
  });

  const reveal = () => { canvas.dataset.done = 'true'; };
  root.querySelector('#stk-27-reveal').addEventListener('click', reveal);
  root.querySelector('#stk-27-reset').addEventListener('click', coat);
  coat();
})();
```
