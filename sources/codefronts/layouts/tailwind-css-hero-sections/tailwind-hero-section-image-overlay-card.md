---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-image-overlay-card/"
title: "Tailwind CSS Hero Section with Image & Overlay Card"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "An Aesop-style editorial product hero — a moody, CSS-lit still life of a chore coat on a peg (swap in your photo), with a linen copy card anchored…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Hero Section with Image & Overlay Card
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-image-overlay-card/

An Aesop-style editorial product hero — a moody, CSS-lit still life of a chore coat on a peg (swap in your photo), with a linen copy card anchored bottom-right and a catalogue meta line. Desaturated denim, rust accent.
## HTML
```html
<section class="ths-15 relative isolate grid w-full min-h-svh overflow-hidden bg-linear-to-b from-ths15-wall via-ths15-wall2 to-ths15-floor font-ths15-sans text-ths15-linen md:grid-cols-[1.05fr_1fr]" aria-label="Product hero with image and overlay card">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[repeating-linear-gradient(95deg,transparent_0_80px,rgb(255_255_255/0.02)_80px_81px),repeating-linear-gradient(0deg,transparent_0_4px,rgb(0_0_0/0.06)_4px_5px)]"></div>
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(40%_60%_at_30%_25%,rgb(255_230_180/0.18),transparent_60%),radial-gradient(80%_100%_at_50%_100%,rgb(0_0_0/0.5),transparent_70%)]"></div>
  <div aria-hidden="true" class="relative min-h-[320px]">
    <span class="absolute inset-x-[18%] top-[18%] h-2 rounded-sm bg-linear-to-b from-ths15-wood to-ths15-wood2 shadow-[inset_0_1px_0_rgb(255_255_255/0.08),0_4px_8px_rgb(0_0_0/0.35)]"></span>
    <span class="absolute top-[16%] left-1/2 z-10 h-[26px] w-3.5 -translate-x-1/2 rounded-t-md rounded-b bg-linear-to-b from-ths15-brass to-ths15-brass2 shadow-[0_2px_4px_rgb(0_0_0/0.4)]"></span>
    <div class="absolute top-[22%] left-1/2 h-[min(280px,52svh)] w-[min(200px,40vw)] -translate-x-1/2 bg-[radial-gradient(80%_100%_at_50%_0%,var(--color-ths15-denim),var(--color-ths15-denim2)_50%,var(--color-ths15-denim3))] shadow-[inset_-8px_0_24px_rgb(0_0_0/0.4),inset_8px_0_16px_rgb(255_255_255/0.04)] [clip-path:polygon(35%_0,65%_0,78%_8%,95%_14%,100%_100%,0_100%,5%_14%,22%_8%)]">
      <span class="absolute top-[4%] left-1/2 h-6 w-14 -translate-x-1/2 bg-ths15-collar [clip-path:polygon(0_0,100%_0,75%_100%,25%_100%)]"></span>
      <span class="absolute top-1/2 left-[14%] h-[60px] w-[25%] rounded-sm border-[1.5px] border-ths15-seam bg-black/18"></span>
      <span class="absolute top-1/2 right-[14%] h-[60px] w-[25%] rounded-sm border-[1.5px] border-ths15-seam bg-black/18"></span>
      <span class="absolute top-[22%] left-1/2 size-2 -translate-x-1/2 rounded-full bg-[radial-gradient(circle_at_35%_35%,var(--color-ths15-brass),#6a4818)]"></span>
      <span class="absolute top-[40%] left-1/2 size-2 -translate-x-1/2 rounded-full bg-[radial-gradient(circle_at_35%_35%,var(--color-ths15-brass),#6a4818)]"></span>
      <span class="absolute top-[58%] left-1/2 size-2 -translate-x-1/2 rounded-full bg-[radial-gradient(circle_at_35%_35%,var(--color-ths15-brass),#6a4818)]"></span>
    </div>
    <!-- Real photo: replace this block's children with <img src="coat.jpg" alt="" class="absolute inset-0 size-full object-cover"> -->
  </div>
  <div class="relative z-10 flex items-end px-4 pb-16 md:px-0 md:pr-10 md:pb-14">
    <article class="-mt-10 w-full max-w-[28rem] rounded-sm bg-ths15-linen p-7 text-ths15-navy shadow-[0_24px_48px_rgb(0_0_0/0.35)] transition duration-700 starting:translate-y-4 starting:opacity-0 md:mt-0 sm:p-9">
      <span class="block font-ths15-serif text-base text-ths15-rust italic">— A garment for the long haul</span>
      <h1 class="mt-2 font-ths15-serif text-[clamp(32px,3.8vw,46px)] leading-[1.06] font-semibold tracking-[-0.01em]">The chore coat, <em class="text-ths15-rust">made to age.</em></h1>
      <p class="mt-4 text-[15px] leading-relaxed text-ths15-body">Heavy duck canvas. Rivet-tacked seams. The kind of jacket that earns its character on the wearer, not in the wash.</p>
      <div class="mt-6 flex flex-wrap items-center gap-x-6 gap-y-3">
        <a href="#shop" class="inline-flex min-h-11 items-center bg-ths15-navy px-5 text-sm font-semibold text-ths15-linen transition hover:bg-ths15-rust focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths15-navy motion-reduce:transition-none">Shop — $248</a>
        <a href="#story" class="inline-flex min-h-11 items-center border-b-[1.5px] border-ths15-navy font-ths15-mono text-xs font-bold tracking-[0.16em] uppercase transition hover:border-ths15-rust hover:text-ths15-rust focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths15-navy">Read the story →</a>
      </div>
    </article>
  </div>
  <span aria-hidden="true" class="absolute bottom-5 left-6 z-10 hidden font-ths15-mono text-[10px] tracking-[0.18em] text-ths15-meta md:block">N°04 — DUCK CANVAS WORKWEAR · MADE IN PORTUGAL</span>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths15-wall: #2c3a48;
  --color-ths15-wall: oklch(0.342 0.031 248.7);
  --color-ths15-wall2: #1f2a35;
  --color-ths15-wall2: oklch(0.28 0.025 248.8);
  --color-ths15-floor: #15202a;
  --color-ths15-floor: oklch(0.238 0.025 246.5);
  --color-ths15-linen: #f3eadb;
  --color-ths15-linen: oklch(0.94 0.022 80.7);
  --color-ths15-navy: #1a2434;
  --color-ths15-navy: oklch(0.259 0.034 259.6);
  --color-ths15-body: #434d5f;
  --color-ths15-body: oklch(0.419 0.033 262.1);
  --color-ths15-rust: #a8481c;
  --color-ths15-rust: oklch(0.521 0.138 42.4);
  --color-ths15-meta: #b5ad9f;
  --color-ths15-meta: oklch(0.75 0.022 81.8);
  --color-ths15-wood: #5a3e22;
  --color-ths15-wood: oklch(0.389 0.057 64.7);
  --color-ths15-wood2: #3a2814;
  --color-ths15-wood2: oklch(0.293 0.042 67.9);
  --color-ths15-brass: #c89a4e;
  --color-ths15-brass: oklch(0.714 0.109 78.1);
  --color-ths15-brass2: #7a5a2e;
  --color-ths15-brass2: oklch(0.491 0.074 73.4);
  --color-ths15-denim: #4a5e7a;
  --color-ths15-denim: oklch(0.477 0.052 256.8);
  --color-ths15-denim2: #34465c;
  --color-ths15-denim2: oklch(0.388 0.044 253.8);
  --color-ths15-denim3: #1f2a3a;
  --color-ths15-denim3: oklch(0.282 0.033 257.7);
  --color-ths15-collar: #5a708c;
  --color-ths15-collar: oklch(0.538 0.051 254.7);
  --color-ths15-seam: #2a3848;
  --color-ths15-seam: oklch(0.335 0.034 252.2);
  --font-ths15-serif: 'Cormorant Garamond', Georgia, serif;
  --font-ths15-sans: 'Geist', system-ui, sans-serif;
  --font-ths15-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-15 {
  width: 100%;
  min-height: 100svh;
}
```
