---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-arrow-key-navigation-columns/"
title: "Tailwind Mega Menu with Arrow Key Navigation Across Columns"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "A rounded fintech header where the keyboard moves like a spreadsheet."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mega Menu with Arrow Key Navigation Across Columns
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-arrow-key-navigation-columns/

A rounded fintech header where the keyboard moves like a spreadsheet. The top bar is one Tab stop with a roving tabindex (Left/Right/Home/End), ArrowDown opens a panel and lands on its first link, and inside the panel Up/Down walk a column while Left/Right jump to the same row of the neighbouring column. Escape always goes back to the trigger. A legend in the panel footer teaches the keys.
## HTML
```html
<section class="tmm-08 relative flow-root w-full min-h-svh bg-tmm08-bg bg-[radial-gradient(64rem_30rem_at_90%_-10%,color-mix(in_oklab,var(--color-tmm08-acc)_14%,transparent),transparent_62%)] font-tmm08-sans leading-normal text-tmm08-ink [&_:focus-visible]:rounded-[10px] [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm08-acc" aria-labelledby="tmm08-title">
  <h2 class="sr-only" id="tmm08-title">Prism</h2>

  <header class="relative z-10 mx-auto mt-[clamp(1rem,3vw,1.75rem)] w-[min(76rem,calc(100%-2rem))] rounded-[20px] bg-tmm08-surf shadow-tmm08-card">
    <div class="absolute top-3 right-3 z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm08-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmm08-line bg-tmm08-surf text-tmm08-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm08-acc" for="tmm08-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>
    <div class="flex min-h-17 flex-wrap items-center gap-[clamp(0.5rem,2vw,1.5rem)] pr-16 pl-[clamp(0.85rem,2vw,1.4rem)] max-[52rem]:flex-col max-[52rem]:items-stretch max-[52rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm08-display text-[1.15rem]/none font-extrabold tracking-[-0.02em] text-tmm08-ink" href="#tmm08-title">
        <svg class="size-[22px] text-tmm08-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3 21 19H3Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 3v16" stroke="currentColor" stroke-width="1.8"/></svg>
        Prism
      </a>
      <nav data-tmm08-nav class="min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-1 max-[52rem]:flex-col">
          <li data-tmm08-item>
            <button data-tmm08-trigger type="button" tabindex="0" aria-expanded="false" aria-controls="tmm08-panel-accounts" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm08-open:after:pointer-events-auto max-[52rem]:after:hidden min-h-11 cursor-pointer rounded-full px-4 font-tmm08-display text-[0.92rem]/none font-bold text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 tmm08-open:bg-tmm08-acc/16 tmm08-open:text-tmm08-acc-ink">Accounts</button>
            <div class="invisible absolute inset-x-0 top-full z-30 mt-2.5 -translate-y-1.5 scale-[0.995] rounded-[20px] bg-tmm08-surf opacity-0 shadow-tmm08-panel pointer-events-none transition-[opacity,translate,scale,visibility] duration-170 before:absolute before:inset-x-0 before:-top-3 before:h-3 tmm08-open:visible tmm08-open:translate-y-0 tmm08-open:scale-100 tmm08-open:opacity-100 tmm08-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:translate-y-0 max-[52rem]:scale-100 max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm08-open:block" id="tmm08-panel-accounts" aria-label="Accounts">
              <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.75rem,2.4vw,1.75rem)] p-[clamp(1rem,3vw,1.6rem)]">
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-personal">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-personal">Personal</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Everyday account</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Savings pots</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Joint accounts</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Currency wallets</a></li>
                  </ul>
                </section>
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-business">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-business">Business</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Company account</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Expense cards</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Payroll</a></li>
                  </ul>
                </section>
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-credit">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-credit">Credit</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Overdraft</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Business loan</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Invoice finance</a></li>
                  </ul>
                </section>
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-manage">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-manage">Manage</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Statements</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Standing orders</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Card controls</a></li>
                  </ul>
                </section>
              </div>
              <p class="flex flex-wrap items-center gap-x-4 gap-y-2 border-t border-tmm08-line px-[clamp(1rem,3vw,1.6rem)] py-3 text-[0.76rem] text-tmm08-mut max-[52rem]:hidden" aria-hidden="true"><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&larr;</kbd><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&rarr;</kbd> columns</span><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&uarr;</kbd><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&darr;</kbd> links</span><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">Esc</kbd> back to menu</span></p>
            </div>
          </li>
          <li data-tmm08-item>
            <button data-tmm08-trigger type="button" tabindex="-1" aria-expanded="false" aria-controls="tmm08-panel-payments" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm08-open:after:pointer-events-auto max-[52rem]:after:hidden min-h-11 cursor-pointer rounded-full px-4 font-tmm08-display text-[0.92rem]/none font-bold text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 tmm08-open:bg-tmm08-acc/16 tmm08-open:text-tmm08-acc-ink">Payments</button>
            <div class="invisible absolute inset-x-0 top-full z-30 mt-2.5 -translate-y-1.5 scale-[0.995] rounded-[20px] bg-tmm08-surf opacity-0 shadow-tmm08-panel pointer-events-none transition-[opacity,translate,scale,visibility] duration-170 before:absolute before:inset-x-0 before:-top-3 before:h-3 tmm08-open:visible tmm08-open:translate-y-0 tmm08-open:scale-100 tmm08-open:opacity-100 tmm08-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:translate-y-0 max-[52rem]:scale-100 max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm08-open:block" id="tmm08-panel-payments" aria-label="Payments">
              <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.75rem,2.4vw,1.75rem)] p-[clamp(1rem,3vw,1.6rem)]">
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-send">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-send">Send</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Domestic transfer</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">International</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Bulk payments</a></li>
                  </ul>
                </section>
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-collect">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-collect">Collect</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Direct debit</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Payment links</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Subscriptions</a></li>
                  </ul>
                </section>
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-fx">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-fx">Currency</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Live rates</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Forward contracts</a></li>
                  </ul>
                </section>
              </div>
              <p class="flex flex-wrap items-center gap-x-4 gap-y-2 border-t border-tmm08-line px-[clamp(1rem,3vw,1.6rem)] py-3 text-[0.76rem] text-tmm08-mut max-[52rem]:hidden" aria-hidden="true"><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&larr;</kbd><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&rarr;</kbd> columns</span><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&uarr;</kbd><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&darr;</kbd> links</span><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">Esc</kbd> back to menu</span></p>
            </div>
          </li>
          <li data-tmm08-item>
            <button data-tmm08-trigger type="button" tabindex="-1" aria-expanded="false" aria-controls="tmm08-panel-support" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm08-open:after:pointer-events-auto max-[52rem]:after:hidden min-h-11 cursor-pointer rounded-full px-4 font-tmm08-display text-[0.92rem]/none font-bold text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 tmm08-open:bg-tmm08-acc/16 tmm08-open:text-tmm08-acc-ink">Support</button>
            <div class="invisible absolute inset-x-0 top-full z-30 mt-2.5 -translate-y-1.5 scale-[0.995] rounded-[20px] bg-tmm08-surf opacity-0 shadow-tmm08-panel pointer-events-none transition-[opacity,translate,scale,visibility] duration-170 before:absolute before:inset-x-0 before:-top-3 before:h-3 tmm08-open:visible tmm08-open:translate-y-0 tmm08-open:scale-100 tmm08-open:opacity-100 tmm08-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:translate-y-0 max-[52rem]:scale-100 max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm08-open:block" id="tmm08-panel-support" aria-label="Support">
              <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.75rem,2.4vw,1.75rem)] p-[clamp(1rem,3vw,1.6rem)]">
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-help">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-help">Help</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Contact the team</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Dispute a payment</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Lost card</a></li>
                  </ul>
                </section>
                <section data-tmm08-col class="min-w-0" aria-labelledby="tmm08-h-status">
                  <h3 class="mb-1.5 font-tmm08-display text-[0.72rem]/none font-extrabold tracking-[0.12em] text-tmm08-mut uppercase" id="tmm08-h-status">Service</h3>
                  <ul class="grid gap-0.5">
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Status page</a></li>
                    <li><a href="#tmm08-title" class="-mx-2.5 flex min-h-11 min-w-0 items-center rounded-[10px] px-2.5 text-[0.92rem] text-tmm08-ink transition-colors hover:bg-tmm08-acc/10 hover:text-tmm08-acc focus-visible:bg-tmm08-acc/10">Planned maintenance</a></li>
                  </ul>
                </section>
              </div>
              <p class="flex flex-wrap items-center gap-x-4 gap-y-2 border-t border-tmm08-line px-[clamp(1rem,3vw,1.6rem)] py-3 text-[0.76rem] text-tmm08-mut max-[52rem]:hidden" aria-hidden="true"><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&larr;</kbd><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&rarr;</kbd> columns</span><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&uarr;</kbd><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">&darr;</kbd> links</span><span class="inline-flex items-center gap-1.5"><kbd class="inline-grid h-6 min-w-6 place-items-center rounded-md border border-tmm08-line bg-tmm08-bg px-1 font-tmm08-display text-[0.7rem]/none font-bold text-tmm08-ink">Esc</kbd> back to menu</span></p>
            </div>
          </li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1.5 max-[52rem]:ml-0">
        <a class="inline-flex min-h-11 items-center px-3 font-tmm08-display text-[0.88rem]/none font-bold text-tmm08-mut hover:text-tmm08-ink" href="#tmm08-title">Log in</a>
        <a class="inline-flex min-h-11 items-center rounded-full bg-tmm08-acc px-4.5 font-tmm08-display text-[0.88rem]/none font-bold text-tmm08-on-acc hover:brightness-110" href="#tmm08-title">Open an account</a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(76rem,calc(100%-2rem))] py-[clamp(2rem,6vw,3.5rem)]">
    <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))] gap-3.5">
      <article class="grid min-w-0 gap-1 rounded-[18px] bg-tmm08-surf px-5 py-4.5 shadow-tmm08-card"><p class="font-tmm08-display text-[0.7rem]/none font-extrabold tracking-[0.16em] text-tmm08-mut uppercase">Everyday</p><p class="font-tmm08-display text-[clamp(1.4rem,4vw,1.9rem)]/none font-extrabold tracking-[-0.02em] tabular-nums">&pound;4,182.60</p><p class="text-[0.8rem] text-tmm08-mut">Prism Everyday &middot; &bull;&bull;&bull;&bull; 4417</p></article>
      <article class="grid min-w-0 gap-1 rounded-[18px] bg-[color-mix(in_oklab,var(--color-tmm08-acc)_14%,var(--color-tmm08-surf))] px-5 py-4.5 shadow-tmm08-card"><p class="font-tmm08-display text-[0.7rem]/none font-extrabold tracking-[0.16em] text-tmm08-mut uppercase">Savings</p><p class="font-tmm08-display text-[clamp(1.4rem,4vw,1.9rem)]/none font-extrabold tracking-[-0.02em] tabular-nums">&pound;12,940.00</p><p class="text-[0.8rem] text-tmm08-mut">4.6% AER &middot; paid monthly</p></article>
      <article class="grid min-w-0 gap-1 rounded-[18px] bg-tmm08-surf px-5 py-4.5 shadow-tmm08-card"><p class="font-tmm08-display text-[0.7rem]/none font-extrabold tracking-[0.16em] text-tmm08-mut uppercase">Business</p><p class="font-tmm08-display text-[clamp(1.4rem,4vw,1.9rem)]/none font-extrabold tracking-[-0.02em] tabular-nums">&pound;38,205.14</p><p class="text-[0.8rem] text-tmm08-mut">Fern Studio Ltd</p></article>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm08-bg: #eef4f1;
  --color-tmm08-bg: oklch(0.962 0.01 165);
  --color-tmm08-surf: #ffffff;
  --color-tmm08-surf: oklch(1 0 0);
  --color-tmm08-line: #d3e0da;
  --color-tmm08-line: oklch(0.895 0.018 165);
  --color-tmm08-ink: #17211d;
  --color-tmm08-ink: oklch(0.23 0.015 165);
  --color-tmm08-mut: #56655f;
  --color-tmm08-mut: oklch(0.48 0.02 165);
  --color-tmm08-acc: #047857;
  --color-tmm08-acc: oklch(0.5 0.12 165);
  --color-tmm08-acc-ink: #035e45;
  --color-tmm08-acc-ink: oklch(0.42 0.1 165);
  --color-tmm08-on-acc: #ffffff;
  --color-tmm08-on-acc: oklch(1 0 0);
  --font-tmm08-display: 'Nunito', ui-rounded, system-ui, sans-serif;
  --font-tmm08-sans: 'DM Sans', system-ui, sans-serif;
  --shadow-tmm08-card: 0 16px 40px -26px rgb(23 33 29 / 0.6);
  --shadow-tmm08-panel: 0 26px 60px -30px rgb(23 33 29 / 0.7);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm08-open: instead of a repeated selector list. */

@custom-variant tmm08-open {
  &:where([data-tmm08-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm08-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-08 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-08:has(#tmm08-theme:checked) {
  --color-tmm08-bg: #0a1310;
  --color-tmm08-bg: oklch(0.17 0.015 165);
  --color-tmm08-surf: #121e19;
  --color-tmm08-surf: oklch(0.22 0.02 165);
  --color-tmm08-line: #23342c;
  --color-tmm08-line: oklch(0.31 0.025 165);
  --color-tmm08-ink: #e9f3ee;
  --color-tmm08-ink: oklch(0.95 0.012 165);
  --color-tmm08-mut: #9ab0a6;
  --color-tmm08-mut: oklch(0.74 0.025 165);
  --color-tmm08-acc: #34d399;
  --color-tmm08-acc: oklch(0.8 0.14 165);
  --color-tmm08-acc-ink: #6ee7b7;
  --color-tmm08-acc-ink: oklch(0.86 0.12 165);
  --color-tmm08-on-acc: #04231a;
  --color-tmm08-on-acc: oklch(0.22 0.04 165);
}

@media (prefers-color-scheme: dark) {
  .tmm-08 {
    --color-tmm08-bg: #0a1310;
    --color-tmm08-bg: oklch(0.17 0.015 165);
    --color-tmm08-surf: #121e19;
    --color-tmm08-surf: oklch(0.22 0.02 165);
    --color-tmm08-line: #23342c;
    --color-tmm08-line: oklch(0.31 0.025 165);
    --color-tmm08-ink: #e9f3ee;
    --color-tmm08-ink: oklch(0.95 0.012 165);
    --color-tmm08-mut: #9ab0a6;
    --color-tmm08-mut: oklch(0.74 0.025 165);
    --color-tmm08-acc: #34d399;
    --color-tmm08-acc: oklch(0.8 0.14 165);
    --color-tmm08-acc-ink: #6ee7b7;
    --color-tmm08-acc-ink: oklch(0.86 0.12 165);
    --color-tmm08-on-acc: #04231a;
    --color-tmm08-on-acc: oklch(0.22 0.04 165);
  }

  .tmm-08:has(#tmm08-theme:checked) {
    --color-tmm08-bg: #eef4f1;
    --color-tmm08-bg: oklch(0.962 0.01 165);
    --color-tmm08-surf: #ffffff;
    --color-tmm08-surf: oklch(1 0 0);
    --color-tmm08-line: #d3e0da;
    --color-tmm08-line: oklch(0.895 0.018 165);
    --color-tmm08-ink: #17211d;
    --color-tmm08-ink: oklch(0.23 0.015 165);
    --color-tmm08-mut: #56655f;
    --color-tmm08-mut: oklch(0.48 0.02 165);
    --color-tmm08-acc: #047857;
    --color-tmm08-acc: oklch(0.5 0.12 165);
    --color-tmm08-acc-ink: #035e45;
    --color-tmm08-acc-ink: oklch(0.42 0.1 165);
    --color-tmm08-on-acc: #ffffff;
    --color-tmm08-on-acc: oklch(1 0 0);
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tmm-08');
  if (!root || root.__tmmCleanup) return;
  const nav = root.querySelector('[data-tmm08-nav]');
  const triggers = [...nav.querySelectorAll('[data-tmm08-trigger]')];

  const setOpen = (item, on) => {
    item.toggleAttribute('data-open', on);
    item.querySelector('[data-tmm08-trigger]').setAttribute('aria-expanded', String(on));
  };
  const closeAll = (except) => nav.querySelectorAll('[data-tmm08-item][data-open]').forEach((i) => { if (i !== except) setOpen(i, false); });
  const rove = (i) => { triggers.forEach((t, n) => { t.tabIndex = n === i ? 0 : -1; }); triggers[i].focus(); };
  const grid = (item) => [...item.querySelectorAll('[data-tmm08-col]')].map((c) => [...c.querySelectorAll('a')]);
  const where = (cols, a) => { for (let c = 0; c < cols.length; c++) { const r = cols[c].indexOf(a); if (r > -1) return [c, r]; } return null; };

  const onKey = (e) => {
    const item = e.target.closest('[data-tmm08-item]');
    if (!item) return;
    const trigger = item.querySelector('[data-tmm08-trigger]');
    if (e.key === 'Escape') { e.preventDefault(); setOpen(item, false); trigger.focus(); return; }

    if (e.target === trigger) {
      const i = triggers.indexOf(trigger), n = triggers.length;
      const go = { ArrowRight: (i + 1) % n, ArrowLeft: (i - 1 + n) % n, Home: 0, End: n - 1 }[e.key];
      if (go !== undefined) { e.preventDefault(); const wasOpen = item.hasAttribute('data-open'); closeAll(); rove(go); if (wasOpen) setOpen(triggers[go].closest('[data-tmm08-item]'), true); return; }
      if (e.key === 'ArrowDown') { e.preventDefault(); closeAll(item); setOpen(item, true); grid(item)[0][0]?.focus(); }
      return;
    }

    // Inside the panel: a real 2-D grid. Up/Down within a column, Left/Right to the same row of the next column.
    const cols = grid(item), pos = where(cols, e.target);
    if (!pos) return;
    let [c, r] = pos;
    if (e.key === 'ArrowDown') r = Math.min(r + 1, cols[c].length - 1);
    else if (e.key === 'ArrowUp') { if (r === 0) { e.preventDefault(); trigger.focus(); return; } r -= 1; }
    else if (e.key === 'ArrowRight') { c = (c + 1) % cols.length; r = Math.min(r, cols[c].length - 1); }
    else if (e.key === 'ArrowLeft') { c = (c - 1 + cols.length) % cols.length; r = Math.min(r, cols[c].length - 1); }
    else if (e.key === 'Home') r = 0;
    else if (e.key === 'End') r = cols[c].length - 1;
    else return;
    e.preventDefault();
    cols[c][r].focus();
  };
  const onClick = (e) => {
    const t = e.target.closest('[data-tmm08-trigger]');
    if (!t) return;
    const item = t.closest('[data-tmm08-item]');
    const open = item.hasAttribute('data-open');
    closeAll(); setOpen(item, !open);
    rove(triggers.indexOf(t));
  };
  const onFocusOut = (e) => {
    const item = e.target.closest('[data-tmm08-item]');
    if (item && (!e.relatedTarget || !item.contains(e.relatedTarget))) setOpen(item, false);
  };

  nav.addEventListener('keydown', onKey);
  nav.addEventListener('click', onClick);
  nav.addEventListener('focusout', onFocusOut);
  root.__tmmCleanup = () => {
    nav.removeEventListener('keydown', onKey);
    nav.removeEventListener('click', onClick);
    nav.removeEventListener('focusout', onFocusOut);
  };
})();
```
