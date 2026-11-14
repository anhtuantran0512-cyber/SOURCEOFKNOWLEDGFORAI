---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/article-pull-quote-tailwind-design-wrap-text/"
title: "Article Pull Quote Tailwind Design with Wrap Text"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Magazine pull quote floated into the running text with float-end and [shape-outside:margin-box], collapsing to a full-width block below 520px of article…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Article Pull Quote Tailwind Design with Wrap Text
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/article-pull-quote-tailwind-design-wrap-text/

Magazine pull quote floated into the running text with float-end and [shape-outside:margin-box], collapsing to a full-width block below 520px of article width via @max-[520px]:float-none. The port adds a drop cap with first-letter: utilities and hides the duplicated pull text from screen readers so it isn't read twice.
## HTML
```html
<section class="tbq-11 w-full min-h-svh grid place-items-center bg-tbq11-bg px-5 py-14 font-tbq11-serif text-tbq11-ink" aria-label="Pull quote with wrapped text demo">
  <div class="grid w-full justify-items-center gap-7">
    <article class="@container w-full max-w-[66ch]">
      <p class="mb-2.5 font-tbq11-sans text-[11.5px] font-bold tracking-[0.22em] uppercase text-tbq11-acc">The Craft Issue · Longform</p>
      <h1 class="mb-5 text-[clamp(28px,3.8vw,42px)] leading-[1.1] font-semibold tracking-[-0.02em] text-balance">What we lost when everything became a feed</h1>
      <div class="flow-root text-[16.5px] leading-[1.75] text-tbq11-quiet">
        <aside aria-hidden="true" class="float-end ms-6.5 mt-[0.35em] mb-[0.8em] w-[min(46%,300px)] border-t-3 border-tbq11-acc pt-[0.55em] [shape-outside:margin-box] @max-[520px]:float-none @max-[520px]:mx-0 @max-[520px]:my-5 @max-[520px]:w-full">
          <p class="text-[1.5em] leading-[1.22] font-semibold tracking-[-0.015em] text-tbq11-ink text-pretty before:text-tbq11-acc before:content-['“']">Pages had edges. A feed has no edges, and so it has no shape — and nothing without a shape can be finished.</p>
        </aside>
        <p class="first-letter:float-left first-letter:mt-[0.06em] first-letter:mr-[0.1em] first-letter:text-[3.4em] first-letter:leading-[0.8] first-letter:font-semibold first-letter:text-tbq11-acc">Print editors used to speak about the architecture of a page the way builders speak about load: every column carried weight, and white space was a decision someone signed off on. A reader could feel — without ever articulating it — that the page had been <em>composed</em>.</p>
        <p class="mt-3.5">Pages had edges. A feed has no edges, and so it has no shape — and nothing without a shape can be finished. The infinite scroll made publishing cheaper and reading thinner in the same gesture, and we are still doing the accounting.</p>
        <p class="mt-3.5">The designers interviewed for this piece kept returning to the same word: boundaries. Not as nostalgia, but as a craft constraint that made every inclusion mean something.</p>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq11-mono text-[11.5px] text-tbq11-mut">float-end · [shape-outside:margin-box] · @max-[520px]:float-none</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq11-bg: #f9f6f2;
  --color-tbq11-bg: oklch(0.975 0.006 75);
  --color-tbq11-ink: #201914;
  --color-tbq11-ink: oklch(0.22 0.015 60);
  --color-tbq11-quiet: #49413b;
  --color-tbq11-quiet: oklch(0.38 0.015 60);
  --color-tbq11-mut: #6c6158;
  --color-tbq11-mut: oklch(0.5 0.02 60);
  --color-tbq11-acc: #bd413f;
  --color-tbq11-acc: oklch(0.55 0.16 25);
  --font-tbq11-serif: 'Newsreader', Georgia, serif;
  --font-tbq11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq11-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-11 {
  width: 100%;
  min-height: 100svh;
}
```
