---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-accordion-tabs-with-details-and-summary-no-js/"
title: "Tailwind Accordion Tabs with Details and Summary (No JS)"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A product FAQ that is a plain accordion in a narrow column and becomes vertical tabs once its card reaches 46rem &mdash; built from five native <details…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accordion Tabs with Details and Summary (No JS)
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-accordion-tabs-with-details-and-summary-no-js/

A product FAQ that is a plain accordion in a narrow column and becomes vertical tabs once its card reaches 46rem &mdash; built from five native <details name="tvt-08-faq"> elements and zero JavaScript. group-open: styles each summary, v4's details-content: variant animates the open height, and one container-query prefix lifts every answer into a right-hand reading pane.
## HTML
```html
<section class="tvt-08 w-full min-h-svh grid place-items-center bg-tvt08-bg bg-[radial-gradient(75%_55%_at_50%_100%,var(--color-tvt08-glow),transparent_70%)] px-4 py-14 font-tvt08-sans text-tvt08-ink antialiased [interpolate-size:allow-keywords] sm:px-6" aria-label="Tailwind accordion tabs with details and summary demo">
  <div class="grid w-full max-w-[58rem] justify-items-center gap-7">
    <header class="grid max-w-[40rem] justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt08-card px-3 py-1.5 font-tvt08-mono text-[11.5px] text-tvt08-acc-ink ring-1 ring-tvt08-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt08-acc shadow-[0_0_0_3px] shadow-tvt08-acc/30"></span>&lt;details name&gt; · @container</p>
      <h2 class="font-tvt08-serif text-[clamp(32px,5vw,48px)] leading-[1.02] font-semibold tracking-[-0.025em] text-balance">Accordion first, <em class="bg-linear-to-r from-tvt08-hl to-tvt08-hl2 bg-clip-text pe-1 text-transparent">tabs when there's room</em></h2>
      <p class="max-w-[46ch] text-[15px] leading-relaxed text-tvt08-mut text-pretty">Five native disclosures. Narrow, they stack; once the card is 46rem wide, each answer lifts into a reading pane. Resize the frame.</p>
    </header>

    <article class="w-full overflow-hidden rounded-[26px] bg-tvt08-card shadow-tvt08-card ring-1 ring-tvt08-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <div class="flex flex-wrap items-center gap-x-4 gap-y-2 border-b border-tvt08-line bg-tvt08-sub px-5 py-4 sm:px-6">
        <span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-linear-to-br from-tvt08-acc to-tvt08-acc2 font-tvt08-serif text-[17px] font-bold text-tvt08-on shadow-tvt08-pill">A</span>
        <div class="min-w-[12rem] flex-1 leading-tight"><p class="text-[15px] font-semibold">Aurum Scale — Help centre</p><p class="text-[12.5px] text-tvt08-mut">Answers for orders, returns and care</p></div>
        <p class="inline-flex items-center gap-1.5 text-[12.5px] font-medium text-tvt08-mut"><span aria-hidden="true" class="size-2 rounded-full bg-tvt08-ok shadow-[0_0_0_3px] shadow-tvt08-ok/25"></span>Support online · replies in 4 min</p>
      </div>
      <div class="@container">
        <div class="relative py-0 @min-[46rem]:min-h-[26rem] @min-[46rem]:pe-[62%] @min-[46rem]:py-3">
          <p aria-hidden="true" class="hidden place-content-center justify-items-center gap-2 text-center text-[14px] text-tvt08-mut @min-[46rem]:absolute @min-[46rem]:inset-y-0 @min-[46rem]:end-0 @min-[46rem]:start-[38%] @min-[46rem]:grid @min-[46rem]:border-s @min-[46rem]:border-tvt08-line"><svg viewBox="0 0 20 20" width="22" height="22" focusable="false" class="text-tvt08-acc-ink"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>Choose a question to read the answer</p>

          <details name="tvt-08-faq" class="group border-b border-tvt08-line last:border-b-0 details-content:h-0 details-content:overflow-hidden details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-350 details-content:ease-[cubic-bezier(.32,.72,.3,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none @min-[46rem]:border-b-0 @min-[46rem]:details-content:overflow-visible" open>
            <summary class="relative flex min-h-16 cursor-pointer list-none items-center gap-3.5 px-5 py-3 text-tvt08-ink outline-none transition-colors duration-200 select-none hover:bg-tvt08-acc/[0.07] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt08-ring group-open:bg-tvt08-acc/[0.1] motion-reduce:transition-none sm:px-6 [&::-webkit-details-marker]:hidden @min-[46rem]:min-h-[4.25rem] @min-[46rem]:rounded-2xl @min-[46rem]:mx-2 @min-[46rem]:my-0.5 @min-[46rem]:px-4 @min-[46rem]:group-open:bg-tvt08-tab @min-[46rem]:group-open:shadow-tvt08-tab before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt08-acc before:to-tvt08-acc2 before:transition-transform before:duration-300 group-open:before:scale-y-100 @min-[46rem]:before:-start-2 motion-reduce:before:transition-none">
              <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt08-acc/12 text-tvt08-acc-ink ring-1 ring-tvt08-acc/20 transition-[background-color,color,box-shadow] duration-300 group-open:bg-linear-to-br group-open:from-tvt08-acc group-open:to-tvt08-acc2 group-open:text-tvt08-on group-open:shadow-tvt08-pill group-open:ring-0"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><path d="M2.5 5.5h9v8h-9zM11.5 8.5h3l2.5 2.5v2.5h-5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="6" cy="14.5" r="1.6" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="14" cy="14.5" r="1.6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></span>
              <span class="min-w-0 flex-1"><span class="block text-[15px] leading-snug font-semibold tracking-[-0.01em]">Shipping &amp; delivery</span><span class="mt-0.5 block truncate text-[12.5px] text-tvt08-mut">Costs, carriers and transit times</span></span>
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 text-tvt08-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-open:rotate-180 group-open:text-tvt08-acc-ink motion-reduce:transition-none @min-[46rem]:-rotate-90 @min-[46rem]:group-open:-rotate-90"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </summary>
            <div class="px-5 pt-1 pb-6 sm:px-6 @min-[46rem]:absolute @min-[46rem]:inset-y-0 @min-[46rem]:end-0 @min-[46rem]:start-[38%] @min-[46rem]:overflow-auto @min-[46rem]:overscroll-contain @min-[46rem]:bg-tvt08-card @min-[46rem]:border-s @min-[46rem]:border-tvt08-line @min-[46rem]:p-9">
              <h3 class="font-tvt08-serif text-[clamp(22px,2.6vw,28px)] leading-[1.15] font-semibold tracking-[-0.015em] text-balance @min-[46rem]:mt-1">Free carbon-neutral shipping over $75</h3>
              <p class="mt-2.5 max-w-[52ch] text-[14.5px] leading-relaxed text-tvt08-mut text-pretty">Every Aurum scale ships from our Portland or Leeds warehouse within one business day, in plastic-free packaging you can compost.</p>
              <dl class="mt-5 divide-y divide-tvt08-line overflow-hidden rounded-2xl bg-tvt08-sub ring-1 ring-tvt08-line">
                <div class="flex items-center justify-between gap-4 px-4 py-3"><dt class="text-[13.5px] font-medium">United States &amp; Canada</dt><dd class="font-tvt08-mono text-[12.5px] text-tvt08-mut tabular-nums">2–4 days</dd></div>
                <div class="flex items-center justify-between gap-4 px-4 py-3"><dt class="text-[13.5px] font-medium">United Kingdom &amp; EU</dt><dd class="font-tvt08-mono text-[12.5px] text-tvt08-mut tabular-nums">1–3 days</dd></div>
                <div class="flex items-center justify-between gap-4 px-4 py-3"><dt class="text-[13.5px] font-medium">Australia &amp; New Zealand</dt><dd class="font-tvt08-mono text-[12.5px] text-tvt08-mut tabular-nums">5–8 days</dd></div>
              </dl>
            </div>
          </details>

          <details name="tvt-08-faq" class="group border-b border-tvt08-line last:border-b-0 details-content:h-0 details-content:overflow-hidden details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-350 details-content:ease-[cubic-bezier(.32,.72,.3,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none @min-[46rem]:border-b-0 @min-[46rem]:details-content:overflow-visible">
            <summary class="relative flex min-h-16 cursor-pointer list-none items-center gap-3.5 px-5 py-3 text-tvt08-ink outline-none transition-colors duration-200 select-none hover:bg-tvt08-acc/[0.07] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt08-ring group-open:bg-tvt08-acc/[0.1] motion-reduce:transition-none sm:px-6 [&::-webkit-details-marker]:hidden @min-[46rem]:min-h-[4.25rem] @min-[46rem]:rounded-2xl @min-[46rem]:mx-2 @min-[46rem]:my-0.5 @min-[46rem]:px-4 @min-[46rem]:group-open:bg-tvt08-tab @min-[46rem]:group-open:shadow-tvt08-tab before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt08-acc before:to-tvt08-acc2 before:transition-transform before:duration-300 group-open:before:scale-y-100 @min-[46rem]:before:-start-2 motion-reduce:before:transition-none">
              <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt08-acc/12 text-tvt08-acc-ink ring-1 ring-tvt08-acc/20 transition-[background-color,color,box-shadow] duration-300 group-open:bg-linear-to-br group-open:from-tvt08-acc group-open:to-tvt08-acc2 group-open:text-tvt08-on group-open:shadow-tvt08-pill group-open:ring-0"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><path d="M4 8h9a4 4 0 0 1 0 8H8M4 8l3.5-3.5M4 8l3.5 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="min-w-0 flex-1"><span class="block text-[15px] leading-snug font-semibold tracking-[-0.01em]">Returns &amp; refunds</span><span class="mt-0.5 block truncate text-[12.5px] text-tvt08-mut">60-day, any-condition returns</span></span>
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 text-tvt08-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-open:rotate-180 group-open:text-tvt08-acc-ink motion-reduce:transition-none @min-[46rem]:-rotate-90 @min-[46rem]:group-open:-rotate-90"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </summary>
            <div class="px-5 pt-1 pb-6 sm:px-6 @min-[46rem]:absolute @min-[46rem]:inset-y-0 @min-[46rem]:end-0 @min-[46rem]:start-[38%] @min-[46rem]:overflow-auto @min-[46rem]:overscroll-contain @min-[46rem]:bg-tvt08-card @min-[46rem]:border-s @min-[46rem]:border-tvt08-line @min-[46rem]:p-9">
              <h3 class="font-tvt08-serif text-[clamp(22px,2.6vw,28px)] leading-[1.15] font-semibold tracking-[-0.015em] text-balance @min-[46rem]:mt-1">60 days to change your mind</h3>
              <p class="mt-2.5 max-w-[52ch] text-[14.5px] leading-relaxed text-tvt08-mut text-pretty">Not in love with it? Send it back in any condition within 60 days for a full refund — return labels are prepaid and print from your order page.</p>
              <ol class="mt-5 grid gap-2.5">
                <li class="flex items-center gap-3 text-[14px]"><span class="grid size-7 shrink-0 place-items-center rounded-full bg-tvt08-acc/14 font-tvt08-mono text-[11.5px] font-semibold text-tvt08-acc-ink">1</span>Open your order and choose <b class="font-semibold">Start a return</b></li>
                <li class="flex items-center gap-3 text-[14px]"><span class="grid size-7 shrink-0 place-items-center rounded-full bg-tvt08-acc/14 font-tvt08-mono text-[11.5px] font-semibold text-tvt08-acc-ink">2</span>Drop the box at any UPS or Royal Mail point</li>
                <li class="flex items-center gap-3 text-[14px]"><span class="grid size-7 shrink-0 place-items-center rounded-full bg-tvt08-acc/14 font-tvt08-mono text-[11.5px] font-semibold text-tvt08-acc-ink">3</span>Refund lands within 3 business days of scan</li>
              </ol>
            </div>
          </details>

          <details name="tvt-08-faq" class="group border-b border-tvt08-line last:border-b-0 details-content:h-0 details-content:overflow-hidden details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-350 details-content:ease-[cubic-bezier(.32,.72,.3,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none @min-[46rem]:border-b-0 @min-[46rem]:details-content:overflow-visible">
            <summary class="relative flex min-h-16 cursor-pointer list-none items-center gap-3.5 px-5 py-3 text-tvt08-ink outline-none transition-colors duration-200 select-none hover:bg-tvt08-acc/[0.07] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt08-ring group-open:bg-tvt08-acc/[0.1] motion-reduce:transition-none sm:px-6 [&::-webkit-details-marker]:hidden @min-[46rem]:min-h-[4.25rem] @min-[46rem]:rounded-2xl @min-[46rem]:mx-2 @min-[46rem]:my-0.5 @min-[46rem]:px-4 @min-[46rem]:group-open:bg-tvt08-tab @min-[46rem]:group-open:shadow-tvt08-tab before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt08-acc before:to-tvt08-acc2 before:transition-transform before:duration-300 group-open:before:scale-y-100 @min-[46rem]:before:-start-2 motion-reduce:before:transition-none">
              <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt08-acc/12 text-tvt08-acc-ink ring-1 ring-tvt08-acc/20 transition-[background-color,color,box-shadow] duration-300 group-open:bg-linear-to-br group-open:from-tvt08-acc group-open:to-tvt08-acc2 group-open:text-tvt08-on group-open:shadow-tvt08-pill group-open:ring-0"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><path d="M10 2.5 16 5v4.5c0 4-2.7 6.7-6 8-3.3-1.3-6-4-6-8V5Z M7.2 10l2 2 3.8-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="min-w-0 flex-1"><span class="block text-[15px] leading-snug font-semibold tracking-[-0.01em]">Warranty</span><span class="mt-0.5 block truncate text-[12.5px] text-tvt08-mut">What two years covers</span></span>
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 text-tvt08-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-open:rotate-180 group-open:text-tvt08-acc-ink motion-reduce:transition-none @min-[46rem]:-rotate-90 @min-[46rem]:group-open:-rotate-90"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </summary>
            <div class="px-5 pt-1 pb-6 sm:px-6 @min-[46rem]:absolute @min-[46rem]:inset-y-0 @min-[46rem]:end-0 @min-[46rem]:start-[38%] @min-[46rem]:overflow-auto @min-[46rem]:overscroll-contain @min-[46rem]:bg-tvt08-card @min-[46rem]:border-s @min-[46rem]:border-tvt08-line @min-[46rem]:p-9">
              <h3 class="font-tvt08-serif text-[clamp(22px,2.6vw,28px)] leading-[1.15] font-semibold tracking-[-0.015em] text-balance @min-[46rem]:mt-1">Two years, every part, no forms</h3>
              <p class="mt-2.5 max-w-[52ch] text-[14.5px] leading-relaxed text-tvt08-mut text-pretty">Load cells, battery and the app-connected timer are all covered for 24 months. Registration is automatic from your order email.</p>
              <div class="mt-5 flex items-center gap-4 rounded-2xl bg-linear-to-br from-tvt08-acc/15 to-tvt08-acc2/10 p-4 ring-1 ring-tvt08-acc/25">
                <span aria-hidden="true" class="flex size-14 shrink-0 items-baseline justify-center pt-3.5 rounded-full bg-linear-to-br from-tvt08-acc to-tvt08-acc2 font-tvt08-serif text-[22px] font-bold text-tvt08-on shadow-tvt08-pill">2<span class="text-[12px]">yr</span></span>
                <p class="text-[13.5px] leading-snug text-tvt08-mut"><b class="block text-[14.5px] font-semibold text-tvt08-ink">Extendable to 5 years</b>Add Aurum Care at checkout for $19 — accidental drops included.</p>
              </div>
            </div>
          </details>

          <details name="tvt-08-faq" class="group border-b border-tvt08-line last:border-b-0 details-content:h-0 details-content:overflow-hidden details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-350 details-content:ease-[cubic-bezier(.32,.72,.3,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none @min-[46rem]:border-b-0 @min-[46rem]:details-content:overflow-visible">
            <summary class="relative flex min-h-16 cursor-pointer list-none items-center gap-3.5 px-5 py-3 text-tvt08-ink outline-none transition-colors duration-200 select-none hover:bg-tvt08-acc/[0.07] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt08-ring group-open:bg-tvt08-acc/[0.1] motion-reduce:transition-none sm:px-6 [&::-webkit-details-marker]:hidden @min-[46rem]:min-h-[4.25rem] @min-[46rem]:rounded-2xl @min-[46rem]:mx-2 @min-[46rem]:my-0.5 @min-[46rem]:px-4 @min-[46rem]:group-open:bg-tvt08-tab @min-[46rem]:group-open:shadow-tvt08-tab before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt08-acc before:to-tvt08-acc2 before:transition-transform before:duration-300 group-open:before:scale-y-100 @min-[46rem]:before:-start-2 motion-reduce:before:transition-none">
              <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt08-acc/12 text-tvt08-acc-ink ring-1 ring-tvt08-acc/20 transition-[background-color,color,box-shadow] duration-300 group-open:bg-linear-to-br group-open:from-tvt08-acc group-open:to-tvt08-acc2 group-open:text-tvt08-on group-open:shadow-tvt08-pill group-open:ring-0"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><path d="M10 2.8s5 5.4 5 9a5 5 0 0 1-10 0c0-3.6 5-9 5-9Z M7.8 12.5a2.3 2.3 0 0 0 2.2 2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="min-w-0 flex-1"><span class="block text-[15px] leading-snug font-semibold tracking-[-0.01em]">Care &amp; cleaning</span><span class="mt-0.5 block truncate text-[12.5px] text-tvt08-mut">Keeping the glass top pristine</span></span>
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 text-tvt08-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-open:rotate-180 group-open:text-tvt08-acc-ink motion-reduce:transition-none @min-[46rem]:-rotate-90 @min-[46rem]:group-open:-rotate-90"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </summary>
            <div class="px-5 pt-1 pb-6 sm:px-6 @min-[46rem]:absolute @min-[46rem]:inset-y-0 @min-[46rem]:end-0 @min-[46rem]:start-[38%] @min-[46rem]:overflow-auto @min-[46rem]:overscroll-contain @min-[46rem]:bg-tvt08-card @min-[46rem]:border-s @min-[46rem]:border-tvt08-line @min-[46rem]:p-9">
              <h3 class="font-tvt08-serif text-[clamp(22px,2.6vw,28px)] leading-[1.15] font-semibold tracking-[-0.015em] text-balance @min-[46rem]:mt-1">A damp cloth, never the dishwasher</h3>
              <p class="mt-2.5 max-w-[52ch] text-[14.5px] leading-relaxed text-tvt08-mut text-pretty">The glass top is tempered and food-safe; wipe it with a soft cloth and mild soap. Keep the base out of water — it seals against splashes, not submersion.</p>
              <div class="mt-5 flex flex-wrap gap-2"><span class="rounded-full bg-tvt08-sub px-2.5 py-1 text-[12px] font-medium text-tvt08-ink ring-1 ring-tvt08-line">Soft microfibre</span><span class="rounded-full bg-tvt08-sub px-2.5 py-1 text-[12px] font-medium text-tvt08-ink ring-1 ring-tvt08-line">Mild soap</span><span class="rounded-full bg-tvt08-sub px-2.5 py-1 text-[12px] font-medium text-tvt08-ink ring-1 ring-tvt08-line">Recalibrate monthly</span><span class="rounded-full bg-tvt08-sub px-2.5 py-1 text-[12px] font-medium text-tvt08-ink ring-1 ring-tvt08-line">No abrasive pads</span></div>
            </div>
          </details>

          <details name="tvt-08-faq" class="group border-b border-tvt08-line last:border-b-0 details-content:h-0 details-content:overflow-hidden details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-350 details-content:ease-[cubic-bezier(.32,.72,.3,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none @min-[46rem]:border-b-0 @min-[46rem]:details-content:overflow-visible">
            <summary class="relative flex min-h-16 cursor-pointer list-none items-center gap-3.5 px-5 py-3 text-tvt08-ink outline-none transition-colors duration-200 select-none hover:bg-tvt08-acc/[0.07] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt08-ring group-open:bg-tvt08-acc/[0.1] motion-reduce:transition-none sm:px-6 [&::-webkit-details-marker]:hidden @min-[46rem]:min-h-[4.25rem] @min-[46rem]:rounded-2xl @min-[46rem]:mx-2 @min-[46rem]:my-0.5 @min-[46rem]:px-4 @min-[46rem]:group-open:bg-tvt08-tab @min-[46rem]:group-open:shadow-tvt08-tab before:absolute before:inset-y-3 before:start-0 before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-linear-to-b before:from-tvt08-acc before:to-tvt08-acc2 before:transition-transform before:duration-300 group-open:before:scale-y-100 @min-[46rem]:before:-start-2 motion-reduce:before:transition-none">
              <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-xl bg-tvt08-acc/12 text-tvt08-acc-ink ring-1 ring-tvt08-acc/20 transition-[background-color,color,box-shadow] duration-300 group-open:bg-linear-to-br group-open:from-tvt08-acc group-open:to-tvt08-acc2 group-open:text-tvt08-on group-open:shadow-tvt08-pill group-open:ring-0"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><rect x="2.5" y="4.5" width="15" height="11" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M2.5 8h15M5.5 12.5h3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
              <span class="min-w-0 flex-1"><span class="block text-[15px] leading-snug font-semibold tracking-[-0.01em]">Payment options</span><span class="mt-0.5 block truncate text-[12.5px] text-tvt08-mut">Cards, wallets and pay-in-four</span></span>
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 text-tvt08-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-open:rotate-180 group-open:text-tvt08-acc-ink motion-reduce:transition-none @min-[46rem]:-rotate-90 @min-[46rem]:group-open:-rotate-90"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </summary>
            <div class="px-5 pt-1 pb-6 sm:px-6 @min-[46rem]:absolute @min-[46rem]:inset-y-0 @min-[46rem]:end-0 @min-[46rem]:start-[38%] @min-[46rem]:overflow-auto @min-[46rem]:overscroll-contain @min-[46rem]:bg-tvt08-card @min-[46rem]:border-s @min-[46rem]:border-tvt08-line @min-[46rem]:p-9">
              <h3 class="font-tvt08-serif text-[clamp(22px,2.6vw,28px)] leading-[1.15] font-semibold tracking-[-0.015em] text-balance @min-[46rem]:mt-1">Card, wallet or four interest-free payments</h3>
              <p class="mt-2.5 max-w-[52ch] text-[14.5px] leading-relaxed text-tvt08-mut text-pretty">We accept Visa, Mastercard, Amex, Apple Pay and Google Pay. Split any order over $100 into four payments with no interest or fees.</p>
              <div class="mt-5 grid grid-cols-4 gap-2 max-[420px]:grid-cols-2">
                <span class="grid h-11 place-items-center rounded-xl bg-tvt08-sub font-tvt08-mono text-[11.5px] font-semibold tracking-wide ring-1 ring-tvt08-line">VISA</span>
                <span class="grid h-11 place-items-center rounded-xl bg-tvt08-sub font-tvt08-mono text-[11.5px] font-semibold tracking-wide ring-1 ring-tvt08-line">AMEX</span>
                <span class="grid h-11 place-items-center rounded-xl bg-tvt08-sub font-tvt08-mono text-[11.5px] font-semibold tracking-wide ring-1 ring-tvt08-line">Pay</span>
                <span class="grid h-11 place-items-center rounded-xl bg-tvt08-sub font-tvt08-mono text-[11.5px] font-semibold tracking-wide ring-1 ring-tvt08-line">4×</span>
              </div>
            </div>
          </details>
        </div>
      </div>
      <div class="flex flex-wrap items-center justify-between gap-3 border-t border-tvt08-line px-5 py-4 sm:px-6">
        <p class="text-[13.5px] text-tvt08-mut">Still stuck? A human reads every message.</p>
        <span class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tvt08-ink px-4 text-[13.5px] font-semibold text-tvt08-card shadow-tvt08-tab">Contact support <svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full bg-tvt08-card px-3.5 py-2 text-center font-tvt08-mono text-[11.5px] text-tvt08-mut ring-1 ring-tvt08-line">group-open: · details-content: · @min-[46rem]:absolute</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt08-bg: #fbf4e6;
  --color-tvt08-bg: oklch(0.97 0.02 85);
  --color-tvt08-glow: #ffd896a6;
  --color-tvt08-glow: oklch(0.9 0.1 80 / 0.65);
  --color-tvt08-card: #fffdfa;
  --color-tvt08-card: oklch(0.995 0.006 85);
  --color-tvt08-sub: #fbf6ec;
  --color-tvt08-sub: oklch(0.975 0.014 85);
  --color-tvt08-tab: #ffffff;
  --color-tvt08-tab: oklch(1 0 0);
  --color-tvt08-ink: #301d0d;
  --color-tvt08-ink: oklch(0.25 0.04 60);
  --color-tvt08-mut: #715844;
  --color-tvt08-mut: oklch(0.48 0.045 60);
  --color-tvt08-line: #e9dcc8;
  --color-tvt08-line: oklch(0.9 0.03 80);
  --color-tvt08-acc: #f2a618;
  --color-tvt08-acc: oklch(0.78 0.16 75);
  --color-tvt08-acc2: #ee7a1f;
  --color-tvt08-acc2: oklch(0.7 0.17 52);
  --color-tvt08-acc-ink: #944e00;
  --color-tvt08-acc-ink: oklch(0.5 0.12 58);
  --color-tvt08-on: #371801;
  --color-tvt08-on: oklch(0.25 0.06 55);
  --color-tvt08-hl: #c46d00;
  --color-tvt08-hl: oklch(0.62 0.15 60);
  --color-tvt08-hl2: #bf4213;
  --color-tvt08-hl2: oklch(0.55 0.17 38);
  --color-tvt08-ring: #b36300;
  --color-tvt08-ring: oklch(0.58 0.15 60);
  --color-tvt08-ok: #2a904b;
  --color-tvt08-ok: oklch(0.58 0.14 150);
  --font-tvt08-sans: 'Figtree', system-ui, sans-serif;
  --font-tvt08-serif: 'Fraunces', Georgia, serif;
  --font-tvt08-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tvt08-card: 0 1px 2px oklch(0.35 0.06 60 / 0.07), 0 32px 72px -32px oklch(0.45 0.12 60 / 0.4);
  --shadow-tvt08-tab: 0 1px 2px oklch(0.35 0.06 60 / 0.1), 0 8px 20px -10px oklch(0.5 0.12 60 / 0.35), inset 0 0 0 1px oklch(0.6 0.12 70 / 0.12);
  --shadow-tvt08-pill: 0 8px 18px -8px oklch(0.65 0.17 60 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.4);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-08 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-08:not([data-theme="light"]) {
    --color-tvt08-bg: #170d05;
    --color-tvt08-bg: oklch(0.17 0.025 60);
    --color-tvt08-glow: #4c2e0073;
    --color-tvt08-glow: oklch(0.33 0.08 70 / 0.45);
    --color-tvt08-card: #22150a;
    --color-tvt08-card: oklch(0.21 0.028 62);
    --color-tvt08-sub: #281b0f;
    --color-tvt08-sub: oklch(0.235 0.03 62);
    --color-tvt08-tab: #372513;
    --color-tvt08-tab: oklch(0.28 0.04 65);
    --color-tvt08-ink: #f6f1e7;
    --color-tvt08-ink: oklch(0.96 0.015 85);
    --color-tvt08-mut: #c5b59f;
    --color-tvt08-mut: oklch(0.78 0.035 75);
    --color-tvt08-line: #3f2f20;
    --color-tvt08-line: oklch(0.32 0.035 65);
    --color-tvt08-acc: #f5ae39;
    --color-tvt08-acc: oklch(0.8 0.15 75);
    --color-tvt08-acc2: #f18336;
    --color-tvt08-acc2: oklch(0.72 0.16 52);
    --color-tvt08-acc-ink: #fac871;
    --color-tvt08-acc-ink: oklch(0.86 0.12 80);
    --color-tvt08-on: #2e1604;
    --color-tvt08-on: oklch(0.23 0.05 55);
    --color-tvt08-hl: #f8c562;
    --color-tvt08-hl: oklch(0.85 0.13 82);
    --color-tvt08-hl2: #fc9252;
    --color-tvt08-hl2: oklch(0.76 0.15 50);
    --color-tvt08-ring: #f2b95a;
    --color-tvt08-ring: oklch(0.82 0.13 78);
    --color-tvt08-ok: #67d283;
    --color-tvt08-ok: oklch(0.78 0.15 150);
  }
}

.tvt-08[data-theme="dark"] {
  --color-tvt08-bg: #170d05;
  --color-tvt08-bg: oklch(0.17 0.025 60);
  --color-tvt08-glow: #4c2e0073;
  --color-tvt08-glow: oklch(0.33 0.08 70 / 0.45);
  --color-tvt08-card: #22150a;
  --color-tvt08-card: oklch(0.21 0.028 62);
  --color-tvt08-sub: #281b0f;
  --color-tvt08-sub: oklch(0.235 0.03 62);
  --color-tvt08-tab: #372513;
  --color-tvt08-tab: oklch(0.28 0.04 65);
  --color-tvt08-ink: #f6f1e7;
  --color-tvt08-ink: oklch(0.96 0.015 85);
  --color-tvt08-mut: #c5b59f;
  --color-tvt08-mut: oklch(0.78 0.035 75);
  --color-tvt08-line: #3f2f20;
  --color-tvt08-line: oklch(0.32 0.035 65);
  --color-tvt08-acc: #f5ae39;
  --color-tvt08-acc: oklch(0.8 0.15 75);
  --color-tvt08-acc2: #f18336;
  --color-tvt08-acc2: oklch(0.72 0.16 52);
  --color-tvt08-acc-ink: #fac871;
  --color-tvt08-acc-ink: oklch(0.86 0.12 80);
  --color-tvt08-on: #2e1604;
  --color-tvt08-on: oklch(0.23 0.05 55);
  --color-tvt08-hl: #f8c562;
  --color-tvt08-hl: oklch(0.85 0.13 82);
  --color-tvt08-hl2: #fc9252;
  --color-tvt08-hl2: oklch(0.76 0.15 50);
  --color-tvt08-ring: #f2b95a;
  --color-tvt08-ring: oklch(0.82 0.13 78);
  --color-tvt08-ok: #67d283;
  --color-tvt08-ok: oklch(0.78 0.15 150);
}
```
