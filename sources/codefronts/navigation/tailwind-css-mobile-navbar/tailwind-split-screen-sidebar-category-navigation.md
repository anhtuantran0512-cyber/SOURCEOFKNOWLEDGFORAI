---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-split-screen-sidebar-category-navigation/"
title: "Tailwind Split-Screen Sidebar Category Navigation"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A two-pane shop layout: a 104px category rail with an active edge indicator, and a content panel that fades and slides as you switch."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split-Screen Sidebar Category Navigation
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-split-screen-sidebar-category-navigation/

A two-pane shop layout: a 104px category rail with an active edge indicator, and a content panel that fades and slides as you switch. The whole phone re-tints per category &mdash; violet, green, red, blue &mdash; with a colour transition the original could not animate. Zero JavaScript.
## HTML
```html
<section class="tmn-14 w-full min-h-svh grid place-items-center bg-tmn14-stage px-4 py-6 font-tmn14-sans antialiased" aria-label="Tailwind split-screen category navigation demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] text-white shadow-[0_40px_100px_-30px_oklch(0_0_0/0.85)] ring-1 ring-white/8">
    <input type="radio" name="tmn-14-cat" id="tmn-14-c1" class="sr-only" checked>
    <input type="radio" name="tmn-14-cat" id="tmn-14-c2" class="sr-only">
    <input type="radio" name="tmn-14-cat" id="tmn-14-c3" class="sr-only">
    <input type="radio" name="tmn-14-cat" id="tmn-14-c4" class="sr-only">

    <aside aria-label="Categories" class="absolute inset-y-0 left-0 flex w-26 flex-col bg-tmn14-c1-rail pt-20 transition-colors duration-500 group-has-[#tmn-14-c2:checked]:bg-tmn14-c2-rail group-has-[#tmn-14-c3:checked]:bg-tmn14-c3-rail group-has-[#tmn-14-c4:checked]:bg-tmn14-c4-rail">
      <label for="tmn-14-c1" class="relative flex cursor-pointer flex-col items-center gap-1.5 px-2 py-4 text-white/55 transition-colors group-has-[#tmn-14-c1:checked]:text-white group-has-[#tmn-14-c1:focus-visible]:bg-white/8">
        <span class="grid size-11 place-items-center rounded-2xl bg-violet-400/20 text-violet-300 transition-transform duration-250 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tmn-14-c1:checked]:scale-110"><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><path d="M6 12h4M8 10v4M15 13h.01M18 11h.01"/><path d="M17.3 5H6.7a4 4 0 0 0-4 3.6L2 15a3 3 0 0 0 5.4 1.8l1.1-1.6A2 2 0 0 1 10.2 14h3.6a2 2 0 0 1 1.7.9l1.1 1.7A3 3 0 0 0 22 15l-.7-6.4A4 4 0 0 0 17.3 5z"/></svg></span>
        <span class="text-[11px] font-semibold">Gaming</span>
        <span aria-hidden="true" class="absolute top-1/2 right-0 h-0 w-[3px] -translate-y-1/2 rounded-l bg-white transition-[height] duration-300 group-has-[#tmn-14-c1:checked]:h-7"></span>
      </label>
      <label for="tmn-14-c2" class="relative flex cursor-pointer flex-col items-center gap-1.5 px-2 py-4 text-white/55 transition-colors group-has-[#tmn-14-c2:checked]:text-white group-has-[#tmn-14-c2:focus-visible]:bg-white/8">
        <span class="grid size-11 place-items-center rounded-2xl bg-green-400/20 text-green-300 transition-transform duration-250 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tmn-14-c2:checked]:scale-110"><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><path d="M11 20A7 7 0 0 1 4 13c0-6 7-10 16-10 0 9-4 16-10 16zM4 21c3-4 6-7 10-9"/></svg></span>
        <span class="text-[11px] font-semibold">Nature</span>
        <span aria-hidden="true" class="absolute top-1/2 right-0 h-0 w-[3px] -translate-y-1/2 rounded-l bg-white transition-[height] duration-300 group-has-[#tmn-14-c2:checked]:h-7"></span>
      </label>
      <label for="tmn-14-c3" class="relative flex cursor-pointer flex-col items-center gap-1.5 px-2 py-4 text-white/55 transition-colors group-has-[#tmn-14-c3:checked]:text-white group-has-[#tmn-14-c3:focus-visible]:bg-white/8">
        <span class="grid size-11 place-items-center rounded-2xl bg-red-400/20 text-red-300 transition-transform duration-250 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tmn-14-c3:checked]:scale-110"><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></span>
        <span class="text-[11px] font-semibold">Health</span>
        <span aria-hidden="true" class="absolute top-1/2 right-0 h-0 w-[3px] -translate-y-1/2 rounded-l bg-white transition-[height] duration-300 group-has-[#tmn-14-c3:checked]:h-7"></span>
      </label>
      <label for="tmn-14-c4" class="relative flex cursor-pointer flex-col items-center gap-1.5 px-2 py-4 text-white/55 transition-colors group-has-[#tmn-14-c4:checked]:text-white group-has-[#tmn-14-c4:focus-visible]:bg-white/8">
        <span class="grid size-11 place-items-center rounded-2xl bg-blue-400/20 text-blue-300 transition-transform duration-250 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tmn-14-c4:checked]:scale-110"><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/></svg></span>
        <span class="text-[11px] font-semibold">Tech</span>
        <span aria-hidden="true" class="absolute top-1/2 right-0 h-0 w-[3px] -translate-y-1/2 rounded-l bg-white transition-[height] duration-300 group-has-[#tmn-14-c4:checked]:h-7"></span>
      </label>
    </aside>

    <div class="absolute inset-y-0 right-0 left-26 overflow-hidden">
      <div class="invisible absolute inset-0 translate-x-5 overflow-y-auto bg-linear-160 from-[#1a1232] to-[#0d0a1f] opacity-0 transition duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tmn-14-c1:checked]:visible group-has-[#tmn-14-c1:checked]:translate-x-0 group-has-[#tmn-14-c1:checked]:opacity-100">
        <div class="flex h-20 items-end justify-between px-4 pb-3"><h2 class="text-[22px] font-bold tracking-[-0.02em]">Gaming</h2><span class="text-xs text-white/60">3 items</span></div>
        <div class="space-y-2.5 px-3.5 pt-2 pb-5">
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-violet-400 to-fuchsia-600"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Pro Controller</span><span class="block text-[11px] text-white/60">Wireless · 40hr</span><span class="mt-1 block text-sm font-bold">$79</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#1a1232] transition active:scale-95"><span class="sr-only">Add Pro Controller to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-indigo-400 to-violet-700"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Gaming Headset</span><span class="block text-[11px] text-white/60">7.1 surround · ANC</span><span class="mt-1 block text-sm font-bold">$120</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#1a1232] transition active:scale-95"><span class="sr-only">Add Gaming Headset to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-purple-400 to-pink-600"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">144Hz Monitor</span><span class="block text-[11px] text-white/60">27&quot; IPS · 1ms</span><span class="mt-1 block text-sm font-bold">$349</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#1a1232] transition active:scale-95"><span class="sr-only">Add 144Hz Monitor to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
        </div>
      </div>
      <div class="invisible absolute inset-0 translate-x-5 overflow-y-auto bg-linear-160 from-[#0a2e14] to-[#051509] opacity-0 transition duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tmn-14-c2:checked]:visible group-has-[#tmn-14-c2:checked]:translate-x-0 group-has-[#tmn-14-c2:checked]:opacity-100">
        <div class="flex h-20 items-end justify-between px-4 pb-3"><h2 class="text-[22px] font-bold tracking-[-0.02em]">Nature</h2><span class="text-xs text-white/60">3 items</span></div>
        <div class="space-y-2.5 px-3.5 pt-2 pb-5">
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-lime-300 to-green-600"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Succulent Set</span><span class="block text-[11px] text-white/60">6-pack · Indoor</span><span class="mt-1 block text-sm font-bold">$32</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#0a2e14] transition active:scale-95"><span class="sr-only">Add Succulent Set to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-stone-200 to-stone-400"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Ceramic Planter</span><span class="block text-[11px] text-white/60">Matte white · 8&quot;</span><span class="mt-1 block text-sm font-bold">$28</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#0a2e14] transition active:scale-95"><span class="sr-only">Add Ceramic Planter to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-emerald-300 to-teal-700"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Plant Food</span><span class="block text-[11px] text-white/60">Organic · 500ml</span><span class="mt-1 block text-sm font-bold">$14</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#0a2e14] transition active:scale-95"><span class="sr-only">Add Plant Food to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
        </div>
      </div>
      <div class="invisible absolute inset-0 translate-x-5 overflow-y-auto bg-linear-160 from-[#2e0a0e] to-[#170507] opacity-0 transition duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tmn-14-c3:checked]:visible group-has-[#tmn-14-c3:checked]:translate-x-0 group-has-[#tmn-14-c3:checked]:opacity-100">
        <div class="flex h-20 items-end justify-between px-4 pb-3"><h2 class="text-[22px] font-bold tracking-[-0.02em]">Health</h2><span class="text-xs text-white/60">2 items</span></div>
        <div class="space-y-2.5 px-3.5 pt-2 pb-5">
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-rose-300 to-red-600"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Fitness Tracker</span><span class="block text-[11px] text-white/60">Heart rate · Sleep</span><span class="mt-1 block text-sm font-bold">$89</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#2e0a0e] transition active:scale-95"><span class="sr-only">Add Fitness Tracker to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-amber-200 to-orange-500"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Vitamin D3</span><span class="block text-[11px] text-white/60">5000 IU · 90 caps</span><span class="mt-1 block text-sm font-bold">$22</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#2e0a0e] transition active:scale-95"><span class="sr-only">Add Vitamin D3 to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
        </div>
      </div>
      <div class="invisible absolute inset-0 translate-x-5 overflow-y-auto bg-linear-160 from-[#0a1a3a] to-[#050d20] opacity-0 transition duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tmn-14-c4:checked]:visible group-has-[#tmn-14-c4:checked]:translate-x-0 group-has-[#tmn-14-c4:checked]:opacity-100">
        <div class="flex h-20 items-end justify-between px-4 pb-3"><h2 class="text-[22px] font-bold tracking-[-0.02em]">Tech</h2><span class="text-xs text-white/60">3 items</span></div>
        <div class="space-y-2.5 px-3.5 pt-2 pb-5">
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-sky-300 to-blue-600"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">ANC Earbuds</span><span class="block text-[11px] text-white/60">Wireless · 30hr</span><span class="mt-1 block text-sm font-bold">$149</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#0a1a3a] transition active:scale-95"><span class="sr-only">Add ANC Earbuds to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-slate-300 to-slate-600"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Charging Pad</span><span class="block text-[11px] text-white/60">15W · Qi2</span><span class="mt-1 block text-sm font-bold">$35</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#0a1a3a] transition active:scale-95"><span class="sr-only">Add Charging Pad to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
          <div class="flex items-center gap-3 rounded-2xl border border-white/8 bg-white/6 p-3"><span class="size-13 flex-none rounded-xl bg-linear-135 from-cyan-300 to-indigo-600"></span><span class="min-w-0 flex-1"><span class="block text-[13px] font-semibold">Wireless Mouse</span><span class="block text-[11px] text-white/60">Silent · Ergonomic</span><span class="mt-1 block text-sm font-bold">$55</span></span><button type="button" class="grid size-9 place-items-center rounded-full bg-white text-[#0a1a3a] transition active:scale-95"><span class="sr-only">Add Wireless Mouse to bag</span><svg viewBox="0 0 24 24" class="size-4 stroke-[2.4]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn14-stage: #08080d;
  --color-tmn14-stage: oklch(0.13 0.01 285);
  --color-tmn14-c1-rail: #1a1530;
  --color-tmn14-c1-rail: oklch(0.21 0.05 290);
  --color-tmn14-c2-rail: #0c2414;
  --color-tmn14-c2-rail: oklch(0.24 0.05 150);
  --color-tmn14-c3-rail: #2a0f12;
  --color-tmn14-c3-rail: oklch(0.22 0.06 18);
  --color-tmn14-c4-rail: #0c1a36;
  --color-tmn14-c4-rail: oklch(0.23 0.06 260);
  --font-tmn14-sans: 'Onest', system-ui, sans-serif;
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-14 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-14 {
  width: 100%;
  min-height: 100svh;
}
```
