---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-frosted-glass-dark-ui-breadcrumb-component/"
title: "Tailwind Frosted Glass Dark UI Breadcrumb Component"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The dark counterpart to the glassmorphism pill: a translucent charcoal panel over a moody gradient, with a lit top edge, a darkened bottom edge, and cool…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Frosted Glass Dark UI Breadcrumb Component
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-frosted-glass-dark-ui-breadcrumb-component/

The dark counterpart to the glassmorphism pill: a translucent charcoal panel over a moody gradient, with a lit top edge, a darkened bottom edge, and cool accent links. Asymmetric border colours do the lighting, which is the detail that separates dark glass from a grey box.
## HTML
```html
<section class="tbc-38 w-full min-h-svh flex items-center justify-center font-tbc38-sans px-8 py-12 bg-[radial-gradient(120%_140%_at_20%_0%,oklch(0.32_0.09_280),oklch(0.14_0.03_260)_55%,oklch(0.1_0.02_240))]">
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center list-none m-0 px-4 py-2.75 rounded-[15px] bg-tbc38-panel border border-tbc38-edge border-b-tbc38-edgedark [backdrop-filter:blur(14px)_saturate(160%)] shadow-[0_10px_40px_oklch(0_0_0/0.4),inset_0_1px_0_oklch(1_0_0/0.12)]">
      <li class="flex items-center"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-[9px] text-sm font-medium text-tbc38-ink no-underline transition-colors duration-200 hover:text-white hover:bg-tbc38-hover focus-visible:outline-2 focus-visible:outline-tbc38-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Studio</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2.25 before:text-tbc38-sep"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-[9px] text-sm font-medium text-tbc38-ink no-underline transition-colors duration-200 hover:text-white hover:bg-tbc38-hover focus-visible:outline-2 focus-visible:outline-tbc38-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Sessions</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2.25 before:text-tbc38-sep"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-[9px] text-sm font-medium text-tbc38-ink no-underline transition-colors duration-200 hover:text-white hover:bg-tbc38-hover focus-visible:outline-2 focus-visible:outline-tbc38-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Mixes</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2.25 before:text-tbc38-sep"><a href="#" aria-current="page" class="flex items-center min-h-9 px-2.5 rounded-[9px] text-sm font-semibold text-white no-underline bg-[color-mix(in_oklab,var(--color-tbc38-acc)_26%,var(--color-tbc38-solid))] shadow-[inset_0_1px_0_oklch(1_0_0/0.15)] focus-visible:outline-2 focus-visible:outline-tbc38-acc focus-visible:outline-offset-2">Midnight Set</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc38-panel: #2b2e3a;
  --color-tbc38-panel: oklch(0.2 0.02 265 / 0.55);
  --color-tbc38-solid: #33374a;
  --color-tbc38-solid: oklch(0.25 0.02 265);
  --color-tbc38-edge: #4e5361;
  --color-tbc38-edge: oklch(0.35 0.02 265 / 0.5);
  --color-tbc38-edgedark: #101218;
  --color-tbc38-edgedark: oklch(0.08 0.01 265 / 0.6);
  --color-tbc38-ink: #d8dae2;
  --color-tbc38-ink: oklch(0.88 0.02 265);
  --color-tbc38-hover: #4d5260;
  --color-tbc38-hover: oklch(0.4 0.02 265 / 0.5);
  --color-tbc38-sep: #8b909d;
  --color-tbc38-sep: oklch(0.63 0.02 265);
  --color-tbc38-acc: #63c8dc;
  --color-tbc38-acc: oklch(0.72 0.15 200);
  --font-tbc38-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-38 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 backdrop-filter prefix. */

.tbc-38 ol {
  -webkit-backdrop-filter: blur(14px) saturate(160%);
}
```
