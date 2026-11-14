---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/accessible-aria-disclosure-mega-menu-tailwind/"
title: "Accessible ARIA Disclosure Mega Menu in Tailwind CSS"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "The boundary marker for the whole collection: a mega menu is a disclosure, not an ARIA menu."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible ARIA Disclosure Mega Menu in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/accessible-aria-disclosure-mega-menu-tailwind/

The boundary marker for the whole collection: a mega menu is a disclosure, not an ARIA menu. Each trigger is a <button> with aria-expanded and aria-controls; each panel is named by its trigger via aria-labelledby; the current page is marked with aria-current="page" and styled with the aria-[current=page]: variant. A monochrome camera specialist with hard rules and one red accent. Zero JavaScript.
## HTML
```html
<section class="tmm-09 relative w-full min-h-svh bg-tmm09-bg font-tmm09-sans leading-[1.55] text-tmm09-ink [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-2 [&_:focus-visible]:outline-tmm09-red" aria-labelledby="tmm09-title">
  <h2 class="sr-only" id="tmm09-title">Aperture</h2>

  <div class="absolute top-[11px] right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm09-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-none border border-tmm09-line bg-tmm09-surf text-tmm09-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm09-red" for="tmm09-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b-2 border-tmm09-line bg-tmm09-surf">
    <div class="mx-auto flex min-h-[66px] w-[min(80rem,calc(100%-2rem))] flex-wrap items-center gap-[clamp(0.75rem,3vw,2.5rem)] pr-15 max-[52rem]:flex-col max-[52rem]:items-stretch max-[52rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm09-mono text-[0.95rem]/none font-medium tracking-[0.22em] text-tmm09-ink" href="#tmm09-title">
        <svg class="size-[22px]" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5 15 12M20.5 12l-8 3M12 20.5 9 12M3.5 12l8-3" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>
        APERTURE
      </a>
      <nav class="min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-[clamp(0.15rem,1.5vw,0.5rem)] max-[52rem]:flex-col">
          <li data-tmm09-item class="flex items-center max-[52rem]:block">
            <button type="button" id="tmm09-trigger-products" aria-expanded="false" aria-controls="tmm09-panel-products" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm09-open:after:pointer-events-auto max-[52rem]:after:hidden inline-flex min-h-11 cursor-pointer items-center gap-1.5 px-2.5 font-tmm09-mono text-[0.82rem]/none font-medium tracking-[0.14em] text-tmm09-ink uppercase tmm09-open:bg-tmm09-ink tmm09-open:text-tmm09-bg">Products<span aria-hidden="true" class="font-normal transition-transform tmm09-open:rotate-45">+</span></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b-2 border-tmm09-line bg-tmm09-surf opacity-0 pointer-events-none transition-[opacity,visibility] duration-150 tmm09-open:visible tmm09-open:opacity-100 tmm09-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:tmm09-open:block" id="tmm09-panel-products" aria-labelledby="tmm09-trigger-products">
              <div class="mx-auto grid w-[min(80rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-x-[clamp(1rem,4vw,3rem)] gap-y-4 py-[clamp(1.1rem,3vw,1.9rem)] max-[52rem]:w-full max-[52rem]:px-4">
                <section class="min-w-0" aria-labelledby="tmm09-h-bodies">
                  <h3 class="mb-1.5 border-b-2 border-tmm09-line pb-1.5 font-tmm09-mono text-[0.7rem]/none font-bold tracking-[0.18em] uppercase" id="tmm09-h-bodies">Bodies</h3>
                  <ul class="grid">
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Full frame</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">APS-C</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Medium format</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Rangefinder</a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm09-h-glass">
                  <h3 class="mb-1.5 border-b-2 border-tmm09-line pb-1.5 font-tmm09-mono text-[0.7rem]/none font-bold tracking-[0.18em] uppercase" id="tmm09-h-glass">Lenses</h3>
                  <ul class="grid">
                    <li><a href="#tmm09-title" aria-current="page" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Primes<span class="font-tmm09-mono text-[0.6rem]/none font-bold tracking-[0.14em] text-tmm09-red uppercase">You are here</span></a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Zooms</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Tilt-shift</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Adapters</a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm09-h-light">
                  <h3 class="mb-1.5 border-b-2 border-tmm09-line pb-1.5 font-tmm09-mono text-[0.7rem]/none font-bold tracking-[0.18em] uppercase" id="tmm09-h-light">Lighting</h3>
                  <ul class="grid">
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Strobes</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Continuous</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Modifiers</a></li>
                  </ul>
                </section>
                <dl class="grid min-w-0 content-start gap-3 bg-tmm09-soft px-4 py-3.5">
                  <div><dt class="font-tmm09-mono text-[0.64rem]/none font-bold tracking-[0.16em] text-tmm09-mut uppercase">In stock today</dt><dd class="mt-1 text-[0.88rem]">412 items</dd></div>
                  <div><dt class="font-tmm09-mono text-[0.64rem]/none font-bold tracking-[0.16em] text-tmm09-mut uppercase">Trade-in</dt><dd class="mt-1 text-[0.88rem]">Valuation in 24h</dd></div>
                  <div><dt class="font-tmm09-mono text-[0.64rem]/none font-bold tracking-[0.16em] text-tmm09-mut uppercase">Rental</dt><dd class="mt-1 text-[0.88rem]">Next-day to 42 cities</dd></div>
                </dl>
              </div>
            </div>
          </li>
          <li data-tmm09-item class="flex items-center max-[52rem]:block">
            <button type="button" id="tmm09-trigger-service" aria-expanded="false" aria-controls="tmm09-panel-service" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm09-open:after:pointer-events-auto max-[52rem]:after:hidden inline-flex min-h-11 cursor-pointer items-center gap-1.5 px-2.5 font-tmm09-mono text-[0.82rem]/none font-medium tracking-[0.14em] text-tmm09-ink uppercase tmm09-open:bg-tmm09-ink tmm09-open:text-tmm09-bg">Service<span aria-hidden="true" class="font-normal transition-transform tmm09-open:rotate-45">+</span></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b-2 border-tmm09-line bg-tmm09-surf opacity-0 pointer-events-none transition-[opacity,visibility] duration-150 tmm09-open:visible tmm09-open:opacity-100 tmm09-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:tmm09-open:block" id="tmm09-panel-service" aria-labelledby="tmm09-trigger-service">
              <div class="mx-auto grid w-[min(80rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-x-[clamp(1rem,4vw,3rem)] gap-y-4 py-[clamp(1.1rem,3vw,1.9rem)] max-[52rem]:w-full max-[52rem]:px-4">
                <section class="min-w-0" aria-labelledby="tmm09-h-repair">
                  <h3 class="mb-1.5 border-b-2 border-tmm09-line pb-1.5 font-tmm09-mono text-[0.7rem]/none font-bold tracking-[0.18em] uppercase" id="tmm09-h-repair">Repair</h3>
                  <ul class="grid">
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Sensor clean</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Shutter replacement</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Lens calibration</a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm09-h-trade">
                  <h3 class="mb-1.5 border-b-2 border-tmm09-line pb-1.5 font-tmm09-mono text-[0.7rem]/none font-bold tracking-[0.18em] uppercase" id="tmm09-h-trade">Trade</h3>
                  <ul class="grid">
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Sell your kit</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Part exchange</a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm09-h-learn9">
                  <h3 class="mb-1.5 border-b-2 border-tmm09-line pb-1.5 font-tmm09-mono text-[0.7rem]/none font-bold tracking-[0.18em] uppercase" id="tmm09-h-learn9">Learn</h3>
                  <ul class="grid">
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Workshops</a></li>
                    <li><a href="#tmm09-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm09-soft text-[0.92rem] text-tmm09-ink transition-[color,padding] hover:pl-1 hover:text-tmm09-red aria-[current=page]:pl-2.5 aria-[current=page]:font-bold aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tmm09-red)]">Darkroom hire</a></li>
                  </ul>
                </section>
                <dl class="grid min-w-0 content-start gap-3 bg-tmm09-soft px-4 py-3.5">
                  <div><dt class="font-tmm09-mono text-[0.64rem]/none font-bold tracking-[0.16em] text-tmm09-mut uppercase">Turnaround</dt><dd class="mt-1 text-[0.88rem]">5 working days</dd></div>
                  <div><dt class="font-tmm09-mono text-[0.64rem]/none font-bold tracking-[0.16em] text-tmm09-mut uppercase">Warranty</dt><dd class="mt-1 text-[0.88rem]">12 months on repairs</dd></div>
                </dl>
              </div>
            </div>
          </li>
          <li class="flex items-center"><a class="inline-flex min-h-11 items-center px-2.5 font-tmm09-mono text-[0.82rem]/none font-medium tracking-[0.14em] text-tmm09-ink uppercase hover:underline hover:underline-offset-4" href="#tmm09-title">Used</a></li>
          <li class="flex items-center"><a class="inline-flex min-h-11 items-center gap-1.5 px-2.5 font-tmm09-mono text-[0.82rem]/none font-medium tracking-[0.14em] text-tmm09-red uppercase hover:underline hover:underline-offset-4" href="#tmm09-title"><span aria-hidden="true" class="size-1.5 bg-tmm09-red"></span>Clearance</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-4 max-[52rem]:ml-0">
        <a class="inline-flex min-h-11 items-center font-tmm09-mono text-[0.78rem]/none tracking-[0.1em] text-tmm09-mut uppercase hover:text-tmm09-ink" href="#tmm09-title">Stores</a>
        <a class="inline-flex min-h-11 items-center font-tmm09-mono text-[0.78rem]/none tracking-[0.1em] text-tmm09-mut uppercase hover:text-tmm09-ink" href="#tmm09-title">Account</a>
        <a class="inline-flex min-h-9 items-center gap-2 border border-tmm09-line px-3 font-tmm09-mono text-[0.75rem]/none font-semibold tracking-[0.1em] text-tmm09-ink uppercase transition-colors hover:bg-tmm09-ink hover:text-tmm09-bg" href="#tmm09-title">Bag <span class="grid size-5 place-items-center bg-tmm09-red text-[0.66rem] text-white">1</span></a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(80rem,calc(100%-2rem))] py-[clamp(2.5rem,8vw,5rem)]">
    <div class="grid max-w-[40rem] gap-2.5">
      <p class="font-tmm09-mono text-[0.74rem]/none font-medium tracking-[0.2em] text-tmm09-red uppercase">Primes / 35mm</p>
      <h1 class="font-tmm09-mono text-[clamp(1.9rem,6vw,3.2rem)]/[1.05] font-normal tracking-[-0.04em] text-balance">Aperture 35mm f/1.4 Mark III</h1>
      <p class="text-[clamp(0.95rem,2.3vw,1.05rem)] text-tmm09-mut text-pretty">Eleven elements, weather sealed, 420g. Built for the frame you did not plan for.</p>
      <p class="mt-2 flex flex-wrap items-baseline gap-x-3 font-tmm09-mono text-[1.6rem]/none font-medium tabular-nums">&pound;1,290 <span class="text-[0.85rem] font-normal text-tmm09-mut">or &pound;107/mo</span><span class="inline-flex items-center gap-1.5 text-[0.75rem] tracking-[0.1em] text-tmm09-ok uppercase"><span aria-hidden="true" class="size-1.5 rounded-full bg-tmm09-ok"></span>In stock</span></p>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm09-bg: #ffffff;
  --color-tmm09-bg: oklch(1 0 0);
  --color-tmm09-surf: #ffffff;
  --color-tmm09-surf: oklch(1 0 0);
  --color-tmm09-line: #111111;
  --color-tmm09-line: oklch(0.18 0 0);
  --color-tmm09-soft: #ededed;
  --color-tmm09-soft: oklch(0.94 0 0);
  --color-tmm09-ink: #111111;
  --color-tmm09-ink: oklch(0.18 0 0);
  --color-tmm09-mut: #616161;
  --color-tmm09-mut: oklch(0.48 0 0);
  --color-tmm09-red: #d90429;
  --color-tmm09-red: oklch(0.55 0.23 25);
  --color-tmm09-ok: #1d7a3e;
  --color-tmm09-ok: oklch(0.5 0.13 150);
  --font-tmm09-mono: 'DM Mono', ui-monospace, monospace;
  --font-tmm09-sans: 'Instrument Sans', system-ui, sans-serif;
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm09-open: instead of a repeated selector list. */

@custom-variant tmm09-open {
  &:where([data-tmm09-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm09-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-09 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-09:has(#tmm09-theme:checked) {
  --color-tmm09-bg: #0b0b0b;
  --color-tmm09-bg: oklch(0.15 0 0);
  --color-tmm09-surf: #131313;
  --color-tmm09-surf: oklch(0.19 0 0);
  --color-tmm09-line: #f2f2f2;
  --color-tmm09-line: oklch(0.96 0 0);
  --color-tmm09-soft: #262626;
  --color-tmm09-soft: oklch(0.27 0 0);
  --color-tmm09-ink: #f2f2f2;
  --color-tmm09-ink: oklch(0.96 0 0);
  --color-tmm09-mut: #a8a8a8;
  --color-tmm09-mut: oklch(0.74 0 0);
  --color-tmm09-red: #ff4d6d;
  --color-tmm09-red: oklch(0.71 0.18 20);
  --color-tmm09-ok: #4ade80;
  --color-tmm09-ok: oklch(0.8 0.18 150);
}

@media (prefers-color-scheme: dark) {
  .tmm-09 {
    --color-tmm09-bg: #0b0b0b;
    --color-tmm09-bg: oklch(0.15 0 0);
    --color-tmm09-surf: #131313;
    --color-tmm09-surf: oklch(0.19 0 0);
    --color-tmm09-line: #f2f2f2;
    --color-tmm09-line: oklch(0.96 0 0);
    --color-tmm09-soft: #262626;
    --color-tmm09-soft: oklch(0.27 0 0);
    --color-tmm09-ink: #f2f2f2;
    --color-tmm09-ink: oklch(0.96 0 0);
    --color-tmm09-mut: #a8a8a8;
    --color-tmm09-mut: oklch(0.74 0 0);
    --color-tmm09-red: #ff4d6d;
    --color-tmm09-red: oklch(0.71 0.18 20);
    --color-tmm09-ok: #4ade80;
    --color-tmm09-ok: oklch(0.8 0.18 150);
  }

  .tmm-09:has(#tmm09-theme:checked) {
    --color-tmm09-bg: #ffffff;
    --color-tmm09-bg: oklch(1 0 0);
    --color-tmm09-surf: #ffffff;
    --color-tmm09-surf: oklch(1 0 0);
    --color-tmm09-line: #111111;
    --color-tmm09-line: oklch(0.18 0 0);
    --color-tmm09-soft: #ededed;
    --color-tmm09-soft: oklch(0.94 0 0);
    --color-tmm09-ink: #111111;
    --color-tmm09-ink: oklch(0.18 0 0);
    --color-tmm09-mut: #616161;
    --color-tmm09-mut: oklch(0.48 0 0);
    --color-tmm09-red: #d90429;
    --color-tmm09-red: oklch(0.55 0.23 25);
    --color-tmm09-ok: #1d7a3e;
    --color-tmm09-ok: oklch(0.5 0.13 150);
  }
}
```
