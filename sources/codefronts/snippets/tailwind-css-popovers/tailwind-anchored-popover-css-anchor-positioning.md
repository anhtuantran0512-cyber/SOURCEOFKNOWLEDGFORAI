---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-anchored-popover-css-anchor-positioning/"
title: "Tailwind Anchored Popover with CSS Anchor Positioning"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "Popover owns the top layer and dismissal; anchor positioning owns placement."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Anchored Popover with CSS Anchor Positioning
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-anchored-popover-css-anchor-positioning/

Popover owns the top layer and dismissal; anchor positioning owns placement. In Tailwind both halves are arbitrary properties on the elements they describe — [anchor-name:--tpop03-a] on the chip, [position-anchor:--tpop03-a] [position-area:block-end_span-inline-end] on the panel — and the UA reset that makes it work sits behind supports-[anchor-name:--a]: so unanchored engines still get a centred panel.
## HTML
```html
<section class="tpop-03 transition-[--tpop03-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop03-d:1] [[data-theme=dark]_&]:[--tpop03-d:1] [[data-theme=light]_&]:[--tpop03-d:0] group/root w-full min-h-svh bg-tpop03-paper px-4.5 py-10 font-tpop03-sans text-tpop03-ink" aria-label="Anchored popover with CSS anchor positioning demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[30rem] border-2 border-tpop03-edge bg-tpop03-pop px-5 pt-5.5 pb-5 shadow-[8px_8px_0_var(--color-tpop03-edge)]">
      <p class="mb-2 text-[11px] font-bold uppercase tracking-[0.18em] text-tpop03-acc">Checkout · Order 40118</p>
      <h2 class="mb-5 font-tpop03-serif text-[clamp(28px,6vw,38px)] leading-[1.05] tracking-[-0.01em]">Two features, <em class="italic text-tpop03-acc">one panel</em></h2>
      <table class="w-full border-collapse">
        <tbody>
          <tr class="border-b border-tpop03-edge/15"><th scope="row" class="py-3 text-left text-sm font-normal text-tpop03-mut">Subtotal</th><td class="py-3 text-right text-sm font-medium tabular-nums">$248.00</td></tr>
          <tr class="border-b border-tpop03-edge/15">
            <th scope="row" class="py-1.5 text-left font-normal">
              <button id="tpop-03-trigger" type="button" popovertarget="tpop-03-panel" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 border-2 border-tpop03-edge bg-tpop03-paper px-3 text-[13px] font-semibold text-tpop03-ink transition-[background-color,color,translate,box-shadow] duration-150 [anchor-name:--tpop03-a] hover:-translate-x-px hover:-translate-y-px hover:shadow-[3px_3px_0_var(--color-tpop03-edge)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop03-acc motion-reduce:transition-none group-has-[#tpop-03-panel:popover-open]/root:translate-0 group-has-[#tpop-03-panel:popover-open]/root:bg-tpop03-ink group-has-[#tpop-03-panel:popover-open]/root:text-tpop03-pop group-has-[#tpop-03-panel:popover-open]/root:shadow-none">
                Duties estimate
                <svg viewBox="0 0 16 16" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="8" cy="8" r="6"/><path d="M8 7.2v4M8 5.2v.6"/></svg>
              </button>
            </th>
            <td class="py-3 text-right text-sm font-medium tabular-nums">$19.84</td>
          </tr>
          <tr class="border-b border-tpop03-edge/15"><th scope="row" class="py-3 text-left text-sm font-normal text-tpop03-mut">Shipping</th><td class="py-3 text-right text-sm font-medium tabular-nums">$0.00</td></tr>
          <tr><th scope="row" class="pt-3.5 text-left text-base font-bold">Total</th><td class="pt-3.5 text-right text-base font-bold tabular-nums">$267.84</td></tr>
        </tbody>
      </table>
      <p class="mt-4 text-[12.5px] text-tpop03-mut">The chip is the anchor. The panel finds it by name.</p>
    </div>
  </div>

  <div popover="auto" id="tpop-03-panel" role="group" aria-label="How duties are estimated" class="fixed m-auto w-[min(20rem,calc(100vw-32px))] border-2 border-tpop03-edge bg-tpop03-pop p-4 text-tpop03-ink opacity-0 shadow-[6px_6px_0_var(--color-tpop03-edge)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop03-a] [position-area:block-end_span-inline-end] [position-try-fallbacks:flip-block,flip-inline] open:opacity-100 starting:open:-translate-y-1.5 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2.5">
    <p class="mb-2 text-[11px] font-bold uppercase tracking-[0.16em] text-tpop03-acc">How this is estimated</p>
    <p class="mb-3.5 text-[13.5px] leading-relaxed text-tpop03-mut text-pretty">8% of the declared value for goods entering the EU under DDP terms. Final duties are set at the border and may differ by a few cents.</p>
    <dl class="grid gap-1.5 border-t-2 border-tpop03-edge pt-2.5">
      <div class="flex min-w-0 justify-between gap-3"><dt class="text-[13px] text-tpop03-mut">Basis</dt><dd class="text-[13px] font-semibold tabular-nums">$248.00</dd></div>
      <div class="flex min-w-0 justify-between gap-3"><dt class="text-[13px] text-tpop03-mut">Rate</dt><dd class="text-[13px] font-semibold tabular-nums">8.0%</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop03-paper: #f1eadc;
  --color-tpop03-paper: oklch(0.94 0.02 85);
  --color-tpop03-pop: #fefdf7;
  --color-tpop03-pop: oklch(0.993 0.008 95);
  --color-tpop03-ink: #251e15;
  --color-tpop03-ink: oklch(0.24 0.02 75);
  --color-tpop03-mut: #645642;
  --color-tpop03-mut: oklch(0.46 0.035 75);
  --color-tpop03-edge: #251e15;
  --color-tpop03-edge: oklch(0.24 0.02 75);
  --color-tpop03-acc: #b13e06;
  --color-tpop03-acc: oklch(0.52 0.16 40);
  --font-tpop03-serif: 'Instrument Serif', Georgia, serif;
  --font-tpop03-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop03-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-03 {
  width: 100%;
  min-height: 100svh;
  --color-tpop03-paper: color-mix(in oklch, oklch(0.18 0.014 75) calc(var(--tpop03-d) * 100%), oklch(0.94 0.02 85));
  --color-tpop03-pop: color-mix(in oklch, oklch(0.22 0.014 75) calc(var(--tpop03-d) * 100%), oklch(0.993 0.008 95));
  --color-tpop03-ink: color-mix(in oklch, oklch(0.94 0.015 85) calc(var(--tpop03-d) * 100%), oklch(0.24 0.02 75));
  --color-tpop03-mut: color-mix(in oklch, oklch(0.74 0.03 80) calc(var(--tpop03-d) * 100%), oklch(0.46 0.035 75));
  --color-tpop03-edge: color-mix(in oklch, oklch(0.94 0.015 85) calc(var(--tpop03-d) * 100%), oklch(0.24 0.02 75));
  --color-tpop03-acc: color-mix(in oklch, oklch(0.74 0.13 45) calc(var(--tpop03-d) * 100%), oklch(0.52 0.16 40));
}
```
