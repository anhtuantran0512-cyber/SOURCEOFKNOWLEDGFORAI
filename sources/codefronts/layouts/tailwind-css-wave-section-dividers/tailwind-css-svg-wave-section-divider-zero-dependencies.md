---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-css-svg-wave-section-divider-zero-dependencies/"
title: "Tailwind CSS SVG Wave Section Divider with Zero Dependencies"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "The baseline everyone actually needs, three ways: an inline SVG path, the same wave as a reusable mask-image utility, and a low-amplitude editorial seam."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS SVG Wave Section Divider with Zero Dependencies
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-css-svg-wave-section-divider-zero-dependencies/

The baseline everyone actually needs, three ways: an inline SVG path, the same wave as a reusable mask-image utility, and a low-amplitude editorial seam. The port's win is text-twd01-next [&_path]:fill-current — the seam colour now lives on the SVG that renders it, so re-theming one divider needs no new CSS rule.
## HTML
```html
<section class="twd-01 w-full min-h-svh flex flex-col font-twd01-sans">

  <!-- Classic inline SVG wave -->
  <div class="relative bg-twd01-ink text-white px-6 pt-18 pb-27 text-center">
    <p class="font-twd01-mono text-xs tracking-[0.18em] uppercase text-twd01-mute mb-3.5">Pure Tailwind + inline SVG</p>
    <h2 class="text-[clamp(26px,4vw,40px)] leading-[1.1] font-semibold mb-2.5">Break the boxy grid</h2>
    <p class="text-[15px] text-twd01-onink">One path, one class list, zero dependencies.</p>
    <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(56px,9vw,110px)] text-twd01-next [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,64 C240,120 480,8 720,40 C960,72 1200,120 1440,72 L1440,120 L0,120 Z"></path>
    </svg>
  </div>
  <div class="bg-twd01-next text-twd01-ink px-6 pt-11 pb-16 text-center">
    <p class="text-[15px] text-twd01-body">Next section starts here &mdash; the wave is this block&rsquo;s own edge.</p>
  </div>

  <!-- Reusable data-URI mask: one arbitrary property, any two sections -->
  <div class="bg-twd01-teal text-white px-6 pt-16 pb-10 text-center">
    <h2 class="text-[clamp(24px,3.6vw,34px)] font-semibold mb-2">Reusable divider utility</h2>
    <p class="text-[15px] text-twd01-onteal">The wave lives in a custom property, so the markup stays a single div.</p>
  </div>
  <div class="bg-twd01-teal">
    <div role="presentation" class="-mt-px h-[clamp(48px,7vw,88px)] bg-twd01-pale [mask:var(--twd01-wave)_no-repeat_center/100%_100%]"></div>
  </div>
  <div class="bg-twd01-pale text-twd01-teal px-6 pt-7 pb-15 text-center">
    <p class="text-[15px]">Drop the masked div between any two blocks &mdash; <code class="font-twd01-mono text-[13.5px] bg-twd01-tint px-1.5 py-0.5 rounded">[mask:var(--twd01-wave)&hellip;]</code></p>
  </div>

  <!-- Soft double-curve seam -->
  <div class="relative bg-twd01-warm text-twd01-deep px-6 pt-17 pb-24 text-center">
    <h2 class="text-[clamp(24px,3.6vw,34px)] font-semibold">Gentle, editorial seam</h2>
    <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(44px,6vw,80px)] text-twd01-deep [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,52 C180,4 360,4 540,44 C740,88 900,88 1080,50 C1220,20 1330,20 1440,42 L1440,90 L0,90 Z"></path>
    </svg>
  </div>
  <div class="bg-twd01-deep text-twd01-warm px-6 pt-8 pb-16 text-center">
    <p class="text-[15px]">Low-amplitude curves read as premium; tall waves read as playful.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd01-ink: #2d3555;
  --color-twd01-ink: oklch(0.28 0.06 264);
  --color-twd01-onink: #d9dcea;
  --color-twd01-onink: oklch(0.88 0.02 264);
  --color-twd01-mute: #a8aec8;
  --color-twd01-mute: oklch(0.74 0.03 264);
  --color-twd01-next: #f5f6fa;
  --color-twd01-next: oklch(0.97 0.01 264);
  --color-twd01-body: #4a5170;
  --color-twd01-body: oklch(0.42 0.04 264);
  --color-twd01-teal: #1c7f9e;
  --color-twd01-teal: oklch(0.55 0.16 205);
  --color-twd01-onteal: #dff1f7;
  --color-twd01-onteal: oklch(0.93 0.02 205);
  --color-twd01-pale: #f7fbfc;
  --color-twd01-pale: oklch(0.98 0.01 205);
  --color-twd01-tint: #d7eaf1;
  --color-twd01-tint: oklch(0.92 0.03 205);
  --color-twd01-warm: #f4e6c8;
  --color-twd01-warm: oklch(0.93 0.05 78);
  --color-twd01-deep: #6b3a2c;
  --color-twd01-deep: oklch(0.35 0.07 30);
  --font-twd01-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd01-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.twd-01 {
  width: 100%;
  min-height: 100svh;
}
/* The wave shape for the mask variant: geometry, not a design-scale value, so it stays
   a plain custom property instead of an @theme entry. */

.twd-01 {
  --twd01-wave: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201440%20100'%20preserveAspectRatio='none'%3E%3Cpath%20d='M0,40%20C300,110%20640,-10%20960,34%20C1200,68%201320,74%201440,44%20L1440,100%20L0,100%20Z'%20fill='%23000'/%3E%3C/svg%3E");
}
/* Safari < 15.4 mask shim — no variant form exists for the -webkit- prefix. */

.twd-01 [role="presentation"] {
  -webkit-mask: var(--twd01-wave) no-repeat center/100% 100%;
}
```
