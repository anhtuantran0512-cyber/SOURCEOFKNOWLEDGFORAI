---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/skewed-tailwind-css-accordion-slanted-headers/"
title: "Skewed Tailwind CSS Accordion with Slanted Headers"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "Headers as racing stripes: every summary is a -skew-x-12 parallelogram with its label counter-skewed by skew-x-12 so the type stays upright, stacked in a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skewed Tailwind CSS Accordion with Slanted Headers
Source: https://codefronts.com/navigation/tailwind-css-accordions/skewed-tailwind-css-accordion-slanted-headers/

Headers as racing stripes: every summary is a -skew-x-12 parallelogram with its label counter-skewed by skew-x-12 so the type stays upright, stacked in a zigzag with alternating translate-x offsets. Opening a stripe squares it up (group-open:skew-x-0), floods it electric red and drops a hard offset shadow &mdash; the geometry itself is the state. An esports match-day guide on a dark speed-lined stage.
## HTML
```html
<section class="tac-15 w-full min-h-svh grid place-items-center bg-tac15-bg bg-[radial-gradient(60%_45%_at_85%_10%,var(--color-tac15-glow),transparent_70%),repeating-linear-gradient(115deg,transparent_0_46px,oklch(1_0_0/0.025)_46px_48px)] px-5 py-14 font-tac15-sans text-tac15-ink [interpolate-size:allow-keywords]" aria-label="Skewed slanted header accordion demo">
  <div class="grid w-full max-w-xl gap-9">
    <header class="grid gap-4 px-3">
      <p class="flex items-center gap-2.5 font-tac15-mono text-[12px] font-bold tracking-[0.2em] text-tac15-hot uppercase"><span aria-hidden="true" class="h-2.5 w-6 -skew-x-12 bg-tac15-red"></span>Grand final · Fan guide</p>
      <h2 class="text-[clamp(34px,7vw,52px)] leading-[0.95] font-black tracking-[-0.02em] uppercase italic [font-stretch:112%]">Match day,<br>no surprises.</h2>
      <div class="flex w-fit -skew-x-12 items-center gap-4 bg-tac15-panel px-4 py-2 ring-1 ring-white/10">
        <span class="flex skew-x-12 items-center gap-3 font-tac15-mono text-[12.5px] font-bold tracking-wide uppercase"><span>Nova</span><span class="text-tac15-hot">vs</span><span>Kraken</span><span aria-hidden="true" class="h-3.5 w-px bg-white/20"></span><span class="whitespace-nowrap text-tac15-mut">Sat · 19:00<span class="max-sm:hidden"> · Arena 9</span></span></span>
      </div>
    </header>

    <div class="grid gap-4 px-3">
      <details name="tac15-guide" class="group details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none" open>
        <summary class="block cursor-pointer list-none outline-none [&::-webkit-details-marker]:hidden [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-4 [&:focus-visible>span]:outline-white">
          <span class="block translate-x-3 -skew-x-12 border-l-4 border-tac15-red bg-tac15-panel shadow-[6px_6px_0_oklch(0_0_0/0.5)] ring-1 ring-white/8 transition-[transform,translate,background-color,box-shadow] duration-500 ease-[cubic-bezier(0.3,1.3,0.4,1)] hover:bg-tac15-panel2 group-open:translate-x-0 group-open:skew-x-0 group-open:bg-linear-to-r group-open:from-tac15-red group-open:to-tac15-red2 group-open:shadow-[0_6px_0_var(--color-tac15-deep)] motion-reduce:transition-none">
            <span class="flex min-h-14 skew-x-12 items-center gap-4 px-5 py-2 transition-transform duration-500 ease-[cubic-bezier(0.3,1.3,0.4,1)] group-open:skew-x-0 motion-reduce:transition-none">
              <span class="font-tac15-mono text-[13px] font-bold text-tac15-hot transition-colors group-open:text-white/75">01</span>
              <span class="flex-1 text-[17px] font-extrabold tracking-[0.04em] uppercase italic">Tickets &amp; entry</span>
              <svg aria-hidden="true" class="flex-none transition-transform duration-500 group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 20 20" width="20" height="20"><path d="M5 4l6 6-6 6M11 4l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/></svg>
            </span>
          </span>
        </summary>
        <div class="mt-3 grid gap-4 border-l-4 border-tac15-red/40 bg-tac15-panel/70 px-5 py-4">
          <p class="text-[14.5px] leading-relaxed text-tac15-mut">Digital tickets only. Add yours to your phone wallet before you reach the arena &mdash; signal drops once 18,000 fans are inside.</p>
          <dl class="grid grid-cols-3 gap-2 text-center">
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Gates</dt><dd class="mt-0.5 text-[17px] font-black italic">17:30</dd></div>
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Bag max</dt><dd class="mt-0.5 text-[17px] font-black italic">A4</dd></div>
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Re-entry</dt><dd class="mt-0.5 text-[17px] font-black italic">No</dd></div>
          </dl>
        </div>
      </details>

      <details name="tac15-guide" class="group details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
        <summary class="block cursor-pointer list-none outline-none [&::-webkit-details-marker]:hidden [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-4 [&:focus-visible>span]:outline-white">
          <span class="block -translate-x-3 -skew-x-12 border-l-4 border-tac15-red bg-tac15-panel shadow-[6px_6px_0_oklch(0_0_0/0.5)] ring-1 ring-white/8 transition-[transform,translate,background-color,box-shadow] duration-500 ease-[cubic-bezier(0.3,1.3,0.4,1)] hover:bg-tac15-panel2 group-open:translate-x-0 group-open:skew-x-0 group-open:bg-linear-to-r group-open:from-tac15-red group-open:to-tac15-red2 group-open:shadow-[0_6px_0_var(--color-tac15-deep)] motion-reduce:transition-none">
            <span class="flex min-h-14 skew-x-12 items-center gap-4 px-5 py-2 transition-transform duration-500 ease-[cubic-bezier(0.3,1.3,0.4,1)] group-open:skew-x-0 motion-reduce:transition-none">
              <span class="font-tac15-mono text-[13px] font-bold text-tac15-hot transition-colors group-open:text-white/75">02</span>
              <span class="flex-1 text-[17px] font-extrabold tracking-[0.04em] uppercase italic">Getting there</span>
              <svg aria-hidden="true" class="flex-none transition-transform duration-500 group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 20 20" width="20" height="20"><path d="M5 4l6 6-6 6M11 4l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/></svg>
            </span>
          </span>
        </summary>
        <div class="mt-3 grid gap-4 border-l-4 border-tac15-red/40 bg-tac15-panel/70 px-5 py-4">
          <p class="text-[14.5px] leading-relaxed text-tac15-mut">The Arena Line runs every 6 minutes from Central until 01:00. Riding in? Two thousand free, staffed bike racks wait at the north gate.</p>
          <dl class="grid grid-cols-3 gap-2 text-center">
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Metro</dt><dd class="mt-0.5 text-[17px] font-black italic">6 min</dd></div>
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Bikes</dt><dd class="mt-0.5 text-[17px] font-black italic">2,000</dd></div>
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Parking</dt><dd class="mt-0.5 text-[17px] font-black italic">P3</dd></div>
          </dl>
        </div>
      </details>

      <details name="tac15-guide" class="group details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
        <summary class="block cursor-pointer list-none outline-none [&::-webkit-details-marker]:hidden [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-4 [&:focus-visible>span]:outline-white">
          <span class="block translate-x-3 -skew-x-12 border-l-4 border-tac15-red bg-tac15-panel shadow-[6px_6px_0_oklch(0_0_0/0.5)] ring-1 ring-white/8 transition-[transform,translate,background-color,box-shadow] duration-500 ease-[cubic-bezier(0.3,1.3,0.4,1)] hover:bg-tac15-panel2 group-open:translate-x-0 group-open:skew-x-0 group-open:bg-linear-to-r group-open:from-tac15-red group-open:to-tac15-red2 group-open:shadow-[0_6px_0_var(--color-tac15-deep)] motion-reduce:transition-none">
            <span class="flex min-h-14 skew-x-12 items-center gap-4 px-5 py-2 transition-transform duration-500 ease-[cubic-bezier(0.3,1.3,0.4,1)] group-open:skew-x-0 motion-reduce:transition-none">
              <span class="font-tac15-mono text-[13px] font-bold text-tac15-hot transition-colors group-open:text-white/75">03</span>
              <span class="flex-1 text-[17px] font-extrabold tracking-[0.04em] uppercase italic">Food &amp; merch</span>
              <svg aria-hidden="true" class="flex-none transition-transform duration-500 group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 20 20" width="20" height="20"><path d="M5 4l6 6-6 6M11 4l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/></svg>
            </span>
          </span>
        </summary>
        <div class="mt-3 grid gap-4 border-l-4 border-tac15-red/40 bg-tac15-panel/70 px-5 py-4">
          <p class="text-[14.5px] leading-relaxed text-tac15-mut">Twelve local vendors line the main concourse. Team jerseys and the limited final-day hoodie sell out fast &mdash; the merch truck opens at 16:00.</p>
          <dl class="grid grid-cols-3 gap-2 text-center">
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Vendors</dt><dd class="mt-0.5 text-[17px] font-black italic">12</dd></div>
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Merch</dt><dd class="mt-0.5 text-[17px] font-black italic">16:00</dd></div>
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Cashless</dt><dd class="mt-0.5 text-[17px] font-black italic">Yes</dd></div>
          </dl>
        </div>
      </details>

      <details name="tac15-guide" class="group details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
        <summary class="block cursor-pointer list-none outline-none [&::-webkit-details-marker]:hidden [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-4 [&:focus-visible>span]:outline-white">
          <span class="block -translate-x-3 -skew-x-12 border-l-4 border-tac15-red bg-tac15-panel shadow-[6px_6px_0_oklch(0_0_0/0.5)] ring-1 ring-white/8 transition-[transform,translate,background-color,box-shadow] duration-500 ease-[cubic-bezier(0.3,1.3,0.4,1)] hover:bg-tac15-panel2 group-open:translate-x-0 group-open:skew-x-0 group-open:bg-linear-to-r group-open:from-tac15-red group-open:to-tac15-red2 group-open:shadow-[0_6px_0_var(--color-tac15-deep)] motion-reduce:transition-none">
            <span class="flex min-h-14 skew-x-12 items-center gap-4 px-5 py-2 transition-transform duration-500 ease-[cubic-bezier(0.3,1.3,0.4,1)] group-open:skew-x-0 motion-reduce:transition-none">
              <span class="font-tac15-mono text-[13px] font-bold text-tac15-hot transition-colors group-open:text-white/75">04</span>
              <span class="flex-1 text-[17px] font-extrabold tracking-[0.04em] uppercase italic">Accessibility</span>
              <svg aria-hidden="true" class="flex-none transition-transform duration-500 group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 20 20" width="20" height="20"><path d="M5 4l6 6-6 6M11 4l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/></svg>
            </span>
          </span>
        </summary>
        <div class="mt-3 grid gap-4 border-l-4 border-tac15-red/40 bg-tac15-panel/70 px-5 py-4">
          <p class="text-[14.5px] leading-relaxed text-tac15-mut">Step-free routes from every gate, sensory kits at guest services and live audio-described commentary on channel 3 of the arena app.</p>
          <dl class="grid grid-cols-3 gap-2 text-center">
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Step-free</dt><dd class="mt-0.5 text-[17px] font-black italic">All</dd></div>
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Quiet room</dt><dd class="mt-0.5 text-[17px] font-black italic">L2</dd></div>
            <div class="bg-white/5 px-2 py-2.5 ring-1 ring-white/8"><dt class="font-tac15-mono text-[10.5px] tracking-widest text-tac15-mut uppercase">Audio</dt><dd class="mt-0.5 text-[17px] font-black italic">Ch 3</dd></div>
          </dl>
        </div>
      </details>
    </div>

    <p aria-hidden="true" class="justify-self-center rounded-full px-3.5 py-2 text-center font-tac15-mono text-[11.5px] text-tac15-mut ring-1 ring-white/10">-skew-x-12 · skew-x-12 · group-open:skew-x-0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac15-bg: #100909;
  --color-tac15-bg: oklch(0.15 0.012 20);
  --color-tac15-glow: #a9000c59;
  --color-tac15-glow: oklch(0.45 0.2 25 / 0.35);
  --color-tac15-panel: #1e1616;
  --color-tac15-panel: oklch(0.21 0.014 20);
  --color-tac15-panel2: #291f1e;
  --color-tac15-panel2: oklch(0.25 0.016 20);
  --color-tac15-ink: #f8f4f4;
  --color-tac15-ink: oklch(0.97 0.005 20);
  --color-tac15-mut: #baadad;
  --color-tac15-mut: oklch(0.76 0.015 20);
  --color-tac15-red: #c5002b;
  --color-tac15-red: oklch(0.52 0.21 22);
  --color-tac15-red2: #d81327;
  --color-tac15-red2: oklch(0.56 0.22 25);
  --color-tac15-hot: #ff6a65;
  --color-tac15-hot: oklch(0.72 0.19 25);
  --color-tac15-deep: #800613;
  --color-tac15-deep: oklch(0.38 0.15 25);
  --font-tac15-sans: 'Archivo', system-ui, sans-serif;
  --font-tac15-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-15 {
  width: 100%;
  min-height: 100svh;
}
```
