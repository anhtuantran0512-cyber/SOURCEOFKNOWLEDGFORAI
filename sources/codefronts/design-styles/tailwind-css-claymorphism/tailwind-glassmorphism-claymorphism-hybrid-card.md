---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-glassmorphism-claymorphism-hybrid-card/"
title: "Tailwind Glassmorphism + Claymorphism Hybrid Card"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "The hybrid dominating 2026 product pages: clay geometry and clay shadow layering, but a frosted-glass fill."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism + Claymorphism Hybrid Card
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-glassmorphism-claymorphism-hybrid-card/

The hybrid dominating 2026 product pages: clay geometry and clay shadow layering, but a frosted-glass fill. backdrop-blur-[26px] backdrop-saturate-170 lets the photo through while the inset sheen keeps the puffy silhouette. Fallbacks are variants — not-supports-[backdrop-filter:blur(1px)]: and a prefers-reduced-transparency custom variant — and the status dot now has a label.
## HTML
```html
<section class="tcl-05 w-full min-h-svh grid place-items-center bg-tcl05-bg px-5 py-14 font-tcl05-sans text-tcl05-ink" aria-label="Glassmorphism and claymorphism hybrid card demo">
  <div class="grid w-full justify-items-center gap-6">
    <div class="relative isolate grid min-h-[min(74vh,540px)] w-full max-w-[780px] place-items-center overflow-hidden rounded-[48px] bg-[linear-gradient(140deg,oklch(0.45_0.16_300),oklch(0.38_0.14_250))] p-[clamp(18px,4vw,44px)] shadow-[0_40px_80px_-30px_oklch(0.15_0.06_285/0.8)]">
      <div aria-hidden="true" class="absolute inset-0 -z-20 scale-[1.02] animate-tcl05-drift bg-[url('https://images.unsplash.com/photo-1502691876148-a84978e59af8?q=80&w=1400&auto=format&fit=crop'),linear-gradient(140deg,oklch(0.5_0.17_305),oklch(0.34_0.13_250))] bg-cover bg-center opacity-90 motion-reduce:animate-none"></div>
      <div aria-hidden="true" class="absolute inset-0 -z-10">
        <i class="absolute -top-[12%] -left-[8%] aspect-square w-[44%] rounded-full bg-[oklch(0.8_0.16_30/0.55)] opacity-60 blur-md"></i>
        <i class="absolute -right-[10%] -bottom-[14%] aspect-square w-[44%] rounded-full bg-[oklch(0.82_0.15_175/0.5)] opacity-60 blur-md"></i>
      </div>
      <article class="grid w-full max-w-[400px] gap-3.5 rounded-[40px] border border-white/40 bg-tcl05-tint/24 p-[clamp(24px,3.4vw,34px)] shadow-tcl05-card backdrop-blur-[26px] backdrop-saturate-170 transition-[translate,box-shadow] duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-2 hover:shadow-tcl05-lift not-supports-[backdrop-filter:blur(1px)]:bg-tcl05-tint/90 not-supports-[backdrop-filter:blur(1px)]:text-tcl05-deep tcl05-rt:bg-tcl05-tint/95 tcl05-rt:text-tcl05-deep tcl05-rt:backdrop-blur-none motion-reduce:transition-none">
        <header class="flex items-center justify-between gap-3">
          <span class="rounded-full bg-white/20 px-3.5 py-1.5 text-[11px] font-bold uppercase tracking-[0.14em] shadow-tcl05-chip">Frosted clay</span>
          <span class="inline-flex items-center gap-2 text-xs font-semibold"><span aria-hidden="true" class="relative size-2.5 rounded-full bg-tcl05-live shadow-[0_0_0_4px_oklch(0.85_0.17_150/0.22)] after:absolute after:inset-0 after:animate-ping after:rounded-full after:bg-tcl05-live/60 motion-reduce:after:animate-none"></span>On sale now</span>
        </header>
        <h2 class="font-tcl05-display text-[clamp(28px,4vw,36px)] font-extrabold leading-none tracking-[-0.03em]">Aurora Pass</h2>
        <p class="text-[14.5px] leading-relaxed text-tcl05-mut text-pretty tcl05-rt:text-tcl05-deep/80">Clay geometry, glass fill. The inset sheen keeps the puffy silhouette while the backdrop shows through.</p>
        <dl class="mt-0.5 grid grid-cols-3 gap-2.5">
          <div class="grid gap-0.5 rounded-[22px] bg-white/14 px-3.5 py-3 shadow-tcl05-chip"><dt class="text-[10.5px] uppercase tracking-[0.1em] text-tcl05-mut">Blur</dt><dd class="text-[15px] font-bold tabular-nums">26px</dd></div>
          <div class="grid gap-0.5 rounded-[22px] bg-white/14 px-3.5 py-3 shadow-tcl05-chip"><dt class="text-[10.5px] uppercase tracking-[0.1em] text-tcl05-mut">Tint</dt><dd class="text-[15px] font-bold tabular-nums">24%</dd></div>
          <div class="grid gap-0.5 rounded-[22px] bg-white/14 px-3.5 py-3 shadow-tcl05-chip"><dt class="text-[10.5px] uppercase tracking-[0.1em] text-tcl05-mut">Radius</dt><dd class="text-[15px] font-bold tabular-nums">40px</dd></div>
        </dl>
        <div class="mt-1.5 flex flex-wrap gap-2.5">
          <button type="button" class="min-h-12 cursor-pointer rounded-[26px] bg-tcl05-solid/95 px-5.5 text-sm font-bold text-tcl05-deep shadow-tcl05-solid transition-[translate,background-color] duration-200 hover:-translate-y-0.5 hover:bg-white active:translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">Get the pass</button>
          <button type="button" class="min-h-12 cursor-pointer rounded-[26px] border border-white/30 bg-white/14 px-5.5 text-sm font-semibold text-tcl05-ink shadow-tcl05-chip transition-[translate,background-color] duration-200 hover:-translate-y-0.5 hover:bg-white/24 active:translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">Details</button>
        </div>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/10 px-4 py-2 text-center font-tcl05-mono text-[11.5px] text-tcl05-mut">backdrop-blur-[26px] backdrop-saturate-170 · border-white/40 rim light · not-supports-[…]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@custom-variant tcl05-rt (@media (prefers-reduced-transparency: reduce));

@theme {
  --color-tcl05-bg: #2b2458;
  --color-tcl05-bg: oklch(0.3 0.09 285);
  --color-tcl05-tint: #dac4ff;
  --color-tcl05-tint: oklch(0.86 0.09 300);
  --color-tcl05-solid: #f3e8ff;
  --color-tcl05-solid: oklch(0.95 0.045 300);
  --color-tcl05-shade: #190f41b3;
  --color-tcl05-shade: oklch(0.22 0.09 285 / 0.7);
  --color-tcl05-ink: #fdfaff;
  --color-tcl05-ink: oklch(0.99 0.01 300);
  --color-tcl05-mut: #e7e1f6;
  --color-tcl05-mut: oklch(0.92 0.03 300);
  --color-tcl05-deep: #241c43;
  --color-tcl05-deep: oklch(0.26 0.07 290);
  --color-tcl05-live: #70ec90;
  --color-tcl05-live: oklch(0.85 0.17 150);
  --font-tcl05-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl05-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl05-card: 0 30px 60px -20px var(--color-tcl05-shade), inset 0 -18px 30px -14px var(--color-tcl05-shade), inset 0 20px 30px -10px oklch(1 0 0 / 0.5);
  --shadow-tcl05-lift: 0 44px 80px -26px var(--color-tcl05-shade), inset 0 -18px 30px -14px var(--color-tcl05-shade), inset 0 22px 32px -10px oklch(1 0 0 / 0.58);
  --shadow-tcl05-chip: inset 0 -6px 10px -8px var(--color-tcl05-shade), inset 0 8px 10px -6px oklch(1 0 0 / 0.5);
  --shadow-tcl05-solid: 0 14px 24px -14px var(--color-tcl05-shade), inset 0 -8px 12px -9px oklch(0.6 0.1 290 / 0.5), inset 0 9px 12px -7px white;
  --animate-tcl05-drift: tcl05-drift 26s ease-in-out infinite alternate;

  @keyframes tcl05-drift {
    to {
      scale: 1.1;
      translate: -2% 1%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-05 {
  width: 100%;
  min-height: 100svh;
}
```
