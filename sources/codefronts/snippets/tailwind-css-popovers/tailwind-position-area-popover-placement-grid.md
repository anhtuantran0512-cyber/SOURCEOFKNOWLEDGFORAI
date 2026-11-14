---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-position-area-popover-placement-grid/"
title: "Tailwind Position Area Popover Placement Grid"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "position-area treats the space around an anchor as a 3×3 grid and lets you name a cell."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Position Area Popover Placement Grid
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-position-area-popover-placement-grid/

position-area treats the space around an anchor as a 3×3 grid and lets you name a cell. This board makes it literal: eight buttons around one anchor, each opening a panel in its own cell — and in the port, each panel's placement is one arbitrary property you can read off the markup: [position-area:block-start_inline-start]. The panel also prints its physical equivalent, and the cell that opened it lights up while it's open.
## HTML
```html
<section class="tpop-06 transition-[--tpop06-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop06-d:1] [[data-theme=dark]_&]:[--tpop06-d:1] [[data-theme=light]_&]:[--tpop06-d:0] group/root w-full min-h-svh bg-tpop06-bg px-4 py-9 font-tpop06-sans text-tpop06-ink" aria-label="Position area placement grid demo">
  <div class="grid min-h-[calc(100svh-72px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[30rem]">
      <p class="mb-3 font-tpop06-mono text-[11px] font-semibold uppercase tracking-[0.1em] text-tpop06-mut">position-area · nine cells, one anchor</p>
      <div class="grid grid-cols-3 gap-0.5 overflow-hidden rounded-lg border border-tpop06-rule bg-tpop06-rule">
        <button id="tpop-06-trigger" type="button" popovertarget="tpop-06-p1" class="min-h-16 min-w-0 cursor-pointer bg-tpop06-surface px-1 py-1.5 font-tpop06-mono text-[10.5px] font-semibold leading-snug text-tpop06-mut transition-colors hover:bg-tpop06-acc/8 hover:text-tpop06-ink focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop06-acc group-has-[#tpop-06-p1:popover-open]/root:bg-tpop06-acc group-has-[#tpop-06-p1:popover-open]/root:text-tpop06-surface">block-start<br>inline-start</button>
        <button type="button" popovertarget="tpop-06-p2" class="min-h-16 min-w-0 cursor-pointer bg-tpop06-surface px-1 py-1.5 font-tpop06-mono text-[10.5px] font-semibold leading-snug text-tpop06-mut transition-colors hover:bg-tpop06-acc/8 hover:text-tpop06-ink focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop06-acc group-has-[#tpop-06-p2:popover-open]/root:bg-tpop06-acc group-has-[#tpop-06-p2:popover-open]/root:text-tpop06-surface">block-start<br>center</button>
        <button type="button" popovertarget="tpop-06-p3" class="min-h-16 min-w-0 cursor-pointer bg-tpop06-surface px-1 py-1.5 font-tpop06-mono text-[10.5px] font-semibold leading-snug text-tpop06-mut transition-colors hover:bg-tpop06-acc/8 hover:text-tpop06-ink focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop06-acc group-has-[#tpop-06-p3:popover-open]/root:bg-tpop06-acc group-has-[#tpop-06-p3:popover-open]/root:text-tpop06-surface">block-start<br>inline-end</button>
        <button type="button" popovertarget="tpop-06-p4" class="min-h-16 min-w-0 cursor-pointer bg-tpop06-surface px-1 py-1.5 font-tpop06-mono text-[10.5px] font-semibold leading-snug text-tpop06-mut transition-colors hover:bg-tpop06-acc/8 hover:text-tpop06-ink focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop06-acc group-has-[#tpop-06-p4:popover-open]/root:bg-tpop06-acc group-has-[#tpop-06-p4:popover-open]/root:text-tpop06-surface">center<br>inline-start</button>
        <div class="grid min-h-16 place-items-center bg-tpop06-ink font-tpop06-mono text-[10.5px] font-bold tracking-[0.2em] text-tpop06-surface [anchor-name:--tpop06-a]">ANCHOR</div>
        <button type="button" popovertarget="tpop-06-p6" class="min-h-16 min-w-0 cursor-pointer bg-tpop06-surface px-1 py-1.5 font-tpop06-mono text-[10.5px] font-semibold leading-snug text-tpop06-mut transition-colors hover:bg-tpop06-acc/8 hover:text-tpop06-ink focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop06-acc group-has-[#tpop-06-p6:popover-open]/root:bg-tpop06-acc group-has-[#tpop-06-p6:popover-open]/root:text-tpop06-surface">center<br>inline-end</button>
        <button type="button" popovertarget="tpop-06-p7" class="min-h-16 min-w-0 cursor-pointer bg-tpop06-surface px-1 py-1.5 font-tpop06-mono text-[10.5px] font-semibold leading-snug text-tpop06-mut transition-colors hover:bg-tpop06-acc/8 hover:text-tpop06-ink focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop06-acc group-has-[#tpop-06-p7:popover-open]/root:bg-tpop06-acc group-has-[#tpop-06-p7:popover-open]/root:text-tpop06-surface">block-end<br>inline-start</button>
        <button type="button" popovertarget="tpop-06-p8" class="min-h-16 min-w-0 cursor-pointer bg-tpop06-surface px-1 py-1.5 font-tpop06-mono text-[10.5px] font-semibold leading-snug text-tpop06-mut transition-colors hover:bg-tpop06-acc/8 hover:text-tpop06-ink focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop06-acc group-has-[#tpop-06-p8:popover-open]/root:bg-tpop06-acc group-has-[#tpop-06-p8:popover-open]/root:text-tpop06-surface">block-end<br>center</button>
        <button type="button" popovertarget="tpop-06-p9" class="min-h-16 min-w-0 cursor-pointer bg-tpop06-surface px-1 py-1.5 font-tpop06-mono text-[10.5px] font-semibold leading-snug text-tpop06-mut transition-colors hover:bg-tpop06-acc/8 hover:text-tpop06-ink focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop06-acc group-has-[#tpop-06-p9:popover-open]/root:bg-tpop06-acc group-has-[#tpop-06-p9:popover-open]/root:text-tpop06-surface">block-end<br>inline-end</button>
      </div>
      <p class="mt-3.5 text-[13px] leading-relaxed text-tpop06-mut">Eight buttons, eight panels, one anchor. Every panel differs by a single arbitrary property.</p>
    </div>
  </div>

  <div popover="auto" id="tpop-06-p1" role="group" aria-label="block-start inline-start" class="fixed m-auto w-max max-w-[min(14rem,calc(100vw-24px))] rounded-md bg-tpop06-ink px-3 py-2.5 font-tpop06-mono text-[11.5px] font-semibold leading-snug text-tpop06-surface opacity-0 shadow-[0_12px_28px_-14px_oklch(0.2_0.02_260/0.7)] transition-[opacity,scale,display,overlay] duration-150 transition-discrete [position-anchor:--tpop06-a] [position-area:block-start_inline-start] open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mr-2 supports-[anchor-name:--a]:mb-2">block-start inline-start<span class="block pt-1 font-normal text-tpop06-surface/70">≈ top left</span></div>
  <div popover="auto" id="tpop-06-p2" role="group" aria-label="block-start center" class="fixed m-auto w-max max-w-[min(14rem,calc(100vw-24px))] rounded-md bg-tpop06-ink px-3 py-2.5 font-tpop06-mono text-[11.5px] font-semibold leading-snug text-tpop06-surface opacity-0 shadow-[0_12px_28px_-14px_oklch(0.2_0.02_260/0.7)] transition-[opacity,scale,display,overlay] duration-150 transition-discrete [position-anchor:--tpop06-a] [position-area:block-start_center] open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mb-2">block-start center<span class="block pt-1 font-normal text-tpop06-surface/70">≈ top</span></div>
  <div popover="auto" id="tpop-06-p3" role="group" aria-label="block-start inline-end" class="fixed m-auto w-max max-w-[min(14rem,calc(100vw-24px))] rounded-md bg-tpop06-ink px-3 py-2.5 font-tpop06-mono text-[11.5px] font-semibold leading-snug text-tpop06-surface opacity-0 shadow-[0_12px_28px_-14px_oklch(0.2_0.02_260/0.7)] transition-[opacity,scale,display,overlay] duration-150 transition-discrete [position-anchor:--tpop06-a] [position-area:block-start_inline-end] open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:ml-2 supports-[anchor-name:--a]:mb-2">block-start inline-end<span class="block pt-1 font-normal text-tpop06-surface/70">≈ top right</span></div>
  <div popover="auto" id="tpop-06-p4" role="group" aria-label="center inline-start" class="fixed m-auto w-max max-w-[min(14rem,calc(100vw-24px))] rounded-md bg-tpop06-ink px-3 py-2.5 font-tpop06-mono text-[11.5px] font-semibold leading-snug text-tpop06-surface opacity-0 shadow-[0_12px_28px_-14px_oklch(0.2_0.02_260/0.7)] transition-[opacity,scale,display,overlay] duration-150 transition-discrete [position-anchor:--tpop06-a] [position-area:center_inline-start] open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mr-2">center inline-start<span class="block pt-1 font-normal text-tpop06-surface/70">≈ left</span></div>
  <div popover="auto" id="tpop-06-p6" role="group" aria-label="center inline-end" class="fixed m-auto w-max max-w-[min(14rem,calc(100vw-24px))] rounded-md bg-tpop06-ink px-3 py-2.5 font-tpop06-mono text-[11.5px] font-semibold leading-snug text-tpop06-surface opacity-0 shadow-[0_12px_28px_-14px_oklch(0.2_0.02_260/0.7)] transition-[opacity,scale,display,overlay] duration-150 transition-discrete [position-anchor:--tpop06-a] [position-area:center_inline-end] open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:ml-2">center inline-end<span class="block pt-1 font-normal text-tpop06-surface/70">≈ right</span></div>
  <div popover="auto" id="tpop-06-p7" role="group" aria-label="block-end inline-start" class="fixed m-auto w-max max-w-[min(14rem,calc(100vw-24px))] rounded-md bg-tpop06-ink px-3 py-2.5 font-tpop06-mono text-[11.5px] font-semibold leading-snug text-tpop06-surface opacity-0 shadow-[0_12px_28px_-14px_oklch(0.2_0.02_260/0.7)] transition-[opacity,scale,display,overlay] duration-150 transition-discrete [position-anchor:--tpop06-a] [position-area:block-end_inline-start] open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mr-2 supports-[anchor-name:--a]:mt-2">block-end inline-start<span class="block pt-1 font-normal text-tpop06-surface/70">≈ bottom left</span></div>
  <div popover="auto" id="tpop-06-p8" role="group" aria-label="block-end center" class="fixed m-auto w-max max-w-[min(14rem,calc(100vw-24px))] rounded-md bg-tpop06-ink px-3 py-2.5 font-tpop06-mono text-[11.5px] font-semibold leading-snug text-tpop06-surface opacity-0 shadow-[0_12px_28px_-14px_oklch(0.2_0.02_260/0.7)] transition-[opacity,scale,display,overlay] duration-150 transition-discrete [position-anchor:--tpop06-a] [position-area:block-end_center] open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2">block-end center<span class="block pt-1 font-normal text-tpop06-surface/70">≈ bottom</span></div>
  <div popover="auto" id="tpop-06-p9" role="group" aria-label="block-end inline-end" class="fixed m-auto w-max max-w-[min(14rem,calc(100vw-24px))] rounded-md bg-tpop06-ink px-3 py-2.5 font-tpop06-mono text-[11.5px] font-semibold leading-snug text-tpop06-surface opacity-0 shadow-[0_12px_28px_-14px_oklch(0.2_0.02_260/0.7)] transition-[opacity,scale,display,overlay] duration-150 transition-discrete [position-anchor:--tpop06-a] [position-area:block-end_inline-end] open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:ml-2 supports-[anchor-name:--a]:mt-2">block-end inline-end<span class="block pt-1 font-normal text-tpop06-surface/70">≈ bottom right</span></div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop06-bg: #f0f2f4;
  --color-tpop06-bg: oklch(0.96 0.004 260);
  --color-tpop06-surface: #ffffff;
  --color-tpop06-surface: oklch(1 0 0);
  --color-tpop06-ink: #171b22;
  --color-tpop06-ink: oklch(0.22 0.015 260);
  --color-tpop06-mut: #545b66;
  --color-tpop06-mut: oklch(0.47 0.02 260);
  --color-tpop06-rule: #d4d8dd;
  --color-tpop06-rule: oklch(0.88 0.008 260);
  --color-tpop06-acc: #325ac2;
  --color-tpop06-acc: oklch(0.5 0.17 265);
  --font-tpop06-sans: 'Geist', system-ui, sans-serif;
  --font-tpop06-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop06-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-06 {
  width: 100%;
  min-height: 100svh;
  --color-tpop06-bg: color-mix(in oklch, oklch(0.17 0.01 260) calc(var(--tpop06-d) * 100%), oklch(0.96 0.004 260));
  --color-tpop06-surface: color-mix(in oklch, oklch(0.215 0.012 260) calc(var(--tpop06-d) * 100%), oklch(1 0 0));
  --color-tpop06-ink: color-mix(in oklch, oklch(0.95 0.006 260) calc(var(--tpop06-d) * 100%), oklch(0.22 0.015 260));
  --color-tpop06-mut: color-mix(in oklch, oklch(0.73 0.02 260) calc(var(--tpop06-d) * 100%), oklch(0.47 0.02 260));
  --color-tpop06-rule: color-mix(in oklch, oklch(0.3 0.014 260) calc(var(--tpop06-d) * 100%), oklch(0.88 0.008 260));
  --color-tpop06-acc: color-mix(in oklch, oklch(0.7 0.14 265) calc(var(--tpop06-d) * 100%), oklch(0.5 0.17 265));
}
```
