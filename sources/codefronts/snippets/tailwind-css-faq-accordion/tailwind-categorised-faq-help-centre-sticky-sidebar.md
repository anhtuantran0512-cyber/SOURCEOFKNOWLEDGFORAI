---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-categorised-faq-help-centre-sticky-sidebar/"
title: "Tailwind Categorised FAQ Help Centre with a Sticky Sidebar Menu"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The help-centre layout: questions grouped under category headings with a sticky sidebar that jumps between sections."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Categorised FAQ Help Centre with a Sticky Sidebar Menu
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-categorised-faq-help-centre-sticky-sidebar/

The help-centre layout: questions grouped under category headings with a sticky sidebar that jumps between sections. Every piece of navigation is native — sticky top-6 self-start pins the menu, scroll-mt-6 stops headings hiding under the top edge, scroll-smooth makes jumps glide — and the two rules people always miss are now visible in the class list rather than buried in a stylesheet.
## HTML
```html
<section class="tfa-16 w-full min-h-svh font-tfa16-sans text-tfa16-ink">
  <div class="@container h-svh w-full overflow-y-auto scroll-smooth bg-tfa16-bg">
    <div class="mx-auto grid w-[min(900px,100%)] gap-6 px-5 py-8 @3xl:grid-cols-[220px_minmax(0,1fr)] @3xl:gap-12 @3xl:px-10 @3xl:py-12">

      <nav aria-label="FAQ categories" class="sticky top-0 z-10 flex flex-row flex-wrap items-center gap-1.5 bg-tfa16-bg/90 py-2.5 backdrop-blur-sm @3xl:top-6 @3xl:z-auto @3xl:flex-col @3xl:items-stretch @3xl:self-start @3xl:bg-transparent @3xl:py-0 @3xl:backdrop-blur-none">
        <span class="w-full font-tfa16-mono text-[11px] font-extrabold uppercase tracking-[0.14em] text-tfa16-mut @3xl:mb-1.5">Help centre</span>
          <a href="#tfa16-account" class="flex min-h-11 items-center justify-between gap-2.5 rounded-[11px] px-3.5 text-[14px] font-semibold text-tfa16-ink no-underline transition-colors duration-200 hover:bg-tfa16-tint hover:text-tfa16-acc focus-visible:bg-tfa16-tint focus-visible:text-tfa16-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc aria-[current=true]:bg-tfa16-tint aria-[current=true]:text-tfa16-acc">Account<span class="rounded-full border border-tfa16-edge bg-white px-2 py-0.5 font-tfa16-mono text-[11px] font-bold text-tfa16-mut">3</span></a>
          <a href="#tfa16-billing" class="flex min-h-11 items-center justify-between gap-2.5 rounded-[11px] px-3.5 text-[14px] font-semibold text-tfa16-ink no-underline transition-colors duration-200 hover:bg-tfa16-tint hover:text-tfa16-acc focus-visible:bg-tfa16-tint focus-visible:text-tfa16-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc aria-[current=true]:bg-tfa16-tint aria-[current=true]:text-tfa16-acc">Billing<span class="rounded-full border border-tfa16-edge bg-white px-2 py-0.5 font-tfa16-mono text-[11px] font-bold text-tfa16-mut">2</span></a>
          <a href="#tfa16-privacy" class="flex min-h-11 items-center justify-between gap-2.5 rounded-[11px] px-3.5 text-[14px] font-semibold text-tfa16-ink no-underline transition-colors duration-200 hover:bg-tfa16-tint hover:text-tfa16-acc focus-visible:bg-tfa16-tint focus-visible:text-tfa16-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc aria-[current=true]:bg-tfa16-tint aria-[current=true]:text-tfa16-acc">Privacy<span class="rounded-full border border-tfa16-edge bg-white px-2 py-0.5 font-tfa16-mono text-[11px] font-bold text-tfa16-mut">2</span></a>
        <p class="mt-3 hidden rounded-[10px] border border-dashed border-tfa16-edge px-3 py-2.5 text-[11.5px] leading-[1.55] text-tfa16-mut @3xl:block">Sticky via <code class="font-tfa16-mono text-tfa16-acc">sticky top-6 self-start</code> — no JS scroll-spy for the jump pattern.</p>
      </nav>

      <div data-panel class="flex flex-col gap-9">
        <section id="tfa16-account" class="scroll-mt-6 target:[&>h2]:border-tfa16-acc target:[&>h2]:text-tfa16-acc">
          <h2 class="border-b-2 border-tfa16-edge pb-2.5 text-[19px] font-extrabold tracking-[-0.02em] transition-colors duration-300">Account</h2>
          <div class="mt-2.5 flex flex-col gap-2.5">
          <details class="group rounded-[13px] border border-tfa16-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa16-accedge open:shadow-[0_10px_26px_-18px_oklch(0.45_0.15_295/0.4)]" open>
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-4 py-3.5 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa16-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc [&::-webkit-details-marker]:hidden">How do I change my email address?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa16-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa16-mut">Settings → Account → Email. We send a confirmation link to both the old and new address; the change applies when the new one is verified. Login sessions stay active.</p>
          </details>
          <details class="group rounded-[13px] border border-tfa16-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa16-accedge open:shadow-[0_10px_26px_-18px_oklch(0.45_0.15_295/0.4)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-4 py-3.5 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa16-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc [&::-webkit-details-marker]:hidden">Can I merge two accounts?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa16-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa16-mut">Yes — from the older account, Settings → Advanced → Merge. Projects, history and integrations move over; the source account becomes an alias that still accepts logins for 90 days.</p>
          </details>
          <details class="group rounded-[13px] border border-tfa16-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa16-accedge open:shadow-[0_10px_26px_-18px_oklch(0.45_0.15_295/0.4)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-4 py-3.5 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa16-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc [&::-webkit-details-marker]:hidden">How do I delete my account?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa16-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa16-mut">Settings → Advanced → Delete. There is a 14-day grace period during which logging back in cancels the deletion; after that everything is purged, including backups, within 30 days.</p>
          </details>
          </div>
        </section>
        <section id="tfa16-billing" class="scroll-mt-6 target:[&>h2]:border-tfa16-acc target:[&>h2]:text-tfa16-acc">
          <h2 class="border-b-2 border-tfa16-edge pb-2.5 text-[19px] font-extrabold tracking-[-0.02em] transition-colors duration-300">Billing</h2>
          <div class="mt-2.5 flex flex-col gap-2.5">
          <details class="group rounded-[13px] border border-tfa16-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa16-accedge open:shadow-[0_10px_26px_-18px_oklch(0.45_0.15_295/0.4)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-4 py-3.5 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa16-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc [&::-webkit-details-marker]:hidden">Where do I find my invoices?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa16-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa16-mut">Settings → Billing → History lists every invoice as a PDF with your tax details. Accountants can be added as billing-only members who see nothing else.</p>
          </details>
          <details class="group rounded-[13px] border border-tfa16-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa16-accedge open:shadow-[0_10px_26px_-18px_oklch(0.45_0.15_295/0.4)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-4 py-3.5 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa16-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc [&::-webkit-details-marker]:hidden">Why was my card declined?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa16-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa16-mut">Nine times out of ten it is a 3-D Secure prompt your bank never delivered. Retry from Billing → Payment method and we trigger a fresh authentication. Failing that, the decline code from your bank tells the real story.</p>
          </details>
          </div>
        </section>
        <section id="tfa16-privacy" class="scroll-mt-6 target:[&>h2]:border-tfa16-acc target:[&>h2]:text-tfa16-acc">
          <h2 class="border-b-2 border-tfa16-edge pb-2.5 text-[19px] font-extrabold tracking-[-0.02em] transition-colors duration-300">Privacy</h2>
          <div class="mt-2.5 flex flex-col gap-2.5">
          <details class="group rounded-[13px] border border-tfa16-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa16-accedge open:shadow-[0_10px_26px_-18px_oklch(0.45_0.15_295/0.4)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-4 py-3.5 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa16-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc [&::-webkit-details-marker]:hidden">Can I export everything you hold on me?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa16-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa16-mut">Settings → Privacy → Export builds a machine-readable archive (JSON plus attachments) within 24 hours — the full GDPR/CCPA portability package, self-serve.</p>
          </details>
          <details class="group rounded-[13px] border border-tfa16-edge bg-white transition-[border-color,box-shadow] duration-300 open:border-tfa16-accedge open:shadow-[0_10px_26px_-18px_oklch(0.45_0.15_295/0.4)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-4 py-3.5 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa16-acc focus-visible:rounded-[13px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa16-acc [&::-webkit-details-marker]:hidden">Do you sell or share my data?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa16-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[60ch] px-4 pb-3.5 text-[13.5px] leading-[1.7] text-tfa16-mut">No, and the DPA says so contractually. Subprocessors are listed publicly with 30-day change notices; analytics run first-party and cookieless.</p>
          </details>
          </div>
        </section>
        <p class="text-[12.5px] text-tfa16-mut">Delete the stage's <code class="font-tfa16-mono text-tfa16-acc">overflow-y-auto</code> and this layout runs on document scroll.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa16-bg: #f9f8fd;
  --color-tfa16-bg: oklch(0.975 0.006 285);
  --color-tfa16-ink: #23202e;
  --color-tfa16-ink: oklch(0.23 0.03 285);
  --color-tfa16-mut: #5b566b;
  --color-tfa16-mut: oklch(0.47 0.022 285);
  --color-tfa16-edge: #e4e1ee;
  --color-tfa16-edge: oklch(0.91 0.01 285);
  --color-tfa16-accedge: #a793e3;
  --color-tfa16-accedge: oklch(0.73 0.1 295);
  --color-tfa16-tint: #efeafd;
  --color-tfa16-tint: oklch(0.94 0.03 295);
  --color-tfa16-acc: #6b3fd4;
  --color-tfa16-acc: oklch(0.48 0.2 295);
  --font-tfa16-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa16-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-16 {
  width: 100%;
  min-height: 100svh;
}

.tfa-16 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-16 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .tfa-16 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-16 details::details-content {
    transition-duration: 1ms;
  }

  .tfa-16 .overflow-y-auto {
    scroll-behavior: auto;
  }
}
```
