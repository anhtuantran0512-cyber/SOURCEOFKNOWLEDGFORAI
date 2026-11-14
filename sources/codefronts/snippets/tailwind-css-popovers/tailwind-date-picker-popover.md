---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-date-picker-popover/"
title: "Tailwind Date Picker Popover"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "A calendar tethered to a date field — the field wrapper is the anchor, the icon button is only the invoker — with the month as a seven-column grid of…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Date Picker Popover
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-date-picker-popover/

A calendar tethered to a date field — the field wrapper is the anchor, the icon button is only the invoker — with the month as a seven-column grid of tabular-nums cells. No date logic; the lesson is tethering and legibility at 320px. The port fixes the original's invalid role="grid" (grids require rows and gridcells), and marks today with a dot and the selection with fill and weight.
## HTML
```html
<section class="tpop-14 transition-[--tpop14-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop14-d:1] [[data-theme=dark]_&]:[--tpop14-d:1] [[data-theme=light]_&]:[--tpop14-d:0] group/root w-full min-h-svh bg-tpop14-bg px-4.5 py-10 font-tpop14-sans text-tpop14-ink" aria-label="Date picker popover demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[24rem] rounded-2xl border border-tpop14-rule bg-tpop14-surface px-4.5 pt-5 pb-4.5 shadow-[0_18px_40px_-32px_oklch(0.3_0.03_70/0.5)]">
      <p class="mb-4 text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop14-sel">Booking · Studio 2</p>
      <label for="tpop-14-date" class="mb-1.5 block text-[12.5px] font-semibold text-tpop14-mut">Session date</label>
      <div class="flex items-center gap-1 rounded-xl border border-tpop14-rule bg-tpop14-surface pr-1 transition-[border-color,box-shadow] duration-150 [anchor-name:--tpop14-a] focus-within:border-tpop14-sel group-has-[#tpop-14-cal:popover-open]/root:border-tpop14-sel group-has-[#tpop-14-cal:popover-open]/root:shadow-[0_0_0_3px_oklch(0.47_0.07_150/0.15)]">
        <input id="tpop-14-date" type="text" value="14 September 2026" readonly aria-describedby="tpop-14-help" class="min-h-11 min-w-0 flex-auto rounded-l-xl bg-transparent px-3 text-[14px] font-medium text-tpop14-ink focus-visible:outline-3 focus-visible:-outline-offset-1 focus-visible:outline-tpop14-sel">
        <button id="tpop-14-trigger" type="button" popovertarget="tpop-14-cal" aria-label="Choose a date" class="inline-flex size-11 flex-none cursor-pointer items-center justify-center rounded-lg text-tpop14-mut transition-colors hover:bg-tpop14-bg hover:text-tpop14-sel focus-visible:outline-3 focus-visible:-outline-offset-2 focus-visible:outline-tpop14-sel group-has-[#tpop-14-cal:popover-open]/root:bg-tpop14-sel/10 group-has-[#tpop-14-cal:popover-open]/root:text-tpop14-sel">
          <svg viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="4.6" width="14" height="12" rx="2"/><path d="M3 8.4h14M7 3v2.6M13 3v2.6"/></svg>
        </button>
      </div>
      <p id="tpop-14-help" class="mt-2.5 text-[12.5px] leading-relaxed text-tpop14-mut">The field is the anchor. The icon button is only the invoker.</p>
    </div>
  </div>

  <div popover="auto" id="tpop-14-cal" role="group" aria-label="September 2026" class="fixed m-auto w-[min(20rem,calc(100vw-28px))] rounded-2xl border border-tpop14-rule bg-tpop14-surface p-3.5 text-tpop14-ink opacity-0 shadow-[0_24px_48px_-26px_oklch(0.3_0.03_70/0.5)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop14-a] [position-area:block-end_span-inline-end] [position-try-fallbacks:flip-block] open:opacity-100 starting:open:-translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2">
    <div class="mb-3 flex items-baseline justify-between gap-2.5 px-1">
      <span class="font-tpop14-serif text-[22px] leading-none">September <span class="italic text-tpop14-mut">2026</span></span>
      <span class="text-[10px] font-semibold uppercase tracking-[0.14em] text-tpop14-mut">static month</span>
    </div>
    <div class="mb-1 grid grid-cols-7 gap-0.5 text-center text-[10.5px] font-bold text-tpop14-mut" aria-hidden="true">
      <span>M</span><span>T</span><span>W</span><span>T</span><span>F</span><span class="text-tpop14-sel">S</span><span class="text-tpop14-sel">S</span>
    </div>
    <div class="grid grid-cols-7 gap-0.5 text-[13px] tabular-nums" aria-label="Days in September 2026">
      <span class="grid aspect-square min-h-9 place-items-center rounded-lg text-tpop14-mut/55">31</span>
      <span class="grid aspect-square min-h-9 place-items-center rounded-lg">1</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">2</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">3</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">4</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-bg">5</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-bg">6</span>
      <span class="grid aspect-square min-h-9 place-items-center rounded-lg">7</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">8</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">9</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">10</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">11</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-bg">12</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-bg">13</span>
      <span aria-selected="true" class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-sel font-bold text-tpop14-surface shadow-[0_6px_14px_-6px_oklch(0.47_0.07_150/0.8)]">14</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">15</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">16</span><span aria-current="date" class="relative grid aspect-square min-h-9 place-items-center rounded-lg font-semibold text-tpop14-sel after:absolute after:bottom-1 after:size-1 after:rounded-full after:bg-tpop14-sel after:content-['']">17</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">18</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-bg">19</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-bg">20</span>
      <span class="grid aspect-square min-h-9 place-items-center rounded-lg">21</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">22</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">23</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">24</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">25</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-bg">26</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg bg-tpop14-bg">27</span>
      <span class="grid aspect-square min-h-9 place-items-center rounded-lg">28</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">29</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg">30</span>
      <span class="grid aspect-square min-h-9 place-items-center rounded-lg text-tpop14-mut/55">1</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg text-tpop14-mut/55">2</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg text-tpop14-mut/55">3</span><span class="grid aspect-square min-h-9 place-items-center rounded-lg text-tpop14-mut/55">4</span>
    </div>
    <p class="mt-3 flex items-center gap-3 border-t border-tpop14-rule px-1 pt-2.5 text-[11.5px] text-tpop14-mut"><span class="inline-flex items-center gap-1.5"><span aria-hidden="true" class="size-2.5 rounded-[3px] bg-tpop14-sel"></span>Selected</span><span class="inline-flex items-center gap-1.5"><span aria-hidden="true" class="size-1 rounded-full bg-tpop14-sel"></span>Today</span></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop14-bg: #f2ece4;
  --color-tpop14-bg: oklch(0.945 0.012 75);
  --color-tpop14-surface: #fffdfa;
  --color-tpop14-surface: oklch(0.995 0.004 80);
  --color-tpop14-ink: #26201a;
  --color-tpop14-ink: oklch(0.25 0.015 70);
  --color-tpop14-mut: #675b4f;
  --color-tpop14-mut: oklch(0.48 0.025 70);
  --color-tpop14-rule: #dfd6cb;
  --color-tpop14-rule: oklch(0.88 0.018 75);
  --color-tpop14-sel: #3d6646;
  --color-tpop14-sel: oklch(0.47 0.07 150);
  --font-tpop14-serif: 'Instrument Serif', Georgia, serif;
  --font-tpop14-sans: 'Geist', system-ui, sans-serif;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop14-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-14 {
  width: 100%;
  min-height: 100svh;
  --color-tpop14-bg: color-mix(in oklch, oklch(0.17 0.012 70) calc(var(--tpop14-d) * 100%), oklch(0.945 0.012 75));
  --color-tpop14-surface: color-mix(in oklch, oklch(0.215 0.014 70) calc(var(--tpop14-d) * 100%), oklch(0.995 0.004 80));
  --color-tpop14-ink: color-mix(in oklch, oklch(0.94 0.014 80) calc(var(--tpop14-d) * 100%), oklch(0.25 0.015 70));
  --color-tpop14-mut: color-mix(in oklch, oklch(0.74 0.025 75) calc(var(--tpop14-d) * 100%), oklch(0.48 0.025 70));
  --color-tpop14-rule: color-mix(in oklch, oklch(0.32 0.018 70) calc(var(--tpop14-d) * 100%), oklch(0.88 0.018 75));
  --color-tpop14-sel: color-mix(in oklch, oklch(0.76 0.09 150) calc(var(--tpop14-d) * 100%), oklch(0.47 0.07 150));
}
```
