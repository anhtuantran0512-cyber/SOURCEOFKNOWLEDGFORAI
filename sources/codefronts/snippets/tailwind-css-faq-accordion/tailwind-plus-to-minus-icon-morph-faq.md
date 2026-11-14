---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-plus-to-minus-icon-morph-faq/"
title: "Tailwind Animated Plus to Minus Icon Morph FAQ Accordion"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The +/− morph elevated from “the vertical bar fades out” to choreography: both bars rotate a half-turn together while the vertical one collapses along its…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Plus to Minus Icon Morph FAQ Accordion
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-plus-to-minus-icon-morph-faq/

The +/− morph elevated from “the vertical bar fades out” to choreography: both bars rotate a half-turn together while the vertical one collapses along its own length, so the glyph appears to twist itself into a minus. Two before:/after: bars, no SVG, no icon font — and Tailwind's pseudo-element variants make the whole thing a class list.
## HTML
```html
<section class="tfa-12 w-full min-h-svh grid place-items-center bg-tfa12-bg font-tfa12-sans text-tfa12-ink px-5 py-12 bg-[radial-gradient(900px_600px_at_0%_0%,var(--color-tfa12-glow),transparent_55%)]">
  <div class="w-[min(660px,100%)]">
    <header>
      <h1 class="text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Studio FAQ</h1>
      <p class="mt-3 max-w-[54ch] text-[15px] leading-relaxed text-tfa12-mut">Watch the plus twist itself into a minus — both bars rotate, one collapses along its length.</p>
    </header>

    <div class="mt-8 flex flex-col gap-2.5">
      <div class="relative overflow-hidden rounded-2xl border border-tfa12-edge bg-tfa12-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa12-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.85_0.17_130/0.45)]">
        <input id="tfa12-q1" type="checkbox" class="peer absolute opacity-0 pointer-events-none" checked>
        <label for="tfa12-q1" class="group/row flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa12-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa12-acc">Do you take on freelance projects?
          <i aria-hidden="true" class="relative grid size-[26px] shrink-0 place-items-center rounded-[9px] bg-tfa12-tint text-tfa12-mut transition-[scale,color] duration-250 group-hover/row:scale-110 group-hover/row:text-tfa12-acc peer-checked:text-tfa12-acc before:absolute before:h-0.5 before:w-3.5 before:rounded-full before:bg-current before:transition-[rotate,scale] before:duration-450 before:ease-[cubic-bezier(0.5,-0.3,0.3,1.3)] after:absolute after:h-0.5 after:w-3.5 after:rounded-full after:bg-current after:rotate-90 after:transition-[rotate,scale] after:duration-450 after:ease-[cubic-bezier(0.5,-0.3,0.3,1.3)] peer-checked:before:rotate-180 peer-checked:after:rotate-180 peer-checked:after:scale-x-0 motion-reduce:before:transition-none motion-reduce:after:transition-none motion-reduce:transition-colors"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa12-mut">Selectively — two or three a quarter, usually brand systems or product design sprints. Send a short brief with timeline and budget range; we reply within two business days either way.</p></div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-2xl border border-tfa12-edge bg-tfa12-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa12-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.85_0.17_130/0.45)]">
        <input id="tfa12-q2" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa12-q2" class="group/row flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa12-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa12-acc">What does a typical engagement cost?
          <i aria-hidden="true" class="relative grid size-[26px] shrink-0 place-items-center rounded-[9px] bg-tfa12-tint text-tfa12-mut transition-[scale,color] duration-250 group-hover/row:scale-110 group-hover/row:text-tfa12-acc peer-checked:text-tfa12-acc before:absolute before:h-0.5 before:w-3.5 before:rounded-full before:bg-current before:transition-[rotate,scale] before:duration-450 before:ease-[cubic-bezier(0.5,-0.3,0.3,1.3)] after:absolute after:h-0.5 after:w-3.5 after:rounded-full after:bg-current after:rotate-90 after:transition-[rotate,scale] after:duration-450 after:ease-[cubic-bezier(0.5,-0.3,0.3,1.3)] peer-checked:before:rotate-180 peer-checked:after:rotate-180 peer-checked:after:scale-x-0 motion-reduce:before:transition-none motion-reduce:after:transition-none motion-reduce:transition-colors"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa12-mut">Sprints start at $12k for two weeks; full brand systems run $40–90k depending on scope. Fixed-price after discovery — we do not bill hours, so a slow Tuesday is our problem, not yours.</p></div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-2xl border border-tfa12-edge bg-tfa12-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa12-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.85_0.17_130/0.45)]">
        <input id="tfa12-q3" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa12-q3" class="group/row flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa12-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa12-acc">Can we hire you to work inside our team?
          <i aria-hidden="true" class="relative grid size-[26px] shrink-0 place-items-center rounded-[9px] bg-tfa12-tint text-tfa12-mut transition-[scale,color] duration-250 group-hover/row:scale-110 group-hover/row:text-tfa12-acc peer-checked:text-tfa12-acc before:absolute before:h-0.5 before:w-3.5 before:rounded-full before:bg-current before:transition-[rotate,scale] before:duration-450 before:ease-[cubic-bezier(0.5,-0.3,0.3,1.3)] after:absolute after:h-0.5 after:w-3.5 after:rounded-full after:bg-current after:rotate-90 after:transition-[rotate,scale] after:duration-450 after:ease-[cubic-bezier(0.5,-0.3,0.3,1.3)] peer-checked:before:rotate-180 peer-checked:after:rotate-180 peer-checked:after:scale-x-0 motion-reduce:before:transition-none motion-reduce:after:transition-none motion-reduce:transition-colors"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa12-mut">Yes — embedded engagements of 1–3 months, joining your standups and shipping in your codebase or design system. It is the fastest way to transfer taste, not just deliverables.</p></div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-2xl border border-tfa12-edge bg-tfa12-panel transition-[border-color,box-shadow] duration-300 has-checked:border-tfa12-accedge has-checked:shadow-[0_16px_38px_-24px_oklch(0.85_0.17_130/0.45)]">
        <input id="tfa12-q4" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa12-q4" class="group/row flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-2xl px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa12-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa12-acc">Who owns the work?
          <i aria-hidden="true" class="relative grid size-[26px] shrink-0 place-items-center rounded-[9px] bg-tfa12-tint text-tfa12-mut transition-[scale,color] duration-250 group-hover/row:scale-110 group-hover/row:text-tfa12-acc peer-checked:text-tfa12-acc before:absolute before:h-0.5 before:w-3.5 before:rounded-full before:bg-current before:transition-[rotate,scale] before:duration-450 before:ease-[cubic-bezier(0.5,-0.3,0.3,1.3)] after:absolute after:h-0.5 after:w-3.5 after:rounded-full after:bg-current after:rotate-90 after:transition-[rotate,scale] after:duration-450 after:ease-[cubic-bezier(0.5,-0.3,0.3,1.3)] peer-checked:before:rotate-180 peer-checked:after:rotate-180 peer-checked:after:scale-x-0 motion-reduce:before:transition-none motion-reduce:after:transition-none motion-reduce:transition-colors"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa12-mut">You do, fully, on final payment — source files, fonts we licensed for you, the lot. We keep the right to show the work in our portfolio unless the contract says otherwise.</p></div>
        </div>
      </div>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa12-mut">The morph: both bars to 180°, the vertical one to <code class="rounded bg-tfa12-tint px-1.5 py-0.5 font-tfa12-mono text-[0.88em] text-tfa12-acc">scale-x-0</code>, on one overshoot curve.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa12-bg: #1e2620;
  --color-tfa12-bg: oklch(0.24 0.03 145);
  --color-tfa12-panel: #26302a;
  --color-tfa12-panel: oklch(0.28 0.035 148);
  --color-tfa12-glow: #2a3a26;
  --color-tfa12-glow: oklch(0.3 0.06 130 / 0.6);
  --color-tfa12-ink: #f2f7f0;
  --color-tfa12-ink: oklch(0.96 0.01 140);
  --color-tfa12-mut: #bcc7b9;
  --color-tfa12-mut: oklch(0.81 0.022 142);
  --color-tfa12-edge: #3b473c;
  --color-tfa12-edge: oklch(0.37 0.04 146);
  --color-tfa12-accedge: #6c9a55;
  --color-tfa12-accedge: oklch(0.62 0.11 130);
  --color-tfa12-tint: #30412b;
  --color-tfa12-tint: oklch(0.33 0.055 130);
  --color-tfa12-acc: #b9ec7f;
  --color-tfa12-acc: oklch(0.87 0.16 130);
  --font-tfa12-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa12-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-12 {
  width: 100%;
  min-height: 100svh;
}
```
