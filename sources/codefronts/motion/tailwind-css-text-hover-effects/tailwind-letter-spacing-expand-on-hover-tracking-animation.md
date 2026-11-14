---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-letter-spacing-expand-on-hover-tracking-animation/"
title: "Tailwind Letter Spacing Expand on Hover (Tracking Animation)"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A luxury-magazine masthead that breathes outward from a stable centre: tracking-[0.14em] → hover:tracking-[0.46em], with a matching negative right margin…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Letter Spacing Expand on Hover (Tracking Animation)
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-letter-spacing-expand-on-hover-tracking-animation/

A luxury-magazine masthead that breathes outward from a stable centre: tracking-[0.14em] → hover:tracking-[0.46em], with a matching negative right margin that swallows the phantom trailing space letter-spacing adds. The issue number does the opposite and tightens; the section nav expands subtly.
## HTML
```html
<section class="tth-15 w-full min-h-svh grid place-items-center bg-tth15-bg px-5 py-14 font-tth15-sans text-tth15-ink" aria-label="Letter spacing expansion demo">
  <div class="flex flex-col items-center gap-[clamp(16px,3vw,26px)] text-center">
    <p><a id="tth15-top" href="#tth15-top" class="font-tth15-mono text-[13px] tracking-[0.34em] -mr-[0.34em] text-tth15-mut no-underline transition-[letter-spacing,margin-right,color] duration-500 ease-[cubic-bezier(.25,.8,.25,1)] hover:tracking-[0.12em] hover:-mr-[0.12em] hover:text-tth15-ink focus-visible:tracking-[0.12em] focus-visible:-mr-[0.12em] focus-visible:outline-[1.5px] focus-visible:outline-offset-[6px] focus-visible:outline-tth15-ink motion-reduce:transition-none">N&deg; 08</a></p>
    <h2 class="flex flex-col leading-[1.02]">
      <a href="#tth15-top" class="block text-[clamp(50px,11.5vw,116px)] font-[275] tracking-[0.14em] -mr-[0.14em] no-underline transition-[letter-spacing,margin-right,font-weight] duration-700 ease-[cubic-bezier(.25,.8,.25,1)] hover:font-[340] hover:tracking-[0.46em] hover:-mr-[0.46em] focus-visible:font-[340] focus-visible:tracking-[0.46em] focus-visible:-mr-[0.46em] focus-visible:outline-[1.5px] focus-visible:outline-offset-[10px] focus-visible:outline-tth15-ink motion-reduce:transition-none">MAISON</a>
      <a href="#tth15-top" class="block text-[clamp(50px,11.5vw,116px)] font-semibold tracking-[0.14em] -mr-[0.14em] no-underline transition-[letter-spacing,margin-right,font-weight] duration-700 ease-[cubic-bezier(.25,.8,.25,1)] hover:font-bold hover:tracking-[0.46em] hover:-mr-[0.46em] focus-visible:font-bold focus-visible:tracking-[0.46em] focus-visible:-mr-[0.46em] focus-visible:outline-[1.5px] focus-visible:outline-offset-[10px] focus-visible:outline-tth15-ink motion-reduce:transition-none">VERRE</a>
    </h2>
    <p class="max-w-[46ch] font-tth15-serif text-lg italic leading-[1.6] text-tth15-mut">The glass issue &mdash; transparency as a material, a metaphor, and a marketing problem.</p>
    <nav class="flex flex-wrap justify-center gap-1 border-y border-tth15-line py-1.5" aria-label="Sections">
      <a href="#tth15-top" aria-current="page" class="relative grid min-h-11 place-items-center px-[18px] text-xs font-semibold uppercase tracking-[0.18em] -mr-[0.18em] text-tth15-mut no-underline transition-[letter-spacing,margin-right,color] duration-400 ease-[cubic-bezier(.25,.8,.25,1)] hover:tracking-[0.3em] hover:-mr-[0.3em] hover:text-tth15-ink focus-visible:text-tth15-ink focus-visible:outline-[1.5px] focus-visible:-outline-offset-4 focus-visible:outline-tth15-ink aria-[current=page]:text-tth15-ink aria-[current=page]:after:absolute aria-[current=page]:after:bottom-1.5 aria-[current=page]:after:left-1/2 aria-[current=page]:after:size-1 aria-[current=page]:after:-translate-x-1/2 aria-[current=page]:after:rounded-full aria-[current=page]:after:bg-current aria-[current=page]:after:content-[''] motion-reduce:transition-none">Essays</a>
      <a href="#tth15-top" class="relative grid min-h-11 place-items-center px-[18px] text-xs font-semibold uppercase tracking-[0.18em] -mr-[0.18em] text-tth15-mut no-underline transition-[letter-spacing,margin-right,color] duration-400 ease-[cubic-bezier(.25,.8,.25,1)] hover:tracking-[0.3em] hover:-mr-[0.3em] hover:text-tth15-ink focus-visible:text-tth15-ink focus-visible:outline-[1.5px] focus-visible:-outline-offset-4 focus-visible:outline-tth15-ink motion-reduce:transition-none">Objects</a>
      <a href="#tth15-top" class="relative grid min-h-11 place-items-center px-[18px] text-xs font-semibold uppercase tracking-[0.18em] -mr-[0.18em] text-tth15-mut no-underline transition-[letter-spacing,margin-right,color] duration-400 ease-[cubic-bezier(.25,.8,.25,1)] hover:tracking-[0.3em] hover:-mr-[0.3em] hover:text-tth15-ink focus-visible:text-tth15-ink focus-visible:outline-[1.5px] focus-visible:-outline-offset-4 focus-visible:outline-tth15-ink motion-reduce:transition-none">Ateliers</a>
      <a href="#tth15-top" class="relative grid min-h-11 place-items-center px-[18px] text-xs font-semibold uppercase tracking-[0.18em] -mr-[0.18em] text-tth15-mut no-underline transition-[letter-spacing,margin-right,color] duration-400 ease-[cubic-bezier(.25,.8,.25,1)] hover:tracking-[0.3em] hover:-mr-[0.3em] hover:text-tth15-ink focus-visible:text-tth15-ink focus-visible:outline-[1.5px] focus-visible:-outline-offset-4 focus-visible:outline-tth15-ink motion-reduce:transition-none">Archive</a>
    </nav>
    <p class="max-w-[58ch] text-[12.5px] leading-[1.7] text-tth15-mut">Hover the masthead &mdash; it expands around a stable centre: <code class="rounded bg-tth15-chip px-1.5 py-px font-tth15-mono text-[0.9em]">-mr-[0.46em]</code> mirrors <code class="rounded bg-tth15-chip px-1.5 py-px font-tth15-mono text-[0.9em]">tracking-[0.46em]</code> to swallow the phantom trailing space. The issue number tightens instead.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth15-bg: #f7f7f4;
  --color-tth15-bg: oklch(0.97 0.003 90);
  --color-tth15-chip: #e9e8e4;
  --color-tth15-chip: oklch(0.92 0.004 90);
  --color-tth15-ink: #141310;
  --color-tth15-ink: oklch(0.17 0.005 90);
  --color-tth15-mut: #67645d;
  --color-tth15-mut: oklch(0.49 0.008 90);
  --color-tth15-line: #dddcd7;
  --color-tth15-line: oklch(0.88 0.005 90);
  --font-tth15-sans: 'Hanken Grotesk', system-ui, sans-serif;
  --font-tth15-serif: 'Instrument Serif', Georgia, serif;
  --font-tth15-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-15 {
  width: 100%;
  min-height: 100svh;
}
```
