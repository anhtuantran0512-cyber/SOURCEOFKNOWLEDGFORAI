---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-pagination-with-first-last-previous-and-next-icons/"
title: "Tailwind Pagination with First, Last, Previous and Next Icons"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "The full four-control bracket &mdash; first, previous, next, last &mdash; around a page row, framed as a floating toolbar under real search results."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pagination with First, Last, Previous and Next Icons
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-pagination-with-first-last-previous-and-next-icons/

The full four-control bracket &mdash; first, previous, next, last &mdash; around a page row, framed as a floating toolbar under real search results. Every icon-only link carries a destination-aware name (&ldquo;Last page, page 18&rdquo;) and a CSS-only tooltip that appears on hover and keyboard focus via group-hover/t: and group-focus-visible/t:; boundaries use aria-disabled on href-less links.
## HTML
```html
<section class="tpg-04 w-full min-h-svh grid place-items-center bg-tpg04-bg bg-[radial-gradient(75%_60%_at_50%_0%,var(--color-tpg04-glow),transparent_72%)] px-5 py-14 font-tpg04-sans text-tpg04-ink antialiased" aria-label="Tailwind pagination with first, last, previous and next icons demo">
  <div class="grid w-full max-w-[42rem] grid-cols-[minmax(0,1fr)] justify-items-center gap-6">
    <article class="w-full rounded-2xl bg-tpg04-card shadow-tpg04-card ring-1 ring-tpg04-line">
      <header class="border-b border-tpg04-line px-5 pt-5 pb-4 sm:px-6">
        <p class="flex items-center gap-1.5 text-[11.5px] font-semibold tracking-[0.12em] text-tpg04-acc-ink uppercase"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m13.2 13.2 3.3 3.3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>Docs search</p>
        <h2 class="mt-1.5 text-[clamp(19px,2.6vw,22px)] font-bold tracking-[-0.02em] text-balance">Results for “container queries”</h2>
        <p class="mt-1 text-[13px] text-tpg04-mut tabular-nums">Showing <b class="font-semibold text-tpg04-ink">1–20</b> of <b class="font-semibold text-tpg04-ink">356</b> results · page 1 of 18</p>
      </header>
      <ul class="divide-y divide-tpg04-line">
        <li class="group/r relative px-5 py-4.5 transition-colors duration-200 hover:bg-tpg04-sub/60 sm:px-6">
          <p class="flex items-center gap-2 text-[12.5px] text-tpg04-mut"><span aria-hidden="true" class="grid size-5 place-items-center rounded-full bg-linear-to-br from-tpg04-acc/15 to-tpg04-acc2/15 text-[10px] font-bold text-tpg04-acc-ink ring-1 ring-tpg04-acc2/25">D</span><span class="min-w-0 truncate"><span class="text-tpg04-ink">docs.northwind.dev</span> › css › layout › container-queries</span></p>
          <h3 class="mt-1.5 text-[16.5px] leading-snug font-semibold tracking-[-0.015em] text-tpg04-acc-ink"><a href="#tpg-04-r" class="rounded-sm after:absolute after:inset-0 group-hover/r:underline group-hover/r:underline-offset-3 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring">Container queries: a quick-start guide</a></h3>
          <p class="mt-1 text-[14px] leading-relaxed text-tpg04-mut text-pretty [&_b]:font-semibold [&_b]:text-tpg04-ink">Size a component by its parent, not the viewport. Covers <b>container-type</b>, named containers and the new query units with copy-paste examples.</p>
        </li>
        <li class="group/r relative px-5 py-4.5 transition-colors duration-200 hover:bg-tpg04-sub/60 sm:px-6">
          <p class="flex items-center gap-2 text-[12.5px] text-tpg04-mut"><span aria-hidden="true" class="grid size-5 place-items-center rounded-full bg-linear-to-br from-tpg04-acc/15 to-tpg04-acc2/15 text-[10px] font-bold text-tpg04-acc-ink ring-1 ring-tpg04-acc2/25">B</span><span class="min-w-0 truncate"><span class="text-tpg04-ink">blog.fieldnotes.io</span> › 2026 › 09 › container-queries-pitfalls</span></p>
          <h3 class="mt-1.5 text-[16.5px] leading-snug font-semibold tracking-[-0.015em] text-tpg04-acc-ink"><a href="#tpg-04-r" class="rounded-sm after:absolute after:inset-0 group-hover/r:underline group-hover/r:underline-offset-3 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring">Why your container query collapses to zero width</a></h3>
          <p class="mt-1 text-[14px] leading-relaxed text-tpg04-mut text-pretty [&_b]:font-semibold [&_b]:text-tpg04-ink">An inline-size container cannot be sized by its own contents. Here is the one-line fix and three layouts where it bites.</p>
        </li>
        <li class="group/r relative px-5 py-4.5 transition-colors duration-200 hover:bg-tpg04-sub/60 sm:px-6">
          <p class="flex items-center gap-2 text-[12.5px] text-tpg04-mut"><span aria-hidden="true" class="grid size-5 place-items-center rounded-full bg-linear-to-br from-tpg04-acc/15 to-tpg04-acc2/15 text-[10px] font-bold text-tpg04-acc-ink ring-1 ring-tpg04-acc2/25">P</span><span class="min-w-0 truncate"><span class="text-tpg04-ink">patterns.harbor.design</span> › components › card</span></p>
          <h3 class="mt-1.5 text-[16.5px] leading-snug font-semibold tracking-[-0.015em] text-tpg04-acc-ink"><a href="#tpg-04-r" class="rounded-sm after:absolute after:inset-0 group-hover/r:underline group-hover/r:underline-offset-3 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring">Responsive cards without media queries</a></h3>
          <p class="mt-1 text-[14px] leading-relaxed text-tpg04-mut text-pretty [&_b]:font-semibold [&_b]:text-tpg04-ink">A card that re-stacks itself in a sidebar, a modal and a three-up grid, using <b>@container</b> and a 26rem breakpoint.</p>
        </li>
      </ul>
      <div class="flex justify-center border-t border-tpg04-line px-3 pt-4 pb-5">
        <nav aria-label="Pagination" class="rounded-2xl bg-tpg04-card p-1 shadow-tpg04-bar ring-1 ring-tpg04-line">
          <ol class="flex items-center gap-0.5">
            <li><a role="link" aria-disabled="true" aria-label="First page" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring group/t relative text-tpg04-mut hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 aria-disabled:cursor-not-allowed aria-disabled:text-tpg04-mut/45 aria-disabled:hover:translate-y-0 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg04-mut/45 aria-disabled:active:scale-100"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false"><path d="M15 4.5 9.5 10l5.5 5.5M5 4.5v11" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span aria-hidden="true" class="pointer-events-none absolute bottom-[calc(100%+10px)] z-10 translate-y-1 rounded-lg bg-tpg04-tip px-2.5 py-1.5 text-[11.5px] font-medium whitespace-nowrap text-white ring-1 ring-white/10 opacity-0 shadow-tpg04-tip transition-[opacity,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] group-hover/t:translate-y-0 group-hover/t:opacity-100 group-focus-visible/t:translate-y-0 group-focus-visible/t:opacity-100 motion-reduce:transition-none after:absolute after:top-full after:-ml-1 after:border-4 after:border-transparent after:border-t-tpg04-tip left-0 after:left-[22px]">Already on page 1</span></a></li>
            <li><a role="link" aria-disabled="true" aria-label="Previous page" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring group/t relative text-tpg04-mut hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 aria-disabled:cursor-not-allowed aria-disabled:text-tpg04-mut/45 aria-disabled:hover:translate-y-0 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg04-mut/45 aria-disabled:active:scale-100"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span aria-hidden="true" class="pointer-events-none absolute bottom-[calc(100%+10px)] z-10 translate-y-1 rounded-lg bg-tpg04-tip px-2.5 py-1.5 text-[11.5px] font-medium whitespace-nowrap text-white ring-1 ring-white/10 opacity-0 shadow-tpg04-tip transition-[opacity,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] group-hover/t:translate-y-0 group-hover/t:opacity-100 group-focus-visible/t:translate-y-0 group-focus-visible/t:opacity-100 motion-reduce:transition-none after:absolute after:top-full after:-ml-1 after:border-4 after:border-transparent after:border-t-tpg04-tip left-1/2 -translate-x-1/2 after:left-1/2">No previous page</span></a></li>
            <li aria-hidden="true" class="mx-1 h-6 w-px bg-linear-to-b from-transparent via-tpg04-acc2/40 to-transparent max-sm:mx-0.5"></li>
          <li><a href="#tpg-04-page-1" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring px-2 relative text-tpg04-ink hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 after:pointer-events-none after:absolute after:-bottom-[3px] after:left-1/2 after:size-1 after:-translate-x-1/2 after:rounded-full after:bg-tpg04-hi after:opacity-0 after:shadow-[0_0_8px_2px] after:shadow-tpg04-hi/70 after:transition-opacity aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg04-acc aria-[current=page]:via-[oklch(0.5_0.134_242.7)] aria-[current=page]:to-tpg04-acc2 aria-[current=page]:text-white aria-[current=page]:shadow-tpg04-pill aria-[current=page]:hover:text-white aria-[current=page]:after:opacity-100" aria-current="page">1</a></li>
          <li><a href="#tpg-04-page-2" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring px-2 relative text-tpg04-ink hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 after:pointer-events-none after:absolute after:-bottom-[3px] after:left-1/2 after:size-1 after:-translate-x-1/2 after:rounded-full after:bg-tpg04-hi after:opacity-0 after:shadow-[0_0_8px_2px] after:shadow-tpg04-hi/70 after:transition-opacity aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg04-acc aria-[current=page]:via-[oklch(0.5_0.134_242.7)] aria-[current=page]:to-tpg04-acc2 aria-[current=page]:text-white aria-[current=page]:shadow-tpg04-pill aria-[current=page]:hover:text-white aria-[current=page]:after:opacity-100">2</a></li>
          <li><a href="#tpg-04-page-3" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring px-2 relative text-tpg04-ink hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 after:pointer-events-none after:absolute after:-bottom-[3px] after:left-1/2 after:size-1 after:-translate-x-1/2 after:rounded-full after:bg-tpg04-hi after:opacity-0 after:shadow-[0_0_8px_2px] after:shadow-tpg04-hi/70 after:transition-opacity aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg04-acc aria-[current=page]:via-[oklch(0.5_0.134_242.7)] aria-[current=page]:to-tpg04-acc2 aria-[current=page]:text-white aria-[current=page]:shadow-tpg04-pill aria-[current=page]:hover:text-white aria-[current=page]:after:opacity-100">3</a></li>
          <li class="max-sm:hidden"><a href="#tpg-04-page-4" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring px-2 relative text-tpg04-ink hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 after:pointer-events-none after:absolute after:-bottom-[3px] after:left-1/2 after:size-1 after:-translate-x-1/2 after:rounded-full after:bg-tpg04-hi after:opacity-0 after:shadow-[0_0_8px_2px] after:shadow-tpg04-hi/70 after:transition-opacity aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg04-acc aria-[current=page]:via-[oklch(0.5_0.134_242.7)] aria-[current=page]:to-tpg04-acc2 aria-[current=page]:text-white aria-[current=page]:shadow-tpg04-pill aria-[current=page]:hover:text-white aria-[current=page]:after:opacity-100">4</a></li>
          <li class="max-sm:hidden"><a href="#tpg-04-page-5" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring px-2 relative text-tpg04-ink hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 after:pointer-events-none after:absolute after:-bottom-[3px] after:left-1/2 after:size-1 after:-translate-x-1/2 after:rounded-full after:bg-tpg04-hi after:opacity-0 after:shadow-[0_0_8px_2px] after:shadow-tpg04-hi/70 after:transition-opacity aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg04-acc aria-[current=page]:via-[oklch(0.5_0.134_242.7)] aria-[current=page]:to-tpg04-acc2 aria-[current=page]:text-white aria-[current=page]:shadow-tpg04-pill aria-[current=page]:hover:text-white aria-[current=page]:after:opacity-100">5</a></li>
            <li aria-hidden="true" class="mx-1 h-6 w-px bg-linear-to-b from-transparent via-tpg04-acc2/40 to-transparent max-sm:mx-0.5"></li>
            <li><a href="#tpg-04-page-2" aria-label="Next page, page 2" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring group/t relative text-tpg04-mut hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 aria-disabled:cursor-not-allowed aria-disabled:text-tpg04-mut/45 aria-disabled:hover:translate-y-0 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg04-mut/45 aria-disabled:active:scale-100"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span aria-hidden="true" class="pointer-events-none absolute bottom-[calc(100%+10px)] z-10 translate-y-1 rounded-lg bg-tpg04-tip px-2.5 py-1.5 text-[11.5px] font-medium whitespace-nowrap text-white ring-1 ring-white/10 opacity-0 shadow-tpg04-tip transition-[opacity,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] group-hover/t:translate-y-0 group-hover/t:opacity-100 group-focus-visible/t:translate-y-0 group-focus-visible/t:opacity-100 motion-reduce:transition-none after:absolute after:top-full after:-ml-1 after:border-4 after:border-transparent after:border-t-tpg04-tip left-1/2 -translate-x-1/2 after:left-1/2">Next page · 2</span></a></li>
            <li><a href="#tpg-04-page-18" aria-label="Last page, page 18" class="grid min-h-11 min-w-11 place-items-center rounded-xl text-[14.5px] font-semibold tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg04-ring group/t relative text-tpg04-mut hover:-translate-y-0.5 hover:bg-tpg04-acc2/10 hover:text-tpg04-acc-ink active:translate-y-0 active:scale-95 motion-reduce:hover:translate-y-0 aria-disabled:cursor-not-allowed aria-disabled:text-tpg04-mut/45 aria-disabled:hover:translate-y-0 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg04-mut/45 aria-disabled:active:scale-100"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 4.5 10.5 10 5 15.5M15 4.5v11" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span aria-hidden="true" class="pointer-events-none absolute bottom-[calc(100%+10px)] z-10 translate-y-1 rounded-lg bg-tpg04-tip px-2.5 py-1.5 text-[11.5px] font-medium whitespace-nowrap text-white ring-1 ring-white/10 opacity-0 shadow-tpg04-tip transition-[opacity,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] group-hover/t:translate-y-0 group-hover/t:opacity-100 group-focus-visible/t:translate-y-0 group-focus-visible/t:opacity-100 motion-reduce:transition-none after:absolute after:top-full after:-ml-1 after:border-4 after:border-transparent after:border-t-tpg04-tip right-0 after:right-[18px]">Last page · 18</span></a></li>
          </ol>
        </nav>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full bg-tpg04-card px-3.5 py-2 text-center font-tpg04-mono text-[11.5px] text-tpg04-mut ring-1 ring-tpg04-line">aria-disabled: · group-focus-visible/t: · aria-current</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg04-bg: #e9f6fe;
  --color-tpg04-bg: oklch(0.966 0.018 235);
  --color-tpg04-glow: #a8e1fdb3;
  --color-tpg04-glow: oklch(0.88 0.07 230 / 0.7);
  --color-tpg04-card: #fafeff;
  --color-tpg04-card: oklch(0.995 0.005 235);
  --color-tpg04-sub: #e2f3fd;
  --color-tpg04-sub: oklch(0.955 0.022 232);
  --color-tpg04-ink: #0a2036;
  --color-tpg04-ink: oklch(0.24 0.05 250);
  --color-tpg04-mut: #435e75;
  --color-tpg04-mut: oklch(0.47 0.05 245);
  --color-tpg04-line: #cce2ef;
  --color-tpg04-line: oklch(0.9 0.03 235);
  --color-tpg04-acc: #1d5ab0;
  --color-tpg04-acc: oklch(0.48 0.15 258);
  --color-tpg04-acc2: #007994;
  --color-tpg04-acc2: oklch(0.53 0.105 218);
  --color-tpg04-acc-ink: #005c9b;
  --color-tpg04-acc-ink: oklch(0.46 0.13 245);
  --color-tpg04-hi: #00cdef;
  --color-tpg04-hi: oklch(0.78 0.14 215);
  --color-tpg04-tip: #172a5a;
  --color-tpg04-tip: oklch(0.3 0.09 265);
  --color-tpg04-ring: #007ac5;
  --color-tpg04-ring: oklch(0.56 0.15 245);
  --font-tpg04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tpg04-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tpg04-card: 0 1px 2px oklch(0.3 0.08 250 / 0.06), 0 26px 56px -24px oklch(0.45 0.14 245 / 0.3);
  --shadow-tpg04-bar: 0 1px 2px oklch(0.3 0.08 250 / 0.07), 0 10px 24px -10px oklch(0.45 0.14 240 / 0.3);
  --shadow-tpg04-pill: 0 8px 22px -6px oklch(0.55 0.14 230 / 0.6), 0 1px 2px oklch(0.3 0.1 250 / 0.3), inset 0 1px 0 oklch(1 0 0 / 0.3);
  --shadow-tpg04-tip: 0 8px 20px -6px oklch(0.25 0.1 262 / 0.45);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-04 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tpg-04:not([data-theme="light"]) {
    --color-tpg04-bg: #040e21;
    --color-tpg04-bg: oklch(0.165 0.045 260);
    --color-tpg04-glow: #0035628c;
    --color-tpg04-glow: oklch(0.32 0.1 245 / 0.55);
    --color-tpg04-card: #08172e;
    --color-tpg04-card: oklch(0.205 0.05 258);
    --color-tpg04-sub: #0b223e;
    --color-tpg04-sub: oklch(0.25 0.06 255);
    --color-tpg04-ink: #e9f4fb;
    --color-tpg04-ink: oklch(0.96 0.015 235);
    --color-tpg04-mut: #98b9d1;
    --color-tpg04-mut: oklch(0.77 0.05 240);
    --color-tpg04-line: #1a3658;
    --color-tpg04-line: oklch(0.33 0.07 255);
    --color-tpg04-acc: #1d5ab0;
    --color-tpg04-acc: oklch(0.48 0.15 258);
    --color-tpg04-acc2: #007994;
    --color-tpg04-acc2: oklch(0.53 0.105 218);
    --color-tpg04-acc-ink: #7ad5f8;
    --color-tpg04-acc-ink: oklch(0.83 0.1 225);
    --color-tpg04-hi: #34e9ff;
    --color-tpg04-hi: oklch(0.86 0.14 210);
    --color-tpg04-tip: #203f7c;
    --color-tpg04-tip: oklch(0.38 0.11 262);
    --color-tpg04-ring: #52cff3;
    --color-tpg04-ring: oklch(0.8 0.12 220);
  }
}

.tpg-04[data-theme="dark"] {
  --color-tpg04-bg: #040e21;
  --color-tpg04-bg: oklch(0.165 0.045 260);
  --color-tpg04-glow: #0035628c;
  --color-tpg04-glow: oklch(0.32 0.1 245 / 0.55);
  --color-tpg04-card: #08172e;
  --color-tpg04-card: oklch(0.205 0.05 258);
  --color-tpg04-sub: #0b223e;
  --color-tpg04-sub: oklch(0.25 0.06 255);
  --color-tpg04-ink: #e9f4fb;
  --color-tpg04-ink: oklch(0.96 0.015 235);
  --color-tpg04-mut: #98b9d1;
  --color-tpg04-mut: oklch(0.77 0.05 240);
  --color-tpg04-line: #1a3658;
  --color-tpg04-line: oklch(0.33 0.07 255);
  --color-tpg04-acc: #1d5ab0;
  --color-tpg04-acc: oklch(0.48 0.15 258);
  --color-tpg04-acc2: #007994;
  --color-tpg04-acc2: oklch(0.53 0.105 218);
  --color-tpg04-acc-ink: #7ad5f8;
  --color-tpg04-acc-ink: oklch(0.83 0.1 225);
  --color-tpg04-hi: #34e9ff;
  --color-tpg04-hi: oklch(0.86 0.14 210);
  --color-tpg04-tip: #203f7c;
  --color-tpg04-tip: oklch(0.38 0.11 262);
  --color-tpg04-ring: #52cff3;
  --color-tpg04-ring: oklch(0.8 0.12 220);
}
```
