---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/pure-tailwind-css-vertical-tabs-without-javascript-peer-checked/"
title: "Pure Tailwind CSS Vertical Tabs Without JavaScript (peer-checked)"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A project workspace that switches between Overview, Activity, Members and Billing with zero JavaScript: four sr-only radios, four labels and v4's named peers…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind CSS Vertical Tabs Without JavaScript (peer-checked)
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/pure-tailwind-css-vertical-tabs-without-javascript-peer-checked/

A project workspace that switches between Overview, Activity, Members and Billing with zero JavaScript: four sr-only radios, four labels and v4's named peers &mdash; peer/t2 on a radio, peer-checked/t2:visible on its panel &mdash; so every label and panel listens to exactly one input in one flat grid. Panels cross-fade in a shared grid cell, so the card never changes height between tabs.
## HTML
```html
<section class="tvt-01 w-full min-h-svh grid place-items-center bg-tvt01-bg bg-[radial-gradient(70%_55%_at_50%_0%,var(--color-tvt01-glow),transparent_72%)] px-4 py-14 font-tvt01-sans text-tvt01-ink antialiased sm:px-6" aria-label="Pure Tailwind CSS vertical tabs without JavaScript demo">
  <div class="grid w-full max-w-[56rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt01-card px-3 py-1.5 font-tvt01-mono text-[11.5px] text-tvt01-acc-ink ring-1 ring-tvt01-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt01-acc2 shadow-[0_0_0_3px] shadow-tvt01-acc2/25"></span>0 KB JavaScript</p>
      <h2 class="text-[clamp(28px,4.4vw,42px)] leading-[1.05] font-extrabold tracking-[-0.035em] text-balance">Vertical tabs, <span class="bg-linear-to-r from-tvt01-hl to-tvt01-hl2 bg-clip-text pe-1 text-transparent">zero JavaScript</span></h2>
      <p class="max-w-[46ch] text-[15px] leading-relaxed text-tvt01-mut text-pretty">Four radios, four labels and named <code class="font-tvt01-mono text-[13px] text-tvt01-ink">peer-checked/*</code> variants. Click a tab, or focus the rail and use the arrow keys.</p>
    </header>

    <article class="w-full overflow-hidden rounded-[22px] bg-tvt01-card shadow-tvt01-card ring-1 ring-tvt01-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <div class="flex items-center gap-3 border-b border-tvt01-line px-5 py-3.5 sm:px-6">
        <span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-linear-to-br from-tvt01-acc to-tvt01-acc2 text-white shadow-tvt01-pill"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="M10 2.5 17 6.5v7L10 17.5 3 13.5v-7Z M10 10l7-3.5M10 10v7.5M10 10 3 6.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
        <div class="min-w-0 flex-1 leading-tight">
          <p class="text-[14.5px] font-bold tracking-[-0.01em]">Project Atlas</p>
          <p class="text-[12.5px] text-tvt01-mut">Northstar Labs · Q4 roadmap</p>
        </div>
        <div aria-hidden="true" class="flex -space-x-2 max-[420px]:hidden"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.7_0.16_25)] to-[oklch(0.6_0.2_350)] text-[12px] font-bold text-white ring-2 ring-tvt01-card size-7 text-[10px]">MR</span><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.68_0.15_200)] to-[oklch(0.55_0.17_250)] text-[12px] font-bold text-white ring-2 ring-tvt01-card size-7 text-[10px]">AK</span><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.75_0.15_85)] to-[oklch(0.62_0.17_45)] text-[12px] font-bold text-white ring-2 ring-tvt01-card size-7 text-[10px]">JL</span><span class="grid size-7 place-items-center rounded-full bg-tvt01-rail text-[10px] font-bold text-tvt01-mut ring-2 ring-tvt01-card">+5</span></div>
      </div>

      <div class="@container">
      <div role="radiogroup" aria-label="Project workspace sections" class="relative grid grid-cols-[clamp(11.5rem,28%,15rem)_minmax(0,1fr)] grid-rows-[repeat(4,auto)_1fr] before:col-start-1 before:row-[1/-1] before:border-e before:border-tvt01-line before:bg-tvt01-rail @max-[36rem]:grid-cols-2 @max-[36rem]:grid-rows-[auto_auto_auto] @max-[36rem]:pb-0 @max-[36rem]:before:hidden">

        <input type="radio" name="tvt-01-tabs" id="tvt-01-t1" class="peer/t1 sr-only" checked>
        <label for="tvt-01-t1" class="relative z-10 col-start-1 row-start-1 mx-2.5 my-0.5 flex min-h-12 cursor-pointer items-center gap-3 rounded-xl px-3.5 text-[14.5px] font-semibold text-tvt01-mut transition-[color,background-color,box-shadow] duration-200 select-none first-of-type:mt-3 hover:bg-tvt01-ink/[0.045] hover:text-tvt01-ink peer-checked/t1:bg-tvt01-tab peer-checked/t1:text-tvt01-acc-ink peer-checked/t1:shadow-tvt01-tab peer-focus-visible/t1:outline-2 peer-focus-visible/t1:outline-offset-2 peer-focus-visible/t1:outline-tvt01-ring after:absolute after:inset-y-3 after:-start-2.5 after:w-[3px] after:scale-y-0 after:rounded-e-full after:bg-linear-to-b after:from-tvt01-acc after:to-tvt01-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t1:after:scale-y-100 motion-reduce:transition-none motion-reduce:after:transition-none @max-[36rem]:col-start-1 @max-[36rem]:row-start-1">
          <span class="font-tvt01-mono text-[10.5px] tracking-[0.08em] text-current/55 tabular-nums">01</span>
          <span class="flex-1">Overview</span>
        </label>

        <input type="radio" name="tvt-01-tabs" id="tvt-01-t2" class="peer/t2 sr-only">
        <label for="tvt-01-t2" class="relative z-10 col-start-1 row-start-2 mx-2.5 my-0.5 flex min-h-12 cursor-pointer items-center gap-3 rounded-xl px-3.5 text-[14.5px] font-semibold text-tvt01-mut transition-[color,background-color,box-shadow] duration-200 select-none first-of-type:mt-3 hover:bg-tvt01-ink/[0.045] hover:text-tvt01-ink peer-checked/t2:bg-tvt01-tab peer-checked/t2:text-tvt01-acc-ink peer-checked/t2:shadow-tvt01-tab peer-focus-visible/t2:outline-2 peer-focus-visible/t2:outline-offset-2 peer-focus-visible/t2:outline-tvt01-ring after:absolute after:inset-y-3 after:-start-2.5 after:w-[3px] after:scale-y-0 after:rounded-e-full after:bg-linear-to-b after:from-tvt01-acc after:to-tvt01-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t2:after:scale-y-100 motion-reduce:transition-none motion-reduce:after:transition-none @max-[36rem]:col-start-2 @max-[36rem]:row-start-1 @max-[36rem]:mt-3">
          <span class="font-tvt01-mono text-[10.5px] tracking-[0.08em] text-current/55 tabular-nums">02</span>
          <span class="flex-1">Activity</span><span class="rounded-full bg-tvt01-acc/12 px-2 py-0.5 text-[11px] font-bold text-tvt01-acc-ink tabular-nums">6</span>
        </label>

        <input type="radio" name="tvt-01-tabs" id="tvt-01-t3" class="peer/t3 sr-only">
        <label for="tvt-01-t3" class="relative z-10 col-start-1 row-start-3 mx-2.5 my-0.5 flex min-h-12 cursor-pointer items-center gap-3 rounded-xl px-3.5 text-[14.5px] font-semibold text-tvt01-mut transition-[color,background-color,box-shadow] duration-200 select-none first-of-type:mt-3 hover:bg-tvt01-ink/[0.045] hover:text-tvt01-ink peer-checked/t3:bg-tvt01-tab peer-checked/t3:text-tvt01-acc-ink peer-checked/t3:shadow-tvt01-tab peer-focus-visible/t3:outline-2 peer-focus-visible/t3:outline-offset-2 peer-focus-visible/t3:outline-tvt01-ring after:absolute after:inset-y-3 after:-start-2.5 after:w-[3px] after:scale-y-0 after:rounded-e-full after:bg-linear-to-b after:from-tvt01-acc after:to-tvt01-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t3:after:scale-y-100 motion-reduce:transition-none motion-reduce:after:transition-none @max-[36rem]:col-start-1 @max-[36rem]:row-start-2 @max-[36rem]:mb-3">
          <span class="font-tvt01-mono text-[10.5px] tracking-[0.08em] text-current/55 tabular-nums">03</span>
          <span class="flex-1">Members</span>
        </label>

        <input type="radio" name="tvt-01-tabs" id="tvt-01-t4" class="peer/t4 sr-only">
        <label for="tvt-01-t4" class="relative z-10 col-start-1 row-start-4 mx-2.5 my-0.5 flex min-h-12 cursor-pointer items-center gap-3 rounded-xl px-3.5 text-[14.5px] font-semibold text-tvt01-mut transition-[color,background-color,box-shadow] duration-200 select-none first-of-type:mt-3 hover:bg-tvt01-ink/[0.045] hover:text-tvt01-ink peer-checked/t4:bg-tvt01-tab peer-checked/t4:text-tvt01-acc-ink peer-checked/t4:shadow-tvt01-tab peer-focus-visible/t4:outline-2 peer-focus-visible/t4:outline-offset-2 peer-focus-visible/t4:outline-tvt01-ring after:absolute after:inset-y-3 after:-start-2.5 after:w-[3px] after:scale-y-0 after:rounded-e-full after:bg-linear-to-b after:from-tvt01-acc after:to-tvt01-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t4:after:scale-y-100 motion-reduce:transition-none motion-reduce:after:transition-none @max-[36rem]:col-start-2 @max-[36rem]:row-start-2 @max-[36rem]:mb-3">
          <span class="font-tvt01-mono text-[10.5px] tracking-[0.08em] text-current/55 tabular-nums">04</span>
          <span class="flex-1">Billing</span>
        </label>

        <div class="col-start-1 row-start-5 m-3 self-end rounded-xl bg-tvt01-card p-3.5 ring-1 ring-tvt01-line @max-[36rem]:hidden">
          <p class="flex justify-between text-[12px] font-semibold"><span>Storage</span><span class="text-tvt01-mut tabular-nums">34 / 50 GB</span></p>
          <div class="mt-2 h-1.5 overflow-hidden rounded-full bg-tvt01-line"><div class="h-full w-[68%] rounded-full bg-linear-to-r from-tvt01-acc to-tvt01-acc2"></div></div>
        </div>

        <article id="tvt-01-p1" aria-labelledby="tvt-01-h1" class="invisible col-start-2 row-[1/-1] translate-y-2 p-6 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t1:visible peer-checked/t1:translate-y-0 peer-checked/t1:opacity-100 motion-reduce:transition-none sm:p-8 @max-[36rem]:col-[1/-1] @max-[36rem]:row-[3] @max-[36rem]:border-t @max-[36rem]:border-tvt01-line">
          <div class="flex flex-wrap items-center gap-2.5">
            <h3 id="tvt-01-h1" class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Sprint 14 overview</h3>
            <span class="inline-flex items-center gap-1.5 rounded-full bg-tvt01-ok/12 px-2.5 py-1 text-[12px] font-semibold text-tvt01-ok"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt01-ok"></span>On track</span>
          </div>
          <p class="mt-2 max-w-[48ch] text-[14.5px] leading-relaxed text-tvt01-mut text-pretty">Checkout redesign ships Friday. Two blockers left, both owned and both under a day.</p>
          <dl class="mt-6 grid grid-cols-3 gap-2.5 sm:gap-3">
            <div class="rounded-2xl bg-tvt01-rail p-3 ring-1 ring-tvt01-line sm:p-4"><dt class="text-[12px] font-medium text-tvt01-mut">Velocity</dt><dd class="mt-1 text-[20px] font-extrabold sm:text-[24px] tracking-[-0.03em] tabular-nums">42<span class="ms-1 text-[13px] font-semibold text-tvt01-mut">pts</span></dd></div>
            <div class="rounded-2xl bg-tvt01-rail p-3 ring-1 ring-tvt01-line sm:p-4"><dt class="text-[12px] font-medium text-tvt01-mut">Open issues</dt><dd class="mt-1 text-[20px] font-extrabold sm:text-[24px] tracking-[-0.03em] tabular-nums">18<span class="ms-1.5 text-[12px] font-semibold text-tvt01-ok">−6</span></dd></div>
            <div class="rounded-2xl bg-tvt01-rail p-3 ring-1 ring-tvt01-line sm:p-4"><dt class="text-[12px] font-medium text-tvt01-mut">Cycle time</dt><dd class="mt-1 text-[20px] font-extrabold sm:text-[24px] tracking-[-0.03em] tabular-nums">2.4<span class="ms-1 text-[13px] font-semibold text-tvt01-mut">days</span></dd></div>
          </dl>
          <div class="mt-4 rounded-2xl p-4 ring-1 ring-tvt01-line">
            <p class="flex justify-between text-[12.5px] font-semibold"><span>Burndown</span><span class="text-tvt01-mut">Day 7 of 10</span></p>
            <svg viewBox="0 0 300 70" class="mt-2 h-16 w-full text-tvt01-acc" preserveAspectRatio="none" aria-hidden="true" focusable="false"><defs><linearGradient id="tvt-01-area" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="currentColor" stop-opacity=".28"/><stop offset="1" stop-color="currentColor" stop-opacity="0"/></linearGradient></defs><path d="M0 8 L30 12 L60 10 L90 22 L120 26 L150 34 L180 33 L210 46" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"/><path d="M0 8 L30 12 L60 10 L90 22 L120 26 L150 34 L180 33 L210 46 L210 70 L0 70Z" fill="url(#tvt-01-area)"/><path d="M0 8 L300 66" fill="none" stroke="currentColor" stroke-opacity=".35" stroke-dasharray="4 5" stroke-width="1.5" vector-effect="non-scaling-stroke"/></svg>
          </div>
        </article>

        <article id="tvt-01-p2" aria-labelledby="tvt-01-h2" class="invisible col-start-2 row-[1/-1] translate-y-2 p-6 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t2:visible peer-checked/t2:translate-y-0 peer-checked/t2:opacity-100 motion-reduce:transition-none sm:p-8 @max-[36rem]:col-[1/-1] @max-[36rem]:row-[3] @max-[36rem]:border-t @max-[36rem]:border-tvt01-line">
          <h3 id="tvt-01-h2" class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Recent activity</h3>
          <p class="mt-2 text-[14.5px] text-tvt01-mut">Six updates since your last visit.</p>
          <ol class="relative mt-5 grid gap-4 before:absolute before:inset-y-2 before:start-[17px] before:w-px before:bg-tvt01-line">
            <li class="relative flex gap-3.5"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.7_0.16_25)] to-[oklch(0.6_0.2_350)] text-[12px] font-bold text-white ring-2 ring-tvt01-card ">MR</span><div class="min-w-0 pt-0.5"><p class="text-[14px] leading-snug"><b class="font-semibold">Maya Ruiz</b> merged <span class="font-tvt01-mono text-[12.5px] text-tvt01-acc-ink">#412 checkout-v2</span></p><p class="mt-0.5 text-[12.5px] text-tvt01-mut">12 minutes ago</p></div></li>
            <li class="relative flex gap-3.5"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.68_0.15_200)] to-[oklch(0.55_0.17_250)] text-[12px] font-bold text-white ring-2 ring-tvt01-card ">AK</span><div class="min-w-0 pt-0.5"><p class="text-[14px] leading-snug"><b class="font-semibold">Arjun Kapoor</b> moved <b class="font-semibold">Payment retries</b> to Review</p><p class="mt-0.5 text-[12.5px] text-tvt01-mut">1 hour ago</p></div></li>
            <li class="relative flex gap-3.5"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.75_0.15_85)] to-[oklch(0.62_0.17_45)] text-[12px] font-bold text-white ring-2 ring-tvt01-card ">JL</span><div class="min-w-0 pt-0.5"><p class="text-[14px] leading-snug"><b class="font-semibold">Jess Liu</b> commented on <b class="font-semibold">Address autocomplete</b></p><p class="mt-1.5 rounded-xl bg-tvt01-rail px-3 py-2 text-[13px] text-tvt01-mut ring-1 ring-tvt01-line">“Postcode lookup is live for UK and AU — US next.”</p></div></li>
          </ol>
        </article>

        <article id="tvt-01-p3" aria-labelledby="tvt-01-h3" class="invisible col-start-2 row-[1/-1] translate-y-2 p-6 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t3:visible peer-checked/t3:translate-y-0 peer-checked/t3:opacity-100 motion-reduce:transition-none sm:p-8 @max-[36rem]:col-[1/-1] @max-[36rem]:row-[3] @max-[36rem]:border-t @max-[36rem]:border-tvt01-line">
          <div class="flex flex-wrap items-center justify-between gap-3">
            <div><h3 id="tvt-01-h3" class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Members</h3><p class="mt-1 text-[14.5px] text-tvt01-mut">8 of 10 seats in use</p></div>
            <span class="inline-flex min-h-10 items-center gap-1.5 rounded-xl bg-linear-to-br from-tvt01-acc to-tvt01-acc2 px-3.5 text-[13.5px] font-semibold text-white shadow-tvt01-pill">+ Invite</span>
          </div>
          <ul class="mt-5 divide-y divide-tvt01-line rounded-2xl ring-1 ring-tvt01-line">
            <li class="flex items-center gap-3 px-4 py-3"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.7_0.16_25)] to-[oklch(0.6_0.2_350)] text-[12px] font-bold text-white ring-2 ring-tvt01-card ">MR</span><div class="min-w-0 flex-1"><p class="truncate text-[14px] font-semibold">Maya Ruiz</p><p class="truncate text-[12.5px] text-tvt01-mut">[email protected]</p></div><span class="rounded-full bg-tvt01-acc/12 px-2.5 py-1 text-[11.5px] font-semibold text-tvt01-acc-ink">Owner</span></li>
            <li class="flex items-center gap-3 px-4 py-3"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.68_0.15_200)] to-[oklch(0.55_0.17_250)] text-[12px] font-bold text-white ring-2 ring-tvt01-card ">AK</span><div class="min-w-0 flex-1"><p class="truncate text-[14px] font-semibold">Arjun Kapoor</p><p class="truncate text-[12.5px] text-tvt01-mut">[email protected]</p></div><span class="rounded-full bg-tvt01-rail px-2.5 py-1 text-[11.5px] font-semibold text-tvt01-mut ring-1 ring-tvt01-line">Admin</span></li>
            <li class="flex items-center gap-3 px-4 py-3"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.75_0.15_85)] to-[oklch(0.62_0.17_45)] text-[12px] font-bold text-white ring-2 ring-tvt01-card ">JL</span><div class="min-w-0 flex-1"><p class="truncate text-[14px] font-semibold">Jess Liu</p><p class="truncate text-[12.5px] text-tvt01-mut">[email protected]</p></div><span class="rounded-full bg-tvt01-rail px-2.5 py-1 text-[11.5px] font-semibold text-tvt01-mut ring-1 ring-tvt01-line">Editor</span></li>
          </ul>
        </article>

        <article id="tvt-01-p4" aria-labelledby="tvt-01-h4" class="invisible col-start-2 row-[1/-1] translate-y-2 p-6 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] peer-checked/t4:visible peer-checked/t4:translate-y-0 peer-checked/t4:opacity-100 motion-reduce:transition-none sm:p-8 @max-[36rem]:col-[1/-1] @max-[36rem]:row-[3] @max-[36rem]:border-t @max-[36rem]:border-tvt01-line">
          <h3 id="tvt-01-h4" class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Billing</h3>
          <p class="mt-2 text-[14.5px] text-tvt01-mut">Next invoice <b class="font-semibold text-tvt01-ink">Nov 1, 2026</b> · Visa ending 4242</p>
          <div class="relative mt-5 overflow-hidden rounded-2xl bg-linear-to-br from-tvt01-acc to-tvt01-acc2 p-5 text-white shadow-tvt01-pill">
            <div aria-hidden="true" class="absolute -end-10 -top-12 size-40 rounded-full bg-white/12 blur-2xl"></div>
            <p class="text-[12px] font-semibold tracking-[0.12em] text-white/80 uppercase">Team plan</p>
            <p class="mt-1 text-[32px] font-extrabold tracking-[-0.04em] tabular-nums">$48<span class="text-[14px] font-semibold text-white/80"> / month</span></p>
            <p class="mt-1 text-[13px] text-white/85">Billed monthly · cancel anytime</p>
          </div>
          <div class="mt-4 grid gap-3 sm:grid-cols-2">
            <div class="rounded-2xl p-4 ring-1 ring-tvt01-line"><p class="flex justify-between text-[12.5px] font-semibold"><span>Seats</span><span class="text-tvt01-mut tabular-nums">8 / 10</span></p><div class="mt-2 h-1.5 rounded-full bg-tvt01-line"><div class="h-full w-4/5 rounded-full bg-tvt01-acc"></div></div></div>
            <div class="rounded-2xl p-4 ring-1 ring-tvt01-line"><p class="flex justify-between text-[12.5px] font-semibold"><span>Build minutes</span><span class="text-tvt01-mut tabular-nums">2,940 / 3,000</span></p><div class="mt-2 h-1.5 rounded-full bg-tvt01-line"><div class="h-full w-[98%] rounded-full bg-tvt01-warn"></div></div></div>
          </div>
        </article>
      </div>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full bg-tvt01-card px-3.5 py-2 text-center font-tvt01-mono text-[11.5px] text-tvt01-mut ring-1 ring-tvt01-line">peer/t1 · peer-checked/t1: · sr-only radios</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt01-bg: #f2f3fd;
  --color-tvt01-bg: oklch(0.966 0.014 282);
  --color-tvt01-glow: #cfcfffb3;
  --color-tvt01-glow: oklch(0.87 0.08 285 / 0.7);
  --color-tvt01-card: #fefeff;
  --color-tvt01-card: oklch(0.997 0.003 280);
  --color-tvt01-tab: #ffffff;
  --color-tvt01-tab: oklch(1 0 0);
  --color-tvt01-rail: #f5f6fe;
  --color-tvt01-rail: oklch(0.975 0.01 282);
  --color-tvt01-ink: #191a32;
  --color-tvt01-ink: oklch(0.23 0.045 280);
  --color-tvt01-mut: #595b74;
  --color-tvt01-mut: oklch(0.48 0.04 280);
  --color-tvt01-line: #dee0f0;
  --color-tvt01-line: oklch(0.91 0.022 282);
  --color-tvt01-acc: #5445ed;
  --color-tvt01-acc: oklch(0.52 0.24 278);
  --color-tvt01-acc2: #8e3de8;
  --color-tvt01-acc2: oklch(0.56 0.24 300);
  --color-tvt01-acc-ink: #4b34cd;
  --color-tvt01-acc-ink: oklch(0.46 0.22 280);
  --color-tvt01-hl: #5445ed;
  --color-tvt01-hl: oklch(0.52 0.24 278);
  --color-tvt01-hl2: #b431cf;
  --color-tvt01-hl2: oklch(0.58 0.24 320);
  --color-tvt01-ring: #6c50e9;
  --color-tvt01-ring: oklch(0.55 0.22 285);
  --color-tvt01-ok: #007d51;
  --color-tvt01-ok: oklch(0.52 0.13 160);
  --color-tvt01-warn: #da720d;
  --color-tvt01-warn: oklch(0.66 0.16 55);
  --font-tvt01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tvt01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tvt01-card: 0 1px 2px oklch(0.3 0.1 280 / 0.06), 0 30px 70px -30px oklch(0.4 0.2 285 / 0.38);
  --shadow-tvt01-tab: 0 1px 2px oklch(0.3 0.1 280 / 0.1), 0 6px 16px -8px oklch(0.45 0.2 285 / 0.35), inset 0 0 0 1px oklch(0.5 0.2 285 / 0.1);
  --shadow-tvt01-pill: 0 10px 24px -10px oklch(0.52 0.25 290 / 0.65), inset 0 1px 0 oklch(1 0 0 / 0.25);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-01 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-01:not([data-theme="light"]) {
    --color-tvt01-bg: #0a0b1e;
    --color-tvt01-bg: oklch(0.16 0.04 280);
    --color-tvt01-glow: #30217180;
    --color-tvt01-glow: oklch(0.32 0.13 285 / 0.5);
    --color-tvt01-card: #13142b;
    --color-tvt01-card: oklch(0.205 0.045 280);
    --color-tvt01-tab: #26254f;
    --color-tvt01-tab: oklch(0.29 0.075 282);
    --color-tvt01-rail: #0e0f23;
    --color-tvt01-rail: oklch(0.18 0.04 280);
    --color-tvt01-ink: #f1f1fa;
    --color-tvt01-ink: oklch(0.96 0.012 285);
    --color-tvt01-mut: #acafcb;
    --color-tvt01-mut: oklch(0.76 0.04 282);
    --color-tvt01-line: #2c2c4e;
    --color-tvt01-line: oklch(0.31 0.06 282);
    --color-tvt01-acc: #5b53f2;
    --color-tvt01-acc: oklch(0.55 0.23 278);
    --color-tvt01-acc2: #8d42e4;
    --color-tvt01-acc2: oklch(0.56 0.23 300);
    --color-tvt01-acc-ink: #c1c0ff;
    --color-tvt01-acc-ink: oklch(0.83 0.1 285);
    --color-tvt01-hl: #b0b7ff;
    --color-tvt01-hl: oklch(0.8 0.12 280);
    --color-tvt01-hl2: #e59ff6;
    --color-tvt01-hl2: oklch(0.8 0.14 320);
    --color-tvt01-ring: #a9a5ff;
    --color-tvt01-ring: oklch(0.76 0.15 285);
    --color-tvt01-ok: #5ed99e;
    --color-tvt01-ok: oklch(0.8 0.14 160);
    --color-tvt01-warn: #feb354;
    --color-tvt01-warn: oklch(0.82 0.14 70);
  }
}

.tvt-01[data-theme="dark"] {
  --color-tvt01-bg: #0a0b1e;
  --color-tvt01-bg: oklch(0.16 0.04 280);
  --color-tvt01-glow: #30217180;
  --color-tvt01-glow: oklch(0.32 0.13 285 / 0.5);
  --color-tvt01-card: #13142b;
  --color-tvt01-card: oklch(0.205 0.045 280);
  --color-tvt01-tab: #26254f;
  --color-tvt01-tab: oklch(0.29 0.075 282);
  --color-tvt01-rail: #0e0f23;
  --color-tvt01-rail: oklch(0.18 0.04 280);
  --color-tvt01-ink: #f1f1fa;
  --color-tvt01-ink: oklch(0.96 0.012 285);
  --color-tvt01-mut: #acafcb;
  --color-tvt01-mut: oklch(0.76 0.04 282);
  --color-tvt01-line: #2c2c4e;
  --color-tvt01-line: oklch(0.31 0.06 282);
  --color-tvt01-acc: #5b53f2;
  --color-tvt01-acc: oklch(0.55 0.23 278);
  --color-tvt01-acc2: #8d42e4;
  --color-tvt01-acc2: oklch(0.56 0.23 300);
  --color-tvt01-acc-ink: #c1c0ff;
  --color-tvt01-acc-ink: oklch(0.83 0.1 285);
  --color-tvt01-hl: #b0b7ff;
  --color-tvt01-hl: oklch(0.8 0.12 280);
  --color-tvt01-hl2: #e59ff6;
  --color-tvt01-hl2: oklch(0.8 0.14 320);
  --color-tvt01-ring: #a9a5ff;
  --color-tvt01-ring: oklch(0.76 0.15 285);
  --color-tvt01-ok: #5ed99e;
  --color-tvt01-ok: oklch(0.8 0.14 160);
  --color-tvt01-warn: #feb354;
  --color-tvt01-warn: oklch(0.82 0.14 70);
}
```
