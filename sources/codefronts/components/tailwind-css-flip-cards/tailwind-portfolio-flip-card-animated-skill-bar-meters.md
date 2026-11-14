---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-portfolio-flip-card-animated-skill-bar-meters/"
title: "Tailwind Portfolio Flip Card with Animated Skill Bar Proficiency Meters"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A case-study card whose back is a proficiency ledger: five labelled meters that fill as the card turns."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Portfolio Flip Card with Animated Skill Bar Proficiency Meters
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-portfolio-flip-card-animated-skill-bar-meters/

A case-study card whose back is a proficiency ledger: five labelled meters that fill as the card turns. The port fixes the original's quiet accessibility hole &mdash; a bar whose only value was an inline width percentage now carries role="progressbar" with real aria-valuenow, so the number is available to a screen reader and not just to sighted users.
## HTML
```html
<section class="tfc-05 w-full min-h-svh grid place-items-center bg-tfc05-bg font-tfc05-sans px-5 py-10 text-tfc05-ink">
  <div class="group relative w-[340px] h-[450px] [perspective:1200px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc05-orange has-[:focus-visible]:outline-offset-4">
    <input id="tfc-05-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-05-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show the tech stack and proficiency meters for Orbit Dashboard</span></label>

    <div class="relative w-full h-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden bg-tfc05-panel border border-tfc05-orange/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.55_0.18_45/0.35)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div class="relative h-50 shrink-0 overflow-hidden bg-linear-135 from-tfc05-stage to-tfc05-stage2 before:absolute before:inset-0 before:bg-[radial-gradient(circle_at_30%_40%,oklch(0.7_0.18_45/0.2),transparent_60%)]">
          <div class="absolute inset-5 grid grid-cols-2 grid-rows-2 gap-2">
            <div class="col-span-2 rounded-lg border border-white/7 bg-linear-135 from-tfc05-orange/12 to-tfc05-amber/6"></div>
            <div class="rounded-lg border border-white/7 bg-white/4"></div>
            <div class="rounded-lg border border-white/7 bg-white/4"></div>
          </div>
        </div>
        <div class="px-5 py-5">
          <p class="mb-1.5 font-tfc05-mono text-[10px] font-medium uppercase tracking-[0.15em] text-tfc05-orange">Case Study &middot; 2025</p>
          <h3 class="text-xl font-extrabold tracking-[-0.02em] text-white">Orbit Dashboard</h3>
          <p class="mt-1.5 text-xs leading-[1.65] text-tfc05-muted text-pretty">A real-time analytics platform with customisable widget grids and live WebSocket feeds.</p>
          <ul class="mt-3 flex flex-wrap gap-1.5">
            <li class="rounded-full border border-tfc05-orange/20 bg-tfc05-orange/10 px-2.5 py-0.5 text-[10px] tracking-[0.06em] text-tfc05-ink/70">React</li>
            <li class="rounded-full border border-tfc05-orange/20 bg-tfc05-orange/10 px-2.5 py-0.5 text-[10px] tracking-[0.06em] text-tfc05-ink/70">TypeScript</li>
            <li class="rounded-full border border-tfc05-orange/20 bg-tfc05-orange/10 px-2.5 py-0.5 text-[10px] tracking-[0.06em] text-tfc05-ink/70">D3.js</li>
          </ul>
        </div>
        <p class="mt-auto px-5 pb-4 text-[10px] tracking-[0.08em] text-tfc05-dim">Hover, tap or press Space for the stack &rarr;</p>
      </div>

      <div class="absolute inset-0 flex flex-col gap-3.5 rounded-2xl overflow-hidden p-7 bg-linear-160 from-tfc05-panel to-tfc05-back2 border border-tfc05-amber/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.6_0.15_70/0.3)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <h3 class="text-[11px] font-bold uppercase tracking-[0.15em] text-tfc05-amber">Tech Stack &amp; Proficiency</h3>
        <ul class="flex flex-1 flex-col gap-3">
          <li class="flex flex-col gap-1.5">
            <div class="flex items-center justify-between"><span id="tfc-05-s1" class="text-xs font-semibold text-tfc05-ink/80">React / Next.js</span><span class="font-tfc05-mono text-[11px] font-bold text-tfc05-orange">96%</span></div>
            <div role="progressbar" aria-labelledby="tfc-05-s1" aria-valuenow="96" aria-valuemin="0" aria-valuemax="100" class="h-1.5 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-0 rounded-full bg-linear-to-r from-tfc05-orange to-tfc05-amber transition-[width] duration-700 delay-300 ease-out group-hover:w-[96%] group-has-checked:w-[96%] group-has-[:focus-visible]:w-[96%] motion-reduce:transition-none"></span></div>
          </li>
          <li class="flex flex-col gap-1.5">
            <div class="flex items-center justify-between"><span id="tfc-05-s2" class="text-xs font-semibold text-tfc05-ink/80">TypeScript</span><span class="font-tfc05-mono text-[11px] font-bold text-tfc05-orange">92%</span></div>
            <div role="progressbar" aria-labelledby="tfc-05-s2" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" class="h-1.5 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-0 rounded-full bg-linear-to-r from-tfc05-orange to-tfc05-amber transition-[width] duration-700 delay-300 ease-out group-hover:w-[92%] group-has-checked:w-[92%] group-has-[:focus-visible]:w-[92%] motion-reduce:transition-none"></span></div>
          </li>
          <li class="flex flex-col gap-1.5">
            <div class="flex items-center justify-between"><span id="tfc-05-s3" class="text-xs font-semibold text-tfc05-ink/80">D3.js / Recharts</span><span class="font-tfc05-mono text-[11px] font-bold text-tfc05-orange">85%</span></div>
            <div role="progressbar" aria-labelledby="tfc-05-s3" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100" class="h-1.5 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-0 rounded-full bg-linear-to-r from-tfc05-orange to-tfc05-amber transition-[width] duration-700 delay-300 ease-out group-hover:w-[85%] group-has-checked:w-[85%] group-has-[:focus-visible]:w-[85%] motion-reduce:transition-none"></span></div>
          </li>
          <li class="flex flex-col gap-1.5">
            <div class="flex items-center justify-between"><span id="tfc-05-s4" class="text-xs font-semibold text-tfc05-ink/80">Node / WebSocket</span><span class="font-tfc05-mono text-[11px] font-bold text-tfc05-orange">88%</span></div>
            <div role="progressbar" aria-labelledby="tfc-05-s4" aria-valuenow="88" aria-valuemin="0" aria-valuemax="100" class="h-1.5 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-0 rounded-full bg-linear-to-r from-tfc05-orange to-tfc05-amber transition-[width] duration-700 delay-300 ease-out group-hover:w-[88%] group-has-checked:w-[88%] group-has-[:focus-visible]:w-[88%] motion-reduce:transition-none"></span></div>
          </li>
          <li class="flex flex-col gap-1.5">
            <div class="flex items-center justify-between"><span id="tfc-05-s5" class="text-xs font-semibold text-tfc05-ink/80">PostgreSQL</span><span class="font-tfc05-mono text-[11px] font-bold text-tfc05-orange">78%</span></div>
            <div role="progressbar" aria-labelledby="tfc-05-s5" aria-valuenow="78" aria-valuemin="0" aria-valuemax="100" class="h-1.5 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-0 rounded-full bg-linear-to-r from-tfc05-orange to-tfc05-amber transition-[width] duration-700 delay-300 ease-out group-hover:w-[78%] group-has-checked:w-[78%] group-has-[:focus-visible]:w-[78%] motion-reduce:transition-none"></span></div>
          </li>
        </ul>
        <a href="#" class="relative z-30 flex min-h-11 items-center justify-center rounded-xl bg-linear-135 from-tfc05-orange to-tfc05-amber text-[13px] font-extrabold tracking-[0.04em] text-black no-underline transition-opacity duration-150 hover:opacity-90 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">View Live Project &rarr;</a>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc05-bg: #0a0a0a;
  --color-tfc05-bg: oklch(0.14 0.005 60);
  --color-tfc05-panel: #111111;
  --color-tfc05-panel: oklch(0.17 0.004 60);
  --color-tfc05-back2: #1a1008;
  --color-tfc05-back2: oklch(0.2 0.03 60);
  --color-tfc05-stage: #1c0a00;
  --color-tfc05-stage: oklch(0.19 0.06 45);
  --color-tfc05-stage2: #0d1a2e;
  --color-tfc05-stage2: oklch(0.21 0.05 260);
  --color-tfc05-orange: #f97316;
  --color-tfc05-orange: oklch(0.7 0.19 45);
  --color-tfc05-amber: #fbbf24;
  --color-tfc05-amber: oklch(0.83 0.16 82);
  --color-tfc05-ink: #fef3e2;
  --color-tfc05-ink: oklch(0.97 0.02 75);
  --color-tfc05-muted: #bfae9a;
  --color-tfc05-muted: oklch(0.78 0.03 75);
  --color-tfc05-dim: #8a7d70;
  --color-tfc05-dim: oklch(0.62 0.02 75);
  --font-tfc05-sans: 'Sora', system-ui, sans-serif;
  --font-tfc05-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfc-05 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-05 * {
    transition-duration: 1ms !important;
  }
}
```
