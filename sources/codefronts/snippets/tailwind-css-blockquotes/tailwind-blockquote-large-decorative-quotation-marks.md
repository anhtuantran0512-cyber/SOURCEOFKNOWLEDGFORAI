---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/tailwind-blockquote-large-decorative-quotation-marks/"
title: "Tailwind Blockquote with Large Decorative Quotation Marks"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "The most-searched quote treatment, ported whole into utilities: an editorial serif quote crowned by a giant opening mark drawn with before:content-['“']."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Blockquote with Large Decorative Quotation Marks
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/tailwind-blockquote-large-decorative-quotation-marks/

The most-searched quote treatment, ported whole into utilities: an editorial serif quote crowned by a giant opening mark drawn with before:content-['“']. The mark is generated (invisible to screen readers), tinted with the opacity modifier text-tbq01-acc/40 — Tailwind's spelling of color-mix() — and cropped with before:h-[0.5em] so the first line sits inside its curl.
## HTML
```html
<section class="tbq-01 w-full min-h-svh grid place-items-center bg-tbq01-bg bg-[radial-gradient(120%_90%_at_50%_0%,var(--color-tbq01-glow),transparent_70%)] px-5 py-14 font-tbq01-serif text-tbq01-ink" aria-label="Large decorative quotation marks blockquote demo">
  <div class="grid w-full justify-items-center gap-8">
    <figure class="w-full max-w-[38rem]">
      <blockquote class="before:-mb-[0.02em] before:-ml-[0.07em] before:block before:h-[0.5em] before:font-tbq01-serif before:text-[clamp(150px,22vw,220px)] before:leading-none before:text-tbq01-acc/40 before:content-['“']">
        <p class="text-[clamp(22px,3.4vw,34px)] leading-[1.38] tracking-[-0.012em] italic text-balance">Typography is the craft of endowing human language with a durable visual form. It is what turns a wall of words into a voice.</p>
      </blockquote>
      <figcaption class="mt-7 flex items-center gap-3.5 font-tbq01-sans text-sm text-tbq01-mut">
        <span aria-hidden="true" class="h-0.5 w-11 flex-none rounded-full bg-tbq01-acc"></span>
        <span><strong class="font-semibold text-tbq01-ink">Robert Bringhurst</strong> · <cite class="italic">The Elements of Typographic Style</cite></span>
      </figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-tbq01-ink/12 bg-white/60 px-3.5 py-2 font-tbq01-mono text-[11.5px] text-tbq01-mut">before:content-['“'] · text-tbq01-acc/40 · text-balance</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq01-bg: #f8f5ef;
  --color-tbq01-bg: oklch(0.97 0.008 85);
  --color-tbq01-glow: #fffdfa;
  --color-tbq01-glow: oklch(0.995 0.004 85);
  --color-tbq01-ink: #261d16;
  --color-tbq01-ink: oklch(0.24 0.02 60);
  --color-tbq01-mut: #61564d;
  --color-tbq01-mut: oklch(0.46 0.02 60);
  --color-tbq01-acc: #af5331;
  --color-tbq01-acc: oklch(0.55 0.13 40);
  --font-tbq01-serif: 'Newsreader', Georgia, serif;
  --font-tbq01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq01-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-01 {
  width: 100%;
  min-height: 100svh;
}
```
