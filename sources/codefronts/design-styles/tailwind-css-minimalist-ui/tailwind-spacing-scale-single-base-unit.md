---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-spacing-scale-single-base-unit/"
title: "Tailwind Spacing Scale from a Single Base Unit"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "Tailwind v4 already is a single-base-unit system: every p-*, gap-* and m-* is calc(var(--spacing) * n)."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Spacing Scale from a Single Base Unit
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-spacing-scale-single-base-unit/

Tailwind v4 already is a single-base-unit system: every p-*, gap-* and m-* is calc(var(--spacing) * n). This demo draws that scale as a ruler, then puts the same deployment card side by side &mdash; once with arbitrary p-[13px]-style values, once on the 8px steps &mdash; so the cost of escaping the scale is visible.
## HTML
```html
<section class="tmu-05 relative w-full min-h-svh bg-tmu05-bg font-tmu05-ui text-tmu05-ink antialiased" aria-labelledby="tmu05-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu05-theme" type="checkbox" class="peer sr-only">
    <label for="tmu05-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu05-line bg-tmu05-surface text-tmu05-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu05-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu05-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[74rem] gap-12 px-6 pt-20 pb-16 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu05-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu05-ink-2"><span class="tabular-nums text-tmu05-acc">05</span><span aria-hidden="true" class="h-px w-6 bg-tmu05-line"></span>Spacing</p>
      <h2 id="tmu05-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Every gap is a multiple of one unit</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu05-ink-2 text-pretty">Tailwind’s scale is <code class="font-tmu05-mono text-[0.9em]">calc(var(--spacing) * n)</code>. Stay on it and components line up without trying; step off it and every card becomes a one-off.</p>
    </header>
    <section aria-labelledby="tmu05-ruler" class="grid min-w-0 gap-4 rounded-xl border border-tmu05-line bg-tmu05-surface p-6">
      <h3 id="tmu05-ruler" class="font-tmu05-mono text-xs font-medium uppercase tracking-[0.1em]">The scale &middot; base 8px</h3>
      <ul class="grid min-w-0 gap-2">
        <li class="grid min-w-0 grid-cols-[2.25rem_6.5rem_minmax(0,1fr)] items-center gap-4 py-0.5 font-tmu05-mono text-xs tabular-nums"><b class="font-medium">s1</b><i class="not-italic text-tmu05-ink-2">gap-2 &middot; 8px</i><span class="block h-2.5 rounded-sm bg-tmu05-acc w-[calc(var(--spacing)*2)]"></span></li>
        <li class="grid min-w-0 grid-cols-[2.25rem_6.5rem_minmax(0,1fr)] items-center gap-4 py-0.5 font-tmu05-mono text-xs tabular-nums"><b class="font-medium">s2</b><i class="not-italic text-tmu05-ink-2">gap-4 &middot; 16px</i><span class="block h-2.5 rounded-sm bg-tmu05-acc w-[calc(var(--spacing)*4)]"></span></li>
        <li class="grid min-w-0 grid-cols-[2.25rem_6.5rem_minmax(0,1fr)] items-center gap-4 py-0.5 font-tmu05-mono text-xs tabular-nums"><b class="font-medium">s3</b><i class="not-italic text-tmu05-ink-2">gap-6 &middot; 24px</i><span class="block h-2.5 rounded-sm bg-tmu05-acc w-[calc(var(--spacing)*6)]"></span></li>
        <li class="grid min-w-0 grid-cols-[2.25rem_6.5rem_minmax(0,1fr)] items-center gap-4 py-0.5 font-tmu05-mono text-xs tabular-nums"><b class="font-medium">s4</b><i class="not-italic text-tmu05-ink-2">gap-8 &middot; 32px</i><span class="block h-2.5 rounded-sm bg-tmu05-acc w-[calc(var(--spacing)*8)]"></span></li>
        <li class="grid min-w-0 grid-cols-[2.25rem_6.5rem_minmax(0,1fr)] items-center gap-4 py-0.5 font-tmu05-mono text-xs tabular-nums"><b class="font-medium">s5</b><i class="not-italic text-tmu05-ink-2">gap-12 &middot; 48px</i><span class="block h-2.5 rounded-sm bg-tmu05-acc w-[calc(var(--spacing)*12)]"></span></li>
        <li class="grid min-w-0 grid-cols-[2.25rem_6.5rem_minmax(0,1fr)] items-center gap-4 py-0.5 font-tmu05-mono text-xs tabular-nums"><b class="font-medium">s6</b><i class="not-italic text-tmu05-ink-2">gap-16 &middot; 64px</i><span class="block h-2.5 rounded-sm bg-tmu05-acc w-[calc(var(--spacing)*16)]"></span></li>
      </ul>
    </section>
    <div class="grid gap-6 md:grid-cols-2">
      <article aria-labelledby="tmu05-bad" class="grid min-w-0 content-start gap-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-tmu05-line pb-2">
          <h3 id="tmu05-bad" class="inline-flex items-center gap-2 font-tmu05-mono text-xs font-medium uppercase tracking-[0.1em]"><span aria-hidden="true" class="size-2 rounded-full bg-tmu05-bad"></span>Arbitrary values</h3>
          <p class="font-tmu05-mono text-xs tabular-nums text-tmu05-ink-2">13 &middot; 17 &middot; 22 &middot; 9 &middot; 31</p>
        </div>
        <div class="min-w-0 rounded-lg border border-tmu05-line bg-tmu05-surface pt-[17px] px-[13px] pb-[22px]">
          <p class="font-tmu05-mono text-[0.6875rem] uppercase tracking-[0.1em] text-tmu05-ink-2 mb-[9px]">Deployment</p>
          <h4 class="text-xl/[1.2] font-semibold tracking-[-0.018em] mb-[11px]">Orbit API, region eu-west</h4>
          <p class="max-w-[46ch] text-[0.9375rem] text-tmu05-ink-2 text-pretty mb-[22px]">Rolled out to 34 of 34 instances. No error budget consumed in the last hour.</p>
          <ul class="flex flex-wrap font-tmu05-mono text-xs text-tmu05-ink-2 gap-x-[13px] gap-y-[6px] mb-[31px]"><li>Build 4c19f0</li><li>Jordan Lee</li><li>11 min ago</li></ul>
          <div class="flex flex-wrap gap-[9px]">
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu05-acc motion-reduce:transition-none border-tmu05-acc bg-tmu05-acc text-tmu05-acc-ink hover:bg-tmu05-acc-hover hover:border-tmu05-acc-hover">Promote to production</button>
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu05-acc motion-reduce:transition-none border-tmu05-line text-tmu05-ink hover:border-tmu05-ink">Roll back</button>
          </div>
        </div>
      </article>
      <article aria-labelledby="tmu05-good" class="grid min-w-0 content-start gap-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-tmu05-line pb-2">
          <h3 id="tmu05-good" class="inline-flex items-center gap-2 font-tmu05-mono text-xs font-medium uppercase tracking-[0.1em]"><span aria-hidden="true" class="size-2 rounded-full bg-tmu05-acc"></span>8px scale</h3>
          <p class="font-tmu05-mono text-xs tabular-nums text-tmu05-ink-2">8 &middot; 16 &middot; 24 &middot; 32</p>
        </div>
        <div class="min-w-0 rounded-lg border border-tmu05-line bg-tmu05-surface grid content-start gap-4 p-8">
          <p class="font-tmu05-mono text-[0.6875rem] uppercase tracking-[0.1em] text-tmu05-ink-2">Deployment</p>
          <h4 class="text-xl/[1.2] font-semibold tracking-[-0.018em]">Orbit API, region eu-west</h4>
          <p class="max-w-[46ch] text-[0.9375rem] text-tmu05-ink-2 text-pretty">Rolled out to 34 of 34 instances. No error budget consumed in the last hour.</p>
          <ul class="flex flex-wrap font-tmu05-mono text-xs text-tmu05-ink-2 gap-x-4 gap-y-2"><li>Build 4c19f0</li><li>Jordan Lee</li><li>11 min ago</li></ul>
          <div class="flex flex-wrap mt-2 gap-2">
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu05-acc motion-reduce:transition-none border-tmu05-acc bg-tmu05-acc text-tmu05-acc-ink hover:bg-tmu05-acc-hover hover:border-tmu05-acc-hover">Promote to production</button>
            <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-center rounded-md border px-4 text-sm font-medium cursor-pointer transition-[border-color,background-color] duration-150 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu05-acc motion-reduce:transition-none border-tmu05-line text-tmu05-ink hover:border-tmu05-ink">Roll back</button>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu05-bg: light-dark(#eef1ea, #101310);
  --color-tmu05-bg: light-dark(oklch(94.5% 0.014 140), oklch(17.5% 0.008 140));
  --color-tmu05-surface: light-dark(#fbfcf9, #181d18);
  --color-tmu05-surface: light-dark(oklch(98.8% 0.006 140), oklch(22.5% 0.01 140));
  --color-tmu05-ink: light-dark(#161a15, #eef2ec);
  --color-tmu05-ink: light-dark(oklch(19.5% 0.012 140), oklch(95.5% 0.008 140));
  --color-tmu05-ink-2: light-dark(#4e564c, #a5ad9f);
  --color-tmu05-ink-2: light-dark(oklch(44% 0.016 140), oklch(74% 0.014 140));
  --color-tmu05-line: light-dark(#ccd3c6, #333a31);
  --color-tmu05-line: light-dark(oklch(85% 0.018 140), oklch(33% 0.014 140));
  --color-tmu05-acc: light-dark(#1f6b3f, #6ed49a);
  --color-tmu05-acc: light-dark(oklch(46% 0.11 155), oklch(82% 0.13 155));
  --color-tmu05-acc-ink: light-dark(#ffffff, #0b1a0f);
  --color-tmu05-acc-ink: light-dark(oklch(100% 0 0), oklch(16% 0.02 155));
  --color-tmu05-bad: light-dark(#b4462f, #f08c73);
  --color-tmu05-bad: light-dark(oklch(52% 0.15 35), oklch(74% 0.13 35));
  --color-tmu05-acc-hover: color-mix(in oklab, var(--color-tmu05-acc) 86%, var(--color-tmu05-ink));
  --font-tmu05-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --font-tmu05-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-05:has(#tmu05-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-05:has(#tmu05-theme:checked) {
    color-scheme: light;
  }
}
```
