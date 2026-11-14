---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-cursor-lens-glass-nav-gsap-ready/"
title: "Tailwind Cursor-Lens Glass Nav (GSAP-ready)"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A bright refraction lens that follows the cursor across the frosted bar &mdash; the effect people install GSAP for."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cursor-Lens Glass Nav (GSAP-ready)
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-cursor-lens-glass-nav-gsap-ready/

A bright refraction lens that follows the cursor across the frosted bar &mdash; the effect people install GSAP for. The port keeps the lens itself entirely in utilities and leaves exactly two numbers to JavaScript: an eased --nb15-mx and --nb15-my. Swapping the hand-rolled lerp for gsap.quickTo() is then a three-line change that touches no markup.
## HTML
```html
<section class="nbtw-15 grid place-items-center w-full min-h-svh p-5 font-nb15-sans bg-[conic-gradient(from_90deg_at_50%_50%,#ff8a00,#e52e71,#7f00ff,#ff8a00)] bg-[length:200%_200%] animate-nb15-bg motion-reduce:animate-none" aria-label="Cursor lens interactive glass nav demo">
  <nav class="relative overflow-hidden flex flex-wrap items-center gap-x-5.5 gap-y-3 px-5 py-3.5 rounded-[20px] isolate text-white bg-[color-mix(in_oklab,white_12%,transparent)] border border-white/[0.34] shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_22px_46px_-24px_rgba(0,0,0,.6)] backdrop-blur-[20px] backdrop-saturate-[1.8]" id="nbtw-15-bar" aria-label="Primary">
    <span class="absolute inset-0 z-0 rounded-[inherit] pointer-events-none bg-[radial-gradient(140px_140px_at_var(--nb15-mx,50%)_var(--nb15-my,50%),rgba(255,255,255,.55),rgba(255,255,255,.12)_40%,transparent_65%)] [opacity:var(--nb15-on,0)] transition-opacity duration-300 motion-reduce:transition-none" aria-hidden="true"></span>
    <span class="relative z-[1] text-base font-extrabold">◇ Refract</span>
    <div class="relative z-[1] flex flex-wrap gap-1.5">
      <a class="flex items-center min-h-10 px-4 rounded-xl no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:opacity-100 aria-[current=page]:bg-white/[0.18]" href="#nbtw-15" aria-current="page">Work</a>
      <a class="flex items-center min-h-10 px-4 rounded-xl no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-15">Studio</a>
      <a class="flex items-center min-h-10 px-4 rounded-xl no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-15">Lab</a>
      <a class="flex items-center min-h-10 px-4 rounded-xl no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-15">Contact</a>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb15-sans: system-ui, 'Segoe UI', sans-serif;
  --animate-nb15-bg: nb15-bg 22s ease-in-out infinite;
}

@keyframes nb15-bg {
  50% {
    background-position: 100% 100%;
  }
}
```

## JavaScript
```js
(() => {
  const bar = document.querySelector('#nbtw-15-bar');
  if (!bar) return;
  let tx = 50, ty = 50, cx = 50, cy = 50, raf = null;
  // GSAP upgrade: const qx = gsap.quickTo(bar, '--nb15-mx', { duration: .4, unit: '%' });
  const loop = () => {
    cx += (tx - cx) * 0.18;
    cy += (ty - cy) * 0.18;
    bar.style.setProperty('--nb15-mx', cx.toFixed(1) + '%');
    bar.style.setProperty('--nb15-my', cy.toFixed(1) + '%');
    raf = (Math.abs(tx - cx) > 0.1 || Math.abs(ty - cy) > 0.1) ? requestAnimationFrame(loop) : null;
  };
  bar.addEventListener('pointermove', (e) => {
    const r = bar.getBoundingClientRect();
    tx = ((e.clientX - r.left) / r.width) * 100;
    ty = ((e.clientY - r.top) / r.height) * 100;
    bar.style.setProperty('--nb15-on', '1');
    if (!raf) raf = requestAnimationFrame(loop);
  });
  bar.addEventListener('pointerleave', () => bar.style.setProperty('--nb15-on', '0'));
})();
```
