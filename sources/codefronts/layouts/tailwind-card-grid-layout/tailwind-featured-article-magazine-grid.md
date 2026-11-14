---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-featured-article-magazine-grid/"
title: "Tailwind Featured Article Magazine Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "One hero story on the left, four stacked supporting cards on the right, and colour-coded category pills so the wall can be scanned by section &mdash; the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Featured Article Magazine Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-featured-article-magazine-grid/

One hero story on the left, four stacked supporting cards on the right, and colour-coded category pills so the wall can be scanned by section &mdash; the hierarchy every news homepage converges on. Five per-category colours live in @theme, which is exactly the case for a token: one value, used by many elements, meaningful across the design.
## HTML
```html
<section class="tcg-14 w-full min-h-svh bg-tcg14-bg font-tcg14-sans text-tcg14-ink px-[clamp(20px,3vw,40px)] py-[clamp(24px,3vw,40px)]" aria-label="Featured article magazine grid demo">

  <header class="max-w-[1240px] mx-auto flex flex-wrap items-center justify-between gap-3 pb-4.5 mb-[clamp(24px,3vw,40px)] border-b-2 border-tcg14-ink">
    <span class="font-tcg14-serif italic font-black text-[clamp(1.5rem,2.4vw,2rem)] tracking-[-0.01em]">The Quarterly</span>
    <span class="text-[.78rem] font-bold tracking-[0.18em] uppercase text-tcg14-muted">Issue 38 &middot; Summer 2026</span>
  </header>

  <div class="max-w-[1240px] mx-auto grid [grid-template-columns:1.5fr_1fr] max-[900px]:[grid-template-columns:1fr] gap-[clamp(20px,2.6vw,36px)]">

    <article class="group flex flex-col overflow-hidden rounded-[14px] border border-tcg14-line bg-tcg14-card transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_18px_36px_-18px_oklch(0.2_0.04_260/0.18)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="h-[clamp(220px,28vw,360px)] bg-[linear-gradient(180deg,oklch(0.21_0.04_260/0)_60%,oklch(0.21_0.04_260/0.4)),linear-gradient(135deg,#dc2626_0%,#7c1d1d_60%,#1a0a0a_100%)]" aria-hidden="true"></div>
      <div class="flex flex-col gap-3 p-[clamp(22px,2.4vw,32px)]">
        <span class="self-start px-2.5 py-1 rounded-[3px] bg-tcg14-cat-politics text-white text-[.66rem] font-bold tracking-[0.18em] uppercase">Politics</span>
        <h2 class="font-tcg14-serif font-black text-[clamp(1.6rem,2.8vw,2.4rem)] leading-[1.1] tracking-[-0.02em] text-pretty"><a href="#feature" class="no-underline text-tcg14-ink hover:text-tcg14-cat-politics focus-visible:outline-2 focus-visible:outline-tcg14-ink focus-visible:outline-offset-3">The Quiet Reformers Behind 2026's Strangest Bipartisan Bill</a></h2>
        <p class="text-[clamp(.95rem,1.15vw,1.06rem)] leading-[1.5] text-tcg14-muted text-pretty">A coalition of 14 senators, six think tanks, and a Reddit forum spent three years drafting the housing reform nobody believed could pass. It just did.</p>
        <footer class="flex flex-wrap items-center gap-2.5 mt-1 pt-3.5 border-t border-tcg14-line text-[.82rem] text-tcg14-muted">
          <span class="flex items-center gap-2.5">
            <span class="w-8 h-8 rounded-full bg-linear-[135deg,#f9c1cf,#d97a99]" aria-hidden="true"></span>
            <span><strong class="font-bold text-tcg14-ink">Maya Chen</strong> &middot; Politics Editor</span>
          </span>
          <span class="text-[.5rem] opacity-40" aria-hidden="true">&#9679;</span>
          <span class="font-semibold">14 min read</span>
          <span class="text-[.5rem] opacity-40" aria-hidden="true">&#9679;</span>
          <time datetime="2026-06-28" class="font-semibold">June 28, 2026</time>
        </footer>
      </div>
    </article>

    <div class="grid [grid-template-rows:repeat(4,1fr)] gap-[clamp(12px,1.4vw,16px)]">

      <article class="flex max-[520px]:flex-col gap-3.5 p-3.5 rounded-xl border border-tcg14-line bg-tcg14-card transition-[translate,box-shadow] duration-250 hover:-translate-y-0.5 hover:shadow-[0_12px_22px_-14px_oklch(0.2_0.04_260/0.18)] focus-within:-translate-y-0.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="shrink-0 w-24 h-24 max-[520px]:w-full max-[520px]:h-35 rounded-lg bg-linear-[135deg,#0ea5e9,#0c4a6e]" aria-hidden="true"></div>
        <div class="flex-1 min-w-0 flex flex-col justify-between gap-1.5">
          <span class="self-start px-2 py-0.75 rounded-[3px] bg-tcg14-cat-tech text-white text-[.6rem] font-bold tracking-[0.16em] uppercase">Tech</span>
          <h3 class="font-tcg14-serif font-extrabold text-[clamp(.95rem,1.2vw,1.1rem)] leading-[1.22] text-pretty"><a href="#tech" class="no-underline text-tcg14-ink hover:text-tcg14-cat-tech focus-visible:outline-2 focus-visible:outline-tcg14-ink focus-visible:outline-offset-3">The Engineer Who Resigned Over an AI Memo</a></h3>
          <span class="text-[.74rem] font-semibold text-tcg14-muted">8 min &middot; June 27</span>
        </div>
      </article>

      <article class="flex max-[520px]:flex-col gap-3.5 p-3.5 rounded-xl border border-tcg14-line bg-tcg14-card transition-[translate,box-shadow] duration-250 hover:-translate-y-0.5 hover:shadow-[0_12px_22px_-14px_oklch(0.2_0.04_260/0.18)] focus-within:-translate-y-0.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="shrink-0 w-24 h-24 max-[520px]:w-full max-[520px]:h-35 rounded-lg bg-linear-[135deg,#c026d3,#581c87]" aria-hidden="true"></div>
        <div class="flex-1 min-w-0 flex flex-col justify-between gap-1.5">
          <span class="self-start px-2 py-0.75 rounded-[3px] bg-tcg14-cat-culture text-white text-[.6rem] font-bold tracking-[0.16em] uppercase">Culture</span>
          <h3 class="font-tcg14-serif font-extrabold text-[clamp(.95rem,1.2vw,1.1rem)] leading-[1.22] text-pretty"><a href="#culture" class="no-underline text-tcg14-ink hover:text-tcg14-cat-culture focus-visible:outline-2 focus-visible:outline-tcg14-ink focus-visible:outline-offset-3">Why the Best Bookstores in 2026 Have Bouncers</a></h3>
          <span class="text-[.74rem] font-semibold text-tcg14-muted">6 min &middot; June 26</span>
        </div>
      </article>

      <article class="flex max-[520px]:flex-col gap-3.5 p-3.5 rounded-xl border border-tcg14-line bg-tcg14-card transition-[translate,box-shadow] duration-250 hover:-translate-y-0.5 hover:shadow-[0_12px_22px_-14px_oklch(0.2_0.04_260/0.18)] focus-within:-translate-y-0.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="shrink-0 w-24 h-24 max-[520px]:w-full max-[520px]:h-35 rounded-lg bg-linear-[135deg,#16a34a,#14532d]" aria-hidden="true"></div>
        <div class="flex-1 min-w-0 flex flex-col justify-between gap-1.5">
          <span class="self-start px-2 py-0.75 rounded-[3px] bg-tcg14-cat-climate text-white text-[.6rem] font-bold tracking-[0.16em] uppercase">Climate</span>
          <h3 class="font-tcg14-serif font-extrabold text-[clamp(.95rem,1.2vw,1.1rem)] leading-[1.22] text-pretty"><a href="#climate" class="no-underline text-tcg14-ink hover:text-tcg14-cat-climate focus-visible:outline-2 focus-visible:outline-tcg14-ink focus-visible:outline-offset-3">The Farmers Quietly Outsmarting the Drought</a></h3>
          <span class="text-[.74rem] font-semibold text-tcg14-muted">11 min &middot; June 25</span>
        </div>
      </article>

      <article class="flex max-[520px]:flex-col gap-3.5 p-3.5 rounded-xl border border-tcg14-line bg-tcg14-card transition-[translate,box-shadow] duration-250 hover:-translate-y-0.5 hover:shadow-[0_12px_22px_-14px_oklch(0.2_0.04_260/0.18)] focus-within:-translate-y-0.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="shrink-0 w-24 h-24 max-[520px]:w-full max-[520px]:h-35 rounded-lg bg-linear-[135deg,#dc2626,#7c1d1d]" aria-hidden="true"></div>
        <div class="flex-1 min-w-0 flex flex-col justify-between gap-1.5">
          <span class="self-start px-2 py-0.75 rounded-[3px] bg-tcg14-cat-biz text-white text-[.6rem] font-bold tracking-[0.16em] uppercase">Business</span>
          <h3 class="font-tcg14-serif font-extrabold text-[clamp(.95rem,1.2vw,1.1rem)] leading-[1.22] text-pretty"><a href="#business" class="no-underline text-tcg14-ink hover:text-tcg14-cat-biz focus-visible:outline-2 focus-visible:outline-tcg14-ink focus-visible:outline-offset-3">Inside the Five-Day Workweek Comeback</a></h3>
          <span class="text-[.74rem] font-semibold text-tcg14-muted">9 min &middot; June 24</span>
        </div>
      </article>

    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg14-bg: #fffefb;
  --color-tcg14-bg: oklch(0.995 0.004 95);
  --color-tcg14-card: #ffffff;
  --color-tcg14-card: oklch(1 0 0);
  --color-tcg14-ink: #0f172a;
  --color-tcg14-ink: oklch(0.21 0.04 260);
  --color-tcg14-muted: #64748b;
  --color-tcg14-muted: oklch(0.55 0.03 257);
  --color-tcg14-line: #e7e3d8;
  --color-tcg14-line: oklch(0.91 0.01 90);
  --color-tcg14-cat-politics: #0f172a;
  --color-tcg14-cat-politics: oklch(0.21 0.04 260);
  --color-tcg14-cat-tech: #0369a1;
  --color-tcg14-cat-tech: oklch(0.48 0.13 245);
  --color-tcg14-cat-culture: #a21caf;
  --color-tcg14-cat-culture: oklch(0.48 0.24 320);
  --color-tcg14-cat-climate: #15803d;
  --color-tcg14-cat-climate: oklch(0.5 0.14 150);
  --color-tcg14-cat-biz: #b91c1c;
  --color-tcg14-cat-biz: oklch(0.48 0.2 27);
  --font-tcg14-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcg14-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
}
/* Root rule: the full-bleed contract. */

.tcg-14 {
  width: 100%;
  min-height: 100svh;
}

.tcg-14 ::selection {
  background: #0f172a;
  color: #fff;
}
```
