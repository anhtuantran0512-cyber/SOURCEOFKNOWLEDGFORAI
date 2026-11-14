---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-expand-all-collapse-all-faq-accordion/"
title: "Tailwind Expand All and Collapse All FAQ Accordion Buttons"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The bulk controls every long FAQ needs — Expand all / Collapse all over a native <details> list, for readers who skim, Ctrl+F or print."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Expand All and Collapse All FAQ Accordion Buttons
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-expand-all-collapse-all-faq-accordion/

The bulk controls every long FAQ needs — Expand all / Collapse all over a native <details> list, for readers who skim, Ctrl+F or print. Fourteen lines of JS loop the open attribute; the interesting engineering is state truthfulness (each button disables when it would do nothing), and the print layer is now a print: variant instead of a media query.
## HTML
```html
<section class="tfa-19 w-full min-h-svh grid place-items-center bg-tfa19-bg font-tfa19-sans text-tfa19-ink px-5 py-12">
  <div class="w-[min(700px,100%)]">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div>
        <h1 class="text-[clamp(24px,4.2vw,34px)] font-extrabold tracking-[-0.025em]">Rental agreement FAQ</h1>
        <p class="mt-2 max-w-[44ch] text-[14px] leading-relaxed text-tfa19-mut">Bulk controls for readers who skim, search, or print. Buttons disable when they would do nothing.</p>
      </div>
      <div role="group" aria-label="Bulk expand controls" class="flex gap-2 print:hidden">
        <button type="button" id="tfa19-expand" class="min-h-11 cursor-pointer rounded-[11px] border border-tfa19-accedge bg-white px-4 font-tfa19-sans text-[13.5px] font-bold text-tfa19-acc transition-[background-color,translate,opacity] duration-200 enabled:hover:bg-tfa19-tint enabled:hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfa19-acc disabled:cursor-default disabled:opacity-50 motion-reduce:transition-colors">Expand all</button>
        <button type="button" id="tfa19-collapse" disabled class="min-h-11 cursor-pointer rounded-[11px] border border-tfa19-accedge bg-white px-4 font-tfa19-sans text-[13.5px] font-bold text-tfa19-acc transition-[background-color,translate,opacity] duration-200 enabled:hover:bg-tfa19-tint enabled:hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfa19-acc disabled:cursor-default disabled:opacity-50 motion-reduce:transition-colors">Collapse all</button>
      </div>
    </header>

    <div data-panel id="tfa19-list" class="mt-6 flex flex-col gap-2.5">
        <details class="group rounded-[13px] border border-tfa19-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa19-accedge open:shadow-[0_10px_26px_-18px_oklch(0.52_0.14_155/0.4)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa19-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa19-acc [&::-webkit-details-marker]:hidden">How much is the security deposit?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa19-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa19-mut">One month of rent, held in a government-approved deposit scheme within 14 days of payment — you receive the scheme certificate by email, and interest accrues to you, not us.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa19-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa19-accedge open:shadow-[0_10px_26px_-18px_oklch(0.52_0.14_155/0.4)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa19-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa19-acc [&::-webkit-details-marker]:hidden">Are pets allowed?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa19-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa19-mut">Cats and dogs under 25kg, with a pet addendum and a refundable pet deposit of $300. Aquariums under 100L need no addendum; exotic animals are case-by-case.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa19-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa19-accedge open:shadow-[0_10px_26px_-18px_oklch(0.52_0.14_155/0.4)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa19-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa19-acc [&::-webkit-details-marker]:hidden">Who handles repairs?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa19-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa19-mut">Report through the tenant portal — urgent issues (water, heat, locks) get a four-hour response window, everything else three business days. Repairs under $150 caused by normal wear are always on us.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa19-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa19-accedge open:shadow-[0_10px_26px_-18px_oklch(0.52_0.14_155/0.4)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa19-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa19-acc [&::-webkit-details-marker]:hidden">Can I sublet or list on a short-let site?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa19-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa19-mut">Long-term subletting is allowed with written consent and a referenced subtenant. Short-term letting is not permitted — it breaches both the lease and most building insurance policies.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa19-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa19-accedge open:shadow-[0_10px_26px_-18px_oklch(0.52_0.14_155/0.4)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa19-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa19-acc [&::-webkit-details-marker]:hidden">How do I end the tenancy?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa19-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa19-mut">Two months of written notice after the initial fixed term, served via the portal. The move-out checklist and cleaning standard are attached to the lease — deposits return within 10 days of a clear inspection.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa19-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa19-accedge open:shadow-[0_10px_26px_-18px_oklch(0.52_0.14_155/0.4)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa19-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa19-acc [&::-webkit-details-marker]:hidden">What happens if rent is late?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa19-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa19-mut">A five-day grace period applies before any fee. After that it is a flat $50, never compounding — and if something has gone wrong, talk to us first; payment plans beat penalties for everyone.</p>
        </details>
    </div>

    <p class="mt-5 text-[12.5px] text-tfa19-mut">Printing this page auto-expands every answer — <code class="rounded bg-tfa19-tint px-1.5 py-0.5 font-tfa19-mono text-[0.88em] text-tfa19-acc">print:hidden</code> on the controls plus three lines of print CSS.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa19-bg: #f7faf7;
  --color-tfa19-bg: oklch(0.975 0.008 145);
  --color-tfa19-ink: #253028;
  --color-tfa19-ink: oklch(0.24 0.03 155);
  --color-tfa19-mut: #576159;
  --color-tfa19-mut: oklch(0.46 0.025 150);
  --color-tfa19-edge: #e0e8e1;
  --color-tfa19-edge: oklch(0.91 0.015 148);
  --color-tfa19-accedge: #7aab88;
  --color-tfa19-accedge: oklch(0.7 0.08 155);
  --color-tfa19-tint: #e6f2e9;
  --color-tfa19-tint: oklch(0.94 0.03 155);
  --color-tfa19-acc: #276b45;
  --color-tfa19-acc: oklch(0.45 0.13 155);
  --font-tfa19-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa19-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-19 {
  width: 100%;
  min-height: 100svh;
}

.tfa-19 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-19 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .tfa-19 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}
/* The one thing print: variants cannot reach — a pseudo-element with a closed-state height. */

@media print {
  .tfa-19 details::details-content {
    display: block !important;
    height: auto !important;
    opacity: 1 !important;
    overflow: visible !important;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-19 details::details-content {
    transition-duration: 1ms;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.tfa-19');if(!root||root.dataset.tfa19)return;root.dataset.tfa19='1';
  var items=[].slice.call(root.querySelectorAll('#tfa19-list details')),
      ex=root.querySelector('#tfa19-expand'),co=root.querySelector('#tfa19-collapse');
  function sync(){
    var open=items.filter(function(d){return d.open}).length;
    ex.disabled=open===items.length;
    co.disabled=open===0;
  }
  ex.addEventListener('click',function(){items.forEach(function(d){d.open=true})});
  co.addEventListener('click',function(){items.forEach(function(d){d.open=false})});
  items.forEach(function(d){d.addEventListener('toggle',sync)});
  sync();
})();
```
