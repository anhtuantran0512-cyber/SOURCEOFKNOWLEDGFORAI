---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-icon-keycaps-inline-svg/"
title: "Tailwind Icon Keycaps with Inline SVG"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "Keys whose visible label is a mark — search, escape, backspace, eject, power — drawn as inline SVG with stroke-current so they re-theme with the text colour."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon Keycaps with Inline SVG
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-icon-keycaps-inline-svg/

Keys whose visible label is a mark — search, escape, backspace, eject, power — drawn as inline SVG with stroke-current so they re-theme with the text colour. Every graphic is aria-hidden and paired with sr-only text, so the announced name is always a word; a visible caption under each cap teaches sighted readers the same word.
## HTML
```html
<section class="kbd-10 relative w-full min-h-svh scheme-light kbd10-dark:scheme-dark bg-kbd10-bg text-kbd10-ink font-kbd10-sans" aria-label="Icon only keys with inline SVG demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[32rem] rounded-3xl border border-kbd10-rule bg-kbd10-panel p-6 sm:p-8">
        <h2 class="text-xl font-bold tracking-tight">Icon caps</h2>
        <ul class="mt-6 grid grid-cols-[repeat(auto-fit,minmax(4.5rem,1fr))] gap-y-6">
          <li class="grid justify-items-center gap-2.5"><kbd class="grid size-16 place-items-center rounded-2xl border border-kbd10-rim bg-linear-to-b from-kbd10-top to-kbd10-cap text-kbd10-capink shadow-[0_2px_0_var(--color-kbd10-edge),0_10px_20px_-10px_var(--color-kbd10-shade)]"><svg class="size-6 fill-none stroke-current [stroke-linecap:round] [stroke-linejoin:round] [stroke-width:1.8]" viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 L21 21"/></svg><span class="sr-only">Search</span></kbd><span aria-hidden="true" class="text-[12px] font-medium text-kbd10-mut">Search</span></li>
          <li class="grid justify-items-center gap-2.5"><kbd class="grid size-16 place-items-center rounded-2xl border border-kbd10-rim bg-linear-to-b from-kbd10-top to-kbd10-cap text-kbd10-capink shadow-[0_2px_0_var(--color-kbd10-edge),0_10px_20px_-10px_var(--color-kbd10-shade)]"><svg class="size-6 fill-none stroke-current [stroke-linecap:round] [stroke-linejoin:round] [stroke-width:1.8]" viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6 L6 18"/><path d="M6 18 L6 12"/><path d="M6 18 L12 18"/></svg><span class="sr-only">Escape</span></kbd><span aria-hidden="true" class="text-[12px] font-medium text-kbd10-mut">Escape</span></li>
          <li class="grid justify-items-center gap-2.5"><kbd class="grid size-16 place-items-center rounded-2xl border border-kbd10-rim bg-linear-to-b from-kbd10-top to-kbd10-cap text-kbd10-capink shadow-[0_2px_0_var(--color-kbd10-edge),0_10px_20px_-10px_var(--color-kbd10-shade)]"><svg class="size-6 fill-none stroke-current [stroke-linecap:round] [stroke-linejoin:round] [stroke-width:1.8]" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12 L6 12"/><path d="M11 7 L6 12 L11 17"/><path d="M20 5 L20 19"/></svg><span class="sr-only">Backspace</span></kbd><span aria-hidden="true" class="text-[12px] font-medium text-kbd10-mut">Backspace</span></li>
          <li class="grid justify-items-center gap-2.5"><kbd class="grid size-16 place-items-center rounded-2xl border border-kbd10-rim bg-linear-to-b from-kbd10-top to-kbd10-cap text-kbd10-capink shadow-[0_2px_0_var(--color-kbd10-edge),0_10px_20px_-10px_var(--color-kbd10-shade)]"><svg class="size-6 fill-none stroke-current [stroke-linecap:round] [stroke-linejoin:round] [stroke-width:1.8]" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4 L20 13 L4 13 Z"/><path d="M4 19 L20 19"/></svg><span class="sr-only">Eject</span></kbd><span aria-hidden="true" class="text-[12px] font-medium text-kbd10-mut">Eject</span></li>
          <li class="grid justify-items-center gap-2.5"><kbd class="grid size-16 place-items-center rounded-2xl border border-kbd10-rim bg-linear-to-b from-kbd10-top to-kbd10-cap text-kbd10-capink shadow-[0_2px_0_var(--color-kbd10-edge),0_10px_20px_-10px_var(--color-kbd10-shade)]"><svg class="size-6 fill-none stroke-current [stroke-linecap:round] [stroke-linejoin:round] [stroke-width:1.8]" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 L12 11"/><path d="M6.6 6.4 A 8 8 0 1 0 17.4 6.4"/></svg><span class="sr-only">Power</span></kbd><span aria-hidden="true" class="text-[12px] font-medium text-kbd10-mut">Power</span></li>
        </ul>
        <p class="mt-7 border-t border-kbd10-rule pt-5 text-[13.5px] leading-relaxed text-kbd10-mut text-pretty">Each cap pairs an <code class="rounded bg-kbd10-code px-1.5 py-0.5 font-mono text-[12px] text-kbd10-ink">aria-hidden</code> graphic with visually hidden text, so the announced name is a word even though the visible label is a mark.</p>
      </section>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-10-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-10-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd10-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd10-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd10-dark:bg-transparent kbd10-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd10-dark:hidden">Light</span><span class="hidden kbd10-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd10-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-10:not(:has(#kbd-10-theme:checked)), .kbd-10:not(:has(#kbd-10-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-10:has(#kbd-10-theme:checked), .kbd-10:has(#kbd-10-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd10-bg: light-dark(#f3f1ee, #0f0e0d);
  --color-kbd10-bg: light-dark(oklch(0.959 0.005 78.3), oklch(0.165 0.003 67.6));
  --color-kbd10-panel: light-dark(#ffffff, #181716);
  --color-kbd10-panel: light-dark(oklch(1 0 0), oklch(0.205 0.003 67.7));
  --color-kbd10-shade: light-dark(#2a1d1033, #000000a6);
  --color-kbd10-shade: light-dark(oklch(0.243 0.03 65.6 / 0.2), oklch(0 0 0 / 0.65));
  --color-kbd10-ink: light-dark(#1d1a17, #eeebe7);
  --color-kbd10-ink: light-dark(oklch(0.22 0.007 67.4), oklch(0.941 0.006 75.4));
  --color-kbd10-mut: light-dark(#5e5852, #a59f98);
  --color-kbd10-mut: light-dark(oklch(0.464 0.012 67.5), oklch(0.706 0.012 71.8));
  --color-kbd10-rule: light-dark(#e7e3dd, #2a2826);
  --color-kbd10-rule: light-dark(oklch(0.917 0.009 78.3), oklch(0.278 0.005 67.6));
  --color-kbd10-code: light-dark(#f1ede7, #24221f);
  --color-kbd10-code: light-dark(oklch(0.948 0.009 78.3), oklch(0.253 0.006 78.2));
  --color-kbd10-cap: light-dark(#f7f5f2, #22201e);
  --color-kbd10-cap: light-dark(oklch(0.971 0.005 78.3), oklch(0.245 0.005 67.6));
  --color-kbd10-top: light-dark(#ffffff, #2e2b28);
  --color-kbd10-top: light-dark(oklch(1 0 0), oklch(0.291 0.007 67.6));
  --color-kbd10-rim: light-dark(#d4cec6, #3d3935);
  --color-kbd10-rim: light-dark(oklch(0.854 0.013 75.4), oklch(0.347 0.009 67.5));
  --color-kbd10-edge: light-dark(#b9b2a8, #060505);
  --color-kbd10-edge: light-dark(oklch(0.767 0.016 77), oklch(0.117 0.003 17.5));
  --color-kbd10-capink: light-dark(#2a2622, #ece8e3);
  --color-kbd10-capink: light-dark(oklch(0.272 0.009 67.4), oklch(0.933 0.008 73.7));
  --color-kbd10-acc: light-dark(#c2410c, #fb923c);
  --color-kbd10-acc: light-dark(oklch(0.553 0.174 38.4), oklch(0.758 0.159 55.9));
  --font-kbd10-sans: 'Manrope', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-10 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
