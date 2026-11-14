---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/ide-code-comment-style-blockquote-tailwind/"
title: "IDE Code Comment Style Blockquote in Tailwind"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A quote dressed as a JSDoc comment inside an editor window — tab bar, CSS-counter line numbers, an active-line highlight, syntax colours and a blinking caret."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: IDE Code Comment Style Blockquote in Tailwind
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/ide-code-comment-style-blockquote-tailwind/

A quote dressed as a JSDoc comment inside an editor window — tab bar, CSS-counter line numbers, an active-line highlight, syntax colours and a blinking caret. The port styles all nine lines from the parent with arbitrary variants ([&>span]:before:content-[counter(tbq21-line)]) and adds whitespace-pre so the comment's asterisks finally line up like real code.
## HTML
```html
<section class="tbq-21 w-full min-h-svh grid place-items-center bg-tbq21-bg bg-[radial-gradient(80%_60%_at_50%_-10%,var(--color-tbq21-glow),transparent)] px-5 py-14 font-tbq21-sans text-tbq21-ink" aria-label="IDE code comment style blockquote demo">
  <div class="grid w-full justify-items-center gap-7">
    <figure class="w-full max-w-[640px] overflow-hidden rounded-[14px] border border-white/9 bg-tbq21-pane shadow-[0_26px_60px_oklch(0_0_0/0.5)]">
      <div class="flex items-stretch gap-3 border-b border-black/25 bg-tbq21-bar ps-3.5">
        <span aria-hidden="true" class="flex items-center gap-1.5 py-3"><i class="size-3 rounded-full bg-tbq21-red"></i><i class="size-3 rounded-full bg-tbq21-amber"></i><i class="size-3 rounded-full bg-tbq21-green"></i></span>
        <p class="ms-2 flex items-center gap-2 border-x border-t-2 border-x-black/25 border-t-tbq21-ts bg-tbq21-pane px-3.5 text-xs"><span aria-hidden="true" class="font-tbq21-mono text-[10px] font-bold text-tbq21-ts">TS</span>principles.ts</p>
        <span aria-hidden="true" class="ms-auto hidden items-center pe-3.5 font-tbq21-mono text-[10.5px] text-tbq21-lineno sm:flex">engineering-handbook</span>
      </div>
      <blockquote class="overflow-x-auto py-4">
        <code class="block font-tbq21-mono text-[13.5px] leading-[1.7] [counter-reset:tbq21-line] [&>span]:block [&>span]:pe-4 [&>span]:whitespace-pre [&>span]:transition-colors [&>span]:[counter-increment:tbq21-line] [&>span]:hover:bg-white/4 [&>span]:before:me-[1.8ch] [&>span]:before:inline-block [&>span]:before:w-[3.4ch] [&>span]:before:text-right [&>span]:before:text-tbq21-lineno [&>span]:before:select-none [&>span]:before:content-[counter(tbq21-line)]">
          <span><span class="text-tbq21-cmt">/**</span></span>
          <span><span class="text-tbq21-cmt"> * Every sufficiently senior engineer eventually</span></span>
          <span class="bg-tbq21-sel before:text-tbq21-ink!"><span class="text-tbq21-cmt"> * rewrites the same sentence:</span> <span class="text-tbq21-str">"make it work,"</span></span>
          <span><span class="text-tbq21-str"> * "make it right, make it fast"</span> <span class="text-tbq21-cmt">— in that order,</span></span>
          <span><span class="text-tbq21-cmt"> * and never all in the same pull request.</span></span>
          <span><span class="text-tbq21-cmt"> *</span></span>
          <span><span class="text-tbq21-cmt"> * </span><span class="font-semibold text-tbq21-tag">@author</span><span class="text-tbq21-cmt"> Kent Beck (paraphrasing generations)</span></span>
          <span><span class="text-tbq21-cmt"> * </span><span class="font-semibold text-tbq21-tag">@since</span><span class="text-tbq21-cmt">  forever</span></span>
          <span><span class="text-tbq21-cmt"> */</span><span aria-hidden="true" class="ms-0.5 inline-block h-[1.1em] w-0.5 animate-tbq21-blink bg-tbq21-ink align-[-0.18em] motion-reduce:animate-none"></span></span>
        </code>
      </blockquote>
      <figcaption class="flex justify-end gap-4.5 border-t border-black/25 bg-tbq21-bar px-3.5 py-2 font-tbq21-mono text-[10.5px] text-tbq21-lineno"><span>UTF-8</span><span>Ln 9, Col 4</span><span>Spaces: 2</span></figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-white/12 px-3.5 py-2 font-tbq21-mono text-[11.5px] text-tbq21-lineno">[&amp;&gt;span]:before:content-[counter()] · select-none gutter · whitespace-pre</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq21-bg: #0d0f15;
  --color-tbq21-bg: oklch(0.17 0.012 270);
  --color-tbq21-glow: #1a1b2b99;
  --color-tbq21-glow: oklch(0.23 0.03 280 / 0.6);
  --color-tbq21-pane: #16181f;
  --color-tbq21-pane: oklch(0.21 0.014 270);
  --color-tbq21-bar: #1f212a;
  --color-tbq21-bar: oklch(0.25 0.016 270);
  --color-tbq21-ink: #e1e5eb;
  --color-tbq21-ink: oklch(0.92 0.01 260);
  --color-tbq21-lineno: #767a84;
  --color-tbq21-lineno: oklch(0.58 0.015 265);
  --color-tbq21-cmt: #8cb894;
  --color-tbq21-cmt: oklch(0.74 0.07 150);
  --color-tbq21-tag: #ba9cef;
  --color-tbq21-tag: oklch(0.75 0.12 300);
  --color-tbq21-str: #ebb25f;
  --color-tbq21-str: oklch(0.8 0.12 75);
  --color-tbq21-sel: #262e3d;
  --color-tbq21-sel: oklch(0.3 0.03 265);
  --color-tbq21-ts: #55aee8;
  --color-tbq21-ts: oklch(0.72 0.12 240);
  --color-tbq21-red: #e85854;
  --color-tbq21-red: oklch(0.65 0.18 25);
  --color-tbq21-amber: #e3b831;
  --color-tbq21-amber: oklch(0.8 0.15 90);
  --color-tbq21-green: #54bf5c;
  --color-tbq21-green: oklch(0.72 0.17 145);
  --font-tbq21-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-tbq21-sans: 'Geist', system-ui, sans-serif;
  --animate-tbq21-blink: tbq21-blink 1.1s steps(1, end) infinite;

  @keyframes tbq21-blink {
    0%,
        49% {
      opacity: 1;
    }

    50%,
        100% {
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-21 {
  width: 100%;
  min-height: 100svh;
}
```
