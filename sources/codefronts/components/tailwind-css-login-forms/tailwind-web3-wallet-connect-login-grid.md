---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-web3-wallet-connect-login-grid/"
title: "Tailwind Web3 Wallet Connect Login Grid"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The non-traditional auth flow for crypto and AI toolkits: a tidy grid of connection tiles &mdash; MetaMask, WalletConnect, Coinbase, Ledger &mdash; in…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Web3 Wallet Connect Login Grid
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-web3-wallet-connect-login-grid/

The non-traditional auth flow for crypto and AI toolkits: a tidy grid of connection tiles &mdash; MetaMask, WalletConnect, Coinbase, Ledger &mdash; in strict, uniform boxes with a hardware-accelerated lift and a brand-tinted glow on hover. Each tile's brand hue rides a --tint custom property, so four connectors need one class list, not four.
## HTML
```html
<section class="tlf-04 w-full min-h-svh grid place-items-center bg-tlf04-stage font-tlf04-sans text-tlf04-ink p-6">
  <div class="w-[min(440px,100%)] p-7 bg-tlf04-card border border-tlf04-edge rounded-[20px] shadow-[0_30px_70px_-44px_black]">
    <h1 class="text-[22px] font-bold tracking-tight">Connect a wallet</h1>
    <p class="mt-1.5 mb-5 text-[13.5px] text-tlf04-mut">Choose how you&rsquo;d like to sign in to the app.</p>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
      <button type="button" style="--tint:45" class="flex flex-col items-start gap-1.5 p-4 min-h-11 cursor-pointer text-left rounded-[14px] bg-tlf04-tile border-[1.5px] border-tlf04-tileedge text-tlf04-ink transition-[translate,box-shadow,border-color] duration-150 hover:-translate-y-[3px] hover:border-[oklch(0.62_0.16_var(--tint))] hover:shadow-[0_12px_26px_-14px_oklch(0.62_0.18_var(--tint)/0.6)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.62_0.18_var(--tint)/0.6)] motion-reduce:transition-[box-shadow,border-color] motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="grid place-items-center size-9 rounded-[10px] text-[18px] bg-[color-mix(in_oklch,oklch(0.62_0.16_var(--tint))_22%,var(--color-tlf04-card))]">&#129418;</span>
        <span class="text-[14.5px] font-semibold">MetaMask</span>
        <span class="text-[11.5px] text-tlf04-mut">Popular</span>
      </button>
      <button type="button" style="--tint:250" class="flex flex-col items-start gap-1.5 p-4 min-h-11 cursor-pointer text-left rounded-[14px] bg-tlf04-tile border-[1.5px] border-tlf04-tileedge text-tlf04-ink transition-[translate,box-shadow,border-color] duration-150 hover:-translate-y-[3px] hover:border-[oklch(0.62_0.16_var(--tint))] hover:shadow-[0_12px_26px_-14px_oklch(0.62_0.18_var(--tint)/0.6)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.62_0.18_var(--tint)/0.6)] motion-reduce:transition-[box-shadow,border-color] motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="grid place-items-center size-9 rounded-[10px] text-[18px] bg-[color-mix(in_oklch,oklch(0.62_0.16_var(--tint))_22%,var(--color-tlf04-card))]">&#9672;</span>
        <span class="text-[14.5px] font-semibold">WalletConnect</span>
        <span class="text-[11.5px] text-tlf04-mut">Mobile</span>
      </button>
      <button type="button" style="--tint:255" class="flex flex-col items-start gap-1.5 p-4 min-h-11 cursor-pointer text-left rounded-[14px] bg-tlf04-tile border-[1.5px] border-tlf04-tileedge text-tlf04-ink transition-[translate,box-shadow,border-color] duration-150 hover:-translate-y-[3px] hover:border-[oklch(0.62_0.16_var(--tint))] hover:shadow-[0_12px_26px_-14px_oklch(0.62_0.18_var(--tint)/0.6)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.62_0.18_var(--tint)/0.6)] motion-reduce:transition-[box-shadow,border-color] motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="grid place-items-center size-9 rounded-[10px] text-[18px] bg-[color-mix(in_oklch,oklch(0.62_0.16_var(--tint))_22%,var(--color-tlf04-card))]">&#9673;</span>
        <span class="text-[14.5px] font-semibold">Coinbase</span>
        <span class="text-[11.5px] text-tlf04-mut">Custodial</span>
      </button>
      <button type="button" style="--tint:200" class="flex flex-col items-start gap-1.5 p-4 min-h-11 cursor-pointer text-left rounded-[14px] bg-tlf04-tile border-[1.5px] border-tlf04-tileedge text-tlf04-ink transition-[translate,box-shadow,border-color] duration-150 hover:-translate-y-[3px] hover:border-[oklch(0.62_0.16_var(--tint))] hover:shadow-[0_12px_26px_-14px_oklch(0.62_0.18_var(--tint)/0.6)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.62_0.18_var(--tint)/0.6)] motion-reduce:transition-[box-shadow,border-color] motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="grid place-items-center size-9 rounded-[10px] text-[18px] bg-[color-mix(in_oklch,oklch(0.62_0.16_var(--tint))_22%,var(--color-tlf04-card))]">&#9638;</span>
        <span class="text-[14.5px] font-semibold">Ledger</span>
        <span class="text-[11.5px] text-tlf04-mut">Hardware</span>
      </button>
    </div>
    <p class="mt-5 text-center text-xs text-tlf04-mut">By connecting you agree to the <a href="#" class="text-tlf04-link no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf04-link">Terms</a>.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf04-stage: #0b0d12;
  --color-tlf04-stage: oklch(0.15 0.012 265);
  --color-tlf04-card: #14171f;
  --color-tlf04-card: oklch(0.19 0.014 265);
  --color-tlf04-edge: #232734;
  --color-tlf04-edge: oklch(0.26 0.016 265);
  --color-tlf04-tile: #1b1f2a;
  --color-tlf04-tile: oklch(0.23 0.016 265);
  --color-tlf04-tileedge: #2a2f3d;
  --color-tlf04-tileedge: oklch(0.3 0.018 265);
  --color-tlf04-ink: #e8ebf3;
  --color-tlf04-ink: oklch(0.93 0.01 265);
  --color-tlf04-mut: #a2a9bd;
  --color-tlf04-mut: oklch(0.72 0.02 265);
  --color-tlf04-link: #8fb4ff;
  --color-tlf04-link: oklch(0.76 0.12 255);
  --font-tlf04-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tlf-04 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
```
