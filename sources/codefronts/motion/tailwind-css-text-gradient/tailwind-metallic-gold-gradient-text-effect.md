---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-metallic-gold-gradient-text-effect/"
title: "Tailwind Metallic Gold Gradient Text Effect"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A luxury membership card with real metallic gold: an eight-stop bronze → gold → near-white highlight → gold ramp, shared as one --ttg10-gold custom property…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Metallic Gold Gradient Text Effect
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-metallic-gold-gradient-text-effect/

A luxury membership card with real metallic gold: an eight-stop bronze → gold → near-white highlight → gold ramp, shared as one --ttg10-gold custom property and applied with bg-(image:--ttg10-gold). The highlight glides slowly across the wordmark and price like light across foil.
## HTML
```html
<section class="ttg-10 w-full min-h-svh grid place-items-center bg-ttg10-bg bg-[radial-gradient(60%_50%_at_50%_40%,var(--color-ttg10-glow),transparent)] px-5 py-14 font-ttg10-sans text-ttg10-ink" aria-labelledby="ttg10-title">
  <article class="w-full max-w-sm rounded-[28px] border border-transparent p-10 text-center shadow-[0_40px_80px_-30px_rgb(0_0_0/0.9)] [background:linear-gradient(var(--color-ttg10-card),var(--color-ttg10-card))_padding-box,linear-gradient(160deg,var(--color-ttg10-edge),transparent_40%,transparent_60%,var(--color-ttg10-edge))_border-box] max-sm:p-7">
    <svg class="mx-auto size-8" viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="ttg10-g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b45309"/><stop offset=".5" stop-color="#fff2c4"/><stop offset="1" stop-color="#c27a12"/></linearGradient></defs><path d="M16 2l3.6 10.4L30 16l-10.4 3.6L16 30l-3.6-10.4L2 16l10.4-3.6z" fill="url(#ttg10-g)"/></svg>
    <p class="mt-4 text-[11px] font-bold tracking-[0.22em] text-ttg10-mut uppercase">Premier membership</p>
    <h2 id="ttg10-title" class="mt-3 font-ttg10-serif text-[4.5rem] leading-none font-semibold tracking-[-0.01em]"><span class="bg-(image:--ttg10-gold) bg-[length:200%_100%] bg-clip-text text-transparent animate-ttg10-sheen motion-reduce:animate-none">Aurum</span></h2>
    <p class="mt-2 font-ttg10-serif text-lg text-ttg10-mut italic">Excellence, redefined.</p>
    <ul class="mt-8 grid gap-3 text-left text-[14.5px]">
      <li class="flex items-center gap-3"><span aria-hidden="true" class="bg-(image:--ttg10-gold) bg-clip-text text-xs text-transparent">&#10022;</span>Priority concierge, 24/7</li>
      <li class="flex items-center gap-3"><span aria-hidden="true" class="bg-(image:--ttg10-gold) bg-clip-text text-xs text-transparent">&#10022;</span>Curated portfolio management</li>
      <li class="flex items-center gap-3"><span aria-hidden="true" class="bg-(image:--ttg10-gold) bg-clip-text text-xs text-transparent">&#10022;</span>Private event invitations</li>
    </ul>
    <div class="mt-8 flex items-baseline justify-center gap-1 border-t border-ttg10-line pt-6"><span class="bg-(image:--ttg10-gold) bg-[length:200%_100%] bg-clip-text text-4xl font-bold tracking-tight text-transparent animate-ttg10-sheen motion-reduce:animate-none">$2,500</span><span class="text-sm text-ttg10-mut">/ year</span></div>
    <a href="#" class="mt-6 flex min-h-12 items-center justify-center rounded-xl bg-(image:--ttg10-gold) bg-[length:200%_100%] bg-left text-[15px] font-bold text-ttg10-bg transition-[background-position] duration-700 hover:bg-right focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ttg10-edge motion-reduce:transition-none">Request access</a>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg10-bg: #080604;
  --color-ttg10-bg: oklch(0.12 0.008 70);
  --color-ttg10-glow: #3a2a0f66;
  --color-ttg10-glow: oklch(0.28 0.05 75 / 0.4);
  --color-ttg10-card: #110d08;
  --color-ttg10-card: oklch(0.155 0.012 70);
  --color-ttg10-edge: #e2b453;
  --color-ttg10-edge: oklch(0.8 0.12 80);
  --color-ttg10-line: #3a2f1f;
  --color-ttg10-line: oklch(0.3 0.025 75);
  --color-ttg10-ink: #f7efe0;
  --color-ttg10-ink: oklch(0.95 0.02 80);
  --color-ttg10-mut: #b8a68a;
  --color-ttg10-mut: oklch(0.73 0.04 80);
  --font-ttg10-serif: 'Cormorant Garamond', Georgia, serif;
  --font-ttg10-sans: 'Manrope', system-ui, sans-serif;
  --animate-ttg10-sheen: ttg10-sheen 6s ease-in-out infinite;

  @keyframes ttg10-sheen {
    0%,
        100% {
      background-position: 0% 50%;
    }

    50% {
      background-position: 100% 50%;
    }
  }
}
/* No background-image namespace exists in @theme, so the shared ramp is a plain custom property. */

.ttg-10 {
  width: 100%;
  min-height: 100svh;
  --ttg10-gold: linear-gradient(120deg, #7a3a0c 0%, #b45309 14%, #d99a1e 30%, #fcd770 44%, #fff6dc 52%, #fcd770 60%, #c27a12 78%, #7a3a0c 100%);
}
```
