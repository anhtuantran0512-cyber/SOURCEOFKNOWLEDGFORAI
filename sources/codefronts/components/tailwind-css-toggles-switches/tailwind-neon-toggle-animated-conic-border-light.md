---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-neon-toggle-animated-conic-border-light/"
title: "Tailwind Neon Toggle with Animated Conic Border Light"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Demo 16's neon, but the light moves: a registered <angle> property spins a conic gradient around the frame, masked into a 2px border, so an armed switch has…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Toggle with Animated Conic Border Light
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-neon-toggle-animated-conic-border-light/

Demo 16's neon, but the light moves: a registered <angle> property spins a conic gradient around the frame, masked into a 2px border, so an armed switch has a single point of light running its perimeter. The chase IS the on state.
## HTML
```html
<section class="ttg-37 w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg37-bg font-ttg37-mono" aria-label="Neon toggle with running border light">
  <label for="ttg-37-sw" class="group relative flex items-center gap-6 p-0.5 rounded-2xl cursor-pointer has-checked:[&_.ttg37-ring]:animate-ttg37-spin has-checked:[&_.ttg37-ring]:opacity-100 motion-reduce:has-checked:[&_.ttg37-ring]:animate-none">
    <span aria-hidden="true" class="ttg37-ring pointer-events-none absolute inset-0 rounded-2xl opacity-0 transition-opacity duration-300 [background:conic-gradient(from_var(--ttg37-a,0deg),transparent_0deg,var(--color-ttg37-live)_40deg,transparent_110deg)] [mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] [mask-composite:exclude] p-0.5"></span>
    <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-2xl border border-ttg37-cold transition-colors duration-300 group-has-checked:border-transparent"></span>
    <span class="relative flex items-center gap-6 px-7 py-5 rounded-[15px] bg-ttg37-panel">
      <span class="flex flex-col gap-0.5">
        <b class="text-[14px] font-bold tracking-[0.18em] text-ttg37-dim transition-colors duration-300 group-has-checked:text-ttg37-live">REACTOR</b>
        <span class="text-[11px] tracking-[0.12em] text-ttg37-mute">Coolant loop &middot; primary</span>
      </span>
      <input type="checkbox" id="ttg-37-sw" role="switch" aria-label="Reactor" class="peer appearance-none shrink-0 w-16 h-8 rounded-full bg-ttg37-track relative cursor-pointer transition-[background-color,box-shadow] duration-300 before:content-[''] before:absolute before:top-1 before:left-1 before:w-6 before:h-6 before:rounded-full before:bg-ttg37-thumboff before:transition-[transform,background-color,box-shadow] before:duration-300 checked:bg-ttg37-trackon checked:shadow-[0_0_14px_-2px_var(--color-ttg37-live)] checked:before:translate-x-8 checked:before:bg-ttg37-live checked:before:shadow-[0_0_10px_var(--color-ttg37-live)] focus-visible:outline-3 focus-visible:outline-ttg37-live focus-visible:outline-offset-4 motion-reduce:transition-none motion-reduce:before:transition-none">
    </span>
  </label>
  <p class="text-[11px] tracking-[0.2em] uppercase text-ttg37-mute">Armed = light runs the perimeter</p>
</section>
```
## CSS
```css
@import "tailwindcss";
/* An angle must be registered to animate; a plain custom property jumps. */

@property --ttg37-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-ttg37-bg: #07060d;
  --color-ttg37-bg: oklch(0.13 0.02 290);
  --color-ttg37-panel: #110f1c;
  --color-ttg37-panel: oklch(0.18 0.025 290);
  --color-ttg37-cold: #2b2740;
  --color-ttg37-cold: oklch(0.3 0.03 290);
  --color-ttg37-live: #57f2d0;
  --color-ttg37-live: oklch(0.86 0.15 175);
  --color-ttg37-track: #1b1830;
  --color-ttg37-track: oklch(0.23 0.03 290);
  --color-ttg37-trackon: #123a38;
  --color-ttg37-trackon: oklch(0.32 0.07 180);
  --color-ttg37-thumboff: #4a4566;
  --color-ttg37-thumboff: oklch(0.45 0.04 290);
  --color-ttg37-dim: #8c85ab;
  --color-ttg37-dim: oklch(0.63 0.04 290);
  --color-ttg37-mute: #7b7599;
  --color-ttg37-mute: oklch(0.58 0.04 290);
  --font-ttg37-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --animate-ttg37-spin: ttg37-spin 3s linear infinite;
}

@keyframes ttg37-spin {
  to {
    --ttg37-a: 360deg;
  }
}

.ttg-37 {
  width: 100%;
  min-height: 100svh;
}

.ttg-37 input[type="checkbox"] {
  -webkit-appearance: none;
}
/* Reduced motion keeps the border lit, just still. */

@media (prefers-reduced-motion: reduce) {
  .ttg-37 label:has(:checked) .ttg37-ring {
    --ttg37-a: 140deg;
  }
}
```
