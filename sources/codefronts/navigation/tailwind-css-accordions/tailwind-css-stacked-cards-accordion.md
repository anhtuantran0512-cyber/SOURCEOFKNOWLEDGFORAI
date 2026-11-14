---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-stacked-cards-accordion/"
title: "Tailwind CSS Stacked Cards Accordion"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A digital-wallet deck: credit cards, a boarding pass and a loyalty card rest in an overlapping pile, each showing only its header strip."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Stacked Cards Accordion
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-stacked-cards-accordion/

A digital-wallet deck: credit cards, a boarding pass and a loyalty card rest in an overlapping pile, each showing only its header strip. Pick one and it pulls out of the stack — the negative margin releases, the tilt straightens, the shadow deepens and a details sheet unrolls beneath it while the rest of the deck closes ranks. Radio-driven with has-checked:, [:has(input:checked)+&]: and a grid-rows-[0fr]→[1fr] panel.
## HTML
```html
<section class="tac-22 w-full min-h-svh grid place-items-center bg-tac22-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tac22-glow),transparent_70%)] px-4 py-14 font-tac22-sans text-tac22-ink" aria-label="Stacked wallet cards accordion demo">
  <div class="grid w-full justify-items-center gap-7">
    <article class="w-full max-w-[25rem] rounded-[32px] bg-white/80 p-4 shadow-[0_1px_2px_oklch(0.3_0.02_80/0.06),0_30px_70px_-30px_oklch(0.3_0.03_80/0.35)] ring-1 ring-tac22-ink/8 sm:p-5">
      <header class="flex items-end justify-between gap-4 px-1 pb-5 pt-1">
        <div>
          <p class="text-[12px] font-semibold tracking-[0.14em] uppercase text-tac22-mut">Wallet</p>
          <h2 class="mt-1 text-[26px] font-extrabold tracking-[-0.03em]">$12,480<span class="text-tac22-mut">.22</span></h2>
        </div>
        <p class="rounded-full bg-tac22-ok/12 px-2.5 py-1 text-[12px] font-semibold text-tac22-ok-ink">+$842 this week</p>
      </header>

      <fieldset class="relative">
        <legend class="sr-only">Choose a card to view its details</legend>

        <div class="group/c relative rotate-[-1.2deg] transition-[margin,rotate,translate] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] not-has-checked:hover:-translate-y-1.5 has-checked:rotate-0 [:has(input:checked)+&]:mt-5 motion-reduce:transition-none">
          <label class="relative block h-[12.5rem] cursor-pointer overflow-hidden rounded-[22px] bg-tac22-c1a bg-linear-135 from-tac22-c1a via-tac22-c1b to-tac22-c1a p-5 text-white shadow-[0_2px_4px_oklch(0.2_0.02_270/0.2),0_10px_24px_-10px_oklch(0.2_0.02_270/0.45)] ring-1 ring-white/10 transition-shadow duration-500 group-has-checked/c:shadow-[0_4px_10px_oklch(0.2_0.02_270/0.2),0_28px_50px_-18px_oklch(0.2_0.02_270/0.6)] has-[:focus-visible]:outline-3 has-[:focus-visible]:outline-offset-3 has-[:focus-visible]:outline-tac22-focus">
            <input type="radio" name="tac22-card" class="sr-only" aria-label="Aurora Platinum Visa ending 4821" checked>
            <span aria-hidden="true" class="pointer-events-none absolute -right-16 -top-20 size-56 rounded-full bg-[conic-gradient(from_200deg,#ffffff00,#b7c4ff40,#f4b8ff38,#ffffff00)] blur-xl"></span>
            <span class="relative flex h-3 items-center justify-between text-[13px] font-semibold">
              <span class="tracking-[0.02em]">Aurora Bank · Platinum</span>
              <span class="font-tac22-mono text-white/80">•• 4821</span>
            </span>
            <svg class="relative mt-10 h-8 w-11" viewBox="0 0 44 32" aria-hidden="true"><rect x="0.5" y="0.5" width="43" height="31" rx="6" fill="#d9c08a"/><path d="M0 11h15M0 21h15M29 11h15M29 21h15M15 0v32M29 0v32" stroke="#a88a52" stroke-width="1.2"/></svg>
            <span class="relative mt-3 block font-tac22-mono text-[17px] tracking-[0.14em] text-white/95">•••• •••• •••• 4821</span>
            <span class="relative mt-2 flex items-end justify-between text-[11.5px] text-white/75">
              <span>ELENA MARCHETTI · 09/29</span>
              <span class="text-[19px] font-extrabold italic tracking-[-0.02em] text-white">VISA</span>
            </span>
          </label>
          <div class="invisible grid grid-rows-[0fr] opacity-0 transition-[grid-template-rows,opacity,visibility] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-checked/c:visible group-has-checked/c:grid-rows-[1fr] group-has-checked/c:opacity-100 motion-reduce:transition-none">
            <div class="min-h-0 overflow-hidden">
              <div class="mx-2 mt-3 rounded-2xl bg-tac22-sheet p-4 ring-1 ring-tac22-ink/6">
                <div class="flex items-baseline justify-between text-[13px]"><span class="text-tac22-mut">Balance</span><span class="font-bold">$2,318.40 <span class="font-medium text-tac22-mut">/ $8,000</span></span></div>
                <div class="mt-2 h-1.5 overflow-hidden rounded-full bg-tac22-ink/8"><div class="h-full w-[29%] rounded-full bg-tac22-c1b"></div></div>
                <ul class="mt-4 divide-y divide-tac22-ink/6 text-[13.5px]">
                  <li class="flex justify-between py-2"><span>Blue Bottle Coffee</span><span class="font-tac22-mono font-medium">−$6.50</span></li>
                  <li class="flex justify-between py-2"><span>Figma · Annual</span><span class="font-tac22-mono font-medium">−$144.00</span></li>
                  <li class="flex justify-between py-2"><span>Refund · Patagonia</span><span class="font-tac22-mono font-medium text-tac22-ok-ink">+$89.00</span></li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div class="group/c relative -mt-[8.75rem] rotate-[1deg] transition-[margin,rotate,translate] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] not-has-checked:hover:-translate-y-1.5 has-checked:mt-5 has-checked:rotate-0 [:has(input:checked)+&]:mt-5 motion-reduce:transition-none">
          <label class="relative block h-[12.5rem] cursor-pointer overflow-hidden rounded-[22px] bg-tac22-c2a bg-linear-135 from-tac22-c2a to-tac22-c2b p-5 text-white shadow-[0_-6px_16px_-8px_oklch(0.2_0.03_200/0.35),0_10px_24px_-10px_oklch(0.2_0.03_200/0.45)] ring-1 ring-white/10 transition-shadow duration-500 group-has-checked/c:shadow-[0_4px_10px_oklch(0.2_0.03_200/0.2),0_28px_50px_-18px_oklch(0.2_0.03_200/0.6)] has-[:focus-visible]:outline-3 has-[:focus-visible]:outline-offset-3 has-[:focus-visible]:outline-tac22-focus">
            <input type="radio" name="tac22-card" class="sr-only" aria-label="Meridian Rewards Mastercard ending 0937">
            <span aria-hidden="true" class="pointer-events-none absolute -bottom-24 -left-10 size-64 rounded-full border-[28px] border-white/6"></span>
            <span class="relative flex h-3 items-center justify-between text-[13px] font-semibold">
              <span class="tracking-[0.02em]">Meridian · Rewards</span>
              <span class="font-tac22-mono text-white/80">•• 0937</span>
            </span>
            <svg class="relative mt-10 h-8 w-11" viewBox="0 0 44 32" aria-hidden="true"><rect x="0.5" y="0.5" width="43" height="31" rx="6" fill="#e6d3a3"/><path d="M0 11h15M0 21h15M29 11h15M29 21h15M15 0v32M29 0v32" stroke="#b39b62" stroke-width="1.2"/></svg>
            <span class="relative mt-3 block font-tac22-mono text-[17px] tracking-[0.14em] text-white/95">•••• •••• •••• 0937</span>
            <span class="relative mt-2 flex items-end justify-between text-[11.5px] text-white/80">
              <span>ELENA MARCHETTI · 03/28</span>
              <svg class="h-6 w-10" viewBox="0 0 40 24" aria-hidden="true"><circle cx="14" cy="12" r="11" fill="#eb3b3b"/><circle cx="26" cy="12" r="11" fill="#f5a524" opacity="0.92"/></svg>
            </span>
          </label>
          <div class="invisible grid grid-rows-[0fr] opacity-0 transition-[grid-template-rows,opacity,visibility] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-checked/c:visible group-has-checked/c:grid-rows-[1fr] group-has-checked/c:opacity-100 motion-reduce:transition-none">
            <div class="min-h-0 overflow-hidden">
              <div class="mx-2 mt-3 rounded-2xl bg-tac22-sheet p-4 ring-1 ring-tac22-ink/6">
                <div class="grid grid-cols-2 gap-3 text-[13px]">
                  <div class="rounded-xl bg-white p-3 ring-1 ring-tac22-ink/6"><p class="text-tac22-mut">Points</p><p class="mt-0.5 text-lg font-extrabold">48,210</p></div>
                  <div class="rounded-xl bg-white p-3 ring-1 ring-tac22-ink/6"><p class="text-tac22-mut">Cash back</p><p class="mt-0.5 text-lg font-extrabold">$61.30</p></div>
                </div>
                <ul class="mt-3 divide-y divide-tac22-ink/6 text-[13.5px]">
                  <li class="flex justify-between py-2"><span>Whole Foods Market</span><span class="font-tac22-mono font-medium">−$72.18</span></li>
                  <li class="flex justify-between py-2"><span>Shell · Fuel</span><span class="font-tac22-mono font-medium">−$48.90</span></li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div class="group/c relative -mt-[8.75rem] rotate-[-0.8deg] transition-[margin,rotate,translate] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] not-has-checked:hover:-translate-y-1.5 has-checked:mt-5 has-checked:rotate-0 [:has(input:checked)+&]:mt-5 motion-reduce:transition-none">
          <label class="relative block h-[12.5rem] cursor-pointer overflow-hidden rounded-[22px] bg-tac22-c3a bg-linear-160 from-tac22-c3a to-tac22-c3b p-5 text-white shadow-[0_-6px_16px_-8px_oklch(0.3_0.08_40/0.35),0_10px_24px_-10px_oklch(0.3_0.08_40/0.45)] ring-1 ring-white/10 transition-shadow duration-500 group-has-checked/c:shadow-[0_4px_10px_oklch(0.3_0.08_40/0.2),0_28px_50px_-18px_oklch(0.3_0.08_40/0.6)] has-[:focus-visible]:outline-3 has-[:focus-visible]:outline-offset-3 has-[:focus-visible]:outline-tac22-focus">
            <input type="radio" name="tac22-card" class="sr-only" aria-label="Northwind Air boarding pass, San Francisco to New York">
            <span class="relative flex h-3 items-center justify-between text-[13px] font-semibold">
              <span class="tracking-[0.02em]">Northwind Air · Boarding pass</span>
              <span class="font-tac22-mono text-white/85">NW 218</span>
            </span>
            <span class="relative mt-9 grid grid-cols-[auto_1fr_auto] items-center gap-3">
              <span><span class="block text-[34px] leading-none font-extrabold tracking-[-0.03em]">SFO</span><span class="mt-1 block text-[11.5px] text-white/85">San Francisco</span></span>
              <span aria-hidden="true" class="h-0 border-t-[1.5px] border-dashed border-white/70"></span>
              <span class="text-right"><span class="block text-[34px] leading-none font-extrabold tracking-[-0.03em]">JFK</span><span class="mt-1 block text-[11.5px] text-white/85">New York</span></span>
            </span>
            <span class="relative mt-5 flex justify-between font-tac22-mono text-[12px] text-white/90"><span>Thu 16 Oct</span><span>Boards 07:35</span></span>
          </label>
          <div class="invisible grid grid-rows-[0fr] opacity-0 transition-[grid-template-rows,opacity,visibility] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-checked/c:visible group-has-checked/c:grid-rows-[1fr] group-has-checked/c:opacity-100 motion-reduce:transition-none">
            <div class="min-h-0 overflow-hidden">
              <div class="mx-2 mt-3 rounded-2xl bg-tac22-sheet p-4 ring-1 ring-tac22-ink/6">
                <dl class="grid grid-cols-3 gap-3 text-center">
                  <div class="rounded-xl bg-white py-2.5 ring-1 ring-tac22-ink/6"><dt class="text-[11.5px] text-tac22-mut">Gate</dt><dd class="text-lg font-extrabold">B14</dd></div>
                  <div class="rounded-xl bg-white py-2.5 ring-1 ring-tac22-ink/6"><dt class="text-[11.5px] text-tac22-mut">Seat</dt><dd class="text-lg font-extrabold">22A</dd></div>
                  <div class="rounded-xl bg-white py-2.5 ring-1 ring-tac22-ink/6"><dt class="text-[11.5px] text-tac22-mut">Group</dt><dd class="text-lg font-extrabold">3</dd></div>
                </dl>
                <div aria-hidden="true" class="mt-3 h-12 rounded-lg bg-[repeating-linear-gradient(90deg,var(--color-tac22-ink)_0_2px,transparent_2px_4px,var(--color-tac22-ink)_4px_5px,transparent_5px_8px,var(--color-tac22-ink)_8px_11px,transparent_11px_12px)] opacity-85"></div>
                <p class="mt-2 text-center font-tac22-mono text-[11.5px] text-tac22-mut">Confirmation K7QX2M · Economy Plus</p>
              </div>
            </div>
          </div>
        </div>

        <div class="group/c relative -mt-[8.75rem] rotate-[1.2deg] transition-[margin,rotate,translate] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] not-has-checked:hover:-translate-y-1.5 has-checked:mt-5 has-checked:rotate-0 [:has(input:checked)+&]:mt-5 motion-reduce:transition-none">
          <label class="relative block h-[12.5rem] cursor-pointer overflow-hidden rounded-[22px] bg-tac22-c4a p-5 text-tac22-c4ink shadow-[0_-6px_16px_-8px_oklch(0.3_0.04_60/0.3),0_10px_24px_-10px_oklch(0.3_0.04_60/0.4)] ring-1 ring-tac22-c4ink/10 transition-shadow duration-500 group-has-checked/c:shadow-[0_4px_10px_oklch(0.3_0.04_60/0.15),0_28px_50px_-18px_oklch(0.3_0.04_60/0.5)] has-[:focus-visible]:outline-3 has-[:focus-visible]:outline-offset-3 has-[:focus-visible]:outline-tac22-focus">
            <input type="radio" name="tac22-card" class="sr-only" aria-label="Kiln Coffee loyalty card, 7 of 10 stamps">
            <span aria-hidden="true" class="pointer-events-none absolute -right-8 -bottom-10 size-40 rounded-full bg-tac22-c4b"></span>
            <span class="relative flex h-3 items-center justify-between text-[13px] font-semibold">
              <span class="tracking-[0.02em]">Kiln Coffee · Loyalty</span>
              <span class="font-tac22-mono">7 / 10</span>
            </span>
            <span class="relative mt-10 block text-[28px] leading-[1.05] font-extrabold tracking-[-0.03em]">Three more cups<br>and the next is ours.</span>
            <span class="relative mt-4 flex gap-1.5" aria-hidden="true">
              <span class="size-3.5 rounded-full bg-tac22-c4ink"></span><span class="size-3.5 rounded-full bg-tac22-c4ink"></span><span class="size-3.5 rounded-full bg-tac22-c4ink"></span><span class="size-3.5 rounded-full bg-tac22-c4ink"></span><span class="size-3.5 rounded-full bg-tac22-c4ink"></span><span class="size-3.5 rounded-full bg-tac22-c4ink"></span><span class="size-3.5 rounded-full bg-tac22-c4ink"></span><span class="size-3.5 rounded-full ring-[1.5px] ring-tac22-c4ink ring-inset"></span><span class="size-3.5 rounded-full ring-[1.5px] ring-tac22-c4ink ring-inset"></span><span class="size-3.5 rounded-full ring-[1.5px] ring-tac22-c4ink ring-inset"></span>
            </span>
          </label>
          <div class="invisible grid grid-rows-[0fr] opacity-0 transition-[grid-template-rows,opacity,visibility] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-checked/c:visible group-has-checked/c:grid-rows-[1fr] group-has-checked/c:opacity-100 motion-reduce:transition-none">
            <div class="min-h-0 overflow-hidden">
              <div class="mx-2 mt-3 rounded-2xl bg-tac22-sheet p-4 text-[13.5px] ring-1 ring-tac22-ink/6">
                <p class="leading-relaxed text-tac22-soft">Show this card at any Kiln location. Stamps expire 12 months after your first visit; oat milk is always free for members.</p>
                <p class="mt-3 flex justify-between"><span class="text-tac22-mut">Nearest store</span><span class="font-semibold">Hayes Valley · 0.4 mi</span></p>
              </div>
            </div>
          </div>
        </div>
      </fieldset>
    </article>
    <p aria-hidden="true" class="max-w-full rounded-full border border-tac22-ink/10 bg-white px-3.5 py-2 text-center font-tac22-mono text-[11.5px] text-tac22-mut">-mt-[8.75rem] · has-checked:mt-5 · [:has(input:checked)+&amp;]:mt-5</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac22-bg: #eeebe6;
  --color-tac22-bg: oklch(0.94 0.008 80);
  --color-tac22-glow: #fffdf9;
  --color-tac22-glow: oklch(0.995 0.005 80);
  --color-tac22-sheet: #f7f5f1;
  --color-tac22-sheet: oklch(0.97 0.006 80);
  --color-tac22-ink: #1c1b1f;
  --color-tac22-ink: oklch(0.22 0.008 290);
  --color-tac22-soft: #45434b;
  --color-tac22-soft: oklch(0.4 0.012 290);
  --color-tac22-mut: #5f5c66;
  --color-tac22-mut: oklch(0.49 0.015 290);
  --color-tac22-ok: #1fa86a;
  --color-tac22-ok: oklch(0.64 0.15 155);
  --color-tac22-ok-ink: #0f7146;
  --color-tac22-ok-ink: oklch(0.48 0.11 155);
  --color-tac22-focus: #3b6cf6;
  --color-tac22-focus: oklch(0.57 0.21 265);
  --color-tac22-c1a: #1d1f2a;
  --color-tac22-c1a: oklch(0.24 0.02 275);
  --color-tac22-c1b: #3f3a63;
  --color-tac22-c1b: oklch(0.38 0.07 290);
  --color-tac22-c2a: #0d4f4c;
  --color-tac22-c2a: oklch(0.4 0.07 190);
  --color-tac22-c2b: #0f2e3d;
  --color-tac22-c2b: oklch(0.29 0.05 225);
  --color-tac22-c3a: #c2410c;
  --color-tac22-c3a: oklch(0.55 0.18 40);
  --color-tac22-c3b: #8c2a1a;
  --color-tac22-c3b: oklch(0.42 0.14 32);
  --color-tac22-c4a: #f0dcc0;
  --color-tac22-c4a: oklch(0.9 0.045 75);
  --color-tac22-c4b: #e5c79c;
  --color-tac22-c4b: oklch(0.84 0.07 75);
  --color-tac22-c4ink: #4a2a14;
  --color-tac22-c4ink: oklch(0.33 0.06 55);
  --font-tac22-sans: 'Manrope', system-ui, sans-serif;
  --font-tac22-mono: 'IBM Plex Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-22 {
  width: 100%;
  min-height: 100svh;
}
```
