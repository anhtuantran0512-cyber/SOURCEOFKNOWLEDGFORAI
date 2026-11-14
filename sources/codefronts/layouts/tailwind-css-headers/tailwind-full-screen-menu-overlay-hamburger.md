---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-full-screen-menu-overlay-hamburger/"
title: "Tailwind Full Screen Menu Overlay with Hamburger Toggle"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "A header that opens into a full-screen navigation overlay with no JavaScript: a visually hidden checkbox, a label drawn as the hamburger, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full Screen Menu Overlay with Hamburger Toggle
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-full-screen-menu-overlay-hamburger/

A header that opens into a full-screen navigation overlay with no JavaScript: a visually hidden checkbox, a label drawn as the hamburger, and group-has-[#thd-15-menu:checked] on every element that changes. The bars morph into an X on a spring curve, the overlay expands as a circle from the button with clip-path, and items stagger in from one token.
## HTML
```html
<div class="thd-15 group/thd15 w-full min-h-svh bg-thd15-bg font-thd15-sans text-thd15-ink antialiased">
  <a href="#thd-15-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-full focus:bg-thd15-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-black">Skip to content</a>
  <input id="thd-15-menu" type="checkbox" class="peer/menu sr-only" aria-label="Open navigation menu">
  <header class="sticky top-0 z-50 flex h-16 items-center gap-4 px-[clamp(.75rem,3vw,1.75rem)] mix-blend-normal">
    <a href="#thd-15-main" class="flex items-baseline gap-3"><span class="font-thd15-display text-xl font-extrabold tracking-tight">Vantage</span><span class="hidden text-xs text-thd15-mut sm:inline">Studio for interface engineering</span></a>
    <div class="ml-auto flex items-center gap-1">
      <input id="thd-15-t" type="checkbox" class="peer/t sr-only">
      <label for="thd-15-t" class="grid size-11 cursor-pointer place-items-center rounded-full hover:bg-thd15-ink/10 peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd15-acc">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px] group-has-[#thd-15-t:checked]/thd15:hidden"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-15-t:checked]/thd15:block"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
        <span class="sr-only">Switch light or dark theme</span>
      </label>
      <label for="thd-15-menu" class="flex min-h-11 cursor-pointer items-center gap-3 rounded-full border border-thd15-ink/20 pl-4 pr-1.5 text-sm font-semibold transition-colors hover:border-thd15-acc group-has-[#thd-15-menu:focus-visible]/thd15:outline-2 group-has-[#thd-15-menu:focus-visible]/thd15:outline-offset-2 group-has-[#thd-15-menu:focus-visible]/thd15:outline-thd15-acc group-has-[#thd-15-menu:checked]/thd15:border-thd15-acc">
        <span class="group-has-[#thd-15-menu:checked]/thd15:hidden">Menu</span><span class="hidden group-has-[#thd-15-menu:checked]/thd15:inline">Close</span>
        <span aria-hidden="true" class="relative grid size-8 place-items-center rounded-full bg-thd15-acc text-black">
          <span class="absolute h-0.5 w-3.5 -translate-y-[3px] rounded-full bg-current transition-transform duration-500 ease-[cubic-bezier(.5,1.6,.4,1)] group-has-[#thd-15-menu:checked]/thd15:translate-y-0 group-has-[#thd-15-menu:checked]/thd15:rotate-45"></span>
          <span class="absolute h-0.5 w-3.5 translate-y-[3px] rounded-full bg-current transition-transform duration-500 ease-[cubic-bezier(.5,1.6,.4,1)] group-has-[#thd-15-menu:checked]/thd15:translate-y-0 group-has-[#thd-15-menu:checked]/thd15:-rotate-45"></span>
        </span>
      </label>
    </div>
  </header>
  <div class="invisible fixed inset-0 z-40 overflow-y-auto bg-thd15-over text-thd15-overink transition-[clip-path,visibility] duration-700 ease-[cubic-bezier(.7,0,.2,1)] [clip-path:circle(0%_at_calc(100%-2.75rem)_2rem)] group-has-[#thd-15-menu:checked]/thd15:visible group-has-[#thd-15-menu:checked]/thd15:[clip-path:circle(150%_at_calc(100%-2.75rem)_2rem)]">
    <div class="mx-auto grid min-h-full max-w-7xl gap-10 px-[clamp(.75rem,3vw,1.75rem)] pb-10 pt-24 md:grid-cols-[1fr_18rem] md:items-end">
      <nav aria-label="Main">
        <ul class="group/list grid gap-1">
          <li style="--i:1" class="group-has-[#thd-15-menu:checked]/thd15:animate-thd15-rise"><a href="#thd-15-main" aria-current="page" class="group/l flex items-baseline gap-4 py-1 font-thd15-display text-[clamp(2.6rem,9vw,6rem)] font-bold leading-[1] tracking-[-.03em] transition-opacity group-hover/list:opacity-35 hover:!opacity-100"><span class="font-thd15-sans text-sm font-medium text-thd15-acc">01</span>Work<span aria-hidden="true" class="hidden size-3 self-center rounded-full bg-thd15-acc group-aria-[current=page]/l:block"></span></a></li>
          <li style="--i:2" class="group-has-[#thd-15-menu:checked]/thd15:animate-thd15-rise"><a href="#thd-15-main" class="flex items-baseline gap-4 py-1 font-thd15-display text-[clamp(2.6rem,9vw,6rem)] font-bold leading-[1] tracking-[-.03em] transition-opacity group-hover/list:opacity-35 hover:!opacity-100"><span class="font-thd15-sans text-sm font-medium text-thd15-acc">02</span>Services</a></li>
          <li style="--i:3" class="group-has-[#thd-15-menu:checked]/thd15:animate-thd15-rise"><a href="#thd-15-main" class="flex items-baseline gap-4 py-1 font-thd15-display text-[clamp(2.6rem,9vw,6rem)] font-bold leading-[1] tracking-[-.03em] transition-opacity group-hover/list:opacity-35 hover:!opacity-100"><span class="font-thd15-sans text-sm font-medium text-thd15-acc">03</span>Studio</a></li>
          <li style="--i:4" class="group-has-[#thd-15-menu:checked]/thd15:animate-thd15-rise"><a href="#thd-15-main" class="flex items-baseline gap-4 py-1 font-thd15-display text-[clamp(2.6rem,9vw,6rem)] font-bold leading-[1] tracking-[-.03em] transition-opacity group-hover/list:opacity-35 hover:!opacity-100"><span class="font-thd15-sans text-sm font-medium text-thd15-acc">04</span>Writing</a></li>
          <li style="--i:5" class="group-has-[#thd-15-menu:checked]/thd15:animate-thd15-rise"><a href="#thd-15-main" class="flex items-baseline gap-4 py-1 font-thd15-display text-[clamp(2.6rem,9vw,6rem)] font-bold leading-[1] tracking-[-.03em] transition-opacity group-hover/list:opacity-35 hover:!opacity-100"><span class="font-thd15-sans text-sm font-medium text-thd15-acc">05</span>Contact</a></li>
        </ul>
      </nav>
      <div style="--i:6" class="grid gap-6 border-t border-thd15-overink/20 pt-6 text-sm group-has-[#thd-15-menu:checked]/thd15:animate-thd15-rise">
        <div><p class="text-xs uppercase tracking-[.16em] text-thd15-acc">Studio</p><p class="mt-2 leading-relaxed">Unit 4, Ropewalk<br>Bristol BS1 6QT</p></div>
        <div><p class="text-xs uppercase tracking-[.16em] text-thd15-acc">New work</p><p class="mt-2 leading-relaxed"><a href="#thd-15-main" class="underline-offset-4 hover:underline">[email protected]</a><br>+44 117 496 0142</p></div>
        <label for="thd-15-menu" class="inline-flex min-h-11 w-fit cursor-pointer items-center rounded-full border border-thd15-overink/30 px-4 font-semibold hover:bg-thd15-overink hover:text-thd15-over">Close navigation menu</label>
      </div>
    </div>
  </div>
  <main id="thd-15-main" class="px-[clamp(.75rem,3vw,1.75rem)] pb-20 pt-[clamp(3rem,10vw,7rem)]">
    <h1 class="max-w-[12ch] font-thd15-display text-[clamp(3rem,11vw,8rem)] font-extrabold leading-[.9] tracking-[-.04em]">Interfaces with <span class="text-thd15-acc">nerve.</span></h1>
    <p class="mt-6 max-w-[42ch] text-lg text-thd15-mut">Open the menu: the overlay pours out of the button as an expanding circle, and the items rise in sequence.</p>
    <div aria-hidden="true" class="h-[50svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd15-bg: var(--thd15-bg);
  --color-thd15-ink: var(--thd15-ink);
  --color-thd15-mut: var(--thd15-mut);
  --color-thd15-acc: var(--thd15-acc);
  --color-thd15-over: var(--thd15-over);
  --color-thd15-overink: var(--thd15-overink);
}

@theme {
  --font-thd15-display: 'Syne', system-ui, sans-serif;
  --font-thd15-sans: 'Schibsted Grotesk', system-ui, sans-serif;
  --animate-thd15-rise: thd15-rise 700ms cubic-bezier(0.2,0.8,0.2,1) calc(var(--i, 1) * 60ms + 180ms) backwards;

  @keyframes thd15-rise {
    from {
      opacity: 0;
      translate: 0 2.5rem;
    }
  }
}

.thd-15 {
  width: 100%;
  min-height: 100svh;
  --thd15-bg: #0e0e0c;
  --thd15-ink: #f2f0e8;
  --thd15-mut: #a9a69b;
  --thd15-acc: #c6f432;
  --thd15-over: #1b1b17;
  --thd15-overink: #f2f0e8;
}

.thd-15:has(#thd-15-t:checked) {
  --thd15-bg: #f2f0e8;
  --thd15-ink: #0e0e0c;
  --thd15-mut: #55534b;
  --thd15-acc: #4d7c0f;
  --thd15-over: #0e0e0c;
  --thd15-overink: #f2f0e8;
}

@media (prefers-reduced-motion: reduce) {
  .thd-15 * {
    animation: none !important;
    transition-duration: 1ms !important;
  }
}
```
