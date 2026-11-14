---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/bookmark-ribbon-navigation-tailwind-css/"
title: "Bookmark Ribbon Navigation in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A velvet aubergine ribbon trimmed in gilt hangs from a top rail over the active icon, on warm linen."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bookmark Ribbon Navigation in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/bookmark-ribbon-navigation-tailwind-css/

A velvet aubergine ribbon trimmed in gilt hangs from a top rail over the active icon, on warm linen. The original measured each button to centre the ribbon; the port wraps the ribbon in a column-wide frame that slides with the index trick, so it stays centred at any width. Labels are set in Cinzel for the bookplate register.
## HTML
```html
<section class="ttb-31 group/tabs grid min-h-svh w-full place-items-center bg-ttb31-linen px-5 py-14 font-ttb31-caps text-ttb31-velvet" aria-label="Bookmark ribbon navigation demo">
  <div class="grid w-full max-w-md justify-items-center gap-6">
    <div class="w-full">
      <div role="radiogroup" aria-label="Club" class="relative flex px-3 pt-7 pb-3 [--i:0] has-[#ttb31-r2:checked]:[--i:1] has-[#ttb31-r3:checked]:[--i:2] has-[#ttb31-r4:checked]:[--i:3]">
        <span aria-hidden="true" class="absolute inset-x-0 top-7 h-[3px] bg-ttb31-velvet"></span>
        <span aria-hidden="true" class="pointer-events-none absolute top-7 left-3 grid w-[calc((100%-24px)/4)] translate-x-[calc(var(--i)*100%)] justify-items-center drop-shadow-[0_4px_8px_rgb(61_30_74/0.4)] transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"><span class="relative h-21 w-14 bg-ttb31-velvet [clip-path:polygon(0_0,100%_0,100%_calc(100%_-_10px),50%_100%,0_calc(100%_-_10px))] after:absolute after:inset-x-2 after:bottom-3.5 after:h-[1.5px] after:bg-ttb31-gilt"></span></span>
        <label class="group/tab relative z-10 flex min-h-[70px] flex-1 cursor-pointer flex-col items-center gap-2 pt-3.5 text-[11px] font-bold tracking-[0.1em] text-ttb31-dim uppercase transition-colors duration-300 hover:text-ttb31-velvet has-checked:text-ttb31-linen has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb31-gilt"><input class="sr-only" type="radio" name="ttb31" id="ttb31-r1" checked><svg aria-hidden="true" class="size-5 transition-[scale] duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8M5 9.5V20h5v-6h4v6h5V9.5"/></svg>Home</label>
        <label class="group/tab relative z-10 flex min-h-[70px] flex-1 cursor-pointer flex-col items-center gap-2 pt-3.5 text-[11px] font-bold tracking-[0.1em] text-ttb31-dim uppercase transition-colors duration-300 hover:text-ttb31-velvet has-checked:text-ttb31-linen has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb31-gilt"><input class="sr-only" type="radio" name="ttb31" id="ttb31-r2"><svg aria-hidden="true" class="size-5 transition-[scale] duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-5-5"/></svg>Find</label>
        <label class="group/tab relative z-10 flex min-h-[70px] flex-1 cursor-pointer flex-col items-center gap-2 pt-3.5 text-[11px] font-bold tracking-[0.1em] text-ttb31-dim uppercase transition-colors duration-300 hover:text-ttb31-velvet has-checked:text-ttb31-linen has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb31-gilt"><input class="sr-only" type="radio" name="ttb31" id="ttb31-r3"><svg aria-hidden="true" class="size-5 transition-[scale] duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h11l3 3v13H5zM9 11h6M9 15h6"/></svg>Read</label>
        <label class="group/tab relative z-10 flex min-h-[70px] flex-1 cursor-pointer flex-col items-center gap-2 pt-3.5 text-[11px] font-bold tracking-[0.1em] text-ttb31-dim uppercase transition-colors duration-300 hover:text-ttb31-velvet has-checked:text-ttb31-linen has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb31-gilt"><input class="sr-only" type="radio" name="ttb31" id="ttb31-r4"><svg aria-hidden="true" class="size-5 transition-[scale] duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0 1 7-7h2a7 7 0 0 1 7 7v1"/></svg>Me</label>
      </div>
      <div class="px-3 pt-4 text-center font-ttb31-serif text-[16px] text-ttb31-dim italic">
        <p class="hidden group-has-[#ttb31-r1:checked]/tabs:block">The reading room — this week's acquisitions.</p>
        <p class="hidden group-has-[#ttb31-r2:checked]/tabs:block">Search the catalogue by title, author or shelf.</p>
        <p class="hidden group-has-[#ttb31-r3:checked]/tabs:block">Volumes you have on loan, and when they're due.</p>
        <p class="hidden group-has-[#ttb31-r4:checked]/tabs:block">Membership, preferences and your bookplate.</p>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb31-velvet/15 px-3.5 py-2 font-ttb31-mono text-[11.5px] text-ttb31-dim">column frame + justify-items-center · drop-shadow traces the tail</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb31-linen: #f5efe0;
  --color-ttb31-linen: oklch(0.953 0.021 88.7);
  --color-ttb31-velvet: #3d1e4a;
  --color-ttb31-velvet: oklch(0.299 0.084 315.0);
  --color-ttb31-dim: #6e5679;
  --color-ttb31-dim: oklch(0.491 0.062 315.0);
  --color-ttb31-gilt: #e6c149;
  --color-ttb31-gilt: oklch(0.822 0.141 91.6);
  --font-ttb31-caps: 'Cinzel', 'Trajan Pro', Georgia, serif;
  --font-ttb31-serif: 'Newsreader', Georgia, serif;
  --font-ttb31-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-31 {
  width: 100%;
  min-height: 100svh;
}
```
