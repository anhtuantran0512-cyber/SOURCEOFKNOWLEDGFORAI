---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-brutalist-hero-section/"
title: "Brutalist Hero Section in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "Raw Swiss-punk brutalism — pure black, traffic-cone orange highlight, acid-lime italic, hard 8px offset shadows that collapse on press, and a mono index line."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Hero Section in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-brutalist-hero-section/

Raw Swiss-punk brutalism — pure black, traffic-cone orange highlight, acid-lime italic, hard 8px offset shadows that collapse on press, and a mono index line. No images, no gradients, no soft anything.
## HTML
```html
<section class="ths-16 grid w-full min-h-svh place-items-center bg-ths16-bg px-5 py-16 font-ths16-sans text-white sm:px-14" aria-label="Brutalist hero">
  <div class="w-full max-w-[52rem]">
    <div class="flex flex-wrap items-center justify-between gap-3">
      <span class="bg-ths16-orange px-2.5 py-1 font-ths16-mono text-xs font-bold tracking-[0.2em] text-ths16-bg">001 / 042</span>
      <span class="font-ths16-mono text-xs tracking-[0.2em] text-ths16-mut">STUDIO — BERLIN / NYC</span>
    </div>
    <h1 class="mt-7 text-[clamp(44px,8vw,96px)] leading-[0.9] font-bold tracking-[-0.045em] uppercase">The web <em class="text-ths16-lime">was never</em> meant to <span class="mt-2 inline-block -rotate-1 bg-ths16-orange px-3 text-ths16-bg">look safe.</span></h1>
    <div class="mt-8 grid gap-8 border-t-2 border-ths16-orange pt-6 md:grid-cols-[1fr_auto]">
      <p class="max-w-md font-ths16-mono text-sm leading-relaxed text-ths16-mut">A design studio for brands that would rather be remembered than liked.</p>
      <dl class="grid grid-cols-[auto_1fr] gap-x-6 gap-y-1 font-ths16-mono text-xs text-ths16-mut">
        <dt>Founded</dt><dd class="text-white">2014</dd>
        <dt>Shipped</dt><dd class="text-white">212 brands</dd>
        <dt>Awards</dt><dd class="text-white">0 wanted</dd>
      </dl>
    </div>
    <div class="mt-9 flex flex-wrap gap-5">
      <a href="#work" class="inline-flex min-h-12 items-center border-2 border-ths16-orange bg-ths16-orange px-6 font-ths16-mono text-sm font-bold tracking-[0.12em] text-ths16-bg shadow-[8px_8px_0_var(--color-ths16-lime)] transition-[translate,box-shadow,background-color] duration-100 hover:translate-x-1 hover:translate-y-1 hover:shadow-[4px_4px_0_var(--color-ths16-lime)] active:translate-x-2 active:translate-y-2 active:shadow-none focus-visible:outline-3 focus-visible:outline-offset-[12px] focus-visible:outline-white motion-reduce:transition-none">[ SEE WORK ]</a>
      <a href="#talk" class="inline-flex min-h-12 items-center border-2 border-white px-6 font-ths16-mono text-sm font-bold tracking-[0.12em] text-white shadow-[8px_8px_0_white] transition-[translate,box-shadow,background-color] duration-100 hover:translate-x-1 hover:translate-y-1 hover:bg-white hover:text-ths16-bg hover:shadow-[4px_4px_0_var(--color-ths16-orange)] active:translate-x-2 active:translate-y-2 active:shadow-none focus-visible:outline-3 focus-visible:outline-offset-[12px] focus-visible:outline-ths16-lime motion-reduce:transition-none">[ EMAIL ]</a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths16-bg: #0a0a0a;
  --color-ths16-bg: oklch(0.145 0 0);
  --color-ths16-mut: #b5b5b5;
  --color-ths16-mut: oklch(0.773 0 0);
  --color-ths16-orange: #ff5e1a;
  --color-ths16-orange: oklch(0.687 0.208 39.4);
  --color-ths16-lime: #c4f048;
  --color-ths16-lime: oklch(0.894 0.194 123.2);
  --font-ths16-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-ths16-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-16 {
  width: 100%;
  min-height: 100svh;
}
```
