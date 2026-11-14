---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/classic-left-border-tailwind-blockquote-snippet/"
title: "Classic Left Border Tailwind Blockquote Snippet"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "The ten-line blockquote everyone types from memory — left rule, soft wash, serif italic — but with language-aware quotation marks: [quotes:'“'_'”'_'‘'_'’']…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Classic Left Border Tailwind Blockquote Snippet
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/classic-left-border-tailwind-blockquote-snippet/

The ten-line blockquote everyone types from memory — left rule, soft wash, serif italic — but with language-aware quotation marks: [quotes:'“'_'”'_'‘'_'’'] plus before:content-[open-quote] means the nested <q> automatically gets single marks. No hard-coded characters in the text anywhere.
## HTML
```html
<section class="tbq-07 w-full min-h-svh grid place-items-center bg-tbq07-bg px-5 py-14 font-tbq07-sans text-tbq07-ink" aria-label="Classic left border blockquote demo">
  <div class="grid w-full justify-items-center gap-8">
    <article class="w-full max-w-[60ch] text-base leading-[1.7]">
      <h1 class="mb-3.5 text-[clamp(24px,3vw,30px)] font-bold tracking-[-0.02em] text-balance">The ten lines everyone starts with</h1>
      <p class="text-tbq07-quiet text-pretty">Ask a room of developers to style a quote and most will type the same thing from muscle memory. As one CSS textbook puts it:</p>
      <figure class="my-6">
        <blockquote class="rounded-r-[10px] border-l-4 border-tbq07-rule bg-tbq07-rule/10 px-5 py-4 font-tbq07-serif italic [quotes:'“'_'”'_'‘'_'’']">
          <p class="text-[1.12em] leading-[1.6] text-tbq07-quiet before:content-[open-quote] after:content-[close-quote]">The left-border blockquote persists because it solves the real problem — <q class="font-semibold text-tbq07-ink not-italic underline decoration-tbq07-rule/40 decoration-2 underline-offset-4">where does the quote end?</q> — with one line of CSS and no ambiguity.</p>
        </blockquote>
        <figcaption class="mt-2.5 flex items-center gap-2 ps-6 text-[13px] text-tbq07-mut"><span aria-hidden="true" class="h-px w-4 bg-tbq07-mut/60"></span><span>Sarah Drasner, <cite class="italic">Notes on Modern CSS</cite></span></figcaption>
      </figure>
      <p class="text-tbq07-quiet text-pretty">Note the nested <em>inner quote</em> above: it got single marks automatically. That's the <code class="rounded-md bg-tbq07-code px-1.5 py-px font-tbq07-mono text-[0.84em]">quotes</code> property tracking depth — no hard-coded characters anywhere.</p>
    </article>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq07-mono text-[11.5px] text-tbq07-mut">[quotes:…] · before:content-[open-quote] · bg-rule/10</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq07-bg: #f6f9fb;
  --color-tbq07-bg: oklch(0.98 0.005 240);
  --color-tbq07-ink: #1a2026;
  --color-tbq07-ink: oklch(0.24 0.015 250);
  --color-tbq07-quiet: #424850;
  --color-tbq07-quiet: oklch(0.4 0.015 250);
  --color-tbq07-mut: #5d646c;
  --color-tbq07-mut: oklch(0.5 0.015 250);
  --color-tbq07-rule: #4984bf;
  --color-tbq07-rule: oklch(0.6 0.11 250);
  --color-tbq07-code: #e2e9f0;
  --color-tbq07-code: oklch(0.93 0.012 250);
  --font-tbq07-serif: 'Newsreader', Georgia, serif;
  --font-tbq07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq07-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-07 {
  width: 100%;
  min-height: 100svh;
}
```
