---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-semantic-html-css-grid-no-divs/"
title: "Tailwind Minimal Layout with CSS Grid and No Divs"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "One release card, two builds."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimal Layout with CSS Grid and No Divs
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-semantic-html-css-grid-no-divs/

One release card, two builds. The left is a row/column div tree &mdash; fourteen elements, five of which exist only for layout. The right is an <article> with a header, two paragraphs and a list, placed by grid-areas-[...] on the parent: nine elements, zero wrappers, identical rendering, and a document outline a screen reader can navigate.
## HTML
```html
<section class="tmu-08 relative w-full min-h-svh bg-tmu08-bg font-tmu08-ui text-tmu08-ink antialiased" aria-labelledby="tmu08-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu08-theme" type="checkbox" class="peer sr-only">
    <label for="tmu08-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu08-line bg-tmu08-surface text-tmu08-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu08-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu08-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[74rem] gap-12 px-6 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu08-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu08-ink-2"><span class="tabular-nums text-tmu08-acc">08</span><span aria-hidden="true" class="h-px w-6 bg-tmu08-line"></span>Markup</p>
      <h2 id="tmu08-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Minimal markup is part of minimal design</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu08-ink-2 text-pretty">Identical cards. One is built from wrappers, the other from meaning &mdash; and the grid on the parent does the layout the wrappers were pretending to do.</p>
    </header>
    <div class="grid gap-6 md:grid-cols-2">
      <section aria-labelledby="tmu08-a" class="grid min-w-0 content-start gap-4 rounded-xl border border-tmu08-line bg-tmu08-surface p-5">
        <header class="flex flex-wrap items-baseline justify-between gap-2">
          <h3 id="tmu08-a" class="text-[0.8125rem] font-semibold uppercase tracking-[0.1em]">Div-heavy</h3>
          <p class="rounded-full bg-tmu08-code text-tmu08-ink-2 px-2.5 py-0.5 font-tmu08-mono text-xs">14 elements &middot; 5 wrappers</p>
        </header>
        <div class="grid min-w-0 gap-3 rounded-lg border border-tmu08-line p-5">
          <div class="grid grid-cols-[minmax(0,1fr)_auto] gap-3">
            <div class="grid min-w-0 content-start gap-0.5">
              <div class="font-tmu08-mono text-[0.6875rem] uppercase tracking-[0.1em] text-tmu08-ink-2">Release 4.2</div>
              <div class="text-lg/[1.2] font-semibold tracking-[-0.016em]">Prism Query Engine</div>
            </div>
            <div class="grid justify-items-end"><div class="font-tmu08-mono text-lg font-medium tabular-nums text-tmu08-acc">+18%</div></div>
          </div>
          <div class="grid"><div class="text-[0.9375rem] text-tmu08-ink-2 text-pretty">Cold-start latency down across all regions after the planner rewrite.</div></div>
          <div class="grid"><div class="flex flex-wrap gap-x-4 gap-y-2 border-t border-tmu08-line pt-2"><div><a href="#tmu08-title" class="inline-flex min-h-11 items-center gap-1 text-sm font-medium text-tmu08-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu08-acc motion-reduce:transition-none">Changelog</a></div><div><a href="#tmu08-title" class="inline-flex min-h-11 items-center gap-1 text-sm font-medium text-tmu08-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu08-acc motion-reduce:transition-none">Migration notes</a></div><div><a href="#tmu08-title" class="inline-flex min-h-11 items-center gap-1 text-sm font-medium text-tmu08-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu08-acc motion-reduce:transition-none">Benchmarks</a></div></div></div>
        </div>
        <pre class="min-w-0 overflow-x-auto rounded-lg border border-tmu08-line bg-tmu08-code p-3.5 font-tmu08-mono text-xs leading-[1.6] text-tmu08-ink-2"><code class="whitespace-pre">&lt;div class="card"&gt;
  &lt;div class="row"&gt;
    &lt;div class="col"&gt;&hellip;&lt;/div&gt;
    &lt;div class="col end"&gt;&hellip;&lt;/div&gt;
  &lt;/div&gt;
  &lt;div class="row"&gt;&hellip;&lt;/div&gt;
&lt;/div&gt;</code></pre>
      </section>
      <section aria-labelledby="tmu08-b" class="grid min-w-0 content-start gap-4 rounded-xl border border-tmu08-acc bg-tmu08-surface p-5">
        <header class="flex flex-wrap items-baseline justify-between gap-2">
          <h3 id="tmu08-b" class="text-[0.8125rem] font-semibold uppercase tracking-[0.1em]">Semantic</h3>
          <p class="rounded-full bg-tmu08-acc text-tmu08-acc-ink px-2.5 py-0.5 font-tmu08-mono text-xs">9 elements &middot; 0 wrappers</p>
        </header>
        <article class="grid min-w-0 grid-cols-[minmax(0,1fr)_auto] gap-3 rounded-lg border border-tmu08-line p-5 [grid-template-areas:'head_stat'_'text_text'_'links_links']">
          <header class="grid min-w-0 gap-0.5 [grid-area:head]">
            <p class="font-tmu08-mono text-[0.6875rem] uppercase tracking-[0.1em] text-tmu08-ink-2">Release 4.2</p>
            <h4 class="text-lg/[1.2] font-semibold tracking-[-0.016em]">Prism Query Engine</h4>
          </header>
          <p class="justify-self-end font-tmu08-mono text-lg font-medium tabular-nums text-tmu08-acc [grid-area:stat]">+18%</p>
          <p class="text-[0.9375rem] text-tmu08-ink-2 text-pretty [grid-area:text]">Cold-start latency down across all regions after the planner rewrite.</p>
          <ul class="flex flex-wrap gap-x-4 gap-y-2 border-t border-tmu08-line pt-2 [grid-area:links]"><li><a href="#tmu08-title" class="inline-flex min-h-11 items-center gap-1 text-sm font-medium text-tmu08-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu08-acc motion-reduce:transition-none">Changelog</a></li><li><a href="#tmu08-title" class="inline-flex min-h-11 items-center gap-1 text-sm font-medium text-tmu08-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu08-acc motion-reduce:transition-none">Migration notes</a></li><li><a href="#tmu08-title" class="inline-flex min-h-11 items-center gap-1 text-sm font-medium text-tmu08-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu08-acc motion-reduce:transition-none">Benchmarks</a></li></ul>
        </article>
        <pre class="min-w-0 overflow-x-auto rounded-lg border border-tmu08-line bg-tmu08-code p-3.5 font-tmu08-mono text-xs leading-[1.6] text-tmu08-ink-2"><code class="whitespace-pre">&lt;article class="grid [grid-template-areas:…]"&gt;
  &lt;header class="[grid-area:head]"&gt;&hellip;&lt;/header&gt;
  &lt;p class="[grid-area:stat]"&gt;&hellip;&lt;/p&gt;
  &lt;p class="[grid-area:text]"&gt;&hellip;&lt;/p&gt;
  &lt;ul class="[grid-area:links]"&gt;&hellip;&lt;/ul&gt;
&lt;/article&gt;</code></pre>
      </section>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu08-bg: light-dark(#eceef0, #101315);
  --color-tmu08-bg: light-dark(oklch(94% 0.004 240), oklch(17.5% 0.006 250));
  --color-tmu08-surface: light-dark(#ffffff, #191d20);
  --color-tmu08-surface: light-dark(oklch(100% 0 0), oklch(23% 0.007 250));
  --color-tmu08-code: light-dark(#f4f6f7, #12171a);
  --color-tmu08-code: light-dark(oklch(97% 0.003 240), oklch(19.5% 0.008 250));
  --color-tmu08-ink: light-dark(#16191c, #eef1f3);
  --color-tmu08-ink: light-dark(oklch(20% 0.008 250), oklch(95.5% 0.004 250));
  --color-tmu08-ink-2: light-dark(#4d565e, #a4adb4);
  --color-tmu08-ink-2: light-dark(oklch(44% 0.014 250), oklch(74% 0.01 250));
  --color-tmu08-line: light-dark(#ccd2d7, #333b41);
  --color-tmu08-line: light-dark(oklch(85% 0.007 250), oklch(33% 0.011 250));
  --color-tmu08-acc: light-dark(#0f5f8f, #6fbde8);
  --color-tmu08-acc: light-dark(oklch(45% 0.11 240), oklch(78% 0.1 235));
  --color-tmu08-acc-ink: light-dark(#ffffff, #0e1116);
  --color-tmu08-acc-ink: light-dark(oklch(100% 0 0), oklch(17% 0.01 250));
  --font-tmu08-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu08-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-08:has(#tmu08-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-08:has(#tmu08-theme:checked) {
    color-scheme: light;
  }
}
```
