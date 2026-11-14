---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/animated-tailwind-pagination-with-sliding-active-indicator/"
title: "Animated Tailwind Pagination with Sliding Active Indicator"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "One aurora pill that glides between pages instead of five backgrounds blinking on and off — its indigo → pink → orange gradient pans as it travels, and the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Tailwind Pagination with Sliding Active Indicator
Source: https://codefronts.com/navigation/tailwind-css-pagination/animated-tailwind-pagination-with-sliding-active-indicator/

One aurora pill that glides between pages instead of five backgrounds blinking on and off — its indigo → pink → orange gradient pans as it travels, and the results panel slides with it. A native radio group gives arrow-key traversal for free; has-[#tpg-14-p3:checked]:[--tpg14-i:2] on the root writes the page index into one custom property, and the pill, the results strip, the edge controls and the readout all read it. Zero JavaScript.
## HTML
```html
<section class="tpg-14 group/tpg14 w-full min-h-svh grid place-items-center bg-tpg14-bg bg-[radial-gradient(45%_40%_at_15%_10%,var(--color-tpg14-glow1),transparent_70%),radial-gradient(40%_40%_at_90%_15%,var(--color-tpg14-glow2),transparent_70%),radial-gradient(50%_40%_at_50%_100%,var(--color-tpg14-glow3),transparent_70%)] px-5 py-14 font-tpg14-sans text-tpg14-ink antialiased [--tpg14-i:0] has-[#tpg-14-p2:checked]:[--tpg14-i:1] has-[#tpg-14-p3:checked]:[--tpg14-i:2] has-[#tpg-14-p4:checked]:[--tpg14-i:3] has-[#tpg-14-p5:checked]:[--tpg14-i:4]" aria-label="Animated pagination with sliding active indicator demo">
  <div class="grid w-full max-w-[36rem] justify-items-center gap-8">
    <div class="w-full overflow-hidden rounded-3xl bg-tpg14-card shadow-tpg14-card ring-1 ring-tpg14-line">
      <header class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1 border-b border-tpg14-line px-5 pt-5 pb-4 sm:px-6">
        <h2 class="text-[19px] font-semibold tracking-[-0.02em]">Results for <span class="bg-linear-to-r from-tpg14-a via-tpg14-b to-tpg14-c bg-clip-text text-transparent">&ldquo;color&rdquo;</span></h2>
        <p class="font-tpg14-mono text-xs text-tpg14-mut tabular-nums">15 docs &middot; 0.04s</p>
      </header>
      <div class="overflow-hidden">
        <div class="flex translate-x-[calc(var(--tpg14-i)*-100%)] transition-[translate] duration-500 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
            <ol role="list" aria-label="Results 1 to 3" class="invisible w-full flex-none divide-y divide-tpg14-line px-5 transition-[visibility] duration-500 group-has-[#tpg-14-p1:checked]/tpg14:visible sm:px-6">
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / oklch</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">oklch() and the OKLCH colour space</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Perceptually even lightness, so a 10% step looks like 10% on every hue.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / color-mix</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">color-mix() in practice</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Blend two colours in any space; the engine behind every opacity modifier.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / relative</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">Relative colour syntax</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Derive hover and border shades from one token with oklch(from &hellip;).</p></li>
            </ol>
            <ol role="list" aria-label="Results 4 to 6" class="invisible w-full flex-none divide-y divide-tpg14-line px-5 transition-[visibility] duration-500 group-has-[#tpg-14-p2:checked]/tpg14:visible sm:px-6">
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / at-rules / property</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">Registering colours with @property</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Typed custom properties make gradients and tokens animatable.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / light-dark</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">light-dark() for two-theme tokens</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">One declaration per token, resolved by the inherited color-scheme.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / ui / accent-color</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">accent-color for native controls</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Brand checkboxes, radios and range inputs without rebuilding them.</p></li>
            </ol>
            <ol role="list" aria-label="Results 7 to 9" class="invisible w-full flex-none divide-y divide-tpg14-line px-5 transition-[visibility] duration-500 group-has-[#tpg-14-p3:checked]/tpg14:visible sm:px-6">
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / currentcolor</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">currentColor and inheritance</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Let icons and borders follow text colour through every state.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / a11y / forced-colors</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">forced-color-adjust and High Contrast</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">What survives Windows High Contrast, and what you must redraw.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / ui / color-scheme</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">color-scheme and form controls</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Opt native scrollbars and inputs into dark mode in one line.</p></li>
            </ol>
            <ol role="list" aria-label="Results 10 to 12" class="invisible w-full flex-none divide-y divide-tpg14-line px-5 transition-[visibility] duration-500 group-has-[#tpg-14-p4:checked]/tpg14:visible sm:px-6">
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / gamut</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">Designing for Display P3</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Wider-gamut accents with an sRGB fallback that still passes contrast.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / contrast-color</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">contrast-color() is arriving</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Pick black or white text against any background, automatically.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / a11y / prefers-contrast</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">prefers-contrast media feature</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">Thicker borders and stronger ink when the user asks for more.</p></li>
            </ol>
            <ol role="list" aria-label="Results 13 to 15" class="invisible w-full flex-none divide-y divide-tpg14-line px-5 transition-[visibility] duration-500 group-has-[#tpg-14-p5:checked]/tpg14:visible sm:px-6">
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / system</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">System colours: Canvas, LinkText</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">The palette the OS hands you, and when to lean on it.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / interpolation</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">Colour interpolation in gradients</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">in oklch avoids the grey dead zone in the middle of a blend.</p></li>
              <li class="grid gap-1 py-3.5"><p class="font-tpg14-mono text-[11.5px] text-tpg14-a">css / color / named</p><p class="text-[15.5px] font-semibold tracking-[-0.01em]">Named colours, ranked</p><p class="text-[13.5px] leading-relaxed text-tpg14-mut text-pretty">All 148 keywords, and the eleven worth actually using.</p></li>
            </ol>
        </div>
      </div>
      <nav class="@container border-t border-tpg14-line bg-tpg14-foot px-2 py-3 sm:px-4" aria-label="Pagination">
        <div class="flex items-center justify-between gap-1 sm:gap-2">
          <div class="flex justify-start">
            <span aria-hidden="true" class="hidden min-h-11 min-w-11 items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium text-tpg14-mut opacity-50 group-has-[#tpg-14-p1:checked]/tpg14:inline-flex @max-[26rem]:px-0"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[26rem]:sr-only">Prev</span></span>
            <label for="tpg-14-p1" aria-hidden="true" class="hidden min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium @max-[26rem]:px-0 text-tpg14-ink transition-colors hover:bg-tpg14-b/10 hover:text-tpg14-b group-has-[#tpg-14-p2:checked]/tpg14:inline-flex"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[26rem]:sr-only">Prev</span></label>
            <label for="tpg-14-p2" aria-hidden="true" class="hidden min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium @max-[26rem]:px-0 text-tpg14-ink transition-colors hover:bg-tpg14-b/10 hover:text-tpg14-b group-has-[#tpg-14-p3:checked]/tpg14:inline-flex"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[26rem]:sr-only">Prev</span></label>
            <label for="tpg-14-p3" aria-hidden="true" class="hidden min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium @max-[26rem]:px-0 text-tpg14-ink transition-colors hover:bg-tpg14-b/10 hover:text-tpg14-b group-has-[#tpg-14-p4:checked]/tpg14:inline-flex"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[26rem]:sr-only">Prev</span></label>
            <label for="tpg-14-p4" aria-hidden="true" class="hidden min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium @max-[26rem]:px-0 text-tpg14-ink transition-colors hover:bg-tpg14-b/10 hover:text-tpg14-b group-has-[#tpg-14-p5:checked]/tpg14:inline-flex"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[26rem]:sr-only">Prev</span></label>
          </div>
          <div class="relative grid grid-flow-col auto-cols-(--tpg14-w) rounded-full bg-tpg14-track p-1 shadow-tpg14-track ring-1 ring-tpg14-a/15 [--tpg14-w:3rem] @max-[22rem]:[--tpg14-w:2.75rem]" role="radiogroup" aria-label="Choose a page">
            <span aria-hidden="true" class="absolute inset-y-1 left-1 w-(--tpg14-w) translate-x-[calc(var(--tpg14-i)*var(--tpg14-w))] rounded-full bg-linear-to-r from-tpg14-a via-tpg14-b to-tpg14-c bg-size-[300%_100%] bg-position-[calc(var(--tpg14-i)*25%)_0] opacity-70 blur-md transition-[translate,background-position] duration-500 ease-[cubic-bezier(.34,1.4,.5,1)] motion-reduce:transition-none"></span>
            <span aria-hidden="true" class="absolute inset-y-1 left-1 w-(--tpg14-w) translate-x-[calc(var(--tpg14-i)*var(--tpg14-w))] rounded-full bg-linear-to-r from-tpg14-a via-tpg14-b to-tpg14-c bg-size-[300%_100%] bg-position-[calc(var(--tpg14-i)*25%)_0] shadow-tpg14-pill transition-[translate,background-position] duration-500 ease-[cubic-bezier(.34,1.4,.5,1)] motion-reduce:transition-none"></span>
          <input class="peer/p1 sr-only" type="radio" name="tpg-14-page" id="tpg-14-p1" aria-label="Page 1">
          <label for="tpg-14-p1" class="relative z-10 grid h-11 cursor-pointer place-items-center rounded-full text-[15px] font-medium tabular-nums text-tpg14-mut transition-[color,background-color] duration-300 peer-not-checked/p1:hover:bg-tpg14-a/8 peer-not-checked/p1:hover:text-tpg14-a peer-checked/p1:text-tpg14-on-acc peer-focus-visible/p1:outline-2 peer-focus-visible/p1:outline-offset-2 peer-focus-visible/p1:outline-tpg14-ring">1</label>
          <input class="peer/p2 sr-only" type="radio" name="tpg-14-page" id="tpg-14-p2" aria-label="Page 2">
          <label for="tpg-14-p2" class="relative z-10 grid h-11 cursor-pointer place-items-center rounded-full text-[15px] font-medium tabular-nums text-tpg14-mut transition-[color,background-color] duration-300 peer-not-checked/p2:hover:bg-tpg14-a/8 peer-not-checked/p2:hover:text-tpg14-a peer-checked/p2:text-tpg14-on-acc peer-focus-visible/p2:outline-2 peer-focus-visible/p2:outline-offset-2 peer-focus-visible/p2:outline-tpg14-ring">2</label>
          <input class="peer/p3 sr-only" type="radio" name="tpg-14-page" id="tpg-14-p3" aria-label="Page 3" checked>
          <label for="tpg-14-p3" class="relative z-10 grid h-11 cursor-pointer place-items-center rounded-full text-[15px] font-medium tabular-nums text-tpg14-mut transition-[color,background-color] duration-300 peer-not-checked/p3:hover:bg-tpg14-a/8 peer-not-checked/p3:hover:text-tpg14-a peer-checked/p3:text-tpg14-on-acc peer-focus-visible/p3:outline-2 peer-focus-visible/p3:outline-offset-2 peer-focus-visible/p3:outline-tpg14-ring">3</label>
          <input class="peer/p4 sr-only" type="radio" name="tpg-14-page" id="tpg-14-p4" aria-label="Page 4">
          <label for="tpg-14-p4" class="relative z-10 grid h-11 cursor-pointer place-items-center rounded-full text-[15px] font-medium tabular-nums text-tpg14-mut transition-[color,background-color] duration-300 peer-not-checked/p4:hover:bg-tpg14-a/8 peer-not-checked/p4:hover:text-tpg14-a peer-checked/p4:text-tpg14-on-acc peer-focus-visible/p4:outline-2 peer-focus-visible/p4:outline-offset-2 peer-focus-visible/p4:outline-tpg14-ring">4</label>
          <input class="peer/p5 sr-only" type="radio" name="tpg-14-page" id="tpg-14-p5" aria-label="Page 5">
          <label for="tpg-14-p5" class="relative z-10 grid h-11 cursor-pointer place-items-center rounded-full text-[15px] font-medium tabular-nums text-tpg14-mut transition-[color,background-color] duration-300 peer-not-checked/p5:hover:bg-tpg14-a/8 peer-not-checked/p5:hover:text-tpg14-a peer-checked/p5:text-tpg14-on-acc peer-focus-visible/p5:outline-2 peer-focus-visible/p5:outline-offset-2 peer-focus-visible/p5:outline-tpg14-ring">5</label>
          </div>
          <div class="flex justify-end">
            <label for="tpg-14-p2" aria-hidden="true" class="hidden min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium @max-[26rem]:px-0 text-tpg14-ink transition-colors hover:bg-tpg14-b/10 hover:text-tpg14-b group-has-[#tpg-14-p1:checked]/tpg14:inline-flex"><span class="@max-[26rem]:sr-only">Next</span><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 3.5 10.5 8 6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></label>
            <label for="tpg-14-p3" aria-hidden="true" class="hidden min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium @max-[26rem]:px-0 text-tpg14-ink transition-colors hover:bg-tpg14-b/10 hover:text-tpg14-b group-has-[#tpg-14-p2:checked]/tpg14:inline-flex"><span class="@max-[26rem]:sr-only">Next</span><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 3.5 10.5 8 6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></label>
            <label for="tpg-14-p4" aria-hidden="true" class="hidden min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium @max-[26rem]:px-0 text-tpg14-ink transition-colors hover:bg-tpg14-b/10 hover:text-tpg14-b group-has-[#tpg-14-p3:checked]/tpg14:inline-flex"><span class="@max-[26rem]:sr-only">Next</span><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 3.5 10.5 8 6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></label>
            <label for="tpg-14-p5" aria-hidden="true" class="hidden min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium @max-[26rem]:px-0 text-tpg14-ink transition-colors hover:bg-tpg14-b/10 hover:text-tpg14-b group-has-[#tpg-14-p4:checked]/tpg14:inline-flex"><span class="@max-[26rem]:sr-only">Next</span><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 3.5 10.5 8 6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></label>
            <span aria-hidden="true" class="hidden min-h-11 min-w-11 items-center justify-center gap-1.5 rounded-full px-3 text-[13.5px] font-medium text-tpg14-mut opacity-50 group-has-[#tpg-14-p5:checked]/tpg14:inline-flex @max-[26rem]:px-0"><span class="@max-[26rem]:sr-only">Next</span><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 3.5 10.5 8 6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </div>
        </div>
      </nav>
    </div>
    <p role="status" aria-live="polite" class="-mt-3 text-sm text-tpg14-mut tabular-nums"><span class="hidden group-has-[#tpg-14-p1:checked]/tpg14:inline">Page <b class="font-semibold text-tpg14-b">1</b> of 5 &middot; results 1&ndash;3 of 15</span><span class="hidden group-has-[#tpg-14-p2:checked]/tpg14:inline">Page <b class="font-semibold text-tpg14-b">2</b> of 5 &middot; results 4&ndash;6 of 15</span><span class="hidden group-has-[#tpg-14-p3:checked]/tpg14:inline">Page <b class="font-semibold text-tpg14-b">3</b> of 5 &middot; results 7&ndash;9 of 15</span><span class="hidden group-has-[#tpg-14-p4:checked]/tpg14:inline">Page <b class="font-semibold text-tpg14-b">4</b> of 5 &middot; results 10&ndash;12 of 15</span><span class="hidden group-has-[#tpg-14-p5:checked]/tpg14:inline">Page <b class="font-semibold text-tpg14-b">5</b> of 5 &middot; results 13&ndash;15 of 15</span></p>
    <p aria-hidden="true" class="rounded-full bg-tpg14-card px-3.5 py-2 font-tpg14-mono text-[11.5px] text-tpg14-mut ring-1 ring-tpg14-line">has-[:checked]: · bg-position-[…]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg14-bg: #f6f4fd;
  --color-tpg14-bg: oklch(0.971 0.012 296);
  --color-tpg14-glow1: #c7d2fecc;
  --color-tpg14-glow1: oklch(0.870 0.062 274 / 0.80);
  --color-tpg14-glow2: #fbcfe8b3;
  --color-tpg14-glow2: oklch(0.899 0.059 343 / 0.70);
  --color-tpg14-glow3: #fed7aa99;
  --color-tpg14-glow3: oklch(0.901 0.073 71 / 0.60);
  --color-tpg14-card: #fefcff;
  --color-tpg14-card: oklch(0.993 0.004 315);
  --color-tpg14-foot: #faf7fe;
  --color-tpg14-foot: oklch(0.980 0.010 305);
  --color-tpg14-track: #efeafb;
  --color-tpg14-track: oklch(0.946 0.023 299);
  --color-tpg14-ink: #1c1630;
  --color-tpg14-ink: oklch(0.222 0.050 292);
  --color-tpg14-mut: #5c5574;
  --color-tpg14-mut: oklch(0.468 0.050 295);
  --color-tpg14-line: #e6e0f5;
  --color-tpg14-line: oklch(0.918 0.029 299);
  --color-tpg14-a: #4f46e5;
  --color-tpg14-a: oklch(0.511 0.230 277);
  --color-tpg14-b: #be185d;
  --color-tpg14-b: oklch(0.525 0.199 4);
  --color-tpg14-c: #c2410c;
  --color-tpg14-c: oklch(0.553 0.174 38);
  --color-tpg14-on-acc: #ffffff;
  --color-tpg14-on-acc: oklch(1.000 0.000 0);
  --color-tpg14-ring: #4f46e5;
  --color-tpg14-ring: oklch(0.511 0.230 277);
  --font-tpg14-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tpg14-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tpg14-card: 0 1px 2px oklch(0.3 0.08 285 / 0.06), 0 20px 48px -22px oklch(0.5 0.2 300 / 0.35);
  --shadow-tpg14-track: inset 0 1px 2px oklch(0.3 0.1 285 / 0.08);
  --shadow-tpg14-pill: inset 0 1px 0 oklch(1 0 0 / 0.35), inset 0 -1px 0 oklch(0 0 0 / 0.12), 0 2px 6px oklch(0.4 0.2 300 / 0.3);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-14 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: aurora night — the pill's stops brighten to indigo-400 / pink-400 / orange-400 with deep violet ink; same tokens, re-pointed. */

@media (prefers-color-scheme: dark) {
  .tpg-14:not([data-theme="light"]) {
    --color-tpg14-bg: #0c0a18;
    --color-tpg14-bg: oklch(0.156 0.029 289);
    --color-tpg14-glow1: #3730a399;
    --color-tpg14-glow1: oklch(0.398 0.177 277 / 0.60);
    --color-tpg14-glow2: #83184380;
    --color-tpg14-glow2: oklch(0.408 0.144 2 / 0.50);
    --color-tpg14-glow3: #7c2d1266;
    --color-tpg14-glow3: oklch(0.408 0.116 38 / 0.40);
    --color-tpg14-card: #15122a;
    --color-tpg14-card: oklch(0.200 0.047 287);
    --color-tpg14-foot: #120f24;
    --color-tpg14-foot: oklch(0.185 0.042 288);
    --color-tpg14-track: #0c0a18;
    --color-tpg14-track: oklch(0.156 0.029 289);
    --color-tpg14-ink: #f1effa;
    --color-tpg14-ink: oklch(0.957 0.015 294);
    --color-tpg14-mut: #a59ec0;
    --color-tpg14-mut: oklch(0.717 0.049 295);
    --color-tpg14-line: #2a2545;
    --color-tpg14-line: oklch(0.287 0.058 289);
    --color-tpg14-a: #818cf8;
    --color-tpg14-a: oklch(0.680 0.158 277);
    --color-tpg14-b: #f472b6;
    --color-tpg14-b: oklch(0.725 0.175 350);
    --color-tpg14-c: #fb923c;
    --color-tpg14-c: oklch(0.758 0.159 56);
    --color-tpg14-on-acc: #1a0b2e;
    --color-tpg14-on-acc: oklch(0.195 0.067 300);
    --color-tpg14-ring: #a5b4fc;
    --color-tpg14-ring: oklch(0.785 0.104 275);
    --shadow-tpg14-card: 0 0 0 1px oklch(0.7 0.12 285 / 0.06), 0 1px 0 oklch(1 0 0 / 0.05) inset, 0 28px 60px -26px oklch(0.45 0.2 300 / 0.6);
    --shadow-tpg14-track: inset 0 1px 3px oklch(0 0 0 / 0.5);
    --shadow-tpg14-pill: inset 0 1px 0 oklch(1 0 0 / 0.55), inset 0 -1px 0 oklch(0 0 0 / 0.15), 0 0 0 1px oklch(1 0 0 / 0.12);
  }
}

.tpg-14[data-theme="dark"] {
  --color-tpg14-bg: #0c0a18;
  --color-tpg14-bg: oklch(0.156 0.029 289);
  --color-tpg14-glow1: #3730a399;
  --color-tpg14-glow1: oklch(0.398 0.177 277 / 0.60);
  --color-tpg14-glow2: #83184380;
  --color-tpg14-glow2: oklch(0.408 0.144 2 / 0.50);
  --color-tpg14-glow3: #7c2d1266;
  --color-tpg14-glow3: oklch(0.408 0.116 38 / 0.40);
  --color-tpg14-card: #15122a;
  --color-tpg14-card: oklch(0.200 0.047 287);
  --color-tpg14-foot: #120f24;
  --color-tpg14-foot: oklch(0.185 0.042 288);
  --color-tpg14-track: #0c0a18;
  --color-tpg14-track: oklch(0.156 0.029 289);
  --color-tpg14-ink: #f1effa;
  --color-tpg14-ink: oklch(0.957 0.015 294);
  --color-tpg14-mut: #a59ec0;
  --color-tpg14-mut: oklch(0.717 0.049 295);
  --color-tpg14-line: #2a2545;
  --color-tpg14-line: oklch(0.287 0.058 289);
  --color-tpg14-a: #818cf8;
  --color-tpg14-a: oklch(0.680 0.158 277);
  --color-tpg14-b: #f472b6;
  --color-tpg14-b: oklch(0.725 0.175 350);
  --color-tpg14-c: #fb923c;
  --color-tpg14-c: oklch(0.758 0.159 56);
  --color-tpg14-on-acc: #1a0b2e;
  --color-tpg14-on-acc: oklch(0.195 0.067 300);
  --color-tpg14-ring: #a5b4fc;
  --color-tpg14-ring: oklch(0.785 0.104 275);
  --shadow-tpg14-card: 0 0 0 1px oklch(0.7 0.12 285 / 0.06), 0 1px 0 oklch(1 0 0 / 0.05) inset, 0 28px 60px -26px oklch(0.45 0.2 300 / 0.6);
  --shadow-tpg14-track: inset 0 1px 3px oklch(0 0 0 / 0.5);
  --shadow-tpg14-pill: inset 0 1px 0 oklch(1 0 0 / 0.55), inset 0 -1px 0 oklch(0 0 0 / 0.15), 0 0 0 1px oklch(1 0 0 / 0.12);
}
```
