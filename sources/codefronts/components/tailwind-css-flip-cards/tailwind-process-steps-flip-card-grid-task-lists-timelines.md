---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-process-steps-flip-card-grid-task-lists-timelines/"
title: "Tailwind Process Steps Flip Card Grid with Task Lists & Timelines"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "Four numbered phases, each flipping to its task list and duration."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Process Steps Flip Card Grid with Task Lists & Timelines
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-process-steps-flip-card-grid-task-lists-timelines/

Four numbered phases, each flipping to its task list and duration. The port's structural win is deleting eight :nth-child colour rules: in utilities each card simply states its own palette, so reordering the steps &mdash; or dropping one &mdash; cannot silently recolour the rest of the sequence.
## HTML
```html
<section class="tfc-14 w-full min-h-svh grid place-items-center bg-tfc14-bg font-tfc14-sans px-5 py-10 text-tfc14-ink">
  <ol class="grid w-full max-w-[920px] grid-cols-[repeat(auto-fit,minmax(200px,1fr))] gap-5">

    <li class="group relative h-[290px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc14-indigo has-[:focus-visible]:outline-offset-4">
      <input id="tfc-14-s1" type="checkbox" class="peer sr-only">
      <label for="tfc-14-s1" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show tasks for step 1, Strategy</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col items-center justify-center gap-3 rounded-2xl overflow-hidden px-4 py-6 bg-linear-160 from-tfc14-i1 to-tfc14-i2 border border-tfc14-indigo/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_16px_36px_-16px_oklch(0.4_0.18_275/0.5)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="pointer-events-none absolute -bottom-5 -right-2.5 text-[80px] font-black italic leading-none text-tfc14-indigo/8">01</span>
          <span class="relative z-1 grid size-13 place-items-center rounded-2xl border border-white/12 bg-tfc14-indigo/15 text-[22px]">&#127919;</span>
          <p class="relative z-1 text-[11px] font-bold uppercase tracking-[0.12em] text-tfc14-indigoL">01 &middot; Strategy</p>
          <h3 class="relative z-1 text-center text-base font-extrabold leading-snug text-tfc14-indigoP">Define Goals &amp; Scope</h3>
          <p class="absolute bottom-3 text-[9px] tracking-[0.08em] text-tfc14-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden px-4 py-4.5 bg-linear-160 from-tfc14-b1 to-tfc14-b2 border border-tfc14-sky/20 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.15em] text-tfc14-indigoL">Step 01 &middot; Strategy</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">Define Goals &amp; Scope</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] leading-[1.4] text-tfc14-ink/70">
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-indigoL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Stakeholder interviews &amp; alignment</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-indigoL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>OKR definition &amp; success metrics</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-indigoL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Risk &amp; constraint mapping</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-indigoL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Project charter sign-off</li>
          </ul>
          <p class="mt-auto border-t border-white/6 pt-2 text-[10px] text-tfc14-muted">1&ndash;2 weeks</p>
        </div>
      </div>
    </li>

    <li class="group relative h-[290px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc14-green has-[:focus-visible]:outline-offset-4">
      <input id="tfc-14-s2" type="checkbox" class="peer sr-only">
      <label for="tfc-14-s2" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show tasks for step 2, Research</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col items-center justify-center gap-3 rounded-2xl overflow-hidden px-4 py-6 bg-linear-160 from-tfc14-g1 to-tfc14-g2 border border-tfc14-green/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_16px_36px_-16px_oklch(0.5_0.15_150/0.4)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="pointer-events-none absolute -bottom-5 -right-2.5 text-[80px] font-black italic leading-none text-tfc14-green/8">02</span>
          <span class="relative z-1 grid size-13 place-items-center rounded-2xl border border-white/12 bg-tfc14-green/12 text-[22px]">&#128300;</span>
          <p class="relative z-1 text-[11px] font-bold uppercase tracking-[0.12em] text-tfc14-greenL">02 &middot; Research</p>
          <h3 class="relative z-1 text-center text-base font-extrabold leading-snug text-tfc14-greenP">Discover &amp; Validate</h3>
          <p class="absolute bottom-3 text-[9px] tracking-[0.08em] text-tfc14-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden px-4 py-4.5 bg-linear-160 from-tfc14-b1 to-tfc14-b2 border border-tfc14-green/20 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.15em] text-tfc14-greenL">Step 02 &middot; Research</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">Discover &amp; Validate</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] leading-[1.4] text-tfc14-ink/70">
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-greenL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>User interviews (12+ sessions)</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-greenL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Competitive analysis matrix</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-greenL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Journey &amp; persona mapping</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-greenL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Insights synthesis report</li>
          </ul>
          <p class="mt-auto border-t border-white/6 pt-2 text-[10px] text-tfc14-muted">2&ndash;3 weeks</p>
        </div>
      </div>
    </li>

    <li class="group relative h-[290px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc14-orange has-[:focus-visible]:outline-offset-4">
      <input id="tfc-14-s3" type="checkbox" class="peer sr-only">
      <label for="tfc-14-s3" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show tasks for step 3, Design</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col items-center justify-center gap-3 rounded-2xl overflow-hidden px-4 py-6 bg-linear-160 from-tfc14-o1 to-tfc14-o2 border border-tfc14-orange/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_16px_36px_-16px_oklch(0.55_0.18_45/0.4)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="pointer-events-none absolute -bottom-5 -right-2.5 text-[80px] font-black italic leading-none text-tfc14-orange/8">03</span>
          <span class="relative z-1 grid size-13 place-items-center rounded-2xl border border-white/12 bg-tfc14-orange/12 text-[22px]">&#9999;&#65039;</span>
          <p class="relative z-1 text-[11px] font-bold uppercase tracking-[0.12em] text-tfc14-orangeL">03 &middot; Design</p>
          <h3 class="relative z-1 text-center text-base font-extrabold leading-snug text-tfc14-orangeP">Prototype &amp; Test</h3>
          <p class="absolute bottom-3 text-[9px] tracking-[0.08em] text-tfc14-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden px-4 py-4.5 bg-linear-160 from-tfc14-b1 to-tfc14-b2 border border-tfc14-orange/20 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.15em] text-tfc14-orangeL">Step 03 &middot; Design</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">Prototype &amp; Test</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] leading-[1.4] text-tfc14-ink/70">
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-orangeL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Information architecture</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-orangeL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Hi-fi interactive prototypes</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-orangeL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Usability test rounds</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-orangeL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Design system tokens</li>
          </ul>
          <p class="mt-auto border-t border-white/6 pt-2 text-[10px] text-tfc14-muted">3&ndash;4 weeks</p>
        </div>
      </div>
    </li>

    <li class="group relative h-[290px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc14-violet has-[:focus-visible]:outline-offset-4">
      <input id="tfc-14-s4" type="checkbox" class="peer sr-only">
      <label for="tfc-14-s4" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show tasks for step 4, Launch</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col items-center justify-center gap-3 rounded-2xl overflow-hidden px-4 py-6 bg-linear-160 from-tfc14-v1 to-tfc14-v2 border border-tfc14-violet/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_16px_36px_-16px_oklch(0.5_0.2_300/0.4)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="pointer-events-none absolute -bottom-5 -right-2.5 text-[80px] font-black italic leading-none text-tfc14-violet/8">04</span>
          <span class="relative z-1 grid size-13 place-items-center rounded-2xl border border-white/12 bg-tfc14-violet/12 text-[22px]">&#128640;</span>
          <p class="relative z-1 text-[11px] font-bold uppercase tracking-[0.12em] text-tfc14-violetL">04 &middot; Launch</p>
          <h3 class="relative z-1 text-center text-base font-extrabold leading-snug text-tfc14-violetP">Ship &amp; Measure</h3>
          <p class="absolute bottom-3 text-[9px] tracking-[0.08em] text-tfc14-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden px-4 py-4.5 bg-linear-160 from-tfc14-b1 to-tfc14-b2 border border-tfc14-violet/20 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.15em] text-tfc14-violetL">Step 04 &middot; Launch</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">Ship &amp; Measure</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] leading-[1.4] text-tfc14-ink/70">
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-violetL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Staged rollout &amp; QA pass</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-violetL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Analytics instrumentation</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-violetL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>30/60/90 day OKR review</li>
            <li class="flex items-start gap-1.5"><svg viewBox="0 0 10 10" class="mt-0.5 size-2.5 shrink-0 fill-none stroke-tfc14-violetL stroke-[2.5]" aria-hidden="true"><polyline points="2,5 4,8 8,2"/></svg>Retrospective &amp; iteration</li>
          </ul>
          <p class="mt-auto border-t border-white/6 pt-2 text-[10px] text-tfc14-muted">Ongoing</p>
        </div>
      </div>
    </li>

  </ol>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc14-bg: #070710;
  --color-tfc14-bg: oklch(0.12 0.02 280);
  --color-tfc14-i1: #0f0f2e;
  --color-tfc14-i1: oklch(0.18 0.06 280);
  --color-tfc14-i2: #080820;
  --color-tfc14-i2: oklch(0.14 0.05 280);
  --color-tfc14-g1: #0d1a10;
  --color-tfc14-g1: oklch(0.19 0.04 155);
  --color-tfc14-g2: #080e0a;
  --color-tfc14-g2: oklch(0.14 0.02 155);
  --color-tfc14-o1: #1a0d0d;
  --color-tfc14-o1: oklch(0.19 0.04 30);
  --color-tfc14-o2: #0e0808;
  --color-tfc14-o2: oklch(0.14 0.02 30);
  --color-tfc14-v1: #0d0a20;
  --color-tfc14-v1: oklch(0.17 0.06 295);
  --color-tfc14-v2: #080614;
  --color-tfc14-v2: oklch(0.13 0.04 295);
  --color-tfc14-b1: #0d0d22;
  --color-tfc14-b1: oklch(0.17 0.04 280);
  --color-tfc14-b2: #0a1020;
  --color-tfc14-b2: oklch(0.16 0.035 265);
  --color-tfc14-indigo: #6366f1;
  --color-tfc14-indigo: oklch(0.58 0.2 280);
  --color-tfc14-indigoL: #818cf8;
  --color-tfc14-indigoL: oklch(0.68 0.16 280);
  --color-tfc14-indigoP: #c7d2fe;
  --color-tfc14-indigoP: oklch(0.86 0.07 280);
  --color-tfc14-green: #22c55e;
  --color-tfc14-green: oklch(0.73 0.18 150);
  --color-tfc14-greenL: #4ade80;
  --color-tfc14-greenL: oklch(0.8 0.17 152);
  --color-tfc14-greenP: #bbf7d0;
  --color-tfc14-greenP: oklch(0.92 0.08 155);
  --color-tfc14-orange: #f97316;
  --color-tfc14-orange: oklch(0.7 0.19 45);
  --color-tfc14-orangeL: #fb923c;
  --color-tfc14-orangeL: oklch(0.76 0.16 55);
  --color-tfc14-orangeP: #fed7aa;
  --color-tfc14-orangeP: oklch(0.9 0.07 70);
  --color-tfc14-violet: #a855f7;
  --color-tfc14-violet: oklch(0.65 0.22 300);
  --color-tfc14-violetL: #c084fc;
  --color-tfc14-violetL: oklch(0.75 0.17 300);
  --color-tfc14-violetP: #e9d5ff;
  --color-tfc14-violetP: oklch(0.91 0.06 300);
  --color-tfc14-ink: #eef2ff;
  --color-tfc14-ink: oklch(0.96 0.015 280);
  --color-tfc14-muted: #a8adc7;
  --color-tfc14-muted: oklch(0.75 0.03 280);
  --color-tfc14-dim: #83879e;
  --color-tfc14-dim: oklch(0.62 0.025 280);
  --font-tfc14-sans: 'Sora', system-ui, sans-serif;
}

.tfc-14 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-14 * {
    transition-duration: 1ms !important;
  }
}
```
