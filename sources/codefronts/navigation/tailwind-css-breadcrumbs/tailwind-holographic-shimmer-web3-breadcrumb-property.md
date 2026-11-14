---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-holographic-shimmer-web3-breadcrumb-property/"
title: "Tailwind Holographic Shimmer Web3 Breadcrumb with Animated @property"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A deep-space glass pill with a holo-card iridescence: a conic rainbow rotates under a masked diagonal ruling, both fading in on hover or focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Holographic Shimmer Web3 Breadcrumb with Animated @property
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-holographic-shimmer-web3-breadcrumb-property/

A deep-space glass pill with a holo-card iridescence: a conic rainbow rotates under a masked diagonal ruling, both fading in on hover or focus. This is the collection's clearest example of the port's limit &mdash; @property and @keyframes cannot be utilities, so the animation stays CSS and the markup keeps only what it can hold.
## HTML
```html
<section class="tbc-18 w-full min-h-svh grid place-items-center overflow-hidden px-6 py-10 font-tbc18-sans text-tbc18-ink bg-[radial-gradient(1200px_700px_at_15%_10%,oklch(0.3_0.1_285/0.55),transparent_60%),radial-gradient(900px_600px_at_85%_90%,oklch(0.28_0.12_320/0.45),transparent_65%),linear-gradient(160deg,oklch(0.16_0.06_275),oklch(0.11_0.05_295)_55%,oklch(0.09_0.04_250))]">
  <nav aria-label="Breadcrumb" class="w-[min(100%,720px)]">
    <ol class="group relative isolate flex flex-wrap items-center gap-x-2 gap-y-1 list-none m-0 px-4 py-2 rounded-full overflow-hidden bg-tbc18-card border border-tbc18-stroke [backdrop-filter:blur(18px)_saturate(140%)] shadow-[inset_0_1px_0_oklch(1_0_0/0.08),0_20px_50px_-20px_oklch(0_0_0/0.55)] before:content-[''] before:absolute before:inset-0 before:rounded-[inherit] before:pointer-events-none before:opacity-0 before:z-0 before:transition-opacity before:duration-300 before:[mix-blend-mode:color-dodge] before:[filter:blur(6px)_saturate(160%)] before:bg-[conic-gradient(from_var(--tbc18-angle),oklch(0.82_0.19_25),oklch(0.86_0.19_90),oklch(0.84_0.18_160),oklch(0.8_0.2_240),oklch(0.78_0.22_315),oklch(0.82_0.19_25))] after:content-[''] after:absolute after:inset-0 after:rounded-[inherit] after:pointer-events-none after:opacity-0 after:z-0 after:transition-opacity after:duration-300 after:[mix-blend-mode:overlay] after:bg-[repeating-linear-gradient(115deg,oklch(1_0_0/0.1)_0_2px,transparent_2px_7px)] after:[mask-image:linear-gradient(115deg,transparent_20%,black_45%,black_60%,transparent_85%)] hover:before:opacity-35 hover:before:animate-tbc18-spin focus-within:before:opacity-35 focus-within:before:animate-tbc18-spin hover:after:opacity-55 hover:after:animate-tbc18-sweep focus-within:after:opacity-55 focus-within:after:animate-tbc18-sweep motion-reduce:hover:before:animate-none motion-reduce:hover:after:animate-none">
      <li class="relative z-1 inline-flex items-center min-h-11"><a href="#" class="relative inline-flex items-center gap-1.5 min-h-11 px-2.5 rounded-lg text-[15px] font-medium tracking-[0.01em] text-tbc18-mut no-underline transition-colors duration-200 hover:text-tbc18-ink hover:bg-[color-mix(in_oklch,var(--color-tbc18-ink)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc18-focus focus-visible:outline-offset-3 focus-visible:text-tbc18-ink motion-reduce:transition-none"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="w-4 h-4 flex-none"><path d="M3 11.5 12 4l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg><span>Home</span></a></li>
      <li class="relative z-1 inline-flex items-center min-h-11 before:content-[''] before:inline-block before:w-2 before:h-2 before:mr-1.5 before:ml-0.5 before:rotate-45 before:opacity-70 before:border-r-[1.5px] before:border-t-[1.5px] before:border-tbc18-mut"><a href="#" class="relative inline-flex items-center gap-1.5 min-h-11 px-2.5 rounded-lg text-[15px] font-medium tracking-[0.01em] text-tbc18-mut no-underline transition-colors duration-200 hover:text-tbc18-ink hover:bg-[color-mix(in_oklch,var(--color-tbc18-ink)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc18-focus focus-visible:outline-offset-3 focus-visible:text-tbc18-ink motion-reduce:transition-none">Collections</a></li>
      <li class="relative z-1 inline-flex items-center min-h-11 before:content-[''] before:inline-block before:w-2 before:h-2 before:mr-1.5 before:ml-0.5 before:rotate-45 before:opacity-70 before:border-r-[1.5px] before:border-t-[1.5px] before:border-tbc18-mut"><a href="#" class="relative inline-flex items-center gap-1.5 min-h-11 px-2.5 rounded-lg text-[15px] font-medium tracking-[0.01em] text-tbc18-mut no-underline transition-colors duration-200 hover:text-tbc18-ink hover:bg-[color-mix(in_oklch,var(--color-tbc18-ink)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc18-focus focus-visible:outline-offset-3 focus-visible:text-tbc18-ink motion-reduce:transition-none">CryptoPunks</a></li>
      <li class="relative z-1 inline-flex items-center min-h-11 before:content-[''] before:inline-block before:w-2 before:h-2 before:mr-1.5 before:ml-0.5 before:rotate-45 before:opacity-70 before:border-r-[1.5px] before:border-t-[1.5px] before:border-tbc18-mut"><a href="#" aria-current="page" class="relative inline-flex items-center gap-1.5 min-h-11 px-2.5 rounded-t-lg text-[15px] font-semibold tracking-[0.01em] text-tbc18-ink no-underline bg-[color-mix(in_oklch,var(--color-tbc18-ink)_6%,transparent)] border-b-2 border-b-tbc18-holo focus-visible:outline-2 focus-visible:outline-tbc18-focus focus-visible:outline-offset-3">Punk #7804</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";
/* @property is what makes the conic angle animatable. There is no utility form —
   this registration is the whole reason the shimmer can rotate. */

@property --tbc18-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tbc18-card: #2b2a45;
  --color-tbc18-card: oklch(0.22 0.03 275 / 0.55);
  --color-tbc18-stroke: #6f6a95;
  --color-tbc18-stroke: oklch(0.78 0.05 280 / 0.22);
  --color-tbc18-ink: #eae6f5;
  --color-tbc18-ink: oklch(0.94 0.02 280);
  --color-tbc18-mut: #b0a8c4;
  --color-tbc18-mut: oklch(0.72 0.04 280);
  --color-tbc18-focus: #d08cf0;
  --color-tbc18-focus: oklch(0.82 0.18 300);
  --color-tbc18-holo: #e88fb4;
  --color-tbc18-holo: oklch(0.82 0.19 350);
  --font-tbc18-sans: 'Space Grotesk', ui-sans-serif, system-ui, sans-serif;
  --animate-tbc18-spin: tbc18-spin 6s linear infinite;
  --animate-tbc18-sweep: tbc18-sweep 3.6s ease-in-out infinite;
}

@keyframes tbc18-spin {
  to {
    --tbc18-angle: 360deg;
  }
}

@keyframes tbc18-sweep {
  0%,
    100% {
    transform: translateX(-8%);
  }

  50% {
    transform: translateX(8%);
  }
}

.tbc-18 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 backdrop-filter prefix. */

.tbc-18 ol {
  -webkit-backdrop-filter: blur(18px) saturate(140%);
}
/* The one relational rule kept in CSS: dimming every crumb except the hovered one
   would be an unreadable arbitrary variant, and it is genuinely a list-level rule. */

.tbc-18 ol:has(a:hover) a:not(:hover):not([aria-current="page"]) {
  color: color-mix(in oklch, var(--color-tbc18-mut) 80%, transparent);
}
```
