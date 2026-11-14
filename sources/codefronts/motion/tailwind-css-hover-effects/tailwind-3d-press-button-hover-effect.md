---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-3d-press-button-hover-effect/"
title: "Tailwind 3D Press Button Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six buttons with real depth — push-down platform, colour-graduated extrusion, isometric offset, carved emboss, chamfered bevel and a neumorphic pillow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Press Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-3d-press-button-hover-effect/

Six buttons with real depth — push-down platform, colour-graduated extrusion, isometric offset, carved emboss, chamfered bevel and a neumorphic pillow. The shadow stack and the translate-y that must match it finally live in the same class list.
## HTML
```html
<section class="thv-11 w-full min-h-svh grid place-items-center bg-thv11-bg font-thv11-sans px-6 py-14">
  <div class="w-[min(860px,100%)] grid grid-cols-[repeat(auto-fit,minmax(230px,1fr))] gap-9">
    <div class="flex flex-col items-center gap-5 px-5 py-12 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 rounded-lg border-0 bg-thv11-blue text-[0.95rem] font-bold tracking-[0.05em] text-white cursor-pointer shadow-[0_6px_0_var(--color-thv11-navy)] transition-[transform,box-shadow] duration-100 hover:translate-y-[3px] hover:shadow-[0_3px_0_var(--color-thv11-navy)] focus-visible:translate-y-[3px] focus-visible:shadow-[0_3px_0_var(--color-thv11-navy)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv11-blue active:translate-y-[6px] active:shadow-[0_0_0_var(--color-thv11-navy)] motion-reduce:transition-none">Push Down</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv11-dim">shadow shrink press</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-12 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 rounded-lg border-0 bg-thv11-amber text-[0.95rem] font-bold tracking-[0.05em] text-black cursor-pointer shadow-[0_2px_0_#b45309,0_4px_0_#9a3412,0_6px_0_#7c2d12,0_8px_0_#5a1a08,0_10px_0_#3d1004,0_14px_18px_rgba(0,0,0,.55)] transition-[transform,box-shadow] duration-100 hover:translate-y-[8px] hover:shadow-[0_1px_0_#b45309,0_2px_0_#9a3412,0_3px_6px_rgba(0,0,0,.5)] focus-visible:translate-y-[8px] focus-visible:shadow-[0_1px_0_#b45309,0_2px_0_#9a3412,0_3px_6px_rgba(0,0,0,.5)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv11-amber motion-reduce:transition-none">Extrude</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv11-dim">stacked shadow layers</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-12 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 rounded-lg border-0 bg-thv11-green text-[0.95rem] font-bold tracking-[0.05em] text-white cursor-pointer shadow-[4px_4px_0_#065f46,5px_5px_0_#064e3b] transition-[transform,box-shadow] duration-100 hover:translate-x-1 hover:translate-y-1 hover:shadow-[0_0_0_#065f46] focus-visible:translate-x-1 focus-visible:translate-y-1 focus-visible:shadow-[0_0_0_#065f46] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv11-green motion-reduce:transition-none">Isometric</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv11-dim">angled depth edge</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-12 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 rounded-lg border-0 bg-[#1f2937] text-[0.95rem] font-bold tracking-[0.05em] text-[#9ca3af] cursor-pointer [text-shadow:0_-1px_0_#000,0_1px_0_rgba(255,255,255,.08)] shadow-[inset_0_3px_6px_rgba(0,0,0,.7),inset_0_-2px_4px_rgba(0,0,0,.5),inset_0_1px_0_rgba(255,255,255,.06)] transition-[color,box-shadow] duration-150 hover:text-[#e5e7eb] hover:shadow-[inset_0_4px_10px_rgba(0,0,0,.9),inset_0_-3px_6px_rgba(0,0,0,.6),inset_0_1px_0_rgba(255,255,255,.04)] focus-visible:text-[#e5e7eb] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv11-slate motion-reduce:transition-none">Embossed</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv11-dim">groove press</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-12 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 rounded-lg border-0 text-[0.95rem] font-bold tracking-[0.05em] text-white cursor-pointer bg-[linear-gradient(180deg,#8b5cf6_0%,#7c3aed_50%,#5b21b6_100%)] [text-shadow:0_-1px_0_rgba(0,0,0,.4)] shadow-[inset_0_3px_0_rgba(255,255,255,.4),inset_3px_0_0_rgba(255,255,255,.15),inset_-3px_0_0_rgba(0,0,0,.25),inset_0_-4px_0_rgba(0,0,0,.45),0_4px_0_#3c1a78,0_6px_8px_rgba(0,0,0,.4)] transition-[transform,box-shadow,background] duration-100 hover:translate-y-0.5 hover:bg-[linear-gradient(180deg,#7c3aed_0%,#6d28d9_50%,#4c1d95_100%)] hover:shadow-[inset_0_2px_0_rgba(255,255,255,.25),inset_0_-3px_0_rgba(0,0,0,.5),0_2px_0_#3c1a78,0_3px_4px_rgba(0,0,0,.4)] focus-visible:translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv11-violet motion-reduce:transition-none">Beveled</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv11-dim">inset bevel edges</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-12 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 rounded-lg border-0 bg-[#e2e8f0] text-[0.95rem] font-bold tracking-[0.05em] text-[#334155] cursor-pointer shadow-[5px_5px_10px_#b8bec9,-5px_-5px_10px_#ffffff] transition-shadow duration-150 hover:shadow-[inset_4px_4px_8px_#b8bec9,inset_-4px_-4px_8px_#ffffff] focus-visible:shadow-[inset_4px_4px_8px_#b8bec9,inset_-4px_-4px_8px_#ffffff] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv11-slate motion-reduce:transition-none">Neumorphic</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv11-dim">concave surface</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv11-bg: #0b0f1a;
  --color-thv11-bg: oklch(0.15 0.02 265);
  --color-thv11-dim: #475569;
  --color-thv11-dim: oklch(0.45 0.03 257);
  --color-thv11-blue: #3b82f6;
  --color-thv11-blue: oklch(0.64 0.19 258);
  --color-thv11-navy: #1d4ed8;
  --color-thv11-navy: oklch(0.49 0.22 264);
  --color-thv11-amber: #f59e0b;
  --color-thv11-amber: oklch(0.77 0.16 70);
  --color-thv11-green: #10b981;
  --color-thv11-green: oklch(0.7 0.15 163);
  --color-thv11-violet: #8b5cf6;
  --color-thv11-violet: oklch(0.63 0.21 295);
  --color-thv11-slate: #94a3b8;
  --color-thv11-slate: oklch(0.7 0.03 257);
  --font-thv11-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-11 {
  width: 100%;
  min-height: 100svh;
}

.thv-11 ::selection {
  background: var(--color-thv11-navy);
  color: #fff;
}
```
