---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-screen-portfolio-gallery-scroll-sections/"
title: "Tailwind Full Screen Portfolio Gallery Scroll Sections"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "Five full-viewport panels, one project each: a full-bleed photograph that settles from 108% to 100% as its panel arrives, an Instrument Serif project title,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full Screen Portfolio Gallery Scroll Sections
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-screen-portfolio-gallery-scroll-sections/

Five full-viewport panels, one project each: a full-bleed photograph that settles from 108% to 100% as its panel arrives, an Instrument Serif project title, and role / year / sector chips in frosted monospace. object-cover with per-image object-[50%_40%] keeps every photo undistorted and well-framed, and the next panel's rounded edge always shows so the reader knows there's more work below.
## HTML
```html
<div class="tfps-10 relative isolate w-full min-h-svh bg-tfps10-bg font-tfps10-sans text-tfps10-ink antialiased [&_code]:font-tfps10-mono [&_code]:text-[.92em] text-white">
  <input class="peer sr-only" type="checkbox" id="tfps-10-theme">
  <label for="tfps-10-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-white/25 bg-black/30 text-white hover:bg-black/45 shadow-[0_8px_24px_-12px_var(--color-tfps10-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-white forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps10-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps10-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Dim the photographs</span>
  </label>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Selected work, five projects">

    <section class="[view-timeline-name:--tfps10] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[#141418] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,6vh,4rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-10-s1" aria-labelledby="tfps-10-h1">
      <img class="tfps10-settle absolute inset-0 -z-20 size-full rounded-[inherit] object-cover object-[50%_46%] transition-opacity duration-300 tfps10-dark:opacity-60" src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&amp;auto=format" alt="Sunlit minimalist living space with pale timber flooring" width="1600" height="1067" loading="eager" fetchpriority="high" decoding="async">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[inherit] bg-linear-to-t from-black/90 via-black/45 via-35% to-black/25"></span>
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] gap-[clamp(.6rem,1.5vh,.95rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px] font-tfps10-mono text-[.7rem] tracking-[.14em] uppercase text-white/85">Selected work &mdash; Maya Okonkwo</p>
        <p class="font-tfps10-mono text-[.8rem] tracking-[.1em] tabular-nums text-white/75"><span class="text-base text-white">01</span> / 05</p>
        <h2 class="font-tfps10-serif text-[clamp(2.9rem,10vw,7.5rem)] leading-[.92] font-normal tracking-[-.02em] text-balance [text-shadow:0_2px_40px_rgb(0_0_0/.5)]" id="tfps-10-h1">Nordhavn Interiors</h2>
        <ul class="flex flex-wrap items-center gap-x-2.5 gap-y-2 font-tfps10-mono text-[.77rem] text-white/85"><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Art direction &amp; web</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">2026</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Retail</li></ul>
        <p class="max-w-[48ch] text-[clamp(.97rem,1.3vw,1.1rem)] leading-[1.55] text-pretty text-white/85 [text-shadow:0_1px_16px_rgb(0_0_0/.6)]">A 340-page catalogue reduced to eleven full-screen rooms. Bounce rate fell 22% in the first month.</p>
        <a href="#tfps-10-s2" class="inline-flex min-h-11 items-center gap-2.5 rounded-full pe-3 font-tfps10-mono text-[.78rem] text-white/85 no-underline transition-colors hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"><svg class="size-4 animate-tfps10-bob motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Four more below</a>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps10] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[#141418] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,6vh,4rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-10-s2" aria-labelledby="tfps-10-h2">
      <img class="tfps10-settle absolute inset-0 -z-20 size-full rounded-[inherit] object-cover object-[50%_40%] transition-opacity duration-300 tfps10-dark:opacity-60" src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=1600&amp;auto=format" alt="Empty open-plan studio office with glass partitions" width="1600" height="1067" loading="lazy" decoding="async">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[inherit] bg-linear-to-t from-black/90 via-black/45 via-35% to-black/25"></span>
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] gap-[clamp(.6rem,1.5vh,.95rem)]">
        <p class="font-tfps10-mono text-[.8rem] tracking-[.1em] tabular-nums text-white/75"><span class="text-base text-white">02</span> / 05</p>
        <h2 class="font-tfps10-serif text-[clamp(2.9rem,10vw,7.5rem)] leading-[.92] font-normal tracking-[-.02em] text-balance [text-shadow:0_2px_40px_rgb(0_0_0/.5)]" id="tfps-10-h2">Fold Workspace</h2>
        <ul class="flex flex-wrap items-center gap-x-2.5 gap-y-2 font-tfps10-mono text-[.77rem] text-white/85"><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Product design</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">2026</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">SaaS</li></ul>
        <p class="max-w-[48ch] text-[clamp(.97rem,1.3vw,1.1rem)] leading-[1.55] text-pretty text-white/85 [text-shadow:0_1px_16px_rgb(0_0_0/.6)]">Desk booking for hybrid teams. Shipped the floor-plan picker in six weeks with two engineers.</p>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps10] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[#141418] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,6vh,4rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-10-s3" aria-labelledby="tfps-10-h3">
      <img class="tfps10-settle absolute inset-0 -z-20 size-full rounded-[inherit] object-cover object-[50%_52%] transition-opacity duration-300 tfps10-dark:opacity-60" src="https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=1600&amp;auto=format" alt="Low lounge seating beside a dark panelled wall" width="1600" height="1067" loading="lazy" decoding="async">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[inherit] bg-linear-to-t from-black/90 via-black/45 via-35% to-black/25"></span>
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] gap-[clamp(.6rem,1.5vh,.95rem)]">
        <p class="font-tfps10-mono text-[.8rem] tracking-[.1em] tabular-nums text-white/75"><span class="text-base text-white">03</span> / 05</p>
        <h2 class="font-tfps10-serif text-[clamp(2.9rem,10vw,7.5rem)] leading-[.92] font-normal tracking-[-.02em] text-balance [text-shadow:0_2px_40px_rgb(0_0_0/.5)]" id="tfps-10-h3">Ashgrove Hotel</h2>
        <ul class="flex flex-wrap items-center gap-x-2.5 gap-y-2 font-tfps10-mono text-[.77rem] text-white/85"><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Identity &amp; booking flow</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">2025</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Hospitality</li></ul>
        <p class="max-w-[48ch] text-[clamp(.97rem,1.3vw,1.1rem)] leading-[1.55] text-pretty text-white/85 [text-shadow:0_1px_16px_rgb(0_0_0/.6)]">One-screen-per-room booking. Direct reservations up 31% against the previous template.</p>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps10] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[#141418] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,6vh,4rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-10-s4" aria-labelledby="tfps-10-h4">
      <img class="tfps10-settle absolute inset-0 -z-20 size-full rounded-[inherit] object-cover object-[50%_38%] transition-opacity duration-300 tfps10-dark:opacity-60" src="https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=1600&amp;auto=format" alt="Four colleagues reviewing work around a meeting table" width="1600" height="1067" loading="lazy" decoding="async">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[inherit] bg-linear-to-t from-black/90 via-black/45 via-35% to-black/25"></span>
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] gap-[clamp(.6rem,1.5vh,.95rem)]">
        <p class="font-tfps10-mono text-[.8rem] tracking-[.1em] tabular-nums text-white/75"><span class="text-base text-white">04</span> / 05</p>
        <h2 class="font-tfps10-serif text-[clamp(2.9rem,10vw,7.5rem)] leading-[.92] font-normal tracking-[-.02em] text-balance [text-shadow:0_2px_40px_rgb(0_0_0/.5)]" id="tfps-10-h4">Quorum Research</h2>
        <ul class="flex flex-wrap items-center gap-x-2.5 gap-y-2 font-tfps10-mono text-[.77rem] text-white/85"><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Design system</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">2025</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Civic</li></ul>
        <p class="max-w-[48ch] text-[clamp(.97rem,1.3vw,1.1rem)] leading-[1.55] text-pretty text-white/85 [text-shadow:0_1px_16px_rgb(0_0_0/.6)]">Forty-one components, one accessibility audit, zero contrast failures at hand-off.</p>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps10] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[#141418] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,6vh,4rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-10-s5" aria-labelledby="tfps-10-h5">
      <img class="tfps10-settle absolute inset-0 -z-20 size-full rounded-[inherit] object-cover object-[50%_44%] transition-opacity duration-300 tfps10-dark:opacity-60" src="https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=1600&amp;auto=format" alt="Laptop on a desk lit by saturated pink and blue light" width="1600" height="1067" loading="lazy" decoding="async">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[inherit] bg-linear-to-t from-black/90 via-black/45 via-35% to-black/25"></span>
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] gap-[clamp(.6rem,1.5vh,.95rem)]">
        <p class="font-tfps10-mono text-[.8rem] tracking-[.1em] tabular-nums text-white/75"><span class="text-base text-white">05</span> / 05</p>
        <h2 class="font-tfps10-serif text-[clamp(2.9rem,10vw,7.5rem)] leading-[.92] font-normal tracking-[-.02em] text-balance [text-shadow:0_2px_40px_rgb(0_0_0/.5)]" id="tfps-10-h5">Halcyon Player</h2>
        <ul class="flex flex-wrap items-center gap-x-2.5 gap-y-2 font-tfps10-mono text-[.77rem] text-white/85"><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Interaction design</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">2024</li><li class="rounded-[.45rem] border border-white/25 bg-black/25 px-2.5 py-1 backdrop-blur-[6px]">Audio</li></ul>
        <p class="max-w-[48ch] text-[clamp(.97rem,1.3vw,1.1rem)] leading-[1.55] text-pretty text-white/85 [text-shadow:0_1px_16px_rgb(0_0_0/.6)]">A listening app with one control. Retention at day 30 doubled after the redesign.</p>
        <a class="mt-1.5 inline-flex min-h-11 items-center gap-2 rounded-full border border-white/25 bg-black/30 px-[1.15rem] py-3 text-[.9rem] text-white no-underline backdrop-blur-[8px] transition-colors hover:bg-black/55 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white" href="#tfps-10-s1"><svg class="size-4 -rotate-90" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h13.5M12.6 6.5 18.2 12l-5.6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Back to the first project</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps10-bg: #0a0a0c;
  --color-tfps10-bg: oklch(0.146 0.004 285.9);
  --color-tfps10-ink: #ffffff;
  --color-tfps10-ink: oklch(1 0 0);
  --color-tfps10-acc: #ffffff;
  --color-tfps10-acc: oklch(1 0 0);
  --color-tfps10-shade: rgb(0 0 0 / .5);
  --font-tfps10-serif: 'Instrument Serif', ui-serif, Georgia, 'Times New Roman', serif;
  --font-tfps10-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps10-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --animate-tfps10-bob: tfps10-bob 2.4s ease-in-out infinite;

  @keyframes tfps10-bob {
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

@custom-variant tfps10-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-10:has(#tfps-10-theme:checked), .tfps-10:has(#tfps-10-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-10:not(:has(#tfps-10-theme:checked)), .tfps-10:not(:has(#tfps-10-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles, photographic, so dark by nature: the toggle dims the photos. */

.tfps-10 {
  width: 100%;
  min-height: 100svh;
}
/* What stayed CSS: the photograph settles from 108% to 100% as its panel arrives. */

@keyframes tfps10-settle {
  from {
    scale: 1.08;
  }

  to {
    scale: 1;
  }
}

@utility tfps10-settle {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps10-settle linear both;
      animation-timeline: --tfps10;
      animation-range: entry 0% cover 50%;
    }
  }
}
```
