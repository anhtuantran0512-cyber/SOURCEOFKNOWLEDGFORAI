---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-mobile-navigation-accordion-menu/"
title: "Tailwind CSS Mobile Navigation Accordion Menu"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A complete app-style mobile nav inside a phone frame: a checkbox hamburger that morphs into an X, a panel that slides open with grid-rows-[0fr] →…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Mobile Navigation Accordion Menu
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-mobile-navigation-accordion-menu/

A complete app-style mobile nav inside a phone frame: a checkbox hamburger that morphs into an X, a panel that slides open with grid-rows-[0fr] → grid-rows-[1fr], and drill-down <details> sections with icon tiles, item counts and a lime CTA. State is read with group-has-[#tac02-burger:checked]/nav: &mdash; Tailwind's spelling of :has().
## HTML
```html
<section class="tac-02 w-full min-h-svh grid place-items-center bg-tac02-bg bg-[radial-gradient(60%_45%_at_50%_0%,var(--color-tac02-glow),transparent_75%)] px-4 py-12 font-tac02-sans text-tac02-ink [interpolate-size:allow-keywords]" aria-label="Tailwind mobile navigation accordion menu demo">
  <div class="grid w-full justify-items-center gap-8">
    <div class="w-full max-w-[24rem] rounded-[3rem] bg-tac02-frame p-2.5 shadow-[0_40px_90px_-30px_oklch(0_0_0/0.9),0_0_0_1px_oklch(1_0_0/0.08),inset_0_1px_0_oklch(1_0_0/0.1)] max-sm:rounded-[2.5rem] max-sm:p-2">
      <nav class="group/nav relative flex min-h-[40rem] flex-col overflow-hidden rounded-[2.4rem] bg-tac02-screen ring-1 ring-white/5 max-sm:rounded-[2rem]" aria-label="Main">
        <div aria-hidden="true" class="flex items-center justify-between px-7 pt-3.5 pb-1 font-tac02-mono text-[12px] font-medium text-tac02-ink">
          <span>9:41</span>
          <span class="h-6 w-24 rounded-full bg-black"></span>
          <span class="flex items-center gap-1.5"><svg viewBox="0 0 18 12" width="17" height="11"><rect x="0" y="8" width="3" height="4" rx="1" fill="currentColor"/><rect x="5" y="5.5" width="3" height="6.5" rx="1" fill="currentColor"/><rect x="10" y="3" width="3" height="9" rx="1" fill="currentColor"/><rect x="15" y="0" width="3" height="12" rx="1" fill="currentColor" opacity="0.35"/></svg><svg viewBox="0 0 26 12" width="24" height="11"><rect x="0.5" y="0.5" width="22" height="11" rx="3.2" fill="none" stroke="currentColor" opacity="0.4"/><rect x="2.5" y="2.5" width="15" height="7" rx="1.8" fill="currentColor"/><rect x="24" y="4" width="1.6" height="4" rx="0.8" fill="currentColor" opacity="0.4"/></svg></span>
        </div>
        <div class="flex items-center justify-between gap-3 px-5 py-2.5">
          <a href="#" class="inline-flex min-h-11 items-center gap-2.5 rounded-xl pe-2 text-[19px] font-semibold tracking-[-0.03em] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac02-acc">
            <svg aria-hidden="true" viewBox="0 0 32 32" width="30" height="30"><rect width="32" height="32" rx="9" fill="currentColor" class="text-tac02-acc"/><path d="M6 23 13.5 11l4.5 7 2.5-3.5L26 23z" fill="currentColor" class="text-tac02-acc-ink"/></svg>
            <span>north<span class="text-tac02-acc">peak</span></span>
          </a>
          <label class="group/burger relative grid size-12 cursor-pointer place-content-center gap-[5px] rounded-2xl bg-white/5 ring-1 ring-white/10 transition hover:bg-white/10 has-focus-visible:ring-2 has-focus-visible:ring-tac02-acc has-checked:bg-tac02-acc/12 has-checked:ring-tac02-acc/40 motion-reduce:transition-none">
            <input type="checkbox" id="tac02-burger" class="sr-only" checked>
            <span class="sr-only">Menu</span>
            <span aria-hidden="true" class="block h-[2px] w-5 rounded-full bg-tac02-ink transition duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked/burger:translate-y-[7px] group-has-checked/burger:rotate-45 group-has-checked/burger:bg-tac02-acc motion-reduce:transition-none"></span>
            <span aria-hidden="true" class="block h-[2px] w-5 rounded-full bg-tac02-ink transition duration-200 group-has-checked/burger:scale-x-0 group-has-checked/burger:opacity-0 motion-reduce:transition-none"></span>
            <span aria-hidden="true" class="block h-[2px] w-5 rounded-full bg-tac02-ink transition duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked/burger:-translate-y-[7px] group-has-checked/burger:-rotate-45 group-has-checked/burger:bg-tac02-acc motion-reduce:transition-none"></span>
          </label>
        </div>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(0.3,0.7,0.2,1)] group-has-[#tac02-burger:checked]/nav:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="invisible min-h-0 overflow-hidden transition-[visibility] duration-500 group-has-[#tac02-burger:checked]/nav:visible motion-reduce:transition-none">
            <div class="px-3 pt-2 pb-5">
              <p class="px-3 pb-2 font-tac02-mono text-[11px] tracking-[0.14em] text-tac02-mut uppercase">Shop</p>
              <details class="group rounded-2xl transition-colors open:bg-white/[0.04] details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-400 details-content:transition-discrete open:details-content:h-auto motion-reduce:details-content:transition-none" open>
                <summary class="flex min-h-14 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-3 py-2 outline-none hover:bg-white/5 focus-visible:ring-2 focus-visible:ring-tac02-acc [&::-webkit-details-marker]:hidden">
                  <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-white/6 text-tac02-acc ring-1 ring-white/10 transition group-open:bg-tac02-acc group-open:text-tac02-acc-ink group-open:ring-tac02-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" width="19" height="19"><path d="M8 7V5.5A2.5 2.5 0 0 1 10.5 3h3A2.5 2.5 0 0 1 16 5.5V7M6 7h12a2 2 0 0 1 2 2v9a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V9a2 2 0 0 1 2-2zM9 13h6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
                  <span class="min-w-0 flex-1"><span class="block text-[15.5px] font-semibold tracking-[-0.01em]">Gear</span><span class="block truncate text-[12.5px] text-tac02-mut">Packs, shelter, footwear</span></span>
                  <svg aria-hidden="true" class="flex-none text-tac02-mut transition-transform duration-300 group-open:rotate-90 group-open:text-tac02-acc motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="m6 3.5 4.5 4.5L6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </summary>
                <ul class="ms-[2.15rem] mb-2 border-s border-white/10 ps-3 pe-2 pt-0.5 pb-1.5">
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Backpacks<span class="font-tac02-mono text-[11.5px] text-tac02-mut">86</span></a></li>
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Tents &amp; shelter<span class="rounded-full bg-tac02-acc px-2 py-0.5 text-[10.5px] font-bold text-tac02-acc-ink">New</span></a></li>
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Trail footwear<span class="font-tac02-mono text-[11.5px] text-tac02-mut">142</span></a></li>
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Headlamps<span class="font-tac02-mono text-[11.5px] text-tac02-mut">31</span></a></li>
                </ul>
              </details>
              <details class="group rounded-2xl transition-colors open:bg-white/[0.04] details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-400 details-content:transition-discrete open:details-content:h-auto motion-reduce:details-content:transition-none">
                <summary class="flex min-h-14 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-3 py-2 outline-none hover:bg-white/5 focus-visible:ring-2 focus-visible:ring-tac02-acc [&::-webkit-details-marker]:hidden">
                  <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-white/6 text-tac02-acc ring-1 ring-white/10 transition group-open:bg-tac02-acc group-open:text-tac02-acc-ink group-open:ring-tac02-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" width="19" height="19"><path d="M9 3.5 12 6l3-2.5 4.5 2L21 11l-3 1v8.5H6V12l-3-1 1.5-5.5zM12 6v14.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
                  <span class="min-w-0 flex-1"><span class="block text-[15.5px] font-semibold tracking-[-0.01em]">Apparel</span><span class="block truncate text-[12.5px] text-tac02-mut">Shells, insulation, base layers</span></span>
                  <svg aria-hidden="true" class="flex-none text-tac02-mut transition-transform duration-300 group-open:rotate-90 group-open:text-tac02-acc motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="m6 3.5 4.5 4.5L6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </summary>
                <ul class="ms-[2.15rem] mb-2 border-s border-white/10 ps-3 pe-2 pt-0.5 pb-1.5">
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Rain jackets<span class="font-tac02-mono text-[11.5px] text-tac02-mut">54</span></a></li>
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Down &amp; synthetic<span class="font-tac02-mono text-[11.5px] text-tac02-mut">38</span></a></li>
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Merino base layers<span class="font-tac02-mono text-[11.5px] text-tac02-mut">47</span></a></li>
                </ul>
              </details>
              <details class="group rounded-2xl transition-colors open:bg-white/[0.04] details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-400 details-content:transition-discrete open:details-content:h-auto motion-reduce:details-content:transition-none">
                <summary class="flex min-h-14 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-3 py-2 outline-none hover:bg-white/5 focus-visible:ring-2 focus-visible:ring-tac02-acc [&::-webkit-details-marker]:hidden">
                  <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-white/6 text-tac02-acc ring-1 ring-white/10 transition group-open:bg-tac02-acc group-open:text-tac02-acc-ink group-open:ring-tac02-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" width="19" height="19"><path d="M3 6.5 9 4l6 2.5L21 4v13.5L15 20l-6-2.5L3 20zM9 4v13.5M15 6.5V20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
                  <span class="min-w-0 flex-1"><span class="block text-[15.5px] font-semibold tracking-[-0.01em]">Trail guides</span><span class="block truncate text-[12.5px] text-tac02-mut">Routes, maps, safety</span></span>
                  <svg aria-hidden="true" class="flex-none text-tac02-mut transition-transform duration-300 group-open:rotate-90 group-open:text-tac02-acc motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="m6 3.5 4.5 4.5L6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </summary>
                <ul class="ms-[2.15rem] mb-2 border-s border-white/10 ps-3 pe-2 pt-0.5 pb-1.5">
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Route planning</a></li>
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Winter safety</a></li>
                  <li><a href="#" class="flex min-h-11 items-center justify-between gap-3 rounded-xl px-3 text-[14.5px] text-tac02-soft transition-colors hover:bg-white/5 hover:text-tac02-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">Offline maps</a></li>
                </ul>
              </details>
              <div class="mx-3 my-2 h-px bg-white/8" aria-hidden="true"></div>
              <a href="#" class="flex min-h-14 items-center gap-3.5 rounded-2xl px-3 py-2 transition-colors hover:bg-white/5 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tac02-acc">
                <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-white/6 text-tac02-acc ring-1 ring-white/10"><svg viewBox="0 0 24 24" width="19" height="19"><path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.3" fill="currentColor"/></svg></span>
                <span class="flex-1 text-[15.5px] font-semibold tracking-[-0.01em]">Stores &amp; events</span>
                <span class="rounded-full bg-white/8 px-2.5 py-1 font-tac02-mono text-[11px] text-tac02-soft">12 near you</span>
              </a>
              <div class="mt-4 grid gap-2.5 px-1">
                <a href="#" class="flex min-h-12 items-center justify-center gap-2 rounded-2xl bg-tac02-acc text-[15px] font-bold text-tac02-acc-ink shadow-[0_10px_30px_-10px_var(--color-tac02-acc),inset_0_1px_0_oklch(1_0_0/0.5)] transition hover:brightness-105 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac02-acc active:scale-[0.98] motion-reduce:transition-none">Find a store<svg aria-hidden="true" viewBox="0 0 16 16" width="15" height="15"><path d="M3 8h9M8.5 4.5 12 8l-3.5 3.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                <a href="#" class="flex min-h-12 items-center justify-center rounded-2xl text-[15px] font-semibold ring-1 ring-white/12 transition hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac02-acc motion-reduce:transition-none">Sign in</a>
              </div>
            </div>
          </div>
        </div>
        <div class="px-5 pb-6 transition duration-500 group-has-[#tac02-burger:checked]/nav:opacity-30 motion-reduce:transition-none">
          <div class="relative overflow-hidden rounded-3xl ring-1 ring-white/10">
            <svg aria-hidden="true" viewBox="0 0 340 170" class="block h-auto w-full" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="tac02s-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a3a1c"/><stop offset="0.6" stop-color="#7d8f3a"/><stop offset="1" stop-color="#e3d48a"/></linearGradient></defs><rect width="340" height="170" fill="url(#tac02s-sky)"/><circle cx="252" cy="92" r="20" fill="#f4e7a6" opacity="0.9"/><path d="M0 128 60 74l34 30 52-56 58 64 40-30 96 64v24H0z" fill="#1d2414"/><path d="M146 48l14 15-9-3-5 8-6-8-8 4z" fill="#e7ecd8" opacity="0.85"/><path d="M0 150 80 112l60 26 70-34 130 52v14H0z" fill="#11150c"/></svg>
            <div class="absolute inset-x-0 bottom-0 bg-linear-to-t from-black/80 to-transparent p-4 pt-10">
              <p class="font-tac02-mono text-[11px] tracking-[0.12em] text-tac02-acc uppercase">Trail report</p>
              <p class="mt-1 text-[17px] font-semibold tracking-[-0.02em]">Kesugi Ridge · 27 mi · Clear</p>
            </div>
          </div>
          <div class="mt-4 grid grid-cols-2 gap-3">
            <div class="rounded-2xl bg-white/[0.04] p-4 ring-1 ring-white/8">
              <p class="font-tac02-mono text-[11px] tracking-[0.1em] text-tac02-mut uppercase">Weather window</p>
              <p class="mt-1.5 text-[15px] font-semibold">Sat – Sun</p>
              <p class="mt-0.5 text-[12.5px] text-tac02-soft">Low wind · 4 °C</p>
            </div>
            <div class="rounded-2xl bg-white/[0.04] p-4 ring-1 ring-white/8">
              <p class="font-tac02-mono text-[11px] tracking-[0.1em] text-tac02-mut uppercase">Your pack</p>
              <p class="mt-1.5 text-[15px] font-semibold">11.2 lb</p>
              <p class="mt-0.5 text-[12.5px] text-tac02-soft">3-day alpine list</p>
            </div>
          </div>
          <p class="mt-5 mb-1 px-1 font-tac02-mono text-[11px] tracking-[0.1em] text-tac02-mut uppercase">Saved trails</p>
          <ul class="divide-y divide-white/8">
            <li class="flex items-center justify-between gap-3 px-1 py-3"><span><span class="block text-[14.5px] font-semibold">Harding Icefield</span><span class="block text-[12.5px] text-tac02-soft">8.2 mi · 3,800 ft gain</span></span><span class="rounded-full bg-tac02-acc/12 px-2.5 py-1 font-tac02-mono text-[11px] text-tac02-acc">Open</span></li>
            <li class="flex items-center justify-between gap-3 px-1 py-3"><span><span class="block text-[14.5px] font-semibold">Crow Pass</span><span class="block text-[12.5px] text-tac02-soft">23 mi · point to point</span></span><span class="rounded-full bg-white/8 px-2.5 py-1 font-tac02-mono text-[11px] text-tac02-soft">Snow</span></li>
          </ul>
        </div>
        <span aria-hidden="true" class="mx-auto mt-auto mb-2.5 block h-1.5 w-32 rounded-full bg-white/30"></span>
      </nav>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 text-center font-tac02-mono text-[11.5px] text-tac02-mut ring-1 ring-white/10">group-has-[#tac02-burger:checked]/nav: · grid-rows-[0fr→1fr] · details-content:h-auto</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac02-bg: #0a0b0c;
  --color-tac02-bg: oklch(0.15 0.004 120);
  --color-tac02-glow: #2a331433;
  --color-tac02-glow: oklch(0.32 0.06 125 / 0.45);
  --color-tac02-frame: #1c1d1f;
  --color-tac02-frame: oklch(0.23 0.004 270);
  --color-tac02-screen: #121314;
  --color-tac02-screen: oklch(0.185 0.003 270);
  --color-tac02-ink: #f3f4ef;
  --color-tac02-ink: oklch(0.965 0.006 120);
  --color-tac02-soft: #d3d6cc;
  --color-tac02-soft: oklch(0.87 0.012 120);
  --color-tac02-mut: #a1a59a;
  --color-tac02-mut: oklch(0.72 0.014 120);
  --color-tac02-acc: #c6f24a;
  --color-tac02-acc: oklch(0.9 0.19 124);
  --color-tac02-acc-ink: #1b2306;
  --color-tac02-acc-ink: oklch(0.245 0.055 124);
  --font-tac02-sans: 'Sora', system-ui, sans-serif;
  --font-tac02-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-02 {
  width: 100%;
  min-height: 100svh;
}
```
