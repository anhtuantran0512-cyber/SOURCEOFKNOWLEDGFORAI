---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-page-saas-product-feature-showcase/"
title: "Tailwind Full Page SaaS Product Feature Showcase"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "The applied template: five full-viewport panels &mdash; hero, two feature panels with real interface mock-ups, a metrics panel and a closing call to action…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full Page SaaS Product Feature Showcase
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-page-saas-product-feature-showcase/

The applied template: five full-viewport panels &mdash; hero, two feature panels with real interface mock-ups, a metrics panel and a closing call to action &mdash; for a release-orchestration product called Cadence. Progress bars and the sparkline fill as each mock-up scrolls into view (anonymous view() timelines), buttons get hover lift and arrow nudges, and every colour is a token you can swap in one pass.
## HTML
```html
<div class="tfps-09 relative isolate w-full min-h-svh bg-tfps09-bg font-tfps09-sans text-tfps09-ink antialiased [&_code]:font-tfps09-mono [&_code]:text-[.92em]">
  <input class="peer sr-only" type="checkbox" id="tfps-09-theme">
  <label for="tfps-09-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps09-ink/10 bg-white/60 text-tfps09-ink hover:bg-white/85 tfps09-dark:bg-white/[.07] tfps09-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps09-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps09-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps09-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps09-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps09-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Cadence product tour, five panels">

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps09-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps09-panel2 not-first:-mt-16 not-first:rounded-t-[1.9rem] not-first:border-t not-first:border-tfps09-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps09-shade)] forced-colors:border-[CanvasText] bg-[radial-gradient(90%_70%_at_82%_6%,color-mix(in_oklab,var(--color-tfps09-acc)_16%,transparent),transparent_68%)]" id="tfps-09-s1" aria-labelledby="tfps-09-h1">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="flex items-center gap-2 text-[1.04rem] font-semibold tracking-[-.02em]"><svg class="size-[1.35rem] text-tfps09-acc" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M3 15.5l4.2-7.6 3.4 5.2 2.6-3.4 2.3 3.6L21 6.8" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Cadence</p>
        <h2 class="max-w-[21ch] text-[clamp(2rem,5.4vw,4.05rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-09-h1">Ship every service on the same heartbeat</h2>
        <p class="max-w-[56ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps09-ink/75 [&_code]:text-tfps09-ink">Cadence turns 40 independent deploy pipelines into one release train &mdash; with a rollback that takes eleven seconds instead of an incident channel.</p>
        <div class="flex flex-wrap items-center gap-2.5">
          <button class="group inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-full border border-transparent bg-tfps09-acc px-5 py-3 text-[.95rem] font-medium text-white shadow-[0_14px_30px_-18px_var(--color-tfps09-acc)] transition-[translate,background-color] duration-200 hover:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tfps09-ink tfps09-dark:text-[#0a0c18] motion-reduce:hover:translate-y-0" type="button">Start a free workspace<svg class="size-4 transition-transform duration-200 group-hover:translate-x-0.5" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6.5l5.5 5.5-5.5 5.5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <a class="inline-flex min-h-11 cursor-pointer items-center rounded-full border bg-transparent px-[1.15rem] py-3 text-[.95rem] no-underline transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-offset-3 border-tfps09-acc/40 text-tfps09-acc hover:bg-tfps09-acc/8 focus-visible:outline-tfps09-acc" href="#tfps-09-s2">See how it works</a>
        </div>
        <ul class="flex flex-wrap gap-x-5 gap-y-2 font-tfps09-mono text-[.72rem] tracking-[.06em] uppercase text-tfps09-ink/70">
          <li>SOC 2 Type II</li><li>Self-host or cloud</li><li>Terraform provider</li>
        </ul>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps09-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps09-panel2 not-first:-mt-16 not-first:rounded-t-[1.9rem] not-first:border-t not-first:border-tfps09-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps09-shade)] forced-colors:border-[CanvasText]" id="tfps-09-s2" aria-labelledby="tfps-09-h2">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] items-center gap-[clamp(1.5rem,4vw,3.25rem)] min-[60rem]:grid-cols-2">
        <div class="grid justify-items-start gap-[clamp(.85rem,2vh,1.3rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps09-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps09-acc">01 / 03</span><span class="rounded-[.45rem] border border-tfps09-ink/12 px-2 py-[.22rem] font-tfps09-mono text-[.7rem] text-tfps09-ink/75">release trains</span></p>
          <h2 class="max-w-[24ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-09-h2">One board for every service in flight</h2>
          <p class="max-w-[56ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps09-ink/75 [&_code]:text-tfps09-ink">Group services into trains, set a window, and Cadence sequences the rollout &mdash; holding anything whose checks are still amber and promoting the rest without a human in the loop.</p>
          <ul class="grid w-full gap-3">
            <li class="grid grid-cols-[auto_1fr] items-start gap-3 border-t border-tfps09-ink/10 pt-3">
              <svg class="mt-0.5 size-5 text-tfps09-acc" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12.5l4.4 4.2L19.5 6.4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span class="grid gap-0.5 text-[.94rem] leading-[1.5] text-pretty text-tfps09-ink/75"><strong class="text-[.99rem] font-semibold text-tfps09-ink">Gated promotion</strong>Checks, budgets and approvals evaluated per service, not per repo.</span>
            </li>
            <li class="grid grid-cols-[auto_1fr] items-start gap-3 border-t border-tfps09-ink/10 pt-3">
              <svg class="mt-0.5 size-5 text-tfps09-acc" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 7.5v9M7.5 12h9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="12" r="8.2" stroke="currentColor" stroke-width="1.7"/></svg>
              <span class="grid gap-0.5 text-[.94rem] leading-[1.5] text-pretty text-tfps09-ink/75"><strong class="text-[.99rem] font-semibold text-tfps09-ink">Eleven-second rollback</strong>Every train keeps the last good manifest warm.</span>
            </li>
          </ul>
        </div>
        <div class="w-full overflow-hidden rounded-[1.25rem] border border-tfps09-ink/10 bg-tfps09-bg shadow-[0_30px_64px_-38px_var(--color-tfps09-shade)] forced-colors:border-[CanvasText]" role="img" aria-label="Cadence release board showing four services with staged rollout status">
          <div class="flex items-center gap-1.5 border-b border-tfps09-ink/10 bg-tfps09-ink/[.04] px-3.5 py-2.5"><i class="size-2 rounded-full bg-tfps09-ink/15"></i><i class="size-2 rounded-full bg-tfps09-ink/15"></i><i class="size-2 rounded-full bg-tfps09-ink/15"></i><em class="ms-auto font-tfps09-mono text-[.66rem] not-italic text-tfps09-ink/70">release / train-04</em></div>
          <div class="grid gap-2.5 p-3.5">
            <div class="grid grid-cols-[minmax(6rem,1fr)_1.4fr_auto] items-center gap-3"><span class="truncate font-tfps09-mono text-[.77rem]">checkout-api</span><span class="relative h-1.5 overflow-hidden rounded-full bg-tfps09-ink/8"><i class="tfps09-fill [--p:100%] absolute inset-y-0 left-0 w-(--p) origin-left rounded-full bg-linear-to-r from-tfps09-acc to-tfps09-acc/45"></i></span><span class="min-w-[2.6rem] text-end font-tfps09-mono text-[.72rem] tabular-nums text-tfps09-ok">live</span></div>
            <div class="grid grid-cols-[minmax(6rem,1fr)_1.4fr_auto] items-center gap-3"><span class="truncate font-tfps09-mono text-[.77rem]">payments-worker</span><span class="relative h-1.5 overflow-hidden rounded-full bg-tfps09-ink/8"><i class="tfps09-fill [--p:74%] absolute inset-y-0 left-0 w-(--p) origin-left rounded-full bg-linear-to-r from-tfps09-acc to-tfps09-acc/45"></i></span><span class="min-w-[2.6rem] text-end font-tfps09-mono text-[.72rem] tabular-nums text-tfps09-ink/70">74%</span></div>
            <div class="grid grid-cols-[minmax(6rem,1fr)_1.4fr_auto] items-center gap-3"><span class="truncate font-tfps09-mono text-[.77rem]">search-index</span><span class="relative h-1.5 overflow-hidden rounded-full bg-tfps09-ink/8"><i class="tfps09-fill [--p:38%] absolute inset-y-0 left-0 w-(--p) origin-left rounded-full bg-linear-to-r from-tfps09-acc to-tfps09-acc/45"></i></span><span class="min-w-[2.6rem] text-end font-tfps09-mono text-[.72rem] tabular-nums text-tfps09-ink/70">38%</span></div>
            <div class="grid grid-cols-[minmax(6rem,1fr)_1.4fr_auto] items-center gap-3"><span class="truncate font-tfps09-mono text-[.77rem]">notify-fanout</span><span class="relative h-1.5 overflow-hidden rounded-full bg-tfps09-ink/8"><i class="tfps09-fill [--p:12%] absolute inset-y-0 left-0 w-(--p) origin-left rounded-full bg-linear-to-r from-tfps09-hold to-tfps09-hold/40"></i></span><span class="min-w-[2.6rem] text-end font-tfps09-mono text-[.72rem] tabular-nums text-tfps09-hold">held</span></div>
            <p class="border-t border-tfps09-ink/10 pt-2.5 font-tfps09-mono text-[.66rem] text-tfps09-ink/70">Window closes 18:40 UTC &middot; 2 approvals pending</p>
          </div>
        </div>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps09-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps09-panel2 not-first:-mt-16 not-first:rounded-t-[1.9rem] not-first:border-t not-first:border-tfps09-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps09-shade)] forced-colors:border-[CanvasText]" id="tfps-09-s3" aria-labelledby="tfps-09-h3">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] items-center gap-[clamp(1.5rem,4vw,3.25rem)] min-[60rem]:grid-cols-2">
        <div class="grid justify-items-start gap-[clamp(.85rem,2vh,1.3rem)] min-[60rem]:order-2">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps09-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps09-acc">02 / 03</span><span class="rounded-[.45rem] border border-tfps09-ink/12 px-2 py-[.22rem] font-tfps09-mono text-[.7rem] text-tfps09-ink/75">change health</span></p>
          <h2 class="max-w-[24ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-09-h3">Every deploy scored before anyone is paged</h2>
          <p class="max-w-[56ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps09-ink/75 [&_code]:text-tfps09-ink">Cadence watches latency, error rate and saturation for eight minutes after each promotion, compares against the pre-deploy baseline, and pauses the train the moment a signal drifts.</p>
          <ul class="grid w-full gap-3">
            <li class="grid grid-cols-[auto_1fr] items-start gap-3 border-t border-tfps09-ink/10 pt-3">
              <svg class="mt-0.5 size-5 text-tfps09-acc" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M3.5 16.5l4.5-5.4 3.3 3 3-4.4 6.2 6.8" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span class="grid gap-0.5 text-[.94rem] leading-[1.5] text-pretty text-tfps09-ink/75"><strong class="text-[.99rem] font-semibold text-tfps09-ink">Baseline diffing</strong>Compared against the previous seven deploys, not a fixed threshold.</span>
            </li>
            <li class="grid grid-cols-[auto_1fr] items-start gap-3 border-t border-tfps09-ink/10 pt-3">
              <svg class="mt-0.5 size-5 text-tfps09-acc" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.2l7.5 3.4v5.1c0 4-3.1 6.4-7.5 7.6-4.4-1.2-7.5-3.6-7.5-7.6V7.6L12 4.2Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
              <span class="grid gap-0.5 text-[.94rem] leading-[1.5] text-pretty text-tfps09-ink/75"><strong class="text-[.99rem] font-semibold text-tfps09-ink">Auto-hold, never auto-guess</strong>The train pauses and posts the diff; a human decides.</span>
            </li>
          </ul>
        </div>
        <div class="w-full overflow-hidden rounded-[1.25rem] border border-tfps09-ink/10 bg-tfps09-bg shadow-[0_30px_64px_-38px_var(--color-tfps09-shade)] forced-colors:border-[CanvasText]" role="img" aria-label="Change health panel showing p95 latency, error rate and saturation against baseline">
          <div class="flex items-center gap-1.5 border-b border-tfps09-ink/10 bg-tfps09-ink/[.04] px-3.5 py-2.5"><i class="size-2 rounded-full bg-tfps09-ink/15"></i><i class="size-2 rounded-full bg-tfps09-ink/15"></i><i class="size-2 rounded-full bg-tfps09-ink/15"></i><em class="ms-auto font-tfps09-mono text-[.66rem] not-italic text-tfps09-ink/70">health / checkout-api</em></div>
          <div class="grid gap-2.5 p-3.5">
            <dl class="grid grid-cols-3 gap-2.5">
              <div class="grid gap-0.5 rounded-[.8rem] border border-tfps09-ink/10 px-2.5 py-2.5"><dt class="font-tfps09-mono text-[.6rem] tracking-[.08em] uppercase text-tfps09-ink/70">p95 latency</dt><dd class="text-[1.15rem] font-semibold tracking-[-.03em] tabular-nums">182<span class="ms-0.5 text-[.72rem] font-normal text-tfps09-ink/70">ms</span></dd><dd class="font-tfps09-mono text-[.62rem] text-tfps09-ok">&minus;4% vs baseline</dd></div>
              <div class="grid gap-0.5 rounded-[.8rem] border border-tfps09-ink/10 px-2.5 py-2.5"><dt class="font-tfps09-mono text-[.6rem] tracking-[.08em] uppercase text-tfps09-ink/70">error rate</dt><dd class="text-[1.15rem] font-semibold tracking-[-.03em] tabular-nums">0.04<span class="ms-0.5 text-[.72rem] font-normal text-tfps09-ink/70">%</span></dd><dd class="font-tfps09-mono text-[.62rem] text-tfps09-ok">flat</dd></div>
              <div class="grid gap-0.5 rounded-[.8rem] border border-tfps09-ink/10 px-2.5 py-2.5"><dt class="font-tfps09-mono text-[.6rem] tracking-[.08em] uppercase text-tfps09-ink/70">saturation</dt><dd class="text-[1.15rem] font-semibold tracking-[-.03em] tabular-nums">61<span class="ms-0.5 text-[.72rem] font-normal text-tfps09-ink/70">%</span></dd><dd class="font-tfps09-mono text-[.62rem] text-tfps09-ok">+3 pts</dd></div>
            </dl>
            <div aria-hidden="true" class="flex h-14 items-end gap-1 px-0.5 pt-2"><i class="tfps09-grow [--v:38%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:52%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:44%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:66%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:58%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:71%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:49%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:63%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:55%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:74%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:60%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i><i class="tfps09-grow [--v:47%] h-(--v) flex-1 origin-bottom rounded-t-[.2rem] bg-linear-to-t from-tfps09-acc/55 to-tfps09-acc/18"></i></div>
            <p class="border-t border-tfps09-ink/10 pt-2.5 font-tfps09-mono text-[.66rem] text-tfps09-ink/70">Verdict: promote &middot; 8 min observation window met</p>
          </div>
        </div>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps09-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps09-panel2 not-first:-mt-16 not-first:rounded-t-[1.9rem] not-first:border-t not-first:border-tfps09-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps09-shade)] forced-colors:border-[CanvasText]" id="tfps-09-s4" aria-labelledby="tfps-09-h4">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps09-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps09-acc">03 / 03</span><span class="rounded-[.45rem] border border-tfps09-ink/12 px-2 py-[.22rem] font-tfps09-mono text-[.7rem] text-tfps09-ink/75">measured across 8,400 workspaces</span></p>
        <h2 class="max-w-[24ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-09-h4">What changes in the first quarter</h2>
        <dl class="grid w-full grid-cols-[repeat(auto-fit,minmax(11rem,1fr))] gap-[clamp(.85rem,2.5vw,1.75rem)]">
          <div class="grid gap-1.5 border-t-2 border-tfps09-acc pt-3.5"><dt class="text-[clamp(2rem,4.2vw,3.1rem)] leading-none font-semibold tracking-[-.045em] tabular-nums">41%</dt><dd class="text-[.92rem] leading-[1.45] text-pretty text-tfps09-ink/75">shorter median lead time from merge to production</dd></div>
          <div class="grid gap-1.5 border-t-2 border-tfps09-acc pt-3.5"><dt class="text-[clamp(2rem,4.2vw,3.1rem)] leading-none font-semibold tracking-[-.045em] tabular-nums">11s</dt><dd class="text-[.92rem] leading-[1.45] text-pretty text-tfps09-ink/75">median rollback, down from 6 minutes of manual steps</dd></div>
          <div class="grid gap-1.5 border-t-2 border-tfps09-acc pt-3.5"><dt class="text-[clamp(2rem,4.2vw,3.1rem)] leading-none font-semibold tracking-[-.045em] tabular-nums">99.98%</dt><dd class="text-[.92rem] leading-[1.45] text-pretty text-tfps09-ink/75">promotion success rate across 2.4M releases</dd></div>
          <div class="grid gap-1.5 border-t-2 border-tfps09-acc pt-3.5"><dt class="text-[clamp(2rem,4.2vw,3.1rem)] leading-none font-semibold tracking-[-.045em] tabular-nums">3.1&times;</dt><dd class="text-[.92rem] leading-[1.45] text-pretty text-tfps09-ink/75">more deploys per engineer per week, same headcount</dd></div>
        </dl>
        <p class="font-tfps09-mono text-[.7rem] text-tfps09-ink/70">Figures from customer telemetry, rolling 90 days, medians not means.</p>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps09-deep text-[#f6f7ff] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] not-first:-mt-16 not-first:rounded-t-[1.9rem] not-first:border-t not-first:border-tfps09-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps09-shade)] forced-colors:border-[CanvasText]" id="tfps-09-s5" aria-labelledby="tfps-09-h5">
      <div class="grid w-full max-w-[66rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex"><span class="rounded-[.45rem] border border-[#f6f7ff]/25 px-2 py-[.22rem] font-tfps09-mono text-[.7rem] text-[#f6f7ff]/75">get started</span></p>
        <h2 class="max-w-[21ch] text-[clamp(2rem,5.4vw,4.05rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-09-h5">Put your first train on the board this afternoon</h2>
        <p class="max-w-[56ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-[#f6f7ff]/75">Connect a repository, pick three services, set a window. Cadence runs the next release for you and shows the diff before it promotes anything.</p>
        <div class="flex flex-wrap items-center gap-2.5">
          <button class="group inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-full border border-transparent bg-[#a5b4fc] px-5 py-3 text-[.95rem] font-medium text-[#0a0c18] shadow-[0_14px_30px_-18px_var(--color-tfps09-acc)] transition-[translate,background-color] duration-200 hover:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-[#f6f7ff] tfps09-dark:text-[#0a0c18] motion-reduce:hover:translate-y-0" type="button">Create a workspace<svg class="size-4 transition-transform duration-200 group-hover:translate-x-0.5" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6.5l5.5 5.5-5.5 5.5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <button class="inline-flex min-h-11 cursor-pointer items-center rounded-full border bg-transparent px-[1.15rem] py-3 text-[.95rem] no-underline transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-offset-3 border-[#c7d2fe]/40 text-[#c7d2fe] hover:bg-white/10 focus-visible:outline-[#c7d2fe]" type="button">Book a 20-minute walkthrough</button>
        </div>
        <figure class="grid max-w-[46ch] gap-2.5 border-s-2 border-[#a5b4fc] ps-[1.1rem]">
          <blockquote class="text-[clamp(1.05rem,1.9vw,1.35rem)] leading-[1.45] tracking-[-.02em] text-pretty"><p>&ldquo;We cut release night from four people and two hours to one person and a coffee.&rdquo;</p></blockquote>
          <figcaption class="font-tfps09-mono text-[.68rem] tracking-[.1em] uppercase text-[#f6f7ff]/65">Alex Chen &middot; platform lead, Northwind Retail</figcaption>
        </figure>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps09-bg: #f7f8fc;
  --color-tfps09-bg: oklch(97.6% .006 270);
  --color-tfps09-panel: #ffffff;
  --color-tfps09-panel: oklch(1 0 0);
  --color-tfps09-panel2: #f0f2f9;
  --color-tfps09-panel2: oklch(95% .01 270);
  --color-tfps09-deep: #0a0c18;
  --color-tfps09-deep: oklch(0.159 0.026 275.9);
  --color-tfps09-ink: #0a0c18;
  --color-tfps09-ink: oklch(12% .02 270);
  --color-tfps09-acc: #3538cd;
  --color-tfps09-acc: oklch(46% .2 274);
  --color-tfps09-ok: #0f766e;
  --color-tfps09-ok: oklch(48% .1 175);
  --color-tfps09-hold: #b45309;
  --color-tfps09-hold: oklch(56% .13 62);
  --color-tfps09-shade: rgb(10 12 24 / .22);
  --font-tfps09-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps09-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
}
/* Theme state. Dark = OS preference XOR the toggle, so the switch always flips what you see —
   the CSS original's checkbox did nothing for visitors whose OS was already dark. */

@custom-variant tfps09-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-09:has(#tfps-09-theme:checked), .tfps-09:has(#tfps-09-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-09:not(:has(#tfps-09-theme:checked)), .tfps-09:not(:has(#tfps-09-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-09 {
  width: 100%;
  min-height: 100svh;

  @variant tfps09-dark {
    --color-tfps09-bg: #07080f;
    --color-tfps09-bg: oklch(0.137 0.016 276.8);
    --color-tfps09-panel: #0b0d16;
    --color-tfps09-panel: oklch(0.162 0.019 274.4);
    --color-tfps09-panel2: #10131e;
    --color-tfps09-panel2: oklch(0.189 0.023 272.3);
    --color-tfps09-deep: #04050b;
    --color-tfps09-deep: oklch(0.117 0.016 273.8);
    --color-tfps09-ink: #f4f5fb;
    --color-tfps09-ink: oklch(0.971 0.008 278.6);
    --color-tfps09-acc: #a5b4fc;
    --color-tfps09-acc: oklch(0.785 0.104 274.7);
    --color-tfps09-ok: #5eead4;
    --color-tfps09-ok: oklch(0.855 0.125 181.1);
    --color-tfps09-hold: #fbbf24;
    --color-tfps09-hold: oklch(0.837 0.164 84.4);
    --color-tfps09-shade: rgb(0 0 0 / .7);
  }
}
/* What stayed CSS: the mock-ups fill as they scroll into view (anonymous view() timelines). */

@keyframes tfps09-fill {
  from {
    scale: 0 1;
  }
}

@keyframes tfps09-grow {
  from {
    scale: 1 0;
  }
}

@utility tfps09-fill {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps09-fill linear both;
      animation-timeline: view();
      animation-range: entry 20% cover 45%;
    }
  }
}

@utility tfps09-grow {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps09-grow linear both;
      animation-timeline: view();
      animation-range: entry 10% cover 40%;
    }
  }
}
```
