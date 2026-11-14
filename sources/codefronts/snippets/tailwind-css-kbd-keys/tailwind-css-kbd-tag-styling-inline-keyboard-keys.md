---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-css-kbd-tag-styling-inline-keyboard-keys/"
title: "Tailwind CSS Kbd Tag Styling for Inline Keyboard Keys"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "The reference keycap the whole collection builds on: a real <kbd> styled entirely in utilities so it sits inside documentation prose without disturbing the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Kbd Tag Styling for Inline Keyboard Keys
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-css-kbd-tag-styling-inline-keyboard-keys/

The reference keycap the whole collection builds on: a real <kbd> styled entirely in utilities so it sits inside documentation prose without disturbing the line it lives on. A hairline border-kbd01-rim plus a one-pixel shadow-[0_1px_0_…] edge reads as depth, every dimension is in em so the cap tracks the text, and leading-none keeps the line box intact.
## HTML
```html
<section class="kbd-01 relative w-full min-h-svh scheme-light kbd01-dark:scheme-dark bg-kbd01-bg bg-[radial-gradient(110%_80%_at_50%_0%,var(--color-kbd01-glow),transparent_70%)] text-kbd01-ink" aria-label="Inline kbd tag styling demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <article class="w-full min-w-0 max-w-[34rem]">
      <p class="mb-2.5 font-kbd01-key text-[10px] font-semibold uppercase leading-none tracking-[0.24em] text-kbd01-acc">Editor · Keyboard</p>
      <h2 class="mb-5 font-kbd01-serif text-[clamp(28px,5.2vw,38px)] leading-[1.1] tracking-[-0.015em] text-balance">Saving, undoing, escaping</h2>
      <p class="mb-4 font-kbd01-serif text-[clamp(16px,3.4vw,18px)] leading-[1.75] text-pretty">Your work is written to disk the moment you press <kbd class="inline-block min-w-[1.1em] rounded-[0.32em] border border-kbd01-rim bg-kbd01-cap px-[0.55em] py-[0.28em] text-center align-[0.06em] font-kbd01-key text-[max(0.82em,11px)] font-semibold leading-none whitespace-nowrap text-kbd01-capink shadow-[0_1px_0_var(--color-kbd01-edge)]">Ctrl</kbd> <span class="px-[0.05em] font-kbd01-key text-[0.78em] text-kbd01-mut">+</span> <kbd class="inline-block min-w-[1.1em] rounded-[0.32em] border border-kbd01-rim bg-kbd01-cap px-[0.55em] py-[0.28em] text-center align-[0.06em] font-kbd01-key text-[max(0.82em,11px)] font-semibold leading-none whitespace-nowrap text-kbd01-capink shadow-[0_1px_0_var(--color-kbd01-edge)]">S</kbd>, and there is no separate confirm step. If an edit turns out wrong, <kbd class="inline-block min-w-[1.1em] rounded-[0.32em] border border-kbd01-rim bg-kbd01-cap px-[0.55em] py-[0.28em] text-center align-[0.06em] font-kbd01-key text-[max(0.82em,11px)] font-semibold leading-none whitespace-nowrap text-kbd01-capink shadow-[0_1px_0_var(--color-kbd01-edge)]">Ctrl</kbd> <span class="px-[0.05em] font-kbd01-key text-[0.78em] text-kbd01-mut">+</span> <kbd class="inline-block min-w-[1.1em] rounded-[0.32em] border border-kbd01-rim bg-kbd01-cap px-[0.55em] py-[0.28em] text-center align-[0.06em] font-kbd01-key text-[max(0.82em,11px)] font-semibold leading-none whitespace-nowrap text-kbd01-capink shadow-[0_1px_0_var(--color-kbd01-edge)]">Z</kbd> walks back through the history one change at a time; <kbd class="inline-block min-w-[1.1em] rounded-[0.32em] border border-kbd01-rim bg-kbd01-cap px-[0.55em] py-[0.28em] text-center align-[0.06em] font-kbd01-key text-[max(0.82em,11px)] font-semibold leading-none whitespace-nowrap text-kbd01-capink shadow-[0_1px_0_var(--color-kbd01-edge)]">Esc</kbd> closes whichever panel is in the way first.</p>
      <p class="mb-4 font-kbd01-serif text-[clamp(16px,3.4vw,18px)] leading-[1.75] text-pretty">Every key above is a real <code class="rounded-[3px] bg-kbd01-code px-[0.35em] py-[0.2em] font-kbd01-mono text-[0.84em]">&lt;kbd&gt;</code> element sitting in ordinary prose. The lines stay evenly spaced because the cap carries <code class="rounded-[3px] bg-kbd01-code px-[0.35em] py-[0.2em] font-kbd01-mono text-[0.84em]">leading-none</code>, so it never inflates the line box it lives in.</p>
      <div class="mt-8 grid items-center gap-6 border-t border-kbd01-rule pt-6 sm:grid-cols-[auto_minmax(0,1fr)]">
        <span aria-hidden="true" class="grid size-24 place-items-center rounded-2xl bg-kbd01-well text-[46px]"><kbd class="inline-block min-w-[1.1em] rounded-[0.32em] border border-kbd01-rim bg-kbd01-cap px-[0.55em] py-[0.28em] text-center align-[0.06em] font-kbd01-key text-[max(0.82em,11px)] font-semibold leading-none whitespace-nowrap text-kbd01-capink shadow-[0_1px_0_var(--color-kbd01-edge)]">S</kbd></span>
        <dl class="grid gap-2.5">
        <div class="grid grid-cols-1 items-baseline gap-0.5 min-[380px]:grid-cols-[5.5rem_minmax(0,1fr)] min-[380px]:gap-3"><dt class="font-kbd01-key text-[10px] font-semibold uppercase leading-snug tracking-[0.16em] text-kbd01-mut">Border</dt><dd class="min-w-0 font-kbd01-serif text-[15px] leading-normal">One hairline, one tone darker than the cap face</dd></div>
        <div class="grid grid-cols-1 items-baseline gap-0.5 min-[380px]:grid-cols-[5.5rem_minmax(0,1fr)] min-[380px]:gap-3"><dt class="font-kbd01-key text-[10px] font-semibold uppercase leading-snug tracking-[0.16em] text-kbd01-mut">Edge</dt><dd class="min-w-0 font-kbd01-serif text-[15px] leading-normal">A single 1px bottom shadow, no blur</dd></div>
        <div class="grid grid-cols-1 items-baseline gap-0.5 min-[380px]:grid-cols-[5.5rem_minmax(0,1fr)] min-[380px]:gap-3"><dt class="font-kbd01-key text-[10px] font-semibold uppercase leading-snug tracking-[0.16em] text-kbd01-mut">Label</dt><dd class="min-w-0 font-kbd01-serif text-[15px] leading-normal">0.82em of the surrounding text, never below 11px</dd></div>
        </dl>
      </div>
    </article>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-01-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-01-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd01-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd01-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd01-dark:bg-transparent kbd01-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd01-dark:hidden">Light</span><span class="hidden kbd01-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd01-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-01:not(:has(#kbd-01-theme:checked)), .kbd-01:not(:has(#kbd-01-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-01:has(#kbd-01-theme:checked), .kbd-01:has(#kbd-01-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd01-bg: light-dark(#faf7f1, #17150f);
  --color-kbd01-bg: light-dark(oklch(0.977 0.009 84.6), oklch(0.196 0.012 91.8));
  --color-kbd01-glow: light-dark(#fffdf9, #211d15);
  --color-kbd01-glow: light-dark(oklch(0.994 0.006 84.6), oklch(0.233 0.016 84.5));
  --color-kbd01-ink: light-dark(#221e18, #f2ede1);
  --color-kbd01-ink: light-dark(oklch(0.237 0.013 78), oklch(0.947 0.017 88));
  --color-kbd01-mut: light-dark(#665d50, #a99f8e);
  --color-kbd01-mut: light-dark(oklch(0.483 0.023 77.1), oklch(0.706 0.027 81.1));
  --color-kbd01-rule: light-dark(#e2dbcd, #322d23);
  --color-kbd01-rule: light-dark(oklch(0.893 0.02 84.6), oklch(0.299 0.019 84.5));
  --color-kbd01-well: light-dark(#f1ece2, #1f1b14);
  --color-kbd01-well: light-dark(oklch(0.944 0.014 84.6), oklch(0.224 0.014 81.6));
  --color-kbd01-cap: light-dark(#ffffff, #2a251c);
  --color-kbd01-cap: light-dark(oklch(1 0 0), oklch(0.267 0.018 82.2));
  --color-kbd01-rim: light-dark(#cfc7b6, #4a4232);
  --color-kbd01-rim: light-dark(oklch(0.832 0.025 85.8), oklch(0.382 0.028 84.4));
  --color-kbd01-edge: light-dark(#bdb3a0, #0b0906);
  --color-kbd01-edge: light-dark(oklch(0.77 0.029 83.5), oklch(0.141 0.008 81.8));
  --color-kbd01-capink: light-dark(#332d24, #f6f1e5);
  --color-kbd01-capink: light-dark(oklch(0.301 0.018 77.9), oklch(0.959 0.017 88));
  --color-kbd01-code: light-dark(#eee8dc, #26221a);
  --color-kbd01-code: light-dark(oklch(0.932 0.017 84.6), oklch(0.254 0.016 84.5));
  --color-kbd01-acc: light-dark(#a14f27, #e39a6b);
  --color-kbd01-acc: light-dark(oklch(0.522 0.121 44.7), oklch(0.748 0.108 53.1));
  --font-kbd01-serif: 'Newsreader', Georgia, serif;
  --font-kbd01-key: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-kbd01-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-01 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
