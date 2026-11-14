---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-tooltip-arrow-pointing-to-anchor/"
title: "Tailwind Tooltip Arrow Pointing to Anchor"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "The bubble is easy; the tail is what breaks."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tooltip Arrow Pointing to Anchor
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-tooltip-arrow-pointing-to-anchor/

The bubble is easy; the tail is what breaks. Here the tail is the bubble's after: pseudo-element, itself anchor-positioned to the trigger with the same area and the same flip list, so it stays on the button's midline when the bubble is clamped or flipped. Every rule of it is an after: utility — gated so unanchored engines draw no tail rather than a wrong one.
## HTML
```html
<section class="tpop-08 transition-[--tpop08-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop08-d:1] [[data-theme=dark]_&]:[--tpop08-d:1] [[data-theme=light]_&]:[--tpop08-d:0] group/root w-full min-h-svh bg-tpop08-bg px-4.5 py-10 font-tpop08-sans text-tpop08-ink" aria-label="Tooltip arrow pointing to anchor demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[27rem] rounded-2xl border border-tpop08-rule bg-tpop08-surface px-4.5 pt-5 pb-4.5 shadow-[0_14px_30px_-22px_oklch(0.3_0.03_150/0.45)]">
      <p class="mb-3.5 text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop08-sage">Team roster</p>
      <ul class="grid">
        <li class="flex min-w-0 items-center gap-3 border-b border-tpop08-rule py-1.5">
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tpop08-sage/14 text-[11px] font-bold text-tpop08-sage">PS</span>
          <span class="min-w-0 flex-auto text-[14.5px] font-semibold">Priya Sharma</span>
          <span class="flex-none rounded-full bg-tpop08-bg px-2 py-1 text-xs text-tpop08-mut">Reviewer</span>
          <button id="tpop-08-trigger" type="button" popovertarget="tpop-08-tip" aria-label="What reviewer permissions mean" aria-describedby="tpop-08-tip" class="inline-flex size-11 flex-none cursor-pointer items-center justify-center rounded-full border border-tpop08-rule text-tpop08-sage transition-colors [anchor-name:--tpop08-a] hover:bg-tpop08-bg focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop08-sage group-has-[#tpop-08-tip:popover-open]/root:border-tpop08-sage group-has-[#tpop-08-tip:popover-open]/root:bg-tpop08-sage group-has-[#tpop-08-tip:popover-open]/root:text-tpop08-surface">
            <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="10" cy="10" r="7.2"/><path d="M10 9v5M10 6.3v.8"/></svg>
          </button>
        </li>
        <li class="flex min-w-0 items-center gap-3 py-1.5">
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tpop08-ink/8 text-[11px] font-bold text-tpop08-ink">SR</span>
          <span class="min-w-0 flex-auto text-[14.5px] font-semibold">Sam Rivera</span>
          <span class="flex-none rounded-full bg-tpop08-bg px-2 py-1 text-xs text-tpop08-mut">Owner</span>
          <span aria-hidden="true" class="w-11 flex-none"></span>
        </li>
      </ul>
      <p class="mt-4 text-[12.5px] leading-relaxed text-tpop08-mut">Open the hint, then narrow the frame — the tail follows the button, not the bubble.</p>
    </div>
  </div>

  <div popover="auto" id="tpop-08-tip" role="tooltip" class="fixed m-auto w-[min(15rem,calc(100vw-28px))] rounded-2xl bg-tpop08-ink px-3.5 py-2.5 text-[13px] leading-normal text-tpop08-surface opacity-0 shadow-[0_12px_24px_-10px_oklch(0.3_0.03_150/0.45)] text-pretty transition-[opacity,display,overlay] duration-150 transition-discrete [position-anchor:--tpop08-a] [position-area:block-end_center] [justify-self:anchor-center] [position-try-fallbacks:flip-block] open:opacity-100 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-3 after:size-3 after:rotate-45 after:rounded-[3px] after:bg-tpop08-ink after:[position-anchor:--tpop08-a] after:[position-area:block-end_center] after:[justify-self:anchor-center] after:[position-try-fallbacks:flip-block] supports-[anchor-name:--a]:after:fixed supports-[anchor-name:--a]:after:inset-auto supports-[anchor-name:--a]:after:m-0 supports-[anchor-name:--a]:after:mt-1.5 supports-[anchor-name:--a]:after:content-['']">
    Reviewers can comment and approve, but cannot merge or change settings.
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop08-bg: #ecf0e8;
  --color-tpop08-bg: oklch(0.95 0.012 130);
  --color-tpop08-surface: #ffffff;
  --color-tpop08-surface: oklch(1 0 0);
  --color-tpop08-ink: #18281e;
  --color-tpop08-ink: oklch(0.26 0.03 155);
  --color-tpop08-mut: #506353;
  --color-tpop08-mut: oklch(0.48 0.035 150);
  --color-tpop08-rule: #dae0d7;
  --color-tpop08-rule: oklch(0.9 0.015 135);
  --color-tpop08-sage: #386649;
  --color-tpop08-sage: oklch(0.47 0.07 155);
  --font-tpop08-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop08-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-08 {
  width: 100%;
  min-height: 100svh;
  --color-tpop08-bg: color-mix(in oklch, oklch(0.17 0.012 150) calc(var(--tpop08-d) * 100%), oklch(0.95 0.012 130));
  --color-tpop08-surface: color-mix(in oklch, oklch(0.215 0.014 150) calc(var(--tpop08-d) * 100%), oklch(1 0 0));
  --color-tpop08-ink: color-mix(in oklch, oklch(0.94 0.012 140) calc(var(--tpop08-d) * 100%), oklch(0.26 0.03 155));
  --color-tpop08-mut: color-mix(in oklch, oklch(0.73 0.03 145) calc(var(--tpop08-d) * 100%), oklch(0.48 0.035 150));
  --color-tpop08-rule: color-mix(in oklch, oklch(0.31 0.016 150) calc(var(--tpop08-d) * 100%), oklch(0.9 0.015 135));
  --color-tpop08-sage: color-mix(in oklch, oklch(0.76 0.09 155) calc(var(--tpop08-d) * 100%), oklch(0.47 0.07 155));
}
```
