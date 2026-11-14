---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-vertical-tabs-with-sliding-active-indicator/"
title: "Tailwind Vertical Tabs with Sliding Active Indicator"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A release-channel picker where one gradient pill springs between Stable, Beta, Canary and Legacy with zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Tabs with Sliding Active Indicator
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-vertical-tabs-with-sliding-active-indicator/

A release-channel picker where one gradient pill springs between Stable, Beta, Canary and Legacy with zero JavaScript. Each has-[#tvt-05-t2:checked]:[--tvt05-i:1] variant writes an index onto the rail, the pill translates by index &times; step, and a 7% overshoot curve gives it mass &mdash; no measuring, no resize listener, no layout thrash.
## HTML
```html
<section class="tvt-05 w-full min-h-svh grid place-items-center bg-tvt05-bg bg-[radial-gradient(60%_50%_at_80%_0%,var(--color-tvt05-glow),transparent_70%),radial-gradient(55%_45%_at_10%_100%,var(--color-tvt05-glow2),transparent_70%)] px-4 py-14 font-tvt05-sans text-tvt05-ink antialiased sm:px-6" aria-label="Tailwind vertical tabs with sliding active indicator demo">
  <div class="grid w-full max-w-[54rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="rounded-full bg-tvt05-card px-3 py-1.5 font-tvt05-mono text-[11.5px] text-tvt05-acc-ink ring-1 ring-tvt05-line">has-[:checked] → --tvt05-i → translate</p>
      <h2 class="text-[clamp(28px,4.4vw,42px)] leading-[1.05] font-bold tracking-[-0.04em] text-balance">One indicator, <span class="bg-linear-to-r from-tvt05-hl to-tvt05-hl2 bg-clip-text pe-1 text-transparent">four stops</span></h2>
      <p class="max-w-[46ch] text-[15px] leading-relaxed text-tvt05-mut text-pretty">Pick a release channel. A single gradient pill springs to the checked row &mdash; positioned by arithmetic, not measurement.</p>
    </header>

    <div class="group/card @container w-full overflow-hidden rounded-[26px] bg-tvt05-card shadow-tvt05-card ring-1 ring-tvt05-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <div class="grid grid-cols-[clamp(13rem,32%,16.5rem)_minmax(0,1fr)] @max-[38rem]:grid-cols-1">
        <div class="border-e border-tvt05-line bg-tvt05-rail p-3 @max-[38rem]:border-e-0 @max-[38rem]:border-b">
          <p class="px-3 pt-2 pb-3 text-[11.5px] font-semibold tracking-[0.14em] text-tvt05-mut uppercase">Release channel</p>
          <div role="radiogroup" aria-label="Release channel" class="relative [--tvt05-i:0] [--tvt05-step:4rem] has-[#tvt-05-t2:checked]:[--tvt05-i:1] has-[#tvt-05-t3:checked]:[--tvt05-i:2] has-[#tvt-05-t4:checked]:[--tvt05-i:3]">
            <span data-ind aria-hidden="true" class="pointer-events-none absolute inset-x-0 top-0 h-(--tvt05-step) translate-y-[calc(var(--tvt05-i)*var(--tvt05-step))] rounded-2xl bg-linear-to-br from-tvt05-acc to-tvt05-acc2 shadow-tvt05-pill transition-[translate] duration-500 ease-[cubic-bezier(.34,1.32,.44,1)] motion-reduce:transition-none"><span class="absolute inset-0 rounded-2xl bg-[linear-gradient(180deg,oklch(1_0_0/0.22),transparent_55%)]"></span></span>

          <input type="radio" name="tvt-05-ch" id="tvt-05-t1" class="peer/t1 sr-only" checked>
          <label for="tvt-05-t1" class="relative z-10 flex h-(--tvt05-step) cursor-pointer items-center gap-3 rounded-2xl px-4 text-tvt05-mut transition-colors duration-300 select-none hover:text-tvt05-ink peer-checked/t1:text-white peer-focus-visible/t1:outline-2 peer-focus-visible/t1:outline-offset-2 peer-focus-visible/t1:outline-tvt05-ring motion-reduce:transition-none">
            <span aria-hidden="true" class="size-2.5 shrink-0 rounded-full bg-tvt05-ok text-tvt05-ok ring-[3px] ring-current/15"></span>
            <span class="grid min-w-0 leading-tight"><span class="text-[15px] font-semibold tracking-[-0.01em]">Stable</span><span class="font-tvt05-mono text-[11.5px] opacity-80">v4.2.0</span></span>
          </label>

          <input type="radio" name="tvt-05-ch" id="tvt-05-t2" class="peer/t2 sr-only">
          <label for="tvt-05-t2" class="relative z-10 flex h-(--tvt05-step) cursor-pointer items-center gap-3 rounded-2xl px-4 text-tvt05-mut transition-colors duration-300 select-none hover:text-tvt05-ink peer-checked/t2:text-white peer-focus-visible/t2:outline-2 peer-focus-visible/t2:outline-offset-2 peer-focus-visible/t2:outline-tvt05-ring motion-reduce:transition-none">
            <span aria-hidden="true" class="size-2.5 shrink-0 rounded-full bg-tvt05-warn text-tvt05-warn ring-[3px] ring-current/15"></span>
            <span class="grid min-w-0 leading-tight"><span class="text-[15px] font-semibold tracking-[-0.01em]">Beta</span><span class="font-tvt05-mono text-[11.5px] opacity-80">v4.3.0-rc.1</span></span>
          </label>

          <input type="radio" name="tvt-05-ch" id="tvt-05-t3" class="peer/t3 sr-only">
          <label for="tvt-05-t3" class="relative z-10 flex h-(--tvt05-step) cursor-pointer items-center gap-3 rounded-2xl px-4 text-tvt05-mut transition-colors duration-300 select-none hover:text-tvt05-ink peer-checked/t3:text-white peer-focus-visible/t3:outline-2 peer-focus-visible/t3:outline-offset-2 peer-focus-visible/t3:outline-tvt05-ring motion-reduce:transition-none">
            <span aria-hidden="true" class="size-2.5 shrink-0 rounded-full bg-tvt05-hot text-tvt05-hot ring-[3px] ring-current/15"></span>
            <span class="grid min-w-0 leading-tight"><span class="text-[15px] font-semibold tracking-[-0.01em]">Canary</span><span class="font-tvt05-mono text-[11.5px] opacity-80">nightly · 4f2a91c</span></span>
          </label>

          <input type="radio" name="tvt-05-ch" id="tvt-05-t4" class="peer/t4 sr-only">
          <label for="tvt-05-t4" class="relative z-10 flex h-(--tvt05-step) cursor-pointer items-center gap-3 rounded-2xl px-4 text-tvt05-mut transition-colors duration-300 select-none hover:text-tvt05-ink peer-checked/t4:text-white peer-focus-visible/t4:outline-2 peer-focus-visible/t4:outline-offset-2 peer-focus-visible/t4:outline-tvt05-ring motion-reduce:transition-none">
            <span aria-hidden="true" class="size-2.5 shrink-0 rounded-full bg-tvt05-mut text-tvt05-mut ring-[3px] ring-current/15"></span>
            <span class="grid min-w-0 leading-tight"><span class="text-[15px] font-semibold tracking-[-0.01em]">Legacy</span><span class="font-tvt05-mono text-[11.5px] opacity-80">v3.9.x · LTS</span></span>
          </label>
          </div>
          <p class="mt-3 flex items-center gap-2 rounded-xl px-3 py-2.5 text-[12.5px] text-tvt05-mut @max-[38rem]:hidden"><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 6v4.5l3 1.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>Auto-update checks every 6 h</p>
        </div>

        <div class="grid min-h-[22rem] p-6 sm:p-8">

        <article id="tvt-05-p1" aria-labelledby="tvt-05-h1" class="invisible col-start-1 row-start-1 translate-y-2.5 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-05-t1:checked]/card:visible group-has-[#tvt-05-t1:checked]/card:translate-y-0 group-has-[#tvt-05-t1:checked]/card:opacity-100 motion-reduce:transition-none">
          <div class="flex flex-wrap items-center gap-2.5"><span class="rounded-full px-2.5 py-1 text-[11.5px] font-semibold bg-tvt05-ok/14 text-tvt05-ok">Recommended</span><span class="font-tvt05-mono text-[12px] text-tvt05-mut">Released Oct 21, 2026</span></div>
          <h3 id="tvt-05-h1" class="mt-3 text-[clamp(22px,2.8vw,28px)] font-bold tracking-[-0.03em]">Stable 4.2.0</h3>
          <p class="mt-2 max-w-[46ch] text-[14.5px] leading-relaxed text-tvt05-mut text-pretty">Battle-tested for production. Security patches land within 48 hours.</p>
          <div class="mt-5"><div class="flex items-center gap-3"><span class="text-[12.5px] font-medium text-tvt05-mut">Stability</span><span aria-hidden="true" class="flex gap-1"><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span></span><span class="text-[12.5px] font-semibold">Production-ready</span></div></div>
          <ul class="mt-5 grid gap-2.5 text-[14px]"><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Position is arithmetic: the pill moves <code class="font-tvt05-mono text-[12.5px] text-tvt05-acc-ink">index × step</code>, never measured</span></li><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Incremental builds are 38% faster on large monorepos</span></li><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">New <b class="font-semibold">--strict-env</b> flag blocks undeclared variables</span></li></ul>
          <div class="mt-5 flex items-center gap-3 rounded-xl bg-tvt05-code px-4 py-3 font-tvt05-mono text-[13px] text-tvt05-code-ink ring-1 ring-white/8"><span aria-hidden="true" class="text-tvt05-acc2">$</span><code class="min-w-0 flex-1 truncate">npm i @northwind/[email protected]</code><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="shrink-0 opacity-60"><rect x="6.5" y="6.5" width="10" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13.5 6.5V5a1.5 1.5 0 0 0-1.5-1.5H5A1.5 1.5 0 0 0 3.5 5v7A1.5 1.5 0 0 0 5 13.5h1.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></div>
        </article>

        <article id="tvt-05-p2" aria-labelledby="tvt-05-h2" class="invisible col-start-1 row-start-1 translate-y-2.5 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-05-t2:checked]/card:visible group-has-[#tvt-05-t2:checked]/card:translate-y-0 group-has-[#tvt-05-t2:checked]/card:opacity-100 motion-reduce:transition-none">
          <div class="flex flex-wrap items-center gap-2.5"><span class="rounded-full px-2.5 py-1 text-[11.5px] font-semibold bg-tvt05-warn/16 text-tvt05-warn">Pre-release</span><span class="font-tvt05-mono text-[12px] text-tvt05-mut">Released Oct 26, 2026</span></div>
          <h3 id="tvt-05-h2" class="mt-3 text-[clamp(22px,2.8vw,28px)] font-bold tracking-[-0.03em]">Beta 4.3.0-rc.1</h3>
          <p class="mt-2 max-w-[46ch] text-[14.5px] leading-relaxed text-tvt05-mut text-pretty">Feature-complete and in final testing. Great for staging environments.</p>
          <div class="mt-5"><div class="flex items-center gap-3"><span class="text-[12.5px] font-medium text-tvt05-mut">Stability</span><span aria-hidden="true" class="flex gap-1"><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-tvt05-line"></span></span><span class="text-[12.5px] font-semibold">Release candidate</span></div></div>
          <ul class="mt-5 grid gap-2.5 text-[14px]"><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty"><code class="font-tvt05-mono text-[12.5px] text-tvt05-acc-ink">:has()</code> reaches upward: a checked radio sets <code class="font-tvt05-mono text-[12.5px] text-tvt05-acc-ink">--tvt05-i</code> on its ancestor</span></li><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Edge functions gain streaming responses</span></li><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Config file can now be written in TypeScript</span></li></ul>
          <div class="mt-5 flex items-center gap-3 rounded-xl bg-tvt05-code px-4 py-3 font-tvt05-mono text-[13px] text-tvt05-code-ink ring-1 ring-white/8"><span aria-hidden="true" class="text-tvt05-acc2">$</span><code class="min-w-0 flex-1 truncate">npm i @northwind/cli@beta</code><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="shrink-0 opacity-60"><rect x="6.5" y="6.5" width="10" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13.5 6.5V5a1.5 1.5 0 0 0-1.5-1.5H5A1.5 1.5 0 0 0 3.5 5v7A1.5 1.5 0 0 0 5 13.5h1.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></div>
        </article>

        <article id="tvt-05-p3" aria-labelledby="tvt-05-h3" class="invisible col-start-1 row-start-1 translate-y-2.5 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-05-t3:checked]/card:visible group-has-[#tvt-05-t3:checked]/card:translate-y-0 group-has-[#tvt-05-t3:checked]/card:opacity-100 motion-reduce:transition-none">
          <div class="flex flex-wrap items-center gap-2.5"><span class="rounded-full px-2.5 py-1 text-[11.5px] font-semibold bg-tvt05-hot/14 text-tvt05-hot">Unstable</span><span class="font-tvt05-mono text-[12px] text-tvt05-mut">Built 2 hours ago</span></div>
          <h3 id="tvt-05-h3" class="mt-3 text-[clamp(22px,2.8vw,28px)] font-bold tracking-[-0.03em]">Canary nightly</h3>
          <p class="mt-2 max-w-[46ch] text-[14.5px] leading-relaxed text-tvt05-mut text-pretty">Fresh from <code class="font-tvt05-mono text-[12.5px]">main</code> every night. Expect breakage &mdash; and the future.</p>
          <div class="mt-5"><div class="flex items-center gap-3"><span class="text-[12.5px] font-medium text-tvt05-mut">Stability</span><span aria-hidden="true" class="flex gap-1"><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-tvt05-line"></span><span class="h-1.5 w-5 rounded-full bg-tvt05-line"></span><span class="h-1.5 w-5 rounded-full bg-tvt05-line"></span></span><span class="text-[12.5px] font-semibold">Experimental</span></div></div>
          <ul class="mt-5 grid gap-2.5 text-[14px]"><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">The curve is the product: <code class="font-tvt05-mono text-[12.5px] text-tvt05-acc-ink">ease-[cubic-bezier(.34,1.32,.44,1)]</code> overshoots ~7%</span></li><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Rust-based bundler behind <b class="font-semibold">--turbo</b></span></li><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Experimental partial prerendering</span></li></ul>
          <div class="mt-5 flex items-center gap-3 rounded-xl bg-tvt05-code px-4 py-3 font-tvt05-mono text-[13px] text-tvt05-code-ink ring-1 ring-white/8"><span aria-hidden="true" class="text-tvt05-acc2">$</span><code class="min-w-0 flex-1 truncate">npm i @northwind/cli@canary</code><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="shrink-0 opacity-60"><rect x="6.5" y="6.5" width="10" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13.5 6.5V5a1.5 1.5 0 0 0-1.5-1.5H5A1.5 1.5 0 0 0 3.5 5v7A1.5 1.5 0 0 0 5 13.5h1.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></div>
        </article>

        <article id="tvt-05-p4" aria-labelledby="tvt-05-h4" class="invisible col-start-1 row-start-1 translate-y-2.5 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-05-t4:checked]/card:visible group-has-[#tvt-05-t4:checked]/card:translate-y-0 group-has-[#tvt-05-t4:checked]/card:opacity-100 motion-reduce:transition-none">
          <div class="flex flex-wrap items-center gap-2.5"><span class="rounded-full px-2.5 py-1 text-[11.5px] font-semibold bg-tvt05-ink/8 text-tvt05-mut">Security fixes only</span><span class="font-tvt05-mono text-[12px] text-tvt05-mut">End of life: Mar 31, 2027</span></div>
          <h3 id="tvt-05-h4" class="mt-3 text-[clamp(22px,2.8vw,28px)] font-bold tracking-[-0.03em]">Legacy 3.9.x</h3>
          <p class="mt-2 max-w-[46ch] text-[14.5px] leading-relaxed text-tvt05-mut text-pretty">For teams pinned to Node 18. Plan your upgrade &mdash; the codemod does most of it.</p>
          <div class="mt-5"><div class="flex items-center gap-3"><span class="text-[12.5px] font-medium text-tvt05-mut">Stability</span><span aria-hidden="true" class="flex gap-1"><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span><span class="h-1.5 w-5 rounded-full bg-linear-to-r from-tvt05-acc to-tvt05-acc2"></span></span><span class="text-[12.5px] font-semibold">Frozen</span></div></div>
          <ul class="mt-5 grid gap-2.5 text-[14px]"><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Degrades quietly: without <code class="font-tvt05-mono text-[12.5px] text-tvt05-acc-ink">:has()</code> the pill hides and the checked row paints itself</span></li><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Critical CVE patches until EOL</span></li><li class="flex gap-2.5"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt05-acc-ink"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-pretty">Run <b class="font-semibold">npx @northwind/upgrade</b> to migrate</span></li></ul>
          <div class="mt-5 flex items-center gap-3 rounded-xl bg-tvt05-code px-4 py-3 font-tvt05-mono text-[13px] text-tvt05-code-ink ring-1 ring-white/8"><span aria-hidden="true" class="text-tvt05-acc2">$</span><code class="min-w-0 flex-1 truncate">npm i @northwind/cli@3</code><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="shrink-0 opacity-60"><rect x="6.5" y="6.5" width="10" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13.5 6.5V5a1.5 1.5 0 0 0-1.5-1.5H5A1.5 1.5 0 0 0 3.5 5v7A1.5 1.5 0 0 0 5 13.5h1.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></div>
        </article>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt05-card px-3.5 py-2 text-center font-tvt05-mono text-[11.5px] text-tvt05-mut ring-1 ring-tvt05-line">has-[…]:[--tvt05-i:n] · spring easing</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt05-bg: #f7f0fd;
  --color-tvt05-bg: oklch(0.965 0.018 310);
  --color-tvt05-glow: #f7b9f099;
  --color-tvt05-glow: oklch(0.86 0.1 330 / 0.6);
  --color-tvt05-glow2: #cbcbff8c;
  --color-tvt05-glow2: oklch(0.86 0.09 285 / 0.55);
  --color-tvt05-card: #fefdff;
  --color-tvt05-card: oklch(0.995 0.004 310);
  --color-tvt05-rail: #f9f5fd;
  --color-tvt05-rail: oklch(0.975 0.012 310);
  --color-tvt05-ink: #1e142e;
  --color-tvt05-ink: oklch(0.22 0.05 300);
  --color-tvt05-mut: #615874;
  --color-tvt05-mut: oklch(0.48 0.045 300);
  --color-tvt05-line: #e6ddee;
  --color-tvt05-line: oklch(0.91 0.025 310);
  --color-tvt05-acc: #7530e8;
  --color-tvt05-acc: oklch(0.52 0.25 292);
  --color-tvt05-acc2: #d2119a;
  --color-tvt05-acc2: oklch(0.58 0.24 345);
  --color-tvt05-acc-ink: #731dc5;
  --color-tvt05-acc-ink: oklch(0.47 0.23 300);
  --color-tvt05-hl: #7530e8;
  --color-tvt05-hl: oklch(0.52 0.25 292);
  --color-tvt05-hl2: #de1994;
  --color-tvt05-hl2: oklch(0.6 0.24 350);
  --color-tvt05-ring: #8b3ae5;
  --color-tvt05-ring: oklch(0.55 0.24 300);
  --color-tvt05-ok: #007e46;
  --color-tvt05-ok: oklch(0.52 0.14 155);
  --color-tvt05-warn: #b36300;
  --color-tvt05-warn: oklch(0.58 0.14 60);
  --color-tvt05-hot: #d0126f;
  --color-tvt05-hot: oklch(0.56 0.22 0);
  --color-tvt05-code: #1e142e;
  --color-tvt05-code: oklch(0.22 0.05 300);
  --color-tvt05-code-ink: #eae5f4;
  --color-tvt05-code-ink: oklch(0.93 0.02 300);
  --font-tvt05-sans: 'Sora', system-ui, sans-serif;
  --font-tvt05-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tvt05-card: 0 1px 2px oklch(0.3 0.1 300 / 0.06), 0 34px 80px -34px oklch(0.4 0.22 310 / 0.42);
  --shadow-tvt05-pill: 0 12px 28px -10px oklch(0.55 0.25 320 / 0.65), 0 2px 6px -2px oklch(0.4 0.2 300 / 0.4), inset 0 1px 0 oklch(1 0 0 / 0.3);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-05 {
  width: 100%;
  min-height: 100svh;
}
/* Fallback for engines without :has(): the index can't move the pill, so hide it and let the checked row paint itself. */

@supports not selector(:has(*)) {
  .tvt-05 [data-ind] {
    display: none;
  }

  .tvt-05 input:checked + label {
    background: linear-gradient(135deg, var(--color-tvt05-acc), var(--color-tvt05-acc2));
  }

  .tvt-05 #tvt-05-p1 {
    visibility: visible;
    opacity: 1;
    translate: none;
  }
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-05:not([data-theme="light"]) {
    --color-tvt05-bg: #10081d;
    --color-tvt05-bg: oklch(0.16 0.045 300);
    --color-tvt05-glow: #650e6173;
    --color-tvt05-glow: oklch(0.36 0.15 330 / 0.45);
    --color-tvt05-glow2: #2c267573;
    --color-tvt05-glow2: oklch(0.33 0.13 280 / 0.45);
    --color-tvt05-card: #1a1029;
    --color-tvt05-card: oklch(0.2 0.05 300);
    --color-tvt05-rail: #140b21;
    --color-tvt05-rail: oklch(0.175 0.045 300);
    --color-tvt05-ink: #f5effa;
    --color-tvt05-ink: oklch(0.96 0.015 310);
    --color-tvt05-mut: #b8aac9;
    --color-tvt05-mut: oklch(0.76 0.045 305);
    --color-tvt05-line: #35294a;
    --color-tvt05-line: oklch(0.31 0.06 300);
    --color-tvt05-acc-ink: #dcaeff;
    --color-tvt05-acc-ink: oklch(0.82 0.13 310);
    --color-tvt05-hl: #c3afff;
    --color-tvt05-hl: oklch(0.8 0.14 295);
    --color-tvt05-hl2: #ff98ca;
    --color-tvt05-hl2: oklch(0.8 0.15 350);
    --color-tvt05-ring: #d59aff;
    --color-tvt05-ring: oklch(0.78 0.16 310);
    --color-tvt05-ok: #61da92;
    --color-tvt05-ok: oklch(0.8 0.15 155);
    --color-tvt05-warn: #fcb953;
    --color-tvt05-warn: oklch(0.83 0.14 75);
    --color-tvt05-hot: #ff83ad;
    --color-tvt05-hot: oklch(0.76 0.17 0);
    --color-tvt05-code: #0a0415;
    --color-tvt05-code: oklch(0.13 0.04 300);
  }
}

.tvt-05[data-theme="dark"] {
  --color-tvt05-bg: #10081d;
  --color-tvt05-bg: oklch(0.16 0.045 300);
  --color-tvt05-glow: #650e6173;
  --color-tvt05-glow: oklch(0.36 0.15 330 / 0.45);
  --color-tvt05-glow2: #2c267573;
  --color-tvt05-glow2: oklch(0.33 0.13 280 / 0.45);
  --color-tvt05-card: #1a1029;
  --color-tvt05-card: oklch(0.2 0.05 300);
  --color-tvt05-rail: #140b21;
  --color-tvt05-rail: oklch(0.175 0.045 300);
  --color-tvt05-ink: #f5effa;
  --color-tvt05-ink: oklch(0.96 0.015 310);
  --color-tvt05-mut: #b8aac9;
  --color-tvt05-mut: oklch(0.76 0.045 305);
  --color-tvt05-line: #35294a;
  --color-tvt05-line: oklch(0.31 0.06 300);
  --color-tvt05-acc-ink: #dcaeff;
  --color-tvt05-acc-ink: oklch(0.82 0.13 310);
  --color-tvt05-hl: #c3afff;
  --color-tvt05-hl: oklch(0.8 0.14 295);
  --color-tvt05-hl2: #ff98ca;
  --color-tvt05-hl2: oklch(0.8 0.15 350);
  --color-tvt05-ring: #d59aff;
  --color-tvt05-ring: oklch(0.78 0.16 310);
  --color-tvt05-ok: #61da92;
  --color-tvt05-ok: oklch(0.8 0.15 155);
  --color-tvt05-warn: #fcb953;
  --color-tvt05-warn: oklch(0.83 0.14 75);
  --color-tvt05-hot: #ff83ad;
  --color-tvt05-hot: oklch(0.76 0.17 0);
  --color-tvt05-code: #0a0415;
  --color-tvt05-code: oklch(0.13 0.04 300);
}
```
