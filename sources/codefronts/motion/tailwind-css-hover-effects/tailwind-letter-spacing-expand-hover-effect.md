---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-letter-spacing-expand-hover-effect/"
title: "Tailwind Letter Spacing Expand Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Five typographic hovers driven by tracking alone — expand, collapse-in, per-letter stagger, weight-plus-tracking and tracking-plus-glow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Letter Spacing Expand Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-letter-spacing-expand-hover-effect/

Five typographic hovers driven by tracking alone — expand, collapse-in, per-letter stagger, weight-plus-tracking and tracking-plus-glow. Tailwind's tracking-* scale covers the resting values; the wide hover targets are arbitrary, which is the correct split.
## HTML
```html
<section class="thv-03 w-full min-h-svh grid place-items-center bg-thv03-bg font-thv03-sans px-6 py-14">
  <div class="w-[min(720px,100%)] flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-5 px-9 py-7 rounded-xl bg-white/[0.03] border border-white/[0.07] overflow-hidden">
      <span tabindex="0" class="inline-block text-[clamp(1.4rem,4vw,2rem)] font-bold text-thv03-purple tracking-[0.02em] rounded-xs transition-[letter-spacing,color] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:tracking-[0.35em] hover:text-thv03-text focus-visible:tracking-[0.35em] focus-visible:text-thv03-text focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv03-purple motion-reduce:transition-none">EXPAND</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv03-dim">letter-spacing expand</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-9 py-7 rounded-xl bg-white/[0.03] border border-white/[0.07] overflow-hidden">
      <span tabindex="0" class="inline-block text-[clamp(1.4rem,4vw,2rem)] font-bold text-thv03-pink tracking-[0.4em] rounded-xs transition-[letter-spacing,color] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:tracking-[0.02em] hover:text-white focus-visible:tracking-[0.02em] focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv03-pink motion-reduce:transition-none">COLLAPSE</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv03-dim">tracking collapse-in</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-9 py-7 rounded-xl bg-white/[0.03] border border-white/[0.07] overflow-hidden">
      <span tabindex="0" class="group inline-flex text-[clamp(1.4rem,4vw,2rem)] font-bold text-thv03-cyan tracking-[0.02em] rounded-xs focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv03-cyan"><span class="inline-block transition-[letter-spacing,opacity] duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:tracking-[0.2em] group-hover:opacity-30 group-focus-visible:tracking-[0.2em] group-focus-visible:opacity-30 motion-reduce:transition-none">D</span><span class="inline-block transition-[letter-spacing,opacity] duration-400 delay-[40ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:tracking-[0.2em] group-hover:opacity-30 group-focus-visible:tracking-[0.2em] group-focus-visible:opacity-30 motion-reduce:transition-none">R</span><span class="inline-block transition-[letter-spacing,opacity] duration-400 delay-[80ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:tracking-[0.2em] group-hover:opacity-30 group-focus-visible:tracking-[0.2em] group-focus-visible:opacity-30 motion-reduce:transition-none">I</span><span class="inline-block transition-[letter-spacing,opacity] duration-400 delay-[120ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:tracking-[0.2em] group-hover:opacity-30 group-focus-visible:tracking-[0.2em] group-focus-visible:opacity-30 motion-reduce:transition-none">F</span><span class="inline-block transition-[letter-spacing,opacity] duration-400 delay-[160ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:tracking-[0.2em] group-hover:opacity-30 group-focus-visible:tracking-[0.2em] group-focus-visible:opacity-30 motion-reduce:transition-none">T</span></span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv03-dim">stagger fade-out</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-9 py-7 rounded-xl bg-white/[0.03] border border-white/[0.07] overflow-hidden">
      <span tabindex="0" class="inline-block text-[clamp(1.4rem,4vw,2rem)] font-normal text-thv03-amber tracking-[0.02em] rounded-xs transition-[letter-spacing,font-weight,color] duration-350 hover:tracking-[0.25em] hover:font-black hover:text-white focus-visible:tracking-[0.25em] focus-visible:font-black focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv03-amber motion-reduce:transition-none">BOLD TRACK</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv03-dim">weight + spacing</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-9 py-7 rounded-xl bg-white/[0.03] border border-white/[0.07] overflow-hidden">
      <span tabindex="0" class="inline-block text-[clamp(1.4rem,4vw,2rem)] font-bold text-thv03-text tracking-[0.06em] rounded-xs transition-[letter-spacing,text-shadow,color] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:tracking-[0.3em] hover:text-white hover:[text-shadow:0_0_20px_var(--color-thv03-purple),0_0_60px_var(--color-thv03-pink)] focus-visible:tracking-[0.3em] focus-visible:text-white focus-visible:[text-shadow:0_0_20px_var(--color-thv03-purple),0_0_60px_var(--color-thv03-pink)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv03-purple motion-reduce:transition-none">RADIANCE</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv03-dim">spacing + glow</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv03-bg: #0d0d14;
  --color-thv03-bg: oklch(0.16 0.01 285);
  --color-thv03-text: #ede9fe;
  --color-thv03-text: oklch(0.93 0.03 295);
  --color-thv03-dim: #6b7280;
  --color-thv03-dim: oklch(0.55 0.02 265);
  --color-thv03-purple: #a78bfa;
  --color-thv03-purple: oklch(0.72 0.15 295);
  --color-thv03-pink: #f472b6;
  --color-thv03-pink: oklch(0.72 0.19 350);
  --color-thv03-cyan: #67e8f9;
  --color-thv03-cyan: oklch(0.85 0.11 200);
  --color-thv03-amber: #fbbf24;
  --color-thv03-amber: oklch(0.82 0.16 82);
  --font-thv03-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-03 {
  width: 100%;
  min-height: 100svh;
}

.thv-03 ::selection {
  background: var(--color-thv03-purple);
  color: #fff;
}
```
