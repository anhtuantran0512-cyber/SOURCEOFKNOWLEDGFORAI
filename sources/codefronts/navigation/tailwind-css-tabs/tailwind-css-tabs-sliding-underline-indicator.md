---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/tailwind-css-tabs-sliding-underline-indicator/"
title: "Tailwind CSS Tabs with Sliding Underline Indicator"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "The most-searched tab pattern: an ink underline that glides beneath the active tab."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Tabs with Sliding Underline Indicator
Source: https://codefronts.com/navigation/tailwind-css-tabs/tailwind-css-tabs-sliding-underline-indicator/

The most-searched tab pattern: an ink underline that glides beneath the active tab. The CSS original measured offsetLeft in JavaScript; the Tailwind port sets an index with has-[#ttb01-r2:checked]:[--i:1] and moves the bar with translate-x-[calc(var(--i)*100%)]. Zero JavaScript, no resize listener, and the panels fade in with starting:.
## HTML
```html
<section class="ttb-01 group/tabs grid min-h-svh w-full place-items-center bg-ttb01-bg px-5 py-14 font-ttb01-sans text-ttb01-ink" aria-label="Sliding underline tabs demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-xl overflow-hidden rounded-2xl bg-ttb01-card shadow-[0_1px_2px_rgb(35_28_72/0.06),0_16px_40px_-16px_rgb(35_28_72/0.22)] ring-1 ring-ttb01-ink/8">
      <div role="radiogroup" aria-label="Product sections" class="relative flex border-b border-ttb01-ink/10 px-2 [--i:0] has-[#ttb01-r2:checked]:[--i:1] has-[#ttb01-r3:checked]:[--i:2] has-[#ttb01-r4:checked]:[--i:3]">
        <label class="flex min-h-13 flex-1 cursor-pointer items-center justify-center gap-2 rounded-lg text-sm font-semibold text-ttb01-mut transition-colors hover:text-ttb01-ink has-checked:text-ttb01-ink has-focus-visible:outline-2 has-focus-visible:-outline-offset-4 has-focus-visible:outline-ttb01-ink"><input class="sr-only" type="radio" name="ttb01" id="ttb01-r1" checked>Overview</label>
        <label class="flex min-h-13 flex-1 cursor-pointer items-center justify-center gap-2 rounded-lg text-sm font-semibold text-ttb01-mut transition-colors hover:text-ttb01-ink has-checked:text-ttb01-ink has-focus-visible:outline-2 has-focus-visible:-outline-offset-4 has-focus-visible:outline-ttb01-ink"><input class="sr-only" type="radio" name="ttb01" id="ttb01-r2">Pricing</label>
        <label class="flex min-h-13 flex-1 cursor-pointer items-center justify-center gap-2 rounded-lg text-sm font-semibold text-ttb01-mut transition-colors hover:text-ttb01-ink has-checked:text-ttb01-ink has-focus-visible:outline-2 has-focus-visible:-outline-offset-4 has-focus-visible:outline-ttb01-ink"><input class="sr-only" type="radio" name="ttb01" id="ttb01-r3">Reviews <span class="rounded-full bg-ttb01-ink/8 px-1.5 py-0.5 font-ttb01-mono text-[10.5px] font-medium tabular-nums">128</span></label>
        <label class="flex min-h-13 flex-1 cursor-pointer items-center justify-center gap-2 rounded-lg text-sm font-semibold text-ttb01-mut transition-colors hover:text-ttb01-ink has-checked:text-ttb01-ink has-focus-visible:outline-2 has-focus-visible:-outline-offset-4 has-focus-visible:outline-ttb01-ink"><input class="sr-only" type="radio" name="ttb01" id="ttb01-r4">Support</label>
        <span aria-hidden="true" class="pointer-events-none absolute -bottom-px left-2 h-[3px] w-[calc((100%-16px)/4)] translate-x-[calc(var(--i)*100%)] rounded-t-full bg-ttb01-ink transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"></span>
      </div>
      <div class="px-6 py-5 text-[15px] leading-relaxed">
        <div class="hidden transition-[opacity,translate] duration-300 group-has-[#ttb01-r1:checked]/tabs:block starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><h3 class="font-semibold">Everything in one workspace</h3><p class="mt-1 text-ttb01-mut text-pretty">Plans, documents and conversations live side by side, so context never gets lost between tools.</p></div>
        <div class="hidden transition-[opacity,translate] duration-300 group-has-[#ttb01-r2:checked]/tabs:block starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><h3 class="font-semibold">Simple, per-seat pricing</h3><p class="mt-1 text-ttb01-mut text-pretty">One plan for small teams, one for organisations that need SSO and audit logs. Switch any time.</p></div>
        <div class="hidden transition-[opacity,translate] duration-300 group-has-[#ttb01-r3:checked]/tabs:block starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><h3 class="font-semibold">What teams are saying</h3><p class="mt-1 text-ttb01-mut text-pretty">Reviews from design, engineering and operations teams who moved their planning here.</p></div>
        <div class="hidden transition-[opacity,translate] duration-300 group-has-[#ttb01-r4:checked]/tabs:block starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><h3 class="font-semibold">Help when you need it</h3><p class="mt-1 text-ttb01-mut text-pretty">Guides, a searchable help centre and a human reply within one business day.</p></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb01-ink/10 bg-white/70 px-3.5 py-2 font-ttb01-mono text-[11.5px] text-ttb01-mut">has-[#r2:checked]:[--i:1] · translate-x-[calc(var(--i)*100%)] · 0 KB JS</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb01-bg: #f6f4ee;
  --color-ttb01-bg: oklch(0.967 0.008 91.5);
  --color-ttb01-card: #ffffff;
  --color-ttb01-card: oklch(1.000 0 0);
  --color-ttb01-ink: #231c48;
  --color-ttb01-ink: oklch(0.262 0.079 286.9);
  --color-ttb01-mut: #5c5876;
  --color-ttb01-mut: oklch(0.476 0.048 290.6);
  --font-ttb01-sans: 'Geist', system-ui, sans-serif;
  --font-ttb01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-01 {
  width: 100%;
  min-height: 100svh;
}
```
