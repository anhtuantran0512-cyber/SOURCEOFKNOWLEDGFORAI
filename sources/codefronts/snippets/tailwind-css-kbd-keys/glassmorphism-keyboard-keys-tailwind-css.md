---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/glassmorphism-keyboard-keys-tailwind-css/"
title: "Glassmorphism Keyboard Keys in Tailwind CSS"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "A frosted media-player shortcut panel over a colour field: the panel and every key blur what sits behind them."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Keyboard Keys in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/glassmorphism-keyboard-keys-tailwind-css/

A frosted media-player shortcut panel over a colour field: the panel and every key blur what sits behind them. A solid, readable fill is declared first; supports-[backdrop-filter:blur(1px)]: swaps in the translucent fill and backdrop-blur-2xl only where blur actually works — so text never lands on an unblurred, busy background.
## HTML
```html
<section class="kbd-17 relative w-full min-h-svh scheme-light kbd17-dark:scheme-dark bg-kbd17-bg bg-[radial-gradient(38%_48%_at_18%_22%,var(--color-kbd17-b1),transparent_70%),radial-gradient(42%_52%_at_84%_28%,var(--color-kbd17-b2),transparent_70%),radial-gradient(55%_50%_at_50%_95%,var(--color-kbd17-b3),transparent_72%)] text-kbd17-ink font-kbd17-sans" aria-label="Glassmorphic translucent keycap demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <div class="w-full min-w-0 max-w-[26rem] rounded-3xl border border-kbd17-edge bg-kbd17-panel p-6 shadow-[inset_0_1px_0_var(--color-kbd17-shine),0_30px_60px_-30px_var(--color-kbd17-shade)] supports-[backdrop-filter:blur(1px)]:bg-kbd17-glass supports-[backdrop-filter:blur(1px)]:backdrop-blur-2xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-150 sm:p-7">
        <p class="mb-2 text-[11px] font-semibold uppercase tracking-[0.22em] text-kbd17-mut">Now playing · shortcuts</p>
        <div>
          <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd17-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Play or pause</span><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-lg border border-kbd17-edge bg-kbd17-keyfill px-2 text-[13px] font-semibold leading-none text-kbd17-ink shadow-[inset_0_1px_0_var(--color-kbd17-shine),0_4px_12px_-4px_var(--color-kbd17-shade)] supports-[backdrop-filter:blur(1px)]:bg-kbd17-keyglass supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><span class="px-5">Space</span></kbd></kbd></div>
          <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd17-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Next track</span><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-lg border border-kbd17-edge bg-kbd17-keyfill px-2 text-[13px] font-semibold leading-none text-kbd17-ink shadow-[inset_0_1px_0_var(--color-kbd17-shine),0_4px_12px_-4px_var(--color-kbd17-shade)] supports-[backdrop-filter:blur(1px)]:bg-kbd17-keyglass supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><span aria-hidden="true">⌘</span><span class="sr-only">Command</span></kbd><span class="text-[11px] text-kbd17-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-lg border border-kbd17-edge bg-kbd17-keyfill px-2 text-[13px] font-semibold leading-none text-kbd17-ink shadow-[inset_0_1px_0_var(--color-kbd17-shine),0_4px_12px_-4px_var(--color-kbd17-shade)] supports-[backdrop-filter:blur(1px)]:bg-kbd17-keyglass supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><span aria-hidden="true">→</span><span class="sr-only">Right arrow</span></kbd></kbd></div>
          <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd17-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Volume up</span><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-lg border border-kbd17-edge bg-kbd17-keyfill px-2 text-[13px] font-semibold leading-none text-kbd17-ink shadow-[inset_0_1px_0_var(--color-kbd17-shine),0_4px_12px_-4px_var(--color-kbd17-shade)] supports-[backdrop-filter:blur(1px)]:bg-kbd17-keyglass supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><span aria-hidden="true">⌥</span><span class="sr-only">Option</span></kbd><span class="text-[11px] text-kbd17-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-lg border border-kbd17-edge bg-kbd17-keyfill px-2 text-[13px] font-semibold leading-none text-kbd17-ink shadow-[inset_0_1px_0_var(--color-kbd17-shine),0_4px_12px_-4px_var(--color-kbd17-shade)] supports-[backdrop-filter:blur(1px)]:bg-kbd17-keyglass supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><span aria-hidden="true">↑</span><span class="sr-only">Up arrow</span></kbd></kbd></div>
          <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-b border-kbd17-rule py-3 last:border-0"><span class="min-w-0 text-[14.5px]">Shuffle queue</span><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-lg border border-kbd17-edge bg-kbd17-keyfill px-2 text-[13px] font-semibold leading-none text-kbd17-ink shadow-[inset_0_1px_0_var(--color-kbd17-shine),0_4px_12px_-4px_var(--color-kbd17-shade)] supports-[backdrop-filter:blur(1px)]:bg-kbd17-keyglass supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><span aria-hidden="true">⇧</span><span class="sr-only">Shift</span></kbd><span class="text-[11px] text-kbd17-mut" aria-hidden="true">+</span><kbd class="inline-flex h-8 min-w-8 items-center justify-center rounded-lg border border-kbd17-edge bg-kbd17-keyfill px-2 text-[13px] font-semibold leading-none text-kbd17-ink shadow-[inset_0_1px_0_var(--color-kbd17-shine),0_4px_12px_-4px_var(--color-kbd17-shade)] supports-[backdrop-filter:blur(1px)]:bg-kbd17-keyglass supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">S</kbd></kbd></div>
        </div>
        <p class="mt-3 text-[12px] text-kbd17-mut">Solid fill declared first · blur added behind <code class="font-mono">@supports</code></p>
      </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-17-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-17-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd17-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd17-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd17-dark:bg-transparent kbd17-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd17-dark:hidden">Light</span><span class="hidden kbd17-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd17-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-17:not(:has(#kbd-17-theme:checked)), .kbd-17:not(:has(#kbd-17-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-17:has(#kbd-17-theme:checked), .kbd-17:has(#kbd-17-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd17-bg: light-dark(#f3eefb, #0b0a14);
  --color-kbd17-bg: light-dark(oklch(0.957 0.018 303.4), oklch(0.152 0.021 288.2));
  --color-kbd17-b1: light-dark(#ff8fb1, #7a1d4d);
  --color-kbd17-b1: light-dark(oklch(0.779 0.139 1.4), oklch(0.399 0.135 353.5));
  --color-kbd17-b2: light-dark(#7cc4ff, #11407a);
  --color-kbd17-b2: light-dark(oklch(0.796 0.111 244.6), oklch(0.375 0.111 256.1));
  --color-kbd17-b3: light-dark(#ffd27a, #5a3a0c);
  --color-kbd17-b3: light-dark(oklch(0.885 0.118 82.9), oklch(0.378 0.074 70.8));
  --color-kbd17-panel: light-dark(#fbf9ff, #1a1826);
  --color-kbd17-panel: light-dark(oklch(0.985 0.008 301.4), oklch(0.218 0.027 290.5));
  --color-kbd17-glass: light-dark(#ffffff8c, #1c1a2b8c);
  --color-kbd17-glass: light-dark(oklch(1 0 0 / 0.55), oklch(0.229 0.033 288.9 / 0.55));
  --color-kbd17-keyfill: light-dark(#ffffff, #2a2840);
  --color-kbd17-keyfill: light-dark(oklch(1 0 0), oklch(0.291 0.043 287.2));
  --color-kbd17-keyglass: light-dark(#ffffffb3, #ffffff1f);
  --color-kbd17-keyglass: light-dark(oklch(1 0 0 / 0.7), oklch(1 0 0 / 0.12));
  --color-kbd17-edge: light-dark(#ffffffb3, #ffffff26);
  --color-kbd17-edge: light-dark(oklch(1 0 0 / 0.7), oklch(1 0 0 / 0.15));
  --color-kbd17-shine: light-dark(#ffffffe6, #ffffff33);
  --color-kbd17-shine: light-dark(oklch(1 0 0 / 0.9), oklch(1 0 0 / 0.2));
  --color-kbd17-shade: light-dark(#3b1d5c40, #000000b3);
  --color-kbd17-shade: light-dark(oklch(0.308 0.109 302.3 / 0.25), oklch(0 0 0 / 0.7));
  --color-kbd17-rule: light-dark(#1a103014, #ffffff1a);
  --color-kbd17-rule: light-dark(oklch(0.206 0.061 294.9 / 0.08), oklch(1 0 0 / 0.1));
  --color-kbd17-ink: light-dark(#1d1530, #f3f0fb);
  --color-kbd17-ink: light-dark(oklch(0.221 0.052 295.5), oklch(0.961 0.015 298.6));
  --color-kbd17-mut: light-dark(#4e4565, #bdb6cf);
  --color-kbd17-mut: light-dark(oklch(0.413 0.054 296.9), oklch(0.79 0.036 298.4));
  --color-kbd17-acc: light-dark(#7c3aed, #c4a6ff);
  --color-kbd17-acc: light-dark(oklch(0.541 0.247 293), oklch(0.784 0.127 298.9));
  --font-kbd17-sans: 'Sora', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-17 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
