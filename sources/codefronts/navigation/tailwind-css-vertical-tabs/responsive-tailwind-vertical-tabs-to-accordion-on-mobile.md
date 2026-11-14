---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/responsive-tailwind-vertical-tabs-to-accordion-on-mobile/"
title: "Responsive Tailwind Vertical Tabs to Accordion on Mobile"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A help-centre FAQ that renders as vertical tabs on a wide card and an accordion in a narrow column &mdash; from one flat DOM, with no duplicated markup or ids."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Vertical Tabs to Accordion on Mobile
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/responsive-tailwind-vertical-tabs-to-accordion-on-mobile/

A help-centre FAQ that renders as vertical tabs on a wide card and an accordion in a narrow column &mdash; from one flat DOM, with no duplicated markup or ids. Every responsive utility is a container query (@max-[40rem]:), so it switches by its own width, and a built-in switch shrinks the card to a 23rem sidebar to prove it. Accordion panels open with grid-rows-[0fr] &rarr; grid-rows-[1fr], an auto-height animation with nothing measured in JavaScript.
## HTML
```html
<section class="tvt-02 group/stage w-full min-h-svh grid place-items-center bg-tvt02-bg bg-[radial-gradient(75%_55%_at_50%_0%,var(--color-tvt02-glow),transparent_70%)] px-4 py-14 font-tvt02-sans text-tvt02-ink antialiased sm:px-6" aria-label="Responsive Tailwind vertical tabs to accordion demo">
  <div class="grid w-full max-w-[60rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt02-card px-3 py-1.5 font-tvt02-mono text-[11.5px] text-tvt02-acc-ink ring-1 ring-tvt02-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt02-acc shadow-[0_0_0_3px] shadow-tvt02-acc/25"></span>@container · 0fr → 1fr</p>
      <h2 class="text-[clamp(28px,4.4vw,44px)] leading-[1.04] font-bold tracking-[-0.035em] text-balance">Tabs when it's wide, <span class="bg-linear-to-r from-tvt02-hl to-tvt02-hl2 bg-clip-text pe-1 text-transparent">accordion when it's not</span></h2>
      <p class="max-w-[50ch] text-[15px] leading-relaxed text-tvt02-mut text-pretty">The component reads its own width, not the window's. Flip the switch to drop it into a narrow column on this same screen.</p>
      <label class="mt-1 inline-flex min-h-11 cursor-pointer items-center gap-3 rounded-full bg-tvt02-card py-1.5 ps-2 pe-4 text-[13.5px] font-medium ring-1 ring-tvt02-line transition-shadow duration-200 select-none hover:shadow-tvt02-icon has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt02-ring">
        <input type="checkbox" id="tvt-02-narrow" class="peer sr-only">
        <span aria-hidden="true" class="relative h-6 w-11 rounded-full bg-tvt02-line transition-colors duration-300 peer-checked:bg-linear-to-r peer-checked:from-tvt02-acc peer-checked:to-tvt02-acc2"><span class="absolute top-0.5 start-0.5 size-5 rounded-full bg-white shadow-[0_1px_3px_oklch(0_0_0/0.3)] transition-transform duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] [:checked+*_&]:translate-x-5 motion-reduce:transition-none"></span></span>
        Preview in a 23rem sidebar
      </label>
    </header>

    <div class="@container w-full max-w-[60rem] transition-[max-width] duration-500 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-02-narrow:checked]/stage:max-w-[23rem] motion-reduce:transition-none">
      <article class="overflow-hidden rounded-[24px] bg-tvt02-card shadow-tvt02-card ring-1 ring-tvt02-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
        <div class="flex items-center gap-3 border-b border-tvt02-line px-5 py-4 sm:px-6">
          <span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-linear-to-br from-tvt02-acc to-tvt02-acc2 text-white shadow-tvt02-icon"><svg viewBox="0 0 20 20" width="17" height="17" focusable="false"><circle cx="10" cy="10" r="7" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 8a2 2 0 1 1 2.8 1.8c-.5.3-.8.7-.8 1.3v.4M10 14h.01" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
          <div class="min-w-0 flex-1 leading-tight">
            <p class="text-[15px] font-semibold">Help centre</p>
            <p class="truncate text-[12.5px] text-tvt02-mut">Lumen Home · orders &amp; delivery</p>
          </div>
          <p class="shrink-0 rounded-full bg-tvt02-acc/10 px-2.5 py-1 font-tvt02-mono text-[11px] text-tvt02-acc-ink ring-1 ring-tvt02-acc/15"><span class="@max-[40rem]:hidden">Tabs layout</span><span class="hidden @max-[40rem]:inline">Accordion</span></p>
        </div>

        <div role="radiogroup" aria-label="Help topics" class="relative grid grid-cols-[clamp(14rem,32%,17.5rem)_minmax(0,1fr)] grid-rows-[repeat(4,auto)_1fr] before:col-start-1 before:row-[1/-1] before:border-e before:border-tvt02-line before:bg-tvt02-rail @max-[40rem]:grid-cols-1 @max-[40rem]:grid-rows-none @max-[40rem]:before:hidden">

        <input type="radio" name="tvt-02-faq" id="tvt-02-t1" class="peer/t1 sr-only" checked>
        <label for="tvt-02-t1" class="relative z-10 col-start-1 row-start-1 flex min-h-16 cursor-pointer items-center gap-3.5 px-4 transition-[background-color,color] duration-200 select-none hover:bg-tvt02-acc/[0.06] peer-checked/t1:bg-tvt02-acc/[0.09] peer-focus-visible/t1:outline-2 peer-focus-visible/t1:-outline-offset-4 peer-focus-visible/t1:outline-tvt02-ring before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt02-acc before:to-tvt02-acc2 before:transition-transform before:duration-300 peer-checked/t1:before:scale-y-100 motion-reduce:transition-none motion-reduce:before:transition-none @max-[40rem]:row-auto @max-[40rem]:border-t @max-[40rem]:border-tvt02-line first-of-type:border-t-0">
          <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt02-acc/10 text-tvt02-acc-ink ring-1 ring-tvt02-acc/15 transition-[background-color,color,box-shadow,scale] duration-300 [:checked+*_&]:scale-105 [:checked+*_&]:bg-linear-to-br [:checked+*_&]:from-tvt02-acc [:checked+*_&]:to-tvt02-acc2 [:checked+*_&]:text-white [:checked+*_&]:shadow-tvt02-icon [:checked+*_&]:ring-0 motion-reduce:transition-none"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M3 7.5h11v8H3zM14 10h3.6l2.4 2.6v2.9h-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="7" cy="17" r="1.8" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="17" cy="17" r="1.8" fill="none" stroke="currentColor" stroke-width="1.7"/></svg></span>
          <span class="grid min-w-0 flex-1 leading-tight"><span class="text-[15px] font-semibold text-tvt02-ink">Shipping</span><span class="mt-0.5 truncate text-[12.5px] text-tvt02-mut">Free over $50 · ships same day</span></span>
          <svg aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="18" height="18" class="hidden shrink-0 text-tvt02-mut transition-transform duration-300 ease-[cubic-bezier(.32,.72,.3,1)] motion-reduce:transition-none @max-[40rem]:block [:checked+*_&]:rotate-180 [:checked+*_&]:text-tvt02-acc-ink"><path d="m5 7.5 5 5 5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </label>
        <div id="tvt-02-p1" class="invisible col-start-2 row-[1/-1] grid grid-rows-[1fr] translate-x-2 opacity-0 transition-[opacity,translate,visibility,grid-template-rows] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t1:visible peer-checked/t1:grid-rows-[1fr] peer-checked/t1:translate-x-0 peer-checked/t1:opacity-100 motion-reduce:transition-none @max-[40rem]:col-start-1 @max-[40rem]:row-auto @max-[40rem]:grid-rows-[0fr] @max-[40rem]:translate-x-0">
          <div class="min-h-0 overflow-hidden">
            <div class="p-6 sm:p-8 @max-[40rem]:px-5 @max-[40rem]:pt-1 @max-[40rem]:pb-6">
              <h3 class="text-[clamp(20px,2.4vw,25px)] font-semibold tracking-[-0.02em] text-balance @max-[40rem]:hidden">Shipping &amp; delivery</h3>
              <p class="mt-1.5 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt02-mut text-pretty @max-[40rem]:mt-0">Orders placed before 2pm ET leave our warehouse the same day. Every parcel is tracked door to door.</p>
              <ul class="mt-5 grid gap-2.5">
                <li class="flex items-center gap-3 rounded-2xl bg-tvt02-acc/[0.07] p-3.5 ring-1 ring-tvt02-acc/25"><span class="grid min-w-0 flex-1"><span class="text-[14px] font-semibold">Standard</span><span class="text-[12.5px] text-tvt02-mut">3–5 business days</span></span><span class="rounded-full bg-tvt02-ok/12 px-2.5 py-1 text-[12px] font-semibold text-tvt02-ok">Free over $50</span></li>
                <li class="flex items-center gap-3 rounded-2xl p-3.5 ring-1 ring-tvt02-line"><span class="grid min-w-0 flex-1"><span class="text-[14px] font-semibold">Express</span><span class="text-[12.5px] text-tvt02-mut">1–2 business days</span></span><span class="font-tvt02-mono text-[13.5px] font-medium tabular-nums">$12</span></li>
                <li class="flex items-center gap-3 rounded-2xl p-3.5 ring-1 ring-tvt02-line"><span class="grid min-w-0 flex-1"><span class="text-[14px] font-semibold">Next day</span><span class="text-[12.5px] text-tvt02-mut">Order by 2pm ET, Mon–Thu</span></span><span class="font-tvt02-mono text-[13.5px] font-medium tabular-nums">$24</span></li>
              </ul>
            </div>
          </div>
        </div>

        <input type="radio" name="tvt-02-faq" id="tvt-02-t2" class="peer/t2 sr-only">
        <label for="tvt-02-t2" class="relative z-10 col-start-1 row-start-2 flex min-h-16 cursor-pointer items-center gap-3.5 px-4 transition-[background-color,color] duration-200 select-none hover:bg-tvt02-acc/[0.06] peer-checked/t2:bg-tvt02-acc/[0.09] peer-focus-visible/t2:outline-2 peer-focus-visible/t2:-outline-offset-4 peer-focus-visible/t2:outline-tvt02-ring before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt02-acc before:to-tvt02-acc2 before:transition-transform before:duration-300 peer-checked/t2:before:scale-y-100 motion-reduce:transition-none motion-reduce:before:transition-none @max-[40rem]:row-auto @max-[40rem]:border-t @max-[40rem]:border-tvt02-line first-of-type:border-t-0">
          <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt02-acc/10 text-tvt02-acc-ink ring-1 ring-tvt02-acc/15 transition-[background-color,color,box-shadow,scale] duration-300 [:checked+*_&]:scale-105 [:checked+*_&]:bg-linear-to-br [:checked+*_&]:from-tvt02-acc [:checked+*_&]:to-tvt02-acc2 [:checked+*_&]:text-white [:checked+*_&]:shadow-tvt02-icon [:checked+*_&]:ring-0 motion-reduce:transition-none"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M9 7 5 11l4 4M5 11h9a5 5 0 0 1 0 10h-2" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 -3)"/></svg></span>
          <span class="grid min-w-0 flex-1 leading-tight"><span class="text-[15px] font-semibold text-tvt02-ink">Returns</span><span class="mt-0.5 truncate text-[12.5px] text-tvt02-mut">30 days · free return label</span></span>
          <svg aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="18" height="18" class="hidden shrink-0 text-tvt02-mut transition-transform duration-300 ease-[cubic-bezier(.32,.72,.3,1)] motion-reduce:transition-none @max-[40rem]:block [:checked+*_&]:rotate-180 [:checked+*_&]:text-tvt02-acc-ink"><path d="m5 7.5 5 5 5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </label>
        <div id="tvt-02-p2" class="invisible col-start-2 row-[1/-1] grid grid-rows-[1fr] translate-x-2 opacity-0 transition-[opacity,translate,visibility,grid-template-rows] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t2:visible peer-checked/t2:grid-rows-[1fr] peer-checked/t2:translate-x-0 peer-checked/t2:opacity-100 motion-reduce:transition-none @max-[40rem]:col-start-1 @max-[40rem]:row-auto @max-[40rem]:grid-rows-[0fr] @max-[40rem]:translate-x-0">
          <div class="min-h-0 overflow-hidden">
            <div class="p-6 sm:p-8 @max-[40rem]:px-5 @max-[40rem]:pt-1 @max-[40rem]:pb-6">
              <h3 class="text-[clamp(20px,2.4vw,25px)] font-semibold tracking-[-0.02em] text-balance @max-[40rem]:hidden">Free returns for 30 days</h3>
              <p class="mt-1.5 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt02-mut text-pretty @max-[40rem]:mt-0">Changed your mind? Send it back unused within 30 days and we cover the postage.</p>
              <ol class="mt-5 grid gap-3.5">
                <li class="flex gap-3.5"><span class="grid size-7 shrink-0 place-items-center rounded-full bg-linear-to-br from-tvt02-acc to-tvt02-acc2 font-tvt02-mono text-[12px] font-medium text-white">1</span><span class="pt-0.5 text-[14px] leading-snug"><b class="font-semibold">Start a return online.</b> <span class="text-tvt02-mut">Pick the items, tell us why.</span></span></li>
                <li class="flex gap-3.5"><span class="grid size-7 shrink-0 place-items-center rounded-full bg-tvt02-acc/12 font-tvt02-mono text-[12px] font-medium text-tvt02-acc-ink">2</span><span class="pt-0.5 text-[14px] leading-snug"><b class="font-semibold">Drop it off.</b> <span class="text-tvt02-mut">Print the label or show the QR code at any UPS point.</span></span></li>
                <li class="flex gap-3.5"><span class="grid size-7 shrink-0 place-items-center rounded-full bg-tvt02-acc/12 font-tvt02-mono text-[12px] font-medium text-tvt02-acc-ink">3</span><span class="pt-0.5 text-[14px] leading-snug"><b class="font-semibold">Get your refund.</b> <span class="text-tvt02-mut">Back on your card within 3–5 business days.</span></span></li>
              </ol>
            </div>
          </div>
        </div>

        <input type="radio" name="tvt-02-faq" id="tvt-02-t3" class="peer/t3 sr-only">
        <label for="tvt-02-t3" class="relative z-10 col-start-1 row-start-3 flex min-h-16 cursor-pointer items-center gap-3.5 px-4 transition-[background-color,color] duration-200 select-none hover:bg-tvt02-acc/[0.06] peer-checked/t3:bg-tvt02-acc/[0.09] peer-focus-visible/t3:outline-2 peer-focus-visible/t3:-outline-offset-4 peer-focus-visible/t3:outline-tvt02-ring before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt02-acc before:to-tvt02-acc2 before:transition-transform before:duration-300 peer-checked/t3:before:scale-y-100 motion-reduce:transition-none motion-reduce:before:transition-none @max-[40rem]:row-auto @max-[40rem]:border-t @max-[40rem]:border-tvt02-line first-of-type:border-t-0">
          <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt02-acc/10 text-tvt02-acc-ink ring-1 ring-tvt02-acc/15 transition-[background-color,color,box-shadow,scale] duration-300 [:checked+*_&]:scale-105 [:checked+*_&]:bg-linear-to-br [:checked+*_&]:from-tvt02-acc [:checked+*_&]:to-tvt02-acc2 [:checked+*_&]:text-white [:checked+*_&]:shadow-tvt02-icon [:checked+*_&]:ring-0 motion-reduce:transition-none"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M12 3 5 6v5.5c0 4.2 2.9 7.8 7 9.5 4.1-1.7 7-5.3 7-9.5V6Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="m9 12 2.2 2.2L15.5 10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <span class="grid min-w-0 flex-1 leading-tight"><span class="text-[15px] font-semibold text-tvt02-ink">Warranty</span><span class="mt-0.5 truncate text-[12.5px] text-tvt02-mut">2-year limited cover</span></span>
          <svg aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="18" height="18" class="hidden shrink-0 text-tvt02-mut transition-transform duration-300 ease-[cubic-bezier(.32,.72,.3,1)] motion-reduce:transition-none @max-[40rem]:block [:checked+*_&]:rotate-180 [:checked+*_&]:text-tvt02-acc-ink"><path d="m5 7.5 5 5 5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </label>
        <div id="tvt-02-p3" class="invisible col-start-2 row-[1/-1] grid grid-rows-[1fr] translate-x-2 opacity-0 transition-[opacity,translate,visibility,grid-template-rows] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t3:visible peer-checked/t3:grid-rows-[1fr] peer-checked/t3:translate-x-0 peer-checked/t3:opacity-100 motion-reduce:transition-none @max-[40rem]:col-start-1 @max-[40rem]:row-auto @max-[40rem]:grid-rows-[0fr] @max-[40rem]:translate-x-0">
          <div class="min-h-0 overflow-hidden">
            <div class="p-6 sm:p-8 @max-[40rem]:px-5 @max-[40rem]:pt-1 @max-[40rem]:pb-6">
              <h3 class="text-[clamp(20px,2.4vw,25px)] font-semibold tracking-[-0.02em] text-balance @max-[40rem]:hidden">Two-year limited warranty</h3>
              <p class="mt-1.5 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt02-mut text-pretty @max-[40rem]:mt-0">Every Lumen product is covered against manufacturing defects for 24 months from delivery.</p>
              <div class="mt-5 grid gap-3 sm:grid-cols-2 @max-[40rem]:grid-cols-1">
                <ul class="grid gap-2 rounded-2xl p-4 ring-1 ring-tvt02-line"><li class="text-[12px] font-semibold tracking-[0.1em] text-tvt02-mut uppercase">Covered</li><li class="flex gap-2 text-[14px]"><span aria-hidden="true" class="text-tvt02-ok">✓</span>Faulty electronics</li><li class="flex gap-2 text-[14px]"><span aria-hidden="true" class="text-tvt02-ok">✓</span>Loose seams &amp; joints</li><li class="flex gap-2 text-[14px]"><span aria-hidden="true" class="text-tvt02-ok">✓</span>Finish defects</li></ul>
                <ul class="grid gap-2 rounded-2xl p-4 ring-1 ring-tvt02-line"><li class="text-[12px] font-semibold tracking-[0.1em] text-tvt02-mut uppercase">Not covered</li><li class="flex gap-2 text-[14px]"><span aria-hidden="true" class="text-tvt02-acc-ink">✕</span>Accidental damage</li><li class="flex gap-2 text-[14px]"><span aria-hidden="true" class="text-tvt02-acc-ink">✕</span>Normal wear</li><li class="flex gap-2 text-[14px]"><span aria-hidden="true" class="text-tvt02-acc-ink">✕</span>Third-party repairs</li></ul>
              </div>
            </div>
          </div>
        </div>

        <input type="radio" name="tvt-02-faq" id="tvt-02-t4" class="peer/t4 sr-only">
        <label for="tvt-02-t4" class="relative z-10 col-start-1 row-start-4 flex min-h-16 cursor-pointer items-center gap-3.5 px-4 transition-[background-color,color] duration-200 select-none hover:bg-tvt02-acc/[0.06] peer-checked/t4:bg-tvt02-acc/[0.09] peer-focus-visible/t4:outline-2 peer-focus-visible/t4:-outline-offset-4 peer-focus-visible/t4:outline-tvt02-ring before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt02-acc before:to-tvt02-acc2 before:transition-transform before:duration-300 peer-checked/t4:before:scale-y-100 motion-reduce:transition-none motion-reduce:before:transition-none @max-[40rem]:row-auto @max-[40rem]:border-t @max-[40rem]:border-tvt02-line first-of-type:border-t-0">
          <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt02-acc/10 text-tvt02-acc-ink ring-1 ring-tvt02-acc/15 transition-[background-color,color,box-shadow,scale] duration-300 [:checked+*_&]:scale-105 [:checked+*_&]:bg-linear-to-br [:checked+*_&]:from-tvt02-acc [:checked+*_&]:to-tvt02-acc2 [:checked+*_&]:text-white [:checked+*_&]:shadow-tvt02-icon [:checked+*_&]:ring-0 motion-reduce:transition-none"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M4 5.5h16v10H9l-5 4Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M8.5 10.5h.01M12 10.5h.01M15.5 10.5h.01" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span>
          <span class="grid min-w-0 flex-1 leading-tight"><span class="text-[15px] font-semibold text-tvt02-ink">Support</span><span class="mt-0.5 truncate text-[12.5px] text-tvt02-mut">Chat replies in ~2 min</span></span>
          <svg aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="18" height="18" class="hidden shrink-0 text-tvt02-mut transition-transform duration-300 ease-[cubic-bezier(.32,.72,.3,1)] motion-reduce:transition-none @max-[40rem]:block [:checked+*_&]:rotate-180 [:checked+*_&]:text-tvt02-acc-ink"><path d="m5 7.5 5 5 5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </label>
        <div id="tvt-02-p4" class="invisible col-start-2 row-[1/-1] grid grid-rows-[1fr] translate-x-2 opacity-0 transition-[opacity,translate,visibility,grid-template-rows] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t4:visible peer-checked/t4:grid-rows-[1fr] peer-checked/t4:translate-x-0 peer-checked/t4:opacity-100 motion-reduce:transition-none @max-[40rem]:col-start-1 @max-[40rem]:row-auto @max-[40rem]:grid-rows-[0fr] @max-[40rem]:translate-x-0">
          <div class="min-h-0 overflow-hidden">
            <div class="p-6 sm:p-8 @max-[40rem]:px-5 @max-[40rem]:pt-1 @max-[40rem]:pb-6">
              <h3 class="text-[clamp(20px,2.4vw,25px)] font-semibold tracking-[-0.02em] text-balance @max-[40rem]:hidden">Talk to a person</h3>
              <p class="mt-1.5 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt02-mut text-pretty @max-[40rem]:mt-0">Real humans in Austin and Manchester, seven days a week.</p>
              <ul class="mt-5 grid gap-2.5">
                <li class="flex items-center gap-3 rounded-2xl p-3.5 ring-1 ring-tvt02-line"><span aria-hidden="true" class="relative grid size-9 place-items-center rounded-xl bg-tvt02-acc/10 text-tvt02-acc-ink"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M4 5.5h16v10H9l-5 4Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M8.5 10.5h.01M12 10.5h.01M15.5 10.5h.01" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg><span class="absolute -end-0.5 -top-0.5 size-2.5 rounded-full bg-tvt02-ok ring-2 ring-tvt02-card"></span></span><span class="grid min-w-0 flex-1"><span class="text-[14px] font-semibold">Live chat</span><span class="text-[12.5px] text-tvt02-mut">Online now · average reply 2 min</span></span></li>
                <li class="flex items-center gap-3 rounded-2xl p-3.5 ring-1 ring-tvt02-line"><span aria-hidden="true" class="grid size-9 place-items-center rounded-xl bg-tvt02-acc/10 text-tvt02-acc-ink"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M4 6h16v12H4zM4 7l8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></span><span class="grid min-w-0 flex-1"><span class="text-[14px] font-semibold">Email</span><span class="truncate text-[12.5px] text-tvt02-mut">[email protected] · within 24h</span></span></li>
                <li class="flex items-center gap-3 rounded-2xl p-3.5 ring-1 ring-tvt02-line"><span aria-hidden="true" class="grid size-9 place-items-center rounded-xl bg-tvt02-acc/10 text-tvt02-acc-ink"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M6.5 4h3l1.5 4-2 1.3a10 10 0 0 0 5.7 5.7L16 13l4 1.5v3A1.5 1.5 0 0 1 18.5 19 14.5 14.5 0 0 1 5 5.5 1.5 1.5 0 0 1 6.5 4Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></span><span class="grid min-w-0 flex-1"><span class="text-[14px] font-semibold">Phone</span><span class="text-[12.5px] text-tvt02-mut">Mon–Fri, 9am–6pm ET</span></span></li>
              </ul>
            </div>
          </div>
        </div>

          <div class="col-start-1 row-start-5 m-3 self-end rounded-2xl bg-linear-to-br from-tvt02-acc/12 to-tvt02-acc2/8 p-4 ring-1 ring-tvt02-acc/15 @max-[40rem]:hidden">
            <p class="text-[13.5px] font-semibold">Order #LH-20817</p>
            <p class="mt-0.5 text-[12.5px] text-tvt02-mut">Out for delivery · arrives today</p>
            <div aria-hidden="true" class="mt-3 grid grid-cols-4 gap-1"><span class="h-1.5 rounded-full bg-tvt02-acc"></span><span class="h-1.5 rounded-full bg-tvt02-acc"></span><span class="h-1.5 rounded-full bg-tvt02-acc2"></span><span class="h-1.5 rounded-full bg-tvt02-line"></span></div>
          </div>
        </div>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt02-card px-3.5 py-2 text-center font-tvt02-mono text-[11.5px] text-tvt02-mut ring-1 ring-tvt02-line">@container · @max-[40rem]: · 0fr → 1fr</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt02-bg: #fff1ea;
  --color-tvt02-bg: oklch(0.968 0.018 50);
  --color-tvt02-glow: #ffc9bba6;
  --color-tvt02-glow: oklch(0.88 0.08 35 / 0.65);
  --color-tvt02-card: #fffdfc;
  --color-tvt02-card: oklch(0.996 0.004 50);
  --color-tvt02-rail: #fff5f1;
  --color-tvt02-rail: oklch(0.977 0.013 45);
  --color-tvt02-ink: #321a14;
  --color-tvt02-ink: oklch(0.25 0.04 35);
  --color-tvt02-mut: #72564e;
  --color-tvt02-mut: oklch(0.48 0.04 35);
  --color-tvt02-line: #efdbd3;
  --color-tvt02-line: oklch(0.905 0.025 40);
  --color-tvt02-acc: #d54023;
  --color-tvt02-acc: oklch(0.585 0.19 33);
  --color-tvt02-acc2: #cd285e;
  --color-tvt02-acc2: oklch(0.56 0.2 8);
  --color-tvt02-acc-ink: #af2c1f;
  --color-tvt02-acc-ink: oklch(0.5 0.17 30);
  --color-tvt02-hl: #d84b00;
  --color-tvt02-hl: oklch(0.6 0.19 40);
  --color-tvt02-hl2: #cf1e64;
  --color-tvt02-hl2: oklch(0.56 0.21 5);
  --color-tvt02-ring: #cc3526;
  --color-tvt02-ring: oklch(0.56 0.19 30);
  --color-tvt02-ok: #00764c;
  --color-tvt02-ok: oklch(0.5 0.12 160);
  --font-tvt02-sans: 'Outfit', system-ui, sans-serif;
  --font-tvt02-mono: 'DM Mono', ui-monospace, monospace;
  --shadow-tvt02-card: 0 1px 2px oklch(0.3 0.08 30 / 0.06), 0 30px 70px -30px oklch(0.45 0.16 30 / 0.4);
  --shadow-tvt02-icon: 0 8px 18px -8px oklch(0.58 0.2 25 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.25);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-02 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-02:not([data-theme="light"]) {
    --color-tvt02-bg: #1b0a08;
    --color-tvt02-bg: oklch(0.17 0.03 30);
    --color-tvt02-glow: #621e1680;
    --color-tvt02-glow: oklch(0.34 0.1 30 / 0.5);
    --color-tvt02-card: #261411;
    --color-tvt02-card: oklch(0.215 0.03 32);
    --color-tvt02-rail: #1f0f0c;
    --color-tvt02-rail: oklch(0.19 0.028 32);
    --color-tvt02-ink: #f9f0eb;
    --color-tvt02-ink: oklch(0.96 0.012 50);
    --color-tvt02-mut: #c8aea2;
    --color-tvt02-mut: oklch(0.77 0.035 45);
    --color-tvt02-line: #452b25;
    --color-tvt02-line: oklch(0.32 0.04 35);
    --color-tvt02-acc: #da4620;
    --color-tvt02-acc: oklch(0.6 0.19 35);
    --color-tvt02-acc2: #d02c61;
    --color-tvt02-acc2: oklch(0.57 0.2 8);
    --color-tvt02-acc-ink: #ffb797;
    --color-tvt02-acc-ink: oklch(0.84 0.1 45);
    --color-tvt02-hl: #ffaf78;
    --color-tvt02-hl: oklch(0.82 0.12 55);
    --color-tvt02-hl2: #ff92a4;
    --color-tvt02-hl2: oklch(0.78 0.14 10);
    --color-tvt02-ring: #fd9976;
    --color-tvt02-ring: oklch(0.78 0.13 40);
    --color-tvt02-ok: #5ed99e;
    --color-tvt02-ok: oklch(0.8 0.14 160);
  }
}

.tvt-02[data-theme="dark"] {
  --color-tvt02-bg: #1b0a08;
  --color-tvt02-bg: oklch(0.17 0.03 30);
  --color-tvt02-glow: #621e1680;
  --color-tvt02-glow: oklch(0.34 0.1 30 / 0.5);
  --color-tvt02-card: #261411;
  --color-tvt02-card: oklch(0.215 0.03 32);
  --color-tvt02-rail: #1f0f0c;
  --color-tvt02-rail: oklch(0.19 0.028 32);
  --color-tvt02-ink: #f9f0eb;
  --color-tvt02-ink: oklch(0.96 0.012 50);
  --color-tvt02-mut: #c8aea2;
  --color-tvt02-mut: oklch(0.77 0.035 45);
  --color-tvt02-line: #452b25;
  --color-tvt02-line: oklch(0.32 0.04 35);
  --color-tvt02-acc: #da4620;
  --color-tvt02-acc: oklch(0.6 0.19 35);
  --color-tvt02-acc2: #d02c61;
  --color-tvt02-acc2: oklch(0.57 0.2 8);
  --color-tvt02-acc-ink: #ffb797;
  --color-tvt02-acc-ink: oklch(0.84 0.1 45);
  --color-tvt02-hl: #ffaf78;
  --color-tvt02-hl: oklch(0.82 0.12 55);
  --color-tvt02-hl2: #ff92a4;
  --color-tvt02-hl2: oklch(0.78 0.14 10);
  --color-tvt02-ring: #fd9976;
  --color-tvt02-ring: oklch(0.78 0.13 40);
  --color-tvt02-ok: #5ed99e;
  --color-tvt02-ok: oklch(0.8 0.14 160);
}
```
