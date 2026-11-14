---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-animated-strikethrough-text-hover-effect/"
title: "Tailwind Animated Strikethrough Text Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A pen stroke drawn across text in three real contexts: a compare-at price that's crossed out while you aim at the buy row, a to-do list where…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Strikethrough Text Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-animated-strikethrough-text-hover-effect/

A pen stroke drawn across text in three real contexts: a compare-at price that's crossed out while you aim at the buy row, a to-do list where group-has-checked/todo: draws the line with zero JS, and a sold-out link whose line enters left and exits right via not-hover:after:origin-right.
## HTML
```html
<section class="tth-04 @container w-full min-h-svh grid place-items-center bg-tth04-bg px-5 py-14 font-tth04-sans text-tth04-ink" aria-label="Animated strike-through demo">
  <div class="flex w-full max-w-[45rem] flex-col gap-5">
    <article class="rounded-[18px] border border-tth04-line bg-white p-[clamp(18px,3.4cqi,28px)] shadow-[0_1px_0_white_inset,0_18px_44px_-12px_oklch(0.4_0.04_60/0.16)]">
      <header class="flex items-center justify-between gap-3">
        <h2 class="text-[17px] font-extrabold tracking-[-0.01em]">Studio membership</h2>
        <span class="rounded-full border border-tth04-pen/40 bg-tth04-pen/6 px-2.5 py-1 text-[10.5px] font-bold uppercase tracking-[0.1em] text-tth04-pen">Spring pricing</span>
      </header>
      <a id="tth04-top" href="#tth04-top" class="group/buy mt-4 flex min-h-16 items-center justify-between gap-4 rounded-[13px] border-[1.5px] border-tth04-line px-[18px] py-3.5 no-underline transition-[border-color,background-color] duration-300 hover:border-tth04-ink hover:bg-tth04-bg/50 focus-visible:border-tth04-ink focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth04-pen @max-[37rem]:flex-col @max-[37rem]:items-start">
        <span class="flex items-baseline gap-3.5">
          <s class="text-[clamp(19px,3cqi,24px)] font-semibold text-tth04-mut no-underline transition-colors duration-350 group-hover/buy:text-tth04-mut/55 group-focus-visible/buy:text-tth04-mut/55"><span class="sr-only">Was </span><span class="relative inline-block after:absolute after:inset-x-[-3%] after:top-[calc(50%-0.045em)] after:h-[0.09em] after:rotate-[-1.5deg] after:origin-left after:scale-x-0 after:rounded-[0.05em] after:bg-tth04-pen after:transition-transform after:duration-350 after:ease-[cubic-bezier(.65,.05,.36,1)] after:content-[''] group-hover/buy:after:scale-x-100 group-focus-visible/buy:after:scale-x-100 motion-reduce:after:transition-none">$79</span></s>
          <b class="text-[clamp(26px,4.4cqi,36px)] font-extrabold tracking-[-0.02em]"><span class="sr-only">now </span>$49<small class="text-[0.5em] font-semibold text-tth04-mut">/mo</small></b>
        </span>
        <span class="inline-flex items-center gap-1.5 whitespace-nowrap rounded-full bg-tth04-ink px-4 py-2 text-[14.5px] font-bold text-white transition-colors duration-300 group-hover/buy:bg-tth04-pen group-focus-visible/buy:bg-tth04-pen">Lock it in <span aria-hidden="true" class="transition-transform duration-300 group-hover/buy:translate-x-0.5">&rarr;</span></span>
      </a>
      <p class="mt-3 text-[12.5px] text-tth04-mut">Hover the row: the compare-at price is crossed out while you aim at the button.</p>
    </article>
    <div class="grid grid-cols-[1.25fr_1fr] items-start gap-[clamp(14px,2.6cqi,22px)] @max-[37rem]:grid-cols-1">
      <ul class="flex flex-col rounded-2xl border border-tth04-line bg-white p-2" aria-label="Launch checklist">
        <li class="group/todo"><label class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[10px] px-3 text-[15px] font-semibold transition-colors duration-300 hover:bg-tth04-bg has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tth04-pen group-has-checked/todo:text-tth04-mut"><input type="checkbox" class="peer sr-only" checked><i aria-hidden="true" class="grid size-[19px] flex-none place-items-center rounded-md border-[1.7px] border-tth04-mut transition-colors duration-250 before:h-[5px] before:w-[9px] before:-translate-y-px before:-rotate-45 before:border-b-2 before:border-l-2 before:border-white before:opacity-0 before:content-[''] group-has-checked/todo:border-tth04-pen group-has-checked/todo:bg-tth04-pen group-has-checked/todo:before:opacity-100"></i><span class="relative inline-block after:absolute after:inset-x-[-3%] after:top-[calc(50%-0.045em)] after:h-[0.09em] after:rotate-[-1.5deg] after:origin-left after:scale-x-0 after:rounded-[0.05em] after:bg-tth04-pen after:transition-transform after:duration-350 after:ease-[cubic-bezier(.65,.05,.36,1)] after:content-[''] group-has-checked/todo:after:scale-x-100 motion-reduce:after:transition-none">Freeze the type scale</span></label></li>
        <li class="group/todo"><label class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[10px] px-3 text-[15px] font-semibold transition-colors duration-300 hover:bg-tth04-bg has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tth04-pen group-has-checked/todo:text-tth04-mut"><input type="checkbox" class="peer sr-only"><i aria-hidden="true" class="grid size-[19px] flex-none place-items-center rounded-md border-[1.7px] border-tth04-mut transition-colors duration-250 before:h-[5px] before:w-[9px] before:-translate-y-px before:-rotate-45 before:border-b-2 before:border-l-2 before:border-white before:opacity-0 before:content-[''] group-has-checked/todo:border-tth04-pen group-has-checked/todo:bg-tth04-pen group-has-checked/todo:before:opacity-100"></i><span class="relative inline-block after:absolute after:inset-x-[-3%] after:top-[calc(50%-0.045em)] after:h-[0.09em] after:rotate-[-1.5deg] after:origin-left after:scale-x-0 after:rounded-[0.05em] after:bg-tth04-pen after:transition-transform after:duration-350 after:ease-[cubic-bezier(.65,.05,.36,1)] after:content-[''] group-has-checked/todo:after:scale-x-100 motion-reduce:after:transition-none">Ship dark mode tokens</span></label></li>
        <li class="group/todo"><label class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[10px] px-3 text-[15px] font-semibold transition-colors duration-300 hover:bg-tth04-bg has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tth04-pen group-has-checked/todo:text-tth04-mut"><input type="checkbox" class="peer sr-only"><i aria-hidden="true" class="grid size-[19px] flex-none place-items-center rounded-md border-[1.7px] border-tth04-mut transition-colors duration-250 before:h-[5px] before:w-[9px] before:-translate-y-px before:-rotate-45 before:border-b-2 before:border-l-2 before:border-white before:opacity-0 before:content-[''] group-has-checked/todo:border-tth04-pen group-has-checked/todo:bg-tth04-pen group-has-checked/todo:before:opacity-100"></i><span class="relative inline-block after:absolute after:inset-x-[-3%] after:top-[calc(50%-0.045em)] after:h-[0.09em] after:rotate-[-1.5deg] after:origin-left after:scale-x-0 after:rounded-[0.05em] after:bg-tth04-pen after:transition-transform after:duration-350 after:ease-[cubic-bezier(.65,.05,.36,1)] after:content-[''] group-has-checked/todo:after:scale-x-100 motion-reduce:after:transition-none">Audit hover states</span></label></li>
      </ul>
      <nav class="flex flex-col gap-1.5 rounded-2xl border border-tth04-line bg-white p-3.5" aria-label="Editions">
        <a href="#tth04-top" class="flex min-h-11 items-center gap-2.5 rounded-[9px] px-2.5 text-base font-bold tracking-[-0.01em] no-underline hover:bg-tth04-bg focus-visible:bg-tth04-bg focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth04-pen">Spring drop</a>
        <a href="#tth04-top" aria-label="Winter drop, sold out" class="relative flex min-h-11 items-center gap-2.5 rounded-[9px] px-2.5 text-base font-bold tracking-[-0.01em] text-tth04-mut no-underline after:absolute after:left-1.5 after:top-[calc(50%-1px)] after:h-0.5 after:w-[calc(100%-90px)] after:origin-left after:scale-x-0 after:rounded-sm after:bg-tth04-pen after:transition-transform after:duration-400 after:ease-[cubic-bezier(.65,.05,.36,1)] after:content-[''] hover:bg-tth04-bg hover:after:scale-x-100 focus-visible:bg-tth04-bg focus-visible:after:scale-x-100 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth04-pen not-hover:not-focus-visible:after:origin-right motion-reduce:after:transition-none">Winter drop<em aria-hidden="true" class="text-[10px] font-extrabold uppercase not-italic tracking-[0.12em] text-tth04-pen">sold out</em></a>
      </nav>
    </div>
    <p class="text-[12.5px] text-tth04-mut">Tick the boxes &mdash; <code class="rounded bg-tth04-ink/6 px-1.5 py-px font-tth04-mono text-[0.9em]">group-has-checked/todo:</code> draws the strike with zero JS. The sold-out link's line enters left, exits right.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth04-bg: #f7f4ed;
  --color-tth04-bg: oklch(0.972 0.008 85);
  --color-tth04-ink: #2c2118;
  --color-tth04-ink: oklch(0.26 0.02 55);
  --color-tth04-mut: #685c52;
  --color-tth04-mut: oklch(0.48 0.02 60);
  --color-tth04-pen: #d32f2f;
  --color-tth04-pen: oklch(0.55 0.21 27);
  --color-tth04-line: #e1dbcf;
  --color-tth04-line: oklch(0.88 0.014 80);
  --font-tth04-sans: 'Manrope', system-ui, sans-serif;
  --font-tth04-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-04 {
  width: 100%;
  min-height: 100svh;
}
```
