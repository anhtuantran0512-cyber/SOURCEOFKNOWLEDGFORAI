---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-gift-card-flip-copy-clipboard-coupon-reveal/"
title: "Tailwind Gift Card Flip with Copy-to-Clipboard Coupon Code Reveal"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A holiday gift card whose back holds a redeemable coupon code and a real copy button."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gift Card Flip with Copy-to-Clipboard Coupon Code Reveal
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-gift-card-flip-copy-clipboard-coupon-reveal/

A holiday gift card whose back holds a redeemable coupon code and a real copy button. Drift animation becomes an @theme --animate-* entry (so animate-tfc03-drift is a utility), and the copy confirmation is announced through an aria-live region rather than by mutating the code text &mdash; which is what the CSS original did, silently destroying the value a screen-reader user was about to read.
## HTML
```html
<section class="tfc-03 w-full min-h-svh grid place-items-center bg-tfc03-bg font-tfc03-sans px-5 py-10 text-tfc03-ink">
  <div class="group relative w-[380px] max-w-full h-[250px] [perspective:1200px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc03-gold has-[:focus-visible]:outline-offset-4">
    <input id="tfc-03-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-03-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Reveal your coupon code</span></label>

    <div class="relative w-full h-full transition-transform duration-[800ms] ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 grid place-content-center justify-items-center rounded-2xl overflow-hidden bg-linear-135 from-tfc03-p1 via-tfc03-p2 to-tfc03-p3 border border-tfc03-pink/30 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_20px_44px_-14px_oklch(0.4_0.2_350/0.5)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden] before:absolute before:inset-0 before:bg-[radial-gradient(ellipse_at_70%_30%,oklch(0.77_0.16_70/0.15),transparent_60%),radial-gradient(ellipse_at_30%_80%,oklch(0.65_0.2_350/0.2),transparent_50%)]">
        <span aria-hidden="true" class="absolute top-[10%] left-[8%] text-xl opacity-25 animate-tfc03-drift motion-reduce:animate-none">&#10052;</span>
        <span aria-hidden="true" class="absolute top-[20%] right-[10%] text-sm opacity-25 animate-tfc03-drift [animation-delay:0.8s] motion-reduce:animate-none">&#10022;</span>
        <span aria-hidden="true" class="absolute bottom-[15%] left-[12%] text-base opacity-25 animate-tfc03-drift [animation-delay:1.6s] motion-reduce:animate-none">&#10052;</span>
        <span aria-hidden="true" class="absolute bottom-[10%] right-[8%] text-xl opacity-25 animate-tfc03-drift [animation-delay:2.4s] motion-reduce:animate-none">&#10022;</span>
        <p class="relative z-1 mb-2 text-xs font-semibold uppercase tracking-[0.2em] text-tfc03-ink/55">Nova Store</p>
        <h3 class="relative z-1 bg-linear-135 from-tfc03-gold via-tfc03-rose to-tfc03-violet bg-clip-text text-center text-[28px] font-black leading-tight tracking-[-0.01em] text-transparent">Holiday Gift Card</h3>
        <p class="relative z-1 mt-2.5 text-[42px] font-black tracking-[-0.02em] text-tfc03-gold [text-shadow:0_0_30px_oklch(0.77_0.16_70/0.5)]">$50</p>
        <p class="absolute bottom-4 right-4 z-1 text-[10px] uppercase tracking-[0.1em] text-tfc03-ink/35">Hover, tap or press Space &rarr;</p>
      </div>

      <div class="absolute inset-0 grid place-content-center justify-items-center gap-4 rounded-2xl overflow-hidden p-7 bg-linear-135 from-tfc03-b1 to-tfc03-b2 border border-tfc03-gold/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_20px_44px_-14px_oklch(0.3_0.1_280/0.6)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden] before:absolute before:inset-0 before:bg-[radial-gradient(ellipse_at_50%_50%,oklch(0.77_0.16_70/0.06),transparent_70%)]">
        <p class="relative z-1 text-[10px] font-semibold uppercase tracking-[0.18em] text-tfc03-ink/40">Your exclusive coupon code</p>
        <code id="tfc-03-code" class="relative z-1 w-full rounded-xl border-2 border-dashed border-tfc03-gold/40 bg-tfc03-gold/8 px-6 py-3 text-center font-tfc03-mono text-[22px] font-bold tracking-[0.2em] text-tfc03-gold [text-shadow:0_0_20px_oklch(0.77_0.16_70/0.4)]">NOVA-XMAS-2025</code>
        <button id="tfc-03-copy" type="button" data-code="NOVA-XMAS-2025" class="relative z-30 inline-flex min-h-11 items-center gap-2 rounded-xl border border-tfc03-gold/40 bg-tfc03-gold/12 px-5 text-[13px] font-semibold text-tfc03-gold transition-colors duration-150 hover:bg-tfc03-gold/22 focus-visible:outline-2 focus-visible:outline-tfc03-gold focus-visible:outline-offset-2">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>
          Copy code
        </button>
        <p class="relative z-1 text-[11px] text-tfc03-ink/45">Expires <span class="text-tfc03-rose">December 31, 2025</span></p>
        <p id="tfc-03-status" role="status" aria-live="polite" class="sr-only"></p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc03-bg: #0c0510;
  --color-tfc03-bg: oklch(0.15 0.03 315);
  --color-tfc03-p1: #3b0764;
  --color-tfc03-p1: oklch(0.29 0.15 300);
  --color-tfc03-p2: #831843;
  --color-tfc03-p2: oklch(0.36 0.14 358);
  --color-tfc03-p3: #7c2d12;
  --color-tfc03-p3: oklch(0.38 0.12 40);
  --color-tfc03-b1: #0a1628;
  --color-tfc03-b1: oklch(0.19 0.04 260);
  --color-tfc03-b2: #1e0833;
  --color-tfc03-b2: oklch(0.2 0.09 300);
  --color-tfc03-pink: #ec4899;
  --color-tfc03-pink: oklch(0.65 0.22 350);
  --color-tfc03-rose: #fb7185;
  --color-tfc03-rose: oklch(0.72 0.17 15);
  --color-tfc03-gold: #f59e0b;
  --color-tfc03-gold: oklch(0.77 0.16 70);
  --color-tfc03-violet: #c084fc;
  --color-tfc03-violet: oklch(0.75 0.17 300);
  --color-tfc03-ink: #fff1f5;
  --color-tfc03-ink: oklch(0.97 0.015 350);
  --font-tfc03-sans: 'Sora', system-ui, sans-serif;
  --font-tfc03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tfc03-drift: tfc03-drift 4s ease-in-out infinite;
}

@keyframes tfc03-drift {
  0%,
    100% {
    transform: translateY(0) rotate(0deg);
  }

  50% {
    transform: translateY(-8px) rotate(15deg);
  }
}

.tfc-03 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-03 * {
    transition-duration: 1ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('tfc-03-copy');
  const status = document.getElementById('tfc-03-status');
  if (!btn) return;
  btn.addEventListener('click', async () => {
    const code = btn.dataset.code || '';
    try {
      if (!navigator.clipboard) throw new Error('insecure context');
      await navigator.clipboard.writeText(code);
      status.textContent = 'Coupon code ' + code + ' copied to clipboard';
      btn.lastChild.textContent = ' Copied';
      setTimeout(() => { btn.lastChild.textContent = ' Copy code'; }, 2000);
    } catch {
      // Insecure origin or denied permission: select the code so a manual copy works.
      const el = document.getElementById('tfc-03-code');
      const range = document.createRange();
      range.selectNodeContents(el);
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      status.textContent = 'Copying is unavailable here — the code is selected, press Ctrl or Cmd + C';
    }
  });
})();
```
