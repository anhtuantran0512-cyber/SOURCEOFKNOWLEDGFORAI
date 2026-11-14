---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/editorial-tailwind-mega-menu-featured-image/"
title: "Editorial Tailwind Mega Menu with Featured Article Image"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "A newspaper masthead whose Sections panel pairs three ruled link columns with a featured long read: a lazy-loaded photo that settles from an overscale and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Tailwind Mega Menu with Featured Article Image
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/editorial-tailwind-mega-menu-featured-image/

A newspaper masthead whose Sections panel pairs three ruled link columns with a featured long read: a lazy-loaded photo that settles from an overscale and blooms from grayscale to colour on hover. Link rows rise from behind their own baseline with a clip-path reveal, like type set into a column. Libre Caslon and Libre Franklin carry the editorial voice. Zero JavaScript.
## HTML
```html
<section class="tmm-15 relative w-full min-h-svh bg-tmm15-bg font-tmm15-sans leading-[1.55] text-tmm15-ink [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm15-acc" aria-labelledby="tmm15-title">
  <h2 class="sr-only" id="tmm15-title">The Meridian Review</h2>

  <div class="absolute top-3 right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm15-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmm15-line bg-tmm15-surf text-tmm15-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm15-acc" for="tmm15-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="mx-auto grid w-[min(74rem,calc(100%-2rem))] justify-items-center gap-1.5 pt-[clamp(2.5rem,6vw,3rem)] pb-[clamp(0.9rem,2.5vw,1.4rem)] text-center">
    <p class="text-[0.7rem]/none font-medium tracking-[0.22em] text-tmm15-mut uppercase">Friday, 28 August 2026 &middot; Late edition</p>
    <p class="font-tmm15-display text-[clamp(1.9rem,7vw,3.6rem)]/none tracking-[-0.015em]">The Meridian Review</p>
    <p class="text-[0.8rem]/none text-tmm15-mut italic">Reporting from 24 bureaux</p>
  </header>
  <header class="relative z-10 w-full border-y border-tmm15-ink bg-tmm15-surf">
    <nav class="mx-auto w-[min(74rem,calc(100%-2rem))]" aria-label="Primary">
      <ul class="flex min-h-[54px] flex-wrap items-stretch justify-center gap-[clamp(0.25rem,2vw,1.5rem)] max-[48rem]:justify-start max-[48rem]:py-1.5">
        <li data-tmm15-item class="flex items-stretch max-[48rem]:block">
            <button type="button" id="tmm15-trigger-sections" aria-expanded="false" aria-controls="tmm15-panel-sections" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 px-2.5 text-[0.8rem]/none font-medium tracking-[0.16em] text-tmm15-ink uppercase transition-[color,box-shadow] hover:text-tmm15-acc tmm15-open:text-tmm15-acc! tmm15-open:shadow-[inset_0_-2px_0_var(--color-tmm15-acc)]">Sections<svg class="size-3.5 transition-transform duration-200 tmm15-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm15-ink bg-tmm15-surf opacity-0 shadow-tmm15-panel pointer-events-none transition-[opacity,visibility] duration-170 tmm15-open:visible tmm15-open:opacity-100 tmm15-open:pointer-events-auto motion-reduce:transition-none max-[48rem]:static max-[48rem]:hidden max-[48rem]:visible max-[48rem]:opacity-100 max-[48rem]:shadow-none max-[48rem]:tmm15-open:block" id="tmm15-panel-sections" aria-labelledby="tmm15-trigger-sections">
              <div class="mx-auto grid w-[min(74rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,10rem),1fr))] gap-[clamp(1rem,3vw,2.5rem)] py-[clamp(1.1rem,3vw,2rem)] min-[64rem]:grid-cols-[repeat(3,minmax(0,1fr))_20rem] max-[48rem]:w-full max-[48rem]:px-4">
                <section class="min-w-0" aria-labelledby="tmm15-h-news">
                  <h3 class="mb-2 border-b border-tmm15-line pb-1.5 font-tmm15-display text-[1.15rem]/tight" id="tmm15-h-news">News</h3>
                  <ul class="grid">
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-30 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Politics</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-75 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Economy</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-120 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Cities</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-165 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Climate</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-210 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Investigations</a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm15-h-culture">
                  <h3 class="mb-2 border-b border-tmm15-line pb-1.5 font-tmm15-display text-[1.15rem]/tight" id="tmm15-h-culture">Culture</h3>
                  <ul class="grid">
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-30 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Books</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-75 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Film</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-120 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Architecture</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-165 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Food</a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm15-h-opinion">
                  <h3 class="mb-2 border-b border-tmm15-line pb-1.5 font-tmm15-display text-[1.15rem]/tight" id="tmm15-h-opinion">Opinion</h3>
                  <ul class="grid">
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-30 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Columnists</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-75 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Letters</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-120 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">The long read</a></li>
                  </ul>
                </section>
                <article class="min-w-0 self-start">
                  <a class="group/f grid gap-1.5 text-inherit" href="#tmm15-title">
                    <span class="block overflow-clip rounded-sm bg-tmm15-line"><img class="aspect-[16/10] w-full scale-110 object-cover grayscale contrast-105 transition-[scale,filter] duration-700 ease-tmm15-out tmm15-open:scale-100 group-hover/f:scale-[1.03] group-hover/f:grayscale-0 motion-reduce:scale-100 motion-reduce:transition-none" src="https://picsum.photos/seed/meridian-harbour/640/400" alt="Cranes above a container terminal at dusk" width="640" height="400" loading="lazy" decoding="async"></span>
                    <p class="mt-1 text-[0.68rem]/none font-bold tracking-[0.2em] text-tmm15-acc uppercase">The long read</p>
                    <h3 class="font-tmm15-display text-[clamp(1.15rem,3vw,1.45rem)]/[1.15] tracking-[-0.01em] text-balance decoration-1 underline-offset-4 group-hover/f:underline">The port that rebuilt itself twice in a decade</h3>
                    <p class="text-[0.8rem]/none text-tmm15-mut">Priya Sharma &middot; 18 min read</p>
                  </a>
                </article>
              </div>
            </div>
          </li>
        <li data-tmm15-item class="flex items-stretch max-[48rem]:block">
            <button type="button" id="tmm15-trigger-more" aria-expanded="false" aria-controls="tmm15-panel-more" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 px-2.5 text-[0.8rem]/none font-medium tracking-[0.16em] text-tmm15-ink uppercase transition-[color,box-shadow] hover:text-tmm15-acc tmm15-open:text-tmm15-acc! tmm15-open:shadow-[inset_0_-2px_0_var(--color-tmm15-acc)]">More<svg class="size-3.5 transition-transform duration-200 tmm15-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm15-ink bg-tmm15-surf opacity-0 shadow-tmm15-panel pointer-events-none transition-[opacity,visibility] duration-170 tmm15-open:visible tmm15-open:opacity-100 tmm15-open:pointer-events-auto motion-reduce:transition-none max-[48rem]:static max-[48rem]:hidden max-[48rem]:visible max-[48rem]:opacity-100 max-[48rem]:shadow-none max-[48rem]:tmm15-open:block" id="tmm15-panel-more" aria-labelledby="tmm15-trigger-more">
              <div class="mx-auto grid w-[min(74rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,10rem),1fr))] gap-[clamp(1rem,3vw,2.5rem)] py-[clamp(1.1rem,3vw,2rem)] min-[64rem]:grid-cols-[repeat(3,minmax(0,1fr))_20rem] max-[48rem]:w-full max-[48rem]:px-4">
                <section class="min-w-0" aria-labelledby="tmm15-h-audio">
                  <h3 class="mb-2 border-b border-tmm15-line pb-1.5 font-tmm15-display text-[1.15rem]/tight" id="tmm15-h-audio">Audio</h3>
                  <ul class="grid">
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-30 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Daily briefing</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-75 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">The interview</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-120 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Archive tapes</a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm15-h-news2">
                  <h3 class="mb-2 border-b border-tmm15-line pb-1.5 font-tmm15-display text-[1.15rem]/tight" id="tmm15-h-news2">Newsletters</h3>
                  <ul class="grid">
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-30 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Morning edition</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-75 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Markets</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-120 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Weekend</a></li>
                  </ul>
                </section>
                <section class="min-w-0" aria-labelledby="tmm15-h-paper">
                  <h3 class="mb-2 border-b border-tmm15-line pb-1.5 font-tmm15-display text-[1.15rem]/tight" id="tmm15-h-paper">The paper</h3>
                  <ul class="grid">
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-30 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Today's front page</a></li>
                    <li class="[clip-path:inset(115%_0_-8px_0)] transition-[clip-path] duration-460 ease-tmm15-out delay-75 tmm15-open:[clip-path:inset(-8px)] motion-reduce:[clip-path:none] motion-reduce:transition-none"><a href="#tmm15-title" class="flex min-h-11 min-w-0 items-center border-b border-dotted border-tmm15-line text-[0.93rem] text-tmm15-ink transition-colors hover:text-tmm15-acc">Archive</a></li>
                  </ul>
                </section>
                <article class="min-w-0 self-start">
                  <a class="group/f grid gap-1.5 text-inherit" href="#tmm15-title">
                    <span class="block overflow-clip rounded-sm bg-tmm15-line"><img class="aspect-[16/10] w-full scale-110 object-cover grayscale contrast-105 transition-[scale,filter] duration-700 ease-tmm15-out tmm15-open:scale-100 group-hover/f:scale-[1.03] group-hover/f:grayscale-0 motion-reduce:scale-100 motion-reduce:transition-none" src="https://picsum.photos/seed/meridian-studio/640/400" alt="A recording studio desk lit by a single lamp" width="640" height="400" loading="lazy" decoding="async"></span>
                    <p class="mt-1 text-[0.68rem]/none font-bold tracking-[0.2em] text-tmm15-acc uppercase">New series</p>
                    <h3 class="font-tmm15-display text-[clamp(1.15rem,3vw,1.45rem)]/[1.15] tracking-[-0.01em] text-balance decoration-1 underline-offset-4 group-hover/f:underline">Six weeks inside the coastal defence review</h3>
                    <p class="text-[0.8rem]/none text-tmm15-mut">Jordan Lee &middot; 6 episodes</p>
                  </a>
                </article>
              </div>
            </div>
          </li>
        <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-2.5 text-[0.8rem]/none font-medium tracking-[0.16em] text-tmm15-ink uppercase hover:text-tmm15-acc " href="#tmm15-title">Newsletters</a></li>
        <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-2.5 text-[0.8rem]/none font-medium tracking-[0.16em] text-tmm15-ink uppercase hover:text-tmm15-acc " href="#tmm15-title">Podcasts</a></li>
        <li class="flex items-center"><a class="inline-flex min-h-10 items-center rounded-full bg-tmm15-acc px-4 text-[0.78rem]/none font-bold tracking-[0.14em] text-tmm15-on-acc uppercase hover:brightness-110" href="#tmm15-title">Subscribe</a></li>
      </ul>
    </nav>
  </header>

  <main class="mx-auto w-[min(74rem,calc(100%-2rem))] py-[clamp(2.5rem,8vw,4.5rem)]">
    <article class="grid max-w-[44rem] gap-2.5">
      <p class="text-[0.7rem]/none font-bold tracking-[0.2em] text-tmm15-acc uppercase">Economy</p>
      <h1 class="font-tmm15-display text-[clamp(1.8rem,5.5vw,3rem)]/[1.08] tracking-[-0.02em] text-balance">Freight volumes recover to pre-strike levels, but only on two corridors</h1>
      <p class="font-tmm15-display text-[clamp(1rem,2.4vw,1.2rem)]/normal text-tmm15-mut italic text-pretty">Operators report a fourteen per cent rebound since June, concentrated almost entirely on the eastern routes.</p>
      <p class="mt-1.5 text-[0.78rem]/none font-medium tracking-[0.08em] text-tmm15-mut uppercase">By Alex Chen &middot; 06:00</p>
    </article>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm15-bg: #f7f4ee;
  --color-tmm15-bg: oklch(0.967 0.01 85);
  --color-tmm15-surf: #fffdf9;
  --color-tmm15-surf: oklch(0.995 0.005 85);
  --color-tmm15-line: #ddd6c8;
  --color-tmm15-line: oklch(0.88 0.02 85);
  --color-tmm15-ink: #14110d;
  --color-tmm15-ink: oklch(0.18 0.01 70);
  --color-tmm15-mut: #655d51;
  --color-tmm15-mut: oklch(0.48 0.02 75);
  --color-tmm15-acc: #8c1c13;
  --color-tmm15-acc: oklch(0.41 0.16 30);
  --color-tmm15-on-acc: #ffffff;
  --color-tmm15-on-acc: oklch(1 0 0);
  --font-tmm15-display: 'Libre Caslon Text', Georgia, serif;
  --font-tmm15-sans: 'Libre Franklin', system-ui, sans-serif;
  --shadow-tmm15-panel: 0 24px 50px -36px rgb(20 17 13 / 0.45);
  --ease-tmm15-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm15-open: instead of a repeated selector list. */

@custom-variant tmm15-open {
  &:where([data-tmm15-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm15-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-15 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-15:has(#tmm15-theme:checked) {
  --color-tmm15-bg: #0e0d0b;
  --color-tmm15-bg: oklch(0.15 0.005 80);
  --color-tmm15-surf: #17150f;
  --color-tmm15-surf: oklch(0.19 0.01 85);
  --color-tmm15-line: #2e2a22;
  --color-tmm15-line: oklch(0.29 0.015 80);
  --color-tmm15-ink: #f4f0e6;
  --color-tmm15-ink: oklch(0.95 0.015 85);
  --color-tmm15-mut: #a79e8d;
  --color-tmm15-mut: oklch(0.71 0.025 80);
  --color-tmm15-acc: #e8836f;
  --color-tmm15-acc: oklch(0.74 0.13 32);
  --color-tmm15-on-acc: #1f0a06;
  --color-tmm15-on-acc: oklch(0.18 0.04 30);
}

@media (prefers-color-scheme: dark) {
  .tmm-15 {
    --color-tmm15-bg: #0e0d0b;
    --color-tmm15-bg: oklch(0.15 0.005 80);
    --color-tmm15-surf: #17150f;
    --color-tmm15-surf: oklch(0.19 0.01 85);
    --color-tmm15-line: #2e2a22;
    --color-tmm15-line: oklch(0.29 0.015 80);
    --color-tmm15-ink: #f4f0e6;
    --color-tmm15-ink: oklch(0.95 0.015 85);
    --color-tmm15-mut: #a79e8d;
    --color-tmm15-mut: oklch(0.71 0.025 80);
    --color-tmm15-acc: #e8836f;
    --color-tmm15-acc: oklch(0.74 0.13 32);
    --color-tmm15-on-acc: #1f0a06;
    --color-tmm15-on-acc: oklch(0.18 0.04 30);
  }

  .tmm-15:has(#tmm15-theme:checked) {
    --color-tmm15-bg: #f7f4ee;
    --color-tmm15-bg: oklch(0.967 0.01 85);
    --color-tmm15-surf: #fffdf9;
    --color-tmm15-surf: oklch(0.995 0.005 85);
    --color-tmm15-line: #ddd6c8;
    --color-tmm15-line: oklch(0.88 0.02 85);
    --color-tmm15-ink: #14110d;
    --color-tmm15-ink: oklch(0.18 0.01 70);
    --color-tmm15-mut: #655d51;
    --color-tmm15-mut: oklch(0.48 0.02 75);
    --color-tmm15-acc: #8c1c13;
    --color-tmm15-acc: oklch(0.41 0.16 30);
    --color-tmm15-on-acc: #ffffff;
    --color-tmm15-on-acc: oklch(1 0 0);
  }
}
```
