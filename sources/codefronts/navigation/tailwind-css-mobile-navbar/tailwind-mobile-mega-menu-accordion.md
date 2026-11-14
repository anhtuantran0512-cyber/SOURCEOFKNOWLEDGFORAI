---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-mobile-mega-menu-accordion/"
title: "Tailwind Mobile Mega Menu with Accordion Dropdowns"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "An e-commerce mobile menu: a pill \"Menu\" button drops a full-height panel holding three accordion sections with sub-links, badges and a newsletter promo."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mobile Mega Menu with Accordion Dropdowns
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-mobile-mega-menu-accordion/

An e-commerce mobile menu: a pill "Menu" button drops a full-height panel holding three accordion sections with sub-links, badges and a newsletter promo. The port replaces max-height: 300px with the grid-rows-[0fr] &rarr; [1fr] technique, so every section animates to its real height with even easing. Zero JavaScript.
## HTML
```html
<section class="tmn-09 w-full min-h-svh grid place-items-center bg-tmn09-stage px-4 py-6 font-tmn09-sans antialiased" aria-label="Tailwind mobile mega menu accordion demo">
  <div class="group relative flex h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] flex-col overflow-hidden rounded-[2.25rem] bg-white text-tmn09-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.45)]">
    <input type="checkbox" id="tmn-09-main" class="peer sr-only" aria-label="Toggle menu">
    <header class="relative z-10 flex h-[60px] flex-none items-center justify-between border-b border-tmn09-line bg-white px-5">
      <p class="text-lg font-extrabold tracking-[-0.03em]">Green<span class="text-tmn09-acc">Co</span></p>
      <label for="tmn-09-main" class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full border border-tmn09-line px-4 text-[13px] font-semibold transition-colors hover:bg-tmn09-soft group-has-[#tmn-09-main:checked]:bg-tmn09-ink group-has-[#tmn-09-main:checked]:text-white group-has-[#tmn-09-main:focus-visible]:ring-2 group-has-[#tmn-09-main:focus-visible]:ring-tmn09-acc">
        <span class="flex w-4 flex-col gap-[3px]">
          <span class="h-0.5 rounded-full bg-current transition-transform duration-300 group-has-[#tmn-09-main:checked]:translate-y-[5px] group-has-[#tmn-09-main:checked]:rotate-45"></span>
          <span class="h-0.5 w-3 rounded-full bg-current transition-opacity duration-200 group-has-[#tmn-09-main:checked]:opacity-0"></span>
          <span class="h-0.5 rounded-full bg-current transition-transform duration-300 group-has-[#tmn-09-main:checked]:-translate-y-[5px] group-has-[#tmn-09-main:checked]:-rotate-45"></span>
        </span>
        Menu
      </label>
    </header>

    <nav aria-label="Main" class="invisible absolute inset-x-0 top-[60px] bottom-0 z-[9] -translate-y-full overflow-y-auto bg-white transition-[translate,visibility] duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tmn-09-main:checked]:visible group-has-[#tmn-09-main:checked]:translate-y-0">
      <div class="divide-y divide-tmn09-line border-b border-tmn09-line">
        <div class="group/acc">
          <input type="checkbox" id="tmn-09-a1" class="sr-only">
          <label for="tmn-09-a1" class="flex min-h-15 cursor-pointer items-center gap-3 px-5 text-[15px] font-semibold group-has-focus-visible/acc:bg-tmn09-soft">
            <span class="grid size-9 place-items-center rounded-xl bg-emerald-50 text-emerald-700"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M11 20A7 7 0 0 1 4 13c0-6 7-10 16-10 0 9-4 16-10 16zM4 21c3-4 6-7 10-9"/></svg></span>
            Products
            <span class="ml-auto grid size-7 place-items-center rounded-full bg-tmn09-soft text-tmn09-mut transition-transform duration-300 group-has-checked/acc:rotate-180"><svg viewBox="0 0 24 24" class="size-4" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></span>
          </label>
          <div class="invisible grid grid-rows-[0fr] bg-tmn09-soft transition-[grid-template-rows,visibility] duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked/acc:visible group-has-checked/acc:grid-rows-[1fr]">
            <div class="min-h-0 overflow-hidden">
              <ul class="divide-y divide-black/5 py-2 pr-5 pl-17 text-sm text-tmn09-mut">
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Organic skincare<span class="ml-auto rounded-full bg-tmn09-acc/12 px-2 py-0.5 text-[10px] font-bold text-tmn09-acc">New</span></a></li>
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Supplements</a></li>
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Home &amp; garden</a></li>
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Food &amp; beverages</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="group/acc">
          <input type="checkbox" id="tmn-09-a2" class="sr-only">
          <label for="tmn-09-a2" class="flex min-h-15 cursor-pointer items-center gap-3 px-5 text-[15px] font-semibold group-has-focus-visible/acc:bg-tmn09-soft">
            <span class="grid size-9 place-items-center rounded-xl bg-cyan-50 text-cyan-700"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/></svg></span>
            Resources
            <span class="ml-auto grid size-7 place-items-center rounded-full bg-tmn09-soft text-tmn09-mut transition-transform duration-300 group-has-checked/acc:rotate-180"><svg viewBox="0 0 24 24" class="size-4" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></span>
          </label>
          <div class="invisible grid grid-rows-[0fr] bg-tmn09-soft transition-[grid-template-rows,visibility] duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked/acc:visible group-has-checked/acc:grid-rows-[1fr]">
            <div class="min-h-0 overflow-hidden">
              <ul class="divide-y divide-black/5 py-2 pr-5 pl-17 text-sm text-tmn09-mut">
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Blog &amp; articles</a></li>
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Sustainability guide</a></li>
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Community</a></li>
              </ul>
              <a href="#" class="mx-4 mb-4 flex items-center gap-3 rounded-2xl border border-tmn09-acc/25 bg-linear-135 from-emerald-50 to-cyan-50 p-3.5 text-[13px] leading-snug"><span class="grid size-9 flex-none place-items-center rounded-full bg-tmn09-acc text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><span>Join <strong class="text-tmn09-acc">12,000+</strong> readers &mdash; a free newsletter every Sunday.</span></a>
            </div>
          </div>
        </div>
        <div class="group/acc">
          <input type="checkbox" id="tmn-09-a3" class="sr-only">
          <label for="tmn-09-a3" class="flex min-h-15 cursor-pointer items-center gap-3 px-5 text-[15px] font-semibold group-has-focus-visible/acc:bg-tmn09-soft">
            <span class="grid size-9 place-items-center rounded-xl bg-violet-50 text-violet-700"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6"/></svg></span>
            Company
            <span class="ml-auto grid size-7 place-items-center rounded-full bg-tmn09-soft text-tmn09-mut transition-transform duration-300 group-has-checked/acc:rotate-180"><svg viewBox="0 0 24 24" class="size-4" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></span>
          </label>
          <div class="invisible grid grid-rows-[0fr] bg-tmn09-soft transition-[grid-template-rows,visibility] duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked/acc:visible group-has-checked/acc:grid-rows-[1fr]">
            <div class="min-h-0 overflow-hidden">
              <ul class="divide-y divide-black/5 py-2 pr-5 pl-17 text-sm text-tmn09-mut">
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">About us</a></li>
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Careers<span class="ml-auto rounded-full bg-tmn09-acc/12 px-2 py-0.5 text-[10px] font-bold text-tmn09-acc">Hiring</span></a></li>
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Press</a></li>
                <li><a href="#" class="flex min-h-11 items-center hover:text-tmn09-ink">Contact</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="flex gap-2.5 p-5">
        <a href="#" class="grid min-h-12 flex-1 place-items-center rounded-xl border border-tmn09-line text-sm font-semibold">Sign in</a>
        <a href="#" class="grid min-h-12 flex-1 place-items-center rounded-xl bg-tmn09-acc text-sm font-semibold text-white">Get started →</a>
      </div>
    </nav>

    <main class="flex-1 overflow-y-auto p-5">
      <p class="mb-2 text-xs font-bold tracking-[0.12em] text-tmn09-acc uppercase">Spring collection</p>
      <h1 class="mb-1 text-[26px] leading-tight font-bold tracking-[-0.03em]">Sustainable living, made simple</h1>
      <p class="mb-5 text-sm text-tmn09-mut">Eco-friendly products for a greener home.</p>
      <div class="grid grid-cols-2 gap-2.5">
        <div class="rounded-2xl border border-tmn09-line bg-tmn09-soft p-4"><svg viewBox="0 0 24 24" class="mb-2 size-6 text-tmn09-acc" aria-hidden="true"><path d="M7 19H4.8a1.8 1.8 0 0 1-1.6-2.7L7 9.5M11 19h8.2a1.8 1.8 0 0 0 1.6-2.7l-1.2-2.1M14 16l-3 3 3 3M8.3 13.6 7 9.5 2.9 10.8M9.3 5.6l1.2-2a1.8 1.8 0 0 1 3.1 0l4 6.9M13.4 10.5l4.1 1.3 1.3-4.1"/></svg><h2 class="mb-1 text-[13px] font-semibold">100% recycled</h2><p class="text-xs leading-snug text-tmn09-mut">Post-consumer packaging only.</p></div>
        <div class="rounded-2xl border border-tmn09-line bg-tmn09-soft p-4"><svg viewBox="0 0 24 24" class="mb-2 size-6 text-tmn09-acc" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg><h2 class="mb-1 text-[13px] font-semibold">Carbon neutral</h2><p class="text-xs leading-snug text-tmn09-mut">Certified shipping worldwide.</p></div>
        <div class="rounded-2xl border border-tmn09-line bg-tmn09-soft p-4"><svg viewBox="0 0 24 24" class="mb-2 size-6 text-tmn09-acc" aria-hidden="true"><path d="M11 20A7 7 0 0 1 4 13c0-6 7-10 16-10 0 9-4 16-10 16zM4 21c3-4 6-7 10-9"/></svg><h2 class="mb-1 text-[13px] font-semibold">Organic</h2><p class="text-xs leading-snug text-tmn09-mut">USDA-certified ingredients.</p></div>
        <div class="rounded-2xl border border-tmn09-line bg-tmn09-soft p-4"><svg viewBox="0 0 24 24" class="mb-2 size-6 text-tmn09-acc" aria-hidden="true"><path d="M12 21s-8-4.5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 6.5-8 11-8 11z"/></svg><h2 class="mb-1 text-[13px] font-semibold">Cruelty-free</h2><p class="text-xs leading-snug text-tmn09-mut">Leaping Bunny certified.</p></div>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn09-stage: #e8ece9;
  --color-tmn09-stage: oklch(0.94 0.008 160);
  --color-tmn09-soft: #f6f7f6;
  --color-tmn09-soft: oklch(0.975 0.003 160);
  --color-tmn09-line: #e5e7eb;
  --color-tmn09-line: oklch(0.93 0.006 265);
  --color-tmn09-ink: #111827;
  --color-tmn09-ink: oklch(0.21 0.03 265);
  --color-tmn09-mut: #565e6b;
  --color-tmn09-mut: oklch(0.47 0.02 260);
  --color-tmn09-acc: #047857;
  --color-tmn09-acc: oklch(0.51 0.11 163);
  --font-tmn09-sans: 'DM Sans', system-ui, sans-serif;
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-09 svg {
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

.tmn-09 {
  width: 100%;
  min-height: 100svh;
}
```
