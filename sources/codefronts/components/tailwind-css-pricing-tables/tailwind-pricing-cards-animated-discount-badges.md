---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-animated-discount-badges/"
title: "Tailwind Pricing Cards with Animated Discount Badges"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "&ldquo;Save 20%&rdquo;, &ldquo;Best value&rdquo; and &ldquo;New&rdquo; badges with personality: they bob on an idle loop, then snap to attention — scaling…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Cards with Animated Discount Badges
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-animated-discount-badges/

&ldquo;Save 20%&rdquo;, &ldquo;Best value&rdquo; and &ldquo;New&rdquo; badges with personality: they bob on an idle loop, then snap to attention — scaling and tilting — when their card is hovered. The port fixes the original: the bob animates v4's individual translate property while hover poses use scale and rotate, so the two never fight over transform.
## HTML
```html
<section class="tpt-07 w-full min-h-svh grid place-items-center bg-tpt07-bg px-5 py-20 font-tpt07-sans text-tpt07-ink antialiased" aria-label="Pricing with animated discount badges">
  <div class="grid w-full max-w-5xl justify-items-center gap-12">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-extrabold tracking-[-0.03em]">Commit longer, pay less</h2>
    <div class="grid w-full gap-8 md:grid-cols-3 md:gap-6">
      <article class="group/c relative flex flex-col gap-2 rounded-[22px] border-[1.5px] border-tpt07-line bg-white px-7 pt-9 pb-7 transition-[border-color,translate] duration-250 hover:-translate-y-1 hover:border-tpt07-acc motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="absolute -top-3.5 right-5 animate-tpt07-bob rounded-[99px_99px_99px_4px] bg-tpt07-acc px-3.5 py-1.5 text-[11.5px] font-extrabold tracking-[0.05em] text-white uppercase shadow-[0_8px_18px_-8px_var(--color-tpt07-acc)] transition-[scale,rotate] duration-300 ease-[cubic-bezier(.4,1.8,.4,1)] group-hover/c:scale-115 group-hover/c:-rotate-6 group-hover/c:[animation-play-state:paused] motion-reduce:animate-none">Save 20%</span>
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt07-mut uppercase">Annual</h3>
        <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$96<small class="text-[15px] font-semibold tracking-normal text-tpt07-mut">/yr</small></p>
        <p class="mb-5 flex-1 text-sm leading-relaxed text-tpt07-body">Two months free — <strong class="font-semibold text-tpt07-ink">20% off</strong> monthly billing.</p>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt07-line text-sm font-bold text-tpt07-ink no-underline transition-colors hover:border-tpt07-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt07-acc">Choose Annual</a>
      </article>
      <article class="group/c relative flex flex-col gap-2 rounded-[22px] border-[1.5px] border-tpt07-acc bg-white px-7 pt-9 pb-7 shadow-[0_20px_44px_-28px_var(--color-tpt07-acc)] transition-[border-color,translate] duration-250 hover:-translate-y-1 motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="absolute -top-7 right-4 grid size-17 animate-tpt07-bob place-items-center bg-tpt07-gold text-center text-[10.5px] leading-[1.1] font-extrabold tracking-[0.03em] text-tpt07-ink uppercase transition-[scale,rotate] duration-300 ease-[cubic-bezier(.4,1.8,.4,1)] [animation-delay:-1.1s] [clip-path:polygon(50%_0,61%_12%,76%_6%,79%_22%,95%_25%,88%_39%,100%_50%,88%_61%,95%_75%,79%_78%,76%_94%,61%_88%,50%_100%,39%_88%,24%_94%,21%_78%,5%_75%,12%_61%,0_50%,12%_39%,5%_25%,21%_22%,24%_6%,39%_12%)] group-hover/c:scale-120 group-hover/c:rotate-12 group-hover/c:[animation-play-state:paused] motion-reduce:animate-none">Best<br>value</span>
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt07-acc-ink uppercase">2-Year</h3>
        <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$160<small class="text-[15px] font-semibold tracking-normal text-tpt07-mut">/2 yr</small></p>
        <p class="mb-5 flex-1 text-sm leading-relaxed text-tpt07-body">Our best value — <strong class="font-semibold text-tpt07-ink">33% off</strong> monthly billing.</p>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt07-acc text-sm font-bold text-white no-underline transition-colors hover:bg-tpt07-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt07-acc">Choose 2-Year</a>
      </article>
      <article class="group/c relative flex flex-col gap-2 rounded-[22px] border-[1.5px] border-tpt07-line bg-white px-7 pt-9 pb-7 transition-[border-color,translate] duration-250 hover:-translate-y-1 hover:border-tpt07-acc motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="absolute -top-3 right-6 animate-tpt07-bob rounded-lg bg-tpt07-ink px-3 py-1.5 text-[11px] font-extrabold tracking-[0.12em] text-white uppercase transition-[scale,rotate] duration-300 ease-[cubic-bezier(.4,1.8,.4,1)] [animation-delay:-2.2s] group-hover/c:scale-110 group-hover/c:rotate-4 group-hover/c:[animation-play-state:paused] motion-reduce:animate-none">New</span>
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt07-mut uppercase">Lifetime</h3>
        <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$399<small class="text-[15px] font-semibold tracking-normal text-tpt07-mut"> once</small></p>
        <p class="mb-5 flex-1 text-sm leading-relaxed text-tpt07-body"><strong class="font-semibold text-tpt07-ink">New tier:</strong> pay once, keep every update forever.</p>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt07-line text-sm font-bold text-tpt07-ink no-underline transition-colors hover:border-tpt07-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt07-acc">Choose Lifetime</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt07-line bg-white px-3.5 py-2 font-tpt07-mono text-[11.5px] text-tpt07-mut">animate-tpt07-bob (translate) · group-hover/c:scale-115 -rotate-6</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt07-bg: #fdf6f0;
  --color-tpt07-bg: oklch(0.975 0.012 60);
  --color-tpt07-ink: #241d18;
  --color-tpt07-ink: oklch(0.23 0.015 55);
  --color-tpt07-body: #574c42;
  --color-tpt07-body: oklch(0.44 0.025 55);
  --color-tpt07-mut: #75695e;
  --color-tpt07-mut: oklch(0.53 0.025 55);
  --color-tpt07-line: #eadfd5;
  --color-tpt07-line: oklch(0.91 0.018 60);
  --color-tpt07-acc: #e2452f;
  --color-tpt07-acc: oklch(0.61 0.2 30);
  --color-tpt07-acc-ink: #b83322;
  --color-tpt07-acc-ink: oklch(0.53 0.18 30);
  --color-tpt07-gold: #f6cb3f;
  --color-tpt07-gold: oklch(0.86 0.16 90);
  --font-tpt07-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tpt07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tpt07-bob: tpt07-bob 3.2s ease-in-out infinite;

  @keyframes tpt07-bob {
    0%,
        100% {
      translate: 0 0;
    }

    50% {
      translate: 0 -5px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-07 {
  width: 100%;
  min-height: 100svh;
}
```
