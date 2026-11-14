---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-3d-keycap-button-press-down-effect/"
title: "Tailwind 3D Keycap Button with Press-Down Effect"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "A chunky 3D keycap whose wall is a solid 0_6px_0 shadow that collapses to 0_2px_0 as the face travels down translate-y-1 — 4px of travel, perfectly…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Keycap Button with Press-Down Effect
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-3d-keycap-button-press-down-effect/

A chunky 3D keycap whose wall is a solid 0_6px_0 shadow that collapses to 0_2px_0 as the face travels down translate-y-1 — 4px of travel, perfectly synchronised, so the key looks pressed rather than sunk. Each cap is a real <button> wrapping a <kbd>, so it responds to pointer and a held Space bar.
## HTML
```html
<section class="kbd-02 relative w-full min-h-svh scheme-light kbd02-dark:scheme-dark bg-kbd02-bg text-kbd02-ink font-kbd02-sans" aria-label="3D keycap press-down demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <div class="grid w-full max-w-[36rem] justify-items-center gap-7 text-center">
      <p class="text-sm text-kbd02-mut">Press and hold a cap — or Tab to one and hold <strong class="font-semibold text-kbd02-ink">Space</strong></p>
      <div class="flex flex-wrap justify-center gap-3 rounded-[22px] bg-kbd02-tray p-5 pb-6 shadow-[inset_0_2px_6px_var(--color-kbd02-drop)]">
        <button type="button" class="group rounded-[14px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd02-acc"><kbd class="grid h-16 min-w-16 rounded-[12px] border bg-linear-to-b px-4 font-kbd02-sans font-semibold transition-[translate,box-shadow] duration-[90ms] ease-out group-active:translate-y-1 motion-reduce:transition-none border-kbd02-accwall from-kbd02-acctop to-kbd02-acc text-kbd02-accink shadow-[inset_0_1px_0_var(--color-kbd02-acctop),0_6px_0_var(--color-kbd02-accwall),0_12px_18px_-6px_var(--color-kbd02-drop)] group-active:shadow-[inset_0_1px_0_var(--color-kbd02-acctop),0_2px_0_var(--color-kbd02-accwall),0_4px_8px_-4px_var(--color-kbd02-drop)] place-items-center text-base">Esc</kbd></button>
        <button type="button" class="group rounded-[14px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd02-acc"><kbd class="grid h-16 min-w-16 rounded-[12px] border bg-linear-to-b px-4 font-kbd02-sans font-semibold transition-[translate,box-shadow] duration-[90ms] ease-out group-active:translate-y-1 motion-reduce:transition-none border-kbd02-rim from-kbd02-top to-kbd02-cap text-kbd02-capink shadow-[inset_0_1px_0_var(--color-kbd02-top),0_6px_0_var(--color-kbd02-wall),0_12px_18px_-6px_var(--color-kbd02-drop)] group-active:shadow-[inset_0_1px_0_var(--color-kbd02-top),0_2px_0_var(--color-kbd02-wall),0_4px_8px_-4px_var(--color-kbd02-drop)] place-items-center text-lg">Q</kbd></button>
        <button type="button" class="group rounded-[14px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd02-acc"><kbd class="grid h-16 min-w-16 rounded-[12px] border bg-linear-to-b px-4 font-kbd02-sans font-semibold transition-[translate,box-shadow] duration-[90ms] ease-out group-active:translate-y-1 motion-reduce:transition-none border-kbd02-rim from-kbd02-top to-kbd02-cap text-kbd02-capink shadow-[inset_0_1px_0_var(--color-kbd02-top),0_6px_0_var(--color-kbd02-wall),0_12px_18px_-6px_var(--color-kbd02-drop)] group-active:shadow-[inset_0_1px_0_var(--color-kbd02-top),0_2px_0_var(--color-kbd02-wall),0_4px_8px_-4px_var(--color-kbd02-drop)] place-items-center text-lg">W</kbd></button>
        <button type="button" class="group rounded-[14px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd02-acc"><kbd class="grid h-16 min-w-16 rounded-[12px] border bg-linear-to-b px-4 font-kbd02-sans font-semibold transition-[translate,box-shadow] duration-[90ms] ease-out group-active:translate-y-1 motion-reduce:transition-none border-kbd02-rim from-kbd02-top to-kbd02-cap text-kbd02-capink shadow-[inset_0_1px_0_var(--color-kbd02-top),0_6px_0_var(--color-kbd02-wall),0_12px_18px_-6px_var(--color-kbd02-drop)] group-active:shadow-[inset_0_1px_0_var(--color-kbd02-top),0_2px_0_var(--color-kbd02-wall),0_4px_8px_-4px_var(--color-kbd02-drop)] place-items-center text-lg">E</kbd></button>
        <button type="button" class="group rounded-[14px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd02-acc"><kbd class="grid h-16 min-w-16 rounded-[12px] border bg-linear-to-b px-4 font-kbd02-sans font-semibold transition-[translate,box-shadow] duration-[90ms] ease-out group-active:translate-y-1 motion-reduce:transition-none border-kbd02-rim from-kbd02-top to-kbd02-cap text-kbd02-capink shadow-[inset_0_1px_0_var(--color-kbd02-top),0_6px_0_var(--color-kbd02-wall),0_12px_18px_-6px_var(--color-kbd02-drop)] group-active:shadow-[inset_0_1px_0_var(--color-kbd02-top),0_2px_0_var(--color-kbd02-wall),0_4px_8px_-4px_var(--color-kbd02-drop)] place-items-center text-lg">R</kbd></button>
        <button type="button" class="group rounded-[14px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd02-acc"><kbd class="grid h-16 min-w-36 rounded-[12px] border bg-linear-to-b px-4 font-kbd02-sans font-semibold transition-[translate,box-shadow] duration-[90ms] ease-out group-active:translate-y-1 motion-reduce:transition-none border-kbd02-rim from-kbd02-top to-kbd02-cap text-kbd02-capink shadow-[inset_0_1px_0_var(--color-kbd02-top),0_6px_0_var(--color-kbd02-wall),0_12px_18px_-6px_var(--color-kbd02-drop)] group-active:shadow-[inset_0_1px_0_var(--color-kbd02-top),0_2px_0_var(--color-kbd02-wall),0_4px_8px_-4px_var(--color-kbd02-drop)] items-end justify-items-start pb-2.5 text-sm">Shift</kbd></button>
      </div>
      <p class="font-mono text-xs tracking-wide text-kbd02-mut">travel 4px · wall 6px → 2px · 90ms</p>
    </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-02-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-02-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd02-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd02-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd02-dark:bg-transparent kbd02-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd02-dark:hidden">Light</span><span class="hidden kbd02-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd02-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-02:not(:has(#kbd-02-theme:checked)), .kbd-02:not(:has(#kbd-02-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-02:has(#kbd-02-theme:checked), .kbd-02:has(#kbd-02-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd02-bg: light-dark(#ebe6dc, #121418);
  --color-kbd02-bg: light-dark(oklch(0.926 0.014 84.6), oklch(0.191 0.009 264.3));
  --color-kbd02-ink: light-dark(#24211c, #e8eaee);
  --color-kbd02-ink: light-dark(oklch(0.249 0.01 80.6), oklch(0.937 0.006 264.5));
  --color-kbd02-mut: light-dark(#5d564b, #9ba2ae);
  --color-kbd02-mut: light-dark(oklch(0.456 0.02 79.2), oklch(0.71 0.019 261.3));
  --color-kbd02-tray: light-dark(#dcd5c7, #0b0d10);
  --color-kbd02-tray: light-dark(oklch(0.875 0.02 84.6), oklch(0.158 0.007 258.4));
  --color-kbd02-cap: light-dark(#f6f2ea, #2a2e36);
  --color-kbd02-cap: light-dark(oklch(0.962 0.011 84.6), oklch(0.301 0.016 264.3));
  --color-kbd02-top: light-dark(#ffffff, #3a404b);
  --color-kbd02-top: light-dark(oklch(1 0 0), oklch(0.37 0.021 262.6));
  --color-kbd02-rim: light-dark(#d3ccbf, #474d59);
  --color-kbd02-rim: light-dark(oklch(0.847 0.019 83.1), oklch(0.419 0.021 264.3));
  --color-kbd02-wall: light-dark(#b9af9d, #05060a);
  --color-kbd02-wall: light-dark(oklch(0.757 0.028 82.4), oklch(0.123 0.011 271.4));
  --color-kbd02-drop: light-dark(#6b5f4c66, #00000099);
  --color-kbd02-drop: light-dark(oklch(0.492 0.033 79.2 / 0.4), oklch(0 0 0 / 0.6));
  --color-kbd02-capink: light-dark(#2b2720, #eef0f4);
  --color-kbd02-capink: light-dark(oklch(0.275 0.014 81.7), oklch(0.955 0.006 264.5));
  --color-kbd02-acc: light-dark(#d9541f, #f0703a);
  --color-kbd02-acc: light-dark(oklch(0.615 0.178 39.6), oklch(0.69 0.172 41.8));
  --color-kbd02-acctop: light-dark(#f2804e, #ff9563);
  --color-kbd02-acctop: light-dark(oklch(0.719 0.154 43.3), oklch(0.772 0.143 45.3));
  --color-kbd02-accwall: light-dark(#9b3510, #8a300c);
  --color-kbd02-accwall: light-dark(oklch(0.473 0.144 38.1), oklch(0.436 0.13 39.2));
  --color-kbd02-accink: light-dark(#ffffff, #ffffff);
  --color-kbd02-accink: light-dark(oklch(1 0 0), oklch(1 0 0));
  --font-kbd02-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-02 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
