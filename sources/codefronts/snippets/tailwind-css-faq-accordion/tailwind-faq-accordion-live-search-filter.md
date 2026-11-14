---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-accordion-live-search-filter/"
title: "Tailwind FAQ Accordion with a Live Search Bar Filter"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "Type-to-filter FAQ: the search bar live-narrows the list, matching question and answer text, auto-expanding hits so the match is visible, announcing a count…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind FAQ Accordion with a Live Search Bar Filter
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-accordion-live-search-filter/

Type-to-filter FAQ: the search bar live-narrows the list, matching question and answer text, auto-expanding hits so the match is visible, announcing a count through aria-live, and showing a designed no-results state. Twenty-four lines of dependency-free JS on top of native <details> — and the search bar's focus ring is the port's quiet win.
## HTML
```html
<section class="tfa-18 w-full min-h-svh grid place-items-center bg-tfa18-bg font-tfa18-sans text-tfa18-ink px-5 py-12 bg-[radial-gradient(1000px_550px_at_50%_-15%,var(--color-tfa18-glow),transparent_60%)]">
  <div class="w-[min(680px,100%)]">
    <header>
      <h1 class="text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Search the FAQ</h1>
      <p class="mt-3 max-w-[54ch] text-[15px] leading-relaxed text-tfa18-mut">Matches run against questions <em>and</em> answers — try “refund”, “VAT”, or gibberish for the empty state.</p>
    </header>

    <div class="mt-6 flex min-h-[52px] items-center gap-2.5 rounded-[14px] border border-tfa18-edge bg-tfa18-panel px-4 transition-[border-color,box-shadow] duration-250 focus-within:border-tfa18-acc focus-within:ring-3 focus-within:ring-tfa18-ring">
      <svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" class="shrink-0 text-tfa18-mut"><circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M13.5 13.5L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="tfa18-search" type="search" aria-label="Search frequently asked questions" placeholder="Type to filter questions…" class="min-h-11 w-full min-w-0 flex-1 border-0 bg-transparent text-[15px] text-tfa18-ink outline-none placeholder:text-tfa18-mut [&::-webkit-search-cancel-button]:appearance-none">
      <span id="tfa18-count" aria-live="polite" class="shrink-0 whitespace-nowrap font-tfa18-mono text-[11.5px] font-semibold text-tfa18-acc"></span>
    </div>

    <div data-panel id="tfa18-list" class="mt-3.5 flex flex-col gap-2.5">
        <details class="group rounded-[13px] border border-tfa18-edge bg-tfa18-panel transition-[border-color,box-shadow] duration-300 open:border-tfa18-accedge open:shadow-[0_14px_34px_-22px_oklch(0.78_0.13_200/0.45)]" open>
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa18-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa18-acc [&::-webkit-details-marker]:hidden">How do refunds work?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa18-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa18-mut">Full refund within 30 days of purchase, self-serve from your order page — money back to the original method in 3–5 business days, VAT included and corrected on the credit note.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa18-edge bg-tfa18-panel transition-[border-color,box-shadow] duration-300 open:border-tfa18-accedge open:shadow-[0_14px_34px_-22px_oklch(0.78_0.13_200/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa18-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa18-acc [&::-webkit-details-marker]:hidden">Do prices include VAT?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa18-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa18-mut">Consumer prices include VAT for EU and UK customers; business customers with a valid VAT ID are reverse-charged. US sales tax is added at checkout by state.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa18-edge bg-tfa18-panel transition-[border-color,box-shadow] duration-300 open:border-tfa18-accedge open:shadow-[0_14px_34px_-22px_oklch(0.78_0.13_200/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa18-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa18-acc [&::-webkit-details-marker]:hidden">Can I use one licence on two machines?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa18-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa18-mut">Yes — licences are per person, not per device. Sign in on up to three machines; deactivating an old one from the dashboard frees a slot instantly.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa18-edge bg-tfa18-panel transition-[border-color,box-shadow] duration-300 open:border-tfa18-accedge open:shadow-[0_14px_34px_-22px_oklch(0.78_0.13_200/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa18-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa18-acc [&::-webkit-details-marker]:hidden">Is there a student discount?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa18-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa18-mut">50% off with a current academic email or ISIC card, verified once a year. It stacks with nothing else, but it beats every coupon we have ever issued.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa18-edge bg-tfa18-panel transition-[border-color,box-shadow] duration-300 open:border-tfa18-accedge open:shadow-[0_14px_34px_-22px_oklch(0.78_0.13_200/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa18-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa18-acc [&::-webkit-details-marker]:hidden">What happens to updates after my licence expires?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa18-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa18-mut">The perpetual-fallback model: the app keeps working forever at the last version your licence covered; renewing unlocks another year of updates. No subscription hostage-taking.</p>
        </details>
        <details class="group rounded-[13px] border border-tfa18-edge bg-tfa18-panel transition-[border-color,box-shadow] duration-300 open:border-tfa18-accedge open:shadow-[0_14px_34px_-22px_oklch(0.78_0.13_200/0.45)]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-4 py-3.5 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa18-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa18-acc [&::-webkit-details-marker]:hidden">Do you offer purchase orders for schools?
            <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa18-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
          </summary>
          <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa18-mut">Yes — POs from accredited institutions are NET-30, with vendor forms available for download. Email a PO and quantities; keys arrive with the countersigned invoice.</p>
        </details>
    </div>

    <div id="tfa18-empty" hidden class="mt-4 rounded-[14px] border border-dashed border-tfa18-edge px-5 py-6 text-center text-tfa18-mut">
      <b class="text-[15px] text-tfa18-ink">No questions match.</b>
      <p class="mt-1.5 text-[13.5px]">Try fewer words, or <button type="button" id="tfa18-clear" class="min-h-11 cursor-pointer border-0 bg-transparent px-1 font-tfa18-sans text-[13.5px] font-bold text-tfa18-acc underline underline-offset-[3px] focus-visible:rounded-md focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfa18-acc">clear the search</button>.</p>
    </div>

    <p class="mt-5 text-[12.5px] text-tfa18-mut">Twenty-four lines of vanilla JS: match on textContent, hide via the <code class="rounded bg-tfa18-tint px-1.5 py-0.5 font-tfa18-mono text-[0.88em] text-tfa18-acc">hidden</code> attribute, announce via <code class="rounded bg-tfa18-tint px-1.5 py-0.5 font-tfa18-mono text-[0.88em] text-tfa18-acc">aria-live</code>.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa18-bg: #1b2028;
  --color-tfa18-bg: oklch(0.21 0.02 250);
  --color-tfa18-panel: #232a33;
  --color-tfa18-panel: oklch(0.25 0.022 250);
  --color-tfa18-glow: #1d3944;
  --color-tfa18-glow: oklch(0.29 0.05 210 / 0.55);
  --color-tfa18-ink: #f1f4f7;
  --color-tfa18-ink: oklch(0.96 0.007 245);
  --color-tfa18-mut: #b2bcc6;
  --color-tfa18-mut: oklch(0.79 0.016 248);
  --color-tfa18-edge: #38424d;
  --color-tfa18-edge: oklch(0.34 0.025 250);
  --color-tfa18-accedge: #4f929e;
  --color-tfa18-accedge: oklch(0.6 0.08 200);
  --color-tfa18-tint: #22383e;
  --color-tfa18-tint: oklch(0.28 0.04 200);
  --color-tfa18-ring: #2f5f6b;
  --color-tfa18-ring: oklch(0.45 0.07 200 / 0.55);
  --color-tfa18-acc: #7fd8e4;
  --color-tfa18-acc: oklch(0.85 0.11 200);
  --font-tfa18-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa18-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-18 {
  width: 100%;
  min-height: 100svh;
}

.tfa-18 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-18 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .tfa-18 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-18 details::details-content {
    transition-duration: 1ms;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.tfa-18');if(!root||root.dataset.tfa18)return;root.dataset.tfa18='1';
  var input=root.querySelector('#tfa18-search'),count=root.querySelector('#tfa18-count'),
      empty=root.querySelector('#tfa18-empty'),items=[].slice.call(root.querySelectorAll('#tfa18-list details'));
  items.forEach(function(d){d.dataset.initOpen=d.open?'1':''});
  function filter(){
    var q=input.value.trim().toLowerCase(),hits=0;
    items.forEach(function(d){
      var hit=!q||d.textContent.toLowerCase().indexOf(q)>-1;
      d.hidden=!hit;
      if(q&&hit)d.open=true;
      if(!q)d.open=!!d.dataset.initOpen;
      if(hit)hits++;
    });
    count.textContent=q?hits+' of '+items.length+' questions':'';
    empty.hidden=hits>0;
  }
  input.addEventListener('input',filter);
  root.querySelector('#tfa18-clear').addEventListener('click',function(){input.value='';filter();input.focus()});
})();
```
