---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-feature-comparison-pricing-table/"
title: "Tailwind Feature Comparison Pricing Table"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Nine features, four plans, one real <table> with <th scope> on both axes."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Comparison Pricing Table
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-feature-comparison-pricing-table/

Nine features, four plans, one real <table> with <th scope> on both axes. The port's lesson is where utilities are weakest: a table's shared cell styling has no ancestor shortcut, so every <td> carries its own class list &mdash; and the recommended column's guide-rail tint becomes a per-cell utility instead of one selector.
## HTML
```html
<section class="tps-03 w-full min-h-svh bg-tps03-bg font-tps03-sans text-tps03-ink px-[clamp(16px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Plan comparison">
  <header class="text-center mb-[clamp(20px,4vw,36px)]">
    <h2 class="m-0 mb-2 text-[clamp(22px,3.2vw,32px)] font-bold tracking-[-0.02em] text-tps03-bright text-pretty">Compare every feature.</h2>
    <p class="m-0 text-sm text-tps03-mut">Pick the column that matches what you ship today.</p>
  </header>
  <div class="max-w-[980px] mx-auto pt-3.5 pb-2 md:pb-0 overflow-x-auto overflow-y-visible [-webkit-overflow-scrolling:touch]">
    <table class="w-full min-w-[720px] border-separate border-spacing-0 text-xs md:text-[13.5px]">
      <thead>
        <tr>
          <th scope="col" class="p-2 md:p-3.5 text-left font-medium text-tps03-mut border-b border-tps03-edge">Feature</th>
          <th scope="col" class="p-2 md:p-3.5 text-center text-[13px] md:text-sm font-bold text-tps03-head2 bg-tps03-head border-b border-tps03-edge">Free<br><span class="block mt-1 text-[13px] font-medium text-tps03-mut">$0</span></th>
          <th scope="col" class="relative p-2 md:p-3.5 text-center text-[13px] md:text-sm font-bold text-tps03-acc2 bg-linear-to-b from-tps03-rec3 to-tps03-rec2 border-b border-tps03-edge">
            <span class="absolute -top-2.5 left-1/2 -translate-x-1/2 px-1.5 md:px-2.5 py-0.5 rounded-full bg-tps03-acc text-tps03-bg text-[9px] md:text-[10px] font-bold uppercase tracking-[0.08em] whitespace-nowrap">Recommended</span>Pro<br><span class="block mt-1 text-[13px] font-medium text-tps03-mut">$24</span>
          </th>
          <th scope="col" class="p-2 md:p-3.5 text-center text-[13px] md:text-sm font-bold text-tps03-head2 bg-tps03-head border-b border-tps03-edge">Team<br><span class="block mt-1 text-[13px] font-medium text-tps03-mut">$48</span></th>
          <th scope="col" class="p-2 md:p-3.5 text-center text-[13px] md:text-sm font-bold text-tps03-head2 bg-tps03-head border-b border-tps03-edge">Enterprise<br><span class="block mt-1 text-[13px] font-medium text-tps03-mut">Contact</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">Projects</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge">1</td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec text-tps03-acc">10</td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge">50</td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge">Unlimited</td>
        </tr>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">Storage</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge">500 MB</td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec text-tps03-acc">10 GB</td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge">50 GB</td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge">500 GB</td>
        </tr>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">Custom domain</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
        </tr>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">Team roles</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
        </tr>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">Priority support</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
        </tr>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">SSO &amp; SAML</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
        </tr>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">Audit logs</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
        </tr>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">99.99% SLA</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
        </tr>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 text-left font-medium text-tps03-head2 border-b border-tps03-edge">Dedicated CSM</th>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge bg-tps03-rec"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="font-medium text-tps03-dim" aria-label="not included">&mdash;</span></td>
          <td class="p-2 md:p-3.5 text-center border-b border-tps03-edge"><span class="inline-grid place-items-center w-5.5 h-5.5 rounded-full bg-tps03-chip text-tps03-acc font-bold" aria-label="included">&#10003;</span></td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th scope="row" class="p-2 md:p-3.5 pt-4.5 text-left"><span class="sr-only">Choose a plan</span></th>
          <td class="px-2 md:px-3.5 pt-4.5 pb-1 text-center"><a href="#free" class="inline-block px-4 py-2.25 rounded-[7px] text-[12.5px] font-semibold no-underline text-tps03-acc2 border border-tps03-ctaedge transition-[background-color,color] duration-200 hover:bg-tps03-chip hover:text-tps03-bright focus-visible:outline-2 focus-visible:outline-tps03-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Get started</a></td>
          <td class="px-2 md:px-3.5 pt-4.5 pb-1 text-center bg-tps03-rec"><a href="#pro" class="inline-block px-4 py-2.25 rounded-[7px] text-[12.5px] font-semibold no-underline bg-tps03-acc text-tps03-bg border border-tps03-acc transition-[background-color] duration-200 hover:bg-tps03-acc2 focus-visible:outline-2 focus-visible:outline-tps03-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Choose Pro &rarr;</a></td>
          <td class="px-2 md:px-3.5 pt-4.5 pb-1 text-center"><a href="#team" class="inline-block px-4 py-2.25 rounded-[7px] text-[12.5px] font-semibold no-underline text-tps03-acc2 border border-tps03-ctaedge transition-[background-color,color] duration-200 hover:bg-tps03-chip hover:text-tps03-bright focus-visible:outline-2 focus-visible:outline-tps03-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Choose Team</a></td>
          <td class="px-2 md:px-3.5 pt-4.5 pb-1 text-center"><a href="#ent" class="inline-block px-4 py-2.25 rounded-[7px] text-[12.5px] font-semibold no-underline text-tps03-acc2 border border-tps03-ctaedge transition-[background-color,color] duration-200 hover:bg-tps03-chip hover:text-tps03-bright focus-visible:outline-2 focus-visible:outline-tps03-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Talk to sales</a></td>
        </tr>
      </tfoot>
    </table>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps03-bg: #06141a;
  --color-tps03-bg: oklch(0.16 0.02 220);
  --color-tps03-head: #0c1f27;
  --color-tps03-head: oklch(0.22 0.02 220);
  --color-tps03-edge: #133540;
  --color-tps03-edge: oklch(0.3 0.03 220);
  --color-tps03-ctaedge: #1d6a7c;
  --color-tps03-ctaedge: oklch(0.48 0.07 215);
  --color-tps03-rec: #0a2630;
  --color-tps03-rec: oklch(0.24 0.03 215);
  --color-tps03-rec2: #0b2c37;
  --color-tps03-rec2: oklch(0.26 0.035 213);
  --color-tps03-rec3: #17505f;
  --color-tps03-rec3: oklch(0.4 0.06 213);
  --color-tps03-chip: #114352;
  --color-tps03-chip: oklch(0.35 0.05 213);
  --color-tps03-ink: #e0f2f7;
  --color-tps03-ink: oklch(0.94 0.02 215);
  --color-tps03-bright: #f1fbff;
  --color-tps03-bright: oklch(0.98 0.01 215);
  --color-tps03-head2: #cfeaf2;
  --color-tps03-head2: oklch(0.91 0.03 215);
  --color-tps03-mut: #88a8b3;
  --color-tps03-mut: oklch(0.7 0.03 215);
  --color-tps03-dim: #5b7480;
  --color-tps03-dim: oklch(0.52 0.03 220);
  --color-tps03-acc: #22d3ee;
  --color-tps03-acc: oklch(0.8 0.14 200);
  --color-tps03-acc2: #5eead4;
  --color-tps03-acc2: oklch(0.87 0.12 175);
  --font-tps03-sans: 'Inter', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is correctly sized in the moment before the
   browser build has compiled its utilities. */

.tps-03 {
  width: 100%;
  min-height: 100svh;
}
```
