---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-editorial-tabloid-bento-layout/"
title: "Tailwind Editorial Tabloid Bento Layout"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "A newsprint bento with a real masthead, a display-poster headline, an in-this-issue index with dashed leaders, a pull-quote ribbon and three section tiles…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Editorial Tabloid Bento Layout
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-editorial-tabloid-bento-layout/

A newsprint bento with a real masthead, a display-poster headline, an in-this-issue index with dashed leaders, a pull-quote ribbon and three section tiles &mdash; all inside one hairline-ruled 12-column grid. The port keeps every print convention and moves all twelve placement rules onto the tiles: col-span-full, col-span-8, col-span-4.
## HTML
```html
<section class="tcg-08 w-full min-h-svh flex items-center justify-center bg-tcg08-paper bg-[repeating-linear-gradient(0deg,oklch(0.2_0.03_50/0.025)_0_1px,transparent_1px_3px)] font-tcg08-sans text-tcg08-ink p-[clamp(20px,3vw,48px)]" aria-label="Editorial tabloid bento layout demo">
  <div class="w-full max-w-[1100px] grid grid-cols-12 gap-0 rounded overflow-hidden border-2 border-tcg08-ink bg-tcg08-paper">

    <div class="col-span-full flex flex-wrap items-center justify-between gap-3.5 border-b-2 border-tcg08-ink bg-tcg08-ink text-tcg08-paper px-[clamp(18px,2.2vw,28px)] py-[clamp(12px,1.4vw,18px)] max-[720px]:flex-col max-[720px]:items-start max-[720px]:gap-2">
      <span class="font-tcg08-serif italic font-black text-[clamp(1.1rem,1.8vw,1.6rem)] tracking-[0.01em] leading-none">THE BRUTALIST</span>
      <span class="flex flex-wrap items-center gap-[clamp(6px,1vw,12px)] text-[clamp(.62rem,.85vw,.74rem)] font-bold tracking-[0.18em] uppercase tabular-nums">
        <span>VOL. 07</span><span class="text-[.6em] opacity-55">&#9679;</span>
        <span>SUMMER 2026</span><span class="text-[.6em] opacity-55">&#9679;</span>
        <span>ISSUE 04</span><span class="text-[.6em] opacity-55">&#9679;</span>
        <span>$12</span>
      </span>
    </div>

    <div class="col-span-8 max-[900px]:col-span-7 max-[720px]:col-span-full flex flex-col justify-center gap-3.5 border-r border-b border-tcg08-ink max-[720px]:border-r-0 px-[clamp(28px,3vw,40px)] py-[clamp(28px,3.4vw,48px)]">
      <span class="text-[clamp(.66rem,.95vw,.78rem)] font-bold tracking-[0.22em] uppercase text-tcg08-accent">The cover story</span>
      <h2 class="font-tcg08-serif font-black text-[clamp(2.4rem,6.6vw,6rem)] leading-[0.88] tracking-[-0.035em]">Brutalist<br><span class="italic text-tcg08-accent">Web</span></h2>
      <span class="font-tcg08-serif italic max-w-[38ch] text-[clamp(.82rem,1.05vw,.96rem)] leading-[1.5] text-tcg08-ink70">Field notes from designers building louder, slower, and on purpose.</span>
    </div>

    <div class="col-span-4 max-[900px]:col-span-5 max-[720px]:col-span-full max-[720px]:border-t flex flex-col gap-3 border-b border-tcg08-ink bg-tcg08-tint px-[clamp(22px,2.4vw,28px)] py-[clamp(22px,2.4vw,32px)]">
      <div class="flex items-baseline justify-between pb-2.5 border-b-2 border-tcg08-ink">
        <span class="font-tcg08-serif italic font-black text-[clamp(.95rem,1.3vw,1.15rem)]">In this issue</span>
        <span class="text-[.62rem] font-bold tracking-[0.18em] uppercase opacity-65">04 / pieces</span>
      </div>
      <ol class="flex flex-col list-none">
        <li class="flex items-baseline gap-2 py-2.5 border-b border-dashed border-tcg08-dash last:border-b-0 last:pb-0">
          <span class="font-tcg08-serif font-black text-[.88rem] min-w-[1.6em] text-tcg08-accent">01</span>
          <span class="flex-1 text-[clamp(.74rem,.92vw,.86rem)] font-medium leading-[1.3]">The Brutalist Web</span>
          <span class="text-[.72rem] font-bold tabular-nums tracking-[0.04em] text-tcg08-ink60">p.12</span>
        </li>
        <li class="flex items-baseline gap-2 py-2.5 border-b border-dashed border-tcg08-dash last:border-b-0 last:pb-0">
          <span class="font-tcg08-serif font-black text-[.88rem] min-w-[1.6em] text-tcg08-accent">02</span>
          <span class="flex-1 text-[clamp(.74rem,.92vw,.86rem)] font-medium leading-[1.3]">Whitespace as protest</span>
          <span class="text-[.72rem] font-bold tabular-nums tracking-[0.04em] text-tcg08-ink60">p.24</span>
        </li>
        <li class="flex items-baseline gap-2 py-2.5 border-b border-dashed border-tcg08-dash last:border-b-0 last:pb-0">
          <span class="font-tcg08-serif font-black text-[.88rem] min-w-[1.6em] text-tcg08-accent">03</span>
          <span class="flex-1 text-[clamp(.74rem,.92vw,.86rem)] font-medium leading-[1.3]">Field notes from the type foundry</span>
          <span class="text-[.72rem] font-bold tabular-nums tracking-[0.04em] text-tcg08-ink60">p.38</span>
        </li>
        <li class="flex items-baseline gap-2 py-2.5 border-b border-dashed border-tcg08-dash last:border-b-0 last:pb-0">
          <span class="font-tcg08-serif font-black text-[.88rem] min-w-[1.6em] text-tcg08-accent">04</span>
          <span class="flex-1 text-[clamp(.74rem,.92vw,.86rem)] font-medium leading-[1.3]">Interview with Massimo Vignelli</span>
          <span class="text-[.72rem] font-bold tabular-nums tracking-[0.04em] text-tcg08-ink60">p.52</span>
        </li>
      </ol>
    </div>

    <figure class="col-span-full relative flex flex-col gap-2 border-b border-tcg08-ink bg-tcg08-paper px-[clamp(28px,3.4vw,56px)] py-[clamp(24px,3vw,40px)]">
      <span class="absolute -top-2.5 left-[clamp(12px,1.6vw,24px)] pointer-events-none font-tcg08-serif font-black leading-none opacity-15 text-tcg08-accent text-[clamp(5rem,12vw,10rem)]" aria-hidden="true">&ldquo;</span>
      <blockquote class="relative z-1 max-w-[32ch] font-tcg08-serif font-semibold text-[clamp(1.15rem,2.2vw,1.7rem)] leading-[1.32] tracking-[-0.005em]">Whitespace is a design choice. <em class="italic text-tcg08-accent">Not a bug.</em></blockquote>
      <figcaption class="text-[.7rem] font-bold tracking-[0.18em] uppercase text-tcg08-ink60">&mdash; Editorial, p. 24</figcaption>
    </figure>

    <div class="col-span-full grid grid-cols-3 max-[720px]:grid-cols-2 max-[480px]:grid-cols-1 gap-0">
      <article class="flex flex-col gap-2.5 border-r border-tcg08-ink max-[720px]:border-b max-[480px]:border-r-0 p-[clamp(20px,2.4vw,28px)] min-h-[clamp(180px,18vw,220px)]">
        <span class="self-start px-2.5 pt-1.25 pb-1 rounded-sm bg-tcg08-ink text-tcg08-paper text-[.62rem] font-bold tracking-[0.2em] uppercase">Editorial</span>
        <h3 class="font-tcg08-serif font-black text-[clamp(1.05rem,1.6vw,1.35rem)] leading-[1.1] tracking-[-0.015em]">Long Reads</h3>
        <p class="max-w-[32ch] text-[clamp(.76rem,.95vw,.88rem)] leading-[1.45] text-tcg08-ink70 text-pretty">Six essays on quiet design, by writers who would rather you stayed.</p>
        <span class="mt-auto pt-2 text-[.72rem] font-bold tracking-[0.16em] uppercase tabular-nums text-tcg08-ink50">p.12</span>
      </article>
      <article class="flex flex-col gap-2.5 border-r border-tcg08-ink max-[720px]:border-r-0 max-[720px]:border-b max-[480px]:border-r-0 p-[clamp(20px,2.4vw,28px)] min-h-[clamp(180px,18vw,220px)]">
        <span class="self-start px-2.5 pt-1.25 pb-1 rounded-sm bg-tcg08-ink text-tcg08-paper text-[.62rem] font-bold tracking-[0.2em] uppercase">Interview</span>
        <h3 class="font-tcg08-serif font-black text-[clamp(1.05rem,1.6vw,1.35rem)] leading-[1.1] tracking-[-0.015em]">Massimo Vignelli</h3>
        <p class="max-w-[32ch] text-[clamp(.76rem,.95vw,.88rem)] leading-[1.45] text-tcg08-ink70 text-pretty">If you can design one thing, you can design everything. A conversation.</p>
        <span class="mt-auto pt-2 text-[.72rem] font-bold tracking-[0.16em] uppercase tabular-nums text-tcg08-ink50">p.24</span>
      </article>
      <article class="flex flex-col gap-2.5 bg-tcg08-ink text-tcg08-paper max-[720px]:col-span-full p-[clamp(20px,2.4vw,28px)] min-h-[clamp(180px,18vw,220px)]">
        <span class="self-start px-2.5 pt-1.25 pb-1 rounded-sm bg-tcg08-accent text-tcg08-paper text-[.62rem] font-bold tracking-[0.2em] uppercase">Read Next</span>
        <h3 class="font-tcg08-serif font-black text-[clamp(1.05rem,1.6vw,1.35rem)] leading-[1.1] tracking-[-0.015em]">The Slow Web Manifesto</h3>
        <p class="max-w-[32ch] text-[clamp(.76rem,.95vw,.88rem)] leading-[1.45] text-tcg08-paper78 text-pretty">Why the best sites in 2026 load in 3 seconds &mdash; on purpose.</p>
        <span class="mt-auto pt-2 text-[.72rem] font-bold tracking-[0.16em] uppercase tabular-nums text-tcg08-accent">p.38 &rarr;</span>
      </article>
    </div>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg08-paper: #f1ece0;
  --color-tcg08-paper: oklch(0.94 0.02 85);
  --color-tcg08-paper78: #d5cfc2;
  --color-tcg08-paper78: oklch(0.85 0.02 85);
  --color-tcg08-ink: #1a1410;
  --color-tcg08-ink: oklch(0.2 0.02 50);
  --color-tcg08-ink70: #5a5148;
  --color-tcg08-ink70: oklch(0.44 0.02 55);
  --color-tcg08-ink60: #6b6158;
  --color-tcg08-ink60: oklch(0.5 0.02 55);
  --color-tcg08-ink50: #7b7168;
  --color-tcg08-ink50: oklch(0.56 0.02 55);
  --color-tcg08-tint: #ebe5d8;
  --color-tcg08-tint: oklch(0.92 0.02 85);
  --color-tcg08-dash: #b8b0a3;
  --color-tcg08-dash: oklch(0.76 0.02 80);
  --color-tcg08-accent: #c93a4a;
  --color-tcg08-accent: oklch(0.55 0.19 20);
  --font-tcg08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcg08-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
}
/* Root rule: the full-bleed contract. */

.tcg-08 {
  width: 100%;
  min-height: 100svh;
}

.tcg-08 ::selection {
  background: #1a1410;
  color: #f1ece0;
}
```
