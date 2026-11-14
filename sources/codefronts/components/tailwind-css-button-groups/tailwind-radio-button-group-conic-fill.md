---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-radio-button-group-conic-fill/"
title: "Tailwind Radio Button Group with Conic Fill Animation (Export Format Picker)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "Four format tiles &mdash; PNG, JPG, WebP, AVIF &mdash; where the chosen one fills with its own colour in a clockwise radial sweep."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Radio Button Group with Conic Fill Animation (Export Format Picker)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-radio-button-group-conic-fill/

Four format tiles &mdash; PNG, JPG, WebP, AVIF &mdash; where the chosen one fills with its own colour in a clockwise radial sweep. An @property-registered angle drives conic-gradient(from -90deg, var(--c) var(--tbg16-a), transparent 0) on a before: layer, and each tile's colour is one inline variable read by has-checked:border-(--c). Every tile now explains what the format is for.
## HTML
```html
<section class="tbg-16 w-full min-h-svh grid place-items-center bg-tbg16-bg bg-linear-160 from-tbg16-bg to-tbg16-bg2 px-5 py-14 font-tbg16-sans text-tbg16-ink" aria-label="Conic fill radio button group demo">
  <div class="grid w-full max-w-[34rem] gap-3.5">
    <p id="tbg16-label" class="ml-0.5 font-tbg16-mono text-xs font-semibold uppercase tracking-[0.16em] text-tbg16-mut">Export format</p>
    <div role="radiogroup" aria-labelledby="tbg16-label" class="grid grid-cols-2 gap-3 sm:grid-cols-4">
      <label style="--c:#ff7a8a" class="relative isolate grid min-h-20 cursor-pointer place-content-center justify-items-center gap-1 overflow-hidden rounded-2xl border-[1.5px] border-tbg16-line bg-tbg16-cell text-tbg16-mut transition-[color,border-color] duration-300 before:absolute before:inset-0 before:-z-1 before:bg-[conic-gradient(from_-90deg,var(--c)_var(--tbg16-a),transparent_0)] before:opacity-0 before:transition-opacity before:content-[''] hover:border-tbg16-hover hover:text-tbg16-ink has-checked:border-(--c) has-checked:text-tbg16-on has-checked:before:opacity-100 has-checked:before:animate-tbg16-sweep has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-(--c) motion-reduce:has-checked:before:animate-none motion-reduce:before:[--tbg16-a:360deg]"><input type="radio" name="tbg16" class="sr-only" checked><span class="text-[17px] font-extrabold tracking-[0.02em]">PNG</span><span class="font-tbg16-mono text-[11px]">Lossless</span></label>
      <label style="--c:#ffbe5c" class="relative isolate grid min-h-20 cursor-pointer place-content-center justify-items-center gap-1 overflow-hidden rounded-2xl border-[1.5px] border-tbg16-line bg-tbg16-cell text-tbg16-mut transition-[color,border-color] duration-300 before:absolute before:inset-0 before:-z-1 before:bg-[conic-gradient(from_-90deg,var(--c)_var(--tbg16-a),transparent_0)] before:opacity-0 before:transition-opacity before:content-[''] hover:border-tbg16-hover hover:text-tbg16-ink has-checked:border-(--c) has-checked:text-tbg16-on has-checked:before:opacity-100 has-checked:before:animate-tbg16-sweep has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-(--c) motion-reduce:has-checked:before:animate-none motion-reduce:before:[--tbg16-a:360deg]"><input type="radio" name="tbg16" class="sr-only"><span class="text-[17px] font-extrabold tracking-[0.02em]">JPG</span><span class="font-tbg16-mono text-[11px]">Photos</span></label>
      <label style="--c:#5ee0cc" class="relative isolate grid min-h-20 cursor-pointer place-content-center justify-items-center gap-1 overflow-hidden rounded-2xl border-[1.5px] border-tbg16-line bg-tbg16-cell text-tbg16-mut transition-[color,border-color] duration-300 before:absolute before:inset-0 before:-z-1 before:bg-[conic-gradient(from_-90deg,var(--c)_var(--tbg16-a),transparent_0)] before:opacity-0 before:transition-opacity before:content-[''] hover:border-tbg16-hover hover:text-tbg16-ink has-checked:border-(--c) has-checked:text-tbg16-on has-checked:before:opacity-100 has-checked:before:animate-tbg16-sweep has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-(--c) motion-reduce:has-checked:before:animate-none motion-reduce:before:[--tbg16-a:360deg]"><input type="radio" name="tbg16" class="sr-only"><span class="text-[17px] font-extrabold tracking-[0.02em]">WebP</span><span class="font-tbg16-mono text-[11px]">Web, smaller</span></label>
      <label style="--c:#93abff" class="relative isolate grid min-h-20 cursor-pointer place-content-center justify-items-center gap-1 overflow-hidden rounded-2xl border-[1.5px] border-tbg16-line bg-tbg16-cell text-tbg16-mut transition-[color,border-color] duration-300 before:absolute before:inset-0 before:-z-1 before:bg-[conic-gradient(from_-90deg,var(--c)_var(--tbg16-a),transparent_0)] before:opacity-0 before:transition-opacity before:content-[''] hover:border-tbg16-hover hover:text-tbg16-ink has-checked:border-(--c) has-checked:text-tbg16-on has-checked:before:opacity-100 has-checked:before:animate-tbg16-sweep has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-(--c) motion-reduce:has-checked:before:animate-none motion-reduce:before:[--tbg16-a:360deg]"><input type="radio" name="tbg16" class="sr-only"><span class="text-[17px] font-extrabold tracking-[0.02em]">AVIF</span><span class="font-tbg16-mono text-[11px]">Smallest</span></label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* @property is an at-rule with no utility: it makes the conic stop animatable. */

@property --tbg16-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tbg16-bg: #14121c;
  --color-tbg16-bg2: #0c0a12;
  --color-tbg16-cell: #1a1726;
  --color-tbg16-line: #2a2540;
  --color-tbg16-hover: #423a62;
  --color-tbg16-ink: #ece7fb;
  --color-tbg16-mut: #aaa2c6;
  --color-tbg16-mut: oklch(0.74 0.05 290);
  --color-tbg16-on: #15111f;
  --font-tbg16-sans: 'Syne', system-ui, sans-serif;
  --font-tbg16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbg16-sweep: tbg16-sweep 0.65s cubic-bezier(0.3, 0.7, 0.3, 1) forwards;

  @keyframes tbg16-sweep {
    from {
      --tbg16-a: 0deg;
    }

    to {
      --tbg16-a: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-16 {
  width: 100%;
  min-height: 100svh;
}
```
