---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-tooltip-popover/"
title: "Tailwind Liquid Glass Tooltip Popover"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A capsule tooltip that frosts the text behind it instead of hiding it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Tooltip Popover
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-tooltip-popover/

A capsule tooltip that frosts the text behind it instead of hiding it. The port's discipline is the pairing: every group-hover: has a group-focus-visible: twin, so the hint is reachable by keyboard &mdash; the single most commonly skipped requirement in tooltip components.
## HTML
```html
<section class="lgt-11 grid w-full min-h-svh place-items-center px-6 py-15 font-lgt11-sans bg-[image:url('https://picsum.photos/seed/lgtip/1100/800')] bg-cover bg-center bg-fixed" aria-label="Tailwind liquid glass tooltip demo">
  <p class="max-w-[44ch] text-center text-[22px] leading-loose text-white [text-shadow:0_1px_10px_rgba(0,0,0,.5)]">
    Your plan renews on the
    <span tabindex="0" class="group relative cursor-help font-extrabold text-lgt11-accent outline-none border-b-2 border-dotted border-white/50 focus-visible:rounded focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">14th<span role="tooltip" class="pointer-events-none invisible absolute bottom-[calc(100%+12px)] left-1/2 z-5 w-max max-w-[220px] -translate-x-1/2 translate-y-1.5 rounded-[14px] border border-white/40 bg-white/16 px-3.25 py-2.25 text-[13px] font-semibold leading-snug text-white opacity-0 backdrop-blur-[16px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_16px_34px_-18px_rgba(0,0,0,.7)] transition-[opacity,transform,visibility] duration-250 [text-shadow:none] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-visible:visible group-focus-visible:translate-y-0 group-focus-visible:opacity-100 motion-reduce:transition-[opacity,visibility] after:absolute after:top-full after:left-1/2 after:size-3 after:-translate-x-1/2 after:-translate-y-[5px] after:rotate-45 after:border-r after:border-b after:border-white/40 after:bg-inherit">Auto-renews &middot; cancel anytime up to 24h before</span></span>.
    You've used
    <span tabindex="0" class="group relative cursor-help font-extrabold text-lgt11-accent outline-none border-b-2 border-dotted border-white/50 focus-visible:rounded focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">68%<span role="tooltip" class="pointer-events-none invisible absolute bottom-[calc(100%+12px)] left-1/2 z-5 w-max max-w-[220px] -translate-x-1/2 translate-y-1.5 rounded-[14px] border border-white/40 bg-white/16 px-3.25 py-2.25 text-[13px] font-semibold leading-snug text-white opacity-0 backdrop-blur-[16px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_16px_34px_-18px_rgba(0,0,0,.7)] transition-[opacity,transform,visibility] duration-250 [text-shadow:none] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-visible:visible group-focus-visible:translate-y-0 group-focus-visible:opacity-100 motion-reduce:transition-[opacity,visibility] after:absolute after:top-full after:left-1/2 after:size-3 after:-translate-x-1/2 after:-translate-y-[5px] after:rotate-45 after:border-r after:border-b after:border-white/40 after:bg-inherit">34 GB of your 50 GB quota</span></span>
    of storage this cycle, and
    <span tabindex="0" class="group relative cursor-help font-extrabold text-lgt11-accent outline-none border-b-2 border-dotted border-white/50 focus-visible:rounded focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">3 seats<span role="tooltip" class="pointer-events-none invisible absolute bottom-[calc(100%+12px)] left-1/2 z-5 w-max max-w-[220px] -translate-x-1/2 translate-y-1.5 rounded-[14px] border border-white/40 bg-white/16 px-3.25 py-2.25 text-[13px] font-semibold leading-snug text-white opacity-0 backdrop-blur-[16px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_16px_34px_-18px_rgba(0,0,0,.7)] transition-[opacity,transform,visibility] duration-250 [text-shadow:none] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-visible:visible group-focus-visible:translate-y-0 group-focus-visible:opacity-100 motion-reduce:transition-[opacity,visibility] after:absolute after:top-full after:left-1/2 after:size-3 after:-translate-x-1/2 after:-translate-y-[5px] after:rotate-45 after:border-r after:border-b after:border-white/40 after:bg-inherit">2 active, 1 pending invite</span></span>
    are assigned.
  </p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt11-accent: #7fd7ea;
  --color-lgt11-accent: oklch(0.85 0.13 200);
  --font-lgt11-sans: 'Manrope', system-ui, sans-serif;
}
```
