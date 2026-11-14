---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-transparent-header-over-hero/"
title: "Tailwind Transparent Header Over Hero Image"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The landing-page classic without a scroll listener: the header floats transparent over a full-bleed hero, then solidifies into an opaque bar with dark ink as…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Transparent Header Over Hero Image
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-transparent-header-over-hero/

The landing-page classic without a scroll listener: the header floats transparent over a full-bleed hero, then solidifies into an opaque bar with dark ink as the reader passes 60&nbsp;px. A gradient scrim and v4.1's text-shadow-* utilities keep nav text readable over the image, and the fallback is the solid bar — never white text on a white page.
## HTML
```html
<div class="thd-08 group/thd08 w-full min-h-svh bg-thd08-bg font-thd08-sans text-thd08-ink antialiased">
  <a href="#thd-08-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-white focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-black">Skip to content</a>
  <header class="thd08-solidify sticky top-0 z-40 h-16 bg-thd08-panel text-thd08-ink shadow-[0_1px_0_var(--color-thd08-line)]">
    <div class="mx-auto flex h-full max-w-7xl items-center gap-4 px-[clamp(.75rem,3vw,1.75rem)]">
      <a href="#thd-08-main" class="flex items-center gap-2 text-xl font-extrabold tracking-tight text-current text-shadow-md">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-6"><path d="m3 19 6-10 4 6 2-3 6 7H3Z"/><circle cx="17" cy="6" r="2"/></svg>Wayfare
      </a>
      <nav aria-label="Main" class="mx-auto hidden md:block">
        <ul class="flex items-center gap-1 text-[15px] font-semibold">
          <li><a href="#thd-08-main" class="rounded-full px-3.5 py-2 text-current text-shadow-md transition-colors hover:bg-current/10">Stays</a></li>
          <li><a href="#thd-08-main" class="rounded-full px-3.5 py-2 text-current text-shadow-md transition-colors hover:bg-current/10">Routes</a></li>
          <li><a href="#thd-08-main" class="rounded-full px-3.5 py-2 text-current text-shadow-md transition-colors hover:bg-current/10">Guides</a></li>
          <li><a href="#thd-08-main" class="rounded-full px-3.5 py-2 text-current text-shadow-md transition-colors hover:bg-current/10">Hosts</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1.5 md:ml-0">
        <input id="thd-08-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-08-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-current hover:bg-current/10 peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-current">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-08-t:checked]/thd08:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-08-t:checked]/thd08:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-08-main" class="grid min-h-11 place-items-center whitespace-nowrap rounded-full bg-thd08-acc px-5 text-sm font-bold text-thd08-on shadow-lg shadow-black/20 transition hover:-translate-y-px">Plan a trip</a>
      </div>
    </div>
  </header>
  <section aria-label="Hero" class="relative -mt-16 grid min-h-[88svh] place-items-end overflow-hidden bg-[radial-gradient(40rem_22rem_at_72%_38%,#ffd9a0_0%,#f6926b_26%,transparent_60%),linear-gradient(180deg,#3b2a5c_0%,#b75a6d_46%,#f0a071_64%,#2a2338_64.2%,#15121e_100%)] px-[clamp(.75rem,3vw,1.75rem)] pb-[clamp(2.5rem,8vw,5rem)] text-white">
    <div aria-hidden="true" class="absolute inset-x-0 top-0 h-40 bg-gradient-to-b from-black/45 to-transparent"></div>
    <div aria-hidden="true" class="absolute inset-x-0 bottom-[36%] h-[22%] bg-[linear-gradient(170deg,transparent_48%,#2a2338_49%),linear-gradient(195deg,transparent_55%,#342a45_56%)]"></div>
    <div class="relative mx-auto w-full max-w-7xl">
      <p class="text-sm font-semibold uppercase tracking-[.18em] text-white/85">Dolomites &middot; 7 nights</p>
      <h1 class="mt-3 max-w-[14ch] text-[clamp(2.6rem,8vw,5.6rem)] font-extrabold leading-[.95] tracking-[-.035em] text-balance text-shadow-lg">Go where the light goes.</h1>
      <p class="mt-4 max-w-[44ch] text-lg text-white/90 text-shadow-md">Scroll 60px and the transparent header becomes a solid bar &mdash; no scroll listener.</p>
    </div>
  </section>
  <main id="thd-08-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.75rem)] py-14">
    <h2 class="text-2xl font-extrabold tracking-tight">Trending routes</h2>
    <ul class="mt-5 grid grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))] gap-4">
      <li class="rounded-2xl bg-thd08-panel p-5 ring-1 ring-thd08-line"><p class="font-bold">Alta Via 1</p><p class="mt-1 text-sm text-thd08-mut">Hut to hut, 120 km &middot; from $1,240</p></li>
      <li class="rounded-2xl bg-thd08-panel p-5 ring-1 ring-thd08-line"><p class="font-bold">Lofoten by ferry</p><p class="mt-1 text-sm text-thd08-mut">Island hopping &middot; from $980</p></li>
      <li class="rounded-2xl bg-thd08-panel p-5 ring-1 ring-thd08-line"><p class="font-bold">Picos de Europa</p><p class="mt-1 text-sm text-thd08-mut">Gorges and cider houses &middot; from $860</p></li>
    </ul>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd08-bg: var(--thd08-bg);
  --color-thd08-panel: var(--thd08-panel);
  --color-thd08-ink: var(--thd08-ink);
  --color-thd08-mut: var(--thd08-mut);
  --color-thd08-line: var(--thd08-line);
  --color-thd08-acc: var(--thd08-acc);
  --color-thd08-on: var(--thd08-on);
}

@theme {
  --font-thd08-sans: 'Epilogue', system-ui, sans-serif;
}

.thd-08 {
  width: 100%;
  min-height: 100svh;
  --thd08-bg: #f7f5f2;
  --thd08-panel: #ffffff;
  --thd08-ink: #17141f;
  --thd08-mut: #5c5766;
  --thd08-line: rgb(23 20 31 / 0.09);
  --thd08-acc: #ffd166;
  --thd08-on: #1a1206;
}

.thd-08:has(#thd-08-t:checked) {
  --thd08-bg: #0f0d14;
  --thd08-panel: #17141f;
  --thd08-ink: #f3f0f7;
  --thd08-mut: #aaa4b5;
  --thd08-line: rgb(255 255 255 / 0.09);
  --thd08-acc: #ffd166;
  --thd08-on: #1a1206;
}
/* Resting classes are the SOLID bar. Only with scroll timelines does it start transparent. */

@utility thd08-solidify {
  @supports (animation-timeline: scroll()) {
    animation: thd08-solidify linear both;
    animation-timeline: scroll(root);
    animation-range: 0 60px;
  }
}

@keyframes thd08-solidify {
  from {
    background-color: transparent;
    color: #fff;
    box-shadow: none;
  }

  to {
    background-color: var(--thd08-panel);
    color: var(--thd08-ink);
    box-shadow: 0 1px 0 var(--thd08-line), 0 10px 30px -18px rgb(0 0 0 / 0.4);
  }
}
```
