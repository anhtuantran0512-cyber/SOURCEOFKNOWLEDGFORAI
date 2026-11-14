---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/brutalist-tailwind-blockquote-design/"
title: "Brutalist Tailwind Blockquote Design"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Neo-brutalist quote: 3px ink borders, a hard shadow-[8px_8px_0_…], zero radius and a tilted sticker for attribution, on ruled-paper background."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Tailwind Blockquote Design
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/brutalist-tailwind-blockquote-design/

Neo-brutalist quote: 3px ink borders, a hard shadow-[8px_8px_0_…], zero radius and a tilted sticker for attribution, on ruled-paper background. Hover presses the card halfway into its shadow; active: presses it flat. The port drops the original's tabindex="0" on a non-interactive card and gives the sticker a group-hover:rotate-1 wobble instead.
## HTML
```html
<section class="tbq-08 w-full min-h-svh grid place-items-center bg-tbq08-bg bg-[repeating-linear-gradient(0deg,transparent_0_23px,var(--color-tbq08-line)_23px_24px)] px-6 py-16 font-tbq08-sans text-tbq08-ink" aria-label="Brutalist blockquote demo">
  <div class="grid w-full justify-items-center gap-14">
    <figure class="group relative w-full max-w-[540px]">
      <div class="border-3 border-tbq08-ink bg-tbq08-pop px-7 pt-6.5 pb-9 shadow-[8px_8px_0_var(--color-tbq08-ink)] transition-[translate,box-shadow] duration-150 ease-out hover:translate-x-1 hover:translate-y-1 hover:shadow-[4px_4px_0_var(--color-tbq08-ink)] active:translate-x-2 active:translate-y-2 active:shadow-[0_0_0_var(--color-tbq08-ink)] motion-reduce:transition-none">
        <p class="mb-4 inline-flex items-center gap-2 bg-tbq08-ink px-2.5 py-1.5 font-tbq08-mono text-[11px] font-bold tracking-[0.08em] uppercase text-tbq08-paper"><span aria-hidden="true" class="size-2 bg-tbq08-pop"></span>Quote_004.txt</p>
        <blockquote>
          <p class="text-[clamp(21px,2.8vw,28px)] leading-[1.28] font-bold tracking-[-0.02em] text-pretty">Perfection is a lie the tools sell you. Ship the thing with the seams showing — at least everyone can see how it's made.</p>
        </blockquote>
      </div>
      <figcaption class="absolute -right-2.5 -bottom-6 -rotate-2 border-3 border-tbq08-ink bg-tbq08-paper px-3 py-2 font-tbq08-mono text-[11.5px] font-bold tracking-[0.06em] shadow-[5px_5px_0_var(--color-tbq08-ink)] transition-transform duration-200 group-hover:rotate-1 motion-reduce:transition-none">— RIKO TANAKA, ZINE PUBLISHER</figcaption>
    </figure>
    <p aria-hidden="true" class="border-2 border-tbq08-ink bg-tbq08-paper px-3.5 py-2 font-tbq08-mono text-[11.5px] font-bold">shadow-[8px_8px_0] · hover:translate · active:press flat</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq08-bg: #ece8d9;
  --color-tbq08-bg: oklch(0.93 0.02 95);
  --color-tbq08-line: #d5d1c3;
  --color-tbq08-line: oklch(0.86 0.02 95);
  --color-tbq08-ink: #181611;
  --color-tbq08-ink: oklch(0.2 0.01 90);
  --color-tbq08-pop: #fadf27;
  --color-tbq08-pop: oklch(0.9 0.18 100);
  --color-tbq08-paper: #fdfcf8;
  --color-tbq08-paper: oklch(0.99 0.005 95);
  --font-tbq08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tbq08-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-08 {
  width: 100%;
  min-height: 100svh;
}
```
