---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/brutalist-design-bordered-tailwind-hamburger-menu/"
title: "Brutalist Design Bordered Tailwind Hamburger Menu"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Neo-brutalism with its rules intact: 3px black borders on everything, hard offset shadows that do not blur, one shrieking yellow, uppercase mono type &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Design Bordered Tailwind Hamburger Menu
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/brutalist-design-bordered-tailwind-hamburger-menu/

Neo-brutalism with its rules intact: 3px black borders on everything, hard offset shadows that do not blur, one shrieking yellow, uppercase mono type &mdash; and motion that CUTS instead of eases, because in this dialect a transition curve is a lie. The press is the port's neatest line: the plate travels exactly its shadow's offset and lands flat, which is two utilities sitting next to each other.
## HTML
```html
<section class="thb-27 w-full min-h-svh grid justify-center content-start bg-thb27-paper font-thb27-mono text-thb27-ink px-5 py-9" aria-label="Brutalist bordered menu demo">
  <div class="group relative flex flex-col w-[min(400px,88vw)] h-140 overflow-hidden border-[3px] border-thb27-ink bg-thb27-paper shadow-[8px_8px_0_var(--color-thb27-ink)] [background-image:radial-gradient(oklch(0.18_0.01_90/0.14)_1.2px,transparent_1.3px)] [background-size:18px_18px]">
    <input type="checkbox" id="thb27-t" class="peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
    <header class="relative z-2 flex items-center justify-between p-3.5 border-b-[3px] border-thb27-ink bg-thb27-paper">
      <span class="text-base font-bold tracking-[0.04em]">RAW&mdash;GOODS<i class="not-italic align-super text-[10px]" aria-hidden="true">&reg;</i></span>
      <label for="thb27-t" class="flex items-center gap-2.5 min-h-11.5 px-3.5 border-[3px] border-thb27-ink bg-thb27-acc cursor-pointer select-none shadow-[6px_6px_0_var(--color-thb27-ink)] transition-[translate,box-shadow,background] duration-[60ms] ease-linear hover:bg-thb27-acc2 peer-focus-visible:outline-3 peer-focus-visible:outline-thb27-ink peer-focus-visible:outline-offset-3 group-has-checked:translate-x-1.5 group-has-checked:translate-y-1.5 group-has-checked:shadow-[0_0_0_var(--color-thb27-ink)]">
        <span class="relative block w-5 h-3.5" aria-hidden="true">
          <i class="absolute left-0 top-0 w-5 h-[3px] bg-thb27-ink transition-[translate,rotate] duration-[60ms] ease-linear group-has-checked:translate-y-[5.5px] group-has-checked:rotate-45"></i>
          <i class="absolute left-0 top-[5.5px] w-5 h-[3px] bg-thb27-ink transition-[opacity] duration-[60ms] ease-linear group-has-checked:opacity-0"></i>
          <i class="absolute left-0 top-[11px] w-5 h-[3px] bg-thb27-ink transition-[translate,rotate] duration-[60ms] ease-linear group-has-checked:-translate-y-[5.5px] group-has-checked:-rotate-45"></i>
        </span>
        <span class="text-xs font-bold tracking-[0.08em] group-has-checked:hidden" aria-hidden="true">MENU</span>
        <span class="hidden text-xs font-bold tracking-[0.08em] group-has-checked:block" aria-hidden="true">CLOSE</span>
      </label>
    </header>
    <nav aria-label="Site" class="absolute inset-x-0 top-[79px] bottom-10 z-1 hidden flex-col bg-thb27-paper border-b-[3px] border-thb27-ink group-has-checked:flex">
      <div class="border-b-[3px] border-thb27-ink"><a href="#shop" class="group/r flex items-center gap-3.5 min-h-16 px-4.5 text-[15px] font-bold tracking-[0.06em] text-thb27-ink no-underline hover:bg-thb27-ink hover:text-thb27-paper focus-visible:bg-thb27-ink focus-visible:text-thb27-paper focus-visible:outline-3 focus-visible:outline-thb27-acc focus-visible:-outline-offset-6"><b class="px-1.5 py-0.5 border-2 border-thb27-ink text-[11px] group-hover/r:border-thb27-paper group-focus-visible/r:border-thb27-paper">01</b>SHOP ALL<span class="ml-auto text-lg" aria-hidden="true">&rarr;</span></a></div>
      <div class="border-b-[3px] border-thb27-ink"><a href="#drops" class="group/r flex items-center gap-3.5 min-h-16 px-4.5 text-[15px] font-bold tracking-[0.06em] text-thb27-ink no-underline hover:bg-thb27-ink hover:text-thb27-paper focus-visible:bg-thb27-ink focus-visible:text-thb27-paper focus-visible:outline-3 focus-visible:outline-thb27-acc focus-visible:-outline-offset-6"><b class="px-1.5 py-0.5 border-2 border-thb27-ink text-[11px] group-hover/r:border-thb27-paper group-focus-visible/r:border-thb27-paper">02</b>DROPS<span class="ml-auto text-lg" aria-hidden="true">&rarr;</span></a></div>
      <div class="border-b-[3px] border-thb27-ink"><a href="#manifesto" class="group/r flex items-center gap-3.5 min-h-16 px-4.5 text-[15px] font-bold tracking-[0.06em] text-thb27-ink no-underline hover:bg-thb27-ink hover:text-thb27-paper focus-visible:bg-thb27-ink focus-visible:text-thb27-paper focus-visible:outline-3 focus-visible:outline-thb27-acc focus-visible:-outline-offset-6"><b class="px-1.5 py-0.5 border-2 border-thb27-ink text-[11px] group-hover/r:border-thb27-paper group-focus-visible/r:border-thb27-paper">03</b>MANIFESTO<span class="ml-auto text-lg" aria-hidden="true">&rarr;</span></a></div>
      <div class="border-b-[3px] border-thb27-ink"><a href="#faq" class="group/r flex items-center gap-3.5 min-h-16 px-4.5 text-[15px] font-bold tracking-[0.06em] text-thb27-ink no-underline hover:bg-thb27-ink hover:text-thb27-paper focus-visible:bg-thb27-ink focus-visible:text-thb27-paper focus-visible:outline-3 focus-visible:outline-thb27-acc focus-visible:-outline-offset-6"><b class="px-1.5 py-0.5 border-2 border-thb27-ink text-[11px] group-hover/r:border-thb27-paper group-focus-visible/r:border-thb27-paper">04</b>FAQ<span class="ml-auto text-lg" aria-hidden="true">&rarr;</span></a></div>
    </nav>
    <div class="flex-1 grid content-start gap-4.5 p-5.5" aria-hidden="true">
      <div class="w-max -rotate-1.5 px-4 py-3 border-[3px] border-thb27-ink bg-thb27-acc text-xs font-bold leading-[1.7] tracking-[0.06em] shadow-[6px_6px_0_var(--color-thb27-ink)]">EST. 2026<br>NO COOKIES<br>NO TRACKING</div>
      <div class="h-37.5 border-[3px] border-thb27-ink [background:repeating-linear-gradient(-45deg,var(--color-thb27-paper)_0_12px,oklch(0.18_0.01_90/0.12)_12px_24px)]"></div>
    </div>
    <div class="mt-auto overflow-hidden py-2.25 border-t-[3px] border-thb27-ink bg-thb27-ink text-thb27-paper" aria-hidden="true">
      <div class="flex w-max animate-thb27-tape motion-reduce:animate-none">
        <span class="whitespace-nowrap text-[11.5px] font-bold tracking-[0.14em]">FREE SHIPPING OVER $80 &#9733; PRESS THE PLATE &#9733; EVERYTHING HAS A BORDER &#9733;&nbsp;</span>
        <span class="whitespace-nowrap text-[11.5px] font-bold tracking-[0.14em]">FREE SHIPPING OVER $80 &#9733; PRESS THE PLATE &#9733; EVERYTHING HAS A BORDER &#9733;&nbsp;</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb27-paper: #f7f4e9;
  --color-thb27-paper: oklch(0.96 0.01 95);
  --color-thb27-ink: #1f1c14;
  --color-thb27-ink: oklch(0.18 0.01 90);
  --color-thb27-acc: #f2d43c;
  --color-thb27-acc: oklch(0.86 0.17 95);
  --color-thb27-acc2: #ffe23f;
  --color-thb27-acc2: oklch(0.9 0.19 95);
  --font-thb27-mono: 'JetBrains Mono', ui-monospace, 'Cascadia Mono', Menlo, monospace;
  --animate-thb27-tape: thb27-tape 14s linear infinite;
}
/* Keyframes are a rule, not a value — the @theme --animate-* entry only names this. */

@keyframes thb27-tape {
  to {
    translate: -50% 0;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-27 {
  width: 100%;
  min-height: 100svh;
}
```
