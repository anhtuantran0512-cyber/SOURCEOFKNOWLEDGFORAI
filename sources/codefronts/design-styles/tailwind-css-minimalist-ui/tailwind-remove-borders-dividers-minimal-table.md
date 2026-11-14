---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-remove-borders-dividers-minimal-table/"
title: "Tailwind Borders and Dividers You Can Actually Remove"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "A border audit in three parts: a fully ruled table (nine kinds of rule), the same table with eight removed and one kept, and a card set with no outlines at all."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Borders and Dividers You Can Actually Remove
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-remove-borders-dividers-minimal-table/

A border audit in three parts: a fully ruled table (nine kinds of rule), the same table with eight removed and one kept, and a card set with no outlines at all. The kept rule is the header underline at 3:1; row rules are replaced by a hover tint, and the cards separate by tone and padding &mdash; with a has-[a:hover]: lift tying the card to its link.
## HTML
```html
<section class="tmu-11 relative w-full min-h-svh bg-tmu11-bg font-tmu11-ui text-tmu11-ink antialiased" aria-labelledby="tmu11-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu11-theme" type="checkbox" class="peer sr-only">
    <label for="tmu11-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu11-line bg-tmu11-surface text-tmu11-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu11-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu11-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[70rem] gap-11 px-5 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu11-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu11-ink-2"><span class="tabular-nums text-tmu11-acc">11</span><span aria-hidden="true" class="h-px w-6 bg-tmu11-line"></span>Border audit</p>
      <h2 id="tmu11-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Remove every rule that is not doing a job</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu11-ink-2 text-pretty">Nine kinds of line become one. Alignment, tone and padding carry the structure; the header rule stays because it is the only one that tells you something.</p>
    </header>
    <section aria-labelledby="tmu11-t1" class="grid min-w-0 gap-4">
      <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2">
        <h3 id="tmu11-t1" class="text-[0.8125rem] font-bold uppercase tracking-[0.1em]">Before &mdash; fully ruled</h3>
        <p class="font-tmu11-mono text-xs text-tmu11-ink-2">9 rules &middot; box, header, every row, every column</p>
      </div>
      <div class="min-w-0 overflow-x-auto">
        <table class="w-full min-w-[22rem] border-collapse bg-tmu11-surface text-sm border border-tmu11-line-strong [&_td]:border [&_td]:border-tmu11-line-strong [&_th]:border [&_th]:border-tmu11-line-strong">
          <caption class="sr-only">Regional revenue, fully ruled version</caption>
          <thead><tr><th scope="col" class="whitespace-nowrap px-3.5 py-3 text-[0.6875rem] font-bold uppercase tracking-[0.1em] text-tmu11-ink-2 text-left">Region</th><th scope="col" class="whitespace-nowrap px-3.5 py-3 text-[0.6875rem] font-bold uppercase tracking-[0.1em] text-tmu11-ink-2 text-right">Accounts</th><th scope="col" class="whitespace-nowrap px-3.5 py-3 text-[0.6875rem] font-bold uppercase tracking-[0.1em] text-tmu11-ink-2 text-right">MRR</th><th scope="col" class="whitespace-nowrap px-3.5 py-3 text-[0.6875rem] font-bold uppercase tracking-[0.1em] text-tmu11-ink-2 text-right">Change</th></tr></thead>
          <tbody>
            <tr><th scope="row" class="px-3.5 py-3 text-left font-medium">Nordics</th><td class="px-3.5 py-3 text-right tabular-nums">184</td><td class="px-3.5 py-3 text-right tabular-nums">$92,400</td><td class="px-3.5 py-3 text-right tabular-nums text-tmu11-ink">+4.2%</td></tr>
            <tr><th scope="row" class="px-3.5 py-3 text-left font-medium">DACH</th><td class="px-3.5 py-3 text-right tabular-nums">231</td><td class="px-3.5 py-3 text-right tabular-nums">$118,900</td><td class="px-3.5 py-3 text-right tabular-nums text-tmu11-ink">+1.8%</td></tr>
            <tr><th scope="row" class="px-3.5 py-3 text-left font-medium">Benelux</th><td class="px-3.5 py-3 text-right tabular-nums">96</td><td class="px-3.5 py-3 text-right tabular-nums">$41,300</td><td class="px-3.5 py-3 text-right tabular-nums text-tmu11-acc">&minus;0.6%</td></tr>
            <tr><th scope="row" class="px-3.5 py-3 text-left font-medium">Iberia</th><td class="px-3.5 py-3 text-right tabular-nums">74</td><td class="px-3.5 py-3 text-right tabular-nums">$28,750</td><td class="px-3.5 py-3 text-right tabular-nums text-tmu11-ink">+6.1%</td></tr>
          </tbody>
        </table>
      </div>
    </section>
    <section aria-labelledby="tmu11-t2" class="grid min-w-0 gap-4">
      <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2">
        <h3 id="tmu11-t2" class="text-[0.8125rem] font-bold uppercase tracking-[0.1em]">After &mdash; 8 removed, 1 kept</h3>
        <p class="font-tmu11-mono text-xs text-tmu11-ink-2">Header rule at 3:1 &middot; hover tint replaces row rules</p>
      </div>
      <div class="min-w-0 overflow-x-auto rounded-xl bg-tmu11-surface px-2">
        <table class="w-full min-w-[22rem] border-collapse bg-tmu11-surface text-sm">
          <caption class="sr-only">Regional revenue, audited version</caption>
          <thead><tr><th scope="col" class="whitespace-nowrap px-3.5 py-3 text-[0.6875rem] font-bold uppercase tracking-[0.1em] text-tmu11-ink-2 text-left border-b border-tmu11-line-strong">Region</th><th scope="col" class="whitespace-nowrap px-3.5 py-3 text-[0.6875rem] font-bold uppercase tracking-[0.1em] text-tmu11-ink-2 text-right border-b border-tmu11-line-strong">Accounts</th><th scope="col" class="whitespace-nowrap px-3.5 py-3 text-[0.6875rem] font-bold uppercase tracking-[0.1em] text-tmu11-ink-2 text-right border-b border-tmu11-line-strong">MRR</th><th scope="col" class="whitespace-nowrap px-3.5 py-3 text-[0.6875rem] font-bold uppercase tracking-[0.1em] text-tmu11-ink-2 text-right border-b border-tmu11-line-strong">Change</th></tr></thead>
          <tbody>
            <tr class="transition-colors duration-150 hover:bg-tmu11-surface-2 motion-reduce:transition-none"><th scope="row" class="px-3.5 py-3 text-left font-medium first:rounded-l-lg">Nordics</th><td class="px-3.5 py-3 text-right tabular-nums">184</td><td class="px-3.5 py-3 text-right tabular-nums">$92,400</td><td class="px-3.5 py-3 text-right tabular-nums text-tmu11-ink rounded-r-lg">+4.2%</td></tr>
            <tr class="transition-colors duration-150 hover:bg-tmu11-surface-2 motion-reduce:transition-none"><th scope="row" class="px-3.5 py-3 text-left font-medium first:rounded-l-lg">DACH</th><td class="px-3.5 py-3 text-right tabular-nums">231</td><td class="px-3.5 py-3 text-right tabular-nums">$118,900</td><td class="px-3.5 py-3 text-right tabular-nums text-tmu11-ink rounded-r-lg">+1.8%</td></tr>
            <tr class="transition-colors duration-150 hover:bg-tmu11-surface-2 motion-reduce:transition-none"><th scope="row" class="px-3.5 py-3 text-left font-medium first:rounded-l-lg">Benelux</th><td class="px-3.5 py-3 text-right tabular-nums">96</td><td class="px-3.5 py-3 text-right tabular-nums">$41,300</td><td class="px-3.5 py-3 text-right tabular-nums text-tmu11-acc rounded-r-lg">&minus;0.6%</td></tr>
            <tr class="transition-colors duration-150 hover:bg-tmu11-surface-2 motion-reduce:transition-none"><th scope="row" class="px-3.5 py-3 text-left font-medium first:rounded-l-lg">Iberia</th><td class="px-3.5 py-3 text-right tabular-nums">74</td><td class="px-3.5 py-3 text-right tabular-nums">$28,750</td><td class="px-3.5 py-3 text-right tabular-nums text-tmu11-ink rounded-r-lg">+6.1%</td></tr>
          </tbody>
        </table>
      </div>
    </section>
    <section aria-labelledby="tmu11-t3" class="grid min-w-0 gap-4">
      <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2">
        <h3 id="tmu11-t3" class="text-[0.8125rem] font-bold uppercase tracking-[0.1em]">Card set &mdash; borders removed</h3>
        <p class="font-tmu11-mono text-xs text-tmu11-ink-2">Tone and padding replace the outline</p>
      </div>
      <ul class="grid gap-4 grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))]">
        <li class="group grid min-w-0 content-start gap-2 rounded-xl bg-tmu11-surface p-5 transition-colors duration-150 has-[a:hover]:bg-tmu11-surface-2 md:p-7 motion-reduce:transition-none">
          <p class="font-tmu11-mono text-[0.6875rem] uppercase tracking-[0.12em] text-tmu11-ink-2">Fern</p>
          <h4 class="text-[1.0625rem]/[1.25] font-bold tracking-[-0.014em]">Support inbox</h4>
          <p class="text-sm text-tmu11-ink-2 text-pretty">14 open, 3 waiting on a customer reply. Median first response 42 minutes.</p>
          <a href="#tmu11-title" class="inline-flex min-h-11 items-center gap-1.5 justify-self-start text-sm font-semibold text-tmu11-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu11-acc motion-reduce:transition-none">Open queue<svg class="size-4 transition-transform duration-150 group-has-[a:hover]:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
        </li>
        <li class="group grid min-w-0 content-start gap-2 rounded-xl bg-tmu11-surface p-5 transition-colors duration-150 has-[a:hover]:bg-tmu11-surface-2 md:p-7 motion-reduce:transition-none">
          <p class="font-tmu11-mono text-[0.6875rem] uppercase tracking-[0.12em] text-tmu11-ink-2">Talon</p>
          <h4 class="text-[1.0625rem]/[1.25] font-bold tracking-[-0.014em]">Renewals this month</h4>
          <p class="text-sm text-tmu11-ink-2 text-pretty">9 contracts, $214,000 combined. Two need a signature before the 14th.</p>
          <a href="#tmu11-title" class="inline-flex min-h-11 items-center gap-1.5 justify-self-start text-sm font-semibold text-tmu11-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu11-acc motion-reduce:transition-none">Review renewals<svg class="size-4 transition-transform duration-150 group-has-[a:hover]:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
        </li>
        <li class="group grid min-w-0 content-start gap-2 rounded-xl bg-tmu11-surface p-5 transition-colors duration-150 has-[a:hover]:bg-tmu11-surface-2 md:p-7 motion-reduce:transition-none">
          <p class="font-tmu11-mono text-[0.6875rem] uppercase tracking-[0.12em] text-tmu11-ink-2">Quill</p>
          <h4 class="text-[1.0625rem]/[1.25] font-bold tracking-[-0.014em]">Draft releases</h4>
          <p class="text-sm text-tmu11-ink-2 text-pretty">Draft saved 6 minutes ago by Alex Chen. No blocking review comments.</p>
          <a href="#tmu11-title" class="inline-flex min-h-11 items-center gap-1.5 justify-self-start text-sm font-semibold text-tmu11-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu11-acc motion-reduce:transition-none">Continue editing<svg class="size-4 transition-transform duration-150 group-has-[a:hover]:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
        </li>
      </ul>
    </section>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu11-bg: light-dark(#f2ece7, #16130f);
  --color-tmu11-bg: light-dark(oklch(93.5% 0.012 55), oklch(18.5% 0.008 50));
  --color-tmu11-surface: light-dark(#fbf7f4, #1f1b16);
  --color-tmu11-surface: light-dark(oklch(98% 0.007 60), oklch(23% 0.01 52));
  --color-tmu11-surface-2: light-dark(#e8e0d9, #2a241d);
  --color-tmu11-surface-2: light-dark(oklch(90% 0.014 58), oklch(27.5% 0.013 55));
  --color-tmu11-ink: light-dark(#1e1a17, #f4efe9);
  --color-tmu11-ink: light-dark(oklch(21.5% 0.01 50), oklch(96% 0.008 60));
  --color-tmu11-ink-2: light-dark(#57504a, #b2a89d);
  --color-tmu11-ink-2: light-dark(oklch(45% 0.012 52), oklch(75% 0.014 58));
  --color-tmu11-line: light-dark(#d6cbc1, #3c342b);
  --color-tmu11-line: light-dark(oklch(85% 0.016 58), oklch(33% 0.014 55));
  --color-tmu11-line-strong: light-dark(#7d726a, #97897c);
  --color-tmu11-line-strong: light-dark(oklch(54% 0.018 55), oklch(64% 0.018 58));
  --color-tmu11-acc: light-dark(#8c3b1c, #e8956a);
  --color-tmu11-acc: light-dark(oklch(45% 0.13 40), oklch(76% 0.12 45));
  --font-tmu11-ui: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
  --font-tmu11-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-11:has(#tmu11-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-11:has(#tmu11-theme:checked) {
    color-scheme: light;
  }
}
```
