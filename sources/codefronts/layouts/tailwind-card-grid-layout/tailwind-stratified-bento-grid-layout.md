---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-stratified-bento-grid-layout/"
title: "Tailwind Stratified Bento Grid Layout"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "Twelve tiles on a carmine canvas, each split by a hard-stop duotone gradient, and each carrying its inverse as a before: layer that wipes down on hover via…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stratified Bento Grid Layout
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-stratified-bento-grid-layout/

Twelve tiles on a carmine canvas, each split by a hard-stop duotone gradient, and each carrying its inverse as a before: layer that wipes down on hover via clip-path: inset(). Every one of the CSS version's twelve placement rules moves onto its tile, so the bento's weighting is finally readable in the markup.
## HTML
```html
<section class="tcg-07 w-full min-h-svh flex items-center justify-center bg-tcg07-bg font-tcg07-sans text-tcg07-ink p-9" aria-label="Stratified duotone bento grid demo">
  <div class="w-full max-w-[1100px] grid grid-cols-6 max-[640px]:grid-cols-3 [grid-auto-rows:110px] gap-3.5">

    <a href="#users" style="--top:#f4a572;--bot:#d97f4f" class="group relative isolate col-span-2 max-[640px]:col-span-1 flex flex-col justify-end gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[.68rem] font-semibold tracking-[0.12em] uppercase text-tcg07-shade">Active users</span>
      <span class="relative z-1 text-[1.8rem] font-extrabold tracking-[-0.02em] leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)] tabular-nums">247,318</span>
      <span class="relative z-1 text-[.72rem] font-semibold text-white/92">&#9650; 12.4% this week</span>
    </a>

    <a href="#uptime" style="--top:#1f8c6e;--bot:#0f5b48" class="group relative isolate col-span-1 flex flex-col items-center justify-center text-center gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[1.8rem] leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.18)]" aria-hidden="true">&#10003;</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">99.98% uptime</span>
    </a>

    <a href="#plan" style="--top:#c4b5fd;--bot:#9b87e5" class="group relative isolate col-span-1 row-span-2 flex flex-col justify-end gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[.68rem] font-semibold tracking-[0.12em] uppercase text-tcg07-shade">Plan</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">Pro</span>
      <span class="relative z-1 text-[1.5rem] font-extrabold leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">$24<small class="ml-0.5 text-[.7rem] font-semibold opacity-85">/mo</small></span>
      <span class="relative z-1 self-start mt-1 px-2.25 py-1.25 rounded-md bg-black/22 text-[.74rem] font-bold text-white transition-[background] duration-250 group-hover:bg-black/38 motion-reduce:transition-none">Upgrade &rarr;</span>
    </a>

    <a href="#cache" style="--top:#34d399;--bot:#0f7a52" class="group relative isolate col-span-1 flex flex-col items-center justify-center text-center gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[1.8rem] leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.18)]" aria-hidden="true">&#9889;</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">Edge cache</span>
    </a>

    <a href="#search" style="--top:#f0bb91;--bot:#cc8a5e" class="group relative isolate col-span-1 flex flex-col items-center justify-center text-center gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[1.8rem] leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.18)]" aria-hidden="true">&#8984;</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">Command search</span>
    </a>

    <a href="#story" style="--top:#f9c1cf;--bot:#e187a0" class="group relative isolate col-span-3 max-[640px]:col-span-2 flex flex-col justify-end gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[.68rem] font-semibold tracking-[0.12em] uppercase text-tcg07-shade">Customer story</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">It paid back in 6 weeks.</span>
      <span class="relative z-1 text-[.68rem] font-semibold text-tcg07-shade">Maya Chen &middot; Linear</span>
    </a>

    <a href="#rating" style="--top:#c5da9c;--bot:#94b864" class="group relative isolate col-span-1 flex flex-col items-center justify-center text-center gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[1.8rem] leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.18)]" aria-hidden="true">&#9733;</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)] tabular-nums">4.9 / 5</span>
    </a>

    <a href="#revenue" style="--top:#fff4a3;--bot:#e8d558" class="group relative isolate col-span-2 max-[640px]:col-span-1 flex flex-col justify-end gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-tcg07-ink focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[.68rem] font-semibold tracking-[0.12em] uppercase text-tcg07-shade">Monthly revenue</span>
      <span class="relative z-1 text-[1.8rem] font-extrabold tracking-[-0.02em] leading-none text-tcg07-ink tabular-nums">$2.4M</span>
      <span class="relative z-1 text-[.72rem] font-semibold text-tcg07-shade">&#9650; 38% YoY</span>
    </a>

    <a href="#api" style="--top:#1f8c6e;--bot:#0f5b48" class="group relative isolate col-span-1 flex flex-col items-center justify-center text-center gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[1.8rem] leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.18)]" aria-hidden="true">&#9881;</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">API v3</span>
    </a>

    <a href="#dark" style="--top:#f4a572;--bot:#d97f4f" class="group relative isolate col-span-1 flex flex-col items-center justify-center text-center gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[1.8rem] leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.18)]" aria-hidden="true">&#9790;</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">Dark mode</span>
    </a>

    <a href="#sync" style="--top:#c4b5fd;--bot:#9b87e5" class="group relative isolate col-span-1 flex flex-col items-center justify-center text-center gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[1.8rem] leading-none text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.18)]" aria-hidden="true">&#10227;</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">Auto sync</span>
    </a>

    <a href="#trial" style="--top:#f9c1cf;--bot:#e187a0" class="group relative isolate col-span-3 max-[640px]:col-span-2 flex flex-col justify-end gap-1 px-4.5 py-4 rounded-[14px] overflow-hidden no-underline text-inherit bg-linear-[to_bottom,var(--top)_0_50%,var(--bot)_50%_100%] before:absolute before:inset-0 before:z-0 before:bg-linear-[to_bottom,var(--bot)_0_50%,var(--top)_50%_100%] before:[clip-path:inset(0_0_100%_0)] before:transition-[clip-path] before:duration-[380ms] before:ease-tcg07 hover:before:[clip-path:inset(0)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:before:hidden">
      <span class="relative z-1 text-[.68rem] font-semibold tracking-[0.12em] uppercase text-tcg07-shade">Get started</span>
      <span class="relative z-1 text-[.95rem] font-bold leading-[1.25] text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.22)]">Start your 14-day free trial</span>
      <span class="relative z-1 self-start mt-1 px-2.25 py-1.25 rounded-md bg-black/22 text-[.74rem] font-bold text-white transition-[background] duration-250 group-hover:bg-black/38 motion-reduce:transition-none">Create account &rarr;</span>
    </a>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg07-bg: #c93a4a;
  --color-tcg07-bg: oklch(0.55 0.19 20);
  --color-tcg07-ink: #1a1414;
  --color-tcg07-ink: oklch(0.2 0.02 30);
  --color-tcg07-shade: #3a2a2a;
  --color-tcg07-shade: oklch(0.3 0.02 30);
  --font-tcg07-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tcg07: cubic-bezier(0.65, 0.05, 0.35, 1);
}
/* Root rule: the full-bleed contract. */

.tcg-07 {
  width: 100%;
  min-height: 100svh;
}

.tcg-07 ::selection {
  background: #fff;
  color: #c93a4a;
}
```
