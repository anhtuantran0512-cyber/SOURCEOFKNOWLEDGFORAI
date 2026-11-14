---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-faqpage-json-ld-rich-snippet/"
title: "Tailwind FAQ with FAQPage JSON-LD Schema for Rich Snippets and AI Search"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "A FAQ wearing its structured data: the visible accordion is mirrored 1:1 by a FAQPage JSON-LD block in the same component, making answers parseable by search…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind FAQ with FAQPage JSON-LD Schema for Rich Snippets and AI Search
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-faqpage-json-ld-rich-snippet/

A FAQ wearing its structured data: the visible accordion is mirrored 1:1 by a FAQPage JSON-LD block in the same component, making answers parseable by search engines and — increasingly the point — by AI answer engines. Includes a mock SERP preview of the rich result, and the eligibility reality check for 2026.
## HTML
```html
<section class="tfa-22 w-full min-h-svh grid place-items-center bg-tfa22-bg font-tfa22-sans text-tfa22-ink px-5 py-12">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {"@type":"Question","name":"How long does shipping take?","acceptedAnswer":{"@type":"Answer","text":"Standard shipping takes 3-5 business days in the US, UK, Canada and Australia. Express 1-2 day options are available at checkout."}},
      {"@type":"Question","name":"What is your return policy?","acceptedAnswer":{"@type":"Answer","text":"Returns are free for 60 days from delivery. Start a return from your order email; refunds process within 3-5 days of the carrier scan."}},
      {"@type":"Question","name":"Do you ship internationally?","acceptedAnswer":{"@type":"Answer","text":"Yes, to 40+ countries with duties calculated at checkout, so there are no surprise fees at the door."}},
      {"@type":"Question","name":"How can I track my order?","acceptedAnswer":{"@type":"Answer","text":"Every order emails a tracked link at dispatch, and live status appears on your account orders page."}}
    ]
  }
  </script>

  <div class="w-[min(680px,100%)]">
    <header>
      <span class="inline-block rounded-full bg-tfa22-tint px-3.5 py-1.5 font-tfa22-mono text-[11.5px] font-semibold text-tfa22-acc">&lt;script type="application/ld+json"&gt;</span>
      <h1 class="mt-4 text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Machine-readable FAQ</h1>
      <p class="mt-3 max-w-[56ch] text-[15px] leading-relaxed text-tfa22-mut">The accordion below is mirrored 1:1 in a FAQPage JSON-LD block — same four answers, one set for humans, one for crawlers and AI engines.</p>
    </header>

    <div role="img" aria-label="Mock search result showing a FAQ rich snippet" class="mt-6 rounded-[14px] border border-tfa22-edge bg-white px-5 py-4">
      <div class="font-tfa22-sans text-[12px] text-[oklch(0.45_0.02_150)]">example.com › help › shipping</div>
      <div class="mt-1 text-[18px] font-semibold text-[oklch(0.42_0.16_265)]">Shipping &amp; Returns FAQ — Example Store</div>
      <div class="mt-1 text-[13px] leading-[1.5] text-[oklch(0.35_0.01_260)]">Answers about delivery times, returns, international shipping and order tracking.</div>
      <div class="mt-2.5 divide-y divide-[oklch(0.9_0.005_260)] border-t border-[oklch(0.9_0.005_260)]">
        <div class="flex items-center justify-between py-2 text-[13px] text-[oklch(0.35_0.01_260)]">How long does shipping take?<b class="text-[oklch(0.55_0.01_260)]">⌄</b></div>
        <div class="flex items-center justify-between py-2 text-[13px] text-[oklch(0.35_0.01_260)]">What is your return policy?<b class="text-[oklch(0.55_0.01_260)]">⌄</b></div>
      </div>
      <span class="mt-2.5 block font-tfa22-mono text-[10.5px] text-[oklch(0.5_0.02_150)]">what the rich result renders, where eligible</span>
    </div>

    <div data-panel class="mt-5 flex flex-col gap-2.5">
      <details class="group rounded-[13px] border border-tfa22-edge bg-tfa22-panel transition-[border-color,box-shadow] duration-300 open:border-tfa22-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_150/0.4)]" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa22-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa22-acc [&::-webkit-details-marker]:hidden">How long does shipping take?
          <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa22-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa22-mut">Standard shipping takes 3–5 business days in the US, UK, Canada and Australia. Express 1–2 day options are available at checkout.</p>
      </details>
      <details class="group rounded-[13px] border border-tfa22-edge bg-tfa22-panel transition-[border-color,box-shadow] duration-300 open:border-tfa22-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_150/0.4)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa22-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa22-acc [&::-webkit-details-marker]:hidden">What is your return policy?
          <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa22-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa22-mut">Returns are free for 60 days from delivery. Start a return from your order email; refunds process within 3–5 days of the carrier scan.</p>
      </details>
      <details class="group rounded-[13px] border border-tfa22-edge bg-tfa22-panel transition-[border-color,box-shadow] duration-300 open:border-tfa22-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_150/0.4)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa22-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa22-acc [&::-webkit-details-marker]:hidden">Do you ship internationally?
          <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa22-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa22-mut">Yes — to 40+ countries with duties calculated at checkout, so there are no surprise fees at the door.</p>
      </details>
      <details class="group rounded-[13px] border border-tfa22-edge bg-tfa22-panel transition-[border-color,box-shadow] duration-300 open:border-tfa22-accedge open:shadow-[0_12px_30px_-20px_oklch(0.8_0.14_150/0.4)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa22-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa22-acc [&::-webkit-details-marker]:hidden">How can I track my order?
          <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa22-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa22-mut">Every order emails a tracked link at dispatch, and live status appears on your account's orders page.</p>
      </details>
    </div>

    <p class="mt-5 text-[12.5px] text-tfa22-mut">One FAQPage block per page, answers matching the visible text — the two rules with penalties attached.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa22-bg: #171d1a;
  --color-tfa22-bg: oklch(0.21 0.018 150);
  --color-tfa22-panel: #1f2723;
  --color-tfa22-panel: oklch(0.25 0.022 150);
  --color-tfa22-ink: #f0f5f2;
  --color-tfa22-ink: oklch(0.96 0.008 150);
  --color-tfa22-mut: #b3c0b8;
  --color-tfa22-mut: oklch(0.79 0.016 150);
  --color-tfa22-edge: #343f39;
  --color-tfa22-edge: oklch(0.34 0.025 150);
  --color-tfa22-accedge: #4d9070;
  --color-tfa22-accedge: oklch(0.6 0.09 150);
  --color-tfa22-tint: #23392e;
  --color-tfa22-tint: oklch(0.29 0.045 150);
  --color-tfa22-acc: #7fe0ac;
  --color-tfa22-acc: oklch(0.85 0.13 150);
  --font-tfa22-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa22-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-22 {
  width: 100%;
  min-height: 100svh;
}

.tfa-22 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-22 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .tfa-22 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-22 details::details-content {
    transition-duration: 1ms;
  }
}
```
