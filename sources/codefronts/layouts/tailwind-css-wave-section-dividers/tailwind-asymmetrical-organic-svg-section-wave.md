---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-asymmetrical-organic-svg-section-wave/"
title: "Tailwind Asymmetrical Organic SVG Section Wave"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "Non-repeating, hand-drawn-feeling curves for editorial and brand-showcase pages."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Asymmetrical Organic SVG Section Wave
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-asymmetrical-organic-svg-section-wave/

Non-repeating, hand-drawn-feeling curves for editorial and brand-showcase pages. Symmetry reads as template; asymmetry reads as art direction &mdash; these paths deliberately break the mirror, and the blob variant overflows its box on both sides so the curve reads as a fragment of something larger.
## HTML
```html
<section class="twd-10 w-full min-h-svh flex flex-col font-twd10-sans">

  <!-- Editorial off-balance sweep -->
  <div class="relative overflow-hidden bg-twd10-ink text-twd10-cream px-[8%] pt-18 pb-33 text-left">
    <p class="font-twd10-mono text-xs tracking-[0.16em] text-twd10-num mb-3.5">01 / Studio</p>
    <h2 class="text-[clamp(28px,5.4vw,54px)] leading-[1.02] tracking-[-0.02em] font-semibold max-w-[16ch]">Curves with<br>a point of view</h2>
    <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(66px,10vw,130px)] text-twd10-cream [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 130" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,96 C280,-8 520,104 760,78 C920,60 1120,86 1440,22 L1440,130 L0,130 Z"></path>
    </svg>
  </div>
  <div class="bg-twd10-cream text-twd10-ink px-[8%] pt-3.5 pb-15">
    <p class="text-[15px] max-w-[52ch]">One dominant crest on the left, a long quiet run-out to the right.</p>
  </div>

  <!-- Organic blob fragment -->
  <div class="relative overflow-hidden bg-twd10-deep text-white px-6 pt-18 pb-35 text-center">
    <h2 class="text-[clamp(25px,4.2vw,40px)] leading-[1.06] font-semibold max-w-[22ch] mx-auto">A fragment of something bigger</h2>
    <svg class="absolute -left-[4%] -bottom-px block w-[108%] h-[clamp(90px,14vw,180px)] text-twd10-sand [&_path]:fill-current pointer-events-none" viewBox="0 0 1200 220" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M-40,150 C120,60 280,206 470,168 C640,134 700,44 880,62 C1030,77 1090,150 1240,120 L1240,240 L-40,240 Z"></path>
    </svg>
  </div>
  <div class="bg-twd10-sand text-twd10-deepink px-6 pt-3 pb-15 text-center">
    <p class="text-[15px] max-w-[52ch] mx-auto">The path overflows on both sides, so the curve never looks boxed by the viewport.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd10-ink: #2a2620;
  --color-twd10-ink: oklch(0.24 0.02 60);
  --color-twd10-cream: #f1e4c3;
  --color-twd10-cream: oklch(0.94 0.04 82);
  --color-twd10-num: #b9a97f;
  --color-twd10-num: oklch(0.76 0.05 82);
  --color-twd10-deep: #1a5b66;
  --color-twd10-deep: oklch(0.42 0.08 200);
  --color-twd10-deepink: #235561;
  --color-twd10-deepink: oklch(0.4 0.07 200);
  --color-twd10-sand: #f3edd9;
  --color-twd10-sand: oklch(0.95 0.04 96);
  --font-twd10-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd10-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.twd-10 {
  width: 100%;
  min-height: 100svh;
}
```
