---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-animated-3-line-to-x-hamburger-icon-toggle/"
title: "Tailwind Animated 3-Line to X Hamburger Icon Toggle"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Four production-grade line-to-X morphs on one stage &mdash; Spin, Squeeze, Arrow and Drop &mdash; and the port deletes the variant classes entirely."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated 3-Line to X Hamburger Icon Toggle
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-animated-3-line-to-x-hamburger-icon-toggle/

Four production-grade line-to-X morphs on one stage &mdash; Spin, Squeeze, Arrow and Drop &mdash; and the port deletes the variant classes entirely. There is no .spin or .squeeze rule: each tile is a group whose three bars carry their own end states as group-aria-pressed: utilities, so a variant is now a class list you copy rather than a stylesheet block you maintain.
## HTML
```html
<section class="thb-03 w-full min-h-svh bg-thb03-bg font-thb03-sans text-thb03-ink px-5 py-9" aria-label="Animated hamburger to X icon variants demo">
  <div class="p-6 rounded-[20px] border border-thb03-edge bg-thb03-bg bg-[radial-gradient(100%_90%_at_50%_-20%,oklch(0.26_0.05_285/0.7),transparent_60%)]">
    <header class="flex items-baseline justify-between gap-3 flex-wrap mb-5">
      <h2 class="text-base font-semibold tracking-[-0.01em]">Line &rarr; X morphs</h2>
      <span class="text-[11.5px] text-thb03-mut">click a tile &middot; real aria-pressed buttons</span>
    </header>
    <div class="grid grid-cols-[repeat(auto-fit,minmax(min(150px,100%),1fr))] gap-3.5">
      <figure class="flex flex-col items-center gap-3">
        <button type="button" aria-pressed="false" aria-label="Toggle spin morph demo" class="group w-full aspect-[1.25] grid place-items-center rounded-2xl border border-thb03-edge bg-linear-[165deg,color-mix(in_oklch,var(--color-thb03-card)_88%,white),var(--color-thb03-card)_60%] text-thb03-ink cursor-pointer transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb03-acc)_55%,var(--color-thb03-edge))] focus-visible:outline-2 focus-visible:outline-thb03-acc focus-visible:outline-offset-3 aria-pressed:border-thb03-acc aria-pressed:text-thb03-acc motion-reduce:transition-none">
          <span class="relative block w-5.5 h-4 transition-[rotate] duration-450 ease-thb03out group-aria-pressed:rotate-180 motion-reduce:transition-none" aria-hidden="true">
            <i class="absolute left-0 top-0 w-5.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 ease-thb03 group-aria-pressed:translate-y-[7px] group-aria-pressed:rotate-45 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[7px] w-5.5 h-0.5 rounded-sm bg-current transition-[opacity,scale] duration-250 ease-thb03 group-aria-pressed:opacity-0 group-aria-pressed:scale-x-0 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-3.5 w-5.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 ease-thb03 group-aria-pressed:-translate-y-[7px] group-aria-pressed:-rotate-45 motion-reduce:transition-none"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[13px] font-semibold">Spin</b><code class="font-thb03-mono text-[10.5px] text-thb03-mut">rotate 180&deg; &middot; fold 45&deg;</code></figcaption>
      </figure>
      <figure class="flex flex-col items-center gap-3">
        <button type="button" aria-pressed="false" aria-label="Toggle squeeze morph demo" class="group w-full aspect-[1.25] grid place-items-center rounded-2xl border border-thb03-edge bg-linear-[165deg,color-mix(in_oklch,var(--color-thb03-card)_88%,white),var(--color-thb03-card)_60%] text-thb03-ink cursor-pointer transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb03-acc)_55%,var(--color-thb03-edge))] focus-visible:outline-2 focus-visible:outline-thb03-acc focus-visible:outline-offset-3 aria-pressed:border-thb03-acc aria-pressed:text-thb03-acc motion-reduce:transition-none">
          <span class="relative block w-5.5 h-4" aria-hidden="true">
            <i class="absolute left-0 top-0 w-5.5 h-0.5 rounded-sm bg-current [transition:translate_.2s_cubic-bezier(.55,0,.55,1),rotate_.25s_var(--ease-thb03)_.18s,opacity_.15s_.08s] group-aria-pressed:translate-y-[7px] group-aria-pressed:rotate-45 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[7px] w-5.5 h-0.5 rounded-sm bg-current [transition:opacity_.15s_.08s] group-aria-pressed:opacity-0 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-3.5 w-5.5 h-0.5 rounded-sm bg-current [transition:translate_.2s_cubic-bezier(.55,0,.55,1),rotate_.25s_var(--ease-thb03)_.18s,opacity_.15s_.08s] group-aria-pressed:-translate-y-[7px] group-aria-pressed:-rotate-45 motion-reduce:transition-none"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[13px] font-semibold">Squeeze</b><code class="font-thb03-mono text-[10.5px] text-thb03-mut">converge &rarr; rotate, 2 beats</code></figcaption>
      </figure>
      <figure class="flex flex-col items-center gap-3">
        <button type="button" aria-pressed="false" aria-label="Toggle arrow morph demo" class="group w-full aspect-[1.25] grid place-items-center rounded-2xl border border-thb03-edge bg-linear-[165deg,color-mix(in_oklch,var(--color-thb03-card)_88%,white),var(--color-thb03-card)_60%] text-thb03-ink cursor-pointer transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb03-acc)_55%,var(--color-thb03-edge))] focus-visible:outline-2 focus-visible:outline-thb03-acc focus-visible:outline-offset-3 aria-pressed:border-thb03-acc aria-pressed:text-thb03-acc motion-reduce:transition-none">
          <span class="relative block w-5.5 h-4" aria-hidden="true">
            <i class="absolute left-0 top-0 w-5.5 h-0.5 rounded-sm bg-current origin-left transition-[translate,rotate,scale] duration-300 ease-thb03 group-aria-pressed:scale-x-[0.62] group-aria-pressed:-rotate-40 group-aria-pressed:translate-y-px motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[7px] w-5.5 h-0.5 rounded-sm bg-current origin-left transition-[scale] duration-300 ease-thb03 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-3.5 w-5.5 h-0.5 rounded-sm bg-current origin-left transition-[translate,rotate,scale] duration-300 ease-thb03 group-aria-pressed:scale-x-[0.62] group-aria-pressed:rotate-40 group-aria-pressed:-translate-y-px motion-reduce:transition-none"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[13px] font-semibold">Arrow</b><code class="font-thb03-mono text-[10.5px] text-thb03-mut">scale-x .62 &middot; origin-left</code></figcaption>
      </figure>
      <figure class="flex flex-col items-center gap-3">
        <button type="button" aria-pressed="false" aria-label="Toggle drop morph demo" class="group w-full aspect-[1.25] grid place-items-center rounded-2xl border border-thb03-edge bg-linear-[165deg,color-mix(in_oklch,var(--color-thb03-card)_88%,white),var(--color-thb03-card)_60%] text-thb03-ink cursor-pointer transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb03-acc)_55%,var(--color-thb03-edge))] focus-visible:outline-2 focus-visible:outline-thb03-acc focus-visible:outline-offset-3 aria-pressed:border-thb03-acc aria-pressed:text-thb03-acc motion-reduce:transition-none">
          <span class="relative block w-5.5 h-4" aria-hidden="true">
            <i class="absolute left-0 top-0 w-5.5 h-0.5 rounded-sm bg-current [transition:translate_.32s_cubic-bezier(.5,0,.9,.6),rotate_.3s_var(--ease-thb03)_.16s,opacity_.26s_ease-in] group-aria-pressed:translate-y-[7px] group-aria-pressed:rotate-45 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[7px] w-5.5 h-0.5 rounded-sm bg-current [transition:translate_.32s_cubic-bezier(.5,0,.9,.6),rotate_.3s_var(--ease-thb03)_.16s,opacity_.26s_ease-in] group-aria-pressed:translate-x-[3px] group-aria-pressed:translate-y-4 group-aria-pressed:rotate-[14deg] group-aria-pressed:opacity-0 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-3.5 w-5.5 h-0.5 rounded-sm bg-current [transition:translate_.32s_cubic-bezier(.5,0,.9,.6),rotate_.3s_var(--ease-thb03)_.16s,opacity_.26s_ease-in] group-aria-pressed:-translate-y-[7px] group-aria-pressed:-rotate-45 motion-reduce:transition-none"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[13px] font-semibold">Drop</b><code class="font-thb03-mono text-[10.5px] text-thb03-mut">mid falls &middot; outers cross late</code></figcaption>
      </figure>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb03-bg: #23252f;
  --color-thb03-bg: oklch(0.17 0.02 275);
  --color-thb03-card: #2f3140;
  --color-thb03-card: oklch(0.22 0.025 275);
  --color-thb03-edge: #454858;
  --color-thb03-edge: oklch(0.3 0.03 275);
  --color-thb03-ink: #f0f0f4;
  --color-thb03-ink: oklch(0.95 0.008 275);
  --color-thb03-mut: #9a9daa;
  --color-thb03-mut: oklch(0.65 0.02 275);
  --color-thb03-acc: #57d3a4;
  --color-thb03-acc: oklch(0.75 0.15 165);
  --font-thb03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb03: cubic-bezier(0.2, 0.7, 0.2, 1);
  --ease-thb03out: cubic-bezier(0.3, 0.9, 0.35, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-03 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-03 button[aria-pressed]').forEach(function (btn) {
    if (btn.dataset.bound) return; btn.dataset.bound = '1';
    btn.addEventListener('click', function () {
      btn.setAttribute('aria-pressed', String(btn.getAttribute('aria-pressed') !== 'true'));
    });
  });
})();
```
