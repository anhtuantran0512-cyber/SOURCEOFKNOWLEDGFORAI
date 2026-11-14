---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-vertical-axis-flip-card-rotatex-top-to-bottom/"
title: "Tailwind Vertical Axis Flip Card with rotateX Top-to-Bottom Reveal"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "The axis study: identical machinery to a horizontal flip with rotateY swapped for rotateX in exactly two places."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Axis Flip Card with rotateX Top-to-Bottom Reveal
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-vertical-axis-flip-card-rotatex-top-to-bottom/

The axis study: identical machinery to a horizontal flip with rotateY swapped for rotateX in exactly two places. Written as utilities, those two places are both visible in the class list &mdash; which is the point of the demo, because forgetting the second one is what renders the back face upside-down.
## HTML
```html
<section class="tfc-15 w-full min-h-svh grid place-items-center content-center gap-5 bg-tfc15-bg font-tfc15-sans px-5 py-10 text-tfc15-ink">
  <div class="text-center">
    <h2 class="text-lg font-extrabold tracking-[-0.01em] text-white">Vertical axis (rotateX) flip</h2>
    <p class="mt-1 text-xs text-tfc15-muted">The card turns top-to-bottom instead of side-to-side</p>
    <code class="mt-2 inline-block rounded border border-tfc15-teal/30 bg-tfc15-teal/15 px-2 py-0.5 font-tfc15-mono text-[11px] text-tfc15-teal">transform: rotateX(180deg)</code>
  </div>

  <div class="group relative mx-auto h-[250px] w-[360px] max-w-full [perspective:1200px] [perspective-origin:50%_80%] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc15-teal has-[:focus-visible]:outline-offset-4">
    <input id="tfc-15-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-15-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Flip the card on its vertical axis</span></label>

    <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateX(180deg)] group-has-checked:[transform:rotateX(180deg)] group-has-[:focus-visible]:[transform:rotateX(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex items-center gap-5 rounded-2xl overflow-hidden px-8 py-7 bg-linear-160 from-tfc15-panel to-tfc15-panel2 border border-tfc15-teal/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_20px_44px_-18px_oklch(0.45_0.09_185/0.5)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <span class="grid size-16 shrink-0 place-items-center rounded-[18px] border border-tfc15-teal/30 bg-linear-135 from-tfc15-teal/20 to-tfc15-emerald/10 shadow-[0_0_20px_oklch(0.6_0.1_185/0.15)]">
          <svg viewBox="0 0 24 24" class="size-7 fill-none stroke-tfc15-teal stroke-[1.8]" aria-hidden="true"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
        </span>
        <div class="flex-1">
          <p class="mb-1.5 text-[10px] font-bold uppercase tracking-[0.15em] text-tfc15-teal">Feature &middot; flip axis</p>
          <h3 class="text-xl font-extrabold leading-tight tracking-[-0.01em] text-white">Vertical card flip</h3>
          <p class="mt-1.5 text-xs text-tfc15-muted">Hover, tap or press Space to turn it top-to-bottom</p>
        </div>
        <span aria-hidden="true" class="absolute right-4 top-1/2 flex -translate-y-1/2 flex-col items-center gap-0.5 text-[10px] tracking-[0.08em] text-tfc15-teal opacity-35"><span>&#9650;</span><span class="[writing-mode:vertical-rl]">flip</span><span>&#9660;</span></span>
      </div>

      <div class="absolute inset-0 flex items-center gap-5 rounded-2xl overflow-hidden px-8 py-7 bg-linear-160 from-tfc15-back to-tfc15-back2 border border-tfc15-emerald/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_20px_44px_-18px_oklch(0.5_0.12_165/0.45)] [transform:rotateX(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <span class="grid size-16 shrink-0 place-items-center rounded-[18px] border border-tfc15-emerald/30 bg-linear-135 from-tfc15-emerald/20 to-tfc15-teal/10">
          <svg viewBox="0 0 24 24" class="size-7 fill-none stroke-tfc15-emerald stroke-[2]" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        </span>
        <div class="flex-1">
          <p class="mb-1.5 text-[10px] font-bold uppercase tracking-[0.15em] text-tfc15-emerald">Back face &middot; revealed</p>
          <h3 class="text-lg font-extrabold leading-tight text-white">rotateX flip complete</h3>
          <ul class="mt-2.5 flex flex-wrap gap-1.5">
            <li class="rounded-full border border-tfc15-emerald/20 bg-tfc15-emerald/10 px-2.5 py-1 font-tfc15-mono text-[11px] text-tfc15-ink/75">rotateX(180deg)</li>
            <li class="rounded-full border border-tfc15-emerald/20 bg-tfc15-emerald/10 px-2.5 py-1 font-tfc15-mono text-[11px] text-tfc15-ink/75">backface-visibility</li>
            <li class="rounded-full border border-tfc15-emerald/20 bg-tfc15-emerald/10 px-2.5 py-1 font-tfc15-mono text-[11px] text-tfc15-ink/75">perspective:1200px</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc15-bg: #04100e;
  --color-tfc15-bg: oklch(0.14 0.025 180);
  --color-tfc15-panel: #071a16;
  --color-tfc15-panel: oklch(0.19 0.04 180);
  --color-tfc15-panel2: #04100e;
  --color-tfc15-panel2: oklch(0.15 0.025 180);
  --color-tfc15-back: #031a14;
  --color-tfc15-back: oklch(0.19 0.045 165);
  --color-tfc15-back2: #040e0c;
  --color-tfc15-back2: oklch(0.14 0.02 175);
  --color-tfc15-teal: #0d9488;
  --color-tfc15-teal: oklch(0.62 0.1 185);
  --color-tfc15-emerald: #10b981;
  --color-tfc15-emerald: oklch(0.72 0.16 165);
  --color-tfc15-ink: #f0fdf4;
  --color-tfc15-ink: oklch(0.98 0.02 160);
  --color-tfc15-muted: #9dbfb1;
  --color-tfc15-muted: oklch(0.78 0.04 170);
  --font-tfc15-sans: 'Sora', system-ui, sans-serif;
  --font-tfc15-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfc-15 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-15 * {
    transition-duration: 1ms !important;
  }
}
```
