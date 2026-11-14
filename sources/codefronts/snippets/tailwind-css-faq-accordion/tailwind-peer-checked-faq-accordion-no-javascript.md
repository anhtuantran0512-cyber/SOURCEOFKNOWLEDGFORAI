---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-peer-checked-faq-accordion-no-javascript/"
title: "Tailwind Peer-Checked FAQ Accordion with No JavaScript"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The checkbox hack, ported whole: a peer checkbox holds the open state, its <label> is the question row, and peer-checked:grid-rows-[1fr] animates the answer…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Peer-Checked FAQ Accordion with No JavaScript
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-peer-checked-faq-accordion-no-javascript/

The checkbox hack, ported whole: a peer checkbox holds the open state, its <label> is the question row, and peer-checked:grid-rows-[1fr] animates the answer to its natural height. This is the one accordion pattern that needs no CSS block at all — the 0fr&rarr;1fr trick is fully expressible in utilities, so the entire disclosure lives in the markup.
## HTML
```html
<section class="tfa-01 w-full min-h-svh grid place-items-center bg-tfa01-bg font-tfa01-sans text-tfa01-ink px-5 py-12 bg-[radial-gradient(1100px_600px_at_80%_-10%,var(--color-tfa01-glow),transparent_60%)]">
  <div class="w-[min(680px,100%)]">
    <header>
      <span class="inline-flex items-center gap-2 rounded-full border border-tfa01-accedge px-3 py-1.5 font-tfa01-mono text-[11px] font-semibold uppercase tracking-[0.16em] text-tfa01-acc">Billing &amp; plans</span>
      <h1 class="mt-4 text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Frequently asked questions</h1>
      <p class="mt-3 max-w-[54ch] text-[15px] leading-relaxed text-tfa01-mut">Every panel opens with zero JavaScript — the state is a <code class="rounded bg-tfa01-code px-1.5 py-0.5 font-tfa01-mono text-[0.85em] text-tfa01-acc">peer</code> checkbox, the animation is a grid row.</p>
    </header>

    <div class="mt-8 flex flex-col gap-2.5">
      <div class="group/item relative overflow-hidden rounded-2xl border border-tfa01-edge bg-tfa01-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa01-accedge has-checked:shadow-[0_18px_40px_-24px_oklch(0.6_0.15_165/0.45)]">
        <input id="tfa01-q1" type="checkbox" class="peer absolute opacity-0 pointer-events-none" checked>
        <label for="tfa01-q1" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa01-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa01-acc">
          <span>Can I switch plans mid-cycle?</span>
          <i aria-hidden="true" class="relative grid size-7 shrink-0 place-items-center rounded-lg bg-tfa01-code before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa01-acc before:transition-transform before:duration-450 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa01-acc after:rotate-90 after:transition-transform after:duration-450 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14.5px] leading-[1.7] text-tfa01-mut">Yes — upgrades apply instantly and we prorate the difference on your next invoice. Downgrades take effect at the end of the current billing period, so you never lose time you already paid for.</p></div>
        </div>
      </div>

      <div class="group/item relative overflow-hidden rounded-2xl border border-tfa01-edge bg-tfa01-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa01-accedge has-checked:shadow-[0_18px_40px_-24px_oklch(0.6_0.15_165/0.45)]">
        <input id="tfa01-q2" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa01-q2" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa01-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa01-acc">
          <span>Do you offer an annual discount?</span>
          <i aria-hidden="true" class="relative grid size-7 shrink-0 place-items-center rounded-lg bg-tfa01-code before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa01-acc before:transition-transform before:duration-450 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa01-acc after:rotate-90 after:transition-transform after:duration-450 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14.5px] leading-[1.7] text-tfa01-mut">Annual billing saves 20% on every tier and locks your price for the year. Switch from monthly at any time from Settings → Billing — the unused portion of your month is credited automatically.</p></div>
        </div>
      </div>

      <div class="group/item relative overflow-hidden rounded-2xl border border-tfa01-edge bg-tfa01-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa01-accedge has-checked:shadow-[0_18px_40px_-24px_oklch(0.6_0.15_165/0.45)]">
        <input id="tfa01-q3" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa01-q3" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa01-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa01-acc">
          <span>What happens when my trial ends?</span>
          <i aria-hidden="true" class="relative grid size-7 shrink-0 place-items-center rounded-lg bg-tfa01-code before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa01-acc before:transition-transform before:duration-450 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa01-acc after:rotate-90 after:transition-transform after:duration-450 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14.5px] leading-[1.7] text-tfa01-mut">Your workspace switches to the free tier — nothing is deleted. Projects over the free limit become read-only until you pick a plan, and we email you three days before, so it is never a surprise.</p></div>
        </div>
      </div>

      <div class="group/item relative overflow-hidden rounded-2xl border border-tfa01-edge bg-tfa01-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa01-accedge has-checked:shadow-[0_18px_40px_-24px_oklch(0.6_0.15_165/0.45)]">
        <input id="tfa01-q4" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa01-q4" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa01-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa01-acc">
          <span>Can I get a refund?</span>
          <i aria-hidden="true" class="relative grid size-7 shrink-0 place-items-center rounded-lg bg-tfa01-code before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa01-acc before:transition-transform before:duration-450 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa01-acc after:rotate-90 after:transition-transform after:duration-450 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14.5px] leading-[1.7] text-tfa01-mut">Every paid plan has a 30-day money-back guarantee, no questions asked. Reply to any invoice email and we refund to the original payment method within 3–5 business days.</p></div>
        </div>
      </div>

      <div class="group/item relative overflow-hidden rounded-2xl border border-tfa01-edge bg-tfa01-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa01-accedge has-checked:shadow-[0_18px_40px_-24px_oklch(0.6_0.15_165/0.45)]">
        <input id="tfa01-q5" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa01-q5" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa01-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa01-acc">
          <span>Is my payment data secure?</span>
          <i aria-hidden="true" class="relative grid size-7 shrink-0 place-items-center rounded-lg bg-tfa01-code before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa01-acc before:transition-transform before:duration-450 before:ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa01-acc after:rotate-90 after:transition-transform after:duration-450 after:ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:before:rotate-180 peer-checked:after:rotate-0 motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14.5px] leading-[1.7] text-tfa01-mut">Card details never touch our servers — payments run through a PCI-DSS Level 1 processor, and your dashboard only ever sees the last four digits. All traffic is TLS 1.3 end to end.</p></div>
        </div>
      </div>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa01-mut">Tab to a question and press <kbd class="rounded-md border border-b-2 border-tfa01-edge bg-tfa01-panel px-1.5 py-0.5 font-tfa01-mono text-[0.9em]">Space</kbd> — the hidden checkbox is a real form control.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa01-bg: #1b1d26;
  --color-tfa01-bg: oklch(0.21 0.02 275);
  --color-tfa01-panel: #23262f;
  --color-tfa01-panel: oklch(0.25 0.022 275);
  --color-tfa01-glow: #1d3a3f;
  --color-tfa01-glow: oklch(0.3 0.05 200 / 0.55);
  --color-tfa01-ink: #f4f5f7;
  --color-tfa01-ink: oklch(0.97 0.004 260);
  --color-tfa01-mut: #b7bcc6;
  --color-tfa01-mut: oklch(0.8 0.012 265);
  --color-tfa01-edge: #3a3e4a;
  --color-tfa01-edge: oklch(0.35 0.022 272);
  --color-tfa01-accedge: #4d8f79;
  --color-tfa01-accedge: oklch(0.6 0.09 165);
  --color-tfa01-code: #2b3a37;
  --color-tfa01-code: oklch(0.32 0.04 165);
  --color-tfa01-acc: #7fe3b8;
  --color-tfa01-acc: oklch(0.85 0.14 165);
  --font-tfa01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa01-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfa-01 {
  width: 100%;
  min-height: 100svh;
}
```
