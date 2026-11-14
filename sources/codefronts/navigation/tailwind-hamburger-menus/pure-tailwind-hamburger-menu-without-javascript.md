---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/pure-tailwind-hamburger-menu-without-javascript/"
title: "Pure Tailwind Hamburger Menu Without JavaScript"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The checkbox hack rebuilt for the :has() era, and this is where the port pays back demo 05's friction: group-has-checked: reads the state from an ANCESTOR,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Hamburger Menu Without JavaScript
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/pure-tailwind-hamburger-menu-without-javascript/

The checkbox hack rebuilt for the :has() era, and this is where the port pays back demo 05's friction: group-has-checked: reads the state from an ANCESTOR, so the burger, the header, the fullscreen panel and even the page content in a different subtree all respond &mdash; no sibling order, no arbitrary variants, no hook classes. Same zero-JS guarantee, none of the DOM gymnastics.
## HTML
```html
<section class="thb-09 w-full min-h-svh grid justify-center content-start bg-thb09-bg font-thb09-sans text-thb09-ink px-5 py-9" aria-label="Pure Tailwind :has() hamburger menu demo">
  <div class="group relative w-[min(400px,88vw)] h-135 rounded-3xl overflow-hidden bg-thb09-bg border border-thb09-edge">
    <input type="checkbox" id="thb09-t" class="peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
    <div class="absolute inset-0 grid content-start gap-3.5 px-6 pt-21.5 pb-6 transition-[scale,filter,opacity] duration-500 ease-thb09 group-has-checked:scale-96 group-has-checked:blur-[2px] group-has-checked:opacity-55 motion-reduce:transition-none motion-reduce:group-has-checked:blur-none" aria-hidden="true">
      <div class="flex flex-col justify-end h-47.5 mb-1.5 p-4.5 rounded-2xl bg-linear-[150deg,oklch(0.9_0.035_70),oklch(0.84_0.06_45)]">
        <b class="font-thb09-mono text-[30px] font-bold tracking-[-0.02em]">:has()</b>
        <span class="text-[12.5px] text-thb09-mut">state, readable anywhere</span>
      </div>
      <div class="h-2.75 w-[82%] rounded-full bg-thb09-line"></div>
      <div class="h-2.75 w-[60%] rounded-full bg-thb09-line"></div>
      <div class="h-2.75 w-[73%] rounded-full bg-thb09-line"></div>
    </div>
    <nav aria-label="Site" class="absolute inset-0 z-2 flex flex-col justify-center px-8 bg-linear-[170deg,color-mix(in_oklch,var(--color-thb09-panel)_92%,white),var(--color-thb09-panel)_60%] opacity-0 scale-[1.04] invisible [transition:opacity_.4s,scale_.5s_var(--ease-thb09),visibility_0s_.5s] group-has-checked:opacity-100 group-has-checked:scale-100 group-has-checked:visible group-has-checked:[transition:opacity_.4s,scale_.5s_var(--ease-thb09),visibility_0s_0s]">
      <a href="#index" style="--i:0" class="group/l flex items-center justify-between py-4 px-0.5 rounded border-b border-[oklch(1_0_0/0.12)] text-[30px] font-bold tracking-[-0.02em] text-thb09-panelink no-underline opacity-0 translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb09 hover:text-thb09-panhover focus-visible:text-thb09-panhover focus-visible:outline-2 focus-visible:outline-thb09-acc focus-visible:outline-offset-4 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(140ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><span>Index</span><span class="text-lg text-thb09-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-250 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a>
      <a href="#essays" style="--i:1" class="group/l flex items-center justify-between py-4 px-0.5 rounded border-b border-[oklch(1_0_0/0.12)] text-[30px] font-bold tracking-[-0.02em] text-thb09-panelink no-underline opacity-0 translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb09 hover:text-thb09-panhover focus-visible:text-thb09-panhover focus-visible:outline-2 focus-visible:outline-thb09-acc focus-visible:outline-offset-4 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(140ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><span>Essays</span><span class="text-lg text-thb09-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-250 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a>
      <a href="#library" style="--i:2" class="group/l flex items-center justify-between py-4 px-0.5 rounded border-b border-[oklch(1_0_0/0.12)] text-[30px] font-bold tracking-[-0.02em] text-thb09-panelink no-underline opacity-0 translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb09 hover:text-thb09-panhover focus-visible:text-thb09-panhover focus-visible:outline-2 focus-visible:outline-thb09-acc focus-visible:outline-offset-4 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(140ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><span>Library</span><span class="text-lg text-thb09-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-250 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a>
      <a href="#colophon" style="--i:3" class="group/l flex items-center justify-between py-4 px-0.5 rounded border-b border-[oklch(1_0_0/0.12)] text-[30px] font-bold tracking-[-0.02em] text-thb09-panelink no-underline opacity-0 translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb09 hover:text-thb09-panhover focus-visible:text-thb09-panhover focus-visible:outline-2 focus-visible:outline-thb09-acc focus-visible:outline-offset-4 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(140ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><span>Colophon</span><span class="text-lg text-thb09-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-250 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a>
    </nav>
    <header class="absolute inset-x-0 top-0 z-3 flex items-center justify-between h-17.5 pl-6 pr-4">
      <span class="text-base font-bold italic tracking-[-0.01em] transition-[color] duration-350 group-has-checked:text-thb09-panelink">marginalia</span>
      <label for="thb09-t" class="grid place-items-center w-11.5 h-11.5 rounded-full bg-thb09-ink text-thb09-bg cursor-pointer select-none transition-[background,color,scale] duration-300 hover:scale-106 peer-focus-visible:outline-2 peer-focus-visible:outline-thb09-acc peer-focus-visible:outline-offset-3 group-has-checked:bg-thb09-panelink group-has-checked:text-thb09-panel motion-reduce:transition-none">
        <span class="relative block w-4.5 h-3" aria-hidden="true">
          <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-has-checked:translate-y-[5px] group-has-checked:rotate-45 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 group-has-checked:opacity-0 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-has-checked:-translate-y-[5px] group-has-checked:-rotate-45 motion-reduce:transition-none"></i>
        </span>
      </label>
    </header>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb09-bg: #f7f4ec;
  --color-thb09-bg: oklch(0.965 0.008 85);
  --color-thb09-edge: #ddd7cb;
  --color-thb09-edge: oklch(0.87 0.015 80);
  --color-thb09-line: #e2ddd0;
  --color-thb09-line: oklch(0.89 0.012 80);
  --color-thb09-ink: #38322a;
  --color-thb09-ink: oklch(0.24 0.02 60);
  --color-thb09-mut: #787064;
  --color-thb09-mut: oklch(0.52 0.02 60);
  --color-thb09-panel: #3a2f26;
  --color-thb09-panel: oklch(0.24 0.03 55);
  --color-thb09-panelink: #f3efe6;
  --color-thb09-panelink: oklch(0.95 0.015 80);
  --color-thb09-panhover: #d8bb92;
  --color-thb09-panhover: oklch(0.85 0.09 60);
  --color-thb09-acc: #b4713f;
  --color-thb09-acc: oklch(0.58 0.16 45);
  --font-thb09-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb09-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb09: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-09 {
  width: 100%;
  min-height: 100svh;
}
```
