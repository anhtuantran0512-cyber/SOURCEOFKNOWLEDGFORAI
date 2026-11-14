---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-portfolio-project-list/"
title: "Tailwind Minimalist Portfolio Project Listing"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "A portfolio index as six text rows: name, discipline, year and an arrow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Portfolio Project Listing
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-portfolio-project-list/

A portfolio index as six text rows: name, discipline, year and an arrow. No thumbnails, no cards. On hover or keyboard focus the row tints, its rule turns accent, the name drifts 2px and the arrow travels 4px &mdash; every movement a group-hover: / group-focus-visible: pair, with a colour-only fallback under motion-reduce:.
## HTML
```html
<section class="tmu-17 relative w-full min-h-svh bg-tmu17-bg font-tmu17-ui text-tmu17-ink antialiased" aria-labelledby="tmu17-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu17-theme" type="checkbox" class="peer sr-only">
    <label for="tmu17-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu17-line bg-tmu17-bg text-tmu17-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu17-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu17-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[62rem] gap-10 px-5 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu17-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu17-ink-2"><span class="tabular-nums text-tmu17-acc">17</span><span aria-hidden="true" class="h-px w-6 bg-tmu17-line"></span>Vera Lindstr&ouml;m &middot; Portfolio</p>
      <h2 id="tmu17-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Selected work, 2022&ndash;2026</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu17-ink-2 text-pretty">Six projects, one line each. The list is the design &mdash; hover or tab through it and every row answers the same way.</p>
    </header>
    <nav aria-label="Project index" class="min-w-0">
      <ul class="border-t border-tmu17-line">
        <li class="min-w-0 border-b border-tmu17-line transition-colors duration-150 hover:border-tmu17-acc has-focus-visible:border-tmu17-acc motion-reduce:transition-none">
          <a href="#tmu17-title" class="group -mx-3 grid min-h-11 min-w-0 grid-cols-[minmax(0,1fr)_auto_1.25rem] items-baseline gap-x-4 gap-y-0.5 rounded-lg px-3 py-[1.125rem] text-tmu17-ink no-underline transition-colors duration-150 hover:bg-tmu17-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu17-ring sm:grid-cols-[minmax(0,1fr)_minmax(0,14rem)_4rem_1.5rem] sm:items-center motion-reduce:transition-none">
            <span class="col-start-1 min-w-0 text-[clamp(1.0625rem,1rem+0.5vw,1.375rem)] font-medium leading-[1.2] tracking-[-0.018em] text-pretty transition-transform duration-200 group-hover:translate-x-0.5 group-focus-visible:translate-x-0.5 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0">Meridian platform rebuild</span>
            <span class="col-start-1 row-start-2 min-w-0 text-[0.8125rem] text-tmu17-ink-2 sm:col-start-2 sm:row-start-1">Product design &middot; 8 months</span>
            <span class="col-start-2 row-start-1 font-tmu17-mono text-[0.8125rem] tabular-nums text-tmu17-ink-2 sm:col-start-3 sm:justify-self-end">2026</span>
            <svg class="col-start-3 row-start-1 size-5 text-tmu17-ink-2 transition-[translate,color] duration-200 group-hover:translate-x-1 group-hover:text-tmu17-acc group-focus-visible:translate-x-1 group-focus-visible:text-tmu17-acc sm:col-start-4 sm:justify-self-end motion-reduce:transition-colors motion-reduce:group-hover:translate-x-0 motion-reduce:group-focus-visible:translate-x-0" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="min-w-0 border-b border-tmu17-line transition-colors duration-150 hover:border-tmu17-acc has-focus-visible:border-tmu17-acc motion-reduce:transition-none">
          <a href="#tmu17-title" class="group -mx-3 grid min-h-11 min-w-0 grid-cols-[minmax(0,1fr)_auto_1.25rem] items-baseline gap-x-4 gap-y-0.5 rounded-lg px-3 py-[1.125rem] text-tmu17-ink no-underline transition-colors duration-150 hover:bg-tmu17-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu17-ring sm:grid-cols-[minmax(0,1fr)_minmax(0,14rem)_4rem_1.5rem] sm:items-center motion-reduce:transition-none">
            <span class="col-start-1 min-w-0 text-[clamp(1.0625rem,1rem+0.5vw,1.375rem)] font-medium leading-[1.2] tracking-[-0.018em] text-pretty transition-transform duration-200 group-hover:translate-x-0.5 group-focus-visible:translate-x-0.5 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0">Basalt identity and type system</span>
            <span class="col-start-1 row-start-2 min-w-0 text-[0.8125rem] text-tmu17-ink-2 sm:col-start-2 sm:row-start-1">Brand &middot; with Priya Sharma</span>
            <span class="col-start-2 row-start-1 font-tmu17-mono text-[0.8125rem] tabular-nums text-tmu17-ink-2 sm:col-start-3 sm:justify-self-end">2025</span>
            <svg class="col-start-3 row-start-1 size-5 text-tmu17-ink-2 transition-[translate,color] duration-200 group-hover:translate-x-1 group-hover:text-tmu17-acc group-focus-visible:translate-x-1 group-focus-visible:text-tmu17-acc sm:col-start-4 sm:justify-self-end motion-reduce:transition-colors motion-reduce:group-hover:translate-x-0 motion-reduce:group-focus-visible:translate-x-0" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="min-w-0 border-b border-tmu17-line transition-colors duration-150 hover:border-tmu17-acc has-focus-visible:border-tmu17-acc motion-reduce:transition-none">
          <a href="#tmu17-title" class="group -mx-3 grid min-h-11 min-w-0 grid-cols-[minmax(0,1fr)_auto_1.25rem] items-baseline gap-x-4 gap-y-0.5 rounded-lg px-3 py-[1.125rem] text-tmu17-ink no-underline transition-colors duration-150 hover:bg-tmu17-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu17-ring sm:grid-cols-[minmax(0,1fr)_minmax(0,14rem)_4rem_1.5rem] sm:items-center motion-reduce:transition-none">
            <span class="col-start-1 min-w-0 text-[clamp(1.0625rem,1rem+0.5vw,1.375rem)] font-medium leading-[1.2] tracking-[-0.018em] text-pretty transition-transform duration-200 group-hover:translate-x-0.5 group-focus-visible:translate-x-0.5 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0">Orbit developer documentation</span>
            <span class="col-start-1 row-start-2 min-w-0 text-[0.8125rem] text-tmu17-ink-2 sm:col-start-2 sm:row-start-1">Information architecture</span>
            <span class="col-start-2 row-start-1 font-tmu17-mono text-[0.8125rem] tabular-nums text-tmu17-ink-2 sm:col-start-3 sm:justify-self-end">2025</span>
            <svg class="col-start-3 row-start-1 size-5 text-tmu17-ink-2 transition-[translate,color] duration-200 group-hover:translate-x-1 group-hover:text-tmu17-acc group-focus-visible:translate-x-1 group-focus-visible:text-tmu17-acc sm:col-start-4 sm:justify-self-end motion-reduce:transition-colors motion-reduce:group-hover:translate-x-0 motion-reduce:group-focus-visible:translate-x-0" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="min-w-0 border-b border-tmu17-line transition-colors duration-150 hover:border-tmu17-acc has-focus-visible:border-tmu17-acc motion-reduce:transition-none">
          <a href="#tmu17-title" class="group -mx-3 grid min-h-11 min-w-0 grid-cols-[minmax(0,1fr)_auto_1.25rem] items-baseline gap-x-4 gap-y-0.5 rounded-lg px-3 py-[1.125rem] text-tmu17-ink no-underline transition-colors duration-150 hover:bg-tmu17-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu17-ring sm:grid-cols-[minmax(0,1fr)_minmax(0,14rem)_4rem_1.5rem] sm:items-center motion-reduce:transition-none">
            <span class="col-start-1 min-w-0 text-[clamp(1.0625rem,1rem+0.5vw,1.375rem)] font-medium leading-[1.2] tracking-[-0.018em] text-pretty transition-transform duration-200 group-hover:translate-x-0.5 group-focus-visible:translate-x-0.5 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0">Fern onboarding, mobile first</span>
            <span class="col-start-1 row-start-2 min-w-0 text-[0.8125rem] text-tmu17-ink-2 sm:col-start-2 sm:row-start-1">Product design &middot; iOS and Android</span>
            <span class="col-start-2 row-start-1 font-tmu17-mono text-[0.8125rem] tabular-nums text-tmu17-ink-2 sm:col-start-3 sm:justify-self-end">2024</span>
            <svg class="col-start-3 row-start-1 size-5 text-tmu17-ink-2 transition-[translate,color] duration-200 group-hover:translate-x-1 group-hover:text-tmu17-acc group-focus-visible:translate-x-1 group-focus-visible:text-tmu17-acc sm:col-start-4 sm:justify-self-end motion-reduce:transition-colors motion-reduce:group-hover:translate-x-0 motion-reduce:group-focus-visible:translate-x-0" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="min-w-0 border-b border-tmu17-line transition-colors duration-150 hover:border-tmu17-acc has-focus-visible:border-tmu17-acc motion-reduce:transition-none">
          <a href="#tmu17-title" class="group -mx-3 grid min-h-11 min-w-0 grid-cols-[minmax(0,1fr)_auto_1.25rem] items-baseline gap-x-4 gap-y-0.5 rounded-lg px-3 py-[1.125rem] text-tmu17-ink no-underline transition-colors duration-150 hover:bg-tmu17-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu17-ring sm:grid-cols-[minmax(0,1fr)_minmax(0,14rem)_4rem_1.5rem] sm:items-center motion-reduce:transition-none">
            <span class="col-start-1 min-w-0 text-[clamp(1.0625rem,1rem+0.5vw,1.375rem)] font-medium leading-[1.2] tracking-[-0.018em] text-pretty transition-transform duration-200 group-hover:translate-x-0.5 group-focus-visible:translate-x-0.5 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0">Quill editorial commissioning tool</span>
            <span class="col-start-1 row-start-2 min-w-0 text-[0.8125rem] text-tmu17-ink-2 sm:col-start-2 sm:row-start-1">Interface design &middot; with Jordan Lee</span>
            <span class="col-start-2 row-start-1 font-tmu17-mono text-[0.8125rem] tabular-nums text-tmu17-ink-2 sm:col-start-3 sm:justify-self-end">2023</span>
            <svg class="col-start-3 row-start-1 size-5 text-tmu17-ink-2 transition-[translate,color] duration-200 group-hover:translate-x-1 group-hover:text-tmu17-acc group-focus-visible:translate-x-1 group-focus-visible:text-tmu17-acc sm:col-start-4 sm:justify-self-end motion-reduce:transition-colors motion-reduce:group-hover:translate-x-0 motion-reduce:group-focus-visible:translate-x-0" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="min-w-0 border-b border-tmu17-line transition-colors duration-150 hover:border-tmu17-acc has-focus-visible:border-tmu17-acc motion-reduce:transition-none">
          <a href="#tmu17-title" class="group -mx-3 grid min-h-11 min-w-0 grid-cols-[minmax(0,1fr)_auto_1.25rem] items-baseline gap-x-4 gap-y-0.5 rounded-lg px-3 py-[1.125rem] text-tmu17-ink no-underline transition-colors duration-150 hover:bg-tmu17-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu17-ring sm:grid-cols-[minmax(0,1fr)_minmax(0,14rem)_4rem_1.5rem] sm:items-center motion-reduce:transition-none">
            <span class="col-start-1 min-w-0 text-[clamp(1.0625rem,1rem+0.5vw,1.375rem)] font-medium leading-[1.2] tracking-[-0.018em] text-pretty transition-transform duration-200 group-hover:translate-x-0.5 group-focus-visible:translate-x-0.5 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0">Vale annual report</span>
            <span class="col-start-1 row-start-2 min-w-0 text-[0.8125rem] text-tmu17-ink-2 sm:col-start-2 sm:row-start-1">Editorial &middot; print and web</span>
            <span class="col-start-2 row-start-1 font-tmu17-mono text-[0.8125rem] tabular-nums text-tmu17-ink-2 sm:col-start-3 sm:justify-self-end">2022</span>
            <svg class="col-start-3 row-start-1 size-5 text-tmu17-ink-2 transition-[translate,color] duration-200 group-hover:translate-x-1 group-hover:text-tmu17-acc group-focus-visible:translate-x-1 group-focus-visible:text-tmu17-acc sm:col-start-4 sm:justify-self-end motion-reduce:transition-colors motion-reduce:group-hover:translate-x-0 motion-reduce:group-focus-visible:translate-x-0" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu17-bg: light-dark(#eef0f1, #121416);
  --color-tmu17-bg: light-dark(oklch(94.5% 0.003 220), oklch(18% 0.005 240));
  --color-tmu17-ink: light-dark(#15181a, #eef1f2);
  --color-tmu17-ink: light-dark(oklch(19.5% 0.005 240), oklch(95.5% 0.003 240));
  --color-tmu17-ink-2: light-dark(#4e565b, #a2aab0);
  --color-tmu17-ink-2: light-dark(oklch(45% 0.008 240), oklch(74% 0.008 240));
  --color-tmu17-line: light-dark(#c9ced1, #333a3e);
  --color-tmu17-line: light-dark(oklch(84.5% 0.005 240), oklch(33% 0.009 240));
  --color-tmu17-acc: light-dark(#15181a, #eef1f2);
  --color-tmu17-acc: light-dark(oklch(19.5% 0.005 240), oklch(95.5% 0.003 240));
  --color-tmu17-ring: light-dark(#1f5fd0, #8ab4ff);
  --color-tmu17-ring: light-dark(oklch(48% 0.17 262), oklch(80% 0.12 262));
  --color-tmu17-hover: color-mix(in oklab, var(--color-tmu17-ink) 4%, transparent);
  --font-tmu17-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu17-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-17:has(#tmu17-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-17:has(#tmu17-theme:checked) {
    color-scheme: light;
  }
}
```
