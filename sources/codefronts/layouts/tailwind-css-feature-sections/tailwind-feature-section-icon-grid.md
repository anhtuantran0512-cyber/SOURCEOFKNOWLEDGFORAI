---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-icon-grid/"
title: "Tailwind Feature Section Icon Grid"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "The most-used feature layout, refined: six features in a hairline-ruled grid (gap-px over a tinted background), each with a gradient icon tile."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Section Icon Grid
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-icon-grid/

The most-used feature layout, refined: six features in a hairline-ruled grid (gap-px over a tinted background), each with a gradient icon tile. On hover a soft radial spotlight blooms from the icon corner and the arrow link slides in — all group-hover:, no extra elements.
## HTML
```html
<section class="tfs-13 w-full min-h-svh bg-tfs13-bg px-5 py-20 font-tfs13-sans text-tfs13-ink antialiased sm:py-28" aria-labelledby="tfs-13-h">
  <div class="mx-auto grid w-full max-w-6xl gap-14">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="mx-auto rounded-full bg-tfs13-acc/10 px-3 py-1 text-xs font-bold uppercase tracking-[0.16em] text-tfs13-acc">Features</p>
      <h2 id="tfs-13-h" class="text-balance text-4xl font-extrabold tracking-tight sm:text-5xl">Everything you need to ship a design system</h2>
      <p class="text-pretty text-lg text-tfs13-mut">Aperture keeps tokens, components and docs in lockstep — from Figma to production.</p>
    </header>
    <ul class="grid gap-px overflow-hidden rounded-3xl bg-tfs13-line ring-1 ring-tfs13-line sm:grid-cols-2 lg:grid-cols-3">
      <li class="group relative grid content-start gap-4 overflow-hidden bg-white p-8 transition">
        <span aria-hidden="true" class="pointer-events-none absolute -left-16 -top-16 size-64 rounded-full bg-tfs13-acc/10 opacity-0 blur-2xl transition duration-500 group-hover:opacity-100"></span>
        <span class="relative grid size-12 place-items-center rounded-2xl bg-linear-to-br from-indigo-500 to-violet-500 text-white shadow-lg ring-1 ring-inset ring-white/30 transition duration-300 group-hover:-rotate-6 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="m12 2 10 5-10 5L2 7l10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></span>
        <h3 class="relative text-lg font-bold">Token pipeline</h3>
        <p class="relative text-pretty text-tfs13-mut">Edit a colour in Figma; every platform gets a typed token by the next build.</p>
        <a href="#tfs-13-h" class="relative inline-flex min-h-11 w-fit -translate-x-1 items-center gap-1.5 text-sm font-semibold text-tfs13-acc opacity-70 transition group-hover:translate-x-0 group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs13-acc pointer-coarse:opacity-100">Learn more<span class="sr-only"> about Token pipeline</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
      <li class="group relative grid content-start gap-4 overflow-hidden bg-white p-8 transition">
        <span aria-hidden="true" class="pointer-events-none absolute -left-16 -top-16 size-64 rounded-full bg-tfs13-acc/10 opacity-0 blur-2xl transition duration-500 group-hover:opacity-100"></span>
        <span class="relative grid size-12 place-items-center rounded-2xl bg-linear-to-br from-sky-500 to-cyan-400 text-white shadow-lg ring-1 ring-inset ring-white/30 transition duration-300 group-hover:-rotate-6 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/></svg></span>
        <h3 class="relative text-lg font-bold">Component codegen</h3>
        <p class="relative text-pretty text-tfs13-mut">React, Vue and SwiftUI stubs generated from the same spec.</p>
        <a href="#tfs-13-h" class="relative inline-flex min-h-11 w-fit -translate-x-1 items-center gap-1.5 text-sm font-semibold text-tfs13-acc opacity-70 transition group-hover:translate-x-0 group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs13-acc pointer-coarse:opacity-100">Learn more<span class="sr-only"> about Component codegen</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
      <li class="group relative grid content-start gap-4 overflow-hidden bg-white p-8 transition">
        <span aria-hidden="true" class="pointer-events-none absolute -left-16 -top-16 size-64 rounded-full bg-tfs13-acc/10 opacity-0 blur-2xl transition duration-500 group-hover:opacity-100"></span>
        <span class="relative grid size-12 place-items-center rounded-2xl bg-linear-to-br from-rose-500 to-orange-400 text-white shadow-lg ring-1 ring-inset ring-white/30 transition duration-300 group-hover:-rotate-6 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12zM12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/></svg></span>
        <h3 class="relative text-lg font-bold">Visual regression</h3>
        <p class="relative text-pretty text-tfs13-mut">Every PR screenshots 400 states and flags the 3 that changed.</p>
        <a href="#tfs-13-h" class="relative inline-flex min-h-11 w-fit -translate-x-1 items-center gap-1.5 text-sm font-semibold text-tfs13-acc opacity-70 transition group-hover:translate-x-0 group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs13-acc pointer-coarse:opacity-100">Learn more<span class="sr-only"> about Visual regression</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
      <li class="group relative grid content-start gap-4 overflow-hidden bg-white p-8 transition">
        <span aria-hidden="true" class="pointer-events-none absolute -left-16 -top-16 size-64 rounded-full bg-tfs13-acc/10 opacity-0 blur-2xl transition duration-500 group-hover:opacity-100"></span>
        <span class="relative grid size-12 place-items-center rounded-2xl bg-linear-to-br from-emerald-500 to-teal-400 text-white shadow-lg ring-1 ring-inset ring-white/30 transition duration-300 group-hover:-rotate-6 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span>
        <h3 class="relative text-lg font-bold">Contribution flow</h3>
        <p class="relative text-pretty text-tfs13-mut">Propose, review and merge new components without leaving the docs.</p>
        <a href="#tfs-13-h" class="relative inline-flex min-h-11 w-fit -translate-x-1 items-center gap-1.5 text-sm font-semibold text-tfs13-acc opacity-70 transition group-hover:translate-x-0 group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs13-acc pointer-coarse:opacity-100">Learn more<span class="sr-only"> about Contribution flow</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
      <li class="group relative grid content-start gap-4 overflow-hidden bg-white p-8 transition">
        <span aria-hidden="true" class="pointer-events-none absolute -left-16 -top-16 size-64 rounded-full bg-tfs13-acc/10 opacity-0 blur-2xl transition duration-500 group-hover:opacity-100"></span>
        <span class="relative grid size-12 place-items-center rounded-2xl bg-linear-to-br from-amber-500 to-yellow-400 text-white shadow-lg ring-1 ring-inset ring-white/30 transition duration-300 group-hover:-rotate-6 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.3-4.3"/></svg></span>
        <h3 class="relative text-lg font-bold">Usage analytics</h3>
        <p class="relative text-pretty text-tfs13-mut">See where each component ships and which props nobody uses.</p>
        <a href="#tfs-13-h" class="relative inline-flex min-h-11 w-fit -translate-x-1 items-center gap-1.5 text-sm font-semibold text-tfs13-acc opacity-70 transition group-hover:translate-x-0 group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs13-acc pointer-coarse:opacity-100">Learn more<span class="sr-only"> about Usage analytics</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
      <li class="group relative grid content-start gap-4 overflow-hidden bg-white p-8 transition">
        <span aria-hidden="true" class="pointer-events-none absolute -left-16 -top-16 size-64 rounded-full bg-tfs13-acc/10 opacity-0 blur-2xl transition duration-500 group-hover:opacity-100"></span>
        <span class="relative grid size-12 place-items-center rounded-2xl bg-linear-to-br from-fuchsia-500 to-pink-500 text-white shadow-lg ring-1 ring-inset ring-white/30 transition duration-300 group-hover:-rotate-6 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span>
        <h3 class="relative text-lg font-bold">Accessibility lint</h3>
        <p class="relative text-pretty text-tfs13-mut">Contrast, focus order and ARIA checked on every change.</p>
        <a href="#tfs-13-h" class="relative inline-flex min-h-11 w-fit -translate-x-1 items-center gap-1.5 text-sm font-semibold text-tfs13-acc opacity-70 transition group-hover:translate-x-0 group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs13-acc pointer-coarse:opacity-100">Learn more<span class="sr-only"> about Accessibility lint</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs13-bg: #f8f8fc;
  --color-tfs13-bg: oklch(0.98 0.005 286);
  --color-tfs13-ink: #111827;
  --color-tfs13-ink: oklch(0.21 0.032 265);
  --color-tfs13-mut: #4b5563;
  --color-tfs13-mut: oklch(0.446 0.026 257);
  --color-tfs13-line: #e5e7f0;
  --color-tfs13-line: oklch(0.929 0.012 276);
  --color-tfs13-acc: #4f46e5;
  --color-tfs13-acc: oklch(0.511 0.23 277);
  --font-tfs13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-13 {
  width: 100%;
  min-height: 100svh;
}
```
