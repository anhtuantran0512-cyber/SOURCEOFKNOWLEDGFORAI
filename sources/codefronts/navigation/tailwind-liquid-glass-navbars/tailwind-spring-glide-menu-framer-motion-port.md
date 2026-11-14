---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-spring-glide-menu-framer-motion-port/"
title: "Tailwind Spring Glide Menu (Framer Motion Port)"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The shared-element indicator: one frosted pill glides between links on a spring, the layoutId feel without the library."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Spring Glide Menu (Framer Motion Port)
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-spring-glide-menu-framer-motion-port/

The shared-element indicator: one frosted pill glides between links on a spring, the layoutId feel without the library. The port draws a clean line &mdash; the pill's look and its transition are utilities, its two measured numbers are inline styles written by the handler, and the notes are explicit that measurement is the one job utilities cannot do.
## HTML
```html
<section class="nbtw-10 grid place-items-center w-full min-h-svh p-5 font-nb10-sans bg-[conic-gradient(from_30deg_at_40%_40%,#00dbde,#fc00ff,#00dbde)] bg-[length:200%_200%] animate-nb10-bg motion-reduce:animate-none" aria-label="Spring glide menu demo">
  <nav class="relative flex flex-wrap gap-1 p-2 rounded-full isolate bg-[color-mix(in_oklab,white_14%,transparent)] border border-white/40 shadow-[inset_0_1px_0_rgba(255,255,255,.55),0_20px_44px_-22px_rgba(0,0,0,.55)] backdrop-blur-[22px] backdrop-saturate-[1.8]" id="nbtw-10-bar" aria-label="Primary">
    <span class="absolute inset-y-2 left-2 z-0 w-24 rounded-full bg-white/[0.24] border border-white/50 shadow-[inset_0_1px_0_rgba(255,255,255,.7)] transition-[left,width] duration-500 ease-nb10 motion-reduce:transition-none" id="nbtw-10-pill" aria-hidden="true"></span>
    <a class="relative z-[1] flex items-center min-h-10 px-4.5 rounded-full no-underline text-white text-[14.5px] font-semibold transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-10" aria-current="page">Overview</a>
    <a class="relative z-[1] flex items-center min-h-10 px-4.5 rounded-full no-underline text-white text-[14.5px] font-semibold transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-10">Analytics</a>
    <a class="relative z-[1] flex items-center min-h-10 px-4.5 rounded-full no-underline text-white text-[14.5px] font-semibold transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-10">Reports</a>
    <a class="relative z-[1] flex items-center min-h-10 px-4.5 rounded-full no-underline text-white text-[14.5px] font-semibold transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-10">Settings</a>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb10-sans: system-ui, 'Segoe UI', sans-serif;
  --ease-nb10: cubic-bezier(0.34, 1.56, 0.5, 1);
  --animate-nb10-bg: nb10-bg 18s ease-in-out infinite;
}

@keyframes nb10-bg {
  50% {
    background-position: 100% 100%;
  }
}
```

## JavaScript
```js
(() => {
  const bar = document.querySelector('#nbtw-10-bar');
  const pill = document.querySelector('#nbtw-10-pill');
  if (!bar || !pill) return;
  const links = [...bar.querySelectorAll('a')];
  let active = links.find((l) => l.hasAttribute('aria-current')) || links[0];
  const move = (el) => {
    const b = bar.getBoundingClientRect(), r = el.getBoundingClientRect();
    pill.style.left = (r.left - b.left) + 'px';
    pill.style.width = r.width + 'px';
  };
  links.forEach((l) => {
    l.addEventListener('pointerenter', () => move(l));
    l.addEventListener('focus', () => move(l));
    l.addEventListener('click', (e) => {
      e.preventDefault();
      links.forEach((x) => x.removeAttribute('aria-current'));
      l.setAttribute('aria-current', 'page');
      active = l;
    });
  });
  bar.addEventListener('pointerleave', () => move(active));
  requestAnimationFrame(() => move(active));
  addEventListener('resize', () => move(active));
})();
```
