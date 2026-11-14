---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-one-accent-color-restraint-budget/"
title: "Tailwind One Accent Color Restraint Budget"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "The same invoice panel on a one-accent budget and a three-accent budget."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind One Accent Color Restraint Budget
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-one-accent-color-restraint-budget/

The same invoice panel on a one-accent budget and a three-accent budget. With one hue the primary action is found before anything is read; with three, every button shouts and the hierarchy collapses into a label-reading exercise. Accent dots in each header count the hues, and the hover/press steps are derived with color-mix() so the budget stays at one.
## HTML
```html
<section class="tmu-09 relative w-full min-h-svh bg-tmu09-bg font-tmu09-ui text-tmu09-ink antialiased" aria-labelledby="tmu09-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu09-theme" type="checkbox" class="peer sr-only">
    <label for="tmu09-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu09-line bg-tmu09-surface text-tmu09-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu09-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu09-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[72rem] gap-12 px-6 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu09-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu09-ink-2"><span class="tabular-nums text-tmu09-acc">09</span><span aria-hidden="true" class="h-px w-6 bg-tmu09-line"></span>Colour budget</p>
      <h2 id="tmu09-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Spend one accent, and spend it on the action</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu09-ink-2 text-pretty">Hierarchy between buttons comes from fill, border and nothing &mdash; not from three different hues. The second panel shows what happens when every action gets a colour.</p>
    </header>
    <div class="grid gap-6 md:grid-cols-2">
      <article aria-labelledby="tmu09-a" class="grid min-w-0 content-start gap-5 rounded-2xl border border-tmu09-line bg-tmu09-surface p-6 md:p-8 shadow-[0_1px_2px_rgb(16_26_44/0.05),0_12px_32px_-24px_rgb(16_26_44/0.4)]">
        <header class="flex flex-wrap items-center justify-between gap-3">
          <h3 id="tmu09-a" class="text-[0.8125rem] font-semibold uppercase tracking-[0.1em]">Budget: 1 accent</h3>
          <p class="flex items-center gap-1.5" aria-label="1 accent colour in use"><span aria-hidden="true" class="size-3 rounded-full bg-tmu09-acc ring-2 ring-tmu09-surface"></span><span class="ml-1 font-tmu09-mono text-xs text-tmu09-ink-2">1 hue</span></p>
        </header>
        <div class="grid min-w-0 gap-4 rounded-xl bg-tmu09-surface-2 p-5">
          <p class="text-xs font-medium uppercase tracking-[0.08em] text-tmu09-ink-2">Invoice INV-2043 &middot; Basalt Industries</p>
          <p class="text-[clamp(1.875rem,1.5rem+1.6vw,2.5rem)] font-semibold leading-[1.05] tracking-[-0.03em] tabular-nums">$18,420.00</p>
          <ul class="grid gap-2 border-y border-tmu09-line py-3 text-sm">
            <li class="flex justify-between gap-4"><span class="text-tmu09-ink-2">Retainer</span><b class="font-medium tabular-nums">$12,000.00</b></li>
            <li class="flex justify-between gap-4"><span class="text-tmu09-ink-2">Overage, 42 hrs</span><b class="font-medium tabular-nums">$6,420.00</b></li>
            <li class="flex justify-between gap-4"><span class="text-tmu09-ink-2">Due</span><b class="font-medium tabular-nums">14 September</b></li>
          </ul>
          <p class="inline-flex items-center gap-2 text-[0.8125rem] font-semibold text-tmu09-status-ok"><svg class="size-4 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Approved by Priya Sharma</p>
          <div class="flex flex-wrap gap-2">
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color,color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu09-acc motion-reduce:transition-none border-tmu09-acc bg-tmu09-acc font-semibold text-tmu09-acc-ink hover:bg-tmu09-acc-hover active:bg-tmu09-acc-press">Send for payment</button>
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color,color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu09-acc motion-reduce:transition-none border-tmu09-line text-tmu09-ink hover:border-tmu09-ink-2">Edit lines</button>
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color,color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu09-acc motion-reduce:transition-none border-transparent text-tmu09-ink-2 hover:bg-tmu09-line/50 hover:text-tmu09-ink">Duplicate</button>
          </div>
        </div>
        <p class="text-sm text-tmu09-ink-2 text-pretty">One filled button. The next action is found before any label is read.</p>
      </article>
      <article aria-labelledby="tmu09-b" class="grid min-w-0 content-start gap-5 rounded-2xl border border-tmu09-line bg-tmu09-surface p-6 md:p-8 shadow-[0_1px_2px_rgb(16_26_44/0.05),0_12px_32px_-24px_rgb(16_26_44/0.4)]">
        <header class="flex flex-wrap items-center justify-between gap-3">
          <h3 id="tmu09-b" class="text-[0.8125rem] font-semibold uppercase tracking-[0.1em]">Budget: 3 accents</h3>
          <p class="flex items-center gap-1.5" aria-label="3 accent colours in use"><span aria-hidden="true" class="size-3 rounded-full bg-tmu09-acc ring-2 ring-tmu09-surface"></span><span aria-hidden="true" class="size-3 rounded-full bg-tmu09-alt2 ring-2 ring-tmu09-surface"></span><span aria-hidden="true" class="size-3 rounded-full bg-tmu09-alt3 ring-2 ring-tmu09-surface"></span><span class="ml-1 font-tmu09-mono text-xs text-tmu09-ink-2">3 hues</span></p>
        </header>
        <div class="grid min-w-0 gap-4 rounded-xl bg-tmu09-surface-2 p-5">
          <p class="text-xs font-medium uppercase tracking-[0.08em] text-tmu09-alt3">Invoice INV-2043 &middot; Basalt Industries</p>
          <p class="text-[clamp(1.875rem,1.5rem+1.6vw,2.5rem)] font-semibold leading-[1.05] tracking-[-0.03em] tabular-nums text-tmu09-alt2">$18,420.00</p>
          <ul class="grid gap-2 border-y border-tmu09-line py-3 text-sm">
            <li class="flex justify-between gap-4"><span class="text-tmu09-ink-2">Retainer</span><b class="font-medium tabular-nums">$12,000.00</b></li>
            <li class="flex justify-between gap-4"><span class="text-tmu09-ink-2">Overage, 42 hrs</span><b class="font-medium tabular-nums">$6,420.00</b></li>
            <li class="flex justify-between gap-4"><span class="text-tmu09-ink-2">Due</span><b class="font-medium tabular-nums">14 September</b></li>
          </ul>
          <p class="inline-flex items-center gap-2 text-[0.8125rem] font-semibold text-tmu09-status-ok"><svg class="size-4 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Approved by Priya Sharma</p>
          <div class="flex flex-wrap gap-2">
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color,color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu09-acc motion-reduce:transition-none border-tmu09-acc bg-tmu09-acc font-semibold text-tmu09-acc-ink hover:bg-tmu09-acc-hover active:bg-tmu09-acc-press">Send for payment</button>
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color,color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu09-acc motion-reduce:transition-none border-tmu09-alt2 bg-tmu09-alt2 font-semibold text-tmu09-acc-ink hover:brightness-110">Edit lines</button>
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color,color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu09-acc motion-reduce:transition-none border-tmu09-alt3 bg-tmu09-alt3 font-semibold text-tmu09-acc-ink hover:brightness-110">Duplicate</button>
          </div>
        </div>
        <p class="text-sm text-tmu09-ink-2 text-pretty">Three filled buttons compete; the eye has to read labels to find the one that moves money.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu09-bg: light-dark(#eef1f6, #101a2c);
  --color-tmu09-bg: light-dark(oklch(94.5% 0.008 258), oklch(21% 0.04 258));
  --color-tmu09-surface: light-dark(#ffffff, #17233a);
  --color-tmu09-surface: light-dark(oklch(100% 0 0), oklch(25.5% 0.042 258));
  --color-tmu09-surface-2: light-dark(#f6f8fb, #1e2c46);
  --color-tmu09-surface-2: light-dark(oklch(97.8% 0.005 258), oklch(29% 0.044 258));
  --color-tmu09-ink: light-dark(#101a2c, #f2f5fa);
  --color-tmu09-ink: light-dark(oklch(21% 0.04 258), oklch(96.5% 0.005 258));
  --color-tmu09-ink-2: light-dark(#4b5872, #a9b6cc);
  --color-tmu09-ink-2: light-dark(oklch(45% 0.035 258), oklch(76% 0.026 258));
  --color-tmu09-line: light-dark(#ccd5e2, #2d3c58);
  --color-tmu09-line: light-dark(oklch(86% 0.014 258), oklch(35% 0.038 258));
  --color-tmu09-acc: light-dark(#14459e, #7fb4ff);
  --color-tmu09-acc: light-dark(oklch(40% 0.16 262), oklch(79% 0.13 260));
  --color-tmu09-acc-ink: light-dark(#ffffff, #0b1526);
  --color-tmu09-acc-ink: light-dark(oklch(100% 0 0), oklch(18% 0.03 258));
  --color-tmu09-alt2: light-dark(#8a4a06, #f0a35c);
  --color-tmu09-alt2: light-dark(oklch(45% 0.12 58), oklch(78% 0.13 62));
  --color-tmu09-alt3: light-dark(#5b2fb0, #b79bf5);
  --color-tmu09-alt3: light-dark(oklch(42% 0.18 298), oklch(76% 0.13 300));
  --color-tmu09-status-ok: light-dark(#16663d, #6ed49a);
  --color-tmu09-status-ok: light-dark(oklch(44% 0.11 155), oklch(82% 0.13 155));
  --color-tmu09-status-warn: light-dark(#7a5b12, #f2c661);
  --color-tmu09-status-warn: light-dark(oklch(46% 0.1 85), oklch(85% 0.12 90));
  --color-tmu09-acc-hover: color-mix(in oklab, var(--color-tmu09-acc) 90%, var(--color-tmu09-ink));
  --color-tmu09-acc-press: color-mix(in oklab, var(--color-tmu09-acc) 82%, var(--color-tmu09-bg));
  --font-tmu09-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu09-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-09:has(#tmu09-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-09:has(#tmu09-theme:checked) {
    color-scheme: light;
  }
}
```
