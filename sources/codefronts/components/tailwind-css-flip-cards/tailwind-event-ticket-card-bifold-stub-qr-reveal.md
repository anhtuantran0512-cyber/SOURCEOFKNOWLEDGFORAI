---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-event-ticket-card-bifold-stub-qr-reveal/"
title: "Tailwind Event Ticket Card with Bi-Fold Stub Reveal & QR Panel"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A concert ticket that bi-folds: the left half turns around its right edge, the stub turns around its left, and the two backs meet in the middle."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Event Ticket Card with Bi-Fold Stub Reveal & QR Panel
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-event-ticket-card-bifold-stub-qr-reveal/

A concert ticket that bi-folds: the left half turns around its right edge, the stub turns around its left, and the two backs meet in the middle. The whole trick is a shared perspective on one ancestor &mdash; two halves in one vanishing-point space &mdash; which is exactly the mistake the original's gotcha list warns about and which the utility version makes structurally obvious.
## HTML
```html
<section class="tfc-22 w-full min-h-svh grid place-items-center content-center gap-7 bg-tfc22-bg font-tfc22-sans px-5 py-10 text-tfc22-ink">
  <div class="group relative mx-auto h-[210px] w-[430px] max-w-full [perspective:1400px] [perspective-origin:50%_50%] rounded-xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc22-orange has-[:focus-visible]:outline-offset-4">
    <input id="tfc-22-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-22-flip" class="absolute inset-0 z-20 cursor-pointer rounded-xl"><span class="sr-only">Unfold the ticket to see its details and barcode</span></label>

    <div class="relative flex h-full w-full">

      <div class="relative h-full w-1/2 origin-right transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(-180deg)] group-has-checked:[transform:rotateY(-180deg)] group-has-[:focus-visible]:[transform:rotateY(-180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col justify-center gap-2 rounded-l-xl border border-r-0 border-tfc22-orange/25 bg-linear-160 from-tfc22-p1 to-tfc22-p2 py-5 pr-5 pl-6 [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.18em] text-tfc22-orange">Live concert &middot; 2025</p>
          <h2 class="text-[19px] font-black leading-[1.15] text-white">Neon Pulse<br>World Tour</h2>
          <p class="text-[11px] text-tfc22-muted">The Meridian Arena &middot; San Francisco</p>
          <p class="mt-1 flex items-center gap-1.5 text-[11px] text-tfc22-muted">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="shrink-0 opacity-70" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            Sat, Nov 29 &middot; 8:00 PM
          </p>
          <p class="flex items-center gap-1.5 text-[11px] text-tfc22-muted">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="shrink-0 opacity-70" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            Floor &middot; general admission
          </p>
        </div>
        <div class="absolute inset-0 flex flex-col justify-center gap-2 rounded-l-xl border-r border-dashed border-tfc22-sky/30 bg-linear-160 from-tfc22-b1 to-tfc22-b2 py-5 pr-4.5 pl-6 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.18em] text-tfc22-sky">Ticket details</p>
          <h3 class="text-[17px] font-black leading-tight text-white">Neon Pulse &middot; SF</h3>
          <dl class="mt-1 grid grid-cols-2 gap-2">
            <div class="rounded-lg border border-white/7 bg-white/4 px-2.5 py-2"><dt class="mb-0.5 text-[9px] uppercase tracking-[0.1em] text-tfc22-dim">Date</dt><dd class="text-[13px] font-bold text-white">Nov 29</dd></div>
            <div class="rounded-lg border border-white/7 bg-white/4 px-2.5 py-2"><dt class="mb-0.5 text-[9px] uppercase tracking-[0.1em] text-tfc22-dim">Doors</dt><dd class="text-[13px] font-bold text-tfc22-sky">6:30 PM</dd></div>
            <div class="rounded-lg border border-white/7 bg-white/4 px-2.5 py-2"><dt class="mb-0.5 text-[9px] uppercase tracking-[0.1em] text-tfc22-dim">Zone</dt><dd class="text-[13px] font-bold text-white">Floor A</dd></div>
            <div class="rounded-lg border border-white/7 bg-white/4 px-2.5 py-2"><dt class="mb-0.5 text-[9px] uppercase tracking-[0.1em] text-tfc22-dim">Price</dt><dd class="text-[13px] font-bold text-tfc22-sky">$149</dd></div>
          </dl>
        </div>
      </div>

      <div class="relative h-full w-1/2 origin-left transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div aria-hidden="true" class="pointer-events-none absolute inset-y-0 -left-px z-5 flex flex-col justify-between py-2.5">
          <span class="-ml-[5px] size-2.5 rounded-full border border-tfc22-orange/20 bg-tfc22-bg"></span>
          <span class="-ml-[5px] size-2.5 rounded-full border border-tfc22-orange/20 bg-tfc22-bg"></span>
          <span class="-ml-[5px] size-2.5 rounded-full border border-tfc22-orange/20 bg-tfc22-bg"></span>
          <span class="-ml-[5px] size-2.5 rounded-full border border-tfc22-orange/20 bg-tfc22-bg"></span>
          <span class="-ml-[5px] size-2.5 rounded-full border border-tfc22-orange/20 bg-tfc22-bg"></span>
        </div>
        <div class="absolute inset-0 flex flex-col items-center justify-center gap-2.5 rounded-r-xl border border-l border-dashed border-tfc22-orange/30 bg-linear-160 from-tfc22-p2 to-tfc22-p3 p-4 [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span class="grid size-17 place-items-center rounded-lg bg-white p-1.5">
            <svg viewBox="0 0 17 17" width="56" height="56" fill="black" aria-hidden="true">
              <rect x="0" y="0" width="5" height="5" fill="none" stroke="black" stroke-width=".8"/><rect x="1.5" y="1.5" width="2" height="2"/>
              <rect x="12" y="0" width="5" height="5" fill="none" stroke="black" stroke-width=".8"/><rect x="13.5" y="1.5" width="2" height="2"/>
              <rect x="0" y="12" width="5" height="5" fill="none" stroke="black" stroke-width=".8"/><rect x="1.5" y="13.5" width="2" height="2"/>
              <rect x="6" y="0" width="1" height="1"/><rect x="7" y="1" width="1" height="1"/><rect x="9" y="0" width="1" height="1"/><rect x="10" y="1" width="1" height="1"/>
              <rect x="6" y="2" width="2" height="1"/><rect x="9" y="3" width="1" height="1"/>
              <rect x="6" y="6" width="1" height="1"/><rect x="8" y="6" width="1" height="1"/><rect x="10" y="6" width="1" height="1"/>
              <rect x="7" y="7" width="2" height="1"/><rect x="11" y="7" width="1" height="1"/>
              <rect x="6" y="8" width="1" height="1"/><rect x="9" y="8" width="1" height="1"/><rect x="12" y="8" width="1" height="1"/>
              <rect x="6" y="10" width="2" height="1"/><rect x="10" y="10" width="1" height="1"/>
              <rect x="7" y="12" width="1" height="1"/><rect x="9" y="12" width="1" height="1"/><rect x="11" y="12" width="1" height="1"/>
              <rect x="6" y="13" width="1" height="1"/><rect x="10" y="13" width="2" height="1"/>
              <rect x="6" y="15" width="1" height="1"/><rect x="8" y="15" width="1" height="1"/><rect x="11" y="15" width="1" height="1"/>
              <rect x="12" y="6" width="5" height="5" fill="none" stroke="black" stroke-width=".8"/><rect x="13.5" y="7.5" width="2" height="2"/>
            </svg>
          </span>
          <p class="text-center text-[22px] font-black leading-none text-tfc22-amber">B14</p>
          <p class="text-[9px] uppercase tracking-[0.1em] text-tfc22-dim">Seat</p>
          <p class="text-center text-[9px] uppercase tracking-[0.14em] text-tfc22-dim">Scan at entry</p>
        </div>
        <div class="absolute inset-0 flex flex-col items-center justify-center gap-2 rounded-r-xl bg-linear-160 from-tfc22-b2 to-tfc22-b3 p-4 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="flex h-13 items-end gap-0.5">
            <span class="w-0.5 rounded-px bg-tfc22-ink" style="height:52px"></span><span class="w-[3px] rounded-px bg-tfc22-ink" style="height:40px"></span><span class="w-0.5 rounded-px bg-tfc22-ink" style="height:52px"></span><span class="w-px rounded-px bg-tfc22-ink" style="height:32px"></span><span class="w-[3px] rounded-px bg-tfc22-ink" style="height:48px"></span><span class="w-0.5 rounded-px bg-tfc22-ink" style="height:44px"></span><span class="w-px rounded-px bg-tfc22-ink" style="height:52px"></span><span class="w-0.5 rounded-px bg-tfc22-ink" style="height:36px"></span><span class="w-[3px] rounded-px bg-tfc22-ink" style="height:52px"></span><span class="w-px rounded-px bg-tfc22-ink" style="height:44px"></span><span class="w-0.5 rounded-px bg-tfc22-ink" style="height:40px"></span><span class="w-[3px] rounded-px bg-tfc22-ink" style="height:52px"></span><span class="w-px rounded-px bg-tfc22-ink" style="height:34px"></span><span class="w-0.5 rounded-px bg-tfc22-ink" style="height:48px"></span>
          </span>
          <p class="font-tfc22-mono text-[9px] tracking-[0.08em] text-tfc22-dim">4829-1104-B14</p>
          <p class="text-[28px] font-black leading-none text-tfc22-sky">B14</p>
          <p class="text-[9px] uppercase tracking-[0.12em] text-tfc22-dim">Confirmed seat</p>
          <p class="flex items-center gap-1.5 rounded-full border border-tfc22-sky/25 bg-tfc22-sky/10 px-2.5 py-1 text-[10px] font-bold text-tfc22-sky"><span class="size-1.5 rounded-full bg-tfc22-sky"></span>Valid entry</p>
        </div>
      </div>

      <span aria-hidden="true" class="pointer-events-none absolute inset-y-0 left-1/2 z-10 w-0.5 -translate-x-1/2 bg-linear-180 from-transparent via-tfc22-orange/25 to-transparent"></span>
    </div>
  </div>
  <p class="text-center text-[10px] uppercase tracking-[0.15em] text-tfc22-dim">Hover, tap or press Space to unfold</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc22-bg: #07080f;
  --color-tfc22-bg: oklch(0.13 0.015 275);
  --color-tfc22-p1: #1e1000;
  --color-tfc22-p1: oklch(0.2 0.05 65);
  --color-tfc22-p2: #120900;
  --color-tfc22-p2: oklch(0.16 0.035 65);
  --color-tfc22-p3: #0d0700;
  --color-tfc22-p3: oklch(0.14 0.03 65);
  --color-tfc22-b1: #0a1a28;
  --color-tfc22-b1: oklch(0.2 0.04 240);
  --color-tfc22-b2: #061020;
  --color-tfc22-b2: oklch(0.15 0.03 250);
  --color-tfc22-b3: #04090f;
  --color-tfc22-b3: oklch(0.12 0.02 250);
  --color-tfc22-orange: #f97316;
  --color-tfc22-orange: oklch(0.7 0.19 45);
  --color-tfc22-amber: #fbbf24;
  --color-tfc22-amber: oklch(0.83 0.16 82);
  --color-tfc22-sky: #38bdf8;
  --color-tfc22-sky: oklch(0.76 0.13 230);
  --color-tfc22-ink: #fff7ed;
  --color-tfc22-ink: oklch(0.98 0.015 70);
  --color-tfc22-muted: #bfb0a0;
  --color-tfc22-muted: oklch(0.78 0.025 70);
  --color-tfc22-dim: #948878;
  --color-tfc22-dim: oklch(0.64 0.02 70);
  --font-tfc22-sans: 'Sora', system-ui, sans-serif;
  --font-tfc22-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfc-22 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-22 * {
    transition-duration: 1ms !important;
  }
}
```
