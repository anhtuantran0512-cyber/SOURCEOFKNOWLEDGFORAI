---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-glass-aurora-pricing-cards/"
title: "Tailwind Glass Aurora Pricing Cards"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Frosted cards floating over three slow-drifting aurora blobs."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glass Aurora Pricing Cards
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-glass-aurora-pricing-cards/

Frosted cards floating over three slow-drifting aurora blobs. The port keeps the whole glass recipe in the class list &mdash; bg-white/6, border-white/12, backdrop-blur-[20px] backdrop-saturate-150 &mdash; and moves the one genuinely CSS-only part, the drift keyframes, into an --animate-* theme token so the blobs read as animate-tps10-drift on the element.
## HTML
```html
<section class="tps-10 relative w-full min-h-svh overflow-hidden [contain:layout_paint] bg-tps10-bg font-tps10-sans text-tps10-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none" aria-hidden="true">
    <span class="absolute -top-[10%] -left-[10%] size-[380px] rounded-full blur-[60px] opacity-70 bg-[radial-gradient(circle,--theme(--color-tps10-sky)_0%,transparent_60%)] animate-tps10-drift [animation-delay:-3s] motion-reduce:animate-none"></span>
    <span class="absolute top-[20%] -right-[8%] size-[320px] rounded-full blur-[60px] opacity-70 bg-[radial-gradient(circle,--theme(--color-tps10-indigo)_0%,transparent_60%)] animate-tps10-drift [animation-delay:-8s] motion-reduce:animate-none"></span>
    <span class="absolute -bottom-[15%] left-[30%] size-[360px] rounded-full blur-[60px] opacity-70 bg-[radial-gradient(circle,--theme(--color-tps10-cyan)_0%,transparent_60%)] animate-tps10-drift [animation-delay:-14s] motion-reduce:animate-none"></span>
  </div>
  <header class="relative z-2 text-center mb-[clamp(28px,4vw,44px)]">
    <h2 class="m-0 mb-2 text-[clamp(24px,3.6vw,36px)] font-bold tracking-[-0.02em] text-white">Pricing, on the house.</h2>
    <p class="m-0 text-sm text-tps10-muted">Three tiers, all built on the same calm interface.</p>
  </header>
  <div class="relative z-2 grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-center gap-[18px] max-w-[380px] md:max-w-[980px] mx-auto">
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[18px] bg-white/6 border border-white/12 backdrop-blur-[20px] backdrop-saturate-150 shadow-[0_18px_48px_rgba(0,0,0,0.25)]">
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps10-label">Drift</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[42px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>0<span class="ml-1.5 text-[0.32em] font-medium opacity-65">free</span></div>
      <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13.5px]/[1.9] text-tps10-body">
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">Personal projects</li>
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">1 GB storage</li>
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">Community access</li>
      </ul>
      <a href="#drift" class="block text-center px-4 py-2.75 rounded-[10px] bg-white/8 text-tps10-label no-underline text-[13.5px] font-semibold border border-tps10-label/30 transition-[background-color,color] duration-[180ms] hover:bg-white/18 hover:text-white focus-visible:outline-2 focus-visible:outline-tps10-sky focus-visible:outline-offset-[3px] motion-reduce:transition-none">Get started</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[18px] bg-white/10 border border-tps10-sky/40 backdrop-blur-[20px] backdrop-saturate-150 md:scale-[1.04] shadow-[inset_0_0_0_1px_--alpha(--color-tps10-sky/40),0_22px_56px_--alpha(--color-tps10-sky/18)]">
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1.25 rounded-full bg-linear-90 from-tps10-sky to-tps10-indigo text-tps10-bg text-[10.5px] font-bold uppercase tracking-[0.08em]">Recommended</span>
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps10-label">Float</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[42px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>18<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13.5px]/[1.9] text-tps10-body">
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">Unlimited projects</li>
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">30 GB storage</li>
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">Priority email support</li>
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">Custom domains</li>
      </ul>
      <a href="#float" class="block text-center px-4 py-2.75 rounded-[10px] bg-linear-90 from-tps10-sky to-tps10-indigo text-tps10-bg no-underline text-[13.5px] font-semibold border border-transparent transition-[filter] duration-[180ms] hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tps10-sky focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Float</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[18px] bg-white/6 border border-white/12 backdrop-blur-[20px] backdrop-saturate-150 shadow-[0_18px_48px_rgba(0,0,0,0.25)]">
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps10-label">Stratos</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[42px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>56<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13.5px]/[1.9] text-tps10-body">
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">Everything in Float</li>
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">SSO + audit logs</li>
        <li class="before:content-['\25C7'] before:inline-block before:w-5 before:text-tps10-sky">Dedicated success manager</li>
      </ul>
      <a href="#stratos" class="block text-center px-4 py-2.75 rounded-[10px] bg-white/8 text-tps10-label no-underline text-[13.5px] font-semibold border border-tps10-label/30 transition-[background-color,color] duration-[180ms] hover:bg-white/18 hover:text-white focus-visible:outline-2 focus-visible:outline-tps10-sky focus-visible:outline-offset-[3px] motion-reduce:transition-none">Talk to sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps10-bg: #050a1a;
  --color-tps10-bg: oklch(0.14 0.04 265);
  --color-tps10-body: #d1ddee;
  --color-tps10-body: oklch(0.89 0.02 250);
  --color-tps10-muted: #b8c4dc;
  --color-tps10-muted: oklch(0.81 0.03 255);
  --color-tps10-label: #93c5fd;
  --color-tps10-label: oklch(0.81 0.1 250);
  --color-tps10-sky: #38bdf8;
  --color-tps10-sky: oklch(0.75 0.14 231);
  --color-tps10-indigo: #818cf8;
  --color-tps10-indigo: oklch(0.68 0.16 277);
  --color-tps10-cyan: #22d3ee;
  --color-tps10-cyan: oklch(0.79 0.14 202);
  --font-tps10-sans: 'Sora', system-ui, sans-serif;
  --animate-tps10-drift: tps10-drift 22s ease-in-out infinite alternate;
}
/* Keyframes have no utility form — the shorthand is a theme token
   (--animate-tps10-drift → animate-tps10-drift), the body lives here. */

@keyframes tps10-drift {
  0% {
    transform: translate(0, 0) scale(1);
  }

  50% {
    transform: translate(40px, -30px) scale(1.08);
  }

  100% {
    transform: translate(-30px, 30px) scale(0.95);
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-10 {
  width: 100%;
  min-height: 100svh;
}
```
