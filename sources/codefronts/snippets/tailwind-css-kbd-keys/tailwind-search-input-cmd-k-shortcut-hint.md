---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-search-input-cmd-k-shortcut-hint/"
title: "Tailwind Search Input with Cmd+K Shortcut Hint"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "The docs-site search field with a ⌘ K badge tucked inside — and the badge behaves: it is pointer-events-none so clicks land in the input, it fades out on…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Search Input with Cmd+K Shortcut Hint
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/tailwind-search-input-cmd-k-shortcut-hint/

The docs-site search field with a ⌘ K badge tucked inside — and the badge behaves: it is pointer-events-none so clicks land in the input, it fades out on focus via peer-focus:opacity-0, and an Esc hint fades in to tell the user how to leave. The input advertises the shortcut to assistive tech with aria-keyshortcuts.
## HTML
```html
<section class="kbd-11 relative w-full min-h-svh scheme-light kbd11-dark:scheme-dark bg-kbd11-bg bg-[radial-gradient(80%_60%_at_50%_0%,var(--color-kbd11-glow),transparent_70%)] text-kbd11-ink font-kbd11-sans" aria-label="Search bar shortcut hint demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <div class="w-full min-w-0 max-w-[34rem]">
      <label class="mb-2.5 block text-[13px] font-semibold" for="kbd-11-input">Search documentation</label>
      <div class="relative">
        <svg class="pointer-events-none absolute top-1/2 left-4 size-[18px] -translate-y-1/2 fill-none stroke-kbd11-mut [stroke-linecap:round] [stroke-width:2]" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16 L20 20"/></svg>
        <input id="kbd-11-input" type="search" aria-keyshortcuts="Meta+K Control+K" placeholder="Search components, tokens, guides" class="peer h-13 w-full rounded-xl border border-kbd11-rim bg-kbd11-field pr-24 pl-11 text-[15px] text-kbd11-ink shadow-[0_1px_2px_var(--color-kbd11-shade)] outline-none transition-[border-color,box-shadow] placeholder:text-kbd11-mut hover:border-kbd11-rimhi focus:border-kbd11-acc focus:shadow-[0_0_0_4px_var(--color-kbd11-ring)] motion-reduce:transition-none [&::-webkit-search-cancel-button]:hidden">
        <kbd aria-hidden="true" class="pointer-events-none absolute top-1/2 right-3 inline-flex -translate-y-1/2 gap-1 transition-opacity duration-150 peer-focus:opacity-0 peer-[:not(:placeholder-shown)]:opacity-0 motion-reduce:transition-none"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd11-rim bg-kbd11-cap px-1.5 text-[12px] font-medium leading-none text-kbd11-capink shadow-[0_1px_0_var(--color-kbd11-edge)]">⌘</kbd><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd11-rim bg-kbd11-cap px-1.5 text-[12px] font-medium leading-none text-kbd11-capink shadow-[0_1px_0_var(--color-kbd11-edge)]">K</kbd></kbd>
        <kbd aria-hidden="true" class="pointer-events-none absolute top-1/2 right-3 inline-flex -translate-y-1/2 items-center gap-1.5 text-[11.5px] text-kbd11-mut opacity-0 transition-opacity duration-150 peer-focus:opacity-100 motion-reduce:transition-none"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-md border border-kbd11-rim bg-kbd11-cap px-1.5 text-[12px] font-medium leading-none text-kbd11-capink shadow-[0_1px_0_var(--color-kbd11-edge)]">Esc</kbd>to close</kbd>
      </div>
      <p class="mt-4 text-[13.5px] leading-relaxed text-kbd11-mut text-pretty">Click anywhere on the field, including the badge — it carries <code class="rounded bg-kbd11-code px-1.5 py-0.5 font-mono text-[12px] text-kbd11-ink">pointer-events-none</code>, so the click lands in the input. Focus the field and the hint swaps to <strong class="font-semibold text-kbd11-ink">Esc</strong>.</p>
    </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-11-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-11-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd11-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd11-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd11-dark:bg-transparent kbd11-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd11-dark:hidden">Light</span><span class="hidden kbd11-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd11-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-11:not(:has(#kbd-11-theme:checked)), .kbd-11:not(:has(#kbd-11-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-11:has(#kbd-11-theme:checked), .kbd-11:has(#kbd-11-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd11-bg: light-dark(#f6f7f9, #0c0d10);
  --color-kbd11-bg: light-dark(oklch(0.976 0.003 264.5), oklch(0.159 0.007 271));
  --color-kbd11-glow: light-dark(#e3e9ff, #171d33);
  --color-kbd11-glow: light-dark(oklch(0.936 0.03 273.6), oklch(0.237 0.043 271.2));
  --color-kbd11-field: light-dark(#ffffff, #14161b);
  --color-kbd11-field: light-dark(oklch(1 0 0), oklch(0.2 0.01 268.2));
  --color-kbd11-shade: light-dark(#1020340f, #00000066);
  --color-kbd11-shade: light-dark(oklch(0.241 0.044 254.8 / 0.06), oklch(0 0 0 / 0.4));
  --color-kbd11-ink: light-dark(#121418, #eceef2);
  --color-kbd11-ink: light-dark(oklch(0.191 0.009 264.3), oklch(0.949 0.006 264.5));
  --color-kbd11-mut: light-dark(#5a626e, #98a1ae);
  --color-kbd11-mut: light-dark(oklch(0.494 0.022 258.4), oklch(0.706 0.022 257.5));
  --color-kbd11-rim: light-dark(#d5d9e0, #2c313a);
  --color-kbd11-rim: light-dark(oklch(0.884 0.011 261.8), oklch(0.312 0.018 262.2));
  --color-kbd11-rimhi: light-dark(#b9c0ca, #404754);
  --color-kbd11-rimhi: light-dark(oklch(0.805 0.016 257.2), oklch(0.397 0.024 262.8));
  --color-kbd11-code: light-dark(#eef0f4, #1d2027);
  --color-kbd11-code: light-dark(oklch(0.955 0.006 264.5), oklch(0.244 0.014 267));
  --color-kbd11-cap: light-dark(#f6f7f9, #1e2128);
  --color-kbd11-cap: light-dark(oklch(0.976 0.003 264.5), oklch(0.248 0.014 267));
  --color-kbd11-edge: light-dark(#c4c9d1, #050608);
  --color-kbd11-edge: light-dark(oklch(0.834 0.012 259.8), oklch(0.122 0.006 261.6));
  --color-kbd11-capink: light-dark(#3a414c, #c9d0da);
  --color-kbd11-capink: light-dark(oklch(0.373 0.021 259.4), oklch(0.855 0.016 257.2));
  --color-kbd11-acc: light-dark(#3e63dd, #7b9bff);
  --color-kbd11-acc: light-dark(oklch(0.544 0.191 267), oklch(0.71 0.151 268.9));
  --color-kbd11-ring: light-dark(#3e63dd2e, #7b9bff33);
  --color-kbd11-ring: light-dark(oklch(0.544 0.191 267 / 0.18), oklch(0.71 0.151 268.9 / 0.2));
  --font-kbd11-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-11 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```
