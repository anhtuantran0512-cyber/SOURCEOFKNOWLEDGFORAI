---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-promotional-mega-menu-offer-banner/"
title: "Tailwind Promotional Mega Menu with Offer Banner"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "A stationery shop whose mega panel gives a full third of its width to the offer: a solid amber block with an end-date pill, a one-line headline and a navy…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Promotional Mega Menu with Offer Banner
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-promotional-mega-menu-offer-banner/

A stationery shop whose mega panel gives a full third of its width to the offer: a solid amber block with an end-date pill, a one-line headline and a navy CTA, beside three link columns. Hard offset shadows tie the panel to the floating bar, and links pop in with an overshoot, alternate columns lagging for a ripple. Zero JavaScript.
## HTML
```html
<section class="tmm-20 relative flow-root w-full min-h-svh bg-tmm20-bg font-tmm20-sans leading-[1.55] text-tmm20-ink [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm20-ink" aria-labelledby="tmm20-title">
  <h2 class="sr-only" id="tmm20-title">Orbit Supply Co.</h2>

  <header class="relative z-10 mx-auto mt-[clamp(1rem,3vw,1.75rem)] w-[min(70rem,calc(100%-2rem))]">
    <div class="absolute top-[10px] right-2.5 z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm20-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-none border-2 border-tmm20-line bg-tmm20-surf text-tmm20-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm20-ink" for="tmm20-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>
    <div class="flex min-h-17 flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,1.75rem)] border-2 border-tmm20-line bg-tmm20-surf pr-16 pl-[clamp(0.85rem,2vw,1.25rem)] max-[52rem]:flex-col max-[52rem]:py-2.5">
      <a class="grid content-center font-tmm20-display text-base/none font-bold tracking-[0.14em] text-tmm20-ink" href="#tmm20-title">ORBIT<span class="mt-0.5 font-tmm20-sans text-[0.6rem]/[1.3] font-normal tracking-[0.2em] text-tmm20-mut uppercase">supply co.</span></a>
      <nav class="flex min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-1 max-[52rem]:flex-col">
          <li data-tmm20-item class="flex items-stretch max-[52rem]:block">
            <button type="button" id="tmm20-trigger-shop" aria-expanded="false" aria-controls="tmm20-panel-shop" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 self-center px-3.5 font-tmm20-display text-[0.9rem]/none font-semibold tracking-[0.1em] text-tmm20-ink uppercase transition-colors hover:text-tmm20-mut tmm20-open:bg-tmm20-acc tmm20-open:text-tmm20-on-acc!">Shop<svg class="size-3.5 transition-transform duration-200 tmm20-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute -inset-x-0.5 top-full z-30 grid border-2 border-tmm20-line bg-tmm20-surf opacity-0 shadow-[5px_5px_0_var(--color-tmm20-line)] pointer-events-none transition-[opacity,visibility] duration-160 min-[58rem]:grid-cols-[2fr_1fr] tmm20-open:visible tmm20-open:opacity-100 tmm20-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:mt-2 max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:tmm20-open:grid" id="tmm20-panel-shop" aria-labelledby="tmm20-trigger-shop">
              <div class="grid min-w-0 grid-cols-[repeat(auto-fit,minmax(min(100%,10rem),1fr))] gap-[clamp(0.75rem,2.4vw,1.75rem)] p-[clamp(1rem,2.8vw,1.6rem)]">
                <section class="min-w-0">
                  <h3 class="mb-1.5 border-b-2 border-tmm20-line pb-1.5 font-tmm20-display text-[0.86rem]/tight font-bold tracking-[0.12em] uppercase">Desk</h3>
                  <ul class="grid gap-px">
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-20 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Notebooks</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-52 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Pens and refills</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-84 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Desk mats</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-116 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Organisers</a></li>
                  </ul>
                </section>
                <section class="min-w-0">
                  <h3 class="mb-1.5 border-b-2 border-tmm20-line pb-1.5 font-tmm20-display text-[0.86rem]/tight font-bold tracking-[0.12em] uppercase">Carry</h3>
                  <ul class="grid gap-px">
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-100 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Backpacks</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-132 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Sleeves</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-164 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Pouches</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-196 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Travel sets</a></li>
                  </ul>
                </section>
                <section class="min-w-0">
                  <h3 class="mb-1.5 border-b-2 border-tmm20-line pb-1.5 font-tmm20-display text-[0.86rem]/tight font-bold tracking-[0.12em] uppercase">Gifting</h3>
                  <ul class="grid gap-px">
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-20 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Under &pound;40</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-52 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Bundles</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-84 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Gift cards</a></li>
                  </ul>
                </section>
              </div>
              <aside class="relative grid min-w-0 content-start gap-1.5 overflow-hidden bg-tmm20-acc p-[clamp(1rem,2.8vw,1.6rem)] text-tmm20-on-acc" aria-label="Autumn offer">
                <span aria-hidden="true" class="pointer-events-none absolute -right-8 -bottom-10 size-36 rounded-full border-[18px] border-tmm20-on-acc/10"></span>
                <p class="flex items-center justify-between gap-2 font-tmm20-display text-[0.7rem]/none font-bold tracking-[0.2em] uppercase">Autumn offer<span class="rounded-full bg-tmm20-on-acc px-2 py-1 text-[0.62rem] tracking-[0.12em] text-tmm20-acc">Ends Sunday</span></p>
                <p class="font-tmm20-display text-[clamp(1.15rem,3vw,1.45rem)]/[1.15] font-bold text-balance">Second notebook half price</p>
                <p class="text-[0.88rem] text-pretty">On every A5 dot-grid in the Meridian range. No code needed.</p>
                <a class="group/o mt-1.5 inline-flex min-h-11 w-fit items-center gap-2 bg-tmm20-on-acc px-4 font-tmm20-display text-[0.8rem]/none font-bold tracking-[0.12em] text-white uppercase transition-colors hover:bg-black" href="#tmm20-title">Shop the range<span aria-hidden="true" class="transition-transform group-hover/o:translate-x-0.5">&rarr;</span></a>
              </aside>
            </div>
          </li>
          <li data-tmm20-item class="flex items-stretch max-[52rem]:block">
            <button type="button" id="tmm20-trigger-new" aria-expanded="false" aria-controls="tmm20-panel-new" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 self-center px-3.5 font-tmm20-display text-[0.9rem]/none font-semibold tracking-[0.1em] text-tmm20-ink uppercase transition-colors hover:text-tmm20-mut tmm20-open:bg-tmm20-acc tmm20-open:text-tmm20-on-acc!">New in<svg class="size-3.5 transition-transform duration-200 tmm20-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute -inset-x-0.5 top-full z-30 grid border-2 border-tmm20-line bg-tmm20-surf opacity-0 shadow-[5px_5px_0_var(--color-tmm20-line)] pointer-events-none transition-[opacity,visibility] duration-160 min-[58rem]:grid-cols-[2fr_1fr] tmm20-open:visible tmm20-open:opacity-100 tmm20-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:mt-2 max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:tmm20-open:grid" id="tmm20-panel-new" aria-labelledby="tmm20-trigger-new">
              <div class="grid min-w-0 grid-cols-[repeat(auto-fit,minmax(min(100%,10rem),1fr))] gap-[clamp(0.75rem,2.4vw,1.75rem)] p-[clamp(1rem,2.8vw,1.6rem)]">
                <section class="min-w-0">
                  <h3 class="mb-1.5 border-b-2 border-tmm20-line pb-1.5 font-tmm20-display text-[0.86rem]/tight font-bold tracking-[0.12em] uppercase">This season</h3>
                  <ul class="grid gap-px">
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-20 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Winter linen range</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-52 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Brass edition pens</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-84 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Archive reprints</a></li>
                  </ul>
                </section>
                <section class="min-w-0">
                  <h3 class="mb-1.5 border-b-2 border-tmm20-line pb-1.5 font-tmm20-display text-[0.86rem]/tight font-bold tracking-[0.12em] uppercase">Collaborations</h3>
                  <ul class="grid gap-px">
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-100 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Fern Studio</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-132 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Quill Press</a></li>
                  </ul>
                </section>
                <section class="min-w-0">
                  <h3 class="mb-1.5 border-b-2 border-tmm20-line pb-1.5 font-tmm20-display text-[0.86rem]/tight font-bold tracking-[0.12em] uppercase">Back in stock</h3>
                  <ul class="grid gap-px">
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-20 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">A5 dot grid</a></li>
                    <li class="origin-left scale-[0.86] opacity-0 transition-[opacity,scale] duration-[140ms,400ms] ease-tmm20-pop delay-52 tmm20-open:scale-100 tmm20-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm20-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm20-ink decoration-2 underline-offset-4 hover:underline">Card wallet</a></li>
                  </ul>
                </section>
              </div>
              <aside class="relative grid min-w-0 content-start gap-1.5 overflow-hidden bg-tmm20-acc p-[clamp(1rem,2.8vw,1.6rem)] text-tmm20-on-acc" aria-label="Members offer">
                <span aria-hidden="true" class="pointer-events-none absolute -right-8 -bottom-10 size-36 rounded-full border-[18px] border-tmm20-on-acc/10"></span>
                <p class="flex items-center justify-between gap-2 font-tmm20-display text-[0.7rem]/none font-bold tracking-[0.2em] uppercase">Members</p>
                <p class="font-tmm20-display text-[clamp(1.15rem,3vw,1.45rem)]/[1.15] font-bold text-balance">Early access from Thursday</p>
                <p class="text-[0.88rem] text-pretty">Sign in to shop the winter range 48 hours before general release.</p>
                <a class="group/o mt-1.5 inline-flex min-h-11 w-fit items-center gap-2 bg-tmm20-on-acc px-4 font-tmm20-display text-[0.8rem]/none font-bold tracking-[0.12em] text-white uppercase transition-colors hover:bg-black" href="#tmm20-title">Sign in<span aria-hidden="true" class="transition-transform group-hover/o:translate-x-0.5">&rarr;</span></a>
              </aside>
            </div>
          </li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center self-center px-3.5 font-tmm20-display text-[0.9rem]/none font-semibold tracking-[0.1em] text-tmm20-ink uppercase hover:text-tmm20-mut" href="#tmm20-title">Journal</a></li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center self-center px-3.5 font-tmm20-display text-[0.9rem]/none font-semibold tracking-[0.1em] text-tmm20-ink uppercase hover:text-tmm20-mut" href="#tmm20-title">Stores</a></li>
        </ul>
      </nav>
      <a class="ml-auto inline-flex min-h-11 items-center gap-2 self-center px-3 font-tmm20-display text-[0.82rem]/none font-semibold tracking-[0.1em] text-tmm20-ink uppercase max-[52rem]:ml-0" href="#tmm20-title">
        <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 8h14l-1.2 11H6.2Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 8a3 3 0 0 1 6 0" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
        Bag <span class="grid size-5 place-items-center rounded-full bg-tmm20-acc text-[0.7rem] text-tmm20-on-acc">2</span>
      </a>
    </div>
  </header>

  <main class="mx-auto w-[min(70rem,calc(100%-2rem))] py-[clamp(3rem,9vw,5.5rem)]">
    <div class="grid max-w-[34rem] gap-2.5">
      <p class="font-tmm20-display text-[0.72rem]/none font-bold tracking-[0.22em] text-tmm20-mut uppercase">Made in Britain since 2009</p>
      <h1 class="font-tmm20-display text-[clamp(2.2rem,7vw,3.8rem)]/[1.02] font-bold tracking-[-0.02em] text-balance">Paper worth writing on.</h1>
      <p class="text-[clamp(0.95rem,2.3vw,1.1rem)] text-tmm20-mut">120gsm, fountain-pen friendly, bound to lie flat.</p>
      <a class="mt-1.5 inline-flex min-h-12 w-fit items-center gap-2 border-2 border-tmm20-line bg-tmm20-acc px-5.5 font-tmm20-display text-[0.85rem]/none font-bold tracking-[0.14em] text-tmm20-on-acc uppercase shadow-[5px_5px_0_var(--color-tmm20-line)] transition-[translate,box-shadow] hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[3px_3px_0_var(--color-tmm20-line)] active:translate-x-[5px] active:translate-y-[5px] active:shadow-none" href="#tmm20-title">Shop notebooks <span aria-hidden="true">&rarr;</span></a>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm20-bg: #eef2f8;
  --color-tmm20-bg: oklch(0.96 0.01 255);
  --color-tmm20-surf: #ffffff;
  --color-tmm20-surf: oklch(1 0 0);
  --color-tmm20-line: #10213f;
  --color-tmm20-line: oklch(0.25 0.06 260);
  --color-tmm20-ink: #10213f;
  --color-tmm20-ink: oklch(0.25 0.06 260);
  --color-tmm20-mut: #4f5f82;
  --color-tmm20-mut: oklch(0.48 0.05 262);
  --color-tmm20-acc: #f0a202;
  --color-tmm20-acc: oklch(0.78 0.16 78);
  --color-tmm20-on-acc: #10213f;
  --color-tmm20-on-acc: oklch(0.25 0.06 260);
  --font-tmm20-display: 'Jost', Futura, 'Century Gothic', sans-serif;
  --font-tmm20-sans: 'Jost', system-ui, sans-serif;
  --ease-tmm20-pop: cubic-bezier(0.34, 1.6, 0.64, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm20-open: instead of a repeated selector list. */

@custom-variant tmm20-open {
  &:where([data-tmm20-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm20-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-20 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-20:has(#tmm20-theme:checked) {
  --color-tmm20-bg: #060b16;
  --color-tmm20-bg: oklch(0.15 0.025 262);
  --color-tmm20-surf: #0d1626;
  --color-tmm20-surf: oklch(0.2 0.035 262);
  --color-tmm20-line: #5d7398;
  --color-tmm20-line: oklch(0.56 0.06 262);
  --color-tmm20-ink: #eaf0f9;
  --color-tmm20-ink: oklch(0.95 0.012 255);
  --color-tmm20-mut: #93a5c2;
  --color-tmm20-mut: oklch(0.72 0.04 260);
  --color-tmm20-acc: #fbbf24;
  --color-tmm20-acc: oklch(0.83 0.15 80);
  --color-tmm20-on-acc: #10213f;
  --color-tmm20-on-acc: oklch(0.25 0.06 260);
}

@media (prefers-color-scheme: dark) {
  .tmm-20 {
    --color-tmm20-bg: #060b16;
    --color-tmm20-bg: oklch(0.15 0.025 262);
    --color-tmm20-surf: #0d1626;
    --color-tmm20-surf: oklch(0.2 0.035 262);
    --color-tmm20-line: #5d7398;
    --color-tmm20-line: oklch(0.56 0.06 262);
    --color-tmm20-ink: #eaf0f9;
    --color-tmm20-ink: oklch(0.95 0.012 255);
    --color-tmm20-mut: #93a5c2;
    --color-tmm20-mut: oklch(0.72 0.04 260);
    --color-tmm20-acc: #fbbf24;
    --color-tmm20-acc: oklch(0.83 0.15 80);
    --color-tmm20-on-acc: #10213f;
    --color-tmm20-on-acc: oklch(0.25 0.06 260);
  }

  .tmm-20:has(#tmm20-theme:checked) {
    --color-tmm20-bg: #eef2f8;
    --color-tmm20-bg: oklch(0.96 0.01 255);
    --color-tmm20-surf: #ffffff;
    --color-tmm20-surf: oklch(1 0 0);
    --color-tmm20-line: #10213f;
    --color-tmm20-line: oklch(0.25 0.06 260);
    --color-tmm20-ink: #10213f;
    --color-tmm20-ink: oklch(0.25 0.06 260);
    --color-tmm20-mut: #4f5f82;
    --color-tmm20-mut: oklch(0.48 0.05 262);
    --color-tmm20-acc: #f0a202;
    --color-tmm20-acc: oklch(0.78 0.16 78);
    --color-tmm20-on-acc: #10213f;
    --color-tmm20-on-acc: oklch(0.25 0.06 260);
  }
}
```
