---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/minimal-tailwind-accordion-animated-underline/"
title: "Minimal Tailwind Accordion with Animated Underline"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "An editorial, box-free accordion for studios and portfolios: oversized serif questions on warm paper, separated only by hairlines."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Tailwind Accordion with Animated Underline
Source: https://codefronts.com/navigation/tailwind-css-accordions/minimal-tailwind-accordion-animated-underline/

An editorial, box-free accordion for studios and portfolios: oversized serif questions on warm paper, separated only by hairlines. State is a rule that draws itself across the row &mdash; after:scale-x-0 after:origin-left to group-open:after:scale-x-100 &mdash; previewed at low opacity on hover, while the italic index letter fills from outline to vermilion and a thin plus turns into a cross.
## HTML
```html
<section class="tac-07 w-full min-h-svh grid place-items-center bg-tac07-bg bg-[radial-gradient(90%_60%_at_80%_0%,var(--color-tac07-glow),transparent_70%)] px-5 py-16 font-tac07-sans text-tac07-ink" aria-label="Minimal editorial accordion with animated underline demo">
  <div class="grid w-full justify-items-center gap-10">
    <article class="w-full max-w-3xl">
      <header>
        <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1 border-b-2 border-tac07-ink pb-3 text-[11.5px] font-semibold tracking-[0.22em] uppercase text-tac07-mut">
          <span>Field Notes</span>
          <span>№ 4 · Autumn 2026</span>
        </div>
        <h2 class="mt-9 font-tac07-serif text-[clamp(44px,8vw,80px)] leading-[0.92] tracking-[-0.025em]">Questions, <em class="text-tac07-acc">answered.</em></h2>
        <p class="mt-5 max-w-[46ch] text-[15.5px] leading-relaxed text-tac07-mut">Four things people ask before the first call with Ørsted &amp; Vale &mdash; and the honest answers we give them.</p>
      </header>

      <div class="mt-12 border-b border-tac07-rule">
        <details class="group border-t border-tac07-rule" open>
          <summary class="relative flex min-h-11 cursor-pointer list-none items-baseline gap-[clamp(12px,2.5vw,22px)] py-[clamp(20px,3vw,28px)] pe-1 font-tac07-serif text-[clamp(24px,3.8vw,36px)] leading-[1.15] tracking-[-0.012em] outline-none after:absolute after:inset-x-0 after:-bottom-px after:h-[1.5px] after:origin-left after:scale-x-0 after:bg-tac07-ink after:transition-[scale,opacity] after:duration-700 after:ease-[cubic-bezier(0.65,0,0.2,1)] hover:after:scale-x-100 hover:after:opacity-25 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac07-ink group-open:after:scale-x-100 group-open:after:opacity-100! motion-reduce:after:transition-none [&::-webkit-details-marker]:hidden">
            <i aria-hidden="true" class="w-[1.1em] flex-none text-[0.72em] text-transparent transition-colors duration-500 [-webkit-text-stroke:1px_var(--color-tac07-mut)] group-open:text-tac07-acc group-open:[-webkit-text-stroke:0]">a</i>
            <span class="min-w-0 flex-1 text-balance">What does the studio actually make?</span>
            <span aria-hidden="true" class="relative ms-2 size-5 flex-none self-center transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.2,1)] before:absolute before:inset-x-0 before:top-1/2 before:h-px before:-translate-y-1/2 before:bg-tac07-ink after:absolute after:inset-y-0 after:left-1/2 after:w-px after:-translate-x-1/2 after:bg-tac07-ink group-open:rotate-45 motion-reduce:transition-none"></span>
          </summary>
          <div class="pb-9 pt-6 ps-[calc(clamp(24px,3.8vw,36px)*0.792+clamp(12px,2.5vw,22px))] group-open:animate-tac07-rise motion-reduce:animate-none max-sm:ps-0">
            <p class="max-w-[60ch] text-base leading-[1.75] text-tac07-body text-pretty">Identity systems, editorial websites and the occasional typeface. We take four projects a year and finish all four &mdash; the constraint is the offer.</p>
            <p class="mt-4 font-tac07-mono text-xs tracking-wide text-tac07-mut">Recent: Halden Press · Nordlys Ferries · Common Hours</p>
          </div>
        </details>

        <details class="group border-t border-tac07-rule">
          <summary class="relative flex min-h-11 cursor-pointer list-none items-baseline gap-[clamp(12px,2.5vw,22px)] py-[clamp(20px,3vw,28px)] pe-1 font-tac07-serif text-[clamp(24px,3.8vw,36px)] leading-[1.15] tracking-[-0.012em] outline-none after:absolute after:inset-x-0 after:-bottom-px after:h-[1.5px] after:origin-left after:scale-x-0 after:bg-tac07-ink after:transition-[scale,opacity] after:duration-700 after:ease-[cubic-bezier(0.65,0,0.2,1)] hover:after:scale-x-100 hover:after:opacity-25 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac07-ink group-open:after:scale-x-100 group-open:after:opacity-100! motion-reduce:after:transition-none [&::-webkit-details-marker]:hidden">
            <i aria-hidden="true" class="w-[1.1em] flex-none text-[0.72em] text-transparent transition-colors duration-500 [-webkit-text-stroke:1px_var(--color-tac07-mut)] group-open:text-tac07-acc group-open:[-webkit-text-stroke:0]">b</i>
            <span class="min-w-0 flex-1 text-balance">How does an engagement begin?</span>
            <span aria-hidden="true" class="relative ms-2 size-5 flex-none self-center transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.2,1)] before:absolute before:inset-x-0 before:top-1/2 before:h-px before:-translate-y-1/2 before:bg-tac07-ink after:absolute after:inset-y-0 after:left-1/2 after:w-px after:-translate-x-1/2 after:bg-tac07-ink group-open:rotate-45 motion-reduce:transition-none"></span>
          </summary>
          <div class="pb-9 pt-6 ps-[calc(clamp(24px,3.8vw,36px)*0.792+clamp(12px,2.5vw,22px))] group-open:animate-tac07-rise motion-reduce:animate-none max-sm:ps-0">
            <p class="max-w-[60ch] text-base leading-[1.75] text-tac07-body text-pretty">With a two-week discovery sprint: interviews, an audit, and a written point of view. If we turn out to be wrong for each other, you keep the document and we part as friends.</p>
          </div>
        </details>

        <details class="group border-t border-tac07-rule">
          <summary class="relative flex min-h-11 cursor-pointer list-none items-baseline gap-[clamp(12px,2.5vw,22px)] py-[clamp(20px,3vw,28px)] pe-1 font-tac07-serif text-[clamp(24px,3.8vw,36px)] leading-[1.15] tracking-[-0.012em] outline-none after:absolute after:inset-x-0 after:-bottom-px after:h-[1.5px] after:origin-left after:scale-x-0 after:bg-tac07-ink after:transition-[scale,opacity] after:duration-700 after:ease-[cubic-bezier(0.65,0,0.2,1)] hover:after:scale-x-100 hover:after:opacity-25 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac07-ink group-open:after:scale-x-100 group-open:after:opacity-100! motion-reduce:after:transition-none [&::-webkit-details-marker]:hidden">
            <i aria-hidden="true" class="w-[1.1em] flex-none text-[0.72em] text-transparent transition-colors duration-500 [-webkit-text-stroke:1px_var(--color-tac07-mut)] group-open:text-tac07-acc group-open:[-webkit-text-stroke:0]">c</i>
            <span class="min-w-0 flex-1 text-balance">Do you work with early-stage teams?</span>
            <span aria-hidden="true" class="relative ms-2 size-5 flex-none self-center transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.2,1)] before:absolute before:inset-x-0 before:top-1/2 before:h-px before:-translate-y-1/2 before:bg-tac07-ink after:absolute after:inset-y-0 after:left-1/2 after:w-px after:-translate-x-1/2 after:bg-tac07-ink group-open:rotate-45 motion-reduce:transition-none"></span>
          </summary>
          <div class="pb-9 pt-6 ps-[calc(clamp(24px,3.8vw,36px)*0.792+clamp(12px,2.5vw,22px))] group-open:animate-tac07-rise motion-reduce:animate-none max-sm:ps-0">
            <p class="max-w-[60ch] text-base leading-[1.75] text-tac07-body text-pretty">Two of our four annual slots are reserved for pre-seed and seed companies at a reduced rate. Bring conviction; the deck can be ugly.</p>
          </div>
        </details>

        <details class="group border-t border-tac07-rule">
          <summary class="relative flex min-h-11 cursor-pointer list-none items-baseline gap-[clamp(12px,2.5vw,22px)] py-[clamp(20px,3vw,28px)] pe-1 font-tac07-serif text-[clamp(24px,3.8vw,36px)] leading-[1.15] tracking-[-0.012em] outline-none after:absolute after:inset-x-0 after:-bottom-px after:h-[1.5px] after:origin-left after:scale-x-0 after:bg-tac07-ink after:transition-[scale,opacity] after:duration-700 after:ease-[cubic-bezier(0.65,0,0.2,1)] hover:after:scale-x-100 hover:after:opacity-25 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac07-ink group-open:after:scale-x-100 group-open:after:opacity-100! motion-reduce:after:transition-none [&::-webkit-details-marker]:hidden">
            <i aria-hidden="true" class="w-[1.1em] flex-none text-[0.72em] text-transparent transition-colors duration-500 [-webkit-text-stroke:1px_var(--color-tac07-mut)] group-open:text-tac07-acc group-open:[-webkit-text-stroke:0]">d</i>
            <span class="min-w-0 flex-1 text-balance">Where are you based?</span>
            <span aria-hidden="true" class="relative ms-2 size-5 flex-none self-center transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.2,1)] before:absolute before:inset-x-0 before:top-1/2 before:h-px before:-translate-y-1/2 before:bg-tac07-ink after:absolute after:inset-y-0 after:left-1/2 after:w-px after:-translate-x-1/2 after:bg-tac07-ink group-open:rotate-45 motion-reduce:transition-none"></span>
          </summary>
          <div class="pb-9 pt-6 ps-[calc(clamp(24px,3.8vw,36px)*0.792+clamp(12px,2.5vw,22px))] group-open:animate-tac07-rise motion-reduce:animate-none max-sm:ps-0">
            <p class="max-w-[60ch] text-base leading-[1.75] text-tac07-body text-pretty">Copenhagen and Toronto, and the six hours of overlap between them. Everything ships from a shared repository and a long-running phone call.</p>
          </div>
        </details>
      </div>

      <footer class="mt-8 flex flex-wrap items-center justify-between gap-4 text-[15px] text-tac07-mut">
        <p>Something we didn't cover?</p>
        <button type="button" class="group/cta relative inline-flex min-h-11 items-center gap-2 font-semibold text-tac07-ink after:absolute after:inset-x-0 after:bottom-2.5 after:h-px after:origin-right after:scale-x-0 after:bg-tac07-acc after:transition-[scale] after:duration-500 hover:after:origin-left hover:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac07-ink motion-reduce:after:transition-none">Write to the studio <span aria-hidden="true" class="transition-transform duration-300 group-hover/cta:translate-x-1 motion-reduce:transition-none">→</span></button>
      </footer>
    </article>
    <p aria-hidden="true" class="rounded-full border border-tac07-rule bg-tac07-paper px-3.5 py-2 text-center font-tac07-mono text-[11.5px] text-tac07-mut">after:origin-left · after:scale-x-0 → group-open:after:scale-x-100</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac07-bg: #f9f5ec;
  --color-tac07-bg: oklch(0.97 0.012 85);
  --color-tac07-glow: #fefcf7;
  --color-tac07-glow: oklch(0.99 0.006 85);
  --color-tac07-paper: #fefcf7;
  --color-tac07-paper: oklch(0.99 0.006 85);
  --color-tac07-ink: #1a1511;
  --color-tac07-ink: oklch(0.2 0.012 60);
  --color-tac07-body: #433c36;
  --color-tac07-body: oklch(0.36 0.014 60);
  --color-tac07-mut: #625952;
  --color-tac07-mut: oklch(0.47 0.016 60);
  --color-tac07-rule: #d9d2c6;
  --color-tac07-rule: oklch(0.87 0.016 78);
  --color-tac07-acc: #c8331a;
  --color-tac07-acc: oklch(0.55 0.19 32);
  --font-tac07-serif: 'Instrument Serif', 'Iowan Old Style', Georgia, serif;
  --font-tac07-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tac07-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --animate-tac07-rise: tac07-rise 0.6s cubic-bezier(0.2, 0.7, 0.3, 1);

  @keyframes tac07-rise {
    from {
      opacity: 0;
      translate: 0 8px;
    }

    to {
      opacity: 1;
      translate: 0 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-07 {
  width: 100%;
  min-height: 100svh;
}
```
