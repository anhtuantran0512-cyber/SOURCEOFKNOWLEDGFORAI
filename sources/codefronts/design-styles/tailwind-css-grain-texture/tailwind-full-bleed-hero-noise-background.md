---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-full-bleed-hero-noise-background/"
title: "Tailwind Full-Bleed Hero Section Noise Background"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "A production hero: unedited photograph, colour wash, two grain scales, and a legibility scrim — five stacked layers, zero added requests."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full-Bleed Hero Section Noise Background
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-full-bleed-hero-noise-background/

A production hero: unedited photograph, colour wash, two grain scales, and a legibility scrim — five stacked layers, zero added requests. The fine grain gives the surface tooth, the coarse grain at a fifth of the frequency gives the frame weather, and the staggered reveal is a single @theme animation token applied as animate-gtw10-rise.
## HTML
```html
<section class="gtw-10 relative block w-full min-h-svh bg-gtw10-bg text-gtw10-ink" aria-labelledby="gtw-10-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-60">
    <input type="checkbox" id="gtw-10-theme" class="gtw-10-theme peer sr-only">
    <label for="gtw-10-theme" class="grid place-items-center w-11 h-11 rounded-full border border-white/30 bg-[oklch(0.15_0.02_180/0.45)] backdrop-blur-[8px] text-white cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw10-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <div class="gtw-10-hero relative isolate overflow-hidden grid grid-rows-[auto_1fr] min-h-svh">
    <img src="https://picsum.photos/id/1018/2000/1200" alt="" aria-hidden="true" width="2000" height="1200" class="absolute inset-0 z-0 w-full h-full object-cover">
    <span aria-hidden="true" class="absolute inset-0 z-[1] bg-[linear-gradient(200deg,color-mix(in_oklab,var(--gtw10-wash)_74%,transparent)_0%,color-mix(in_oklab,var(--gtw10-wash)_42%,transparent)_55%,transparent_100%)]"></span>
    <span aria-hidden="true" class="absolute inset-0 z-[2] pointer-events-none bg-[image:var(--gtw10-coarse)] opacity-[0.07] mix-blend-overlay"></span>
    <span aria-hidden="true" class="absolute inset-0 z-[3] pointer-events-none bg-[image:var(--gtw10-fine)] opacity-[0.1] mix-blend-luminosity"></span>
    <span aria-hidden="true" class="absolute inset-0 z-[4] bg-[linear-gradient(to_top,oklch(0.15_0.01_180/0.88)_0%,oklch(0.15_0.01_180/0.62)_34%,oklch(0.15_0.01_180/0.12)_68%,transparent_100%)]"></span>

    <nav aria-label="Primary" class="relative z-[6] w-[min(78rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto flex flex-wrap items-center gap-y-2 gap-x-[clamp(1rem,3vw,2rem)] py-[clamp(1rem,3vw,1.6rem)] pr-[60px] text-white">
      <a href="#gtw-10-title" class="text-inherit no-underline font-gtw10-display text-[1.05rem] font-semibold leading-none tracking-[-0.02em]">Northline</a>
      <ul class="list-none m-0 p-0 flex flex-wrap gap-[0.2rem]">
        <li><a href="#gtw-10-title" class="inline-flex items-center min-h-11 px-[0.8rem] text-white/85 no-underline text-[0.9rem] transition-colors duration-150 hover:text-white focus-visible:outline-2 focus-visible:outline-gtw10-acc focus-visible:outline-offset-2">Expeditions</a></li>
        <li><a href="#gtw-10-title" class="inline-flex items-center min-h-11 px-[0.8rem] text-white/85 no-underline text-[0.9rem] transition-colors duration-150 hover:text-white focus-visible:outline-2 focus-visible:outline-gtw10-acc focus-visible:outline-offset-2">Field notes</a></li>
        <li><a href="#gtw-10-title" class="inline-flex items-center min-h-11 px-[0.8rem] text-white/85 no-underline text-[0.9rem] transition-colors duration-150 hover:text-white focus-visible:outline-2 focus-visible:outline-gtw10-acc focus-visible:outline-offset-2">Kit</a></li>
      </ul>
      <a href="#gtw-10-title" class="ml-auto inline-flex items-center min-h-11 px-4 rounded-full border border-white/35 backdrop-blur-[6px] text-white no-underline font-gtw10-display text-[0.84rem] font-semibold leading-none transition-colors duration-200 hover:bg-white/15 focus-visible:outline-2 focus-visible:outline-gtw10-acc focus-visible:outline-offset-2">Book a slot</a>
    </nav>

    <div class="relative z-[6] self-end w-[min(78rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto grid gap-[0.9rem] max-w-[44rem] py-[clamp(2.5rem,8vw,5rem)] text-white">
      <p class="m-0 animate-gtw10-rise [animation-delay:60ms] motion-reduce:animate-none font-gtw10-mono text-[0.74rem] font-medium leading-none tracking-[0.16em] uppercase text-gtw10-acc">Season opens 14 March · 9 departures</p>
      <h1 id="gtw-10-title" class="m-0 animate-gtw10-rise [animation-delay:130ms] motion-reduce:animate-none font-gtw10-display text-[clamp(2.4rem,8vw,5.2rem)] font-semibold leading-[0.97] tracking-[-0.045em] text-balance">Ten days above the treeline</h1>
      <p class="m-0 animate-gtw10-rise [animation-delay:200ms] motion-reduce:animate-none max-w-[36rem] text-white text-[clamp(0.97rem,2vw,1.13rem)] text-pretty">Guided high routes across the northern ranges. Small groups, real weather, no helicopters. The photograph is unedited — everything you see over it is four layers of CSS.</p>
      <div class="flex flex-wrap gap-[0.65rem] mt-[0.4rem] animate-gtw10-rise [animation-delay:270ms] motion-reduce:animate-none">
        <a href="#gtw-10-title" class="inline-flex items-center min-h-[50px] px-[1.4rem] rounded-full no-underline font-gtw10-display text-[0.92rem] font-semibold leading-none text-gtw10-onacc bg-[image:var(--gtw10-fine),linear-gradient(var(--color-gtw10-acc),var(--color-gtw10-acc))] [background-blend-mode:soft-light,normal] transition-[filter] duration-200 hover:brightness-[1.06] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px]">See the routes</a>
        <a href="#gtw-10-title" class="inline-flex items-center min-h-[50px] px-[1.4rem] rounded-full no-underline font-gtw10-display text-[0.92rem] font-semibold leading-none text-white bg-white/10 border border-white/30 backdrop-blur-[6px] transition-colors duration-200 hover:bg-white/20 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px]">Read the kit list</a>
      </div>
      <dl class="flex flex-wrap gap-y-2 gap-x-[1.6rem] mt-[0.9rem] mb-0 pt-[0.9rem] border-t border-white/25 animate-gtw10-rise [animation-delay:340ms] motion-reduce:animate-none">
        <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw10-mono text-[0.68rem] leading-none tracking-[0.12em] uppercase text-white/75">Layers</dt><dd class="m-0 font-gtw10-mono text-[1.15rem] font-semibold leading-none">5</dd></div>
        <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw10-mono text-[0.68rem] leading-none tracking-[0.12em] uppercase text-white/75">Grain scales</dt><dd class="m-0 font-gtw10-mono text-[1.15rem] font-semibold leading-none">2</dd></div>
        <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw10-mono text-[0.68rem] leading-none tracking-[0.12em] uppercase text-white/75">Requests added</dt><dd class="m-0 font-gtw10-mono text-[1.15rem] font-semibold leading-none">0</dd></div>
      </dl>
    </div>
  </div>

  <section class="w-[min(78rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto py-[clamp(2.5rem,7vw,4.5rem)] grid gap-[0.7rem] max-w-[56rem]" aria-labelledby="gtw-10-h-below">
    <h2 id="gtw-10-h-below" class="m-0 font-gtw10-display text-[clamp(1.2rem,3vw,1.6rem)] font-semibold leading-tight tracking-[-0.02em]">Why two grain scales</h2>
    <p class="m-0 text-gtw10-mut text-[0.96rem] text-pretty">One fine layer over a photo reads as sensor noise. A second layer at a fifth of the frequency and a twentieth of the opacity adds unevenness the eye interprets as atmosphere. The fine layer gives the surface tooth; the coarse layer gives the frame weather. Together they cost two composites and no requests.</p>
  </section>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw10-bg: #06100f;
  --color-gtw10-bg: oklch(0.15 0.015 180);
  --color-gtw10-surf: #0d1a19;
  --color-gtw10-surf: oklch(0.2 0.018 180);
  --color-gtw10-line: #1e3230;
  --color-gtw10-line: oklch(0.29 0.02 180);
  --color-gtw10-ink: #ecf6f4;
  --color-gtw10-ink: oklch(0.96 0.012 180);
  --color-gtw10-mut: #9ab5b1;
  --color-gtw10-mut: oklch(0.74 0.02 180);
  --color-gtw10-acc: #5eead4;
  --color-gtw10-acc: oklch(0.86 0.13 175);
  --color-gtw10-onacc: #04211d;
  --color-gtw10-onacc: oklch(0.23 0.04 175);
  --font-gtw10-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw10-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  /* An @theme animation entry mints animate-gtw10-rise; the @keyframes still live below. */
  --animate-gtw10-rise: gtw-10-rise 720ms cubic-bezier(0.22, 1, 0.36, 1) both;
}

@keyframes gtw-10-rise {
  from {
    opacity: 0;
    translate: 0 14px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.gtw-10 {
  width: 100%;
  min-height: 100svh;
  --gtw10-wash: #062b28;
  --gtw10-fine: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='170' height='170'%3E%3Cfilter id='gtw10a'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='170' height='170' filter='url(%23gtw10a)'/%3E%3C/svg%3E");
  --gtw10-coarse: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='420' height='420'%3E%3Cfilter id='gtw10b'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.14' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='420' height='420' filter='url(%23gtw10b)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}
/* vh fallback before svh, for engines below the svh floor. */

.gtw-10-hero {
  min-height: 100vh;
  min-height: 100svh;
}

.gtw-10:has(.gtw-10-theme:checked) {
  --color-gtw10-bg: #eef5f3;
  --color-gtw10-bg: oklch(0.96 0.008 180);
  --color-gtw10-surf: #ffffff;
  --color-gtw10-surf: oklch(1 0 0);
  --color-gtw10-line: #d3e3e0;
  --color-gtw10-line: oklch(0.9 0.015 180);
  --color-gtw10-ink: #06100f;
  --color-gtw10-ink: oklch(0.15 0.015 180);
  --color-gtw10-mut: #52706c;
  --color-gtw10-mut: oklch(0.48 0.025 180);
  --color-gtw10-acc: #0f766e;
  --color-gtw10-acc: oklch(0.5 0.1 180);
  --color-gtw10-onacc: #ecfdf5;
  --color-gtw10-onacc: oklch(0.98 0.02 165);
  --gtw10-wash: #0d3b36;
}

@media (prefers-color-scheme: light) {
  .gtw-10 {
    --color-gtw10-bg: #eef5f3;
    --color-gtw10-bg: oklch(0.96 0.008 180);
    --color-gtw10-surf: #ffffff;
    --color-gtw10-surf: oklch(1 0 0);
    --color-gtw10-line: #d3e3e0;
    --color-gtw10-line: oklch(0.9 0.015 180);
    --color-gtw10-ink: #06100f;
    --color-gtw10-ink: oklch(0.15 0.015 180);
    --color-gtw10-mut: #52706c;
    --color-gtw10-mut: oklch(0.48 0.025 180);
    --color-gtw10-acc: #0f766e;
    --color-gtw10-acc: oklch(0.5 0.1 180);
    --color-gtw10-onacc: #ecfdf5;
    --color-gtw10-onacc: oklch(0.98 0.02 165);
    --gtw10-wash: #0d3b36;
  }

  .gtw-10:has(.gtw-10-theme:checked) {
    --color-gtw10-bg: #06100f;
    --color-gtw10-bg: oklch(0.15 0.015 180);
    --color-gtw10-surf: #0d1a19;
    --color-gtw10-surf: oklch(0.2 0.018 180);
    --color-gtw10-line: #1e3230;
    --color-gtw10-line: oklch(0.29 0.02 180);
    --color-gtw10-ink: #ecf6f4;
    --color-gtw10-ink: oklch(0.96 0.012 180);
    --color-gtw10-mut: #9ab5b1;
    --color-gtw10-mut: oklch(0.74 0.02 180);
    --color-gtw10-acc: #5eead4;
    --color-gtw10-acc: oklch(0.86 0.13 175);
    --color-gtw10-onacc: #04211d;
    --color-gtw10-onacc: oklch(0.23 0.04 175);
    --gtw10-wash: #062b28;
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-10:has(.gtw-10-theme:checked) {
    --color-gtw10-bg: #eef5f3;
    --color-gtw10-bg: oklch(0.96 0.008 180);
    --color-gtw10-surf: #ffffff;
    --color-gtw10-surf: oklch(1 0 0);
    --color-gtw10-line: #d3e3e0;
    --color-gtw10-line: oklch(0.9 0.015 180);
    --color-gtw10-ink: #06100f;
    --color-gtw10-ink: oklch(0.15 0.015 180);
    --color-gtw10-mut: #52706c;
    --color-gtw10-mut: oklch(0.48 0.025 180);
    --color-gtw10-acc: #0f766e;
    --color-gtw10-acc: oklch(0.5 0.1 180);
    --color-gtw10-onacc: #ecfdf5;
    --color-gtw10-onacc: oklch(0.98 0.02 165);
    --gtw10-wash: #0d3b36;
  }
}
```
