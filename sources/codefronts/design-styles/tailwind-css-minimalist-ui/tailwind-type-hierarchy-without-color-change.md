---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-type-hierarchy-without-color-change/"
title: "Tailwind Type Hierarchy Without Any Color Change"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "The same invoice card twice: once leaning on three colours, once in a single ink."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Type Hierarchy Without Any Color Change
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-type-hierarchy-without-color-change/

The same invoice card twice: once leaning on three colours, once in a single ink. The single-ink card still reads in the right order &mdash; kicker, client, amount, meta &mdash; because size, weight, tracking-* and space carry the hierarchy. The legend prints every utility decision so the comparison is a spec, not a vibe.
## HTML
```html
<section class="tmu-02 relative w-full min-h-svh bg-tmu02-bg font-tmu02-serif text-tmu02-ink antialiased" aria-labelledby="tmu02-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu02-theme" type="checkbox" class="peer sr-only">
    <label for="tmu02-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu02-line bg-tmu02-surface text-tmu02-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu02-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu02-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[72rem] gap-12 px-6 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3 font-tmu02-ui">
      <p class="inline-flex items-center gap-2.5 font-tmu02-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu02-ink-2"><span class="tabular-nums text-tmu02-acc">02</span><span aria-hidden="true" class="h-px w-6 bg-tmu02-line"></span>Hierarchy</p>
      <h2 id="tmu02-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Hierarchy without colour</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu02-ink-2 text-pretty">Size, weight, tracking and space decide the reading order. Colour is optional seasoning &mdash; remove it and the right card still reads top to bottom.</p>
    </header>
    <div class="grid gap-6 md:grid-cols-2">
      <article aria-labelledby="tmu02-side-a" class="grid min-w-0 content-start gap-4 rounded-xl border border-tmu02-line bg-transparent p-6">
        <div class="flex flex-wrap items-baseline justify-between gap-2">
          <h3 id="tmu02-side-a" class="font-tmu02-ui text-[0.8125rem] font-semibold uppercase tracking-[0.1em]">With colour</h3>
          <span class="font-tmu02-ui text-xs text-tmu02-ink-2">Three hues doing the work</span>
        </div>
        <div class="grid min-w-0 gap-3 rounded-lg bg-tmu02-surface p-6 shadow-[0_1px_2px_rgb(0_0_0/0.05),0_8px_24px_-16px_rgb(0_0_0/0.18)]">
          <p class="font-tmu02-ui text-xs font-medium uppercase tracking-[0.1em] text-tmu02-tint">Invoice INV-2043</p>
          <h4 class="text-2xl/[1.15] font-semibold tracking-[-0.02em]">Basalt Industries</h4>
          <p class="font-tmu02-ui text-[clamp(1.875rem,1.5rem+1.5vw,2.25rem)] font-semibold leading-[1.05] tracking-[-0.03em] tabular-nums text-tmu02-tint">$18,420.00</p>
          <p class="font-tmu02-ui text-sm text-pretty text-tmu02-ink-2">Due 14 September &middot; Net 30 &middot; Sent by Priya Sharma</p>
          <ul class="mt-2 grid gap-2 border-t border-tmu02-line pt-4 font-tmu02-ui text-sm">
            <li class="flex justify-between gap-4"><span class="text-tmu02-ink-2">Retainer</span><b class="font-medium tabular-nums">$12,000.00</b></li>
            <li class="flex justify-between gap-4"><span class="text-tmu02-ink-2">Overage, 42 hrs</span><b class="font-medium tabular-nums">$6,420.00</b></li>
          </ul>
          <p class="inline-flex items-center gap-2 font-tmu02-ui text-[0.8125rem] font-semibold uppercase tracking-[0.04em] text-tmu02-tint-2">
            <svg class="size-4 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Approved
          </p>
        </div>
      </article>
      <article aria-labelledby="tmu02-side-b" class="grid min-w-0 content-start gap-4 rounded-xl border border-tmu02-line bg-tmu02-surface-2 p-6">
        <div class="flex flex-wrap items-baseline justify-between gap-2">
          <h3 id="tmu02-side-b" class="font-tmu02-ui text-[0.8125rem] font-semibold uppercase tracking-[0.1em]">One ink colour</h3>
          <span class="font-tmu02-ui text-xs text-tmu02-ink-2">Weight and space doing the work</span>
        </div>
        <div class="grid min-w-0 gap-3 rounded-lg bg-tmu02-surface p-6 shadow-[0_1px_2px_rgb(0_0_0/0.05),0_8px_24px_-16px_rgb(0_0_0/0.18)]">
          <p class="font-tmu02-ui text-xs font-medium uppercase tracking-[0.1em] text-tmu02-ink">Invoice INV-2043</p>
          <h4 class="text-2xl/[1.15] font-semibold tracking-[-0.02em]">Basalt Industries</h4>
          <p class="font-tmu02-ui text-[clamp(1.875rem,1.5rem+1.5vw,2.25rem)] font-semibold leading-[1.05] tracking-[-0.03em] tabular-nums text-tmu02-ink">$18,420.00</p>
          <p class="font-tmu02-ui text-sm text-pretty text-tmu02-ink">Due 14 September &middot; Net 30 &middot; Sent by Priya Sharma</p>
          <ul class="mt-2 grid gap-2 border-t border-tmu02-line pt-4 font-tmu02-ui text-sm">
            <li class="flex justify-between gap-4"><span class="text-tmu02-ink">Retainer</span><b class="font-medium tabular-nums">$12,000.00</b></li>
            <li class="flex justify-between gap-4"><span class="text-tmu02-ink">Overage, 42 hrs</span><b class="font-medium tabular-nums">$6,420.00</b></li>
          </ul>
          <p class="inline-flex items-center gap-2 font-tmu02-ui text-[0.8125rem] font-semibold uppercase tracking-[0.04em] text-tmu02-ink">
            <svg class="size-4 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Approved
          </p>
        </div>
      </article>
    </div>
    <dl class="grid gap-x-6 gap-y-4 border-y border-tmu02-line py-6 font-tmu02-ui text-[0.8125rem] grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))]">
      <div class="grid min-w-0 gap-1"><dt class="font-semibold">Kicker</dt><dd class="font-tmu02-mono text-xs leading-relaxed text-tmu02-ink-2">text-xs &middot; 500 &middot; tracking-[0.1em] &middot; uppercase</dd></div>
      <div class="grid min-w-0 gap-1"><dt class="font-semibold">Title</dt><dd class="font-tmu02-mono text-xs leading-relaxed text-tmu02-ink-2">text-2xl &middot; 600 &middot; tracking-[-0.02em]</dd></div>
      <div class="grid min-w-0 gap-1"><dt class="font-semibold">Amount</dt><dd class="font-tmu02-mono text-xs leading-relaxed text-tmu02-ink-2">2.25rem &middot; 600 &middot; tracking-[-0.03em] &middot; tabular</dd></div>
      <div class="grid min-w-0 gap-1"><dt class="font-semibold">Meta</dt><dd class="font-tmu02-mono text-xs leading-relaxed text-tmu02-ink-2">text-sm &middot; 400 &middot; normal</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu02-bg: light-dark(#ffffff, #101112);
  --color-tmu02-bg: light-dark(oklch(100% 0 0), oklch(17.5% 0.002 250));
  --color-tmu02-surface: light-dark(#ffffff, #191b1d);
  --color-tmu02-surface: light-dark(oklch(100% 0 0), oklch(23% 0.003 250));
  --color-tmu02-ink: light-dark(#1a1a1a, #f2f3f4);
  --color-tmu02-ink: light-dark(oklch(22% 0 0), oklch(96% 0.002 250));
  --color-tmu02-ink-2: light-dark(#55595c, #a9aeb2);
  --color-tmu02-ink-2: light-dark(oklch(46% 0.004 250), oklch(75% 0.005 250));
  --color-tmu02-line: light-dark(#d5d7d9, #353839);
  --color-tmu02-line: light-dark(oklch(86% 0.003 250), oklch(34% 0.004 250));
  --color-tmu02-tint: light-dark(#0b5cd5, #7fb0ff);
  --color-tmu02-tint: light-dark(oklch(48% 0.18 258), oklch(78% 0.12 258));
  --color-tmu02-tint-2: light-dark(#7a5b12, #dcbb63);
  --color-tmu02-tint-2: light-dark(oklch(46% 0.1 85), oklch(81% 0.1 85));
  --color-tmu02-acc: light-dark(#0b5cd5, #7fb0ff);
  --color-tmu02-acc: light-dark(oklch(48% 0.18 258), oklch(78% 0.12 258));
  --color-tmu02-surface-2: light-dark(#f6f6f4, #1c1c1f);
  --color-tmu02-surface-2: light-dark(oklch(97% 0.003 90), oklch(22% 0.005 280));
  --font-tmu02-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --font-tmu02-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu02-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-02:has(#tmu02-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-02:has(#tmu02-theme:checked) {
    color-scheme: light;
  }
}
```
