---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/retro-typewriter-round-keys-tailwind-css/"
title: "Retro Typewriter Round Keys in Tailwind CSS"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "Round glass-top typewriter keys on an enamel plate, after the Wickfield No."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Typewriter Round Keys in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/retro-typewriter-round-keys-tailwind-css/

Round glass-top typewriter keys on an enamel plate, after the Wickfield No. 5: a domed radial-gradient face, a nickel ring-[3px] rim, a hard offset stem shadow and a Courier Prime legend. Each key is a button that drops 4px on group-active: while the stem shadow shortens, and the second row is offset half a key like the real machine.
## HTML
```html
<section class="kbd-18 relative w-full min-h-svh scheme-light kbd18-dark:scheme-dark bg-kbd18-bg bg-[radial-gradient(80%_60%_at_50%_30%,var(--color-kbd18-glow),transparent_70%)] text-kbd18-ink" aria-label="Retro typewriter round keycap demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <div class="w-full min-w-0 max-w-[34rem] rounded-[28px] bg-kbd18-plate p-[clamp(18px,5vw,34px)] shadow-[inset_0_1px_0_var(--color-kbd18-plateshine),inset_0_-6px_12px_var(--color-kbd18-platesh),0_30px_60px_-30px_var(--color-kbd18-drop)] [--k:clamp(46px,12vw,60px)]">
        <p class="mb-6 text-center font-kbd18-serif text-[clamp(22px,5vw,30px)] italic tracking-wide text-kbd18-gold">Wickfield · No. 5</p>
        <div class="grid gap-4">
          <div class="flex flex-wrap justify-center gap-3">
          <button type="button" class="group size-(--k) rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">Q</kbd></button>
          <button type="button" class="group size-(--k) rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">W</kbd></button>
          <button type="button" class="group size-(--k) rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">E</kbd></button>
          <button type="button" class="group size-(--k) rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">R</kbd></button>
          <button type="button" class="group size-(--k) rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">T</kbd></button>
          </div>
          <div class="flex flex-wrap justify-center gap-3 sm:pl-[calc(var(--k)*0.5)]">
          <button type="button" class="group size-(--k) rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">A</kbd></button>
          <button type="button" class="group size-(--k) rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">S</kbd></button>
          <button type="button" class="group size-(--k) rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">D</kbd></button>
          <button type="button" class="group h-(--k) w-[calc(var(--k)*1.9)] *:rounded-full *:text-[15px] rounded-full outline-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-kbd18-acc"><kbd class="grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-kbd18-caphi),var(--color-kbd18-cap)_68%)] font-kbd18-type text-[clamp(16px,4vw,20px)] font-bold text-kbd18-capink ring-[3px] ring-kbd18-nickel shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_5px_0_var(--color-kbd18-stem),0_9px_10px_-2px_var(--color-kbd18-drop)] transition-[translate,box-shadow] duration-75 group-active:translate-y-1 group-active:shadow-[inset_0_-2px_3px_var(--color-kbd18-capsh),0_1px_0_var(--color-kbd18-stem),0_3px_4px_-1px_var(--color-kbd18-drop)] motion-reduce:transition-none">Shift</kbd></button>
          </div>
        </div>
        <p class="mt-7 text-center font-kbd18-type text-[12.5px] text-kbd18-platemut">Hard offset stem · nickel ring · domed glass top</p>
      </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-18-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-18-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd18-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd18-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd18-dark:bg-transparent kbd18-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd18-dark:hidden">Light</span><span class="hidden kbd18-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd18-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-18:not(:has(#kbd-18-theme:checked)), .kbd-18:not(:has(#kbd-18-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-18:has(#kbd-18-theme:checked), .kbd-18:has(#kbd-18-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd18-bg: light-dark(#efe6d2, #0d0c0a);
  --color-kbd18-bg: light-dark(oklch(0.927 0.028 86.6), oklch(0.155 0.004 84.6));
  --color-kbd18-glow: light-dark(#fbf5e8, #1d1a14);
  --color-kbd18-glow: light-dark(oklch(0.971 0.018 86.1), oklch(0.219 0.012 84.5));
  --color-kbd18-ink: light-dark(#2a241a, #efe6d2);
  --color-kbd18-ink: light-dark(oklch(0.264 0.02 80.3), oklch(0.927 0.028 86.6));
  --color-kbd18-plate: light-dark(#1f2a24, #18201c);
  --color-kbd18-plate: light-dark(oklch(0.272 0.019 161), oklch(0.234 0.014 163.5));
  --color-kbd18-plateshine: light-dark(#3c4a42, #2d3832);
  --color-kbd18-plateshine: light-dark(oklch(0.394 0.022 160.1), oklch(0.328 0.018 161.4));
  --color-kbd18-platesh: light-dark(#0b100d, #060807);
  --color-kbd18-platesh: light-dark(oklch(0.166 0.01 158.8), oklch(0.131 0.005 165.2));
  --color-kbd18-platemut: light-dark(#b9c2b6, #a8b2a6);
  --color-kbd18-platemut: light-dark(oklch(0.804 0.019 137.8), oklch(0.752 0.02 140.5));
  --color-kbd18-gold: light-dark(#e3c27a, #d9b56a);
  --color-kbd18-gold: light-dark(oklch(0.827 0.098 85.7), oklch(0.789 0.103 84.4));
  --color-kbd18-cap: light-dark(#f4ecd8, #e9dfc6);
  --color-kbd18-cap: light-dark(oklch(0.944 0.028 88.8), oklch(0.905 0.035 88.8));
  --color-kbd18-caphi: light-dark(#ffffff, #fbf6ea);
  --color-kbd18-caphi: light-dark(oklch(1 0 0), oklch(0.974 0.017 88));
  --color-kbd18-capsh: light-dark(#c9bb98, #bcae8c);
  --color-kbd18-capsh: light-dark(oklch(0.795 0.05 88.8), oklch(0.754 0.049 88.3));
  --color-kbd18-capink: light-dark(#1c1a16, #1c1a16);
  --color-kbd18-capink: light-dark(oklch(0.219 0.008 84.6), oklch(0.219 0.008 84.6));
  --color-kbd18-nickel: light-dark(#c7ccd1, #a9afb6);
  --color-kbd18-nickel: light-dark(oklch(0.843 0.009 247.9), oklch(0.751 0.012 252.1));
  --color-kbd18-stem: light-dark(#4b4f54, #2b2e32);
  --color-kbd18-stem: light-dark(oklch(0.426 0.01 253.9), oklch(0.3 0.008 255.6));
  --color-kbd18-drop: light-dark(#00000059, #000000b3);
  --color-kbd18-drop: light-dark(oklch(0 0 0 / 0.35), oklch(0 0 0 / 0.7));
  --color-kbd18-acc: light-dark(#b5651d, #f0a24a);
  --color-kbd18-acc: light-dark(oklch(0.587 0.13 56.8), oklch(0.773 0.138 66.3));
  --font-kbd18-type: 'Courier Prime', 'Courier New', monospace;
  --font-kbd18-serif: 'Instrument Serif', Georgia, serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-18 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
