---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/minimal-editorial-table-design-tailwind-css/"
title: "Minimal Editorial Table Design in Tailwind CSS"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A magazine-style review index set in Newsreader's optical-size serif: borderless rows, a heavy masthead rule, two hairlines framing the header and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Editorial Table Design in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-tables/minimal-editorial-table-design-tailwind-css/

A magazine-style review index set in Newsreader's optical-size serif: borderless rows, a heavy masthead rule, two hairlines framing the header and a terracotta arrow that slides in on hover. Ratings became a score plus a hairline meter instead of ★ glyphs a screen reader spells out, and titles are real links with an animated underline.
## HTML
```html
<section class="ttb-08 grid-cols-1 w-full min-h-svh grid place-items-center bg-ttb08-bg px-8 py-16 font-ttb08-sans text-ttb08-ink" aria-label="Minimal editorial table demo">
  <div class="w-full max-w-3xl">
    <header class="flex items-start justify-between gap-6 border-b-[3px] border-ttb08-ink pb-3">
      <p class="font-ttb08-serif text-[clamp(26px,4vw,34px)] leading-none font-bold tracking-[-0.03em]">The Marginalia Review</p>
      <p class="text-right text-[11px] leading-relaxed tracking-[0.14em] text-ttb08-mut uppercase">Issue No. 48<br>Summer 2025</p>
    </header>
    <p class="mt-2 text-[11px] tracking-[0.24em] text-ttb08-mut uppercase">Literature · Art · Culture · Ideas</p>
    <h2 class="mt-10 font-ttb08-serif text-2xl italic">Notable works of the season</h2>
    <p class="mt-2 max-w-xl text-sm leading-relaxed text-ttb08-mut text-pretty">An editorial index of the quarter's most significant titles, curated by our panel of contributing critics and independent reviewers.</p>
    <table class="mt-8 w-full border-collapse text-left">
      <caption class="sr-only">Notable works of the season with genre, length, publication month and panel score</caption>
      <thead class="border-y border-ttb08-ink [&_th]:py-2.5 [&_th]:text-[10.5px] [&_th]:font-semibold [&_th]:tracking-[0.18em] [&_th]:text-ttb08-mut [&_th]:uppercase [&_th:not(:first-child)]:pl-5">
        <tr><th scope="col">Title &amp; author</th><th scope="col">Genre</th><th scope="col" class="text-right max-sm:hidden">Pages</th><th scope="col" class="max-sm:hidden">Published</th><th scope="col" class="text-right">Score</th></tr>
      </thead>
      <tbody class="[&_td]:py-4 [&_td]:align-top [&_td:not(:first-child)]:pl-5 [&_tr]:border-b [&_tr]:border-ttb08-line [&_tr:last-child]:border-ttb08-ink">
        <tr class="group/row">
          <td class="relative"><span aria-hidden="true" class="absolute top-4 -left-6 font-bold text-ttb08-acc opacity-0 -translate-x-1.5 transition duration-200 group-focus-within/row:translate-x-0 group-focus-within/row:opacity-100 group-hover/row:translate-x-0 group-hover/row:opacity-100 motion-reduce:transition-none">→</span><a href="#" class="font-ttb08-serif text-[17px] italic underline decoration-transparent decoration-1 underline-offset-4 transition-colors hover:decoration-ttb08-acc focus-visible:decoration-ttb08-acc focus-visible:outline-none">The Architecture of Forgetting</a><div class="mt-0.5 text-xs text-ttb08-mut">Miriam Osei-Bonsu</div></td>
          <td class="text-[11px] font-semibold tracking-[0.1em] text-ttb08-mut uppercase">Literary fiction</td>
          <td class="text-right text-sm tabular-nums max-sm:hidden">384</td>
          <td class="text-sm text-ttb08-mut max-sm:hidden">Mar 2025</td>
          <td class="text-right"><div class="font-ttb08-serif text-xl font-bold tabular-nums">9.2</div><div class="mt-1 ml-auto h-0.5 w-14 bg-ttb08-line" role="img" aria-label="9.2 out of 10"><div class="h-full w-[92%] bg-ttb08-acc"></div></div></td>
        </tr>
        <tr class="group/row">
          <td class="relative"><span aria-hidden="true" class="absolute top-4 -left-6 font-bold text-ttb08-acc opacity-0 -translate-x-1.5 transition duration-200 group-focus-within/row:translate-x-0 group-focus-within/row:opacity-100 group-hover/row:translate-x-0 group-hover/row:opacity-100 motion-reduce:transition-none">→</span><a href="#" class="font-ttb08-serif text-[17px] italic underline decoration-transparent decoration-1 underline-offset-4 transition-colors hover:decoration-ttb08-acc focus-visible:decoration-ttb08-acc focus-visible:outline-none">Meridian</a><div class="mt-0.5 text-xs text-ttb08-mut">Takeshi Murakami-White</div></td>
          <td class="text-[11px] font-semibold tracking-[0.1em] text-ttb08-mut uppercase">Essays</td>
          <td class="text-right text-sm tabular-nums max-sm:hidden">228</td>
          <td class="text-sm text-ttb08-mut max-sm:hidden">Jan 2025</td>
          <td class="text-right"><div class="font-ttb08-serif text-xl font-bold tabular-nums">8.7</div><div class="mt-1 ml-auto h-0.5 w-14 bg-ttb08-line" role="img" aria-label="8.7 out of 10"><div class="h-full w-[87%] bg-ttb08-acc"></div></div></td>
        </tr>
        <tr class="group/row">
          <td class="relative"><span aria-hidden="true" class="absolute top-4 -left-6 font-bold text-ttb08-acc opacity-0 -translate-x-1.5 transition duration-200 group-focus-within/row:translate-x-0 group-focus-within/row:opacity-100 group-hover/row:translate-x-0 group-hover/row:opacity-100 motion-reduce:transition-none">→</span><a href="#" class="font-ttb08-serif text-[17px] italic underline decoration-transparent decoration-1 underline-offset-4 transition-colors hover:decoration-ttb08-acc focus-visible:decoration-ttb08-acc focus-visible:outline-none">Salt Coast Elegy</a><div class="mt-0.5 text-xs text-ttb08-mut">Priya Venkatesh</div></td>
          <td class="text-[11px] font-semibold tracking-[0.1em] text-ttb08-mut uppercase">Poetry</td>
          <td class="text-right text-sm tabular-nums max-sm:hidden">112</td>
          <td class="text-sm text-ttb08-mut max-sm:hidden">Feb 2025</td>
          <td class="text-right"><div class="font-ttb08-serif text-xl font-bold tabular-nums">9.5</div><div class="mt-1 ml-auto h-0.5 w-14 bg-ttb08-line" role="img" aria-label="9.5 out of 10"><div class="h-full w-[95%] bg-ttb08-acc"></div></div></td>
        </tr>
        <tr class="group/row">
          <td class="relative"><span aria-hidden="true" class="absolute top-4 -left-6 font-bold text-ttb08-acc opacity-0 -translate-x-1.5 transition duration-200 group-focus-within/row:translate-x-0 group-focus-within/row:opacity-100 group-hover/row:translate-x-0 group-hover/row:opacity-100 motion-reduce:transition-none">→</span><a href="#" class="font-ttb08-serif text-[17px] italic underline decoration-transparent decoration-1 underline-offset-4 transition-colors hover:decoration-ttb08-acc focus-visible:decoration-ttb08-acc focus-visible:outline-none">Cartographies of the Unseen</a><div class="mt-0.5 text-xs text-ttb08-mut">Elara J. Hoffmann</div></td>
          <td class="text-[11px] font-semibold tracking-[0.1em] text-ttb08-mut uppercase">Non-fiction</td>
          <td class="text-right text-sm tabular-nums max-sm:hidden">471</td>
          <td class="text-sm text-ttb08-mut max-sm:hidden">Apr 2025</td>
          <td class="text-right"><div class="font-ttb08-serif text-xl font-bold tabular-nums">8.1</div><div class="mt-1 ml-auto h-0.5 w-14 bg-ttb08-line" role="img" aria-label="8.1 out of 10"><div class="h-full w-[81%] bg-ttb08-acc"></div></div></td>
        </tr>
        <tr class="group/row">
          <td class="relative"><span aria-hidden="true" class="absolute top-4 -left-6 font-bold text-ttb08-acc opacity-0 -translate-x-1.5 transition duration-200 group-focus-within/row:translate-x-0 group-focus-within/row:opacity-100 group-hover/row:translate-x-0 group-hover/row:opacity-100 motion-reduce:transition-none">→</span><a href="#" class="font-ttb08-serif text-[17px] italic underline decoration-transparent decoration-1 underline-offset-4 transition-colors hover:decoration-ttb08-acc focus-visible:decoration-ttb08-acc focus-visible:outline-none">A Brief History of Thresholds</a><div class="mt-0.5 text-xs text-ttb08-mut">Tobias Lund</div></td>
          <td class="text-[11px] font-semibold tracking-[0.1em] text-ttb08-mut uppercase">Autofiction</td>
          <td class="text-right text-sm tabular-nums max-sm:hidden">296</td>
          <td class="text-sm text-ttb08-mut max-sm:hidden">May 2025</td>
          <td class="text-right"><div class="font-ttb08-serif text-xl font-bold tabular-nums">7.9</div><div class="mt-1 ml-auto h-0.5 w-14 bg-ttb08-line" role="img" aria-label="7.9 out of 10"><div class="h-full w-[79%] bg-ttb08-acc"></div></div></td>
        </tr>
      </tbody>
    </table>
    <footer class="mt-4 flex flex-wrap justify-between gap-2 text-[11px] tracking-[0.12em] text-ttb08-mut uppercase">
      <span>Scores out of 10 · panel consensus</span><span>© The Marginalia Review</span>
    </footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb08-bg: #fbf7f1;
  --color-ttb08-bg: oklch(0.975 0.01 80);
  --color-ttb08-ink: #1a1714;
  --color-ttb08-ink: oklch(0.2 0.01 60);
  --color-ttb08-mut: #6b645c;
  --color-ttb08-mut: oklch(0.5 0.015 65);
  --color-ttb08-line: #e6ddd2;
  --color-ttb08-line: oklch(0.9 0.016 75);
  --color-ttb08-acc: #b5472a;
  --color-ttb08-acc: oklch(0.53 0.15 37);
  --font-ttb08-serif: 'Newsreader', Georgia, serif;
  --font-ttb08-sans: 'Instrument Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-08 {
  width: 100%;
  min-height: 100svh;
}
```
