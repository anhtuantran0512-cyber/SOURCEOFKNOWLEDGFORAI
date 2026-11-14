---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-landing-page-section/"
title: "Tailwind Minimalist Landing Page Section"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "A landing section that sells with a sentence, not a scene: kicker, a balanced headline at a fluid clamp() size, one paragraph, one filled call to action and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Landing Page Section
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-landing-page-section/

A landing section that sells with a sentence, not a scene: kicker, a balanced headline at a fluid clamp() size, one paragraph, one filled call to action and one underlined secondary link, then three proof points. A 3px accent bar is the only decoration &mdash; everything else is type, space and the restraint of a single colour.
## HTML
```html
<section class="tmu-20 relative w-full min-h-svh bg-tmu20-bg font-tmu20-ui text-tmu20-ink antialiased" aria-labelledby="tmu20-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu20-theme" type="checkbox" class="peer sr-only">
    <label for="tmu20-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu20-line bg-tmu20-surface text-tmu20-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu20-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu20-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid min-h-svh max-w-[76rem] content-start gap-12 px-5 py-20 lg:place-content-center lg:px-12 lg:py-28">
    <div class="grid min-w-0 max-w-[44rem] content-start gap-5 border-l-[3px] border-tmu20-acc pl-5 lg:pl-7">
      <p class="font-tmu20-mono text-xs uppercase tracking-[0.12em] text-tmu20-ink-2">Meridian</p>
      <h2 id="tmu20-title" class="text-[clamp(2.25rem,1.6rem+3.4vw,4rem)] font-semibold leading-[1.02] tracking-[-0.036em] text-balance">Ship the release, not the release notes</h2>
      <p class="max-w-[52ch] text-[clamp(1.0625rem,1rem+0.5vw,1.25rem)] leading-[1.45] text-tmu20-ink-2 text-pretty">Meridian turns your deploy pipeline into one reviewable timeline, so the person on call can see what changed without reading nine dashboards.</p>
      <div class="flex flex-wrap items-center gap-x-6 gap-y-3 pt-2">
        <button type="button" class="group inline-flex min-h-12 min-w-11 items-center justify-center gap-2 rounded-md bg-tmu20-acc px-6 text-[0.9375rem] font-semibold text-tmu20-acc-ink cursor-pointer shadow-[0_1px_2px_rgb(0_0_0/0.1)] transition-[translate,box-shadow] duration-150 hover:-translate-y-px hover:shadow-[0_8px_20px_-10px_var(--color-tmu20-acc)] active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tmu20-ink motion-reduce:transition-none motion-reduce:hover:translate-y-0">Start a 14-day trial<svg class="size-[18px] transition-transform duration-150 group-hover:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
        <a href="#tmu20-title" class="inline-flex min-h-11 items-center text-[0.9375rem] font-medium text-tmu20-ink underline decoration-1 underline-offset-[3px] hover:decoration-2 focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tmu20-acc">Read the documentation</a>
        <p class="basis-full text-xs text-tmu20-ink-2">No card required &middot; cancel in one click</p>
      </div>
      <dl class="grid gap-4 border-t border-tmu20-line pt-6 grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))]">
        <div class="grid min-w-0 gap-0.5"><dt class="text-xs uppercase tracking-[0.06em] text-tmu20-ink-2">Median time to first deploy</dt><dd class="text-[0.9375rem] font-semibold tabular-nums text-pretty">11 minutes</dd></div>
        <div class="grid min-w-0 gap-0.5"><dt class="text-xs uppercase tracking-[0.06em] text-tmu20-ink-2">Teams running Meridian</dt><dd class="text-[0.9375rem] font-semibold tabular-nums text-pretty">Basalt, Fern, Orbit, Prism</dd></div>
        <div class="grid min-w-0 gap-0.5"><dt class="text-xs uppercase tracking-[0.06em] text-tmu20-ink-2">Compliance</dt><dd class="text-[0.9375rem] font-semibold tabular-nums text-pretty">SOC 2 Type II, ISO 27001</dd></div>
      </dl>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu20-bg: light-dark(#f8f6f1, #131215);
  --color-tmu20-bg: light-dark(oklch(97% 0.007 85), oklch(18% 0.006 285));
  --color-tmu20-surface: light-dark(#ffffff, #1c1b20);
  --color-tmu20-surface: light-dark(oklch(100% 0 0), oklch(23% 0.008 285));
  --color-tmu20-ink: light-dark(#17161a, #f2f1f4);
  --color-tmu20-ink: light-dark(oklch(19.5% 0.006 285), oklch(96% 0.004 285));
  --color-tmu20-ink-2: light-dark(#55535c, #aaa7b3);
  --color-tmu20-ink-2: light-dark(oklch(45% 0.012 285), oklch(74% 0.012 285));
  --color-tmu20-line: light-dark(#d8d4ca, #363441);
  --color-tmu20-line: light-dark(oklch(86% 0.011 85), oklch(33% 0.014 285));
  --color-tmu20-acc: light-dark(#3a2ea8, #a99cff);
  --color-tmu20-acc: light-dark(oklch(40% 0.19 285), oklch(76% 0.15 285));
  --color-tmu20-acc-ink: light-dark(#ffffff, #14112b);
  --color-tmu20-acc-ink: light-dark(oklch(100% 0 0), oklch(18% 0.04 285));
  --font-tmu20-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu20-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-20:has(#tmu20-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-20:has(#tmu20-theme:checked) {
    color-scheme: light;
  }
}
```
