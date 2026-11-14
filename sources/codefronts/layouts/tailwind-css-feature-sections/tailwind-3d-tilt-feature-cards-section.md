---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-3d-tilt-feature-cards-section/"
title: "Tailwind 3D Tilt Feature Cards Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "Three feature cards resting in a gentle 3D tilt that straighten and lift toward you on hover or focus, with inner layers (icon, title, glow) floating at…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Feature Cards Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-3d-tilt-feature-cards-section/

Three feature cards resting in a gentle 3D tilt that straighten and lift toward you on hover or focus, with inner layers (icon, title, glow) floating at different depths. Built entirely on v4's native 3D utilities — perspective-distant, transform-3d, rotate-y-*, translate-z-*.
## HTML
```html
<section class="tfs-20 relative w-full min-h-svh overflow-hidden bg-tfs20-bg px-5 py-20 font-tfs20-sans text-white antialiased sm:py-28" aria-labelledby="tfs-20-h">
  <div aria-hidden="true" class="absolute inset-x-0 bottom-0 h-1/2 bg-[linear-gradient(to_right,rgb(255_255_255/0.06)_1px,transparent_1px),linear-gradient(to_bottom,rgb(255_255_255/0.06)_1px,transparent_1px)] bg-size-[48px_48px] [mask-image:linear-gradient(to_top,black,transparent)] [transform:perspective(600px)_rotateX(60deg)] origin-bottom"></div>
  <div class="relative mx-auto grid w-full max-w-6xl gap-16">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="text-sm font-medium text-tfs20-acc">Prism Engine</p>
      <h2 id="tfs-20-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-6xl">Depth for every pixel you ship</h2>
    </header>
    <ul class="grid gap-8 perspective-distant md:grid-cols-3">
      <li class="group relative grid gap-5 rounded-3xl bg-tfs20-card p-8 ring-1 ring-white/10 transform-3d rotate-x-6 rotate-y-12 transition duration-500 ease-out hover:rotate-x-0 hover:rotate-y-0 hover:translate-z-8 hover:ring-tfs20-acc/50 focus-within:rotate-x-0 focus-within:rotate-y-0 focus-within:translate-z-8 motion-reduce:transform-none motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 -z-10 rounded-3xl bg-linear-to-br from-fuchsia-500 to-violet-600 opacity-0 blur-2xl transition duration-500 -translate-z-10 group-hover:opacity-50"></span>
        <span class="grid size-14 place-items-center rounded-2xl bg-linear-to-br from-fuchsia-500 to-violet-600 text-white shadow-[0_20px_40px_-12px_rgb(0_0_0/0.6)] translate-z-12"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M6 6h12v12H6zM9 9h6v6H9zM9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg></span>
        <h3 class="text-2xl font-semibold translate-z-6">Spatial rendering</h3>
        <p class="text-pretty text-tfs20-mut translate-z-4">Physically based lighting in the browser at 120 fps.</p>
        <a href="#tfs-20-h" class="inline-flex min-h-11 w-fit items-center gap-2 text-sm font-semibold text-tfs20-acc translate-z-4 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tfs20-acc">Explore<span class="sr-only"> Spatial rendering</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-hover:translate-x-1"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
      <li class="group relative grid gap-5 rounded-3xl bg-tfs20-card p-8 ring-1 ring-white/10 transform-3d rotate-x-6 transition duration-500 ease-out hover:rotate-x-0 hover:rotate-y-0 hover:translate-z-8 hover:ring-tfs20-acc/50 focus-within:rotate-x-0 focus-within:rotate-y-0 focus-within:translate-z-8 motion-reduce:transform-none motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 -z-10 rounded-3xl bg-linear-to-br from-violet-500 to-indigo-600 opacity-0 blur-2xl transition duration-500 -translate-z-10 group-hover:opacity-50"></span>
        <span class="grid size-14 place-items-center rounded-2xl bg-linear-to-br from-violet-500 to-indigo-600 text-white shadow-[0_20px_40px_-12px_rgb(0_0_0/0.6)] translate-z-12"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="m12 2 10 5-10 5L2 7l10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></span>
        <h3 class="text-2xl font-semibold translate-z-6">Scene graph API</h3>
        <p class="text-pretty text-tfs20-mut translate-z-4">Compose 3D scenes declaratively, like components.</p>
        <a href="#tfs-20-h" class="inline-flex min-h-11 w-fit items-center gap-2 text-sm font-semibold text-tfs20-acc translate-z-4 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tfs20-acc">Explore<span class="sr-only"> Scene graph API</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-hover:translate-x-1"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
      <li class="group relative grid gap-5 rounded-3xl bg-tfs20-card p-8 ring-1 ring-white/10 transform-3d rotate-x-6 -rotate-y-12 transition duration-500 ease-out hover:rotate-x-0 hover:rotate-y-0 hover:translate-z-8 hover:ring-tfs20-acc/50 focus-within:rotate-x-0 focus-within:rotate-y-0 focus-within:translate-z-8 motion-reduce:transform-none motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 -z-10 rounded-3xl bg-linear-to-br from-indigo-500 to-cyan-500 opacity-0 blur-2xl transition duration-500 -translate-z-10 group-hover:opacity-50"></span>
        <span class="grid size-14 place-items-center rounded-2xl bg-linear-to-br from-indigo-500 to-cyan-500 text-white shadow-[0_20px_40px_-12px_rgb(0_0_0/0.6)] translate-z-12"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg></span>
        <h3 class="text-2xl font-semibold translate-z-6">Edge streaming</h3>
        <p class="text-pretty text-tfs20-mut translate-z-4">Assets stream progressively from 300 PoPs.</p>
        <a href="#tfs-20-h" class="inline-flex min-h-11 w-fit items-center gap-2 text-sm font-semibold text-tfs20-acc translate-z-4 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tfs20-acc">Explore<span class="sr-only"> Edge streaming</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-hover:translate-x-1"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs20-bg: #0a0714;
  --color-tfs20-bg: oklch(0.141 0.029 294);
  --color-tfs20-card: #151026;
  --color-tfs20-card: oklch(0.192 0.044 292);
  --color-tfs20-mut: #bdb4d8;
  --color-tfs20-mut: oklch(0.789 0.051 297);
  --color-tfs20-acc: #c4b5fd;
  --color-tfs20-acc: oklch(0.811 0.101 294);
  --font-tfs20-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-20 {
  width: 100%;
  min-height: 100svh;
}
```
