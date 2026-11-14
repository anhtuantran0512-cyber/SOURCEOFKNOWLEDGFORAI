---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-gradient-wave-section-divider-background-mask/"
title: "Tailwind Gradient Wave Section Divider with a Background Mask"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "A mesh-gradient section whose edge is cut into a wave by a mask, so the gradient is the divider &mdash; no flat fill, no visible seam, just a coloured field…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Wave Section Divider with a Background Mask
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-gradient-wave-section-divider-background-mask/

A mesh-gradient section whose edge is cut into a wave by a mask, so the gradient is the divider &mdash; no flat fill, no visible seam, just a coloured field that ends in a curve. Plus the safer variant, where the gradient lives inside the path via <linearGradient>.
## HTML
```html
<section class="twd-09 w-full min-h-svh flex flex-col bg-twd09-paper font-twd09-sans">

  <!-- Mesh gradient cut by a wave mask -->
  <div class="bg-twd09-void bg-[radial-gradient(70%_80%_at_12%_18%,var(--color-twd09-violet),transparent_70%),radial-gradient(60%_70%_at_88%_26%,var(--color-twd09-cyan),transparent_68%),radial-gradient(80%_90%_at_50%_100%,var(--color-twd09-pink),transparent_72%)] text-white px-6 pt-19 pb-[clamp(96px,13vw,150px)] text-center [mask:var(--twd09-wave)_no-repeat_center/100%_100%]">
    <p class="font-twd09-mono text-xs tracking-[0.2em] uppercase text-twd09-onvoid mb-3">Gradient mask</p>
    <h2 class="text-[clamp(26px,4.2vw,42px)] leading-[1.1] font-semibold mb-2.5">The gradient is the divider</h2>
    <p class="text-[15px] text-twd09-onvoid">One mask, any background underneath.</p>
  </div>
  <div class="-mt-0.5 bg-twd09-paper text-twd09-paperink px-6 pt-6 pb-15 text-center">
    <p class="text-[15px]">The section below stays a plain block &mdash; no wave markup needed.</p>
  </div>

  <!-- Gradient inside the path -->
  <div class="relative bg-twd09-dark text-white px-6 pt-17 pb-29 text-center">
    <h2 class="text-[clamp(24px,3.8vw,36px)] font-semibold">Gradient inside the path</h2>
    <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(58px,9vw,120px)] pointer-events-none" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <defs>
        <linearGradient id="twd09-grad" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stop-color="oklch(0.7 0.19 30)"></stop>
          <stop offset="0.5" stop-color="oklch(0.72 0.17 340)"></stop>
          <stop offset="1" stop-color="oklch(0.68 0.17 285)"></stop>
        </linearGradient>
      </defs>
      <path class="fill-[url(#twd09-grad)]" d="M0,58 C280,116 560,8 840,52 C1080,90 1250,104 1440,74 L1440,120 L0,120 Z"></path>
    </svg>
  </div>
  <div class="bg-[linear-gradient(90deg,oklch(0.7_0.19_30),oklch(0.72_0.17_340),oklch(0.68_0.17_285))] text-twd09-onband px-6 pt-7 pb-14 text-center">
    <p class="text-[15px] font-semibold max-w-[52ch] mx-auto">A gradient-filled path is safer over unpredictable content than masking a whole block.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd09-void: #14112a;
  --color-twd09-void: oklch(0.16 0.04 280);
  --color-twd09-onvoid: #ddd8ef;
  --color-twd09-onvoid: oklch(0.89 0.03 285);
  --color-twd09-violet: #9a5ce0;
  --color-twd09-violet: oklch(0.62 0.22 300);
  --color-twd09-cyan: #4bc6dd;
  --color-twd09-cyan: oklch(0.76 0.12 205);
  --color-twd09-pink: #d3529b;
  --color-twd09-pink: oklch(0.6 0.2 340);
  --color-twd09-paper: #f7f6fb;
  --color-twd09-paper: oklch(0.97 0.01 285);
  --color-twd09-paperink: #453d5c;
  --color-twd09-paperink: oklch(0.4 0.05 285);
  --color-twd09-dark: #15121f;
  --color-twd09-dark: oklch(0.18 0.03 300);
  --color-twd09-onband: #2b1b2c;
  --color-twd09-onband: oklch(0.24 0.05 330);
  --font-twd09-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd09-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* The cutter shape for the masked mesh section. */

.twd-09 {
  width: 100%;
  min-height: 100svh;
  --twd09-wave: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201440%20400'%20preserveAspectRatio='none'%3E%3Cpath%20d='M0,0%20L1440,0%20L1440,340%20C1180,392%20900,292%20660,336%20C420,380%20200,392%200,356%20Z'%20fill='%23000'/%3E%3C/svg%3E");
}
/* Safari < 15.4 mask shim — targets the masked mesh block only. */

.twd-09 > div:first-child {
  -webkit-mask: var(--twd09-wave) no-repeat center/100% 100%;
}
```
