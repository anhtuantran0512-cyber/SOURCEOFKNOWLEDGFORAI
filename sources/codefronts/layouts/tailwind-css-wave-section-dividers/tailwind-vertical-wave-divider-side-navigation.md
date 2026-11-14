---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-vertical-wave-divider-side-navigation/"
title: "Tailwind Vertical Wave Divider for Side Navigation"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "The wave rotated 90&deg;: a curved vertical seam between a sidebar and the content column."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Wave Divider for Side Navigation
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-vertical-wave-divider-side-navigation/

The wave rotated 90&deg;: a curved vertical seam between a sidebar and the content column. Includes the container-query collapse &mdash; @max-md: on a @container root &mdash; that turns the vertical wave into a horizontal one when the layout stacks.
## HTML
```html
<section class="twd-14 w-full min-h-svh flex flex-col justify-center gap-0 font-twd14-sans">

  <!-- Sidebar with a curved vertical seam -->
  <div class="@container w-full">
    <div class="grid grid-cols-[minmax(190px,28%)_1fr] @max-[560px]:grid-cols-1 min-h-[320px] bg-twd14-main">
      <aside class="relative bg-twd14-side text-white pl-7 pr-6 py-8 @max-[560px]:pb-14">
        <p class="text-base font-extrabold tracking-[-0.01em] mb-6">codefronts</p>
        <nav aria-label="Section navigation">
          <ul class="list-none flex flex-col gap-1 pr-9 @max-[560px]:pr-0">
            <li><a href="#0" aria-current="page" class="flex items-center min-h-11 px-2.5 rounded-lg text-[14.5px] text-twd14-onside no-underline hover:bg-twd14-hover hover:text-white aria-[current=page]:bg-twd14-active aria-[current=page]:text-white aria-[current=page]:shadow-[inset_2px_0_0_var(--color-twd14-accent)] focus-visible:outline-2 focus-visible:outline-twd14-accent focus-visible:outline-offset-2">Overview</a></li>
            <li><a href="#0" class="flex items-center min-h-11 px-2.5 rounded-lg text-[14.5px] text-twd14-onside no-underline hover:bg-twd14-hover hover:text-white focus-visible:outline-2 focus-visible:outline-twd14-accent focus-visible:outline-offset-2">Dividers</a></li>
            <li><a href="#0" class="flex items-center min-h-11 px-2.5 rounded-lg text-[14.5px] text-twd14-onside no-underline hover:bg-twd14-hover hover:text-white focus-visible:outline-2 focus-visible:outline-twd14-accent focus-visible:outline-offset-2">Gradients</a></li>
            <li><a href="#0" class="flex items-center min-h-11 px-2.5 rounded-lg text-[14.5px] text-twd14-onside no-underline hover:bg-twd14-hover hover:text-white focus-visible:outline-2 focus-visible:outline-twd14-accent focus-visible:outline-offset-2">Masks</a></li>
          </ul>
        </nav>
        <svg class="absolute inset-y-0 -right-px block h-full w-[clamp(26px,4vw,58px)] text-twd14-main [&_path]:fill-current pointer-events-none @max-[560px]:inset-y-auto @max-[560px]:inset-x-0 @max-[560px]:-bottom-px @max-[560px]:h-[34px] @max-[560px]:w-full" viewBox="0 0 120 800" preserveAspectRatio="none" aria-hidden="true" focusable="false">
          <path d="M64,0 C104,140 24,260 60,400 C96,540 20,660 56,800 L120,800 L120,0 Z"></path>
        </svg>
      </aside>
      <main class="px-8 pt-9 pb-10 text-twd14-mainink">
        <h2 class="text-[clamp(21px,3vw,30px)] font-semibold mb-2.5">Vertical seam, authored portrait</h2>
        <p class="text-[15px] max-w-[48ch]">The wave runs down the grid instead of across it &mdash; for split-screen and creative sidebar layouts. Narrow the pane and the container query re-pins it to the bottom edge.</p>
      </main>
    </div>
  </div>

  <!-- Split-screen vertical mask -->
  <div class="@container w-full">
    <div class="grid grid-cols-2 @max-[620px]:grid-cols-1 min-h-[300px] bg-twd14-left">
      <div class="flex flex-col justify-center gap-2 px-7 py-10 text-twd14-onleft">
        <h2 class="text-[clamp(22px,3.2vw,32px)] font-semibold">Split screen</h2>
        <p class="text-[15px] max-w-[36ch]">Masked edge, no SVG node.</p>
      </div>
      <div class="twd-14-seam flex items-center -ml-8 pl-32 pr-7 py-10 bg-twd14-right text-twd14-rightink [mask:var(--twd14-seam)_no-repeat_left_center/120px_100%,linear-gradient(#000,#000)_no-repeat_right_center/calc(100%-118px)_100%] @max-[620px]:ml-0 @max-[620px]:pl-7 @max-[620px]:[mask:none]">
        <p class="text-[15px]">The right panel carries a vertical wave mask on its left edge, so the two halves interlock.</p>
      </div>
    </div>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd14-side: #2b2547;
  --color-twd14-side: oklch(0.26 0.06 285);
  --color-twd14-onside: #ddd8ec;
  --color-twd14-onside: oklch(0.89 0.03 285);
  --color-twd14-hover: #3c3560;
  --color-twd14-hover: oklch(0.34 0.06 285);
  --color-twd14-active: #473c73;
  --color-twd14-active: oklch(0.38 0.08 285);
  --color-twd14-accent: #e3c14a;
  --color-twd14-accent: oklch(0.83 0.14 95);
  --color-twd14-main: #f5f4f9;
  --color-twd14-main: oklch(0.96 0.01 285);
  --color-twd14-mainink: #3f3a55;
  --color-twd14-mainink: oklch(0.4 0.04 285);
  --color-twd14-left: #4a221f;
  --color-twd14-left: oklch(0.3 0.08 25);
  --color-twd14-onleft: #f6e7db;
  --color-twd14-onleft: oklch(0.94 0.03 60);
  --color-twd14-right: #f6efe3;
  --color-twd14-right: oklch(0.95 0.03 70);
  --color-twd14-rightink: #54382a;
  --color-twd14-rightink: oklch(0.38 0.07 45);
  --font-twd14-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* The portrait seam for the split-screen mask. It is masked at a FIXED 120px width and
   composited with an opaque layer for the rest of the panel, so the curve keeps its
   authored proportions instead of stretching across the whole half. */

.twd-14 {
  width: 100%;
  min-height: 100svh;
  --twd14-seam: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20800'%20preserveAspectRatio='none'%3E%3Cpath%20d='M60,0%20C110,160%2020,300%2066,440%20C104,556%2026,660%2062,800%20L200,800%20L200,0%20Z'%20fill='%23000'/%3E%3C/svg%3E");
}
/* Safari < 15.4 mask shim for the split-screen seam. */

@media (width >= 39rem) {
  .twd-14 .twd-14-seam {
    -webkit-mask: var(--twd14-seam) no-repeat left center/120px 100%, linear-gradient(#000, #000) no-repeat right center/calc(100% - 118px) 100%;
  }
}
```
