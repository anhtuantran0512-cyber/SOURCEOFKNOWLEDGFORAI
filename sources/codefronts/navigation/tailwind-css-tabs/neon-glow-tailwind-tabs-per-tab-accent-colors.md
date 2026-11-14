---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/neon-glow-tailwind-tabs-per-tab-accent-colors/"
title: "Neon Glow Tailwind Tabs with Per-Tab Accent Colors"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Four electric tabs, each carrying its own accent in one custom property."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Tailwind Tabs with Per-Tab Accent Colors
Source: https://codefronts.com/navigation/tailwind-css-tabs/neon-glow-tailwind-tabs-per-tab-accent-colors/

Four electric tabs, each carrying its own accent in one custom property. Every label shares a single class list — text-(--c) border-(--c) bg-(--c)/12 — and only [--c:…] differs. The root re-points the same variable for the active tab, so the panel's glow and title follow the selection.
## HTML
```html
<section class="ttb-02 group/tabs grid min-h-svh w-full place-items-center bg-ttb02-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-ttb02-glow),transparent)] px-5 py-14 font-ttb02-mono text-ttb02-ink [--c:var(--color-ttb02-pink)] has-[#ttb02-r2:checked]:[--c:var(--color-ttb02-cyan)] has-[#ttb02-r3:checked]:[--c:var(--color-ttb02-lime)] has-[#ttb02-r4:checked]:[--c:var(--color-ttb02-amber)]" aria-label="Neon glow tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div role="radiogroup" aria-label="Signal mode" class="grid w-full grid-cols-2 gap-2.5 sm:grid-cols-4">
      <label class="flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-lg border border-white/10 text-[11px] font-bold tracking-[0.16em] text-ttb02-mut uppercase transition-[color,border-color,background-color,box-shadow] duration-300 [--c:var(--color-ttb02-pink)] hover:border-white/25 hover:text-ttb02-ink has-checked:border-(--c) has-checked:bg-(--c)/12 has-checked:text-(--c) has-checked:shadow-[0_0_16px_color-mix(in_oklab,var(--c)_55%,transparent),inset_0_0_10px_color-mix(in_oklab,var(--c)_25%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-(--c) motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb02" id="ttb02-r1" checked>Pulse</label>
      <label class="flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-lg border border-white/10 text-[11px] font-bold tracking-[0.16em] text-ttb02-mut uppercase transition-[color,border-color,background-color,box-shadow] duration-300 [--c:var(--color-ttb02-cyan)] hover:border-white/25 hover:text-ttb02-ink has-checked:border-(--c) has-checked:bg-(--c)/12 has-checked:text-(--c) has-checked:shadow-[0_0_16px_color-mix(in_oklab,var(--c)_55%,transparent),inset_0_0_10px_color-mix(in_oklab,var(--c)_25%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-(--c) motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb02" id="ttb02-r2">Wave</label>
      <label class="flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-lg border border-white/10 text-[11px] font-bold tracking-[0.16em] text-ttb02-mut uppercase transition-[color,border-color,background-color,box-shadow] duration-300 [--c:var(--color-ttb02-lime)] hover:border-white/25 hover:text-ttb02-ink has-checked:border-(--c) has-checked:bg-(--c)/12 has-checked:text-(--c) has-checked:shadow-[0_0_16px_color-mix(in_oklab,var(--c)_55%,transparent),inset_0_0_10px_color-mix(in_oklab,var(--c)_25%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-(--c) motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb02" id="ttb02-r3">Surge</label>
      <label class="flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-lg border border-white/10 text-[11px] font-bold tracking-[0.16em] text-ttb02-mut uppercase transition-[color,border-color,background-color,box-shadow] duration-300 [--c:var(--color-ttb02-amber)] hover:border-white/25 hover:text-ttb02-ink has-checked:border-(--c) has-checked:bg-(--c)/12 has-checked:text-(--c) has-checked:shadow-[0_0_16px_color-mix(in_oklab,var(--c)_55%,transparent),inset_0_0_10px_color-mix(in_oklab,var(--c)_25%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-(--c) motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb02" id="ttb02-r4">Bloom</label>
    </div>
    <div class="w-full rounded-xl border border-(--c)/35 bg-white/[0.03] p-5 shadow-[0_0_40px_-12px_color-mix(in_oklab,var(--c)_45%,transparent)] transition-[border-color,box-shadow] duration-500 motion-reduce:transition-none">
      <p class="flex items-center gap-2 text-[11px] font-bold tracking-[0.2em] text-(--c) uppercase"><span aria-hidden="true" class="size-1.5 rounded-full bg-(--c) shadow-[0_0_8px_var(--c)]"></span>Live signal</p>
      <p class="mt-3 hidden font-ttb02-sans text-[15px] leading-relaxed text-ttb02-soft transition-opacity duration-300 group-has-[#ttb02-r1:checked]/tabs:block starting:opacity-0">Pulse — short, rhythmic bursts of light at a steady 120 BPM.</p>
      <p class="mt-3 hidden font-ttb02-sans text-[15px] leading-relaxed text-ttb02-soft transition-opacity duration-300 group-has-[#ttb02-r2:checked]/tabs:block starting:opacity-0">Wave — a continuous oscillation that rises and falls across the strip.</p>
      <p class="mt-3 hidden font-ttb02-sans text-[15px] leading-relaxed text-ttb02-soft transition-opacity duration-300 group-has-[#ttb02-r3:checked]/tabs:block starting:opacity-0">Surge — a sudden upward swell of power, then a slow release.</p>
      <p class="mt-3 hidden font-ttb02-sans text-[15px] leading-relaxed text-ttb02-soft transition-opacity duration-300 group-has-[#ttb02-r4:checked]/tabs:block starting:opacity-0">Bloom — a soft glow front that expands outward from the centre.</p>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 text-[11.5px] text-ttb02-mut">[--c:…] · has-checked:bg-(--c)/12 · root re-points --c</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb02-bg: #0b0b12;
  --color-ttb02-bg: oklch(0.153 0.015 284.5);
  --color-ttb02-glow: #1d1636;
  --color-ttb02-glow: oklch(0.228 0.060 290.9);
  --color-ttb02-ink: #f2f1f7;
  --color-ttb02-ink: oklch(0.961 0.008 293.9);
  --color-ttb02-soft: #c9c7d6;
  --color-ttb02-soft: oklch(0.836 0.021 292.1);
  --color-ttb02-mut: #9a98ad;
  --color-ttb02-mut: oklch(0.688 0.031 289.9);
  --color-ttb02-pink: #ff4df2;
  --color-ttb02-pink: oklch(0.727 0.271 331.1);
  --color-ttb02-cyan: #3df0ff;
  --color-ttb02-cyan: oklch(0.875 0.138 203.6);
  --color-ttb02-lime: #c6ff3d;
  --color-ttb02-lime: oklch(0.928 0.216 125.2);
  --color-ttb02-amber: #ff9a3d;
  --color-ttb02-amber: oklch(0.776 0.159 59.0);
  --font-ttb02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttb02-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-02 {
  width: 100%;
  min-height: 100svh;
}
```
