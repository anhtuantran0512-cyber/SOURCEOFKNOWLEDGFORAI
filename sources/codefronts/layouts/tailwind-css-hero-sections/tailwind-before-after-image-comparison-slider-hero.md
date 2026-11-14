---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-before-after-image-comparison-slider-hero/"
title: "Before and After Image Comparison Slider Hero in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A native <input type=range> drives a single CSS custom property that wipes a clip-path between a scorched before landscape and a restored after one."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Before and After Image Comparison Slider Hero in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-before-after-image-comparison-slider-hero/

A native <input type=range> drives a single CSS custom property that wipes a clip-path between a scorched before landscape and a restored after one. Keyboard-accessible with a visible focus ring on the handle. Burnt orange, petrol blue and cream.
## HTML
```html
<section class="ths-09 grid w-full min-h-svh items-center gap-10 bg-ths09-bg px-5 py-12 font-ths09-sans text-ths09-ink sm:px-10 lg:grid-cols-[1.1fr_1fr] lg:gap-14" aria-label="Before and after comparison hero">
  <div data-ths09-stage style="--ths09-pos:50%" class="relative h-[min(68svh,560px)] min-h-[340px] overflow-hidden rounded-2xl border-4 border-ths09-ink shadow-[8px_8px_0_var(--color-ths09-rust)]">
    <div aria-hidden="true" class="absolute inset-0 bg-linear-to-b from-ths09-sky via-ths09-meadow to-ths09-field">
      <span class="absolute top-[16%] left-[70%] size-16 rounded-full bg-ths09-sun shadow-[0_0_60px_var(--color-ths09-sun)]"></span>
      <span class="absolute inset-x-0 bottom-[22%] h-[38%] bg-ths09-pine/70 [clip-path:polygon(0_70%,14%_30%,28%_62%,44%_18%,60%_58%,76%_26%,90%_52%,100%_34%,100%_100%,0_100%)]"></span>
      <span class="absolute inset-x-0 bottom-0 h-[36%] bg-ths09-pine [clip-path:polygon(0_40%,18%_10%,34%_46%,52%_0,70%_38%,86%_14%,100%_30%,100%_100%,0_100%)]"></span>
      <span class="absolute right-4 bottom-4 bg-ths09-ink px-2.5 py-1 font-ths09-mono text-[11px] font-bold tracking-[0.18em] text-ths09-bg">AFTER</span>
    </div>
    <div aria-hidden="true" class="absolute inset-0 bg-linear-to-b from-ths09-rust via-ths09-dune to-ths09-sand [clip-path:inset(0_calc(100%_-_var(--ths09-pos))_0_0)]">
      <span class="absolute top-[14%] left-[24%] size-14 rounded-full bg-ths09-bg shadow-[0_0_30px_rgb(247_236_217/0.5)]"></span>
      <span class="absolute inset-x-0 bottom-[22%] h-[38%] bg-ths09-clay/70 [clip-path:polygon(0_70%,14%_30%,28%_62%,44%_18%,60%_58%,76%_26%,90%_52%,100%_34%,100%_100%,0_100%)]"></span>
      <span class="absolute inset-x-0 bottom-0 h-[36%] bg-ths09-clay [clip-path:polygon(0_40%,18%_10%,34%_46%,52%_0,70%_38%,86%_14%,100%_30%,100%_100%,0_100%)]"></span>
      <span class="absolute bottom-4 left-4 bg-ths09-clay px-2.5 py-1 font-ths09-mono text-[11px] font-bold tracking-[0.18em] text-ths09-bg">BEFORE</span>
    </div>
    <input type="range" min="0" max="100" value="50" aria-label="Compare before and after" aria-valuetext="50 percent restored" class="peer absolute inset-0 z-30 m-0 size-full cursor-ew-resize opacity-0">
    <span aria-hidden="true" class="pointer-events-none absolute inset-y-0 left-(--ths09-pos) z-20 w-[3px] -translate-x-1/2 bg-ths09-bg shadow-[0_0_0_1px_var(--color-ths09-ink)] peer-focus-visible:[&>span]:ring-4 peer-focus-visible:[&>span]:ring-ths09-rust/60">
      <span class="absolute top-1/2 left-1/2 grid size-11 -translate-1/2 place-items-center rounded-full border-2 border-ths09-ink bg-ths09-bg text-sm font-bold text-ths09-ink shadow-lg">⇆</span>
    </span>
  </div>
  <div class="max-w-lg">
    <span class="font-ths09-mono text-[11px] font-bold tracking-[0.18em] text-ths09-rust">DRAG TO COMPARE</span>
    <h1 class="mt-4 font-ths09-serif text-[clamp(32px,4.6vw,52px)] leading-[1.06] font-bold tracking-[-0.01em] text-balance">Restoration, <em class="text-ths09-rust">one acre at a time.</em></h1>
    <p class="mt-5 text-base/relaxed text-ths09-body">We turn dust to forest in 18 months — proven on three continents.</p>
    <dl class="mt-7 grid grid-cols-3 gap-4 border-y border-ths09-ink/15 py-5">
      <div><dt class="text-xs text-ths09-body">Acres</dt><dd class="mt-1 font-ths09-serif text-2xl font-bold">41k</dd></div>
      <div><dt class="text-xs text-ths09-body">Trees</dt><dd class="mt-1 font-ths09-serif text-2xl font-bold">9.2M</dd></div>
      <div><dt class="text-xs text-ths09-body">Survival</dt><dd class="mt-1 font-ths09-serif text-2xl font-bold">87%</dd></div>
    </dl>
    <a href="#donate" class="mt-8 inline-flex min-h-12 items-center rounded-md bg-ths09-rust px-6 text-sm font-bold text-ths09-bg transition hover:bg-ths09-clay focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths09-rust motion-reduce:transition-none">Plant a tree →</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths09-bg: #f7ecd9;
  --color-ths09-bg: oklch(0.947 0.028 81.5);
  --color-ths09-ink: #2c4a4f;
  --color-ths09-ink: oklch(0.388 0.037 209.1);
  --color-ths09-body: #3f5e4c;
  --color-ths09-body: oklch(0.452 0.047 158.4);
  --color-ths09-rust: #b5501f;
  --color-ths09-rust: oklch(0.553 0.144 43.3);
  --color-ths09-clay: #8a3614;
  --color-ths09-clay: oklch(0.445 0.123 40.3);
  --color-ths09-dune: #e8a36e;
  --color-ths09-dune: oklch(0.771 0.107 57.9);
  --color-ths09-sand: #f0b87a;
  --color-ths09-sand: oklch(0.82 0.102 68.4);
  --color-ths09-sky: #87b8a8;
  --color-ths09-sky: oklch(0.743 0.057 172.5);
  --color-ths09-meadow: #b9c08f;
  --color-ths09-meadow: oklch(0.79 0.067 114.5);
  --color-ths09-field: #d6c69a;
  --color-ths09-field: oklch(0.829 0.061 90.4);
  --color-ths09-pine: #3f6450;
  --color-ths09-pine: oklch(0.469 0.054 159.8);
  --color-ths09-sun: #f7d875;
  --color-ths09-sun: oklch(0.888 0.124 92.4);
  --font-ths09-serif: 'Playfair Display', Georgia, serif;
  --font-ths09-sans: 'Geist', system-ui, sans-serif;
  --font-ths09-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-09 {
  width: 100%;
  min-height: 100svh;
}

[data-ths09-stage] {
  --ths09-pos: 50%;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ths09-stage]').forEach((stage) => {
    if (stage.dataset.wired) return;
    stage.dataset.wired = '1';
    const range = stage.querySelector('input[type="range"]');
    const update = () => {
      stage.style.setProperty('--ths09-pos', range.value + '%');
      range.setAttribute('aria-valuetext', range.value + ' percent restored');
    };
    range.addEventListener('input', update);
    update();
  });
})();
```
