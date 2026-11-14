---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-mac-cmd-vs-windows-ctrl-shortcut-toggle/"
title: "Tailwind Mac Cmd vs Windows Ctrl Shortcut Toggle"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "A shortcut reference with a macOS / Windows segmented control — zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mac Cmd vs Windows Ctrl Shortcut Toggle
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-mac-cmd-vs-windows-ctrl-shortcut-toggle/

A shortcut reference with a macOS / Windows segmented control — zero JavaScript. The radios live inside their labels, so has-checked: styles the active tab, and a one-line @custom-variant kbd06-win lets every key inside the demo choose between ⌘ and Ctrl. Mac glyphs carry sr-only names, so a screen reader says “Command”, not “place of interest sign”.
## HTML
```html
<section class="kbd-06 relative w-full min-h-svh scheme-light kbd06-dark:scheme-dark bg-kbd06-bg text-kbd06-ink font-kbd06-sans" aria-label="Mac versus Windows shortcut toggle demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[30rem] rounded-2xl border border-kbd06-rule bg-kbd06-panel p-6 shadow-[0_1px_2px_var(--color-kbd06-shade),0_16px_40px_-16px_var(--color-kbd06-shade)] sm:p-7">
        <h2 class="text-lg font-semibold tracking-tight">Shortcut reference</h2>
        <fieldset class="mt-4 grid grid-cols-2 gap-1 rounded-xl bg-kbd06-seg p-1">
          <legend class="sr-only">Choose a platform</legend>
          <label class="flex min-h-11 cursor-pointer items-center justify-center rounded-lg text-sm font-medium text-kbd06-mut transition-[background-color,color,box-shadow] hover:text-kbd06-ink has-checked:bg-kbd06-segon has-checked:text-kbd06-ink has-checked:shadow-[0_1px_2px_var(--color-kbd06-shade),0_0_0_1px_var(--color-kbd06-rule)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-kbd06-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="kbd-06-os" id="kbd-06-mac" checked>macOS</label>
          <label class="flex min-h-11 cursor-pointer items-center justify-center rounded-lg text-sm font-medium text-kbd06-mut transition-[background-color,color,box-shadow] hover:text-kbd06-ink has-checked:bg-kbd06-segon has-checked:text-kbd06-ink has-checked:shadow-[0_1px_2px_var(--color-kbd06-shade),0_0_0_1px_var(--color-kbd06-rule)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-kbd06-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="kbd-06-os" id="kbd-06-win">Windows</label>
        </fieldset>
        <ul class="mt-3 divide-y divide-kbd06-rule">
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Save file</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]"><span class="kbd06-win:hidden"><span aria-hidden="true" class="text-[15px]">⌘</span><span class="sr-only">Command</span></span><span class="hidden kbd06-win:inline">Ctrl</span></kbd><span class="text-[11px] text-kbd06-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]">S</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Redo</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]"><span class="kbd06-win:hidden"><span aria-hidden="true" class="text-[15px]">⇧</span><span class="sr-only">Shift</span></span><span class="hidden kbd06-win:inline">Shift</span></kbd><span class="text-[11px] text-kbd06-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]"><span class="kbd06-win:hidden"><span aria-hidden="true" class="text-[15px]">⌘</span><span class="sr-only">Command</span></span><span class="hidden kbd06-win:inline">Ctrl</span></kbd><span class="text-[11px] text-kbd06-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]">Z</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Delete word left</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]"><span class="kbd06-win:hidden"><span aria-hidden="true" class="text-[15px]">⌥</span><span class="sr-only">Option</span></span><span class="hidden kbd06-win:inline">Ctrl</span></kbd><span class="text-[11px] text-kbd06-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]"><span class="kbd06-win:hidden"><span aria-hidden="true" class="text-[15px]">⌫</span><span class="sr-only">Delete</span></span><span class="hidden kbd06-win:inline">Backspace</span></kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Open terminal</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]"><span class="kbd06-win:hidden"><span aria-hidden="true" class="text-[15px]">⌃</span><span class="sr-only">Control</span></span><span class="hidden kbd06-win:inline">Ctrl</span></kbd><span class="text-[11px] text-kbd06-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]">Backtick</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Confirm dialog</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]"><span class="kbd06-win:hidden"><span aria-hidden="true" class="text-[15px]">⏎</span><span class="sr-only">Return</span></span><span class="hidden kbd06-win:inline">Enter</span></kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 py-3"><span class="min-w-0 text-[14.5px]">Dismiss dialog</span><kbd class="inline-flex flex-wrap items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)]"><span class="kbd06-win:hidden"><span aria-hidden="true" class="text-[15px]">⎋</span><span class="sr-only">Escape</span></span><span class="hidden kbd06-win:inline">Esc</span></kbd></kbd></li>
        </ul>
        <div class="mt-4 border-t border-kbd06-rule pt-4 kbd06-win:hidden">
          <p class="mb-2.5 text-xs text-kbd06-mut">Mac modifiers print in Apple's order</p>
          <ol class="flex flex-wrap gap-x-4 gap-y-2 text-[13px] text-kbd06-mut"><li class="flex items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)] h-7 min-w-7 text-[14px]" aria-hidden="true">⌃</kbd><span>Control</span></li><li class="flex items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)] h-7 min-w-7 text-[14px]" aria-hidden="true">⌥</kbd><span>Option</span></li><li class="flex items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)] h-7 min-w-7 text-[14px]" aria-hidden="true">⇧</kbd><span>Shift</span></li><li class="flex items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-md border border-kbd06-rim bg-kbd06-cap px-2 text-[12.5px] font-medium leading-none text-kbd06-capink shadow-[0_1px_0_var(--color-kbd06-edge)] h-7 min-w-7 text-[14px]" aria-hidden="true">⌘</kbd><span>Command</span></li></ol>
        </div>
      </section>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-06-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-06-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd06-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd06-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd06-dark:bg-transparent kbd06-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd06-dark:hidden">Light</span><span class="hidden kbd06-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd06-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-06:not(:has(#kbd-06-theme:checked)), .kbd-06:not(:has(#kbd-06-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-06:has(#kbd-06-theme:checked), .kbd-06:has(#kbd-06-theme:checked) *) {
      @slot;
    }
  }
}

@custom-variant kbd06-win (&: where(.kbd-06: has(#kbd-06-win: checked) *));
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd06-bg: light-dark(#f2f3f5, #0e1013);
  --color-kbd06-bg: light-dark(oklch(0.964 0.003 264.5), oklch(0.172 0.007 258.4));
  --color-kbd06-panel: light-dark(#ffffff, #16191e);
  --color-kbd06-panel: light-dark(oklch(1 0 0), oklch(0.212 0.011 260.7));
  --color-kbd06-shade: light-dark(#10203414, #00000080);
  --color-kbd06-shade: light-dark(oklch(0.241 0.044 254.8 / 0.08), oklch(0 0 0 / 0.5));
  --color-kbd06-ink: light-dark(#111418, #eceef1);
  --color-kbd06-ink: light-dark(oklch(0.19 0.009 255.6), oklch(0.948 0.005 258.3));
  --color-kbd06-mut: light-dark(#545c67, #9aa3af);
  --color-kbd06-mut: light-dark(oklch(0.472 0.02 256.4), oklch(0.712 0.02 255.6));
  --color-kbd06-rule: light-dark(#e5e7eb, #272b32);
  --color-kbd06-rule: light-dark(oklch(0.928 0.006 264.5), oklch(0.288 0.014 261.7));
  --color-kbd06-seg: light-dark(#eceef1, #0f1216);
  --color-kbd06-seg: light-dark(oklch(0.948 0.005 258.3), oklch(0.181 0.01 255.6));
  --color-kbd06-segon: light-dark(#ffffff, #2a2f38);
  --color-kbd06-segon: light-dark(oklch(1 0 0), oklch(0.304 0.018 262.2));
  --color-kbd06-cap: light-dark(#f8f9fb, #20242b);
  --color-kbd06-cap: light-dark(oklch(0.982 0.003 264.5), oklch(0.259 0.014 261.7));
  --color-kbd06-rim: light-dark(#cdd2d9, #3b414b);
  --color-kbd06-rim: light-dark(oklch(0.862 0.011 256.7), oklch(0.374 0.019 260.7));
  --color-kbd06-edge: light-dark(#b3b9c2, #050608);
  --color-kbd06-edge: light-dark(oklch(0.784 0.014 258.4), oklch(0.122 0.006 261.6));
  --color-kbd06-capink: light-dark(#1b1f25, #e9ecf0);
  --color-kbd06-capink: light-dark(oklch(0.238 0.013 258.4), oklch(0.942 0.006 255.5));
  --color-kbd06-acc: light-dark(#0a62d0, #5ea2ff);
  --color-kbd06-acc: light-dark(oklch(0.517 0.186 258.1), oklch(0.709 0.153 256.7));
  --font-kbd06-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-06 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
