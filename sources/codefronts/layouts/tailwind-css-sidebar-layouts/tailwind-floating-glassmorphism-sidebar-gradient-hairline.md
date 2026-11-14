---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-floating-glassmorphism-sidebar-gradient-hairline/"
title: "Tailwind Floating Glassmorphism Sidebar with Gradient Hairline"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The elevated dashboard rail: detached on a 16px inset, frosted with backdrop-blur + backdrop-saturate, and finished with the gradient hairline that makes…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Glassmorphism Sidebar with Gradient Hairline
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-floating-glassmorphism-sidebar-gradient-hairline/

The elevated dashboard rail: detached on a 16px inset, frosted with backdrop-blur + backdrop-saturate, and finished with the gradient hairline that makes glass read as glass instead of grey plastic. The hairline is the one thing utilities cannot say &mdash; and the demo is honest about it.
## HTML
```html
<section class="tsl-16 w-full h-svh min-h-svh grid grid-cols-[auto_1fr] font-tsl16-sans text-tsl16-ink bg-[radial-gradient(55%_65%_at_18%_22%,oklch(0.45_0.16_300/0.65),transparent_60%),radial-gradient(50%_60%_at_85%_75%,oklch(0.5_0.15_220/0.55),transparent_65%),radial-gradient(40%_50%_at_65%_15%,oklch(0.55_0.12_170/0.35),transparent_60%),oklch(0.16_0.025_280)]">
  <aside aria-label="Main" class="tsl-16-glass w-[248px] m-4 flex flex-col gap-1 px-3.5 py-5 rounded-[20px] border border-transparent backdrop-blur-[18px] backdrop-saturate-150 shadow-[0_8px_32px_oklch(0_0_0/0.3),0_2px_8px_oklch(0_0_0/0.2)]">
    <div class="flex items-center gap-2.5 px-2.5 pt-1 pb-[18px] text-base font-bold tracking-tight"><span aria-hidden="true" class="w-[26px] h-[26px] rounded-lg bg-[conic-gradient(from_200deg,oklch(0.75_0.14_200),oklch(0.65_0.17_300),oklch(0.75_0.14_200))]"></span>Prism</div>
    <nav class="flex flex-col gap-[3px]">
      <a href="#" aria-current="page" class="flex items-center gap-3 min-h-11 px-3 rounded-xl text-sm font-medium text-tsl16-mut no-underline transition-colors duration-200 hover:text-tsl16-ink hover:bg-white/[0.09] aria-[current=page]:text-tsl16-ink aria-[current=page]:bg-white/[0.14] aria-[current=page]:shadow-[inset_0_1px_0_rgb(255_255_255/0.15)] focus-visible:outline-2 focus-visible:outline-tsl16-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg>Overview</a>
      <a href="#" class="flex items-center gap-3 min-h-11 px-3 rounded-xl text-sm font-medium text-tsl16-mut no-underline transition-colors duration-200 hover:text-tsl16-ink hover:bg-white/[0.09] focus-visible:outline-2 focus-visible:outline-tsl16-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M21 12a9 9 0 1 1-9-9"/><path d="M12 3a9 9 0 0 1 9 9h-9z"/></svg>Reports</a>
      <a href="#" class="flex items-center gap-3 min-h-11 px-3 rounded-xl text-sm font-medium text-tsl16-mut no-underline transition-colors duration-200 hover:text-tsl16-ink hover:bg-white/[0.09] focus-visible:outline-2 focus-visible:outline-tsl16-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5m1-13.5a3.5 3.5 0 0 1 0 7"/></svg>Audience</a>
      <a href="#" class="flex items-center gap-3 min-h-11 px-3 rounded-xl text-sm font-medium text-tsl16-mut no-underline transition-colors duration-200 hover:text-tsl16-ink hover:bg-white/[0.09] focus-visible:outline-2 focus-visible:outline-tsl16-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg>Settings</a>
    </nav>
    <div class="mt-auto grid gap-1.5 p-3.5 rounded-2xl bg-white/[0.08] border border-white/[0.14]">
      <strong class="text-[13.5px] font-bold">Prism Pro</strong>
      <small class="text-[11.5px] leading-snug text-tsl16-mut">Unlock cohort analysis</small>
      <button type="button" class="mt-1 min-h-11 px-3 rounded-[9px] border-0 bg-tsl16-accent text-tsl16-onaccent text-[12.5px] font-bold cursor-pointer transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Upgrade</button>
    </div>
  </aside>
  <main class="px-8 py-9 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Overview</h1>
    <p class="max-w-[48ch] text-sm leading-[1.65] text-tsl16-mut text-pretty">The rail floats on a 16px inset &mdash; frosted, gradient-edged, shadow-lifted. The aurora behind it is what the backdrop filter is sampling.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl16-ink: #f4f3f8;
  --color-tsl16-ink: oklch(0.96 0.005 280);
  --color-tsl16-mut: #c3c0cd;
  --color-tsl16-mut: oklch(0.82 0.02 280);
  --color-tsl16-accent: #57c9e0;
  --color-tsl16-accent: oklch(0.75 0.14 200);
  --color-tsl16-onaccent: #10222b;
  --color-tsl16-onaccent: oklch(0.18 0.03 220);
  --font-tsl16-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-16 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* The lit-glass hairline: two background layers with DIFFERENT clip boxes.
   Tailwind has bg-clip-* but not per-layer, so this stays CSS — and it is
   the difference between glass and grey plastic. */

.tsl-16-glass {
  background: linear-gradient(rgb(255 255 255 / 0.07), rgb(255 255 255 / 0.07)) padding-box, linear-gradient(160deg, rgb(255 255 255 / 0.5), rgb(255 255 255 / 0.12) 40%, rgb(255 255 255 / 0.03)) border-box;
  -webkit-backdrop-filter: blur(18px) saturate(1.5);
}
```
