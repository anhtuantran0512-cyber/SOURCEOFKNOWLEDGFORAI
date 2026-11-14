---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-optical-alignment-vs-mathematical-centering/"
title: "Tailwind Optical Alignment vs Mathematical Centering"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "Three cases where the geometric centre looks wrong: a play triangle in a round button, an opening quote mark, and an arrow beside a label."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Optical Alignment vs Mathematical Centering
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-optical-alignment-vs-mathematical-centering/

Three cases where the geometric centre looks wrong: a play triangle in a round button, an opening quote mark, and an arrow beside a label. Each is shown mathematically centred and then optically corrected with a single em-based utility &mdash; translate-x-[0.06em], indent-[-0.42em], -translate-y-[0.03em] &mdash; with a dashed centre guide drawn by an after: pseudo-element.
## HTML
```html
<section class="tmu-04 relative w-full min-h-svh bg-tmu04-bg font-tmu04-ui text-tmu04-ink antialiased" aria-labelledby="tmu04-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu04-theme" type="checkbox" class="peer sr-only">
    <label for="tmu04-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu04-line bg-tmu04-surface text-tmu04-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu04-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu04-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[68rem] gap-12 px-6 pt-20 pb-20 lg:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu04-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu04-ink-2"><span class="tabular-nums text-tmu04-acc">04</span><span aria-hidden="true" class="h-px w-6 bg-tmu04-line"></span>Alignment</p>
      <h2 id="tmu04-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Centred is not the same as looks centred</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu04-ink-2 text-pretty">Geometry puts mass where the box says. Eyes put it where the ink is. Each pair shows the maths, then the correction &mdash; one em-based utility each.</p>
    </header>
    <div class="grid gap-6 grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]">
      <article aria-labelledby="tmu04-c1" class="grid min-w-0 content-start gap-5 rounded-2xl bg-tmu04-surface p-6 ring-1 ring-tmu04-line/60">
        <h3 id="tmu04-c1" class="text-[0.9375rem] font-semibold tracking-[-0.008em]">Play triangle in a round button</h3>
        <div class="grid grid-cols-2 gap-4">
          <div class="grid min-w-0 justify-items-start gap-2.5">
            <button type="button" class="relative grid size-11 place-items-center rounded-full border border-tmu04-line text-tmu04-ink cursor-pointer transition-[color,border-color,scale] duration-150 after:pointer-events-none after:absolute after:inset-y-1.5 after:left-1/2 after:border-l after:border-dashed after:border-tmu04-guide hover:border-tmu04-acc hover:text-tmu04-acc active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu04-acc motion-reduce:transition-none">
              <svg class="size-7" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>
              <span class="sr-only">Play &mdash; mathematically centred</span>
            </button>
            <p class="grid min-w-0 gap-0.5 font-tmu04-mono text-[0.6875rem] uppercase tracking-[0.06em] text-tmu04-ink">Mathematical<span class="normal-case tracking-normal text-tmu04-ink-2 wrap-break-word">translate: 0</span></p>
          </div>
          <div class="grid min-w-0 justify-items-start gap-2.5">
            <button type="button" class="relative grid size-11 place-items-center rounded-full border border-tmu04-acc text-tmu04-ink cursor-pointer transition-[color,border-color,scale] duration-150 after:pointer-events-none after:absolute after:inset-y-1.5 after:left-1/2 after:border-l after:border-dashed after:border-tmu04-guide hover:border-tmu04-acc hover:text-tmu04-acc active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu04-acc motion-reduce:transition-none">
              <svg class="size-7 translate-x-[0.06em]" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>
              <span class="sr-only">Play &mdash; optically corrected</span>
            </button>
            <p class="grid min-w-0 gap-0.5 font-tmu04-mono text-[0.6875rem] uppercase tracking-[0.06em] text-tmu04-acc">Optical<span class="normal-case tracking-normal text-tmu04-ink-2 wrap-break-word">translate-x-[0.06em]</span></p>
          </div>
        </div>
      </article>
      <article aria-labelledby="tmu04-c2" class="grid min-w-0 content-start gap-5 rounded-2xl bg-tmu04-surface p-6 ring-1 ring-tmu04-line/60">
        <h3 id="tmu04-c2" class="text-[0.9375rem] font-semibold tracking-[-0.008em]">Opening quotation mark</h3>
        <div class="grid gap-4">
          <div class="grid min-w-0 gap-2"><blockquote class="border-t border-tmu04-line py-3"><p class="text-lg/[1.35] tracking-[-0.012em] text-pretty">&ldquo;Restraint is a budget, not a mood.&rdquo;</p></blockquote><p class="grid min-w-0 gap-0.5 font-tmu04-mono text-[0.6875rem] uppercase tracking-[0.06em] text-tmu04-ink">Mathematical<span class="normal-case tracking-normal text-tmu04-ink-2 wrap-break-word">indent-0</span></p></div>
          <div class="grid min-w-0 gap-2"><blockquote class="border-t border-tmu04-line py-3"><p class="text-lg/[1.35] tracking-[-0.012em] text-pretty indent-[-0.42em] [hanging-punctuation:first]">&ldquo;Restraint is a budget, not a mood.&rdquo;</p></blockquote><p class="grid min-w-0 gap-0.5 font-tmu04-mono text-[0.6875rem] uppercase tracking-[0.06em] text-tmu04-acc">Optical<span class="normal-case tracking-normal text-tmu04-ink-2 wrap-break-word">indent-[-0.42em]</span></p></div>
        </div>
      </article>
      <article aria-labelledby="tmu04-c3" class="grid min-w-0 content-start gap-5 rounded-2xl bg-tmu04-surface p-6 ring-1 ring-tmu04-line/60">
        <h3 id="tmu04-c3" class="text-[0.9375rem] font-semibold tracking-[-0.008em]">Icon beside a label</h3>
        <div class="grid grid-cols-2 gap-4">
          <div class="grid min-w-0 justify-items-start gap-2.5"><span class="inline-flex min-h-11 items-center gap-2.5 rounded-full border border-tmu04-line px-4 text-[0.9375rem] font-medium"><svg class="size-[18px] flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Continue</span><p class="grid min-w-0 gap-0.5 font-tmu04-mono text-[0.6875rem] uppercase tracking-[0.06em] text-tmu04-ink">Mathematical<span class="normal-case tracking-normal text-tmu04-ink-2 wrap-break-word">baseline aligned</span></p></div>
          <div class="grid min-w-0 justify-items-start gap-2.5"><span class="inline-flex min-h-11 items-center gap-2.5 rounded-full border border-tmu04-line px-4 text-[0.9375rem] font-medium"><svg class="size-[18px] flex-none -translate-y-[0.03em]" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Continue</span><p class="grid min-w-0 gap-0.5 font-tmu04-mono text-[0.6875rem] uppercase tracking-[0.06em] text-tmu04-acc">Optical<span class="normal-case tracking-normal text-tmu04-ink-2 wrap-break-word">-translate-y-[0.03em]</span></p></div>
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
  --color-tmu04-bg: light-dark(#f3f5f6, #08090a);
  --color-tmu04-bg: light-dark(oklch(96% 0.003 250), oklch(13% 0.004 250));
  --color-tmu04-surface: light-dark(#ffffff, #121416);
  --color-tmu04-surface: light-dark(oklch(100% 0 0), oklch(19% 0.005 250));
  --color-tmu04-ink: light-dark(#14171a, #f4f6f7);
  --color-tmu04-ink: light-dark(oklch(19% 0.006 250), oklch(97% 0.002 250));
  --color-tmu04-ink-2: light-dark(#545c62, #a8b0b6);
  --color-tmu04-ink-2: light-dark(oklch(45% 0.011 250), oklch(75% 0.008 250));
  --color-tmu04-line: light-dark(#d3d8db, #2b3034);
  --color-tmu04-line: light-dark(oklch(86% 0.005 250), oklch(29% 0.007 250));
  --color-tmu04-guide: light-dark(#8d959a, #6b747a);
  --color-tmu04-guide: light-dark(oklch(66% 0.008 250), oklch(56% 0.01 250));
  --color-tmu04-acc: light-dark(#05704f, #6ee7b7);
  --color-tmu04-acc: light-dark(oklch(45% 0.11 165), oklch(85% 0.13 165));
  --font-tmu04-ui: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-tmu04-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-04:has(#tmu04-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-04:has(#tmu04-theme:checked) {
    color-scheme: light;
  }
}
```
