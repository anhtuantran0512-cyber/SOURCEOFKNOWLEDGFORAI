---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-usage-meters-progress-bars/"
title: "Tailwind Pricing Cards with Usage Meters & Progress Bars"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Show, don't tell, which plan fits: each card measures your current usage against its limits, bars sweep in as the section scrolls into view, and they turn…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Cards with Usage Meters & Progress Bars
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-usage-meters-progress-bars/

Show, don't tell, which plan fits: each card measures your current usage against its limits, bars sweep in as the section scrolls into view, and they turn amber near a limit and red past it. The sweep is a v4 animation token plus two arbitrary properties — [animation-timeline:view()] and [animation-range:entry_0%_entry_60%] — and each bar's fill is a single [--tpt13-fill:.42].
## HTML
```html
<section class="tpt-13 w-full min-h-svh grid place-items-center bg-tpt13-bg px-5 py-16 font-tpt13-sans text-tpt13-ink antialiased" aria-label="Pricing with usage meters">
  <div class="grid w-full max-w-5xl justify-items-center gap-10">
    <header class="grid justify-items-center gap-3 text-center">
      <h2 class="text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em] text-balance">See exactly what fits</h2>
      <p class="rounded-full bg-white px-4 py-2 text-sm text-tpt13-body ring-1 ring-tpt13-line">Your usage: <strong class="font-semibold text-tpt13-ink">42 projects · 180 GB · 8 seats</strong></p>
    </header>
    <div class="grid w-full gap-5 md:grid-cols-3">
      <article class="flex flex-col gap-4 rounded-[20px] border border-tpt13-line bg-white p-7">
        <div class="flex items-baseline justify-between"><h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt13-mut uppercase">Free</h3><span class="rounded-full bg-tpt13-over/10 px-2.5 py-0.5 text-[11px] font-semibold text-tpt13-over-ink">Over limits</span></div>
        <p class="text-[42px] leading-none font-bold tracking-[-0.035em]">$0</p>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Projects</span><b class="font-semibold text-tpt13-over-ink tabular-nums">42 of 3</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Projects" aria-valuemin="0" aria-valuemax="3" aria-valuenow="3" aria-valuetext="42 of 3, over limit"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-over [--tpt13-fill:1] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Storage</span><b class="font-semibold text-tpt13-over-ink tabular-nums">180 of 2 GB</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Storage" aria-valuemin="0" aria-valuemax="2" aria-valuenow="2" aria-valuetext="180 of 2 GB, over limit"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-over [--tpt13-fill:1] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Seats</span><b class="font-semibold text-tpt13-over-ink tabular-nums">8 of 1</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Seats" aria-valuemin="0" aria-valuemax="1" aria-valuenow="1" aria-valuetext="8 of 1, over limit"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-over [--tpt13-fill:1] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <a href="#" class="mt-auto grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt13-line text-sm font-semibold text-tpt13-ink no-underline transition-colors hover:border-tpt13-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt13-acc">Start free</a>
      </article>
      <article class="relative flex flex-col gap-4 rounded-[20px] bg-white p-7 shadow-[0_18px_40px_-26px_var(--color-tpt13-acc)] ring-2 ring-tpt13-acc">
        <div class="flex items-baseline justify-between"><h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt13-acc-ink uppercase">Pro</h3><span class="rounded-full bg-tpt13-acc px-2.5 py-0.5 text-[11px] font-semibold text-white">Fits your usage</span></div>
        <p class="text-[42px] leading-none font-bold tracking-[-0.035em]">$24<small class="text-[15px] font-medium tracking-normal text-tpt13-mut">/mo</small></p>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Projects</span><b class="font-semibold text-tpt13-ink tabular-nums">42 of 100</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Projects" aria-valuemin="0" aria-valuemax="100" aria-valuenow="42" aria-valuetext="42 of 100"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-ok [--tpt13-fill:.42] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Storage</span><b class="font-semibold text-tpt13-ink tabular-nums">180 of 250 GB</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Storage" aria-valuemin="0" aria-valuemax="250" aria-valuenow="180" aria-valuetext="180 of 250 GB"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-ok [--tpt13-fill:.72] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Seats</span><b class="font-semibold text-tpt13-warn-ink tabular-nums">8 of 10</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Seats" aria-valuemin="0" aria-valuemax="10" aria-valuenow="8" aria-valuetext="8 of 10, near limit"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-warn [--tpt13-fill:.8] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <a href="#" class="mt-auto grid min-h-11 place-items-center rounded-xl bg-tpt13-acc text-sm font-semibold text-white no-underline transition-colors hover:bg-tpt13-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt13-acc">Go Pro</a>
      </article>
      <article class="flex flex-col gap-4 rounded-[20px] border border-tpt13-line bg-white p-7">
        <div class="flex items-baseline justify-between"><h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt13-mut uppercase">Max</h3><span class="rounded-full bg-tpt13-track px-2.5 py-0.5 text-[11px] font-semibold text-tpt13-mut">Room to grow</span></div>
        <p class="text-[42px] leading-none font-bold tracking-[-0.035em]">$59<small class="text-[15px] font-medium tracking-normal text-tpt13-mut">/mo</small></p>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Projects</span><b class="font-semibold text-tpt13-ink tabular-nums">42 of unlimited</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Projects" aria-valuemin="0" aria-valuemax="1000" aria-valuenow="42" aria-valuetext="42, unlimited plan"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-ok [--tpt13-fill:.04] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Storage</span><b class="font-semibold text-tpt13-ink tabular-nums">180 GB of 2 TB</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Storage" aria-valuemin="0" aria-valuemax="2000" aria-valuenow="180" aria-valuetext="180 GB of 2 TB"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-ok [--tpt13-fill:.09] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <div class="grid gap-1.5"><div class="flex justify-between text-[13px] font-medium text-tpt13-mut"><span>Seats</span><b class="font-semibold text-tpt13-ink tabular-nums">8 of unlimited</b></div><span class="block h-2 overflow-hidden rounded-full bg-tpt13-track" role="meter" aria-label="Seats" aria-valuemin="0" aria-valuemax="200" aria-valuenow="8" aria-valuetext="8, unlimited plan"><span class="block h-full origin-left animate-tpt13-sweep rounded-full bg-tpt13-ok [--tpt13-fill:.04] [animation-range:entry_0%_entry_60%] [animation-timeline:view()] [scale:var(--tpt13-fill)_1] motion-reduce:animate-none"></span></span></div>
        <a href="#" class="mt-auto grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt13-line text-sm font-semibold text-tpt13-ink no-underline transition-colors hover:border-tpt13-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt13-acc">Go Max</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt13-line bg-white px-3.5 py-2 font-tpt13-mono text-[11.5px] text-tpt13-mut">[animation-timeline:view()] · [scale:var(--tpt13-fill)_1] · role="meter"</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt13-bg: #f3f6fa;
  --color-tpt13-bg: oklch(0.97 0.007 245);
  --color-tpt13-track: #e6ebf2;
  --color-tpt13-track: oklch(0.94 0.01 245);
  --color-tpt13-ink: #141c24;
  --color-tpt13-ink: oklch(0.22 0.02 245);
  --color-tpt13-body: #44515f;
  --color-tpt13-body: oklch(0.43 0.03 245);
  --color-tpt13-mut: #586779;
  --color-tpt13-mut: oklch(0.5 0.03 245);
  --color-tpt13-line: #dce4ec;
  --color-tpt13-line: oklch(0.91 0.012 245);
  --color-tpt13-acc: #1780cc;
  --color-tpt13-acc: oklch(0.58 0.15 245);
  --color-tpt13-acc-ink: #0e619e;
  --color-tpt13-acc-ink: oklch(0.49 0.13 248);
  --color-tpt13-ok: #2b95d6;
  --color-tpt13-ok: oklch(0.64 0.14 240);
  --color-tpt13-warn: #eba417;
  --color-tpt13-warn: oklch(0.77 0.16 75);
  --color-tpt13-warn-ink: #955f00;
  --color-tpt13-warn-ink: oklch(0.52 0.12 70);
  --color-tpt13-over: #de3b3b;
  --color-tpt13-over: oklch(0.6 0.2 25);
  --color-tpt13-over-ink: #b3262a;
  --color-tpt13-over-ink: oklch(0.52 0.19 25);
  --font-tpt13-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tpt13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tpt13-sweep: tpt13-sweep 1s cubic-bezier(0.3, 0, 0.2, 1) both;

  @keyframes tpt13-sweep {
    from {
      scale: 0 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-13 {
  width: 100%;
  min-height: 100svh;
}
```
