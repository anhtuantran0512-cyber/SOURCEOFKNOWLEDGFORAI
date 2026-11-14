---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-hover-to-reveal-hidden-spoiler-text/"
title: "Tailwind Hover to Reveal Hidden Spoiler Text"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A pub-quiz card with answers blurred out: hover a row to peek, the Reveal pill pins it (keyboard and touch get equal rights), and a Reveal all switch unblurs…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hover to Reveal Hidden Spoiler Text
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-hover-to-reveal-hidden-spoiler-text/

A pub-quiz card with answers blurred out: hover a row to peek, the Reveal pill pins it (keyboard and touch get equal rights), and a Reveal all switch unblurs every answer in a staggered cascade. All state is :has(:checked) — written as group-has-[[data-pin]:checked]/row: and group-has-[[data-all]:checked]/card:. Zero JS.
## HTML
```html
<section class="tth-12 @container w-full min-h-svh grid place-items-center bg-tth12-bg px-5 py-14 font-tth12-sans text-tth12-ink" aria-label="Spoiler reveal demo">
  <article class="group/card w-full max-w-[42.5rem] rounded-[20px] border border-tth12-line bg-white p-[clamp(20px,4cqi,34px)] shadow-[0_20px_60px_oklch(0.35_0.05_295/0.1)]">
    <header class="flex items-start justify-between gap-4 border-b-[1.5px] border-tth12-ink pb-4 @max-[29rem]:flex-col">
      <div>
        <p class="text-[11.5px] font-bold uppercase tracking-[0.2em] text-tth12-acc">The Thursday Quiz &mdash; round 4</p>
        <h2 class="mt-1 text-[clamp(20px,3.4cqi,27px)] font-extrabold tracking-[-0.02em]">Cinema, unspoiled</h2>
      </div>
      <label class="group/all flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full border-[1.5px] border-tth12-line pl-2 pr-4 text-[13px] font-bold transition-colors duration-250 hover:border-tth12-acc has-checked:border-tth12-acc has-checked:bg-tth12-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-[3px] has-focus-visible:outline-tth12-acc"><input data-all type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative h-5 w-9 rounded-full bg-tth12-line transition-colors duration-250 after:absolute after:left-0.5 after:top-0.5 after:size-4 after:rounded-full after:bg-white after:shadow after:transition-transform after:duration-250 after:content-[''] peer-checked:bg-white/30 peer-checked:after:translate-x-4"></span>Reveal all</label>
    </header>
    <ol class="flex flex-col">
      <li style="--i:0" class="group/row border-b border-tth12-line py-[clamp(14px,2.6cqi,20px)]">
        <p class="text-[15.5px] font-bold leading-normal"><span class="mr-2 font-tth12-mono text-[11px] font-semibold tracking-[0.06em] text-tth12-acc">Q1</span>Which 2024 film's twist hinges on the narrator being the composer?</p>
        <div class="mt-2.5 flex items-center gap-3.5 @max-[29rem]:flex-col @max-[29rem]:items-start">
          <span class="flex-1 text-[14.5px] leading-[1.6] text-tth12-mut blur-[9px] saturate-70 select-none transition-[filter] duration-400 group-hover/row:blur-none group-hover/row:saturate-100 group-hover/row:select-text group-has-[[data-pin]:checked]/row:blur-none group-has-[[data-pin]:checked]/row:select-text group-has-[[data-all]:checked]/card:blur-none group-has-[[data-all]:checked]/card:select-text group-has-[[data-all]:checked]/card:delay-[calc(var(--i)*70ms)] motion-reduce:transition-none"><em>The Long Static</em> &mdash; the score was the confession all along.</span>
          <label class="grid min-h-11 min-w-[74px] flex-none cursor-pointer place-items-center"><input data-pin type="checkbox" class="peer sr-only" aria-label="Reveal answer 1"><i aria-hidden="true" class="rounded-full border-[1.5px] border-tth12-acc/45 px-3.5 py-2 text-[11px] font-extrabold uppercase not-italic tracking-[0.12em] text-tth12-acc transition-colors duration-250 before:content-['Reveal'] hover:border-tth12-acc peer-checked:border-tth12-acc peer-checked:bg-tth12-acc peer-checked:text-white peer-checked:before:content-['Hide'] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-[3px] peer-focus-visible:outline-tth12-acc"></i></label>
        </div>
      </li>
      <li style="--i:1" class="group/row border-b border-tth12-line py-[clamp(14px,2.6cqi,20px)]">
        <p class="text-[15.5px] font-bold leading-normal"><span class="mr-2 font-tth12-mono text-[11px] font-semibold tracking-[0.06em] text-tth12-acc">Q2</span>Who directed it &mdash; and what was their day job until 2019?</p>
        <div class="mt-2.5 flex items-center gap-3.5 @max-[29rem]:flex-col @max-[29rem]:items-start">
          <span class="flex-1 text-[14.5px] leading-[1.6] text-tth12-mut blur-[9px] saturate-70 select-none transition-[filter] duration-400 group-hover/row:blur-none group-hover/row:saturate-100 group-hover/row:select-text group-has-[[data-pin]:checked]/row:blur-none group-has-[[data-pin]:checked]/row:select-text group-has-[[data-all]:checked]/card:blur-none group-has-[[data-all]:checked]/card:select-text group-has-[[data-all]:checked]/card:delay-[calc(var(--i)*70ms)] motion-reduce:transition-none">Mara Chen &mdash; she was a foley artist, which explains everything.</span>
          <label class="grid min-h-11 min-w-[74px] flex-none cursor-pointer place-items-center"><input data-pin type="checkbox" class="peer sr-only" aria-label="Reveal answer 2"><i aria-hidden="true" class="rounded-full border-[1.5px] border-tth12-acc/45 px-3.5 py-2 text-[11px] font-extrabold uppercase not-italic tracking-[0.12em] text-tth12-acc transition-colors duration-250 before:content-['Reveal'] hover:border-tth12-acc peer-checked:border-tth12-acc peer-checked:bg-tth12-acc peer-checked:text-white peer-checked:before:content-['Hide'] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-[3px] peer-focus-visible:outline-tth12-acc"></i></label>
        </div>
      </li>
      <li style="--i:2" class="group/row border-b border-tth12-line py-[clamp(14px,2.6cqi,20px)]">
        <p class="text-[15.5px] font-bold leading-normal"><span class="mr-2 font-tth12-mono text-[11px] font-semibold tracking-[0.06em] text-tth12-acc">Q3</span>The final shot mirrors which 1962 classic, frame for frame?</p>
        <div class="mt-2.5 flex items-center gap-3.5 @max-[29rem]:flex-col @max-[29rem]:items-start">
          <span class="flex-1 text-[14.5px] leading-[1.6] text-tth12-mut blur-[9px] saturate-70 select-none transition-[filter] duration-400 group-hover/row:blur-none group-hover/row:saturate-100 group-hover/row:select-text group-has-[[data-pin]:checked]/row:blur-none group-has-[[data-pin]:checked]/row:select-text group-has-[[data-all]:checked]/card:blur-none group-has-[[data-all]:checked]/card:select-text group-has-[[data-all]:checked]/card:delay-[calc(var(--i)*70ms)] motion-reduce:transition-none"><em>La Jet&eacute;e</em> &mdash; a still photograph, finally allowed to move.</span>
          <label class="grid min-h-11 min-w-[74px] flex-none cursor-pointer place-items-center"><input data-pin type="checkbox" class="peer sr-only" aria-label="Reveal answer 3"><i aria-hidden="true" class="rounded-full border-[1.5px] border-tth12-acc/45 px-3.5 py-2 text-[11px] font-extrabold uppercase not-italic tracking-[0.12em] text-tth12-acc transition-colors duration-250 before:content-['Reveal'] hover:border-tth12-acc peer-checked:border-tth12-acc peer-checked:bg-tth12-acc peer-checked:text-white peer-checked:before:content-['Hide'] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-[3px] peer-focus-visible:outline-tth12-acc"></i></label>
        </div>
      </li>
    </ol>
    <p class="mt-4 text-[12.5px] leading-[1.7] text-tth12-mut">Hover an answer to peek; the <b>Reveal</b> pill pins it (touch &amp; keyboard get equal rights). <code class="rounded bg-tth12-chip px-1.5 py-px font-tth12-mono text-[0.9em]">group-has-[[data-pin]:checked]</code> does the state &mdash; no JS.</p>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth12-bg: #f6f4ee;
  --color-tth12-bg: oklch(0.965 0.008 90);
  --color-tth12-chip: #efecf4;
  --color-tth12-chip: oklch(0.94 0.01 290);
  --color-tth12-ink: #2a2433;
  --color-tth12-ink: oklch(0.27 0.02 290);
  --color-tth12-mut: #5e5867;
  --color-tth12-mut: oklch(0.47 0.02 290);
  --color-tth12-acc: #7543d6;
  --color-tth12-acc: oklch(0.52 0.2 295);
  --color-tth12-line: #e3e0ea;
  --color-tth12-line: oklch(0.9 0.01 290);
  --font-tth12-sans: 'Figtree', system-ui, sans-serif;
  --font-tth12-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-12 {
  width: 100%;
  min-height: 100svh;
}
```
