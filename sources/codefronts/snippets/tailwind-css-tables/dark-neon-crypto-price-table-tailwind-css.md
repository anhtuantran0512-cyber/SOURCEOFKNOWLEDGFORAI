---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/dark-neon-crypto-price-table-tailwind-css/"
title: "Dark Neon Crypto Price Table in Tailwind CSS"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A cyberpunk market tracker where hovering the body dims every row to 40% and the hovered row glows back with a cyan laser rail — group-hover/tb:opacity-40…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Neon Crypto Price Table in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-tables/dark-neon-crypto-price-table-tailwind-css/

A cyberpunk market tracker where hovering the body dims every row to 40% and the hovered row glows back with a cyan laser rail — group-hover/tb:opacity-40 plus hover:opacity-100!, two classes and no script. The original's bar charts became SVG sparklines that draw themselves in with a stroke-dashoffset keyframe, over a gradient area fill.
## HTML
```html
<section class="ttb-04 grid-cols-1 w-full min-h-svh grid place-items-center bg-ttb04-bg bg-[linear-gradient(var(--color-ttb04-grid)_1px,transparent_1px),linear-gradient(90deg,var(--color-ttb04-grid)_1px,transparent_1px)] bg-size-[32px_32px] px-5 py-14 font-ttb04-sans text-ttb04-ink" aria-label="Neon crypto price table demo">
  <svg width="0" height="0" class="absolute" aria-hidden="true">
    <defs>
      <linearGradient id="ttb04g-up" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#39ff14" stop-opacity=".35"/><stop offset="1" stop-color="#39ff14" stop-opacity="0"/></linearGradient>
      <linearGradient id="ttb04g-dn" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#ff2d55" stop-opacity=".35"/><stop offset="1" stop-color="#ff2d55" stop-opacity="0"/></linearGradient>
    </defs>
  </svg>
  <div class="w-full max-w-4xl rounded-2xl border border-ttb04-line bg-ttb04-panel/90 p-5 shadow-[0_0_0_1px_oklch(0.9_0.15_195/0.04),0_30px_80px_-30px_oklch(0.85_0.17_195/0.25)] sm:p-7">
    <header class="mb-5 flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-4">
        <h2 class="bg-linear-to-r from-ttb04-neon to-ttb04-neon2 bg-clip-text font-ttb04-mono text-xl font-bold tracking-[0.2em] text-transparent">CRYPTO.NEXUS</h2>
        <span class="flex items-center gap-2 font-ttb04-mono text-[11px] font-bold tracking-[0.2em] text-ttb04-bull">
          <span class="relative flex size-2"><span class="absolute inset-0 animate-ping rounded-full bg-ttb04-bull opacity-75 motion-reduce:animate-none"></span><span class="relative size-2 rounded-full bg-ttb04-bull"></span></span>LIVE
        </span>
      </div>
      <p class="font-ttb04-mono text-xs text-ttb04-mut">Updated 12s ago · USD</p>
    </header>
    <div class="relative overflow-x-auto">
      <table class="w-full border-collapse text-left text-sm">
        <caption class="sr-only">Top cryptocurrencies by market cap with 24 hour change and 7 day trend</caption>
        <thead class="[&_th]:border-b [&_th]:border-ttb04-line [&_th]:px-4 [&_th]:py-3 [&_th]:font-ttb04-mono [&_th]:text-[10.5px] [&_th]:font-semibold [&_th]:tracking-[0.18em] [&_th]:text-ttb04-mut [&_th]:uppercase">
          <tr><th scope="col">Asset</th><th scope="col" class="text-right">Price</th><th scope="col" class="text-right">24h</th><th scope="col" class="text-right max-sm:hidden">Market cap</th><th scope="col" class="text-right max-sm:hidden">Volume</th><th scope="col" class="text-right">7d</th></tr>
        </thead>
        <tbody class="group/tb [&_td]:relative [&_td]:px-4 [&_td]:py-3.5 [&_td]:align-middle [&_td:not(:first-child)]:text-right [&_td:not(:first-child)]:font-ttb04-mono [&_td:not(:first-child)]:tabular-nums">
          <tr class="group/row border-b border-white/5 transition duration-300 group-hover/tb:opacity-40 hover:bg-ttb04-neon/5 hover:opacity-100! motion-reduce:transition-none">
            <th scope="row" class="relative px-4 py-3.5 text-left font-normal before:absolute before:inset-y-0 before:left-0 before:w-0.5 before:bg-ttb04-neon before:opacity-0 before:shadow-[0_0_12px_var(--color-ttb04-neon)] before:transition-opacity group-hover/row:before:opacity-100">
              <div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-[#f7931a]/10 font-ttb04-mono text-[15px] font-bold text-[#f7931a] ring-1 ring-[#f7931a]/35">₿</span><div><div class="font-ttb04-mono font-bold tracking-wider text-ttb04-neon">BTC</div><div class="text-xs text-ttb04-mut">Bitcoin</div></div></div>
            </th>
            <td class="font-semibold">$67,420</td>
            <td><span class="rounded bg-ttb04-bull/10 px-2 py-1 text-[13px] font-bold text-ttb04-bull">+3.14%</span></td>
            <td class="text-ttb04-mut max-sm:hidden">$1.31T</td>
            <td class="text-ttb04-mut max-sm:hidden">$42.8B</td>
            <td><svg class="ml-auto h-8 w-24 text-ttb04-bull" viewBox="0 0 96 32" fill="none" role="img" aria-label="Up over 7 days"><path d="M0 22L16 18L32 20L48 13L64 15L80 8L96 4V32H0Z" fill="url(#ttb04g-up)"/><path d="M0 22L16 18L32 20L48 13L64 15L80 8L96 4" pathLength="1" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" class="animate-ttb04-draw [stroke-dasharray:1] motion-reduce:animate-none"/></svg></td>
          </tr>
          <tr class="group/row border-b border-white/5 transition duration-300 group-hover/tb:opacity-40 hover:bg-ttb04-neon/5 hover:opacity-100! motion-reduce:transition-none">
            <th scope="row" class="relative px-4 py-3.5 text-left font-normal before:absolute before:inset-y-0 before:left-0 before:w-0.5 before:bg-ttb04-neon before:opacity-0 before:shadow-[0_0_12px_var(--color-ttb04-neon)] before:transition-opacity group-hover/row:before:opacity-100">
              <div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-[#627eea]/10 font-ttb04-mono text-[15px] font-bold text-[#8aa0f5] ring-1 ring-[#627eea]/35">Ξ</span><div><div class="font-ttb04-mono font-bold tracking-wider text-ttb04-neon">ETH</div><div class="text-xs text-ttb04-mut">Ethereum</div></div></div>
            </th>
            <td class="font-semibold">$3,890</td>
            <td><span class="rounded bg-ttb04-bear/10 px-2 py-1 text-[13px] font-bold text-ttb04-bear">−1.22%</span></td>
            <td class="text-ttb04-mut max-sm:hidden">$468B</td>
            <td class="text-ttb04-mut max-sm:hidden">$18.1B</td>
            <td><svg class="ml-auto h-8 w-24 text-ttb04-bear" viewBox="0 0 96 32" fill="none" role="img" aria-label="Down over 7 days"><path d="M0 6L16 10L32 9L48 15L64 16L80 20L96 25V32H0Z" fill="url(#ttb04g-dn)"/><path d="M0 6L16 10L32 9L48 15L64 16L80 20L96 25" pathLength="1" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" class="animate-ttb04-draw [animation-delay:80ms] [stroke-dasharray:1] motion-reduce:animate-none"/></svg></td>
          </tr>
          <tr class="group/row border-b border-white/5 transition duration-300 group-hover/tb:opacity-40 hover:bg-ttb04-neon/5 hover:opacity-100! motion-reduce:transition-none">
            <th scope="row" class="relative px-4 py-3.5 text-left font-normal before:absolute before:inset-y-0 before:left-0 before:w-0.5 before:bg-ttb04-neon before:opacity-0 before:shadow-[0_0_12px_var(--color-ttb04-neon)] before:transition-opacity group-hover/row:before:opacity-100">
              <div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-[#00ffa3]/10 font-ttb04-mono text-[15px] font-bold text-[#00ffa3] ring-1 ring-[#00ffa3]/35">◎</span><div><div class="font-ttb04-mono font-bold tracking-wider text-ttb04-neon">SOL</div><div class="text-xs text-ttb04-mut">Solana</div></div></div>
            </th>
            <td class="font-semibold">$183.50</td>
            <td><span class="rounded bg-ttb04-bull/10 px-2 py-1 text-[13px] font-bold text-ttb04-bull">+8.77%</span></td>
            <td class="text-ttb04-mut max-sm:hidden">$84B</td>
            <td class="text-ttb04-mut max-sm:hidden">$6.4B</td>
            <td><svg class="ml-auto h-8 w-24 text-ttb04-bull" viewBox="0 0 96 32" fill="none" role="img" aria-label="Up over 7 days"><path d="M0 26L16 24L32 19L48 16L64 11L80 7L96 3V32H0Z" fill="url(#ttb04g-up)"/><path d="M0 26L16 24L32 19L48 16L64 11L80 7L96 3" pathLength="1" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" class="animate-ttb04-draw [animation-delay:160ms] [stroke-dasharray:1] motion-reduce:animate-none"/></svg></td>
          </tr>
          <tr class="group/row border-b border-white/5 transition duration-300 group-hover/tb:opacity-40 hover:bg-ttb04-neon/5 hover:opacity-100! motion-reduce:transition-none">
            <th scope="row" class="relative px-4 py-3.5 text-left font-normal before:absolute before:inset-y-0 before:left-0 before:w-0.5 before:bg-ttb04-neon before:opacity-0 before:shadow-[0_0_12px_var(--color-ttb04-neon)] before:transition-opacity group-hover/row:before:opacity-100">
              <div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-[#2a5ada]/15 font-ttb04-mono text-[15px] font-bold text-[#7d9cf0] ring-1 ring-[#2a5ada]/40">⬢</span><div><div class="font-ttb04-mono font-bold tracking-wider text-ttb04-neon">LINK</div><div class="text-xs text-ttb04-mut">Chainlink</div></div></div>
            </th>
            <td class="font-semibold">$18.42</td>
            <td><span class="rounded bg-ttb04-bull/10 px-2 py-1 text-[13px] font-bold text-ttb04-bull">+2.06%</span></td>
            <td class="text-ttb04-mut max-sm:hidden">$10.8B</td>
            <td class="text-ttb04-mut max-sm:hidden">$612M</td>
            <td><svg class="ml-auto h-8 w-24 text-ttb04-bull" viewBox="0 0 96 32" fill="none" role="img" aria-label="Up over 7 days"><path d="M0 20L16 21L32 16L48 17L64 12L80 13L96 9V32H0Z" fill="url(#ttb04g-up)"/><path d="M0 20L16 21L32 16L48 17L64 12L80 13L96 9" pathLength="1" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" class="animate-ttb04-draw [animation-delay:240ms] [stroke-dasharray:1] motion-reduce:animate-none"/></svg></td>
          </tr>
          <tr class="group/row transition duration-300 group-hover/tb:opacity-40 hover:bg-ttb04-neon/5 hover:opacity-100! motion-reduce:transition-none">
            <th scope="row" class="relative px-4 py-3.5 text-left font-normal before:absolute before:inset-y-0 before:left-0 before:w-0.5 before:bg-ttb04-neon before:opacity-0 before:shadow-[0_0_12px_var(--color-ttb04-neon)] before:transition-opacity group-hover/row:before:opacity-100">
              <div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-[#e84142]/10 font-ttb04-mono text-[15px] font-bold text-[#ff6b6c] ring-1 ring-[#e84142]/35">▲</span><div><div class="font-ttb04-mono font-bold tracking-wider text-ttb04-neon">AVAX</div><div class="text-xs text-ttb04-mut">Avalanche</div></div></div>
            </th>
            <td class="font-semibold">$41.20</td>
            <td><span class="rounded bg-ttb04-bear/10 px-2 py-1 text-[13px] font-bold text-ttb04-bear">−0.55%</span></td>
            <td class="text-ttb04-mut max-sm:hidden">$17B</td>
            <td class="text-ttb04-mut max-sm:hidden">$820M</td>
            <td><svg class="ml-auto h-8 w-24 text-ttb04-bear" viewBox="0 0 96 32" fill="none" role="img" aria-label="Down over 7 days"><path d="M0 14L16 12L32 16L48 10L64 15L80 17L96 19V32H0Z" fill="url(#ttb04g-dn)"/><path d="M0 14L16 12L32 16L48 10L64 15L80 17L96 19" pathLength="1" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" class="animate-ttb04-draw [animation-delay:320ms] [stroke-dasharray:1] motion-reduce:animate-none"/></svg></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb04-bg: #07070e;
  --color-ttb04-bg: oklch(0.13 0.015 285);
  --color-ttb04-grid: #0f1220;
  --color-ttb04-grid: oklch(0.85 0.17 195 / 0.04);
  --color-ttb04-panel: #0c0d1a;
  --color-ttb04-panel: oklch(0.16 0.025 285);
  --color-ttb04-line: #13303a;
  --color-ttb04-line: oklch(0.85 0.17 195 / 0.14);
  --color-ttb04-ink: #d8def2;
  --color-ttb04-ink: oklch(0.9 0.025 270);
  --color-ttb04-mut: #8189b0;
  --color-ttb04-mut: oklch(0.65 0.05 275);
  --color-ttb04-neon: #00f0ff;
  --color-ttb04-neon: oklch(0.87 0.16 200);
  --color-ttb04-neon2: #8b5cff;
  --color-ttb04-neon2: oklch(0.6 0.24 290);
  --color-ttb04-bull: #39ff14;
  --color-ttb04-bull: oklch(0.88 0.27 142);
  --color-ttb04-bear: #ff2d55;
  --color-ttb04-bear: oklch(0.65 0.24 15);
  --font-ttb04-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-ttb04-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttb04-draw: ttb04-draw 1.1s cubic-bezier(0.65, 0, 0.35, 1) both;

  @keyframes ttb04-draw {
    from {
      stroke-dashoffset: 1;
    }

    to {
      stroke-dashoffset: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-04 {
  width: 100%;
  min-height: 100svh;
}
```
