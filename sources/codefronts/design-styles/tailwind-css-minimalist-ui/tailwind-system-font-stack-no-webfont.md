---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-system-font-stack-no-webfont/"
title: "Tailwind System Font Stack That Needs No Webfont"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "Four --font-* theme tokens, four specimens, four fallback ladders &mdash; sans, serif, mono and rounded, each built from what the operating system already has."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind System Font Stack That Needs No Webfont
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-system-font-stack-no-webfont/

Four --font-* theme tokens, four specimens, four fallback ladders &mdash; sans, serif, mono and rounded, each built from what the operating system already has. Every ladder is numbered with a CSS counter written as an arbitrary property, so you can see exactly which face resolves where and why the rounded stack degrades to sans on Windows.
## HTML
```html
<section class="tmu-03 relative w-full min-h-svh bg-tmu03-bg font-tmu03-sans text-tmu03-ink antialiased" aria-labelledby="tmu03-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu03-theme" type="checkbox" class="peer sr-only">
    <label for="tmu03-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu03-line bg-tmu03-surface text-tmu03-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu03-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu03-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[76rem] gap-12 px-6 pt-20 pb-20 lg:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu03-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu03-ink-2"><span class="tabular-nums text-tmu03-acc">03</span><span aria-hidden="true" class="h-px w-6 bg-tmu03-line"></span>Font stacks</p>
      <h2 id="tmu03-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Four stacks, zero webfonts</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu03-ink-2 text-pretty">Every face below is already installed. Each ladder lists what the browser tries, in order &mdash; the first match wins, and nothing is downloaded.</p>
    </header>
    <div class="grid gap-6 lg:grid-cols-2">
      <article aria-labelledby="tmu03-h1" class="grid min-w-0 content-start gap-5 rounded-xl border border-tmu03-line bg-tmu03-surface p-7 even:bg-tmu03-surface-2">
        <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
          <h3 id="tmu03-h1" class="font-tmu03-mono text-[0.8125rem] font-medium uppercase tracking-[0.08em] text-tmu03-acc">Interface sans</h3>
          <p class="text-[0.8125rem] text-tmu03-ink-2">Buttons, labels, dense UI</p>
        </div>
        <p class="min-w-0 wrap-break-word text-[clamp(1.5rem,1.1rem+2.2vw,2.5rem)] font-medium leading-[1.1] font-tmu03-sans tracking-[-0.022em]">Continue to payment</p>
        <ol class="grid min-w-0 border-t border-tmu03-line [counter-reset:tmu03]">
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)] first:[&>code]:text-tmu03-acc"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">system-ui</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Resolves the OS UI face</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">-apple-system</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Safari before 11</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">&quot;Segoe UI&quot;</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Windows, explicit</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">Roboto</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Android, Chrome OS</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">&quot;Helvetica Neue&quot;, Arial</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Metric-compatible pair</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">sans-serif</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Last resort</span></li>
        </ol>
      </article>
      <article aria-labelledby="tmu03-h2" class="grid min-w-0 content-start gap-5 rounded-xl border border-tmu03-line bg-tmu03-surface p-7 even:bg-tmu03-surface-2">
        <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
          <h3 id="tmu03-h2" class="font-tmu03-mono text-[0.8125rem] font-medium uppercase tracking-[0.08em] text-tmu03-acc">Reading serif</h3>
          <p class="text-[0.8125rem] text-tmu03-ink-2">Long-form prose</p>
        </div>
        <p class="min-w-0 wrap-break-word text-[clamp(1.5rem,1.1rem+2.2vw,2.5rem)] font-medium leading-[1.1] font-tmu03-serif tracking-[-0.012em]">A calm measure, set in Georgia</p>
        <ol class="grid min-w-0 border-t border-tmu03-line [counter-reset:tmu03]">
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)] first:[&>code]:text-tmu03-acc"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">ui-serif</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Apple platforms</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">Georgia</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Everywhere since 1996</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">&quot;Iowan Old Style&quot;</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">iOS reading face</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">&quot;Palatino Linotype&quot;, Palatino</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Metric-compatible pair</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">serif</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Last resort</span></li>
        </ol>
      </article>
      <article aria-labelledby="tmu03-h3" class="grid min-w-0 content-start gap-5 rounded-xl border border-tmu03-line bg-tmu03-surface p-7 even:bg-tmu03-surface-2">
        <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
          <h3 id="tmu03-h3" class="font-tmu03-mono text-[0.8125rem] font-medium uppercase tracking-[0.08em] text-tmu03-acc">Data monospace</h3>
          <p class="text-[0.8125rem] text-tmu03-ink-2">Figures, code, logs</p>
        </div>
        <p class="min-w-0 wrap-break-word text-[clamp(1.5rem,1.1rem+2.2vw,2.5rem)] font-medium leading-[1.1] font-tmu03-mono tabular-nums tracking-[-0.01em]">1,284.06 &middot; 99.982% &middot; 0x1F</p>
        <ol class="grid min-w-0 border-t border-tmu03-line [counter-reset:tmu03]">
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)] first:[&>code]:text-tmu03-acc"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">ui-monospace</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Apple platforms</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">SFMono-Regular</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">macOS, older Safari</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">Menlo, Consolas</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">macOS / Windows pair</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">&quot;Liberation Mono&quot;</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Linux, Android</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">monospace</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Last resort</span></li>
        </ol>
      </article>
      <article aria-labelledby="tmu03-h4" class="grid min-w-0 content-start gap-5 rounded-xl border border-tmu03-line bg-tmu03-surface p-7 even:bg-tmu03-surface-2">
        <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
          <h3 id="tmu03-h4" class="font-tmu03-mono text-[0.8125rem] font-medium uppercase tracking-[0.08em] text-tmu03-acc">Rounded, with a caveat</h3>
          <p class="text-[0.8125rem] text-tmu03-ink-2">Degrades to sans</p>
        </div>
        <p class="min-w-0 wrap-break-word text-[clamp(1.5rem,1.1rem+2.2vw,2.5rem)] font-medium leading-[1.1] font-tmu03-round tracking-[-0.022em]">Draft saved</p>
        <ol class="grid min-w-0 border-t border-tmu03-line [counter-reset:tmu03]">
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)] first:[&>code]:text-tmu03-acc"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">ui-rounded</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Apple only &mdash; falls through elsewhere</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">&quot;SF Pro Rounded&quot;</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">macOS, iOS</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">&quot;Hiragino Maru Gothic ProN&quot;</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Japanese rounded</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">system-ui</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">The realistic result on Windows</span></li>
          <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-4 gap-y-0.5 border-b border-tmu03-line py-2.5 [counter-increment:tmu03] before:row-span-2 before:pt-0.5 before:font-tmu03-mono before:text-xs before:tabular-nums before:text-tmu03-ink-2 before:content-[counter(tmu03,decimal-leading-zero)]"><code class="min-w-0 wrap-break-word font-tmu03-mono text-[0.8125rem]">sans-serif</code><span class="min-w-0 text-[0.8125rem] text-tmu03-ink-2">Last resort</span></li>
        </ol>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu03-bg: light-dark(#f7f4ee, #14120f);
  --color-tmu03-bg: light-dark(oklch(96.5% 0.008 85), oklch(18% 0.008 70));
  --color-tmu03-surface: light-dark(#fffdf9, #1d1a16);
  --color-tmu03-surface: light-dark(oklch(99% 0.005 85), oklch(23% 0.009 70));
  --color-tmu03-surface-2: light-dark(#f0ece3, #262218);
  --color-tmu03-surface-2: light-dark(oklch(93.5% 0.011 85), oklch(27% 0.012 75));
  --color-tmu03-ink: light-dark(#1b1915, #f3efe7);
  --color-tmu03-ink: light-dark(oklch(20% 0.008 70), oklch(95.5% 0.008 85));
  --color-tmu03-ink-2: light-dark(#575249, #b0a998);
  --color-tmu03-ink-2: light-dark(oklch(45% 0.012 75), oklch(76% 0.016 82));
  --color-tmu03-line: light-dark(#d8d2c6, #3b3529);
  --color-tmu03-line: light-dark(oklch(86% 0.013 82), oklch(33% 0.014 78));
  --color-tmu03-acc: light-dark(#8a4b12, #e8a86a);
  --color-tmu03-acc: light-dark(oklch(46% 0.13 55), oklch(79% 0.11 60));
  --font-tmu03-sans: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu03-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --font-tmu03-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --font-tmu03-round: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-03:has(#tmu03-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-03:has(#tmu03-theme:checked) {
    color-scheme: light;
  }
}
```
