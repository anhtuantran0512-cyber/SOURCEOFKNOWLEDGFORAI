---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-elevation-without-shadows-tonal-surfaces/"
title: "Tailwind Elevation Without Shadows or Gradients"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "Four levels of elevation built from tone alone: each step up is a few percent lighter, carries a single top hairline, and gains 4px of padding."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Elevation Without Shadows or Gradients
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-elevation-without-shadows-tonal-surfaces/

Four levels of elevation built from tone alone: each step up is a few percent lighter, carries a single top hairline, and gains 4px of padding. No shadows, no gradients. The overlay level sits on a scrim, because a dialog is the one surface that tone alone cannot lift off the page.
## HTML
```html
<section class="tmu-12 relative w-full min-h-svh bg-tmu12-e0 font-tmu12-ui text-tmu12-ink antialiased" aria-labelledby="tmu12-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu12-theme" type="checkbox" class="peer sr-only">
    <label for="tmu12-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu12-edge bg-tmu12-e1 text-tmu12-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu12-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu12-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[62rem] gap-10 px-5 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu12-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu12-ink-2"><span class="tabular-nums text-tmu12-acc">12</span><span aria-hidden="true" class="h-px w-6 bg-tmu12-edge"></span>Elevation</p>
      <h2 id="tmu12-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Depth from tone, not from shadow</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu12-ink-2 text-pretty">Each level is a little lighter, gets one top hairline and a little more room. Only the overlay needs help &mdash; a scrim.</p>
    </header>
    <article aria-labelledby="tmu12-l0" class="grid min-w-0 gap-3 rounded-2xl bg-tmu12-e0 p-6 ring-1 ring-tmu12-edge md:p-8">
      <header class="grid min-w-0 gap-0.5"><h3 id="tmu12-l0" class="text-[0.9375rem] font-semibold tracking-[-0.008em]">Level 0 &mdash; page</h3><p class="font-tmu12-mono text-xs tabular-nums text-tmu12-ink-2">base tone &middot; no edge &middot; p-6</p></header>
      <article aria-labelledby="tmu12-l1" class="grid min-w-0 gap-3 rounded-xl bg-tmu12-e1 p-7 border-t border-t-tmu12-edge-hi md:p-9">
        <header class="grid min-w-0 gap-0.5"><h4 id="tmu12-l1" class="text-[0.9375rem] font-semibold tracking-[-0.008em]">Level 1 &mdash; panel</h4><p class="font-tmu12-mono text-xs tabular-nums text-tmu12-ink-2">+4% lightness &middot; top hairline &middot; p-7</p></header>
        <article aria-labelledby="tmu12-l2" class="grid min-w-0 gap-3 rounded-xl bg-tmu12-e2 p-8 border-t border-t-tmu12-edge-hi md:p-10">
          <header class="grid min-w-0 gap-0.5"><h5 id="tmu12-l2" class="text-[0.9375rem] font-semibold tracking-[-0.008em]">Level 2 &mdash; raised</h5><p class="font-tmu12-mono text-xs tabular-nums text-tmu12-ink-2">+8% lightness &middot; top hairline &middot; p-8</p></header>
          <div class="flex flex-wrap gap-2 pt-1"><button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg border px-4 text-sm cursor-pointer transition-[filter,border-color,translate] duration-150 active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu12-acc motion-reduce:transition-none border-tmu12-acc bg-tmu12-acc font-semibold text-tmu12-acc-ink hover:brightness-110">Save workspace</button><button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg border px-4 text-sm cursor-pointer transition-[filter,border-color,translate] duration-150 active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu12-acc motion-reduce:transition-none border-tmu12-edge font-medium text-tmu12-ink hover:border-tmu12-ink-2">Discard</button></div>
        </article>
      </article>
    </article>
    <section aria-labelledby="tmu12-l3" class="grid min-w-0 place-items-center rounded-2xl bg-tmu12-scrim px-4 py-10 backdrop-blur-[2px] md:p-14">
      <div class="grid w-full min-w-0 max-w-[26rem] gap-2.5 rounded-xl bg-tmu12-e3 p-9 border-t border-t-tmu12-edge-hi">
        <header class="grid min-w-0 gap-0.5"><h3 id="tmu12-l3" class="text-[0.9375rem] font-semibold tracking-[-0.008em]">Level 3 &mdash; overlay</h3><p class="font-tmu12-mono text-xs tabular-nums text-tmu12-ink-2">+12% lightness &middot; top hairline &middot; scrim &middot; z-50</p></header>
        <p class="text-sm text-tmu12-ink-2 text-pretty">Move $4,200.00 from Operating to Payroll? This cannot be undone.</p>
        <div class="flex flex-wrap gap-2 pt-1"><button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg border px-4 text-sm cursor-pointer transition-[filter,border-color,translate] duration-150 active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu12-acc motion-reduce:transition-none border-tmu12-acc bg-tmu12-acc font-semibold text-tmu12-acc-ink hover:brightness-110">Confirm transfer</button><button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg border px-4 text-sm cursor-pointer transition-[filter,border-color,translate] duration-150 active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu12-acc motion-reduce:transition-none border-tmu12-edge font-medium text-tmu12-ink hover:border-tmu12-ink-2">Cancel</button></div>
      </div>
    </section>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu12-e0: light-dark(#eeecea, #1b1917);
  --color-tmu12-e0: light-dark(oklch(94% 0.004 70), oklch(22% 0.006 60));
  --color-tmu12-e1: light-dark(#f5f3f1, #232120);
  --color-tmu12-e1: light-dark(oklch(96.5% 0.004 70), oklch(26% 0.006 60));
  --color-tmu12-e2: light-dark(#fbfaf9, #2c2a28);
  --color-tmu12-e2: light-dark(oklch(98.5% 0.003 70), oklch(30% 0.006 60));
  --color-tmu12-e3: light-dark(#ffffff, #363331);
  --color-tmu12-e3: light-dark(oklch(100% 0 0), oklch(34% 0.007 60));
  --color-tmu12-edge: light-dark(#cfcac5, #4a4643);
  --color-tmu12-edge: light-dark(oklch(84% 0.007 70), oklch(42% 0.008 60));
  --color-tmu12-ink: light-dark(#1b1917, #f5f2ef);
  --color-tmu12-ink: light-dark(oklch(22% 0.006 60), oklch(96% 0.005 70));
  --color-tmu12-ink-2: light-dark(#57514b, #b3aca6);
  --color-tmu12-ink-2: light-dark(oklch(45% 0.01 62), oklch(75% 0.009 65));
  --color-tmu12-scrim: light-dark(rgba(24, 22, 20, 0.48), rgba(8, 7, 6, 0.62));
  --color-tmu12-acc: light-dark(#0d6355, #8fd4c4);
  --color-tmu12-acc: light-dark(oklch(43% 0.09 175), oklch(84% 0.09 175));
  --color-tmu12-acc-ink: light-dark(#ffffff, #12201d);
  --color-tmu12-acc-ink: light-dark(oklch(100% 0 0), oklch(19% 0.02 175));
  --color-tmu12-edge-hi: color-mix(in oklab, var(--color-tmu12-edge) 85%, var(--color-tmu12-ink));
  --font-tmu12-ui: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-tmu12-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-12:has(#tmu12-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-12:has(#tmu12-theme:checked) {
    color-scheme: light;
  }
}
```
