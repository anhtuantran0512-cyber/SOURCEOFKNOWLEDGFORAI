---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-horizontal-scroll-snap-full-screen-panels/"
title: "Tailwind Horizontal Scroll Snap Full Screen Panels"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "Five full-viewport chapters that scroll sideways with snap-x snap-mandatory &mdash; and flip to a vertical stack under 48&nbsp;rem with max-md:flex-col…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Horizontal Scroll Snap Full Screen Panels
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-horizontal-scroll-snap-full-screen-panels/

Five full-viewport chapters that scroll sideways with snap-x snap-mandatory &mdash; and flip to a vertical stack under 48&nbsp;rem with max-md:flex-col max-md:snap-y, because horizontal scrolling on a phone is hostile. Chapter anchors that light up for the chapter you jumped to, a visible next-panel edge, native keyboard support from the focusable scrollport, and no JavaScript.
## HTML
```html
<div class="tfps-11 [timeline-scope:--tfps11-1,--tfps11-2,--tfps11-3,--tfps11-4,--tfps11-5] relative isolate w-full min-h-svh bg-tfps11-bg font-tfps11-sans text-tfps11-ink antialiased [&_code]:font-tfps11-mono [&_code]:text-[.92em]">
  <input class="peer sr-only" type="checkbox" id="tfps-11-theme">
  <label for="tfps-11-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps11-ink/10 bg-white/60 text-tfps11-ink hover:bg-white/85 tfps11-dark:bg-white/[.07] tfps11-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps11-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps11-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps11-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps11-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <nav aria-label="Chapters" class="fixed bottom-[1.15rem] left-1/2 z-70 flex -translate-x-1/2 gap-0.5 rounded-full border border-tfps11-ink/10 bg-white/70 p-1 shadow-[0_14px_34px_-22px_var(--color-tfps11-shade)] backdrop-blur-md backdrop-saturate-150 tfps11-dark:bg-white/[.07] forced-colors:border-[CanvasText]"><a href="#tfps-11-s1" aria-label="Chapter 1" class="[--tl:--tfps11-1] tfps11-spy grid min-h-11 min-w-11 place-items-center rounded-full font-tfps11-mono text-[.76rem] tracking-[.06em] text-tfps11-ink/75 no-underline transition-colors duration-200 hover:bg-tfps11-acc/10 hover:text-tfps11-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps11-acc in-[.tfps-11:has(#tfps-11-s1:target)]:bg-tfps11-acc in-[.tfps-11:has(#tfps-11-s1:target)]:text-tfps11-bg in-[.tfps-11:not(:has(section:target))]:bg-tfps11-acc in-[.tfps-11:not(:has(section:target))]:text-tfps11-bg">01</a><a href="#tfps-11-s2" aria-label="Chapter 2" class="[--tl:--tfps11-2] tfps11-spy grid min-h-11 min-w-11 place-items-center rounded-full font-tfps11-mono text-[.76rem] tracking-[.06em] text-tfps11-ink/75 no-underline transition-colors duration-200 hover:bg-tfps11-acc/10 hover:text-tfps11-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps11-acc in-[.tfps-11:has(#tfps-11-s2:target)]:bg-tfps11-acc in-[.tfps-11:has(#tfps-11-s2:target)]:text-tfps11-bg">02</a><a href="#tfps-11-s3" aria-label="Chapter 3" class="[--tl:--tfps11-3] tfps11-spy grid min-h-11 min-w-11 place-items-center rounded-full font-tfps11-mono text-[.76rem] tracking-[.06em] text-tfps11-ink/75 no-underline transition-colors duration-200 hover:bg-tfps11-acc/10 hover:text-tfps11-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps11-acc in-[.tfps-11:has(#tfps-11-s3:target)]:bg-tfps11-acc in-[.tfps-11:has(#tfps-11-s3:target)]:text-tfps11-bg">03</a><a href="#tfps-11-s4" aria-label="Chapter 4" class="[--tl:--tfps11-4] tfps11-spy grid min-h-11 min-w-11 place-items-center rounded-full font-tfps11-mono text-[.76rem] tracking-[.06em] text-tfps11-ink/75 no-underline transition-colors duration-200 hover:bg-tfps11-acc/10 hover:text-tfps11-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps11-acc in-[.tfps-11:has(#tfps-11-s4:target)]:bg-tfps11-acc in-[.tfps-11:has(#tfps-11-s4:target)]:text-tfps11-bg">04</a><a href="#tfps-11-s5" aria-label="Chapter 5" class="[--tl:--tfps11-5] tfps11-spy grid min-h-11 min-w-11 place-items-center rounded-full font-tfps11-mono text-[.76rem] tracking-[.06em] text-tfps11-ink/75 no-underline transition-colors duration-200 hover:bg-tfps11-acc/10 hover:text-tfps11-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps11-acc in-[.tfps-11:has(#tfps-11-s5:target)]:bg-tfps11-acc in-[.tfps-11:has(#tfps-11-s5:target)]:text-tfps11-bg">05</a></nav>

  <div class="flex h-dvh flex-nowrap overflow-x-auto overflow-y-hidden snap-x snap-mandatory scroll-smooth overscroll-x-contain overscroll-y-none [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps11-acc max-md:flex-col max-md:overflow-x-hidden max-md:overflow-y-auto max-md:snap-y max-md:overscroll-x-auto max-md:overscroll-y-contain motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Horizontal chapter panels, five chapters. Use left and right arrow keys.">

    <section class="[--h:196] relative flex h-dvh flex-[0_0_100%] snap-start items-center bg-[oklch(96.5%_.03_calc(var(--h)*1deg))] ps-[clamp(2.5rem,6vw,6rem)] pe-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4.5rem)] not-first:-ms-16 not-first:rounded-s-[2rem] not-first:border-s not-first:border-tfps11-ink/10 not-first:ps-[calc(clamp(2.5rem,6vw,6rem)+4rem)] not-first:shadow-[-30px_0_64px_-34px_var(--color-tfps11-shade)] tfps11-dark:bg-[oklch(19%_.035_calc(var(--h)*1deg))] max-md:h-auto max-md:min-h-dvh max-md:flex-none max-md:px-[clamp(1.25rem,5vw,2rem)] max-md:not-first:ms-0 max-md:not-first:-mt-14 max-md:not-first:rounded-es-none max-md:not-first:rounded-se-[2rem] max-md:not-first:border-s-0 max-md:not-first:border-t max-md:not-first:ps-[clamp(1.25rem,5vw,2rem)] max-md:not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps11-shade)] forced-colors:border-[CanvasText] [view-timeline-name:--tfps11-1] [view-timeline-axis:inline] max-md:[view-timeline-axis:block]" id="tfps-11-s1" aria-labelledby="tfps-11-h1">
      <div class="grid w-full max-w-[48rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps11-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(42%_.12_calc(var(--h)*1deg))] tfps11-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">Chapter 01</span><span class="rounded-[.45rem] border border-tfps11-ink/12 bg-white/50 px-2 py-[.22rem] font-tfps11-mono text-[.7rem] text-tfps11-ink/75 tfps11-dark:bg-white/[.06]">snap-x snap-mandatory</span></p>
        <h2 class="max-w-[18ch] text-[clamp(2.1rem,6vw,4.4rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-11-h1">Sideways, on purpose</h2>
        <p class="max-w-[52ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps11-ink/75 [&_code]:text-tfps11-ink">Five full-viewport chapters on one horizontal scrollport. The technique mirrors the vertical case &mdash; a flex row that will not wrap, snapping on the inline axis, and a container that owns its own scroll.</p>
        <a href="#tfps-11-s2" class="inline-flex min-h-11 items-center gap-2.5 rounded-full pe-3 font-tfps11-mono text-[.82rem] text-tfps11-ink/75 no-underline transition-colors hover:text-tfps11-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps11-acc max-md:[&_svg]:rotate-90"><svg class="size-[1.1rem] animate-tfps11-nudge motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h13.5M12.6 6.5 18.2 12l-5.6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Swipe, press &rarr;, or Shift + scroll</a>
      </div>
    </section>

    <section class="[--h:152] relative flex h-dvh flex-[0_0_100%] snap-start items-center bg-[oklch(96.5%_.03_calc(var(--h)*1deg))] ps-[clamp(2.5rem,6vw,6rem)] pe-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4.5rem)] not-first:-ms-16 not-first:rounded-s-[2rem] not-first:border-s not-first:border-tfps11-ink/10 not-first:ps-[calc(clamp(2.5rem,6vw,6rem)+4rem)] not-first:shadow-[-30px_0_64px_-34px_var(--color-tfps11-shade)] tfps11-dark:bg-[oklch(19%_.035_calc(var(--h)*1deg))] max-md:h-auto max-md:min-h-dvh max-md:flex-none max-md:px-[clamp(1.25rem,5vw,2rem)] max-md:not-first:ms-0 max-md:not-first:-mt-14 max-md:not-first:rounded-es-none max-md:not-first:rounded-se-[2rem] max-md:not-first:border-s-0 max-md:not-first:border-t max-md:not-first:ps-[clamp(1.25rem,5vw,2rem)] max-md:not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps11-shade)] forced-colors:border-[CanvasText] [view-timeline-name:--tfps11-2] [view-timeline-axis:inline] max-md:[view-timeline-axis:block]" id="tfps-11-s2" aria-labelledby="tfps-11-h2">
      <div class="grid w-full max-w-[48rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps11-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(42%_.12_calc(var(--h)*1deg))] tfps11-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">Chapter 02</span><span class="rounded-[.45rem] border border-tfps11-ink/12 bg-white/50 px-2 py-[.22rem] font-tfps11-mono text-[.7rem] text-tfps11-ink/75 tfps11-dark:bg-white/[.06]">overscroll-x-contain</span></p>
        <h2 class="max-w-[24ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-11-h2">The utility that stops the browser going back</h2>
        <p class="max-w-[52ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps11-ink/75 [&_code]:text-tfps11-ink">A horizontal overscroll at the first panel is indistinguishable from a swipe-back gesture. <code>overscroll-x-contain</code> keeps the gesture inside your scroller &mdash; the difference between a slider and an accidental exit.</p>
        <pre class="w-full overflow-x-auto overflow-y-hidden rounded-2xl border border-tfps11-ink/10 bg-tfps11-ink/[.04] px-[1.1rem] py-4 bg-white/60 tfps11-dark:bg-white/[.05]"><code class="text-[clamp(.78rem,1vw,.88rem)] leading-[1.75] whitespace-pre text-tfps11-ink/75 [&_mark]:rounded-[.25rem] [&_mark]:bg-tfps11-acc/15 [&_mark]:px-[.2rem] [&_mark]:text-tfps11-acc">&lt;div class="flex overflow-x-auto
  snap-x snap-mandatory
  <mark>overscroll-x-contain</mark>"&gt;</code></pre>
      </div>
    </section>

    <section class="[--h:96] relative flex h-dvh flex-[0_0_100%] snap-start items-center bg-[oklch(96.5%_.03_calc(var(--h)*1deg))] ps-[clamp(2.5rem,6vw,6rem)] pe-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4.5rem)] not-first:-ms-16 not-first:rounded-s-[2rem] not-first:border-s not-first:border-tfps11-ink/10 not-first:ps-[calc(clamp(2.5rem,6vw,6rem)+4rem)] not-first:shadow-[-30px_0_64px_-34px_var(--color-tfps11-shade)] tfps11-dark:bg-[oklch(19%_.035_calc(var(--h)*1deg))] max-md:h-auto max-md:min-h-dvh max-md:flex-none max-md:px-[clamp(1.25rem,5vw,2rem)] max-md:not-first:ms-0 max-md:not-first:-mt-14 max-md:not-first:rounded-es-none max-md:not-first:rounded-se-[2rem] max-md:not-first:border-s-0 max-md:not-first:border-t max-md:not-first:ps-[clamp(1.25rem,5vw,2rem)] max-md:not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps11-shade)] forced-colors:border-[CanvasText] [view-timeline-name:--tfps11-3] [view-timeline-axis:inline] max-md:[view-timeline-axis:block]" id="tfps-11-s3" aria-labelledby="tfps-11-h3">
      <div class="grid w-full max-w-[48rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps11-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(42%_.12_calc(var(--h)*1deg))] tfps11-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">Chapter 03</span><span class="rounded-[.45rem] border border-tfps11-ink/12 bg-white/50 px-2 py-[.22rem] font-tfps11-mono text-[.7rem] text-tfps11-ink/75 tfps11-dark:bg-white/[.06]">max-md: flip</span></p>
        <h2 class="max-w-[24ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-11-h3">Below 48rem this becomes a vertical scroller</h2>
        <p class="max-w-[52ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps11-ink/75 [&_code]:text-tfps11-ink">Vertical is muscle memory on a phone. Rather than shrinking the horizontal experience, <code>max-md:flex-col max-md:snap-y</code> changes the direction and the snap axis &mdash; same markup, same panels, a gesture people already have.</p>
        <p class="rounded-[.6rem] border border-dashed border-tfps11-acc/40 px-3 py-2 font-tfps11-mono text-[.78rem] text-tfps11-acc">Narrow this window past 48&nbsp;rem to watch the axis flip.</p>
      </div>
    </section>

    <section class="[--h:44] relative flex h-dvh flex-[0_0_100%] snap-start items-center bg-[oklch(96.5%_.03_calc(var(--h)*1deg))] ps-[clamp(2.5rem,6vw,6rem)] pe-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4.5rem)] not-first:-ms-16 not-first:rounded-s-[2rem] not-first:border-s not-first:border-tfps11-ink/10 not-first:ps-[calc(clamp(2.5rem,6vw,6rem)+4rem)] not-first:shadow-[-30px_0_64px_-34px_var(--color-tfps11-shade)] tfps11-dark:bg-[oklch(19%_.035_calc(var(--h)*1deg))] max-md:h-auto max-md:min-h-dvh max-md:flex-none max-md:px-[clamp(1.25rem,5vw,2rem)] max-md:not-first:ms-0 max-md:not-first:-mt-14 max-md:not-first:rounded-es-none max-md:not-first:rounded-se-[2rem] max-md:not-first:border-s-0 max-md:not-first:border-t max-md:not-first:ps-[clamp(1.25rem,5vw,2rem)] max-md:not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps11-shade)] forced-colors:border-[CanvasText] [view-timeline-name:--tfps11-4] [view-timeline-axis:inline] max-md:[view-timeline-axis:block]" id="tfps-11-s4" aria-labelledby="tfps-11-h4">
      <div class="grid w-full max-w-[48rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps11-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(42%_.12_calc(var(--h)*1deg))] tfps11-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">Chapter 04</span><span class="rounded-[.45rem] border border-tfps11-ink/12 bg-white/50 px-2 py-[.22rem] font-tfps11-mono text-[.7rem] text-tfps11-ink/75 tfps11-dark:bg-white/[.06]">discoverability</span></p>
        <h2 class="max-w-[24ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-11-h4">Always show a sliver of what is next</h2>
        <p class="max-w-[52ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps11-ink/75 [&_code]:text-tfps11-ink">Horizontal scrollers fail mostly because readers never realise they can scroll. Each panel is pulled 4&nbsp;rem left with <code>not-first:-ms-16</code> and a rounded leading edge, so the next chapter's colour is on screen from the start &mdash; plus chapter anchors for people who would rather click.</p>
      </div>
    </section>

    <section class="[--h:320] relative flex h-dvh flex-[0_0_100%] snap-start items-center bg-[oklch(96.5%_.03_calc(var(--h)*1deg))] ps-[clamp(2.5rem,6vw,6rem)] pe-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4.5rem)] not-first:-ms-16 not-first:rounded-s-[2rem] not-first:border-s not-first:border-tfps11-ink/10 not-first:ps-[calc(clamp(2.5rem,6vw,6rem)+4rem)] not-first:shadow-[-30px_0_64px_-34px_var(--color-tfps11-shade)] tfps11-dark:bg-[oklch(19%_.035_calc(var(--h)*1deg))] max-md:h-auto max-md:min-h-dvh max-md:flex-none max-md:px-[clamp(1.25rem,5vw,2rem)] max-md:not-first:ms-0 max-md:not-first:-mt-14 max-md:not-first:rounded-es-none max-md:not-first:rounded-se-[2rem] max-md:not-first:border-s-0 max-md:not-first:border-t max-md:not-first:ps-[clamp(1.25rem,5vw,2rem)] max-md:not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps11-shade)] forced-colors:border-[CanvasText] [view-timeline-name:--tfps11-5] [view-timeline-axis:inline] max-md:[view-timeline-axis:block]" id="tfps-11-s5" aria-labelledby="tfps-11-h5">
      <div class="grid w-full max-w-[48rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps11-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(42%_.12_calc(var(--h)*1deg))] tfps11-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">Chapter 05</span><span class="rounded-[.45rem] border border-tfps11-ink/12 bg-white/50 px-2 py-[.22rem] font-tfps11-mono text-[.7rem] text-tfps11-ink/75 tfps11-dark:bg-white/[.06]">keyboard, for free</span></p>
        <h2 class="max-w-[24ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-11-h5">A focusable scrollport is already accessible</h2>
        <p class="max-w-[52ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps11-ink/75 [&_code]:text-tfps11-ink">Give the container <code>tabindex="0"</code> and a labelled <code>role="group"</code> and the browser handles Left, Right, Home, End and Page&nbsp;Up/Down itself. No key handler, no synthetic scrolling, nothing to get wrong.</p>
        <a class="inline-flex min-h-11 items-center gap-2 rounded-full border border-tfps11-acc/40 px-[1.15rem] py-3 text-[.9rem] text-tfps11-acc no-underline transition-colors hover:bg-tfps11-acc/10 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tfps11-acc" href="#tfps-11-s1"><svg class="size-4 -rotate-90" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h13.5M12.6 6.5 18.2 12l-5.6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Back to chapter one</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps11-bg: #f6fbfd;
  --color-tfps11-bg: oklch(98% .008 220);
  --color-tfps11-ink: #04141a;
  --color-tfps11-ink: oklch(14% .02 220);
  --color-tfps11-acc: #0e7490;
  --color-tfps11-acc: oklch(52% .11 220);
  --color-tfps11-shade: rgb(4 20 26 / .25);
  --font-tfps11-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps11-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --animate-tfps11-nudge: tfps11-nudge 2.4s ease-in-out infinite;

  @keyframes tfps11-nudge {
    0%,
        100% {
      translate: -2px 0;
    }

    50% {
      translate: 4px 0;
    }
  }
}
/* Theme state. Dark = OS preference XOR the toggle, so the switch always flips what you see —
   the CSS original's checkbox did nothing for visitors whose OS was already dark. */

@custom-variant tfps11-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-11:has(#tfps-11-theme:checked), .tfps-11:has(#tfps-11-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-11:not(:has(#tfps-11-theme:checked)), .tfps-11:not(:has(#tfps-11-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-11 {
  width: 100%;
  min-height: 100svh;

  @variant tfps11-dark {
    --color-tfps11-bg: #04090b;
    --color-tfps11-bg: oklch(0.134 0.011 219.1);
    --color-tfps11-ink: #eef8fb;
    --color-tfps11-ink: oklch(0.973 0.011 217.5);
    --color-tfps11-acc: #67e8f9;
    --color-tfps11-acc: oklch(0.865 0.115 207.1);
    --color-tfps11-shade: rgb(0 0 0 / .75);
  }
}
/* Live chapter spy: each pill button scrubs against its own panel's view timeline (inline axis on
   desktop, block below 48rem) and is lit only while that panel fills the scroller. */

@keyframes tfps11-spy {
  0%,
    33% {
    background-color: transparent;
    color: color-mix(in oklab, var(--color-tfps11-ink) 75%, transparent);
  }

  34%,
    66% {
    background-color: var(--color-tfps11-acc);
    color: var(--color-tfps11-bg);
  }

  67%,
    100% {
    background-color: transparent;
    color: color-mix(in oklab, var(--color-tfps11-ink) 75%, transparent);
  }
}

@utility tfps11-spy {
  @supports (animation-timeline: view()) {
    animation: tfps11-spy linear both;
    animation-timeline: var(--tl);
    animation-range: cover 0% cover 100%;
  }
}
```
