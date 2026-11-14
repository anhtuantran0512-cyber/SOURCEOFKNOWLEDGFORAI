---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/inline-highlighted-text-tailwind-blockquote/"
title: "Inline Highlighted Text Tailwind Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Annotated quote with two highlighter styles on real <mark> elements: a rounded wash that repeats its padding on every wrapped line (box-decoration-clone) and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Highlighted Text Tailwind Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/inline-highlighted-text-tailwind-blockquote/

Annotated quote with two highlighter styles on real <mark> elements: a rounded wash that repeats its padding on every wrapped line (box-decoration-clone) and a slanted-edge marker swipe. The port fixes two bugs in the original's swipe — its z-index:-1 pseudo-element slid behind the stage background, and as one absolute box it smeared across line breaks — by redrawing it as a cloned angled gradient, and makes the first highlight draw across on load.
## HTML
```html
<section class="tbq-15 w-full min-h-svh grid place-items-center bg-tbq15-bg px-5 py-14 font-tbq15-serif text-tbq15-ink" aria-label="Inline highlighted text blockquote demo">
  <div class="grid w-full justify-items-center gap-8">
    <figure class="max-w-[58ch]">
      <p class="mb-4 font-tbq15-sans text-[11.5px] font-bold tracking-[0.2em] uppercase text-tbq15-mut">Annotated · from the postmortem</p>
      <blockquote>
        <p class="text-[clamp(20px,2.6vw,26px)] leading-[1.7] text-pretty">The outage taught us that <mark class="rounded-[0.3em] bg-transparent bg-linear-to-r from-tbq15-hl to-tbq15-hl bg-[length:100%_100%] bg-no-repeat px-[0.3em] py-[0.08em] text-inherit box-decoration-clone transition-[background-size] duration-1000 ease-[cubic-bezier(0.6,0,0.3,1)] starting:bg-[length:0%_100%] motion-reduce:transition-none">alerting is a design problem, not a tooling problem</mark> — we had forty dashboards and zero answers. The fix wasn't another graph; it was deciding, in advance, <mark class="rounded-[0.4em_0.2em_0.45em_0.25em] bg-transparent bg-[linear-gradient(100deg,transparent_0.2em,var(--color-tbq15-hl2)_0.42em,var(--color-tbq15-hl2)_calc(100%_-_0.42em),transparent_calc(100%_-_0.2em))] px-[0.4em] py-[0.04em] text-inherit box-decoration-clone">which three numbers mean the site is healthy</mark> and paging on nothing else.</p>
      </blockquote>
      <figcaption class="mt-5 font-tbq15-sans text-[13px] text-tbq15-mut">Incident review, <cite class="italic">Q3 Reliability Report</cite> — highlights by the SRE lead</figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq15-mono text-[11.5px] text-tbq15-mut">&lt;mark&gt; · box-decoration-clone · angled-gradient swipe</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq15-bg: #fbfaf7;
  --color-tbq15-bg: oklch(0.985 0.004 95);
  --color-tbq15-ink: #231f17;
  --color-tbq15-ink: oklch(0.24 0.015 80);
  --color-tbq15-mut: #625d54;
  --color-tbq15-mut: oklch(0.48 0.015 80);
  --color-tbq15-hl: #f9d54499;
  --color-tbq15-hl: oklch(0.88 0.16 95 / 0.6);
  --color-tbq15-hl2: #fbb4e29e;
  --color-tbq15-hl2: oklch(0.85 0.1 340 / 0.62);
  --font-tbq15-serif: 'Newsreader', Georgia, serif;
  --font-tbq15-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq15-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-15 {
  width: 100%;
  min-height: 100svh;
}
```
