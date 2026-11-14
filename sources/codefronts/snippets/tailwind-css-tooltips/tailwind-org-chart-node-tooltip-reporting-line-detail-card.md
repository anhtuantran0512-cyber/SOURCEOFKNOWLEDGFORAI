---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-org-chart-node-tooltip-reporting-line-detail-card/"
title: "Tailwind Org Chart Node Tooltip with Reporting-Line Detail Card"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A four-node org tree where each box opens a person card: hero band, ringed portrait, department pill, reports / org size / tenure, and contact plus timezone."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Org Chart Node Tooltip with Reporting-Line Detail Card
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-org-chart-node-tooltip-reporting-line-detail-card/

A four-node org tree where each box opens a person card: hero band, ringed portrait, department pill, reports / org size / tenure, and contact plus timezone. The port's placement rule is declarative &mdash; nodes left of centre open right, nodes right of centre open left, one modifier class each.
## HTML
```html
<section class="ttp-18 w-full min-h-svh flex items-center justify-center bg-ttp18-stage px-[280px] py-10 font-ttp18-sans max-xl:px-7">
  <div class="flex flex-col items-center">

    <div class="flex justify-center gap-4.5">
      <div class="group relative">
        <button type="button" aria-describedby="ttp18-n1" class="ttp18-box border-ttp18-ceo bg-linear-to-br from-[#faf9ff] to-white">
          <span class="ttp18-av bg-linear-to-br from-[#6028a0] to-[#9060d0]">SL</span>
          <span class="ttp18-bname">Sarah Lindqvist</span>
          <span class="ttp18-btitle">Chief Executive Officer</span>
          <span class="ttp18-bdept">Executive</span>
        </button>
        <div id="ttp18-n1" role="tooltip" class="ttp18-card ttp18-card-left">
          <div class="relative h-12.5 bg-linear-to-br from-[#4a1880] to-[#8050c0]"></div>
          <div class="ttp18-photo bg-linear-to-br from-[#6028a0] to-[#9060d0]">SL</div>
          <div class="px-3.5 pt-5 pb-2.75">
            <div class="ttp18-name">Sarah Lindqvist</div>
            <div class="ttp18-title">Chief Executive Officer</div>
            <span class="ttp18-pill">Executive · Board</span>
            <div class="ttp18-stats"><div><div class="ttp18-sn">2</div><div class="ttp18-sl">Reports</div></div><div><div class="ttp18-sn">214</div><div class="ttp18-sl">Org Size</div></div><div><div class="ttp18-sn">8yr</div><div class="ttp18-sl">Tenure</div></div></div>
          </div>
          <div class="ttp18-foot"><span>[email protected]</span><span>NYC · EST</span></div>
        </div>
      </div>
    </div>

    <div class="mx-auto h-6 w-px bg-ttp18-line" aria-hidden="true"></div>

    <div class="flex justify-center gap-4.5">
      <div class="group relative">
        <button type="button" aria-describedby="ttp18-n2" class="ttp18-box border-ttp18-edge bg-white">
          <span class="ttp18-av bg-linear-to-br from-[#204080] to-[#4070c0]">MW</span>
          <span class="ttp18-bname">Marcus Webb</span>
          <span class="ttp18-btitle">Chief Technology Officer</span>
          <span class="ttp18-bdept">Engineering</span>
        </button>
        <div id="ttp18-n2" role="tooltip" class="ttp18-card ttp18-card-left">
          <div class="relative h-12.5 bg-linear-to-br from-[#102060] to-[#3060a0]"></div>
          <div class="ttp18-photo bg-linear-to-br from-[#204080] to-[#4070c0]">MW</div>
          <div class="px-3.5 pt-5 pb-2.75">
            <div class="ttp18-name">Marcus Webb</div>
            <div class="ttp18-title">Chief Technology Officer</div>
            <span class="ttp18-pill">Engineering · Platform</span>
            <div class="ttp18-stats"><div><div class="ttp18-sn">2</div><div class="ttp18-sl">Reports</div></div><div><div class="ttp18-sn">96</div><div class="ttp18-sl">Org Size</div></div><div><div class="ttp18-sn">5yr</div><div class="ttp18-sl">Tenure</div></div></div>
          </div>
          <div class="ttp18-foot"><span>[email protected]</span><span>SF · PST</span></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp18-n3" class="ttp18-box border-ttp18-edge bg-white">
          <span class="ttp18-av bg-linear-to-br from-[#0a6050] to-[#1aa080]">ER</span>
          <span class="ttp18-bname">Elena Russo</span>
          <span class="ttp18-btitle">Chief Marketing Officer</span>
          <span class="ttp18-bdept">Marketing</span>
        </button>
        <div id="ttp18-n3" role="tooltip" class="ttp18-card">
          <div class="relative h-12.5 bg-linear-to-br from-[#054030] to-[#108060]"></div>
          <div class="ttp18-photo bg-linear-to-br from-[#0a6050] to-[#1aa080]">ER</div>
          <div class="px-3.5 pt-5 pb-2.75">
            <div class="ttp18-name">Elena Russo</div>
            <div class="ttp18-title">Chief Marketing Officer</div>
            <span class="ttp18-pill">Marketing · Growth</span>
            <div class="ttp18-stats"><div><div class="ttp18-sn">2</div><div class="ttp18-sl">Reports</div></div><div><div class="ttp18-sn">68</div><div class="ttp18-sl">Org Size</div></div><div><div class="ttp18-sn">3yr</div><div class="ttp18-sl">Tenure</div></div></div>
          </div>
          <div class="ttp18-foot"><span>[email protected]</span><span>London · GMT</span></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp18-n4" class="ttp18-box border-ttp18-edge bg-white">
          <span class="ttp18-av bg-linear-to-br from-[#804010] to-[#c07030]">AT</span>
          <span class="ttp18-bname">Amir Tahir</span>
          <span class="ttp18-btitle">Chief Financial Officer</span>
          <span class="ttp18-bdept">Finance</span>
        </button>
        <div id="ttp18-n4" role="tooltip" class="ttp18-card">
          <div class="relative h-12.5 bg-linear-to-br from-[#603008] to-[#a06020]"></div>
          <div class="ttp18-photo bg-linear-to-br from-[#804010] to-[#c07030]">AT</div>
          <div class="px-3.5 pt-5 pb-2.75">
            <div class="ttp18-name">Amir Tahir</div>
            <div class="ttp18-title">Chief Financial Officer</div>
            <span class="ttp18-pill">Finance · Strategy</span>
            <div class="ttp18-stats"><div><div class="ttp18-sn">2</div><div class="ttp18-sl">Reports</div></div><div><div class="ttp18-sn">50</div><div class="ttp18-sl">Org Size</div></div><div><div class="ttp18-sn">2yr</div><div class="ttp18-sl">Tenure</div></div></div>
          </div>
          <div class="ttp18-foot"><span>[email protected]</span><span>Dubai · GST</span></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp18-stage: #f7f7f9;
  --color-ttp18-stage: oklch(0.97 0.002 285);
  --color-ttp18-ink: #1a1a2e;
  --color-ttp18-ink: oklch(0.23 0.03 280);
  --color-ttp18-accent: #5555a0;
  --color-ttp18-accent: oklch(0.47 0.09 285);
  --color-ttp18-muted: #6e6e80;
  --color-ttp18-muted: oklch(0.52 0.02 285);
  --color-ttp18-edge: #e0e0e8;
  --color-ttp18-edge: oklch(0.91 0.005 285);
  --color-ttp18-line: #d0d0d8;
  --color-ttp18-line: oklch(0.86 0.005 285);
  --color-ttp18-ceo: #b9a6e4;
  --color-ttp18-ceo: oklch(0.75 0.08 293);
  --color-ttp18-chip: #f0f0f8;
  --color-ttp18-chip: oklch(0.96 0.005 285);
  --font-ttp18-sans: 'Inter', system-ui, sans-serif;
}

.ttp-18 {
  width: 100%;
  min-height: 100svh;
}
/* Four nodes, one card at two placements. */

.ttp-18 .ttp18-box {
  @apply block w-[130px] cursor-help rounded-lg border p-0 px-3 py-2.25 text-center transition-[border-color,box-shadow] duration-150 group-hover:border-ttp18-accent/50 group-hover:shadow-[0_4px_16px_rgba(0,0,40,0.08)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp18-accent;
}

.ttp-18 .ttp18-av {
  @apply mx-auto mb-1.75 flex h-7.5 w-7.5 items-center justify-center rounded-full text-[10.5px] font-semibold tracking-[0.03em] text-white;
}

.ttp-18 .ttp18-bname {
  @apply block text-[10.5px] font-semibold text-ttp18-ink;
}

.ttp-18 .ttp18-btitle {
  @apply mt-0.5 block text-[9px] tracking-[0.04em] text-ttp18-muted;
}

.ttp-18 .ttp18-bdept {
  @apply mt-px block text-[8.5px] uppercase tracking-[0.06em] text-ttp18-muted;
}

.ttp-18 .ttp18-card {
  @apply pointer-events-none invisible absolute top-1/2 left-[calc(100%+12px)] z-50 w-[230px] max-w-[calc(100vw-48px)] -translate-y-1/2 translate-x-1.5 overflow-hidden rounded-[10px] border border-ttp18-edge bg-white text-left opacity-0 shadow-[0_8px_30px_rgba(0,0,40,0.12),0_2px_8px_rgba(0,0,40,0.06)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-x-0 group-focus-within:opacity-100;
}

.ttp-18 .ttp18-card-left {
  @apply left-auto right-[calc(100%+12px)] -translate-x-1.5 group-hover:translate-x-0 group-focus-within:translate-x-0;
}

.ttp-18 .ttp18-photo {
  @apply absolute top-[36px] left-3.5 flex h-11 w-11 items-center justify-center rounded-full border-3 border-white text-[13px] font-semibold text-white shadow-[0_2px_8px_rgba(0,0,0,0.15)];
}

.ttp-18 .ttp18-name {
  @apply text-sm font-semibold text-ttp18-ink;
}

.ttp-18 .ttp18-title {
  @apply mt-px text-[10.5px] text-ttp18-accent;
}

.ttp-18 .ttp18-pill {
  @apply mt-1.5 inline-block rounded border border-ttp18-edge bg-ttp18-chip px-1.75 py-0.5 text-[9px] tracking-[0.04em] text-ttp18-accent;
}

.ttp-18 .ttp18-stats {
  @apply mt-2.75 grid grid-cols-3 border-t border-ttp18-chip pt-2.5 text-center;
}

.ttp-18 .ttp18-sn {
  @apply text-sm font-semibold text-ttp18-ink;
}

.ttp-18 .ttp18-sl {
  @apply mt-0.5 text-[8.5px] uppercase tracking-[0.08em] text-ttp18-muted;
}

.ttp-18 .ttp18-foot {
  @apply flex justify-between gap-2 border-t border-ttp18-chip px-3.5 py-2.25 text-[10px] text-ttp18-muted;
}

@media (max-width: 1279px) {
  .ttp-18 .ttp18-card,
    .ttp-18 .ttp18-card-left {
    @apply static hidden mt-2 w-full translate-x-0 translate-y-0 group-hover:block group-focus-within:block;
  }

  .ttp-18 .ttp18-photo {
    @apply top-[36px];
  }
}
```
