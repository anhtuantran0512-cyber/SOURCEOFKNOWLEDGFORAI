---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-keyboard-shortcut-settings-table/"
title: "Tailwind Keyboard Shortcut Settings Table"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "An app's keybinding settings as a real data table — <caption>, scoped headers, status pills and per-row Reset buttons with sr-only context."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Keyboard Shortcut Settings Table
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-keyboard-shortcut-settings-table/

An app's keybinding settings as a real data table — <caption>, scoped headers, status pills and per-row Reset buttons with sr-only context. On narrow screens the table scrolls inside its own container while the Action column stays pinned with sticky left-0, and the conflicting binding is flagged with colour, an icon, a text explanation and an inset accent bar.
## HTML
```html
<section class="kbd-14 relative w-full min-h-svh scheme-light kbd14-dark:scheme-dark bg-kbd14-bg text-kbd14-ink font-kbd14-sans" aria-label="Settings shortcut mapping table demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[52rem] rounded-2xl border border-kbd14-rule bg-kbd14-panel p-5 shadow-[0_20px_50px_-28px_var(--color-kbd14-shade)] sm:p-7">
        <header class="mb-5 flex flex-wrap items-end justify-between gap-2">
          <div><p class="text-[11px] font-semibold uppercase tracking-[0.18em] text-kbd14-acc">Settings · Shortcuts</p><h2 class="mt-1 text-2xl font-semibold tracking-tight">Keyboard</h2></div>
          <p class="text-[13px] text-kbd14-mut">6 of 214 bindings customised</p>
        </header>
        <div class="overflow-x-auto rounded-xl border border-kbd14-rule [scrollbar-width:thin]">
          <table class="w-full min-w-[40rem] border-collapse">
            <caption class="sr-only">Shortcut bindings for Atlas editor. One binding conflicts and is flagged in the Status column.</caption>
            <thead class="bg-kbd14-head">
              <tr><th scope="col" class="sticky left-0 z-[1] bg-kbd14-head px-4 py-3 text-left text-[11px] font-semibold uppercase tracking-[0.14em] text-kbd14-mut">Action</th><th scope="col" class="px-4 py-3 text-left text-[11px] font-semibold uppercase tracking-[0.14em] text-kbd14-mut">Binding</th><th scope="col" class="px-4 py-3 text-left text-[11px] font-semibold uppercase tracking-[0.14em] text-kbd14-mut">Scope</th><th scope="col" class="px-4 py-3 text-left text-[11px] font-semibold uppercase tracking-[0.14em] text-kbd14-mut">Status</th><th scope="col" class="px-4 py-3 text-left text-[11px] font-semibold uppercase tracking-[0.14em] text-kbd14-mut"><span class="sr-only">Reset</span></th></tr>
            </thead>
            <tbody>
              <tr class="bg-kbd14-panel border-t border-kbd14-rule">
                <th scope="row" class="sticky left-0 z-[1] bg-inherit px-4 py-3 align-middle text-left text-[14px] font-medium whitespace-nowrap ">Save file</th>
                <td class="px-4 py-3 align-middle"><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">Ctrl</kbd><span class="text-[10.5px] text-kbd14-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">S</kbd></kbd></td>
                <td class="px-4 py-3 align-middle text-[13.5px] text-kbd14-mut">Global</td>
                <td class="px-4 py-3 align-middle"><span class="inline-flex items-center rounded-full bg-kbd14-chip px-2.5 py-1 text-[12px] font-medium text-kbd14-mut">Default</span></td>
                <td class="px-4 py-3 align-middle text-right"></td>
              </tr>
              <tr class="bg-kbd14-panel border-t border-kbd14-rule">
                <th scope="row" class="sticky left-0 z-[1] bg-inherit px-4 py-3 align-middle text-left text-[14px] font-medium whitespace-nowrap ">Toggle sidebar</th>
                <td class="px-4 py-3 align-middle"><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">Ctrl</kbd><span class="text-[10.5px] text-kbd14-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">Shift</kbd><span class="text-[10.5px] text-kbd14-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">E</kbd></kbd></td>
                <td class="px-4 py-3 align-middle text-[13.5px] text-kbd14-mut">Workbench</td>
                <td class="px-4 py-3 align-middle"><span class="inline-flex items-center rounded-full bg-kbd14-accbg px-2.5 py-1 text-[12px] font-semibold text-kbd14-acc">Customised</span></td>
                <td class="px-4 py-3 align-middle text-right"><button type="button" class="min-h-11 rounded-lg border border-kbd14-rim bg-kbd14-panel px-3.5 text-[13px] font-medium text-kbd14-ink transition-colors hover:border-kbd14-acc hover:text-kbd14-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-kbd14-acc">Reset<span class="sr-only"> toggle sidebar to default</span></button></td>
              </tr>
              <tr class="bg-kbd14-warnbg border-t border-kbd14-rule">
                <th scope="row" class="sticky left-0 z-[1] bg-inherit px-4 py-3 align-middle text-left text-[14px] font-medium whitespace-nowrap shadow-[inset_3px_0_0_var(--color-kbd14-warn)]">Split editor right</th>
                <td class="px-4 py-3 align-middle"><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">Ctrl</kbd><span class="text-[10.5px] text-kbd14-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">K</kbd></kbd></td>
                <td class="px-4 py-3 align-middle text-[13.5px] text-kbd14-mut">Editor</td>
                <td class="px-4 py-3 align-middle"><span class="inline-flex items-center gap-1.5 rounded-full bg-kbd14-warnchip px-2.5 py-1 text-[12px] font-semibold text-kbd14-warn"><svg class="size-3.5 fill-none stroke-current [stroke-linecap:round] [stroke-linejoin:round] [stroke-width:2.2]" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4 L21 19 L3 19 Z"/><path d="M12 10 L12 14"/><path d="M12 16.6 L12 16.7"/></svg>Conflict</span><span class="mt-1 block text-[12px] text-kbd14-warn">also bound to Open command bar</span></td>
                <td class="px-4 py-3 align-middle text-right"><button type="button" class="min-h-11 rounded-lg border border-kbd14-rim bg-kbd14-panel px-3.5 text-[13px] font-medium text-kbd14-ink transition-colors hover:border-kbd14-acc hover:text-kbd14-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-kbd14-acc">Reset<span class="sr-only"> split editor right to default</span></button></td>
              </tr>
              <tr class="bg-kbd14-panel border-t border-kbd14-rule">
                <th scope="row" class="sticky left-0 z-[1] bg-inherit px-4 py-3 align-middle text-left text-[14px] font-medium whitespace-nowrap ">Go to file</th>
                <td class="px-4 py-3 align-middle"><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">Ctrl</kbd><span class="text-[10.5px] text-kbd14-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">P</kbd></kbd></td>
                <td class="px-4 py-3 align-middle text-[13.5px] text-kbd14-mut">Global</td>
                <td class="px-4 py-3 align-middle"><span class="inline-flex items-center rounded-full bg-kbd14-chip px-2.5 py-1 text-[12px] font-medium text-kbd14-mut">Default</span></td>
                <td class="px-4 py-3 align-middle text-right"></td>
              </tr>
              <tr class="bg-kbd14-panel border-t border-kbd14-rule">
                <th scope="row" class="sticky left-0 z-[1] bg-inherit px-4 py-3 align-middle text-left text-[14px] font-medium whitespace-nowrap ">Rename symbol</th>
                <td class="px-4 py-3 align-middle"><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd14-rim bg-kbd14-cap px-1.5 font-kbd14-mono text-[11.5px] font-medium leading-none text-kbd14-capink shadow-[0_1px_0_var(--color-kbd14-edge)]">F2</kbd></kbd></td>
                <td class="px-4 py-3 align-middle text-[13.5px] text-kbd14-mut">Editor</td>
                <td class="px-4 py-3 align-middle"><span class="inline-flex items-center rounded-full bg-kbd14-chip px-2.5 py-1 text-[12px] font-medium text-kbd14-mut">Default</span></td>
                <td class="px-4 py-3 align-middle text-right"></td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="mt-4 text-[12.5px] text-kbd14-mut">Reviewed by Priya Sharma · scroll sideways on small screens — the Action column stays pinned</p>
      </section>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-14-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-14-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd14-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd14-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd14-dark:bg-transparent kbd14-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd14-dark:hidden">Light</span><span class="hidden kbd14-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd14-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-14:not(:has(#kbd-14-theme:checked)), .kbd-14:not(:has(#kbd-14-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-14:has(#kbd-14-theme:checked), .kbd-14:has(#kbd-14-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd14-bg: light-dark(#eff1f4, #0c0e11);
  --color-kbd14-bg: light-dark(oklch(0.957 0.005 258.3), oklch(0.163 0.007 258.4));
  --color-kbd14-panel: light-dark(#ffffff, #15181d);
  --color-kbd14-panel: light-dark(oklch(1 0 0), oklch(0.208 0.011 260.7));
  --color-kbd14-head: light-dark(#f6f7f9, #1a1e24);
  --color-kbd14-head: light-dark(oklch(0.976 0.003 264.5), oklch(0.234 0.013 258.4));
  --color-kbd14-shade: light-dark(#10203433, #000000b3);
  --color-kbd14-shade: light-dark(oklch(0.241 0.044 254.8 / 0.2), oklch(0 0 0 / 0.7));
  --color-kbd14-ink: light-dark(#14171c, #e9ecf0);
  --color-kbd14-ink: light-dark(oklch(0.204 0.011 260.7), oklch(0.942 0.006 255.5));
  --color-kbd14-mut: light-dark(#576070, #9aa3b1);
  --color-kbd14-mut: light-dark(oklch(0.487 0.028 262), oklch(0.713 0.023 259.2));
  --color-kbd14-rule: light-dark(#e3e6eb, #262a31);
  --color-kbd14-rule: light-dark(oklch(0.924 0.008 260.7), oklch(0.284 0.014 261.7));
  --color-kbd14-chip: light-dark(#eef0f3, #21252c);
  --color-kbd14-chip: light-dark(oklch(0.954 0.005 258.3), oklch(0.263 0.014 261.7));
  --color-kbd14-cap: light-dark(#f7f8fa, #1f232a);
  --color-kbd14-cap: light-dark(oklch(0.979 0.003 264.5), oklch(0.255 0.014 261.7));
  --color-kbd14-rim: light-dark(#cdd2da, #3a404a);
  --color-kbd14-rim: light-dark(oklch(0.862 0.012 259.8), oklch(0.37 0.019 260.7));
  --color-kbd14-edge: light-dark(#b4bac4, #050608);
  --color-kbd14-edge: light-dark(oklch(0.787 0.016 260.7), oklch(0.122 0.006 261.6));
  --color-kbd14-capink: light-dark(#1e232a, #e4e8ee);
  --color-kbd14-capink: light-dark(oklch(0.254 0.015 256.8), oklch(0.93 0.009 258.3));
  --color-kbd14-acc: light-dark(#1d5fd1, #78a6ff);
  --color-kbd14-acc: light-dark(oklch(0.515 0.188 260.8), oklch(0.73 0.139 262.7));
  --color-kbd14-accbg: light-dark(#e8effc, #1a2741);
  --color-kbd14-accbg: light-dark(oklch(0.951 0.019 263), oklch(0.275 0.052 263.2));
  --color-kbd14-warn: light-dark(#a63a00, #ffae7a);
  --color-kbd14-warn: light-dark(oklch(0.497 0.153 41), oklch(0.818 0.117 53.1));
  --color-kbd14-warnbg: light-dark(#fff6ef, #24180f);
  --color-kbd14-warnbg: light-dark(oklch(0.978 0.013 60.6), oklch(0.222 0.025 57.8));
  --color-kbd14-warnchip: light-dark(#ffe8d6, #3a2414);
  --color-kbd14-warnchip: light-dark(oklch(0.945 0.035 60.4), oklch(0.284 0.043 56));
  --font-kbd14-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-kbd14-mono: 'IBM Plex Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-14 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
