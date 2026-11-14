---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-card-stack-tilt-on-hover-quadrant/"
title: "Tailwind Card Stack Tilt on Hover Quadrant"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A deck that snaps to one of four poses depending on which quadrant your pointer is in &mdash; crisper and far cheaper than continuous tilt."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Card Stack Tilt on Hover Quadrant
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-card-stack-tilt-on-hover-quadrant/

A deck that snaps to one of four poses depending on which quadrant your pointer is in &mdash; crisper and far cheaper than continuous tilt. The script writes two unitless numbers and CSS multiplies them into degrees, which is the pattern worth stealing: rotateX(calc(var(--ty,0)*1deg)) keeps the JS free of units and the CSS free of parsing.
## HTML
```html
<section class="stk-24 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk24-sans bg-stk24-bg [background-image:radial-gradient(circle_at_50%_40%,var(--color-stk24-glow),transparent_70%)]" aria-label="Quadrant tilt card stack">
  <div class="w-[min(300px,90vw)] [perspective:900px] has-focus-visible:[--tx:-9] has-focus-visible:[--ty:7]">
    <div class="group relative h-55 outline-none [transform-style:preserve-3d] [transform:rotateX(calc(var(--ty,0)*1deg))_rotateY(calc(var(--tx,0)*1deg))] transition-transform duration-400 ease-out motion-reduce:transition-none" id="stk-24-stack" tabindex="0" role="group" aria-label="Tilting card deck">
      <div class="absolute inset-0 rounded-[20px] border border-stk24-line bg-stk24-card shadow-[0_22px_44px_-26px_rgba(0,0,0,0.85)] [transform:translate(calc(var(--i)*8px),calc(var(--i)*8px))_translateZ(calc(var(--i)*-20px))]" style="--i:2" aria-hidden="true"></div>
      <div class="absolute inset-0 rounded-[20px] border border-stk24-line bg-stk24-card shadow-[0_22px_44px_-26px_rgba(0,0,0,0.85)] [transform:translate(calc(var(--i)*8px),calc(var(--i)*8px))_translateZ(calc(var(--i)*-20px))]" style="--i:1" aria-hidden="true"></div>
      <div class="absolute inset-0 overflow-hidden rounded-[20px] border border-stk24-line p-7 text-stk24-ink bg-linear-[150deg,var(--color-stk24-t1),var(--color-stk24-t2)] shadow-[0_22px_44px_-26px_rgba(0,0,0,0.85)] [transform:translate(calc(var(--i)*8px),calc(var(--i)*8px))_translateZ(calc(var(--i)*-20px))]" style="--i:0">
        <p class="m-0 font-stk24-mono text-xs font-medium tracking-[0.16em] uppercase text-stk24-accent">Interactive</p>
        <h3 class="mt-2.5 mb-2 text-3xl font-extrabold tracking-[-0.02em]">Tilt me</h3>
        <p class="m-0 max-w-[26ch] text-sm leading-snug text-stk24-body">Enter from any corner &mdash; the deck banks toward you.</p>
        <span class="absolute inset-0 pointer-events-none opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 [background-image:radial-gradient(200px_circle_at_var(--mx,50%)_var(--my,50%),rgba(255,255,255,0.22),transparent_60%)]" id="stk-24-sheen" aria-hidden="true"></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk24-bg: #080d12;
  --color-stk24-bg: oklch(0.13 0.014 220);
  --color-stk24-glow: #10222a;
  --color-stk24-glow: oklch(0.24 0.030 215);
  --color-stk24-card: #132831;
  --color-stk24-card: oklch(0.27 0.030 215);
  --color-stk24-line: #1e3b46;
  --color-stk24-line: oklch(0.34 0.035 215);
  --color-stk24-t1: #153039;
  --color-stk24-t1: oklch(0.29 0.032 215);
  --color-stk24-t2: #0e2028;
  --color-stk24-t2: oklch(0.22 0.028 215);
  --color-stk24-ink: #eaf6f8;
  --color-stk24-ink: oklch(0.96 0.012 215);
  --color-stk24-body: #a9c6cd;
  --color-stk24-body: oklch(0.80 0.028 215);
  --color-stk24-accent: #4fd0dc;
  --color-stk24-accent: oklch(0.80 0.13 195);
  --font-stk24-sans: 'Archivo', system-ui, sans-serif;
  --font-stk24-mono: 'JetBrains Mono', ui-monospace, monospace;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.stk-24');
  if (!root) return;
  const stack = root.querySelector('#stk-24-stack');
  const sheen = root.querySelector('#stk-24-sheen');
  const MAX = 12;

  /* Unitless numbers only. CSS multiplies them into degrees, so this handler
     never concatenates units and the same values could drive anything else. */
  stack.addEventListener('pointermove', (e) => {
    const r = stack.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width;
    const py = (e.clientY - r.top) / r.height;
    stack.style.setProperty('--tx', String((px < 0.5 ? -1 : 1) * MAX));
    stack.style.setProperty('--ty', String((py < 0.5 ? 1 : -1) * MAX));
    sheen.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
    sheen.style.setProperty('--my', (py * 100).toFixed(1) + '%');
  });

  stack.addEventListener('pointerleave', () => {
    stack.style.setProperty('--tx', '0');
    stack.style.setProperty('--ty', '0');
  });
})();
```
