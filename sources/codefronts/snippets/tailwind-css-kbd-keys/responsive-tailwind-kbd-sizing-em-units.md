---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/responsive-tailwind-kbd-sizing-em-units/"
title: "Responsive Tailwind Kbd Sizing with Em Units"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "One class list, three contexts: a 68px display headline, body copy and a caption — and the cap is correct in all of them because padding, radius, border…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Kbd Sizing with Em Units
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/responsive-tailwind-kbd-sizing-em-units/

One class list, three contexts: a 68px display headline, body copy and a caption — and the cap is correct in all of them because padding, radius, border width and even the edge shadow are authored in em. Tailwind's spacing scale is rem-based, so this is where arbitrary values earn their keep.
## HTML
```html
<section class="kbd-05 relative w-full min-h-svh scheme-light kbd05-dark:scheme-dark bg-kbd05-bg bg-[radial-gradient(90%_70%_at_80%_0%,var(--color-kbd05-glow),transparent_70%)] text-kbd05-ink" aria-label="Fluid em-based kbd sizing demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <div class="w-full min-w-0 max-w-[40rem]">
      <p class="mb-4 font-kbd05-sans text-[10.5px] font-semibold uppercase tracking-[0.24em] text-kbd05-acc">Same markup · three contexts</p>
      <h2 class="mb-6 font-kbd05-serif text-[clamp(36px,7.5vw,68px)] leading-[1.05] tracking-[-0.01em] text-balance">Press <kbd class="inline-block whitespace-nowrap rounded-[0.32em] border-[0.07em] border-kbd05-rim bg-kbd05-cap px-[0.55em] py-[0.3em] align-[0.08em] font-kbd05-sans text-[0.85em] font-semibold not-italic leading-none text-kbd05-capink shadow-[0_0.08em_0_var(--color-kbd05-edge)]">Ctrl</kbd> <span class="font-kbd05-sans text-[0.7em] text-kbd05-mut">+</span> <kbd class="inline-block whitespace-nowrap rounded-[0.32em] border-[0.07em] border-kbd05-rim bg-kbd05-cap px-[0.55em] py-[0.3em] align-[0.08em] font-kbd05-sans text-[0.85em] font-semibold not-italic leading-none text-kbd05-capink shadow-[0_0.08em_0_var(--color-kbd05-edge)]">P</kbd> to <em>jump</em></h2>
      <p class="mb-4 font-kbd05-sans text-[clamp(15px,3.2vw,17px)] leading-[1.7] text-pretty">In body copy the same cap settles down to something you can read past: <kbd class="inline-block whitespace-nowrap rounded-[0.32em] border-[0.07em] border-kbd05-rim bg-kbd05-cap px-[0.55em] py-[0.3em] align-[0.08em] font-kbd05-sans text-[0.85em] font-semibold not-italic leading-none text-kbd05-capink shadow-[0_0.08em_0_var(--color-kbd05-edge)]">Ctrl</kbd> <span class="font-kbd05-sans text-[0.7em] text-kbd05-mut">+</span> <kbd class="inline-block whitespace-nowrap rounded-[0.32em] border-[0.07em] border-kbd05-rim bg-kbd05-cap px-[0.55em] py-[0.3em] align-[0.08em] font-kbd05-sans text-[0.85em] font-semibold not-italic leading-none text-kbd05-capink shadow-[0_0.08em_0_var(--color-kbd05-edge)]">P</kbd> opens the file switcher, and <kbd class="inline-block whitespace-nowrap rounded-[0.32em] border-[0.07em] border-kbd05-rim bg-kbd05-cap px-[0.55em] py-[0.3em] align-[0.08em] font-kbd05-sans text-[0.85em] font-semibold not-italic leading-none text-kbd05-capink shadow-[0_0.08em_0_var(--color-kbd05-edge)]">Esc</kbd> closes it again.</p>
      <p class="font-kbd05-serif text-[15px] italic text-kbd05-mut">Even in a caption it stays centred and legible — <kbd class="inline-block whitespace-nowrap rounded-[0.32em] border-[0.07em] border-kbd05-rim bg-kbd05-cap px-[0.55em] py-[0.3em] align-[0.08em] font-kbd05-sans text-[0.85em] font-semibold not-italic leading-none text-kbd05-capink shadow-[0_0.08em_0_var(--color-kbd05-edge)]">Ctrl</kbd> <span class="font-kbd05-sans text-[0.7em] text-kbd05-mut">+</span> <kbd class="inline-block whitespace-nowrap rounded-[0.32em] border-[0.07em] border-kbd05-rim bg-kbd05-cap px-[0.55em] py-[0.3em] align-[0.08em] font-kbd05-sans text-[0.85em] font-semibold not-italic leading-none text-kbd05-capink shadow-[0_0.08em_0_var(--color-kbd05-edge)]">P</kbd> · figure 2</p>
      <ul class="mt-8 grid grid-cols-2 gap-2 border-t border-kbd05-rule pt-6 sm:grid-cols-4">
        <li class="grid gap-1 rounded-lg bg-kbd05-chip px-3 py-2.5"><span class="font-kbd05-sans text-[10px] font-semibold uppercase tracking-[0.16em] text-kbd05-mut">padding</span><span class="font-kbd05-mono text-[13px] text-kbd05-ink">0.3em 0.55em</span></li>
        <li class="grid gap-1 rounded-lg bg-kbd05-chip px-3 py-2.5"><span class="font-kbd05-sans text-[10px] font-semibold uppercase tracking-[0.16em] text-kbd05-mut">radius</span><span class="font-kbd05-mono text-[13px] text-kbd05-ink">0.32em</span></li>
        <li class="grid gap-1 rounded-lg bg-kbd05-chip px-3 py-2.5"><span class="font-kbd05-sans text-[10px] font-semibold uppercase tracking-[0.16em] text-kbd05-mut">border</span><span class="font-kbd05-mono text-[13px] text-kbd05-ink">0.07em</span></li>
        <li class="grid gap-1 rounded-lg bg-kbd05-chip px-3 py-2.5"><span class="font-kbd05-sans text-[10px] font-semibold uppercase tracking-[0.16em] text-kbd05-mut">label</span><span class="font-kbd05-mono text-[13px] text-kbd05-ink">0.85em</span></li>
      </ul>
    </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-05-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-05-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd05-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd05-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd05-dark:bg-transparent kbd05-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd05-dark:hidden">Light</span><span class="hidden kbd05-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd05-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-05:not(:has(#kbd-05-theme:checked)), .kbd-05:not(:has(#kbd-05-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-05:has(#kbd-05-theme:checked), .kbd-05:has(#kbd-05-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd05-bg: light-dark(#f5f2fb, #13111a);
  --color-kbd05-bg: light-dark(oklch(0.966 0.012 301.3), oklch(0.184 0.018 294.7));
  --color-kbd05-glow: light-dark(#e8e0fb, #241c3a);
  --color-kbd05-glow: light-dark(oklch(0.921 0.037 299.2), oklch(0.252 0.056 294.3));
  --color-kbd05-ink: light-dark(#1e1830, #ece8f6);
  --color-kbd05-ink: light-dark(oklch(0.229 0.046 294), oklch(0.938 0.019 299.1));
  --color-kbd05-mut: light-dark(#59506f, #a69ebc);
  --color-kbd05-mut: light-dark(oklch(0.452 0.051 297.6), oklch(0.716 0.044 297.5));
  --color-kbd05-rule: light-dark(#e0dbee, #2a2537);
  --color-kbd05-rule: light-dark(oklch(0.901 0.026 297.9), oklch(0.278 0.033 296.9));
  --color-kbd05-chip: light-dark(#ece7f8, #1d1a27);
  --color-kbd05-chip: light-dark(oklch(0.937 0.023 299.4), oklch(0.227 0.025 294.9));
  --color-kbd05-cap: light-dark(#ffffff, #26213a);
  --color-kbd05-cap: light-dark(oklch(1 0 0), oklch(0.266 0.046 292.1));
  --color-kbd05-rim: light-dark(#c9c0df, #4a4262);
  --color-kbd05-rim: light-dark(oklch(0.825 0.044 298.7), oklch(0.401 0.054 295.3));
  --color-kbd05-edge: light-dark(#ada2c8, #07060a);
  --color-kbd05-edge: light-dark(oklch(0.734 0.055 298.3), oklch(0.126 0.01 297.7));
  --color-kbd05-capink: light-dark(#2a2240, #ebe6f7);
  --color-kbd05-capink: light-dark(oklch(0.276 0.055 294.8), oklch(0.934 0.023 299.4));
  --color-kbd05-acc: light-dark(#6236b8, #b49af2);
  --color-kbd05-acc: light-dark(oklch(0.465 0.192 292.9), oklch(0.743 0.127 296.8));
  --font-kbd05-serif: 'Instrument Serif', Georgia, serif;
  --font-kbd05-sans: 'Geist', system-ui, sans-serif;
  --font-kbd05-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-05 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
