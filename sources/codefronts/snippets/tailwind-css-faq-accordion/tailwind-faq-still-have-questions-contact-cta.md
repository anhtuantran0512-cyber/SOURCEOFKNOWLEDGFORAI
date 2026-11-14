---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-still-have-questions-contact-cta/"
title: "Tailwind FAQ with a Still Have Questions Contact CTA Card"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The conversion completion of every FAQ: a “Still have questions?” card that catches the users your answers did not — the difference between a dead-end page…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind FAQ with a Still Have Questions Contact CTA Card
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-still-have-questions-contact-cta/

The conversion completion of every FAQ: a “Still have questions?” card that catches the users your answers did not — the difference between a dead-end page and a support funnel. A warm gradient panel with an overlapping avatar group (the real-humans-reply trust signal), a response-time promise, and exactly two actions in clear hierarchy.
## HTML
```html
<section class="tfa-20 w-full min-h-svh grid place-items-center bg-tfa20-bg font-tfa20-sans text-tfa20-ink px-5 py-12">
  <div class="w-[min(660px,100%)]">
    <header>
      <h1 class="text-[clamp(26px,4.6vw,38px)] font-extrabold tracking-[-0.025em]">Frequently asked questions</h1>
      <p class="mt-3 max-w-[50ch] text-[14.5px] leading-relaxed text-tfa20-mut">And for everything we did not think of — real humans, four-hour replies.</p>
    </header>

    <div data-panel class="mt-6 flex flex-col gap-2.5">
      <details class="group rounded-[13px] border border-tfa20-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa20-accedge open:shadow-[0_12px_28px_-20px_oklch(0.6_0.16_50/0.45)]" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa20-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa20-acc [&::-webkit-details-marker]:hidden">Can I try before buying?
          <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa20-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa20-mut">Every plan starts with a 14-day full-featured trial, no card required. Trial workspaces convert in place — nothing to migrate when you subscribe.</p>
      </details>
      <details class="group rounded-[13px] border border-tfa20-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa20-accedge open:shadow-[0_12px_28px_-20px_oklch(0.6_0.16_50/0.45)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa20-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa20-acc [&::-webkit-details-marker]:hidden">How does seat billing work mid-month?
          <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa20-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa20-mut">Added seats are prorated to the day; removed seats credit your next invoice. The billing page shows a live preview of the next charge before you confirm anything.</p>
      </details>
      <details class="group rounded-[13px] border border-tfa20-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa20-accedge open:shadow-[0_12px_28px_-20px_oklch(0.6_0.16_50/0.45)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa20-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa20-acc [&::-webkit-details-marker]:hidden">Do you have an uptime SLA?
          <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa20-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa20-mut">99.9% on Business, 99.99% on Enterprise, both with service credits. The status page keeps five years of incident history public — judge us on it.</p>
      </details>
      <details class="group rounded-[13px] border border-tfa20-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa20-accedge open:shadow-[0_12px_28px_-20px_oklch(0.6_0.16_50/0.45)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa20-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa20-acc [&::-webkit-details-marker]:hidden">Can I export my data?
          <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa20-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa20-mut">Any time, in full: JSON, CSV and attachments via one-click export or the API. Your data is yours — leaving must be easy for staying to mean anything.</p>
      </details>
    </div>

    <aside class="mt-6 rounded-[20px] bg-[linear-gradient(140deg,var(--color-tfa20-ctabg),var(--color-tfa20-ctabg2))] px-6 py-8 text-center text-white shadow-[0_20px_48px_-24px_oklch(0.3_0.06_50/0.5)] sm:px-9">
      <div aria-hidden="true" class="flex justify-center">
        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=200&auto=format&fit=crop" width="44" height="44" alt="" class="size-11 rounded-full border-[3px] border-tfa20-ctabg object-cover -ml-3 first:ml-0">
        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop" width="44" height="44" alt="" class="size-11 rounded-full border-[3px] border-tfa20-ctabg object-cover -ml-3 first:ml-0">
        <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=200&auto=format&fit=crop" width="44" height="44" alt="" class="size-11 rounded-full border-[3px] border-tfa20-ctabg object-cover -ml-3 first:ml-0">
      </div>
      <h2 class="mt-4 text-[clamp(20px,3.2vw,26px)] font-extrabold tracking-[-0.02em]">Still have questions?</h2>
      <p class="mx-auto mt-2 max-w-[42ch] text-[13.5px] leading-[1.6] text-white/85">Our support team replies within 4 hours, every day including weekends.</p>
      <div class="mt-5 flex flex-wrap items-center justify-center gap-3.5">
        <a href="#tfa20-chat" class="inline-flex min-h-[46px] items-center rounded-xl bg-white px-6 text-[14px] font-extrabold text-tfa20-ctabg no-underline transition-[translate,box-shadow] duration-200 hover:-translate-y-0.5 hover:shadow-[0_10px_24px_oklch(0.1_0.03_50/0.4)] focus-visible:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-white motion-reduce:transition-none motion-reduce:hover:translate-y-0">Chat with us</a>
        <a href="mailto:[email protected]" class="inline-flex min-h-11 items-center text-[13.5px] font-semibold text-white/90 underline underline-offset-4 transition-colors duration-200 hover:text-white focus-visible:rounded-md focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-white">[email protected]</a>
      </div>
    </aside>

    <p class="mt-5 text-[12.5px] text-tfa20-mut">The CTA sits after the list on purpose — it catches users at the exact moment the answers ran out.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa20-bg: #fcfaf7;
  --color-tfa20-bg: oklch(0.98 0.008 75);
  --color-tfa20-ink: #33291f;
  --color-tfa20-ink: oklch(0.25 0.025 55);
  --color-tfa20-mut: #6b5c4e;
  --color-tfa20-mut: oklch(0.47 0.025 55);
  --color-tfa20-edge: #e7e0d6;
  --color-tfa20-edge: oklch(0.9 0.015 70);
  --color-tfa20-accedge: #d99b6a;
  --color-tfa20-accedge: oklch(0.74 0.09 55);
  --color-tfa20-acc: #a8541b;
  --color-tfa20-acc: oklch(0.52 0.15 50);
  --color-tfa20-ctabg: #2d2318;
  --color-tfa20-ctabg: oklch(0.25 0.04 55);
  --color-tfa20-ctabg2: #4a3220;
  --color-tfa20-ctabg2: oklch(0.34 0.07 52);
  --font-tfa20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tfa-20 {
  width: 100%;
  min-height: 100svh;
}

.tfa-20 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-20 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .tfa-20 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-20 details::details-content {
    transition-duration: 1ms;
  }
}
```
