---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-with-phone-mockup/"
title: "Tailwind Feature Section with Phone Mockup"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "A mobile-app feature section with a CSS-drawn phone at the centre, flanked by features on both sides on desktop."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Section with Phone Mockup
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-with-phone-mockup/

A mobile-app feature section with a CSS-drawn phone at the centre, flanked by features on both sides on desktop. The phone floats on a slow keyframe, notification chips orbit it at different speeds, and the screen shows a real app UI — no images, no device-frame library.
## HTML
```html
<section class="tfs-21 relative w-full min-h-svh overflow-hidden bg-tfs21-bg px-5 py-20 font-tfs21-sans text-tfs21-ink antialiased sm:py-28" aria-labelledby="tfs-21-h">
  <div aria-hidden="true" class="absolute left-1/2 top-1/2 size-[40rem] -translate-1/2 rounded-full bg-[radial-gradient(circle,color-mix(in_oklab,var(--color-tfs21-acc)_22%,transparent),transparent_65%)]"></div>
  <div class="relative mx-auto grid w-full max-w-6xl gap-14">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="text-sm font-bold text-tfs21-acc">Fern for iOS &amp; Android</p>
      <h2 id="tfs-21-h" class="text-balance text-4xl font-extrabold tracking-tight sm:text-5xl">Your money, understood at a glance</h2>
    </header>
    <div class="grid items-center gap-12 lg:grid-cols-[1fr_auto_1fr]">
      <ul class="grid gap-8 lg:text-right">
        <li class="flex gap-4 lg:flex-row-reverse"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-white text-tfs21-acc shadow-lg shadow-tfs21-acc/10 ring-1 ring-tfs21-line"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M3 3v18h18M7 15l4-4 3 3 5-6"/></svg></span><div class="grid gap-1"><h3 class="text-lg font-bold">Spending insights</h3><p class="text-pretty text-tfs21-mut">Automatic categories and gentle nudges when a budget runs hot.</p></div></li>
        <li class="flex gap-4 lg:flex-row-reverse"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-white text-tfs21-acc shadow-lg shadow-tfs21-acc/10 ring-1 ring-tfs21-line"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg></span><div class="grid gap-1"><h3 class="text-lg font-bold">Bill reminders</h3><p class="text-pretty text-tfs21-mut">Never pay a late fee — Fern warns you three days ahead.</p></div></li>
      </ul>
      <div aria-hidden="true" class="relative mx-auto w-[17rem]">
        <div class="relative aspect-[9/19] rounded-[3rem] bg-tfs21-ink p-2.5 shadow-[0_50px_100px_-30px_rgb(6_40_30/0.55)] animate-tfs21-float motion-reduce:animate-none">
          <div class="relative flex size-full flex-col gap-3 overflow-hidden rounded-[2.4rem] bg-tfs21-bg p-4 pt-10">
            <span class="absolute left-1/2 top-2.5 h-6 w-20 -translate-x-1/2 rounded-full bg-tfs21-ink"></span>
            <p class="text-xs font-semibold text-tfs21-mut">Good morning, Sam</p>
            <div class="rounded-2xl bg-linear-to-br from-tfs21-acc to-tfs21-acc2 p-4 text-white shadow-lg"><p class="text-[11px] text-white/80">Total balance</p><p class="text-2xl font-extrabold tabular-nums">$8,412.50</p><p class="mt-1 text-[11px] font-semibold">▲ $320 this month</p></div>
            <div class="grid grid-cols-4 gap-2"><div class="grid justify-items-center gap-1"><span class="size-9 rounded-xl bg-white shadow-sm"></span><span class="text-[9px] font-semibold text-tfs21-mut">Send</span></div><div class="grid justify-items-center gap-1"><span class="size-9 rounded-xl bg-white shadow-sm"></span><span class="text-[9px] font-semibold text-tfs21-mut">Pay</span></div><div class="grid justify-items-center gap-1"><span class="size-9 rounded-xl bg-white shadow-sm"></span><span class="text-[9px] font-semibold text-tfs21-mut">Save</span></div><div class="grid justify-items-center gap-1"><span class="size-9 rounded-xl bg-white shadow-sm"></span><span class="text-[9px] font-semibold text-tfs21-mut">More</span></div></div>
            <p class="mt-1 text-[11px] font-bold">Recent</p>
            <div class="flex items-center gap-2 rounded-xl bg-white p-2 shadow-sm"><span class="size-7 rounded-lg bg-sky-200"></span><span class="flex-1 text-[11px] font-semibold">Blue Bottle</span><span class="text-[11px] font-bold tabular-nums">−$6.40</span></div><div class="flex items-center gap-2 rounded-xl bg-white p-2 shadow-sm"><span class="size-7 rounded-lg bg-emerald-200"></span><span class="flex-1 text-[11px] font-semibold">Payroll</span><span class="text-[11px] font-bold tabular-nums">+$3,200</span></div><div class="flex items-center gap-2 rounded-xl bg-white p-2 shadow-sm"><span class="size-7 rounded-lg bg-rose-200"></span><span class="flex-1 text-[11px] font-semibold">Spotify</span><span class="text-[11px] font-bold tabular-nums">−$11.99</span></div>
          </div>
        </div>
        <div class="absolute -left-16 top-[18%] flex items-center gap-2 rounded-2xl bg-white px-3 py-2.5 text-xs font-bold shadow-xl ring-1 ring-tfs21-line animate-tfs21-float [animation-delay:-2s] motion-reduce:animate-none"><span class="grid size-7 place-items-center rounded-full bg-emerald-100 text-emerald-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span>Rent paid</div>
        <div class="absolute -right-14 top-[52%] grid gap-0.5 rounded-2xl bg-white px-3.5 py-2.5 shadow-xl ring-1 ring-tfs21-line animate-tfs21-float [animation-delay:-4s] motion-reduce:animate-none"><span class="text-[10px] font-semibold text-tfs21-mut">Saved this year</span><span class="text-base font-extrabold text-tfs21-acc">$2,140</span></div>
      </div>
      <ul class="grid gap-8">
        <li class="flex gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-white text-tfs21-acc shadow-lg shadow-tfs21-acc/10 ring-1 ring-tfs21-line"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span><div class="grid gap-1"><h3 class="text-lg font-bold">Bank-level security</h3><p class="text-pretty text-tfs21-mut">Face ID, 256-bit encryption and instant card freeze.</p></div></li>
        <li class="flex gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-white text-tfs21-acc shadow-lg shadow-tfs21-acc/10 ring-1 ring-tfs21-line"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span><div class="grid gap-1"><h3 class="text-lg font-bold">Shared spaces</h3><p class="text-pretty text-tfs21-mut">Split bills and save toward goals with a partner or roommates.</p></div></li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs21-bg: #f2f8f5;
  --color-tfs21-bg: oklch(0.974 0.007 165);
  --color-tfs21-ink: #0c1f17;
  --color-tfs21-ink: oklch(0.22 0.03 165);
  --color-tfs21-mut: #4a5d54;
  --color-tfs21-mut: oklch(0.46 0.027 165);
  --color-tfs21-line: #dbe8e1;
  --color-tfs21-line: oklch(0.919 0.017 163);
  --color-tfs21-acc: #059669;
  --color-tfs21-acc: oklch(0.596 0.127 163);
  --color-tfs21-acc2: #0ea5e9;
  --color-tfs21-acc2: oklch(0.685 0.148 237);
  --font-tfs21-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-tfs21-float: tfs21-float 6s ease-in-out infinite;

  @keyframes tfs21-float {
    0%,
        100% {
      transform: translateY(0);
    }

    50% {
      transform: translateY(-12px);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-21 {
  width: 100%;
  min-height: 100svh;
}
```
