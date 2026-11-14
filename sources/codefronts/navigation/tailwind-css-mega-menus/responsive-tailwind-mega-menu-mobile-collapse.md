---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/responsive-tailwind-mega-menu-mobile-collapse/"
title: "Responsive Tailwind Mega Menu: How It Should Collapse on Mobile"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "One navigation, two forms, side by side: the desktop mega panel on the left (inside a browser frame that is its own @container, so it collapses when the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Mega Menu: How It Should Collapse on Mobile
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/responsive-tailwind-mega-menu-mobile-collapse/

One navigation, two forms, side by side: the desktop mega panel on the left (inside a browser frame that is its own @container, so it collapses when the frame narrows), and the phone drawer on the right, built from native <details name> so only one section opens at a time with no script. On phones the mega columns flatten to a short list of the five links people actually tap. Zero JavaScript.
## HTML
```html
<section class="tmm-14 relative w-full min-h-svh bg-tmm14-bg font-tmm14-sans leading-[1.55] text-tmm14-ink [&_:focus-visible]:rounded [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm14-acc" aria-labelledby="tmm14-title">
  <h2 class="sr-only" id="tmm14-title">Vale Health</h2>

  <div class="absolute top-3 right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm14-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-lg border border-tmm14-line bg-tmm14-surf text-tmm14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm14-acc" for="tmm14-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid min-h-svh items-start gap-[clamp(1.25rem,4vw,2.5rem)] px-[clamp(0.75rem,3vw,2.5rem)] pt-[clamp(3.75rem,8vw,5rem)] pb-[clamp(2rem,6vw,4rem)] min-[66rem]:grid-cols-[minmax(0,1fr)_21rem]">
    <div class="@container min-w-0 overflow-clip rounded-xl border border-tmm14-line bg-tmm14-surf shadow-tmm14-frame">
      <div class="flex h-8 items-center gap-1.5 border-b border-tmm14-line bg-tmm14-bg px-3" aria-hidden="true"><span class="size-2.5 rounded-full bg-tmm14-line"></span><span class="size-2.5 rounded-full bg-tmm14-line"></span><span class="size-2.5 rounded-full bg-tmm14-line"></span><span class="ml-2 truncate rounded bg-tmm14-surf px-2 py-0.5 font-tmm14-display text-[0.62rem] tracking-[0.06em] text-tmm14-mut">valehealth.co.uk</span></div>
      <header class="relative z-10">
        <div class="flex min-h-16 flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,1.75rem)] border-b border-tmm14-line px-4 @max-[40rem]:flex-col @max-[40rem]:py-2">
          <a class="inline-flex items-center gap-2 font-tmm14-display text-base/none font-bold tracking-[0.02em] text-tmm14-ink" href="#tmm14-title">
            <svg class="size-[22px] text-tmm14-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6Z" fill="currentColor"/></svg>
            Vale Health
          </a>
          <nav class="flex min-w-0" aria-label="Primary">
            <ul class="flex flex-wrap gap-0.5 @max-[40rem]:flex-col">
              <li data-tmm14-item class="flex items-stretch @max-[40rem]:block">
                <button type="button" aria-expanded="false" aria-controls="tmm14-panel-care" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 px-3.5 font-tmm14-display text-[0.8rem]/none font-semibold tracking-[0.14em] text-tmm14-ink uppercase transition-[color,box-shadow] hover:text-tmm14-acc tmm14-open:text-tmm14-acc! tmm14-open:shadow-[inset_0_-2px_0_var(--color-tmm14-acc)]">Care<svg class="size-3.5 transition-transform duration-200 tmm14-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
                <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm14-line bg-tmm14-surf opacity-0 shadow-tmm14-panel transition-[opacity,visibility] duration-160 tmm14-open:visible tmm14-open:opacity-100 motion-reduce:transition-none @max-[40rem]:static @max-[40rem]:hidden @max-[40rem]:visible @max-[40rem]:opacity-100 @max-[40rem]:shadow-none @max-[40rem]:[[data-open]>&]:block @max-[40rem]:[[data-tmm14-item]:focus-within>&]:block" id="tmm14-panel-care" aria-label="Care">
                  <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,10rem),1fr))] gap-[clamp(0.75rem,2.4vw,1.75rem)] px-4 py-[clamp(0.9rem,2.6vw,1.5rem)]">
                  <section class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm14-out delay-20 tmm14-open:translate-x-0 tmm14-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm14-h-gp">
                    <h3 class="mb-1 font-tmm14-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm14-mut uppercase" id="tmm14-h-gp">Everyday care</h3>
                    <ul class="grid gap-px">
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Book a GP</a></li>
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Repeat prescriptions</a></li>
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Vaccinations</a></li>
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Health checks</a></li>
                    </ul>
                  </section>
                  <section class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm14-out delay-85 tmm14-open:translate-x-0 tmm14-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm14-h-spec">
                    <h3 class="mb-1 font-tmm14-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm14-mut uppercase" id="tmm14-h-spec">Specialists</h3>
                    <ul class="grid gap-px">
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Dermatology</a></li>
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Physiotherapy</a></li>
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Cardiology</a></li>
                    </ul>
                  </section>
                  <section class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm14-out delay-150 tmm14-open:translate-x-0 tmm14-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm14-h-mind">
                    <h3 class="mb-1 font-tmm14-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm14-mut uppercase" id="tmm14-h-mind">Mental health</h3>
                    <ul class="grid gap-px">
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Talking therapies</a></li>
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Self-referral</a></li>
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Crisis support</a></li>
                    </ul>
                  </section>
                  <section class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm14-out delay-215 tmm14-open:translate-x-0 tmm14-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm14-h-urgent">
                    <h3 class="mb-1 font-tmm14-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm14-mut uppercase" id="tmm14-h-urgent">Urgent</h3>
                    <ul class="grid gap-px">
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Same-day clinic</a></li>
                      <li><a href="#tmm14-title" class="flex min-h-11 min-w-0 items-center text-[0.9rem] text-tmm14-ink transition-colors hover:text-tmm14-acc">Out of hours</a></li>
                    </ul>
                  </section>
                  </div>
                </div>
              </li>
              <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 font-tmm14-display text-[0.8rem]/none font-semibold tracking-[0.14em] text-tmm14-ink uppercase hover:text-tmm14-acc" href="#tmm14-title">Clinics</a></li>
              <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 font-tmm14-display text-[0.8rem]/none font-semibold tracking-[0.14em] text-tmm14-ink uppercase hover:text-tmm14-acc" href="#tmm14-title">Pricing</a></li>
              <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 font-tmm14-display text-[0.8rem]/none font-semibold tracking-[0.14em] text-tmm14-ink uppercase hover:text-tmm14-acc" href="#tmm14-title">About</a></li>
            </ul>
          </nav>
          <a class="ml-auto inline-flex min-h-10 items-center justify-center self-center rounded-md bg-tmm14-acc px-4 font-tmm14-display text-[0.76rem]/none font-semibold tracking-[0.12em] text-tmm14-on-acc uppercase hover:brightness-110 @max-[40rem]:ml-0 @max-[40rem]:self-stretch" href="#tmm14-title">Book an appointment</a>
        </div>
      </header>
      <div class="grid gap-2 px-4 pt-[clamp(1.5rem,5vw,3rem)] pb-[clamp(2rem,6vw,3.5rem)]">
        <p class="font-tmm14-display text-[0.7rem]/none font-semibold tracking-[0.24em] text-tmm14-acc uppercase">42 clinics &middot; same-day appointments</p>
        <h1 class="max-w-[22ch] font-tmm14-display text-[clamp(1.6rem,4.5vw,2.6rem)]/[1.08] font-bold tracking-[-0.02em] text-balance">Care that fits around the rest of your life.</h1>
        <p class="max-w-[40ch] text-[0.95rem] text-tmm14-mut text-pretty">Evening and weekend slots at every clinic. Most people are seen within 48 hours.</p>
      </div>
    </div>

    <div class="w-[min(21rem,100%)] justify-self-center overflow-hidden rounded-[28px] border border-tmm14-line bg-tmm14-surf shadow-tmm14-frame ring-6 ring-tmm14-ink/5">
      <div class="flex min-h-14 items-center justify-between gap-4 border-b border-tmm14-line px-4">
        <span class="inline-flex items-center gap-2 font-tmm14-display text-[0.92rem]/none font-bold"><svg class="size-[18px] text-tmm14-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6Z" fill="currentColor"/></svg>Vale Health</span>
        <span class="-mr-2.5 grid size-11 place-items-center text-tmm14-mut" aria-hidden="true"><svg class="size-5" viewBox="0 0 24 24" focusable="false"><path d="m6 6 12 12M18 6 6 18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
      </div>
      <nav class="grid" aria-label="Vale Health mobile">
          <details class="group/acc border-b border-tmm14-line" name="tmm14-acc" open>
            <summary class="flex min-h-12 cursor-pointer list-none items-center justify-between gap-3 px-4 text-[0.95rem]/none font-semibold transition-colors group-open/acc:text-tmm14-acc [&::-webkit-details-marker]:hidden">Care
              <svg class="size-[18px] text-tmm14-mut transition-transform duration-200 group-open/acc:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </summary>
            <ul class="grid pb-2">
              <li><a href="#tmm14-title" class="flex min-h-11 items-center gap-2.5 px-6 text-[0.9rem] text-tmm14-mut transition-colors hover:bg-tmm14-acc/8 hover:text-tmm14-acc"><span aria-hidden="true" class="h-px w-2 bg-current opacity-50"></span>Book a GP</a></li>
              <li><a href="#tmm14-title" class="flex min-h-11 items-center gap-2.5 px-6 text-[0.9rem] text-tmm14-mut transition-colors hover:bg-tmm14-acc/8 hover:text-tmm14-acc"><span aria-hidden="true" class="h-px w-2 bg-current opacity-50"></span>Repeat prescriptions</a></li>
              <li><a href="#tmm14-title" class="flex min-h-11 items-center gap-2.5 px-6 text-[0.9rem] text-tmm14-mut transition-colors hover:bg-tmm14-acc/8 hover:text-tmm14-acc"><span aria-hidden="true" class="h-px w-2 bg-current opacity-50"></span>Specialists</a></li>
              <li><a href="#tmm14-title" class="flex min-h-11 items-center gap-2.5 px-6 text-[0.9rem] text-tmm14-mut transition-colors hover:bg-tmm14-acc/8 hover:text-tmm14-acc"><span aria-hidden="true" class="h-px w-2 bg-current opacity-50"></span>Mental health</a></li>
              <li><a href="#tmm14-title" class="flex min-h-11 items-center gap-2.5 px-6 text-[0.9rem] text-tmm14-mut transition-colors hover:bg-tmm14-acc/8 hover:text-tmm14-acc"><span aria-hidden="true" class="h-px w-2 bg-current opacity-50"></span>Same-day clinic</a></li>
            </ul>
          </details>
          <details class="group/acc border-b border-tmm14-line" name="tmm14-acc">
            <summary class="flex min-h-12 cursor-pointer list-none items-center justify-between gap-3 px-4 text-[0.95rem]/none font-semibold transition-colors group-open/acc:text-tmm14-acc [&::-webkit-details-marker]:hidden">Clinics
              <svg class="size-[18px] text-tmm14-mut transition-transform duration-200 group-open/acc:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </summary>
            <ul class="grid pb-2">
              <li><a href="#tmm14-title" class="flex min-h-11 items-center gap-2.5 px-6 text-[0.9rem] text-tmm14-mut transition-colors hover:bg-tmm14-acc/8 hover:text-tmm14-acc"><span aria-hidden="true" class="h-px w-2 bg-current opacity-50"></span>Find a clinic</a></li>
              <li><a href="#tmm14-title" class="flex min-h-11 items-center gap-2.5 px-6 text-[0.9rem] text-tmm14-mut transition-colors hover:bg-tmm14-acc/8 hover:text-tmm14-acc"><span aria-hidden="true" class="h-px w-2 bg-current opacity-50"></span>Opening hours</a></li>
            </ul>
          </details>
          <a class="flex min-h-12 items-center border-b border-tmm14-line px-4 text-[0.95rem]/none font-semibold text-tmm14-ink hover:text-tmm14-acc" href="#tmm14-title">Pricing</a>
          <a class="flex min-h-12 items-center border-b border-tmm14-line px-4 text-[0.95rem]/none font-semibold text-tmm14-ink hover:text-tmm14-acc" href="#tmm14-title">About</a>
          <a class="mx-4 mt-3.5 mb-2 grid min-h-13 place-items-center rounded-md bg-tmm14-acc font-tmm14-display text-[0.8rem]/none font-semibold tracking-[0.12em] text-tmm14-on-acc uppercase hover:brightness-110" href="#tmm14-title">Book an appointment</a>
          <a class="mx-4 mb-4 grid min-h-11 place-items-center text-[0.85rem] font-semibold text-tmm14-acc" href="#tmm14-title">Call 0300 123 4567</a>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm14-bg: #f7f5f1;
  --color-tmm14-bg: oklch(0.97 0.006 80);
  --color-tmm14-surf: #ffffff;
  --color-tmm14-surf: oklch(1 0 0);
  --color-tmm14-line: #e2ded6;
  --color-tmm14-line: oklch(0.9 0.01 80);
  --color-tmm14-ink: #1a1917;
  --color-tmm14-ink: oklch(0.21 0.005 80);
  --color-tmm14-mut: #65615b;
  --color-tmm14-mut: oklch(0.48 0.01 75);
  --color-tmm14-acc: #0f6d8c;
  --color-tmm14-acc: oklch(0.48 0.11 220);
  --color-tmm14-on-acc: #ffffff;
  --color-tmm14-on-acc: oklch(1 0 0);
  --font-tmm14-display: 'Hanken Grotesk', system-ui, sans-serif;
  --font-tmm14-sans: 'Hanken Grotesk', system-ui, sans-serif;
  --shadow-tmm14-panel: 0 24px 50px -34px rgb(26 25 23 / 0.5);
  --shadow-tmm14-frame: 0 30px 70px -40px rgb(26 25 23 / 0.6);
  --ease-tmm14-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm14-open: instead of a repeated selector list. */

@custom-variant tmm14-open {
  &:where([data-tmm14-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm14-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-14 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-14:has(#tmm14-theme:checked) {
  --color-tmm14-bg: #0f0f0e;
  --color-tmm14-bg: oklch(0.16 0.003 80);
  --color-tmm14-surf: #191817;
  --color-tmm14-surf: oklch(0.21 0.004 80);
  --color-tmm14-line: #2c2a27;
  --color-tmm14-line: oklch(0.29 0.006 80);
  --color-tmm14-ink: #f3f1ed;
  --color-tmm14-ink: oklch(0.96 0.005 80);
  --color-tmm14-mut: #a5a09a;
  --color-tmm14-mut: oklch(0.71 0.01 75);
  --color-tmm14-acc: #5ec8e8;
  --color-tmm14-acc: oklch(0.8 0.11 220);
  --color-tmm14-on-acc: #04212b;
  --color-tmm14-on-acc: oklch(0.22 0.04 220);
}

@media (prefers-color-scheme: dark) {
  .tmm-14 {
    --color-tmm14-bg: #0f0f0e;
    --color-tmm14-bg: oklch(0.16 0.003 80);
    --color-tmm14-surf: #191817;
    --color-tmm14-surf: oklch(0.21 0.004 80);
    --color-tmm14-line: #2c2a27;
    --color-tmm14-line: oklch(0.29 0.006 80);
    --color-tmm14-ink: #f3f1ed;
    --color-tmm14-ink: oklch(0.96 0.005 80);
    --color-tmm14-mut: #a5a09a;
    --color-tmm14-mut: oklch(0.71 0.01 75);
    --color-tmm14-acc: #5ec8e8;
    --color-tmm14-acc: oklch(0.8 0.11 220);
    --color-tmm14-on-acc: #04212b;
    --color-tmm14-on-acc: oklch(0.22 0.04 220);
  }

  .tmm-14:has(#tmm14-theme:checked) {
    --color-tmm14-bg: #f7f5f1;
    --color-tmm14-bg: oklch(0.97 0.006 80);
    --color-tmm14-surf: #ffffff;
    --color-tmm14-surf: oklch(1 0 0);
    --color-tmm14-line: #e2ded6;
    --color-tmm14-line: oklch(0.9 0.01 80);
    --color-tmm14-ink: #1a1917;
    --color-tmm14-ink: oklch(0.21 0.005 80);
    --color-tmm14-mut: #65615b;
    --color-tmm14-mut: oklch(0.48 0.01 75);
    --color-tmm14-acc: #0f6d8c;
    --color-tmm14-acc: oklch(0.48 0.11 220);
    --color-tmm14-on-acc: #ffffff;
    --color-tmm14-on-acc: oklch(1 0 0);
  }
}
/* What stayed CSS: ::details-content has no variant here, and interpolate-size is inherited. */

.tmm-14 {
  interpolate-size: allow-keywords;
}

.tmm-14 details::details-content {
  block-size: 0;
  overflow: clip;
  transition: block-size 260ms cubic-bezier(0.22, 1, 0.36, 1), content-visibility 260ms allow-discrete;
}

.tmm-14 details[open]::details-content {
  block-size: auto;
}

@media (prefers-reduced-motion: reduce) {
  .tmm-14 details::details-content {
    transition: none;
  }
}
```
