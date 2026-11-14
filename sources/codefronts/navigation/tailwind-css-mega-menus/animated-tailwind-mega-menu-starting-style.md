---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/animated-tailwind-mega-menu-starting-style/"
title: "Animated Tailwind Mega Menu with @starting-style and display Transitions"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "The panel is genuinely display: none while closed &mdash; not just invisible &mdash; and still fades and slides in and out."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Tailwind Mega Menu with @starting-style and display Transitions
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/animated-tailwind-mega-menu-starting-style/

The panel is genuinely display: none while closed &mdash; not just invisible &mdash; and still fades and slides in and out. Tailwind v4 makes the new CSS a class list: transition-discrete lets display transition, and starting:tmm13-open:opacity-0 declares where the entry animation begins. A brutalist coffee-subscription header with hard offset shadows and links that snap in on a steps() clock. Zero JavaScript.
## HTML
```html
<section class="tmm-13 relative flow-root w-full min-h-svh bg-tmm13-bg font-tmm13-sans leading-[1.55] text-tmm13-ink [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm13-acc" aria-labelledby="tmm13-title">
  <h2 class="sr-only" id="tmm13-title">Sable Coffee Roasters</h2>

  <header class="relative z-10 mx-auto mt-[clamp(1rem,3vw,1.75rem)] w-[min(72rem,calc(100%-2rem))]">
    <div class="absolute top-[9px] right-2.5 z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm13-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-none border-2 border-tmm13-line bg-tmm13-surf text-tmm13-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm13-acc" for="tmm13-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>
    <div class="flex min-h-[62px] flex-wrap items-center gap-[clamp(0.5rem,2vw,1.75rem)] border-2 border-tmm13-line bg-tmm13-surf pr-16 pl-3.5 shadow-[6px_6px_0_var(--color-tmm13-line)] max-[52rem]:flex-col max-[52rem]:items-stretch max-[52rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm13-display text-[1.2rem]/none font-semibold tracking-[0.14em] text-tmm13-ink uppercase" href="#tmm13-title">
        <svg class="size-[22px] text-tmm13-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><ellipse cx="12" cy="12" rx="6.5" ry="9" fill="currentColor"/><path d="M12 3.5c-2 3-2 5.5 0 8.5s2 5.5 0 8.5" fill="none" stroke="var(--color-tmm13-surf)" stroke-width="1.5"/></svg>
        Sable
      </a>
      <nav class="min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-1 max-[52rem]:flex-col">
          <li data-tmm13-item class="max-[52rem]:block">
            <button type="button" aria-expanded="false" aria-controls="tmm13-panel-coffee" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm13-open:after:pointer-events-auto max-[52rem]:after:hidden inline-flex min-h-11 cursor-pointer items-center px-3.5 font-tmm13-display text-[0.92rem]/none font-medium tracking-[0.1em] text-tmm13-ink uppercase transition-colors hover:text-tmm13-acc tmm13-open:bg-tmm13-ink tmm13-open:text-tmm13-surf!">Coffee</button>
            <div class="absolute inset-x-0 top-full z-30 mt-3 hidden -translate-y-2 grid-cols-2 border-2 border-tmm13-line bg-tmm13-surf opacity-0 shadow-[6px_6px_0_var(--color-tmm13-line)] transition-[opacity,translate,display] transition-discrete duration-260 before:absolute before:inset-x-0 before:-top-3.5 before:h-3 tmm13-open:grid tmm13-open:translate-y-0 tmm13-open:opacity-100 tmm13-open:duration-200 starting:tmm13-open:-translate-y-2 starting:tmm13-open:opacity-0 motion-reduce:transition-none max-[52rem]:static max-[52rem]:mt-2.5 max-[52rem]:grid-cols-1 max-[52rem]:translate-y-0 max-[52rem]:opacity-100" id="tmm13-panel-coffee" aria-label="Coffee">
              <div class="min-w-0 p-[clamp(0.9rem,2.4vw,1.35rem)] ">
                <h3 class="mb-2 font-tmm13-display text-[0.76rem]/none font-semibold tracking-[0.18em] text-tmm13-mut uppercase">Single origin</h3>
                <ul class="grid gap-px">
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-30 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Yirgacheffe<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Jasmine, bergamot</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-85 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Huila<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Red apple, cane sugar</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-140 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Antigua<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Cocoa, orange peel</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-195 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Kirinyaga<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Blackcurrant</span></a></li>
                </ul>
              </div>
              <div class="min-w-0 p-[clamp(0.9rem,2.4vw,1.35rem)] bg-tmm13-soft">
                <h3 class="mb-2 font-tmm13-display text-[0.76rem]/none font-semibold tracking-[0.18em] text-tmm13-mut uppercase">Blends and gear</h3>
                <ul class="grid gap-px">
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-30 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Morning house<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Everyday filter</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-85 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Espresso No.4<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">For milk drinks</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-140 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Decaf Vale<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Sugarcane process</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-195 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Brewers and grinders<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Kit and spares</span></a></li>
                </ul>
              </div>
            </div>
          </li>
          <li data-tmm13-item class="max-[52rem]:block">
            <button type="button" aria-expanded="false" aria-controls="tmm13-panel-plans" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm13-open:after:pointer-events-auto max-[52rem]:after:hidden inline-flex min-h-11 cursor-pointer items-center px-3.5 font-tmm13-display text-[0.92rem]/none font-medium tracking-[0.1em] text-tmm13-ink uppercase transition-colors hover:text-tmm13-acc tmm13-open:bg-tmm13-ink tmm13-open:text-tmm13-surf!">Subscribe</button>
            <div class="absolute inset-x-0 top-full z-30 mt-3 hidden -translate-y-2 grid-cols-2 border-2 border-tmm13-line bg-tmm13-surf opacity-0 shadow-[6px_6px_0_var(--color-tmm13-line)] transition-[opacity,translate,display] transition-discrete duration-260 before:absolute before:inset-x-0 before:-top-3.5 before:h-3 tmm13-open:grid tmm13-open:translate-y-0 tmm13-open:opacity-100 tmm13-open:duration-200 starting:tmm13-open:-translate-y-2 starting:tmm13-open:opacity-0 motion-reduce:transition-none max-[52rem]:static max-[52rem]:mt-2.5 max-[52rem]:grid-cols-1 max-[52rem]:translate-y-0 max-[52rem]:opacity-100" id="tmm13-panel-plans" aria-label="Subscribe">
              <div class="min-w-0 p-[clamp(0.9rem,2.4vw,1.35rem)] ">
                <h3 class="mb-2 font-tmm13-display text-[0.76rem]/none font-semibold tracking-[0.18em] text-tmm13-mut uppercase">Plans</h3>
                <ul class="grid gap-px">
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-30 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Weekly<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">250g, every Monday</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-85 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Fortnightly<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">500g</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-140 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Roaster's choice<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">We pick, you brew</span></a></li>
                </ul>
              </div>
              <div class="min-w-0 p-[clamp(0.9rem,2.4vw,1.35rem)] bg-tmm13-soft">
                <h3 class="mb-2 font-tmm13-display text-[0.76rem]/none font-semibold tracking-[0.18em] text-tmm13-mut uppercase">Manage</h3>
                <ul class="grid gap-px">
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-30 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Pause or skip<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Any time</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-85 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Change grind<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">Before dispatch</span></a></li>
                  <li class="-translate-x-2.5 opacity-0 transition-[opacity,translate] duration-[1ms,180ms] ease-[steps(1,end),steps(3,end)] delay-140 tmm13-open:translate-x-0 tmm13-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm13-title" class="group/l grid min-h-12 min-w-0 content-center gap-px text-tmm13-ink"><b class="flex items-center gap-2 text-[0.95rem]/tight font-semibold decoration-2 underline-offset-4 group-hover/l:text-tmm13-acc group-hover/l:underline">Gift a subscription<span aria-hidden="true" class="-translate-x-1 font-normal opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></b><span class="text-[0.8rem] text-tmm13-mut">3, 6 or 12 months</span></a></li>
                </ul>
              </div>
            </div>
          </li>
          <li><a class="inline-flex min-h-11 items-center px-3.5 font-tmm13-display text-[0.92rem]/none font-medium tracking-[0.1em] text-tmm13-ink uppercase hover:text-tmm13-acc" href="#tmm13-title">Wholesale</a></li>
          <li><a class="inline-flex min-h-11 items-center px-3.5 font-tmm13-display text-[0.92rem]/none font-medium tracking-[0.1em] text-tmm13-ink uppercase hover:text-tmm13-acc" href="#tmm13-title">Cafes</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-2 max-[52rem]:ml-0">
        <a class="inline-flex min-h-11 items-center px-2 font-tmm13-display text-[0.8rem]/none font-medium tracking-[0.12em] text-tmm13-mut uppercase hover:text-tmm13-ink" href="#tmm13-title">Account</a>
        <a class="inline-flex min-h-9 items-center gap-2 border-2 border-tmm13-line px-3 font-tmm13-display text-[0.78rem]/none font-semibold tracking-[0.12em] text-tmm13-ink uppercase transition-[translate,box-shadow] hover:-translate-x-0.5 hover:-translate-y-0.5 hover:shadow-[3px_3px_0_var(--color-tmm13-line)]" href="#tmm13-title">Cart <span class="grid size-5 place-items-center bg-tmm13-acc text-[0.7rem] text-tmm13-on-acc">2</span></a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(72rem,calc(100%-2rem))] py-[clamp(3rem,10vw,6rem)]">
    <div class="grid max-w-[34rem] gap-2.5">
      <p class="font-tmm13-display text-[0.76rem]/none font-medium tracking-[0.22em] text-tmm13-acc uppercase">This week on the roaster</p>
      <h1 class="font-tmm13-display text-[clamp(2.2rem,7vw,4rem)]/none font-semibold tracking-[0.01em] uppercase">Kirinyaga AA<br>washed, 1,780m</h1>
      <p class="flex flex-wrap items-center gap-2 text-[clamp(0.95rem,2.3vw,1.05rem)] text-tmm13-mut">Roasted Tuesday, shipped Wednesday. 250g from &pound;14. <span class="border border-tmm13-line px-1.5 py-0.5 font-tmm13-display text-[0.7rem] tracking-[0.12em] text-tmm13-ink uppercase">Batch 214</span></p>
      <a class="mt-1.5 inline-flex min-h-12 w-fit items-center border-2 border-tmm13-line bg-tmm13-acc px-5.5 font-tmm13-display text-[0.88rem]/none font-semibold tracking-[0.14em] text-tmm13-on-acc uppercase shadow-[6px_6px_0_var(--color-tmm13-line)] transition-[translate,box-shadow] hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[3px_3px_0_var(--color-tmm13-line)] active:translate-x-1.5 active:translate-y-1.5 active:shadow-none" href="#tmm13-title">Start a subscription</a>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm13-bg: #f4efe9;
  --color-tmm13-bg: oklch(0.955 0.012 65);
  --color-tmm13-surf: #fffcf8;
  --color-tmm13-surf: oklch(0.993 0.006 70);
  --color-tmm13-line: #2b211b;
  --color-tmm13-line: oklch(0.25 0.02 50);
  --color-tmm13-soft: #ece3d9;
  --color-tmm13-soft: oklch(0.92 0.017 65);
  --color-tmm13-ink: #2b211b;
  --color-tmm13-ink: oklch(0.25 0.02 50);
  --color-tmm13-mut: #665549;
  --color-tmm13-mut: oklch(0.48 0.03 55);
  --color-tmm13-acc: #7c4a2d;
  --color-tmm13-acc: oklch(0.45 0.1 50);
  --color-tmm13-on-acc: #ffffff;
  --color-tmm13-on-acc: oklch(1 0 0);
  --font-tmm13-display: 'Oswald', 'Archivo Narrow', sans-serif;
  --font-tmm13-sans: 'Work Sans', system-ui, sans-serif;
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm13-open: instead of a repeated selector list. */

@custom-variant tmm13-open {
  &:where([data-tmm13-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm13-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-13 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-13:has(#tmm13-theme:checked) {
  --color-tmm13-bg: #130f0c;
  --color-tmm13-bg: oklch(0.17 0.01 60);
  --color-tmm13-surf: #1c1712;
  --color-tmm13-surf: oklch(0.21 0.013 65);
  --color-tmm13-line: #efe6dc;
  --color-tmm13-line: oklch(0.93 0.015 70);
  --color-tmm13-soft: #2c241d;
  --color-tmm13-soft: oklch(0.27 0.017 60);
  --color-tmm13-ink: #f4ece3;
  --color-tmm13-ink: oklch(0.94 0.015 70);
  --color-tmm13-mut: #ae9e90;
  --color-tmm13-mut: oklch(0.71 0.025 65);
  --color-tmm13-acc: #e0a878;
  --color-tmm13-acc: oklch(0.78 0.1 58);
  --color-tmm13-on-acc: #1c1209;
  --color-tmm13-on-acc: oklch(0.19 0.025 60);
}

@media (prefers-color-scheme: dark) {
  .tmm-13 {
    --color-tmm13-bg: #130f0c;
    --color-tmm13-bg: oklch(0.17 0.01 60);
    --color-tmm13-surf: #1c1712;
    --color-tmm13-surf: oklch(0.21 0.013 65);
    --color-tmm13-line: #efe6dc;
    --color-tmm13-line: oklch(0.93 0.015 70);
    --color-tmm13-soft: #2c241d;
    --color-tmm13-soft: oklch(0.27 0.017 60);
    --color-tmm13-ink: #f4ece3;
    --color-tmm13-ink: oklch(0.94 0.015 70);
    --color-tmm13-mut: #ae9e90;
    --color-tmm13-mut: oklch(0.71 0.025 65);
    --color-tmm13-acc: #e0a878;
    --color-tmm13-acc: oklch(0.78 0.1 58);
    --color-tmm13-on-acc: #1c1209;
    --color-tmm13-on-acc: oklch(0.19 0.025 60);
  }

  .tmm-13:has(#tmm13-theme:checked) {
    --color-tmm13-bg: #f4efe9;
    --color-tmm13-bg: oklch(0.955 0.012 65);
    --color-tmm13-surf: #fffcf8;
    --color-tmm13-surf: oklch(0.993 0.006 70);
    --color-tmm13-line: #2b211b;
    --color-tmm13-line: oklch(0.25 0.02 50);
    --color-tmm13-soft: #ece3d9;
    --color-tmm13-soft: oklch(0.92 0.017 65);
    --color-tmm13-ink: #2b211b;
    --color-tmm13-ink: oklch(0.25 0.02 50);
    --color-tmm13-mut: #665549;
    --color-tmm13-mut: oklch(0.48 0.03 55);
    --color-tmm13-acc: #7c4a2d;
    --color-tmm13-acc: oklch(0.45 0.1 50);
    --color-tmm13-on-acc: #ffffff;
    --color-tmm13-on-acc: oklch(1 0 0);
  }
}
```
