---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-vs-brutalist-side-by-side/"
title: "Tailwind Minimalist and Brutalist Side by Side"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "The same trial sign-up card built twice from the same markup skeleton: minimalist (one accent, 1px hairline, tonal raise) and brutalist (three colours, 4px…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist and Brutalist Side by Side
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-vs-brutalist-side-by-side/

The same trial sign-up card built twice from the same markup skeleton: minimalist (one accent, 1px hairline, tonal raise) and brutalist (three colours, 4px border, 8px hard offset shadow). A decision table under each names what the style optimises for and how it fails &mdash; so the choice reads as a trade-off, not a taste.
## HTML
```html
<section class="tmu-14 relative w-full min-h-svh bg-tmu14-bg font-tmu14-m text-tmu14-ink antialiased" aria-labelledby="tmu14-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu14-theme" type="checkbox" class="peer sr-only">
    <label for="tmu14-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu14-m-line bg-tmu14-m-surface text-tmu14-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu14-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu14-m-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[74rem] gap-10 px-5 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu14-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu14-ink-2"><span class="tabular-nums text-tmu14-m-acc">14</span><span aria-hidden="true" class="h-px w-6 bg-tmu14-m-line"></span>Opposite poles</p>
      <h2 id="tmu14-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Minimalist and brutalist, same card</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu14-ink-2 text-pretty">Same content, same fields, same action. One subtracts until only the task is left; the other adds until it cannot be forgotten.</p>
    </header>
    <div class="grid gap-10 md:grid-cols-2">
      <article aria-labelledby="tmu14-a" class="grid min-w-0 content-start gap-5">
        <header class="flex flex-wrap items-center justify-between gap-2">
          <div class="grid gap-0.5"><h3 id="tmu14-a" class="text-[0.8125rem] font-semibold uppercase tracking-[0.14em]">Minimalist</h3><p class="text-xs tabular-nums text-tmu14-ink-2">1 accent &middot; 1px hairline &middot; +4% tonal raise</p></div>
          <p class="flex gap-1" aria-hidden="true"><span class="size-3 rounded-full bg-tmu14-m-acc"></span></p>
        </header>
        <div class="grid min-w-0 content-start gap-3.5 rounded-xl border border-tmu14-m-line bg-tmu14-m-surface p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04),0_16px_40px_-28px_rgb(0_0_0/0.35)] md:p-8">
          <p class="text-[0.6875rem] uppercase tracking-[0.14em] text-tmu14-ink-2">Meridian</p>
          <h4 class="text-[1.375rem]/[1.15] font-semibold tracking-[-0.018em]">Start a 14-day trial</h4>
          <p class="text-[0.9375rem] text-tmu14-ink-2 text-pretty">Every workspace feature, no card required. Cancel from the billing page in one click.</p>
          <div class="grid min-w-0 gap-1.5">
            <label for="tmu14-m-mail" class="text-[0.8125rem] font-semibold">Work email</label>
            <input id="tmu14-m-mail" type="email" placeholder="[email protected]" autocomplete="email" class="min-h-11 w-full min-w-0 rounded-md border border-tmu14-m-line bg-tmu14-m-surface px-3 text-[0.9375rem] text-tmu14-ink placeholder:text-tmu14-ink-2 focus-visible:border-tmu14-m-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu14-m-acc">
          </div>
          <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center justify-self-start rounded-md border border-tmu14-m-acc bg-tmu14-m-acc px-5 text-[0.9375rem] font-semibold text-tmu14-m-acc-ink cursor-pointer transition-[filter] duration-150 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu14-ink motion-reduce:transition-none">Create workspace</button>
          <p class="text-xs text-tmu14-ink-2">No credit card. SOC 2 Type II.</p>
        </div>
        <dl class="grid min-w-0 text-[0.8125rem]">
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b border-tmu14-m-line"><dt class="font-semibold">Elevation</dt><dd class="text-tmu14-ink-2">Tone step plus hairline</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b border-tmu14-m-line"><dt class="font-semibold">Border</dt><dd class="text-tmu14-ink-2">1px at 3:1</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b border-tmu14-m-line"><dt class="font-semibold">Colour budget</dt><dd class="text-tmu14-ink-2">One accent, on the action</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b border-tmu14-m-line"><dt class="font-semibold">Hierarchy</dt><dd class="text-tmu14-ink-2">Size, weight, space</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b border-tmu14-m-line"><dt class="font-semibold">Optimises for</dt><dd class="text-tmu14-ink-2">Calm, repeat use, content first</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b border-tmu14-m-line"><dt class="font-semibold">Fails by</dt><dd class="text-tmu14-ink-2">Becoming generic; hiding affordances</dd></div>
        </dl>
      </article>
      <article aria-labelledby="tmu14-b" class="grid min-w-0 content-start gap-5 font-tmu14-b">
        <header class="flex flex-wrap items-center justify-between gap-2">
          <div class="grid gap-0.5"><h3 id="tmu14-b" class="text-[0.8125rem] font-bold uppercase tracking-[0.14em] text-tmu14-b-acc">Brutalist</h3><p class="text-xs tabular-nums text-tmu14-ink-2">3 colours &middot; 4px border &middot; 8px hard offset</p></div>
          <p class="flex gap-1" aria-hidden="true"><span class="size-3 border-2 border-tmu14-b-line bg-tmu14-b-acc"></span><span class="size-3 border-2 border-tmu14-b-line bg-tmu14-b-acc2"></span><span class="size-3 border-2 border-tmu14-b-line bg-tmu14-b-surface"></span></p>
        </header>
        <div class="grid min-w-0 content-start gap-3.5 border-4 border-tmu14-b-line bg-tmu14-b-surface p-5 text-tmu14-b-line shadow-[8px_8px_0_var(--color-tmu14-b-line)] md:p-7">
          <p class="text-[0.6875rem] font-bold uppercase tracking-[0.14em] text-tmu14-b-acc">Meridian</p>
          <h4 class="text-2xl/[1.15] font-bold tracking-[-0.03em]">Start a 14-day trial</h4>
          <p class="text-[0.9375rem] text-pretty">Every workspace feature, no card required. Cancel from the billing page in one click.</p>
          <div class="grid min-w-0 gap-1.5">
            <label for="tmu14-b-mail" class="text-[0.8125rem] font-semibold">Work email</label>
            <input id="tmu14-b-mail" type="email" placeholder="[email protected]" autocomplete="email" class="min-h-11 w-full min-w-0 rounded-none border-4 border-tmu14-b-line bg-tmu14-b-surface px-3 text-[0.9375rem] text-tmu14-b-line placeholder:text-tmu14-ink-2 transition-shadow duration-100 focus-visible:shadow-[4px_4px_0_var(--color-tmu14-b-acc2)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tmu14-b-acc2 motion-reduce:transition-none">
          </div>
          <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center justify-self-start rounded-none border-4 border-tmu14-b-line bg-tmu14-b-acc px-5 text-[0.9375rem] font-semibold tracking-[0.02em] text-tmu14-b-acc-ink cursor-pointer shadow-[4px_4px_0_var(--color-tmu14-b-line)] transition-[translate,box-shadow] duration-75 hover:-translate-px hover:shadow-[5px_5px_0_var(--color-tmu14-b-line)] active:translate-[2px] active:shadow-[2px_2px_0_var(--color-tmu14-b-line)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tmu14-b-acc2 motion-reduce:transition-none motion-reduce:hover:translate-0 motion-reduce:active:translate-0">Create workspace</button>
          <p class="text-xs">No credit card. SOC 2 Type II.</p>
        </div>
        <dl class="grid min-w-0 text-[0.8125rem]">
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b-2 border-tmu14-b-line"><dt class="font-semibold">Elevation</dt><dd class="text-tmu14-ink-2">Hard offset shadow, no blur</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b-2 border-tmu14-b-line"><dt class="font-semibold">Border</dt><dd class="text-tmu14-ink-2">4px, maximum contrast</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b-2 border-tmu14-b-line"><dt class="font-semibold">Colour budget</dt><dd class="text-tmu14-ink-2">Three, used deliberately</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b-2 border-tmu14-b-line"><dt class="font-semibold">Hierarchy</dt><dd class="text-tmu14-ink-2">Scale and mass</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b-2 border-tmu14-b-line"><dt class="font-semibold">Optimises for</dt><dd class="text-tmu14-ink-2">Memorability, character, voice</dd></div>
          <div class="grid min-w-0 grid-cols-[minmax(0,8rem)_minmax(0,1fr)] gap-x-4 gap-y-0.5 py-2 border-b-2 border-tmu14-b-line"><dt class="font-semibold">Fails by</dt><dd class="text-tmu14-ink-2">Becoming exhausting; hurting legibility</dd></div>
        </dl>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu14-bg: light-dark(#f6f4ef, #14120e);
  --color-tmu14-bg: light-dark(oklch(96.5% 0.008 90), oklch(18% 0.008 80));
  --color-tmu14-ink: light-dark(#17150f, #f4f1e8);
  --color-tmu14-ink: light-dark(oklch(19.5% 0.008 80), oklch(96% 0.01 90));
  --color-tmu14-ink-2: light-dark(#55503f, #b0a993);
  --color-tmu14-ink-2: light-dark(oklch(44% 0.016 85), oklch(75% 0.018 88));
  --color-tmu14-m-surface: light-dark(#ffffff, #1d1a15);
  --color-tmu14-m-surface: light-dark(oklch(100% 0 0), oklch(22.5% 0.009 82));
  --color-tmu14-m-line: light-dark(#cfc9b9, #3b352a);
  --color-tmu14-m-line: light-dark(oklch(84% 0.016 88), oklch(33% 0.014 85));
  --color-tmu14-m-acc: light-dark(#1f4ea8, #8fb4ff);
  --color-tmu14-m-acc: light-dark(oklch(43% 0.15 262), oklch(80% 0.12 262));
  --color-tmu14-m-acc-ink: light-dark(#ffffff, #0d1526);
  --color-tmu14-m-acc-ink: light-dark(oklch(100% 0 0), oklch(18% 0.03 258));
  --color-tmu14-b-surface: light-dark(#fff8e6, #241f10);
  --color-tmu14-b-surface: light-dark(oklch(97.5% 0.045 95), oklch(25% 0.05 95));
  --color-tmu14-b-line: light-dark(#0d0b06, #ffe9a3);
  --color-tmu14-b-line: light-dark(oklch(13% 0.008 80), oklch(92% 0.1 95));
  --color-tmu14-b-acc: light-dark(#d12817, #ff6a5c);
  --color-tmu14-b-acc: light-dark(oklch(51% 0.19 29), oklch(72% 0.19 30));
  --color-tmu14-b-acc2: light-dark(#2f4cff, #8ea0ff);
  --color-tmu14-b-acc2: light-dark(oklch(52% 0.25 268), oklch(76% 0.15 268));
  --color-tmu14-b-acc-ink: light-dark(#fffdf5, #1a0f0c);
  --color-tmu14-b-acc-ink: light-dark(oklch(99% 0.012 95), oklch(18% 0.03 30));
  --font-tmu14-m: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu14-b: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --font-tmu14-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-14:has(#tmu14-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-14:has(#tmu14-theme:checked) {
    color-scheme: light;
  }
}
```
