---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/flat-minimalist-tailwind-kbd-key-body-text/"
title: "Flat Minimalist Tailwind Kbd Key for Body Text"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "For prose that mentions a dozen keys, the raised cap gets noisy."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flat Minimalist Tailwind Kbd Key for Body Text
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/flat-minimalist-tailwind-kbd-key-body-text/

For prose that mentions a dozen keys, the raised cap gets noisy. This flat treatment is a tinted chip — no border, no edge — with a faint inset ring-kbd04-rim/50 so it stays perceivable on any surface. Side-by-side cards compare it to the raised cap so the reader can see which to reach for.
## HTML
```html
<section class="kbd-04 relative w-full min-h-svh scheme-light kbd04-dark:scheme-dark bg-kbd04-bg text-kbd04-ink" aria-label="Flat minimalist kbd key demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <article class="w-full min-w-0 max-w-[36rem]">
      <h2 class="mb-4 font-kbd04-serif text-[clamp(26px,5vw,34px)] font-semibold leading-tight tracking-[-0.01em]">Selection and navigation</h2>
      <p class="mb-4 font-kbd04-serif text-[clamp(16px,3.4vw,18px)] leading-[1.75] text-pretty">Hold <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">Shift</kbd> and use the arrow keys to grow the selection by one character, or add <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">Alt</kbd> to grow it by one word. <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">Home</kbd> and <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">End</kbd> jump to the ends of the visual line; add <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">Ctrl</kbd> to jump to the ends of the document instead. Numbered tabs respond to <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">Ctrl</kbd> plus <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">1</kbd> through <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">9</kbd>, and <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">Ctrl</kbd> plus <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">0</kbd> returns to the last one you looked at.</p>
      <p class="mb-7 font-kbd04-serif text-[clamp(16px,3.4vw,18px)] italic leading-[1.75] text-kbd04-mut">Twelve keys in two paragraphs, and the page still reads as prose. That is the argument for the flat treatment.</p>
      <div class="grid gap-3 sm:grid-cols-2">
        <div class="min-w-0 rounded-xl border border-kbd04-rule bg-kbd04-card p-4"><p class="mb-2 font-kbd04-sans text-[10.5px] font-semibold uppercase tracking-[0.16em] text-kbd04-acc">Flat · this demo</p><p class="font-kbd04-serif text-[17px]">Press <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">Ctrl</kbd> <kbd class="whitespace-nowrap rounded-[0.28em] bg-kbd04-cap px-[0.38em] py-[0.06em] font-kbd04-sans text-[0.84em] font-medium text-kbd04-capink ring-1 ring-kbd04-rim/50 ring-inset [box-decoration-break:clone]">K</kbd> to search.</p><p class="mt-2 font-kbd04-sans text-[13px] leading-snug text-kbd04-mut">Reference prose, changelogs, dense help pages.</p></div>
        <div class="min-w-0 rounded-xl border border-kbd04-rule bg-kbd04-card p-4"><p class="mb-2 font-kbd04-sans text-[10.5px] font-semibold uppercase tracking-[0.16em] text-kbd04-acc">Raised · demo 01</p><p class="font-kbd04-serif text-[17px]">Press <kbd class="inline-block whitespace-nowrap rounded-[0.3em] border border-kbd04-rim bg-kbd04-card px-[0.5em] py-[0.24em] align-[0.06em] font-kbd04-sans text-[0.8em] font-semibold leading-none text-kbd04-capink shadow-[0_1px_0_var(--color-kbd04-edge)]">Ctrl</kbd> <kbd class="inline-block whitespace-nowrap rounded-[0.3em] border border-kbd04-rim bg-kbd04-card px-[0.5em] py-[0.24em] align-[0.06em] font-kbd04-sans text-[0.8em] font-semibold leading-none text-kbd04-capink shadow-[0_1px_0_var(--color-kbd04-edge)]">K</kbd> to search.</p><p class="mt-2 font-kbd04-sans text-[13px] leading-snug text-kbd04-mut">Tips, callouts, first-run hints — one shortcut at a time.</p></div>
      </div>
    </article>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-04-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-04-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd04-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd04-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd04-dark:bg-transparent kbd04-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd04-dark:hidden">Light</span><span class="hidden kbd04-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd04-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-04:not(:has(#kbd-04-theme:checked)), .kbd-04:not(:has(#kbd-04-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-04:has(#kbd-04-theme:checked), .kbd-04:has(#kbd-04-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd04-bg: light-dark(#fbfbf9, #141513);
  --color-kbd04-bg: light-dark(oklch(0.988 0.003 106.4), oklch(0.194 0.004 128.7));
  --color-kbd04-card: light-dark(#ffffff, #1c1d1a);
  --color-kbd04-card: light-dark(oklch(1 0 0), oklch(0.229 0.006 121.9));
  --color-kbd04-ink: light-dark(#1f211d, #e9eae5);
  --color-kbd04-ink: light-dark(oklch(0.244 0.008 128.8), oklch(0.935 0.007 115.7));
  --color-kbd04-mut: light-dark(#585c53, #a3a79c);
  --color-kbd04-mut: light-dark(oklch(0.468 0.015 126.6), oklch(0.722 0.016 123.1));
  --color-kbd04-rule: light-dark(#e3e4dd, #2c2e29);
  --color-kbd04-rule: light-dark(oklch(0.916 0.009 113.2), oklch(0.297 0.009 124.8));
  --color-kbd04-cap: light-dark(#ecede6, #2a2c27);
  --color-kbd04-cap: light-dark(oklch(0.943 0.009 113.2), oklch(0.289 0.009 124.8));
  --color-kbd04-capink: light-dark(#2b2e28, #e4e6df);
  --color-kbd04-capink: light-dark(oklch(0.296 0.011 128.9), oklch(0.921 0.01 119.6));
  --color-kbd04-rim: light-dark(#bfc2b6, #4a4e44);
  --color-kbd04-rim: light-dark(oklch(0.808 0.017 118.2), oklch(0.417 0.017 124.9));
  --color-kbd04-edge: light-dark(#b5b8ac, #0a0b09);
  --color-kbd04-edge: light-dark(oklch(0.777 0.017 118.2), oklch(0.148 0.005 128.5));
  --color-kbd04-acc: light-dark(#2f6e42, #7cc496);
  --color-kbd04-acc: light-dark(oklch(0.485 0.096 151.1), oklch(0.76 0.099 155.3));
  --font-kbd04-serif: 'Source Serif 4', Georgia, serif;
  --font-kbd04-sans: 'IBM Plex Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-04 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
