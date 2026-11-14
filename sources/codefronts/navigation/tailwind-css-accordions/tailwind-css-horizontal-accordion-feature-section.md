---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-horizontal-accordion-feature-section/"
title: "Tailwind CSS Horizontal Accordion Feature Section"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A landing-page features section disguised as an accordion: four gapless, saturated colour blocks — one per product pillar — where the chosen block expands to…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Horizontal Accordion Feature Section
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-horizontal-accordion-feature-section/

A landing-page features section disguised as an accordion: four gapless, saturated colour blocks — one per product pillar — where the chosen block expands to a headline, proof copy and two metrics while the rest collapse to an icon and a rotated word. Headlines scale with the panel via text-[clamp(24px,6.2cqw,40px)], and a real CTA row sits under the section.
## HTML
```html
<section class="tac-27 w-full min-h-svh grid place-items-center bg-tac27-bg px-5 py-14 font-tac27-sans text-tac27-ink" aria-label="Horizontal accordion feature section demo">
  <div class="grid w-full max-w-5xl gap-10">
    <header class="grid justify-items-center gap-4 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tac27-card px-3 py-1.5 font-tac27-mono text-xs font-medium text-tac27-mut ring-1 ring-tac27-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac27-c1"></span>Why teams switch to Relay</p>
      <h2 class="max-w-[20ch] font-tac27-display text-[clamp(28px,4.6vw,48px)] leading-[1.04] font-bold tracking-[-0.04em] text-balance">The deploy platform that gets out of your way.</h2>
      <p class="max-w-[52ch] text-base leading-relaxed text-tac27-mut">Four promises, kept on every push. Pick one to see how we hold ourselves to it.</p>
    </header>

    <div class="@container/row w-full">
      <div role="radiogroup" aria-label="Product pillars" class="flex h-[27rem] overflow-hidden rounded-[28px] shadow-tac27-block ring-1 ring-black/5 @max-2xl/row:h-auto @max-2xl/row:flex-col @max-2xl/row:rounded-3xl">

        <label class="group/p @container/panel relative flex min-w-[4.5rem] grow basis-0 cursor-pointer overflow-hidden bg-tac27-c1 text-tac27-k1 shadow-[inset_-1px_0_0_rgb(0_0_0/0.14)] transition-[flex-grow,filter] duration-[650ms] ease-[cubic-bezier(.7,0,.2,1)] last:shadow-none hover:brightness-[1.06] has-checked:grow-[5] has-checked:hover:brightness-100 has-focus-visible:outline-3 has-focus-visible:outline-offset-[-10px] has-focus-visible:outline-current motion-reduce:transition-none @max-2xl/row:basis-auto @max-2xl/row:flex-col @max-2xl/row:shadow-[inset_0_-1px_0_rgb(0_0_0/0.14)]">
          <input type="radio" name="tac27-pillar" id="tac27-fast" class="sr-only" checked>
          <span class="absolute inset-0 flex flex-col items-center justify-between py-6 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl/row:relative @max-2xl/row:min-h-[4.25rem] @max-2xl/row:flex-row @max-2xl/row:justify-start @max-2xl/row:gap-3.5 @max-2xl/row:px-5 @max-2xl/row:py-0 @max-2xl/row:group-has-checked/p:opacity-100">
            <span class="grid size-11 place-items-center rounded-full ring-1 ring-current/30 transition-transform duration-300 group-hover/p:scale-110 motion-reduce:transition-none @max-2xl/row:size-9"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg></span>
            <b class="rotate-180 font-tac27-display text-lg font-extrabold tracking-[0.1em] uppercase [writing-mode:vertical-rl] @max-2xl/row:rotate-0 @max-2xl/row:text-base @max-2xl/row:[writing-mode:horizontal-tb]">Fast</b>
            <span aria-hidden="true" class="hidden font-tac27-mono text-xs font-medium opacity-80 @max-2xl/row:ml-auto @max-2xl/row:block">01</span>
          </span>
          <span class="relative flex min-w-0 flex-1 translate-y-2.5 opacity-0 transition-[opacity,translate] duration-300 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-200 motion-reduce:transition-none @max-2xl/row:grid @max-2xl/row:grid-rows-[0fr] @max-2xl/row:translate-y-0 @max-2xl/row:transition-[grid-template-rows,opacity] @max-2xl/row:group-has-checked/p:grid-rows-[1fr] @max-2xl/row:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[23rem] overflow-hidden @max-2xl/row:min-h-0 @max-2xl/row:min-w-0">
              <span class="relative flex h-full flex-col justify-between gap-6 p-8 @max-2xl/row:h-auto @max-2xl/row:px-5 @max-2xl/row:pt-1 @max-2xl/row:pb-6">
                <svg class="pointer-events-none absolute -top-10 -right-10 size-64 opacity-[0.13] @max-2xl/row:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>
                <span class="flex items-center gap-3 @max-2xl/row:hidden">
                  <span class="grid size-11 place-items-center rounded-full bg-current/12 ring-1 ring-current/30"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg></span>
                  <span class="font-tac27-mono text-xs font-medium tracking-[0.12em] uppercase">01 — Performance</span>
                </span>
                <span class="block">
                  <span class="block font-tac27-display text-[clamp(24px,6.2cqw,40px)] leading-[1.04] font-bold tracking-[-0.035em] text-balance">Cold start to first byte in 40&nbsp;ms. Everywhere.</span>
                  <span class="mt-4 block max-w-[44ch] text-[15px] leading-relaxed opacity-90">Functions boot on the edge node closest to each visitor, so Sydney and São Paulo get the same snappy response as Virginia.</span>
                  <span class="mt-5 flex divide-x divide-current/25 border-t border-current/25 pt-3"><span class="px-4 py-3 first:pl-0"><b class="block font-tac27-display text-2xl font-bold tracking-tight">40ms</b><span class="text-[13px] opacity-85">p95 TTFB</span></span><span class="px-4 py-3 first:pl-0"><b class="block font-tac27-display text-2xl font-bold tracking-tight">312</b><span class="text-[13px] opacity-85">edge regions</span></span></span>
                </span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p @container/panel relative flex min-w-[4.5rem] grow basis-0 cursor-pointer overflow-hidden bg-tac27-c2 text-tac27-k2 shadow-[inset_-1px_0_0_rgb(0_0_0/0.14)] transition-[flex-grow,filter] duration-[650ms] ease-[cubic-bezier(.7,0,.2,1)] last:shadow-none hover:brightness-[1.06] has-checked:grow-[5] has-checked:hover:brightness-100 has-focus-visible:outline-3 has-focus-visible:outline-offset-[-10px] has-focus-visible:outline-current motion-reduce:transition-none @max-2xl/row:basis-auto @max-2xl/row:flex-col @max-2xl/row:shadow-[inset_0_-1px_0_rgb(0_0_0/0.14)]">
          <input type="radio" name="tac27-pillar" id="tac27-simple" class="sr-only">
          <span class="absolute inset-0 flex flex-col items-center justify-between py-6 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl/row:relative @max-2xl/row:min-h-[4.25rem] @max-2xl/row:flex-row @max-2xl/row:justify-start @max-2xl/row:gap-3.5 @max-2xl/row:px-5 @max-2xl/row:py-0 @max-2xl/row:group-has-checked/p:opacity-100">
            <span class="grid size-11 place-items-center rounded-full ring-1 ring-current/30 transition-transform duration-300 group-hover/p:scale-110 motion-reduce:transition-none @max-2xl/row:size-9"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h16M4 12h11M4 18h7"/></svg></span>
            <b class="rotate-180 font-tac27-display text-lg font-extrabold tracking-[0.1em] uppercase [writing-mode:vertical-rl] @max-2xl/row:rotate-0 @max-2xl/row:text-base @max-2xl/row:[writing-mode:horizontal-tb]">Simple</b>
            <span aria-hidden="true" class="hidden font-tac27-mono text-xs font-medium opacity-80 @max-2xl/row:ml-auto @max-2xl/row:block">02</span>
          </span>
          <span class="relative flex min-w-0 flex-1 translate-y-2.5 opacity-0 transition-[opacity,translate] duration-300 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-200 motion-reduce:transition-none @max-2xl/row:grid @max-2xl/row:grid-rows-[0fr] @max-2xl/row:translate-y-0 @max-2xl/row:transition-[grid-template-rows,opacity] @max-2xl/row:group-has-checked/p:grid-rows-[1fr] @max-2xl/row:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[23rem] overflow-hidden @max-2xl/row:min-h-0 @max-2xl/row:min-w-0">
              <span class="relative flex h-full flex-col justify-between gap-6 p-8 @max-2xl/row:h-auto @max-2xl/row:px-5 @max-2xl/row:pt-1 @max-2xl/row:pb-6">
                <svg class="pointer-events-none absolute -top-10 -right-10 size-64 opacity-[0.13] @max-2xl/row:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h16M4 12h11M4 18h7"/></svg>
                <span class="flex items-center gap-3 @max-2xl/row:hidden">
                  <span class="grid size-11 place-items-center rounded-full bg-current/12 ring-1 ring-current/30"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h16M4 12h11M4 18h7"/></svg></span>
                  <span class="font-tac27-mono text-xs font-medium tracking-[0.12em] uppercase">02 — Developer experience</span>
                </span>
                <span class="block">
                  <span class="block font-tac27-display text-[clamp(24px,6.2cqw,40px)] leading-[1.04] font-bold tracking-[-0.035em] text-balance">One config file. Twelve keys. You’ll memorise them.</span>
                  <span class="mt-4 block max-w-[44ch] text-[15px] leading-relaxed opacity-90">No YAML pyramids, no plugin marketplace. Framework detection does the rest, and every key is documented on one page.</span>
                  <span class="mt-5 flex divide-x divide-current/25 border-t border-current/25 pt-3"><span class="px-4 py-3 first:pl-0"><b class="block font-tac27-display text-2xl font-bold tracking-tight">12</b><span class="text-[13px] opacity-85">config keys</span></span><span class="px-4 py-3 first:pl-0"><b class="block font-tac27-display text-2xl font-bold tracking-tight">0</b><span class="text-[13px] opacity-85">build plugins</span></span></span>
                </span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p @container/panel relative flex min-w-[4.5rem] grow basis-0 cursor-pointer overflow-hidden bg-tac27-c3 text-tac27-k3 shadow-[inset_-1px_0_0_rgb(0_0_0/0.14)] transition-[flex-grow,filter] duration-[650ms] ease-[cubic-bezier(.7,0,.2,1)] last:shadow-none hover:brightness-[1.06] has-checked:grow-[5] has-checked:hover:brightness-100 has-focus-visible:outline-3 has-focus-visible:outline-offset-[-10px] has-focus-visible:outline-current motion-reduce:transition-none @max-2xl/row:basis-auto @max-2xl/row:flex-col @max-2xl/row:shadow-[inset_0_-1px_0_rgb(0_0_0/0.14)]">
          <input type="radio" name="tac27-pillar" id="tac27-safe" class="sr-only">
          <span class="absolute inset-0 flex flex-col items-center justify-between py-6 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl/row:relative @max-2xl/row:min-h-[4.25rem] @max-2xl/row:flex-row @max-2xl/row:justify-start @max-2xl/row:gap-3.5 @max-2xl/row:px-5 @max-2xl/row:py-0 @max-2xl/row:group-has-checked/p:opacity-100">
            <span class="grid size-11 place-items-center rounded-full ring-1 ring-current/30 transition-transform duration-300 group-hover/p:scale-110 motion-reduce:transition-none @max-2xl/row:size-9"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 20 6v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="m9 12 2 2 4-4"/></svg></span>
            <b class="rotate-180 font-tac27-display text-lg font-extrabold tracking-[0.1em] uppercase [writing-mode:vertical-rl] @max-2xl/row:rotate-0 @max-2xl/row:text-base @max-2xl/row:[writing-mode:horizontal-tb]">Safe</b>
            <span aria-hidden="true" class="hidden font-tac27-mono text-xs font-medium opacity-80 @max-2xl/row:ml-auto @max-2xl/row:block">03</span>
          </span>
          <span class="relative flex min-w-0 flex-1 translate-y-2.5 opacity-0 transition-[opacity,translate] duration-300 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-200 motion-reduce:transition-none @max-2xl/row:grid @max-2xl/row:grid-rows-[0fr] @max-2xl/row:translate-y-0 @max-2xl/row:transition-[grid-template-rows,opacity] @max-2xl/row:group-has-checked/p:grid-rows-[1fr] @max-2xl/row:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[23rem] overflow-hidden @max-2xl/row:min-h-0 @max-2xl/row:min-w-0">
              <span class="relative flex h-full flex-col justify-between gap-6 p-8 @max-2xl/row:h-auto @max-2xl/row:px-5 @max-2xl/row:pt-1 @max-2xl/row:pb-6">
                <svg class="pointer-events-none absolute -top-10 -right-10 size-64 opacity-[0.13] @max-2xl/row:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 20 6v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>
                <span class="flex items-center gap-3 @max-2xl/row:hidden">
                  <span class="grid size-11 place-items-center rounded-full bg-current/12 ring-1 ring-current/30"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 20 6v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="m9 12 2 2 4-4"/></svg></span>
                  <span class="font-tac27-mono text-xs font-medium tracking-[0.12em] uppercase">03 — Reliability</span>
                </span>
                <span class="block">
                  <span class="block font-tac27-display text-[clamp(24px,6.2cqw,40px)] leading-[1.04] font-bold tracking-[-0.035em] text-balance">Every deploy is a snapshot. Rollback is one click.</span>
                  <span class="mt-4 block max-w-[44ch] text-[15px] leading-relaxed opacity-90">Immutable builds, instant promotion and automatic rollbacks when error rates spike — before your pager does.</span>
                  <span class="mt-5 flex divide-x divide-current/25 border-t border-current/25 pt-3"><span class="px-4 py-3 first:pl-0"><b class="block font-tac27-display text-2xl font-bold tracking-tight">1-click</b><span class="text-[13px] opacity-85">rollback</span></span><span class="px-4 py-3 first:pl-0"><b class="block font-tac27-display text-2xl font-bold tracking-tight">99.99%</b><span class="text-[13px] opacity-85">uptime SLA</span></span></span>
                </span>
              </span>
            </span>
          </span>
        </label>

        <label class="group/p @container/panel relative flex min-w-[4.5rem] grow basis-0 cursor-pointer overflow-hidden bg-tac27-c4 text-tac27-k4 shadow-[inset_-1px_0_0_rgb(0_0_0/0.14)] transition-[flex-grow,filter] duration-[650ms] ease-[cubic-bezier(.7,0,.2,1)] last:shadow-none hover:brightness-[1.06] has-checked:grow-[5] has-checked:hover:brightness-100 has-focus-visible:outline-3 has-focus-visible:outline-offset-[-10px] has-focus-visible:outline-current motion-reduce:transition-none @max-2xl/row:basis-auto @max-2xl/row:flex-col @max-2xl/row:shadow-[inset_0_-1px_0_rgb(0_0_0/0.14)]">
          <input type="radio" name="tac27-pillar" id="tac27-open" class="sr-only">
          <span class="absolute inset-0 flex flex-col items-center justify-between py-6 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl/row:relative @max-2xl/row:min-h-[4.25rem] @max-2xl/row:flex-row @max-2xl/row:justify-start @max-2xl/row:gap-3.5 @max-2xl/row:px-5 @max-2xl/row:py-0 @max-2xl/row:group-has-checked/p:opacity-100">
            <span class="grid size-11 place-items-center rounded-full ring-1 ring-current/30 transition-transform duration-300 group-hover/p:scale-110 motion-reduce:transition-none @max-2xl/row:size-9"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 5l-4 14"/></svg></span>
            <b class="rotate-180 font-tac27-display text-lg font-extrabold tracking-[0.1em] uppercase [writing-mode:vertical-rl] @max-2xl/row:rotate-0 @max-2xl/row:text-base @max-2xl/row:[writing-mode:horizontal-tb]">Open</b>
            <span aria-hidden="true" class="hidden font-tac27-mono text-xs font-medium opacity-80 @max-2xl/row:ml-auto @max-2xl/row:block">04</span>
          </span>
          <span class="relative flex min-w-0 flex-1 translate-y-2.5 opacity-0 transition-[opacity,translate] duration-300 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-200 motion-reduce:transition-none @max-2xl/row:grid @max-2xl/row:grid-rows-[0fr] @max-2xl/row:translate-y-0 @max-2xl/row:transition-[grid-template-rows,opacity] @max-2xl/row:group-has-checked/p:grid-rows-[1fr] @max-2xl/row:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[23rem] overflow-hidden @max-2xl/row:min-h-0 @max-2xl/row:min-w-0">
              <span class="relative flex h-full flex-col justify-between gap-6 p-8 @max-2xl/row:h-auto @max-2xl/row:px-5 @max-2xl/row:pt-1 @max-2xl/row:pb-6">
                <svg class="pointer-events-none absolute -top-10 -right-10 size-64 opacity-[0.13] @max-2xl/row:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 5l-4 14"/></svg>
                <span class="flex items-center gap-3 @max-2xl/row:hidden">
                  <span class="grid size-11 place-items-center rounded-full bg-current/12 ring-1 ring-current/30"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 5l-4 14"/></svg></span>
                  <span class="font-tac27-mono text-xs font-medium tracking-[0.12em] uppercase">04 — Ownership</span>
                </span>
                <span class="block">
                  <span class="block font-tac27-display text-[clamp(24px,6.2cqw,40px)] leading-[1.04] font-bold tracking-[-0.035em] text-balance">MIT licensed. Self-host it, or let us run it.</span>
                  <span class="mt-4 block max-w-[44ch] text-[15px] leading-relaxed opacity-90">The cloud runs exactly the same code you can clone. No lock-in clauses, and an export button that actually exports.</span>
                  <span class="mt-5 flex divide-x divide-current/25 border-t border-current/25 pt-3"><span class="px-4 py-3 first:pl-0"><b class="block font-tac27-display text-2xl font-bold tracking-tight">MIT</b><span class="text-[13px] opacity-85">license</span></span><span class="px-4 py-3 first:pl-0"><b class="block font-tac27-display text-2xl font-bold tracking-tight">18.4k</b><span class="text-[13px] opacity-85">GitHub stars</span></span></span>
                </span>
              </span>
            </span>
          </span>
        </label>

      </div>
    </div>

    <div class="flex flex-wrap items-center justify-center gap-3">
      <a href="#" class="inline-flex min-h-11 items-center gap-2 rounded-full bg-tac27-ink px-5 text-sm font-semibold text-tac27-bg shadow-[0_8px_20px_-8px_rgb(0_0_0/0.5)] transition-[translate,box-shadow] hover:-translate-y-0.5 hover:shadow-[0_12px_24px_-8px_rgb(0_0_0/0.5)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac27-c3 motion-reduce:transition-none">Start building free <svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      <a href="#" class="inline-flex min-h-11 items-center rounded-full bg-tac27-card px-5 text-sm font-semibold text-tac27-ink ring-1 ring-tac27-line transition-colors hover:bg-tac27-line/60 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac27-c3">Book a demo</a>
      <p class="w-full text-center text-[13px] text-tac27-mut">No credit card · 14-day Pro trial · Cancel in one click</p>
    </div>

    <p aria-hidden="true" class="max-w-full justify-self-center rounded-full border border-tac27-line bg-tac27-card/70 px-3.5 py-2 text-center font-tac27-mono text-[11.5px] text-balance text-tac27-mut">@container/panel · text-[…6.2cqw…] · ring-current/30</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac27-bg: #f5f3ee;
  --color-tac27-bg: oklch(0.966 0.007 85);
  --color-tac27-card: #ffffff;
  --color-tac27-card: oklch(1 0 0);
  --color-tac27-line: #e2ded5;
  --color-tac27-line: oklch(0.9 0.012 85);
  --color-tac27-ink: #18171b;
  --color-tac27-ink: oklch(0.2 0.006 290);
  --color-tac27-mut: #59565f;
  --color-tac27-mut: oklch(0.47 0.012 290);
  --color-tac27-c1: #ff6b4a;
  --color-tac27-c1: oklch(0.7 0.19 35);
  --color-tac27-k1: #2a0b04;
  --color-tac27-k1: oklch(0.2 0.05 35);
  --color-tac27-c2: #ffc933;
  --color-tac27-c2: oklch(0.86 0.16 85);
  --color-tac27-k2: #352400;
  --color-tac27-k2: oklch(0.27 0.06 80);
  --color-tac27-c3: #2a4bd9;
  --color-tac27-c3: oklch(0.48 0.21 266);
  --color-tac27-k3: #ffffff;
  --color-tac27-k3: oklch(1 0 0);
  --color-tac27-c4: #0f6a4f;
  --color-tac27-c4: oklch(0.46 0.09 165);
  --color-tac27-k4: #ffffff;
  --color-tac27-k4: oklch(1 0 0);
  --shadow-tac27-block: 0 1px 2px oklch(0.2 0.01 290 / 0.08), 0 30px 60px -24px oklch(0.25 0.04 290 / 0.35);
  --font-tac27-display: 'Unbounded', system-ui, sans-serif;
  --font-tac27-sans: 'Archivo', system-ui, sans-serif;
  --font-tac27-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-27 {
  width: 100%;
  min-height: 100svh;
}
```
