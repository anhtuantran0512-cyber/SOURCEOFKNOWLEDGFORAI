---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-page-scroll-snap-without-javascript/"
title: "Tailwind Full Page Scroll Snap Without JavaScript"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "The library replacement, in four utility classes: a one-page scroller built from h-dvh overflow-y-auto snap-y snap-mandatory and snap-start &mdash; no…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full Page Scroll Snap Without JavaScript
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-page-scroll-snap-without-javascript/

The library replacement, in four utility classes: a one-page scroller built from h-dvh overflow-y-auto snap-y snap-mandatory and snap-start &mdash; no fullPage.js, no observers, no 60&nbsp;kB of script. A frosted side rail of anchor links jumps between sections with native scroll-smooth, lights the clicked link through in-[…:has(#id:target)]:, and folds into a bottom pill on phones. An honest trade-off panel lists what the library gave you that CSS does not.
## HTML
```html
<div class="tfps-02 [timeline-scope:--tfps02-1,--tfps02-2,--tfps02-3,--tfps02-4] relative isolate w-full min-h-svh bg-tfps02-bg font-tfps02-sans text-tfps02-ink antialiased [&_code]:font-tfps02-mono [&_code]:text-[.92em]">
  <input class="peer sr-only" type="checkbox" id="tfps-02-theme">
  <label for="tfps-02-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps02-ink/10 bg-white/60 text-tfps02-ink hover:bg-white/85 tfps02-dark:bg-white/[.07] tfps02-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps02-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps02-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps02-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps02-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <nav aria-label="Section links" class="fixed z-70 grid gap-0.5 rounded-2xl border border-tfps02-ink/10 bg-white/60 p-1.5 shadow-[0_18px_40px_-26px_var(--color-tfps02-shade)] backdrop-blur-md backdrop-saturate-150 tfps02-dark:bg-white/[.06] max-lg:bottom-4 max-lg:left-1/2 max-lg:-translate-x-1/2 max-lg:grid-flow-col max-lg:rounded-full lg:top-1/2 lg:left-[clamp(.6rem,2vw,1.5rem)] lg:-translate-y-1/2 forced-colors:border-[CanvasText]">
    <a href="#tfps-02-s1" class="[--tl:--tfps02-1] tfps02-spy flex min-h-11 min-w-11 items-center justify-center gap-2.5 rounded-xl px-3 py-1.5 text-[.84rem] whitespace-nowrap text-tfps02-ink/75 no-underline transition-colors duration-200 hover:bg-tfps02-ink/6 hover:text-tfps02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps02-acc max-lg:rounded-full lg:justify-start in-[.tfps-02:has(#tfps-02-s1:target)]:bg-tfps02-acc/12 in-[.tfps-02:has(#tfps-02-s1:target)]:text-tfps02-ink in-[.tfps-02:not(:has(section:target))]:bg-tfps02-acc/12 in-[.tfps-02:not(:has(section:target))]:text-tfps02-ink"><span class="font-tfps02-mono text-[.68rem] tracking-[.06em] text-tfps02-acc">01</span><span class="max-lg:sr-only">Overview</span></a>
    <a href="#tfps-02-s2" class="[--tl:--tfps02-2] tfps02-spy flex min-h-11 min-w-11 items-center justify-center gap-2.5 rounded-xl px-3 py-1.5 text-[.84rem] whitespace-nowrap text-tfps02-ink/75 no-underline transition-colors duration-200 hover:bg-tfps02-ink/6 hover:text-tfps02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps02-acc max-lg:rounded-full lg:justify-start in-[.tfps-02:has(#tfps-02-s2:target)]:bg-tfps02-acc/12 in-[.tfps-02:has(#tfps-02-s2:target)]:text-tfps02-ink"><span class="font-tfps02-mono text-[.68rem] tracking-[.06em] text-tfps02-acc">02</span><span class="max-lg:sr-only">The three rules</span></a>
    <a href="#tfps-02-s3" class="[--tl:--tfps02-3] tfps02-spy flex min-h-11 min-w-11 items-center justify-center gap-2.5 rounded-xl px-3 py-1.5 text-[.84rem] whitespace-nowrap text-tfps02-ink/75 no-underline transition-colors duration-200 hover:bg-tfps02-ink/6 hover:text-tfps02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps02-acc max-lg:rounded-full lg:justify-start in-[.tfps-02:has(#tfps-02-s3:target)]:bg-tfps02-acc/12 in-[.tfps-02:has(#tfps-02-s3:target)]:text-tfps02-ink"><span class="font-tfps02-mono text-[.68rem] tracking-[.06em] text-tfps02-acc">03</span><span class="max-lg:sr-only">Trade-offs</span></a>
    <a href="#tfps-02-s4" class="[--tl:--tfps02-4] tfps02-spy flex min-h-11 min-w-11 items-center justify-center gap-2.5 rounded-xl px-3 py-1.5 text-[.84rem] whitespace-nowrap text-tfps02-ink/75 no-underline transition-colors duration-200 hover:bg-tfps02-ink/6 hover:text-tfps02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps02-acc max-lg:rounded-full lg:justify-start in-[.tfps-02:has(#tfps-02-s4:target)]:bg-tfps02-acc/12 in-[.tfps-02:has(#tfps-02-s4:target)]:text-tfps02-ink"><span class="font-tfps02-mono text-[.68rem] tracking-[.06em] text-tfps02-acc">04</span><span class="max-lg:sr-only">Ship it</span></a>
  </nav>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps02-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="One page scroller, four sections">

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps02-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps02-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps02-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps02-shade)] forced-colors:border-[CanvasText] lg:ps-[clamp(11rem,20vw,15rem)] [view-timeline-name:--tfps02-1] [view-timeline-axis:block]" id="tfps-02-s1" aria-labelledby="tfps-02-h1">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] items-center gap-[clamp(1.5rem,4vw,3.5rem)] min-[56rem]:grid-cols-[1.1fr_.9fr] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <div class="grid justify-items-start gap-[clamp(.9rem,2vh,1.35rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps02-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps02-acc">01 / 04</span><span class="rounded-[.45rem] border border-tfps02-ink/12 px-2 py-[.22rem] font-tfps02-mono text-[.7rem] text-tfps02-ink/75">0&nbsp;kB of JavaScript</span></p>
          <h2 class="max-w-[20ch] text-[clamp(2rem,5.4vw,3.9rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-02-h1">A one-page scroller with nothing to install</h2>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps02-ink/75 [&_code]:text-tfps02-ink">Full-viewport sections, native momentum, smooth anchor jumps, a working back button. Everything a full-page scrolling library gives you, minus the library &mdash; and minus the scroll hijacking that breaks trackpads.</p>
          <ul class="flex flex-wrap gap-[clamp(1rem,3vw,2.25rem)]">
            <li class="grid gap-0.5"><strong class="text-[clamp(1.6rem,3vw,2.2rem)] font-semibold tracking-[-.03em] tabular-nums">4</strong><span class="font-tfps02-mono text-[.68rem] tracking-[.1em] uppercase text-tfps02-ink/70">utility classes</span></li>
            <li class="grid gap-0.5"><strong class="text-[clamp(1.6rem,3vw,2.2rem)] font-semibold tracking-[-.03em] tabular-nums">0</strong><span class="font-tfps02-mono text-[.68rem] tracking-[.1em] uppercase text-tfps02-ink/70">dependencies</span></li>
            <li class="grid gap-0.5"><strong class="text-[clamp(1.6rem,3vw,2.2rem)] font-semibold tracking-[-.03em] tabular-nums">0</strong><span class="font-tfps02-mono text-[.68rem] tracking-[.1em] uppercase text-tfps02-ink/70">wheel listeners</span></li>
          </ul>
        </div>
        <aside aria-label="Core markup" class="w-full overflow-hidden rounded-[1.25rem] border border-tfps02-ink/10 bg-tfps02-ink/[.04] shadow-[0_26px_56px_-34px_var(--color-tfps02-shade)]">
          <p class="flex items-center justify-between border-b border-tfps02-ink/10 px-4 py-3 font-tfps02-mono text-[.66rem] tracking-[.12em] uppercase text-tfps02-ink/70">the entire engine<span class="normal-case tracking-normal text-tfps02-acc">4 classes</span></p>
          <pre class="overflow-x-auto overflow-y-hidden px-4 pt-4 pb-5"><code class="text-[clamp(.78rem,1.05vw,.9rem)] leading-[1.8] whitespace-pre text-tfps02-ink/75 [&_mark]:rounded-[.25rem] [&_mark]:bg-tfps02-acc/15 [&_mark]:px-[.15rem] [&_mark]:text-tfps02-acc">&lt;div class="h-dvh overflow-y-auto
  <mark>snap-y snap-mandatory</mark>
  scroll-smooth"&gt;
  &lt;section class="min-h-dvh
    <mark>snap-start</mark>"&gt;
  &lt;/section&gt;
&lt;/div&gt;</code></pre>
        </aside>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps02-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps02-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps02-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps02-shade)] forced-colors:border-[CanvasText] lg:ps-[clamp(11rem,20vw,15rem)] [view-timeline-name:--tfps02-2] [view-timeline-axis:block]" id="tfps-02-s2" aria-labelledby="tfps-02-h2">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps02-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps02-acc">02 / 04</span><span class="rounded-[.45rem] border border-tfps02-ink/12 px-2 py-[.22rem] font-tfps02-mono text-[.7rem] text-tfps02-ink/75">how it works</span></p>
        <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-02-h2">Three rules, in the order they matter</h2>
        <ol class="grid w-full gap-1.5">
          <li class="grid gap-1.5 border-t border-tfps02-ink/10 py-[clamp(.9rem,1.8vh,1.2rem)]">
            <p class="flex items-baseline gap-3 text-[1.06rem] font-semibold tracking-[-.01em]"><span class="font-tfps02-mono text-[.7rem] font-medium text-tfps02-acc">01</span>Own the scrollport</p>
            <p class="max-w-[64ch] text-[.97rem] leading-[1.6] text-pretty text-tfps02-ink/75">A container with <code>h-dvh overflow-y-auto</code>. Snapping applies to the element that scrolls, so it must be yours &mdash; never <code>html</code>.</p>
          </li>
          <li class="grid gap-1.5 border-t border-tfps02-ink/10 py-[clamp(.9rem,1.8vh,1.2rem)]">
            <p class="flex items-baseline gap-3 text-[1.06rem] font-semibold tracking-[-.01em]"><span class="font-tfps02-mono text-[.7rem] font-medium text-tfps02-acc">02</span>Declare the snap axis</p>
            <p class="max-w-[64ch] text-[.97rem] leading-[1.6] text-pretty text-tfps02-ink/75"><code>snap-y snap-mandatory</code>. The compositor now lands the scroll on the nearest snap point on its own thread, off the main thread entirely.</p>
          </li>
          <li class="grid gap-1.5 border-t border-tfps02-ink/10 py-[clamp(.9rem,1.8vh,1.2rem)]">
            <p class="flex items-baseline gap-3 text-[1.06rem] font-semibold tracking-[-.01em]"><span class="font-tfps02-mono text-[.7rem] font-medium text-tfps02-acc">03</span>Mark the snap edges</p>
            <p class="max-w-[64ch] text-[.97rem] leading-[1.6] text-pretty text-tfps02-ink/75"><code>snap-start</code> on each <code>min-h-dvh</code> panel. Every panel top becomes a stop; the sequence is now a scroller.</p>
          </li>
        </ol>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps02-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps02-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps02-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps02-shade)] forced-colors:border-[CanvasText] lg:ps-[clamp(11rem,20vw,15rem)] [view-timeline-name:--tfps02-3] [view-timeline-axis:block]" id="tfps-02-s3" aria-labelledby="tfps-02-h3">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps02-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps02-acc">03 / 04</span><span class="rounded-[.45rem] border border-tfps02-ink/12 px-2 py-[.22rem] font-tfps02-mono text-[.7rem] text-tfps02-ink/75">honest comparison</span></p>
        <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-02-h3">What you gain, what you give up</h2>
        <div class="grid w-full grid-cols-[repeat(auto-fit,minmax(16rem,1fr))] gap-[clamp(.85rem,2vw,1.5rem)]">
          <div class="grid content-start gap-3.5 rounded-[1.25rem] border border-tfps02-ink/10 bg-tfps02-bg p-[clamp(1.1rem,2.4vw,1.6rem)] forced-colors:border-[CanvasText]">
            <p class="flex items-center gap-2 font-tfps02-mono text-[.7rem] tracking-[.12em] uppercase text-tfps02-yes"><svg class="size-[1.05rem]" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12.8l4.6 4.4L19.5 6.9" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>You gain</p>
            <ul class="grid gap-2.5">
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-yes before:content-['']">Native touch momentum and iOS rubber-banding</li>
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-yes before:content-['']">Space, Page&nbsp;Up/Down and arrow keys, for free</li>
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-yes before:content-['']">Find-in-page and screen readers keep working</li>
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-yes before:content-['']">Snap runs on the compositor thread &mdash; no jank</li>
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-yes before:content-['']">Nothing to load, nothing to version-bump</li>
            </ul>
          </div>
          <div class="grid content-start gap-3.5 rounded-[1.25rem] border border-tfps02-ink/10 bg-tfps02-bg p-[clamp(1.1rem,2.4vw,1.6rem)] forced-colors:border-[CanvasText]">
            <p class="flex items-center gap-2 font-tfps02-mono text-[.7rem] tracking-[.12em] uppercase text-tfps02-no"><svg class="size-[1.05rem]" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>You give up</p>
            <ul class="grid gap-2.5">
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-no before:content-['']">No programmatic <code>moveTo(n)</code> section API</li>
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-no before:content-['']">No <code>afterLoad</code> / <code>onLeave</code> lifecycle callbacks</li>
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-no before:content-['']">No section-change events without an observer</li>
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-no before:content-['']">No horizontal sub-slides inside a section</li>
              <li class="relative ps-[1.1rem] text-[.95rem] leading-[1.5] text-pretty text-tfps02-ink/75 before:absolute before:start-0 before:top-[.55em] before:size-[.35rem] before:rounded-full before:bg-tfps02-no before:content-['']">One-per-gesture needs <code>snap-always</code></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps02-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps02-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps02-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps02-shade)] forced-colors:border-[CanvasText] lg:ps-[clamp(11rem,20vw,15rem)] [view-timeline-name:--tfps02-4] [view-timeline-axis:block]" id="tfps-02-s4" aria-labelledby="tfps-02-h4">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps02-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps02-acc">04 / 04</span><span class="rounded-[.45rem] border border-tfps02-ink/12 px-2 py-[.22rem] font-tfps02-mono text-[.7rem] text-tfps02-ink/75">copy the pattern</span></p>
        <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-02-h4">Then add script only where it earns its place</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps02-ink/75 [&_code]:text-tfps02-ink">Start from the classes. If the design later needs a section-change event for analytics or a lazy video, one <code>IntersectionObserver</code> at <code>threshold:.6</code> gives you the callback &mdash; and the scroller still works when that script fails.</p>
        <figure class="grid max-w-[46ch] gap-2.5 border-s-2 border-tfps02-acc ps-[1.1rem]">
          <blockquote class="text-[clamp(1.05rem,1.9vw,1.35rem)] leading-[1.45] tracking-[-.02em] text-pretty"><p>&ldquo;We replaced a full-page library with four utility classes and the marketing site&rsquo;s Largest Contentful Paint dropped by 340&nbsp;ms.&rdquo;</p></blockquote>
          <figcaption class="font-tfps02-mono text-[.68rem] tracking-[.1em] uppercase text-tfps02-ink/70">Priya Sharma &middot; front-end lead</figcaption>
        </figure>
        <a class="inline-flex min-h-11 items-center gap-2 rounded-full border border-tfps02-acc/40 px-[1.15rem] py-3 text-[.9rem] text-tfps02-acc no-underline transition-colors hover:bg-tfps02-acc/10 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tfps02-acc" href="#tfps-02-s1"><svg class="size-4 -rotate-90" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h13.5M12.6 6.5 18.2 12l-5.6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Back to the first panel</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps02-bg: #fbfbfd;
  --color-tfps02-bg: oklch(0.989 0.003 286.4);
  --color-tfps02-panel: #ffffff;
  --color-tfps02-panel: oklch(1 0 0);
  --color-tfps02-panel2: #f2f2f7;
  --color-tfps02-panel2: oklch(0.963 0.007 286.3);
  --color-tfps02-ink: #0e0e14;
  --color-tfps02-ink: oklch(14% .01 285);
  --color-tfps02-acc: #6d28d9;
  --color-tfps02-acc: oklch(50% .22 292);
  --color-tfps02-yes: #0f766e;
  --color-tfps02-yes: oklch(48% .1 175);
  --color-tfps02-no: #9f1239;
  --color-tfps02-no: oklch(48% .16 12);
  --color-tfps02-shade: rgb(14 14 20 / .22);
  --font-tfps02-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps02-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
}
/* Theme state. Dark = OS preference XOR the toggle, so the switch always flips what you see —
   the CSS original's checkbox did nothing for visitors whose OS was already dark. */

@custom-variant tfps02-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-02:has(#tfps-02-theme:checked), .tfps-02:has(#tfps-02-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-02:not(:has(#tfps-02-theme:checked)), .tfps-02:not(:has(#tfps-02-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-02 {
  width: 100%;
  min-height: 100svh;

  @variant tfps02-dark {
    --color-tfps02-bg: #08080c;
    --color-tfps02-bg: oklch(0.137 0.009 285.1);
    --color-tfps02-panel: #0c0c12;
    --color-tfps02-panel: oklch(0.157 0.013 284.9);
    --color-tfps02-panel2: #12121a;
    --color-tfps02-panel2: oklch(0.186 0.016 284.7);
    --color-tfps02-ink: #f4f4f8;
    --color-tfps02-ink: oklch(0.968 0.005 286.3);
    --color-tfps02-acc: #c4b5fd;
    --color-tfps02-acc: oklch(0.811 0.101 293.6);
    --color-tfps02-yes: #5eead4;
    --color-tfps02-yes: oklch(0.855 0.125 181.1);
    --color-tfps02-no: #fda4af;
    --color-tfps02-no: oklch(0.81 0.106 11.6);
    --color-tfps02-shade: rgb(0 0 0 / .7);
  }
}
/* Live scroll spy: each link scrubs against its own panel's view timeline and is lit only while
   that panel fills the scrollport (the 34–66% band of cover). Overrides the :target fallback. */

@keyframes tfps02-spy {
  0%,
    33% {
    background-color: transparent;
    color: color-mix(in oklab, var(--color-tfps02-ink) 75%, transparent);
  }

  34%,
    66% {
    background-color: color-mix(in oklab, var(--color-tfps02-acc) 12%, transparent);
    color: var(--color-tfps02-ink);
  }

  67%,
    100% {
    background-color: transparent;
    color: color-mix(in oklab, var(--color-tfps02-ink) 75%, transparent);
  }
}

@utility tfps02-spy {
  @supports (animation-timeline: view()) {
    animation: tfps02-spy linear both;
    animation-timeline: var(--tl);
    animation-range: cover 0% cover 100%;
  }
}
```
