---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-magnetic-cursor-pull-hover-effect/"
title: "Tailwind Magnetic Cursor Pull Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four elements that lean toward the cursor when it comes near and spring back when it leaves — a primary CTA, an outline button, a round icon and a pill link."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magnetic Cursor Pull Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-magnetic-cursor-pull-hover-effect/

Four elements that lean toward the cursor when it comes near and spring back when it leaves — a primary CTA, an outline button, a round icon and a pill link. CSS owns the spring, JS owns only the live translate, and every element stays a real control.
## HTML
```html
<section class="thv-30 w-full min-h-svh bg-thv30-bg font-thv30-sans px-8 py-12 flex flex-col items-center gap-8">
  <p class="text-[0.72rem] tracking-[0.15em] uppercase text-thv30-dim">Magnetic Cursor Pull — 4 Types</p>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(220px,1fr))] gap-14 place-items-center p-8 w-full max-w-[720px]">
    <div class="flex flex-col items-center gap-4">
      <button type="button" data-strength="0.35" data-radius="80" class="thv30-magnet inline-flex items-center justify-center min-h-11 px-9 py-3.5 rounded-full border-0 bg-thv30-acc text-base font-semibold tracking-[0.02em] text-white cursor-pointer shadow-[0_6px_28px_rgba(91,79,207,.4)] [will-change:transform] transition-transform duration-450 ease-[cubic-bezier(.23,1,.32,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv30-lilac motion-reduce:transition-none">
        <span data-strength="0.55" class="thv30-magnet-inner inline-block pointer-events-none [will-change:transform] transition-transform duration-450 ease-[cubic-bezier(.23,1,.32,1)] motion-reduce:transition-none">Get Started</span>
      </button>
      <span class="text-[0.68rem] tracking-[0.1em] uppercase text-thv30-dim">Primary CTA</span>
    </div>
    <div class="flex flex-col items-center gap-4">
      <button type="button" data-strength="0.4" data-radius="90" class="thv30-magnet inline-flex items-center justify-center min-h-11 px-9 py-3.5 rounded-full border-2 border-thv30-acc bg-transparent text-base font-semibold tracking-[0.02em] text-thv30-lilac cursor-pointer [will-change:transform] transition-[transform,box-shadow] duration-450 ease-[cubic-bezier(.23,1,.32,1)] hover:shadow-[0_6px_28px_rgba(91,79,207,.25)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv30-lilac motion-reduce:transition-none">
        <span data-strength="0.6" class="thv30-magnet-inner inline-block pointer-events-none [will-change:transform] transition-transform duration-450 ease-[cubic-bezier(.23,1,.32,1)] motion-reduce:transition-none">Learn More</span>
      </button>
      <span class="text-[0.68rem] tracking-[0.1em] uppercase text-thv30-dim">Outline Button</span>
    </div>
    <div class="flex flex-col items-center gap-4">
      <button type="button" aria-label="Add to favourites" data-strength="0.5" data-radius="70" class="thv30-magnet grid place-items-center w-16 h-16 rounded-full border-0 text-2xl text-white cursor-pointer bg-[linear-gradient(135deg,#7c6af7,#f764a8)] shadow-[0_6px_24px_rgba(124,106,247,.4)] [will-change:transform] transition-transform duration-450 ease-[cubic-bezier(.23,1,.32,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv30-lilac motion-reduce:transition-none">
        <span aria-hidden="true" data-strength="0.75" class="thv30-magnet-inner inline-block pointer-events-none [will-change:transform] transition-transform duration-450 ease-[cubic-bezier(.23,1,.32,1)] motion-reduce:transition-none">★</span>
      </button>
      <span class="text-[0.68rem] tracking-[0.1em] uppercase text-thv30-dim">Icon Pull</span>
    </div>
    <div class="flex flex-col items-center gap-4">
      <a href="#" data-strength="0.3" data-radius="100" class="thv30-magnet inline-flex items-center min-h-11 px-7 py-2.5 rounded-full border border-white/12 bg-white/6 backdrop-blur-[6px] text-[0.9rem] text-thv30-ink no-underline cursor-pointer [will-change:transform] transition-[transform,background-color,border-color,color] duration-450 ease-[cubic-bezier(.23,1,.32,1)] hover:bg-white/10 hover:border-white/25 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv30-lilac motion-reduce:transition-none">
        <span data-strength="0.5" class="thv30-magnet-inner inline-block pointer-events-none [will-change:transform] transition-transform duration-450 ease-[cubic-bezier(.23,1,.32,1)] motion-reduce:transition-none">View Project →</span>
      </a>
      <span class="text-[0.68rem] tracking-[0.1em] uppercase text-thv30-dim">Pill Link</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv30-bg: #090912;
  --color-thv30-bg: oklch(0.12 0.02 285);
  --color-thv30-ink: #cfcfd8;
  --color-thv30-ink: oklch(0.84 0.01 285);
  --color-thv30-dim: #8a8a98;
  --color-thv30-dim: oklch(0.64 0.01 285);
  --color-thv30-acc: #5b4fcf;
  --color-thv30-acc: oklch(0.5 0.2 285);
  --color-thv30-lilac: #a99ef7;
  --color-thv30-lilac: oklch(0.74 0.13 290);
  --font-thv30-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-30 {
  width: 100%;
  min-height: 100svh;
}

.thv-30 ::selection {
  background: var(--color-thv30-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  if (window.matchMedia('(pointer: coarse)').matches) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const magnets = document.querySelectorAll('.thv30-magnet');

  function reset(el) {
    el.style.transform = '';
    const inner = el.querySelector('.thv30-magnet-inner');
    if (inner) inner.style.transform = '';
  }

  function handleMove(e, el) {
    const rect = el.getBoundingClientRect();
    const dx = e.clientX - (rect.left + rect.width / 2);
    const dy = e.clientY - (rect.top + rect.height / 2);
    const dist = Math.hypot(dx, dy);
    const radius = parseFloat(el.dataset.radius) || 80;
    const strength = parseFloat(el.dataset.strength) || 0.35;

    if (dist >= radius) { reset(el); return; }

    const pull = 1 - dist / radius;
    el.style.transform = 'translate(' + dx * strength * pull + 'px,' + dy * strength * pull + 'px)';

    const inner = el.querySelector('.thv30-magnet-inner');
    if (inner) {
      const is = parseFloat(inner.dataset.strength) || 0.5;
      inner.style.transform = 'translate(' + dx * is * pull + 'px,' + dy * is * pull + 'px)';
    }
  }

  magnets.forEach((el) => {
    document.addEventListener('mousemove', (e) => handleMove(e, el));
    el.addEventListener('mouseleave', () => reset(el));
    el.addEventListener('blur', () => reset(el));
  });
})();
```
