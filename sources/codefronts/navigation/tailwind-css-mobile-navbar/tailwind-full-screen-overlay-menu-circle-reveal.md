---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-full-screen-overlay-menu-circle-reveal/"
title: "Tailwind Full-Screen Overlay Menu with Circle Reveal Animation"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "An editorial agency menu that bursts out of the button as a circular clip-path reveal, then staggers five oversized serif links up through overflow masks."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full-Screen Overlay Menu with Circle Reveal Animation
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-full-screen-overlay-menu-circle-reveal/

An editorial agency menu that bursts out of the button as a circular clip-path reveal, then staggers five oversized serif links up through overflow masks. The port expresses the whole choreography as arbitrary values and per-item group-has-checked:delay-* utilities. Zero JavaScript.
## HTML
```html
<section class="tmn-02 w-full min-h-svh grid place-items-center bg-tmn02-stage px-4 py-6 font-tmn02-sans antialiased" aria-label="Tailwind full-screen overlay menu demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn02-paper text-tmn02-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.8)]">
    <input type="checkbox" id="tmn-02-toggle" class="peer sr-only" aria-label="Toggle full-screen menu">
    <label for="tmn-02-toggle" class="absolute top-5 right-5 z-30 grid size-11 cursor-pointer place-items-center rounded-full bg-tmn02-ink text-tmn02-paper transition-colors group-has-checked:bg-white/12 peer-focus-visible:ring-2 peer-focus-visible:ring-tmn02-acc peer-focus-visible:ring-offset-2">
      <span class="relative block h-3.5 w-5.5">
        <span class="absolute top-0 left-0 h-0.5 w-full rounded-full bg-current transition-all duration-350 group-has-checked:top-1/2 group-has-checked:-translate-y-1/2 group-has-checked:rotate-45"></span>
        <span class="absolute top-1/2 left-0 h-0.5 w-full -translate-y-1/2 rounded-full bg-current transition-opacity duration-200 group-has-checked:opacity-0"></span>
        <span class="absolute bottom-0 left-0 h-0.5 w-full rounded-full bg-current transition-all duration-350 group-has-checked:bottom-1/2 group-has-checked:translate-y-1/2 group-has-checked:-rotate-45"></span>
      </span>
    </label>

    <nav aria-label="Main" class="invisible absolute inset-0 z-20 flex flex-col justify-center bg-tmn02-ink px-9 py-10 text-tmn02-paper [clip-path:circle(0%_at_calc(100%_-_42px)_42px)] transition-[clip-path,visibility] duration-700 ease-[cubic-bezier(.77,0,.175,1)] group-has-checked:visible group-has-checked:[clip-path:circle(150%_at_calc(100%_-_42px)_42px)] motion-reduce:opacity-0 motion-reduce:[clip-path:none] motion-reduce:transition-[opacity,visibility] motion-reduce:group-has-checked:opacity-100">
      <p class="font-tmn02-mono text-[11px] tracking-[0.2em] text-tmn02-dim uppercase">Navigation</p>
      <ul class="mt-8 font-tmn02-serif text-[44px] leading-[1.15] tracking-[-0.01em]">
        <li class="overflow-hidden py-0.5"><a href="#" class="group/l flex translate-y-full items-baseline gap-4 opacity-0 transition duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[150ms] hover:text-tmn02-acc focus-visible:text-tmn02-acc focus-visible:outline-none"><span class="min-w-7 font-tmn02-mono text-xs text-tmn02-dim">01</span>Work<span aria-hidden="true" class="ml-auto -translate-x-2 text-2xl opacity-0 transition group-hover/l:translate-x-0 group-hover/l:opacity-100">→</span></a></li>
        <li class="overflow-hidden py-0.5"><a href="#" class="group/l flex translate-y-full items-baseline gap-4 opacity-0 transition duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[220ms] hover:text-tmn02-acc focus-visible:text-tmn02-acc focus-visible:outline-none"><span class="min-w-7 font-tmn02-mono text-xs text-tmn02-dim">02</span><em>About</em><span aria-hidden="true" class="ml-auto -translate-x-2 text-2xl opacity-0 transition group-hover/l:translate-x-0 group-hover/l:opacity-100">→</span></a></li>
        <li class="overflow-hidden py-0.5"><a href="#" class="group/l flex translate-y-full items-baseline gap-4 opacity-0 transition duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[290ms] hover:text-tmn02-acc focus-visible:text-tmn02-acc focus-visible:outline-none"><span class="min-w-7 font-tmn02-mono text-xs text-tmn02-dim">03</span>Services<span aria-hidden="true" class="ml-auto -translate-x-2 text-2xl opacity-0 transition group-hover/l:translate-x-0 group-hover/l:opacity-100">→</span></a></li>
        <li class="overflow-hidden py-0.5"><a href="#" class="group/l flex translate-y-full items-baseline gap-4 opacity-0 transition duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[360ms] hover:text-tmn02-acc focus-visible:text-tmn02-acc focus-visible:outline-none"><span class="min-w-7 font-tmn02-mono text-xs text-tmn02-dim">04</span><em>Journal</em><span aria-hidden="true" class="ml-auto -translate-x-2 text-2xl opacity-0 transition group-hover/l:translate-x-0 group-hover/l:opacity-100">→</span></a></li>
        <li class="overflow-hidden py-0.5"><a href="#" class="group/l flex translate-y-full items-baseline gap-4 opacity-0 transition duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[430ms] hover:text-tmn02-acc focus-visible:text-tmn02-acc focus-visible:outline-none"><span class="min-w-7 font-tmn02-mono text-xs text-tmn02-dim">05</span>Contact<span aria-hidden="true" class="ml-auto -translate-x-2 text-2xl opacity-0 transition group-hover/l:translate-x-0 group-hover/l:opacity-100">→</span></a></li>
      </ul>
      <div class="mt-12 flex gap-6 text-[13px] text-tmn02-dim opacity-0 transition-opacity duration-500 group-has-checked:opacity-100 group-has-checked:delay-[520ms]">
        <a href="#" class="py-2 hover:text-tmn02-paper">Twitter</a><a href="#" class="py-2 hover:text-tmn02-paper">Instagram</a><a href="#" class="py-2 hover:text-tmn02-paper">Dribbble</a>
      </div>
    </nav>

    <main class="flex h-full flex-col">
      <header class="flex h-[84px] items-center px-6"><p class="text-xl font-extrabold tracking-[-0.03em]">Studio<span class="text-tmn02-acc">.</span></p></header>
      <div class="flex flex-1 flex-col justify-center px-6 pb-10">
        <p class="mb-4 font-tmn02-mono text-[11px] tracking-[0.2em] text-tmn02-acc uppercase">Creative Agency · Est. 2014</p>
        <h1 class="mb-5 font-tmn02-serif text-[52px] leading-[0.98] tracking-[-0.02em] text-balance">We craft <em>digital</em> experiences</h1>
        <p class="max-w-[30ch] text-[15px] leading-relaxed text-tmn02-mut">Award-winning studio for brand identity and digital products.</p>
        <a href="#" class="mt-8 inline-flex min-h-12 w-fit items-center gap-2 rounded-full bg-tmn02-ink px-6 text-sm font-semibold text-tmn02-paper transition hover:gap-3">View our work <span aria-hidden="true">→</span></a>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn02-stage: #1b1916;
  --color-tmn02-stage: oklch(0.22 0.008 70);
  --color-tmn02-paper: #f6f1e9;
  --color-tmn02-paper: oklch(0.96 0.012 80);
  --color-tmn02-ink: #1c1917;
  --color-tmn02-ink: oklch(0.22 0.008 60);
  --color-tmn02-mut: #5c544c;
  --color-tmn02-mut: oklch(0.45 0.015 60);
  --color-tmn02-dim: #a39a90;
  --color-tmn02-dim: oklch(0.7 0.015 70);
  --color-tmn02-acc: #c2410c;
  --color-tmn02-acc: oklch(0.55 0.18 40);
  --font-tmn02-sans: 'Geist', system-ui, sans-serif;
  --font-tmn02-serif: 'Instrument Serif', Georgia, serif;
  --font-tmn02-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-02 {
  width: 100%;
  min-height: 100svh;
}
```
