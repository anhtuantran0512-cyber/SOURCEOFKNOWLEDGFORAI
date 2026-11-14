---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-on-multiline-paragraph/"
title: "Tailwind Gradient Text on Multiline Paragraph"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "How gradient text behaves when it wraps &mdash; demonstrated, not just described."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Text on Multiline Paragraph
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-on-multiline-paragraph/

How gradient text behaves when it wraps &mdash; demonstrated, not just described. An editorial article sets a multiline gradient headline and blockquote, then puts the two models side by side: one gradient across the whole block, versus box-decoration-clone giving every line its own full ramp.
## HTML
```html
<section class="ttg-19 w-full min-h-svh bg-ttg19-bg font-ttg19-serif text-ttg19-ink" aria-labelledby="ttg19-title">
  <article class="mx-auto max-w-2xl px-6 py-16">
    <p class="font-ttg19-sans text-xs font-semibold tracking-[0.14em] text-ttg19-mut uppercase">Technique spotlight</p>
    <h1 id="ttg19-title" class="mt-5 bg-linear-110 from-ttg19-a via-ttg19-b to-ttg19-c bg-clip-text pb-[0.06em] text-[clamp(2.1rem,5.6vw,3.25rem)] leading-[1.14] font-semibold tracking-[-0.02em] text-transparent text-balance">Design is not just what it looks like — it's how it works.</h1>
    <p class="mt-6 font-ttg19-sans text-[15.5px]/[1.75] text-ttg19-mut text-pretty">When a gradient is applied to a multiline element, the background covers the element's whole box, so each line samples a different section of the ramp.</p>
    <blockquote class="mt-8 flex gap-5">
      <span aria-hidden="true" class="w-[3px] flex-none rounded-full bg-linear-to-b from-ttg19-a to-ttg19-c"></span>
      <p class="bg-linear-110 from-ttg19-a via-ttg19-b to-ttg19-c to-90% bg-clip-text text-[19px]/[1.65] text-transparent italic">A <code class="rounded bg-ttg19-a/8 px-1.5 py-0.5 font-ttg19-mono text-[0.78em] text-ttg19-b not-italic">linear-gradient(to right)</code> stretches across the widest line — narrower lines sample only part of it, which is why a short last line ends in a different hue.</p>
    </blockquote>
    <div class="mt-12 grid gap-4 font-ttg19-sans sm:grid-cols-2">
      <figure class="rounded-2xl border border-ttg19-line bg-white p-5">
        <figcaption class="font-ttg19-mono text-[11.5px] text-ttg19-mut">block · one gradient for the box</figcaption>
        <p class="mt-3 bg-linear-to-r from-ttg19-a to-ttg19-c bg-clip-text text-[19px]/[1.5] font-bold text-transparent">Every line shares one ramp, so the last short line stops partway.</p>
      </figure>
      <figure class="rounded-2xl border border-ttg19-line bg-white p-5">
        <figcaption class="font-ttg19-mono text-[11.5px] text-ttg19-mut">inline · box-decoration-clone</figcaption>
        <p class="mt-3 text-[19px]/[1.5] font-bold"><span class="bg-linear-to-r from-ttg19-a to-ttg19-c bg-clip-text box-decoration-clone text-transparent">Every line gets its own full ramp, start to finish, however short.</span></p>
      </figure>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg19-bg: #fbfaf8;
  --color-ttg19-bg: oklch(0.985 0.003 80);
  --color-ttg19-ink: #1c1917;
  --color-ttg19-ink: oklch(0.22 0.006 60);
  --color-ttg19-mut: #615a55;
  --color-ttg19-mut: oklch(0.47 0.012 55);
  --color-ttg19-line: #e9e5e1;
  --color-ttg19-line: oklch(0.925 0.008 60);
  --color-ttg19-a: #4338ca;
  --color-ttg19-a: oklch(0.46 0.21 277);
  --color-ttg19-b: #7c3aed;
  --color-ttg19-b: oklch(0.54 0.25 293);
  --color-ttg19-c: #a21caf;
  --color-ttg19-c: oklch(0.52 0.23 322);
  --font-ttg19-serif: 'Newsreader', Georgia, serif;
  --font-ttg19-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg19-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.ttg-19 {
  width: 100%;
  min-height: 100svh;
}
```
