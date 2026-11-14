---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-stack-lift-card-hover-effect/"
title: "Tailwind Stack Lift Card Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four depth studies — single lift with shadow bloom, deck fan-out, a cascade of columns and a group that dims every card except the one you are on."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stack Lift Card Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-stack-lift-card-hover-effect/

Four depth studies — single lift with shadow bloom, deck fan-out, a cascade of columns and a group that dims every card except the one you are on. The last one is the port's most interesting: group-hover:opacity-35 plus hover:opacity-100 on the same element.
## HTML
```html
<section class="thv-18 w-full min-h-svh grid place-items-center bg-thv18-bg font-thv18-sans px-6 py-14">
  <div class="w-[min(880px,100%)] grid grid-cols-[repeat(auto-fit,minmax(300px,1fr))] gap-10">

    <div class="flex flex-col items-center gap-5 px-6 py-10 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <div class="pb-6">
        <a href="#" class="block w-[248px] text-left rounded-xl overflow-hidden bg-white/[0.04] border border-white/10 shadow-[0_4px_12px_rgba(0,0,0,.3)] no-underline cursor-pointer transition-[transform,translate,scale,rotate,box-shadow] duration-350 ease-[cubic-bezier(.4,0,.2,1)] hover:-translate-y-[14px] hover:shadow-[0_28px_56px_rgba(0,0,0,.5),0_0_24px_rgba(16,185,129,.2)] focus-visible:-translate-y-[14px] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv18-green motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:hover:border-thv18-green">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80" alt="Sunlit living room with a pale sectional sofa" decoding="async" class="w-full aspect-[4/3] object-cover">
          <span class="flex flex-col gap-1.5 p-5">
            <span class="flex items-baseline justify-between gap-3">
              <span class="text-[0.95rem] font-bold text-thv18-text">Cedar House</span>
              <span class="text-[0.95rem] font-bold text-thv18-green">$248<span class="text-[0.72rem] font-medium text-thv18-dim"> / night</span></span>
            </span>
            <span class="text-[0.8rem] leading-snug text-thv18-dim">Sonoma, California · Sleeps 4 · Free cancellation</span>
          </span>
        </a>
      </div>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv18-dim">listing card — shadow bloom lift</span>
    </div>

    <div class="flex flex-col items-center gap-5 px-6 py-10 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" aria-label="Open saved collection: Coastal Escapes, 3 stays" class="group relative block w-[210px] h-[190px] bg-transparent border-0 p-0 cursor-pointer rounded-xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv18-green">
        <span class="absolute inset-0 z-30 block overflow-hidden rounded-xl border border-white/10 transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:-translate-y-3 group-focus-visible:-translate-y-3 motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=600&q=80" alt="Contemporary white villa behind a manicured lawn" decoding="async" class="absolute inset-0 w-full h-full object-cover">
          <span class="absolute inset-x-0 bottom-0 flex flex-col gap-0.5 px-4 pt-10 pb-3.5 text-left bg-[linear-gradient(to_top,rgba(2,12,8,.92),transparent)]">
            <span class="text-[0.95rem] font-bold text-thv18-text">Coastal Escapes</span>
            <span class="text-[0.75rem] text-thv18-dim">3 saved stays</span>
          </span>
        </span>
        <span aria-hidden="true" class="absolute inset-0 z-20 translate-y-2 overflow-hidden rounded-xl border border-white/10 transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:translate-y-1 group-focus-visible:translate-y-1 motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=600&q=80" alt="" decoding="async" class="w-full h-full object-cover opacity-70">
        </span>
        <span aria-hidden="true" class="absolute inset-0 z-10 translate-y-4 overflow-hidden rounded-xl border border-white/10 transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:translate-y-5 group-focus-visible:translate-y-5 motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=600&q=80" alt="" decoding="async" class="w-full h-full object-cover opacity-50">
        </span>
      </button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv18-dim">saved collection — fan-out</span>
    </div>

    <div class="flex flex-col items-center gap-5 px-6 py-10 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <div class="flex items-end gap-2.5">
        <button type="button" aria-label="View photo 1 of 3: kitchen" class="relative block w-[76px] h-24 p-0 overflow-hidden rounded-xl border border-white/10 bg-transparent cursor-pointer transition-[transform,translate,scale,rotate,box-shadow] duration-350 ease-[cubic-bezier(.4,0,.2,1)] hover:-translate-y-2.5 hover:shadow-[0_12px_30px_rgba(0,0,0,.4)] focus-visible:-translate-y-2.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv18-teal motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=600&q=80" alt="" decoding="async" class="absolute inset-0 w-full h-full object-cover">
          <span class="absolute bottom-1.5 left-1.5 px-1.5 py-0.5 rounded-md text-[11px] font-bold text-thv18-text bg-black/65">01</span>
        </button>
        <button type="button" aria-label="View photo 2 of 3: lounge" class="relative block w-[76px] h-[118px] p-0 overflow-hidden rounded-xl border border-white/10 bg-transparent cursor-pointer transition-[transform,translate,scale,rotate,box-shadow] duration-350 ease-[cubic-bezier(.4,0,.2,1)] hover:-translate-y-[14px] hover:shadow-[0_16px_36px_rgba(0,0,0,.4)] focus-visible:-translate-y-[14px] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv18-green motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=600&q=80" alt="" decoding="async" class="absolute inset-0 w-full h-full object-cover">
          <span class="absolute bottom-1.5 left-1.5 px-1.5 py-0.5 rounded-md text-[11px] font-bold text-thv18-text bg-black/65">02</span>
        </button>
        <button type="button" aria-label="View photo 3 of 3: exterior" class="relative block w-[76px] h-[140px] p-0 overflow-hidden rounded-xl border border-white/10 bg-transparent cursor-pointer transition-[transform,translate,scale,rotate,box-shadow] duration-350 ease-[cubic-bezier(.4,0,.2,1)] hover:-translate-y-[18px] hover:shadow-[0_20px_40px_rgba(0,0,0,.4)] focus-visible:-translate-y-[18px] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv18-emerald motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=600&q=80" alt="" decoding="async" class="absolute inset-0 w-full h-full object-cover">
          <span class="absolute bottom-1.5 left-1.5 px-1.5 py-0.5 rounded-md text-[11px] font-bold text-thv18-text bg-black/65">03</span>
        </button>
      </div>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv18-dim">gallery strip — cascade z-lift</span>
    </div>

    <div class="flex flex-col items-center gap-5 px-6 py-10 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <div class="group flex gap-2.5">
        <button type="button" class="relative block w-[82px] h-[104px] p-0 overflow-hidden rounded-xl border border-thv18-green/30 bg-transparent cursor-pointer transition-[transform,translate,scale,rotate,opacity,box-shadow] duration-300 group-hover:opacity-35 group-hover:scale-95 hover:opacity-100! hover:scale-100 hover:-translate-y-2.5 hover:shadow-[0_16px_36px_rgba(0,0,0,.4)] focus-visible:opacity-100! focus-visible:-translate-y-2.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv18-green motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=600&q=80" alt="" decoding="async" class="absolute inset-0 w-full h-full object-cover">
          <span class="absolute inset-x-0 bottom-0 px-2 pt-6 pb-2 text-[11px] font-bold tracking-wide text-thv18-text bg-[linear-gradient(to_top,rgba(2,12,8,.92),transparent)]">Suite</span>
        </button>
        <button type="button" class="relative block w-[82px] h-[104px] p-0 overflow-hidden rounded-xl border border-thv18-green/30 bg-transparent cursor-pointer transition-[transform,translate,scale,rotate,opacity,box-shadow] duration-300 group-hover:opacity-35 group-hover:scale-95 hover:opacity-100! hover:scale-100 hover:-translate-y-2.5 hover:shadow-[0_16px_36px_rgba(0,0,0,.4)] focus-visible:opacity-100! focus-visible:-translate-y-2.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv18-green motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&w=600&q=80" alt="" decoding="async" class="absolute inset-0 w-full h-full object-cover">
          <span class="absolute inset-x-0 bottom-0 px-2 pt-6 pb-2 text-[11px] font-bold tracking-wide text-thv18-text bg-[linear-gradient(to_top,rgba(2,12,8,.92),transparent)]">Loft</span>
        </button>
        <button type="button" class="relative block w-[82px] h-[104px] p-0 overflow-hidden rounded-xl border border-thv18-green/30 bg-transparent cursor-pointer transition-[transform,translate,scale,rotate,opacity,box-shadow] duration-300 group-hover:opacity-35 group-hover:scale-95 hover:opacity-100! hover:scale-100 hover:-translate-y-2.5 hover:shadow-[0_16px_36px_rgba(0,0,0,.4)] focus-visible:opacity-100! focus-visible:-translate-y-2.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv18-green motion-reduce:transition-none">
          <img src="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=600&q=80" alt="" decoding="async" class="absolute inset-0 w-full h-full object-cover">
          <span class="absolute inset-x-0 bottom-0 px-2 pt-6 pb-2 text-[11px] font-bold tracking-wide text-thv18-text bg-[linear-gradient(to_top,rgba(2,12,8,.92),transparent)]">Villa</span>
        </button>
      </div>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv18-dim">room picker — group isolation</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv18-bg: #020c08;
  --color-thv18-bg: oklch(0.13 0.02 165);
  --color-thv18-text: #d1fae5;
  --color-thv18-text: oklch(0.94 0.05 160);
  --color-thv18-dim: #93a99f;
  --color-thv18-dim: oklch(0.71 0.02 165);
  --color-thv18-green: #10b981;
  --color-thv18-green: oklch(0.7 0.15 163);
  --color-thv18-teal: #14b8a6;
  --color-thv18-teal: oklch(0.72 0.13 180);
  --color-thv18-emerald: #059669;
  --color-thv18-emerald: oklch(0.6 0.13 163);
  --font-thv18-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-18 {
  width: 100%;
  min-height: 100svh;
}

.thv-18 ::selection {
  background: var(--color-thv18-emerald);
  color: #fff;
}
```
