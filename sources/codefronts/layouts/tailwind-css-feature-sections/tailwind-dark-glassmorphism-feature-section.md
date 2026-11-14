---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-dark-glassmorphism-feature-section/"
title: "Tailwind Dark Glassmorphism Feature Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "Frosted glass done properly on a dark aurora: three slowly drifting colour fields sit behind a grid of glass cards with backdrop-blur-xl, a top-edge…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Glassmorphism Feature Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-dark-glassmorphism-feature-section/

Frosted glass done properly on a dark aurora: three slowly drifting colour fields sit behind a grid of glass cards with backdrop-blur-xl, a top-edge highlight and a hairline ring. Where backdrop-filter is unsupported, supports-[…]: swaps in a more opaque fill so text stays readable.
## HTML
```html
<section class="tfs-15 relative isolate w-full min-h-svh overflow-hidden bg-tfs15-bg px-5 py-20 font-tfs15-sans text-white antialiased sm:py-28" aria-labelledby="tfs-15-h">
  <div aria-hidden="true" class="absolute inset-0 -z-10">
    <div class="absolute left-[8%] top-[10%] size-[28rem] rounded-full bg-tfs15-a1/50 blur-[100px] animate-tfs15-drift motion-reduce:animate-none"></div>
    <div class="absolute right-[5%] top-[30%] size-[24rem] rounded-full bg-tfs15-a2/45 blur-[100px] animate-tfs15-drift [animation-delay:-6s] motion-reduce:animate-none"></div>
    <div class="absolute bottom-[0%] left-[35%] size-[26rem] rounded-full bg-tfs15-a3/40 blur-[110px] animate-tfs15-drift [animation-delay:-12s] motion-reduce:animate-none"></div>
  </div>
  <div class="mx-auto grid w-full max-w-6xl gap-14">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="mx-auto rounded-full bg-white/10 px-3 py-1 text-xs font-medium text-white ring-1 ring-white/15 supports-[backdrop-filter:blur(1px)]:backdrop-blur">Vale Studio</p>
      <h2 id="tfs-15-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-6xl">Creative tools that get out of your way</h2>
      <p class="text-pretty text-lg text-tfs15-mut">Real-time rendering, collaborative timelines and AI assists — on any machine.</p>
    </header>
    <ul class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
      <li class="group relative grid gap-4 overflow-hidden rounded-3xl bg-tfs15-card/85 p-7 ring-1 ring-white/10 transition duration-300 before:absolute before:inset-x-6 before:top-0 before:h-px before:bg-linear-to-r before:from-transparent before:via-white/60 before:to-transparent hover:-translate-y-1 hover:ring-white/25 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl">
        <span class="grid size-12 place-items-center rounded-2xl bg-white/10 text-white ring-1 ring-white/15 transition group-hover:bg-white group-hover:text-tfs15-bg"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M6 6h12v12H6zM9 9h6v6H9zM9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg></span>
        <h3 class="text-xl font-semibold">Cloud GPU rendering</h3>
        <p class="text-pretty text-tfs15-mut">4K previews stream in under a second, even on a laptop.</p>
      </li>
      <li class="group relative grid gap-4 overflow-hidden rounded-3xl bg-tfs15-card/85 p-7 ring-1 ring-white/10 transition duration-300 before:absolute before:inset-x-6 before:top-0 before:h-px before:bg-linear-to-r before:from-transparent before:via-white/60 before:to-transparent hover:-translate-y-1 hover:ring-white/25 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl">
        <span class="grid size-12 place-items-center rounded-2xl bg-white/10 text-white ring-1 ring-white/15 transition group-hover:bg-white group-hover:text-tfs15-bg"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span>
        <h3 class="text-xl font-semibold">Multiplayer timelines</h3>
        <p class="text-pretty text-tfs15-mut">Edit the same sequence with your whole team, live.</p>
      </li>
      <li class="group relative grid gap-4 overflow-hidden rounded-3xl bg-tfs15-card/85 p-7 ring-1 ring-white/10 transition duration-300 before:absolute before:inset-x-6 before:top-0 before:h-px before:bg-linear-to-r before:from-transparent before:via-white/60 before:to-transparent hover:-translate-y-1 hover:ring-white/25 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl">
        <span class="grid size-12 place-items-center rounded-2xl bg-white/10 text-white ring-1 ring-white/15 transition group-hover:bg-white group-hover:text-tfs15-bg"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/></svg></span>
        <h3 class="text-xl font-semibold">Generative fill</h3>
        <p class="text-pretty text-tfs15-mut">Extend a shot, remove a boom mic, relight a scene.</p>
      </li>
      <li class="group relative grid gap-4 overflow-hidden rounded-3xl bg-tfs15-card/85 p-7 ring-1 ring-white/10 transition duration-300 before:absolute before:inset-x-6 before:top-0 before:h-px before:bg-linear-to-r before:from-transparent before:via-white/60 before:to-transparent hover:-translate-y-1 hover:ring-white/25 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl">
        <span class="grid size-12 place-items-center rounded-2xl bg-white/10 text-white ring-1 ring-white/15 transition group-hover:bg-white group-hover:text-tfs15-bg"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="m12 2 10 5-10 5L2 7l10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></span>
        <h3 class="text-xl font-semibold">Non-destructive layers</h3>
        <p class="text-pretty text-tfs15-mut">Every change is a layer you can toggle or revisit.</p>
      </li>
      <li class="group relative grid gap-4 overflow-hidden rounded-3xl bg-tfs15-card/85 p-7 ring-1 ring-white/10 transition duration-300 before:absolute before:inset-x-6 before:top-0 before:h-px before:bg-linear-to-r before:from-transparent before:via-white/60 before:to-transparent hover:-translate-y-1 hover:ring-white/25 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl">
        <span class="grid size-12 place-items-center rounded-2xl bg-white/10 text-white ring-1 ring-white/15 transition group-hover:bg-white group-hover:text-tfs15-bg"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 3v5h-5"/></svg></span>
        <h3 class="text-xl font-semibold">Infinite history</h3>
        <p class="text-pretty text-tfs15-mut">Branch an edit, compare versions, merge the best take.</p>
      </li>
      <li class="group relative grid gap-4 overflow-hidden rounded-3xl bg-tfs15-card/85 p-7 ring-1 ring-white/10 transition duration-300 before:absolute before:inset-x-6 before:top-0 before:h-px before:bg-linear-to-r before:from-transparent before:via-white/60 before:to-transparent hover:-translate-y-1 hover:ring-white/25 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl">
        <span class="grid size-12 place-items-center rounded-2xl bg-white/10 text-white ring-1 ring-white/15 transition group-hover:bg-white group-hover:text-tfs15-bg"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg></span>
        <h3 class="text-xl font-semibold">Publish everywhere</h3>
        <p class="text-pretty text-tfs15-mut">Export presets for every platform, auto-captioned.</p>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs15-bg: #05040c;
  --color-tfs15-bg: oklch(0.115 0.022 290);
  --color-tfs15-card: #13111f;
  --color-tfs15-card: oklch(0.188 0.028 290);
  --color-tfs15-mut: #c9c5dd;
  --color-tfs15-mut: oklch(0.834 0.033 293);
  --color-tfs15-a1: #7c3aed;
  --color-tfs15-a1: oklch(0.541 0.247 293);
  --color-tfs15-a2: #06b6d4;
  --color-tfs15-a2: oklch(0.715 0.126 215);
  --color-tfs15-a3: #ec4899;
  --color-tfs15-a3: oklch(0.656 0.212 354);
  --font-tfs15-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tfs15-drift: tfs15-drift 18s ease-in-out infinite alternate;

  @keyframes tfs15-drift {
    0% {
      transform: translate(0, 0) scale(1);
    }

    50% {
      transform: translate(6%, 8%) scale(1.12);
    }

    100% {
      transform: translate(-6%, -4%) scale(0.95);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-15 {
  width: 100%;
  min-height: 100svh;
}
```
