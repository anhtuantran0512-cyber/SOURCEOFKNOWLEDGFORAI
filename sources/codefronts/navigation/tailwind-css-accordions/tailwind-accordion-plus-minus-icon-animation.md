---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-accordion-plus-minus-icon-animation/"
title: "Tailwind Accordion with Plus Minus Icon Animation"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "The plus that folds into a minus, ported into utilities: two <span> bars inside a square key, the vertical one turning group-open:rotate-90 onto the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accordion with Plus Minus Icon Animation
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-accordion-plus-minus-icon-animation/

The plus that folds into a minus, ported into utilities: two <span> bars inside a square key, the vertical one turning group-open:rotate-90 onto the horizontal while the whole key spins group-open:rotate-180 on a springy curve. Set as a bold Swiss type-foundry licensing FAQ in warm ivory, ink black and signal orange &mdash; with a two-way height animation from the details-content: variant.
## HTML
```html
<section class="tac-09 w-full min-h-svh grid place-items-center bg-tac09-bg px-5 py-14 font-tac09-sans text-tac09-ink [interpolate-size:allow-keywords]" aria-label="Plus minus icon accordion demo">
  <div class="grid w-full justify-items-center gap-8">
    <div class="grid w-full max-w-5xl gap-10 lg:grid-cols-[minmax(0,5fr)_minmax(0,7fr)] lg:gap-16">
      <header class="flex flex-col gap-6 lg:pt-1">
        <p class="flex items-center gap-2.5 font-tac09-mono text-xs font-medium tracking-[0.14em] uppercase text-tac09-mut"><span aria-hidden="true" class="size-2.5 rounded-full bg-tac09-acc"></span>Grotesk Foundry · Licensing</p>
        <h2 class="text-[clamp(44px,7vw,76px)] leading-[0.9] font-black tracking-[-0.045em] [font-stretch:88%]">Licences,<br>plainly<span class="text-tac09-acc">.</span></h2>
        <p class="max-w-sm text-[15.5px] leading-[1.6] text-tac09-mut text-pretty">One licence per family, scaled by team size. No page-view meters, no surprise renewals. If something isn't covered here, a type designer answers within a day.</p>
        <dl class="grid max-w-sm grid-cols-3 border-t-2 border-tac09-ink pt-4">
          <div><dt class="font-tac09-mono text-[11px] tracking-[0.1em] uppercase text-tac09-mut">Families</dt><dd class="mt-1 text-2xl font-extrabold tracking-tight">48</dd></div>
          <div><dt class="font-tac09-mono text-[11px] tracking-[0.1em] uppercase text-tac09-mut">Styles</dt><dd class="mt-1 text-2xl font-extrabold tracking-tight">612</dd></div>
          <div><dt class="font-tac09-mono text-[11px] tracking-[0.1em] uppercase text-tac09-mut">Reply</dt><dd class="mt-1 text-2xl font-extrabold tracking-tight">&lt;24h</dd></div>
        </dl>
      </header>

      <div class="border-b-2 border-tac09-ink">
        <details class="group border-t-2 border-tac09-ink details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-500 details-content:ease-[cubic-bezier(.2,.7,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 py-5 outline-none select-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tac09-acc sm:gap-6 [&::-webkit-details-marker]:hidden">
            <span class="w-7 flex-none font-tac09-mono text-sm font-medium text-tac09-mut transition-colors group-open:text-tac09-acc-ink">01</span>
            <span class="flex-1 text-[clamp(18px,2.2vw,22px)] leading-tight font-bold tracking-[-0.02em] transition-colors group-hover:text-tac09-acc-ink group-open:text-tac09-acc-ink">Can I use the fonts in a logo?</span>
            <span aria-hidden="true" class="relative grid size-11 flex-none place-items-center bg-tac09-ink text-tac09-bg transition-[transform,background-color,color] duration-500 ease-[cubic-bezier(.3,1.5,.45,1)] group-open:rotate-180 group-open:bg-tac09-acc group-open:text-tac09-ink motion-reduce:transition-none">
              <span class="absolute inset-0 m-auto h-[3px] w-4 bg-current"></span>
              <span class="absolute inset-0 m-auto h-4 w-[3px] bg-current transition-transform duration-500 ease-[cubic-bezier(.3,1.5,.45,1)] group-open:rotate-90 motion-reduce:transition-none"></span>
            </span>
          </summary>
          <div class="pr-4 pb-7 pl-11 sm:pr-17 sm:pl-13">
            <p class="text-[15.5px] leading-[1.65] text-tac09-quiet text-pretty">Yes &mdash; every desktop licence includes logos and wordmarks at no extra cost, including trademark registration. Outlines may be modified, but you can't redistribute the edited font files.</p>
          </div>
        </details>

        <details class="group border-t-2 border-tac09-ink details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-500 details-content:ease-[cubic-bezier(.2,.7,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 py-5 outline-none select-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tac09-acc sm:gap-6 [&::-webkit-details-marker]:hidden">
            <span class="w-7 flex-none font-tac09-mono text-sm font-medium text-tac09-mut transition-colors group-open:text-tac09-acc-ink">02</span>
            <span class="flex-1 text-[clamp(18px,2.2vw,22px)] leading-tight font-bold tracking-[-0.02em] transition-colors group-hover:text-tac09-acc-ink group-open:text-tac09-acc-ink">How are web licences counted?</span>
            <span aria-hidden="true" class="relative grid size-11 flex-none place-items-center bg-tac09-ink text-tac09-bg transition-[transform,background-color,color] duration-500 ease-[cubic-bezier(.3,1.5,.45,1)] group-open:rotate-180 group-open:bg-tac09-acc group-open:text-tac09-ink motion-reduce:transition-none">
              <span class="absolute inset-0 m-auto h-[3px] w-4 bg-current"></span>
              <span class="absolute inset-0 m-auto h-4 w-[3px] bg-current transition-transform duration-500 ease-[cubic-bezier(.3,1.5,.45,1)] group-open:rotate-90 motion-reduce:transition-none"></span>
            </span>
          </summary>
          <div class="pr-4 pb-7 pl-11 sm:pr-17 sm:pl-13">
            <p class="text-[15.5px] leading-[1.65] text-tac09-quiet text-pretty">By domain, not traffic. One web licence covers a production domain plus unlimited staging and preview URLs. Self-host the WOFF2 files &mdash; we never ping a tracking server.</p>
          </div>
        </details>

        <details class="group border-t-2 border-tac09-ink details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-500 details-content:ease-[cubic-bezier(.2,.7,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 py-5 outline-none select-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tac09-acc sm:gap-6 [&::-webkit-details-marker]:hidden">
            <span class="w-7 flex-none font-tac09-mono text-sm font-medium text-tac09-mut transition-colors group-open:text-tac09-acc-ink">03</span>
            <span class="flex-1 text-[clamp(18px,2.2vw,22px)] leading-tight font-bold tracking-[-0.02em] transition-colors group-hover:text-tac09-acc-ink group-open:text-tac09-acc-ink">Do you offer student and nonprofit pricing?</span>
            <span aria-hidden="true" class="relative grid size-11 flex-none place-items-center bg-tac09-ink text-tac09-bg transition-[transform,background-color,color] duration-500 ease-[cubic-bezier(.3,1.5,.45,1)] group-open:rotate-180 group-open:bg-tac09-acc group-open:text-tac09-ink motion-reduce:transition-none">
              <span class="absolute inset-0 m-auto h-[3px] w-4 bg-current"></span>
              <span class="absolute inset-0 m-auto h-4 w-[3px] bg-current transition-transform duration-500 ease-[cubic-bezier(.3,1.5,.45,1)] group-open:rotate-90 motion-reduce:transition-none"></span>
            </span>
          </summary>
          <div class="pr-4 pb-7 pl-11 sm:pr-17 sm:pl-13">
            <p class="text-[15.5px] leading-[1.65] text-tac09-quiet text-pretty">Students get any family free for non-commercial work with a university email. Registered nonprofits take 50% off every plan &mdash; send your registration number and we'll issue a code the same day.</p>
          </div>
        </details>

        <details class="group border-t-2 border-tac09-ink details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-500 details-content:ease-[cubic-bezier(.2,.7,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 py-5 outline-none select-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tac09-acc sm:gap-6 [&::-webkit-details-marker]:hidden">
            <span class="w-7 flex-none font-tac09-mono text-sm font-medium text-tac09-mut transition-colors group-open:text-tac09-acc-ink">04</span>
            <span class="flex-1 text-[clamp(18px,2.2vw,22px)] leading-tight font-bold tracking-[-0.02em] transition-colors group-hover:text-tac09-acc-ink group-open:text-tac09-acc-ink">Can I upgrade my team size later?</span>
            <span aria-hidden="true" class="relative grid size-11 flex-none place-items-center bg-tac09-ink text-tac09-bg transition-[transform,background-color,color] duration-500 ease-[cubic-bezier(.3,1.5,.45,1)] group-open:rotate-180 group-open:bg-tac09-acc group-open:text-tac09-ink motion-reduce:transition-none">
              <span class="absolute inset-0 m-auto h-[3px] w-4 bg-current"></span>
              <span class="absolute inset-0 m-auto h-4 w-[3px] bg-current transition-transform duration-500 ease-[cubic-bezier(.3,1.5,.45,1)] group-open:rotate-90 motion-reduce:transition-none"></span>
            </span>
          </summary>
          <div class="pr-4 pb-7 pl-11 sm:pr-17 sm:pl-13">
            <p class="text-[15.5px] leading-[1.65] text-tac09-quiet text-pretty">Anytime. You only pay the difference between tiers, prorated to the day, and the new seat count applies to every family you already own.</p>
          </div>
        </details>
      </div>
    </div>
    <p aria-hidden="true" class="border-2 border-tac09-ink px-3.5 py-2 font-tac09-mono text-[11.5px] text-tac09-ink">group-open:rotate-90 · group-open:rotate-180 · open:details-content:h-auto</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac09-bg: #f4efe4;
  --color-tac09-bg: oklch(0.955 0.015 85);
  --color-tac09-ink: #141210;
  --color-tac09-ink: oklch(0.18 0.006 60);
  --color-tac09-quiet: #3b3631;
  --color-tac09-quiet: oklch(0.34 0.012 60);
  --color-tac09-mut: #5f5850;
  --color-tac09-mut: oklch(0.46 0.015 65);
  --color-tac09-acc: #ff5a1f;
  --color-tac09-acc: oklch(0.68 0.21 38);
  --color-tac09-acc-ink: #b53a0c;
  --color-tac09-acc-ink: oklch(0.52 0.17 38);
  --font-tac09-sans: 'Archivo', 'Helvetica Neue', system-ui, sans-serif;
  --font-tac09-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-09 {
  width: 100%;
  min-height: 100svh;
}
```
