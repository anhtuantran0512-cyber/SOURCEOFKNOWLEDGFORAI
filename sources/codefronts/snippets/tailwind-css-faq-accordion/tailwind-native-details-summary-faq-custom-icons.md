---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-native-details-summary-faq-custom-icons/"
title: "Tailwind Native Details/Summary FAQ with Custom Styled Icons"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The most semantic FAQ possible, in utilities: native <details>/<summary> for behaviour, group-open: for every open-state style, and the marker killed by…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Native Details/Summary FAQ with Custom Styled Icons
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-native-details-summary-faq-custom-icons/

The most semantic FAQ possible, in utilities: native <details>/<summary> for behaviour, group-open: for every open-state style, and the marker killed by list-none [&::-webkit-details-marker]:hidden. The height-to-auto animation is the one thing utilities cannot reach, so it stays four lines of @supports CSS — enhancing every accordion on the page at once. Styled as a warm editorial help page.
## HTML
```html
<section class="tfa-02 w-full min-h-svh grid place-items-center bg-tfa02-bg font-tfa02-sans text-tfa02-ink px-5 py-12">
  <div class="w-[min(660px,100%)]">
    <header>
      <h1 class="font-tfa02-serif text-[clamp(32px,6vw,46px)] font-semibold leading-[1.05] tracking-[-0.02em]">Help &amp; support</h1>
      <p class="mt-3 max-w-[56ch] text-[14.5px] leading-[1.7] text-tfa02-mut">Built on native <code class="rounded bg-tfa02-code px-1.5 py-0.5 font-tfa02-mono text-[0.85em] text-tfa02-acc">&lt;details&gt;</code> — keyboard support, screen-reader semantics and find-in-page expansion come free. Try <kbd class="rounded-md border border-b-2 border-tfa02-edge bg-white px-1.5 py-0.5 font-tfa02-mono text-[0.82em]">Ctrl</kbd>+<kbd class="rounded-md border border-b-2 border-tfa02-edge bg-white px-1.5 py-0.5 font-tfa02-mono text-[0.82em]">F</kbd> for “passport”.</p>
    </header>

    <div data-panel class="mt-9 border-t border-tfa02-edge">
      <details class="group border-b border-tfa02-edge open:border-tfa02-accedge" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-1 py-5 font-tfa02-serif text-[19px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa02-acc focus-visible:rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tfa02-acc [&::-webkit-details-marker]:hidden">
          How long does delivery take?
          <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-full border border-tfa02-edge text-tfa02-acc transition-[transform,background-color,border-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:border-tfa02-accedge group-open:-rotate-180 group-open:border-tfa02-accedge group-open:bg-tfa02-code motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[58ch] px-1 pb-6 pt-0.5 text-[14.5px] leading-[1.75] text-tfa02-mut">Standard delivery is 3–5 business days across the US, UK, Canada and Australia. Express (1–2 days) is available at checkout, and every order gets a tracked link the moment it leaves the warehouse.</p>
      </details>

      <details class="group border-b border-tfa02-edge open:border-tfa02-accedge">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-1 py-5 font-tfa02-serif text-[19px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa02-acc focus-visible:rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tfa02-acc [&::-webkit-details-marker]:hidden">
          Do I need a passport copy to book?
          <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-full border border-tfa02-edge text-tfa02-acc transition-[transform,background-color,border-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:border-tfa02-accedge group-open:-rotate-180 group-open:border-tfa02-accedge group-open:bg-tfa02-code motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[58ch] px-1 pb-6 pt-0.5 text-[14.5px] leading-[1.75] text-tfa02-mut">Only for international itineraries. Upload a photo of the ID page once and we auto-fill every future booking — the file is encrypted at rest and deleted 30 days after your trip ends.</p>
      </details>

      <details class="group border-b border-tfa02-edge open:border-tfa02-accedge">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-1 py-5 font-tfa02-serif text-[19px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa02-acc focus-visible:rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tfa02-acc [&::-webkit-details-marker]:hidden">
          Can I change my order after placing it?
          <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-full border border-tfa02-edge text-tfa02-acc transition-[transform,background-color,border-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:border-tfa02-accedge group-open:-rotate-180 group-open:border-tfa02-accedge group-open:bg-tfa02-code motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[58ch] px-1 pb-6 pt-0.5 text-[14.5px] leading-[1.75] text-tfa02-mut">Yes — orders can be edited for 60 minutes after checkout from your account page. After that the warehouse has it, but you can always refuse delivery or start a free return.</p>
      </details>

      <details class="group border-b border-tfa02-edge open:border-tfa02-accedge">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-1 py-5 font-tfa02-serif text-[19px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa02-acc focus-visible:rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tfa02-acc [&::-webkit-details-marker]:hidden">
          Which payment methods do you accept?
          <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-full border border-tfa02-edge text-tfa02-acc transition-[transform,background-color,border-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:border-tfa02-accedge group-open:-rotate-180 group-open:border-tfa02-accedge group-open:bg-tfa02-code motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[58ch] px-1 pb-6 pt-0.5 text-[14.5px] leading-[1.75] text-tfa02-mut">All major cards, Apple Pay, Google Pay and PayPal. Business customers can request invoicing with NET-30 terms once approved.</p>
      </details>
    </div>

    <p class="mt-6 text-[12.5px] leading-relaxed text-tfa02-mut">Open/close animates to <code class="rounded bg-tfa02-code px-1.5 py-0.5 font-tfa02-mono text-[0.85em] text-tfa02-acc">height:auto</code> via <code class="rounded bg-tfa02-code px-1.5 py-0.5 font-tfa02-mono text-[0.85em] text-tfa02-acc">::details-content</code> — the only four lines utilities cannot express.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa02-bg: #f7f3ec;
  --color-tfa02-bg: oklch(0.96 0.014 85);
  --color-tfa02-ink: #2e2620;
  --color-tfa02-ink: oklch(0.25 0.02 60);
  --color-tfa02-mut: #6a5f56;
  --color-tfa02-mut: oklch(0.47 0.022 60);
  --color-tfa02-edge: #ded5c7;
  --color-tfa02-edge: oklch(0.88 0.018 80);
  --color-tfa02-accedge: #c8865f;
  --color-tfa02-accedge: oklch(0.7 0.09 45);
  --color-tfa02-code: #f0e2d6;
  --color-tfa02-code: oklch(0.92 0.026 60);
  --color-tfa02-acc: #a8502a;
  --color-tfa02-acc: oklch(0.52 0.14 45);
  --font-tfa02-serif: 'Newsreader', Georgia, serif;
  --font-tfa02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa02-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-02 {
  width: 100%;
  min-height: 100svh;
}
/* The port's limit, in four lines: ::details-content has no Tailwind variant and interpolate-size
   is an inherited opt-in rather than a design-scale value. Declared once for the whole list. */

.tfa-02 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-02 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .4s cubic-bezier(.4,0,.2,1), opacity .35s, content-visibility .4s allow-discrete;
  }

  .tfa-02 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-02 details::details-content {
    transition-duration: 1ms;
  }
}
```
