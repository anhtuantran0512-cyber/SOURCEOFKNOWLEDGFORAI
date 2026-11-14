---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-cursor-spotlight-glow-button/"
title: "Tailwind Cursor Spotlight Glow Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A sophisticated dark CTA with a soft circle of light that follows the cursor across its surface &mdash; the button appears lit by a moving spotlight."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cursor Spotlight Glow Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-cursor-spotlight-glow-button/

A sophisticated dark CTA with a soft circle of light that follows the cursor across its surface &mdash; the button appears lit by a moving spotlight. Design B applies the same tracked gradient to the BORDER via a mask-composite ring, which is the part worth stealing.
## HTML
```html
<div class="tbh-32-group w-full min-h-svh flex flex-wrap">
<section class="tbh-32a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh32-sans bg-tbh32a-stage" aria-label="Cursor spotlight button">
  <button id="tbh-32a-btn" type="button" class="relative isolate overflow-hidden cursor-pointer rounded-xl border border-white/15 px-[42px] py-[18px] text-base font-bold text-tbh32a-ink bg-tbh32a-base transition-colors duration-300 hover:border-white/30 focus-visible:border-white/30 focus-visible:outline-3 focus-visible:outline-tbh32a-light focus-visible:outline-offset-4 before:content-[''] before:absolute before:inset-0 before:z-0 before:opacity-[var(--lit,0)] before:bg-[radial-gradient(160px_160px_at_var(--mx,50%)_var(--my,50%),color-mix(in_oklab,var(--color-tbh32a-light)_55%,transparent),transparent_60%)] before:transition-opacity before:duration-300 motion-reduce:before:transition-none">
    <span class="relative z-[1]">Explore features</span>
  </button>
</section>
<section class="tbh-32b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh32-sans bg-tbh32b-stage" aria-label="Cursor glow border button">
  <button id="tbh-32b-btn" type="button" class="relative isolate cursor-pointer rounded-xl border border-white/12 px-[42px] py-[18px] text-base font-bold text-tbh32b-ink bg-tbh32b-base focus-visible:outline-3 focus-visible:outline-tbh32b-glow focus-visible:outline-offset-4 before:content-[''] before:absolute before:-inset-px before:z-0 before:rounded-[13px] before:p-px before:opacity-[var(--lit,0)] before:bg-[radial-gradient(120px_120px_at_var(--mx,50%)_var(--my,50%),var(--color-tbh32b-glow),transparent_70%)] before:[mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask-composite:exclude] before:transition-opacity before:duration-300 motion-reduce:before:transition-none">
    <span class="relative z-[1]">View pricing</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh32a-base: #14131c;
  --color-tbh32a-base: oklch(0.19 0.02 285);
  --color-tbh32a-stage: #08070d;
  --color-tbh32a-stage: oklch(0.11 0.01 285);
  --color-tbh32a-ink: #f4f3ff;
  --color-tbh32a-ink: oklch(0.96 0.01 285);
  --color-tbh32a-light: #8c78ff;
  --color-tbh32a-light: oklch(0.68 0.19 285);
  --color-tbh32b-base: #0f1a1c;
  --color-tbh32b-base: oklch(0.19 0.02 195);
  --color-tbh32b-stage: #060d0e;
  --color-tbh32b-stage: oklch(0.11 0.012 195);
  --color-tbh32b-ink: #eafffb;
  --color-tbh32b-ink: oklch(0.97 0.02 175);
  --color-tbh32b-glow: #5fdde8;
  --color-tbh32b-glow: oklch(0.75 0.15 190);
  --font-tbh32-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Stays CSS: the -webkit- mask pair for design B's border ring. The prefixed form needs the
   'xor' keyword where the standard form takes 'exclude', so it cannot be one utility. */

.tbh-32b button::before {
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
}

.tbh-32-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-32a,
.tbh-32b {
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const light = id => {
    const btn = document.querySelector(id); if (!btn) return;
    const set = (mx, my, lit) => {
      btn.style.setProperty('--mx', mx);
      btn.style.setProperty('--my', my);
      btn.style.setProperty('--lit', lit);
    };
    btn.addEventListener('pointermove', e => {
      const r = btn.getBoundingClientRect();
      set((e.clientX - r.left) + 'px', (e.clientY - r.top) + 'px', '1');
    });
    btn.addEventListener('pointerleave', () => btn.style.setProperty('--lit', '0'));
    btn.addEventListener('focus', () => set('50%', '50%', '1'));
    btn.addEventListener('blur', () => btn.style.setProperty('--lit', '0'));
  };
  light('#tbh-32a-btn');
  light('#tbh-32b-btn');
})();
```
