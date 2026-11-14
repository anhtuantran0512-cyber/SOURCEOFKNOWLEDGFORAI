---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-product-comparison-flip-card-hover-tap-keyboard/"
title: "Tailwind Product Comparison Flip Card with Hover, Tap & Keyboard Reveal"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "The reference-grade flip: a product render on the front, an eight-cell specification grid and an Add to Cart CTA on the back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Product Comparison Flip Card with Hover, Tap & Keyboard Reveal
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-product-comparison-flip-card-hover-tap-keyboard/

The reference-grade flip: a product render on the front, an eight-cell specification grid and an Add to Cart CTA on the back. The port's win is the trigger — group-hover:, group-has-checked: and group-has-[:focus-visible]: stack on one element, so the same card answers a mouse, a thumb and a Tab key with one transform.
## HTML
```html
<section class="tfc-01 w-full min-h-svh grid place-items-center bg-tfc01-bg font-tfc01-sans px-5 py-10 text-tfc01-ink">
  <div class="group relative w-[340px] h-[480px] [perspective:1200px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc01-acc has-[:focus-visible]:outline-offset-4">
    <input id="tfc-01-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-01-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show technical specifications for ProVision X7 Monitor</span></label>

    <div class="relative w-full h-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden bg-linear-145 from-tfc01-panel to-tfc01-panel2 border border-tfc01-edge shadow-[0_1px_2px_oklch(0_0_0/0.5),0_18px_40px_-12px_oklch(0_0_0/0.65)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <span class="absolute top-4 right-4 z-10 rounded-full bg-tfc01-gold px-2.5 py-1 text-[10px] font-bold uppercase tracking-[0.1em] text-black">New 2025</span>
        <div class="relative h-[220px] shrink-0 grid place-items-center overflow-hidden bg-linear-135 from-tfc01-stage to-tfc01-stage2 before:absolute before:inset-0 before:bg-[radial-gradient(ellipse_at_50%_70%,oklch(0.5_0.24_295/0.4),transparent_70%)]">
          <svg class="relative z-1" width="140" height="140" viewBox="0 0 140 140" fill="none" aria-hidden="true">
            <rect x="30" y="50" width="80" height="60" rx="8" fill="url(#tfc-01-g1)" opacity=".9"/>
            <rect x="38" y="58" width="64" height="44" rx="4" fill="#0a0a1a"/>
            <rect x="40" y="60" width="60" height="40" rx="3" fill="url(#tfc-01-g2)" opacity=".8"/>
            <circle cx="70" cy="80" r="10" fill="none" stroke="#7c3aed" stroke-width="2"/>
            <circle cx="70" cy="80" r="4" fill="#06b6d4"/>
            <line x1="55" y1="115" x2="85" y2="115" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/>
            <rect x="62" y="110" width="16" height="5" rx="2" fill="#1a1a2e"/>
            <defs>
              <linearGradient id="tfc-01-g1" x1="30" y1="50" x2="110" y2="110" gradientUnits="userSpaceOnUse"><stop stop-color="#2d1b69"/><stop offset="1" stop-color="#0e7490"/></linearGradient>
              <linearGradient id="tfc-01-g2" x1="40" y1="60" x2="100" y2="100" gradientUnits="userSpaceOnUse"><stop stop-color="#7c3aed" stop-opacity=".3"/><stop offset="1" stop-color="#06b6d4" stop-opacity=".2"/></linearGradient>
            </defs>
          </svg>
        </div>
        <div class="flex flex-1 flex-col gap-2.5 p-6">
          <p class="text-[11px] font-semibold uppercase tracking-[0.15em] text-tfc01-acc2">NovaTech</p>
          <h3 class="text-[22px] font-bold leading-tight tracking-[-0.01em] text-white">ProVision X7 Monitor</h3>
          <p class="text-[28px] font-extrabold tracking-[-0.02em] text-tfc01-acc">$649 <span class="text-sm font-normal text-tfc01-muted">/ unit</span></p>
          <p class="mt-auto flex items-center justify-center gap-1.5 text-[11px] tracking-[0.08em] text-tfc01-dim">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="opacity-60" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>
            Hover, tap or press Space for specs
          </p>
        </div>
      </div>

      <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden p-7 bg-linear-145 from-tfc01-back to-tfc01-back2 border border-tfc01-edge2 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_18px_40px_-12px_oklch(0_0_0/0.65)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <h3 class="mb-4 text-[13px] font-bold uppercase tracking-[0.12em] text-tfc01-acc2">Technical Specifications</h3>
        <dl class="grid flex-1 grid-cols-2 gap-3">
          <div class="rounded-xl border border-white/8 bg-white/4 p-3.5"><dt class="mb-1 text-[10px] uppercase tracking-[0.1em] text-tfc01-dim">Display</dt><dd class="text-[15px] font-semibold text-white">27&quot; IPS</dd></div>
          <div class="rounded-xl border border-white/8 bg-white/4 p-3.5"><dt class="mb-1 text-[10px] uppercase tracking-[0.1em] text-tfc01-dim">Resolution</dt><dd class="text-[15px] font-semibold text-white">4K UHD</dd></div>
          <div class="rounded-xl border border-white/8 bg-white/4 p-3.5"><dt class="mb-1 text-[10px] uppercase tracking-[0.1em] text-tfc01-dim">Refresh Rate</dt><dd class="text-[15px] font-semibold text-tfc01-gold">165 Hz</dd></div>
          <div class="rounded-xl border border-white/8 bg-white/4 p-3.5"><dt class="mb-1 text-[10px] uppercase tracking-[0.1em] text-tfc01-dim">Response</dt><dd class="text-[15px] font-semibold text-white">1 ms GTG</dd></div>
          <div class="rounded-xl border border-white/8 bg-white/4 p-3.5"><dt class="mb-1 text-[10px] uppercase tracking-[0.1em] text-tfc01-dim">Panel</dt><dd class="text-[15px] font-semibold text-white">Nano IPS</dd></div>
          <div class="rounded-xl border border-white/8 bg-white/4 p-3.5"><dt class="mb-1 text-[10px] uppercase tracking-[0.1em] text-tfc01-dim">Ports</dt><dd class="text-[15px] font-semibold text-white">2&times; DP 1.4</dd></div>
          <div class="rounded-xl border border-white/8 bg-white/4 p-3.5"><dt class="mb-1 text-[10px] uppercase tracking-[0.1em] text-tfc01-dim">HDR</dt><dd class="text-[15px] font-semibold text-tfc01-gold">HDR 600</dd></div>
          <div class="rounded-xl border border-white/8 bg-white/4 p-3.5"><dt class="mb-1 text-[10px] uppercase tracking-[0.1em] text-tfc01-dim">Coverage</dt><dd class="text-[15px] font-semibold text-white">98% DCI-P3</dd></div>
        </dl>
        <button type="button" class="relative z-30 mt-5 min-h-11 w-full rounded-xl bg-linear-135 from-tfc01-acc to-tfc01-acc2 text-sm font-bold tracking-[0.06em] text-white transition-opacity duration-200 hover:opacity-85 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Add to Cart</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc01-bg: #0d0d14;
  --color-tfc01-bg: oklch(0.17 0.015 285);
  --color-tfc01-panel: #1a1a2e;
  --color-tfc01-panel: oklch(0.23 0.04 285);
  --color-tfc01-panel2: #16213e;
  --color-tfc01-panel2: oklch(0.24 0.06 265);
  --color-tfc01-back: #0f172a;
  --color-tfc01-back: oklch(0.21 0.04 265);
  --color-tfc01-back2: #1e1b4b;
  --color-tfc01-back2: oklch(0.25 0.09 285);
  --color-tfc01-stage: #1a0533;
  --color-tfc01-stage: oklch(0.18 0.09 300);
  --color-tfc01-stage2: #0c1a4f;
  --color-tfc01-stage2: oklch(0.22 0.11 270);
  --color-tfc01-acc: #7c3aed;
  --color-tfc01-acc: oklch(0.55 0.24 295);
  --color-tfc01-acc2: #06b6d4;
  --color-tfc01-acc2: oklch(0.7 0.14 205);
  --color-tfc01-gold: #f59e0b;
  --color-tfc01-gold: oklch(0.77 0.16 70);
  --color-tfc01-ink: #f1f5f9;
  --color-tfc01-ink: oklch(0.97 0.005 250);
  --color-tfc01-muted: #94a3b8;
  --color-tfc01-muted: oklch(0.72 0.03 250);
  --color-tfc01-dim: #7c8798;
  --color-tfc01-dim: oklch(0.62 0.02 250);
  --color-tfc01-edge: #3b2a6b;
  --color-tfc01-edge: oklch(0.38 0.11 295);
  --color-tfc01-edge2: #1c5568;
  --color-tfc01-edge2: oklch(0.42 0.08 210);
  --font-tfc01-sans: 'Sora', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tfc-01 {
  width: 100%;
  min-height: 100svh;
}
/* Reduced motion: the flip becomes an instant face swap, never a slower spin. */

@media (prefers-reduced-motion: reduce) {
  .tfc-01 * {
    transition-duration: 1ms !important;
  }
}
```
