---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-fill-wipe-button-hover-effect/"
title: "Tailwind Fill Wipe Button Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six directional fills — left wipe, diagonal slash, radial burst, curtain drop, centre split and an inset flood."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Fill Wipe Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-fill-wipe-button-hover-effect/

Six directional fills — left wipe, diagonal slash, radial burst, curtain drop, centre split and an inset flood. One pattern, six origin-* and transform pairings, which is exactly the kind of variation utilities are good at.
## HTML
```html
<section class="thv-10 w-full min-h-svh grid place-items-center bg-thv10-bg font-thv10-sans px-6 py-14">
  <div class="w-[min(860px,100%)] grid grid-cols-[repeat(auto-fit,minmax(230px,1fr))] gap-9">
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-8 py-3 rounded-md border-2 border-thv10-red bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv10-red cursor-pointer transition-colors duration-350 before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv10-red before:origin-left before:scale-x-0 before:transition-transform before:duration-350 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:before:scale-x-100 focus-visible:text-white focus-visible:before:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv10-red motion-reduce:before:transition-none"><span class="relative z-10">Left Wipe</span></button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv10-dim">scaleX from left</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-8 py-3 rounded-md border-2 border-thv10-rose bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv10-rose cursor-pointer transition-colors duration-400 before:content-[''] before:absolute before:-inset-[20%] before:-z-10 before:bg-thv10-rose before:origin-left before:-skew-x-[25deg] before:scale-x-0 before:transition-transform before:duration-500 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:before:scale-x-100 focus-visible:text-white focus-visible:before:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv10-rose motion-reduce:before:transition-none"><span class="relative z-10">Diagonal Slash</span></button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv10-dim">skew + scaleX</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-8 py-3 rounded-md border-2 border-thv10-orange bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv10-orange cursor-pointer transition-colors duration-350 before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv10-orange before:rounded-full before:scale-0 before:transition-transform before:duration-450 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:before:scale-[3] focus-visible:text-white focus-visible:before:scale-[3] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv10-orange motion-reduce:before:transition-none"><span class="relative z-10">Radial Burst</span></button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv10-dim">scale from center</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-8 py-3 rounded-md border-2 border-thv10-coral bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv10-coral cursor-pointer transition-colors duration-350 before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv10-coral before:origin-top before:scale-y-0 before:transition-transform before:duration-350 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:before:scale-y-100 focus-visible:text-white focus-visible:before:scale-y-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv10-coral motion-reduce:before:transition-none"><span class="relative z-10">Curtain Drop</span></button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv10-dim">scaleY from top</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-8 py-3 rounded-md border-2 border-thv10-crimson bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv10-crimson cursor-pointer transition-colors duration-350 before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv10-crimson before:origin-center before:scale-x-0 before:transition-transform before:duration-350 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:before:scale-x-100 focus-visible:text-white focus-visible:before:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv10-crimson motion-reduce:before:transition-none"><span class="relative z-10">Center Split</span></button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv10-dim">scaleX outward</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 rounded-md border-2 border-thv10-red bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv10-red cursor-pointer shadow-[inset_0_0_0_0_var(--color-thv10-red)] transition-[box-shadow,color] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:shadow-[inset_0_0_0_60px_var(--color-thv10-red)] focus-visible:text-white focus-visible:shadow-[inset_0_0_0_60px_var(--color-thv10-red)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv10-red motion-reduce:transition-none">Inset Grow</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv10-dim">box-shadow inset fill</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv10-bg: #0f0400;
  --color-thv10-bg: oklch(0.13 0.03 40);
  --color-thv10-dim: #6b7280;
  --color-thv10-dim: oklch(0.55 0.02 265);
  --color-thv10-red: #ef4444;
  --color-thv10-red: oklch(0.64 0.21 25);
  --color-thv10-rose: #f43f5e;
  --color-thv10-rose: oklch(0.65 0.23 16);
  --color-thv10-orange: #f97316;
  --color-thv10-orange: oklch(0.7 0.19 45);
  --color-thv10-coral: #fb923c;
  --color-thv10-coral: oklch(0.76 0.15 55);
  --color-thv10-crimson: #dc2626;
  --color-thv10-crimson: oklch(0.58 0.22 27);
  --font-thv10-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-10 {
  width: 100%;
  min-height: 100svh;
}

.thv-10 ::selection {
  background: var(--color-thv10-crimson);
  color: #fff;
}
```
