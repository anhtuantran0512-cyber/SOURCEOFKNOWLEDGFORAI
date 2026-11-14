---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-brutalist-snap-toggle-hard-offset-shadow/"
title: "Tailwind Brutalist Snap Toggle with Hard Offset Shadow"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Anti-animation as a statement: 3px black borders, a hard 6px offset shadow, and a block thumb that does not glide &mdash; it SNAPS across in a single frame…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Brutalist Snap Toggle with Hard Offset Shadow
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-brutalist-snap-toggle-hard-offset-shadow/

Anti-animation as a statement: 3px black borders, a hard 6px offset shadow, and a block thumb that does not glide &mdash; it SNAPS across in a single frame via ease-[steps(1,end)]. Pressing shoves the whole card into its own shadow.
## HTML
```html
<section class="ttg-17 w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg17-bg font-ttg17-mono" aria-label="Brutalist snap toggle">
  <label for="ttg-17-sw" class="flex items-center gap-8 px-7 py-6 bg-white border-[3px] border-ttg17-ink cursor-pointer shadow-[6px_6px_0_var(--color-ttg17-ink)] transition-[transform,box-shadow] duration-[90ms] ease-[steps(1,end)] active:translate-x-[3px] active:translate-y-[3px] active:shadow-[3px_3px_0_var(--color-ttg17-ink)] motion-reduce:transition-none">
    <span class="text-[15px] font-bold tracking-[0.14em] text-ttg17-ink">NEWSLETTER</span>
    <span class="relative block">
      <input type="checkbox" id="ttg-17-sw" role="switch" aria-label="Newsletter" class="peer appearance-none block w-26 h-12 border-[3px] border-ttg17-ink bg-white cursor-pointer relative transition-colors duration-[90ms] ease-[steps(1,end)] before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:w-9 before:h-9 before:bg-ttg17-ink before:transition-transform before:duration-[90ms] before:ease-[steps(1,end)] checked:bg-ttg17-signal checked:before:translate-x-14 focus-visible:outline-4 focus-visible:outline-ttg17-ink focus-visible:outline-offset-4 motion-reduce:transition-none motion-reduce:before:transition-none">
      <span aria-hidden="true" class="absolute inset-[3px] block pointer-events-none text-[13px] font-extrabold tracking-[0.1em] text-ttg17-ink peer-checked:[&_.ttg17-off]:hidden peer-checked:[&_.ttg17-on]:block">
        <i class="ttg17-off not-italic absolute top-1/2 right-2.5 -translate-y-1/2">OFF</i>
        <i class="ttg17-on not-italic hidden absolute top-1/2 left-2.5 -translate-y-1/2">ON</i>
      </span>
    </span>
  </label>
  <p class="text-[12px] tracking-[0.1em] text-ttg17-mute">steps(1) &mdash; it snaps, it does not glide</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg17-bg: #efece4;
  --color-ttg17-bg: oklch(0.94 0.01 90);
  --color-ttg17-ink: #000000;
  --color-ttg17-ink: oklch(0 0 0);
  --color-ttg17-signal: #ffe600;
  --color-ttg17-signal: oklch(0.91 0.19 103);
  --color-ttg17-mute: #6f6a5d;
  --color-ttg17-mute: oklch(0.52 0.02 90);
  --font-ttg17-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
}

.ttg-17 {
  width: 100%;
  min-height: 100svh;
}

.ttg-17 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
