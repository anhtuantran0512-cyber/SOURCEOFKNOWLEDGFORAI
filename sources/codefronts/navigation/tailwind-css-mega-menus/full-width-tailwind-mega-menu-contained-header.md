---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/full-width-tailwind-mega-menu-contained-header/"
title: "Full-Width Tailwind Mega Menu Inside a Contained Header"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "The panel paints edge to edge while its content stays aligned to the logo."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Width Tailwind Mega Menu Inside a Contained Header
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/full-width-tailwind-mega-menu-contained-header/

The panel paints edge to edge while its content stays aligned to the logo. The trick is which box is the containing block: items are static, so the panel's absolute inset-x-0 resolves against the full-width <header>, and an inner w-[min(72rem,calc(100%-2rem))] mx-auto re-applies the page column. A seasonal garden retailer, with a curtain that opens from the centre outward. Zero JavaScript.
## HTML
```html
<section class="tmm-06 relative w-full min-h-svh overflow-x-clip bg-tmm06-bg font-tmm06-sans leading-[1.55] text-tmm06-ink [&_:focus-visible]:rounded [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm06-acc" aria-labelledby="tmm06-title">
  <h2 class="sr-only" id="tmm06-title">Fern</h2>
  <p class="grid min-h-9 place-items-center bg-tmm06-acc px-4 text-center text-[0.78rem]/snug font-semibold tracking-[0.02em] text-tmm06-on-acc">Free delivery on orders over &pound;40 &middot; Autumn bulbs now shipping</p>

  <div class="absolute top-[49px] right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm06-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmm06-line bg-tmm06-surf text-tmm06-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm06-acc" for="tmm06-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b border-tmm06-line bg-tmm06-surf">
    <div class="mx-auto flex min-h-[70px] w-[min(72rem,calc(100%-2rem))] flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,2rem)] pr-15 max-[54rem]:flex-col max-[54rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm06-display text-[1.35rem]/none font-bold tracking-[-0.01em] text-tmm06-ink" href="#tmm06-title">
        <svg class="size-[22px] text-tmm06-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 21V9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M12 13c-4 0-7-3-7-8 4 0 7 3 7 8Zm0-2c0-4 3-7 7-7 0 4-3 7-7 7Z" fill="currentColor"/></svg>
        Fern
      </a>
      <nav class="flex min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-1 max-[54rem]:flex-col">
          <li data-tmm06-item class="flex items-stretch max-[54rem]:block">
            <button type="button" aria-expanded="false" aria-controls="tmm06-panel-grow" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-md px-3.5 text-[0.92rem]/none font-semibold text-tmm06-ink transition-colors hover:text-tmm06-acc tmm06-open:text-tmm06-acc!">Grow
              <svg class="size-[15px] transition-transform duration-200 tmm06-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm06-line bg-tmm06-panel opacity-0 shadow-tmm06-panel pointer-events-none transition-[opacity,visibility] duration-160 tmm06-open:visible tmm06-open:opacity-100 tmm06-open:pointer-events-auto motion-reduce:transition-none max-[54rem]:static max-[54rem]:hidden max-[54rem]:visible max-[54rem]:opacity-100 max-[54rem]:shadow-none max-[54rem]:tmm06-open:block" id="tmm06-panel-grow" aria-label="Grow">
              <div class="mx-auto grid w-[min(72rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.9rem,2.5vw,2.5rem)] py-[clamp(1.1rem,3vw,2rem)] [clip-path:inset(0_46%_0_46%)] opacity-35 transition-[clip-path,opacity] duration-[480ms,320ms] ease-tmm06-out tmm06-open:[clip-path:inset(-10px)] tmm06-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none max-[54rem]:w-full max-[54rem]:px-4">
                <div class="grid min-w-0 content-start gap-2 rounded-2xl bg-tmm06-acc/9 p-4.5">
                  <p class="font-tmm06-display text-[0.7rem]/none font-bold tracking-[0.18em] text-tmm06-acc uppercase">Field notes</p>
                  <p class="font-tmm06-display text-[1.08rem]/snug font-medium text-pretty">Seasonal planting guidance written by growers, not marketers.</p>
                  <a class="group/cta mt-1 inline-flex min-h-11 w-fit items-center gap-2 rounded-full bg-tmm06-acc px-4 py-2 text-left text-[0.84rem]/tight font-semibold text-tmm06-on-acc transition-[filter] hover:brightness-110" href="#tmm06-title">Read the autumn guide <span aria-hidden="true" class="transition-transform group-hover/cta:translate-x-0.5">&rarr;</span></a>
                </div>
                <section class="min-w-0" aria-labelledby="tmm06-h-soil">
                  <h3 class="mb-1 font-tmm06-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm06-mut uppercase" id="tmm06-h-soil">Soil</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Composting</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">pH testing</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Mulch types</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Raised beds</span></a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm06-h-water">
                  <h3 class="mb-1 font-tmm06-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm06-mut uppercase" id="tmm06-h-water">Water</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Drip systems</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Rain capture</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Drought planting</span></a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm06-h-season">
                  <h3 class="mb-1 font-tmm06-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm06-mut uppercase" id="tmm06-h-season">Season</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Frost dates</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Overwintering</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Cover crops</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Bulb planner</span></a></li>
                  </ul>
                </section>
              </div>
            </div>
          </li>

          <li data-tmm06-item class="flex items-stretch max-[54rem]:block">
            <button type="button" aria-expanded="false" aria-controls="tmm06-panel-shop" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-md px-3.5 text-[0.92rem]/none font-semibold text-tmm06-ink transition-colors hover:text-tmm06-acc tmm06-open:text-tmm06-acc!">Shop
              <svg class="size-[15px] transition-transform duration-200 tmm06-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm06-line bg-tmm06-panel opacity-0 shadow-tmm06-panel pointer-events-none transition-[opacity,visibility] duration-160 tmm06-open:visible tmm06-open:opacity-100 tmm06-open:pointer-events-auto motion-reduce:transition-none max-[54rem]:static max-[54rem]:hidden max-[54rem]:visible max-[54rem]:opacity-100 max-[54rem]:shadow-none max-[54rem]:tmm06-open:block" id="tmm06-panel-shop" aria-label="Shop">
              <div class="mx-auto grid w-[min(72rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.9rem,2.5vw,2.5rem)] py-[clamp(1.1rem,3vw,2rem)] [clip-path:inset(0_46%_0_46%)] opacity-35 transition-[clip-path,opacity] duration-[480ms,320ms] ease-tmm06-out tmm06-open:[clip-path:inset(-10px)] tmm06-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none max-[54rem]:w-full max-[54rem]:px-4">
                <div class="grid min-w-0 content-start gap-2 rounded-2xl bg-tmm06-acc/9 p-4.5">
                  <p class="font-tmm06-display text-[0.7rem]/none font-bold tracking-[0.18em] text-tmm06-acc uppercase">In season</p>
                  <p class="font-tmm06-display text-[1.08rem]/snug font-medium text-pretty">Bulbs and bare-root stock, lifted this week and shipped within two days.</p>
                  <a class="group/cta mt-1 inline-flex min-h-11 w-fit items-center gap-2 rounded-full bg-tmm06-acc px-4 py-2 text-left text-[0.84rem]/tight font-semibold text-tmm06-on-acc transition-[filter] hover:brightness-110" href="#tmm06-title">Shop autumn planting <span aria-hidden="true" class="transition-transform group-hover/cta:translate-x-0.5">&rarr;</span></a>
                </div>
                <section class="min-w-0" aria-labelledby="tmm06-h-plants">
                  <h3 class="mb-1 font-tmm06-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm06-mut uppercase" id="tmm06-h-plants">Plants</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Bulbs</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Perennials</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Hedging</span></a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm06-h-tools">
                  <h3 class="mb-1 font-tmm06-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm06-mut uppercase" id="tmm06-h-tools">Tools</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Spades and forks</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Secateurs</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Watering</span></a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm06-h-gifts">
                  <h3 class="mb-1 font-tmm06-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm06-mut uppercase" id="tmm06-h-gifts">Gifts</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Gift cards</span></a></li>
                    <li><a href="#tmm06-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm06-ink"><span class="bg-[linear-gradient(currentColor,currentColor)] bg-[length:0%_1px] bg-left-bottom bg-no-repeat pb-0.5 transition-[background-size,color] duration-300 hover:bg-[length:100%_1px] hover:text-tmm06-acc">Starter kits</span></a></li>
                  </ul>
                </section>
              </div>
            </div>
          </li>

          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center rounded-md px-3.5 text-[0.92rem]/none font-semibold text-tmm06-ink hover:text-tmm06-acc" href="#tmm06-title">Journal</a></li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center rounded-md px-3.5 text-[0.92rem]/none font-semibold text-tmm06-ink hover:text-tmm06-acc" href="#tmm06-title">Visit us</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-2 max-[54rem]:ml-0">
        <a class="inline-flex min-h-11 items-center px-2.5 text-[0.86rem] font-semibold text-tmm06-mut hover:text-tmm06-ink" href="#tmm06-title">Account</a>
        <a class="relative inline-flex min-h-11 items-center gap-2 rounded-full border border-tmm06-line px-3.5 text-[0.86rem]/none font-semibold text-tmm06-ink transition-colors hover:border-tmm06-acc" href="#tmm06-title">
          <svg class="size-[19px]" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 8h14l-1.2 11H6.2Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 8a3 3 0 0 1 6 0" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>
          Basket <span class="grid size-5 place-items-center rounded-full bg-tmm06-acc text-[0.68rem] text-tmm06-on-acc tabular-nums"><span class="sr-only">items: </span>3</span>
        </a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(72rem,calc(100%-2rem))] py-[clamp(3rem,10vw,6rem)]">
    <div class="grid max-w-[38rem] gap-3">
      <p class="font-tmm06-display text-[0.74rem]/none font-bold tracking-[0.22em] text-tmm06-acc uppercase">Autumn 2026</p>
      <h1 class="font-tmm06-display text-[clamp(2.1rem,6vw,3.7rem)]/[1.03] font-bold tracking-[-0.02em] text-balance">Plant now. Thank yourself in March.</h1>
      <p class="text-[clamp(0.95rem,2.3vw,1.1rem)] text-tmm06-mut text-pretty">Twelve hundred bulb varieties, lifted to order from our Somerset beds.</p>
      <a class="mt-1.5 inline-flex min-h-12 w-fit items-center gap-2 rounded-full bg-tmm06-acc px-5.5 text-[0.95rem]/none font-semibold text-tmm06-on-acc hover:brightness-110" href="#tmm06-title">Shop autumn planting <span aria-hidden="true">&rarr;</span></a>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm06-bg: #f2f5f0;
  --color-tmm06-bg: oklch(0.967 0.008 135);
  --color-tmm06-surf: #ffffff;
  --color-tmm06-surf: oklch(1 0 0);
  --color-tmm06-panel: #f6f8f3;
  --color-tmm06-panel: oklch(0.977 0.008 130);
  --color-tmm06-line: #d3ddcc;
  --color-tmm06-line: oklch(0.89 0.022 135);
  --color-tmm06-ink: #1b2a1f;
  --color-tmm06-ink: oklch(0.26 0.03 150);
  --color-tmm06-mut: #56685a;
  --color-tmm06-mut: oklch(0.49 0.03 150);
  --color-tmm06-acc: #2f6b3f;
  --color-tmm06-acc: oklch(0.46 0.11 152);
  --color-tmm06-on-acc: #ffffff;
  --color-tmm06-on-acc: oklch(1 0 0);
  --font-tmm06-display: 'Alegreya Sans', 'Trebuchet MS', sans-serif;
  --font-tmm06-sans: 'Karla', system-ui, sans-serif;
  --shadow-tmm06-panel: 0 24px 50px -34px rgb(27 42 31 / 0.4);
  --ease-tmm06-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm06-open: instead of a repeated selector list. */

@custom-variant tmm06-open {
  &:where([data-tmm06-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm06-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-06 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-06:has(#tmm06-theme:checked) {
  --color-tmm06-bg: #0e1510;
  --color-tmm06-bg: oklch(0.18 0.015 150);
  --color-tmm06-surf: #141d16;
  --color-tmm06-surf: oklch(0.21 0.018 150);
  --color-tmm06-panel: #18221a;
  --color-tmm06-panel: oklch(0.235 0.02 150);
  --color-tmm06-line: #2a382d;
  --color-tmm06-line: oklch(0.32 0.025 150);
  --color-tmm06-ink: #e7efe6;
  --color-tmm06-ink: oklch(0.94 0.014 145);
  --color-tmm06-mut: #9db09f;
  --color-tmm06-mut: oklch(0.74 0.03 150);
  --color-tmm06-acc: #7cc58d;
  --color-tmm06-acc: oklch(0.77 0.12 150);
  --color-tmm06-on-acc: #0e1a11;
  --color-tmm06-on-acc: oklch(0.2 0.03 150);
}

@media (prefers-color-scheme: dark) {
  .tmm-06 {
    --color-tmm06-bg: #0e1510;
    --color-tmm06-bg: oklch(0.18 0.015 150);
    --color-tmm06-surf: #141d16;
    --color-tmm06-surf: oklch(0.21 0.018 150);
    --color-tmm06-panel: #18221a;
    --color-tmm06-panel: oklch(0.235 0.02 150);
    --color-tmm06-line: #2a382d;
    --color-tmm06-line: oklch(0.32 0.025 150);
    --color-tmm06-ink: #e7efe6;
    --color-tmm06-ink: oklch(0.94 0.014 145);
    --color-tmm06-mut: #9db09f;
    --color-tmm06-mut: oklch(0.74 0.03 150);
    --color-tmm06-acc: #7cc58d;
    --color-tmm06-acc: oklch(0.77 0.12 150);
    --color-tmm06-on-acc: #0e1a11;
    --color-tmm06-on-acc: oklch(0.2 0.03 150);
  }

  .tmm-06:has(#tmm06-theme:checked) {
    --color-tmm06-bg: #f2f5f0;
    --color-tmm06-bg: oklch(0.967 0.008 135);
    --color-tmm06-surf: #ffffff;
    --color-tmm06-surf: oklch(1 0 0);
    --color-tmm06-panel: #f6f8f3;
    --color-tmm06-panel: oklch(0.977 0.008 130);
    --color-tmm06-line: #d3ddcc;
    --color-tmm06-line: oklch(0.89 0.022 135);
    --color-tmm06-ink: #1b2a1f;
    --color-tmm06-ink: oklch(0.26 0.03 150);
    --color-tmm06-mut: #56685a;
    --color-tmm06-mut: oklch(0.49 0.03 150);
    --color-tmm06-acc: #2f6b3f;
    --color-tmm06-acc: oklch(0.46 0.11 152);
    --color-tmm06-on-acc: #ffffff;
    --color-tmm06-on-acc: oklch(1 0 0);
  }
}
```
