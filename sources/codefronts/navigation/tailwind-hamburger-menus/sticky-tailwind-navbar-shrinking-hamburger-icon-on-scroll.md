---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/sticky-tailwind-navbar-shrinking-hamburger-icon-on-scroll/"
title: "Sticky Tailwind Navbar Shrinking Hamburger Icon on Scroll"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The shrinking header without a scroll listener: CSS scroll-driven animations bind a keyframe track to scroll position, so the navbar compresses, the wordmark…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Tailwind Navbar Shrinking Hamburger Icon on Scroll
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/sticky-tailwind-navbar-shrinking-hamburger-icon-on-scroll/

The shrinking header without a scroll listener: CSS scroll-driven animations bind a keyframe track to scroll position, so the navbar compresses, the wordmark tightens, the burger slims and a frosted border fades in &mdash; all proportional to the first 140px. In utilities the animation is a token and its clock is two arbitrary properties, which reads as exactly what it is: this animation's timeline is the scroller.
## HTML
```html
<section class="thb-25 w-full min-h-svh grid justify-center content-start bg-thb25-bg font-thb25-sans text-thb25-ink px-5 py-9" aria-label="Shrinking sticky navbar on scroll demo">
  <div class="w-[min(420px,88vw)] h-135 rounded-3xl overflow-hidden bg-thb25-bg border border-thb25-edge">
    <div class="h-full overflow-y-auto overscroll-contain [scrollbar-gutter:stable]">
      <header class="group sticky top-0 z-2 px-5 py-4.5 bg-[oklch(0.985_0.004_250/0.4)] animate-thb25-shrink [animation-timeline:scroll(nearest)] [animation-range:0_140px] motion-reduce:animate-none">
        <input type="checkbox" id="thb25-t" class="peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
        <div class="flex items-center justify-between">
          <span class="text-[17px] font-extrabold tracking-[0.16em] uppercase animate-thb25-brand [animation-timeline:scroll(nearest)] [animation-range:0_140px] motion-reduce:animate-none">Meridian</span>
          <label for="thb25-t" class="grid place-items-center w-11.5 h-11.5 rounded-xl border border-thb25-edge bg-white cursor-pointer select-none transition-[background] duration-200 hover:bg-thb25-hover peer-focus-visible:outline-2 peer-focus-visible:outline-thb25-acc peer-focus-visible:outline-offset-2 animate-thb25-btn [animation-timeline:scroll(nearest)] [animation-range:0_140px] motion-reduce:animate-none" aria-hidden="true">
            <span class="relative block w-4.5 h-3 animate-thb25-ico [animation-timeline:scroll(nearest)] [animation-range:0_140px] motion-reduce:animate-none">
              <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-thb25-ink transition-[translate,rotate] duration-280 group-has-checked:translate-y-[5px] group-has-checked:rotate-45 motion-reduce:transition-none"></i>
              <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-thb25-ink transition-[opacity] duration-200 group-has-checked:opacity-0 motion-reduce:transition-none"></i>
              <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-thb25-ink transition-[translate,rotate] duration-280 group-has-checked:-translate-y-[5px] group-has-checked:-rotate-45 motion-reduce:transition-none"></i>
            </span>
          </label>
        </div>
        <nav aria-label="Primary" class="grid opacity-0 [grid-template-rows:0fr] transition-[grid-template-rows,opacity] duration-350 ease-thb25 group-has-checked:opacity-100 group-has-checked:[grid-template-rows:1fr] motion-reduce:transition-none">
          <ul class="list-none min-h-0 overflow-hidden">
            <li><a href="#journal" class="flex items-center min-h-11 mt-3 px-1 border-y border-[color-mix(in_oklch,var(--color-thb25-edge)_60%,transparent)] text-sm font-semibold text-thb25-mut no-underline transition-[color,padding] duration-150 hover:text-thb25-acc hover:pl-2.5 focus-visible:text-thb25-acc focus-visible:outline-2 focus-visible:outline-thb25-acc focus-visible:-outline-offset-2">Journal</a></li>
            <li><a href="#maps" class="flex items-center min-h-11 px-1 border-b border-[color-mix(in_oklch,var(--color-thb25-edge)_60%,transparent)] text-sm font-semibold text-thb25-mut no-underline transition-[color,padding] duration-150 hover:text-thb25-acc hover:pl-2.5 focus-visible:text-thb25-acc focus-visible:outline-2 focus-visible:outline-thb25-acc focus-visible:-outline-offset-2">Maps</a></li>
            <li><a href="#expeditions" class="flex items-center min-h-11 px-1 border-b border-[color-mix(in_oklch,var(--color-thb25-edge)_60%,transparent)] text-sm font-semibold text-thb25-mut no-underline transition-[color,padding] duration-150 hover:text-thb25-acc hover:pl-2.5 focus-visible:text-thb25-acc focus-visible:outline-2 focus-visible:outline-thb25-acc focus-visible:-outline-offset-2">Expeditions</a></li>
          </ul>
        </nav>
      </header>
      <div class="grid gap-3.5 px-5 pt-4.5 pb-6.5" aria-hidden="true">
        <div class="flex flex-col justify-end gap-1 h-50 p-4.5 rounded-2xl bg-linear-[150deg,oklch(0.9_0.04_235),oklch(0.82_0.07_255)]">
          <b class="text-2xl font-bold tracking-[-0.01em]">Scroll &darr;</b>
          <span class="text-[12.5px] text-thb25-heroink">the header compresses over the first 140px &mdash; pure CSS</span>
        </div>
        <div class="h-2.75 w-[88%] rounded-full bg-thb25-line"></div>
        <div class="h-2.75 w-[72%] rounded-full bg-thb25-line"></div>
        <div class="h-2.75 w-[80%] rounded-full bg-thb25-line"></div>
        <div class="h-2.75 w-[56%] rounded-full bg-thb25-line"></div>
        <div class="h-32.5 rounded-[14px] bg-white border border-thb25-edge"></div>
        <div class="h-2.75 w-[84%] rounded-full bg-thb25-line"></div>
        <div class="h-2.75 w-[66%] rounded-full bg-thb25-line"></div>
        <div class="h-2.75 w-[77%] rounded-full bg-thb25-line"></div>
        <div class="h-2.75 w-[49%] rounded-full bg-thb25-line"></div>
        <div class="h-32.5 rounded-[14px] bg-linear-[150deg,oklch(0.93_0.02_200),oklch(0.88_0.04_180)]"></div>
        <div class="h-2.75 w-[81%] rounded-full bg-thb25-line"></div>
        <div class="h-2.75 w-[59%] rounded-full bg-thb25-line"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb25-bg: #fafbfc;
  --color-thb25-bg: oklch(0.985 0.004 250);
  --color-thb25-edge: #e3e4ea;
  --color-thb25-edge: oklch(0.9 0.008 250);
  --color-thb25-line: #e8e9ef;
  --color-thb25-line: oklch(0.91 0.006 250);
  --color-thb25-hover: #f2f3f7;
  --color-thb25-hover: oklch(0.96 0.006 250);
  --color-thb25-ink: #32354a;
  --color-thb25-ink: oklch(0.24 0.018 255);
  --color-thb25-mut: #73768c;
  --color-thb25-mut: oklch(0.54 0.014 255);
  --color-thb25-heroink: #4a5a7d;
  --color-thb25-heroink: oklch(0.4 0.05 255);
  --color-thb25-acc: #3f6fd0;
  --color-thb25-acc: oklch(0.55 0.15 240);
  --font-thb25-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb25-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb25: cubic-bezier(0.2, 0.7, 0.2, 1);
  --animate-thb25-shrink: thb25-shrink linear both;
  --animate-thb25-brand: thb25-brand linear both;
  --animate-thb25-btn: thb25-btn linear both;
  --animate-thb25-ico: thb25-ico linear both;
}
/* Four keyframe blocks, one per element riding the shared scroll timeline.
   Keyframes are rules; the @theme --animate-* entries above only name them. */

@keyframes thb25-shrink {
  to {
    padding-block: 8px;
    background: oklch(0.99 0.003 250 / 0.85);
    box-shadow: 0 1px 0 var(--color-thb25-edge), 0 8px 24px -18px oklch(0 0 0 / 0.3);
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
  }
}

@keyframes thb25-brand {
  to {
    font-size: 14.5px;
    letter-spacing: 0.1em;
  }
}

@keyframes thb25-btn {
  to {
    width: 38px;
    height: 38px;
    border-radius: 10px;
  }
}

@keyframes thb25-ico {
  to {
    scale: 0.85;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-25 {
  width: 100%;
  min-height: 100svh;
}
```
