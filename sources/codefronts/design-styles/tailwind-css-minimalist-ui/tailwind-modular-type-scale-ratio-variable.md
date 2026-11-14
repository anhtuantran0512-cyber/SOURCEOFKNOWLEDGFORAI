---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-modular-type-scale-ratio-variable/"
title: "Tailwind Modular Type Scale with a Ratio Variable"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "One arbitrary property &mdash; [--tmu01-ratio:1.2] &mdash; rebuilds an entire type scale, because every text-tmu01-s* utility is minted from @theme inline as…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Modular Type Scale with a Ratio Variable
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-modular-type-scale-ratio-variable/

One arbitrary property &mdash; [--tmu01-ratio:1.2] &mdash; rebuilds an entire type scale, because every text-tmu01-s* utility is minted from @theme inline as a live calc() of base &times; ratio. Three specimens run 1.200, 1.250 and 1.333 from one identical class list, with every computed size printed and drawn to scale.
## HTML
```html
<section class="tmu-01 relative w-full min-h-svh bg-tmu01-bg font-tmu01-ui text-base/normal text-tmu01-ink antialiased" aria-labelledby="tmu01-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu01-theme" type="checkbox" class="peer sr-only">
    <label for="tmu01-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu01-line bg-tmu01-surface text-tmu01-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu01-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu01-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[78rem] gap-12 px-6 pt-20 pb-20 lg:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu01-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu01-ink-2"><span class="tabular-nums text-tmu01-acc">01</span><span aria-hidden="true" class="h-px w-6 bg-tmu01-line"></span>Type scale</p>
      <h2 id="tmu01-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">One ratio, every size</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu01-ink-2 text-pretty">Each step is base &times; ratio<sup>n</sup>. Change one number and the whole hierarchy moves in proportion &mdash; three ratios, one identical class list.</p>
    </header>
    <div class="grid gap-6 grid-cols-[repeat(auto-fit,minmax(min(100%,17rem),1fr))]">
      <article aria-labelledby="tmu01-r1" class="relative grid min-w-0 content-start gap-6 rounded-xl border border-tmu01-line shadow-[0_1px_2px_rgb(20_24_28/0.05)] bg-tmu01-surface p-6 [--tmu01-ratio:1.2]">
        <header class="flex flex-wrap items-baseline gap-3 border-b border-tmu01-line pb-4">
          <h3 id="tmu01-r1" class="min-w-0 font-tmu01-mono text-[1.375rem] font-medium tracking-[-0.01em]">1.200</h3>
          <p class="min-w-0 text-xs uppercase tracking-[0.08em] text-tmu01-ink-2">Minor third &middot; dense UI</p>
        </header>
        <div class="grid min-w-0 gap-3 wrap-break-word">
          <p class="text-tmu01-s4 font-semibold leading-[1.05] tracking-[-0.028em]">Ranger</p>
          <p class="text-tmu01-s3 font-semibold leading-[1.15] tracking-[-0.018em]">Monthly recurring revenue</p>
          <p class="text-tmu01-s2 font-medium leading-[1.25]">Draft saved</p>
          <p class="max-w-[34ch] text-tmu01-s1 leading-normal text-tmu01-ink-2 text-pretty">A ratio this tight keeps a dense console readable, because adjacent steps stay close enough to sit in the same table row.</p>
          <p class="text-tmu01-s0 font-medium">Continue to payment</p>
        </div>
        <dl class="grid gap-1.5 border-t border-tmu01-line pt-4 font-tmu01-mono text-xs tabular-nums text-tmu01-ink-2">
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s4</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:65.7%"></span></span><dd class="text-right text-tmu01-ink">33.18px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s3</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:54.7%"></span></span><dd class="text-right text-tmu01-ink">27.65px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s2</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:45.6%"></span></span><dd class="text-right text-tmu01-ink">23.04px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s1</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:38.0%"></span></span><dd class="text-right text-tmu01-ink">19.20px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s0</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:31.7%"></span></span><dd class="text-right text-tmu01-ink">16.00px</dd></div>
        </dl>
      </article>
      <article aria-labelledby="tmu01-r2" class="relative grid min-w-0 content-start gap-6 rounded-xl border border-tmu01-acc shadow-[0_0_0_3px_var(--color-tmu01-ring),0_12px_32px_-18px_rgb(20_24_28/0.35)] bg-tmu01-surface p-6 [--tmu01-ratio:1.25]">
        <span class="absolute -top-3 left-6 rounded-full bg-tmu01-acc px-2.5 py-1 font-tmu01-mono text-[0.6875rem] font-semibold uppercase tracking-[0.08em] text-tmu01-acc-ink">Default</span>
        <header class="flex flex-wrap items-baseline gap-3 border-b border-tmu01-line pb-4">
          <h3 id="tmu01-r2" class="min-w-0 font-tmu01-mono text-[1.375rem] font-medium tracking-[-0.01em]">1.250</h3>
          <p class="min-w-0 text-xs uppercase tracking-[0.08em] text-tmu01-ink-2">Major third &middot; product UI</p>
        </header>
        <div class="grid min-w-0 gap-3 wrap-break-word">
          <p class="text-tmu01-s4 font-semibold leading-[1.05] tracking-[-0.028em]">Ranger</p>
          <p class="text-tmu01-s3 font-semibold leading-[1.15] tracking-[-0.018em]">Monthly recurring revenue</p>
          <p class="text-tmu01-s2 font-medium leading-[1.25]">Draft saved</p>
          <p class="max-w-[34ch] text-tmu01-s1 leading-normal text-tmu01-ink-2 text-pretty">The working default for most product interfaces: distinguishable steps that still leave room for four or five levels of hierarchy.</p>
          <p class="text-tmu01-s0 font-medium">Continue to payment</p>
        </div>
        <dl class="grid gap-1.5 border-t border-tmu01-line pt-4 font-tmu01-mono text-xs tabular-nums text-tmu01-ink-2">
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s4</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-acc" style="width:77.3%"></span></span><dd class="text-right text-tmu01-ink">39.06px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s3</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-acc" style="width:61.8%"></span></span><dd class="text-right text-tmu01-ink">31.25px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s2</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-acc" style="width:49.5%"></span></span><dd class="text-right text-tmu01-ink">25.00px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s1</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-acc" style="width:39.6%"></span></span><dd class="text-right text-tmu01-ink">20.00px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s0</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-acc" style="width:31.7%"></span></span><dd class="text-right text-tmu01-ink">16.00px</dd></div>
        </dl>
      </article>
      <article aria-labelledby="tmu01-r3" class="relative grid min-w-0 content-start gap-6 rounded-xl border border-tmu01-line shadow-[0_1px_2px_rgb(20_24_28/0.05)] bg-tmu01-surface p-6 [--tmu01-ratio:1.333]">
        <header class="flex flex-wrap items-baseline gap-3 border-b border-tmu01-line pb-4">
          <h3 id="tmu01-r3" class="min-w-0 font-tmu01-mono text-[1.375rem] font-medium tracking-[-0.01em]">1.333</h3>
          <p class="min-w-0 text-xs uppercase tracking-[0.08em] text-tmu01-ink-2">Perfect fourth &middot; editorial</p>
        </header>
        <div class="grid min-w-0 gap-3 wrap-break-word">
          <p class="text-tmu01-s4 font-semibold leading-[1.05] tracking-[-0.028em]">Ranger</p>
          <p class="text-tmu01-s3 font-semibold leading-[1.15] tracking-[-0.018em]">Monthly recurring revenue</p>
          <p class="text-tmu01-s2 font-medium leading-[1.25]">Draft saved</p>
          <p class="max-w-[34ch] text-tmu01-s1 leading-normal text-tmu01-ink-2 text-pretty">Decisive on a landing page and hostile in a data table &mdash; by the fourth step the jump is 13px, which no dense interface can absorb.</p>
          <p class="text-tmu01-s0 font-medium">Continue to payment</p>
        </div>
        <dl class="grid gap-1.5 border-t border-tmu01-line pt-4 font-tmu01-mono text-xs tabular-nums text-tmu01-ink-2">
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s4</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:100.0%"></span></span><dd class="text-right text-tmu01-ink">50.53px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s3</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:75.0%"></span></span><dd class="text-right text-tmu01-ink">37.91px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s2</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:56.3%"></span></span><dd class="text-right text-tmu01-ink">28.44px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s1</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:42.2%"></span></span><dd class="text-right text-tmu01-ink">21.33px</dd></div>
          <div class="grid grid-cols-[2rem_minmax(0,1fr)_4.5rem] items-center gap-3"><dt>s0</dt><span aria-hidden="true" class="h-1 rounded-full bg-tmu01-line"><span class="block h-full rounded-full bg-tmu01-ink-2" style="width:31.7%"></span></span><dd class="text-right text-tmu01-ink">16.00px</dd></div>
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
  --color-tmu01-bg: light-dark(#eef0f2, #0f1215);
  --color-tmu01-bg: light-dark(oklch(94.6% 0.005 240), oklch(17% 0.008 250));
  --color-tmu01-surface: light-dark(#ffffff, #171b1f);
  --color-tmu01-surface: light-dark(oklch(100% 0 0), oklch(22% 0.009 250));
  --color-tmu01-ink: light-dark(#14181c, #eef1f4);
  --color-tmu01-ink: light-dark(oklch(19% 0.012 250), oklch(95% 0.004 250));
  --color-tmu01-ink-2: light-dark(#4c565f, #a3adb6);
  --color-tmu01-ink-2: light-dark(oklch(43% 0.018 250), oklch(74% 0.012 250));
  --color-tmu01-line: light-dark(#c9cfd5, #333c44);
  --color-tmu01-line: light-dark(oklch(84% 0.008 250), oklch(33% 0.012 250));
  --color-tmu01-acc: light-dark(#1d5cff, #7fa6ff);
  --color-tmu01-acc: light-dark(oklch(52% 0.21 264), oklch(76% 0.14 264));
  --color-tmu01-ring: light-dark(#d9e3ff, #1f2d52);
  --color-tmu01-ring: light-dark(oklch(91% 0.04 264), oklch(30% 0.07 264));
  --color-tmu01-acc-ink: light-dark(#ffffff, #0f1215);
  --color-tmu01-acc-ink: light-dark(oklch(100% 0 0), oklch(17% 0.008 250));
  --font-tmu01-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu01-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* inline: each utility carries its own calc(), so it resolves on the element that uses it. */

@theme inline {
  --text-tmu01-s0: var(--tmu01-base);
  --text-tmu01-s1: calc(var(--tmu01-base) * var(--tmu01-ratio));
  --text-tmu01-s2: calc(var(--tmu01-base) * var(--tmu01-ratio) * var(--tmu01-ratio));
  --text-tmu01-s3: calc(var(--tmu01-base) * var(--tmu01-ratio) * var(--tmu01-ratio) * var(--tmu01-ratio));
  --text-tmu01-s4: calc(var(--tmu01-base) * var(--tmu01-ratio) * var(--tmu01-ratio) * var(--tmu01-ratio) * var(--tmu01-ratio));
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
  --tmu01-ratio: 1.25;
  --tmu01-base: clamp(0.9375rem, 0.9rem + 0.25vw, 1rem);
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-01:has(#tmu01-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-01:has(#tmu01-theme:checked) {
    color-scheme: light;
  }
}
```
