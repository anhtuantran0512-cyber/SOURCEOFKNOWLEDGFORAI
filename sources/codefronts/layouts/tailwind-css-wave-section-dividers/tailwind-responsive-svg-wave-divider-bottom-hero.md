---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-responsive-svg-wave-divider-bottom-hero/"
title: "Tailwind Responsive SVG Wave Divider at the Bottom of a Hero"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "A dark hero whose wave sits exactly on its bottom edge and scales from a 320px phone to a 4K display &mdash; plus the flow-layout alternative, where…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive SVG Wave Divider at the Bottom of a Hero
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-responsive-svg-wave-divider-bottom-hero/

A dark hero whose wave sits exactly on its bottom edge and scales from a 320px phone to a 4K display &mdash; plus the flow-layout alternative, where aspect-[1440/160] makes the SVG reserve its own space so it can never overlap the copy.
## HTML
```html
<section class="twd-03 w-full min-h-svh flex flex-col font-twd03-sans">

  <!-- Dark hero, fluid clamp() wave -->
  <header class="relative overflow-hidden bg-twd03-night bg-[radial-gradient(120%_130%_at_20%_0%,var(--color-twd03-glow),var(--color-twd03-night))] text-white px-6 pt-19 pb-[clamp(104px,15vw,180px)] text-center">
    <p class="font-twd03-mono text-xs tracking-[0.2em] uppercase text-twd03-accent mb-3">Responsive hero</p>
    <h2 class="text-[clamp(26px,4.4vw,44px)] leading-[1.08] font-semibold mb-2.5">Scales from 320px to 4K</h2>
    <p class="text-[15px] text-twd03-onnight max-w-[46ch] mx-auto">Wave height is clamped, so the curve keeps its shape at every width.</p>
    <a href="#0" class="inline-flex items-center justify-center min-h-11 mt-5 px-7 rounded-full text-sm font-bold text-twd03-night bg-twd03-accent no-underline transition-transform duration-200 hover:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:hover:translate-y-0">Read the guide</a>
    <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(52px,8vw,120px)] text-twd03-paper [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,48 C220,112 420,8 720,48 C1020,88 1240,112 1440,64 L1440,120 L0,120 Z"></path>
    </svg>
  </header>
  <div class="bg-twd03-paper text-twd03-body px-6 pt-8 pb-16 text-center">
    <p class="text-[15px]">Content section &mdash; never overlapped, because the hero reserves the padding.</p>
  </div>

  <!-- Aspect-ratio wave in normal flow -->
  <header class="bg-twd03-plum text-white px-6 pt-18 pb-0 text-center">
    <h2 class="text-[clamp(25px,4vw,38px)] font-semibold mb-2.5">Ratio-locked curve</h2>
    <p class="text-[15px] text-twd03-onplum max-w-[48ch] mx-auto"><code class="font-twd03-mono text-[13.5px]">aspect-[1440/160]</code> keeps the wave identical at every width.</p>
    <svg class="block w-full h-auto aspect-[1440/160] -mb-px text-twd03-mist [&_path]:fill-current" viewBox="0 0 1440 160" aria-hidden="true" focusable="false">
      <path d="M0,80 C300,160 560,0 880,64 C1120,112 1280,132 1440,96 L1440,160 L0,160 Z"></path>
    </svg>
  </header>
  <div class="bg-twd03-mist text-twd03-plumink px-6 pt-2 pb-15 text-center">
    <p class="text-[15px]">No <code class="font-twd03-mono text-[13.5px]">preserveAspectRatio</code> override needed &mdash; the box matches the viewBox.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd03-night: #16192a;
  --color-twd03-night: oklch(0.19 0.03 265);
  --color-twd03-glow: #2f3560;
  --color-twd03-glow: oklch(0.28 0.07 272);
  --color-twd03-onnight: #c8cbdb;
  --color-twd03-onnight: oklch(0.84 0.02 265);
  --color-twd03-accent: #4fd6ac;
  --color-twd03-accent: oklch(0.82 0.14 168);
  --color-twd03-paper: #f4f5f9;
  --color-twd03-paper: oklch(0.96 0.01 265);
  --color-twd03-body: #3e4256;
  --color-twd03-body: oklch(0.4 0.03 265);
  --color-twd03-plum: #4c2a4d;
  --color-twd03-plum: oklch(0.33 0.1 324);
  --color-twd03-onplum: #e0c9e2;
  --color-twd03-onplum: oklch(0.85 0.05 324);
  --color-twd03-mist: #f3edf4;
  --color-twd03-mist: oklch(0.95 0.02 320);
  --color-twd03-plumink: #55305a;
  --color-twd03-plumink: oklch(0.38 0.08 320);
  --font-twd03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd03-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.twd-03 {
  width: 100%;
  min-height: 100svh;
}
```
