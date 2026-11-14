---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-leaderboard-card-gradient-medal-ranks/"
title: "Tailwind Leaderboard Card with Gradient Medal Ranks"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A live top-contributors board: gradient medal digits for the podium, tinted row washes, a streak flame, per-row rank deltas and a highlighted…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Leaderboard Card with Gradient Medal Ranks
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-leaderboard-card-gradient-medal-ranks/

A live top-contributors board: gradient medal digits for the podium, tinted row washes, a streak flame, per-row rank deltas and a highlighted &ldquo;you&rdquo; row. The port's win is the forced-colors: variant &mdash; the gradient-text ranks now survive Windows high-contrast mode instead of vanishing, and the fallback is one utility beside the gradient.
## HTML
```html
<section class="twc-10 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc10-bg [background-image:radial-gradient(ellipse_at_20%_15%,oklch(0.82_0.16_80/0.06),transparent_45%),radial-gradient(ellipse_at_80%_85%,oklch(0.68_0.2_350/0.06),transparent_45%)] font-twc10-sans">

  <article class="relative isolate w-full max-w-[400px] overflow-hidden rounded-3xl bg-white border border-black/5 px-5 pt-5 pb-3 shadow-[0_30px_60px_-30px_oklch(0.4_0.05_70/0.22),inset_0_0_0_1px_oklch(1_0_0/0.5)]">

    <div aria-hidden="true" class="absolute -top-20 -left-20 size-75 -z-10 pointer-events-none blur-[30px] [background:radial-gradient(circle,oklch(0.82_0.16_80/0.16)_0%,transparent_55%),radial-gradient(circle_at_60%_60%,oklch(0.68_0.2_350/0.11)_0%,transparent_55%)]"></div>

    <header class="relative z-1 flex items-start justify-between gap-3 mb-4">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <h3 class="m-0 text-base font-bold tracking-[-0.02em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">Top contributors</h3>
          <span class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-twc10-red/8 border border-twc10-red/20 font-twc10-mono text-[9px] font-bold tracking-[0.14em] text-twc10-red">
            <span aria-hidden="true" class="size-[5px] rounded-full bg-twc10-red animate-twc10-blink motion-reduce:animate-none"></span>
            LIVE
          </span>
        </div>
        <p class="inline-flex items-center gap-1 m-0 text-[11px] text-twc10-dim">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          Updated 12s ago &middot; resets Aug 1
        </p>
      </div>
      <div role="group" aria-label="Timeframe" class="inline-flex gap-0.5 p-[3px] rounded-full bg-twc10-track border border-black/4">
        <button type="button" aria-pressed="false" class="min-h-11 px-3 rounded-full border-0 cursor-pointer text-[11px] font-semibold bg-transparent text-twc10-muted transition-[color,background] duration-200 hover:text-twc10-ink focus-visible:outline-2 focus-visible:outline-twc10-gold focus-visible:outline-offset-2 motion-reduce:transition-none">Week</button>
        <button type="button" aria-pressed="true" class="min-h-11 px-3 rounded-full border-0 cursor-pointer text-[11px] font-semibold bg-white text-twc10-ink shadow-[0_2px_6px_oklch(0_0_0/0.08),0_0_0_1px_oklch(0_0_0/0.04)] transition-[color,background] duration-200 focus-visible:outline-2 focus-visible:outline-twc10-gold focus-visible:outline-offset-2 motion-reduce:transition-none">Month</button>
      </div>
    </header>

    <div aria-hidden="true" class="absolute top-17 inset-x-5 h-42 z-0 pointer-events-none">
      <div class="absolute top-0 w-full h-14 rounded-xl blur-[20px] [background:linear-gradient(90deg,oklch(0.82_0.16_80/0.2),transparent_70%)]"></div>
      <div class="absolute top-14 w-full h-14 rounded-xl blur-[20px] [background:linear-gradient(90deg,oklch(0.7_0.03_250/0.16),transparent_70%)]"></div>
      <div class="absolute top-28 w-full h-14 rounded-xl blur-[20px] [background:linear-gradient(90deg,oklch(0.55_0.17_42/0.16),transparent_70%)]"></div>
    </div>

    <ol role="list" class="relative z-1 flex flex-col gap-1 list-none m-0 mb-3 p-0">

      <li role="listitem" class="relative grid grid-cols-[32px_40px_1fr_auto] items-center gap-2.5 px-3 py-2.5 rounded-2xl border border-twc10-gold/22 [background-image:linear-gradient(90deg,oklch(0.82_0.16_80/0.14),oklch(0.82_0.16_80/0.03)_70%)] transition-[background,transform] duration-200 hover:translate-x-0.5 hover:[background-image:linear-gradient(90deg,oklch(0.82_0.16_80/0.2),oklch(0.82_0.16_80/0.05)_70%)] motion-reduce:transition-none motion-reduce:hover:translate-x-0">
        <div class="relative flex items-center justify-center w-8">
          <span class="text-lg font-extrabold tracking-[-0.03em] [font-variant-numeric:tabular-nums] [background-image:linear-gradient(135deg,#fde047_0%,#f59e0b_50%,#b45309_100%)] bg-clip-text text-transparent drop-shadow-[0_1px_1px_oklch(0.55_0.13_65/0.35)] forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">1</span>
          <span aria-hidden="true" class="absolute -top-1.5 -right-1 inline-flex items-center justify-center size-[15px] rounded-full border-[1.5px] border-white text-white [background:linear-gradient(135deg,#fde047_0%,#f59e0b_100%)] shadow-[0_2px_5px_oklch(0.78_0.15_70/0.45)]">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z"/></svg>
          </span>
        </div>
        <span class="relative flex items-center justify-center size-10 rounded-full border-2 border-white [background:linear-gradient(135deg,#f472b6,#ec4899)] text-white text-xs font-bold shadow-[0_0_0_1px_oklch(0_0_0/0.05),0_2px_6px_oklch(0_0_0/0.08)]">
          AK
          <span class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 inline-flex items-center gap-px pl-0.5 pr-1 py-px rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#fb923c,#dc2626)] text-white text-[8px] font-extrabold tracking-[0.02em] shadow-[0_2px_5px_oklch(0.58_0.22_25/0.35)]">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2s-4 4-4 8a4 4 0 0 0 8 0c0-1-1-2-1-2s2 2 2 5a5 5 0 0 1-10 0c0-6 5-11 5-11z"/></svg>
            12<span class="sr-only"> day streak</span>
          </span>
        </span>
        <div class="flex flex-col gap-px min-w-0">
          <span title="Ada Karim" class="text-[13px] font-bold text-twc10-ink truncate">Ada Karim</span>
          <span class="text-[11px] text-twc10-muted truncate">Core maintainer &middot; <span class="px-1 rounded-[3px] font-twc10-mono text-[10px] font-bold text-twc10-greenink bg-twc10-green/15">&#9650; 2<span class="sr-only"> up 2 places</span></span></span>
        </div>
        <div class="flex flex-col items-end gap-px">
          <span class="text-sm font-extrabold tracking-[-0.02em] text-twc10-ink [font-variant-numeric:tabular-nums]">4,820</span>
          <span class="font-twc10-mono text-[9.5px] font-bold text-twc10-greenink">+287</span>
        </div>
      </li>

      <li role="listitem" class="relative grid grid-cols-[32px_40px_1fr_auto] items-center gap-2.5 px-3 py-2.5 rounded-2xl border border-twc10-silver/20 [background-image:linear-gradient(90deg,oklch(0.7_0.03_250/0.12),oklch(0.7_0.03_250/0.02)_70%)] transition-[background,transform] duration-200 hover:translate-x-0.5 hover:[background-image:linear-gradient(90deg,oklch(0.7_0.03_250/0.16),oklch(0.7_0.03_250/0.03)_70%)] motion-reduce:transition-none motion-reduce:hover:translate-x-0">
        <div class="flex items-center justify-center w-8">
          <span class="text-lg font-extrabold tracking-[-0.03em] [font-variant-numeric:tabular-nums] [background-image:linear-gradient(135deg,#e2e8f0_0%,#94a3b8_60%,#64748b_100%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">2</span>
        </div>
        <span class="flex items-center justify-center size-10 rounded-full border-2 border-white [background:linear-gradient(135deg,#60a5fa,#3b82f6)] text-white text-xs font-bold shadow-[0_0_0_1px_oklch(0_0_0/0.05),0_2px_6px_oklch(0_0_0/0.08)]">MO</span>
        <div class="flex flex-col gap-px min-w-0">
          <span title="Miguel Ortiz" class="text-[13px] font-bold text-twc10-ink truncate">Miguel Ortiz</span>
          <span class="text-[11px] text-twc10-muted truncate">Docs lead &middot; <span class="px-1 rounded-[3px] font-twc10-mono text-[10px] font-bold text-twc10-red bg-twc10-red/10">&#9660; 1<span class="sr-only"> down 1 place</span></span></span>
        </div>
        <div class="flex flex-col items-end gap-px">
          <span class="text-sm font-extrabold tracking-[-0.02em] text-twc10-ink [font-variant-numeric:tabular-nums]">3,915</span>
          <span class="font-twc10-mono text-[9.5px] font-bold text-twc10-greenink">+142</span>
        </div>
      </li>

      <li role="listitem" class="relative grid grid-cols-[32px_40px_1fr_auto] items-center gap-2.5 px-3 py-2.5 rounded-2xl border border-twc10-bronze/18 [background-image:linear-gradient(90deg,oklch(0.55_0.17_42/0.12),oklch(0.55_0.17_42/0.02)_70%)] transition-[background,transform] duration-200 hover:translate-x-0.5 hover:[background-image:linear-gradient(90deg,oklch(0.55_0.17_42/0.16),oklch(0.55_0.17_42/0.03)_70%)] motion-reduce:transition-none motion-reduce:hover:translate-x-0">
        <div class="flex items-center justify-center w-8">
          <span class="text-lg font-extrabold tracking-[-0.03em] [font-variant-numeric:tabular-nums] [background-image:linear-gradient(135deg,#fdba74_0%,#ea580c_60%,#9a3412_100%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">3</span>
        </div>
        <span class="flex items-center justify-center size-10 rounded-full border-2 border-white [background:linear-gradient(135deg,#34d399,#10b981)] text-white text-xs font-bold shadow-[0_0_0_1px_oklch(0_0_0/0.05),0_2px_6px_oklch(0_0_0/0.08)]">SN</span>
        <div class="flex flex-col gap-px min-w-0">
          <span title="Sana Novak" class="text-[13px] font-bold text-twc10-ink truncate">Sana Novak</span>
          <span class="text-[11px] text-twc10-muted truncate">Frontend &middot; <span class="px-1 rounded-[3px] font-twc10-mono text-[10px] font-bold text-twc10-greenink bg-twc10-green/15">&#9650; 4<span class="sr-only"> up 4 places</span></span></span>
        </div>
        <div class="flex flex-col items-end gap-px">
          <span class="text-sm font-extrabold tracking-[-0.02em] text-twc10-ink [font-variant-numeric:tabular-nums]">3,204</span>
          <span class="font-twc10-mono text-[9.5px] font-bold text-twc10-greenink">+412</span>
        </div>
      </li>

      <li role="listitem" class="relative grid grid-cols-[32px_40px_1fr_auto] items-center gap-2.5 px-3 py-2.5 rounded-2xl border border-transparent transition-[background,transform] duration-200 hover:translate-x-0.5 hover:bg-black/2 motion-reduce:transition-none motion-reduce:hover:translate-x-0">
        <div class="flex items-center justify-center w-8">
          <span class="text-lg font-extrabold tracking-[-0.03em] text-twc10-hair [font-variant-numeric:tabular-nums]">4</span>
        </div>
        <span class="flex items-center justify-center size-10 rounded-full border-2 border-white [background:linear-gradient(135deg,#a78bfa,#7c3aed)] text-white text-xs font-bold shadow-[0_0_0_1px_oklch(0_0_0/0.05),0_2px_6px_oklch(0_0_0/0.08)]">RT</span>
        <div class="flex flex-col gap-px min-w-0">
          <span title="Ren Tanaka" class="text-[13px] font-bold text-twc10-ink truncate">Ren Tanaka</span>
          <span class="text-[11px] text-twc10-muted truncate">Infra &middot; <span class="px-1 rounded-[3px] font-twc10-mono text-[10px] font-bold text-twc10-dim bg-twc10-silver/18">&mdash; 0<span class="sr-only"> unchanged</span></span></span>
        </div>
        <div class="flex flex-col items-end gap-px">
          <span class="text-sm font-extrabold tracking-[-0.02em] text-twc10-ink [font-variant-numeric:tabular-nums]">2,671</span>
          <span class="font-twc10-mono text-[9.5px] font-bold text-twc10-greenink">+94</span>
        </div>
      </li>

      <li role="listitem" aria-current="true" class="relative grid grid-cols-[32px_40px_1fr_auto] items-center gap-2.5 px-3 py-2.5 rounded-2xl border border-twc10-indigo/20 [background-image:linear-gradient(90deg,oklch(0.55_0.2_275/0.1),transparent_70%)] transition-[background,transform] duration-200 hover:translate-x-0.5 hover:[background-image:linear-gradient(90deg,oklch(0.55_0.2_275/0.14),transparent_70%)] motion-reduce:transition-none motion-reduce:hover:translate-x-0">
        <div class="flex items-center justify-center w-8">
          <span class="text-lg font-extrabold tracking-[-0.03em] text-twc10-hair [font-variant-numeric:tabular-nums]">5</span>
        </div>
        <span class="flex items-center justify-center size-10 rounded-full border-2 border-white [background:linear-gradient(135deg,#fb923c,#f97316)] text-white text-xs font-bold shadow-[0_0_0_1px_oklch(0_0_0/0.05),0_2px_6px_oklch(0_0_0/0.08)]">LF</span>
        <div class="flex flex-col gap-px min-w-0">
          <span class="inline-flex items-center gap-1.5 text-[13px] font-bold text-twc10-ink truncate">
            <span title="Lena Fjord" class="truncate">Lena Fjord</span>
            <span class="inline-block flex-none px-1.5 py-px rounded bg-twc10-indigo/16 text-twc10-indigoink text-[8.5px] font-extrabold tracking-[0.06em]">You</span>
          </span>
          <span class="text-[11px] text-twc10-muted truncate">Design &middot; <span class="px-1 rounded-[3px] font-twc10-mono text-[10px] font-bold text-twc10-greenink bg-twc10-green/15">&#9650; 7<span class="sr-only"> up 7 places</span></span></span>
        </div>
        <div class="flex flex-col items-end gap-px">
          <span class="text-sm font-extrabold tracking-[-0.02em] text-twc10-ink [font-variant-numeric:tabular-nums]">2,140</span>
          <span class="font-twc10-mono text-[9.5px] font-bold text-twc10-greenink">+521</span>
        </div>
      </li>
    </ol>

    <footer class="relative z-1 flex items-center justify-between gap-2 pt-2.5 border-t border-dashed border-black/8">
      <p class="inline-flex items-center gap-1.5 m-0 text-[11.5px] text-twc10-ink2">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="flex-none text-twc10-red drop-shadow-[0_2px_3px_oklch(0.58_0.22_25/0.35)]"><path d="M12 2s-4 4-4 8a4 4 0 0 0 8 0c0-1-1-2-1-2s2 2 2 5a5 5 0 0 1-10 0c0-6 5-11 5-11z"/></svg>
        You're climbing fast &mdash; <strong class="font-bold text-twc10-indigoink">682</strong> to reach rank 4
      </p>
      <a href="#full" class="inline-flex flex-none items-center gap-1 min-h-11 px-2 rounded-md no-underline text-[11.5px] font-bold text-twc10-indigoink transition-[color,background] duration-200 hover:text-twc10-indigodark hover:bg-twc10-indigo/6 focus-visible:outline-2 focus-visible:outline-twc10-gold focus-visible:outline-offset-2">
        See all
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </footer>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc10-bg: #faf9f5;
  --color-twc10-bg: oklch(0.98 0.006 90);
  --color-twc10-track: #f3f2ee;
  --color-twc10-track: oklch(0.95 0.005 90);
  --color-twc10-ink: #1a1a1a;
  --color-twc10-ink: oklch(0.21 0.005 270);
  --color-twc10-ink2: #4b4b57;
  --color-twc10-ink2: oklch(0.4 0.015 280);
  --color-twc10-muted: #6b6b7c;
  --color-twc10-muted: oklch(0.51 0.02 285);
  --color-twc10-dim: #9ca3af;
  --color-twc10-dim: oklch(0.71 0.02 265);
  --color-twc10-hair: #cbd5e1;
  --color-twc10-hair: oklch(0.85 0.02 250);
  --color-twc10-gold: #fbbf24;
  --color-twc10-gold: oklch(0.82 0.16 80);
  --color-twc10-silver: #94a3b8;
  --color-twc10-silver: oklch(0.7 0.03 250);
  --color-twc10-bronze: #c2410c;
  --color-twc10-bronze: oklch(0.55 0.17 42);
  --color-twc10-red: #dc2626;
  --color-twc10-red: oklch(0.58 0.22 25);
  --color-twc10-green: #34d399;
  --color-twc10-green: oklch(0.78 0.14 165);
  --color-twc10-greenink: #059669;
  --color-twc10-greenink: oklch(0.56 0.13 163);
  --color-twc10-indigo: #6366f1;
  --color-twc10-indigo: oklch(0.55 0.2 275);
  --color-twc10-indigoink: #4338ca;
  --color-twc10-indigoink: oklch(0.42 0.21 275);
  --color-twc10-indigodark: #312e81;
  --color-twc10-indigodark: oklch(0.32 0.15 275);
  --font-twc10-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc10-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc10-blink: twc10-blink 1.4s ease-in-out infinite;
}

@keyframes twc10-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.4;
    transform: scale(0.85);
  }
}

.twc-10 {
  width: 100%;
  min-height: 100svh;
}
```
