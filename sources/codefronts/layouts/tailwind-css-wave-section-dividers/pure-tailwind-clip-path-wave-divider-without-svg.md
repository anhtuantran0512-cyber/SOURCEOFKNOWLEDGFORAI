---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/pure-tailwind-clip-path-wave-divider-without-svg/"
title: "Pure Tailwind Clip Path Wave Divider Without SVG"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "For engineers who refuse to ship inline SVG in their markup: three CSS-only cuts &mdash; clip-path: path(), a tiled scallop mask, and an elliptical…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Clip Path Wave Divider Without SVG
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/pure-tailwind-clip-path-wave-divider-without-svg/

For engineers who refuse to ship inline SVG in their markup: three CSS-only cuts &mdash; clip-path: path(), a tiled scallop mask, and an elliptical border-radius dome &mdash; each expressed as a single arbitrary property, with no extra DOM weight at all.
## HTML
```html
<section class="twd-06 w-full min-h-svh flex flex-col font-twd06-sans">

  <!-- clip-path: path() wave -->
  <div class="bg-twd06-forest text-white px-6 pt-16 pb-9 text-center">
    <h2 class="text-[clamp(24px,3.8vw,36px)] font-semibold mb-2">No SVG in the DOM</h2>
    <p class="text-[15px] text-twd06-onforest">The curve is one utility.</p>
  </div>
  <div class="bg-twd06-forest">
    <div role="presentation" class="h-25 -mt-px bg-twd06-mint [clip-path:path('M0,44_C240,110_480,-6_720,38_C960,82_1200,110_1440,58_L5000,58_L5000,100_L0,100_Z')]"></div>
  </div>
  <div class="bg-twd06-mint text-twd06-forestink px-6 pt-3.5 pb-15 text-center">
    <p class="text-[15px]"><code class="font-twd06-mono text-[13.5px]">clip-path: path()</code> takes SVG path syntax straight in CSS &mdash; in px, so this strip is fixed-height on purpose.</p>
  </div>

  <!-- Fluid scallop mask -->
  <div class="bg-twd06-indigo text-white px-6 pt-16 pb-8 text-center">
    <h2 class="text-[clamp(24px,3.8vw,36px)] font-semibold mb-2">Fluid without stretching</h2>
    <p class="text-[15px] text-twd06-onindigo">The wave tiles instead of squashing.</p>
  </div>
  <div class="bg-twd06-indigo">
    <div role="presentation" class="twd-06-scallop h-[42px] -mt-px bg-twd06-frost [mask:radial-gradient(calc(var(--twd06-pitch)/2)_at_50%_100%,transparent_98%,#000)_repeat-x_0_0/var(--twd06-pitch)_42px]"></div>
  </div>
  <div class="bg-twd06-frost text-twd06-indigoink px-6 pt-3 pb-15 text-center">
    <p class="text-[15px] max-w-[52ch] mx-auto">A repeating radial-gradient mask keeps every crest the same size at any viewport.</p>
  </div>

  <!-- Ellipse dome via border-radius -->
  <div class="overflow-hidden">
    <div class="bg-twd06-rust text-white px-6 pt-16 pb-13 text-center">
      <h2 class="text-[clamp(24px,3.8vw,36px)] font-semibold">One-line dome curve</h2>
    </div>
    <div class="relative w-[112%] -ml-[6%] -mt-10 bg-twd06-blush text-twd06-rustink px-6 pt-12 pb-15 text-center [border-radius:50%_50%_0_0/72px_72px_0_0]">
      <p class="text-[15px] max-w-[52ch] mx-auto"><code class="font-twd06-mono text-[13.5px]">[border-radius:50%_50%_0_0/72px_72px_0_0]</code> &mdash; the cheapest curve in CSS.</p>
    </div>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd06-forest: #1f513c;
  --color-twd06-forest: oklch(0.38 0.08 158);
  --color-twd06-onforest: #cfe4d9;
  --color-twd06-onforest: oklch(0.89 0.03 158);
  --color-twd06-mint: #f0f7f2;
  --color-twd06-mint: oklch(0.96 0.02 150);
  --color-twd06-forestink: #2f5a48;
  --color-twd06-forestink: oklch(0.42 0.06 158);
  --color-twd06-indigo: #453a8c;
  --color-twd06-indigo: oklch(0.38 0.14 280);
  --color-twd06-onindigo: #d6d2ee;
  --color-twd06-onindigo: oklch(0.87 0.04 280);
  --color-twd06-frost: #f6f6fc;
  --color-twd06-frost: oklch(0.97 0.01 280);
  --color-twd06-indigoink: #443c7e;
  --color-twd06-indigoink: oklch(0.4 0.11 280);
  --color-twd06-rust: #9a3b21;
  --color-twd06-rust: oklch(0.47 0.15 38);
  --color-twd06-blush: #fcf2ee;
  --color-twd06-blush: oklch(0.97 0.02 38);
  --color-twd06-rustink: #7a3a24;
  --color-twd06-rustink: oklch(0.42 0.11 38);
  --font-twd06-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd06-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Scallop pitch: a per-demo geometry knob, deliberately NOT an @theme entry —
   nothing is gained by minting pitch-* utilities for one shape. */

.twd-06 {
  width: 100%;
  min-height: 100svh;
  --twd06-pitch: 74px;
}
/* Safari < 15.4 mask shim. Scoped to the scallop strip by class, NOT to
   [role="presentation"] — this demo has two such strips, and -webkit-mask is an alias of
   mask in Chromium, so a broad selector would also mask the clip-path strip and the two
   shapes would intersect into slivers. */

.twd-06 .twd-06-scallop {
  -webkit-mask: radial-gradient(calc(var(--twd06-pitch)/2) at 50% 100%, transparent 98%, #000) repeat-x 0 0/var(--twd06-pitch) 42px;
}
```
