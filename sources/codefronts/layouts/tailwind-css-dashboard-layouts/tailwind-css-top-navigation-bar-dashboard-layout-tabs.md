---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-top-navigation-bar-dashboard-layout-tabs/"
title: "Tailwind CSS Top Navigation Bar Dashboard Layout with Tabs"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "The GitHub / Stripe school: no sidebar &mdash; a global top bar, a sticky tab strip with an animated underline, and content in a centred…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Top Navigation Bar Dashboard Layout with Tabs
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-top-navigation-bar-dashboard-layout-tabs/

The GitHub / Stripe school: no sidebar &mdash; a global top bar, a sticky tab strip with an animated underline, and content in a centred w-[min(100%_-_3rem,57.5rem)] column. Tabs are radios: group-has-[#tdl17-t2:checked]/page:grid swaps the panes and has-checked:after:scale-x-100 slides each underline in. New in the port: panes fade in with starting:, the tab strip scrolls horizontally on phones, and invoices and plans gained real status and “Current” affordances.
## HTML
```html
<section class="tdl-17 w-full min-h-svh bg-tdl17-bg font-tdl17-sans text-tdl17-ink antialiased" aria-label="Top-bar navigation dashboard demo">
  <div class="group/page flex h-svh min-h-[32rem] flex-col overflow-hidden">
    <header class="flex h-14 flex-none items-center gap-3.5 bg-tdl17-bar px-4.5 text-tdl17-barink">
      <span aria-hidden="true" class="size-6 flex-none rounded-full bg-[conic-gradient(from_200deg,var(--color-tdl17-acc),var(--color-tdl17-acc2),var(--color-tdl17-acc))]"></span>
      <nav aria-label="Breadcrumb" class="flex min-w-0 items-center gap-2 text-[14px]"><a href="#org" class="truncate rounded-sm font-semibold text-tdl17-barmut no-underline underline-offset-3 hover:text-white hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl17-acc2">acme-inc</a><span aria-hidden="true" class="opacity-45">/</span><b class="font-bold">billing</b></nav>
      <label class="ml-auto flex h-9 w-[min(16rem,40%)] items-center gap-2 rounded-lg border border-tdl17-baredge px-2.5 text-xs text-tdl17-barmut transition focus-within:border-tdl17-acc2 focus-within:bg-white/5 max-sm:hidden"><span class="sr-only">Jump to</span><input type="search" placeholder="Jump to…" class="min-w-0 flex-1 bg-transparent text-white outline-none placeholder:text-tdl17-barmut"><kbd class="rounded border border-tdl17-baredge px-1.5 font-sans text-[10px]">/</kbd></label>
      <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-linear-140 from-tdl17-acc to-tdl17-acc3 text-[11px] font-bold text-white max-sm:ml-auto">AR</span>
    </header>
    <div class="flex min-h-0 flex-1 flex-col overflow-y-auto overscroll-contain [scrollbar-gutter:stable]">
      <div class="sticky top-0 z-10 border-b border-tdl17-edge bg-tdl17-bg/80 backdrop-blur-md">
        <fieldset class="mx-auto flex w-[min(100%_-_3rem,57.5rem)] gap-1 overflow-x-auto [scrollbar-width:none] [&>label]:relative [&>label]:flex-none [&>label]:cursor-pointer [&>label]:rounded-t-lg [&>label]:px-3.5 [&>label]:pt-3.5 [&>label]:pb-3 [&>label]:text-[14px] [&>label]:font-semibold [&>label]:text-tdl17-mut [&>label]:transition-colors [&>label:hover]:bg-tdl17-hover [&>label:hover]:text-tdl17-ink [&>label:has(:checked)]:text-tdl17-ink [&>label:has(:focus-visible)]:outline-2 [&>label:has(:focus-visible)]:-outline-offset-2 [&>label:has(:focus-visible)]:outline-tdl17-acc [&>label]:after:absolute [&>label]:after:inset-x-2 [&>label]:after:-bottom-px [&>label]:after:h-0.75 [&>label]:after:scale-x-0 [&>label]:after:rounded-full [&>label]:after:bg-tdl17-acc [&>label]:after:transition-transform [&>label]:after:duration-250 [&>label]:after:ease-[cubic-bezier(.2,.7,.2,1)] [&>label]:after:content-[''] [&>label:has(:checked)]:after:scale-x-100">
          <legend class="sr-only">Billing sections</legend>
          <label><input class="sr-only" type="radio" name="tdl17" id="tdl17-t1" checked>Overview</label>
          <label><input class="sr-only" type="radio" name="tdl17" id="tdl17-t2">Plans</label>
          <label><input class="sr-only" type="radio" name="tdl17" id="tdl17-t3">Danger zone</label>
        </fieldset>
      </div>
      <main class="mx-auto w-[min(100%_-_3rem,57.5rem)] pt-6 pb-8 *:gap-4 *:transition-[opacity,translate] *:duration-300 *:starting:translate-y-1.5 *:starting:opacity-0 [&_h1]:text-[22px] [&_h1]:font-bold [&_h1]:tracking-tight [&_article]:grid [&_article]:content-start [&_article]:justify-items-start [&_article]:gap-2 [&_article]:rounded-xl [&_article]:border [&_article]:border-tdl17-edge [&_article]:bg-tdl17-panel [&_article]:px-5 [&_article]:py-4.5 [&_h3]:text-[11px] [&_h3]:font-bold [&_h3]:tracking-[0.1em] [&_h3]:text-tdl17-mut [&_h3]:uppercase [&_.big]:text-[28px] [&_.big]:font-bold [&_.big]:tracking-tight [&_.big]:tabular-nums [&_article_small]:text-[13px] [&_article_small]:text-tdl17-mut [&_button]:h-10 [&_button]:cursor-pointer [&_button]:rounded-lg [&_button]:px-3.5 [&_button]:text-[13px] [&_button]:font-semibold [&_button]:transition-colors [&_button:focus-visible]:outline-2 [&_button:focus-visible]:outline-offset-2 [&_button:focus-visible]:outline-tdl17-acc [&_.ghost]:border [&_.ghost]:border-tdl17-edge [&_.ghost]:bg-tdl17-bg [&_.ghost:hover]:border-tdl17-mut/50">
        <div class="hidden group-has-[#tdl17-t1:checked]/page:grid">
          <h1>Billing overview</h1>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(min(15rem,100%),1fr))] gap-4">
            <article><h3>Current plan</h3><p class="big">Team</p><small>$96 / month · renews Oct 12</small><button type="button" class="ghost">Manage plan</button></article>
            <article><h3>Usage this cycle</h3><p class="big">64%</p><span aria-hidden="true" class="h-1.75 w-full overflow-hidden rounded-full bg-tdl17-track"><i class="block h-full w-[64%] rounded-full bg-linear-to-r from-tdl17-acc to-tdl17-acc2"></i></span><small>12,800 / 20,000 build minutes</small></article>
          </div>
          <article>
            <h3>Invoices</h3>
            <ul class="w-full [&>li]:flex [&>li]:items-center [&>li]:gap-3 [&>li]:border-b [&>li]:border-tdl17-edge/55 [&>li]:py-2.5 [&>li]:text-[14px] [&>li:last-child]:border-b-0 [&_b]:mr-auto [&_b]:font-semibold [&_.amt]:text-tdl17-mut [&_.amt]:tabular-nums [&_a]:rounded-sm [&_a]:text-[13px] [&_a]:font-bold [&_a]:text-tdl17-acc [&_a]:no-underline [&_a]:underline-offset-3 [&_a:hover]:underline [&_a:focus-visible]:outline-2 [&_a:focus-visible]:outline-offset-2 [&_a:focus-visible]:outline-tdl17-acc [&_.paid]:rounded-full [&_.paid]:bg-tdl17-good/12 [&_.paid]:px-2 [&_.paid]:py-0.5 [&_.paid]:text-[11px] [&_.paid]:font-bold [&_.paid]:text-tdl17-good">
              <li><b>#0093 · September 2026</b><span class="paid">Paid</span><span class="amt">$96.00</span><a href="#dl">PDF</a></li>
              <li><b>#0091 · August 2026</b><span class="paid">Paid</span><span class="amt">$96.00</span><a href="#dl">PDF</a></li>
              <li><b>#0087 · July 2026</b><span class="paid">Paid</span><span class="amt">$84.00</span><a href="#dl">PDF</a></li>
            </ul>
          </article>
        </div>
        <div class="hidden group-has-[#tdl17-t2:checked]/page:grid">
          <h1>Plans</h1>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(min(14rem,100%),1fr))] gap-4">
            <article><h3>Starter</h3><p class="big">$0</p><small>2 seats · 2k minutes</small><button type="button" class="ghost">Downgrade</button></article>
            <article class="relative border-tdl17-acc/60! shadow-[0_0_0_3px_var(--color-tdl17-ring)]"><span class="absolute top-3.5 right-3.5 rounded-full bg-tdl17-acc px-2 py-0.5 text-[10.5px] font-bold text-white">Current</span><h3>Team</h3><p class="big">$96</p><small>10 seats · 20k minutes</small><button type="button" class="ghost" disabled aria-disabled="true">Your plan</button></article>
            <article><h3>Scale</h3><p class="big">$290</p><small>25 seats · 80k minutes</small><button type="button" class="bg-tdl17-acc text-white hover:bg-tdl17-accdark">Upgrade</button></article>
          </div>
        </div>
        <div class="hidden group-has-[#tdl17-t3:checked]/page:grid">
          <h1>Danger zone</h1>
          <article class="border-tdl17-red/35!"><h3>Cancel subscription</h3><p class="text-[13.5px]/[1.55] text-tdl17-mut">Billing stops at cycle end; data is retained for 90 days.</p><button type="button" class="border border-tdl17-red/45 bg-tdl17-red/7 text-tdl17-red hover:bg-tdl17-red/14">Cancel plan…</button></article>
          <article class="border-tdl17-red/35!"><h3>Delete organization</h3><p class="text-[13.5px]/[1.55] text-tdl17-mut">Permanently removes acme-inc, its repositories and audit history.</p><button type="button" class="border border-tdl17-red/45 bg-tdl17-red/7 text-tdl17-red hover:bg-tdl17-red/14">Delete organization…</button></article>
        </div>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl17-bg: #f8f9fb;
  --color-tdl17-bg: oklch(0.98 0.003 250);
  --color-tdl17-panel: #ffffff;
  --color-tdl17-panel: oklch(1 0 0);
  --color-tdl17-hover: #eef0f3;
  --color-tdl17-hover: oklch(0.948 0.006 250);
  --color-tdl17-track: #e9ecf0;
  --color-tdl17-track: oklch(0.935 0.006 250);
  --color-tdl17-edge: #dfe3e8;
  --color-tdl17-edge: oklch(0.905 0.008 250);
  --color-tdl17-ink: #22272f;
  --color-tdl17-ink: oklch(0.25 0.015 250);
  --color-tdl17-mut: #575e6a;
  --color-tdl17-mut: oklch(0.47 0.015 250);
  --color-tdl17-bar: #1b2130;
  --color-tdl17-bar: oklch(0.23 0.02 260);
  --color-tdl17-barink: #f0f2f5;
  --color-tdl17-barink: oklch(0.96 0.005 250);
  --color-tdl17-barmut: #b6bdc8;
  --color-tdl17-barmut: oklch(0.8 0.015 250);
  --color-tdl17-baredge: #3b4354;
  --color-tdl17-baredge: oklch(0.37 0.02 260);
  --color-tdl17-acc: #2962c4;
  --color-tdl17-acc: oklch(0.52 0.16 257);
  --color-tdl17-accdark: #1f4e9e;
  --color-tdl17-accdark: oklch(0.45 0.14 257);
  --color-tdl17-acc2: #43aecf;
  --color-tdl17-acc2: oklch(0.71 0.11 215);
  --color-tdl17-acc3: #8b5cd6;
  --color-tdl17-acc3: oklch(0.6 0.16 295);
  --color-tdl17-ring: #dbe6f8;
  --color-tdl17-ring: oklch(0.92 0.03 257);
  --color-tdl17-good: #17804a;
  --color-tdl17-good: oklch(0.52 0.13 155);
  --color-tdl17-red: #c3352b;
  --color-tdl17-red: oklch(0.55 0.19 27);
  --font-tdl17-sans: 'Mona Sans', system-ui, sans-serif;
}

.tdl-17 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-17 * {
    transition: none !important;
  }
}
```
