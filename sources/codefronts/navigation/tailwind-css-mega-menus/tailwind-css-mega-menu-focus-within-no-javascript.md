---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-css-mega-menu-focus-within-no-javascript/"
title: "Tailwind CSS Mega Menu with Focus-Within (No JavaScript)"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "The reference build, ported to Tailwind CSS v4: a named <nav>, real <button> triggers with aria-expanded and aria-controls, and a full-width multi-column…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Mega Menu with Focus-Within (No JavaScript)
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-css-mega-menu-focus-within-no-javascript/

The reference build, ported to Tailwind CSS v4: a named <nav>, real <button> triggers with aria-expanded and aria-controls, and a full-width multi-column panel that opens on hover and keyboard focus. The whole open state is one custom variant, tmm01-open:, so every panel, chevron and cascade utility reads a single word. Zero JavaScript.
## HTML
```html
<section class="tmm-01 relative w-full min-h-svh bg-tmm01-bg bg-[linear-gradient(var(--color-tmm01-grid)_1px,transparent_1px),linear-gradient(90deg,var(--color-tmm01-grid)_1px,transparent_1px)] bg-size-[26px_26px] font-tmm01-sans text-tmm01-ink [&_:focus-visible]:rounded-md [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm01-acc" aria-labelledby="tmm01-title">
  <h2 class="sr-only" id="tmm01-title">Meridian</h2>

  <div class="absolute top-3 right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm01-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-xl border border-tmm01-line bg-tmm01-surf text-tmm01-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm01-acc" for="tmm01-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b border-tmm01-line bg-tmm01-surf/92 backdrop-blur-md">
    <div class="mx-auto flex min-h-17 w-[min(74rem,calc(100%-2rem))] flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,1.75rem)] pr-15 max-[52rem]:flex-col max-[52rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm01-mono text-base/none font-bold tracking-[-0.02em] text-tmm01-ink" href="#tmm01-title">
        <svg class="size-[19px] text-tmm01-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 17 12 4l8 13" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M4 20h16" fill="none" stroke="currentColor" stroke-width="2"/></svg>
        Meridian
      </a>

      <nav class="flex min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-0.5 max-[52rem]:flex-col">
          <li data-tmm01-item class="flex items-center max-[52rem]:block">
            <button type="button" aria-expanded="false" aria-controls="tmm01-panel-platform" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-[9px] px-3.5 text-[0.92rem] font-semibold text-tmm01-ink transition-colors hover:text-tmm01-acc tmm01-open:bg-tmm01-acc/11 tmm01-open:text-tmm01-acc!">Platform
              <svg class="size-[15px] transition-transform duration-200 tmm01-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="invisible absolute inset-x-0 top-full z-30 -translate-y-2.5 border-b border-tmm01-line bg-tmm01-surf opacity-0 shadow-tmm01-panel pointer-events-none transition-[opacity,translate,visibility] duration-180 tmm01-open:visible tmm01-open:translate-y-0 tmm01-open:opacity-100 tmm01-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:translate-y-0 max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm01-open:block" id="tmm01-panel-platform" aria-label="Platform">
              <div class="mx-auto grid w-[min(74rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-[clamp(0.9rem,2.6vw,2rem)] py-[clamp(1.1rem,3vw,1.9rem)] min-[68rem]:grid-cols-[repeat(3,minmax(0,1fr))_16rem] max-[52rem]:w-full">
                <section class="min-w-0 translate-y-4 opacity-0 transition-[opacity,translate] duration-[240ms,420ms] ease-tmm01-out delay-40 tmm01-open:translate-y-0 tmm01-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm01-h-build">
                  <h3 class="mb-1.5 font-tmm01-mono text-[0.68rem]/none font-bold tracking-[0.14em] text-tmm01-mut uppercase" id="tmm01-h-build">Build</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Edge runtime</b><span class="text-xs/snug text-tmm01-mut">Deploy to 34 regions</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Managed Postgres</b><span class="text-xs/snug text-tmm01-mut">Branching and PITR</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Object storage</b><span class="text-xs/snug text-tmm01-mut">S3-compatible</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Queues and jobs</b><span class="text-xs/snug text-tmm01-mut">Durable execution</span></a></li>
                  </ul>
                </section>
                <section class="min-w-0 translate-y-4 opacity-0 transition-[opacity,translate] duration-[240ms,420ms] ease-tmm01-out delay-110 tmm01-open:translate-y-0 tmm01-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm01-h-operate">
                  <h3 class="mb-1.5 font-tmm01-mono text-[0.68rem]/none font-bold tracking-[0.14em] text-tmm01-mut uppercase" id="tmm01-h-operate">Operate</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Observability</b><span class="text-xs/snug text-tmm01-mut">Traces and metrics</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Incident timeline</b><span class="text-xs/snug text-tmm01-mut">Shared context</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Access control</b><span class="text-xs/snug text-tmm01-mut">SSO and SCIM</span></a></li>
                    <li><a href="#tmm01-title" aria-current="page" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Status page</b><span class="text-xs/snug text-tmm01-mut">All systems normal</span></a></li>
                  </ul>
                </section>
                <section class="min-w-0 translate-y-4 opacity-0 transition-[opacity,translate] duration-[240ms,420ms] ease-tmm01-out delay-180 tmm01-open:translate-y-0 tmm01-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm01-h-learn">
                  <h3 class="mb-1.5 font-tmm01-mono text-[0.68rem]/none font-bold tracking-[0.14em] text-tmm01-mut uppercase" id="tmm01-h-learn">Developers</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">API reference</b><span class="text-xs/snug text-tmm01-mut">REST and gRPC</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Migration guide</b><span class="text-xs/snug text-tmm01-mut">v3 to v4</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Architecture notes</b><span class="text-xs/snug text-tmm01-mut">Design decisions</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Changelog</b><span class="text-xs/snug text-tmm01-mut">Weekly</span></a></li>
                  </ul>
                </section>
                <aside class="min-w-0 translate-y-4 opacity-0 transition-[opacity,translate] duration-[240ms,420ms] ease-tmm01-out delay-250 tmm01-open:translate-y-0 tmm01-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-1.5 rounded-xl border border-tmm01-acc/20 bg-[linear-gradient(160deg,color-mix(in_oklab,var(--color-tmm01-acc)_14%,transparent),color-mix(in_oklab,var(--color-tmm01-acc)_4%,transparent))] p-[clamp(0.85rem,2.2vw,1.15rem)]" aria-label="Platform release">
                  <p class="w-fit rounded-full bg-tmm01-acc/12 px-2 py-1 font-tmm01-mono text-[0.62rem]/none font-bold tracking-[0.16em] text-tmm01-acc uppercase">v4.2</p>
                  <p class="text-base/tight font-semibold text-balance">Regional read replicas</p>
                  <p class="text-[0.82rem] text-tmm01-mut text-pretty">Cut p95 read latency to 18ms in eu-west-2 without changing a query.</p>
                  <a class="group/cta inline-flex min-h-11 w-fit items-center gap-1.5 text-[0.83rem] font-semibold text-tmm01-acc hover:underline hover:underline-offset-3" href="#tmm01-title">Read the release note <span aria-hidden="true" class="transition-transform group-hover/cta:translate-x-1">&rarr;</span></a>
                </aside>
              </div>
            </div>
          </li>

          <li data-tmm01-item class="flex items-center max-[52rem]:block">
            <button type="button" aria-expanded="false" aria-controls="tmm01-panel-solutions" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-[9px] px-3.5 text-[0.92rem] font-semibold text-tmm01-ink transition-colors hover:text-tmm01-acc tmm01-open:bg-tmm01-acc/11 tmm01-open:text-tmm01-acc!">Solutions
              <svg class="size-[15px] transition-transform duration-200 tmm01-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="invisible absolute inset-x-0 top-full z-30 -translate-y-2.5 border-b border-tmm01-line bg-tmm01-surf opacity-0 shadow-tmm01-panel pointer-events-none transition-[opacity,translate,visibility] duration-180 tmm01-open:visible tmm01-open:translate-y-0 tmm01-open:opacity-100 tmm01-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:translate-y-0 max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm01-open:block" id="tmm01-panel-solutions" aria-label="Solutions">
              <div class="mx-auto grid w-[min(74rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-[clamp(0.9rem,2.6vw,2rem)] py-[clamp(1.1rem,3vw,1.9rem)] min-[68rem]:grid-cols-[repeat(3,minmax(0,1fr))_16rem] max-[52rem]:w-full">
                <section class="min-w-0 translate-y-4 opacity-0 transition-[opacity,translate] duration-[240ms,420ms] ease-tmm01-out delay-40 tmm01-open:translate-y-0 tmm01-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm01-h-team">
                  <h3 class="mb-1.5 font-tmm01-mono text-[0.68rem]/none font-bold tracking-[0.14em] text-tmm01-mut uppercase" id="tmm01-h-team">By team</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Platform engineering</b><span class="text-xs/snug text-tmm01-mut">Golden paths</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Data teams</b><span class="text-xs/snug text-tmm01-mut">Pipelines and warehouses</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Security</b><span class="text-xs/snug text-tmm01-mut">Audit and residency</span></a></li>
                  </ul>
                </section>
                <section class="min-w-0 translate-y-4 opacity-0 transition-[opacity,translate] duration-[240ms,420ms] ease-tmm01-out delay-110 tmm01-open:translate-y-0 tmm01-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm01-h-scale">
                  <h3 class="mb-1.5 font-tmm01-mono text-[0.68rem]/none font-bold tracking-[0.14em] text-tmm01-mut uppercase" id="tmm01-h-scale">By scale</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Startups</b><span class="text-xs/snug text-tmm01-mut">Free for 12 months</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Scale-ups</b><span class="text-xs/snug text-tmm01-mut">Usage-based</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Enterprise</b><span class="text-xs/snug text-tmm01-mut">Committed spend</span></a></li>
                  </ul>
                </section>
                <section class="min-w-0 translate-y-4 opacity-0 transition-[opacity,translate] duration-[240ms,420ms] ease-tmm01-out delay-180 tmm01-open:translate-y-0 tmm01-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm01-h-story">
                  <h3 class="mb-1.5 font-tmm01-mono text-[0.68rem]/none font-bold tracking-[0.14em] text-tmm01-mut uppercase" id="tmm01-h-story">Customers</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Vale Logistics</b><span class="text-xs/snug text-tmm01-mut">212 depots</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Basalt Health</b><span class="text-xs/snug text-tmm01-mut">HIPAA</span></a></li>
                    <li><a href="#tmm01-title" class="group/link -mx-2 grid min-h-12 content-center gap-px rounded-lg px-2 py-1.5 text-tmm01-ink transition-colors hover:bg-tmm01-acc/9 aria-[current=page]:shadow-[inset_2px_0_0_var(--color-tmm01-acc)]"><b class="text-[0.9rem]/tight font-semibold transition-colors group-hover/link:text-tmm01-acc group-aria-[current=page]/link:text-tmm01-acc">Orbit Retail</b><span class="text-xs/snug text-tmm01-mut">Peak traffic</span></a></li>
                  </ul>
                </section>
                <aside class="min-w-0 translate-y-4 opacity-0 transition-[opacity,translate] duration-[240ms,420ms] ease-tmm01-out delay-250 tmm01-open:translate-y-0 tmm01-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-1.5 rounded-xl border border-tmm01-acc/20 bg-[linear-gradient(160deg,color-mix(in_oklab,var(--color-tmm01-acc)_14%,transparent),color-mix(in_oklab,var(--color-tmm01-acc)_4%,transparent))] p-[clamp(0.85rem,2.2vw,1.15rem)]" aria-label="Customer story">
                  <p class="w-fit rounded-full bg-tmm01-acc/12 px-2 py-1 font-tmm01-mono text-[0.62rem]/none font-bold tracking-[0.16em] text-tmm01-acc uppercase">Case study</p>
                  <p class="text-base/tight font-semibold text-balance">Vale cut deploy time by 71%</p>
                  <p class="text-[0.82rem] text-tmm01-mut text-pretty">One pipeline across 212 depots, rolled out in a quarter.</p>
                  <a class="group/cta inline-flex min-h-11 w-fit items-center gap-1.5 text-[0.83rem] font-semibold text-tmm01-acc hover:underline hover:underline-offset-3" href="#tmm01-title">Read the story <span aria-hidden="true" class="transition-transform group-hover/cta:translate-x-1">&rarr;</span></a>
                </aside>
              </div>
            </div>
          </li>

          <li class="flex items-center"><a class="inline-flex min-h-11 items-center rounded-[9px] px-3.5 text-[0.92rem] font-semibold text-tmm01-ink transition-colors hover:text-tmm01-acc" href="#tmm01-title">Docs</a></li>
          <li class="flex items-center"><a class="inline-flex min-h-11 items-center rounded-[9px] px-3.5 text-[0.92rem] font-semibold text-tmm01-ink transition-colors hover:text-tmm01-acc" href="#tmm01-title">Pricing</a></li>
        </ul>
      </nav>

      <div class="ml-auto flex items-center gap-1.5 max-[52rem]:ml-0">
        <a class="inline-flex min-h-11 items-center px-3 text-[0.88rem] font-semibold text-tmm01-mut hover:text-tmm01-ink" href="#tmm01-title">Sign in</a>
        <a class="inline-flex min-h-11 items-center rounded-[9px] bg-tmm01-acc px-4 text-[0.88rem] font-semibold text-tmm01-on-acc shadow-[inset_0_1px_0_rgb(255_255_255/0.2)] hover:brightness-110" href="#tmm01-title">Start free</a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(74rem,calc(100%-2rem))] py-[clamp(3rem,10vw,6rem)]">
    <div class="grid max-w-[46rem] gap-3.5">
      <p class="inline-flex w-fit items-center gap-2 rounded-full border border-tmm01-line bg-tmm01-surf px-3 py-1.5 font-tmm01-mono text-[0.68rem]/none font-bold tracking-[0.18em] text-tmm01-acc uppercase"><span aria-hidden="true" class="size-1.5 rounded-full bg-tmm01-acc"></span>Meridian Platform</p>
      <h1 class="text-[clamp(2rem,6vw,3.6rem)]/[1.05] font-bold tracking-[-0.035em] text-balance">Ship to the edge without leaving Postgres behind.</h1>
      <p class="max-w-[36rem] text-[clamp(0.95rem,2.4vw,1.1rem)] text-tmm01-mut text-pretty">One runtime, one database, one bill. Deploy in 34 regions with a single command and keep your data where your users are.</p>
      <div class="mt-1 flex flex-wrap gap-2.5">
        <a class="inline-flex min-h-12 items-center rounded-[9px] bg-tmm01-acc px-5.5 text-[0.95rem] font-semibold text-tmm01-on-acc hover:brightness-110" href="#tmm01-title">Start free</a>
        <a class="inline-flex min-h-12 items-center rounded-[9px] border border-tmm01-line bg-tmm01-surf px-5 text-[0.95rem] font-semibold text-tmm01-ink transition-colors hover:border-tmm01-acc hover:text-tmm01-acc" href="#tmm01-title">Book a walkthrough</a>
      </div>
      <dl class="mt-[clamp(1rem,4vw,2rem)] flex flex-wrap gap-[clamp(1.25rem,5vw,3rem)] border-t border-tmm01-line pt-[clamp(1rem,3vw,1.5rem)]">
        <div><dt class="font-tmm01-mono text-[0.66rem]/none font-bold tracking-[0.16em] text-tmm01-mut uppercase">Regions</dt><dd class="mt-1.5 text-[clamp(1.3rem,3.6vw,1.7rem)]/none font-bold tracking-[-0.02em] tabular-nums">34</dd></div>
        <div><dt class="font-tmm01-mono text-[0.66rem]/none font-bold tracking-[0.16em] text-tmm01-mut uppercase">p95 read</dt><dd class="mt-1.5 text-[clamp(1.3rem,3.6vw,1.7rem)]/none font-bold tracking-[-0.02em] tabular-nums">18ms</dd></div>
        <div><dt class="font-tmm01-mono text-[0.66rem]/none font-bold tracking-[0.16em] text-tmm01-mut uppercase">Uptime</dt><dd class="mt-1.5 text-[clamp(1.3rem,3.6vw,1.7rem)]/none font-bold tracking-[-0.02em] tabular-nums">99.99%</dd></div>
      </dl>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm01-bg: #f4f6fb;
  --color-tmm01-bg: oklch(0.97 0.007 265);
  --color-tmm01-grid: #e4e9f4;
  --color-tmm01-grid: oklch(0.94 0.014 265);
  --color-tmm01-surf: #ffffff;
  --color-tmm01-surf: oklch(1 0 0);
  --color-tmm01-line: #d6dded;
  --color-tmm01-line: oklch(0.9 0.018 265);
  --color-tmm01-ink: #0c1322;
  --color-tmm01-ink: oklch(0.18 0.03 265);
  --color-tmm01-mut: #56637a;
  --color-tmm01-mut: oklch(0.48 0.035 265);
  --color-tmm01-acc: #2f5bff;
  --color-tmm01-acc: oklch(0.55 0.22 265);
  --color-tmm01-on-acc: #ffffff;
  --color-tmm01-on-acc: oklch(1 0 0);
  --font-tmm01-sans: 'Geist', system-ui, sans-serif;
  --font-tmm01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tmm01-panel: 0 26px 60px -34px rgb(12 19 34 / 0.5);
  --ease-tmm01-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open] anywhere, hover only where
   hover exists. Every panel, chevron and cascade utility reads tmm01-open: instead of three variants. */

@custom-variant tmm01-open {
  &:where([data-tmm01-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm01-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-01 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-01:has(#tmm01-theme:checked) {
  --color-tmm01-bg: #070b13;
  --color-tmm01-bg: oklch(0.14 0.02 265);
  --color-tmm01-grid: #0e1522;
  --color-tmm01-grid: oklch(0.19 0.025 265);
  --color-tmm01-surf: #111a28;
  --color-tmm01-surf: oklch(0.21 0.03 265);
  --color-tmm01-line: #24314a;
  --color-tmm01-line: oklch(0.31 0.04 265);
  --color-tmm01-ink: #e9eff7;
  --color-tmm01-ink: oklch(0.95 0.012 265);
  --color-tmm01-mut: #94a3ba;
  --color-tmm01-mut: oklch(0.71 0.035 265);
  --color-tmm01-acc: #82a0ff;
  --color-tmm01-acc: oklch(0.75 0.15 265);
  --color-tmm01-on-acc: #0a0f1c;
  --color-tmm01-on-acc: oklch(0.15 0.02 265);
}

@media (prefers-color-scheme: dark) {
  .tmm-01 {
    --color-tmm01-bg: #070b13;
    --color-tmm01-bg: oklch(0.14 0.02 265);
    --color-tmm01-grid: #0e1522;
    --color-tmm01-grid: oklch(0.19 0.025 265);
    --color-tmm01-surf: #111a28;
    --color-tmm01-surf: oklch(0.21 0.03 265);
    --color-tmm01-line: #24314a;
    --color-tmm01-line: oklch(0.31 0.04 265);
    --color-tmm01-ink: #e9eff7;
    --color-tmm01-ink: oklch(0.95 0.012 265);
    --color-tmm01-mut: #94a3ba;
    --color-tmm01-mut: oklch(0.71 0.035 265);
    --color-tmm01-acc: #82a0ff;
    --color-tmm01-acc: oklch(0.75 0.15 265);
    --color-tmm01-on-acc: #0a0f1c;
    --color-tmm01-on-acc: oklch(0.15 0.02 265);
  }

  .tmm-01:has(#tmm01-theme:checked) {
    --color-tmm01-bg: #f4f6fb;
    --color-tmm01-bg: oklch(0.97 0.007 265);
    --color-tmm01-grid: #e4e9f4;
    --color-tmm01-grid: oklch(0.94 0.014 265);
    --color-tmm01-surf: #ffffff;
    --color-tmm01-surf: oklch(1 0 0);
    --color-tmm01-line: #d6dded;
    --color-tmm01-line: oklch(0.9 0.018 265);
    --color-tmm01-ink: #0c1322;
    --color-tmm01-ink: oklch(0.18 0.03 265);
    --color-tmm01-mut: #56637a;
    --color-tmm01-mut: oklch(0.48 0.035 265);
    --color-tmm01-acc: #2f5bff;
    --color-tmm01-acc: oklch(0.55 0.22 265);
    --color-tmm01-on-acc: #ffffff;
    --color-tmm01-on-acc: oklch(1 0 0);
  }
}
```
