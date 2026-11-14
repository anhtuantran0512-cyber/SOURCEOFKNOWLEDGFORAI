---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/marker-highlight-underline-tailwind-blockquote/"
title: "Marker Highlight Underline Tailwind Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Three grades of marker underline in one sentence: a thick decoration-[0.22em] text-decoration, a gradient band that grows across the words…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Marker Highlight Underline Tailwind Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/marker-highlight-underline-tailwind-blockquote/

Three grades of marker underline in one sentence: a thick decoration-[0.22em] text-decoration, a gradient band that grows across the words (animate-tbq16-draw), and a hand-drawn SVG stroke that draws itself in. The port rewrites the SVG to pathLength="1" so the dash animation no longer depends on a hard-coded path length.
## HTML
```html
<section class="tbq-16 w-full min-h-svh grid place-items-center bg-tbq16-bg px-5 py-14 font-tbq16-serif text-tbq16-ink" aria-label="Marker highlight underline blockquote demo">
  <div class="grid w-full justify-items-center gap-8">
    <figure class="max-w-[56ch]">
      <blockquote>
        <p class="text-[clamp(22px,2.9vw,30px)] leading-[1.7] text-pretty">Write the docs <span class="underline decoration-tbq16-marker decoration-[0.22em] underline-offset-[0.16em] [text-decoration-skip-ink:none]">as if the reader is tired</span>, ship the API <span class="animate-tbq16-draw bg-[linear-gradient(var(--color-tbq16-m2),var(--color-tbq16-m2))] bg-[length:100%_0.42em] bg-[position:0_88%] bg-no-repeat box-decoration-clone motion-reduce:animate-none">as if the caller is distracted</span>, and design the defaults <span class="relative whitespace-nowrap">as if nobody reads either<svg class="absolute -bottom-[0.28em] -left-[0.1em] h-[0.4em] w-[calc(100%+0.2em)] animate-tbq16-stroke text-tbq16-m3 [stroke-dasharray:1] [stroke-dashoffset:1] motion-reduce:animate-none motion-reduce:[stroke-dashoffset:0]" viewBox="0 0 200 14" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M4 9c28-5 55 3 82-2s58-3 78 1c12 2 24 1 32-2" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/></svg></span>.</p>
      </blockquote>
      <figcaption class="mt-5 font-tbq16-sans text-[13.5px] text-tbq16-mut">— <strong class="font-semibold text-tbq16-ink">Engineering onboarding wall</strong>, week one</figcaption>
      <ul class="mt-4 flex flex-wrap gap-2" aria-label="Techniques used, in order">
        <li class="flex items-center gap-2 rounded-full border border-black/8 bg-white px-3 py-1.5 font-tbq16-mono text-[11px] text-tbq16-mut"><i aria-hidden="true" class="h-1.5 w-4 rounded-full bg-tbq16-marker"></i>text-decoration</li>
        <li class="flex items-center gap-2 rounded-full border border-black/8 bg-white px-3 py-1.5 font-tbq16-mono text-[11px] text-tbq16-mut"><i aria-hidden="true" class="h-1.5 w-4 rounded-full bg-tbq16-m2"></i>background band</li>
        <li class="flex items-center gap-2 rounded-full border border-black/8 bg-white px-3 py-1.5 font-tbq16-mono text-[11px] text-tbq16-mut"><i aria-hidden="true" class="h-1.5 w-4 rounded-full bg-tbq16-m3"></i>SVG stroke</li>
      </ul>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq16-mono text-[11.5px] text-tbq16-mut">decoration-[0.22em] · bg-[length:…] band · pathLength stroke</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq16-bg: #fcf8f4;
  --color-tbq16-bg: oklch(0.98 0.006 60);
  --color-tbq16-ink: #231b17;
  --color-tbq16-ink: oklch(0.23 0.015 50);
  --color-tbq16-mut: #675b54;
  --color-tbq16-mut: oklch(0.48 0.02 50);
  --color-tbq16-marker: #f98f3abf;
  --color-tbq16-marker: oklch(0.75 0.16 55 / 0.75);
  --color-tbq16-m2: #7acf7e8c;
  --color-tbq16-m2: oklch(0.78 0.14 145 / 0.55);
  --color-tbq16-m3: #ca66c3;
  --color-tbq16-m3: oklch(0.66 0.17 330);
  --font-tbq16-serif: 'Newsreader', Georgia, serif;
  --font-tbq16-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbq16-draw: tbq16-draw 1.2s cubic-bezier(0.6, 0, 0.3, 1) 0.3s both;
  --animate-tbq16-stroke: tbq16-stroke 1s ease-out 1.1s forwards;

  @keyframes tbq16-draw {
    from {
      background-size: 0% 0.42em;
    }

    to {
      background-size: 100% 0.42em;
    }
  }

  @keyframes tbq16-stroke {
    to {
      stroke-dashoffset: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-16 {
  width: 100%;
  min-height: 100svh;
}
```
