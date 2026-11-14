---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-floating-action-button-speed-dial/"
title: "Tailwind Floating Action Button (FAB) Speed Dial Menu"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A maps-style screen with a FAB that morphs from a rounded square to a circle and rotates its plus into an X as four labelled actions ripple up above it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Action Button (FAB) Speed Dial Menu
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-floating-action-button-speed-dial/

A maps-style screen with a FAB that morphs from a rounded square to a circle and rotates its plus into an X as four labelled actions ripple up above it. The map is now pure gradients &mdash; park, river, avenues &mdash; with a live animate-ping location pulse and a place card. Zero JavaScript.
## HTML
```html
<section class="tmn-07 w-full min-h-svh grid place-items-center bg-tmn07-stage px-4 py-6 font-tmn07-sans antialiased" aria-label="Tailwind FAB speed dial demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] text-tmn07-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.6)]">
    <input type="checkbox" id="tmn-07-toggle" class="peer sr-only" aria-label="Toggle map actions">

    <div aria-hidden="true" class="absolute inset-0 bg-tmn07-map bg-[radial-gradient(60%_30%_at_95%_75%,var(--color-tmn07-water)_60%,transparent_61%),radial-gradient(40%_22%_at_15%_40%,var(--color-tmn07-park)_70%,transparent_71%),repeating-linear-gradient(0deg,transparent_0_39px,oklch(0_0_0/0.05)_39px_40px),repeating-linear-gradient(90deg,transparent_0_39px,oklch(0_0_0/0.05)_39px_40px)]">
      <span class="absolute inset-x-0 top-[150px] h-[18px] bg-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)]"></span>
      <span class="absolute inset-y-0 left-[140px] w-[18px] bg-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)]"></span>
      <span class="absolute inset-x-0 top-[330px] h-2.5 -rotate-6 bg-white"></span>
      <span class="absolute inset-y-0 left-[60px] w-2.5 bg-white"></span>
      <span class="absolute inset-y-0 right-[80px] w-2.5 bg-white"></span>
      <span class="absolute top-[159px] left-[149px] grid -translate-1/2 place-items-center">
        <span class="absolute size-10 rounded-full bg-tmn07-acc/30 animate-ping motion-reduce:animate-none"></span>
        <span class="relative size-4 rounded-full border-[3px] border-white bg-tmn07-acc shadow-md"></span>
      </span>
    </div>

    <label class="absolute inset-x-4 top-5 z-[3] flex h-13 items-center gap-2.5 rounded-full bg-white px-4.5 shadow-[0_6px_20px_-6px_oklch(0_0_0/0.25)]">
      <svg viewBox="0 0 24 24" class="size-5 text-tmn07-mut" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input type="search" placeholder="Search places" class="w-full bg-transparent text-[15px] placeholder:text-tmn07-mut focus:outline-none">
      <span class="grid size-8 flex-none place-items-center rounded-full bg-linear-135 from-amber-400 to-tmn07-acc text-xs font-semibold text-white">JD</span>
    </label>

    <article class="absolute bottom-7 left-4 z-[3] w-[calc(100%-120px)] rounded-2xl bg-white p-3.5 shadow-[0_10px_30px_-10px_oklch(0_0_0/0.3)]">
      <p class="text-[15px] font-semibold">Blue Bottle Coffee</p>
      <p class="text-[13px] text-tmn07-mut">4 min walk · Open until 6 pm</p>
      <p class="mt-1.5 flex items-center gap-1 text-xs font-medium text-amber-700"><span aria-hidden="true">★★★★★</span>4.8</p>
    </article>

    <label for="tmn-07-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 z-[5] bg-black/0 transition-colors duration-300 group-has-checked:pointer-events-auto group-has-checked:bg-black/30"></label>

    <nav aria-label="Map actions">
      <a href="#" class="invisible absolute right-6 bottom-[104px] z-[15] flex translate-y-5 scale-60 items-center gap-3 opacity-0 transition duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100"><span class="rounded-full bg-tmn07-ink/90 px-3 py-1.5 text-xs font-semibold whitespace-nowrap text-white">Directions</span><span class="grid size-12 place-items-center rounded-full bg-blue-600 text-white shadow-lg"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="m3 11 19-9-9 19-2-8z"/></svg></span></a>
      <a href="#" class="invisible absolute right-6 bottom-[164px] z-[15] flex translate-y-5 scale-60 items-center gap-3 opacity-0 transition duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:delay-[50ms]"><span class="rounded-full bg-tmn07-ink/90 px-3 py-1.5 text-xs font-semibold whitespace-nowrap text-white">Nearby</span><span class="grid size-12 place-items-center rounded-full bg-emerald-600 text-white shadow-lg"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg></span></a>
      <a href="#" class="invisible absolute right-6 bottom-[224px] z-[15] flex translate-y-5 scale-60 items-center gap-3 opacity-0 transition duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:delay-[100ms]"><span class="rounded-full bg-tmn07-ink/90 px-3 py-1.5 text-xs font-semibold whitespace-nowrap text-white">Save location</span><span class="grid size-12 place-items-center rounded-full bg-amber-500 text-white shadow-lg"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M19 21 12 16l-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg></span></a>
      <a href="#" class="invisible absolute right-6 bottom-[284px] z-[15] flex translate-y-5 scale-60 items-center gap-3 opacity-0 transition duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:delay-[150ms]"><span class="rounded-full bg-tmn07-ink/90 px-3 py-1.5 text-xs font-semibold whitespace-nowrap text-white">Share</span><span class="grid size-12 place-items-center rounded-full bg-violet-600 text-white shadow-lg"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8M16 6l-4-4-4 4M12 2v13"/></svg></span></a>
    </nav>

    <label for="tmn-07-toggle" class="absolute right-6 bottom-7 z-20 grid size-14 cursor-pointer place-items-center rounded-2xl bg-tmn07-acc text-white shadow-[0_10px_24px_-6px] shadow-tmn07-acc/60 transition-[border-radius,scale] duration-300 hover:scale-105 group-has-checked:rounded-[50%] peer-focus-visible:ring-2 peer-focus-visible:ring-tmn07-ink peer-focus-visible:ring-offset-2">
      <svg viewBox="0 0 24 24" class="size-6 stroke-[2.2] transition-transform duration-300 group-has-checked:rotate-45" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn07-stage: #e7e2d8;
  --color-tmn07-stage: oklch(0.91 0.015 80);
  --color-tmn07-map: #f1ece2;
  --color-tmn07-map: oklch(0.94 0.015 80);
  --color-tmn07-water: #b9d8ef;
  --color-tmn07-water: oklch(0.86 0.05 240);
  --color-tmn07-park: #cfe5c3;
  --color-tmn07-park: oklch(0.89 0.06 135);
  --color-tmn07-ink: #1c1917;
  --color-tmn07-ink: oklch(0.22 0.008 60);
  --color-tmn07-mut: #6b635b;
  --color-tmn07-mut: oklch(0.5 0.015 60);
  --color-tmn07-acc: #e11d48;
  --color-tmn07-acc: oklch(0.59 0.22 13);
  --font-tmn07-sans: 'Outfit', system-ui, sans-serif;
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-07 svg {
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

.tmn-07 {
  width: 100%;
  min-height: 100svh;
}
```
