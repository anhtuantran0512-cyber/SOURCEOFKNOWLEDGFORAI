---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-plan-feature-comparison-columns/"
title: "Tailwind Plan Feature Comparison Columns"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "Three plan columns whose feature rows line up perfectly across cards, even when one value wraps to two lines."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Plan Feature Comparison Columns
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-plan-feature-comparison-columns/

Three plan columns whose feature rows line up perfectly across cards, even when one value wraps to two lines. Each card is grid-rows-subgrid row-span-8, so all three share one set of row tracks — the alignment the CSS original faked with fixed heights.
## HTML
```html
<section class="tfs-08 w-full min-h-svh bg-tfs08-bg px-5 py-20 font-tfs08-sans text-tfs08-ink antialiased sm:py-28" aria-labelledby="tfs-08-h">
  <div class="mx-auto grid w-full max-w-6xl gap-14">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="text-sm font-semibold text-tfs08-acc">Compare plans</p>
      <h2 id="tfs-08-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">Every plan ships the core. Scale unlocks the rest.</h2>
    </header>
    <div class="grid gap-6 lg:grid-cols-3 lg:gap-x-6 lg:gap-y-0">
      <article class="relative grid gap-0 rounded-3xl bg-white p-2 lg:row-span-8 lg:grid-rows-subgrid ring-1 ring-tfs08-line">
        <div class="grid gap-2 rounded-2xl bg-tfs08-bg p-6"><h3 class="text-xl font-semibold">Starter</h3><p class="text-sm text-tfs08-mut">For side projects and first launches</p><p class="mt-2 text-3xl font-semibold tracking-tight">Free</p><a href="#tfs-08-h" class="mt-3 inline-flex min-h-11 items-center justify-center rounded-xl text-sm font-semibold transition focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs08-acc bg-white text-tfs08-ink ring-1 ring-tfs08-line hover:ring-tfs08-ink">Get started</a></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Projects</span><span class="text-right font-medium">3 projects</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Support</span><span class="text-right font-medium">Community</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Audit log retention</span><span class="text-right font-medium">7 days</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">SSO / SAML</span><span class="text-tfs08-line" aria-hidden="true">—</span><span class="sr-only">Not included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Role-based access</span><span class="text-tfs08-line" aria-hidden="true">—</span><span class="sr-only">Not included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">SCIM provisioning</span><span class="text-tfs08-line" aria-hidden="true">—</span><span class="sr-only">Not included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Data residency</span><span class="text-tfs08-line" aria-hidden="true">—</span><span class="sr-only">Not included</span></div>
      </article>
      <article class="relative grid gap-0 rounded-3xl bg-white p-2 lg:row-span-8 lg:grid-rows-subgrid ring-2 ring-tfs08-acc shadow-[0_30px_80px_-30px_var(--color-tfs08-acc)]">
        <p class="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full bg-tfs08-acc px-3 py-1 text-xs font-semibold text-white shadow">Most popular</p><div class="grid gap-2 rounded-2xl bg-tfs08-acc/5 p-6"><h3 class="text-xl font-semibold">Team</h3><p class="text-sm text-tfs08-mut">For product teams shipping weekly</p><p class="mt-2 text-3xl font-semibold tracking-tight">$24 / seat</p><a href="#tfs-08-h" class="mt-3 inline-flex min-h-11 items-center justify-center rounded-xl text-sm font-semibold transition focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs08-acc bg-tfs08-acc text-white hover:bg-tfs08-ink">Get started</a></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Projects</span><span class="text-right font-medium">Unlimited</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Support</span><span class="text-right font-medium">Email, 24h</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Audit log retention</span><span class="text-right font-medium">90 days</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">SSO / SAML</span><span class="grid size-6 place-items-center rounded-full bg-tfs08-acc/10 text-tfs08-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="sr-only">Included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Role-based access</span><span class="grid size-6 place-items-center rounded-full bg-tfs08-acc/10 text-tfs08-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="sr-only">Included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">SCIM provisioning</span><span class="text-tfs08-line" aria-hidden="true">—</span><span class="sr-only">Not included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Data residency</span><span class="text-tfs08-line" aria-hidden="true">—</span><span class="sr-only">Not included</span></div>
      </article>
      <article class="relative grid gap-0 rounded-3xl bg-white p-2 lg:row-span-8 lg:grid-rows-subgrid ring-1 ring-tfs08-line">
        <div class="grid gap-2 rounded-2xl bg-tfs08-bg p-6"><h3 class="text-xl font-semibold">Enterprise</h3><p class="text-sm text-tfs08-mut">For orgs with compliance needs</p><p class="mt-2 text-3xl font-semibold tracking-tight">Custom</p><a href="#tfs-08-h" class="mt-3 inline-flex min-h-11 items-center justify-center rounded-xl text-sm font-semibold transition focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs08-acc bg-white text-tfs08-ink ring-1 ring-tfs08-line hover:ring-tfs08-ink">Talk to sales</a></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Projects</span><span class="text-right font-medium">Unlimited</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Support</span><span class="text-right font-medium">Dedicated Slack, 1h SLA</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Audit log retention</span><span class="text-right font-medium">Unlimited, exportable to S3</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">SSO / SAML</span><span class="grid size-6 place-items-center rounded-full bg-tfs08-acc/10 text-tfs08-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="sr-only">Included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Role-based access</span><span class="grid size-6 place-items-center rounded-full bg-tfs08-acc/10 text-tfs08-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="sr-only">Included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">SCIM provisioning</span><span class="grid size-6 place-items-center rounded-full bg-tfs08-acc/10 text-tfs08-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="sr-only">Included</span></div>
        <div class="flex items-center justify-between gap-4 border-t border-tfs08-line/70 px-6 py-4 text-sm"><span class="text-tfs08-mut">Data residency</span><span class="grid size-6 place-items-center rounded-full bg-tfs08-acc/10 text-tfs08-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="sr-only">Included</span></div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs08-bg: #f7f7f8;
  --color-tfs08-bg: oklch(0.976 0.001 0);
  --color-tfs08-ink: #18181b;
  --color-tfs08-ink: oklch(0.21 0.006 286);
  --color-tfs08-mut: #52525b;
  --color-tfs08-mut: oklch(0.442 0.015 286);
  --color-tfs08-line: #e4e4e7;
  --color-tfs08-line: oklch(0.92 0.004 286);
  --color-tfs08-acc: #2563eb;
  --color-tfs08-acc: oklch(0.546 0.215 263);
  --font-tfs08-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-08 {
  width: 100%;
  min-height: 100svh;
}
```
