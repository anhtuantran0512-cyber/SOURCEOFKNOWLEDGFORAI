---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-saas-gradient-text-breadcrumb-animated-clip/"
title: "Tailwind SaaS Gradient-Text Breadcrumb Bar with Animated Clip"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The marketing-site trail: crumb labels painted with a slowly drifting conic gradient clipped to the text, on a frosted white bar."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS Gradient-Text Breadcrumb Bar with Animated Clip
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-saas-gradient-text-breadcrumb-animated-clip/

The marketing-site trail: crumb labels painted with a slowly drifting conic gradient clipped to the text, on a frosted white bar. Hover speeds the drift and draws a gradient rule under the label. bg-clip-text text-transparent is a real Tailwind pair, so only the angle registration and keyframes stay CSS.
## HTML
```html
<section class="tbc-19 w-full min-h-svh flex items-center justify-center px-6 py-10 font-tbc19-sans text-tbc19-ink bg-[radial-gradient(1200px_600px_at_50%_-10%,oklch(0.96_0.02_270/0.9),transparent_60%),linear-gradient(180deg,oklch(0.99_0.005_260),oklch(0.97_0.01_265))]">
  <nav aria-label="Breadcrumb" class="w-full max-w-[880px] px-5.5 py-3.5 rounded-2xl bg-white/72 backdrop-blur-[14px] border border-tbc19-edge shadow-[inset_0_1px_0_oklch(1_0_0/0.9),0_12px_40px_-18px_oklch(0.3_0.05_270/0.35)]">
    <ol class="flex flex-wrap items-center gap-x-1 gap-y-0.5 list-none m-0 p-0 text-[15px] font-medium tracking-[-0.005em]">
      <li class="inline-flex items-center min-h-11"><a href="#" class="relative inline-flex items-center min-h-11 px-2 rounded-lg no-underline bg-clip-text text-transparent bg-[conic-gradient(from_var(--tbc19-angle),oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.72_0.2_25),oklch(0.7_0.2_190),oklch(0.62_0.2_285))] animate-tbc19-drift transition-[filter] duration-250 hover:[animation-duration:6s] hover:[filter:saturate(1.15)] focus-visible:[animation-duration:6s] focus-visible:outline-2 focus-visible:outline-tbc19-focus focus-visible:outline-offset-3 after:content-[''] after:absolute after:inset-x-2 after:bottom-1 after:h-[1.5px] after:rounded-[2px] after:opacity-0 after:scale-x-40 after:origin-left after:transition-[opacity,scale] after:duration-300 after:bg-[conic-gradient(from_var(--tbc19-angle),oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.72_0.2_25),oklch(0.7_0.2_190),oklch(0.62_0.2_285))] hover:after:opacity-85 hover:after:scale-x-100 focus-visible:after:opacity-85 focus-visible:after:scale-x-100 motion-reduce:animate-none motion-reduce:bg-linear-[90deg,oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.66_0.24_20)]">Docs</a></li>
      <li class="inline-flex items-center min-h-11 before:content-[''] before:inline-block before:w-1.5 before:h-1.5 before:mx-2.5 before:rotate-[-45deg] before:opacity-70 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tbc19-sep"><a href="#" class="relative inline-flex items-center min-h-11 px-2 rounded-lg no-underline bg-clip-text text-transparent bg-[conic-gradient(from_var(--tbc19-angle),oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.72_0.2_25),oklch(0.7_0.2_190),oklch(0.62_0.2_285))] animate-tbc19-drift transition-[filter] duration-250 hover:[animation-duration:6s] hover:[filter:saturate(1.15)] focus-visible:[animation-duration:6s] focus-visible:outline-2 focus-visible:outline-tbc19-focus focus-visible:outline-offset-3 after:content-[''] after:absolute after:inset-x-2 after:bottom-1 after:h-[1.5px] after:rounded-[2px] after:opacity-0 after:scale-x-40 after:origin-left after:transition-[opacity,scale] after:duration-300 after:bg-[conic-gradient(from_var(--tbc19-angle),oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.72_0.2_25),oklch(0.7_0.2_190),oklch(0.62_0.2_285))] hover:after:opacity-85 hover:after:scale-x-100 focus-visible:after:opacity-85 focus-visible:after:scale-x-100 motion-reduce:animate-none motion-reduce:bg-linear-[90deg,oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.66_0.24_20)]">Guides</a></li>
      <li class="inline-flex items-center min-h-11 before:content-[''] before:inline-block before:w-1.5 before:h-1.5 before:mx-2.5 before:rotate-[-45deg] before:opacity-70 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tbc19-sep"><a href="#" class="relative inline-flex items-center min-h-11 px-2 rounded-lg no-underline bg-clip-text text-transparent bg-[conic-gradient(from_var(--tbc19-angle),oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.72_0.2_25),oklch(0.7_0.2_190),oklch(0.62_0.2_285))] animate-tbc19-drift transition-[filter] duration-250 hover:[animation-duration:6s] hover:[filter:saturate(1.15)] focus-visible:[animation-duration:6s] focus-visible:outline-2 focus-visible:outline-tbc19-focus focus-visible:outline-offset-3 after:content-[''] after:absolute after:inset-x-2 after:bottom-1 after:h-[1.5px] after:rounded-[2px] after:opacity-0 after:scale-x-40 after:origin-left after:transition-[opacity,scale] after:duration-300 after:bg-[conic-gradient(from_var(--tbc19-angle),oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.72_0.2_25),oklch(0.7_0.2_190),oklch(0.62_0.2_285))] hover:after:opacity-85 hover:after:scale-x-100 focus-visible:after:opacity-85 focus-visible:after:scale-x-100 motion-reduce:animate-none motion-reduce:bg-linear-[90deg,oklch(0.62_0.2_285),oklch(0.68_0.22_320),oklch(0.66_0.24_20)]">Authentication</a></li>
      <li class="inline-flex items-center min-h-11 before:content-[''] before:inline-block before:w-1.5 before:h-1.5 before:mx-2.5 before:rotate-[-45deg] before:opacity-70 before:border-r-[1.5px] before:border-b-[1.5px] before:border-tbc19-sep"><a href="#" aria-current="page" class="relative inline-flex items-center min-h-11 px-2 rounded-lg no-underline font-bold bg-clip-text text-transparent bg-[conic-gradient(from_var(--tbc19-angle),oklch(0.6_0.24_300),oklch(0.68_0.24_340),oklch(0.72_0.22_20),oklch(0.66_0.24_275),oklch(0.6_0.24_300))] animate-tbc19-drift [animation-duration:7s] focus-visible:outline-2 focus-visible:outline-tbc19-focus focus-visible:outline-offset-3 motion-reduce:animate-none motion-reduce:bg-linear-[90deg,oklch(0.6_0.24_300),oklch(0.68_0.24_340),oklch(0.66_0.24_275)]">Magic Links</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tbc19-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@theme {
  --color-tbc19-ink: #3b3f4d;
  --color-tbc19-ink: oklch(0.28 0.02 260);
  --color-tbc19-edge: #e2e4ee;
  --color-tbc19-edge: oklch(0.9 0.01 260 / 0.7);
  --color-tbc19-sep: #b3b6c2;
  --color-tbc19-sep: oklch(0.75 0.02 260);
  --color-tbc19-focus: #7a5cf0;
  --color-tbc19-focus: oklch(0.62 0.2 285);
  --font-tbc19-sans: 'Space Grotesk', ui-sans-serif, system-ui, sans-serif;
  --animate-tbc19-drift: tbc19-drift 18s linear infinite;
}

@keyframes tbc19-drift {
  to {
    --tbc19-angle: 360deg;
  }
}

.tbc-19 {
  width: 100%;
  min-height: 100svh;
}
```
