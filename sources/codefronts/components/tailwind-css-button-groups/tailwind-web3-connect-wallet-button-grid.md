---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-web3-connect-wallet-button-grid/"
title: "Tailwind Web3 Connect Wallet Button Grid (Wallet Sign-In Modal)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A dark, glassy wallet picker: a responsive grid-cols-[repeat(auto-fit,minmax(9.5rem,1fr))] of wallet tiles, the recommended one wrapped in a true gradient…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Web3 Connect Wallet Button Grid (Wallet Sign-In Modal)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-web3-connect-wallet-button-grid/

A dark, glassy wallet picker: a responsive grid-cols-[repeat(auto-fit,minmax(9.5rem,1fr))] of wallet tiles, the recommended one wrapped in a true gradient border ([background:…_padding-box,…_border-box]) with a floating badge, and a hover that lifts the tile and reveals a connect arrow. A close button and a reassuring footer make it a complete modal.
## HTML
```html
<section class="tbg-10 w-full min-h-svh grid place-items-center bg-tbg10-bg bg-[radial-gradient(120%_100%_at_50%_-10%,var(--color-tbg10-glow),transparent_70%)] px-5 py-14 font-tbg10-sans text-tbg10-ink" aria-label="Web3 wallet connect grid demo">
  <div role="dialog" aria-labelledby="tbg10-title" class="relative w-full max-w-[29rem] rounded-3xl border border-tbg10-a1/25 bg-linear-to-b from-tbg10-panel/60 to-tbg10-tile/90 px-6 pt-7 pb-6 shadow-tbg10-modal backdrop-blur-md sm:px-7">
    <button type="button" aria-label="Close" class="absolute top-4 right-4 grid size-11 cursor-pointer place-items-center rounded-full text-tbg10-mut transition hover:bg-white/8 hover:text-tbg10-ink focus-visible:outline-3 focus-visible:outline-tbg10-a2"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    <p class="w-fit bg-linear-90 from-tbg10-a1 to-tbg10-a2 bg-clip-text text-xs font-extrabold uppercase tracking-[0.18em] text-transparent">Connect</p>
    <h3 id="tbg10-title" class="mt-1.5 mb-1.5 text-[26px] font-bold tracking-[-0.02em]">Choose a wallet</h3>
    <p class="mb-6 text-sm text-tbg10-mut">Sign in to continue. We never store your keys.</p>
    <div class="grid grid-cols-[repeat(auto-fit,minmax(9.5rem,1fr))] gap-3">
      <button type="button" class="group relative flex cursor-pointer flex-col items-start gap-2.5 rounded-2xl border-[1.5px] border-transparent p-4 text-left transition-[translate,box-shadow] duration-200 [background:linear-gradient(var(--color-tbg10-tile),var(--color-tbg10-tile))_padding-box,linear-gradient(135deg,var(--color-tbg10-a1),var(--color-tbg10-a2))_border-box] hover:-translate-y-0.5 hover:shadow-[0_14px_30px_-14px_var(--color-tbg10-a1)] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg10-a2 motion-reduce:transition-none">
        <span class="absolute -top-2.5 right-3 rounded-full bg-linear-90 from-tbg10-a1 to-tbg10-a2 px-2.5 py-1 text-[10px] font-extrabold uppercase tracking-[0.04em] text-tbg10-bg">Recommended</span>
        <span aria-hidden="true" style="--l:linear-gradient(135deg,#f6851b,#e2761b)" class="grid size-10 place-items-center rounded-xl bg-(image:--l) text-lg font-extrabold text-white">M</span>
        <span class="text-[15.5px] font-bold">MetaMask</span>
        <span class="flex items-center gap-1.5 text-xs text-tbg10-ok"><span aria-hidden="true" class="size-1.5 rounded-full bg-tbg10-ok"></span>Detected in browser</span>
        <svg class="absolute top-4 right-4 -translate-x-1 opacity-0 transition duration-200 group-hover:translate-x-0 group-hover:opacity-100 group-focus-visible:translate-x-0 group-focus-visible:opacity-100" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </button>
      <button type="button" class="group relative flex cursor-pointer flex-col items-start gap-2.5 rounded-2xl border border-white/10 bg-white/4 p-4 text-left transition-[translate,border-color,background-color] duration-200 hover:-translate-y-0.5 hover:border-tbg10-a2 hover:bg-white/7 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg10-a2 motion-reduce:transition-none">
        <span aria-hidden="true" style="--l:linear-gradient(135deg,#3b99fc,#1f6fe5)" class="grid size-10 place-items-center rounded-xl bg-(image:--l) text-lg font-extrabold text-white">W</span>
        <span class="text-[15.5px] font-bold">WalletConnect</span>
        <span class="text-xs text-tbg10-mut">Scan with mobile app</span>
        <svg class="absolute top-4 right-4 -translate-x-1 opacity-0 transition duration-200 group-hover:translate-x-0 group-hover:opacity-100 group-focus-visible:translate-x-0 group-focus-visible:opacity-100" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </button>
      <button type="button" class="group relative flex cursor-pointer flex-col items-start gap-2.5 rounded-2xl border border-white/10 bg-white/4 p-4 text-left transition-[translate,border-color,background-color] duration-200 hover:-translate-y-0.5 hover:border-tbg10-a2 hover:bg-white/7 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg10-a2 motion-reduce:transition-none">
        <span aria-hidden="true" style="--l:linear-gradient(135deg,#2c5ff6,#0a3ecb)" class="grid size-10 place-items-center rounded-xl bg-(image:--l) text-lg font-extrabold text-white">C</span>
        <span class="text-[15.5px] font-bold">Coinbase Wallet</span>
        <span class="text-xs text-tbg10-mut">Extension or app</span>
        <svg class="absolute top-4 right-4 -translate-x-1 opacity-0 transition duration-200 group-hover:translate-x-0 group-hover:opacity-100 group-focus-visible:translate-x-0 group-focus-visible:opacity-100" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </button>
      <button type="button" class="group relative flex cursor-pointer flex-col items-start gap-2.5 rounded-2xl border border-white/10 bg-white/4 p-4 text-left transition-[translate,border-color,background-color] duration-200 hover:-translate-y-0.5 hover:border-tbg10-a2 hover:bg-white/7 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg10-a2 motion-reduce:transition-none">
        <span aria-hidden="true" style="--l:linear-gradient(135deg,#4a4a4a,#141414)" class="grid size-10 place-items-center rounded-xl bg-(image:--l) text-lg font-extrabold text-white ring-1 ring-white/15">L</span>
        <span class="text-[15.5px] font-bold">Ledger</span>
        <span class="text-xs text-tbg10-mut">Hardware wallet</span>
        <svg class="absolute top-4 right-4 -translate-x-1 opacity-0 transition duration-200 group-hover:translate-x-0 group-hover:opacity-100 group-focus-visible:translate-x-0 group-focus-visible:opacity-100" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </button>
    </div>
    <p class="mt-6 flex items-center justify-center gap-2 border-t border-white/8 pt-5 text-[13px] text-tbg10-mut">New to wallets? <a href="#" class="font-semibold text-tbg10-a2 underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-tbg10-a2">Learn how they work</a></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg10-bg: #0a0713;
  --color-tbg10-glow: #1d1636;
  --color-tbg10-panel: #281e46;
  --color-tbg10-tile: #120c22;
  --color-tbg10-ink: #f2eeff;
  --color-tbg10-mut: #b3a9d6;
  --color-tbg10-mut: oklch(0.76 0.06 290);
  --color-tbg10-ok: #6fe2a6;
  --color-tbg10-ok: oklch(0.83 0.14 158);
  --color-tbg10-a1: #9b4dff;
  --color-tbg10-a1: oklch(0.62 0.23 300);
  --color-tbg10-a2: #4dd2e8;
  --color-tbg10-a2: oklch(0.8 0.12 210);
  --shadow-tbg10-modal: 0 40px 90px -40px rgb(90 40 220 / 0.6);
  --font-tbg10-sans: 'Sora', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-10 {
  width: 100%;
  min-height: 100svh;
}
```
