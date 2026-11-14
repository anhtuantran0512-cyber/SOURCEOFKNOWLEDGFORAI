---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-flip-position-try-fallbacks/"
title: "Tailwind Popover Flip with Position Try Fallbacks"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "Collision handling was the main reason to install a positioning library."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Popover Flip with Position Try Fallbacks
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-flip-position-try-fallbacks/

Collision handling was the main reason to install a positioning library. [position-try-fallbacks:flip-block,flip-inline,--tpop07-side] replaces it: list what you accept and the browser tries each until the panel fits. Drag the strip to push the node to an edge and watch the panel change sides. The one thing that stays CSS is the named @position-try block — an at-rule has no utility.
## HTML
```html
<section class="tpop-07 group/root w-full min-h-svh bg-tpop07-bg bg-[repeating-linear-gradient(0deg,transparent_0_3px,oklch(1_0_0/0.018)_3px_4px)] px-3.5 py-9 font-tpop07-mono text-tpop07-ink" aria-label="Popover flip with position-try fallbacks demo">
  <div class="grid min-h-[calc(100svh-72px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[34rem] border border-tpop07-rule bg-tpop07-surface">
      <div class="flex items-center gap-1.5 border-b border-tpop07-rule px-4 py-2.5" aria-hidden="true">
        <span class="size-2 rounded-full bg-tpop07-rule"></span><span class="size-2 rounded-full bg-tpop07-rule"></span><span class="size-2 rounded-full bg-tpop07-phos"></span>
        <span class="ml-2 text-[11px] text-tpop07-mut">~/cluster/eu-west-1b</span>
      </div>
      <div class="px-4 pt-4 pb-4">
        <p class="mb-3.5 text-[11.5px] uppercase tracking-[0.08em] text-tpop07-mut"><span class="text-tpop07-phos">$</span> drag the strip, then open the node</p>
        <div class="snap-x snap-mandatory overflow-x-auto overscroll-x-contain border border-dashed border-tpop07-rule px-3 py-3.5 [scrollbar-color:var(--color-tpop07-phos)_var(--color-tpop07-surface)]">
          <div class="flex w-max items-center gap-2.5">
            <span class="grid min-h-11 w-19 flex-none snap-center place-items-center border border-tpop07-rule text-[11.5px] text-tpop07-mut">idle</span>
            <span class="grid min-h-11 w-19 flex-none snap-center place-items-center border border-tpop07-rule text-[11.5px] text-tpop07-mut">idle</span>
            <span class="grid min-h-11 w-19 flex-none snap-center place-items-center border border-tpop07-rule text-[11.5px] text-tpop07-mut">idle</span>
            <button id="tpop-07-trigger" type="button" popovertarget="tpop-07-panel" class="inline-flex min-h-11 flex-none cursor-pointer snap-center items-center gap-2 border border-tpop07-phos bg-tpop07-phos px-3.5 text-[12.5px] font-bold text-tpop07-bg transition-[background-color,color,box-shadow] duration-150 [anchor-name:--tpop07-a] hover:shadow-[0_0_18px_oklch(0.86_0.2_150/0.45)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop07-ink group-has-[#tpop-07-panel:popover-open]/root:bg-tpop07-bg group-has-[#tpop-07-panel:popover-open]/root:text-tpop07-phos">
              node-07
              <svg viewBox="0 0 16 16" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
            </button>
            <span class="grid min-h-11 w-19 flex-none snap-center place-items-center border border-tpop07-rule text-[11.5px] text-tpop07-mut">idle</span>
            <span class="grid min-h-11 w-19 flex-none snap-center place-items-center border border-tpop07-rule text-[11.5px] text-tpop07-mut">idle</span>
            <span class="grid min-h-11 w-19 flex-none snap-center place-items-center border border-tpop07-rule text-[11.5px] text-tpop07-mut">idle</span>
          </div>
        </div>
        <ol class="mt-4 grid gap-1.5 text-[12px] leading-normal text-tpop07-mut">
          <li class="min-w-0"><span class="text-tpop07-phos">1</span> · position-area: block-end center</li>
          <li class="min-w-0"><span class="text-tpop07-phos">2</span> · flip-block</li>
          <li class="min-w-0"><span class="text-tpop07-phos">3</span> · flip-inline</li>
          <li class="min-w-0"><span class="text-tpop07-phos">4</span> · @position-try --tpop07-side</li>
        </ol>
      </div>
    </div>
  </div>

  <div popover="auto" id="tpop-07-panel" role="group" aria-label="Node detail" class="fixed m-auto w-[min(17rem,calc(100vw-24px))] border border-tpop07-phos bg-tpop07-surface px-3.5 py-3.5 text-tpop07-ink opacity-0 shadow-[0_0_0_1px_oklch(0.86_0.2_150/0.12),0_18px_40px_-22px_oklch(0.86_0.2_150/0.4)] transition-[opacity,display,overlay] duration-150 transition-discrete [position-anchor:--tpop07-a] [position-area:block-end_center] [position-try-fallbacks:flip-block,flip-inline,--tpop07-side] [position-visibility:anchors-visible] open:opacity-100 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2.5">
    <p class="mb-2.5 text-[12.5px] font-bold tracking-[0.04em] text-tpop07-phos">node-07 · eu-west-1b</p>
    <dl class="mb-1 grid grid-cols-[auto_1fr] gap-x-3 gap-y-1 text-[12px] leading-normal">
      <dt class="text-tpop07-mut">cpu</dt><dd class="flex items-center gap-2">41%<span class="h-1 flex-auto bg-tpop07-rule"><span class="block h-full w-[41%] bg-tpop07-phos"></span></span></dd>
      <dt class="text-tpop07-mut">mem</dt><dd class="flex items-center gap-2">2.8/8 GiB<span class="h-1 flex-auto bg-tpop07-rule"><span class="block h-full w-[35%] bg-tpop07-phos"></span></span></dd>
      <dt class="text-tpop07-mut">pods</dt><dd>14</dd>
      <dt class="text-tpop07-mut">drain</dt><dd>6d ago · Jordan Lee</dd>
    </dl>
    <p class="mt-2.5 border-t border-dashed border-tpop07-rule pt-2.5 text-[11.5px]">I flip rather than clip.<span class="ml-0.5 inline-block w-[0.6ch] animate-pulse bg-tpop07-phos motion-reduce:animate-none">&nbsp;</span></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop07-bg: #060a08;
  --color-tpop07-bg: oklch(0.14 0.01 170);
  --color-tpop07-surface: #0b1411;
  --color-tpop07-surface: oklch(0.18 0.014 170);
  --color-tpop07-ink: #d5f4e2;
  --color-tpop07-ink: oklch(0.94 0.04 160);
  --color-tpop07-mut: #84b198;
  --color-tpop07-mut: oklch(0.72 0.06 160);
  --color-tpop07-phos: #56f487;
  --color-tpop07-phos: oklch(0.86 0.2 150);
  --color-tpop07-rule: #1f332a;
  --color-tpop07-rule: oklch(0.3 0.03 165);
  --font-tpop07-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* The one at-rule utilities cannot express: a named fallback bundle. Referenced from the panel's
   [position-try-fallbacks:…,--tpop07-side] utility. Ignored by engines without anchoring. */

@position-try --tpop07-side {
  position-area: inline-end center;
  margin: 0 0 0 10px;
  max-inline-size: min(15rem, calc(100vw - 24px));
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpop-07 {
  width: 100%;
  min-height: 100svh;
}
```
