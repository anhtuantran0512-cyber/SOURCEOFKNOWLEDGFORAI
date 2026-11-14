---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-floating-glass-pill-navbar-backdrop-blur/"
title: "Tailwind Floating Glass Pill Navbar (Backdrop Blur)"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "A floating, rounded glass pill that hovers over full-bleed photography: sticky top-4 mx-auto w-fit rounded-full plus backdrop-blur-2xl backdrop-saturate-200."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Glass Pill Navbar (Backdrop Blur)
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-floating-glass-pill-navbar-backdrop-blur/

A floating, rounded glass pill that hovers over full-bleed photography: sticky top-4 mx-auto w-fit rounded-full plus backdrop-blur-2xl backdrop-saturate-200. The glass only turns translucent inside supports-[backdrop-filter:blur(1px)]:, so browsers without blur get a readable solid pill, never invisible text.
## HTML
```html
<div class="tsn-05 w-full min-h-svh bg-tsn05-bg font-tsn05-sans text-tsn05-ink antialiased" aria-label="Floating glass pill navbar demo">
  <header class="sticky top-4 z-40 mx-auto -mb-[4.5rem] flex w-fit max-w-[calc(100%-1.5rem)] items-center gap-1 rounded-full bg-white/85 p-1.5 text-tsn05-bar shadow-[0_1px_0_rgb(255_255_255/0.7)_inset,0_12px_32px_-8px_rgb(10_20_40/0.35),0_2px_6px_rgb(10_20_40/0.12)] ring-1 ring-white/50 backdrop-blur-2xl backdrop-saturate-200 supports-[backdrop-filter:blur(1px)]:bg-white/45">
    <a href="#tsn-05-s1" class="flex min-h-11 flex-none items-center gap-2 rounded-full pl-3 pr-2 font-semibold tracking-tight focus-visible:outline-2 focus-visible:outline-tsn05-acc"><span aria-hidden="true" class="size-6 rounded-full bg-[radial-gradient(circle_at_30%_30%,#fff,var(--color-tsn05-acc)_55%,var(--color-tsn05-bar))]"></span><span class="max-sm:sr-only">Halo</span></a>
    <nav aria-label="Primary" class="flex min-w-0 gap-0.5 overflow-x-auto [scrollbar-width:none]">
      <a href="#tsn-05-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center rounded-full px-4 text-sm font-medium text-tsn05-bar/75 transition hover:bg-white/60 hover:text-tsn05-bar focus-visible:outline-2 focus-visible:outline-tsn05-acc aria-[current=page]:bg-white aria-[current=page]:text-tsn05-bar aria-[current=page]:shadow-[0_2px_8px_rgb(10_20_40/0.12)]">Coast</a>
      <a href="#tsn-05-s2" class="inline-flex min-h-11 flex-none items-center rounded-full px-4 text-sm font-medium text-tsn05-bar/75 transition hover:bg-white/60 hover:text-tsn05-bar focus-visible:outline-2 focus-visible:outline-tsn05-acc">Alps</a>
      <a href="#tsn-05-s3" class="inline-flex min-h-11 flex-none items-center rounded-full px-4 text-sm font-medium text-tsn05-bar/75 transition hover:bg-white/60 hover:text-tsn05-bar focus-visible:outline-2 focus-visible:outline-tsn05-acc">Forest</a>
      <a href="#tsn-05-s4" class="inline-flex min-h-11 flex-none items-center rounded-full px-4 text-sm font-medium text-tsn05-bar/75 transition hover:bg-white/60 hover:text-tsn05-bar focus-visible:outline-2 focus-visible:outline-tsn05-acc">Desert</a>
    </nav>
    <a href="#tsn-05-s4" class="inline-flex min-h-11 flex-none items-center rounded-full bg-tsn05-bar px-4 text-sm font-semibold text-white transition hover:bg-tsn05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn05-acc">Book</a>
  </header>
  <main id="tsn-05-main" class="grid gap-3 p-3">
    <section id="tsn-05-s1" aria-labelledby="tsn-05-h1" class="relative isolate grid min-h-svh scroll-mt-0 content-end overflow-hidden rounded-[2rem] bg-[linear-gradient(160deg,#1f5f7a,#0b2233)] p-[clamp(1.5rem,5vw,4rem)] text-white">
      <img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=70" alt="" class="absolute inset-0 -z-10 size-full object-cover">
      <div aria-hidden="true" class="absolute inset-0 -z-10 bg-[linear-gradient(to_top,rgb(5_15_25/0.75),transparent_60%)]"></div>
      <p class="font-tsn05-mono text-[11.5px] uppercase tracking-[0.18em] text-white/80">sticky top-4 · w-fit · backdrop-blur-2xl</p>
      <h1 id="tsn-05-h1" class="mt-3 max-w-[14ch] text-[clamp(40px,8vw,96px)] font-semibold leading-[0.95] tracking-[-0.04em] text-balance">A pill of glass over the world</h1>
      <p class="mt-5 max-w-[46ch] text-[17px] leading-relaxed text-white/85 text-pretty">Scroll: the navbar floats 16px from the top, blurring and saturating whatever photograph slides beneath it.</p>
    </section>
    <section id="tsn-05-s2" aria-labelledby="tsn-05-h2" class="relative isolate grid min-h-[90svh] scroll-mt-24 content-end overflow-hidden rounded-[2rem] bg-[linear-gradient(160deg,#5b6b84,#1b2433)] p-[clamp(1.5rem,5vw,4rem)] text-white">
      <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1600&q=70" alt="" loading="lazy" class="absolute inset-0 -z-10 size-full object-cover">
      <div aria-hidden="true" class="absolute inset-0 -z-10 bg-[linear-gradient(to_top,rgb(5_15_25/0.7),transparent_60%)]"></div>
      <h2 id="tsn-05-h2" class="max-w-[18ch] text-[clamp(28px,4.5vw,52px)] font-semibold leading-[1.02] tracking-[-0.03em]">Translucent only where blur works</h2>
      <p class="mt-4 max-w-[52ch] leading-relaxed text-white/85">The pill is 85% white by default and drops to 45% inside <code class="font-tsn05-mono text-[0.9em]">supports-[backdrop-filter:blur(1px)]:</code>.</p>
    </section>
    <section id="tsn-05-s3" aria-labelledby="tsn-05-h3" class="relative isolate grid min-h-[90svh] scroll-mt-24 content-end overflow-hidden rounded-[2rem] bg-[linear-gradient(160deg,#2f5a3a,#0f2016)] p-[clamp(1.5rem,5vw,4rem)] text-white">
      <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1600&q=70" alt="" loading="lazy" class="absolute inset-0 -z-10 size-full object-cover">
      <div aria-hidden="true" class="absolute inset-0 -z-10 bg-[linear-gradient(to_top,rgb(5_15_10/0.7),transparent_60%)]"></div>
      <h2 id="tsn-05-h3" class="max-w-[18ch] text-[clamp(28px,4.5vw,52px)] font-semibold leading-[1.02] tracking-[-0.03em]">An edge of light</h2>
      <p class="mt-4 max-w-[52ch] leading-relaxed text-white/85">An inset white highlight, a <code class="font-tsn05-mono text-[0.9em]">ring-white/50</code> rim and a two-layer drop shadow give the pill a physical edge over any image.</p>
    </section>
    <section id="tsn-05-s4" aria-labelledby="tsn-05-h4" class="relative isolate grid min-h-[90svh] scroll-mt-24 content-end overflow-hidden rounded-[2rem] bg-[linear-gradient(160deg,#b0663a,#3a1d10)] p-[clamp(1.5rem,5vw,4rem)] text-white">
      <img src="https://images.unsplash.com/photo-1509316785289-025f5b846b35?auto=format&fit=crop&w=1600&q=70" alt="" loading="lazy" class="absolute inset-0 -z-10 size-full object-cover">
      <div aria-hidden="true" class="absolute inset-0 -z-10 bg-[linear-gradient(to_top,rgb(25_10_5/0.7),transparent_60%)]"></div>
      <h2 id="tsn-05-h4" class="max-w-[18ch] text-[clamp(28px,4.5vw,52px)] font-semibold leading-[1.02] tracking-[-0.03em]">Shrink-wrapped and centred</h2>
      <p class="mt-4 max-w-[52ch] leading-relaxed text-white/85"><code class="font-tsn05-mono text-[0.9em]">w-fit mx-auto</code> sizes the pill to its links, capped at <code class="font-tsn05-mono text-[0.9em]">max-w-[calc(100%-1.5rem)]</code> so it scrolls rather than overflows on phones.</p>
    </section>
  </main>
  <footer class="px-6 py-10 text-center font-tsn05-mono text-xs text-tsn05-mut">Tailwind sticky navigation · pattern 05 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn05-bg: #0b1018;
  --color-tsn05-bg: oklch(0.16 0.015 255);
  --color-tsn05-ink: #eef2f7;
  --color-tsn05-ink: oklch(0.96 0.008 255);
  --color-tsn05-mut: #9aa4b4;
  --color-tsn05-mut: oklch(0.72 0.02 255);
  --color-tsn05-bar: #0f1b2d;
  --color-tsn05-bar: oklch(0.21 0.04 258);
  --color-tsn05-acc: #2b7fff;
  --color-tsn05-acc: oklch(0.62 0.2 258);
  --font-tsn05-sans: 'Outfit', system-ui, sans-serif;
  --font-tsn05-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-05 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-05) {
    scroll-behavior: smooth;
  }
}
```
