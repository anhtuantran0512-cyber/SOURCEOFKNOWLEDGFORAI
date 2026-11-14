---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-glowing-gradient-text-web3-neon-glow/"
title: "Tailwind Glowing Gradient Text (Web3 Neon Glow)"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A Web3 protocol card where the gradient headline blooms: a blurred, aria-hidden duplicate sits behind the real text and breathes with animate-ttg02-pulse."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glowing Gradient Text (Web3 Neon Glow)
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-glowing-gradient-text-web3-neon-glow/

A Web3 protocol card where the gradient headline blooms: a blurred, aria-hidden duplicate sits behind the real text and breathes with animate-ttg02-pulse. Because the bloom is the same gradient clipped to the same glyphs, the glow is multi-coloured &mdash; something text-shadow can't do.
## HTML
```html
<section class="ttg-02 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-ttg02-bg px-5 py-16 font-ttg02-sans text-ttg02-ink" aria-labelledby="ttg02-title">
  <span aria-hidden="true" class="absolute -top-48 left-1/2 -z-10 size-[38rem] -translate-x-1/2 rounded-full bg-ttg02-b/25 blur-3xl"></span>
  <span aria-hidden="true" class="absolute -bottom-56 -left-24 -z-10 size-[28rem] rounded-full bg-ttg02-a/15 blur-3xl"></span>
  <article class="relative w-full max-w-xl rounded-3xl border border-white/10 bg-white/[0.03] p-10 text-center shadow-[inset_0_1px_0_0_rgb(255_255_255/0.08),0_40px_80px_-30px_rgb(0_0_0/0.8)] backdrop-blur-xl max-sm:p-7">
    <p class="inline-flex items-center gap-2 font-ttg02-mono text-xs font-semibold tracking-[0.18em] text-ttg02-a uppercase"><span aria-hidden="true" class="size-1.5 rounded-full bg-ttg02-a shadow-[0_0_10px_var(--color-ttg02-a)] animate-ttg02-blink motion-reduce:animate-none"></span>Mainnet live</p>
    <h2 id="ttg02-title" class="mt-5 text-[clamp(2.4rem,6.5vw,3.9rem)] leading-[1.04] font-bold tracking-[-0.035em]">Own your<br>
      <span class="relative inline-block">
        <span class="relative z-10 bg-linear-to-r from-ttg02-a via-ttg02-b to-ttg02-c bg-clip-text text-transparent">digital future</span>
        <span aria-hidden="true" class="absolute inset-0 bg-linear-to-r from-ttg02-a via-ttg02-b to-ttg02-c bg-clip-text text-transparent opacity-60 blur-xl select-none animate-ttg02-pulse motion-reduce:animate-none">digital future</span>
      </span>
    </h2>
    <p class="mx-auto mt-5 max-w-md text-[15.5px]/[1.7] text-ttg02-mut text-pretty">Stake, earn and govern with transparent on-chain contracts &mdash; audited, open-source and live on three networks.</p>
    <ul class="mt-8 flex flex-wrap justify-center gap-2.5" aria-label="Supported networks">
      <li class="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/[0.04] px-3.5 py-1.5 text-[13px] font-medium"><span aria-hidden="true" class="size-2 rounded-full bg-ttg02-b"></span>Polygon</li>
      <li class="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/[0.04] px-3.5 py-1.5 text-[13px] font-medium"><span aria-hidden="true" class="size-2 rounded-full bg-linear-to-br from-ttg02-a to-ttg02-b"></span>Solana</li>
      <li class="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/[0.04] px-3.5 py-1.5 text-[13px] font-medium"><span aria-hidden="true" class="size-2 rounded-full bg-ttg02-c"></span>Ethereum</li>
    </ul>
    <a href="#" class="mt-9 inline-flex min-h-12 items-center gap-2 rounded-xl bg-white px-6 text-[15px] font-semibold text-ttg02-bg transition hover:bg-ttg02-a focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ttg02-a">Launch app <span aria-hidden="true">&rarr;</span></a>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg02-bg: #04060f;
  --color-ttg02-bg: oklch(0.13 0.02 270);
  --color-ttg02-ink: #eef2f8;
  --color-ttg02-ink: oklch(0.96 0.01 255);
  --color-ttg02-mut: #a9c4dc;
  --color-ttg02-mut: oklch(0.8 0.045 240);
  --color-ttg02-a: #00e5ff;
  --color-ttg02-a: oklch(0.86 0.15 205);
  --color-ttg02-b: #a36cff;
  --color-ttg02-b: oklch(0.66 0.21 295);
  --color-ttg02-c: #ff3d84;
  --color-ttg02-c: oklch(0.66 0.23 5);
  --font-ttg02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-ttg02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttg02-pulse: ttg02-pulse 4s ease-in-out infinite;
  --animate-ttg02-blink: ttg02-blink 1.6s ease-in-out infinite;

  @keyframes ttg02-pulse {
    0%,
        100% {
      opacity: 0.4;
      transform: scale(1);
    }

    50% {
      opacity: 0.8;
      transform: scale(1.03);
    }
  }

  @keyframes ttg02-blink {
    50% {
      opacity: 0.35;
    }
  }
}

.ttg-02 {
  width: 100%;
  min-height: 100svh;
}
```
