---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-glossary-word-tooltip-dictionary-definition-card/"
title: "Tailwind Glossary Word Tooltip with Dictionary Definition Card"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "Dotted-underlined terms in a paragraph that open a full dictionary card &mdash; part of speech, headword, IPA, etymology, italic definition, a usage…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glossary Word Tooltip with Dictionary Definition Card
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-glossary-word-tooltip-dictionary-definition-card/

Dotted-underlined terms in a paragraph that open a full dictionary card &mdash; part of speech, headword, IPA, etymology, italic definition, a usage quotation and synonym pills. The port is a relocation: every declaration has a utility, so the stylesheet shrinks to tokens and the card's five stacked sections become visible as five class lists.
## HTML
```html
<section class="ttp-07 w-full min-h-svh bg-ttp07-stage px-7 pt-[300px] pb-10 font-ttp07-serif">
  <div class="mx-auto max-w-[560px]">
    <p class="m-0 text-[18px] leading-[1.85] text-ttp07-ink">
      There is a word for the smell of rain on dry earth —
      <button type="button" aria-describedby="ttp07-w1" class="group relative inline-block cursor-help border-0 bg-transparent p-0 align-baseline font-ttp07-serif text-[18px] text-ttp07-term transition-colors duration-150 hover:text-ttp07-termhover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp07-term">
        <dfn class="not-italic [border-bottom:1.5px_dotted_currentColor]">petrichor</dfn>
        <span id="ttp07-w1" role="tooltip" class="pointer-events-none invisible absolute bottom-[calc(100%+10px)] left-1/2 z-30 block w-80 max-w-[calc(100vw-48px)] -translate-x-1/2 translate-y-1 overflow-hidden whitespace-normal rounded-[10px] border border-ttp07-edge bg-white text-left opacity-0 shadow-[0_8px_36px_rgba(60,40,10,0.13),0_2px_8px_rgba(60,40,10,0.06)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-visible:visible group-focus-visible:translate-y-0 group-focus-visible:opacity-100">
          <span class="block border-b border-ttp07-edge bg-ttp07-well px-4.5 pt-4 pb-3">
            <span class="mb-1.25 block font-ttp07-sans text-[10px] font-medium uppercase tracking-[0.1em] text-ttp07-meta">noun · meteorology</span>
            <span class="mb-1 block text-2xl font-medium leading-none text-ttp07-head">petrichor</span>
            <span class="block text-xs italic text-ttp07-meta">/ˈpɛtrɪkɔːr/</span>
          </span>
          <span class="block border-b border-ttp07-edge px-4.5 py-2.75 font-ttp07-sans text-[11.5px] leading-[1.5] text-ttp07-muted"><strong class="font-medium text-ttp07-strong">Origin:</strong> Greek <em>petra</em> (stone) + <em>ichor</em> (the ethereal fluid said to flow through the veins of gods). Coined 1964 by Bear &amp; Thomas.</span>
          <span class="block border-b border-ttp07-edge px-4.5 py-3.25 text-[13px] italic leading-[1.65] text-ttp07-ink">The pleasant, earthy scent that arises when rain falls on dry soil, produced by geosmin released from actinobacteria.</span>
          <span class="block px-4.5 pt-2.75 pb-3.25 font-ttp07-sans text-xs text-ttp07-muted">
            <span class="mb-1.25 block text-[9.5px] uppercase tracking-[0.1em] text-ttp07-meta">In use</span>
            <span class="block font-ttp07-serif text-[13px] italic leading-[1.5] text-ttp07-strong">"The petrichor that rose from the cracked earth was the first sign that the long drought had broken."</span>
          </span>
          <span class="flex flex-wrap gap-1.25 border-t border-ttp07-edge px-4.5 pt-2.25 pb-3.25">
            <span class="rounded-full border border-ttp07-edge bg-ttp07-pill px-2 py-0.75 font-ttp07-sans text-[10px] text-ttp07-strong">geosmin</span>
            <span class="rounded-full border border-ttp07-edge bg-ttp07-pill px-2 py-0.75 font-ttp07-sans text-[10px] text-ttp07-strong">earthy scent</span>
            <span class="rounded-full border border-ttp07-edge bg-ttp07-pill px-2 py-0.75 font-ttp07-sans text-[10px] text-ttp07-strong">rain smell</span>
          </span>
        </span>
      </button>
      — a sensation so specific it once had no name. Equally unnamed was
      <button type="button" aria-describedby="ttp07-w2" class="group relative inline-block cursor-help border-0 bg-transparent p-0 align-baseline font-ttp07-serif text-[18px] text-ttp07-term transition-colors duration-150 hover:text-ttp07-termhover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp07-term">
        <dfn class="not-italic [border-bottom:1.5px_dotted_currentColor]">sonder</dfn>
        <span id="ttp07-w2" role="tooltip" class="pointer-events-none invisible absolute bottom-[calc(100%+10px)] left-1/2 z-30 block w-80 max-w-[calc(100vw-48px)] -translate-x-1/2 translate-y-1 overflow-hidden whitespace-normal rounded-[10px] border border-ttp07-edge bg-white text-left opacity-0 shadow-[0_8px_36px_rgba(60,40,10,0.13),0_2px_8px_rgba(60,40,10,0.06)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-visible:visible group-focus-visible:translate-y-0 group-focus-visible:opacity-100">
          <span class="block border-b border-ttp07-edge bg-ttp07-well px-4.5 pt-4 pb-3">
            <span class="mb-1.25 block font-ttp07-sans text-[10px] font-medium uppercase tracking-[0.1em] text-ttp07-meta">noun · neologism</span>
            <span class="mb-1 block text-2xl font-medium leading-none text-ttp07-head">sonder</span>
            <span class="block text-xs italic text-ttp07-meta">/ˈsɒndər/</span>
          </span>
          <span class="block border-b border-ttp07-edge px-4.5 py-2.75 font-ttp07-sans text-[11.5px] leading-[1.5] text-ttp07-muted"><strong class="font-medium text-ttp07-strong">Origin:</strong> Coined by John Koenig in <em>The Dictionary of Obscure Sorrows</em> (2012). Likely influenced by French <em>sonder</em> (to probe, to fathom).</span>
          <span class="block border-b border-ttp07-edge px-4.5 py-3.25 text-[13px] italic leading-[1.65] text-ttp07-ink">The sudden realization that every passerby is living a life as vivid and complex as one's own — filled with ambitions, fears, and an intricate private world.</span>
          <span class="block px-4.5 pt-2.75 pb-3.25 font-ttp07-sans text-xs text-ttp07-muted">
            <span class="mb-1.25 block text-[9.5px] uppercase tracking-[0.1em] text-ttp07-meta">In use</span>
            <span class="block font-ttp07-serif text-[13px] italic leading-[1.5] text-ttp07-strong">"Staring out the train window, she was struck by sonder — each lit window a whole life she'd never know."</span>
          </span>
          <span class="flex flex-wrap gap-1.25 border-t border-ttp07-edge px-4.5 pt-2.25 pb-3.25">
            <span class="rounded-full border border-ttp07-edge bg-ttp07-pill px-2 py-0.75 font-ttp07-sans text-[10px] text-ttp07-strong">empathy</span>
            <span class="rounded-full border border-ttp07-edge bg-ttp07-pill px-2 py-0.75 font-ttp07-sans text-[10px] text-ttp07-strong">weltanschauung</span>
          </span>
        </span>
      </button>,
      the act of registering that strangers have entire interior worlds. We live in
      <button type="button" aria-describedby="ttp07-w3" class="group relative inline-block cursor-help border-0 bg-transparent p-0 align-baseline font-ttp07-serif text-[18px] text-ttp07-term transition-colors duration-150 hover:text-ttp07-termhover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp07-term">
        <dfn class="not-italic [border-bottom:1.5px_dotted_currentColor]">liminal</dfn>
        <span id="ttp07-w3" role="tooltip" class="pointer-events-none invisible absolute bottom-[calc(100%+10px)] left-1/2 z-30 block w-80 max-w-[calc(100vw-48px)] -translate-x-1/2 translate-y-1 overflow-hidden whitespace-normal rounded-[10px] border border-ttp07-edge bg-white text-left opacity-0 shadow-[0_8px_36px_rgba(60,40,10,0.13),0_2px_8px_rgba(60,40,10,0.06)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-visible:visible group-focus-visible:translate-y-0 group-focus-visible:opacity-100">
          <span class="block border-b border-ttp07-edge bg-ttp07-well px-4.5 pt-4 pb-3">
            <span class="mb-1.25 block font-ttp07-sans text-[10px] font-medium uppercase tracking-[0.1em] text-ttp07-meta">adjective · anthropology</span>
            <span class="mb-1 block text-2xl font-medium leading-none text-ttp07-head">liminal</span>
            <span class="block text-xs italic text-ttp07-meta">/ˈlɪmɪnəl/</span>
          </span>
          <span class="block border-b border-ttp07-edge px-4.5 py-2.75 font-ttp07-sans text-[11.5px] leading-[1.5] text-ttp07-muted"><strong class="font-medium text-ttp07-strong">Origin:</strong> Latin <em>limen</em> (threshold). Popularised by anthropologist Arnold van Gennep (1909) to describe transitional ritual phases.</span>
          <span class="block border-b border-ttp07-edge px-4.5 py-3.25 text-[13px] italic leading-[1.65] text-ttp07-ink">Occupying a position at, or on both sides of, a threshold or boundary; relating to a transitional or initial stage of a process.</span>
          <span class="block px-4.5 pt-2.75 pb-3.25 font-ttp07-sans text-xs text-ttp07-muted">
            <span class="mb-1.25 block text-[9.5px] uppercase tracking-[0.1em] text-ttp07-meta">In use</span>
            <span class="block font-ttp07-serif text-[13px] italic leading-[1.5] text-ttp07-strong">"The airport is the most liminal of spaces — everyone passing through on the way to somewhere else."</span>
          </span>
          <span class="flex flex-wrap gap-1.25 border-t border-ttp07-edge px-4.5 pt-2.25 pb-3.25">
            <span class="rounded-full border border-ttp07-edge bg-ttp07-pill px-2 py-0.75 font-ttp07-sans text-[10px] text-ttp07-strong">transitional</span>
            <span class="rounded-full border border-ttp07-edge bg-ttp07-pill px-2 py-0.75 font-ttp07-sans text-[10px] text-ttp07-strong">threshold</span>
            <span class="rounded-full border border-ttp07-edge bg-ttp07-pill px-2 py-0.75 font-ttp07-sans text-[10px] text-ttp07-strong">interstitial</span>
          </span>
        </span>
      </button>
      spaces more than we realise.
    </p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp07-stage: #fdf9f3;
  --color-ttp07-stage: oklch(0.98 0.012 85);
  --color-ttp07-well: #faf6ef;
  --color-ttp07-well: oklch(0.97 0.012 85);
  --color-ttp07-pill: #f3ece0;
  --color-ttp07-pill: oklch(0.94 0.018 85);
  --color-ttp07-edge: #e3d8c4;
  --color-ttp07-edge: oklch(0.88 0.03 85);
  --color-ttp07-rule: #a08050;
  --color-ttp07-ink: #2c2416;
  --color-ttp07-ink: oklch(0.27 0.025 75);
  --color-ttp07-head: #1a1008;
  --color-ttp07-head: oklch(0.2 0.02 60);
  --color-ttp07-strong: #5a4020;
  --color-ttp07-strong: oklch(0.4 0.05 65);
  --color-ttp07-muted: #6d5733;
  --color-ttp07-muted: oklch(0.47 0.05 75);
  --color-ttp07-meta: #7a6440;
  --color-ttp07-meta: oklch(0.52 0.05 78);
  --color-ttp07-term: #6a4820;
  --color-ttp07-term: oklch(0.42 0.07 62);
  --color-ttp07-termhover: #3a2010;
  --color-ttp07-termhover: oklch(0.27 0.05 45);
  --font-ttp07-serif: Georgia, 'Times New Roman', serif;
  --font-ttp07-sans: 'Inter', system-ui, sans-serif;
}

.ttp-07 {
  width: 100%;
  min-height: 100svh;
}
```
