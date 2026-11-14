---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/modern-minimalist-left-border-tailwind-blockquote/"
title: "Modern Minimalist Left Border Tailwind Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "The quiet blog quote: a 2px logical rule (border-s-2, so it flips in RTL) and a serif italic line."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern Minimalist Left Border Tailwind Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/modern-minimalist-left-border-tailwind-blockquote/

The quiet blog quote: a 2px logical rule (border-s-2, so it flips in RTL) and a serif italic line. The Tailwind port keeps the hover accent but fixes how it moves — instead of animating padding (which reflowed every line of the quote), an accent rail draws down over the grey rule with before:scale-y-0 hover:before:scale-y-100, compositor-only.
## HTML
```html
<section class="tbq-05 w-full min-h-svh grid place-items-center bg-tbq05-bg px-5 py-14 font-tbq05-sans text-tbq05-ink" aria-label="Minimalist left border blockquote demo">
  <div class="grid w-full justify-items-center gap-8">
    <article class="w-full max-w-[60ch] text-[16.5px] leading-[1.72]">
      <p class="mb-2.5 text-xs font-semibold tracking-[0.12em] uppercase text-tbq05-mut">Design notes · 4 min read</p>
      <h1 class="mb-4 text-[clamp(26px,3.2vw,34px)] font-bold leading-[1.18] tracking-[-0.025em] text-balance">Interfaces that get out of the way</h1>
      <p class="text-tbq05-quiet text-pretty">The best tools disappear while you use them. We spent a year removing features from our editor, and usage went up every quarter. One reviewer put it better than we ever managed to:</p>
      <blockquote class="relative my-[1.6em] border-s-2 border-tbq05-rule ps-[1.25em] before:absolute before:inset-y-0 before:-start-0.5 before:w-0.5 before:origin-top before:scale-y-0 before:bg-tbq05-acc before:transition-transform before:duration-500 before:ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:before:scale-y-100 motion-reduce:before:transition-none">
        <p class="font-tbq05-serif text-[1.2em] leading-[1.55] italic text-tbq05-ink/85 text-pretty">It feels less like software and more like a well-lit room. Nothing asks for my attention until I ask for it, and then it is exactly where my hand already was.</p>
      </blockquote>
      <p class="text-tbq05-quiet text-pretty">That sentence is now taped above the team's door. Restraint, it turns out, is a feature you ship by deleting.</p>
    </article>
    <p aria-hidden="true" class="rounded-full border border-black/8 bg-white px-3.5 py-2 font-tbq05-mono text-[11.5px] text-tbq05-mut">border-s-2 · before:scale-y rail · RTL-safe</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq05-bg: #fbfaf8;
  --color-tbq05-bg: oklch(0.985 0.003 90);
  --color-tbq05-ink: #1f1c18;
  --color-tbq05-ink: oklch(0.23 0.01 80);
  --color-tbq05-quiet: #4b4742;
  --color-tbq05-quiet: oklch(0.4 0.01 80);
  --color-tbq05-mut: #68625a;
  --color-tbq05-mut: oklch(0.5 0.015 80);
  --color-tbq05-rule: #cecac3;
  --color-tbq05-rule: oklch(0.84 0.01 80);
  --color-tbq05-acc: #0a9068;
  --color-tbq05-acc: oklch(0.58 0.12 165);
  --font-tbq05-sans: 'Geist', system-ui, sans-serif;
  --font-tbq05-serif: 'Newsreader', Georgia, serif;
  --font-tbq05-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-05 {
  width: 100%;
  min-height: 100svh;
}
```
