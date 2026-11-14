---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-saas-features-section-grid/"
title: "Tailwind SaaS Features Section Grid"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "A modern SaaS feature grid with a split header (headline left, summary + CTA right), a wide featured card with a drawn dashboard, and four supporting cards."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS Features Section Grid
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-saas-features-section-grid/

A modern SaaS feature grid with a split header (headline left, summary + CTA right), a wide featured card with a drawn dashboard, and four supporting cards. Cards reveal a gradient border on hover via a padding-box/border-box background pair, and the whole block reflows from one to three columns.
## HTML
```html
<section class="tfs-19 w-full min-h-svh bg-tfs19-bg px-5 py-20 font-tfs19-sans text-tfs19-ink antialiased sm:py-28" aria-labelledby="tfs-19-h">
  <div class="mx-auto grid w-full max-w-6xl gap-14">
    <header class="grid gap-6 lg:grid-cols-2 lg:items-end">
      <div class="grid gap-4"><p class="font-tfs19-mono text-xs uppercase tracking-[0.18em] text-tfs19-acc">Platform</p><h2 id="tfs-19-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">The revenue stack, finally in one place</h2></div>
      <div class="grid gap-5 lg:justify-items-start"><p class="text-pretty text-lg text-tfs19-mut">Billing, usage metering and revenue analytics share one data model — so finance and product stop arguing over whose number is right.</p><a href="#tfs-19-h" class="group inline-flex min-h-11 items-center gap-2 rounded-full bg-tfs19-ink px-5 text-sm font-semibold text-white transition hover:bg-tfs19-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs19-acc">Book a demo <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-hover:translate-x-0.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>
    </header>
    <div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
      <article class="grid gap-8 overflow-hidden rounded-3xl bg-tfs19-ink p-8 text-white sm:col-span-2 lg:grid-cols-[1fr_1.2fr] lg:items-center">
        <div class="grid gap-3"><span class="font-tfs19-mono text-xs text-tfs19-acc2">FEATURED</span><h3 class="text-2xl font-semibold">Usage-based billing</h3><p class="text-pretty text-white/70">Meter any event, price it any way — tiers, credits, commits — and invoice automatically.</p></div>
        <div aria-hidden="true" class="grid gap-3 rounded-2xl bg-white/5 p-5 ring-1 ring-white/10">
          <div class="flex items-center justify-between text-xs text-white/70"><span>API calls · Vale Inc.</span><span class="font-tfs19-mono">Sep 2026</span></div>
          <div class="flex h-24 items-end gap-1.5"><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:30%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:42%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:38%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:55%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:48%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:62%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:58%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:70%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:66%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:82%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:78%"></i><i class="flex-1 rounded-t bg-linear-to-t from-tfs19-acc to-tfs19-acc2" style="height:94%"></i></div>
          <div class="flex items-center justify-between border-t border-white/10 pt-3 text-sm"><span class="text-white/70">Next invoice</span><span class="font-semibold tabular-nums">$18,240.00</span></div>
        </div>
      </article>
      <article class="group grid content-start gap-4 rounded-3xl border border-tfs19-line bg-white p-7 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:shadow-[0_24px_50px_-28px_var(--color-tfs19-acc)] hover:[background:linear-gradient(#fff,#fff)_padding-box,linear-gradient(135deg,var(--color-tfs19-acc),var(--color-tfs19-acc2))_border-box]">
        <div class="flex items-center justify-between"><span class="grid size-11 place-items-center rounded-xl bg-tfs19-soft text-tfs19-acc transition group-hover:bg-tfs19-acc group-hover:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M3 3v18h18M7 15l4-4 3 3 5-6"/></svg></span><span class="font-tfs19-mono text-xs text-tfs19-mut">01</span></div>
        <h3 class="text-lg font-semibold">Revenue analytics</h3>
        <p class="text-pretty text-sm leading-relaxed text-tfs19-mut">MRR, NRR and cohort retention computed from the ledger, not a CSV.</p>
      </article>
      <article class="group grid content-start gap-4 rounded-3xl border border-tfs19-line bg-white p-7 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:shadow-[0_24px_50px_-28px_var(--color-tfs19-acc)] hover:[background:linear-gradient(#fff,#fff)_padding-box,linear-gradient(135deg,var(--color-tfs19-acc),var(--color-tfs19-acc2))_border-box]">
        <div class="flex items-center justify-between"><span class="grid size-11 place-items-center rounded-xl bg-tfs19-soft text-tfs19-acc transition group-hover:bg-tfs19-acc group-hover:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 3v5h-5"/></svg></span><span class="font-tfs19-mono text-xs text-tfs19-mut">02</span></div>
        <h3 class="text-lg font-semibold">Smart dunning</h3>
        <p class="text-pretty text-sm leading-relaxed text-tfs19-mut">Retries timed to each card network recover 38% of failed payments.</p>
      </article>
      <article class="group grid content-start gap-4 rounded-3xl border border-tfs19-line bg-white p-7 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:shadow-[0_24px_50px_-28px_var(--color-tfs19-acc)] hover:[background:linear-gradient(#fff,#fff)_padding-box,linear-gradient(135deg,var(--color-tfs19-acc),var(--color-tfs19-acc2))_border-box]">
        <div class="flex items-center justify-between"><span class="grid size-11 place-items-center rounded-xl bg-tfs19-soft text-tfs19-acc transition group-hover:bg-tfs19-acc group-hover:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg></span><span class="font-tfs19-mono text-xs text-tfs19-mut">03</span></div>
        <h3 class="text-lg font-semibold">Global tax</h3>
        <p class="text-pretty text-sm leading-relaxed text-tfs19-mut">Sales tax, VAT and GST calculated and filed in 40+ countries.</p>
      </article>
      <article class="group grid content-start gap-4 rounded-3xl border border-tfs19-line bg-white p-7 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:shadow-[0_24px_50px_-28px_var(--color-tfs19-acc)] hover:[background:linear-gradient(#fff,#fff)_padding-box,linear-gradient(135deg,var(--color-tfs19-acc),var(--color-tfs19-acc2))_border-box]">
        <div class="flex items-center justify-between"><span class="grid size-11 place-items-center rounded-xl bg-tfs19-soft text-tfs19-acc transition group-hover:bg-tfs19-acc group-hover:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0V8zM12 18v4"/></svg></span><span class="font-tfs19-mono text-xs text-tfs19-mut">04</span></div>
        <h3 class="text-lg font-semibold">Warehouse sync</h3>
        <p class="text-pretty text-sm leading-relaxed text-tfs19-mut">Every billing event lands in Snowflake or BigQuery within a minute.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs19-bg: #f7f8fb;
  --color-tfs19-bg: oklch(0.979 0.004 271);
  --color-tfs19-soft: #eef0ff;
  --color-tfs19-soft: oklch(0.958 0.02 280);
  --color-tfs19-ink: #0b1023;
  --color-tfs19-ink: oklch(0.18 0.04 271);
  --color-tfs19-mut: #4f566b;
  --color-tfs19-mut: oklch(0.455 0.035 271);
  --color-tfs19-line: #e3e6ef;
  --color-tfs19-line: oklch(0.925 0.013 271);
  --color-tfs19-acc: #4f46e5;
  --color-tfs19-acc: oklch(0.511 0.23 277);
  --color-tfs19-acc2: #06b6d4;
  --color-tfs19-acc2: oklch(0.715 0.126 215);
  --font-tfs19-sans: 'Sora', system-ui, sans-serif;
  --font-tfs19-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-19 {
  width: 100%;
  min-height: 100svh;
}
```
