---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-team-profile-card-masked-grid-cover/"
title: "Tailwind Team Profile Card with Masked Grid Cover"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A profile tile: mesh-gradient cover with a masked 20px grid, an avatar overlapping it by half, a verified name, a semantic stat row and a social icon row."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Team Profile Card with Masked Grid Cover
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-team-profile-card-masked-grid-cover/

A profile tile: mesh-gradient cover with a masked 20px grid, an avatar overlapping it by half, a verified name, a semantic stat row and a social icon row. The port's win is the cover &mdash; a two-gradient grid plus a fade mask, expressed as three arbitrary properties on one element instead of a separate pattern class.
## HTML
```html
<section class="twc-11 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc11-bg [background-image:radial-gradient(ellipse_at_20%_20%,oklch(0.6_0.2_295/0.07),transparent_50%),radial-gradient(ellipse_at_80%_80%,oklch(0.68_0.2_350/0.05),transparent_50%)] font-twc11-sans">

  <article class="relative w-full max-w-[340px] overflow-hidden rounded-[22px] bg-white border border-black/5 shadow-[0_30px_60px_-30px_oklch(0.35_0.1_290/0.2),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_40px_80px_-30px_oklch(0.35_0.1_290/0.3)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">

    <div aria-hidden="true" class="relative h-23 overflow-hidden [background:linear-gradient(160deg,#a5b4fc_0%,#6366f1_45%,#ec4899_100%)]">
      <div class="absolute inset-0 [background:radial-gradient(ellipse_at_20%_30%,oklch(1_0_0/0.35)_0%,transparent_40%),radial-gradient(ellipse_at_80%_70%,oklch(0.75_0.16_350/0.4)_0%,transparent_45%),radial-gradient(circle_at_55%_40%,oklch(0.6_0.2_295/0.3)_0%,transparent_40%)]"></div>
      <div class="absolute inset-0 [background-image:linear-gradient(oklch(1_0_0/0.06)_1px,transparent_1px),linear-gradient(90deg,oklch(1_0_0/0.06)_1px,transparent_1px)] [background-size:20px_20px] [mask-image:linear-gradient(180deg,transparent_0%,black_40%,black_80%,transparent_100%)] [-webkit-mask-image:linear-gradient(180deg,transparent_0%,black_40%,black_80%,transparent_100%)]"></div>
    </div>

    <button type="button" aria-label="More options" class="absolute top-2.5 right-2.5 z-3 inline-flex items-center justify-center size-11 rounded-lg bg-white/15 backdrop-blur-[8px] border border-white/25 text-white cursor-pointer transition-[background,border-color] duration-200 hover:bg-white/25 hover:border-white/40 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg>
    </button>

    <div class="relative z-2 w-17 h-17 -mt-8.5 mx-auto">
      <div aria-hidden="true" class="relative size-17 p-[3px] rounded-full [background:linear-gradient(135deg,#6366f1_0%,#ec4899_100%)] shadow-[0_6px_18px_oklch(0.55_0.2_275/0.35)]">
        <span class="flex items-center justify-center size-full rounded-full border-[3px] border-white [background:linear-gradient(180deg,#f5f4fb_0%,#e4e4f0_100%)] text-twc11-accdeep text-xl font-extrabold tracking-[-0.01em]">AC</span>
      </div>
      <span role="img" aria-label="Available for work" class="absolute bottom-0.5 right-0.5 flex items-center justify-center size-4.5 rounded-full bg-white shadow-[0_2px_6px_oklch(0_0_0/0.15)]">
        <span aria-hidden="true" class="size-2.5 rounded-full bg-twc11-green shadow-[0_0_0_2px_oklch(0.78_0.14_165/0.32)] animate-twc11-pulse motion-reduce:animate-none"></span>
      </span>
    </div>

    <div class="px-5.5 pt-3 pb-4 text-center">
      <div class="inline-flex items-center gap-1.5 mb-1">
        <h3 class="m-0 text-[19px] font-bold tracking-[-0.02em] text-twc11-ink [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">Alex Chen</h3>
        <svg role="img" aria-label="Verified" width="15" height="15" viewBox="0 0 24 24" fill="none" class="flex-none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#6366f1"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <p class="m-0 mb-1.5 text-[12.5px] font-medium text-twc11-ink2">Founding Engineer at <span class="font-bold text-twc11-accdeep">Anthropic</span></p>
      <p class="m-0 mb-3 text-[12.5px]/[1.5] text-twc11-muted">Building the tools I wish I had. Ex-Vercel, ex-Stripe.</p>

      <ul aria-label="Profile info" class="inline-flex flex-wrap justify-center gap-y-1.5 gap-x-3 list-none m-0 mb-3.5 p-0">
        <li class="inline-flex items-center gap-1 text-[11px] font-medium text-twc11-muted">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc11-dim"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          San Francisco
        </li>
        <li class="inline-flex items-center gap-1 text-[11px] font-medium text-twc11-muted">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc11-dim"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          GMT&minus;8
        </li>
      </ul>

      <dl class="grid grid-cols-3 m-0 py-3 rounded-xl [background:linear-gradient(180deg,#fafafd_0%,#f4f4fa_100%)] border border-black/5">
        <div class="flex flex-col items-center gap-0.5">
          <dt class="m-0 text-[9.5px] font-semibold tracking-[0.1em] uppercase text-twc11-dim">Following</dt>
          <dd class="m-0 text-sm font-bold tracking-[-0.01em] text-twc11-ink [font-variant-numeric:tabular-nums]">1,284</dd>
        </div>
        <div class="flex flex-col items-center gap-0.5 border-l border-black/6">
          <dt class="m-0 text-[9.5px] font-semibold tracking-[0.1em] uppercase text-twc11-dim">Followers</dt>
          <dd class="m-0 text-sm font-bold tracking-[-0.01em] text-twc11-ink [font-variant-numeric:tabular-nums]">12.4k</dd>
        </div>
        <div class="flex flex-col items-center gap-0.5 border-l border-black/6">
          <dt class="m-0 text-[9.5px] font-semibold tracking-[0.1em] uppercase text-twc11-dim">Repos</dt>
          <dd class="m-0 text-sm font-bold tracking-[-0.01em] text-twc11-ink [font-variant-numeric:tabular-nums]">47</dd>
        </div>
      </dl>
    </div>

    <footer class="flex items-center justify-between gap-2 px-5.5 pt-3.5 pb-4.5">
      <button type="button" class="inline-flex items-center gap-1.5 min-h-11 px-4 rounded-full border-0 cursor-pointer text-[13px] font-bold tracking-[-0.01em] text-white [background:linear-gradient(180deg,#1e1e2c_0%,#06070c_100%)] shadow-[0_4px_12px_oklch(0_0_0/0.2),inset_0_0_0_1px_oklch(1_0_0/0.12)] transition-[transform,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_6px_16px_oklch(0_0_0/0.28),inset_0_0_0_1px_oklch(1_0_0/0.18)] focus-visible:outline-2 focus-visible:outline-twc11-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8v8M8 12h8"/></svg>
        Follow
      </button>
      <div aria-label="Social links" class="flex gap-1">
        <a href="#github" aria-label="GitHub" class="inline-flex items-center justify-center size-11 rounded-[10px] bg-transparent border border-black/6 text-twc11-muted no-underline transition-[color,background,border-color,transform] duration-200 hover:text-twc11-acc hover:bg-twc11-acc/6 hover:border-twc11-acc/25 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc11-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .3a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.6-1.4-1.4-1.8-1.4-1.8-1.1-.7.1-.7.1-.7 1.2 0 1.9 1.2 1.9 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-6 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.7.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .3"/></svg>
        </a>
        <a href="#linkedin" aria-label="LinkedIn" class="inline-flex items-center justify-center size-11 rounded-[10px] bg-transparent border border-black/6 text-twc11-muted no-underline transition-[color,background,border-color,transform] duration-200 hover:text-twc11-acc hover:bg-twc11-acc/6 hover:border-twc11-acc/25 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc11-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.5 2h-17A1.5 1.5 0 0 0 2 3.5v17A1.5 1.5 0 0 0 3.5 22h17a1.5 1.5 0 0 0 1.5-1.5v-17A1.5 1.5 0 0 0 20.5 2zM8 19H5v-9h3v9zM6.5 8.25A1.75 1.75 0 1 1 8.3 6.5a1.78 1.78 0 0 1-1.8 1.75zM19 19h-3v-4.7c0-1.1 0-2.5-1.6-2.5s-1.8 1.2-1.8 2.4V19h-3v-9h2.9v1.2a3.1 3.1 0 0 1 2.8-1.5c3 0 3.6 2 3.6 4.5V19z"/></svg>
        </a>
        <a href="#x" aria-label="X" class="inline-flex items-center justify-center size-11 rounded-[10px] bg-transparent border border-black/6 text-twc11-muted no-underline transition-[color,background,border-color,transform] duration-200 hover:text-twc11-acc hover:bg-twc11-acc/6 hover:border-twc11-acc/25 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc11-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2H21l-6.52 7.45L22 22h-6.828l-4.79-6.213L4.83 22H2.07l6.97-7.965L1.5 2h6.99l4.33 5.688L18.244 2z"/></svg>
        </a>
      </div>
    </footer>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc11-bg: #f5f4f0;
  --color-twc11-bg: oklch(0.96 0.005 90);
  --color-twc11-ink: #1a1a1a;
  --color-twc11-ink: oklch(0.21 0.005 270);
  --color-twc11-ink2: #4b5563;
  --color-twc11-ink2: oklch(0.44 0.02 260);
  --color-twc11-muted: #6b6b7c;
  --color-twc11-muted: oklch(0.51 0.02 285);
  --color-twc11-dim: #9ca3af;
  --color-twc11-dim: oklch(0.71 0.02 265);
  --color-twc11-acc: #6366f1;
  --color-twc11-acc: oklch(0.55 0.2 275);
  --color-twc11-accdeep: #4338ca;
  --color-twc11-accdeep: oklch(0.42 0.21 275);
  --color-twc11-green: #34d399;
  --color-twc11-green: oklch(0.78 0.14 165);
  --font-twc11-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc11-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc11-pulse: twc11-pulse 2.4s ease-in-out infinite;
}

@keyframes twc11-pulse {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 0 2px oklch(0.78 0.14 165 / 0.32);
  }

  50% {
    transform: scale(1.15);
    box-shadow: 0 0 0 4px oklch(0.78 0.14 165 / 0.16);
  }
}

.twc-11 {
  width: 100%;
  min-height: 100svh;
}
```
