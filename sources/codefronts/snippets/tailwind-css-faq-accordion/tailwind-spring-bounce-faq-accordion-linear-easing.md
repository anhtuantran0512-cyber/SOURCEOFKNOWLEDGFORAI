---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-spring-bounce-faq-accordion-linear-easing/"
title: "Tailwind Spring Bounce FAQ Accordion with linear() Easing"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "Spring physics without a physics engine: linear() plays back a real damped-spring curve — overshoot, wobble, settle — and in v4 it becomes a utility the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Spring Bounce FAQ Accordion with linear() Easing
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-spring-bounce-faq-accordion-linear-easing/

Spring physics without a physics engine: linear() plays back a real damped-spring curve — overshoot, wobble, settle — and in v4 it becomes a utility the moment you name it --ease-tfa13-spring in @theme. Panels bounce open like they have mass, the icon over-rotates and recoils, and closing stays deliberately calm.
## HTML
```html
<section class="tfa-13 w-full min-h-svh grid place-items-center bg-tfa13-bg font-tfa13-sans text-tfa13-ink px-5 py-12 bg-[radial-gradient(800px_500px_at_90%_10%,var(--color-tfa13-glow),transparent_60%)]">
  <div class="w-[min(680px,100%)]">
    <header>
      <span class="inline-block rounded-full bg-tfa13-tint px-3.5 py-1.5 font-tfa13-mono text-[11.5px] font-semibold text-tfa13-acc">ease-tfa13-spring · linear(…)</span>
      <h1 class="mt-4 text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Panels with mass</h1>
      <p class="mt-3 max-w-[54ch] text-[15px] leading-relaxed text-tfa13-mut">A real damped-spring curve, sampled into CSS and named as a utility. Open = bounce. Close = calm, on purpose.</p>
    </header>

    <div class="mt-8 flex flex-col gap-2.5">
      <div class="relative overflow-hidden rounded-[15px] border border-tfa13-edge bg-white shadow-[0_3px_12px_oklch(0.4_0.06_40/0.06)] transition-[border-color,box-shadow] duration-300 has-checked:border-tfa13-accedge has-checked:shadow-[0_16px_36px_-22px_oklch(0.62_0.19_35/0.4)]">
        <input id="tfa13-q1" type="checkbox" class="peer absolute opacity-0 pointer-events-none" checked>
        <label for="tfa13-q1" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-[15px] px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa13-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa13-acc">What makes this a “spring”, not just easing?
          <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center rounded-lg bg-tfa13-tint before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa13-acc before:transition-[rotate] before:duration-350 before:ease-out after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa13-acc after:rotate-90 after:transition-[rotate,scale] after:duration-350 after:ease-out peer-checked:before:rotate-180 peer-checked:before:duration-800 peer-checked:before:ease-tfa13-spring peer-checked:after:rotate-180 peer-checked:after:scale-x-0 peer-checked:after:duration-800 peer-checked:after:ease-tfa13-spring motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out peer-checked:grid-rows-[1fr] peer-checked:duration-800 peer-checked:ease-tfa13-spring motion-reduce:transition-none motion-reduce:peer-checked:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa13-mut">The curve crosses its target more than once. This panel opens about 16% past its height, recoils, overshoots a little again, and settles — three crossings. A cubic-bezier manages one. That multi-crossing wobble is what your brain reads as mass and tension.</p></div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-[15px] border border-tfa13-edge bg-white shadow-[0_3px_12px_oklch(0.4_0.06_40/0.06)] transition-[border-color,box-shadow] duration-300 has-checked:border-tfa13-accedge has-checked:shadow-[0_16px_36px_-22px_oklch(0.62_0.19_35/0.4)]">
        <input id="tfa13-q2" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa13-q2" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-[15px] px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa13-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa13-acc">Why does it not bounce when closing?
          <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center rounded-lg bg-tfa13-tint before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa13-acc before:transition-[rotate] before:duration-350 before:ease-out after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa13-acc after:rotate-90 after:transition-[rotate,scale] after:duration-350 after:ease-out peer-checked:before:rotate-180 peer-checked:before:duration-800 peer-checked:before:ease-tfa13-spring peer-checked:after:rotate-180 peer-checked:after:scale-x-0 peer-checked:after:duration-800 peer-checked:after:ease-tfa13-spring motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out peer-checked:grid-rows-[1fr] peer-checked:duration-800 peer-checked:ease-tfa13-spring motion-reduce:transition-none motion-reduce:peer-checked:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa13-mut">Deliberate asymmetry. A wobbly close feels like the UI resisting you. The base classes carry a calm 350ms ease-out, and <code class="rounded bg-tfa13-tint px-1.5 py-0.5 font-tfa13-mono text-[0.88em] text-tfa13-acc">peer-checked:</code> overrides duration and easing for the open direction only.</p></div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-[15px] border border-tfa13-edge bg-white shadow-[0_3px_12px_oklch(0.4_0.06_40/0.06)] transition-[border-color,box-shadow] duration-300 has-checked:border-tfa13-accedge has-checked:shadow-[0_16px_36px_-22px_oklch(0.62_0.19_35/0.4)]">
        <input id="tfa13-q3" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa13-q3" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-[15px] px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa13-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa13-acc">How do I make my own curve?
          <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center rounded-lg bg-tfa13-tint before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa13-acc before:transition-[rotate] before:duration-350 before:ease-out after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa13-acc after:rotate-90 after:transition-[rotate,scale] after:duration-350 after:ease-out peer-checked:before:rotate-180 peer-checked:before:duration-800 peer-checked:before:ease-tfa13-spring peer-checked:after:rotate-180 peer-checked:after:scale-x-0 peer-checked:after:duration-800 peer-checked:after:ease-tfa13-spring motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out peer-checked:grid-rows-[1fr] peer-checked:duration-800 peer-checked:ease-tfa13-spring motion-reduce:transition-none motion-reduce:peer-checked:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa13-mut">Use a linear() generator: set mass, stiffness and damping, and it exports the sampled point list. Damping near 0.4 is cartoon, 0.55 (this demo) is playful-professional, 0.8 is barely-there luxury. Then name it in <code class="rounded bg-tfa13-tint px-1.5 py-0.5 font-tfa13-mono text-[0.88em] text-tfa13-acc">@theme</code> and it is a utility.</p></div>
        </div>
      </div>
      <div class="relative overflow-hidden rounded-[15px] border border-tfa13-edge bg-white shadow-[0_3px_12px_oklch(0.4_0.06_40/0.06)] transition-[border-color,box-shadow] duration-300 has-checked:border-tfa13-accedge has-checked:shadow-[0_16px_36px_-22px_oklch(0.62_0.19_35/0.4)]">
        <input id="tfa13-q4" type="checkbox" class="peer absolute opacity-0 pointer-events-none">
        <label for="tfa13-q4" class="flex min-h-11 cursor-pointer select-none items-center justify-between gap-4 rounded-[15px] px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa13-acc peer-focus-visible:outline-2 peer-focus-visible:-outline-offset-2 peer-focus-visible:outline-tfa13-acc">Where should springs never be used?
          <i aria-hidden="true" class="relative grid size-6 shrink-0 place-items-center rounded-lg bg-tfa13-tint before:absolute before:h-0.5 before:w-3 before:rounded-full before:bg-tfa13-acc before:transition-[rotate] before:duration-350 before:ease-out after:absolute after:h-0.5 after:w-3 after:rounded-full after:bg-tfa13-acc after:rotate-90 after:transition-[rotate,scale] after:duration-350 after:ease-out peer-checked:before:rotate-180 peer-checked:before:duration-800 peer-checked:before:ease-tfa13-spring peer-checked:after:rotate-180 peer-checked:after:scale-x-0 peer-checked:after:duration-800 peer-checked:after:ease-tfa13-spring motion-reduce:before:transition-none motion-reduce:after:transition-none"></i>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out peer-checked:grid-rows-[1fr] peer-checked:duration-800 peer-checked:ease-tfa13-spring motion-reduce:transition-none motion-reduce:peer-checked:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa13-mut">Anywhere a user is about to click: the overshoot moves buttons under the cursor. And under reduced motion — a spring is precisely the vestibular trigger that setting exists for, so both directions drop to no transition.</p></div>
        </div>
      </div>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa13-mut">Open: 800ms sampled spring · Close: 350ms ease-out · Fallback: one-overshoot bezier.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa13-bg: #fbf5ef;
  --color-tfa13-bg: oklch(0.97 0.015 60);
  --color-tfa13-glow: #f6e0cf;
  --color-tfa13-glow: oklch(0.93 0.05 45 / 0.7);
  --color-tfa13-ink: #3a2a22;
  --color-tfa13-ink: oklch(0.25 0.03 40);
  --color-tfa13-mut: #6e5a50;
  --color-tfa13-mut: oklch(0.47 0.03 45);
  --color-tfa13-edge: #e8ddd2;
  --color-tfa13-edge: oklch(0.89 0.02 55);
  --color-tfa13-accedge: #dd9a7a;
  --color-tfa13-accedge: oklch(0.75 0.09 40);
  --color-tfa13-tint: #fbe7dc;
  --color-tfa13-tint: oklch(0.93 0.035 45);
  --color-tfa13-acc: #b5471f;
  --color-tfa13-acc: oklch(0.55 0.19 35);
  --font-tfa13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa13-mono: 'JetBrains Mono', ui-monospace, monospace;
  /* The whole point of this demo: an easing entry in @theme mints ease-tfa13-spring. */
  --ease-tfa13-spring: linear(0,0.009,0.035 2.1%,0.141 4.4%,0.723 12.9%,0.938,1.077 20.4%,1.121,1.149 24.3%,1.159,1.163 27%,1.154,1.129 32.8%,1.051 39.6%,1.017 43.1%,0.991,0.977 51%,0.974 53.8%,0.975 57.1%,0.997 69.8%,1.003 76.9%,1);
}

.tfa-13 {
  width: 100%;
  min-height: 100svh;
}
/* Single-overshoot fallback where linear() is unsupported — graceful, not broken. */

@supports not (transition-timing-function: linear(0, 1)) {
  .tfa-13 .peer:checked ~ * {
    transition-timing-function: cubic-bezier(.34,1.56,.64,1) !important;
    transition-duration: .5s !important;
  }
}
```
