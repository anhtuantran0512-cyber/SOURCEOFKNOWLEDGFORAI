---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-arrow-keys-navigation-key-layout/"
title: "Tailwind Arrow Keys and Navigation Key Layout"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "The inverted-T arrow cluster and the six-key navigation block, laid out on explicit grid tracks so the shape survives every viewport."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Arrow Keys and Navigation Key Layout
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-arrow-keys-navigation-key-layout/

The inverted-T arrow cluster and the six-key navigation block, laid out on explicit grid tracks so the shape survives every viewport. One [--u:clamp(…)] unit sizes every cap through size-(--u), and each arrow glyph is aria-hidden with a spoken name beside it.
## HTML
```html
<section class="kbd-07 relative w-full min-h-svh scheme-light kbd07-dark:scheme-dark bg-kbd07-bg text-kbd07-ink font-kbd07-sans" aria-label="Arrow keys and navigation glyphs demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <div class="grid w-full min-w-0 max-w-[46rem] gap-4 sm:grid-cols-2">
      <section class="grid min-w-0 content-start justify-items-center gap-5 rounded-2xl border border-kbd07-rule bg-kbd07-panel p-6 sm:p-7">
        <h2 class="justify-self-start text-[11px] font-semibold uppercase tracking-[0.2em] text-kbd07-acc">Arrow cluster</h2>
        <div class="grid grid-cols-[repeat(3,var(--u))] gap-1.5 [--u:clamp(44px,12vw,56px)]">
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] col-start-2 row-start-1 size-(--u) text-xl"><span aria-hidden="true">↑</span><span class="sr-only">Arrow up</span></kbd>
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] col-start-1 row-start-2 size-(--u) text-xl"><span aria-hidden="true">←</span><span class="sr-only">Arrow left</span></kbd>
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] col-start-2 row-start-2 size-(--u) text-xl"><span aria-hidden="true">↓</span><span class="sr-only">Arrow down</span></kbd>
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] col-start-3 row-start-2 size-(--u) text-xl"><span aria-hidden="true">→</span><span class="sr-only">Arrow right</span></kbd>
        </div>
        <p class="justify-self-start text-[13px] leading-snug text-kbd07-mut">Explicit grid tracks — the inverted T survives every viewport.</p>
      </section>
      <section class="grid min-w-0 content-start justify-items-center gap-5 rounded-2xl border border-kbd07-rule bg-kbd07-panel p-6 sm:p-7">
        <h2 class="justify-self-start text-[11px] font-semibold uppercase tracking-[0.2em] text-kbd07-acc">Navigation</h2>
        <div class="grid w-full max-w-[15rem] grid-cols-3 gap-1.5 [--u:clamp(44px,12vw,52px)]">
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] h-(--u) min-w-0 px-2 text-[13px] leading-tight">Insert</kbd>
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] h-(--u) min-w-0 px-2 text-[13px] leading-tight">Home</kbd>
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] h-(--u) min-w-0 px-2 text-[13px] leading-tight">Page <span aria-hidden="true">↑</span><span class="sr-only">up</span></kbd>
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] h-(--u) min-w-0 px-2 text-[13px] leading-tight">Delete</kbd>
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] h-(--u) min-w-0 px-2 text-[13px] leading-tight">End</kbd>
          <kbd class="grid place-items-center rounded-[10px] border border-kbd07-rim bg-linear-to-b from-kbd07-top to-kbd07-cap font-kbd07-sans font-semibold text-kbd07-capink shadow-[0_2px_0_var(--color-kbd07-edge),0_6px_12px_-6px_var(--color-kbd07-shade)] h-(--u) min-w-0 px-2 text-[13px] leading-tight">Page <span aria-hidden="true">↓</span><span class="sr-only">down</span></kbd>
        </div>
        <p class="justify-self-start text-[13px] leading-snug text-kbd07-mut">Word labels get their own grid, in the order they sit on a full-size board.</p>
      </section>
    </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-07-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-07-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd07-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd07-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd07-dark:bg-transparent kbd07-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd07-dark:hidden">Light</span><span class="hidden kbd07-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd07-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-07:not(:has(#kbd-07-theme:checked)), .kbd-07:not(:has(#kbd-07-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-07:has(#kbd-07-theme:checked), .kbd-07:has(#kbd-07-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd07-bg: light-dark(#edf3f0, #0d1412);
  --color-kbd07-bg: light-dark(oklch(0.959 0.007 164.9), oklch(0.183 0.011 175.6));
  --color-kbd07-panel: light-dark(#ffffff, #141d1a);
  --color-kbd07-panel: light-dark(oklch(1 0 0), oklch(0.221 0.014 172.5));
  --color-kbd07-shade: light-dark(#0d2a2033, #00000099);
  --color-kbd07-shade: light-dark(oklch(0.259 0.04 167.8 / 0.2), oklch(0 0 0 / 0.6));
  --color-kbd07-ink: light-dark(#13201c, #e3eeea);
  --color-kbd07-ink: light-dark(oklch(0.23 0.02 173.3), oklch(0.94 0.013 172.4));
  --color-kbd07-mut: light-dark(#4f615b, #94a9a1);
  --color-kbd07-mut: light-dark(oklch(0.476 0.024 173), oklch(0.716 0.026 170.6));
  --color-kbd07-rule: light-dark(#dce6e1, #22302b);
  --color-kbd07-rule: light-dark(oklch(0.916 0.013 164.8), oklch(0.295 0.021 170.9));
  --color-kbd07-cap: light-dark(#f6faf8, #1d2925);
  --color-kbd07-cap: light-dark(oklch(0.982 0.005 165), oklch(0.268 0.018 172.4));
  --color-kbd07-top: light-dark(#ffffff, #26342f);
  --color-kbd07-top: light-dark(oklch(1 0 0), oklch(0.311 0.021 171));
  --color-kbd07-rim: light-dark(#c3d2cc, #34453f);
  --color-kbd07-rim: light-dark(oklch(0.851 0.018 170), oklch(0.374 0.024 171.4));
  --color-kbd07-edge: light-dark(#a6b8b1, #040706);
  --color-kbd07-edge: light-dark(oklch(0.767 0.022 170.4), oklch(0.123 0.008 174.7));
  --color-kbd07-capink: light-dark(#17241f, #e2ede9);
  --color-kbd07-capink: light-dark(oklch(0.246 0.02 168.8), oklch(0.937 0.013 172.4));
  --color-kbd07-acc: light-dark(#0b7a5d, #4fd1a8);
  --color-kbd07-acc: light-dark(oklch(0.516 0.101 168.4), oklch(0.778 0.129 168.7));
  --font-kbd07-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-07 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
