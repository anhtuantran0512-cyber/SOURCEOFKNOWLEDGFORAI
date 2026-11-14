---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/editorial-horizontal-accordion-numbered-spines-tailwind/"
title: "Editorial Horizontal Accordion with Numbered Spines in Tailwind"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A magazine table of contents turned interactive: cream paper, a heavy ink rule top and bottom, hairline column rules, and a giant ghosted serif numeral on…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Horizontal Accordion with Numbered Spines in Tailwind
Source: https://codefronts.com/navigation/tailwind-css-accordions/editorial-horizontal-accordion-numbered-spines-tailwind/

A magazine table of contents turned interactive: cream paper, a heavy ink rule top and bottom, hairline column rules, and a giant ghosted serif numeral on every spine. Opening a story swells the same numeral from scale-[.55] to scale-100 and tints it red while the headline, italic dek and byline set over it like an art-directed spread.
## HTML
```html
<section class="tac-28 w-full min-h-svh grid place-items-center bg-tac28-bg px-5 py-14 font-tac28-body text-tac28-ink" aria-label="Editorial numbered spine horizontal accordion demo">
  <div class="grid w-full max-w-5xl gap-8">
    <header class="grid gap-5">
      <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1 border-y-[3px] border-double border-tac28-ink py-2 font-tac28-mono text-[11px] tracking-[0.18em] text-tac28-ink uppercase">
        <span>The Quiet Review</span>
        <span class="text-tac28-mut">No. 48 · Autumn 2026</span>
      </div>
      <div class="flex flex-wrap items-end justify-between gap-x-10 gap-y-3">
        <h2 class="font-tac28-serif text-[clamp(40px,7vw,76px)] leading-[0.9] font-semibold tracking-[-0.04em]">Contents<span class="text-tac28-red">.</span></h2>
        <p class="max-w-[36ch] font-tac28-body text-lg leading-snug text-tac28-soft italic">Four long reads on craft, memory and the virtue of taking your time.</p>
      </div>
    </header>

    <div class="@container/row w-full">
      <div role="radiogroup" aria-label="Issue contents" class="flex h-[27rem] border-y-2 border-tac28-ink @max-2xl/row:h-auto @max-2xl/row:flex-col">

        <label class="group/p relative flex min-w-20 grow basis-0 cursor-pointer overflow-hidden border-l border-tac28-rule transition-[flex-grow,background-color] duration-[600ms] ease-[cubic-bezier(.6,0,.2,1)] first:border-l-0 hover:bg-tac28-hover has-checked:grow-[5] has-checked:bg-tac28-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-[-6px] has-focus-visible:outline-tac28-red motion-reduce:transition-none @max-2xl/row:basis-auto @max-2xl/row:flex-col @max-2xl/row:border-t @max-2xl/row:border-l-0 @max-2xl/row:first:border-t-0">
          <input type="radio" name="tac28-story" id="tac28-interview" class="sr-only" checked>
          <span aria-hidden="true" class="pointer-events-none absolute top-2 left-3 origin-top-left scale-[.55] font-tac28-serif text-[15rem] leading-[0.8] font-black tracking-[-0.06em] text-tac28-ink/[0.09] transition-[scale,color,translate] duration-[600ms] ease-[cubic-bezier(.6,0,.2,1)] group-hover/p:text-tac28-ink/[0.16] group-has-checked/p:translate-x-3 group-has-checked/p:scale-100 group-has-checked/p:text-tac28-red/[0.14] motion-reduce:transition-none @max-2xl/row:hidden">1</span>
          <span class="absolute inset-x-0 bottom-6 flex flex-col items-center gap-3 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl/row:relative @max-2xl/row:bottom-0 @max-2xl/row:min-h-[4.5rem] @max-2xl/row:flex-row @max-2xl/row:gap-4 @max-2xl/row:px-4 @max-2xl/row:group-has-checked/p:opacity-100">
            <i class="hidden font-tac28-serif text-4xl leading-none font-black not-italic text-tac28-red @max-2xl/row:block">1</i>
            <span aria-hidden="true" class="h-0.5 w-7 bg-tac28-red @max-2xl/row:hidden"></span>
            <b class="rotate-180 font-tac28-mono text-[11.5px] font-semibold tracking-[0.2em] text-tac28-mut uppercase transition-colors [writing-mode:vertical-rl] group-hover/p:text-tac28-ink @max-2xl/row:rotate-0 @max-2xl/row:text-tac28-ink @max-2xl/row:[writing-mode:horizontal-tb]">The Interview</b>
            <span class="hidden font-tac28-mono text-[11px] text-tac28-mut @max-2xl/row:ml-auto @max-2xl/row:block">p. 14</span>
          </span>
          <span class="relative z-10 flex min-w-0 flex-1 translate-y-2.5 items-end opacity-0 transition-[opacity,translate] duration-[400ms] group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-[250ms] motion-reduce:transition-none @max-2xl/row:grid @max-2xl/row:grid-rows-[0fr] @max-2xl/row:translate-y-0 @max-2xl/row:transition-[grid-template-rows,opacity] @max-2xl/row:group-has-checked/p:grid-rows-[1fr] @max-2xl/row:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[24rem] overflow-hidden @max-2xl/row:min-h-0 @max-2xl/row:min-w-0">
              <span class="block px-9 pt-6 pb-8 @max-2xl/row:px-4 @max-2xl/row:pt-0 @max-2xl/row:pb-6">
                <span class="flex items-center gap-3 font-tac28-mono text-[11px] font-semibold tracking-[0.18em] text-tac28-red uppercase @max-2xl/row:hidden">The Interview<span aria-hidden="true" class="h-px flex-1 bg-tac28-rule"></span><span class="font-medium tracking-[0.08em] text-tac28-mut">p. 14</span></span>
                <b class="mt-4 block max-w-[17ch] font-tac28-serif text-[clamp(28px,3.6vw,42px)] leading-[1.02] font-semibold tracking-[-0.025em] text-balance text-tac28-ink @max-2xl/row:mt-0">The last typesetter of Fleet Street</b>
                <span class="mt-4 block max-w-[42ch] font-tac28-body text-lg leading-snug text-tac28-soft italic">Sixty years of hot metal, and what the craft knew that the software forgot.</span>
                <span class="mt-6 flex flex-wrap items-center gap-x-3 gap-y-1 border-t border-tac28-ink pt-3 font-tac28-mono text-[11px] tracking-[0.08em] text-tac28-mut uppercase"><span class="text-tac28-ink">Words by Margaret Okafor</span><span aria-hidden="true">·</span>18 min read</span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p relative flex min-w-20 grow basis-0 cursor-pointer overflow-hidden border-l border-tac28-rule transition-[flex-grow,background-color] duration-[600ms] ease-[cubic-bezier(.6,0,.2,1)] first:border-l-0 hover:bg-tac28-hover has-checked:grow-[5] has-checked:bg-tac28-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-[-6px] has-focus-visible:outline-tac28-red motion-reduce:transition-none @max-2xl/row:basis-auto @max-2xl/row:flex-col @max-2xl/row:border-t @max-2xl/row:border-l-0 @max-2xl/row:first:border-t-0">
          <input type="radio" name="tac28-story" id="tac28-report" class="sr-only">
          <span aria-hidden="true" class="pointer-events-none absolute top-2 left-3 origin-top-left scale-[.55] font-tac28-serif text-[15rem] leading-[0.8] font-black tracking-[-0.06em] text-tac28-ink/[0.09] transition-[scale,color,translate] duration-[600ms] ease-[cubic-bezier(.6,0,.2,1)] group-hover/p:text-tac28-ink/[0.16] group-has-checked/p:translate-x-3 group-has-checked/p:scale-100 group-has-checked/p:text-tac28-red/[0.14] motion-reduce:transition-none @max-2xl/row:hidden">2</span>
          <span class="absolute inset-x-0 bottom-6 flex flex-col items-center gap-3 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl/row:relative @max-2xl/row:bottom-0 @max-2xl/row:min-h-[4.5rem] @max-2xl/row:flex-row @max-2xl/row:gap-4 @max-2xl/row:px-4 @max-2xl/row:group-has-checked/p:opacity-100">
            <i class="hidden font-tac28-serif text-4xl leading-none font-black not-italic text-tac28-red @max-2xl/row:block">2</i>
            <span aria-hidden="true" class="h-0.5 w-7 bg-tac28-red @max-2xl/row:hidden"></span>
            <b class="rotate-180 font-tac28-mono text-[11.5px] font-semibold tracking-[0.2em] text-tac28-mut uppercase transition-colors [writing-mode:vertical-rl] group-hover/p:text-tac28-ink @max-2xl/row:rotate-0 @max-2xl/row:text-tac28-ink @max-2xl/row:[writing-mode:horizontal-tb]">Field Report</b>
            <span class="hidden font-tac28-mono text-[11px] text-tac28-mut @max-2xl/row:ml-auto @max-2xl/row:block">p. 32</span>
          </span>
          <span class="relative z-10 flex min-w-0 flex-1 translate-y-2.5 items-end opacity-0 transition-[opacity,translate] duration-[400ms] group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-[250ms] motion-reduce:transition-none @max-2xl/row:grid @max-2xl/row:grid-rows-[0fr] @max-2xl/row:translate-y-0 @max-2xl/row:transition-[grid-template-rows,opacity] @max-2xl/row:group-has-checked/p:grid-rows-[1fr] @max-2xl/row:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[24rem] overflow-hidden @max-2xl/row:min-h-0 @max-2xl/row:min-w-0">
              <span class="block px-9 pt-6 pb-8 @max-2xl/row:px-4 @max-2xl/row:pt-0 @max-2xl/row:pb-6">
                <span class="flex items-center gap-3 font-tac28-mono text-[11px] font-semibold tracking-[0.18em] text-tac28-red uppercase @max-2xl/row:hidden">Field Report<span aria-hidden="true" class="h-px flex-1 bg-tac28-rule"></span><span class="font-medium tracking-[0.08em] text-tac28-mut">p. 32</span></span>
                <b class="mt-4 block max-w-[17ch] font-tac28-serif text-[clamp(28px,3.6vw,42px)] leading-[1.02] font-semibold tracking-[-0.025em] text-balance text-tac28-ink @max-2xl/row:mt-0">Notes from the seed vault</b>
                <span class="mt-4 block max-w-[42ch] font-tac28-body text-lg leading-snug text-tac28-soft italic">Inside the Arctic archive where every harvest on earth keeps a backup copy.</span>
                <span class="mt-6 flex flex-wrap items-center gap-x-3 gap-y-1 border-t border-tac28-ink pt-3 font-tac28-mono text-[11px] tracking-[0.08em] text-tac28-mut uppercase"><span class="text-tac28-ink">Words by Tove Lindqvist</span><span aria-hidden="true">·</span>12 min read</span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p relative flex min-w-20 grow basis-0 cursor-pointer overflow-hidden border-l border-tac28-rule transition-[flex-grow,background-color] duration-[600ms] ease-[cubic-bezier(.6,0,.2,1)] first:border-l-0 hover:bg-tac28-hover has-checked:grow-[5] has-checked:bg-tac28-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-[-6px] has-focus-visible:outline-tac28-red motion-reduce:transition-none @max-2xl/row:basis-auto @max-2xl/row:flex-col @max-2xl/row:border-t @max-2xl/row:border-l-0 @max-2xl/row:first:border-t-0">
          <input type="radio" name="tac28-story" id="tac28-essay" class="sr-only">
          <span aria-hidden="true" class="pointer-events-none absolute top-2 left-3 origin-top-left scale-[.55] font-tac28-serif text-[15rem] leading-[0.8] font-black tracking-[-0.06em] text-tac28-ink/[0.09] transition-[scale,color,translate] duration-[600ms] ease-[cubic-bezier(.6,0,.2,1)] group-hover/p:text-tac28-ink/[0.16] group-has-checked/p:translate-x-3 group-has-checked/p:scale-100 group-has-checked/p:text-tac28-red/[0.14] motion-reduce:transition-none @max-2xl/row:hidden">3</span>
          <span class="absolute inset-x-0 bottom-6 flex flex-col items-center gap-3 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl/row:relative @max-2xl/row:bottom-0 @max-2xl/row:min-h-[4.5rem] @max-2xl/row:flex-row @max-2xl/row:gap-4 @max-2xl/row:px-4 @max-2xl/row:group-has-checked/p:opacity-100">
            <i class="hidden font-tac28-serif text-4xl leading-none font-black not-italic text-tac28-red @max-2xl/row:block">3</i>
            <span aria-hidden="true" class="h-0.5 w-7 bg-tac28-red @max-2xl/row:hidden"></span>
            <b class="rotate-180 font-tac28-mono text-[11.5px] font-semibold tracking-[0.2em] text-tac28-mut uppercase transition-colors [writing-mode:vertical-rl] group-hover/p:text-tac28-ink @max-2xl/row:rotate-0 @max-2xl/row:text-tac28-ink @max-2xl/row:[writing-mode:horizontal-tb]">Essay</b>
            <span class="hidden font-tac28-mono text-[11px] text-tac28-mut @max-2xl/row:ml-auto @max-2xl/row:block">p. 48</span>
          </span>
          <span class="relative z-10 flex min-w-0 flex-1 translate-y-2.5 items-end opacity-0 transition-[opacity,translate] duration-[400ms] group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-[250ms] motion-reduce:transition-none @max-2xl/row:grid @max-2xl/row:grid-rows-[0fr] @max-2xl/row:translate-y-0 @max-2xl/row:transition-[grid-template-rows,opacity] @max-2xl/row:group-has-checked/p:grid-rows-[1fr] @max-2xl/row:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[24rem] overflow-hidden @max-2xl/row:min-h-0 @max-2xl/row:min-w-0">
              <span class="block px-9 pt-6 pb-8 @max-2xl/row:px-4 @max-2xl/row:pt-0 @max-2xl/row:pb-6">
                <span class="flex items-center gap-3 font-tac28-mono text-[11px] font-semibold tracking-[0.18em] text-tac28-red uppercase @max-2xl/row:hidden">Essay<span aria-hidden="true" class="h-px flex-1 bg-tac28-rule"></span><span class="font-medium tracking-[0.08em] text-tac28-mut">p. 48</span></span>
                <b class="mt-4 block max-w-[17ch] font-tac28-serif text-[clamp(28px,3.6vw,42px)] leading-[1.02] font-semibold tracking-[-0.025em] text-balance text-tac28-ink @max-2xl/row:mt-0">In defence of the long way round</b>
                <span class="mt-4 block max-w-[42ch] font-tac28-body text-lg leading-snug text-tac28-soft italic">On slowness as a design material, and why the fastest path is rarely the best one.</span>
                <span class="mt-6 flex flex-wrap items-center gap-x-3 gap-y-1 border-t border-tac28-ink pt-3 font-tac28-mono text-[11px] tracking-[0.08em] text-tac28-mut uppercase"><span class="text-tac28-ink">Words by Amélie Fontaine</span><span aria-hidden="true">·</span>9 min read</span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p relative flex min-w-20 grow basis-0 cursor-pointer overflow-hidden border-l border-tac28-rule transition-[flex-grow,background-color] duration-[600ms] ease-[cubic-bezier(.6,0,.2,1)] first:border-l-0 hover:bg-tac28-hover has-checked:grow-[5] has-checked:bg-tac28-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-[-6px] has-focus-visible:outline-tac28-red motion-reduce:transition-none @max-2xl/row:basis-auto @max-2xl/row:flex-col @max-2xl/row:border-t @max-2xl/row:border-l-0 @max-2xl/row:first:border-t-0">
          <input type="radio" name="tac28-story" id="tac28-archive" class="sr-only">
          <span aria-hidden="true" class="pointer-events-none absolute top-2 left-3 origin-top-left scale-[.55] font-tac28-serif text-[15rem] leading-[0.8] font-black tracking-[-0.06em] text-tac28-ink/[0.09] transition-[scale,color,translate] duration-[600ms] ease-[cubic-bezier(.6,0,.2,1)] group-hover/p:text-tac28-ink/[0.16] group-has-checked/p:translate-x-3 group-has-checked/p:scale-100 group-has-checked/p:text-tac28-red/[0.14] motion-reduce:transition-none @max-2xl/row:hidden">4</span>
          <span class="absolute inset-x-0 bottom-6 flex flex-col items-center gap-3 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl/row:relative @max-2xl/row:bottom-0 @max-2xl/row:min-h-[4.5rem] @max-2xl/row:flex-row @max-2xl/row:gap-4 @max-2xl/row:px-4 @max-2xl/row:group-has-checked/p:opacity-100">
            <i class="hidden font-tac28-serif text-4xl leading-none font-black not-italic text-tac28-red @max-2xl/row:block">4</i>
            <span aria-hidden="true" class="h-0.5 w-7 bg-tac28-red @max-2xl/row:hidden"></span>
            <b class="rotate-180 font-tac28-mono text-[11.5px] font-semibold tracking-[0.2em] text-tac28-mut uppercase transition-colors [writing-mode:vertical-rl] group-hover/p:text-tac28-ink @max-2xl/row:rotate-0 @max-2xl/row:text-tac28-ink @max-2xl/row:[writing-mode:horizontal-tb]">Archive</b>
            <span class="hidden font-tac28-mono text-[11px] text-tac28-mut @max-2xl/row:ml-auto @max-2xl/row:block">p. 61</span>
          </span>
          <span class="relative z-10 flex min-w-0 flex-1 translate-y-2.5 items-end opacity-0 transition-[opacity,translate] duration-[400ms] group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-[250ms] motion-reduce:transition-none @max-2xl/row:grid @max-2xl/row:grid-rows-[0fr] @max-2xl/row:translate-y-0 @max-2xl/row:transition-[grid-template-rows,opacity] @max-2xl/row:group-has-checked/p:grid-rows-[1fr] @max-2xl/row:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[24rem] overflow-hidden @max-2xl/row:min-h-0 @max-2xl/row:min-w-0">
              <span class="block px-9 pt-6 pb-8 @max-2xl/row:px-4 @max-2xl/row:pt-0 @max-2xl/row:pb-6">
                <span class="flex items-center gap-3 font-tac28-mono text-[11px] font-semibold tracking-[0.18em] text-tac28-red uppercase @max-2xl/row:hidden">Archive<span aria-hidden="true" class="h-px flex-1 bg-tac28-rule"></span><span class="font-medium tracking-[0.08em] text-tac28-mut">p. 61</span></span>
                <b class="mt-4 block max-w-[17ch] font-tac28-serif text-[clamp(28px,3.6vw,42px)] leading-[1.02] font-semibold tracking-[-0.025em] text-balance text-tac28-ink @max-2xl/row:mt-0">The 1961 foundry letters</b>
                <span class="mt-4 block max-w-[42ch] font-tac28-body text-lg leading-snug text-tac28-soft italic">A rediscovered correspondence between two rival type foundries, annotated line by line.</span>
                <span class="mt-6 flex flex-wrap items-center gap-x-3 gap-y-1 border-t border-tac28-ink pt-3 font-tac28-mono text-[11px] tracking-[0.08em] text-tac28-mut uppercase"><span class="text-tac28-ink">Edited by the staff</span><span aria-hidden="true">·</span>15 min read</span>
              </span>
            </span>
          </span>
        </label>

      </div>
    </div>

    <p aria-hidden="true" class="max-w-full justify-self-center rounded-full border border-tac28-rule px-3.5 py-2 text-center font-tac28-mono text-[11.5px] text-balance text-tac28-mut">scale-[.55] → scale-100 · [writing-mode:vertical-rl]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac28-bg: #f5f0e6;
  --color-tac28-bg: oklch(0.956 0.014 85);
  --color-tac28-hover: #ede6d8;
  --color-tac28-hover: oklch(0.925 0.018 85);
  --color-tac28-rule: #d4cab6;
  --color-tac28-rule: oklch(0.84 0.025 85);
  --color-tac28-ink: #1f1a14;
  --color-tac28-ink: oklch(0.22 0.015 70);
  --color-tac28-soft: #463e33;
  --color-tac28-soft: oklch(0.38 0.02 70);
  --color-tac28-mut: #6b604f;
  --color-tac28-mut: oklch(0.49 0.025 75);
  --color-tac28-red: #c3301f;
  --color-tac28-red: oklch(0.53 0.19 30);
  --font-tac28-serif: 'Fraunces', Georgia, serif;
  --font-tac28-body: 'Newsreader', Georgia, serif;
  --font-tac28-mono: 'IBM Plex Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-28 {
  width: 100%;
  min-height: 100svh;
}
```
