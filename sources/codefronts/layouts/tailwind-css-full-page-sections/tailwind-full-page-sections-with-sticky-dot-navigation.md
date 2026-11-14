---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-page-sections-with-sticky-dot-navigation/"
title: "Tailwind Full Page Sections with Sticky Dot Navigation"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "Six full-viewport panels with a frosted dot rail down the right edge."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full Page Sections with Sticky Dot Navigation
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-page-sections-with-sticky-dot-navigation/

Six full-viewport panels with a frosted dot rail down the right edge. Every dot is a real 44px anchor with a text label revealed on hover and focus, and the active dot grows and fills as its panel passes &mdash; driven by [view-timeline-name:…] plus the root's [timeline-scope:…], applied through one small @utility. Where scroll-driven animation is missing, in-[…:has(#id:target)]: keeps the active state working.
## HTML
```html
<div class="tfps-05 relative isolate w-full min-h-svh bg-tfps05-bg font-tfps05-sans text-tfps05-ink antialiased [&_code]:font-tfps05-mono [&_code]:text-[.92em] [timeline-scope:--tfps05-1,--tfps05-2,--tfps05-3,--tfps05-4,--tfps05-5,--tfps05-6]">
  <input class="peer sr-only" type="checkbox" id="tfps-05-theme">
  <label for="tfps-05-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps05-ink/10 bg-white/60 text-tfps05-ink hover:bg-white/85 tfps05-dark:bg-white/[.07] tfps05-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps05-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps05-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps05-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps05-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <nav aria-label="Section navigation" class="fixed top-1/2 right-[clamp(.35rem,1.4vw,1rem)] z-70 grid -translate-y-1/2 rounded-full border border-tfps05-ink/10 bg-white/55 py-1.5 backdrop-blur-md tfps05-dark:bg-white/[.05] forced-colors:border-[CanvasText]">
    <a href="#tfps-05-s1" class="group/link relative grid size-11 place-items-center rounded-full no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps05-acc"><span class="pointer-events-none absolute top-1/2 right-[calc(100%+.35rem)] -translate-y-1/2 translate-x-1.5 rounded-lg border border-tfps05-ink/10 bg-tfps05-panel/85 px-2 py-1 text-[.78rem] whitespace-nowrap text-tfps05-ink opacity-0 shadow-[0_8px_20px_-12px_var(--color-tfps05-shade)] backdrop-blur-sm transition-[opacity,translate] duration-200 group-hover/link:translate-x-0 group-hover/link:opacity-100 group-focus-visible/link:translate-x-0 group-focus-visible/link:opacity-100">Overview</span><span class="[--tl:--tfps05-1] tfps05-scrub size-[.62rem] rounded-full bg-tfps05-ink opacity-35 transition-[opacity,scale,background-color] duration-300 in-[.tfps-05:has(#tfps-05-s1:target)]:scale-[2.1] in-[.tfps-05:has(#tfps-05-s1:target)]:bg-tfps05-acc in-[.tfps-05:has(#tfps-05-s1:target)]:opacity-100 in-[.tfps-05:not(:has(section:target))]:scale-[2.1] in-[.tfps-05:not(:has(section:target))]:bg-tfps05-acc in-[.tfps-05:not(:has(section:target))]:opacity-100"></span></a>
    <a href="#tfps-05-s2" class="group/link relative grid size-11 place-items-center rounded-full no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps05-acc"><span class="pointer-events-none absolute top-1/2 right-[calc(100%+.35rem)] -translate-y-1/2 translate-x-1.5 rounded-lg border border-tfps05-ink/10 bg-tfps05-panel/85 px-2 py-1 text-[.78rem] whitespace-nowrap text-tfps05-ink opacity-0 shadow-[0_8px_20px_-12px_var(--color-tfps05-shade)] backdrop-blur-sm transition-[opacity,translate] duration-200 group-hover/link:translate-x-0 group-hover/link:opacity-100 group-focus-visible/link:translate-x-0 group-focus-visible/link:opacity-100">Signals</span><span class="[--tl:--tfps05-2] tfps05-scrub size-[.62rem] rounded-full bg-tfps05-ink opacity-35 transition-[opacity,scale,background-color] duration-300 in-[.tfps-05:has(#tfps-05-s2:target)]:scale-[2.1] in-[.tfps-05:has(#tfps-05-s2:target)]:bg-tfps05-acc in-[.tfps-05:has(#tfps-05-s2:target)]:opacity-100"></span></a>
    <a href="#tfps-05-s3" class="group/link relative grid size-11 place-items-center rounded-full no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps05-acc"><span class="pointer-events-none absolute top-1/2 right-[calc(100%+.35rem)] -translate-y-1/2 translate-x-1.5 rounded-lg border border-tfps05-ink/10 bg-tfps05-panel/85 px-2 py-1 text-[.78rem] whitespace-nowrap text-tfps05-ink opacity-0 shadow-[0_8px_20px_-12px_var(--color-tfps05-shade)] backdrop-blur-sm transition-[opacity,translate] duration-200 group-hover/link:translate-x-0 group-hover/link:opacity-100 group-focus-visible/link:translate-x-0 group-focus-visible/link:opacity-100">Routing</span><span class="[--tl:--tfps05-3] tfps05-scrub size-[.62rem] rounded-full bg-tfps05-ink opacity-35 transition-[opacity,scale,background-color] duration-300 in-[.tfps-05:has(#tfps-05-s3:target)]:scale-[2.1] in-[.tfps-05:has(#tfps-05-s3:target)]:bg-tfps05-acc in-[.tfps-05:has(#tfps-05-s3:target)]:opacity-100"></span></a>
    <a href="#tfps-05-s4" class="group/link relative grid size-11 place-items-center rounded-full no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps05-acc"><span class="pointer-events-none absolute top-1/2 right-[calc(100%+.35rem)] -translate-y-1/2 translate-x-1.5 rounded-lg border border-tfps05-ink/10 bg-tfps05-panel/85 px-2 py-1 text-[.78rem] whitespace-nowrap text-tfps05-ink opacity-0 shadow-[0_8px_20px_-12px_var(--color-tfps05-shade)] backdrop-blur-sm transition-[opacity,translate] duration-200 group-hover/link:translate-x-0 group-hover/link:opacity-100 group-focus-visible/link:translate-x-0 group-focus-visible/link:opacity-100">Audit</span><span class="[--tl:--tfps05-4] tfps05-scrub size-[.62rem] rounded-full bg-tfps05-ink opacity-35 transition-[opacity,scale,background-color] duration-300 in-[.tfps-05:has(#tfps-05-s4:target)]:scale-[2.1] in-[.tfps-05:has(#tfps-05-s4:target)]:bg-tfps05-acc in-[.tfps-05:has(#tfps-05-s4:target)]:opacity-100"></span></a>
    <a href="#tfps-05-s5" class="group/link relative grid size-11 place-items-center rounded-full no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps05-acc"><span class="pointer-events-none absolute top-1/2 right-[calc(100%+.35rem)] -translate-y-1/2 translate-x-1.5 rounded-lg border border-tfps05-ink/10 bg-tfps05-panel/85 px-2 py-1 text-[.78rem] whitespace-nowrap text-tfps05-ink opacity-0 shadow-[0_8px_20px_-12px_var(--color-tfps05-shade)] backdrop-blur-sm transition-[opacity,translate] duration-200 group-hover/link:translate-x-0 group-hover/link:opacity-100 group-focus-visible/link:translate-x-0 group-focus-visible/link:opacity-100">Scale</span><span class="[--tl:--tfps05-5] tfps05-scrub size-[.62rem] rounded-full bg-tfps05-ink opacity-35 transition-[opacity,scale,background-color] duration-300 in-[.tfps-05:has(#tfps-05-s5:target)]:scale-[2.1] in-[.tfps-05:has(#tfps-05-s5:target)]:bg-tfps05-acc in-[.tfps-05:has(#tfps-05-s5:target)]:opacity-100"></span></a>
    <a href="#tfps-05-s6" class="group/link relative grid size-11 place-items-center rounded-full no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps05-acc"><span class="pointer-events-none absolute top-1/2 right-[calc(100%+.35rem)] -translate-y-1/2 translate-x-1.5 rounded-lg border border-tfps05-ink/10 bg-tfps05-panel/85 px-2 py-1 text-[.78rem] whitespace-nowrap text-tfps05-ink opacity-0 shadow-[0_8px_20px_-12px_var(--color-tfps05-shade)] backdrop-blur-sm transition-[opacity,translate] duration-200 group-hover/link:translate-x-0 group-hover/link:opacity-100 group-focus-visible/link:translate-x-0 group-focus-visible/link:opacity-100">Start</span><span class="[--tl:--tfps05-6] tfps05-scrub size-[.62rem] rounded-full bg-tfps05-ink opacity-35 transition-[opacity,scale,background-color] duration-300 in-[.tfps-05:has(#tfps-05-s6:target)]:scale-[2.1] in-[.tfps-05:has(#tfps-05-s6:target)]:bg-tfps05-acc in-[.tfps-05:has(#tfps-05-s6:target)]:opacity-100"></span></a>
  </nav>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps05-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Full page sections, six panels">

    <section class="[view-timeline-name:--tfps05-1] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps05-panel px-[clamp(3.75rem,8vw,7rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps05-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps05-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps05-shade)] forced-colors:border-[CanvasText]" id="tfps-05-s1" aria-labelledby="tfps-05-h1">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps05-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps05-acc">01 / 06</span><span class="rounded-[.45rem] border border-tfps05-ink/12 px-2 py-[.22rem] font-tfps05-mono text-[.7rem] text-tfps05-ink/75">[view-timeline-name:--tfps05-1]</span></p>
        <h2 class="max-w-[20ch] text-[clamp(2rem,5.6vw,3.9rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-05-h1">A dot rail that knows where you are</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps05-ink/75 [&_code]:text-tfps05-ink">Six panels, six anchors, zero scroll listeners. Each panel publishes a view timeline and each dot consumes it, so the active state is computed by the compositor &mdash; not by a handler racing your scroll.</p>
        <a href="#tfps-05-s2" class="inline-flex min-h-11 items-center gap-2.5 rounded-full pe-3 font-tfps05-mono text-[.82rem] text-tfps05-ink/75 no-underline transition-colors hover:text-tfps05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps05-acc"><svg class="size-[1.1rem] animate-tfps05-bob motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Watch the rail as you scroll &mdash; or Tab into it</a>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps05-2] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps05-panel px-[clamp(3.75rem,8vw,7rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps05-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps05-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps05-shade)] forced-colors:border-[CanvasText]" id="tfps-05-s2" aria-labelledby="tfps-05-h2">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps05-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps05-acc">02 / 06</span><span class="rounded-[.45rem] border border-tfps05-ink/12 px-2 py-[.22rem] font-tfps05-mono text-[.7rem] text-tfps05-ink/75">timeline-scope</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-05-h2">Hoisting a timeline out of the scroller</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps05-ink/75 [&_code]:text-tfps05-ink">A timeline name is only visible to descendants. The rail is fixed and lives outside the panels, so the root declares <code>timeline-scope</code> for all six names &mdash; that one class is what lets a dot animate to a sibling subtree's scroll.</p>
        <pre class="w-full overflow-x-auto overflow-y-hidden rounded-2xl border border-tfps05-ink/10 bg-tfps05-ink/[.04] px-[1.1rem] py-4"><code class="text-[clamp(.78rem,1vw,.88rem)] leading-[1.75] whitespace-pre text-tfps05-ink/75 [&_mark]:rounded-[.25rem] [&_mark]:bg-tfps05-acc/15 [&_mark]:px-[.2rem] [&_mark]:text-tfps05-acc">&lt;div class="<mark>[timeline-scope:--tfps05-1,…,--tfps05-6]</mark>"&gt;
&lt;section class="<mark>[view-timeline-name:--tfps05-2]</mark>"&gt;
&lt;span class="[--tl:--tfps05-2] <mark>tfps05-scrub</mark>"&gt;</code></pre>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps05-3] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps05-panel px-[clamp(3.75rem,8vw,7rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps05-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps05-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps05-shade)] forced-colors:border-[CanvasText]" id="tfps-05-s3" aria-labelledby="tfps-05-h3">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps05-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps05-acc">03 / 06</span><span class="rounded-[.45rem] border border-tfps05-ink/12 px-2 py-[.22rem] font-tfps05-mono text-[.7rem] text-tfps05-ink/75">animation-range: cover</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-05-h3">Why the active band sits at 50%</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps05-ink/75 [&_code]:text-tfps05-ink">The <code>cover</code> range starts when a panel first enters the scrollport and ends when it fully leaves. A panel exactly one scrollport tall is therefore perfectly aligned at 50% &mdash; so the dot is keyed to light between 47% and 53% and nowhere else.</p>
        <ul class="grid w-full gap-1">
          <li class="grid grid-cols-[4.5rem_1fr] items-baseline gap-4 border-t border-tfps05-ink/10 py-3"><strong class="font-tfps05-mono text-[.82rem] font-medium text-tfps05-acc tabular-nums">0%</strong><span class="text-[.95rem] text-tfps05-ink/75">panel&rsquo;s top edge enters from below</span></li>
          <li class="grid grid-cols-[4.5rem_1fr] items-baseline gap-4 border-t border-tfps05-ink/10 py-3"><strong class="font-tfps05-mono text-[.82rem] font-medium text-tfps05-acc tabular-nums">50%</strong><span class="text-[.95rem] text-tfps05-ink/75">panel fills the scrollport &mdash; dot active</span></li>
          <li class="grid grid-cols-[4.5rem_1fr] items-baseline gap-4 border-t border-tfps05-ink/10 py-3"><strong class="font-tfps05-mono text-[.82rem] font-medium text-tfps05-acc tabular-nums">100%</strong><span class="text-[.95rem] text-tfps05-ink/75">panel&rsquo;s bottom edge leaves the top</span></li>
        </ul>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps05-4] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps05-panel px-[clamp(3.75rem,8vw,7rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps05-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps05-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps05-shade)] forced-colors:border-[CanvasText]" id="tfps-05-s4" aria-labelledby="tfps-05-h4">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps05-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps05-acc">04 / 06</span><span class="rounded-[.45rem] border border-tfps05-ink/12 px-2 py-[.22rem] font-tfps05-mono text-[.7rem] text-tfps05-ink/75">size-11 hit target</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-05-h4">Ten-pixel dots, forty-four-pixel targets</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps05-ink/75 [&_code]:text-tfps05-ink">The visual can be tiny; the target cannot. Each anchor is <code>size-11</code> to satisfy WCAG 2.2 target size, its label is real text revealed by <code>group-hover/link:</code> and <code>group-focus-visible/link:</code> rather than a <code>title</code>, and the focus ring is a 2&nbsp;px outline at full contrast.</p>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps05-5] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps05-panel px-[clamp(3.75rem,8vw,7rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps05-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps05-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps05-shade)] forced-colors:border-[CanvasText]" id="tfps-05-s5" aria-labelledby="tfps-05-h5">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps05-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps05-acc">05 / 06</span><span class="rounded-[.45rem] border border-tfps05-ink/12 px-2 py-[.22rem] font-tfps05-mono text-[.7rem] text-tfps05-ink/75">:target fallback</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-05-h5">What happens on a browser without scroll-driven CSS</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps05-ink/75 [&_code]:text-tfps05-ink">The rail still works. Each dot also carries <code>in-[.tfps-05:has(#id:target)]:</code> utilities, shipped unconditionally, so a clicked dot stays lit &mdash; and <code>:not(:has(section:target))</code> lights the first dot before anything is clicked.</p>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps05-6] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps05-panel px-[clamp(3.75rem,8vw,7rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps05-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps05-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps05-shade)] forced-colors:border-[CanvasText]" id="tfps-05-s6" aria-labelledby="tfps-05-h6">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps05-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps05-acc">06 / 06</span><span class="rounded-[.45rem] border border-tfps05-ink/12 px-2 py-[.22rem] font-tfps05-mono text-[.7rem] text-tfps05-ink/75">ship it</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-05-h6">Four edits to add a seventh panel</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps05-ink/75 [&_code]:text-tfps05-ink">Give the section an id and a <code>[view-timeline-name:…]</code>, add that name to the root's <code>timeline-scope</code>, copy one dot anchor. No index arithmetic, no count stored anywhere.</p>
        <a class="inline-flex min-h-11 items-center gap-2 rounded-full border border-tfps05-acc/40 px-[1.15rem] py-3 text-[.9rem] text-tfps05-acc no-underline transition-colors hover:bg-tfps05-acc/10 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tfps05-acc" href="#tfps-05-s1"><svg class="size-4 -rotate-90" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h13.5M12.6 6.5 18.2 12l-5.6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Return to panel one</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps05-bg: #f8f8fb;
  --color-tfps05-bg: oklch(97.6% .004 285);
  --color-tfps05-panel: #ffffff;
  --color-tfps05-panel: oklch(1 0 0);
  --color-tfps05-panel2: #f0f0f6;
  --color-tfps05-panel2: oklch(95.2% .008 285);
  --color-tfps05-ink: #0d0d16;
  --color-tfps05-ink: oklch(13% .015 285);
  --color-tfps05-acc: #4f46e5;
  --color-tfps05-acc: oklch(52% .21 278);
  --color-tfps05-shade: rgb(13 13 22 / .22);
  --font-tfps05-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps05-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --animate-tfps05-bob: tfps05-bob 2.4s ease-in-out infinite;

  @keyframes tfps05-bob {
    0%,
        100% {
      translate: 0 -2px;
    }

    50% {
      translate: 0 3px;
    }
  }
}
/* Theme state. Dark = OS preference XOR the toggle, so the switch always flips what you see —
   the CSS original's checkbox did nothing for visitors whose OS was already dark. */

@custom-variant tfps05-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-05:has(#tfps-05-theme:checked), .tfps-05:has(#tfps-05-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-05:not(:has(#tfps-05-theme:checked)), .tfps-05:not(:has(#tfps-05-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-05 {
  width: 100%;
  min-height: 100svh;

  @variant tfps05-dark {
    --color-tfps05-bg: #07070c;
    --color-tfps05-bg: oklch(0.131 0.012 284.7);
    --color-tfps05-panel: #0b0b11;
    --color-tfps05-panel: oklch(0.153 0.013 284.8);
    --color-tfps05-panel2: #11111a;
    --color-tfps05-panel2: oklch(0.182 0.018 284.4);
    --color-tfps05-ink: #f3f3f9;
    --color-tfps05-ink: oklch(0.966 0.008 286.2);
    --color-tfps05-acc: #a5b4fc;
    --color-tfps05-acc: oklch(0.785 0.104 274.7);
    --color-tfps05-shade: rgb(0 0 0 / .7);
  }
}
/* What stayed CSS: the scrubbed dot. animate-* compiles to the animation shorthand, which resets
   animation-timeline, so shorthand, timeline and range are set together, in order, in one utility. */

@keyframes tfps05-dot {
  0%,
    40% {
    scale: 1;
    opacity: .35;
    background-color: var(--color-tfps05-ink);
  }

  47%,
    53% {
    scale: 2.1;
    opacity: 1;
    background-color: var(--color-tfps05-acc);
  }

  60%,
    100% {
    scale: 1;
    opacity: .35;
    background-color: var(--color-tfps05-ink);
  }
}

@utility tfps05-scrub {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps05-dot linear both;
      animation-timeline: var(--tl);
      animation-range: cover 0% cover 100%;
    }
  }
}
```
