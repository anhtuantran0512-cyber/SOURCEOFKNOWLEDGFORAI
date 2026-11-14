---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-brutalist-rubber-stamp-toggle/"
title: "Tailwind Brutalist Rubber-Stamp Toggle"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Checking it stamps: a rotated APPROVED block slams down over the card with a scale-and-settle keyframe, borders 3px, shadow hard and offset."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Brutalist Rubber-Stamp Toggle
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-brutalist-rubber-stamp-toggle/

Checking it stamps: a rotated APPROVED block slams down over the card with a scale-and-settle keyframe, borders 3px, shadow hard and offset. Where demo 17 snaps a thumb, this one commits an act &mdash; the state looks like a decision that was made.
## HTML
```html
<section class="ttg-38 w-full min-h-svh grid place-items-center px-8 py-16 bg-ttg38-bg font-ttg38-mono" aria-label="Brutalist stamp toggle">
  <div class="relative">
    <input type="checkbox" id="ttg-38-sw" role="switch" aria-label="Approve expense report" class="peer sr-only">
    <label for="ttg-38-sw" class="flex flex-col gap-5 w-[min(340px,100%)] p-7 bg-white border-[3px] border-ttg38-line cursor-pointer shadow-[8px_8px_0_var(--color-ttg38-line)] transition-[background-color,box-shadow] duration-[90ms] ease-[steps(1,end)] active:translate-x-1 active:translate-y-1 active:shadow-[4px_4px_0_var(--color-ttg38-line)] peer-checked:bg-ttg38-paperon peer-focus-visible:outline-4 peer-focus-visible:outline-ttg38-line peer-focus-visible:outline-offset-4 peer-checked:[&_.ttg38-track]:bg-ttg38-ink peer-checked:[&_.ttg38-thumb]:translate-x-[40px] motion-reduce:transition-none">
      <span class="flex flex-col gap-1">
        <b class="text-[11px] font-bold tracking-[0.22em] text-ttg38-muted">EXPENSE / 4471</b>
        <span class="text-[19px] font-extrabold tracking-[-0.01em] text-ttg38-line leading-tight">Q3 hardware &mdash; $2,480</span>
      </span>
      <span class="flex items-center justify-between gap-4 pt-4 border-t-[3px] border-ttg38-line">
        <span class="text-[13px] font-bold tracking-[0.12em] text-ttg38-line">APPROVE</span>
        <span aria-hidden="true" class="ttg38-track block w-20 h-10 border-[3px] border-ttg38-line bg-white relative transition-colors duration-[90ms] ease-[steps(1,end)]">
          <i class="ttg38-thumb absolute top-0.5 left-0.5 block w-7 h-7 bg-ttg38-line transition-transform duration-[90ms] ease-[steps(1,end)]"></i>
        </span>
      </span>
    </label>
    <span aria-hidden="true" class="ttg38-stamp pointer-events-none peer-checked:opacity-100 peer-checked:animate-ttg38-slam motion-reduce:peer-checked:animate-none absolute -top-5 -right-6 grid place-items-center px-5 py-2.5 opacity-0 -rotate-[14deg] border-[5px] border-ttg38-ink outline-4 outline-ttg38-ink outline-offset-[-10px] text-[22px] font-extrabold tracking-[0.14em] text-ttg38-ink">APPROVED</span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg38-bg: #ece8dd;
  --color-ttg38-bg: oklch(0.93 0.012 90);
  --color-ttg38-line: #000000;
  --color-ttg38-line: oklch(0 0 0);
  --color-ttg38-ink: #c2261f;
  --color-ttg38-ink: oklch(0.5 0.2 27);
  --color-ttg38-paperon: #fdf6e8;
  --color-ttg38-paperon: oklch(0.97 0.02 88);
  --color-ttg38-muted: #57534a;
  --color-ttg38-muted: oklch(0.45 0.012 90);
  --font-ttg38-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --animate-ttg38-slam: ttg38-slam 0.26s cubic-bezier(0.2, 0.8, 0.3, 1) forwards;
}

@keyframes ttg38-slam {
  0% {
    opacity: 0;
    transform: rotate(-14deg) scale(2.4);
  }

  60% {
    opacity: 1;
    transform: rotate(-14deg) scale(0.92);
  }

  100% {
    opacity: 1;
    transform: rotate(-14deg) scale(1);
  }
}

.ttg-38 {
  width: 100%;
  min-height: 100svh;
}
/* The stamp is a sibling of the label, not a descendant, so the peer state reaches it
   directly — and it must stay visible after the animation under reduced motion. */

@media (prefers-reduced-motion: reduce) {
  .ttg-38 .peer:checked ~ .ttg38-stamp {
    opacity: 1;
    transform: rotate(-14deg) scale(1);
  }
}
```
