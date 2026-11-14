---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-shrinking-header-on-scroll/"
title: "Tailwind Shrinking Header on Scroll"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The header condenses as you read: 5&nbsp;rem tall at rest, 3.5&nbsp;rem once you pass 200&nbsp;px, with the wordmark scaling down, the tagline fading and the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shrinking Header on Scroll
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-shrinking-header-on-scroll/

The header condenses as you read: 5&nbsp;rem tall at rest, 3.5&nbsp;rem once you pass 200&nbsp;px, with the wordmark scaling down, the tagline fading and the shadow deepening on the same timeline. Custom utilities on scroll(root) — no scroll handler, no requestAnimationFrame — and without support the header simply stays compact.
## HTML
```html
<div class="thd-22 group/thd22 w-full min-h-svh bg-thd22-bg font-thd22-sans text-thd22-ink antialiased">
  <a href="#thd-22-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-md focus:bg-thd22-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-bold focus:text-black">Skip to content</a>
  <header class="thd22-shrink sticky top-0 z-40 h-14 border-b border-thd22-line bg-thd22-bg/90 shadow-[0_10px_30px_-12px_rgb(0_0_0/.6)] backdrop-blur-md">
    <div class="mx-auto flex h-full max-w-7xl items-center gap-4 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-22-main" class="thd22-mark flex origin-left items-center gap-2.5">
        <span aria-hidden="true" class="grid size-9 place-items-center rounded-lg bg-thd22-acc text-black"><svg viewBox="0 0 24 24" fill="currentColor" class="size-5"><path d="M13.5 2 5 13.5h5.5L9.5 22 19 9.5h-5.8L13.5 2Z"/></svg></span>
        <span class="leading-none"><span class="block text-xl font-extrabold uppercase tracking-[.06em]">Voltline</span><span class="thd22-fade mt-1 hidden text-[11px] font-medium tracking-wide text-thd22-mut sm:block">EV charging for fleets</span></span>
      </a>
      <nav aria-label="Main" class="mx-auto hidden md:block">
        <ul class="flex items-center gap-1 text-[15px] font-semibold">
          <li><a href="#thd-22-main" aria-current="page" class="rounded-md px-3 py-2 text-thd22-mut hover:text-thd22-ink aria-[current=page]:text-thd22-acc">Product</a></li>
          <li><a href="#thd-22-main" class="rounded-md px-3 py-2 text-thd22-mut hover:text-thd22-ink">Fleet</a></li>
          <li><a href="#thd-22-main" class="rounded-md px-3 py-2 text-thd22-mut hover:text-thd22-ink">Network</a></li>
          <li><a href="#thd-22-main" class="rounded-md px-3 py-2 text-thd22-mut hover:text-thd22-ink">Support</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1.5 md:ml-0">
        <input id="thd-22-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-22-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd22-mut hover:bg-thd22-ink/8 hover:text-thd22-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd22-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px] group-has-[#thd-22-t:checked]/thd22:hidden"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-22-t:checked]/thd22:block"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-22-main" class="hidden rounded-md px-3 py-2 text-[15px] font-semibold text-thd22-mut hover:text-thd22-ink sm:block">Sign in</a>
        <a href="#thd-22-main" class="grid min-h-11 place-items-center whitespace-nowrap rounded-md bg-thd22-acc px-5 text-[15px] font-bold text-black transition hover:brightness-105 hover:shadow-[0_0_24px_-4px_var(--color-thd22-acc)]">Get a quote</a>
      </div>
    </div>
  </header>
  <main id="thd-22-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.5rem)] py-[clamp(3rem,9vw,6rem)]">
    <p class="text-sm font-bold uppercase tracking-[.2em] text-thd22-acc">Scroll to condense</p>
    <h1 class="mt-3 max-w-[16ch] text-[clamp(2.6rem,8vw,5.4rem)] font-extrabold uppercase leading-[.92] tracking-[-.01em]">Charge the whole fleet overnight.</h1>
    <p class="mt-5 max-w-[48ch] text-lg text-thd22-mut">The header is 5rem at the top. Over the first 200px it drops to 3.5rem, the wordmark scales down, the tagline fades and the shadow deepens.</p>
    <ul class="mt-12 grid grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))] gap-3">
      <li class="rounded-xl border border-thd22-line bg-thd22-panel p-5"><p class="text-3xl font-extrabold tabular-nums text-thd22-acc">350 kW</p><p class="mt-1 text-sm text-thd22-mut">peak depot output</p></li>
      <li class="rounded-xl border border-thd22-line bg-thd22-panel p-5"><p class="text-3xl font-extrabold tabular-nums text-thd22-acc">99.7%</p><p class="mt-1 text-sm text-thd22-mut">charger uptime, 2026</p></li>
      <li class="rounded-xl border border-thd22-line bg-thd22-panel p-5"><p class="text-3xl font-extrabold tabular-nums text-thd22-acc">1,240</p><p class="mt-1 text-sm text-thd22-mut">sites across the UK &amp; EU</p></li>
    </ul>
    <div aria-hidden="true" class="h-[90svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd22-bg: var(--thd22-bg);
  --color-thd22-panel: var(--thd22-panel);
  --color-thd22-ink: var(--thd22-ink);
  --color-thd22-mut: var(--thd22-mut);
  --color-thd22-line: var(--thd22-line);
  --color-thd22-acc: var(--thd22-acc);
}

@theme {
  --font-thd22-sans: 'Barlow', system-ui, sans-serif;
}

.thd-22 {
  width: 100%;
  min-height: 100svh;
  --thd22-bg: #0c0d10;
  --thd22-panel: #14161b;
  --thd22-ink: #f3f4f6;
  --thd22-mut: #a1a6b0;
  --thd22-line: rgb(255 255 255 / 0.08);
  --thd22-acc: #facc15;
}

.thd-22:has(#thd-22-t:checked) {
  --thd22-bg: #f7f7f4;
  --thd22-panel: #ffffff;
  --thd22-ink: #111216;
  --thd22-mut: #545862;
  --thd22-line: rgb(17 18 22 / 0.09);
  --thd22-acc: #eab308;
}

@utility thd22-shrink {
  @supports (animation-timeline: scroll()) {
    animation: thd22-shrink linear both;
    animation-timeline: scroll(root);
    animation-range: 0 200px;
  }
}

@utility thd22-mark {
  @supports (animation-timeline: scroll()) {
    animation: thd22-mark linear both;
    animation-timeline: scroll(root);
    animation-range: 0 200px;
  }
}

@utility thd22-fade {
  @supports (animation-timeline: scroll()) {
    animation: thd22-fade linear both;
    animation-timeline: scroll(root);
    animation-range: 0 120px;
  }
}

@keyframes thd22-shrink {
  from {
    height: 5rem;
    box-shadow: none;
  }
}

@keyframes thd22-mark {
  from {
    scale: 1.18;
  }

  to {
    scale: 0.92;
  }
}

@keyframes thd22-fade {
  to {
    opacity: 0;
  }
}
```
