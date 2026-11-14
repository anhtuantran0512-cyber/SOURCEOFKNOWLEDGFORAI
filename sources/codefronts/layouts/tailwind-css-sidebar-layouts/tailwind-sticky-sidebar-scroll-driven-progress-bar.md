---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sticky-sidebar-scroll-driven-progress-bar/"
title: "Tailwind Sticky Sidebar Layout with Scroll-Driven Progress Bar"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The long-article companion rail: a TOC that rides along as you scroll, with the three constraints people always miss, plus a scroll-driven reading progress bar."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Sidebar Layout with Scroll-Driven Progress Bar
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sticky-sidebar-scroll-driven-progress-bar/

The long-article companion rail: a TOC that rides along as you scroll, with the three constraints people always miss, plus a scroll-driven reading progress bar. The port is a good illustration of the split &mdash; sticky is three utilities, the scroll timeline stays CSS because it has no utility form and should not.
## HTML
```html
<section class="tsl-07 w-full h-svh min-h-svh overflow-y-auto font-tsl07-sans bg-tsl07-bg text-tsl07-ink">
  <div aria-hidden="true" class="sticky top-0 z-10 h-[3px] w-0 bg-[linear-gradient(90deg,var(--color-tsl07-accent),oklch(0.65_0.15_300))] animate-tsl07-grow motion-reduce:animate-none motion-reduce:w-full motion-reduce:opacity-25"></div>
  <div class="grid grid-cols-[230px_minmax(0,1fr)] gap-10 max-w-[920px] mx-auto px-6 pt-8 pb-16">
    <aside aria-label="On this page" class="sticky top-6 self-start max-h-[calc(100svh-3rem)] overflow-y-auto border-r border-tsl07-line pr-5">
      <h2 class="mb-3 text-[11px] font-semibold uppercase tracking-[0.09em] text-tsl07-mut">On this page</h2>
      <nav class="flex flex-col gap-0.5">
        <a href="#tsl07-s1" aria-current="true" class="px-2.5 py-[7px] rounded-lg text-[13px] font-medium leading-snug no-underline text-tsl07-mut transition-colors duration-150 hover:text-tsl07-ink hover:bg-tsl07-hover aria-[current=true]:text-tsl07-accent aria-[current=true]:bg-tsl07-tint aria-[current=true]:font-semibold focus-visible:outline-2 focus-visible:outline-tsl07-accent focus-visible:outline-offset-1">Why grids beat floats</a>
        <a href="#tsl07-s2" class="px-2.5 py-[7px] rounded-lg text-[13px] font-medium leading-snug no-underline text-tsl07-mut transition-colors duration-150 hover:text-tsl07-ink hover:bg-tsl07-hover focus-visible:outline-2 focus-visible:outline-tsl07-accent focus-visible:outline-offset-1">Track sizing deep-dive</a>
        <a href="#tsl07-s3" class="px-2.5 py-[7px] rounded-lg text-[13px] font-medium leading-snug no-underline text-tsl07-mut transition-colors duration-150 hover:text-tsl07-ink hover:bg-tsl07-hover focus-visible:outline-2 focus-visible:outline-tsl07-accent focus-visible:outline-offset-1">Alignment properties</a>
        <a href="#tsl07-s4" class="px-2.5 py-[7px] rounded-lg text-[13px] font-medium leading-snug no-underline text-tsl07-mut transition-colors duration-150 hover:text-tsl07-ink hover:bg-tsl07-hover focus-visible:outline-2 focus-visible:outline-tsl07-accent focus-visible:outline-offset-1">Subgrid in practice</a>
        <a href="#tsl07-s5" class="px-2.5 py-[7px] rounded-lg text-[13px] font-medium leading-snug no-underline text-tsl07-mut transition-colors duration-150 hover:text-tsl07-ink hover:bg-tsl07-hover focus-visible:outline-2 focus-visible:outline-tsl07-accent focus-visible:outline-offset-1">Container queries</a>
      </nav>
    </aside>
    <article>
      <h1 id="tsl07-s1" class="scroll-mt-5 text-[26px] font-bold leading-tight tracking-tight mb-3.5">Modern CSS layout, properly</h1>
      <p class="max-w-[62ch] text-[14.5px] leading-[1.75] text-tsl07-body text-pretty">Scroll this page &mdash; the rail sticks 24px from the top while the article flows past. The bar up top is a scroll-driven animation, no JS.</p>
      <h2 id="tsl07-s2" class="scroll-mt-5 mt-[30px] mb-2.5 text-lg font-bold leading-snug">Track sizing deep-dive</h2>
      <p class="max-w-[62ch] text-[14.5px] leading-[1.75] text-tsl07-body text-pretty">Fixed, fractional, minmax and fit-content tracks each answer a different layout question. Fractional units distribute leftover space, not total space &mdash; the distinction that explains most grid surprises.</p>
      <h2 id="tsl07-s3" class="scroll-mt-5 mt-[30px] mb-2.5 text-lg font-bold leading-snug">Alignment properties</h2>
      <p class="max-w-[62ch] text-[14.5px] leading-[1.75] text-tsl07-body text-pretty">justify- controls the inline axis, align- the block axis. The -content properties move tracks; -items move children within their cells; -self overrides per child.</p>
      <h2 id="tsl07-s4" class="scroll-mt-5 mt-[30px] mb-2.5 text-lg font-bold leading-snug">Subgrid in practice</h2>
      <p class="max-w-[62ch] text-[14.5px] leading-[1.75] text-tsl07-body text-pretty">Subgrid lets nested elements adopt parent rails &mdash; card grids with aligned footers, forms with aligned labels, sidebars with aligned badges (see demo 05).</p>
      <h2 id="tsl07-s5" class="scroll-mt-5 mt-[30px] mb-2.5 text-lg font-bold leading-snug">Container queries</h2>
      <p class="max-w-[62ch] text-[14.5px] leading-[1.75] text-tsl07-body text-pretty">Components respond to their container, not the viewport. Demo 29 rebuilds this sidebar pattern on container queries.</p>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl07-bg: #fcfcfd;
  --color-tsl07-bg: oklch(0.99 0.002 250);
  --color-tsl07-ink: #3b4049;
  --color-tsl07-ink: oklch(0.27 0.015 250);
  --color-tsl07-body: #565c66;
  --color-tsl07-body: oklch(0.38 0.012 250);
  --color-tsl07-mut: #767b85;
  --color-tsl07-mut: oklch(0.52 0.012 250);
  --color-tsl07-line: #e3e4e9;
  --color-tsl07-line: oklch(0.9 0.007 250);
  --color-tsl07-accent: #4360cb;
  --color-tsl07-accent: oklch(0.55 0.16 250);
  --color-tsl07-hover: rgb(59 64 73 / 0.05);
  --color-tsl07-hover: color-mix(in oklab, oklch(0.27 0.015 250) 5%, transparent);
  --color-tsl07-tint: rgb(67 96 203 / 0.09);
  --color-tsl07-tint: color-mix(in oklab, oklch(0.55 0.16 250) 9%, transparent);
  --font-tsl07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-tsl07-grow: tsl07-grow linear;
}

@keyframes tsl07-grow {
  from {
    width: 0;
  }

  to {
    width: 100%;
  }
}

.tsl-07 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: light;
}
/* No utility names a scroll timeline, and none should — this is plumbing,
   not a design-scale value. The bar's animation itself IS a utility. */

.tsl-07 {
  scroll-timeline: --tsl07-scroll block;
}

.tsl-07 > [aria-hidden="true"]:first-child {
  animation-timeline: --tsl07-scroll;
}
```
