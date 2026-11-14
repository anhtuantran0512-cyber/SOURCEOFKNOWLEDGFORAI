---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-editorial-footnote-tooltip-torn-paper-sidenote/"
title: "Tailwind Editorial Footnote Tooltip with Torn-Paper Sidenote"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A sidenote for longform reading: the source phrase grows an underline left-to-right on hover, and a deckle-edged paper card drops on a hairline tether…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Editorial Footnote Tooltip with Torn-Paper Sidenote
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-editorial-footnote-tooltip-torn-paper-sidenote/

A sidenote for longform reading: the source phrase grows an underline left-to-right on hover, and a deckle-edged paper card drops on a hairline tether holding an italic note and a monospaced citation. The port's signature move is the underline &mdash; bg-[size:0_1px] hover:bg-[size:100%_1px], a background-size transition that no text-decoration can animate.
## HTML
```html
<section class="ttp-04 relative w-full min-h-svh flex items-start justify-center bg-ttp04-stage px-10 pt-10 pb-[220px] before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:opacity-50 before:bg-[url(&quot;data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2'/><feColorMatrix values='0 0 0 0 0.16  0 0 0 0 0.12  0 0 0 0 0.09  0 0 0 0.05 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>&quot;)]">
  <article lang="en" class="relative z-1 max-w-[560px] font-ttp04-serif text-[18px] leading-[1.65] text-ttp04-ink">
    <div class="mb-5.5 flex justify-between border-b border-ttp04-rule pb-3 font-ttp04-mono text-[10px] uppercase tracking-[0.25em] text-ttp04-red">
      <span>An essay · No. XII</span>
      <span>14 May 2026</span>
    </div>

    <p class="mb-4.5 text-justify hyphens-auto">
      <span class="float-left mr-2.5 mt-1 font-ttp04-serif text-[76px] font-medium leading-[0.85] text-ttp04-red">T</span>he interface is a place where reading becomes touch. We rarely talk about the cursor as a finger, but it is — it brushes against language, and language flinches back. A tooltip is what happens when a word
      <button type="button" aria-describedby="ttp04-n1" class="group relative inline cursor-help border-0 bg-transparent p-0 pb-0.5 font-ttp04-serif text-[18px] italic font-medium text-ttp04-red bg-linear-to-r from-ttp04-red to-ttp04-red bg-no-repeat bg-[position:0_100%] bg-[size:0_1px] transition-[background-size] duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] hover:bg-[size:100%_1px] focus-visible:bg-[size:100%_1px] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp04-red motion-reduce:transition-none">decides to answer<span class="align-super text-[0.65em] font-semibold">1</span><span id="ttp04-n1" role="tooltip" class="pointer-events-none absolute top-[calc(100%+14px)] left-1/2 z-20 block w-[300px] max-w-[calc(100vw-48px)] -translate-x-1/2 -translate-y-2 rotate-[-0.4deg] bg-ttp04-card px-5 pt-4 pb-4.5 text-left font-ttp04-serif text-sm not-italic leading-[1.55] text-ttp04-ink opacity-0 invisible shadow-[0_1px_0_rgba(0,0,0,0.05),0_10px_26px_-6px_rgba(75,40,20,0.25),0_2px_5px_-1px_rgba(75,40,20,0.15)] transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:visible group-focus-visible:opacity-100 group-focus-visible:translate-y-0 before:content-[''] before:absolute before:bottom-full before:left-1/2 before:h-3.5 before:w-px before:-translate-x-1/2 before:bg-ttp04-red before:opacity-40 [clip-path:polygon(0%_4%,2%_1%,6%_3%,12%_0%,22%_2%,35%_0%,48%_2%,62%_0%,78%_2%,90%_0%,96%_3%,100%_1%,100%_96%,98%_99%,90%_97%,78%_100%,60%_98%,42%_100%,24%_98%,10%_100%,4%_97%,0%_99%)]">
        <span class="mr-1.5 inline-block align-[-2px] font-ttp04-serif text-xl font-medium italic leading-none text-ttp04-red">1.</span>
        <span class="italic">The phrase belongs to Robin Sloan, who described hover states as "the part of the web that whispers back." Most of us, of course, have settled for the part that mumbles.</span>
        <span class="mt-2.5 block border-t border-dotted border-ttp04-rule pt-2 font-ttp04-mono text-[9.5px] uppercase not-italic tracking-[0.1em] text-ttp04-red">— Sloan, 2019, p. 84</span>
      </span></button>. Once it could only do so in gray boxes, a meek municipal voice; now it can do almost anything, and so the question is no longer whether it speaks but what register it speaks in.
    </p>

    <p class="mb-4.5 text-justify hyphens-auto">
      Consider the
      <button type="button" aria-describedby="ttp04-n2" class="group relative inline cursor-help border-0 bg-transparent p-0 pb-0.5 font-ttp04-serif text-[18px] italic font-medium text-ttp04-red bg-linear-to-r from-ttp04-red to-ttp04-red bg-no-repeat bg-[position:0_100%] bg-[size:0_1px] transition-[background-size] duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] hover:bg-[size:100%_1px] focus-visible:bg-[size:100%_1px] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp04-red motion-reduce:transition-none">marginalia of medieval readers<span class="align-super text-[0.65em] font-semibold">2</span><span id="ttp04-n2" role="tooltip" class="pointer-events-none absolute top-[calc(100%+14px)] left-1/2 z-20 block w-[300px] max-w-[calc(100vw-48px)] -translate-x-1/2 -translate-y-2 rotate-[-0.4deg] bg-ttp04-card px-5 pt-4 pb-4.5 text-left font-ttp04-serif text-sm not-italic leading-[1.55] text-ttp04-ink opacity-0 invisible shadow-[0_1px_0_rgba(0,0,0,0.05),0_10px_26px_-6px_rgba(75,40,20,0.25),0_2px_5px_-1px_rgba(75,40,20,0.15)] transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:visible group-focus-visible:opacity-100 group-focus-visible:translate-y-0 before:content-[''] before:absolute before:bottom-full before:left-1/2 before:h-3.5 before:w-px before:-translate-x-1/2 before:bg-ttp04-red before:opacity-40 [clip-path:polygon(0%_4%,2%_1%,6%_3%,12%_0%,22%_2%,35%_0%,48%_2%,62%_0%,78%_2%,90%_0%,96%_3%,100%_1%,100%_96%,98%_99%,90%_97%,78%_100%,60%_98%,42%_100%,24%_98%,10%_100%,4%_97%,0%_99%)]">
        <span class="mr-1.5 inline-block align-[-2px] font-ttp04-serif text-xl font-medium italic leading-none text-ttp04-red">2.</span>
        <span class="italic">In the manuscript tradition, glosses were often longer than the texts they served. The Vulgate, the Talmud, the Glossa Ordinaria — these are pages where the footnote ate the page and called it home.</span>
        <span class="mt-2.5 block border-t border-dotted border-ttp04-rule pt-2 font-ttp04-mono text-[9.5px] uppercase not-italic tracking-[0.1em] text-ttp04-red">— de Hamel, 2016, ch. 4</span>
      </span></button>, who wrote louder than the books they read. Their pages were tooltips made of ink, hovering forever — annotations that became canon because the original was lonely without them.
    </p>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp04-stage: #f3eee3;
  --color-ttp04-stage: oklch(0.94 0.015 85);
  --color-ttp04-card: #faf5ea;
  --color-ttp04-card: oklch(0.97 0.014 85);
  --color-ttp04-ink: #2a1f17;
  --color-ttp04-ink: oklch(0.26 0.03 55);
  --color-ttp04-red: #8a2c1c;
  --color-ttp04-red: oklch(0.42 0.13 35);
  --color-ttp04-rule: #c39b8e;
  --color-ttp04-rule: oklch(0.72 0.06 35);
  --font-ttp04-serif: Georgia, 'Times New Roman', serif;
  --font-ttp04-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.ttp-04 {
  width: 100%;
  min-height: 100svh;
}
```
