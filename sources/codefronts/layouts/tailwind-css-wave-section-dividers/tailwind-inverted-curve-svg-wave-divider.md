---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-inverted-curve-svg-wave-divider/"
title: "Tailwind Inverted Curve SVG Wave Divider"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "Concave dips that pull the eye downward into a CTA."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Inverted Curve SVG Wave Divider
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-inverted-curve-svg-wave-divider/

Concave dips that pull the eye downward into a CTA. The edge scoops inward instead of bulging out, which visually funnels attention to the pinch point &mdash; the reason conversion-focused pages use it around signup banners. The lens variant curves both edges and floats the band off the grid.
## HTML
```html
<section class="twd-07 w-full min-h-svh flex flex-col font-twd07-sans">

  <!-- Concave CTA funnel -->
  <div class="bg-twd07-page text-twd07-pageink px-6 py-12 text-center">
    <p class="text-[15px]">Features, proof, screenshots&hellip;</p>
  </div>
  <div class="relative overflow-hidden bg-twd07-band text-white px-6 pt-[clamp(88px,12vw,140px)] pb-15 text-center">
    <svg class="absolute inset-x-0 -top-px block w-full h-[clamp(56px,8vw,104px)] text-twd07-page [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 110" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,0 C360,0 420,110 720,110 C1020,110 1080,0 1440,0 L1440,0 L0,0 Z"></path>
    </svg>
    <h2 class="text-[clamp(25px,4vw,40px)] font-semibold mb-2.5">Start your free trial</h2>
    <p class="text-[15px] text-twd07-onband max-w-[44ch] mx-auto">The curve funnels the eye to the centre &mdash; put the button there.</p>
    <a href="#0" class="inline-flex items-center justify-center min-h-11 mt-5 px-7 rounded-full text-[14.5px] font-extrabold text-twd07-bandink bg-twd07-accent no-underline transition-transform duration-200 hover:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:hover:translate-y-0">Create account</a>
  </div>
  <div class="bg-twd07-page text-twd07-pageink px-6 py-12 text-center">
    <p class="text-[15px]">&hellip;and the page continues.</p>
  </div>

  <!-- Lens band: arch top + bottom -->
  <div class="bg-twd07-olive text-twd07-oliveink px-6 py-11 text-center">
    <p class="text-[15px]">Section above</p>
  </div>
  <div class="relative overflow-hidden bg-twd07-teal text-white px-6 py-[clamp(80px,11vw,120px)] text-center">
    <svg class="absolute inset-x-0 -top-px block w-full h-[clamp(48px,7vw,86px)] text-twd07-olive [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,0 C420,0 480,90 720,90 C960,90 1020,0 1440,0 Z"></path>
    </svg>
    <h2 class="text-[clamp(24px,3.8vw,36px)] font-semibold mb-2">A lens for one idea</h2>
    <p class="text-[15px] text-twd07-onteal max-w-[44ch] mx-auto">Curved on both edges, the band floats away from the grid.</p>
    <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(48px,7vw,86px)] text-twd07-olive [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,90 C420,90 480,0 720,0 C960,0 1020,90 1440,90 Z"></path>
    </svg>
  </div>
  <div class="bg-twd07-olive text-twd07-oliveink px-6 py-11 text-center">
    <p class="text-[15px]">Section below</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd07-page: #f3f4f9;
  --color-twd07-page: oklch(0.96 0.01 260);
  --color-twd07-pageink: #454a5c;
  --color-twd07-pageink: oklch(0.44 0.03 260);
  --color-twd07-band: #2b2f6b;
  --color-twd07-band: oklch(0.3 0.11 272);
  --color-twd07-bandink: #1d2050;
  --color-twd07-bandink: oklch(0.24 0.08 272);
  --color-twd07-onband: #c9cbe8;
  --color-twd07-onband: oklch(0.85 0.04 272);
  --color-twd07-accent: #f3c651;
  --color-twd07-accent: oklch(0.85 0.15 92);
  --color-twd07-olive: #f1f3e6;
  --color-twd07-olive: oklch(0.95 0.02 110);
  --color-twd07-oliveink: #4a4f3c;
  --color-twd07-oliveink: oklch(0.44 0.04 115);
  --color-twd07-teal: #1c5f5c;
  --color-twd07-teal: oklch(0.42 0.08 185);
  --color-twd07-onteal: #cfe4e2;
  --color-twd07-onteal: oklch(0.89 0.03 185);
  --font-twd07-sans: 'Space Grotesk', system-ui, sans-serif;
}

.twd-07 {
  width: 100%;
  min-height: 100svh;
}
```
