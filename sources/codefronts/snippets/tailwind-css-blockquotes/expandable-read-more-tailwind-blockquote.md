---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/expandable-read-more-tailwind-blockquote/"
title: "Expandable Read More Tailwind Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A long quote clamped to three lines with a fade, expanding on a native <details> toggle — no JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Read More Tailwind Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/expandable-read-more-tailwind-blockquote/

A long quote clamped to three lines with a fade, expanding on a native <details> toggle — no JavaScript. Utilities handle the clamp release (group-has-[[open]]/card:line-clamp-none), the label swap and the chevron; a six-line CSS block adds the smooth height animation via ::details-content + interpolate-size, which have no Tailwind variant.
## HTML
```html
<section class="tbq-24 w-full min-h-svh grid place-items-center bg-tbq24-bg px-5 py-14 font-tbq24-serif text-tbq24-ink" aria-label="Expandable read more blockquote demo">
  <div class="grid w-full justify-items-center gap-7">
    <figure class="group/card flex w-full max-w-[540px] flex-col rounded-[18px] border border-black/8 bg-tbq24-card p-[clamp(24px,4vw,34px)] shadow-[0_2px_6px_oklch(0.35_0.03_45/0.06),0_16px_40px_oklch(0.35_0.03_45/0.09)]">
      <p class="-order-2 mb-3.5 font-tbq24-sans text-[11.5px] font-bold tracking-[0.16em] uppercase text-tbq24-acc-ink">From “The Craftsman” · Richard Sennett</p>
      <details class="group/d contents">
        <summary class="order-1 mt-3 inline-flex min-h-11 cursor-pointer list-none items-center gap-2.5 self-start rounded-lg pe-1 font-tbq24-sans text-[13.5px] font-semibold text-tbq24-acc-ink hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tbq24-acc [&::-webkit-details-marker]:hidden">
          <span class="group-open/d:hidden">Read the full quote</span>
          <span class="hidden group-open/d:inline">Show less</span>
          <span aria-hidden="true" class="grid size-7 place-items-center rounded-full bg-tbq24-acc/12 transition-transform duration-300 group-open/d:rotate-180 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <blockquote>
          <p class="pt-[0.6em] text-[17.5px] leading-[1.68] text-tbq24-quiet text-pretty">It is the ability to focus on the work rather than ourselves that makes craft possible at all — and every workshop, digital or wooden, is finally an argument for patience over speed.</p>
        </blockquote>
      </details>
      <blockquote class="relative -order-1 after:pointer-events-none after:absolute after:inset-x-0 after:bottom-0 after:h-[1.7em] after:bg-linear-to-b after:from-transparent after:to-tbq24-card after:transition-opacity after:duration-300 group-has-[[open]]/card:after:opacity-0">
        <p class="line-clamp-3 text-[17.5px] leading-[1.68] text-tbq24-quiet text-pretty group-has-[[open]]/card:line-clamp-none">Craftsmanship names an enduring, basic human impulse: the desire to do a job well for its own sake. It cuts a far wider swath than skilled manual labor; it serves the programmer, the doctor, the artist, and the parent alike — anyone whose practice improves through the discipline of critique.</p>
      </blockquote>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq24-mono text-[11.5px] text-tbq24-mut">&lt;details&gt; · line-clamp-3 · group-has-[[open]]: · ::details-content</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq24-bg: #f8f2f0;
  --color-tbq24-bg: oklch(0.965 0.007 40);
  --color-tbq24-card: #ffffff;
  --color-tbq24-card: oklch(1 0 0);
  --color-tbq24-ink: #281f1c;
  --color-tbq24-ink: oklch(0.25 0.015 45);
  --color-tbq24-quiet: #4a403c;
  --color-tbq24-quiet: oklch(0.38 0.015 45);
  --color-tbq24-mut: #6b615c;
  --color-tbq24-mut: oklch(0.5 0.015 45);
  --color-tbq24-acc: #bd5833;
  --color-tbq24-acc: oklch(0.58 0.14 40);
  --color-tbq24-acc-ink: #9c4022;
  --color-tbq24-acc-ink: oklch(0.49 0.13 38);
  --font-tbq24-serif: 'Newsreader', Georgia, serif;
  --font-tbq24-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq24-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-24 {
  width: 100%;
  min-height: 100svh;
}
/* ::details-content has no Tailwind variant, and interpolate-size is what lets block-size reach auto. */

@supports (interpolate-size: allow-keywords) {
  .tbq-24 {
    interpolate-size: allow-keywords;
  }

  .tbq-24 details::details-content {
    block-size: 0;
    overflow: hidden;
    transition: block-size 0.45s cubic-bezier(0.2, 0.7, 0.2, 1), content-visibility 0.45s allow-discrete;
  }

  .tbq-24 details[open]::details-content {
    block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tbq-24 details::details-content {
    transition: none;
  }
}
```
