---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-saas-pricing-tier-card-row/"
title: "Tailwind SaaS Pricing Tier Card Row with Popular Plan"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "Three plans in a symmetric grid, with the middle tier lifted, ringed and glowing."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS Pricing Tier Card Row with Popular Plan
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-saas-pricing-tier-card-row/

Three plans in a symmetric grid, with the middle tier lifted, ringed and glowing. The port's win is that the popular tier stops being a --pop modifier class and becomes a visible diff: the same class list as its neighbours plus six utilities, so you can read what &ldquo;most popular&rdquo; costs in styling without opening a stylesheet.
## HTML
```html
<section class="twc-02 w-full min-h-svh flex flex-col items-center justify-center px-5 py-9 bg-twc02-bg [background-image:radial-gradient(ellipse_at_20%_10%,oklch(0.55_0.2_275/0.06),transparent_45%),radial-gradient(ellipse_at_80%_90%,oklch(0.68_0.2_350/0.05),transparent_45%)] font-twc02-sans" aria-label="Pricing">

  <header class="w-full max-w-[780px] mb-5 text-center">
    <div class="inline-flex items-center gap-1.5 mb-3 px-2.5 py-1 rounded-full font-twc02-mono text-[10px] font-extrabold tracking-[0.14em] text-twc02-acc bg-twc02-acc/8 border border-twc02-acc/16">
      <span aria-hidden="true" class="size-[5px] rounded-full bg-twc02-pink shadow-[0_0_8px_oklch(0.68_0.2_350/0.5)] animate-twc02-pulse motion-reduce:animate-none"></span>
      PRICING &middot; 30-DAY MONEY-BACK GUARANTEE
    </div>
    <h3 class="m-0 mb-1 text-[22px] font-extrabold tracking-[-0.025em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Simple pricing, ship faster.</h3>
    <p class="m-0 text-[13px] text-twc02-muted">Start free, upgrade as you grow. Cancel anytime.</p>
    <div class="flex justify-center mt-3.5">
      <div role="tablist" aria-label="Billing period" class="inline-flex gap-0.5 p-[3px] rounded-full bg-twc02-track border border-black/5">
        <button type="button" role="tab" aria-selected="false" class="inline-flex items-center gap-1.5 min-h-11 px-4 rounded-full border-0 cursor-pointer text-xs font-bold bg-transparent text-twc02-muted transition-[color,background,box-shadow] duration-200 hover:text-twc02-ink focus-visible:outline-2 focus-visible:outline-twc02-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Monthly</button>
        <button type="button" role="tab" aria-selected="true" class="inline-flex items-center gap-1.5 min-h-11 px-4 rounded-full border-0 cursor-pointer text-xs font-bold bg-white text-twc02-ink shadow-[0_2px_6px_oklch(0_0_0/0.08),0_0_0_1px_oklch(0_0_0/0.04)] transition-[color,background,box-shadow] duration-200 focus-visible:outline-2 focus-visible:outline-twc02-acc focus-visible:outline-offset-2 motion-reduce:transition-none">
          Yearly
          <span class="inline-flex items-center px-1.5 py-px rounded-full [background:linear-gradient(180deg,#34d399,#059669)] text-white font-twc02-mono text-[9px] font-extrabold tracking-[0.06em] shadow-[0_2px_4px_oklch(0.78_0.14_165/0.35)]">&minus;20%</span>
        </button>
      </div>
    </div>
  </header>

  <div class="w-full max-w-[780px] grid grid-cols-3 max-[780px]:grid-cols-1 max-[780px]:max-w-[340px] gap-3.5 items-stretch">

    <article class="relative flex flex-col p-5 rounded-twc02-card bg-white border border-black/5 shadow-[0_12px_30px_-18px_oklch(0.4_0.06_320/0.16),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-black/10 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div aria-hidden="true" class="inline-flex items-center justify-center size-8.5 mb-3 rounded-[10px] [background:linear-gradient(180deg,#f5f4f0,#ece8db)] text-twc02-muted border border-black/5">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h18M3 6h18M3 14h18M3 18h18"/></svg>
      </div>
      <div class="flex items-center justify-between gap-1.5 mb-1">
        <p class="m-0 text-sm font-extrabold tracking-[-0.01em] text-twc02-ink">Starter</p>
        <span class="px-[7px] py-0.5 rounded-full font-twc02-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-twc02-greenink bg-twc02-green/10 border border-twc02-green/25">Free forever</span>
      </div>
      <p class="m-0 mb-3.5 min-h-8 text-[11.5px]/[1.4] text-twc02-muted">For solo builders shipping their first thing.</p>
      <div class="mb-3.5">
        <div class="inline-flex items-start [font-variant-numeric:tabular-nums]">
          <span class="mt-1.5 text-base font-bold text-twc02-ink2">$</span>
          <span class="text-[42px]/none font-extrabold tracking-[-0.04em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">0</span>
          <span class="mt-5 ml-1 text-[12.5px] text-twc02-dim">/mo</span>
        </div>
        <p class="flex items-center gap-1 m-0 mt-1 text-[10.5px] text-twc02-dim">No card required</p>
      </div>
      <a href="#starter" class="inline-flex items-center justify-center gap-1.5 min-h-11 px-3.5 rounded-xl border border-transparent no-underline text-[12.5px] font-bold text-twc02-ink bg-black/4 transition-[background,transform] duration-200 hover:bg-black/8 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc02-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        Get started free
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
      <p aria-hidden="true" class="relative mt-4 mb-3 text-center text-[9.5px] font-bold tracking-[0.1em] uppercase text-twc02-dim before:absolute before:inset-x-0 before:top-1/2 before:h-px before:bg-black/6 before:content-['']"><span class="relative px-2 bg-white">What's included</span></p>
      <ul class="flex-1 flex flex-col gap-2 list-none m-0 p-0">
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Up to 3 projects</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>5 GB storage</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Community support</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Basic analytics</li>
      </ul>
    </article>

    <article class="relative flex flex-col p-5 rounded-twc02-card bg-white [background-image:linear-gradient(180deg,oklch(0.55_0.2_275/0.05)_0%,transparent_30%)] border-[1.5px] border-twc02-acc/30 shadow-[0_24px_44px_-18px_oklch(0.55_0.2_275/0.26),0_0_0_4px_oklch(0.55_0.2_275/0.07),inset_0_0_0_1px_oklch(1_0_0/0.5)] -translate-y-1.5 max-[780px]:translate-y-0 transition-[transform,box-shadow] duration-300 hover:-translate-y-[9px] max-[780px]:hover:-translate-y-[3px] hover:shadow-[0_36px_60px_-18px_oklch(0.55_0.2_275/0.36),0_0_0_4px_oklch(0.55_0.2_275/0.1),inset_0_0_0_1px_oklch(1_0_0/0.5)] motion-reduce:transition-none motion-reduce:hover:-translate-y-1.5">
      <div aria-hidden="true" class="absolute -inset-x-10 -top-15 h-35 -z-10 pointer-events-none blur-[20px] [background:radial-gradient(ellipse_at_center_top,oklch(0.55_0.2_275/0.16)_0%,transparent_60%)]"></div>
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 inline-flex items-center gap-1 px-3 py-1 rounded-full whitespace-nowrap [background:linear-gradient(180deg,#818cf8_0%,#6366f1_100%)] text-white font-twc02-mono text-[9.5px] font-extrabold tracking-[0.14em] shadow-[0_6px_16px_oklch(0.55_0.2_275/0.38),0_0_0_3px_oklch(1_0_0/0.85)]">
        <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
        MOST POPULAR
      </span>
      <div aria-hidden="true" class="inline-flex items-center justify-center size-8.5 mb-3 rounded-[10px] [background:linear-gradient(180deg,#818cf8,#6366f1)] text-white border border-transparent shadow-[0_6px_16px_oklch(0.55_0.2_275/0.3)]">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
      </div>
      <div class="flex items-center justify-between gap-1.5 mb-1">
        <p class="m-0 text-sm font-extrabold tracking-[-0.01em] text-twc02-ink">Business</p>
        <span class="inline-flex items-center px-[7px] py-0.5 rounded-full [background:linear-gradient(180deg,#34d399,#059669)] text-white font-twc02-mono text-[9px] font-extrabold tracking-[0.1em] shadow-[0_2px_4px_oklch(0.78_0.14_165/0.35)]">Save $84</span>
      </div>
      <p class="m-0 mb-3.5 min-h-8 text-[11.5px]/[1.4] text-twc02-muted">Everything growing teams need to ship together.</p>
      <div class="mb-3.5">
        <div class="inline-flex items-start [font-variant-numeric:tabular-nums]">
          <span class="mt-1.5 text-base font-bold text-twc02-ink2">$</span>
          <span class="text-[42px]/none font-extrabold tracking-[-0.04em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">23</span>
          <span class="mt-5 ml-1 text-[12.5px] text-twc02-dim">/mo</span>
        </div>
        <p class="flex items-center gap-1 m-0 mt-1 text-[10.5px] text-twc02-dim"><span class="line-through text-twc02-strike">$29/mo</span><span>&middot; billed $276/yr</span></p>
      </div>
      <a href="#business" class="inline-flex items-center justify-center gap-1.5 min-h-11 px-3.5 rounded-xl border border-transparent no-underline text-[12.5px] font-bold text-white [background:linear-gradient(180deg,#1e1e2c_0%,#06070c_100%)] shadow-[0_6px_16px_oklch(0_0_0/0.25),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[background,transform,box-shadow] duration-200 hover:[background:linear-gradient(180deg,#2a2a3c_0%,#0d0d16_100%)] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc02-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        Start 14-day trial
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
      <div class="flex items-center gap-2 mt-3 px-2.5 py-2 rounded-[10px] bg-twc02-acc/5 border border-twc02-acc/12">
        <div aria-hidden="true" class="flex">
          <span class="flex items-center justify-center size-[22px] rounded-full border-[1.5px] border-white text-white text-[8.5px] font-extrabold [background:linear-gradient(135deg,#f472b6,#ec4899)]">AR</span>
          <span class="flex items-center justify-center size-[22px] -ml-1.5 rounded-full border-[1.5px] border-white text-white text-[8.5px] font-extrabold [background:linear-gradient(135deg,#60a5fa,#3b82f6)]">JL</span>
          <span class="flex items-center justify-center size-[22px] -ml-1.5 rounded-full border-[1.5px] border-white text-white text-[8.5px] font-extrabold [background:linear-gradient(135deg,#34d399,#10b981)]">MK</span>
          <span class="flex items-center justify-center size-[22px] -ml-1.5 rounded-full border-[1.5px] border-white text-white text-[8px] font-extrabold bg-twc02-accdeep">+9k</span>
        </div>
        <span class="text-[11px] font-bold text-twc02-accdeep [font-variant-numeric:tabular-nums]">12,483 teams shipping</span>
      </div>
      <p aria-hidden="true" class="relative mt-4 mb-3 text-center text-[9.5px] font-bold tracking-[0.1em] uppercase text-twc02-dim before:absolute before:inset-x-0 before:top-1/2 before:h-px before:bg-black/6 before:content-['']"><span class="relative px-2 bg-white">Everything in Starter, plus</span></p>
      <ul class="flex-1 flex flex-col gap-2 list-none m-0 p-0">
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Unlimited projects</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>100 GB storage <span class="inline-flex items-center px-[5px] py-px rounded font-twc02-mono text-[8px] font-extrabold tracking-[0.1em] text-twc02-pinkink bg-twc02-pink/10 border border-twc02-pink/20">NEW</span></li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Priority email support</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Team roles &amp; SSO</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>API access &middot; 10k req/day</li>
      </ul>
    </article>

    <article class="relative flex flex-col p-5 rounded-twc02-card bg-white border border-black/5 shadow-[0_12px_30px_-18px_oklch(0.4_0.06_320/0.16),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-black/10 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div aria-hidden="true" class="inline-flex items-center justify-center size-8.5 mb-3 rounded-[10px] [background:linear-gradient(180deg,#fef3c7,#fde68a)] text-twc02-amberink border border-twc02-amberink/15">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
      </div>
      <div class="flex items-center justify-between gap-1.5 mb-1">
        <p class="m-0 text-sm font-extrabold tracking-[-0.01em] text-twc02-ink">Team</p>
        <span class="px-[7px] py-0.5 rounded-full font-twc02-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-twc02-orangeink bg-twc02-orange/8 border border-twc02-orange/20">Custom</span>
      </div>
      <p class="m-0 mb-3.5 min-h-8 text-[11.5px]/[1.4] text-twc02-muted">For scaling teams that need governance.</p>
      <div class="mb-3.5">
        <div class="inline-flex items-start [font-variant-numeric:tabular-nums]">
          <span class="mt-1.5 text-base font-bold text-twc02-ink2">$</span>
          <span class="text-[42px]/none font-extrabold tracking-[-0.04em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">63</span>
          <span class="mt-5 ml-1 text-[12.5px] text-twc02-dim">/mo</span>
        </div>
        <p class="flex items-center gap-1 m-0 mt-1 text-[10.5px] text-twc02-dim"><span class="line-through text-twc02-strike">$79/mo</span><span>&middot; from 5 seats</span></p>
      </div>
      <a href="#team" class="inline-flex items-center justify-center gap-1.5 min-h-11 px-3.5 rounded-xl border border-transparent no-underline text-[12.5px] font-bold text-twc02-ink bg-black/4 transition-[background,transform] duration-200 hover:bg-black/8 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc02-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        Contact sales
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
      <p aria-hidden="true" class="relative mt-4 mb-3 text-center text-[9.5px] font-bold tracking-[0.1em] uppercase text-twc02-dim before:absolute before:inset-x-0 before:top-1/2 before:h-px before:bg-black/6 before:content-['']"><span class="relative px-2 bg-white">Everything in Business, plus</span></p>
      <ul class="flex-1 flex flex-col gap-2 list-none m-0 p-0">
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>500 GB storage</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Dedicated success mgr</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Audit logs &amp; SOC 2</li>
        <li class="flex items-center gap-[7px] text-xs text-twc02-ink2"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none p-0.5 rounded bg-twc02-green/15 text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>Custom SLA</li>
      </ul>
    </article>

  </div>

  <footer class="w-full max-w-[780px] mt-5 flex flex-wrap items-center justify-center gap-2">
    <span class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-white/70 border border-black/6 text-[10.5px] font-bold text-twc02-muted">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc02-greenink"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      SOC 2
    </span>
    <span class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-white/70 border border-black/6 text-[10.5px] font-bold text-twc02-muted">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc02-greenink"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      GDPR
    </span>
    <span class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-white/70 border border-black/6 text-[10.5px] font-bold text-twc02-muted">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc02-greenink"><polyline points="20 6 9 17 4 12"/></svg>
      14-day trial &middot; no card
    </span>
    <a href="#compare" class="inline-flex items-center gap-1 min-h-11 px-2.5 rounded-full no-underline text-[10.5px] font-bold text-twc02-accdeep transition-[color,background] duration-200 hover:text-twc02-accdark hover:bg-twc02-acc/6 focus-visible:outline-2 focus-visible:outline-twc02-acc focus-visible:outline-offset-2">
      Compare all plans
      <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
    </a>
  </footer>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc02-bg: #faf7f2;
  --color-twc02-bg: oklch(0.975 0.008 85);
  --color-twc02-track: #ede8dc;
  --color-twc02-track: oklch(0.93 0.015 85);
  --color-twc02-ink: #1a1a1a;
  --color-twc02-ink: oklch(0.21 0.005 270);
  --color-twc02-ink2: #4b4b57;
  --color-twc02-ink2: oklch(0.4 0.015 280);
  --color-twc02-muted: #6b6b7c;
  --color-twc02-muted: oklch(0.51 0.02 285);
  --color-twc02-dim: #9ca3af;
  --color-twc02-dim: oklch(0.71 0.02 265);
  --color-twc02-strike: #d4d4d8;
  --color-twc02-strike: oklch(0.87 0.005 285);
  --color-twc02-acc: #6366f1;
  --color-twc02-acc: oklch(0.55 0.2 275);
  --color-twc02-accdeep: #4338ca;
  --color-twc02-accdeep: oklch(0.42 0.21 275);
  --color-twc02-accdark: #312e81;
  --color-twc02-accdark: oklch(0.32 0.15 275);
  --color-twc02-pink: #ec4899;
  --color-twc02-pink: oklch(0.68 0.2 350);
  --color-twc02-pinkink: #be185d;
  --color-twc02-pinkink: oklch(0.5 0.19 355);
  --color-twc02-green: #34d399;
  --color-twc02-green: oklch(0.78 0.14 165);
  --color-twc02-greenink: #059669;
  --color-twc02-greenink: oklch(0.56 0.13 163);
  --color-twc02-amberink: #92400e;
  --color-twc02-amberink: oklch(0.44 0.12 55);
  --color-twc02-orange: #ea580c;
  --color-twc02-orange: oklch(0.62 0.19 45);
  --color-twc02-orangeink: #9a3412;
  --color-twc02-orangeink: oklch(0.44 0.15 42);
  --font-twc02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc02-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --radius-twc02-card: 20px;
  --animate-twc02-pulse: twc02-pulse 2.2s ease-in-out infinite;
}

@keyframes twc02-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

.twc-02 {
  width: 100%;
  min-height: 100svh;
}
```
