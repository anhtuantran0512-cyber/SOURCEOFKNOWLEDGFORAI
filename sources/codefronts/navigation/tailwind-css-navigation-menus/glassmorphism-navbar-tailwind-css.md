---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/glassmorphism-navbar-tailwind-css/"
title: "Glassmorphism Navbar in Tailwind CSS"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A floating frosted-glass navbar over drifting aurora orbs, with a matching glass hero card."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Navbar in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/glassmorphism-navbar-tailwind-css/

A floating frosted-glass navbar over drifting aurora orbs, with a matching glass hero card. The glass is backdrop-blur-2xl backdrop-saturate-150 plus an inner specular highlight, and it falls back to a solid tinted surface via supports-[backdrop-filter:blur(1px)]: where blur isn't available. Orbs drift on three @theme animations and stop under reduced motion. Zero JavaScript.
## HTML
```html
<div class="tnv-10 relative isolate min-h-svh w-full overflow-hidden bg-tnv10-bg bg-[radial-gradient(ellipse_at_20%_50%,#3730a3_0%,transparent_50%),radial-gradient(ellipse_at_80%_20%,#7e22ce_0%,transparent_45%),radial-gradient(ellipse_at_60%_90%,#1d4ed8_0%,transparent_45%)] font-tnv10-sans text-white antialiased selection:bg-indigo-500 selection:text-white">
  <div aria-hidden="true" class="pointer-events-none absolute -top-24 -left-24 -z-10 size-[26rem] animate-tnv10-a rounded-full bg-indigo-500 opacity-50 blur-[70px] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="pointer-events-none absolute right-[10%] -bottom-20 -z-10 size-[22rem] animate-tnv10-b rounded-full bg-violet-600 opacity-45 blur-[70px] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="pointer-events-none absolute top-[40%] left-[60%] -z-10 size-72 animate-tnv10-c rounded-full bg-blue-600 opacity-45 blur-[70px] motion-reduce:animate-none"></div>
  <header class="sticky top-5 z-20 mx-4 mt-5 sm:mx-10">
    <nav aria-label="Main" class="mx-auto flex max-w-5xl items-center justify-between gap-4 rounded-[20px] border border-white/15 bg-tnv10-solid py-2.5 pr-2.5 pl-5 shadow-[0_8px_32px_rgb(0_0_0/0.25),inset_0_1px_0_rgb(255_255_255/0.25)] backdrop-blur-2xl backdrop-saturate-150 supports-[backdrop-filter:blur(1px)]:bg-white/10">
      <a href="#" class="flex items-center gap-2.5 text-lg font-bold tracking-[-0.02em]"><span class="grid size-8 place-items-center rounded-[10px] border border-white/20 bg-white/15 shadow-[inset_0_1px_0_rgb(255_255_255/0.3)]"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></span>Prism</a>
      <ul class="hidden items-center gap-0.5 text-sm font-semibold text-white/75 md:flex [&_a]:flex [&_a]:h-10 [&_a]:items-center [&_a]:rounded-xl [&_a]:px-4 [&_a]:transition-colors [&_a:hover]:bg-white/10 [&_a:hover]:text-white [&_a:focus-visible]:outline-2 [&_a:focus-visible]:outline-white/60 [&_a[aria-current]]:bg-white/15 [&_a[aria-current]]:text-white [&_a[aria-current]]:shadow-[inset_0_1px_0_rgb(255_255_255/0.2)]">
        <li><a href="#" aria-current="page">Home</a></li><li><a href="#">Features</a></li><li><a href="#">Pricing</a></li><li><a href="#">Blog</a></li>
      </ul>
      <div class="flex items-center gap-2 text-sm font-semibold">
        <a href="#" class="hidden h-10 items-center rounded-xl border border-white/20 px-4 transition-colors hover:bg-white/10 sm:inline-flex">Log in</a>
        <a href="#" class="inline-flex h-10 items-center rounded-xl bg-white px-4 text-tnv10-bg shadow-[0_8px_24px_-8px_rgb(165_180_252/0.8)] transition hover:bg-indigo-50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Sign up free</a>
      </div>
    </nav>
  </header>
  <main class="relative grid min-h-[82svh] place-items-center px-5 py-20 text-center [&_code]:rounded [&_code]:bg-white/10 [&_code]:px-1.5 [&_code]:font-tnv10-mono [&_code]:text-[0.85em]">
    <div class="max-w-xl rounded-3xl border border-white/15 bg-tnv10-solid px-7 py-12 shadow-[0_24px_64px_rgb(0_0_0/0.3),inset_0_1px_0_rgb(255_255_255/0.2)] backdrop-blur-2xl backdrop-saturate-150 transition-[opacity,translate,scale] duration-700 ease-out supports-[backdrop-filter:blur(1px)]:bg-white/[0.08] starting:translate-y-4 starting:scale-[0.98] starting:opacity-0 sm:px-12">
      <h1 class="text-[clamp(2rem,5.5vw,3.25rem)] leading-[1.1] font-bold tracking-[-0.04em] text-balance">Design <span class="bg-linear-135 from-indigo-200 to-violet-300 bg-clip-text text-transparent">through glass</span></h1>
      <p class="mt-4 text-base/[1.7] text-white/80 text-pretty">The navbar and this card use <code>backdrop-blur-2xl</code> with <code>backdrop-saturate-150</code>, an inner specular edge, and a solid fallback where blur is unavailable.</p>
      <a href="#" class="mt-7 inline-flex min-h-12 items-center gap-2 rounded-2xl border border-white/25 bg-white/15 px-7 font-bold transition hover:bg-white/25 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Explore<svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      <ul class="mt-7 flex flex-wrap justify-center gap-2.5 text-[13px] font-semibold text-white/75 [&_b]:text-white [&>li]:rounded-full [&>li]:border [&>li]:border-white/12 [&>li]:bg-white/[0.07] [&>li]:px-4 [&>li]:py-2">
        <li><b>backdrop-blur</b> frost</li><li><b>saturate</b> colour</li><li><b>supports-</b> fallback</li>
      </ul>
    </div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv10-bg: #0a0a1a;
  --color-tnv10-bg: oklch(0.15 0.03 285);
  --color-tnv10-solid: #2a2850e6;
  --color-tnv10-solid: oklch(0.3 0.07 285 / 0.9);
  --font-tnv10-sans: 'Sora', system-ui, sans-serif;
  --font-tnv10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tnv10-a: tnv10-drift 14s ease-in-out infinite alternate;
  --animate-tnv10-b: tnv10-drift 18s ease-in-out -4s infinite alternate-reverse;
  --animate-tnv10-c: tnv10-drift 11s ease-in-out -8s infinite alternate;

  @keyframes tnv10-drift {
    0% {
      translate: 0 0;
      scale: 1;
    }

    100% {
      translate: 40px 30px;
      scale: 1.08;
    }
  }
}

.tnv-10 {
  width: 100%;
  min-height: 100svh;
}
```
