---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-tooltip-keyboard-shortcut-hint/"
title: "Tailwind Tooltip with Keyboard Shortcut Hint"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "An editor toolbar whose tooltips name the action and its shortcut."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tooltip with Keyboard Shortcut Hint
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-tooltip-keyboard-shortcut-hint/

An editor toolbar whose tooltips name the action and its shortcut. Pure Tailwind: group-hover: opens a tip after a 300ms intent delay, group-has-focus-visible: opens it instantly for keyboard users, and the arrow is an after: border triangle. Each tip is a real role="tooltip" wired with aria-describedby.
## HTML
```html
<section class="kbd-13 relative w-full min-h-svh scheme-light kbd13-dark:scheme-dark bg-kbd13-bg text-kbd13-ink font-kbd13-sans" aria-label="Tooltip with keyboard shortcut demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <div class="grid justify-items-center gap-6 text-center">
      <div role="toolbar" aria-label="Formatting" class="mt-14 inline-flex gap-1 rounded-xl border border-kbd13-rule bg-kbd13-panel p-1.5 shadow-[0_1px_2px_var(--color-kbd13-shade),0_12px_28px_-14px_var(--color-kbd13-shade)]">
        <div class="group relative">
          <button type="button" aria-describedby="kbd-13-tip-bold" class="grid size-11 place-items-center rounded-lg text-kbd13-ink transition-colors hover:bg-kbd13-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-kbd13-acc"><span aria-hidden="true" class="text-[17px] font-bold">B</span><span class="sr-only">Bold</span></button>
          <span id="kbd-13-tip-bold" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-10 flex -translate-x-1/2 translate-y-1 items-center gap-2.5 rounded-lg bg-kbd13-tip px-2.5 py-2 text-[12.5px] font-medium whitespace-nowrap text-kbd13-tipink opacity-0 shadow-[0_8px_24px_-8px_var(--color-kbd13-shade)] transition-[opacity,translate] duration-150 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-300 group-has-focus-visible:translate-y-0 group-has-focus-visible:opacity-100 group-has-focus-visible:delay-0 after:absolute after:top-full after:left-1/2 after:-translate-x-1/2 after:border-[5px] after:border-transparent after:border-t-kbd13-tip after:content-[''] motion-reduce:transition-none">Bold<kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">Ctrl</kbd><span class="text-[10px] opacity-70" aria-hidden="true">+</span><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">B</kbd></kbd></span>
        </div>
        <div class="group relative">
          <button type="button" aria-describedby="kbd-13-tip-italic" class="grid size-11 place-items-center rounded-lg text-kbd13-ink transition-colors hover:bg-kbd13-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-kbd13-acc"><span aria-hidden="true" class="font-serif text-[18px] italic">I</span><span class="sr-only">Italic</span></button>
          <span id="kbd-13-tip-italic" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-10 flex -translate-x-1/2 translate-y-1 items-center gap-2.5 rounded-lg bg-kbd13-tip px-2.5 py-2 text-[12.5px] font-medium whitespace-nowrap text-kbd13-tipink opacity-0 shadow-[0_8px_24px_-8px_var(--color-kbd13-shade)] transition-[opacity,translate] duration-150 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-300 group-has-focus-visible:translate-y-0 group-has-focus-visible:opacity-100 group-has-focus-visible:delay-0 after:absolute after:top-full after:left-1/2 after:-translate-x-1/2 after:border-[5px] after:border-transparent after:border-t-kbd13-tip after:content-[''] motion-reduce:transition-none">Italic<kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">Ctrl</kbd><span class="text-[10px] opacity-70" aria-hidden="true">+</span><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">I</kbd></kbd></span>
        </div>
        <div class="group relative">
          <button type="button" aria-describedby="kbd-13-tip-link" class="grid size-11 place-items-center rounded-lg text-kbd13-ink transition-colors hover:bg-kbd13-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-kbd13-acc"><svg class="size-5 fill-none stroke-current [stroke-linecap:round] [stroke-linejoin:round] [stroke-width:2]" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7 0l2-2a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-2 2a5 5 0 0 0 7 7l1-1"/></svg><span class="sr-only">Insert link</span></button>
          <span id="kbd-13-tip-link" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-10 flex -translate-x-1/2 translate-y-1 items-center gap-2.5 rounded-lg bg-kbd13-tip px-2.5 py-2 text-[12.5px] font-medium whitespace-nowrap text-kbd13-tipink opacity-0 shadow-[0_8px_24px_-8px_var(--color-kbd13-shade)] transition-[opacity,translate] duration-150 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-300 group-has-focus-visible:translate-y-0 group-has-focus-visible:opacity-100 group-has-focus-visible:delay-0 after:absolute after:top-full after:left-1/2 after:-translate-x-1/2 after:border-[5px] after:border-transparent after:border-t-kbd13-tip after:content-[''] motion-reduce:transition-none">Insert link<kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">Ctrl</kbd><span class="text-[10px] opacity-70" aria-hidden="true">+</span><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">K</kbd></kbd></span>
        </div>
        <div class="group relative">
          <button type="button" aria-describedby="kbd-13-tip-comment" class="grid size-11 place-items-center rounded-lg text-kbd13-ink transition-colors hover:bg-kbd13-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-kbd13-acc"><svg class="size-5 fill-none stroke-current [stroke-linecap:round] [stroke-linejoin:round] [stroke-width:2]" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 15a3 3 0 0 1-3 3H9l-5 3V6a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3z"/></svg><span class="sr-only">Add comment</span></button>
          <span id="kbd-13-tip-comment" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-10 flex -translate-x-1/2 translate-y-1 items-center gap-2.5 rounded-lg bg-kbd13-tip px-2.5 py-2 text-[12.5px] font-medium whitespace-nowrap text-kbd13-tipink opacity-0 shadow-[0_8px_24px_-8px_var(--color-kbd13-shade)] transition-[opacity,translate] duration-150 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-300 group-has-focus-visible:translate-y-0 group-has-focus-visible:opacity-100 group-has-focus-visible:delay-0 after:absolute after:top-full after:left-1/2 after:-translate-x-1/2 after:border-[5px] after:border-transparent after:border-t-kbd13-tip after:content-[''] motion-reduce:transition-none">Add comment<kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">Ctrl</kbd><span class="text-[10px] opacity-70" aria-hidden="true">+</span><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">Alt</kbd><span class="text-[10px] opacity-70" aria-hidden="true">+</span><kbd class="inline-flex h-5 min-w-5 items-center justify-center rounded border border-kbd13-tiprim bg-kbd13-tipcap px-1 font-mono text-[11px] leading-none text-kbd13-tipink">M</kbd></kbd></span>
        </div>
      </div>
      <p class="max-w-[24rem] text-[13.5px] text-kbd13-mut text-pretty">Hover a button and pause, or Tab to one — keyboard focus opens the tooltip instantly.</p>
    </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-13-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-13-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd13-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd13-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd13-dark:bg-transparent kbd13-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd13-dark:hidden">Light</span><span class="hidden kbd13-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd13-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-13:not(:has(#kbd-13-theme:checked)), .kbd-13:not(:has(#kbd-13-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-13:has(#kbd-13-theme:checked), .kbd-13:has(#kbd-13-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd13-bg: light-dark(#f3f4f6, #0d0e11);
  --color-kbd13-bg: light-dark(oklch(0.967 0.003 264.5), oklch(0.164 0.007 271));
  --color-kbd13-panel: light-dark(#ffffff, #17191d);
  --color-kbd13-panel: light-dark(oklch(1 0 0), oklch(0.213 0.008 264.4));
  --color-kbd13-hover: light-dark(#f0f1f4, #23262c);
  --color-kbd13-hover: light-dark(oklch(0.958 0.004 271.4), oklch(0.268 0.012 264.4));
  --color-kbd13-shade: light-dark(#10203426, #000000a6);
  --color-kbd13-shade: light-dark(oklch(0.241 0.044 254.8 / 0.15), oklch(0 0 0 / 0.65));
  --color-kbd13-ink: light-dark(#15171b, #eceef1);
  --color-kbd13-ink: light-dark(oklch(0.204 0.009 264.4), oklch(0.948 0.005 258.3));
  --color-kbd13-mut: light-dark(#59606b, #99a1ad);
  --color-kbd13-mut: light-dark(oklch(0.487 0.02 259.4), oklch(0.706 0.02 258.4));
  --color-kbd13-rule: light-dark(#e3e5e9, #272a30);
  --color-kbd13-rule: light-dark(oklch(0.922 0.006 264.5), oklch(0.284 0.012 264.4));
  --color-kbd13-tip: light-dark(#1b1e23, #f2f4f7);
  --color-kbd13-tip: light-dark(oklch(0.234 0.011 260.7), oklch(0.966 0.005 258.3));
  --color-kbd13-tipink: light-dark(#f4f6f8, #16181c);
  --color-kbd13-tipink: light-dark(oklch(0.972 0.003 247.9), oklch(0.209 0.009 264.4));
  --color-kbd13-tipcap: light-dark(#2c3037, #e3e6eb);
  --color-kbd13-tipcap: light-dark(oklch(0.308 0.014 261.7), oklch(0.924 0.008 260.7));
  --color-kbd13-tiprim: light-dark(#454a53, #c6cbd3);
  --color-kbd13-tiprim: light-dark(oklch(0.408 0.016 262.3), oklch(0.841 0.012 259.8));
  --color-kbd13-acc: light-dark(#2563eb, #7aa7ff);
  --color-kbd13-acc: light-dark(oklch(0.546 0.215 262.9), oklch(0.733 0.137 262.9));
  --font-kbd13-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-13 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
