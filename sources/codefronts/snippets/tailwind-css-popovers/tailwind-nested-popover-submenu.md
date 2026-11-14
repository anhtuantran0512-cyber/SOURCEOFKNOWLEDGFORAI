---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-nested-popover-submenu/"
title: "Tailwind Nested Popover Submenu"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "Two auto popovers can be open at once only if the browser considers one nested in the other — by DOM containment or by the popovertarget relationship."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Nested Popover Submenu
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-nested-popover-submenu/

Two auto popovers can be open at once only if the browser considers one nested in the other — by DOM containment or by the popovertarget relationship. This menu keeps the submenu inside the menu, anchors each level to its own trigger and flips the submenu inward at the edge. The port also fixes a real bug: the original set display: grid on both panels, which overrides the UA's display: none and leaves them permanently visible — here the grid is open:grid.
## HTML
```html
<section class="tpop-10 group/root w-full min-h-svh bg-tpop10-bg px-4.5 py-10 font-tpop10-sans text-tpop10-ink" aria-label="Nested popover submenu demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[30rem] rounded-xl border border-tpop10-rule bg-tpop10-s1 p-4 shadow-[0_30px_60px_-36px_oklch(0_0_0/0.8)]">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <div class="min-w-0">
          <p class="text-[11px] font-semibold uppercase tracking-[0.16em] text-tpop10-mut">Ledger</p>
          <p class="text-[17px] font-bold tracking-[-0.01em]">Q3 close</p>
        </div>
        <button id="tpop-10-trigger" type="button" popovertarget="tpop-10-menu" class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-lg bg-tpop10-amber px-3.5 text-[13.5px] font-bold text-tpop10-bg transition-colors [anchor-name:--tpop10-a] hover:bg-tpop10-amber/90 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop10-ink">
          Actions
          <svg class="transition-transform duration-200 motion-reduce:transition-none group-has-[#tpop-10-menu:popover-open]/root:rotate-180" viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>
        </button>
      </div>
      <p class="mt-3.5 text-[13.5px] leading-[1.65] text-tpop10-mut text-pretty">Nesting is DOM containment or a <code class="text-tpop10-amber">popovertarget</code> relationship. Both levels stay open only because the submenu lives inside the menu.</p>

      <div popover="auto" id="tpop-10-menu" role="menu" aria-label="Actions" class="fixed m-auto w-[min(15rem,calc(100vw-28px))] gap-px rounded-lg border border-tpop10-rule bg-tpop10-s2 p-1.5 text-tpop10-ink opacity-0 shadow-[0_24px_48px_-24px_oklch(0_0_0/0.8)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop10-a] [position-area:block-end_span-inline-start] [position-try-fallbacks:flip-block] open:grid open:opacity-100 starting:open:-translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2">
        <button type="button" role="menuitem" class="flex min-h-11 w-full min-w-0 cursor-pointer items-center justify-between gap-2.5 rounded-md px-3 text-left text-[13.5px] font-medium transition-colors hover:bg-tpop10-s3 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpop10-amber">Lock period<kbd class="text-[11px] text-tpop10-mut">⌘L</kbd></button>
        <button type="button" role="menuitem" class="flex min-h-11 w-full min-w-0 cursor-pointer items-center justify-between gap-2.5 rounded-md px-3 text-left text-[13.5px] font-medium transition-colors hover:bg-tpop10-s3 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpop10-amber">Recalculate accruals</button>
        <button type="button" role="menuitem" aria-haspopup="menu" popovertarget="tpop-10-sub" class="flex min-h-11 w-full min-w-0 cursor-pointer items-center justify-between gap-2.5 rounded-md px-3 text-left text-[13.5px] font-medium text-tpop10-amber transition-colors [anchor-name:--tpop10-sub] hover:bg-tpop10-s3 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpop10-amber group-has-[#tpop-10-sub:popover-open]/root:bg-tpop10-s3">
          Export
          <svg viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 4l4 4-4 4"/></svg>
        </button>
        <span role="separator" class="mx-1 my-1 h-px bg-tpop10-rule"></span>
        <button type="button" role="menuitem" class="flex min-h-11 w-full min-w-0 cursor-pointer items-center justify-between gap-2.5 rounded-md px-3 text-left text-[13.5px] font-medium transition-colors hover:bg-tpop10-s3 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpop10-amber">Invite auditor</button>

        <div popover="auto" id="tpop-10-sub" role="menu" aria-label="Export format" class="fixed m-auto w-[min(15rem,calc(100vw-28px))] gap-px rounded-lg border border-tpop10-rule bg-tpop10-s3 p-1.5 text-tpop10-ink opacity-0 shadow-[0_24px_48px_-24px_oklch(0_0_0/0.8)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop10-sub] [position-area:inline-end_span-block-end] [position-try-fallbacks:flip-inline,flip-block] open:grid open:opacity-100 starting:open:-translate-x-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:-mt-1.5 supports-[anchor-name:--a]:ml-2">
          <button type="button" role="menuitem" class="grid min-h-11 w-full min-w-0 cursor-pointer content-center rounded-md px-3 py-1.5 text-left transition-colors hover:bg-tpop10-rule focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpop10-amber"><span class="text-[13.5px] font-semibold">CSV</span><span class="text-[11.5px] text-tpop10-mut">One row per entry</span></button>
          <button type="button" role="menuitem" class="grid min-h-11 w-full min-w-0 cursor-pointer content-center rounded-md px-3 py-1.5 text-left transition-colors hover:bg-tpop10-rule focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpop10-amber"><span class="text-[13.5px] font-semibold">XLSX</span><span class="text-[11.5px] text-tpop10-mut">Grouped by account</span></button>
          <button type="button" role="menuitem" class="grid min-h-11 w-full min-w-0 cursor-pointer content-center rounded-md px-3 py-1.5 text-left transition-colors hover:bg-tpop10-rule focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpop10-amber"><span class="text-[13.5px] font-semibold">PDF</span><span class="text-[11.5px] text-tpop10-mut">Signed statement</span></button>
          <p class="mx-1.5 mt-1.5 mb-0.5 text-[11.5px] leading-normal text-tpop10-mut">Both levels open. <kbd class="rounded border border-tpop10-rule px-1 text-tpop10-ink">Esc</kbd> closes this one first.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop10-bg: #191512;
  --color-tpop10-bg: oklch(0.2 0.008 60);
  --color-tpop10-s1: #231e1b;
  --color-tpop10-s1: oklch(0.24 0.01 60);
  --color-tpop10-s2: #2d2823;
  --color-tpop10-s2: oklch(0.28 0.012 60);
  --color-tpop10-s3: #38312c;
  --color-tpop10-s3: oklch(0.32 0.014 60);
  --color-tpop10-ink: #f3eee6;
  --color-tpop10-ink: oklch(0.95 0.012 80);
  --color-tpop10-mut: #bcafa0;
  --color-tpop10-mut: oklch(0.76 0.025 70);
  --color-tpop10-rule: #463e37;
  --color-tpop10-rule: oklch(0.37 0.016 60);
  --color-tpop10-amber: #eba440;
  --color-tpop10-amber: oklch(0.77 0.14 72);
  --font-tpop10-sans: 'Bricolage Grotesque', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpop-10 {
  width: 100%;
  min-height: 100svh;
}
```
