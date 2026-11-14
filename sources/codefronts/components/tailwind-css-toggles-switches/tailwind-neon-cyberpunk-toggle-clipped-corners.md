---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-neon-cyberpunk-toggle-clipped-corners/"
title: "Tailwind Neon Cyberpunk Toggle with Clipped Corners"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A clipped-corner neon tube for dark dashboards and game UIs: magenta standby snaps to cyan on engage, and the LIVE legend strikes like a gas tube warming up."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Cyberpunk Toggle with Clipped Corners
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-neon-cyberpunk-toggle-clipped-corners/

A clipped-corner neon tube for dark dashboards and game UIs: magenta standby snaps to cyan on engage, and the LIVE legend strikes like a gas tube warming up. Every glow is layered box-shadow and text-shadow &mdash; no images, no filters.
## HTML
```html
<section class="ttg-16 w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg16-bg font-ttg16-mono" aria-label="Neon cyberpunk toggle">
  <label for="ttg-16-sw" class="flex items-center gap-6 px-7 py-5 cursor-pointer bg-ttg16-panel [clip-path:polygon(10px_0,100%_0,100%_calc(100%-10px),calc(100%-10px)_100%,0_100%,0_10px)] has-checked:[&_.ttg16-stby]:opacity-0 has-checked:[&_.ttg16-live]:opacity-100 has-checked:[&_.ttg16-live]:animate-ttg16-strike motion-reduce:has-checked:[&_.ttg16-live]:animate-none">
    <span aria-hidden="true" class="text-[14px] font-bold tracking-[0.3em] text-ttg16-dim">PWR</span>
    <span class="relative w-23 h-10 bg-ttg16-tube border border-ttg16-standby transition-[border-color,box-shadow] duration-300 shadow-[0_0_1px_var(--color-ttg16-standby),inset_0_0_10px_color-mix(in_oklab,var(--color-ttg16-standby)_25%,transparent)] [clip-path:polygon(8px_0,100%_0,100%_calc(100%-8px),calc(100%-8px)_100%,0_100%,0_8px)] has-checked:border-ttg16-live has-checked:shadow-[0_0_1px_var(--color-ttg16-live),inset_0_0_12px_color-mix(in_oklab,var(--color-ttg16-live)_30%,transparent)] has-checked:[&_.ttg16-thumb]:translate-x-[50px] has-checked:[&_.ttg16-thumb]:bg-ttg16-live has-checked:[&_.ttg16-thumb]:shadow-[0_0_10px_var(--color-ttg16-live)]">
      <input type="checkbox" id="ttg-16-sw" role="switch" aria-label="Power" class="appearance-none absolute inset-0 w-full h-full z-10 bg-transparent cursor-pointer focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[6px]">
      <span aria-hidden="true" class="ttg16-thumb pointer-events-none absolute top-1.5 left-1.5 w-7 h-6.5 bg-ttg16-standby shadow-[0_0_8px_var(--color-ttg16-standby)] transition-[transform,background-color,box-shadow] duration-300 ease-[cubic-bezier(0.6,0,0.3,1.2)] [clip-path:polygon(5px_0,100%_0,100%_calc(100%-5px),calc(100%-5px)_100%,0_100%,0_5px)] motion-reduce:duration-150"></span>
    </span>
    <span aria-hidden="true" class="relative w-13 h-[18px] text-[13px] font-bold tracking-[0.18em]">
      <i class="ttg16-stby absolute inset-0 not-italic transition-opacity duration-250 text-ttg16-standby [text-shadow:0_0_6px_var(--color-ttg16-standby),0_0_16px_color-mix(in_oklab,var(--color-ttg16-standby)_55%,transparent)]">STBY</i>
      <i class="ttg16-live absolute inset-0 not-italic opacity-0 transition-opacity duration-250 text-ttg16-live [text-shadow:0_0_6px_var(--color-ttg16-live),0_0_16px_color-mix(in_oklab,var(--color-ttg16-live)_55%,transparent)]">LIVE</i>
    </span>
  </label>
  <p class="text-[11px] tracking-[0.2em] uppercase text-ttg16-dim">Magenta standby &rarr; cyan engage</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg16-bg: #09070f;
  --color-ttg16-bg: oklch(0.14 0.02 300);
  --color-ttg16-panel: #130f1f;
  --color-ttg16-panel: oklch(0.19 0.03 300);
  --color-ttg16-tube: #0c0a15;
  --color-ttg16-tube: oklch(0.16 0.025 300);
  --color-ttg16-standby: #ff5fd0;
  --color-ttg16-standby: oklch(0.74 0.23 340);
  --color-ttg16-live: #5fe4ff;
  --color-ttg16-live: oklch(0.85 0.14 200);
  --color-ttg16-dim: #7b7395;
  --color-ttg16-dim: oklch(0.58 0.04 300);
  --font-ttg16-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --animate-ttg16-strike: ttg16-strike 0.5s steps(1, end);
}

@keyframes ttg16-strike {
  0% {
    opacity: 0;
  }

  20% {
    opacity: 1;
  }

  30% {
    opacity: 0.2;
  }

  45% {
    opacity: 1;
  }

  55% {
    opacity: 0.4;
  }

  70% {
    opacity: 1;
  }
}

.ttg-16 {
  width: 100%;
  min-height: 100svh;
}

.ttg-16 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
