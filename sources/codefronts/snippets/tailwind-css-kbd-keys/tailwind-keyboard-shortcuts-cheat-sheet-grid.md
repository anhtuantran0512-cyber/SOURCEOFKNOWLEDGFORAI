---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-keyboard-shortcuts-cheat-sheet-grid/"
title: "Tailwind Keyboard Shortcuts Cheat Sheet Grid"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "A four-group reference sheet for the Atlas editor that reflows from four columns to one with grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))]."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Keyboard Shortcuts Cheat Sheet Grid
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-keyboard-shortcuts-cheat-sheet-grid/

A four-group reference sheet for the Atlas editor that reflows from four columns to one with grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))]. Keys hug the right edge of every row so the key column stays aligned across groups, rows highlight on hover for scanning, and print: utilities strip shadows and backgrounds so the sheet prints clean.
## HTML
```html
<section class="kbd-12 relative w-full min-h-svh scheme-light kbd12-dark:scheme-dark bg-kbd12-bg text-kbd12-ink font-kbd12-sans print:bg-white" aria-label="Keyboard shortcut cheatsheet grid demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[64rem] rounded-3xl border border-kbd12-rule bg-kbd12-panel p-6 shadow-[0_24px_60px_-30px_var(--color-kbd12-shade)] sm:p-9 print:border-0 print:shadow-none">
        <header class="mb-8 flex flex-wrap items-end justify-between gap-x-6 gap-y-2">
          <h2 class="text-[clamp(26px,4.5vw,38px)] font-extrabold leading-none tracking-[-0.02em]">Keyboard shortcuts</h2>
          <p class="font-kbd12-mono text-[12px] text-kbd12-mut">Atlas editor · version 4.2</p>
        </header>
        <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))] gap-x-9 gap-y-8">
        <section class="min-w-0 break-inside-avoid">
          <h3 class="mb-2 flex items-center gap-2 border-b border-kbd12-rule pb-2 text-[11px] font-bold uppercase tracking-[0.18em] text-kbd12-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Navigation</h3>
          <div class="grid">
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Go to file</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">P</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Go to symbol</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Shift</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">O</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Back</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">−</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Next problem</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">F8</kbd></kbd></div>
          </div>
        </section>
        <section class="min-w-0 break-inside-avoid">
          <h3 class="mb-2 flex items-center gap-2 border-b border-kbd12-rule pb-2 text-[11px] font-bold uppercase tracking-[0.18em] text-kbd12-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Editing</h3>
          <div class="grid">
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Save</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">S</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Undo</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Z</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Duplicate line</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Shift</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Alt</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">↓</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Rename symbol</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">F2</kbd></kbd></div>
          </div>
        </section>
        <section class="min-w-0 break-inside-avoid">
          <h3 class="mb-2 flex items-center gap-2 border-b border-kbd12-rule pb-2 text-[11px] font-bold uppercase tracking-[0.18em] text-kbd12-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>View</h3>
          <div class="grid">
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Toggle sidebar</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">B</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Split editor</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">\</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Zen mode</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">K</kbd><span class="px-0.5 text-[10px] font-semibold uppercase tracking-[0.1em] text-kbd12-acc">then</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Z</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Toggle terminal</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">&#96;</kbd></kbd></div>
          </div>
        </section>
        <section class="min-w-0 break-inside-avoid">
          <h3 class="mb-2 flex items-center gap-2 border-b border-kbd12-rule pb-2 text-[11px] font-bold uppercase tracking-[0.18em] text-kbd12-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Review</h3>
          <div class="grid">
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Add comment</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Alt</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">M</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Approve changes</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Ctrl</kbd><span class="text-[10.5px] text-kbd12-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">Enter</kbd></kbd></div>
            <div class="-mx-2 flex items-center justify-between gap-3 rounded-lg px-2 py-[7px] transition-colors hover:bg-kbd12-hover"><span class="min-w-0 text-[13.5px]">Resolve thread</span><kbd class="inline-flex flex-none flex-wrap items-center justify-end gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">R</kbd><span class="px-0.5 text-[10px] font-semibold uppercase tracking-[0.1em] text-kbd12-acc">then</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd12-rim bg-kbd12-cap px-1.5 font-kbd12-mono text-[11.5px] font-medium leading-none text-kbd12-capink shadow-[0_1px_0_var(--color-kbd12-edge)] print:shadow-none">T</kbd></kbd></div>
          </div>
        </section>
        </div>
        <footer class="mt-8 border-t border-kbd12-rule pt-4 font-kbd12-mono text-[11.5px] text-kbd12-mut">Keys align to one right edge in every group · prints clean on A4 and Letter</footer>
      </section>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-12-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-12-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd12-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd12-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd12-dark:bg-transparent kbd12-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd12-dark:hidden">Light</span><span class="hidden kbd12-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd12-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-12:not(:has(#kbd-12-theme:checked)), .kbd-12:not(:has(#kbd-12-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-12:has(#kbd-12-theme:checked), .kbd-12:has(#kbd-12-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd12-bg: light-dark(#f4f2ec, #0e0e0c);
  --color-kbd12-bg: light-dark(oklch(0.961 0.008 91.5), oklch(0.163 0.004 106.8));
  --color-kbd12-panel: light-dark(#fffefb, #171714);
  --color-kbd12-panel: light-dark(oklch(0.997 0.004 91.4), oklch(0.203 0.006 106.9));
  --color-kbd12-shade: light-dark(#3b301a40, #000000b3);
  --color-kbd12-shade: light-dark(oklch(0.315 0.039 83.7 / 0.25), oklch(0 0 0 / 0.7));
  --color-kbd12-hover: light-dark(#f4f1e8, #201f1b);
  --color-kbd12-hover: light-dark(oklch(0.958 0.012 91.5), oklch(0.239 0.008 95.4));
  --color-kbd12-ink: light-dark(#1c1b17, #efede6);
  --color-kbd12-ink: light-dark(oklch(0.222 0.008 95.4), oklch(0.946 0.01 93.6));
  --color-kbd12-mut: light-dark(#5f5b51, #a5a195);
  --color-kbd12-mut: light-dark(oklch(0.472 0.016 88.8), oklch(0.709 0.018 91.6));
  --color-kbd12-rule: light-dark(#e6e2d6, #2b2a25);
  --color-kbd12-rule: light-dark(oklch(0.913 0.017 91.6), oklch(0.284 0.009 97.7));
  --color-kbd12-cap: light-dark(#ffffff, #24231f);
  --color-kbd12-cap: light-dark(oklch(1 0 0), oklch(0.256 0.007 95.4));
  --color-kbd12-rim: light-dark(#d3cebf, #3f3d36);
  --color-kbd12-rim: light-dark(oklch(0.851 0.021 91.6), oklch(0.36 0.012 93.8));
  --color-kbd12-edge: light-dark(#b8b2a2, #060605);
  --color-kbd12-edge: light-dark(oklch(0.764 0.023 89.8), oklch(0.121 0.003 106.9));
  --color-kbd12-capink: light-dark(#2b2924, #ebe8df);
  --color-kbd12-capink: light-dark(oklch(0.281 0.009 88.8), oklch(0.931 0.012 91.5));
  --color-kbd12-acc: light-dark(#b4361f, #ff8a6b);
  --color-kbd12-acc: light-dark(oklch(0.518 0.166 32.6), oklch(0.756 0.149 35.8));
  --font-kbd12-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-kbd12-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-12 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
