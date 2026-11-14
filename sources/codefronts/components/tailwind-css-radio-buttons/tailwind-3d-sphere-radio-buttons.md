---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-3d-sphere-radio-buttons/"
title: "Tailwind 3D Sphere Radio Buttons"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "Radio options as glossy 3D orbs: layered radial gradients build each sphere, a specular highlight tracks the cursor (a tiny controller writes two custom…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Sphere Radio Buttons
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-3d-sphere-radio-buttons/

Radio options as glossy 3D orbs: layered radial gradients build each sphere, a specular highlight tracks the cursor (a tiny controller writes two custom properties), and the checked orb earns a slowly orbiting ring. Each orb's hue is one arbitrary property, [--c:oklch(…)], and the shading tokens use @theme inline so they can read it.
## HTML
```html
<section class="trb-09 w-full min-h-svh grid place-items-center bg-trb09-bg bg-[radial-gradient(130%_110%_at_50%_-10%,var(--color-trb09-top),transparent_70%)] px-6 py-14 font-trb09-sans text-trb09-ink" aria-label="Interactive 3D sphere radio buttons demo">
  <fieldset data-trb09-group>
    <legend class="text-center text-[26px] font-bold tracking-[-0.02em]">Pick your world</legend>
    <div class="mt-9 flex flex-wrap justify-center gap-10">
      <label class="group relative grid cursor-pointer justify-items-center gap-3.5 [--c:oklch(0.62_0.19_25)]">
        <input type="radio" name="trb-09" value="ember" class="sr-only" checked>
        <span data-trb09-orb aria-hidden="true" class="relative size-24 rounded-full bg-[radial-gradient(circle_at_32%_28%,color-mix(in_oklab,var(--c)_55%,white),var(--c)_46%,color-mix(in_oklab,var(--c)_45%,black)_88%)] shadow-trb09-orb transition-[scale,translate,box-shadow] duration-350 ease-trb09-spring before:absolute before:top-[14%] before:left-[18%] before:h-[22%] before:w-[30%] before:translate-x-[var(--hx,0px)] before:translate-y-[var(--hy,0px)] before:rounded-full before:bg-[radial-gradient(closest-side,rgb(255_255_255/0.85),transparent)] before:blur-[1px] before:transition-[translate] before:duration-150 before:content-[''] after:absolute after:-inset-3.5 after:rotate-20 after:rounded-full after:border-2 after:border-[color-mix(in_oklab,var(--c)_75%,white)] after:border-y-transparent after:opacity-0 after:transition-opacity after:content-[''] group-hover:-translate-y-1.5 group-has-checked:scale-107 group-has-checked:shadow-trb09-orb-on group-has-checked:after:animate-trb09-orbit group-has-checked:after:opacity-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-[18px] group-has-focus-visible:outline-white motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 motion-reduce:group-has-checked:after:animate-none"></span>
        <span class="grid justify-items-center"><span class="text-[15px] font-semibold text-trb09-mut transition-colors group-has-checked:text-white">Ember</span><span class="text-xs text-trb09-mut">Volcanic · Hard</span></span>
      </label>
      <label class="group relative grid cursor-pointer justify-items-center gap-3.5 [--c:oklch(0.62_0.15_230)]">
        <input type="radio" name="trb-09" value="tide" class="sr-only">
        <span data-trb09-orb aria-hidden="true" class="relative size-24 rounded-full bg-[radial-gradient(circle_at_32%_28%,color-mix(in_oklab,var(--c)_55%,white),var(--c)_46%,color-mix(in_oklab,var(--c)_45%,black)_88%)] shadow-trb09-orb transition-[scale,translate,box-shadow] duration-350 ease-trb09-spring before:absolute before:top-[14%] before:left-[18%] before:h-[22%] before:w-[30%] before:translate-x-[var(--hx,0px)] before:translate-y-[var(--hy,0px)] before:rounded-full before:bg-[radial-gradient(closest-side,rgb(255_255_255/0.85),transparent)] before:blur-[1px] before:transition-[translate] before:duration-150 before:content-[''] after:absolute after:-inset-3.5 after:rotate-20 after:rounded-full after:border-2 after:border-[color-mix(in_oklab,var(--c)_75%,white)] after:border-y-transparent after:opacity-0 after:transition-opacity after:content-[''] group-hover:-translate-y-1.5 group-has-checked:scale-107 group-has-checked:shadow-trb09-orb-on group-has-checked:after:animate-trb09-orbit group-has-checked:after:opacity-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-[18px] group-has-focus-visible:outline-white motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 motion-reduce:group-has-checked:after:animate-none"></span>
        <span class="grid justify-items-center"><span class="text-[15px] font-semibold text-trb09-mut transition-colors group-has-checked:text-white">Tide</span><span class="text-xs text-trb09-mut">Oceanic · Medium</span></span>
      </label>
      <label class="group relative grid cursor-pointer justify-items-center gap-3.5 [--c:oklch(0.68_0.16_145)]">
        <input type="radio" name="trb-09" value="moss" class="sr-only">
        <span data-trb09-orb aria-hidden="true" class="relative size-24 rounded-full bg-[radial-gradient(circle_at_32%_28%,color-mix(in_oklab,var(--c)_55%,white),var(--c)_46%,color-mix(in_oklab,var(--c)_45%,black)_88%)] shadow-trb09-orb transition-[scale,translate,box-shadow] duration-350 ease-trb09-spring before:absolute before:top-[14%] before:left-[18%] before:h-[22%] before:w-[30%] before:translate-x-[var(--hx,0px)] before:translate-y-[var(--hy,0px)] before:rounded-full before:bg-[radial-gradient(closest-side,rgb(255_255_255/0.85),transparent)] before:blur-[1px] before:transition-[translate] before:duration-150 before:content-[''] after:absolute after:-inset-3.5 after:rotate-20 after:rounded-full after:border-2 after:border-[color-mix(in_oklab,var(--c)_75%,white)] after:border-y-transparent after:opacity-0 after:transition-opacity after:content-[''] group-hover:-translate-y-1.5 group-has-checked:scale-107 group-has-checked:shadow-trb09-orb-on group-has-checked:after:animate-trb09-orbit group-has-checked:after:opacity-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-[18px] group-has-focus-visible:outline-white motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 motion-reduce:group-has-checked:after:animate-none"></span>
        <span class="grid justify-items-center"><span class="text-[15px] font-semibold text-trb09-mut transition-colors group-has-checked:text-white">Moss</span><span class="text-xs text-trb09-mut">Temperate · Easy</span></span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb09-bg: #0a0c14;
  --color-trb09-bg: oklch(0.16 0.015 270);
  --color-trb09-top: #1b2136;
  --color-trb09-top: oklch(0.25 0.04 270);
  --color-trb09-ink: #eef1fa;
  --color-trb09-ink: oklch(0.96 0.01 270);
  --color-trb09-mut: #a3abc4;
  --color-trb09-mut: oklch(0.75 0.03 270);
  --ease-trb09-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb09-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-trb09-orbit: trb09-orbit 4s linear infinite;

  @keyframes trb09-orbit {
    to {
      rotate: 380deg;
    }
  }
}
/* inline: these tokens read the per-orb --c, so they must be written into the utility, not :root. */

@theme inline {
  --shadow-trb09-orb: inset -14px -16px 28px rgb(0 0 0 / 0.45), inset 6px 8px 16px rgb(255 255 255 / 0.18), 0 18px 34px -14px color-mix(in oklab, var(--c) 55%, transparent);
  --shadow-trb09-orb-on: inset -14px -16px 28px rgb(0 0 0 / 0.45), inset 6px 8px 16px rgb(255 255 255 / 0.18), 0 24px 44px -14px color-mix(in oklab, var(--c) 75%, transparent);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-09 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const init = () => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches || !matchMedia('(pointer: fine)').matches) return;
    const PULL = 10;
    document.querySelectorAll('[data-trb09-group]').forEach((group) => {
      if (group.dataset.wired) return;
      group.dataset.wired = '1';
      group.querySelectorAll('[data-trb09-orb]').forEach((orb) => {
        const opt = orb.closest('label');
        opt.addEventListener('pointermove', (e) => {
          const r = orb.getBoundingClientRect();
          orb.style.setProperty('--hx', (((e.clientX - r.left) / r.width - 0.5) * PULL).toFixed(1) + 'px');
          orb.style.setProperty('--hy', (((e.clientY - r.top) / r.height - 0.5) * PULL).toFixed(1) + 'px');
        }, { passive: true });
        opt.addEventListener('pointerleave', () => { orb.style.setProperty('--hx', '0px'); orb.style.setProperty('--hy', '0px'); });
      });
    });
  };
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', init) : init();
})();
```
