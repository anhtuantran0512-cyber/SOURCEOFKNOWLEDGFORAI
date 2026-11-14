---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/brutalist-tailwind-css-accordion/"
title: "Brutalist Tailwind CSS Accordion"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "Neo-brutalism for disclosure: 3px ink borders, zero-blur offset shadows written as shadow-[6px_6px_0_var(--color-tac11-ink)], and an open state that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Tailwind CSS Accordion
Source: https://codefronts.com/navigation/tailwind-css-accordions/brutalist-tailwind-css-accordion/

Neo-brutalism for disclosure: 3px ink borders, zero-blur offset shadows written as shadow-[6px_6px_0_var(--color-tac11-ink)], and an open state that physically presses the slab into the page &mdash; open:translate-x-1 open:translate-y-1 while the shadow shrinks by the same 4px. Each question owns a loud colour (yellow, hot pink, cyan) that floods its index chip and arrow key on open. A zine FAQ with ruled-paper answers.
## HTML
```html
<section class="tac-11 w-full min-h-svh grid place-items-center bg-tac11-bg bg-[radial-gradient(var(--color-tac11-ink)_1px,transparent_1.5px)] bg-size-[22px_22px] px-5 py-14 font-tac11-mono text-tac11-ink [interpolate-size:allow-keywords]" aria-label="Brutalist accordion demo">
  <div class="grid w-full justify-items-center gap-9">
    <div class="w-full max-w-[600px]">
      <header class="relative mb-9 border-3 border-tac11-ink bg-white px-5 py-5 shadow-[6px_6px_0_var(--color-tac11-ink)] sm:px-6">
        <span class="absolute -top-4 right-4 rotate-3 border-3 border-tac11-ink bg-tac11-pink px-2.5 py-1 text-xs font-bold tracking-[0.12em] uppercase">Issue #47</span>
        <p class="text-xs font-bold tracking-[0.18em] uppercase">The Unpolished Web · zine</p>
        <h2 class="mt-1 font-tac11-display text-[clamp(44px,9vw,68px)] leading-[0.95] font-extrabold tracking-[-0.04em]">FAQ<span class="text-tac11-pink [-webkit-text-stroke:2px_var(--color-tac11-ink)]">_</span></h2>
        <p class="mt-2 max-w-md text-sm leading-6">Questions people actually email us. Printed badly on purpose.</p>
      </header>

      <div class="flex flex-col gap-5">
        <details class="group border-3 border-tac11-ink bg-white shadow-[6px_6px_0_var(--color-tac11-ink)] transition-[translate,box-shadow] duration-150 ease-out hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[4px_4px_0_var(--color-tac11-ink)] open:translate-x-1 open:translate-y-1 open:shadow-[2px_2px_0_var(--color-tac11-ink)] motion-reduce:transition-none details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-200 details-content:ease-out open:details-content:h-auto motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-4 px-4 py-3 text-[15px] font-bold tracking-[0.08em] uppercase select-none focus-visible:outline-4 focus-visible:outline-offset-4 focus-visible:outline-tac11-ink [&::-webkit-details-marker]:hidden">
            <span class="grid size-10 flex-none place-items-center border-3 border-tac11-ink bg-white text-sm transition-colors duration-150 group-open:bg-tac11-ink group-open:text-tac11-yellow">01</span>
            <span class="flex-1">What is this?</span>
            <span aria-hidden="true" class="grid size-10 flex-none place-items-center border-3 border-tac11-ink bg-white transition-[rotate,background-color] duration-200 ease-out group-open:rotate-180 group-open:bg-tac11-yellow motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="16" height="16"><path d="M8 2.5v10M3.5 8.5 8 13l4.5-4.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg></span>
          </summary>
          <div class="border-t-3 border-tac11-ink bg-[repeating-linear-gradient(180deg,transparent_0_27px,var(--color-tac11-rule)_27px_28px)] bg-origin-content bg-white px-4 pt-3.5 pb-4 sm:pl-[4.5rem]">
            <p class="text-sm leading-7">A weekly zine about the unpolished web — view-source culture, personal sites and software with opinions. One issue, every Friday, no tracking pixels.</p>
          </div>
        </details>

        <details class="group border-3 border-tac11-ink bg-white shadow-[6px_6px_0_var(--color-tac11-ink)] transition-[translate,box-shadow] duration-150 ease-out hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[4px_4px_0_var(--color-tac11-ink)] open:translate-x-1 open:translate-y-1 open:shadow-[2px_2px_0_var(--color-tac11-ink)] motion-reduce:transition-none details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-200 details-content:ease-out open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-4 px-4 py-3 text-[15px] font-bold tracking-[0.08em] uppercase select-none focus-visible:outline-4 focus-visible:outline-offset-4 focus-visible:outline-tac11-ink [&::-webkit-details-marker]:hidden">
            <span class="grid size-10 flex-none place-items-center border-3 border-tac11-ink bg-white text-sm transition-colors duration-150 group-open:bg-tac11-ink group-open:text-tac11-pink">02</span>
            <span class="flex-1">How much?</span>
            <span aria-hidden="true" class="grid size-10 flex-none place-items-center border-3 border-tac11-ink bg-white transition-[rotate,background-color] duration-200 ease-out group-open:rotate-180 group-open:bg-tac11-pink motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="16" height="16"><path d="M8 2.5v10M3.5 8.5 8 13l4.5-4.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg></span>
          </summary>
          <div class="border-t-3 border-tac11-ink bg-[repeating-linear-gradient(180deg,transparent_0_27px,var(--color-tac11-rule)_27px_28px)] bg-origin-content bg-white px-4 pt-3.5 pb-4 sm:pl-[4.5rem]">
            <p class="text-sm leading-7">Free online, forever. The paper edition is $5 — photocopied, stapled crooked and mailed with a sticker you will put on your laptop.</p>
          </div>
        </details>

        <details class="group border-3 border-tac11-ink bg-white shadow-[6px_6px_0_var(--color-tac11-ink)] transition-[translate,box-shadow] duration-150 ease-out hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[4px_4px_0_var(--color-tac11-ink)] open:translate-x-1 open:translate-y-1 open:shadow-[2px_2px_0_var(--color-tac11-ink)] motion-reduce:transition-none details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-200 details-content:ease-out open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-4 px-4 py-3 text-[15px] font-bold tracking-[0.08em] uppercase select-none focus-visible:outline-4 focus-visible:outline-offset-4 focus-visible:outline-tac11-ink [&::-webkit-details-marker]:hidden">
            <span class="grid size-10 flex-none place-items-center border-3 border-tac11-ink bg-white text-sm transition-colors duration-150 group-open:bg-tac11-ink group-open:text-tac11-cyan">03</span>
            <span class="flex-1">Can I submit?</span>
            <span aria-hidden="true" class="grid size-10 flex-none place-items-center border-3 border-tac11-ink bg-white transition-[rotate,background-color] duration-200 ease-out group-open:rotate-180 group-open:bg-tac11-cyan motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="16" height="16"><path d="M8 2.5v10M3.5 8.5 8 13l4.5-4.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg></span>
          </summary>
          <div class="border-t-3 border-tac11-ink bg-[repeating-linear-gradient(180deg,transparent_0_27px,var(--color-tac11-rule)_27px_28px)] bg-origin-content bg-white px-4 pt-3.5 pb-4 sm:pl-[4.5rem]">
            <p class="text-sm leading-7">Yes. 500 words max, no pitches, no PDFs. Send plain text or a URL. If your site needs a cookie banner, it's a no.</p>
          </div>
        </details>
      </div>

      <div class="mt-9 flex flex-wrap items-center gap-4">
        <a href="#tac11-subscribe" id="tac11-subscribe" class="inline-flex min-h-12 items-center gap-2.5 border-3 border-tac11-ink bg-tac11-pink px-5 text-sm font-bold tracking-[0.1em] uppercase shadow-[5px_5px_0_var(--color-tac11-ink)] transition-[translate,box-shadow] duration-100 hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[3px_3px_0_var(--color-tac11-ink)] active:translate-x-1 active:translate-y-1 active:shadow-[1px_1px_0_var(--color-tac11-ink)] focus-visible:outline-4 focus-visible:outline-offset-4 focus-visible:outline-tac11-ink motion-reduce:transition-none">Get the paper — $5<svg aria-hidden="true" viewBox="0 0 16 16" width="16" height="16"><path d="M2.5 8h10M8.5 3.5 13 8l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg></a>
        <p class="bg-tac11-ink px-2.5 py-1.5 text-xs font-bold tracking-[0.1em] text-tac11-yellow uppercase">2,914 readers · 0 ads</p>
      </div>
    </div>
    <p aria-hidden="true" class="border-3 border-tac11-ink bg-white px-3.5 py-2 text-center text-[11.5px]">open:translate-x-1 · open:shadow-[2px_2px_0_…] · group-open:rotate-180</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac11-bg: #ffe14d;
  --color-tac11-bg: oklch(0.91 0.17 98);
  --color-tac11-ink: #111111;
  --color-tac11-ink: oklch(0.18 0 0);
  --color-tac11-yellow: #ffe14d;
  --color-tac11-yellow: oklch(0.91 0.17 98);
  --color-tac11-pink: #ff6bb5;
  --color-tac11-pink: oklch(0.73 0.2 350);
  --color-tac11-cyan: #3ee0f0;
  --color-tac11-cyan: oklch(0.84 0.13 205);
  --color-tac11-rule: #e9e3cf;
  --color-tac11-rule: oklch(0.92 0.025 95);
  --font-tac11-display: 'Bricolage Grotesque', 'Arial Black', system-ui, sans-serif;
  --font-tac11-mono: 'Space Mono', ui-monospace, 'Cascadia Code', Menlo, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-11 {
  width: 100%;
  min-height: 100svh;
}
```
