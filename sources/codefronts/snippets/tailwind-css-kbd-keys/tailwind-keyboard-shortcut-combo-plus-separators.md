---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-keyboard-shortcut-combo-plus-separators/"
title: "Tailwind Keyboard Shortcut Combo with Plus Separators"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "The two shapes a shortcut takes, styled so they can never be confused: chords (held together) sit in one shared tray joined by +, while sequences (pressed in…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Keyboard Shortcut Combo with Plus Separators
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-keyboard-shortcut-combo-plus-separators/

The two shapes a shortcut takes, styled so they can never be confused: chords (held together) sit in one shared tray joined by +, while sequences (pressed in order) float free with a then pill between them. The outer <kbd> wraps inner <kbd>s per the HTML spec, and the separators are siblings with aria-hidden.
## HTML
```html
<section class="kbd-03 relative w-full min-h-svh scheme-light kbd03-dark:scheme-dark bg-kbd03-bg text-kbd03-ink font-kbd03-sans" aria-label="Keyboard shortcut chord and sequence demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[30rem] rounded-2xl border border-kbd03-rule bg-kbd03-panel p-6 shadow-[0_1px_2px_var(--color-kbd03-shade),0_12px_32px_-12px_var(--color-kbd03-shade)] sm:p-7">
        <header class=" flex flex-wrap items-baseline justify-between gap-x-3 gap-y-1"><h2 class="text-lg font-semibold tracking-tight">Chords</h2><p class="text-xs text-kbd03-mut">Held together · joined by plus</p></header>
        <ul class="mt-2">
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd03-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Copy selection</span><kbd class="inline-flex flex-wrap items-center gap-1 rounded-[10px] bg-kbd03-tray p-1 ring-1 ring-kbd03-rule"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">Ctrl</kbd><span class="px-0.5 text-[11px] font-medium text-kbd03-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">C</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd03-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Toggle sidebar</span><kbd class="inline-flex flex-wrap items-center gap-1 rounded-[10px] bg-kbd03-tray p-1 ring-1 ring-kbd03-rule"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">Ctrl</kbd><span class="px-0.5 text-[11px] font-medium text-kbd03-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">B</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd03-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Split editor right</span><kbd class="inline-flex flex-wrap items-center gap-1 rounded-[10px] bg-kbd03-tray p-1 ring-1 ring-kbd03-rule"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">Ctrl</kbd><span class="px-0.5 text-[11px] font-medium text-kbd03-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">Shift</kbd><span class="px-0.5 text-[11px] font-medium text-kbd03-mut" aria-hidden="true">+</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">Backslash</kbd></kbd></li>
        </ul>
        <header class="mt-7 flex flex-wrap items-baseline justify-between gap-x-3 gap-y-1"><h2 class="text-lg font-semibold tracking-tight">Sequences</h2><p class="text-xs text-kbd03-mut">Pressed in order · separated by then</p></header>
        <ul class="mt-2">
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd03-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Go to pull requests</span><kbd class="inline-flex flex-wrap items-center gap-2"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">G</kbd><span class="rounded-full bg-kbd03-thenbg px-2 py-1 text-[10px] font-bold uppercase leading-none tracking-[0.12em] text-kbd03-then">then</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">P</kbd></kbd></li>
          <li class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd03-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Go to issues</span><kbd class="inline-flex flex-wrap items-center gap-2"><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">G</kbd><span class="rounded-full bg-kbd03-thenbg px-2 py-1 text-[10px] font-bold uppercase leading-none tracking-[0.12em] text-kbd03-then">then</span><kbd class="inline-flex h-7 min-w-7 items-center justify-center rounded-md border border-kbd03-rim bg-kbd03-cap px-2 font-kbd03-mono text-xs font-medium leading-none text-kbd03-capink shadow-[0_1px_0_var(--color-kbd03-edge)]">I</kbd></kbd></li>
        </ul>
      </section>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-03-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-03-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd03-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd03-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd03-dark:bg-transparent kbd03-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd03-dark:hidden">Light</span><span class="hidden kbd03-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd03-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-03:not(:has(#kbd-03-theme:checked)), .kbd-03:not(:has(#kbd-03-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-03:has(#kbd-03-theme:checked), .kbd-03:has(#kbd-03-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd03-bg: light-dark(#eef1f5, #0f1318);
  --color-kbd03-bg: light-dark(oklch(0.957 0.006 255.5), oklch(0.185 0.012 254.1));
  --color-kbd03-panel: light-dark(#ffffff, #171c23);
  --color-kbd03-panel: light-dark(oklch(1 0 0), oklch(0.225 0.016 256.8));
  --color-kbd03-shade: light-dark(#1a2a3d1f, #00000080);
  --color-kbd03-shade: light-dark(oklch(0.28 0.041 253.4 / 0.12), oklch(0 0 0 / 0.5));
  --color-kbd03-ink: light-dark(#16202b, #e6ecf2);
  --color-kbd03-ink: light-dark(oklch(0.239 0.026 251.3), oklch(0.94 0.01 247.9));
  --color-kbd03-mut: light-dark(#536173, #94a2b3);
  --color-kbd03-mut: light-dark(oklch(0.488 0.034 254.8), oklch(0.707 0.03 253.3));
  --color-kbd03-rule: light-dark(#e1e6ec, #262d37);
  --color-kbd03-rule: light-dark(oklch(0.923 0.01 252.8), oklch(0.295 0.021 257.3));
  --color-kbd03-cap: light-dark(#ffffff, #232a35);
  --color-kbd03-cap: light-dark(oklch(1 0 0), oklch(0.283 0.023 259.4));
  --color-kbd03-rim: light-dark(#c6cfda, #3b4655);
  --color-kbd03-rim: light-dark(oklch(0.851 0.018 253.4), oklch(0.39 0.029 256.2));
  --color-kbd03-edge: light-dark(#aeb9c6, #06080b);
  --color-kbd03-edge: light-dark(oklch(0.781 0.022 252.5), oklch(0.133 0.008 254.4));
  --color-kbd03-capink: light-dark(#1d2834, #e3eaf2);
  --color-kbd03-capink: light-dark(oklch(0.272 0.027 251), oklch(0.934 0.013 251.6));
  --color-kbd03-tray: light-dark(#eef2f6, #10151b);
  --color-kbd03-tray: light-dark(oklch(0.959 0.007 247.9), oklch(0.193 0.014 253.2));
  --color-kbd03-then: light-dark(#6e35b8, #c8a6f7);
  --color-kbd03-then: light-dark(oklch(0.476 0.194 298.6), oklch(0.784 0.118 303.1));
  --color-kbd03-thenbg: light-dark(#f1e8fc, #2a2140);
  --color-kbd03-thenbg: light-dark(oklch(0.944 0.028 306), oklch(0.274 0.057 295.8));
  --color-kbd03-acc: light-dark(#2f6fd6, #7aa8f5);
  --color-kbd03-acc: light-dark(oklch(0.557 0.172 259.7), oklch(0.73 0.123 260.3));
  --font-kbd03-sans: 'Geist', system-ui, sans-serif;
  --font-kbd03-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-03 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
