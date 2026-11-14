---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-exclusive-accordion-only-one-faq-open/"
title: "Tailwind Exclusive Accordion — Only One FAQ Open at a Time"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "Only-one-open used to mean JavaScript closing siblings; now it is one HTML attribute."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Exclusive Accordion — Only One FAQ Open at a Time
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-exclusive-accordion-only-one-faq-open/

Only-one-open used to mean JavaScript closing siblings; now it is one HTML attribute. Give every <details> the same name and the browser enforces exclusivity like radio buttons. The port's contribution is the attention choreography: has-[details[open]]: on the list dims the closed questions, which is :has() written where you can see it.
## HTML
```html
<section class="tfa-03 w-full min-h-svh grid place-items-center bg-tfa03-bg font-tfa03-sans text-tfa03-ink px-5 py-12 bg-[linear-gradient(180deg,var(--color-tfa03-wash),var(--color-tfa03-bg)_42%)]">
  <div class="w-[min(680px,100%)]">
    <header>
      <span class="inline-block rounded-full bg-tfa03-tint px-3 py-1.5 font-tfa03-mono text-[11.5px] font-semibold text-tfa03-acc">name="faq" · zero-JS exclusivity</span>
      <h1 class="mt-4 text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Pricing questions, answered</h1>
      <p class="mt-3 max-w-[54ch] text-[15px] leading-relaxed text-tfa03-mut">Open any question — the browser closes the previous one. One attribute, no JavaScript.</p>
    </header>

    <div data-panel class="mt-8 flex flex-col gap-2.5 has-[details[open]]:[&>details:not([open])]:opacity-70">
      <details name="tfa03-faq" class="group relative overflow-hidden rounded-2xl border border-tfa03-edge bg-white transition-[border-color,box-shadow,opacity] duration-300 open:border-tfa03-accedge open:shadow-[0_14px_34px_-18px_oklch(0.45_0.14_275/0.35)]" open>
        <span aria-hidden="true" class="absolute inset-y-0 left-0 w-[3px] origin-top scale-y-0 bg-tfa03-acc transition-transform duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-open:scale-y-100 motion-reduce:transition-none"></span>
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3.5 px-5 py-4 text-[15.5px] font-semibold transition-colors duration-200 hover:text-tfa03-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa03-acc [&::-webkit-details-marker]:hidden">
          <span class="font-tfa03-mono text-[11px] font-bold text-tfa03-acc">01</span>Is there a free plan?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa03-mut transition-[rotate,translate,border-color] duration-350 group-hover:border-tfa03-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa03-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[58ch] pb-4 pl-12 pr-5 text-[14.5px] leading-[1.7] text-tfa03-mut">Yes — free forever for up to 3 projects and 2 seats, with no card required. It is a real plan, not a trial: teams ship production work on it every day.</p>
      </details>

      <details name="tfa03-faq" class="group relative overflow-hidden rounded-2xl border border-tfa03-edge bg-white transition-[border-color,box-shadow,opacity] duration-300 open:border-tfa03-accedge open:shadow-[0_14px_34px_-18px_oklch(0.45_0.14_275/0.35)]">
        <span aria-hidden="true" class="absolute inset-y-0 left-0 w-[3px] origin-top scale-y-0 bg-tfa03-acc transition-transform duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-open:scale-y-100 motion-reduce:transition-none"></span>
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3.5 px-5 py-4 text-[15.5px] font-semibold transition-colors duration-200 hover:text-tfa03-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa03-acc [&::-webkit-details-marker]:hidden">
          <span class="font-tfa03-mono text-[11px] font-bold text-tfa03-acc">02</span>What counts as a “seat”?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa03-mut transition-[rotate,translate,border-color] duration-350 group-hover:border-tfa03-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa03-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[58ch] pb-4 pl-12 pr-5 text-[14.5px] leading-[1.7] text-tfa03-mut">Anyone who can edit. Viewers and commenters are unlimited and free on every plan — you only pay for people who change things.</p>
      </details>

      <details name="tfa03-faq" class="group relative overflow-hidden rounded-2xl border border-tfa03-edge bg-white transition-[border-color,box-shadow,opacity] duration-300 open:border-tfa03-accedge open:shadow-[0_14px_34px_-18px_oklch(0.45_0.14_275/0.35)]">
        <span aria-hidden="true" class="absolute inset-y-0 left-0 w-[3px] origin-top scale-y-0 bg-tfa03-acc transition-transform duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-open:scale-y-100 motion-reduce:transition-none"></span>
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3.5 px-5 py-4 text-[15.5px] font-semibold transition-colors duration-200 hover:text-tfa03-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa03-acc [&::-webkit-details-marker]:hidden">
          <span class="font-tfa03-mono text-[11px] font-bold text-tfa03-acc">03</span>Do prices include tax?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa03-mut transition-[rotate,translate,border-color] duration-350 group-hover:border-tfa03-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa03-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[58ch] pb-4 pl-12 pr-5 text-[14.5px] leading-[1.7] text-tfa03-mut">Prices are shown pre-tax; VAT/GST is added at checkout based on your billing country. US customers see applicable state sales tax, and every invoice is compliant for expensing.</p>
      </details>

      <details name="tfa03-faq" class="group relative overflow-hidden rounded-2xl border border-tfa03-edge bg-white transition-[border-color,box-shadow,opacity] duration-300 open:border-tfa03-accedge open:shadow-[0_14px_34px_-18px_oklch(0.45_0.14_275/0.35)]">
        <span aria-hidden="true" class="absolute inset-y-0 left-0 w-[3px] origin-top scale-y-0 bg-tfa03-acc transition-transform duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-open:scale-y-100 motion-reduce:transition-none"></span>
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3.5 px-5 py-4 text-[15.5px] font-semibold transition-colors duration-200 hover:text-tfa03-acc focus-visible:rounded-2xl focus-visible:-outline-offset-2 focus-visible:outline-2 focus-visible:outline-tfa03-acc [&::-webkit-details-marker]:hidden">
          <span class="font-tfa03-mono text-[11px] font-bold text-tfa03-acc">04</span>Can I pay by invoice?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa03-mut transition-[rotate,translate,border-color] duration-350 group-hover:border-tfa03-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa03-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[58ch] pb-4 pl-12 pr-5 text-[14.5px] leading-[1.7] text-tfa03-mut">Annual plans over $2,000 can be paid by bank transfer with NET-30 terms. Contact sales and we will set up procurement, security review and a countersigned DPA if you need one.</p>
      </details>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa03-mut">Closed questions dim via <code class="rounded bg-tfa03-tint px-1.5 py-0.5 font-tfa03-mono text-[0.88em] text-tfa03-acc">has-[details[open]]:</code> — attention follows the open panel.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa03-bg: #fafafd;
  --color-tfa03-bg: oklch(0.98 0.005 270);
  --color-tfa03-wash: #eeecfb;
  --color-tfa03-wash: oklch(0.94 0.025 275);
  --color-tfa03-ink: #1f1d2b;
  --color-tfa03-ink: oklch(0.22 0.03 275);
  --color-tfa03-mut: #5c5a6e;
  --color-tfa03-mut: oklch(0.48 0.025 275);
  --color-tfa03-edge: #e3e1ee;
  --color-tfa03-edge: oklch(0.91 0.012 275);
  --color-tfa03-accedge: #9b8ce0;
  --color-tfa03-accedge: oklch(0.72 0.1 285);
  --color-tfa03-tint: #eeebfd;
  --color-tfa03-tint: oklch(0.94 0.03 285);
  --color-tfa03-acc: #5b3fd0;
  --color-tfa03-acc: oklch(0.47 0.2 285);
  --font-tfa03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa03-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-03 {
  width: 100%;
  min-height: 100svh;
}
/* Same irreducible four lines as demo 02 — the animated panel, once, for the whole list. */

.tfa-03 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-03 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .38s allow-discrete;
  }

  .tfa-03 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-03 details::details-content {
    transition-duration: 1ms;
  }
}
```
