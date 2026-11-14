---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-minimalist-ecommerce-faq-accordion/"
title: "Tailwind Minimalist E-Commerce FAQ Accordion for Product Pages"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The product-page FAQ that converts: shipping, returns and care answers in a bone-white, hairline-divided accordion beside the product photo — the layout…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist E-Commerce FAQ Accordion for Product Pages
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-minimalist-ecommerce-faq-accordion/

The product-page FAQ that converts: shipping, returns and care answers in a bone-white, hairline-divided accordion beside the product photo — the layout premium DTC brands and every good Shopify theme use. The port's real gain is the breakpoint: @container plus @3xl: variants mean the FAQ reflows when the component is narrow, in a theme sidebar or a modal, not when the viewport says so.
## HTML
```html
<section class="tfa-08 w-full min-h-svh font-tfa08-sans text-tfa08-ink">
  <div class="@container grid min-h-svh w-full place-items-center bg-tfa08-bg px-5 py-12">
    <div class="grid w-[min(980px,100%)] items-center gap-8 @3xl:grid-cols-[minmax(0,5fr)_minmax(0,6fr)] @3xl:gap-16">
      <figure class="flex aspect-[16/10] max-h-[340px] items-end bg-[linear-gradient(oklch(0.9_0.01_80/0.1),oklch(0.85_0.015_70/0.2)),url('https://images.unsplash.com/photo-1523381210434-271e8be1f52b?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center @3xl:aspect-[4/5] @3xl:max-h-none">
        <figcaption class="w-full bg-[linear-gradient(transparent,oklch(0.2_0.01_60/0.55))] px-4 py-3.5 text-[12px] uppercase tracking-[0.08em] text-white">Heavyweight organic tee — $48</figcaption>
      </figure>

      <div>
        <h1 class="text-[clamp(22px,3.4vw,30px)] font-semibold tracking-[-0.02em]">Details &amp; care</h1>
        <div data-panel class="mt-5 border-t border-tfa08-line">
          <details class="group border-b border-tfa08-line" open>
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-0.5 py-[22px] text-[14px] font-semibold uppercase tracking-[0.06em] transition-colors duration-200 hover:text-tfa08-acc focus-visible:outline-[1.5px] focus-visible:outline-offset-4 focus-visible:outline-tfa08-acc [&::-webkit-details-marker]:hidden">Shipping &amp; delivery
              <i aria-hidden="true" class="relative size-3.5 shrink-0 before:absolute before:inset-0 before:m-auto before:h-px before:w-3.5 before:bg-current after:absolute after:inset-0 after:m-auto after:h-px after:w-3.5 after:rotate-90 after:bg-current after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] group-open:after:rotate-0 motion-reduce:after:transition-none"></i>
            </summary>
            <p class="max-w-[52ch] px-0.5 pb-[22px] text-[13.5px] leading-[1.8] text-tfa08-mut transition-[translate,opacity] duration-350 group-[&:not([open])]:translate-y-1">Free carbon-neutral shipping over $75, dispatched within 24 hours. US 2–4 business days, UK &amp; EU 3–5, Australia 4–7. A tracked link lands in your inbox at dispatch.</p>
          </details>
          <details class="group border-b border-tfa08-line">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-0.5 py-[22px] text-[14px] font-semibold uppercase tracking-[0.06em] transition-colors duration-200 hover:text-tfa08-acc focus-visible:outline-[1.5px] focus-visible:outline-offset-4 focus-visible:outline-tfa08-acc [&::-webkit-details-marker]:hidden">Returns &amp; exchanges
              <i aria-hidden="true" class="relative size-3.5 shrink-0 before:absolute before:inset-0 before:m-auto before:h-px before:w-3.5 before:bg-current after:absolute after:inset-0 after:m-auto after:h-px after:w-3.5 after:rotate-90 after:bg-current after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] group-open:after:rotate-0 motion-reduce:after:transition-none"></i>
            </summary>
            <p class="max-w-[52ch] px-0.5 pb-[22px] text-[13.5px] leading-[1.8] text-tfa08-mut transition-[translate,opacity] duration-350 group-[&:not([open])]:translate-y-1">60 days, free, no questions. Start a return from your order email and drop the package at any carrier point — refunds land 3–5 days after scanning. Exchanges ship before your return even arrives.</p>
          </details>
          <details class="group border-b border-tfa08-line">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-0.5 py-[22px] text-[14px] font-semibold uppercase tracking-[0.06em] transition-colors duration-200 hover:text-tfa08-acc focus-visible:outline-[1.5px] focus-visible:outline-offset-4 focus-visible:outline-tfa08-acc [&::-webkit-details-marker]:hidden">Fabric &amp; fit
              <i aria-hidden="true" class="relative size-3.5 shrink-0 before:absolute before:inset-0 before:m-auto before:h-px before:w-3.5 before:bg-current after:absolute after:inset-0 after:m-auto after:h-px after:w-3.5 after:rotate-90 after:bg-current after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] group-open:after:rotate-0 motion-reduce:after:transition-none"></i>
            </summary>
            <p class="max-w-[52ch] px-0.5 pb-[22px] text-[13.5px] leading-[1.8] text-tfa08-mut transition-[translate,opacity] duration-350 group-[&:not([open])]:translate-y-1">230gsm organic cotton, garment-dyed and pre-shrunk. The fit is relaxed through the body with a ribbed collar that holds its shape — if you are between sizes, size down.</p>
          </details>
          <details class="group border-b border-tfa08-line">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-0.5 py-[22px] text-[14px] font-semibold uppercase tracking-[0.06em] transition-colors duration-200 hover:text-tfa08-acc focus-visible:outline-[1.5px] focus-visible:outline-offset-4 focus-visible:outline-tfa08-acc [&::-webkit-details-marker]:hidden">Care instructions
              <i aria-hidden="true" class="relative size-3.5 shrink-0 before:absolute before:inset-0 before:m-auto before:h-px before:w-3.5 before:bg-current after:absolute after:inset-0 after:m-auto after:h-px after:w-3.5 after:rotate-90 after:bg-current after:transition-transform after:duration-400 after:ease-[cubic-bezier(0.4,0,0.2,1)] group-open:after:rotate-0 motion-reduce:after:transition-none"></i>
            </summary>
            <p class="max-w-[52ch] px-0.5 pb-[22px] text-[13.5px] leading-[1.8] text-tfa08-mut transition-[translate,opacity] duration-350 group-[&:not([open])]:translate-y-1">Machine wash cold, inside out, with like colours. Hang dry — the dryer is where the garment-dye patina goes to die. Iron low, never on the print.</p>
          </details>
        </div>
        <p class="mt-4 text-[11.5px] tracking-[0.04em] text-tfa08-mut">One hairline per item, one accent colour, zero boxes.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa08-bg: #fdfdfb;
  --color-tfa08-bg: oklch(0.99 0.004 90);
  --color-tfa08-ink: #3b332c;
  --color-tfa08-ink: oklch(0.24 0.012 60);
  --color-tfa08-mut: #6d645c;
  --color-tfa08-mut: oklch(0.45 0.015 60);
  --color-tfa08-line: #e5e1d9;
  --color-tfa08-line: oklch(0.9 0.008 80);
  --color-tfa08-acc: #9d5a2f;
  --color-tfa08-acc: oklch(0.52 0.12 40);
  --font-tfa08-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tfa-08 {
  width: 100%;
  min-height: 100svh;
}

.tfa-08 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-08 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .4s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .4s allow-discrete;
  }

  .tfa-08 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-08 details::details-content {
    transition-duration: 1ms;
  }
}
```
