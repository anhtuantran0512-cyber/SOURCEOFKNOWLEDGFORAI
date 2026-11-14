---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-stacked-multi-color-svg-wave-section-divider/"
title: "Tailwind Stacked Multi Color SVG Wave Section Divider"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "Two or three offset waves in tinted layers, so a change of background colour reads as depth instead of a line."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stacked Multi Color SVG Wave Section Divider
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-stacked-multi-color-svg-wave-section-divider/

Two or three offset waves in tinted layers, so a change of background colour reads as depth instead of a line. The port replaces a ladder of :nth-child() + color-mix() rules with an opacity modifier on each layer&rsquo;s own fill-* utility.
## HTML
```html
<section class="twd-04 w-full min-h-svh flex flex-col font-twd04-sans">

  <!-- Three tinted layers -->
  <div class="relative overflow-hidden bg-twd04-from text-white px-6 pt-18 pb-32 text-center">
    <h2 class="text-[clamp(25px,4vw,38px)] font-semibold">Layered depth, one hue</h2>
    <div aria-hidden="true" class="absolute inset-x-0 -bottom-px h-[clamp(70px,11vw,130px)] pointer-events-none">
      <svg class="absolute inset-x-0 bottom-0 block w-full h-full fill-twd04-to/30" viewBox="0 0 1440 130" preserveAspectRatio="none" focusable="false"><path d="M0,70 C260,20 520,120 780,74 C1040,28 1240,60 1440,40 L1440,130 L0,130 Z"></path></svg>
      <svg class="absolute inset-x-0 bottom-0 block w-full h-full fill-twd04-to/62" viewBox="0 0 1440 130" preserveAspectRatio="none" focusable="false"><path d="M0,86 C240,44 500,126 760,88 C1020,50 1250,96 1440,66 L1440,130 L0,130 Z"></path></svg>
      <svg class="absolute inset-x-0 bottom-0 block w-full h-full fill-twd04-to" viewBox="0 0 1440 130" preserveAspectRatio="none" focusable="false"><path d="M0,100 C220,70 480,132 740,102 C1000,72 1250,120 1440,92 L1440,130 L0,130 Z"></path></svg>
    </div>
  </div>
  <div class="bg-twd04-to text-twd04-toink px-6 pt-8 pb-16 text-center">
    <p class="text-[15px]">Back layers are stepped tints of one hue; only the front layer is opaque.</p>
  </div>

  <!-- Duotone offset ribbons -->
  <div class="relative overflow-hidden bg-twd04-navy text-white px-6 pt-17 pb-29 text-center">
    <h2 class="text-[clamp(25px,4vw,38px)] font-semibold">Two-colour ribbon seam</h2>
    <div aria-hidden="true" class="absolute inset-x-0 -bottom-px h-[clamp(64px,10vw,120px)] pointer-events-none">
      <svg class="absolute inset-x-0 bottom-0 block w-full h-full fill-twd04-accent" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,54 C300,110 620,6 940,52 C1160,84 1300,92 1440,62 L1440,120 L0,120 Z"></path></svg>
      <svg class="absolute inset-x-0 bottom-0 block w-full h-full fill-twd04-shell" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,74 C300,126 620,22 940,70 C1160,102 1300,110 1440,80 L1440,120 L0,120 Z"></path></svg>
    </div>
  </div>
  <div class="bg-twd04-shell text-twd04-navyink px-6 pt-8 pb-15 text-center">
    <p class="text-[15px] max-w-[52ch] mx-auto">An accent ribbon peeks out from under the opaque edge &mdash; brand colour, no extra markup weight.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd04-from: #443a77;
  --color-twd04-from: oklch(0.34 0.12 285);
  --color-twd04-to: #eeeaf7;
  --color-twd04-to: oklch(0.95 0.03 285);
  --color-twd04-toink: #4a4173;
  --color-twd04-toink: oklch(0.4 0.09 285);
  --color-twd04-navy: #17323c;
  --color-twd04-navy: oklch(0.24 0.04 200);
  --color-twd04-navyink: #2b4b57;
  --color-twd04-navyink: oklch(0.38 0.05 200);
  --color-twd04-shell: #f6f9fa;
  --color-twd04-shell: oklch(0.97 0.01 200);
  --color-twd04-accent: #e0a92c;
  --color-twd04-accent: oklch(0.75 0.17 88);
  --font-twd04-sans: 'Space Grotesk', system-ui, sans-serif;
}

.twd-04 {
  width: 100%;
  min-height: 100svh;
}
```
