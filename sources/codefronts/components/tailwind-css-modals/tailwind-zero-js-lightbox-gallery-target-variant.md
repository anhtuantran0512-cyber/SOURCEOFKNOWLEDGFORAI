---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-zero-js-lightbox-gallery-target-variant/"
title: "Tailwind Zero-JS Lightbox Gallery with the target Variant"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A six-frame gallery whose full-screen viewer is pure CSS: every panel is an :target, every control is an anchor."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Zero-JS Lightbox Gallery with the target Variant
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-zero-js-lightbox-gallery-target-variant/

A six-frame gallery whose full-screen viewer is pure CSS: every panel is an :target, every control is an anchor. The port's whole story is two variants — target: on the panel and group-target: on the figure inside it — replacing a pair of :target rules written far from the markup.
## HTML
```html
<section class="tm-09 w-full min-h-svh" id="tm-09">
  <div class="w-full min-h-svh grid place-items-center bg-tm09-bg font-tm09-sans px-6 py-10">
    <div class="grid grid-cols-3 gap-3.5">
      <a href="#tm-09-1" data-n="01" aria-label="Open image 1" class="relative aspect-square w-[120px] rounded-xl overflow-hidden no-underline border border-tm09-edge bg-[repeating-linear-gradient(135deg,var(--color-tm09-stripeA)_0_12px,var(--color-tm09-stripeB)_12px_24px)] transition-[translate,border-color,box-shadow] duration-200 hover:-translate-y-[3px] hover:border-tm09-acc hover:shadow-[0_12px_30px_-14px_var(--color-tm09-acc)] focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0 after:content-[attr(data-n)] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm09-mono after:text-[15px] after:font-semibold after:text-tm09-faint"></a>
      <a href="#tm-09-2" data-n="02" aria-label="Open image 2" class="relative aspect-square w-[120px] rounded-xl overflow-hidden no-underline border border-tm09-edge bg-[repeating-linear-gradient(135deg,var(--color-tm09-stripeA)_0_12px,var(--color-tm09-stripeB)_12px_24px)] transition-[translate,border-color,box-shadow] duration-200 hover:-translate-y-[3px] hover:border-tm09-acc hover:shadow-[0_12px_30px_-14px_var(--color-tm09-acc)] focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0 after:content-[attr(data-n)] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm09-mono after:text-[15px] after:font-semibold after:text-tm09-faint"></a>
      <a href="#tm-09-3" data-n="03" aria-label="Open image 3" class="relative aspect-square w-[120px] rounded-xl overflow-hidden no-underline border border-tm09-edge bg-[repeating-linear-gradient(135deg,var(--color-tm09-stripeA)_0_12px,var(--color-tm09-stripeB)_12px_24px)] transition-[translate,border-color,box-shadow] duration-200 hover:-translate-y-[3px] hover:border-tm09-acc hover:shadow-[0_12px_30px_-14px_var(--color-tm09-acc)] focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0 after:content-[attr(data-n)] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm09-mono after:text-[15px] after:font-semibold after:text-tm09-faint"></a>
      <a href="#tm-09-4" data-n="04" aria-label="Open image 4" class="relative aspect-square w-[120px] rounded-xl overflow-hidden no-underline border border-tm09-edge bg-[repeating-linear-gradient(135deg,var(--color-tm09-stripeA)_0_12px,var(--color-tm09-stripeB)_12px_24px)] transition-[translate,border-color,box-shadow] duration-200 hover:-translate-y-[3px] hover:border-tm09-acc hover:shadow-[0_12px_30px_-14px_var(--color-tm09-acc)] focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0 after:content-[attr(data-n)] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm09-mono after:text-[15px] after:font-semibold after:text-tm09-faint"></a>
      <a href="#tm-09-5" data-n="05" aria-label="Open image 5" class="relative aspect-square w-[120px] rounded-xl overflow-hidden no-underline border border-tm09-edge bg-[repeating-linear-gradient(135deg,var(--color-tm09-stripeA)_0_12px,var(--color-tm09-stripeB)_12px_24px)] transition-[translate,border-color,box-shadow] duration-200 hover:-translate-y-[3px] hover:border-tm09-acc hover:shadow-[0_12px_30px_-14px_var(--color-tm09-acc)] focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0 after:content-[attr(data-n)] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm09-mono after:text-[15px] after:font-semibold after:text-tm09-faint"></a>
      <a href="#tm-09-6" data-n="06" aria-label="Open image 6" class="relative aspect-square w-[120px] rounded-xl overflow-hidden no-underline border border-tm09-edge bg-[repeating-linear-gradient(135deg,var(--color-tm09-stripeA)_0_12px,var(--color-tm09-stripeB)_12px_24px)] transition-[translate,border-color,box-shadow] duration-200 hover:-translate-y-[3px] hover:border-tm09-acc hover:shadow-[0_12px_30px_-14px_var(--color-tm09-acc)] focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0 after:content-[attr(data-n)] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm09-mono after:text-[15px] after:font-semibold after:text-tm09-faint"></a>
    </div>
  </div>

  <div id="tm-09-1" role="dialog" aria-modal="true" aria-label="Image 1 of 6" class="group fixed inset-0 z-20 grid place-items-center px-6 py-14 opacity-0 invisible transition-[opacity,visibility] duration-300 target:opacity-100 target:visible motion-reduce:transition-none">
    <a href="#tm-09" aria-label="Close" class="absolute inset-0 bg-tm09-scrim backdrop-blur-[6px]"></a>
    <a href="#tm-09-6" aria-label="Previous image" class="absolute z-[2] left-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&lsaquo;</a>
    <figure data-label="image 01" class="relative w-[min(620px,90vw)] aspect-[3/2] grid place-items-center rounded-2xl overflow-hidden border border-tm09-figedge bg-[repeating-linear-gradient(135deg,var(--color-tm09-figA)_0_18px,var(--color-tm09-figB)_18px_36px)] scale-90 transition-transform duration-300 group-target:scale-100 motion-reduce:transition-none before:content-[attr(data-label)] before:font-tm09-mono before:text-xs before:tracking-[0.2em] before:uppercase before:text-tm09-faint">
      <figcaption class="absolute inset-x-0 bottom-0 px-4.5 py-3.5 text-[13px] text-tm09-ink bg-[linear-gradient(transparent,var(--color-tm09-capscrim))]">Frame 01 &mdash; desert highway</figcaption>
    </figure>
    <a href="#tm-09-2" aria-label="Next image" class="absolute z-[2] right-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&rsaquo;</a>
    <span aria-hidden="true" class="absolute z-[2] top-5 left-5 px-2.5 py-1 rounded-lg font-tm09-mono text-xs text-tm09-ink bg-tm09-ctl border border-tm09-ctledge">01 / 06</span>
    <a href="#tm-09" aria-label="Close" class="absolute z-[2] top-4 right-4 grid place-items-center size-12 rounded-xl no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&times;</a>
  </div>

  <div id="tm-09-2" role="dialog" aria-modal="true" aria-label="Image 2 of 6" class="group fixed inset-0 z-20 grid place-items-center px-6 py-14 opacity-0 invisible transition-[opacity,visibility] duration-300 target:opacity-100 target:visible motion-reduce:transition-none">
    <a href="#tm-09" aria-label="Close" class="absolute inset-0 bg-tm09-scrim backdrop-blur-[6px]"></a>
    <a href="#tm-09-1" aria-label="Previous image" class="absolute z-[2] left-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&lsaquo;</a>
    <figure data-label="image 02" class="relative w-[min(620px,90vw)] aspect-[3/2] grid place-items-center rounded-2xl overflow-hidden border border-tm09-figedge bg-[repeating-linear-gradient(135deg,var(--color-tm09-figA)_0_18px,var(--color-tm09-figB)_18px_36px)] scale-90 transition-transform duration-300 group-target:scale-100 motion-reduce:transition-none before:content-[attr(data-label)] before:font-tm09-mono before:text-xs before:tracking-[0.2em] before:uppercase before:text-tm09-faint">
      <figcaption class="absolute inset-x-0 bottom-0 px-4.5 py-3.5 text-[13px] text-tm09-ink bg-[linear-gradient(transparent,var(--color-tm09-capscrim))]">Frame 02 &mdash; neon alley</figcaption>
    </figure>
    <a href="#tm-09-3" aria-label="Next image" class="absolute z-[2] right-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&rsaquo;</a>
    <span aria-hidden="true" class="absolute z-[2] top-5 left-5 px-2.5 py-1 rounded-lg font-tm09-mono text-xs text-tm09-ink bg-tm09-ctl border border-tm09-ctledge">02 / 06</span>
    <a href="#tm-09" aria-label="Close" class="absolute z-[2] top-4 right-4 grid place-items-center size-12 rounded-xl no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&times;</a>
  </div>

  <div id="tm-09-3" role="dialog" aria-modal="true" aria-label="Image 3 of 6" class="group fixed inset-0 z-20 grid place-items-center px-6 py-14 opacity-0 invisible transition-[opacity,visibility] duration-300 target:opacity-100 target:visible motion-reduce:transition-none">
    <a href="#tm-09" aria-label="Close" class="absolute inset-0 bg-tm09-scrim backdrop-blur-[6px]"></a>
    <a href="#tm-09-2" aria-label="Previous image" class="absolute z-[2] left-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&lsaquo;</a>
    <figure data-label="image 03" class="relative w-[min(620px,90vw)] aspect-[3/2] grid place-items-center rounded-2xl overflow-hidden border border-tm09-figedge bg-[repeating-linear-gradient(135deg,var(--color-tm09-figA)_0_18px,var(--color-tm09-figB)_18px_36px)] scale-90 transition-transform duration-300 group-target:scale-100 motion-reduce:transition-none before:content-[attr(data-label)] before:font-tm09-mono before:text-xs before:tracking-[0.2em] before:uppercase before:text-tm09-faint">
      <figcaption class="absolute inset-x-0 bottom-0 px-4.5 py-3.5 text-[13px] text-tm09-ink bg-[linear-gradient(transparent,var(--color-tm09-capscrim))]">Frame 03 &mdash; coastal fog</figcaption>
    </figure>
    <a href="#tm-09-4" aria-label="Next image" class="absolute z-[2] right-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&rsaquo;</a>
    <span aria-hidden="true" class="absolute z-[2] top-5 left-5 px-2.5 py-1 rounded-lg font-tm09-mono text-xs text-tm09-ink bg-tm09-ctl border border-tm09-ctledge">03 / 06</span>
    <a href="#tm-09" aria-label="Close" class="absolute z-[2] top-4 right-4 grid place-items-center size-12 rounded-xl no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&times;</a>
  </div>

  <div id="tm-09-4" role="dialog" aria-modal="true" aria-label="Image 4 of 6" class="group fixed inset-0 z-20 grid place-items-center px-6 py-14 opacity-0 invisible transition-[opacity,visibility] duration-300 target:opacity-100 target:visible motion-reduce:transition-none">
    <a href="#tm-09" aria-label="Close" class="absolute inset-0 bg-tm09-scrim backdrop-blur-[6px]"></a>
    <a href="#tm-09-3" aria-label="Previous image" class="absolute z-[2] left-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&lsaquo;</a>
    <figure data-label="image 04" class="relative w-[min(620px,90vw)] aspect-[3/2] grid place-items-center rounded-2xl overflow-hidden border border-tm09-figedge bg-[repeating-linear-gradient(135deg,var(--color-tm09-figA)_0_18px,var(--color-tm09-figB)_18px_36px)] scale-90 transition-transform duration-300 group-target:scale-100 motion-reduce:transition-none before:content-[attr(data-label)] before:font-tm09-mono before:text-xs before:tracking-[0.2em] before:uppercase before:text-tm09-faint">
      <figcaption class="absolute inset-x-0 bottom-0 px-4.5 py-3.5 text-[13px] text-tm09-ink bg-[linear-gradient(transparent,var(--color-tm09-capscrim))]">Frame 04 &mdash; pine ridge</figcaption>
    </figure>
    <a href="#tm-09-5" aria-label="Next image" class="absolute z-[2] right-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&rsaquo;</a>
    <span aria-hidden="true" class="absolute z-[2] top-5 left-5 px-2.5 py-1 rounded-lg font-tm09-mono text-xs text-tm09-ink bg-tm09-ctl border border-tm09-ctledge">04 / 06</span>
    <a href="#tm-09" aria-label="Close" class="absolute z-[2] top-4 right-4 grid place-items-center size-12 rounded-xl no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&times;</a>
  </div>

  <div id="tm-09-5" role="dialog" aria-modal="true" aria-label="Image 5 of 6" class="group fixed inset-0 z-20 grid place-items-center px-6 py-14 opacity-0 invisible transition-[opacity,visibility] duration-300 target:opacity-100 target:visible motion-reduce:transition-none">
    <a href="#tm-09" aria-label="Close" class="absolute inset-0 bg-tm09-scrim backdrop-blur-[6px]"></a>
    <a href="#tm-09-4" aria-label="Previous image" class="absolute z-[2] left-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&lsaquo;</a>
    <figure data-label="image 05" class="relative w-[min(620px,90vw)] aspect-[3/2] grid place-items-center rounded-2xl overflow-hidden border border-tm09-figedge bg-[repeating-linear-gradient(135deg,var(--color-tm09-figA)_0_18px,var(--color-tm09-figB)_18px_36px)] scale-90 transition-transform duration-300 group-target:scale-100 motion-reduce:transition-none before:content-[attr(data-label)] before:font-tm09-mono before:text-xs before:tracking-[0.2em] before:uppercase before:text-tm09-faint">
      <figcaption class="absolute inset-x-0 bottom-0 px-4.5 py-3.5 text-[13px] text-tm09-ink bg-[linear-gradient(transparent,var(--color-tm09-capscrim))]">Frame 05 &mdash; salt flats</figcaption>
    </figure>
    <a href="#tm-09-6" aria-label="Next image" class="absolute z-[2] right-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&rsaquo;</a>
    <span aria-hidden="true" class="absolute z-[2] top-5 left-5 px-2.5 py-1 rounded-lg font-tm09-mono text-xs text-tm09-ink bg-tm09-ctl border border-tm09-ctledge">05 / 06</span>
    <a href="#tm-09" aria-label="Close" class="absolute z-[2] top-4 right-4 grid place-items-center size-12 rounded-xl no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&times;</a>
  </div>

  <div id="tm-09-6" role="dialog" aria-modal="true" aria-label="Image 6 of 6" class="group fixed inset-0 z-20 grid place-items-center px-6 py-14 opacity-0 invisible transition-[opacity,visibility] duration-300 target:opacity-100 target:visible motion-reduce:transition-none">
    <a href="#tm-09" aria-label="Close" class="absolute inset-0 bg-tm09-scrim backdrop-blur-[6px]"></a>
    <a href="#tm-09-5" aria-label="Previous image" class="absolute z-[2] left-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&lsaquo;</a>
    <figure data-label="image 06" class="relative w-[min(620px,90vw)] aspect-[3/2] grid place-items-center rounded-2xl overflow-hidden border border-tm09-figedge bg-[repeating-linear-gradient(135deg,var(--color-tm09-figA)_0_18px,var(--color-tm09-figB)_18px_36px)] scale-90 transition-transform duration-300 group-target:scale-100 motion-reduce:transition-none before:content-[attr(data-label)] before:font-tm09-mono before:text-xs before:tracking-[0.2em] before:uppercase before:text-tm09-faint">
      <figcaption class="absolute inset-x-0 bottom-0 px-4.5 py-3.5 text-[13px] text-tm09-ink bg-[linear-gradient(transparent,var(--color-tm09-capscrim))]">Frame 06 &mdash; city dusk</figcaption>
    </figure>
    <a href="#tm-09-1" aria-label="Next image" class="absolute z-[2] right-4 top-1/2 -translate-y-1/2 grid place-items-center size-14 rounded-full no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&rsaquo;</a>
    <span aria-hidden="true" class="absolute z-[2] top-5 left-5 px-2.5 py-1 rounded-lg font-tm09-mono text-xs text-tm09-ink bg-tm09-ctl border border-tm09-ctledge">06 / 06</span>
    <a href="#tm-09" aria-label="Close" class="absolute z-[2] top-4 right-4 grid place-items-center size-12 rounded-xl no-underline text-2xl text-tm09-ink bg-tm09-ctl border border-tm09-ctledge transition-colors duration-200 hover:bg-tm09-ctlhover focus-visible:outline-2 focus-visible:outline-tm09-acc focus-visible:outline-offset-2">&times;</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm09-bg: #060709;
  --color-tm09-bg: oklch(0.14 0.01 240);
  --color-tm09-stripeA: #1a1f2a;
  --color-tm09-stripeA: oklch(0.23 0.015 250);
  --color-tm09-stripeB: #151a24;
  --color-tm09-stripeB: oklch(0.21 0.015 250);
  --color-tm09-figA: #1c2230;
  --color-tm09-figA: oklch(0.25 0.018 250);
  --color-tm09-figB: #161b27;
  --color-tm09-figB: oklch(0.22 0.018 250);
  --color-tm09-edge: #283040;
  --color-tm09-edge: oklch(0.29 0.018 250);
  --color-tm09-figedge: #303a4c;
  --color-tm09-figedge: oklch(0.34 0.02 250);
  --color-tm09-ctl: #141a24b3;
  --color-tm09-ctl: oklch(0.22 0.018 250 / 0.7);
  --color-tm09-ctlhover: #2b4550;
  --color-tm09-ctlhover: oklch(0.38 0.06 220);
  --color-tm09-ctledge: #333d50;
  --color-tm09-ctledge: oklch(0.35 0.02 250);
  --color-tm09-ink: #e8edf5;
  --color-tm09-ink: oklch(0.93 0.008 250);
  --color-tm09-faint: #7d8799;
  --color-tm09-faint: oklch(0.62 0.02 250);
  --color-tm09-acc: #6fd8e6;
  --color-tm09-acc: oklch(0.82 0.13 200);
  --color-tm09-scrim: #040609d1;
  --color-tm09-scrim: oklch(0.11 0.008 250 / 0.82);
  --color-tm09-capscrim: #06080cd9;
  --color-tm09-capscrim: oklch(0.13 0.01 250 / 0.85);
  --font-tm09-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm09-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tm-09 {
  width: 100%;
}
```
