---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/screen-reader-friendly-tailwind-mega-menu/"
title: "Screen Reader Friendly Tailwind Mega Menu with Panel Summaries"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "What does a screen-reader user hear when they reach a mega menu?"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Screen Reader Friendly Tailwind Mega Menu with Panel Summaries
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/screen-reader-friendly-tailwind-mega-menu/

What does a screen-reader user hear when they reach a mega menu? Here: "Study, button, collapsed, 14 links in 4 groups". Each trigger is described by an sr-only summary via aria-describedby, each panel is named by its trigger, and every column is a labelled <section> so heading and landmark navigation work inside it. A university header whose panel resolves out of a blur. Zero JavaScript.
## HTML
```html
<section class="tmm-11 relative w-full min-h-svh bg-tmm11-bg font-tmm11-sans leading-[1.55] text-tmm11-ink [&_:focus-visible]:rounded-md [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm11-acc" aria-labelledby="tmm11-title">
  <h2 class="sr-only" id="tmm11-title">Vale University</h2>

  <div class="absolute top-[49px] right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm11-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-lg border border-tmm11-line bg-tmm11-surf text-tmm11-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm11-acc" for="tmm11-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b border-tmm11-line bg-tmm11-surf">
    <div class="mx-auto flex min-h-9 w-[min(78rem,calc(100%-2rem))] flex-wrap items-center gap-x-4.5 border-b border-tmm11-line text-[0.76rem]/none font-medium text-tmm11-mut">
      <span>Est. 1874</span>
      <a class="ml-auto inline-flex min-h-9 items-center hover:text-tmm11-acc" href="#tmm11-title">Staff and students</a>
      <a class="inline-flex min-h-9 items-center hover:text-tmm11-acc" href="#tmm11-title">Library</a>
      <a class="inline-flex min-h-9 items-center hover:text-tmm11-acc" href="#tmm11-title">Give</a>
    </div>
    <div class="mx-auto flex min-h-18 w-[min(78rem,calc(100%-2rem))] flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,2rem)] pr-15 max-[54rem]:flex-col max-[54rem]:py-2.5">
      <a class="inline-flex items-center gap-2.5 text-tmm11-ink" href="#tmm11-title">
        <svg class="size-7 text-tmm11-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 9 12 4l8 5v2H4Zm2 3h2v6H6Zm5 0h2v6h-2Zm5 0h2v6h-2ZM3 20h18" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
        <span class="grid font-tmm11-display text-[1.2rem]/none">Vale<b class="font-tmm11-sans text-[0.68rem]/[1.5] font-semibold tracking-[0.24em] text-tmm11-mut uppercase">University</b></span>
      </a>
      <nav class="flex min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-1 max-[54rem]:flex-col">
          <li data-tmm11-item class="flex items-stretch max-[54rem]:block">
            <button type="button" id="tmm11-trigger-study" aria-expanded="false" aria-controls="tmm11-panel-study" aria-describedby="tmm11-sum-study" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 self-center rounded-lg px-3.5 font-tmm11-display text-[1.02rem]/none text-tmm11-ink transition-colors hover:text-tmm11-acc tmm11-open:bg-tmm11-acc/12 tmm11-open:text-tmm11-acc!">Study<svg class="size-3.5 opacity-70 transition-transform duration-200 tmm11-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm11-line bg-tmm11-surf opacity-0 shadow-tmm11-panel pointer-events-none transition-[opacity,visibility] duration-170 tmm11-open:visible tmm11-open:opacity-100 tmm11-open:pointer-events-auto motion-reduce:transition-none max-[54rem]:static max-[54rem]:hidden max-[54rem]:visible max-[54rem]:opacity-100 max-[54rem]:shadow-none max-[54rem]:tmm11-open:block" id="tmm11-panel-study" aria-labelledby="tmm11-trigger-study">
              <p class="sr-only" id="tmm11-sum-study">14 links in 4 groups.</p>
              <div class="mx-auto grid w-[min(78rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-[clamp(0.75rem,2.4vw,2rem)] py-[clamp(1.1rem,3vw,1.9rem)] opacity-0 blur-sm transition-[filter,opacity] duration-[340ms,260ms] tmm11-open:opacity-100 tmm11-open:blur-none motion-reduce:opacity-100 motion-reduce:blur-none motion-reduce:transition-none max-[54rem]:w-full max-[54rem]:px-4">
                <section class="min-w-0 opacity-0 transition-opacity duration-320 delay-60 tmm11-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm11-h-ug">
                  <h3 class="mb-2 border-b border-tmm11-line pb-2 font-tmm11-display text-[1.02rem]/tight" id="tmm11-h-ug">Undergraduate</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Courses A&ndash;Z</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Entry requirements</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Foundation year</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Open days</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Fees and funding</a></li>
                  </ul>
                </section>
                <section class="min-w-0 opacity-0 transition-opacity duration-320 delay-120 tmm11-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm11-h-pg">
                  <h3 class="mb-2 border-b border-tmm11-line pb-2 font-tmm11-display text-[1.02rem]/tight" id="tmm11-h-pg">Postgraduate</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Taught masters</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Research degrees</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Doctoral college</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Scholarships</a></li>
                  </ul>
                </section>
                <section class="min-w-0 opacity-0 transition-opacity duration-320 delay-180 tmm11-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm11-h-life">
                  <h3 class="mb-2 border-b border-tmm11-line pb-2 font-tmm11-display text-[1.02rem]/tight" id="tmm11-h-life">Student life</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Accommodation</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Campus map</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Wellbeing</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Clubs and societies</a></li>
                  </ul>
                </section>
                <aside class="min-w-0 opacity-0 transition-opacity duration-320 delay-240 tmm11-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-1.5 rounded-xl bg-tmm11-deep p-4.5 text-tmm11-on-deep" aria-labelledby="tmm11-h-start">
                  <h3 class="font-tmm11-display text-[1.1rem]/tight" id="tmm11-h-start">Applying for 2027</h3>
                  <p class="text-[0.87rem] text-tmm11-on-deep/80 text-pretty">Applications open on 1 October. Book a campus tour before you decide.</p>
                  <a class="mt-1 inline-flex min-h-11 w-fit items-center gap-2 rounded-lg bg-tmm11-on-deep px-3.5 text-[0.86rem]/none font-semibold text-tmm11-deep transition-transform hover:-translate-y-px" href="#tmm11-title">Book an open day <span aria-hidden="true">&rarr;</span></a>
                </aside>
              </div>
            </div>
          </li>
          <li data-tmm11-item class="flex items-stretch max-[54rem]:block">
            <button type="button" id="tmm11-trigger-research" aria-expanded="false" aria-controls="tmm11-panel-research" aria-describedby="tmm11-sum-research" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 self-center rounded-lg px-3.5 font-tmm11-display text-[1.02rem]/none text-tmm11-ink transition-colors hover:text-tmm11-acc tmm11-open:bg-tmm11-acc/12 tmm11-open:text-tmm11-acc!">Research<svg class="size-3.5 opacity-70 transition-transform duration-200 tmm11-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm11-line bg-tmm11-surf opacity-0 shadow-tmm11-panel pointer-events-none transition-[opacity,visibility] duration-170 tmm11-open:visible tmm11-open:opacity-100 tmm11-open:pointer-events-auto motion-reduce:transition-none max-[54rem]:static max-[54rem]:hidden max-[54rem]:visible max-[54rem]:opacity-100 max-[54rem]:shadow-none max-[54rem]:tmm11-open:block" id="tmm11-panel-research" aria-labelledby="tmm11-trigger-research">
              <p class="sr-only" id="tmm11-sum-research">9 links in 4 groups.</p>
              <div class="mx-auto grid w-[min(78rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-[clamp(0.75rem,2.4vw,2rem)] py-[clamp(1.1rem,3vw,1.9rem)] opacity-0 blur-sm transition-[filter,opacity] duration-[340ms,260ms] tmm11-open:opacity-100 tmm11-open:blur-none motion-reduce:opacity-100 motion-reduce:blur-none motion-reduce:transition-none max-[54rem]:w-full max-[54rem]:px-4">
                <section class="min-w-0 opacity-0 transition-opacity duration-320 delay-60 tmm11-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm11-h-inst">
                  <h3 class="mb-2 border-b border-tmm11-line pb-2 font-tmm11-display text-[1.02rem]/tight" id="tmm11-h-inst">Institutes</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Climate and coasts</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Population health</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Computation</a></li>
                  </ul>
                </section>
                <section class="min-w-0 opacity-0 transition-opacity duration-320 delay-120 tmm11-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm11-h-work">
                  <h3 class="mb-2 border-b border-tmm11-line pb-2 font-tmm11-display text-[1.02rem]/tight" id="tmm11-h-work">Work with us</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Industry partnerships</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Consultancy</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Facilities hire</a></li>
                  </ul>
                </section>
                <section class="min-w-0 opacity-0 transition-opacity duration-320 delay-180 tmm11-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm11-h-out">
                  <h3 class="mb-2 border-b border-tmm11-line pb-2 font-tmm11-display text-[1.02rem]/tight" id="tmm11-h-out">Outputs</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Publications</a></li>
                    <li><a href="#tmm11-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-md px-2 text-[0.9rem] text-tmm11-mut transition-colors hover:bg-tmm11-acc/9 hover:text-tmm11-acc">Open data</a></li>
                  </ul>
                </section>
                <aside class="min-w-0 opacity-0 transition-opacity duration-320 delay-240 tmm11-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-1.5 rounded-xl bg-tmm11-deep p-4.5 text-tmm11-on-deep" aria-labelledby="tmm11-h-fund">
                  <h3 class="font-tmm11-display text-[1.1rem]/tight" id="tmm11-h-fund">Funding calls</h3>
                  <p class="text-[0.87rem] text-tmm11-on-deep/80 text-pretty">Six internal schemes close this term.</p>
                  <a class="mt-1 inline-flex min-h-11 w-fit items-center gap-2 rounded-lg bg-tmm11-on-deep px-3.5 text-[0.86rem]/none font-semibold text-tmm11-deep transition-transform hover:-translate-y-px" href="#tmm11-title">See all calls <span aria-hidden="true">&rarr;</span></a>
                </aside>
              </div>
            </div>
          </li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center self-center rounded-lg px-3.5 font-tmm11-display text-[1.02rem]/none text-tmm11-ink hover:text-tmm11-acc" href="#tmm11-title">About</a></li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center self-center rounded-lg px-3.5 font-tmm11-display text-[1.02rem]/none text-tmm11-ink hover:text-tmm11-acc" href="#tmm11-title">News</a></li>
        </ul>
      </nav>
      <a class="ml-auto inline-flex min-h-11 items-center justify-center self-center rounded-lg bg-tmm11-acc px-5 font-tmm11-display text-[0.95rem]/none tracking-[0.04em] text-tmm11-on-acc hover:brightness-110 max-[54rem]:ml-0 max-[54rem]:self-stretch" href="#tmm11-title">Apply</a>
    </div>
  </header>

  <main class="mx-auto w-[min(78rem,calc(100%-2rem))] py-[clamp(3rem,9vw,5.5rem)]">
    <div class="grid max-w-[40rem] gap-2.5">
      <p class="inline-flex w-fit items-center gap-2 text-[0.7rem]/none font-bold tracking-[0.22em] text-tmm11-acc uppercase"><span aria-hidden="true" class="relative size-2 rounded-full bg-tmm11-live before:absolute before:inset-0 before:animate-ping before:rounded-full before:bg-tmm11-live motion-reduce:before:hidden"></span>Clearing 2026</p>
      <h1 class="font-tmm11-display text-[clamp(2rem,6vw,3.5rem)]/[1.06] tracking-[-0.01em] text-balance">Places still available on 41 courses.</h1>
      <p class="text-[clamp(0.95rem,2.3vw,1.1rem)] text-tmm11-mut text-pretty">Speak to an adviser today. Lines are open until 8pm.</p>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm11-bg: #eef0fa;
  --color-tmm11-bg: oklch(0.955 0.014 277);
  --color-tmm11-surf: #ffffff;
  --color-tmm11-surf: oklch(1 0 0);
  --color-tmm11-deep: #1e1b4b;
  --color-tmm11-deep: oklch(0.26 0.09 279);
  --color-tmm11-on-deep: #f3f2ff;
  --color-tmm11-on-deep: oklch(0.97 0.015 280);
  --color-tmm11-line: #d4d7ee;
  --color-tmm11-line: oklch(0.88 0.03 277);
  --color-tmm11-ink: #171638;
  --color-tmm11-ink: oklch(0.22 0.06 280);
  --color-tmm11-mut: #55577f;
  --color-tmm11-mut: oklch(0.47 0.06 278);
  --color-tmm11-acc: #4338ca;
  --color-tmm11-acc: oklch(0.45 0.21 277);
  --color-tmm11-on-acc: #ffffff;
  --color-tmm11-on-acc: oklch(1 0 0);
  --color-tmm11-live: #16a34a;
  --color-tmm11-live: oklch(0.63 0.17 150);
  --font-tmm11-display: 'Marcellus', Optima, 'Gill Sans', serif;
  --font-tmm11-sans: 'Public Sans', system-ui, sans-serif;
  --shadow-tmm11-panel: 0 30px 60px -34px rgb(23 22 56 / 0.55);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm11-open: instead of a repeated selector list. */

@custom-variant tmm11-open {
  &:where([data-tmm11-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm11-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-11 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-11:has(#tmm11-theme:checked) {
  --color-tmm11-bg: #08081a;
  --color-tmm11-bg: oklch(0.14 0.03 280);
  --color-tmm11-surf: #121233;
  --color-tmm11-surf: oklch(0.2 0.06 280);
  --color-tmm11-deep: #2b2a6e;
  --color-tmm11-deep: oklch(0.33 0.11 280);
  --color-tmm11-on-deep: #f3f2ff;
  --color-tmm11-on-deep: oklch(0.97 0.015 280);
  --color-tmm11-line: #262657;
  --color-tmm11-line: oklch(0.3 0.08 280);
  --color-tmm11-ink: #eceafd;
  --color-tmm11-ink: oklch(0.94 0.02 285);
  --color-tmm11-mut: #a2a3cd;
  --color-tmm11-mut: oklch(0.74 0.05 280);
  --color-tmm11-acc: #a5b4fc;
  --color-tmm11-acc: oklch(0.78 0.11 277);
  --color-tmm11-on-acc: #14123a;
  --color-tmm11-on-acc: oklch(0.2 0.07 280);
  --color-tmm11-live: #4ade80;
  --color-tmm11-live: oklch(0.8 0.18 150);
}

@media (prefers-color-scheme: dark) {
  .tmm-11 {
    --color-tmm11-bg: #08081a;
    --color-tmm11-bg: oklch(0.14 0.03 280);
    --color-tmm11-surf: #121233;
    --color-tmm11-surf: oklch(0.2 0.06 280);
    --color-tmm11-deep: #2b2a6e;
    --color-tmm11-deep: oklch(0.33 0.11 280);
    --color-tmm11-on-deep: #f3f2ff;
    --color-tmm11-on-deep: oklch(0.97 0.015 280);
    --color-tmm11-line: #262657;
    --color-tmm11-line: oklch(0.3 0.08 280);
    --color-tmm11-ink: #eceafd;
    --color-tmm11-ink: oklch(0.94 0.02 285);
    --color-tmm11-mut: #a2a3cd;
    --color-tmm11-mut: oklch(0.74 0.05 280);
    --color-tmm11-acc: #a5b4fc;
    --color-tmm11-acc: oklch(0.78 0.11 277);
    --color-tmm11-on-acc: #14123a;
    --color-tmm11-on-acc: oklch(0.2 0.07 280);
    --color-tmm11-live: #4ade80;
    --color-tmm11-live: oklch(0.8 0.18 150);
  }

  .tmm-11:has(#tmm11-theme:checked) {
    --color-tmm11-bg: #eef0fa;
    --color-tmm11-bg: oklch(0.955 0.014 277);
    --color-tmm11-surf: #ffffff;
    --color-tmm11-surf: oklch(1 0 0);
    --color-tmm11-deep: #1e1b4b;
    --color-tmm11-deep: oklch(0.26 0.09 279);
    --color-tmm11-on-deep: #f3f2ff;
    --color-tmm11-on-deep: oklch(0.97 0.015 280);
    --color-tmm11-line: #d4d7ee;
    --color-tmm11-line: oklch(0.88 0.03 277);
    --color-tmm11-ink: #171638;
    --color-tmm11-ink: oklch(0.22 0.06 280);
    --color-tmm11-mut: #55577f;
    --color-tmm11-mut: oklch(0.47 0.06 278);
    --color-tmm11-acc: #4338ca;
    --color-tmm11-acc: oklch(0.45 0.21 277);
    --color-tmm11-on-acc: #ffffff;
    --color-tmm11-on-acc: oklch(1 0 0);
    --color-tmm11-live: #16a34a;
    --color-tmm11-live: oklch(0.63 0.17 150);
  }
}
```
