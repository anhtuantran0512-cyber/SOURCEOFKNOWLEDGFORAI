---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-logo-for-navbar/"
title: "Tailwind Gradient Text Logo for Navbar"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "An image-free wordmark: Spectr in solid ink, um in a bg-linear-120 gradient, inside a responsive navbar."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Text Logo for Navbar
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-logo-for-navbar/

An image-free wordmark: Spectr in solid ink, um in a bg-linear-120 gradient, inside a responsive navbar. The specimen row proves the logo is resolution-independent from 20px to 56px &mdash; and a dark tile shows the same markup on an inverted surface. Zero HTTP requests, perfectly sharp on every DPI.
## HTML
```html
<section class="ttg-03 w-full min-h-svh bg-ttg03-bg font-ttg03-sans text-ttg03-ink" aria-label="Gradient text navbar logo demo">
  <svg width="0" height="0" class="absolute" aria-hidden="true"><defs><linearGradient id="ttg03-g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--color-ttg03-a)"/><stop offset="1" style="stop-color:var(--color-ttg03-b)"/></linearGradient></defs></svg>
  <header class="sticky top-0 z-10 border-b border-ttg03-line bg-white/80 backdrop-blur-md">
    <nav class="mx-auto flex h-16 max-w-5xl items-center gap-8 px-6" aria-label="Main">
      <a href="#" class="flex items-center gap-2.5 rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ttg03-a" aria-label="Spectrum home">
        <svg class="size-7" viewBox="0 0 28 28" aria-hidden="true"><path d="M14 2 26 14 14 26 2 14Z" fill="url(#ttg03-g)"/><path d="M14 8.5 19.5 14 14 19.5 8.5 14Z" fill="#fff"/></svg>
        <span class="text-[21px] font-extrabold tracking-[-0.035em]">Spectr<span class="bg-linear-120 from-ttg03-a to-ttg03-b bg-clip-text text-transparent">um</span></span>
      </a>
      <ul class="flex gap-1 max-sm:hidden">
        <li><a href="#" class="inline-flex min-h-11 items-center rounded-lg px-3 text-[14.5px] font-medium text-ttg03-mut transition-colors hover:bg-ttg03-ink/5 hover:text-ttg03-ink">Product</a></li>
        <li><a href="#" class="inline-flex min-h-11 items-center rounded-lg px-3 text-[14.5px] font-medium text-ttg03-mut transition-colors hover:bg-ttg03-ink/5 hover:text-ttg03-ink">Pricing</a></li>
        <li><a href="#" class="inline-flex min-h-11 items-center rounded-lg px-3 text-[14.5px] font-medium text-ttg03-mut transition-colors hover:bg-ttg03-ink/5 hover:text-ttg03-ink">Customers</a></li>
      </ul>
      <a href="#" class="ml-auto inline-flex min-h-11 items-center rounded-xl bg-linear-120 from-ttg03-a to-ttg03-b px-5 text-sm font-bold text-white shadow-[0_8px_20px_-8px_var(--color-ttg03-a)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg03-a">Get started</a>
    </nav>
  </header>
  <div class="mx-auto max-w-5xl px-6 py-14">
    <p class="text-xs font-bold tracking-[0.16em] text-ttg03-mut uppercase">Wordmark scale</p>
    <div class="mt-6 grid gap-4 sm:grid-cols-[1fr_1fr_1.4fr]">
      <div class="grid min-h-36 place-items-center rounded-2xl border border-ttg03-line bg-white"><span class="text-xl font-extrabold tracking-[-0.035em]">Spectr<span class="bg-linear-120 from-ttg03-a to-ttg03-b bg-clip-text text-transparent">um</span></span></div>
      <div class="grid min-h-36 place-items-center rounded-2xl border border-ttg03-line bg-white"><span class="text-[32px] font-extrabold tracking-[-0.035em]">Spectr<span class="bg-linear-120 from-ttg03-a to-ttg03-b bg-clip-text text-transparent">um</span></span></div>
      <div class="grid min-h-36 place-items-center rounded-2xl bg-ttg03-ink"><span class="text-[clamp(36px,5vw,56px)] font-extrabold tracking-[-0.04em] text-white">Spectr<span class="bg-linear-120 from-ttg03-a2 to-ttg03-b2 bg-clip-text text-transparent">um</span></span></div>
    </div>
    <div class="mt-8 flex max-w-xl gap-4">
      <span aria-hidden="true" class="w-[3px] flex-none rounded-full bg-linear-to-b from-ttg03-a to-ttg03-b"></span>
      <p class="text-[15px]/[1.7] text-ttg03-mut text-pretty">Gradient text is image-free: it scales infinitely, renders crisply on every DPI and costs zero HTTP requests. On dark surfaces, swap to the lighter <code class="rounded bg-ttg03-ink/5 px-1.5 py-0.5 text-[13px] text-ttg03-ink">-a2 / -b2</code> stops.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg03-bg: #f6f7fb;
  --color-ttg03-bg: oklch(0.975 0.006 270);
  --color-ttg03-ink: #10131f;
  --color-ttg03-ink: oklch(0.2 0.025 270);
  --color-ttg03-mut: #545b70;
  --color-ttg03-mut: oklch(0.47 0.03 270);
  --color-ttg03-line: #e3e5ee;
  --color-ttg03-line: oklch(0.92 0.01 270);
  --color-ttg03-a: #5458ee;
  --color-ttg03-a: oklch(0.55 0.21 275);
  --color-ttg03-b: #a640e8;
  --color-ttg03-b: oklch(0.58 0.24 305);
  --color-ttg03-a2: #8fa0ff;
  --color-ttg03-a2: oklch(0.74 0.14 275);
  --color-ttg03-b2: #e091ff;
  --color-ttg03-b2: oklch(0.78 0.16 315);
  --font-ttg03-sans: 'Manrope', system-ui, sans-serif;
}

.ttg-03 {
  width: 100%;
  min-height: 100svh;
}
```
