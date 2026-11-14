---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-multi-level-dropdown-menu-header/"
title: "Tailwind Multi Level Dropdown Menu Header"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "Three levels of nested navigation opened by hover and by focus-within, each level flying out beside its parent row."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi Level Dropdown Menu Header
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-multi-level-dropdown-menu-header/

Three levels of nested navigation opened by hover and by focus-within, each level flying out beside its parent row. Every level is a real role="menu" with aria-haspopup triggers, the right-most menu flies left so it never leaves the viewport, and the whole tree is walkable with Tab alone. Ink-and-sand minimal luxury, no shadows.
## HTML
```html
<div class="thd-21 group/thd21 w-full min-h-svh bg-thd21-bg font-thd21-sans text-thd21-ink antialiased">
  <a href="#thd-21-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:bg-thd21-ink focus:px-4 focus:py-2.5 focus:text-sm focus:text-thd21-bg">Skip to content</a>
  <header class="sticky top-0 z-40 border-b border-thd21-ink bg-thd21-bg">
    <div class="mx-auto flex h-[72px] max-w-7xl items-center gap-8 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-21-main" class="whitespace-nowrap font-thd21-serif text-2xl font-semibold tracking-[.04em]">Aurelio <span class="font-thd21-sans text-[10px] font-normal uppercase tracking-[.3em] text-thd21-mut">est. 1974</span></a>
      <nav aria-label="Main" class="hidden md:block">
        <ul role="menubar" class="flex items-center text-[13px] uppercase tracking-[.18em]">
          <li role="none" class="group/l1 relative">
            <a role="menuitem" aria-haspopup="menu" href="#thd-21-main" class="flex h-[72px] items-center gap-1.5 px-4 hover:text-thd21-acc group-hover/l1:text-thd21-acc">Collections<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true" class="size-3 transition-transform group-hover/l1:rotate-180 group-focus-within/l1:rotate-180"><path d="m6 9 6 6 6-6"/></svg></a>
            <ul role="menu" aria-label="Collections" class="invisible absolute left-0 top-full w-56 -translate-y-1 border border-thd21-ink bg-thd21-bg py-2 normal-case tracking-normal opacity-0 transition-[opacity,translate,visibility] duration-200 group-hover/l1:visible group-hover/l1:translate-y-0 group-hover/l1:opacity-100 group-focus-within/l1:visible group-focus-within/l1:translate-y-0 group-focus-within/l1:opacity-100">
              <li role="none" class="group/l2 relative">
                <a role="menuitem" aria-haspopup="menu" href="#thd-21-main" class="flex min-h-11 items-center justify-between px-5 font-thd21-serif text-lg hover:bg-thd21-sand group-hover/l2:bg-thd21-sand">Fragrance<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true" class="size-3.5 transition-transform group-hover/l2:translate-x-0.5"><path d="m9 6 6 6-6 6"/></svg></a>
                <ul role="menu" aria-label="Fragrance" class="invisible absolute left-full top-0 -ml-px -mt-[9px] w-52 border border-thd21-ink bg-thd21-bg py-2 opacity-0 transition-[opacity,visibility] duration-150 group-hover/l2:visible group-hover/l2:opacity-100 group-focus-within/l2:visible group-focus-within/l2:opacity-100">
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Eau de parfum</a></li>
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Room sprays</a></li>
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Incense</a></li>
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center justify-between px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Discovery set <span class="text-[10px] uppercase tracking-[.2em] text-thd21-acc">New</span></a></li>
                </ul>
              </li>
              <li role="none" class="group/l2 relative">
                <a role="menuitem" aria-haspopup="menu" href="#thd-21-main" class="flex min-h-11 items-center justify-between px-5 font-thd21-serif text-lg hover:bg-thd21-sand group-hover/l2:bg-thd21-sand">Skin<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true" class="size-3.5 transition-transform group-hover/l2:translate-x-0.5"><path d="m9 6 6 6-6 6"/></svg></a>
                <ul role="menu" aria-label="Skin" class="invisible absolute left-full top-0 -ml-px -mt-[9px] w-52 border border-thd21-ink bg-thd21-bg py-2 opacity-0 transition-[opacity,visibility] duration-150 group-hover/l2:visible group-hover/l2:opacity-100 group-focus-within/l2:visible group-focus-within/l2:opacity-100">
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Cleansers</a></li>
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Serums</a></li>
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Balms</a></li>
                </ul>
              </li>
              <li role="none" class="group/l2 relative">
                <a role="menuitem" aria-haspopup="menu" href="#thd-21-main" class="flex min-h-11 items-center justify-between px-5 font-thd21-serif text-lg hover:bg-thd21-sand group-hover/l2:bg-thd21-sand">Home<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true" class="size-3.5 transition-transform group-hover/l2:translate-x-0.5"><path d="m9 6 6 6-6 6"/></svg></a>
                <ul role="menu" aria-label="Home" class="invisible absolute left-full top-0 -ml-px -mt-[9px] w-52 border border-thd21-ink bg-thd21-bg py-2 opacity-0 transition-[opacity,visibility] duration-150 group-hover/l2:visible group-hover/l2:opacity-100 group-focus-within/l2:visible group-focus-within/l2:opacity-100">
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Candles</a></li>
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Linen care</a></li>
                  <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-10 items-center px-5 text-sm hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Glassware</a></li>
                </ul>
              </li>
              <li role="none" class="mt-2 border-t border-thd21-line pt-2"><a role="menuitem" href="#thd-21-main" class="flex min-h-11 items-center px-5 font-thd21-serif text-lg italic hover:bg-thd21-sand hover:text-thd21-acc focus-visible:bg-thd21-sand">Gifting</a></li>
            </ul>
          </li>
          <li role="none" class="group/l1 relative">
            <a role="menuitem" aria-haspopup="menu" href="#thd-21-main" class="flex h-[72px] items-center gap-1.5 px-4 hover:text-thd21-acc group-hover/l1:text-thd21-acc">Stores<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true" class="size-3 transition-transform group-hover/l1:rotate-180 group-focus-within/l1:rotate-180"><path d="m6 9 6 6 6-6"/></svg></a>
            <ul role="menu" aria-label="Stores" class="invisible absolute left-0 top-full w-64 -translate-y-1 border border-thd21-ink bg-thd21-bg py-2 normal-case tracking-normal opacity-0 transition-[opacity,translate,visibility] duration-200 group-hover/l1:visible group-hover/l1:translate-y-0 group-hover/l1:opacity-100 group-focus-within/l1:visible group-focus-within/l1:translate-y-0 group-focus-within/l1:opacity-100">
              <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-11 flex-col justify-center px-5 py-1 hover:bg-thd21-sand focus-visible:bg-thd21-sand"><span class="font-thd21-serif text-lg leading-tight">London</span><span class="text-xs text-thd21-mut">Marylebone High Street</span></a></li>
              <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-11 flex-col justify-center px-5 py-1 hover:bg-thd21-sand focus-visible:bg-thd21-sand"><span class="font-thd21-serif text-lg leading-tight">Edinburgh</span><span class="text-xs text-thd21-mut">Stockbridge</span></a></li>
              <li role="none"><a role="menuitem" href="#thd-21-main" class="flex min-h-11 flex-col justify-center px-5 py-1 hover:bg-thd21-sand focus-visible:bg-thd21-sand"><span class="font-thd21-serif text-lg leading-tight">Dublin</span><span class="text-xs text-thd21-mut">Drury Street</span></a></li>
              <li role="none" class="mt-2 border-t border-thd21-line pt-2"><a role="menuitem" href="#thd-21-main" class="flex min-h-11 items-center px-5 text-sm text-thd21-acc hover:bg-thd21-sand focus-visible:bg-thd21-sand">Find a stockist &rarr;</a></li>
            </ul>
          </li>
          <li role="none"><a role="menuitem" href="#thd-21-main" class="flex h-[72px] items-center px-4 hover:text-thd21-acc">Journal</a></li>
          <li role="none"><a role="menuitem" href="#thd-21-main" class="flex h-[72px] items-center px-4 hover:text-thd21-acc">About</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1 text-[12px] uppercase tracking-[.18em]">
        <input id="thd-21-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-21-t" class="grid size-11 cursor-pointer place-items-center hover:text-thd21-acc peer-focus-visible/t:outline-1 peer-focus-visible/t:outline-thd21-ink">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-21-t:checked]/thd21:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-21-t:checked]/thd21:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-21-main" class="hidden px-3 py-3 hover:text-thd21-acc lg:block">Search</a>
        <a href="#thd-21-main" class="hidden px-3 py-3 hover:text-thd21-acc sm:block">Account</a>
        <a href="#thd-21-main" class="flex min-h-11 items-center border border-thd21-ink px-4 transition-colors hover:bg-thd21-ink hover:text-thd21-bg">Bag (2)</a>
      </div>
    </div>
  </header>
  <main id="thd-21-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.5rem)] py-[clamp(3rem,9vw,6rem)]">
    <p class="text-[11px] uppercase tracking-[.3em] text-thd21-mut">Autumn / Winter</p>
    <h1 class="mt-4 max-w-[14ch] font-thd21-serif text-[clamp(2.8rem,8vw,5.6rem)] font-medium italic leading-[.95]">Scent, slowly.</h1>
    <p class="mt-6 max-w-[46ch] text-thd21-mut">Hover Collections, then Fragrance: each level flies out beside its parent. Tab alone walks all three levels.</p>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd21-bg: var(--thd21-bg);
  --color-thd21-sand: var(--thd21-sand);
  --color-thd21-ink: var(--thd21-ink);
  --color-thd21-mut: var(--thd21-mut);
  --color-thd21-line: var(--thd21-line);
  --color-thd21-acc: var(--thd21-acc);
}

@theme {
  --font-thd21-serif: 'Cormorant Garamond', Georgia, serif;
  --font-thd21-sans: 'Jost', system-ui, sans-serif;
}

.thd-21 {
  width: 100%;
  min-height: 100svh;
  --thd21-bg: #f4efe6;
  --thd21-sand: #e9e0d0;
  --thd21-ink: #1b1712;
  --thd21-mut: #625a4e;
  --thd21-line: #d6ccba;
  --thd21-acc: #8a5a2b;
}

.thd-21:has(#thd-21-t:checked) {
  --thd21-bg: #14110d;
  --thd21-sand: #221d17;
  --thd21-ink: #eee6d8;
  --thd21-mut: #aa9f8e;
  --thd21-line: #3a3228;
  --thd21-acc: #d6a86e;
}
```
