---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-gooey-liquid-morphing-switch-svg-filter/"
title: "Tailwind Gooey Liquid Morphing Switch with SVG Filter"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The blob that necks and snaps: an inline feGaussianBlur + feColorMatrix chain fuses a thumb with a trailing echo, and the only thing Tailwind has to do is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gooey Liquid Morphing Switch with SVG Filter
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-gooey-liquid-morphing-switch-svg-filter/

The blob that necks and snaps: an inline feGaussianBlur + feColorMatrix chain fuses a thumb with a trailing echo, and the only thing Tailwind has to do is move them &mdash; has-checked: on the track, a delay-[90ms] on the echo, and the filter draws the liquid between them.
## HTML
```html
<section class="ttg-04 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg04-bg font-ttg04-sans" aria-label="Gooey liquid morphing switch">
  <svg width="0" height="0" aria-hidden="true" class="absolute">
    <defs><filter id="ttg04-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="g"/><feComposite in="SourceGraphic" in2="g" operator="atop"/></filter></defs>
  </svg>
  <label for="ttg-04-sw" class="flex items-center gap-8 px-7 py-5 rounded-3xl cursor-pointer bg-ttg04-card border border-ttg04-edge">
    <span class="flex flex-col gap-0.5">
      <span class="text-[15.5px] font-semibold text-ttg04-ink">Liquid mode</span>
      <span class="text-[12.5px] text-ttg04-mute">Metaball transitions between views</span>
    </span>
    <span class="relative shrink-0 w-24 h-12 rounded-[26px] bg-ttg04-track shadow-[inset_0_3px_8px_oklch(0.15_0.03_300/0.6)] has-checked:[&_.ttg04-blob]:translate-x-12 has-checked:[&_.ttg04-echo]:translate-x-12">
      <span aria-hidden="true" class="absolute inset-0 pointer-events-none [filter:url(#ttg04-goo)]">
        <i class="ttg04-blob absolute top-2 left-2 w-8 h-8 rounded-full bg-ttg04-goo transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:duration-200"></i>
        <i class="ttg04-echo absolute top-2 left-2 w-8 h-8 rounded-full bg-ttg04-goo scale-[0.86] transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] delay-[90ms] motion-reduce:duration-200 motion-reduce:delay-0"></i>
      </span>
      <input type="checkbox" id="ttg-04-sw" role="switch" class="appearance-none absolute inset-0 w-full h-full rounded-[26px] bg-transparent cursor-pointer z-10 focus-visible:outline-3 focus-visible:outline-ttg04-goo focus-visible:outline-offset-4">
    </span>
  </label>
  <p class="font-ttg04-mono text-[11px] tracking-[0.14em] uppercase text-ttg04-mute">Watch the drop neck &amp; snap</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg04-bg: #16111f;
  --color-ttg04-bg: oklch(0.19 0.03 300);
  --color-ttg04-card: #1e1730;
  --color-ttg04-card: oklch(0.24 0.04 300);
  --color-ttg04-edge: #2f2547;
  --color-ttg04-edge: oklch(0.32 0.05 300);
  --color-ttg04-track: #241b38;
  --color-ttg04-track: oklch(0.27 0.05 300);
  --color-ttg04-goo: #e878b8;
  --color-ttg04-goo: oklch(0.72 0.19 340);
  --color-ttg04-ink: #ded5f0;
  --color-ttg04-ink: oklch(0.9 0.03 300);
  --color-ttg04-mute: #9b8fba;
  --color-ttg04-mute: oklch(0.68 0.05 300);
  --font-ttg04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg04-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.ttg-04 {
  width: 100%;
  min-height: 100svh;
}

.ttg-04 input[type="checkbox"] {
  -webkit-appearance: none;
}
/* The scale on the echo blob must survive its translate; Tailwind composes both through
   its own transform variables, but the filtered layer is re-rasterised each frame in
   Safari, so pin it to its own compositing layer. */

.ttg-04 .ttg04-blob,
.ttg-04 .ttg04-echo {
  will-change: transform;
}
```
