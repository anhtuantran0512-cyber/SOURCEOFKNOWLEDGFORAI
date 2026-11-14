---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/multi-column-newspaper-editorial-blockquote-tailwind/"
title: "Multi-Column Newspaper Editorial Blockquote in Tailwind"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A broadsheet front page: blackletter masthead, headline, standfirst, three justified columns with hairline rules, a drop cap, and a crossing quote that spans…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Column Newspaper Editorial Blockquote in Tailwind
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/multi-column-newspaper-editorial-blockquote-tailwind/

A broadsheet front page: blackletter masthead, headline, standfirst, three justified columns with hairline rules, a drop cap, and a crossing quote that spans all columns mid-flow with [column-span:all]. Columns step 3 → 2 → 1 with @max-[680px]:columns-2 and @max-[460px]:columns-1 on the paper's own width.
## HTML
```html
<section class="tbq-20 w-full min-h-svh grid place-items-center bg-tbq20-desk px-[clamp(12px,4vw,48px)] py-12 font-tbq20-serif text-tbq20-ink" lang="en" aria-label="Multi-column newspaper editorial blockquote demo">
  <div class="grid w-full justify-items-center gap-6">
    <article class="@container w-full max-w-[860px] bg-tbq20-paper p-[clamp(20px,4vw,44px)] shadow-[0_2px_4px_oklch(0.3_0.02_80/0.12),0_18px_44px_oklch(0.3_0.02_80/0.18)]">
      <header class="grid grid-cols-[1fr_auto_1fr] items-end gap-3 border-b-3 border-double border-tbq20-ink pb-2.5 @max-[520px]:grid-cols-1 @max-[520px]:justify-items-center">
        <p class="font-tbq20-sans text-[10px] tracking-[0.1em] uppercase text-tbq20-mut @max-[520px]:hidden">Vol. CXIV · No. 218</p>
        <p class="font-tbq20-fraktur text-[clamp(26px,5.2cqi,46px)] leading-none">The Morning Ledger</p>
        <p class="text-right font-tbq20-sans text-[10px] tracking-[0.1em] uppercase text-tbq20-mut @max-[520px]:text-center">Tuesday, August 5, 2026</p>
      </header>
      <h1 class="mt-5 text-[clamp(26px,4.6cqi,42px)] leading-[1.06] font-bold tracking-[-0.015em] text-balance">The quiet return of the printed page's best ideas</h1>
      <p class="mt-2.5 border-b border-tbq20-hair pb-3.5 text-[15px] italic text-tbq20-mut text-pretty">Web typography spent twenty years reinventing what compositors solved by hand — now the CSS to do it properly ships in every browser</p>
      <div class="mt-4.5 columns-3 gap-[2.2em] text-justify text-[13.5px] leading-[1.62] hyphens-auto [column-rule:1px_solid_var(--color-tbq20-hair)] @max-[680px]:columns-2 @max-[460px]:columns-1 @max-[460px]:text-left @max-[460px]:hyphens-none">
        <p class="first-letter:float-left first-letter:pt-[0.06em] first-letter:pr-[0.1em] first-letter:text-[3.3em] first-letter:leading-[0.8] first-letter:font-bold first-letter:text-tbq20-acc">For most of the web's life, the column was a metaphor rather than a measurement. Text ran the full width of whatever glass it landed on, and the craft of the compositor — the measured line, the balanced page, the rule between columns — survived only in PDFs and nostalgia.</p>
        <p class="mt-[0.7em]">The tools arrived quietly. Multi-column layout shipped, then column rules, then spanning elements; hyphenation dictionaries came to every major engine. What did not arrive was the habit of using them.</p>
        <blockquote class="my-[1em] border-y-2 border-tbq20-ink py-[0.9em] text-center [column-span:all]">
          <p class="mx-auto max-w-[36ch] text-[clamp(18px,2.8cqi,25px)] leading-[1.35] font-semibold italic tracking-[-0.01em] text-balance hyphens-none">“A newspaper page is an argument about attention — every rule, gutter and crossing quote tells the eye what matters next.”</p>
          <footer class="mt-2 flex items-center justify-center gap-2.5 font-tbq20-sans text-[11px] tracking-[0.08em] uppercase not-italic text-tbq20-mut"><span aria-hidden="true" class="h-px w-6 bg-tbq20-acc"></span>Edda Marston, <cite class="italic normal-case">The Composed Page</cite> (2024)<span aria-hidden="true" class="h-px w-6 bg-tbq20-acc"></span></footer>
        </blockquote>
        <p>Designers who grew up on component libraries often meet these properties with suspicion, as if flowing text were a legacy behavior. Yet the reading research is stubborn: shorter measures read faster, and rules between columns cut skip-backs by a measurable fraction.</p>
        <p class="mt-[0.7em]">The crossing quote above is one property doing what frameworks cannot: interrupting a live text flow, borrowing its full width, and handing the reader back to the exact sentence they left. The linotype operators had a word for it. They called it Tuesday.</p>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-black/12 bg-tbq20-paper px-3.5 py-2 font-tbq20-mono text-[11.5px] text-tbq20-mut">columns-3 · [column-span:all] · @max-[460px]:columns-1</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq20-desk: #dcd7cd;
  --color-tbq20-desk: oklch(0.88 0.015 85);
  --color-tbq20-paper: #f9f7f1;
  --color-tbq20-paper: oklch(0.975 0.008 90);
  --color-tbq20-ink: #191511;
  --color-tbq20-ink: oklch(0.2 0.01 70);
  --color-tbq20-mut: #57514c;
  --color-tbq20-mut: oklch(0.44 0.012 70);
  --color-tbq20-hair: #b3ada4;
  --color-tbq20-hair: oklch(0.75 0.015 80);
  --color-tbq20-acc: #903129;
  --color-tbq20-acc: oklch(0.45 0.13 28);
  --font-tbq20-serif: 'Newsreader', Georgia, serif;
  --font-tbq20-fraktur: 'UnifrakturMaguntia', 'Old English Text MT', serif;
  --font-tbq20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq20-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-20 {
  width: 100%;
  min-height: 100svh;
}
```
