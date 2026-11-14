---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-synthwave-neon-pricing-section/"
title: "Tailwind Synthwave Neon Pricing Section"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Magenta and cyan neon over a perspective grid horizon, a striped retro sun behind the cards and a chrome-reflection heading."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Synthwave Neon Pricing Section
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-synthwave-neon-pricing-section/

Magenta and cyan neon over a perspective grid horizon, a striped retro sun behind the cards and a chrome-reflection heading. The port's headline is text-shadow-* &mdash; a real utility since v4.1 &mdash; which turns eight hand-written glow declarations into text-shadow-[0_0_8px_…] on the elements that glow.
## HTML
```html
<section class="tps-15 relative w-full min-h-svh overflow-hidden [contain:layout_paint] bg-linear-180 from-tps15-bg from-0% via-tps15-mid via-60% to-tps15-top font-tps15-sans text-tps15-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <div class="absolute bottom-0 left-1/2 w-[220%] h-1/2 z-0 bg-[repeating-linear-gradient(0deg,transparent_0,transparent_24px,--alpha(--color-tps15-pink/40)_24px,--alpha(--color-tps15-pink/40)_25px),repeating-linear-gradient(90deg,transparent_0,transparent_24px,--alpha(--color-tps15-cyan/40)_24px,--alpha(--color-tps15-cyan/40)_25px)] [transform:translateX(-50%)_perspective(700px)_rotateX(60deg)] origin-top mask-b-from-65%" aria-hidden="true"></div>
  <div class="absolute left-1/2 top-[22%] md:top-[30%] -translate-x-1/2 size-[240px] md:size-[360px] z-0 rounded-full opacity-55 blur-[0.4px] bg-[repeating-linear-gradient(180deg,transparent_0,transparent_16px,--theme(--color-tps15-bg)_16px,--theme(--color-tps15-bg)_19px),linear-gradient(180deg,--theme(--color-tps15-sun-a)_0%,--theme(--color-tps15-sun-b)_30%,--theme(--color-tps15-pink)_60%,--theme(--color-tps15-sun-d)_90%)]" aria-hidden="true"></div>
  <header class="relative z-2 text-center mb-[clamp(24px,4vw,40px)]">
    <span class="inline-block mb-3.5 font-tps15-mono text-xs font-bold tracking-[0.4em] text-tps15-cyan text-shadow-[0_0_8px_--theme(--color-tps15-cyan)]">&#9733; Pricing &#9733;</span>
    <h2 class="m-0 font-tps15-display text-[clamp(28px,5vw,48px)] font-extrabold tracking-[-0.02em] bg-linear-180 from-white from-50% to-tps15-pink to-100% bg-clip-text text-transparent">Choose your <em class="italic">signal.</em></h2>
  </header>
  <div class="relative z-2 grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-center gap-4 max-w-[360px] md:max-w-[940px] mx-auto">
    <article class="relative flex flex-col px-5 pt-[22px] pb-5 rounded-[4px] bg-tps15-bg/70 border-[1.5px] border-tps15-pink backdrop-blur-[6px] shadow-[inset_0_0_0_1px_--alpha(--color-tps15-pink/40),0_0_24px_--alpha(--color-tps15-pink/30)]">
      <h3 class="m-0 mb-3 font-tps15-mono text-sm font-bold uppercase tracking-[0.16em] text-tps15-pink text-shadow-[0_0_8px_--alpha(--color-tps15-pink/70)]">Wave</h3>
      <div class="mb-[18px] font-tps15-mono text-[42px] font-extrabold tracking-[-0.02em] text-white text-shadow-[0_0_12px_--alpha(--color-tps15-pink/60)]">$15</div>
      <ul class="list-none p-0 m-0 mb-5 flex-1 font-tps15-mono text-[13px]/[1.95] text-tps15-body">
        <li class="before:content-['\25B8_'] before:text-tps15-pink">Solo channel</li>
        <li class="before:content-['\25B8_'] before:text-tps15-pink">5 GB</li>
        <li class="before:content-['\25B8_'] before:text-tps15-pink">Email reach</li>
      </ul>
      <a href="#wave" class="block text-center px-3.5 py-2.5 bg-transparent text-tps15-pink border-[1.5px] border-tps15-pink font-tps15-mono text-xs font-bold uppercase tracking-[0.1em] no-underline transition-[background-color,color,box-shadow] duration-150 hover:bg-tps15-pink hover:text-tps15-bg hover:shadow-[0_0_16px_--theme(--color-tps15-pink)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px] motion-reduce:transition-none">Tune in</a>
    </article>
    <article class="relative flex flex-col px-5 pt-[22px] pb-5 rounded-[4px] bg-tps15-bg/70 border-[1.5px] border-tps15-cyan backdrop-blur-[6px] shadow-[inset_0_0_0_1px_--alpha(--color-tps15-cyan/50),0_0_30px_--alpha(--color-tps15-cyan/50)]">
      <span class="absolute -top-[11px] left-1/2 -translate-x-1/2 px-3 py-0.75 bg-tps15-bg text-tps15-cyan border border-tps15-cyan font-tps15-mono text-[10px] font-bold tracking-[0.18em] text-shadow-[0_0_6px_--theme(--color-tps15-cyan)]">&#9733; FAVORITE &#9733;</span>
      <h3 class="m-0 mb-3 font-tps15-mono text-sm font-bold uppercase tracking-[0.16em] text-tps15-cyan text-shadow-[0_0_8px_--alpha(--color-tps15-cyan/70)]">Pulse</h3>
      <div class="mb-[18px] font-tps15-mono text-[42px] font-extrabold tracking-[-0.02em] text-white text-shadow-[0_0_12px_--alpha(--color-tps15-cyan/60)]">$39</div>
      <ul class="list-none p-0 m-0 mb-5 flex-1 font-tps15-mono text-[13px]/[1.95] text-tps15-body">
        <li class="before:content-['\25B8_'] before:text-tps15-cyan">Multi-channel</li>
        <li class="before:content-['\25B8_'] before:text-tps15-cyan">50 GB</li>
        <li class="before:content-['\25B8_'] before:text-tps15-cyan">Live chat</li>
        <li class="before:content-['\25B8_'] before:text-tps15-cyan">Custom domain</li>
      </ul>
      <a href="#pulse" class="block text-center px-3.5 py-2.5 bg-transparent text-tps15-cyan border-[1.5px] border-tps15-cyan font-tps15-mono text-xs font-bold uppercase tracking-[0.1em] no-underline transition-[background-color,color,box-shadow] duration-150 hover:bg-tps15-cyan hover:text-tps15-bg hover:shadow-[0_0_16px_--theme(--color-tps15-cyan)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px] motion-reduce:transition-none">Tune in</a>
    </article>
    <article class="relative flex flex-col px-5 pt-[22px] pb-5 rounded-[4px] bg-tps15-bg/70 border-[1.5px] border-tps15-pink backdrop-blur-[6px] shadow-[inset_0_0_0_1px_--alpha(--color-tps15-pink/40),0_0_24px_--alpha(--color-tps15-pink/30)]">
      <h3 class="m-0 mb-3 font-tps15-mono text-sm font-bold uppercase tracking-[0.16em] text-tps15-pink text-shadow-[0_0_8px_--alpha(--color-tps15-pink/70)]">Storm</h3>
      <div class="mb-[18px] font-tps15-mono text-[42px] font-extrabold tracking-[-0.02em] text-white text-shadow-[0_0_12px_--alpha(--color-tps15-pink/60)]">$99</div>
      <ul class="list-none p-0 m-0 mb-5 flex-1 font-tps15-mono text-[13px]/[1.95] text-tps15-body">
        <li class="before:content-['\25B8_'] before:text-tps15-pink">Unlimited</li>
        <li class="before:content-['\25B8_'] before:text-tps15-pink">500 GB</li>
        <li class="before:content-['\25B8_'] before:text-tps15-pink">SSO + SLA</li>
      </ul>
      <a href="#storm" class="block text-center px-3.5 py-2.5 bg-transparent text-tps15-pink border-[1.5px] border-tps15-pink font-tps15-mono text-xs font-bold uppercase tracking-[0.1em] no-underline transition-[background-color,color,box-shadow] duration-150 hover:bg-tps15-pink hover:text-tps15-bg hover:shadow-[0_0_16px_--theme(--color-tps15-pink)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px] motion-reduce:transition-none">Tune in</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps15-bg: #0c0420;
  --color-tps15-bg: oklch(0.12 0.07 296);
  --color-tps15-mid: #1a052e;
  --color-tps15-mid: oklch(0.18 0.1 300);
  --color-tps15-top: #2a0843;
  --color-tps15-top: oklch(0.24 0.13 302);
  --color-tps15-body: #d6c8ee;
  --color-tps15-body: oklch(0.85 0.05 300);
  --color-tps15-pink: #ec4899;
  --color-tps15-pink: oklch(0.65 0.23 354);
  --color-tps15-cyan: #22d3ee;
  --color-tps15-cyan: oklch(0.79 0.14 202);
  --color-tps15-sun-a: #fde68a;
  --color-tps15-sun-a: oklch(0.91 0.13 94);
  --color-tps15-sun-b: #f59e0b;
  --color-tps15-sun-b: oklch(0.75 0.16 70);
  --color-tps15-sun-d: #a855f7;
  --color-tps15-sun-d: oklch(0.63 0.24 304);
  --font-tps15-mono: 'JetBrains Mono', monospace;
  --font-tps15-display: 'Chakra Petch', system-ui, sans-serif;
  --font-tps15-sans: 'Chakra Petch', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-15 {
  width: 100%;
  min-height: 100svh;
}
```
