---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-filter-dropdown-checkboxes/"
title: "Tailwind Filter Dropdown with Checkboxes"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "The clearest real use of popover=\"manual\": a filter menu you tick several boxes in, which must not vanish because a click landed just outside it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Filter Dropdown with Checkboxes
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-filter-dropdown-checkboxes/

The clearest real use of popover="manual": a filter menu you tick several boxes in, which must not vanish because a click landed just outside it. The port makes the panel live with zero JS — a CSS counter ([counter-reset:tpop15] + checked:[counter-increment:tpop15]) prints how many filters are ticked, the chip shows a dot whenever any are, and a native type="reset" restores the defaults.
## HTML
```html
<section class="tpop-15 transition-[--tpop15-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop15-d:1] [[data-theme=dark]_&]:[--tpop15-d:1] [[data-theme=light]_&]:[--tpop15-d:0] group/root w-full min-h-svh bg-tpop15-bg px-4 py-9.5 font-tpop15-sans text-tpop15-ink" aria-label="Filter dropdown with checkboxes demo">
  <div class="grid min-h-[calc(100svh-76px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[33rem] border-2 border-tpop15-ink bg-tpop15-surface shadow-[7px_7px_0_var(--color-tpop15-ember)]">
      <div class="flex flex-wrap items-center justify-between gap-2.5 border-b-2 border-tpop15-ink px-3 py-2.5">
        <span class="min-w-0 font-tpop15-mono text-[13px] font-semibold leading-tight">Shipments · 1,284 rows</span>
        <button id="tpop-15-trigger" type="button" popovertarget="tpop-15-filters" popovertargetaction="show" class="relative inline-flex min-h-11 cursor-pointer items-center gap-2 border-2 border-tpop15-ink bg-tpop15-ink px-3 text-[12px] font-bold uppercase tracking-[0.05em] text-tpop15-surface transition-[translate,box-shadow] duration-100 [anchor-name:--tpop15-a] hover:-translate-x-0.5 hover:-translate-y-0.5 hover:shadow-[3px_3px_0_var(--color-tpop15-ember)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop15-ember motion-reduce:transition-none">
          <svg viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M2.5 4h11M4.5 8h7M6.5 12h3"/></svg>
          Filters
          <span aria-hidden="true" class="absolute -top-1.5 -right-1.5 hidden size-3 border-2 border-tpop15-surface bg-tpop15-ember group-has-[#tpop-15-filters_input:checked]/root:block"></span>
        </button>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse">
          <thead>
            <tr><th scope="col" class="border-b border-tpop15-hair px-3 py-2 text-left text-[10px] font-bold uppercase tracking-[0.16em] text-tpop15-mut">Ref</th><th scope="col" class="border-b border-tpop15-hair px-3 py-2 text-left text-[10px] font-bold uppercase tracking-[0.16em] text-tpop15-mut">Lane</th><th scope="col" class="border-b border-tpop15-hair px-3 py-2 text-left text-[10px] font-bold uppercase tracking-[0.16em] text-tpop15-mut">Status</th><th scope="col" class="border-b border-tpop15-hair px-3 py-2 text-right text-[10px] font-bold uppercase tracking-[0.16em] text-tpop15-mut">Weight</th></tr>
          </thead>
          <tbody class="font-tpop15-mono text-[12.5px]">
            <tr class="border-b border-tpop15-hair"><td class="px-3 py-2.5">SH-8841</td><td class="px-3 py-2.5 whitespace-nowrap">Rotterdam → Leeds</td><td class="px-3 py-2.5"><span class="bg-tpop15-ink/8 px-1.5 py-0.5 text-[11px]">transit</span></td><td class="px-3 py-2.5 text-right whitespace-nowrap text-tpop15-mut tabular-nums">1,240 kg</td></tr>
            <tr class="border-b border-tpop15-hair"><td class="px-3 py-2.5">SH-8842</td><td class="px-3 py-2.5 whitespace-nowrap">Gdansk → Bremen</td><td class="px-3 py-2.5"><span class="bg-tpop15-ember/15 px-1.5 py-0.5 text-[11px] text-tpop15-emberdeep">customs</span></td><td class="px-3 py-2.5 text-right whitespace-nowrap text-tpop15-mut tabular-nums">860 kg</td></tr>
            <tr class="border-b border-tpop15-hair"><td class="px-3 py-2.5">SH-8843</td><td class="px-3 py-2.5 whitespace-nowrap">Vigo → Nantes</td><td class="px-3 py-2.5"><span class="bg-tpop15-ink/8 px-1.5 py-0.5 text-[11px]">transit</span></td><td class="px-3 py-2.5 text-right whitespace-nowrap text-tpop15-mut tabular-nums">3,105 kg</td></tr>
            <tr><td class="px-3 py-2.5">SH-8844</td><td class="px-3 py-2.5 whitespace-nowrap">Oslo → Aarhus</td><td class="px-3 py-2.5"><span class="bg-tpop15-ink px-1.5 py-0.5 text-[11px] text-tpop15-surface">exception</span></td><td class="px-3 py-2.5 text-right whitespace-nowrap text-tpop15-mut tabular-nums">412 kg</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div popover="manual" id="tpop-15-filters" role="group" aria-labelledby="tpop-15-legend" class="fixed m-auto w-[min(18rem,calc(100vw-24px))] border-2 border-tpop15-ink bg-tpop15-surface p-3.5 text-tpop15-ink opacity-0 shadow-[7px_7px_0_var(--color-tpop15-ember)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop15-a] [position-area:block-end_span-inline-start] [position-try-fallbacks:flip-block,flip-inline] open:opacity-100 starting:open:-translate-y-1.5 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2.5">
    <div class="mb-1.5 flex items-center justify-between gap-2">
      <p id="tpop-15-legend" class="text-[11.5px] font-bold uppercase tracking-[0.16em]">Filter shipments</p>
      <button type="button" popovertarget="tpop-15-filters" popovertargetaction="hide" aria-label="Close filters" class="-my-3 -mr-3 inline-flex size-11 cursor-pointer items-center justify-center hover:text-tpop15-emberdeep focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop15-ember">
        <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg>
      </button>
    </div>
    <form class="[counter-reset:tpop15]">
      <fieldset class="grid">
        <legend class="mb-1 font-tpop15-mono text-[11px] font-semibold uppercase tracking-[0.1em] text-tpop15-mut">Status</legend>
        <label class="flex min-h-11 min-w-0 cursor-pointer items-center gap-2.5 text-[14px] hover:text-tpop15-emberdeep"><input type="checkbox" checked class="size-4.5 flex-none cursor-pointer accent-tpop15-ember checked:[counter-increment:tpop15] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop15-ember"> In transit</label>
        <label class="flex min-h-11 min-w-0 cursor-pointer items-center gap-2.5 text-[14px] hover:text-tpop15-emberdeep"><input type="checkbox" checked class="size-4.5 flex-none cursor-pointer accent-tpop15-ember checked:[counter-increment:tpop15] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop15-ember"> Held at customs</label>
        <label class="flex min-h-11 min-w-0 cursor-pointer items-center gap-2.5 text-[14px] hover:text-tpop15-emberdeep"><input type="checkbox" class="size-4.5 flex-none cursor-pointer accent-tpop15-ember checked:[counter-increment:tpop15] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop15-ember"> Delivered</label>
        <label class="flex min-h-11 min-w-0 cursor-pointer items-center gap-2.5 text-[14px] hover:text-tpop15-emberdeep"><input type="checkbox" checked class="size-4.5 flex-none cursor-pointer accent-tpop15-ember checked:[counter-increment:tpop15] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop15-ember"> Exception raised</label>
        <label class="flex min-h-11 min-w-0 cursor-pointer items-center gap-2.5 text-[14px] hover:text-tpop15-emberdeep"><input type="checkbox" class="size-4.5 flex-none cursor-pointer accent-tpop15-ember checked:[counter-increment:tpop15] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop15-ember"> Cancelled</label>
      </fieldset>
      <p class="mt-2 mb-3 flex items-center justify-between gap-2 border-t border-tpop15-hair pt-2.5 text-[12.5px] font-semibold">
        <span><span class="font-tpop15-mono text-tpop15-emberdeep after:content-[counter(tpop15)]"></span> selected · click the table, I stay</span>
        <button type="reset" class="min-h-11 cursor-pointer px-1 text-[12px] font-bold uppercase tracking-[0.05em] text-tpop15-mut underline underline-offset-4 hover:text-tpop15-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop15-ember">Reset</button>
      </p>
      <div class="flex flex-wrap gap-2">
        <button type="button" popovertarget="tpop-15-filters" popovertargetaction="hide" class="min-h-11 min-w-0 flex-auto cursor-pointer border-2 border-tpop15-ink bg-tpop15-ink px-3 text-[12px] font-bold uppercase tracking-[0.06em] text-tpop15-surface transition-colors hover:bg-tpop15-ember hover:border-tpop15-ember hover:text-tpop15-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop15-ember">Apply filters</button>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop15-bg: #f2f2ef;
  --color-tpop15-bg: oklch(0.96 0.003 95);
  --color-tpop15-surface: #ffffff;
  --color-tpop15-surface: oklch(1 0 0);
  --color-tpop15-ink: #181614;
  --color-tpop15-ink: oklch(0.2 0.005 70);
  --color-tpop15-mut: #5e5a55;
  --color-tpop15-mut: oklch(0.47 0.01 75);
  --color-tpop15-hair: #dfdeda;
  --color-tpop15-hair: oklch(0.9 0.006 95);
  --color-tpop15-ember: #e04f1a;
  --color-tpop15-ember: oklch(0.62 0.19 38);
  --color-tpop15-emberdeep: #af2f02;
  --color-tpop15-emberdeep: oklch(0.5 0.17 36);
  --font-tpop15-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpop15-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop15-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-15 {
  width: 100%;
  min-height: 100svh;
  --color-tpop15-bg: color-mix(in oklch, oklch(0.16 0.004 70) calc(var(--tpop15-d) * 100%), oklch(0.96 0.003 95));
  --color-tpop15-surface: color-mix(in oklch, oklch(0.205 0.005 70) calc(var(--tpop15-d) * 100%), oklch(1 0 0));
  --color-tpop15-ink: color-mix(in oklch, oklch(0.95 0.006 90) calc(var(--tpop15-d) * 100%), oklch(0.2 0.005 70));
  --color-tpop15-mut: color-mix(in oklch, oklch(0.73 0.01 80) calc(var(--tpop15-d) * 100%), oklch(0.47 0.01 75));
  --color-tpop15-hair: color-mix(in oklch, oklch(0.3 0.006 70) calc(var(--tpop15-d) * 100%), oklch(0.9 0.006 95));
  --color-tpop15-ember: color-mix(in oklch, oklch(0.72 0.17 40) calc(var(--tpop15-d) * 100%), oklch(0.62 0.19 38));
  --color-tpop15-emberdeep: color-mix(in oklch, oklch(0.78 0.15 42) calc(var(--tpop15-d) * 100%), oklch(0.5 0.17 36));
}
```
