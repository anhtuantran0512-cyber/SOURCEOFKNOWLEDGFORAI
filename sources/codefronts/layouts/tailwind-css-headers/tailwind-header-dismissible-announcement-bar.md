---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-header-dismissible-announcement-bar/"
title: "Tailwind Header with Dismissible Announcement Bar"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "A promo bar above the header that collapses to nothing when dismissed — no script, no display:none jump."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Header with Dismissible Announcement Bar
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-header-dismissible-announcement-bar/

A promo bar above the header that collapses to nothing when dismissed — no script, no display:none jump. The close button is a label for a hidden checkbox and the bar animates grid-rows-[1fr] → grid-rows-[0fr], the modern way to transition to intrinsic zero height. New: a small Offer chip appears in the header after dismissal, so the promotion is recoverable.
## HTML
```html
<div class="thd-17 group/thd17 w-full min-h-svh bg-thd17-bg font-thd17-sans text-thd17-ink antialiased">
  <a href="#thd-17-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-xl focus:bg-thd17-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <input id="thd-17-x" type="checkbox" class="sr-only" aria-label="Dismiss announcement">
  <div class="grid grid-rows-[1fr] bg-thd17-acc text-white transition-[grid-template-rows] duration-500 ease-[cubic-bezier(.2,.8,.2,1)] group-has-[#thd-17-x:checked]/thd17:grid-rows-[0fr]">
    <div class="min-h-0 overflow-hidden">
      <div class="mx-auto flex max-w-6xl items-center gap-3 px-[clamp(.75rem,3vw,1.5rem)] py-2 text-sm">
        <p class="min-w-0 flex-1 text-center"><span class="mr-2 rounded-full bg-white/20 px-2 py-0.5 text-[11px] font-bold uppercase tracking-wide">New</span>Autumn roasts land Thursday &mdash; subscribers get first pick and free delivery over &pound;30. <a href="#thd-17-main" class="font-semibold underline underline-offset-2 hover:no-underline">See the lineup</a></p>
        <label for="thd-17-x" class="grid size-11 flex-none cursor-pointer place-items-center rounded-full hover:bg-white/15 group-has-[#thd-17-x:focus-visible]/thd17:outline-2 group-has-[#thd-17-x:focus-visible]/thd17:outline-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" class="size-4"><path d="M6 6l12 12M18 6 6 18"/></svg><span class="sr-only">Dismiss announcement</span></label>
      </div>
    </div>
  </div>
  <header class="sticky top-0 z-40 bg-thd17-bg/95 px-[clamp(.75rem,3vw,1.5rem)] py-3 backdrop-blur-md">
    <div class="mx-auto flex h-14 max-w-6xl items-center gap-3 rounded-2xl bg-thd17-bg px-3 shadow-[6px_6px_14px_var(--color-thd17-lo),-6px_-6px_14px_var(--color-thd17-hi)] sm:px-5">
      <a href="#thd-17-main" class="flex items-center gap-2 font-thd17-serif text-xl"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-thd17-bg text-thd17-acc shadow-[inset_2px_2px_5px_var(--color-thd17-lo),inset_-2px_-2px_5px_var(--color-thd17-hi)]"><svg viewBox="0 0 24 24" fill="currentColor" class="size-4"><ellipse cx="12" cy="12" rx="5.5" ry="8" transform="rotate(30 12 12)"/></svg></span>Kiln &amp; Co</a>
      <label for="thd-17-x" class="hidden cursor-pointer items-center gap-1.5 rounded-full bg-thd17-acc/12 px-2.5 py-1 text-xs font-semibold text-thd17-acc hover:bg-thd17-acc/20 group-has-[#thd-17-x:checked]/thd17:inline-flex"><span aria-hidden="true" class="size-1.5 rounded-full bg-thd17-acc"></span>Offer<span class="sr-only"> — show announcement again</span></label>
      <nav aria-label="Main" class="mx-auto hidden md:block">
        <ul class="flex items-center gap-1 text-sm font-medium">
          <li><a href="#thd-17-main" aria-current="page" class="rounded-xl px-3.5 py-2 text-thd17-mut transition hover:text-thd17-ink aria-[current=page]:text-thd17-ink aria-[current=page]:shadow-[inset_2px_2px_5px_var(--color-thd17-lo),inset_-2px_-2px_5px_var(--color-thd17-hi)]">Coffee</a></li>
          <li><a href="#thd-17-main" class="rounded-xl px-3.5 py-2 text-thd17-mut transition hover:text-thd17-ink">Subscriptions</a></li>
          <li><a href="#thd-17-main" class="rounded-xl px-3.5 py-2 text-thd17-mut transition hover:text-thd17-ink">Equipment</a></li>
          <li><a href="#thd-17-main" class="rounded-xl px-3.5 py-2 text-thd17-mut transition hover:text-thd17-ink">Roastery</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1.5 md:ml-0">
        <input id="thd-17-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-17-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd17-mut hover:text-thd17-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd17-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-17-t:checked]/thd17:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-17-t:checked]/thd17:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-17-main" class="hidden rounded-xl px-3 py-2 text-sm font-medium text-thd17-mut hover:text-thd17-ink sm:block">Account</a>
        <a href="#thd-17-main" aria-label="Basket, 2 items" class="flex min-h-11 items-center gap-2 rounded-xl bg-thd17-bg px-4 text-sm font-semibold shadow-[4px_4px_10px_var(--color-thd17-lo),-4px_-4px_10px_var(--color-thd17-hi)] transition active:shadow-[inset_3px_3px_7px_var(--color-thd17-lo),inset_-3px_-3px_7px_var(--color-thd17-hi)]"><span aria-hidden="true">Basket</span><span aria-hidden="true" class="grid size-5 place-items-center rounded-full bg-thd17-acc text-[11px] font-bold text-white">2</span></a>
      </div>
    </div>
  </header>
  <main id="thd-17-main" class="mx-auto max-w-6xl px-[clamp(.75rem,3vw,1.5rem)] py-12">
    <h1 class="max-w-[16ch] font-thd17-serif text-[clamp(2.4rem,7vw,4.4rem)] leading-[1.02]">Small-batch coffee, roasted on Tuesdays.</h1>
    <p class="mt-5 max-w-[48ch] text-lg text-thd17-mut">Dismiss the bar above: it collapses smoothly to zero height, and an <strong class="text-thd17-acc">Offer</strong> chip appears next to the logo to bring it back.</p>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd17-bg: var(--thd17-bg);
  --color-thd17-ink: var(--thd17-ink);
  --color-thd17-mut: var(--thd17-mut);
  --color-thd17-acc: var(--thd17-acc);
  --color-thd17-hi: var(--thd17-hi);
  --color-thd17-lo: var(--thd17-lo);
}

@theme {
  --font-thd17-serif: 'Young Serif', Georgia, serif;
  --font-thd17-sans: 'Figtree', system-ui, sans-serif;
}

.thd-17 {
  width: 100%;
  min-height: 100svh;
  --thd17-bg: #efe6da;
  --thd17-ink: #2b1d12;
  --thd17-mut: #6a5646;
  --thd17-acc: #9a4a1e;
  --thd17-hi: rgb(255 255 255 / 0.75);
  --thd17-lo: rgb(150 118 88 / 0.38);
}

.thd-17:has(#thd-17-t:checked) {
  --thd17-bg: #231a14;
  --thd17-ink: #f3e6d6;
  --thd17-mut: #bba692;
  --thd17-acc: #e08a52;
  --thd17-hi: rgb(255 255 255 / 0.05);
  --thd17-lo: rgb(0 0 0 / 0.5);
}
```
