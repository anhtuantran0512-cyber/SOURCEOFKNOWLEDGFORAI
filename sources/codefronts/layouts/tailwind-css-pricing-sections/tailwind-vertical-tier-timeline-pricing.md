---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-vertical-tier-timeline-pricing/"
title: "Tailwind Vertical Tier Timeline Pricing"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Tiers as three stops on one road: a glowing lime spine, numbered station markers and a highlighted &ldquo;you are here&rdquo; pane."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Tier Timeline Pricing
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-vertical-tier-timeline-pricing/

Tiers as three stops on one road: a glowing lime spine, numbered station markers and a highlighted &ldquo;you are here&rdquo; pane. Reading it as an <ol> is the whole point &mdash; and the port keeps the spine as a before: pseudo-element on the list, because a connector belongs to the list, not to any tier.
## HTML
```html
<section class="tps-08 w-full min-h-svh bg-tps08-bg font-tps08-sans text-tps08-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(28px,5vw,44px)]">
    <h2 class="m-0 mb-2 text-[clamp(22px,3.4vw,32px)] font-bold tracking-[-0.02em] text-tps08-bright text-pretty">Grow into the next plan, not out of one.</h2>
    <p class="m-0 text-sm text-tps08-mut">Three stops on the same road. Switch up or down with one click.</p>
  </header>
  <ol class="relative list-none p-0 m-0 mx-auto max-w-[580px] before:content-[''] before:absolute before:left-7 before:top-4.5 before:bottom-4.5 before:w-0.5 before:rounded-sm before:bg-linear-to-b before:from-tps08-acc before:to-tps08-fade">
    <li class="relative min-h-14 pl-17.5 pb-6 last:pb-0">
      <span class="absolute left-1.5 top-0 z-1 grid place-items-center size-11.5 rounded-full bg-tps08-bg border-2 border-tps08-acc font-tps08-mono text-[13px] font-bold text-tps08-acc" aria-hidden="true">01</span>
      <article class="p-4.5 pb-4 rounded-xl bg-tps08-pane border border-tps08-edge">
        <header class="flex items-baseline justify-between pb-2.5 mb-2 border-b border-dashed border-tps08-edge">
          <h3 class="m-0 text-sm font-bold tracking-[0.06em] uppercase text-tps08-acc">Free</h3>
          <span class="text-[22px] font-extrabold tracking-[-0.02em] text-tps08-bright">$0</span>
        </header>
        <p class="my-2.5 text-[13px]/[1.55] text-tps08-body">Open-source projects, side experiments, anything you want to ship without a credit card.</p>
        <ul class="list-none p-0 m-0 mb-3.5 text-[13px]/[1.85] text-tps08-body">
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>1 project</li>
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>500 MB storage</li>
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>Public repos only</li>
        </ul>
        <a href="#free" class="inline-block px-3.5 py-2.25 rounded-[7px] text-[13px] font-semibold no-underline text-tps08-acc border border-tps08-ctaedge transition-[background-color,color] duration-200 hover:bg-tps08-chip hover:text-tps08-ink focus-visible:outline-2 focus-visible:outline-tps08-acc2 focus-visible:outline-offset-3 motion-reduce:transition-none">Start free &rarr;</a>
      </article>
    </li>
    <li class="relative min-h-14 pl-17.5 pb-6 last:pb-0">
      <span class="absolute left-1.5 top-0 z-1 grid place-items-center size-11.5 rounded-full bg-tps08-acc text-tps08-bg border-2 border-tps08-acc font-tps08-mono text-[13px] font-bold shadow-[0_0_0_6px_--theme(--color-tps08-halo)]" aria-hidden="true">02</span>
      <article class="p-4.5 pb-4 rounded-xl border border-tps08-acc bg-linear-to-b from-tps08-pane2 to-tps08-pane shadow-[0_8px_24px_--theme(--color-tps08-glow)]">
        <header class="flex items-baseline justify-between pb-2.5 mb-2 border-b border-dashed border-tps08-edge">
          <h3 class="m-0 text-sm font-bold tracking-[0.06em] uppercase text-tps08-acc">Pro</h3>
          <span class="text-[22px] font-extrabold tracking-[-0.02em] text-tps08-bright">$24<em class="ml-0.5 text-xs font-medium not-italic text-tps08-mut">/mo</em></span>
        </header>
        <p class="my-2.5 text-[13px]/[1.55] text-tps08-body">Where most teams settle. Private projects, real support, and the integrations you actually use.</p>
        <ul class="list-none p-0 m-0 mb-3.5 text-[13px]/[1.85] text-tps08-body">
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>Unlimited projects</li>
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>50 GB storage</li>
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>Email + chat support</li>
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>Slack, GitHub, Linear sync</li>
        </ul>
        <a href="#pro" class="inline-block px-3.5 py-2.25 rounded-[7px] text-[13px] font-semibold no-underline bg-tps08-acc text-tps08-bg border border-tps08-acc transition-[background-color,border-color] duration-200 hover:bg-tps08-acc2 hover:border-tps08-acc2 focus-visible:outline-2 focus-visible:outline-tps08-acc2 focus-visible:outline-offset-3 motion-reduce:transition-none">Choose Pro &rarr;</a>
      </article>
    </li>
    <li class="relative min-h-14 pl-17.5 pb-6 last:pb-0">
      <span class="absolute left-1.5 top-0 z-1 grid place-items-center size-11.5 rounded-full bg-tps08-bg border-2 border-tps08-acc font-tps08-mono text-[13px] font-bold text-tps08-acc" aria-hidden="true">03</span>
      <article class="p-4.5 pb-4 rounded-xl bg-tps08-pane border border-tps08-edge">
        <header class="flex items-baseline justify-between pb-2.5 mb-2 border-b border-dashed border-tps08-edge">
          <h3 class="m-0 text-sm font-bold tracking-[0.06em] uppercase text-tps08-acc">Enterprise</h3>
          <span class="text-[22px] font-extrabold tracking-[-0.02em] text-tps08-bright">Custom</span>
        </header>
        <p class="my-2.5 text-[13px]/[1.55] text-tps08-body">For teams with procurement processes, security reviews, and quarterly business reviews.</p>
        <ul class="list-none p-0 m-0 mb-3.5 text-[13px]/[1.85] text-tps08-body">
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>SSO + SAML + audit logs</li>
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>SLA, dedicated CSM</li>
          <li><span class="inline-block w-5 font-bold text-tps08-acc" aria-hidden="true">&rarr;</span>Custom DPA &amp; invoicing</li>
        </ul>
        <a href="#ent" class="inline-block px-3.5 py-2.25 rounded-[7px] text-[13px] font-semibold no-underline text-tps08-acc border border-tps08-ctaedge transition-[background-color,color] duration-200 hover:bg-tps08-chip hover:text-tps08-ink focus-visible:outline-2 focus-visible:outline-tps08-acc2 focus-visible:outline-offset-3 motion-reduce:transition-none">Talk to sales &rarr;</a>
      </article>
    </li>
  </ol>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps08-bg: #0a1408;
  --color-tps08-bg: oklch(0.16 0.03 135);
  --color-tps08-pane: #14210e;
  --color-tps08-pane: oklch(0.22 0.04 135);
  --color-tps08-pane2: #1a3010;
  --color-tps08-pane2: oklch(0.28 0.06 135);
  --color-tps08-edge: #2f4a1f;
  --color-tps08-edge: oklch(0.36 0.06 130);
  --color-tps08-ctaedge: #4d7a2f;
  --color-tps08-ctaedge: oklch(0.5 0.1 130);
  --color-tps08-chip: #1f3a12;
  --color-tps08-chip: oklch(0.3 0.07 132);
  --color-tps08-ink: #ecfccb;
  --color-tps08-ink: oklch(0.96 0.05 120);
  --color-tps08-bright: #f7feec;
  --color-tps08-bright: oklch(0.99 0.02 120);
  --color-tps08-body: #c8d8b0;
  --color-tps08-body: oklch(0.86 0.05 120);
  --color-tps08-mut: #93a87f;
  --color-tps08-mut: oklch(0.7 0.05 125);
  --color-tps08-acc: #84cc16;
  --color-tps08-acc: oklch(0.77 0.2 128);
  --color-tps08-acc2: #a3e635;
  --color-tps08-acc2: oklch(0.85 0.19 126);
  --color-tps08-fade: #84cc1633;
  --color-tps08-fade: oklch(0.77 0.2 128 / 0.2);
  --color-tps08-halo: #84cc162e;
  --color-tps08-halo: oklch(0.77 0.2 128 / 0.18);
  --color-tps08-glow: #84cc161f;
  --color-tps08-glow: oklch(0.77 0.2 128 / 0.12);
  --font-tps08-sans: 'Inter', system-ui, sans-serif;
  --font-tps08-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is correctly sized in the moment before the
   browser build has compiled its utilities. */

.tps-08 {
  width: 100%;
  min-height: 100svh;
}
```
