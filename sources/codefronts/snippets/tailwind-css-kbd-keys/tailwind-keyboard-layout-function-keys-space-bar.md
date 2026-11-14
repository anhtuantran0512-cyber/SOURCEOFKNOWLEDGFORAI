---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-keyboard-layout-function-keys-space-bar/"
title: "Tailwind Keyboard Layout with Function Keys and Space Bar"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "A real keyboard's geometry in utilities: one unit [--u:clamp(26px,7vw,46px)] and per-key multipliers — w-[calc(var(--u)*2.25)] for Shift, *6.25 for Space —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Keyboard Layout with Function Keys and Space Bar
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-keyboard-layout-function-keys-space-bar/

A real keyboard's geometry in utilities: one unit [--u:clamp(26px,7vw,46px)] and per-key multipliers — w-[calc(var(--u)*2.25)] for Shift, *6.25 for Space — so proportions match a physical board at every size. The function row is grouped Esc · F1–F4 · F5–F8 · F9–F12 like the hardware, and wraps by group on phones.
## HTML
```html
<section class="kbd-09 relative w-full min-h-svh scheme-light kbd09-dark:scheme-dark bg-kbd09-bg text-kbd09-ink font-kbd09-sans" aria-label="Function keys and wide space bar demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[48rem] rounded-[22px] border border-kbd09-rule bg-kbd09-board p-[clamp(14px,3vw,26px)] shadow-[inset_0_1px_0_var(--color-kbd09-shine),0_24px_48px_-24px_var(--color-kbd09-shade)] [--u:clamp(26px,7vw,46px)]">
        <p class="mb-3 font-kbd09-mono text-[10.5px] font-semibold uppercase tracking-[0.2em] text-kbd09-mut">Function row · 1u each · grouped like the hardware</p>
        <div class="flex flex-wrap gap-x-[calc(var(--u)*0.5)] gap-y-1.5">
          <div class="flex gap-1"><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-accrim bg-kbd09-acc text-kbd09-accink shadow-[inset_0_-3px_0_var(--color-kbd09-acclip),0_2px_0_var(--color-kbd09-edge)] w-(--u) place-items-center">Esc</kbd></div><div class="flex gap-1"><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F1</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F2</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F3</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F4</kbd></div><div class="flex gap-1"><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F5</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F6</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F7</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F8</kbd></div><div class="flex gap-1"><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F9</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F10</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F11</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-(--u) place-items-center">F12</kbd></div>
        </div>
        <p class="mt-6 mb-3 font-kbd09-mono text-[10.5px] font-semibold uppercase tracking-[0.2em] text-kbd09-mut">Wide caps · width = unit × multiplier</p>
        <div class="grid gap-1.5">
          <div class="flex flex-wrap gap-1"><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-[calc(var(--u)*1.5)] items-end justify-items-start pb-[calc(var(--u)*0.2)]">Tab</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-[calc(var(--u)*2)] items-end justify-items-start pb-[calc(var(--u)*0.2)]">Backspace</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-[calc(var(--u)*2.25)] items-end justify-items-start pb-[calc(var(--u)*0.2)]">Shift</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-accrim bg-kbd09-acc text-kbd09-accink shadow-[inset_0_-3px_0_var(--color-kbd09-acclip),0_2px_0_var(--color-kbd09-edge)] w-[calc(var(--u)*1.75)] items-end justify-items-start pb-[calc(var(--u)*0.2)]">Enter</kbd></div>
          <div class="flex flex-wrap gap-1"><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-[calc(var(--u)*1.25)] items-end justify-items-start pb-[calc(var(--u)*0.2)]">Ctrl</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-[calc(var(--u)*1.25)] items-end justify-items-start pb-[calc(var(--u)*0.2)]">Alt</kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-[calc(var(--u)*6.25)] place-items-center"><span class="sr-only">Space</span></kbd><kbd class="grid h-(--u) min-w-0 rounded-[calc(var(--u)*0.18)] border px-[calc(var(--u)*0.16)] font-kbd09-sans text-[clamp(9.5px,calc(var(--u)*0.27),12.5px)] font-semibold leading-none shadow-[inset_0_-3px_0_var(--color-kbd09-lip),0_2px_0_var(--color-kbd09-edge)] border-kbd09-rim bg-kbd09-cap text-kbd09-capink w-[calc(var(--u)*1.25)] items-end justify-items-start pb-[calc(var(--u)*0.2)]">Alt</kbd></div>
        </div>
        <dl class="mt-6 grid gap-x-6 gap-y-1.5 border-t border-kbd09-rule pt-4 sm:grid-cols-2">
          <div class="flex items-baseline gap-2.5"><dt class="w-12 flex-none font-kbd09-mono text-[12px] font-semibold text-kbd09-acc">1u</dt><dd class="min-w-0 text-[13px] text-kbd09-mut">letter, digit, function key</dd></div>
          <div class="flex items-baseline gap-2.5"><dt class="w-12 flex-none font-kbd09-mono text-[12px] font-semibold text-kbd09-acc">1.5u</dt><dd class="min-w-0 text-[13px] text-kbd09-mut">Tab</dd></div>
          <div class="flex items-baseline gap-2.5"><dt class="w-12 flex-none font-kbd09-mono text-[12px] font-semibold text-kbd09-acc">2.25u</dt><dd class="min-w-0 text-[13px] text-kbd09-mut">left Shift</dd></div>
          <div class="flex items-baseline gap-2.5"><dt class="w-12 flex-none font-kbd09-mono text-[12px] font-semibold text-kbd09-acc">6.25u</dt><dd class="min-w-0 text-[13px] text-kbd09-mut">Space bar</dd></div>
        </dl>
      </section>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-09-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-09-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd09-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd09-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd09-dark:bg-transparent kbd09-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd09-dark:hidden">Light</span><span class="hidden kbd09-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd09-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-09:not(:has(#kbd-09-theme:checked)), .kbd-09:not(:has(#kbd-09-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-09:has(#kbd-09-theme:checked), .kbd-09:has(#kbd-09-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd09-bg: light-dark(#e4e0d6, #0b0c0e);
  --color-kbd09-bg: light-dark(oklch(0.907 0.014 88.7), oklch(0.154 0.005 264.4));
  --color-kbd09-board: light-dark(#d3cec2, #17181b);
  --color-kbd09-board: light-dark(oklch(0.852 0.017 88), oklch(0.209 0.006 271.1));
  --color-kbd09-shine: light-dark(#f2efe8, #2a2c31);
  --color-kbd09-shine: light-dark(oklch(0.953 0.01 87.5), oklch(0.293 0.01 268.3));
  --color-kbd09-shade: light-dark(#3b33264d, #000000b3);
  --color-kbd09-shade: light-dark(oklch(0.326 0.025 79.7 / 0.3), oklch(0 0 0 / 0.7));
  --color-kbd09-ink: light-dark(#211e18, #e9eaec);
  --color-kbd09-ink: light-dark(oklch(0.236 0.012 84.6), oklch(0.937 0.003 264.5));
  --color-kbd09-mut: light-dark(#59534a, #9a9ea6);
  --color-kbd09-mut: light-dark(oklch(0.445 0.016 78.1), oklch(0.699 0.013 264.5));
  --color-kbd09-rule: light-dark(#bfb8aa, #2a2c31);
  --color-kbd09-rule: light-dark(oklch(0.784 0.021 84.6), oklch(0.293 0.01 268.3));
  --color-kbd09-cap: light-dark(#f4f1ea, #26282d);
  --color-kbd09-cap: light-dark(oklch(0.959 0.01 87.5), oklch(0.277 0.01 268.3));
  --color-kbd09-rim: light-dark(#b9b2a3, #3a3d44);
  --color-kbd09-rim: light-dark(oklch(0.765 0.022 86), oklch(0.36 0.013 267.2));
  --color-kbd09-lip: light-dark(#d9d3c6, #1c1e22);
  --color-kbd09-lip: light-dark(oklch(0.868 0.019 86.2), oklch(0.235 0.008 264.4));
  --color-kbd09-edge: light-dark(#9c9483, #050506);
  --color-kbd09-edge: light-dark(oklch(0.669 0.026 85.8), oklch(0.116 0.003 285.9));
  --color-kbd09-capink: light-dark(#2a2620, #e6e8eb);
  --color-kbd09-capink: light-dark(oklch(0.271 0.012 78.1), oklch(0.93 0.005 258.3));
  --color-kbd09-acc: light-dark(#e0612b, #ef7a3f);
  --color-kbd09-acc: light-dark(oklch(0.644 0.172 41.3), oklch(0.704 0.161 45.3));
  --color-kbd09-accrim: light-dark(#b44a1e, #b9551f);
  --color-kbd09-accrim: light-dark(oklch(0.543 0.149 40.7), oklch(0.567 0.144 45.2));
  --color-kbd09-acclip: light-dark(#bc4f20, #c45a22);
  --color-kbd09-acclip: light-dark(oklch(0.563 0.152 41.3), oklch(0.591 0.151 44.8));
  --color-kbd09-accink: light-dark(#ffffff, #ffffff);
  --color-kbd09-accink: light-dark(oklch(1 0 0), oklch(1 0 0));
  --font-kbd09-sans: 'Chakra Petch', system-ui, sans-serif;
  --font-kbd09-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-09 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
