---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-stacked-card-cascade-focus-within/"
title: "Tailwind Stacked Card Cascade with Focus-Within Fan-Out"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "Three project cards in a shallow deck: the top one lifts and the two behind fan wider on hover or keyboard focus, revealing their status chips and progress."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stacked Card Cascade with Focus-Within Fan-Out
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-stacked-card-cascade-focus-within/

Three project cards in a shallow deck: the top one lifts and the two behind fan wider on hover or keyboard focus, revealing their status chips and progress. The port's win is the touch branch &mdash; on a phone, where hover is sticky and traps the deck open, the cards ship already fanned.
## HTML
```html
<section class="twc-20 relative w-full min-h-svh flex items-center justify-center overflow-hidden px-5 py-25 bg-twc20-bg [background-image:radial-gradient(ellipse_at_20%_15%,oklch(0.55_0.2_275/0.07),transparent_45%),radial-gradient(ellipse_at_80%_85%,oklch(0.68_0.2_350/0.06),transparent_45%),linear-gradient(180deg,#faf9f5_0%,#f0ede5_100%)] font-twc20-sans">

  <div aria-hidden="true" class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
    <div class="absolute top-1/2 left-1/2 size-225 -translate-x-1/2 -translate-y-1/2 blur-[60px] [background:radial-gradient(circle_at_30%_30%,oklch(0.55_0.2_275/0.11)_0%,transparent_45%),radial-gradient(circle_at_70%_70%,oklch(0.68_0.2_350/0.07)_0%,transparent_45%)]"></div>
    <div class="absolute inset-0 [background-image:linear-gradient(oklch(0.55_0.2_275/0.04)_1px,transparent_1px),linear-gradient(90deg,oklch(0.55_0.2_275/0.04)_1px,transparent_1px)] [background-size:36px_36px] [mask-image:radial-gradient(ellipse_at_center,black_30%,transparent_70%)] [-webkit-mask-image:radial-gradient(ellipse_at_center,black_30%,transparent_70%)]"></div>
  </div>

  <div tabindex="0" aria-label="Project stack — reveals two more projects" class="group relative z-1 w-full max-w-[380px] pt-12 focus-visible:outline-2 focus-visible:outline-twc20-acc focus-visible:outline-offset-[12px] focus-visible:rounded-3xl">

    <header class="absolute top-0 inset-x-0 flex items-center justify-between gap-2 px-1">
      <div class="inline-flex items-center gap-1.5 pl-1.5 pr-3 py-1.5 rounded-full bg-white/85 backdrop-blur-[8px] border border-twc20-acc/16 text-[11px] font-bold text-twc20-ink shadow-[0_2px_8px_oklch(0.4_0.08_300/0.06)]">
        <span aria-hidden="true" class="inline-flex items-center justify-center size-5.5 rounded-full [background:linear-gradient(135deg,#6366f1,#a855f7)] text-white text-[10px] font-extrabold tracking-[-0.02em] shadow-[inset_0_1px_0_oklch(1_0_0/0.3)]">M</span>
        Meridian Labs
      </div>
      <button type="button" aria-label="Open command palette" class="inline-flex items-center gap-1.5 min-h-11 pl-3 pr-2 rounded-full bg-white/85 backdrop-blur-[8px] border border-black/6 text-twc20-muted cursor-pointer transition-[background,color] duration-200 hover:bg-white hover:text-twc20-ink2 focus-visible:outline-2 focus-visible:outline-twc20-acc focus-visible:outline-offset-2 shadow-[0_2px_8px_oklch(0.4_0.08_300/0.04)]">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.35-4.35"/></svg>
        <kbd aria-hidden="true" class="px-1.5 py-0.5 rounded font-twc20-mono text-[9px] font-bold text-twc20-muted bg-black/4 border border-black/8">&#8984;K</kbd>
      </button>
    </header>

    <article aria-hidden="true" class="absolute top-17 -right-[6%] z-0 w-[88%] px-4 py-3.5 rounded-[20px] border border-black/6 [background:linear-gradient(180deg,#fefefe_0%,#f9f9f8_100%)] shadow-[0_20px_40px_-12px_oklch(0.4_0.08_300/0.2),0_8px_20px_-6px_oklch(0.4_0.08_300/0.12),inset_0_1px_0_oklch(1_0_0/0.6)] [transform:rotate(-8deg)] transition-transform duration-550 ease-[cubic-bezier(0.34,1.15,0.64,1)] group-hover:[transform:translate(40px,32px)_rotate(-12deg)] group-focus-within:[transform:translate(40px,32px)_rotate(-12deg)] [@media(hover:none)]:[transform:translate(28px,24px)_rotate(-11deg)] motion-reduce:transition-none motion-reduce:group-hover:[transform:rotate(-8deg)] motion-reduce:group-focus-within:[transform:rotate(-8deg)]">
      <div class="flex items-center justify-between mb-2">
        <span class="px-[7px] py-[3px] rounded-full font-twc20-mono text-[8.5px] font-extrabold tracking-[0.14em] uppercase text-twc20-amberink bg-twc20-amber/15 border border-twc20-amberink/24">PLANNING</span>
        <span class="font-twc20-mono text-[9.5px] font-bold tracking-[-0.005em] text-twc20-dim">Sep 20</span>
      </div>
      <div class="mb-2.5 text-[13.5px] font-extrabold tracking-[-0.015em] text-twc20-ink truncate">Mobile app redesign</div>
      <div class="flex items-center gap-2.5">
        <div class="flex flex-none">
          <span class="size-4.5 rounded-full border-2 border-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#f472b6,#ec4899)]"></span>
          <span class="size-4.5 -ml-[5px] rounded-full border-2 border-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#60a5fa,#3b82f6)]"></span>
        </div>
        <div class="flex-1 h-1 rounded-full overflow-hidden bg-black/6">
          <div class="h-full w-[12%] rounded-full [background:linear-gradient(90deg,#fbbf24,#d97706)]"></div>
        </div>
      </div>
    </article>

    <article aria-hidden="true" class="absolute top-19 -left-[6%] z-1 w-[88%] px-4 py-3.5 rounded-[20px] border border-black/6 [background:linear-gradient(180deg,#fff_0%,#fafafa_100%)] shadow-[0_20px_40px_-12px_oklch(0.4_0.08_300/0.2),0_8px_20px_-6px_oklch(0.4_0.08_300/0.12),inset_0_1px_0_oklch(1_0_0/0.6)] [transform:rotate(7deg)] transition-transform duration-550 ease-[cubic-bezier(0.34,1.15,0.64,1)] group-hover:[transform:translate(-40px,24px)_rotate(11deg)] group-focus-within:[transform:translate(-40px,24px)_rotate(11deg)] [@media(hover:none)]:[transform:translate(-28px,18px)_rotate(10deg)] motion-reduce:transition-none motion-reduce:group-hover:[transform:rotate(7deg)] motion-reduce:group-focus-within:[transform:rotate(7deg)]">
      <div class="flex items-center justify-between mb-2">
        <span class="px-[7px] py-[3px] rounded-full font-twc20-mono text-[8.5px] font-extrabold tracking-[0.14em] uppercase text-twc20-greenink bg-twc20-green/12 border border-twc20-greenink/24">IN REVIEW</span>
        <span class="font-twc20-mono text-[9.5px] font-bold tracking-[-0.005em] text-twc20-dim">Aug 22</span>
      </div>
      <div class="mb-2.5 text-[13.5px] font-extrabold tracking-[-0.015em] text-twc20-ink truncate">Payment gateway migration</div>
      <div class="flex items-center gap-2.5">
        <div class="flex flex-none">
          <span class="size-4.5 rounded-full border-2 border-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#f472b6,#ec4899)]"></span>
          <span class="size-4.5 -ml-[5px] rounded-full border-2 border-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#60a5fa,#3b82f6)]"></span>
          <span class="size-4.5 -ml-[5px] rounded-full border-2 border-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#34d399,#10b981)]"></span>
        </div>
        <div class="flex-1 h-1 rounded-full overflow-hidden bg-black/6">
          <div class="h-full w-[78%] rounded-full [background:linear-gradient(90deg,#22c55e,#15803d)]"></div>
        </div>
      </div>
    </article>

    <article class="relative z-2 isolate px-5.5 pt-5 pb-4.5 rounded-[20px] border border-twc20-acc/24 [background:linear-gradient(180deg,#fff_0%,#fefdfa_100%)] shadow-[0_40px_70px_-20px_oklch(0.4_0.08_300/0.3),0_20px_40px_-20px_oklch(0.55_0.2_275/0.22),inset_0_1px_0_oklch(1_0_0/0.7)] transition-[transform,box-shadow] duration-550 ease-[cubic-bezier(0.34,1.15,0.64,1)] group-hover:-translate-y-1.5 group-focus-within:-translate-y-1.5 group-hover:shadow-[0_50px_80px_-20px_oklch(0.4_0.08_300/0.36),0_26px_46px_-20px_oklch(0.55_0.2_275/0.28),inset_0_1px_0_oklch(1_0_0/0.7)] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 motion-reduce:group-focus-within:translate-y-0">
      <div aria-hidden="true" class="absolute -top-12 -left-12 size-75 -z-1 pointer-events-none blur-[24px] [background:radial-gradient(circle,oklch(0.55_0.2_275/0.22)_0%,transparent_55%)]"></div>

      <header class="flex items-center gap-1.5 mb-3.5">
        <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-full font-twc20-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-twc20-accdeep bg-twc20-acc/10 border border-twc20-acc/26">
          <span aria-hidden="true" class="size-[5px] rounded-full bg-twc20-acc shadow-[0_0_6px_oklch(0.55_0.2_275)] animate-twc20-pulse motion-reduce:animate-none"></span>
          IN PROGRESS
        </span>
        <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-full font-twc20-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-twc20-pinkink bg-twc20-pink/10 border border-twc20-pink/28">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15 9 22 9 17 14 19 21 12 17 5 21 7 14 2 9 9 9"/></svg>
          P1
        </span>
        <div class="relative ml-auto inline-flex items-center justify-center size-7 rounded-lg bg-black/3 border border-black/6 text-twc20-ink2">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
          <span class="absolute -top-[5px] -right-[5px] inline-flex items-center justify-center min-w-4 h-4 px-1 rounded-full bg-twc20-pink text-white border-[1.5px] border-white font-twc20-mono text-[9px] font-extrabold shadow-[0_0_8px_oklch(0.68_0.2_350/0.5)]">4<span class="sr-only"> unread notifications</span></span>
        </div>
      </header>

      <h3 class="m-0 mb-1 text-[22px]/[1.15] font-extrabold tracking-[-0.025em] text-twc20-ink [background-image:linear-gradient(180deg,#1a1a1a_0%,#4338ca_140%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">Homepage redesign</h3>
      <p class="m-0 mb-4 text-[11.5px] tracking-[-0.005em] text-twc20-muted">Due Aug 14 &middot; Q3 milestone &middot; 14 of 22 tasks</p>

      <div class="mb-3.5">
        <div role="progressbar" aria-valuenow="64" aria-valuemin="0" aria-valuemax="100" aria-label="Homepage redesign progress" class="relative h-1.5 mb-2 rounded-full overflow-hidden bg-black/6">
          <div class="h-full w-[64%] rounded-full [background:linear-gradient(90deg,#22c55e_0%,#16a34a_60%,#15803d_100%)] shadow-[0_0_10px_oklch(0.65_0.18_150/0.4)]"></div>
        </div>
        <div class="flex items-center justify-between">
          <span class="font-twc20-mono text-[15px] font-extrabold tracking-[-0.02em] [background-image:linear-gradient(90deg,#16a34a,#15803d)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">64%</span>
          <div aria-hidden="true" class="flex">
            <span class="inline-flex items-center justify-center size-6 rounded-full border-2 border-white text-white text-[8.5px] font-extrabold tracking-[-0.02em] shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#f472b6,#ec4899)]">AR</span>
            <span class="inline-flex items-center justify-center size-6 -ml-1.5 rounded-full border-2 border-white text-white text-[8.5px] font-extrabold tracking-[-0.02em] shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#60a5fa,#3b82f6)]">JL</span>
            <span class="inline-flex items-center justify-center size-6 -ml-1.5 rounded-full border-2 border-white text-white text-[8.5px] font-extrabold tracking-[-0.02em] shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#34d399,#10b981)]">MK</span>
            <span class="inline-flex items-center justify-center size-6 -ml-1.5 rounded-full border-2 border-white font-twc20-mono text-[8px] font-extrabold text-twc20-accdeep bg-twc20-acc/12 shadow-[0_0_0_1px_oklch(0.55_0.2_275/0.2)]">+2</span>
          </div>
        </div>
      </div>

      <footer class="flex items-center gap-2.5">
        <button type="button" class="group/cta relative flex-1 inline-flex items-center justify-center gap-1.5 overflow-hidden min-h-11 px-4 rounded-xl border-0 cursor-pointer text-[12.5px] font-extrabold tracking-[-0.01em] text-white [background:linear-gradient(180deg,#818cf8_0%,#4338ca_100%)] shadow-[0_4px_12px_oklch(0.55_0.2_275/0.35),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_8px_20px_oklch(0.55_0.2_275/0.5),inset_0_0_0_1px_oklch(1_0_0/0.24)] focus-visible:outline-2 focus-visible:outline-twc20-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <span aria-hidden="true" class="absolute top-0 -left-full w-3/5 h-full transition-[left] duration-600 ease-out group-hover/cta:left-[130%] motion-reduce:transition-none motion-reduce:group-hover/cta:-left-full [background:linear-gradient(115deg,transparent_30%,oklch(1_0_0/0.5)_50%,transparent_70%)]"></span>
          <span class="relative">Open project</span>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="relative"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </button>
        <span class="inline-flex items-center gap-1 max-w-33 text-left text-[10px]/[1.3] font-semibold tracking-[-0.005em] text-twc20-dim">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc20-acc"><polyline points="9 18 15 12 9 6"/></svg>
          <span class="[@media(hover:none)]:hidden">Hover or tab to fan out 2 more</span>
          <span class="hidden [@media(hover:none)]:inline">2 more projects in this stack</span>
        </span>
      </footer>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc20-bg: #faf9f5;
  --color-twc20-bg: oklch(0.98 0.006 90);
  --color-twc20-ink: #1a1a1a;
  --color-twc20-ink: oklch(0.21 0.005 270);
  --color-twc20-ink2: #4b4b57;
  --color-twc20-ink2: oklch(0.4 0.015 280);
  --color-twc20-muted: #6b6b7c;
  --color-twc20-muted: oklch(0.51 0.02 285);
  --color-twc20-dim: #9ca3af;
  --color-twc20-dim: oklch(0.71 0.02 265);
  --color-twc20-acc: #6366f1;
  --color-twc20-acc: oklch(0.55 0.2 275);
  --color-twc20-accdeep: #4338ca;
  --color-twc20-accdeep: oklch(0.42 0.21 275);
  --color-twc20-pink: #ec4899;
  --color-twc20-pink: oklch(0.68 0.2 350);
  --color-twc20-pinkink: #be185d;
  --color-twc20-pinkink: oklch(0.5 0.19 355);
  --color-twc20-green: #22c55e;
  --color-twc20-green: oklch(0.72 0.18 145);
  --color-twc20-greenink: #15803d;
  --color-twc20-greenink: oklch(0.5 0.14 148);
  --color-twc20-amber: #fbbf24;
  --color-twc20-amber: oklch(0.82 0.16 80);
  --color-twc20-amberink: #b45309;
  --color-twc20-amberink: oklch(0.52 0.14 62);
  --font-twc20-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc20-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc20-pulse: twc20-pulse 2s ease-in-out infinite;
}

@keyframes twc20-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.35);
    opacity: 0.6;
  }
}

.twc-20 {
  width: 100%;
  min-height: 100svh;
}
```
