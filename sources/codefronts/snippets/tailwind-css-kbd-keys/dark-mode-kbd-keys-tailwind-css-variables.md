---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/dark-mode-kbd-keys-tailwind-css-variables/"
title: "Dark Mode Kbd Keys with Tailwind CSS Variables"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "The theming technique the whole collection runs on, shown on its own: every token is light-dark(day, night) in @theme, the root flips scheme-light →…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Kbd Keys with Tailwind CSS Variables
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/dark-mode-kbd-keys-tailwind-css-variables/

The theming technique the whole collection runs on, shown on its own: every token is light-dark(day, night) in @theme, the root flips scheme-light → scheme-dark through a :has(:checked) custom variant, and a CSS-only role="switch" drives it. Live swatches in the token list repaint with the theme, so the variable → colour mapping is visible.
## HTML
```html
<section class="kbd-20 relative w-full min-h-svh scheme-light kbd20-dark:scheme-dark bg-kbd20-page text-kbd20-ink font-kbd20-sans transition-colors duration-300 motion-reduce:transition-none" aria-label="Dark mode kbd keys with CSS variables demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[30rem] rounded-2xl border border-kbd20-rule bg-kbd20-panel p-6 shadow-[0_20px_50px_-28px_var(--color-kbd20-shade)] transition-colors duration-300 motion-reduce:transition-none sm:p-7">
        <header class="mb-3 flex flex-wrap items-center justify-between gap-3">
          <h2 class="text-lg font-semibold tracking-tight">Theme-aware keys</h2>
          <label for="kbd-20-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-3">
            <input id="kbd-20-theme" type="checkbox" role="switch" class="peer sr-only">
            <span aria-hidden="true" class="relative h-6 w-11 flex-none rounded-full bg-kbd20-track ring-1 ring-kbd20-rule transition-colors duration-200 peer-checked:bg-kbd20-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd20-acc after:absolute after:top-0.5 after:left-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_#0000004d] after:transition-[translate] after:duration-200 after:content-[''] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none"></span>
            <span class="text-[13.5px] font-medium">Dark mode</span>
          </label>
        </header>
        <ul>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd20-rule py-3 transition-colors duration-300 last:border-0"><span class="min-w-0 text-[14px]">Command palette</span><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">Ctrl</kbd><span class="text-[11px] text-kbd20-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">K</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd20-rule py-3 transition-colors duration-300 last:border-0"><span class="min-w-0 text-[14px]">Toggle theme</span><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">Ctrl</kbd><span class="text-[11px] text-kbd20-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">Shift</kbd><span class="text-[11px] text-kbd20-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">L</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd20-rule py-3 transition-colors duration-300 last:border-0"><span class="min-w-0 text-[14px]">Save all</span><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">Ctrl</kbd><span class="text-[11px] text-kbd20-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">Alt</kbd><span class="text-[11px] text-kbd20-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">S</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd20-rule py-3 transition-colors duration-300 last:border-0"><span class="min-w-0 text-[14px]">Close panel</span><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd20-rim bg-kbd20-cap px-2 text-[12px] font-semibold leading-none text-kbd20-capink shadow-[0_1px_0_var(--color-kbd20-edge)] transition-colors duration-300 motion-reduce:transition-none">Esc</kbd></kbd></li>
        </ul>
        <dl class="mt-4 grid gap-2.5 border-t border-kbd20-rule pt-4 transition-colors duration-300">
          <div class="flex min-w-0 items-center gap-2.5"><span aria-hidden="true" class="size-4 flex-none rounded border border-kbd20-rim bg-kbd20-cap transition-colors duration-300"></span><dt class="rounded bg-kbd20-cap px-1.5 py-0.5 font-kbd20-mono text-[11px] text-kbd20-capink transition-colors duration-300">--color-kbd20-cap</dt><dd class="min-w-0 text-[12px] text-kbd20-mut">cap face</dd></div>
          <div class="flex min-w-0 items-center gap-2.5"><span aria-hidden="true" class="size-4 flex-none rounded border border-kbd20-rim bg-kbd20-capink transition-colors duration-300"></span><dt class="rounded bg-kbd20-cap px-1.5 py-0.5 font-kbd20-mono text-[11px] text-kbd20-capink transition-colors duration-300">--color-kbd20-capink</dt><dd class="min-w-0 text-[12px] text-kbd20-mut">label colour</dd></div>
          <div class="flex min-w-0 items-center gap-2.5"><span aria-hidden="true" class="size-4 flex-none rounded border border-kbd20-rim bg-kbd20-rule transition-colors duration-300"></span><dt class="rounded bg-kbd20-cap px-1.5 py-0.5 font-kbd20-mono text-[11px] text-kbd20-capink transition-colors duration-300">--color-kbd20-rule</dt><dd class="min-w-0 text-[12px] text-kbd20-mut">borders and dividers</dd></div>
          <div class="flex min-w-0 items-center gap-2.5"><span aria-hidden="true" class="size-4 flex-none rounded border border-kbd20-rim bg-kbd20-acc transition-colors duration-300"></span><dt class="rounded bg-kbd20-cap px-1.5 py-0.5 font-kbd20-mono text-[11px] text-kbd20-capink transition-colors duration-300">--color-kbd20-acc</dt><dd class="min-w-0 text-[12px] text-kbd20-mut">switch and focus ring</dd></div>
        </dl>
      </section>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: the in-panel switch IS the theme — checked means dark, whatever the OS says. */

@custom-variant kbd20-dark (&: where(.kbd-20: has(#kbd-20-theme: checked), .kbd-20: has(#kbd-20-theme: checked) *));
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd20-page: light-dark(#eef0f3, #14181d);
  --color-kbd20-page: light-dark(oklch(0.954 0.005 258.3), oklch(0.207 0.012 254.1));
  --color-kbd20-panel: light-dark(#ffffff, #1c222a);
  --color-kbd20-panel: light-dark(oklch(1 0 0), oklch(0.25 0.018 255.7));
  --color-kbd20-shade: light-dark(#10203433, #000000b3);
  --color-kbd20-shade: light-dark(oklch(0.241 0.044 254.8 / 0.2), oklch(0 0 0 / 0.7));
  --color-kbd20-ink: light-dark(#1b2129, #e9eef4);
  --color-kbd20-ink: light-dark(oklch(0.245 0.018 255.7), oklch(0.947 0.01 252.8));
  --color-kbd20-mut: light-dark(#5b6571, #97a3b0);
  --color-kbd20-mut: light-dark(oklch(0.503 0.023 253), oklch(0.71 0.023 250.3));
  --color-kbd20-rule: light-dark(#dce1e7, #2b333d);
  --color-kbd20-rule: light-dark(oklch(0.908 0.01 252.8), oklch(0.318 0.021 254.1));
  --color-kbd20-track: light-dark(#d5dbe3, #323b47);
  --color-kbd20-track: light-dark(oklch(0.889 0.013 255.5), oklch(0.349 0.024 255.7));
  --color-kbd20-cap: light-dark(#f3f5f8, #242c36);
  --color-kbd20-cap: light-dark(oklch(0.969 0.005 258.3), oklch(0.29 0.022 254.2));
  --color-kbd20-rim: light-dark(#c9d1da, #3b4653);
  --color-kbd20-rim: light-dark(oklch(0.857 0.015 251.2), oklch(0.39 0.026 252.8));
  --color-kbd20-edge: light-dark(#b0b9c4, #0a0d10);
  --color-kbd20-edge: light-dark(oklch(0.782 0.019 253.4), oklch(0.157 0.008 248.4));
  --color-kbd20-capink: light-dark(#313b47, #dce6f1);
  --color-kbd20-capink: light-dark(oklch(0.348 0.025 253.2), oklch(0.921 0.018 250.6));
  --color-kbd20-acc: light-dark(#3b6ea5, #7fb0e8);
  --color-kbd20-acc: light-dark(oklch(0.528 0.103 251.9), oklch(0.744 0.097 252.4));
  --font-kbd20-sans: 'Geist', system-ui, sans-serif;
  --font-kbd20-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-20 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
