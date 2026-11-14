---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-cards-with-scroll-reveal/"
title: "Tailwind Feature Cards with Scroll Reveal"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "Six feature cards that rise into place as they enter the viewport — no IntersectionObserver, no AOS library."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Cards with Scroll Reveal
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-cards-with-scroll-reveal/

Six feature cards that rise into place as they enter the viewport — no IntersectionObserver, no AOS library. Each card runs a keyframe on its own view() timeline via arbitrary properties; engines without scroll timelines fall back to a one-time starting: entry, and reduced motion shows everything settled.
## HTML
```html
<section class="tfs-16 w-full min-h-svh bg-tfs16-bg px-5 py-20 font-tfs16-sans text-tfs16-ink antialiased sm:py-28" aria-labelledby="tfs-16-h">
  <div class="mx-auto grid w-full max-w-6xl gap-14">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="text-sm font-semibold text-tfs16-acc">Why Fern Health</p>
      <h2 id="tfs-16-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">Care that fits around your life</h2>
      <p class="text-pretty text-lg text-tfs16-mut">Scroll on — each card arrives as you reach it.</p>
    </header>
    <ul class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      <li class="group grid gap-5 overflow-hidden rounded-3xl bg-white p-2 shadow-[0_20px_50px_-30px_rgb(15_60_60/0.35)] ring-1 ring-tfs16-line transition duration-700 ease-out starting:translate-y-6 starting:opacity-0 hover:-translate-y-1 hover:shadow-[0_30px_60px_-30px_rgb(15_60_60/0.45)] supports-[animation-timeline:view()]:animate-tfs16-rise supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_0%_entry_80%] supports-[animation-timeline:view()]:nth-[3n+2]:[animation-range:entry_10%_entry_90%] supports-[animation-timeline:view()]:nth-[3n]:[animation-range:entry_20%_entry_100%] motion-reduce:animate-none motion-reduce:transition-none">
        <div class="relative grid h-36 place-items-center overflow-hidden rounded-[1.25rem] bg-tfs16-soft"><span class="absolute size-40 rounded-full bg-teal-500 opacity-20 blur-2xl transition duration-500 group-hover:scale-125"></span><span class="relative grid size-14 place-items-center rounded-2xl bg-teal-500 text-white shadow-lg transition duration-500 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM12 6v6l4 2"/></svg></span></div>
        <div class="grid gap-2 px-5 pb-6"><h3 class="text-xl font-semibold">Same-day visits</h3><p class="text-pretty text-tfs16-mut">Video appointments within four hours, 7 days a week.</p></div>
      </li>
      <li class="group grid gap-5 overflow-hidden rounded-3xl bg-white p-2 shadow-[0_20px_50px_-30px_rgb(15_60_60/0.35)] ring-1 ring-tfs16-line transition duration-700 ease-out starting:translate-y-6 starting:opacity-0 hover:-translate-y-1 hover:shadow-[0_30px_60px_-30px_rgb(15_60_60/0.45)] supports-[animation-timeline:view()]:animate-tfs16-rise supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_0%_entry_80%] supports-[animation-timeline:view()]:nth-[3n+2]:[animation-range:entry_10%_entry_90%] supports-[animation-timeline:view()]:nth-[3n]:[animation-range:entry_20%_entry_100%] motion-reduce:animate-none motion-reduce:transition-none">
        <div class="relative grid h-36 place-items-center overflow-hidden rounded-[1.25rem] bg-tfs16-soft"><span class="absolute size-40 rounded-full bg-sky-500 opacity-20 blur-2xl transition duration-500 group-hover:scale-125"></span><span class="relative grid size-14 place-items-center rounded-2xl bg-sky-500 text-white shadow-lg transition duration-500 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span></div>
        <div class="grid gap-2 px-5 pb-6"><h3 class="text-xl font-semibold">Your own care team</h3><p class="text-pretty text-tfs16-mut">A named doctor, nurse and coach who know your history.</p></div>
      </li>
      <li class="group grid gap-5 overflow-hidden rounded-3xl bg-white p-2 shadow-[0_20px_50px_-30px_rgb(15_60_60/0.35)] ring-1 ring-tfs16-line transition duration-700 ease-out starting:translate-y-6 starting:opacity-0 hover:-translate-y-1 hover:shadow-[0_30px_60px_-30px_rgb(15_60_60/0.45)] supports-[animation-timeline:view()]:animate-tfs16-rise supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_0%_entry_80%] supports-[animation-timeline:view()]:nth-[3n+2]:[animation-range:entry_10%_entry_90%] supports-[animation-timeline:view()]:nth-[3n]:[animation-range:entry_20%_entry_100%] motion-reduce:animate-none motion-reduce:transition-none">
        <div class="relative grid h-36 place-items-center overflow-hidden rounded-[1.25rem] bg-tfs16-soft"><span class="absolute size-40 rounded-full bg-violet-500 opacity-20 blur-2xl transition duration-500 group-hover:scale-125"></span><span class="relative grid size-14 place-items-center rounded-2xl bg-violet-500 text-white shadow-lg transition duration-500 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg></span></div>
        <div class="grid gap-2 px-5 pb-6"><h3 class="text-xl font-semibold">Smart reminders</h3><p class="text-pretty text-tfs16-mut">Medication nudges that adapt to your routine.</p></div>
      </li>
      <li class="group grid gap-5 overflow-hidden rounded-3xl bg-white p-2 shadow-[0_20px_50px_-30px_rgb(15_60_60/0.35)] ring-1 ring-tfs16-line transition duration-700 ease-out starting:translate-y-6 starting:opacity-0 hover:-translate-y-1 hover:shadow-[0_30px_60px_-30px_rgb(15_60_60/0.45)] supports-[animation-timeline:view()]:animate-tfs16-rise supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_0%_entry_80%] supports-[animation-timeline:view()]:nth-[3n+2]:[animation-range:entry_10%_entry_90%] supports-[animation-timeline:view()]:nth-[3n]:[animation-range:entry_20%_entry_100%] motion-reduce:animate-none motion-reduce:transition-none">
        <div class="relative grid h-36 place-items-center overflow-hidden rounded-[1.25rem] bg-tfs16-soft"><span class="absolute size-40 rounded-full bg-rose-500 opacity-20 blur-2xl transition duration-500 group-hover:scale-125"></span><span class="relative grid size-14 place-items-center rounded-2xl bg-rose-500 text-white shadow-lg transition duration-500 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M7 11V7a5 5 0 0 1 10 0v4M5 11h14v10H5z"/></svg></span></div>
        <div class="grid gap-2 px-5 pb-6"><h3 class="text-xl font-semibold">Private by design</h3><p class="text-pretty text-tfs16-mut">HIPAA-compliant, end-to-end encrypted messaging.</p></div>
      </li>
      <li class="group grid gap-5 overflow-hidden rounded-3xl bg-white p-2 shadow-[0_20px_50px_-30px_rgb(15_60_60/0.35)] ring-1 ring-tfs16-line transition duration-700 ease-out starting:translate-y-6 starting:opacity-0 hover:-translate-y-1 hover:shadow-[0_30px_60px_-30px_rgb(15_60_60/0.45)] supports-[animation-timeline:view()]:animate-tfs16-rise supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_0%_entry_80%] supports-[animation-timeline:view()]:nth-[3n+2]:[animation-range:entry_10%_entry_90%] supports-[animation-timeline:view()]:nth-[3n]:[animation-range:entry_20%_entry_100%] motion-reduce:animate-none motion-reduce:transition-none">
        <div class="relative grid h-36 place-items-center overflow-hidden rounded-[1.25rem] bg-tfs16-soft"><span class="absolute size-40 rounded-full bg-amber-500 opacity-20 blur-2xl transition duration-500 group-hover:scale-125"></span><span class="relative grid size-14 place-items-center rounded-2xl bg-amber-500 text-white shadow-lg transition duration-500 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M3 3v18h18M7 15l4-4 3 3 5-6"/></svg></span></div>
        <div class="grid gap-2 px-5 pb-6"><h3 class="text-xl font-semibold">Progress you can see</h3><p class="text-pretty text-tfs16-mut">Track sleep, activity and labs in one timeline.</p></div>
      </li>
      <li class="group grid gap-5 overflow-hidden rounded-3xl bg-white p-2 shadow-[0_20px_50px_-30px_rgb(15_60_60/0.35)] ring-1 ring-tfs16-line transition duration-700 ease-out starting:translate-y-6 starting:opacity-0 hover:-translate-y-1 hover:shadow-[0_30px_60px_-30px_rgb(15_60_60/0.45)] supports-[animation-timeline:view()]:animate-tfs16-rise supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_0%_entry_80%] supports-[animation-timeline:view()]:nth-[3n+2]:[animation-range:entry_10%_entry_90%] supports-[animation-timeline:view()]:nth-[3n]:[animation-range:entry_20%_entry_100%] motion-reduce:animate-none motion-reduce:transition-none">
        <div class="relative grid h-36 place-items-center overflow-hidden rounded-[1.25rem] bg-tfs16-soft"><span class="absolute size-40 rounded-full bg-emerald-500 opacity-20 blur-2xl transition duration-500 group-hover:scale-125"></span><span class="relative grid size-14 place-items-center rounded-2xl bg-emerald-500 text-white shadow-lg transition duration-500 group-hover:scale-110"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg></span></div>
        <div class="grid gap-2 px-5 pb-6"><h3 class="text-xl font-semibold">Covered in 50 states</h3><p class="text-pretty text-tfs16-mut">In-network with the plans most employers offer.</p></div>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs16-bg: #f1f7f6;
  --color-tfs16-bg: oklch(0.971 0.006 185);
  --color-tfs16-soft: #e6f1ef;
  --color-tfs16-soft: oklch(0.949 0.012 184);
  --color-tfs16-ink: #0d2624;
  --color-tfs16-ink: oklch(0.248 0.031 188);
  --color-tfs16-mut: #46605d;
  --color-tfs16-mut: oklch(0.467 0.031 187);
  --color-tfs16-line: #d8e7e4;
  --color-tfs16-line: oklch(0.916 0.016 183);
  --color-tfs16-acc: #0d9488;
  --color-tfs16-acc: oklch(0.6 0.104 185);
  --font-tfs16-sans: 'Outfit', system-ui, sans-serif;
  --animate-tfs16-rise: tfs16-rise linear both;

  @keyframes tfs16-rise {
    from {
      opacity: 0.15;
      transform: translateY(60px) scale(0.94);
    }

    to {
      opacity: 1;
      transform: none;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-16 {
  width: 100%;
  min-height: 100svh;
}
```
