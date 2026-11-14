---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-cursor-spotlight-card-border-highlight/"
title: "Tailwind Cursor Spotlight Card with Masked Border Highlight"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "The restrained one: a soft light and a matching border highlight track the cursor across a near-black surface, and nothing else moves."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cursor Spotlight Card with Masked Border Highlight
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-cursor-spotlight-card-border-highlight/

The restrained one: a soft light and a matching border highlight track the cursor across a near-black surface, and nothing else moves. Two pseudo-elements read the same pair of custom properties, which is why the glow and the edge never drift apart.
## HTML
```html
<section class="tch-16 w-full min-h-svh grid place-items-center bg-tch16-bg font-tch16-mono p-8">
  <article data-tch16="root" class="group relative w-[340px] h-[440px] rounded-[18px] overflow-hidden cursor-pointer bg-tch16-card border border-white/6
    before:content-[''] before:absolute before:inset-0 before:z-1 before:pointer-events-none before:opacity-0 before:transition-opacity before:duration-400 group-hover:before:opacity-100 before:bg-[radial-gradient(300px_circle_at_var(--tch16-x,50%)_var(--tch16-y,50%),rgb(120_200_255/0.18),transparent_60%)]
    after:content-[''] after:absolute after:inset-0 after:z-2 after:rounded-[inherit] after:p-px after:pointer-events-none after:opacity-0 after:transition-opacity after:duration-400 group-hover:after:opacity-100 after:bg-[radial-gradient(250px_circle_at_var(--tch16-x,50%)_var(--tch16-y,50%),rgb(120_200_255/0.6),transparent_50%)] after:[-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] after:[-webkit-mask-composite:xor] after:[mask-composite:exclude]">
    <div class="relative z-3 h-full p-[2.4rem] flex flex-col justify-between text-tch16-ink">
      <div class="flex justify-between text-[0.72rem] tracking-[0.1em] text-tch16-mut"><span>CASE STUDY</span><span>2025</span></div>
      <h2 class="font-tch16-display text-[3.4rem] leading-[0.95] text-tch16-head">Quiet<br><em class="text-tch16-light">Interfaces</em></h2>
      <p class="text-[0.82rem] leading-[1.65] text-tch16-body">A design system built on restraint. The light follows you because attention should follow intent.</p>
      <a href="#" class="inline-flex items-center min-h-11 text-[0.72rem] tracking-[0.12em] text-tch16-mut no-underline rounded transition-colors duration-200 hover:text-tch16-light focus-visible:outline-2 focus-visible:outline-tch16-light focus-visible:outline-offset-2">— READ THE ESSAY</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch16-bg: #08080a;
  --color-tch16-bg: oklch(0.1 0.003 285);
  --color-tch16-card: #101014;
  --color-tch16-card: oklch(0.15 0.005 285);
  --color-tch16-head: #f3f5f9;
  --color-tch16-head: oklch(0.97 0.004 265);
  --color-tch16-ink: #d7dbe2;
  --color-tch16-ink: oklch(0.88 0.008 265);
  --color-tch16-body: #8e94a3;
  --color-tch16-body: oklch(0.65 0.015 265);
  --color-tch16-mut: #6a7080;
  --color-tch16-mut: oklch(0.52 0.015 265);
  --color-tch16-light: #78c8ff;
  --color-tch16-light: oklch(0.81 0.12 232);
  --font-tch16-mono: 'Geist Mono', ui-monospace, monospace;
  --font-tch16-display: 'Instrument Serif', Georgia, serif;
}

.tch-16 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tch-16');
  if (!root) return;
  const card = root.querySelector('[data-tch16="root"]');
  if (!card) return;
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  let frame = 0;
  card.addEventListener('mousemove', (e) => {
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      const r = card.getBoundingClientRect();
      card.style.setProperty('--tch16-x', '' + (e.clientX - r.left) + 'px');
      card.style.setProperty('--tch16-y', '' + (e.clientY - r.top) + 'px');
    });
  });
})();
```
