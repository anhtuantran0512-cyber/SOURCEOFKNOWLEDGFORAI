---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-scroll-snap-full-screen-sections-with-100dvh/"
title: "Tailwind Scroll Snap Full Screen Sections with 100dvh"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "The reference build for the collection, ported whole into utilities: four snapping full-viewport panels sized with min-h-dvh, one owned snap-y snap-mandatory…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll Snap Full Screen Sections with 100dvh
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-scroll-snap-full-screen-sections-with-100dvh/

The reference build for the collection, ported whole into utilities: four snapping full-viewport panels sized with min-h-dvh, one owned snap-y snap-mandatory scrollport, and a fourth panel deliberately built on min-h-screen so you can see the iOS bug it causes. A device diagram shows what the collapsing address bar does to vh, and a table settles dvh vs svh vs lvh in Tailwind's own vocabulary. Zero JavaScript.
## HTML
```html
<div class="tfps-01 relative isolate w-full min-h-svh bg-tfps01-bg font-tfps01-sans text-tfps01-ink antialiased [&_code]:font-tfps01-mono [&_code]:text-[.92em]">
  <input class="peer sr-only" type="checkbox" id="tfps-01-theme">
  <label for="tfps-01-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps01-ink/10 bg-white/60 text-tfps01-ink hover:bg-white/85 tfps01-dark:bg-white/[.07] tfps01-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps01-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps01-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps01-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps01-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps01-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Full viewport section scroller, four panels">

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps01-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.75rem)] pb-[calc(clamp(2rem,5vh,3.75rem)+4.5rem)] even:bg-tfps01-panel2 not-first:-mt-18 not-first:rounded-t-[2rem] not-first:border-t not-first:border-tfps01-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps01-shade)] forced-colors:border-[CanvasText]" id="tfps-01-s1" aria-labelledby="tfps-01-h1">
      <div class="grid w-full max-w-[64rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps01-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps01-acc">01 / 04</span><span class="rounded-[.45rem] border border-tfps01-ink/12 px-2 py-[.22rem] font-tfps01-mono text-[.7rem] text-tfps01-ink/75">min-h-dvh</span></p>
        <h2 class="max-w-[22ch] text-[clamp(2.1rem,6.2vw,4.5rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-01-h1">Panels that fill the screen &mdash; and keep filling it</h2>
        <p class="max-w-[56ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps01-ink/75 [&_code]:text-tfps01-ink">Four snapping sections, one owned scroll container, zero JavaScript. Every panel is exactly as tall as the visible viewport, so the snap position never drifts when a mobile toolbar slides away.</p>
        <ul class="flex flex-wrap gap-2.5">
          <li class="grid gap-0.5 rounded-[.85rem] border px-3.5 py-2.5 font-tfps01-mono text-[.9rem] border-tfps01-acc bg-tfps01-acc/8 text-tfps01-acc">h-dvh<span class="font-tfps01-sans text-[.74rem] text-tfps01-acc">tracks the live viewport</span></li>
          <li class="grid gap-0.5 rounded-[.85rem] border px-3.5 py-2.5 font-tfps01-mono text-[.9rem] border-tfps01-ink/10 bg-tfps01-ink/[.03]">h-svh<span class="font-tfps01-sans text-[.74rem] text-tfps01-ink/70">toolbars shown</span></li>
          <li class="grid gap-0.5 rounded-[.85rem] border px-3.5 py-2.5 font-tfps01-mono text-[.9rem] border-tfps01-ink/10 bg-tfps01-ink/[.03]">h-lvh<span class="font-tfps01-sans text-[.74rem] text-tfps01-ink/70">toolbars hidden</span></li>
        </ul>
        <a href="#tfps-01-s2" class="inline-flex min-h-11 items-center gap-2.5 rounded-full pe-3 font-tfps01-mono text-[.82rem] text-tfps01-ink/75 no-underline transition-colors hover:text-tfps01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps01-acc"><svg class="size-[1.1rem] animate-tfps01-bob motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll &mdash; the next panel&rsquo;s edge is already showing</a>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps01-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.75rem)] pb-[calc(clamp(2rem,5vh,3.75rem)+4.5rem)] even:bg-tfps01-panel2 not-first:-mt-18 not-first:rounded-t-[2rem] not-first:border-t not-first:border-tfps01-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps01-shade)] forced-colors:border-[CanvasText]" id="tfps-01-s2" aria-labelledby="tfps-01-h2">
      <div class="grid w-full max-w-[64rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps01-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps01-acc">02 / 04</span><span class="rounded-[.45rem] border border-tfps01-ink/12 px-2 py-[.22rem] font-tfps01-mono text-[.7rem] text-tfps01-ink/75">the address-bar problem</span></p>
        <h2 class="max-w-[26ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-01-h2">What the collapsing toolbar actually does</h2>
        <div class="grid w-full grid-cols-[repeat(auto-fit,minmax(15rem,1fr))] gap-[clamp(1rem,3vw,2rem)]">
          <figure class="grid gap-3.5">
            <div class="relative grid h-[clamp(11rem,26vh,16rem)] grid-rows-[auto_1fr] overflow-hidden rounded-[1.4rem] border border-tfps01-ink/10 bg-tfps01-panel shadow-[0_22px_44px_-28px_var(--color-tfps01-shade)] forced-colors:border-[CanvasText]">
              <span class="border-b border-tfps01-ink/10 bg-tfps01-ink/[.04] px-3 py-2 font-tfps01-mono text-[.62rem] text-tfps01-ink/70">codefronts.com</span>
              <div class="grid h-[calc(100%+2.4rem)] place-items-center pb-16 border-t-2 border-tfps01-warn bg-tfps01-warn/10 bg-[repeating-linear-gradient(135deg,color-mix(in_oklab,var(--color-tfps01-warn)_14%,transparent)_0_10px,transparent_10px_20px)] font-tfps01-mono text-[1.1rem] font-medium text-tfps01-warn"><span>100vh</span></div>
              <span aria-hidden="true" class="absolute inset-x-0 bottom-0 flex h-7 items-center justify-around border-t border-tfps01-ink/10 bg-tfps01-panel/80 backdrop-blur-sm"><i class="size-1.5 rounded-full bg-tfps01-ink/30"></i><i class="size-1.5 rounded-full bg-tfps01-ink/30"></i><i class="size-1.5 rounded-full bg-tfps01-ink/30"></i></span>
              <span class="absolute inset-x-0 bottom-7 bg-tfps01-warn px-3 py-1.5 text-center font-tfps01-mono text-[.62rem] text-white tfps01-dark:text-[#1c1305]">bottom 96px under the toolbar</span>
            </div>
            <figcaption class="text-[.88rem] leading-[1.5] text-pretty text-tfps01-ink/75">Legacy <code>100vh</code> (Tailwind&rsquo;s <code>h-screen</code>) resolves against the <em>large</em> viewport. The panel is taller than the screen from the first paint.</figcaption>
          </figure>
          <figure class="grid gap-3.5">
            <div class="relative grid h-[clamp(11rem,26vh,16rem)] grid-rows-[auto_1fr] overflow-hidden rounded-[1.4rem] border border-tfps01-ink/10 bg-tfps01-panel shadow-[0_22px_44px_-28px_var(--color-tfps01-shade)] forced-colors:border-[CanvasText]">
              <span class="border-b border-tfps01-ink/10 bg-tfps01-ink/[.04] px-3 py-2 font-tfps01-mono text-[.62rem] text-tfps01-ink/70">codefronts.com</span>
              <div class="mb-7 grid place-items-center border-t-2 border-tfps01-acc bg-tfps01-acc/12 font-tfps01-mono text-[1.1rem] font-medium text-tfps01-acc"><span>100dvh</span></div>
              <span aria-hidden="true" class="absolute inset-x-0 bottom-0 flex h-7 items-center justify-around border-t border-tfps01-ink/10 bg-tfps01-panel/80 backdrop-blur-sm"><i class="size-1.5 rounded-full bg-tfps01-ink/30"></i><i class="size-1.5 rounded-full bg-tfps01-ink/30"></i><i class="size-1.5 rounded-full bg-tfps01-ink/30"></i></span>
              
            </div>
            <figcaption class="text-[.88rem] leading-[1.5] text-pretty text-tfps01-ink/75"><code>h-dvh</code> measures what the user can see right now, and re-measures as the browser chrome moves.</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps01-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.75rem)] pb-[calc(clamp(2rem,5vh,3.75rem)+4.5rem)] even:bg-tfps01-panel2 not-first:-mt-18 not-first:rounded-t-[2rem] not-first:border-t not-first:border-tfps01-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps01-shade)] forced-colors:border-[CanvasText]" id="tfps-01-s3" aria-labelledby="tfps-01-h3">
      <div class="grid w-full max-w-[64rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps01-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps01-acc">03 / 04</span><span class="rounded-[.45rem] border border-tfps01-ink/12 px-2 py-[.22rem] font-tfps01-mono text-[.7rem] text-tfps01-ink/75">unit reference</span></p>
        <h2 class="max-w-[26ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-01-h3">Which viewport utility, and when</h2>
        <dl class="grid w-full gap-1">
          <div class="grid grid-cols-[minmax(5.5rem,7rem)_1fr] items-start gap-[clamp(.75rem,2vw,1.75rem)] border-t border-tfps01-ink/10 py-[clamp(.8rem,1.6vh,1.1rem)]"><dt class="font-tfps01-mono text-[.95rem] text-tfps01-acc">min-h-dvh</dt><dd class="text-[.98rem] leading-[1.55] text-pretty text-tfps01-ink/75"><strong class="font-semibold text-tfps01-ink">Snapping panels.</strong> Height follows the live viewport, so panel height and scrollport height stay equal while toolbars animate.</dd></div>
          <div class="grid grid-cols-[minmax(5.5rem,7rem)_1fr] items-start gap-[clamp(.75rem,2vw,1.75rem)] border-t border-tfps01-ink/10 py-[clamp(.8rem,1.6vh,1.1rem)]"><dt class="font-tfps01-mono text-[.95rem] text-tfps01-acc">min-h-svh</dt><dd class="text-[.98rem] leading-[1.55] text-pretty text-tfps01-ink/75"><strong class="font-semibold text-tfps01-ink">Panels with pinned bottom chrome.</strong> Always the short measurement, so a sticky action bar is never swallowed by the browser UI.</dd></div>
          <div class="grid grid-cols-[minmax(5.5rem,7rem)_1fr] items-start gap-[clamp(.75rem,2vw,1.75rem)] border-t border-tfps01-ink/10 py-[clamp(.8rem,1.6vh,1.1rem)]"><dt class="font-tfps01-mono text-[.95rem] text-tfps01-acc">min-h-lvh</dt><dd class="text-[.98rem] leading-[1.55] text-pretty text-tfps01-ink/75"><strong class="font-semibold text-tfps01-ink">Decorative full-bleed art.</strong> Intentionally taller than the screen; fine for a background image, wrong for a snap target.</dd></div>
          <div class="grid grid-cols-[minmax(5.5rem,7rem)_1fr] items-start gap-[clamp(.75rem,2vw,1.75rem)] border-t border-tfps01-ink/10 py-[clamp(.8rem,1.6vh,1.1rem)]"><dt class="font-tfps01-mono text-[.95rem] text-tfps01-warn">min-h-screen</dt><dd class="text-[.98rem] leading-[1.55] text-pretty text-tfps01-ink/75"><strong class="font-semibold text-tfps01-ink">Legacy <code>100vh</code>.</strong> Identical to <code>lvh</code>. Every browser that runs Tailwind v4 understands <code>dvh</code>, so there is no fallback left to write.</dd></div>
        </dl>
      </div>
    </section>

    <section class="relative flex min-h-screen snap-start items-center justify-center bg-[color-mix(in_oklab,var(--color-tfps01-warn)_9%,var(--color-tfps01-panel))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.75rem)] pb-[calc(clamp(2rem,5vh,3.75rem)+4.5rem)] not-first:-mt-18 not-first:rounded-t-[2rem] not-first:border-t not-first:border-tfps01-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps01-shade)] forced-colors:border-[CanvasText]" id="tfps-01-s4" aria-labelledby="tfps-01-h4">
      <div class="grid w-full max-w-[64rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps01-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps01-acc">04 / 04</span><span class="rounded-[.45rem] border border-tfps01-warn/40 px-2 py-[.22rem] font-tfps01-mono text-[.7rem] text-tfps01-warn">min-h-screen &middot; labelled comparison</span></p>
        <h2 class="max-w-[26ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-01-h4">This panel is the broken one</h2>
        <p class="max-w-[56ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps01-ink/75 [&_code]:text-tfps01-ink">It is the only panel in the collection sized with <code>min-h-screen</code> (<code>100vh</code>). On a desktop it looks identical. Open the demo on an iPhone and this panel overshoots the screen: its footer line hides behind the address bar, and the snap edge lands mid-sentence.</p>
        <p class="w-full border-t border-dashed border-tfps01-warn/45 pt-2.5 font-tfps01-mono text-[.8rem] text-tfps01-warn">Bottom line of panel 04 &mdash; visible here, hidden on iOS Safari.</p>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps01-bg: #f7f8fa;
  --color-tfps01-bg: oklch(0.979 0.003 264.5);
  --color-tfps01-panel: #ffffff;
  --color-tfps01-panel: oklch(1 0 0);
  --color-tfps01-panel2: #eef1f6;
  --color-tfps01-panel2: oklch(0.957 0.007 260.7);
  --color-tfps01-ink: #0c0e14;
  --color-tfps01-ink: oklch(16% .015 265);
  --color-tfps01-acc: #2563eb;
  --color-tfps01-acc: oklch(58% .19 258);
  --color-tfps01-warn: #b45309;
  --color-tfps01-warn: oklch(56% .13 62);
  --color-tfps01-shade: rgb(12 14 20 / .2);
  --font-tfps01-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps01-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --animate-tfps01-bob: tfps01-bob 2.4s ease-in-out infinite;

  @keyframes tfps01-bob {
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

@custom-variant tfps01-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-01:has(#tfps-01-theme:checked), .tfps-01:has(#tfps-01-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-01:not(:has(#tfps-01-theme:checked)), .tfps-01:not(:has(#tfps-01-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-01 {
  width: 100%;
  min-height: 100svh;

  @variant tfps01-dark {
    --color-tfps01-bg: #07080b;
    --color-tfps01-bg: oklch(0.135 0.007 269);
    --color-tfps01-panel: #0b0d12;
    --color-tfps01-panel: oklch(0.159 0.011 268);
    --color-tfps01-panel2: #11141b;
    --color-tfps01-panel2: oklch(0.191 0.015 266.8);
    --color-tfps01-ink: #f2f4f9;
    --color-tfps01-ink: oklch(0.967 0.007 268.5);
    --color-tfps01-acc: #7dd3fc;
    --color-tfps01-acc: oklch(0.828 0.101 230.3);
    --color-tfps01-warn: #fbbf24;
    --color-tfps01-warn: oklch(0.837 0.164 84.4);
    --color-tfps01-shade: rgb(0 0 0 / .7);
  }
}
```
