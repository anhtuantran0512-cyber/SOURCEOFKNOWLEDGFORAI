---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-centered-logo-editorial-header/"
title: "Tailwind Centered Logo Editorial Header"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "A masthead in the newspaper tradition: dateline and issue on the left, a serif wordmark dead centre, subscribe and account on the right, and a section row…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Centered Logo Editorial Header
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-centered-logo-editorial-header/

A masthead in the newspaper tradition: dateline and issue on the left, a serif wordmark dead centre, subscribe and account on the right, and a section row under a double rule. The centring is structural — grid-cols-[1fr_auto_1fr] — so the wordmark stays exactly centred however long either side gets.
## HTML
```html
<div class="thd-07 group/thd07 w-full min-h-svh bg-thd07-bg font-thd07-sans text-thd07-ink antialiased">
  <a href="#thd-07-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:bg-thd07-ink focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-thd07-bg">Skip to content</a>
  <header class="sticky top-0 z-40 bg-thd07-bg/95 backdrop-blur-md">
    <div class="mx-auto grid max-w-6xl grid-cols-[1fr_auto_1fr] items-center gap-3 px-[clamp(.75rem,3vw,1.5rem)] py-3 sm:py-4">
      <p class="hidden text-xs leading-snug text-thd07-mut sm:block"><time datetime="2026-09-25" class="block font-semibold text-thd07-ink">Friday, 25 September 2026</time>Issue 214 &middot; London edition</p>
      <span class="sm:hidden"></span>
      <a href="#thd-07-main" class="text-center font-thd07-serif text-[clamp(2rem,6vw,3.4rem)] leading-none tracking-[-.01em]">The Ledger</a>
      <div class="flex items-center justify-self-end gap-1">
        <input id="thd-07-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-07-t" class="grid size-11 cursor-pointer place-items-center rounded-full hover:bg-thd07-ink/5 peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd07-ink">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-07-t:checked]/thd07:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-07-t:checked]/thd07:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-07-main" class="hidden px-2 py-2 text-sm font-medium underline-offset-4 hover:underline md:block">Account</a>
        <a href="#thd-07-main" class="grid min-h-10 place-items-center bg-thd07-acc px-3.5 text-sm font-semibold text-white transition-colors hover:bg-thd07-ink">Subscribe</a>
      </div>
    </div>
    <nav aria-label="Sections" class="mx-auto max-w-6xl px-[clamp(.75rem,3vw,1.5rem)]">
      <ul class="flex snap-x gap-6 overflow-x-auto border-y-[3px] border-double border-thd07-ink py-2.5 pr-8 text-[13px] font-semibold uppercase tracking-[.12em] [scrollbar-width:none] mask-[linear-gradient(90deg,#000_85%,transparent)] md:justify-center md:gap-9 md:pr-0 md:mask-none">
        <li class="snap-start"><a href="#thd-07-main" aria-current="page" class="whitespace-nowrap py-1 hover:text-thd07-acc aria-[current=page]:text-thd07-acc aria-[current=page]:underline aria-[current=page]:decoration-2 aria-[current=page]:underline-offset-[6px]">Markets</a></li>
        <li class="snap-start"><a href="#thd-07-main" class="whitespace-nowrap py-1 hover:text-thd07-acc">Policy</a></li>
        <li class="snap-start"><a href="#thd-07-main" class="whitespace-nowrap py-1 hover:text-thd07-acc">Technology</a></li>
        <li class="snap-start"><a href="#thd-07-main" class="whitespace-nowrap py-1 hover:text-thd07-acc">Culture</a></li>
        <li class="snap-start"><a href="#thd-07-main" class="whitespace-nowrap py-1 hover:text-thd07-acc">Letters</a></li>
        <li class="snap-start"><a href="#thd-07-main" class="whitespace-nowrap py-1 hover:text-thd07-acc">Archive</a></li>
      </ul>
    </nav>
  </header>
  <main id="thd-07-main" class="mx-auto grid max-w-6xl gap-8 px-[clamp(.75rem,3vw,1.5rem)] py-10 md:grid-cols-[2fr_1fr]">
    <article>
      <p class="text-xs font-bold uppercase tracking-[.16em] text-thd07-acc">Markets</p>
      <h1 class="mt-2 font-thd07-serif text-[clamp(2.2rem,5.5vw,3.6rem)] leading-[1.02] text-balance">Sterling steadies as the Bank signals a longer pause</h1>
      <p class="mt-4 max-w-[58ch] text-[1.05rem] leading-relaxed text-thd07-mut">The centred wordmark sits on a <code>1fr auto 1fr</code> grid &mdash; resize the frame and it never drifts off the axis, however long the dateline gets.</p>
    </article>
    <aside class="border-t border-thd07-ink pt-3 md:border-l md:border-t-0 md:pl-6 md:pt-0">
      <p class="text-xs font-bold uppercase tracking-[.16em]">Most read</p>
      <ol class="mt-3 grid gap-3 font-thd07-serif text-xl leading-tight">
        <li class="flex gap-3"><span class="text-thd07-acc">1</span>The quiet return of the four-day week</li>
        <li class="flex gap-3"><span class="text-thd07-acc">2</span>Inside Dublin&rsquo;s data-centre moratorium</li>
        <li class="flex gap-3"><span class="text-thd07-acc">3</span>Letters: on the price of a pint</li>
      </ol>
    </aside>
    <div aria-hidden="true" class="h-[60svh] md:col-span-2"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd07-bg: var(--thd07-bg);
  --color-thd07-ink: var(--thd07-ink);
  --color-thd07-mut: var(--thd07-mut);
  --color-thd07-acc: var(--thd07-acc);
}

@theme {
  --font-thd07-serif: 'Instrument Serif', Georgia, serif;
  --font-thd07-sans: 'IBM Plex Sans', system-ui, sans-serif;
}

.thd-07 {
  width: 100%;
  min-height: 100svh;
  --thd07-bg: #f6f2ea;
  --thd07-ink: #16130f;
  --thd07-mut: #5a5347;
  --thd07-acc: #a3231b;
}

.thd-07:has(#thd-07-t:checked) {
  --thd07-bg: #12110e;
  --thd07-ink: #efe9dd;
  --thd07-mut: #aaa192;
  --thd07-acc: #ef6a5e;
}
```
