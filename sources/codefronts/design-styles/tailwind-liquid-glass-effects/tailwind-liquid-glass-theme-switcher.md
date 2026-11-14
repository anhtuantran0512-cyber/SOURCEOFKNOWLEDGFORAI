---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-theme-switcher/"
title: "Tailwind Liquid Glass Theme Switcher"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A dark/light toggle that releases a liquid glass ripple across the scene as it flips."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Theme Switcher
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-theme-switcher/

A dark/light toggle that releases a liquid glass ripple across the scene as it flips. In the port the entire theme lives in six custom properties re-pointed by one data-theme rule, so every utility in the markup &mdash; bg-lgt06-surface, text-lgt06-fg, border-lgt06-rim &mdash; changes meaning at once and not a single class is duplicated per theme.
## HTML
```html
<section id="lgt-06-root" data-theme="dark" class="lgt-06 grid w-full min-h-svh place-items-center bg-lgt06-bg p-15 font-lgt06-sans" aria-label="Tailwind liquid glass theme switcher">
  <div class="relative w-[min(400px,92vw)] rounded-[26px] border border-lgt06-rim bg-lgt06-surface p-8.5 text-lgt06-fg backdrop-blur-[20px] backdrop-saturate-170 shadow-[inset_0_1px_0_var(--color-lgt06-rim),0_30px_60px_-30px_rgba(0,0,0,.5)]">
    <h3 id="lgt-06-title" class="mb-2 text-[26px] font-extrabold">Good evening</h3>
    <p class="mb-5.5 text-[15px] leading-relaxed text-lgt06-muted">Toggle the switch &mdash; a liquid glass ripple sweeps the new theme across the scene.</p>
    <button id="lgt-06-switch" type="button" role="switch" aria-checked="false" aria-label="Toggle light mode" class="group relative h-9.5 w-19 cursor-pointer rounded-full border border-lgt06-rim bg-lgt06-track p-0 backdrop-blur-[8px] shadow-[inset_0_2px_8px_rgba(0,0,0,.3)] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-lgt06-fg">
      <span id="lgt-06-knob" class="absolute top-0.75 left-0.75 grid size-8 place-items-center rounded-full bg-linear-to-b from-white to-white/70 shadow-[0_4px_10px_rgba(0,0,0,.35),inset_0_1px_0_#fff] transition-[left] duration-400 ease-lgt06 group-aria-checked:left-[41px] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute text-base text-lgt06-moon opacity-100 transition-opacity duration-300 group-aria-checked:opacity-0">&#9790;</span>
        <span aria-hidden="true" class="absolute text-base text-lgt06-sun opacity-0 transition-opacity duration-300 group-aria-checked:opacity-100">&#9728;</span>
      </span>
    </button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt06-bg: #12101f;
  --color-lgt06-surface: rgb(255 255 255 / 0.12);
  --color-lgt06-fg: #f2f0fa;
  --color-lgt06-muted: rgb(255 255 255 / 0.75);
  --color-lgt06-rim: rgb(255 255 255 / 0.35);
  --color-lgt06-track: rgb(120 110 160 / 0.5);
  --color-lgt06-moon: #3a3560;
  --color-lgt06-sun: #e0a020;
  --font-lgt06-sans: 'Manrope', system-ui, sans-serif;
  --ease-lgt06: cubic-bezier(0.5, -0.3, 0.4, 1.4);
  --animate-lgt06-ripple: lgt-06-ripple 0.6s ease-out forwards;
}
/* One rule re-points the whole palette. Every utility in the markup reads these,
   so the entire scene flips with a single attribute and no duplicated classes. */

.lgt-06[data-theme="light"] {
  --color-lgt06-bg: #dfe7f7;
  --color-lgt06-surface: rgb(255 255 255 / 0.55);
  --color-lgt06-fg: #161425;
  --color-lgt06-muted: rgb(30 28 50 / 0.7);
  --color-lgt06-rim: rgb(255 255 255 / 0.8);
  --color-lgt06-track: rgb(255 255 255 / 0.6);
}

@keyframes lgt-06-ripple {
  from {
    transform: scale(0);
    opacity: 0.9;
  }

  to {
    transform: scale(1);
    opacity: 0;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lgt-06-root');
  const sw = root.querySelector('#lgt-06-switch');
  const knob = root.querySelector('#lgt-06-knob');
  const title = root.querySelector('#lgt-06-title');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const apply = () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    sw.setAttribute('aria-checked', String(next === 'light'));
    title.textContent = next === 'light' ? 'Good morning' : 'Good evening';
  };

  const ripple = () => {
    const r = knob.getBoundingClientRect();
    const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
    const far = Math.hypot(Math.max(cx, innerWidth - cx), Math.max(cy, innerHeight - cy));
    const el = document.createElement('span');
    el.className = 'fixed z-9999 pointer-events-none rounded-full border border-lgt06-rim bg-lgt06-surface backdrop-blur-[26px] backdrop-saturate-180 animate-lgt06-ripple';
    el.style.left = (cx - far) + 'px';
    el.style.top = (cy - far) + 'px';
    el.style.width = el.style.height = (far * 2) + 'px';
    root.appendChild(el);
    el.addEventListener('animationend', () => el.remove(), { once: true });
  };

  sw.addEventListener('click', () => {
    if (reduce) { apply(); return; }
    if (document.startViewTransition) { document.startViewTransition(apply); return; }
    ripple();
    setTimeout(apply, 180);
  });
})();
```
