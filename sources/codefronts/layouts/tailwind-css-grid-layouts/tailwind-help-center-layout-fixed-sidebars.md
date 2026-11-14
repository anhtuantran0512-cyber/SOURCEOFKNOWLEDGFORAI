---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-help-center-layout-fixed-sidebars/"
title: "Tailwind Help Center Layout with Fixed Sidebars"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A support knowledge-base article: fixed 170px category rail, the answer in the middle, a related-articles rail, and hairline rules that come from the grid's…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Help Center Layout with Fixed Sidebars
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-help-center-layout-fixed-sidebars/

A support knowledge-base article: fixed 170px category rail, the answer in the middle, a related-articles rail, and hairline rules that come from the grid's own gaps rather than five border declarations.
## HTML
```html
<section class="tgx-07 w-full min-h-svh bg-tgx07-bg font-tgx07-sans p-6">
  <div class="grid gap-px min-h-[400px] bg-tgx07-shell border border-tgx07-shell rounded-xl overflow-hidden [grid-template-areas:'masthead_masthead_masthead'_'menu_content_extras'_'colophon_colophon_colophon'] grid-cols-[170px_minmax(0,1fr)_170px] grid-rows-[auto_1fr_auto] max-sm:[grid-template-areas:'masthead'_'menu'_'content'_'extras'_'colophon'] max-sm:grid-cols-1 max-sm:grid-rows-none">
    <header class="[grid-area:masthead] bg-tgx07-panel px-4 py-3.5 flex items-center justify-between gap-4 flex-wrap">
      <div class="flex items-baseline gap-3">
        <strong class="text-[0.95rem] font-semibold text-tgx07-ink">Northwind Help</strong>
        <span class="font-tgx07-mono text-[0.6rem] text-tgx07-teal bg-tgx07-tealtint border border-tgx07-teal/35 rounded px-1.5 py-0.5">masthead</span>
      </div>
      <span class="text-[0.75rem] text-tgx07-mut bg-tgx07-bg border border-tgx07-line rounded-lg px-3 py-1.5">⌕ Search 412 articles</span>
    </header>
    <nav aria-label="Categories" class="[grid-area:menu] bg-tgx07-panel p-3 flex flex-col gap-1">
      <span class="w-fit font-tgx07-mono text-[0.6rem] text-tgx07-teal bg-tgx07-tealtint border border-tgx07-teal/35 rounded px-1.5 py-0.5 mb-1">menu · 170px</span>
      <a href="#0" aria-current="page" class="text-[0.82rem] no-underline min-h-11 flex items-center px-2 rounded-lg [overflow-wrap:anywhere] text-tgx07-mut transition-colors hover:text-tgx07-ink hover:bg-tgx07-hover aria-[current=page]:text-tgx07-teal aria-[current=page]:bg-tgx07-tealtint aria-[current=page]:font-semibold focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2">Shipping labels</a>
      <a href="#0" class="text-[0.82rem] no-underline min-h-11 flex items-center px-2 rounded-lg [overflow-wrap:anywhere] text-tgx07-mut transition-colors hover:text-tgx07-ink hover:bg-tgx07-hover focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2">Customs paperwork</a>
      <a href="#0" class="text-[0.82rem] no-underline min-h-11 flex items-center px-2 rounded-lg [overflow-wrap:anywhere] text-tgx07-mut transition-colors hover:text-tgx07-ink hover:bg-tgx07-hover focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2">Billing</a>
      <a href="#0" class="text-[0.82rem] no-underline min-h-11 flex items-center px-2 rounded-lg [overflow-wrap:anywhere] text-tgx07-mut transition-colors hover:text-tgx07-ink hover:bg-tgx07-hover focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2">Account access</a>
    </nav>
    <main class="[grid-area:content] bg-tgx07-panel p-5 min-w-0 flex flex-col gap-3">
      <span class="w-fit font-tgx07-mono text-[0.6rem] text-tgx07-teal bg-tgx07-tealtint border border-tgx07-teal/35 rounded px-1.5 py-0.5">content · minmax(0,1fr)</span>
      <h2 class="text-[1.2rem] font-semibold text-tgx07-ink tracking-[-0.01em]">Why did my label print at the wrong size?</h2>
      <p class="text-[0.88rem] leading-[1.7] text-tgx07-mut">Nine times out of ten the printer is scaling to fit. Set the print dialog to 100% (not "shrink to page"), choose the 4×6 media size, and reprint from the PDF rather than the browser preview.</p>
      <ol class="flex flex-col gap-2 text-[0.86rem] leading-[1.6] text-tgx07-mut list-decimal list-inside marker:text-tgx07-teal marker:font-semibold">
        <li>Open the label PDF in a reader, not the browser tab.</li>
        <li>Set <strong class="text-tgx07-ink font-semibold">Scale: 100%</strong> and media <strong class="text-tgx07-ink font-semibold">4in × 6in</strong>.</li>
        <li>Print one test label and measure the barcode — it must be at least 32mm wide.</li>
      </ol>
      <div class="mt-auto pt-3 flex items-center gap-3 flex-wrap">
        <span class="text-[0.78rem] text-tgx07-mut">Was this helpful?</span>
        <button type="button" class="text-[0.78rem] font-medium min-h-11 px-3.5 rounded-lg border border-tgx07-line text-tgx07-ink bg-tgx07-bg cursor-pointer transition-colors hover:bg-tgx07-hover focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2">Yes</button>
        <button type="button" class="text-[0.78rem] font-medium min-h-11 px-3.5 rounded-lg border border-tgx07-line text-tgx07-ink bg-tgx07-bg cursor-pointer transition-colors hover:bg-tgx07-hover focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2">No</button>
      </div>
    </main>
    <aside class="[grid-area:extras] bg-tgx07-panel p-3 flex flex-col gap-2">
      <span class="w-fit font-tgx07-mono text-[0.6rem] text-tgx07-teal bg-tgx07-tealtint border border-tgx07-teal/35 rounded px-1.5 py-0.5">extras · 170px</span>
      <p class="text-[0.7rem] uppercase tracking-[0.12em] text-tgx07-mut">Related</p>
      <a href="#0" class="text-[0.8rem] leading-[1.4] no-underline text-tgx07-ink [overflow-wrap:anywhere] hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2 rounded">Reprinting a voided label</a>
      <a href="#0" class="text-[0.8rem] leading-[1.4] no-underline text-tgx07-ink [overflow-wrap:anywhere] hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2 rounded">Thermal printer setup</a>
      <a href="#0" class="text-[0.8rem] leading-[1.4] no-underline text-tgx07-ink [overflow-wrap:anywhere] hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx07-teal focus-visible:outline-offset-2 rounded">Barcode scan failures</a>
    </aside>
    <footer class="[grid-area:colophon] bg-tgx07-band px-4 py-3 flex items-center justify-between gap-4 flex-wrap text-[0.74rem] text-tgx07-mut">
      <span>Updated 12 September 2026 · Article #4127</span>
      <span class="font-tgx07-mono">gap-px = every divider</span>
    </footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx07-bg: #eef1f1;
  --color-tgx07-bg: oklch(0.94 0.006 195);
  --color-tgx07-panel: #ffffff;
  --color-tgx07-panel: oklch(1 0 0);
  --color-tgx07-band: #f3f6f6;
  --color-tgx07-band: oklch(0.96 0.005 195);
  --color-tgx07-shell: #cbd4d5;
  --color-tgx07-shell: oklch(0.84 0.01 195);
  --color-tgx07-line: #dde3e3;
  --color-tgx07-line: oklch(0.89 0.008 195);
  --color-tgx07-hover: #eff3f3;
  --color-tgx07-hover: oklch(0.95 0.006 195);
  --color-tgx07-ink: #1d2626;
  --color-tgx07-ink: oklch(0.24 0.01 195);
  --color-tgx07-mut: #5b6767;
  --color-tgx07-mut: oklch(0.47 0.012 195);
  --color-tgx07-teal: #0f6b6b;
  --color-tgx07-teal: oklch(0.45 0.09 195);
  --color-tgx07-tealtint: #e0efee;
  --color-tgx07-tealtint: oklch(0.94 0.02 195);
  --font-tgx07-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx07-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-07 {
  width: 100%;
  min-height: 100svh;
}
```
