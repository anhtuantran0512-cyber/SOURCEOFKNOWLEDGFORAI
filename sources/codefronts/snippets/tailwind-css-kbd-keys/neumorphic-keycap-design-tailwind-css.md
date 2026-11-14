---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/neumorphic-keycap-design-tailwind-css/"
title: "Neumorphic Keycap Design in Tailwind CSS"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "Soft UI keycaps extruded from the pad with paired light and dark shadows, pressing into an inset pair on group-active:."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Keycap Design in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/neumorphic-keycap-design-tailwind-css/

Soft UI keycaps extruded from the pad with paired light and dark shadows, pressing into an inset pair on group-active:. The classic neumorphism failure — shadow-only edges with no measurable contrast — is fixed with a hairline border-kbd16-rim, a label above 4.5:1 and an accent label on press, so the control stays perceivable.
## HTML
```html
<section class="kbd-16 relative w-full min-h-svh scheme-light kbd16-dark:scheme-dark bg-kbd16-bg text-kbd16-ink font-kbd16-sans" aria-label="Neumorphic soft UI keycap demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <div class="grid w-full min-w-0 max-w-[34rem] justify-items-center gap-10 text-center">
      <p class="text-[11px] font-semibold uppercase tracking-[0.24em] text-kbd16-mut">Soft UI · press a cap</p>
      <div class="flex flex-wrap justify-center gap-6">
        <button type="button" class="group rounded-[22px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd16-acc"><kbd class="grid place-items-center rounded-[22px] border border-kbd16-rim bg-kbd16-bg font-kbd16-sans font-semibold text-kbd16-capink shadow-[7px_7px_14px_var(--color-kbd16-dk),-7px_-7px_14px_var(--color-kbd16-lt)] transition-[box-shadow,color,scale] duration-150 group-active:scale-[0.98] group-active:text-kbd16-acc group-active:shadow-[inset_5px_5px_10px_var(--color-kbd16-dk),inset_-5px_-5px_10px_var(--color-kbd16-lt)] motion-reduce:transition-none size-[clamp(58px,15vw,76px)] text-2xl"><span aria-hidden="true">⌘</span><span class="sr-only">Command</span></kbd></button>
        <button type="button" class="group rounded-[22px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd16-acc"><kbd class="grid place-items-center rounded-[22px] border border-kbd16-rim bg-kbd16-bg font-kbd16-sans font-semibold text-kbd16-capink shadow-[7px_7px_14px_var(--color-kbd16-dk),-7px_-7px_14px_var(--color-kbd16-lt)] transition-[box-shadow,color,scale] duration-150 group-active:scale-[0.98] group-active:text-kbd16-acc group-active:shadow-[inset_5px_5px_10px_var(--color-kbd16-dk),inset_-5px_-5px_10px_var(--color-kbd16-lt)] motion-reduce:transition-none size-[clamp(58px,15vw,76px)] text-2xl"><span aria-hidden="true">⌥</span><span class="sr-only">Option</span></kbd></button>
        <button type="button" class="group rounded-[22px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd16-acc"><kbd class="grid place-items-center rounded-[22px] border border-kbd16-rim bg-kbd16-bg font-kbd16-sans font-semibold text-kbd16-capink shadow-[7px_7px_14px_var(--color-kbd16-dk),-7px_-7px_14px_var(--color-kbd16-lt)] transition-[box-shadow,color,scale] duration-150 group-active:scale-[0.98] group-active:text-kbd16-acc group-active:shadow-[inset_5px_5px_10px_var(--color-kbd16-dk),inset_-5px_-5px_10px_var(--color-kbd16-lt)] motion-reduce:transition-none size-[clamp(58px,15vw,76px)] text-2xl"><span aria-hidden="true">⇧</span><span class="sr-only">Shift</span></kbd></button>
        <button type="button" class="group rounded-[22px] outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd16-acc"><kbd class="grid place-items-center rounded-[22px] border border-kbd16-rim bg-kbd16-bg font-kbd16-sans font-semibold text-kbd16-capink shadow-[7px_7px_14px_var(--color-kbd16-dk),-7px_-7px_14px_var(--color-kbd16-lt)] transition-[box-shadow,color,scale] duration-150 group-active:scale-[0.98] group-active:text-kbd16-acc group-active:shadow-[inset_5px_5px_10px_var(--color-kbd16-dk),inset_-5px_-5px_10px_var(--color-kbd16-lt)] motion-reduce:transition-none h-[clamp(58px,15vw,76px)] min-w-40 px-6 text-lg">Return</kbd></button>
      </div>
      <p class="max-w-[26rem] text-[13.5px] leading-relaxed text-kbd16-mut text-pretty">Shadow-only edges have no contrast ratio. Every cap here keeps a hairline border, a label above 4.5:1 and an accent press colour, so the control stays perceivable.</p>
    </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-16-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-16-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd16-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd16-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd16-dark:bg-transparent kbd16-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd16-dark:hidden">Light</span><span class="hidden kbd16-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd16-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-16:not(:has(#kbd-16-theme:checked)), .kbd-16:not(:has(#kbd-16-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-16:has(#kbd-16-theme:checked), .kbd-16:has(#kbd-16-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd16-bg: light-dark(#e4e8ee, #22252c);
  --color-kbd16-bg: light-dark(oklch(0.93 0.009 258.3), oklch(0.264 0.014 267));
  --color-kbd16-dk: light-dark(#b8c0cc, #15171b);
  --color-kbd16-dk: light-dark(oklch(0.805 0.019 258.4), oklch(0.204 0.009 264.4));
  --color-kbd16-lt: light-dark(#ffffff, #30343d);
  --color-kbd16-lt: light-dark(oklch(1 0 0), oklch(0.325 0.017 266.4));
  --color-kbd16-rim: light-dark(#a9b2c0, #4b515d);
  --color-kbd16-rim: light-dark(oklch(0.761 0.022 259.2), oklch(0.434 0.021 264.3));
  --color-kbd16-ink: light-dark(#262b35, #e6e9ef);
  --color-kbd16-ink: light-dark(oklch(0.288 0.02 264.2), oklch(0.933 0.009 264.5));
  --color-kbd16-mut: light-dark(#535b68, #a2a9b5);
  --color-kbd16-mut: light-dark(oklch(0.469 0.023 260.1), oklch(0.733 0.019 261.3));
  --color-kbd16-capink: light-dark(#323946, #e1e5ec);
  --color-kbd16-capink: light-dark(oklch(0.343 0.025 262.8), oklch(0.921 0.01 261.8));
  --color-kbd16-acc: light-dark(#3d5bd9, #8ea4ff);
  --color-kbd16-acc: light-dark(oklch(0.525 0.196 268.5), oklch(0.739 0.134 272.4));
  --font-kbd16-sans: 'Outfit', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-16 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
