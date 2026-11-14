---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/pure-tailwind-css-pagination-without-javascript-target/"
title: "Pure Tailwind CSS Pagination Without JavaScript (:target)"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "A changelog that pages with zero JavaScript: each page is a <section id>, each number an ordinary fragment link, and v4's target:block variant swaps the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind CSS Pagination Without JavaScript (:target)
Source: https://codefronts.com/navigation/tailwind-css-pagination/pure-tailwind-css-pagination-without-javascript-target/

A changelog that pages with zero JavaScript: each page is a <section id>, each number an ordinary fragment link, and v4's target:block variant swaps the visible page. A single arbitrary variant, [.tpg-01:not(:has(:target))_&]:block, shows page one on first load — and because every page carries its own pagination bar, aria-current="page" is finally real, not just painted.
## HTML
```html
<section class="tpg-01 w-full min-h-svh grid place-items-center bg-tpg01-bg bg-[radial-gradient(70%_55%_at_50%_0%,var(--color-tpg01-glow),transparent_72%)] px-5 py-14 font-tpg01-sans text-tpg01-ink antialiased" aria-label="Pure Tailwind CSS pagination without JavaScript demo">
  <div class="grid w-full max-w-[42rem] justify-items-center gap-6">
    <article class="w-full overflow-hidden rounded-2xl bg-tpg01-card shadow-tpg01-card ring-1 ring-tpg01-line">
      <header class="flex flex-wrap items-end justify-between gap-x-6 gap-y-3 border-b border-tpg01-line px-5 pt-6 pb-5 sm:px-6">
        <div>
          <p class="text-[11.5px] font-semibold tracking-[0.14em] text-tpg01-mut uppercase">Changelog</p>
          <h2 class="mt-1.5 font-tpg01-serif text-[clamp(28px,4.4vw,36px)] leading-[1.05] tracking-[-0.01em] text-balance">Every release, <em class="bg-linear-to-r from-tpg01-hl to-tpg01-hl2 bg-clip-text pe-1 text-transparent">three at a time</em></h2>
        </div>
        <p class="inline-flex items-center gap-2 rounded-full bg-tpg01-acc/8 px-3 py-1.5 font-tpg01-mono text-[11.5px] text-tpg01-acc-ink ring-1 ring-tpg01-acc/18 ring-inset"><span aria-hidden="true" class="size-1.5 rounded-full bg-tpg01-acc2 shadow-[0_0_0_3px] shadow-tpg01-acc2/25"></span>0 KB JavaScript</p>
      </header>
      <section id="tpg-01-p1" aria-label="Page 1 of 4" class="hidden scroll-mt-16 target:block target:animate-tpg01-in motion-reduce:target:animate-none [.tpg-01:not(:has(:target))_&]:block">
        <ol class="divide-y divide-tpg01-line" start="1">
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.12</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Container queries land in the grid system</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Alex Chen · 14 min read</p>
            </div>
            <time datetime="2026-10-09" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Oct 9</time>
          </li>
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.11</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Subgrid alignment for nested cards</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Priya Sharma · 6 min read</p>
            </div>
            <time datetime="2026-10-02" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Oct 2</time>
          </li>
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.10</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Dropping the last polyfill</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Jordan Lee · 4 min read</p>
            </div>
            <time datetime="2026-09-25" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Sep 25</time>
          </li>
        </ol>
        <nav aria-label="Pagination" class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-t border-tpg01-line bg-tpg01-acc/[0.04] px-4 py-2.5 max-sm:justify-center sm:px-5">
          <p class="text-[13px] text-tpg01-mut tabular-nums">Showing <b class="font-semibold text-tpg01-ink">1–3</b> of <b class="font-semibold text-tpg01-ink">12</b> posts</p>
          <ol class="flex items-center gap-1">
            <li><a role="link" aria-disabled="true" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none gap-1.5 px-2.5 text-tpg01-mut hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink aria-disabled:cursor-not-allowed aria-disabled:opacity-40 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg01-mut sm:px-3"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="max-sm:sr-only">Newer</span></a></li>
              <li><a href="#tpg-01-p1" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-current="page" aria-label="Page 1">1</a></li>
              <li><a href="#tpg-01-p2" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 2">2</a></li>
              <li><a href="#tpg-01-p3" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 3">3</a></li>
              <li><a href="#tpg-01-p4" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 4">4</a></li>
            <li><a href="#tpg-01-p2" aria-label="Older posts, page 2" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none gap-1.5 px-2.5 text-tpg01-mut hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink aria-disabled:cursor-not-allowed aria-disabled:opacity-40 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg01-mut sm:px-3"><span class="max-sm:sr-only">Older</span><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
          </ol>
        </nav>
      </section>
      <section id="tpg-01-p2" aria-label="Page 2 of 4" class="hidden scroll-mt-16 target:block target:animate-tpg01-in motion-reduce:target:animate-none">
        <ol class="divide-y divide-tpg01-line" start="4">
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.9</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Scroll-driven animations, no observers</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Sam Rivera · 9 min read</p>
            </div>
            <time datetime="2026-09-18" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Sep 18</time>
          </li>
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.8</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Anchor positioning for tooltips</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Alex Chen · 7 min read</p>
            </div>
            <time datetime="2026-09-11" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Sep 11</time>
          </li>
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.7</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Rewriting focus management</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Priya Sharma · 11 min read</p>
            </div>
            <time datetime="2026-09-04" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Sep 4</time>
          </li>
        </ol>
        <nav aria-label="Pagination" class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-t border-tpg01-line bg-tpg01-acc/[0.04] px-4 py-2.5 max-sm:justify-center sm:px-5">
          <p class="text-[13px] text-tpg01-mut tabular-nums">Showing <b class="font-semibold text-tpg01-ink">4–6</b> of <b class="font-semibold text-tpg01-ink">12</b> posts</p>
          <ol class="flex items-center gap-1">
            <li><a href="#tpg-01-p1" aria-label="Newer posts, page 1" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none gap-1.5 px-2.5 text-tpg01-mut hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink aria-disabled:cursor-not-allowed aria-disabled:opacity-40 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg01-mut sm:px-3"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="max-sm:sr-only">Newer</span></a></li>
              <li><a href="#tpg-01-p1" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 1">1</a></li>
              <li><a href="#tpg-01-p2" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-current="page" aria-label="Page 2">2</a></li>
              <li><a href="#tpg-01-p3" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 3">3</a></li>
              <li><a href="#tpg-01-p4" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 4">4</a></li>
            <li><a href="#tpg-01-p3" aria-label="Older posts, page 3" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none gap-1.5 px-2.5 text-tpg01-mut hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink aria-disabled:cursor-not-allowed aria-disabled:opacity-40 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg01-mut sm:px-3"><span class="max-sm:sr-only">Older</span><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
          </ol>
        </nav>
      </section>
      <section id="tpg-01-p3" aria-label="Page 3 of 4" class="hidden scroll-mt-16 target:block target:animate-tpg01-in motion-reduce:target:animate-none">
        <ol class="divide-y divide-tpg01-line" start="7">
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.6</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Why we moved to oklch</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Jordan Lee · 5 min read</p>
            </div>
            <time datetime="2026-08-28" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Aug 28</time>
          </li>
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.5</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Popover API in production</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Sam Rivera · 8 min read</p>
            </div>
            <time datetime="2026-08-21" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Aug 21</time>
          </li>
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.4</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Cutting 40kb of layout JavaScript</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Alex Chen · 12 min read</p>
            </div>
            <time datetime="2026-08-14" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Aug 14</time>
          </li>
        </ol>
        <nav aria-label="Pagination" class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-t border-tpg01-line bg-tpg01-acc/[0.04] px-4 py-2.5 max-sm:justify-center sm:px-5">
          <p class="text-[13px] text-tpg01-mut tabular-nums">Showing <b class="font-semibold text-tpg01-ink">7–9</b> of <b class="font-semibold text-tpg01-ink">12</b> posts</p>
          <ol class="flex items-center gap-1">
            <li><a href="#tpg-01-p2" aria-label="Newer posts, page 2" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none gap-1.5 px-2.5 text-tpg01-mut hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink aria-disabled:cursor-not-allowed aria-disabled:opacity-40 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg01-mut sm:px-3"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="max-sm:sr-only">Newer</span></a></li>
              <li><a href="#tpg-01-p1" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 1">1</a></li>
              <li><a href="#tpg-01-p2" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 2">2</a></li>
              <li><a href="#tpg-01-p3" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-current="page" aria-label="Page 3">3</a></li>
              <li><a href="#tpg-01-p4" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 4">4</a></li>
            <li><a href="#tpg-01-p4" aria-label="Older posts, page 4" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none gap-1.5 px-2.5 text-tpg01-mut hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink aria-disabled:cursor-not-allowed aria-disabled:opacity-40 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg01-mut sm:px-3"><span class="max-sm:sr-only">Older</span><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
          </ol>
        </nav>
      </section>
      <section id="tpg-01-p4" aria-label="Page 4 of 4" class="hidden scroll-mt-16 target:block target:animate-tpg01-in motion-reduce:target:animate-none">
        <ol class="divide-y divide-tpg01-line" start="10">
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.3</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">View transitions between routes</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Priya Sharma · 10 min read</p>
            </div>
            <time datetime="2026-08-07" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Aug 7</time>
          </li>
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.2</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">A budget for third-party scripts</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Jordan Lee · 6 min read</p>
            </div>
            <time datetime="2026-07-31" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Jul 31</time>
          </li>
          <li class="flex items-start gap-3.5 px-5 py-4 transition-colors duration-200 hover:bg-tpg01-acc/[0.04] sm:gap-4 sm:px-6">
            <span class="mt-px w-12 shrink-0 rounded-md bg-tpg01-acc/8 py-0.5 text-center font-tpg01-mono text-[11.5px] font-medium text-tpg01-acc-ink tabular-nums ring-1 ring-tpg01-acc/18 ring-inset">v4.1</span>
            <div class="min-w-0 flex-1">
              <h3 class="text-[15px] leading-snug font-medium tracking-[-0.01em] text-pretty">Testing with prefers-reduced-motion</h3>
              <p class="mt-1 text-[13px] text-tpg01-mut tabular-nums">Sam Rivera · 3 min read</p>
            </div>
            <time datetime="2026-07-24" class="mt-0.5 shrink-0 text-[12.5px] text-tpg01-mut tabular-nums max-sm:hidden">Jul 24</time>
          </li>
        </ol>
        <nav aria-label="Pagination" class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-t border-tpg01-line bg-tpg01-acc/[0.04] px-4 py-2.5 max-sm:justify-center sm:px-5">
          <p class="text-[13px] text-tpg01-mut tabular-nums">Showing <b class="font-semibold text-tpg01-ink">10–12</b> of <b class="font-semibold text-tpg01-ink">12</b> posts</p>
          <ol class="flex items-center gap-1">
            <li><a href="#tpg-01-p3" aria-label="Newer posts, page 3" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none gap-1.5 px-2.5 text-tpg01-mut hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink aria-disabled:cursor-not-allowed aria-disabled:opacity-40 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg01-mut sm:px-3"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="max-sm:sr-only">Newer</span></a></li>
              <li><a href="#tpg-01-p1" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 1">1</a></li>
              <li><a href="#tpg-01-p2" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 2">2</a></li>
              <li><a href="#tpg-01-p3" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-label="Page 3">3</a></li>
              <li><a href="#tpg-01-p4" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none px-2 text-tpg01-ink hover:-translate-y-px hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink active:translate-y-0 active:scale-95 aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg01-acc aria-[current=page]:to-tpg01-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-white aria-[current=page]:shadow-tpg01-pill aria-[current=page]:hover:text-white motion-reduce:hover:translate-y-0" aria-current="page" aria-label="Page 4">4</a></li>
            <li><a role="link" aria-disabled="true" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-[10px] text-[14px] font-medium tabular-nums transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg01-ring motion-reduce:transition-none gap-1.5 px-2.5 text-tpg01-mut hover:bg-tpg01-acc/10 hover:text-tpg01-acc-ink aria-disabled:cursor-not-allowed aria-disabled:opacity-40 aria-disabled:hover:bg-transparent aria-disabled:hover:text-tpg01-mut sm:px-3"><span class="max-sm:sr-only">Older</span><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
          </ol>
        </nav>
      </section>
    </article>
    <p class="flex items-center gap-2 text-[13px] text-tpg01-mut text-balance"><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="shrink-0"><path d="M8.5 11.5a3.5 3.5 0 0 0 5 0l2.5-2.5a3.5 3.5 0 0 0-5-5l-1 1M11.5 8.5a3.5 3.5 0 0 0-5 0L4 11a3.5 3.5 0 0 0 5 5l1-1" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>The page lives in the URL fragment: reload, share or press Back and you land on the same page.</p>
    <p aria-hidden="true" class="rounded-full bg-tpg01-card px-3.5 py-2 text-center font-tpg01-mono text-[11.5px] text-tpg01-mut ring-1 ring-tpg01-line">target:block · :has(:target) · aria-current</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg01-bg: #f2f3ff;
  --color-tpg01-bg: oklch(0.966 0.016 285);
  --color-tpg01-glow: #d2d2ffbf;
  --color-tpg01-glow: oklch(0.88 0.07 285 / 0.75);
  --color-tpg01-card: #fdfdff;
  --color-tpg01-card: oklch(0.995 0.004 285);
  --color-tpg01-ink: #1b1c36;
  --color-tpg01-ink: oklch(0.24 0.05 280);
  --color-tpg01-mut: #555877;
  --color-tpg01-mut: oklch(0.47 0.05 280);
  --color-tpg01-line: #dbdcf0;
  --color-tpg01-line: oklch(0.9 0.028 285);
  --color-tpg01-acc: #4f39f6;
  --color-tpg01-acc: oklch(0.511 0.262 277);
  --color-tpg01-acc2: #7c3aed;
  --color-tpg01-acc2: oklch(0.541 0.247 293);
  --color-tpg01-acc-ink: #4b34cd;
  --color-tpg01-acc-ink: oklch(0.46 0.22 280);
  --color-tpg01-hl: #4f39f6;
  --color-tpg01-hl: oklch(0.511 0.262 277);
  --color-tpg01-hl2: #7c3aed;
  --color-tpg01-hl2: oklch(0.541 0.247 293);
  --color-tpg01-ring: #6d49f4;
  --color-tpg01-ring: oklch(0.55 0.24 285);
  --font-tpg01-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tpg01-serif: 'Instrument Serif', Georgia, serif;
  --font-tpg01-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tpg01-card: 0 1px 2px oklch(0.3 0.12 280 / 0.06), 0 24px 56px -22px oklch(0.4 0.2 285 / 0.32);
  --shadow-tpg01-pill: 0 8px 20px -6px oklch(0.52 0.25 288 / 0.6), 0 1px 2px oklch(0.3 0.2 280 / 0.3), inset 0 1px 0 oklch(1 0 0 / 0.28);
  --animate-tpg01-in: tpg01-in 0.42s cubic-bezier(0.16, 1, 0.3, 1);

  @keyframes tpg01-in {
    from {
      opacity: 0;
      translate: 0 6px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-01 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tpg-01:not([data-theme="light"]) {
    --color-tpg01-bg: #0b0b21;
    --color-tpg01-bg: oklch(0.165 0.045 280);
    --color-tpg01-glow: #3021718c;
    --color-tpg01-glow: oklch(0.32 0.13 285 / 0.55);
    --color-tpg01-card: #13142d;
    --color-tpg01-card: oklch(0.205 0.05 280);
    --color-tpg01-ink: #f2f2fe;
    --color-tpg01-ink: oklch(0.965 0.015 285);
    --color-tpg01-mut: #b1b1d1;
    --color-tpg01-mut: oklch(0.77 0.045 285);
    --color-tpg01-line: #303058;
    --color-tpg01-line: oklch(0.33 0.07 282);
    --color-tpg01-acc: #4f39f6;
    --color-tpg01-acc: oklch(0.511 0.262 277);
    --color-tpg01-acc2: #7c3aed;
    --color-tpg01-acc2: oklch(0.541 0.247 293);
    --color-tpg01-acc-ink: #bcbaff;
    --color-tpg01-acc-ink: oklch(0.82 0.11 285);
    --color-tpg01-hl: #aab6ff;
    --color-tpg01-hl: oklch(0.8 0.12 277);
    --color-tpg01-hl2: #d1a8ff;
    --color-tpg01-hl2: oklch(0.8 0.13 305);
    --color-tpg01-ring: #a8a2ff;
    --color-tpg01-ring: oklch(0.76 0.15 285);
  }
}

.tpg-01[data-theme="dark"] {
  --color-tpg01-bg: #0b0b21;
  --color-tpg01-bg: oklch(0.165 0.045 280);
  --color-tpg01-glow: #3021718c;
  --color-tpg01-glow: oklch(0.32 0.13 285 / 0.55);
  --color-tpg01-card: #13142d;
  --color-tpg01-card: oklch(0.205 0.05 280);
  --color-tpg01-ink: #f2f2fe;
  --color-tpg01-ink: oklch(0.965 0.015 285);
  --color-tpg01-mut: #b1b1d1;
  --color-tpg01-mut: oklch(0.77 0.045 285);
  --color-tpg01-line: #303058;
  --color-tpg01-line: oklch(0.33 0.07 282);
  --color-tpg01-acc: #4f39f6;
  --color-tpg01-acc: oklch(0.511 0.262 277);
  --color-tpg01-acc2: #7c3aed;
  --color-tpg01-acc2: oklch(0.541 0.247 293);
  --color-tpg01-acc-ink: #bcbaff;
  --color-tpg01-acc-ink: oklch(0.82 0.11 285);
  --color-tpg01-hl: #aab6ff;
  --color-tpg01-hl: oklch(0.8 0.12 277);
  --color-tpg01-hl2: #d1a8ff;
  --color-tpg01-hl2: oklch(0.8 0.13 305);
  --color-tpg01-ring: #a8a2ff;
  --color-tpg01-ring: oklch(0.76 0.15 285);
}
```
