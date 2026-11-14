---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-dynamic-island-morphing-nav/"
title: "Tailwind Dynamic Island Morphing Nav"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A glass pill that morphs between a slim capsule and a full navigation panel &mdash; and the clearest demonstration of why data-* variants beat class toggling."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dynamic Island Morphing Nav
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-dynamic-island-morphing-nav/

A glass pill that morphs between a slim capsule and a full navigation panel &mdash; and the clearest demonstration of why data-* variants beat class toggling. The script sets data-state to idle or expanded and manages ARIA; every geometric consequence, including the panel's delayed fade, is declared in the markup next to the resting value.
## HTML
```html
<section class="nbtw-06 relative flex flex-col items-center w-full min-h-svh pt-15 px-5 font-nb06-sans bg-[radial-gradient(circle_at_30%_30%,#0f3d2e,#05100b_70%),url('https://picsum.photos/seed/nb06/1000/700')] bg-center bg-cover [background-blend-mode:overlay]" aria-label="Dynamic Island navigation demo">
  <p class="mb-5 text-sm text-white/75">Tap the island to morph it open ↑</p>
  <div class="group relative overflow-hidden w-46 h-[46px] rounded-full isolate bg-[color-mix(in_oklab,black_40%,transparent)] border border-white/[0.22] shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_24px_50px_-22px_rgba(0,0,0,.8)] backdrop-blur-[28px] backdrop-saturate-[1.6] transition-[width,height,border-radius] duration-[550ms] ease-nb06 data-[state=expanded]:w-75 data-[state=expanded]:h-38 data-[state=expanded]:rounded-[30px] motion-reduce:transition-none" id="nbtw-06-island" data-state="idle">
    <button class="absolute top-0 left-0 z-[2] flex items-center justify-center gap-2.5 w-full h-[46px] border-0 bg-transparent text-white text-[15px] font-bold leading-none cursor-pointer focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" id="nbtw-06-trigger" type="button" aria-expanded="false" aria-controls="nbtw-06-panel">
      <span class="flex-none size-[11px] rounded-full bg-nb06-accent shadow-[0_0_12px_var(--color-nb06-accent)] animate-nb06-pulse motion-reduce:animate-none" aria-hidden="true"></span>
      <span class="inline-block leading-none">Lumen</span>
    </button>
    <div class="absolute inset-x-0 top-[46px] bottom-0 grid grid-cols-2 gap-2 px-4 pb-4 opacity-0 pointer-events-none transition-opacity duration-200 group-data-[state=expanded]:opacity-100 group-data-[state=expanded]:pointer-events-auto group-data-[state=expanded]:duration-300 group-data-[state=expanded]:delay-200 motion-reduce:transition-none" id="nbtw-06-panel" role="group" aria-label="Quick navigation">
      <a class="flex items-center justify-center min-h-10 rounded-xl no-underline text-white text-sm font-semibold bg-white/10 border border-white/[0.16] transition-colors duration-200 hover:bg-white/20 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-nb06-accent aria-[current=page]:text-[#04120b]" href="#nbtw-06" aria-current="page">Home</a>
      <a class="flex items-center justify-center min-h-10 rounded-xl no-underline text-white text-sm font-semibold bg-white/10 border border-white/[0.16] transition-colors duration-200 hover:bg-white/20 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-06">Search</a>
      <a class="flex items-center justify-center min-h-10 rounded-xl no-underline text-white text-sm font-semibold bg-white/10 border border-white/[0.16] transition-colors duration-200 hover:bg-white/20 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-06">Alerts</a>
      <a class="flex items-center justify-center min-h-10 rounded-xl no-underline text-white text-sm font-semibold bg-white/10 border border-white/[0.16] transition-colors duration-200 hover:bg-white/20 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-06">You</a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-nb06-accent: #3fd18b;
  --color-nb06-accent: oklch(0.7 0.18 150);
  --font-nb06-sans: system-ui, 'Segoe UI', sans-serif;
  --ease-nb06: cubic-bezier(0.34, 1.4, 0.5, 1);
  --animate-nb06-pulse: nb06-pulse 2.4s ease-in-out infinite;
}

@keyframes nb06-pulse {
  50% {
    transform: scale(1.35);
    opacity: 0.6;
  }
}
```

## JavaScript
```js
(() => {
  const island = document.querySelector('#nbtw-06-island');
  const trigger = document.querySelector('#nbtw-06-trigger');
  const panel = document.querySelector('#nbtw-06-panel');
  if (!island || !trigger || !panel) return;
  const set = (open) => {
    island.dataset.state = open ? 'expanded' : 'idle';
    trigger.setAttribute('aria-expanded', String(open));
    if (open) panel.querySelector('a').focus();
  };
  trigger.addEventListener('click', () => set(island.dataset.state !== 'expanded'));
  island.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { set(false); trigger.focus(); }
  });
})();
```
