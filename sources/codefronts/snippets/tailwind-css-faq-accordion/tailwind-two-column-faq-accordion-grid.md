---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-two-column-faq-accordion-grid/"
title: "Tailwind Two-Column FAQ Accordion Grid with Independent Columns"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "A wide FAQ split into two independent columns — the layout every marketing site wants past eight questions — built so an opening panel pushes down only its…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Two-Column FAQ Accordion Grid with Independent Columns
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-two-column-faq-accordion-grid/

A wide FAQ split into two independent columns — the layout every marketing site wants past eight questions — built so an opening panel pushes down only its own column, never its horizontal neighbour. The trap almost everyone hits is one flat grid of items, where row alignment makes cells stretch each other; the fix is two column containers, and it is two utilities.
## HTML
```html
<section class="tfa-14 w-full min-h-svh font-tfa14-sans text-tfa14-ink">
  <div class="@container grid min-h-svh w-full place-items-center bg-tfa14-bg px-5 py-12 bg-[linear-gradient(180deg,var(--color-tfa14-wash),var(--color-tfa14-bg)_36%)]">
    <div class="w-[min(980px,100%)]">
      <header class="text-center">
        <h1 class="text-[clamp(26px,4.4vw,40px)] font-extrabold tracking-[-0.025em]">Everything buyers ask</h1>
        <p class="mx-auto mt-3 max-w-[52ch] text-[14.5px] leading-relaxed text-tfa14-mut">Two independent columns — open any panel and only its own column reflows.</p>
      </header>

      <div data-panel class="mt-8 grid items-start gap-3 @3xl:grid-cols-2 @3xl:gap-x-8">
        <div class="flex flex-col gap-3">
          <details class="group rounded-2xl border border-tfa14-edge bg-white shadow-[0_2px_10px_oklch(0.4_0.04_215/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa14-accedge open:shadow-[0_12px_30px_-18px_oklch(0.45_0.1_212/0.35)]" open>
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-5 py-4 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa14-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa14-acc [&::-webkit-details-marker]:hidden">How fast is onboarding?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa14-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[54ch] px-5 pb-4 text-[13.5px] leading-[1.7] text-tfa14-mut">Most teams import their data and invite the team in under an hour. A guided setup checklist tracks the six steps, and a specialist can join a call for workspaces over 50 seats.</p>
          </details>
          <details class="group rounded-2xl border border-tfa14-edge bg-white shadow-[0_2px_10px_oklch(0.4_0.04_215/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa14-accedge open:shadow-[0_12px_30px_-18px_oklch(0.45_0.1_212/0.35)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-5 py-4 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa14-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa14-acc [&::-webkit-details-marker]:hidden">Can we migrate from a competitor?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa14-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[54ch] px-5 pb-4 text-[13.5px] leading-[1.7] text-tfa14-mut">One-click importers cover the four biggest tools, mapping projects, comments and attachments. Anything else comes in via CSV or the API — migrations team included on annual plans.</p>
          </details>
          <details class="group rounded-2xl border border-tfa14-edge bg-white shadow-[0_2px_10px_oklch(0.4_0.04_215/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa14-accedge open:shadow-[0_12px_30px_-18px_oklch(0.45_0.1_212/0.35)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-5 py-4 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa14-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa14-acc [&::-webkit-details-marker]:hidden">Is training included?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa14-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[54ch] px-5 pb-4 text-[13.5px] leading-[1.7] text-tfa14-mut">Live weekly webinars and a self-serve academy are free for everyone. Enterprise plans add two bespoke training sessions, recorded for your internal wiki.</p>
          </details>
          <details class="group rounded-2xl border border-tfa14-edge bg-white shadow-[0_2px_10px_oklch(0.4_0.04_215/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa14-accedge open:shadow-[0_12px_30px_-18px_oklch(0.45_0.1_212/0.35)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-5 py-4 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa14-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa14-acc [&::-webkit-details-marker]:hidden">What uptime do you guarantee?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa14-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[54ch] px-5 pb-4 text-[13.5px] leading-[1.7] text-tfa14-mut">99.9% on every paid plan, 99.99% with the enterprise SLA — backed by service credits, with a public status page and five-year incident history.</p>
          </details>
        </div>
        <div class="flex flex-col gap-3">
          <details class="group rounded-2xl border border-tfa14-edge bg-white shadow-[0_2px_10px_oklch(0.4_0.04_215/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa14-accedge open:shadow-[0_12px_30px_-18px_oklch(0.45_0.1_212/0.35)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-5 py-4 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa14-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa14-acc [&::-webkit-details-marker]:hidden">Where is data stored?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa14-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[54ch] px-5 pb-4 text-[13.5px] leading-[1.7] text-tfa14-mut">US or EU region, chosen at workspace creation and never moved without written consent. Backups stay in-region, encrypted with per-tenant keys.</p>
          </details>
          <details class="group rounded-2xl border border-tfa14-edge bg-white shadow-[0_2px_10px_oklch(0.4_0.04_215/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa14-accedge open:shadow-[0_12px_30px_-18px_oklch(0.45_0.1_212/0.35)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-5 py-4 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa14-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa14-acc [&::-webkit-details-marker]:hidden">Do you support SSO and SCIM?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa14-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[54ch] px-5 pb-4 text-[13.5px] leading-[1.7] text-tfa14-mut">SAML SSO and SCIM provisioning ship on the Business tier — Okta, Entra, Google and OneLogin have first-party guides. Enforced 2FA is available on every plan, free.</p>
          </details>
          <details class="group rounded-2xl border border-tfa14-edge bg-white shadow-[0_2px_10px_oklch(0.4_0.04_215/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa14-accedge open:shadow-[0_12px_30px_-18px_oklch(0.45_0.1_212/0.35)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-5 py-4 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa14-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa14-acc [&::-webkit-details-marker]:hidden">Can we self-host?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa14-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[54ch] px-5 pb-4 text-[13.5px] leading-[1.7] text-tfa14-mut">No — and honestly, that is why the product ships weekly. The compliance package (SOC 2 Type II, ISO 27001, DPA, pen-test summaries) answers what self-hosting usually stands in for.</p>
          </details>
          <details class="group rounded-2xl border border-tfa14-edge bg-white shadow-[0_2px_10px_oklch(0.4_0.04_215/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa14-accedge open:shadow-[0_12px_30px_-18px_oklch(0.45_0.1_212/0.35)]">
            <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-3.5 px-5 py-4 text-[14.5px] font-semibold transition-colors duration-200 hover:text-tfa14-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa14-acc [&::-webkit-details-marker]:hidden">What is the contract minimum?
              <i aria-hidden="true" class="size-2 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa14-acc transition-[rotate,translate] duration-350 group-open:translate-y-0.5 group-open:rotate-[225deg] motion-reduce:transition-none"></i>
            </summary>
            <p class="max-w-[54ch] px-5 pb-4 text-[13.5px] leading-[1.7] text-tfa14-mut">None on monthly. Annual contracts run 12 months with a 60-day opt-out pilot window for new enterprise customers — if it is not landing, you leave with a full refund.</p>
          </details>
        </div>
      </div>

      <p class="mt-7 text-center text-[12.5px] text-tfa14-mut">Grid places the columns, flexbox stacks the items — the split is what keeps neighbours independent.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa14-bg: #f9fbfc;
  --color-tfa14-bg: oklch(0.98 0.006 200);
  --color-tfa14-wash: #e8f2f6;
  --color-tfa14-wash: oklch(0.94 0.025 205);
  --color-tfa14-ink: #1e2a33;
  --color-tfa14-ink: oklch(0.22 0.03 220);
  --color-tfa14-mut: #566470;
  --color-tfa14-mut: oklch(0.47 0.022 215);
  --color-tfa14-edge: #e1e7ec;
  --color-tfa14-edge: oklch(0.91 0.012 205);
  --color-tfa14-accedge: #7fb3c8;
  --color-tfa14-accedge: oklch(0.73 0.07 210);
  --color-tfa14-tint: #eaf4f8;
  --color-tfa14-tint: oklch(0.95 0.02 205);
  --color-tfa14-acc: #1f6f91;
  --color-tfa14-acc: oklch(0.5 0.11 220);
  --font-tfa14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tfa-14 {
  width: 100%;
  min-height: 100svh;
}

.tfa-14 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-14 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .38s allow-discrete;
  }

  .tfa-14 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-14 details::details-content {
    transition-duration: 1ms;
  }
}
```
