---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-3d-tilt-perspective-pricing-cards/"
title: "Tailwind 3D Tilt Perspective Pricing Cards"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Three cards standing in a 1400px perspective &mdash; the outer two angled back, the centre one square on, any card snapping forward on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Perspective Pricing Cards
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-3d-tilt-perspective-pricing-cards/

Three cards standing in a 1400px perspective &mdash; the outer two angled back, the centre one square on, any card snapping forward on hover. The port is where v4's per-axis transform utilities earn their keep: rotate-y-*, translate-z-* and translate-y-* compose through separate variables, so the hover state overrides one axis without restating the other two.
## HTML
```html
<section class="tps-14 w-full min-h-svh perspective-[1400px] bg-tps14-bg bg-[radial-gradient(60%_60%_at_50%_0%,--alpha(--color-tps14-violet/18),transparent_60%),radial-gradient(60%_60%_at_50%_100%,--alpha(--color-tps14-cyan/14),transparent_60%)] font-tps14-sans text-tps14-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(24px,4vw,40px)]">
    <h2 class="m-0 mb-2 text-[clamp(24px,3.6vw,36px)] font-bold tracking-[-0.02em] text-white">Pricing with depth.</h2>
    <p class="m-0 text-sm text-tps14-muted">Hover to bring a plan forward.</p>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-center gap-5 max-w-[380px] md:max-w-[980px] mx-auto transform-3d">
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[16px] bg-linear-160 from-tps14-violet/18 to-tps14-cyan/10 border border-tps14-lilac/25 backdrop-blur-[14px] shadow-[0_10px_30px_--alpha(--color-tps14-bg/50)] transition-[transform,box-shadow] duration-[400ms] ease-tps14-out md:rotate-y-[14deg] md:translate-z-[-30px] hover:rotate-y-0 hover:translate-z-[20px] hover:-translate-y-1 hover:z-3 hover:shadow-[0_24px_60px_--alpha(--color-tps14-violet/40)] motion-reduce:transition-none motion-reduce:rotate-y-0 motion-reduce:translate-z-0 motion-reduce:hover:translate-y-0">
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps14-lilac">Lite</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>9<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13px]/[1.95] text-tps14-body">
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-lilac">Personal projects</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-lilac">5 GB storage</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-lilac">Community support</li>
      </ul>
      <a href="#lite" class="block text-center px-4 py-2.75 rounded-[9px] bg-tps14-lilac/12 text-tps14-lilac no-underline text-[13.5px] font-semibold border border-tps14-lilac/30 transition-[background-color,color] duration-[180ms] hover:bg-tps14-lilac/28 hover:text-white focus-visible:outline-2 focus-visible:outline-tps14-cyan focus-visible:outline-offset-[3px] motion-reduce:transition-none">Pick Lite</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[16px] bg-linear-160 from-tps14-violet/32 to-tps14-cyan/18 border border-tps14-cyan/45 backdrop-blur-[14px] shadow-[0_10px_30px_--alpha(--color-tps14-bg/50)] transition-[transform,box-shadow] duration-[400ms] ease-tps14-out md:z-2 hover:translate-z-[20px] hover:-translate-y-1 hover:z-3 hover:shadow-[0_24px_60px_--alpha(--color-tps14-violet/40)] motion-reduce:transition-none motion-reduce:translate-z-0 motion-reduce:hover:translate-y-0">
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1.25 rounded-full bg-linear-135 from-tps14-lilac to-tps14-cyan text-tps14-bg text-[10.5px] font-bold uppercase tracking-[0.08em]">Best fit</span>
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps14-cyan">Plus</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>29<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13px]/[1.95] text-tps14-body">
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-cyan">Unlimited projects</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-cyan">50 GB storage</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-cyan">Priority support</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-cyan">Custom domains</li>
      </ul>
      <a href="#plus" class="block text-center px-4 py-2.75 rounded-[9px] bg-linear-135 from-tps14-lilac to-tps14-cyan text-tps14-bg no-underline text-[13.5px] font-semibold border border-transparent transition-[filter] duration-[180ms] hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tps14-cyan focus-visible:outline-offset-[3px] motion-reduce:transition-none">Pick Plus</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[16px] bg-linear-160 from-tps14-violet/18 to-tps14-cyan/10 border border-tps14-lilac/25 backdrop-blur-[14px] shadow-[0_10px_30px_--alpha(--color-tps14-bg/50)] transition-[transform,box-shadow] duration-[400ms] ease-tps14-out md:rotate-y-[-14deg] md:translate-z-[-30px] hover:rotate-y-0 hover:translate-z-[20px] hover:-translate-y-1 hover:z-3 hover:shadow-[0_24px_60px_--alpha(--color-tps14-violet/40)] motion-reduce:transition-none motion-reduce:rotate-y-0 motion-reduce:translate-z-0 motion-reduce:hover:translate-y-0">
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps14-lilac">Power</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>79<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13px]/[1.95] text-tps14-body">
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-lilac">Everything in Plus</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-lilac">SSO + audit logs</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps14-lilac">Dedicated CSM</li>
      </ul>
      <a href="#power" class="block text-center px-4 py-2.75 rounded-[9px] bg-tps14-lilac/12 text-tps14-lilac no-underline text-[13.5px] font-semibold border border-tps14-lilac/30 transition-[background-color,color] duration-[180ms] hover:bg-tps14-lilac/28 hover:text-white focus-visible:outline-2 focus-visible:outline-tps14-cyan focus-visible:outline-offset-[3px] motion-reduce:transition-none">Pick Power</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps14-bg: #0d0a1a;
  --color-tps14-bg: oklch(0.15 0.04 290);
  --color-tps14-body: #c4bde0;
  --color-tps14-body: oklch(0.81 0.04 290);
  --color-tps14-muted: #a8a0c8;
  --color-tps14-muted: oklch(0.72 0.05 292);
  --color-tps14-lilac: #c4b5fd;
  --color-tps14-lilac: oklch(0.81 0.1 294);
  --color-tps14-violet: #7c3aed;
  --color-tps14-violet: oklch(0.54 0.25 294);
  --color-tps14-cyan: #67e8f9;
  --color-tps14-cyan: oklch(0.87 0.11 200);
  --font-tps14-sans: 'Outfit', system-ui, sans-serif;
  --ease-tps14-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-14 {
  width: 100%;
  min-height: 100svh;
}
```
