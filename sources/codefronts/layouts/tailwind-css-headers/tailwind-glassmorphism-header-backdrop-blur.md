---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-glassmorphism-header-backdrop-blur/"
title: "Tailwind Glassmorphism Header with Backdrop Blur"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "A full header surface in glass: backdrop-blur-xl backdrop-saturate-180 over a slowly drifting aurora, with an inner highlight along the top edge —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Header with Backdrop Blur
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-glassmorphism-header-backdrop-blur/

A full header surface in glass: backdrop-blur-xl backdrop-saturate-180 over a slowly drifting aurora, with an inner highlight along the top edge — shadow-[inset_0_1px_0_…] — that sells the material. The opaque fallback is the default class; supports-[backdrop-filter:blur(1px)]: only thins it when blur is real, so text always meets contrast.
## HTML
```html
<div class="thd-16 group/thd16 relative w-full min-h-svh overflow-x-clip bg-thd16-bg font-thd16-sans text-thd16-ink antialiased">
  <a href="#thd-16-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-full focus:bg-white focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-black">Skip to content</a>
  <div aria-hidden="true" class="pointer-events-none fixed inset-0 overflow-hidden">
    <div class="absolute -left-[10%] -top-[20%] size-[60vmax] animate-thd16-drift rounded-full bg-thd16-a1 opacity-70 blur-3xl motion-reduce:animate-none"></div>
    <div class="absolute -right-[15%] top-[10%] size-[50vmax] animate-thd16-drift rounded-full bg-thd16-a2 opacity-60 blur-3xl [animation-duration:26s] [animation-direction:reverse] motion-reduce:animate-none"></div>
    <div class="absolute bottom-[-30%] left-[20%] size-[55vmax] animate-thd16-drift rounded-full bg-thd16-a3 opacity-50 blur-3xl [animation-duration:32s] motion-reduce:animate-none"></div>
  </div>
  <header class="sticky top-3 z-40 mx-3 mt-3 rounded-2xl border border-white/15 bg-thd16-glass-solid shadow-[inset_0_1px_0_rgb(255_255_255/.35),0_20px_50px_-20px_rgb(0_0_0/.45)] supports-[backdrop-filter:blur(1px)]:bg-thd16-glass supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-180">
    <div class="mx-auto flex h-16 max-w-7xl items-center gap-4 px-4">
      <a href="#thd-16-main" class="flex items-center gap-2 text-lg font-semibold tracking-tight"><span aria-hidden="true" class="size-6 rounded-full bg-[conic-gradient(from_180deg,var(--color-thd16-a1),var(--color-thd16-a2),var(--color-thd16-a3),var(--color-thd16-a1))] shadow-[0_0_16px_var(--color-thd16-a2)]"></span>Aurora</a>
      <nav aria-label="Main" class="mx-auto hidden md:block">
        <ul class="flex items-center gap-1 rounded-full border border-white/10 bg-white/5 p-1 text-sm">
          <li><a href="#thd-16-main" aria-current="page" class="block rounded-full px-4 py-1.5 transition-colors hover:bg-white/10 aria-[current=page]:bg-white/20 aria-[current=page]:shadow-[inset_0_1px_0_rgb(255_255_255/.3)]">Discover</a></li>
          <li><a href="#thd-16-main" class="block rounded-full px-4 py-1.5 transition-colors hover:bg-white/10">Spaces</a></li>
          <li><a href="#thd-16-main" class="block rounded-full px-4 py-1.5 transition-colors hover:bg-white/10">Community</a></li>
          <li><a href="#thd-16-main" class="block rounded-full px-4 py-1.5 transition-colors hover:bg-white/10">Pricing</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1.5 md:ml-0">
        <label class="hidden min-h-10 w-44 items-center gap-2 rounded-full border border-white/15 bg-white/10 px-3 text-sm transition focus-within:bg-white/20 focus-within:ring-2 focus-within:ring-white/40 lg:flex">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true" class="size-4 flex-none opacity-80"><circle cx="11" cy="11" r="6.4"/><path d="m15.8 15.8 5.2 5.2"/></svg>
          <input type="search" placeholder="Search" aria-label="Search" class="min-w-0 flex-1 bg-transparent outline-none placeholder:text-thd16-ink/70">
        </label>
        <input id="thd-16-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-16-t" class="grid size-11 cursor-pointer place-items-center rounded-full hover:bg-white/10 peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-white">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px] group-has-[#thd-16-t:checked]/thd16:hidden"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-16-t:checked]/thd16:block"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-16-main" class="grid min-h-11 place-items-center rounded-full bg-thd16-ink px-5 text-sm font-semibold text-thd16-bg shadow-[0_8px_24px_-8px_rgb(0_0_0/.5)] transition hover:-translate-y-px">Join free</a>
      </div>
    </div>
  </header>
  <main id="thd-16-main" class="relative mx-auto max-w-5xl px-5 pb-20 pt-[clamp(4rem,12vw,8rem)] text-center">
    <h1 class="mx-auto max-w-[14ch] text-[clamp(2.6rem,8vw,5.4rem)] font-light leading-[1] tracking-[-.04em] text-balance">Rooms for the <span class="font-semibold">ideas in between.</span></h1>
    <p class="mx-auto mt-6 max-w-[44ch] text-lg text-thd16-ink/85">Scroll the page: the aurora drifts behind the frosted bar, and its bright top edge catches the light.</p>
    <ul class="mx-auto mt-14 grid max-w-3xl gap-3 text-left sm:grid-cols-3">
      <li class="rounded-2xl border border-white/15 bg-white/10 p-5 shadow-[inset_0_1px_0_rgb(255_255_255/.25)] backdrop-blur-md"><p class="font-semibold">2.4k spaces</p><p class="mt-1 text-sm text-thd16-ink/80">opened this week</p></li>
      <li class="rounded-2xl border border-white/15 bg-white/10 p-5 shadow-[inset_0_1px_0_rgb(255_255_255/.25)] backdrop-blur-md"><p class="font-semibold">Live rooms</p><p class="mt-1 text-sm text-thd16-ink/80">audio, canvas, notes</p></li>
      <li class="rounded-2xl border border-white/15 bg-white/10 p-5 shadow-[inset_0_1px_0_rgb(255_255_255/.25)] backdrop-blur-md"><p class="font-semibold">Free forever</p><p class="mt-1 text-sm text-thd16-ink/80">for teams of five</p></li>
    </ul>
    <div aria-hidden="true" class="h-[80svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd16-bg: var(--thd16-bg);
  --color-thd16-ink: var(--thd16-ink);
  --color-thd16-glass: var(--thd16-glass);
  --color-thd16-glass-solid: var(--thd16-glass-solid);
  --color-thd16-a1: var(--thd16-a1);
  --color-thd16-a2: var(--thd16-a2);
  --color-thd16-a3: var(--thd16-a3);
}

@theme {
  --font-thd16-sans: 'Outfit', system-ui, sans-serif;
  --animate-thd16-drift: thd16-drift 20s ease-in-out infinite alternate;

  @keyframes thd16-drift {
    to {
      translate: 8vmax 6vmax;
      scale: 1.15;
    }
  }
}

.thd-16 {
  width: 100%;
  min-height: 100svh;
  --thd16-bg: #0b0a1f;
  --thd16-ink: #ffffff;
  --thd16-glass: rgb(20 18 50 / 0.28);
  --thd16-glass-solid: rgb(20 18 50 / 0.94);
  --thd16-a1: #7c3aed;
  --thd16-a2: #06b6d4;
  --thd16-a3: #ec4899;
}

.thd-16:has(#thd-16-t:checked) {
  --thd16-bg: #eef2ff;
  --thd16-ink: #111133;
  --thd16-glass: rgb(255 255 255 / 0.4);
  --thd16-glass-solid: rgb(255 255 255 / 0.95);
  --thd16-a1: #a5b4fc;
  --thd16-a2: #67e8f9;
  --thd16-a3: #f9a8d4;
}
```
