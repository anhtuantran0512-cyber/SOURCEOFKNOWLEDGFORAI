---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-dropdown-matching-anchor-width/"
title: "Tailwind Dropdown Matching Anchor Width"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "A panel exactly as wide as the control that opened it reads as part of that control."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dropdown Matching Anchor Width
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-dropdown-matching-anchor-width/

A panel exactly as wide as the control that opened it reads as part of that control. supports-[anchor-name:--a]:w-[anchor-size(width)] sizes the panel from its anchor live, with no offsetWidth — and because the variant is emitted after the base w-[min(23rem,…)], the fallback width is declared first for free. Resize the frame and the seam never opens.
## HTML
```html
<section class="tpop-09 transition-[--tpop09-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop09-d:1] [[data-theme=dark]_&]:[--tpop09-d:1] [[data-theme=light]_&]:[--tpop09-d:0] group/root w-full min-h-svh bg-tpop09-bg px-4.5 py-10 font-tpop09-sans text-tpop09-ink" aria-label="Dropdown matching anchor width demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <form class="w-full min-w-0 max-w-[25rem] rounded-xl border border-tpop09-rule bg-tpop09-surface px-4.5 pt-5 pb-4.5 shadow-[0_16px_36px_-28px_oklch(0.25_0.05_255/0.5)]" aria-label="Deployment target">
      <p class="mb-4 text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop09-brand">Deploy target</p>
      <label for="tpop-09-trigger" class="mb-1.5 block text-[12.5px] font-semibold text-tpop09-mut">Environment</label>
      <button id="tpop-09-trigger" type="button" popovertarget="tpop-09-list" class="flex min-h-11 w-full cursor-pointer items-center justify-between gap-2.5 rounded-lg border border-tpop09-rule bg-tpop09-surface px-3 text-left text-[14px] font-medium text-tpop09-ink transition-[border-color,border-radius,box-shadow] duration-150 [anchor-name:--tpop09-a] hover:border-tpop09-brand focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop09-brand group-has-[#tpop-09-list:popover-open]/root:border-tpop09-brand group-has-[#tpop-09-list:popover-open]/root:shadow-[0_0_0_3px_oklch(0.5_0.15_255/0.14)] supports-[anchor-name:--a]:group-has-[#tpop-09-list:popover-open]/root:rounded-b-none">
        <span class="flex min-w-0 items-center gap-2"><span aria-hidden="true" class="size-2 flex-none rounded-full bg-tpop09-ok"></span><span class="truncate">Production · eu-west-1</span></span>
        <svg class="flex-none text-tpop09-mut transition-transform duration-200 motion-reduce:transition-none group-has-[#tpop-09-list:popover-open]/root:rotate-180" viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>
      </button>
      <p class="mt-2 mb-3.5 text-[12.5px] text-tpop09-mut">The list below takes its width from this button, live. Resize the frame.</p>
      <div class="flex flex-wrap gap-1.5">
        <span class="rounded-md bg-tpop09-brand/10 px-2 py-1.5 font-tpop09-mono text-[11px] font-semibold leading-tight text-tpop09-brand">w-[anchor-size(width)]</span>
        <span class="rounded-md bg-tpop09-bg px-2 py-1.5 font-tpop09-mono text-[11px] font-semibold leading-tight text-tpop09-mut">min-w variant in notes</span>
      </div>
    </form>
  </div>

  <div popover="auto" id="tpop-09-list" role="group" aria-label="Environments" class="fixed m-auto w-[min(23rem,calc(100vw-32px))] rounded-lg border border-tpop09-brand bg-tpop09-surface p-1.5 text-tpop09-ink opacity-0 shadow-[0_18px_36px_-20px_oklch(0.25_0.05_255/0.55)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop09-a] [position-area:block-end_span-inline-end] open:opacity-100 starting:open:-translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:w-[anchor-size(width)] supports-[anchor-name:--a]:rounded-t-none supports-[anchor-name:--a]:border-t-0">
    <p class="flex min-w-0 items-center gap-2.5 rounded-md bg-tpop09-brand/9 px-2.5 py-2.5 text-[13.5px] font-semibold text-tpop09-brand"><span aria-hidden="true" class="size-2 flex-none rounded-full bg-tpop09-ok"></span><span class="min-w-0 flex-auto truncate">Production · eu-west-1</span><svg class="flex-none" viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" aria-label="current"><path d="M3 8.5l3.2 3.2L13 4.8"/></svg></p>
    <p class="flex min-w-0 items-center gap-2.5 rounded-md px-2.5 py-2.5 text-[13.5px]"><span aria-hidden="true" class="size-2 flex-none rounded-full bg-tpop09-ok"></span><span class="min-w-0 flex-auto truncate">Staging · eu-west-1</span></p>
    <p class="flex min-w-0 items-center gap-2.5 rounded-md px-2.5 py-2.5 text-[13.5px]"><span aria-hidden="true" class="size-2 flex-none rounded-full bg-tpop09-warn"></span><span class="min-w-0 flex-auto truncate">Preview · ephemeral per branch</span><span class="flex-none text-[11px] text-tpop09-mut">degraded</span></p>
    <p class="flex min-w-0 items-center gap-2.5 rounded-md px-2.5 py-2.5 text-[13.5px]"><span aria-hidden="true" class="size-2 flex-none rounded-full bg-tpop09-rule"></span><span class="min-w-0 flex-auto truncate">Local · docker compose</span><span class="flex-none text-[11px] text-tpop09-mut">offline</span></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop09-bg: #f2f5f9;
  --color-tpop09-bg: oklch(0.97 0.006 250);
  --color-tpop09-surface: #ffffff;
  --color-tpop09-surface: oklch(1 0 0);
  --color-tpop09-ink: #111b2b;
  --color-tpop09-ink: oklch(0.22 0.035 260);
  --color-tpop09-mut: #515e75;
  --color-tpop09-mut: oklch(0.48 0.04 260);
  --color-tpop09-rule: #ccd5e2;
  --color-tpop09-rule: oklch(0.87 0.02 255);
  --color-tpop09-brand: #1558ad;
  --color-tpop09-brand: oklch(0.47 0.15 257);
  --color-tpop09-ok: #29ac68;
  --color-tpop09-ok: oklch(0.66 0.15 155);
  --color-tpop09-warn: #e8a127;
  --color-tpop09-warn: oklch(0.76 0.15 75);
  --font-tpop09-sans: 'Geist', system-ui, sans-serif;
  --font-tpop09-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop09-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-09 {
  width: 100%;
  min-height: 100svh;
  --color-tpop09-bg: color-mix(in oklch, oklch(0.16 0.018 258) calc(var(--tpop09-d) * 100%), oklch(0.97 0.006 250));
  --color-tpop09-surface: color-mix(in oklch, oklch(0.21 0.022 258) calc(var(--tpop09-d) * 100%), oklch(1 0 0));
  --color-tpop09-ink: color-mix(in oklch, oklch(0.95 0.01 255) calc(var(--tpop09-d) * 100%), oklch(0.22 0.035 260));
  --color-tpop09-mut: color-mix(in oklch, oklch(0.73 0.03 258) calc(var(--tpop09-d) * 100%), oklch(0.48 0.04 260));
  --color-tpop09-rule: color-mix(in oklch, oklch(0.32 0.03 258) calc(var(--tpop09-d) * 100%), oklch(0.87 0.02 255));
  --color-tpop09-brand: color-mix(in oklch, oklch(0.72 0.13 257) calc(var(--tpop09-d) * 100%), oklch(0.47 0.15 257));
  --color-tpop09-ok: color-mix(in oklch, oklch(0.74 0.15 155) calc(var(--tpop09-d) * 100%), oklch(0.66 0.15 155));
  --color-tpop09-warn: color-mix(in oklch, oklch(0.8 0.14 75) calc(var(--tpop09-d) * 100%), oklch(0.76 0.15 75));
}
```
