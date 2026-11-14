---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-dark-mode-noise-without-muddy-shadows/"
title: "Tailwind Dark Mode Noise Without Muddy Shadows"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Grain gets ripped back out of dark products for one reason: overlay can only darken below mid-grey, so noise on a near-black surface turns elevation into mud."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Noise Without Muddy Shadows
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-dark-mode-noise-without-muddy-shadows/

Grain gets ripped back out of dark products for one reason: overlay can only darken below mid-grey, so noise on a near-black surface turns elevation into mud. The fix is three parts — soft-light instead of overlay, roughly 1.6× the light-theme opacity, and a mask that keeps noise out of the deepest shadows. A dark dashboard shipping all three.
## HTML
```html
<section class="gtw-19 relative block w-full min-h-svh bg-gtw19-bg text-gtw19-ink" aria-labelledby="gtw-19-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-60">
    <input type="checkbox" id="gtw-19-theme" class="gtw-19-theme peer sr-only">
    <label for="gtw-19-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw19-line bg-gtw19-s3 text-gtw19-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw19-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle light theme</span>
    </label>
  </div>

  <div class="gtw-19-app grid grid-cols-[minmax(0,1fr)] min-[62rem]:grid-cols-[16rem_minmax(0,1fr)] min-h-svh">
    <aside aria-label="Sections" class="gtw-19-rail relative isolate overflow-hidden grid content-start gap-[1.2rem] p-[clamp(1.2rem,3vw,1.8rem)] border-r border-gtw19-line bg-gtw19-s1">
      <p class="m-0 font-gtw19-display text-[1.05rem] font-semibold leading-none tracking-[-0.01em]">◐ Umbra</p>
      <nav class="grid gap-[0.15rem]">
        <a href="#gtw-19-title" aria-current="page" class="flex items-center min-h-11 px-3 rounded-[9px] text-gtw19-mut no-underline text-[0.92rem] transition-colors duration-150 hover:bg-gtw19-s2 hover:text-gtw19-ink aria-[current=page]:bg-gtw19-s3 aria-[current=page]:text-gtw19-ink aria-[current=page]:shadow-[inset_2px_0_0_var(--color-gtw19-acc)] focus-visible:outline-2 focus-visible:outline-gtw19-acc focus-visible:outline-offset-2">Overview</a>
        <a href="#gtw-19-title" class="flex items-center min-h-11 px-3 rounded-[9px] text-gtw19-mut no-underline text-[0.92rem] transition-colors duration-150 hover:bg-gtw19-s2 hover:text-gtw19-ink focus-visible:outline-2 focus-visible:outline-gtw19-acc focus-visible:outline-offset-2">Surfaces</a>
        <a href="#gtw-19-title" class="flex items-center min-h-11 px-3 rounded-[9px] text-gtw19-mut no-underline text-[0.92rem] transition-colors duration-150 hover:bg-gtw19-s2 hover:text-gtw19-ink focus-visible:outline-2 focus-visible:outline-gtw19-acc focus-visible:outline-offset-2">Elevation</a>
        <a href="#gtw-19-title" class="flex items-center min-h-11 px-3 rounded-[9px] text-gtw19-mut no-underline text-[0.92rem] transition-colors duration-150 hover:bg-gtw19-s2 hover:text-gtw19-ink focus-visible:outline-2 focus-visible:outline-gtw19-acc focus-visible:outline-offset-2">Contrast</a>
        <a href="#gtw-19-title" class="flex items-center min-h-11 px-3 rounded-[9px] text-gtw19-mut no-underline text-[0.92rem] transition-colors duration-150 hover:bg-gtw19-s2 hover:text-gtw19-ink focus-visible:outline-2 focus-visible:outline-gtw19-acc focus-visible:outline-offset-2">Tokens</a>
      </nav>
      <p class="m-0 pt-4 border-t border-gtw19-line text-gtw19-mut text-[0.8rem] text-pretty">Grain weight climbs with elevation. Shadows do almost nothing here.</p>
    </aside>

    <main class="grid content-start gap-[clamp(1.4rem,3.5vw,2.2rem)] p-[clamp(1.5rem,4vw,2.6rem)] pr-[clamp(4rem,8vw,5rem)]">
      <header class="max-w-[46rem] grid gap-[0.55rem]">
        <p class="m-0 font-gtw19-mono text-[0.72rem] font-medium leading-none tracking-[0.18em] uppercase text-gtw19-acc">Dark surface recipe · 19</p>
        <h1 id="gtw-19-title" class="m-0 font-gtw19-display text-[clamp(1.8rem,4.6vw,2.9rem)] font-semibold leading-[1.05] tracking-[-0.035em] text-balance">Texture in the dark, without the mud</h1>
        <p class="m-0 max-w-[40rem] text-gtw19-mut text-[clamp(0.93rem,1.8vw,1.04rem)] text-pretty">Two grain weights, <code class="font-gtw19-mono text-[0.9em]">soft-light</code> instead of <code class="font-gtw19-mono text-[0.9em]">overlay</code>, and a mask that keeps noise out of the deepest shadows. Toggle the theme and watch both numbers change.</p>
      </header>

      <ul class="list-none m-0 p-0 grid gap-[clamp(0.7rem,1.8vw,1.1rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))]">
        <li class="relative isolate overflow-hidden grid gap-[0.15rem] min-w-0 px-[1.15rem] py-4 rounded-[14px] border border-gtw19-line bg-gtw19-s1 transition-[translate] duration-[260ms] ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw19-noise)] after:[mix-blend-mode:var(--gtw19-blend)] after:opacity-[var(--gtw19-g1)]">
          <span class="font-gtw19-mono text-[0.7rem] leading-none tracking-[0.12em] uppercase text-gtw19-mut">Surface 1</span>
          <span class="font-gtw19-display text-[1.5rem] font-semibold leading-[1.1] tracking-[-0.03em]">8% L</span>
          <span class="font-gtw19-mono text-[0.76rem] leading-none text-gtw19-acc">grain 0.055</span>
        </li>
        <li class="relative isolate overflow-hidden grid gap-[0.15rem] min-w-0 px-[1.15rem] py-4 rounded-[14px] border border-gtw19-line bg-gtw19-s2 transition-[translate] duration-[260ms] ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw19-noise)] after:[mix-blend-mode:var(--gtw19-blend)] after:opacity-[var(--gtw19-g2)]">
          <span class="font-gtw19-mono text-[0.7rem] leading-none tracking-[0.12em] uppercase text-gtw19-mut">Surface 2</span>
          <span class="font-gtw19-display text-[1.5rem] font-semibold leading-[1.1] tracking-[-0.03em]">12% L</span>
          <span class="font-gtw19-mono text-[0.76rem] leading-none text-gtw19-acc">grain 0.075</span>
        </li>
        <li class="relative isolate overflow-hidden grid gap-[0.15rem] min-w-0 px-[1.15rem] py-4 rounded-[14px] border border-gtw19-line bg-gtw19-s3 transition-[translate] duration-[260ms] ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw19-noise)] after:[mix-blend-mode:var(--gtw19-blend)] after:opacity-[var(--gtw19-g3)]">
          <span class="font-gtw19-mono text-[0.7rem] leading-none tracking-[0.12em] uppercase text-gtw19-mut">Surface 3</span>
          <span class="font-gtw19-display text-[1.5rem] font-semibold leading-[1.1] tracking-[-0.03em]">17% L</span>
          <span class="font-gtw19-mono text-[0.76rem] leading-none text-gtw19-acc">grain 0.095</span>
        </li>
      </ul>

      <div class="grid gap-[clamp(0.8rem,2vw,1.2rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,17rem),1fr))] items-start">
        <section class="col-span-full relative isolate overflow-hidden grid content-start gap-[0.8rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw19-line bg-gtw19-s2 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw19-noise)] after:[mix-blend-mode:var(--gtw19-blend)] after:opacity-[var(--gtw19-g2)]" aria-labelledby="gtw-19-h-chart">
          <div class="flex items-center justify-between gap-[0.6rem] pb-[0.6rem] border-b border-gtw19-line">
            <h2 id="gtw-19-h-chart" class="m-0 font-gtw19-display text-[1rem] font-semibold leading-tight tracking-[-0.015em]">Perceived texture vs opacity</h2>
            <span class="px-2 py-[0.15rem] rounded-full bg-[color-mix(in_oklab,var(--color-gtw19-acc)_18%,transparent)] text-gtw19-acc font-gtw19-mono text-[0.66rem] font-medium leading-[1.6] tracking-[0.1em] uppercase">measured</span>
          </div>
          <div role="img" aria-label="Bar chart showing dark surfaces need roughly 1.6 times the grain opacity of light surfaces for equal perceived texture" class="grid grid-flow-col auto-cols-fr items-end gap-[clamp(0.4rem,1.5vw,0.9rem)] h-[clamp(7rem,16vw,10rem)] pt-2">
            <span class="relative block h-[32%] rounded-t-lg bg-[color-mix(in_oklab,var(--color-gtw19-acc)_28%,var(--color-gtw19-s3))]"><b class="absolute inset-x-0 -top-[1.35rem] text-center font-gtw19-mono text-[0.7rem] font-medium leading-none text-gtw19-mut">0.03</b></span>
            <span class="relative block h-[48%] rounded-t-lg bg-[color-mix(in_oklab,var(--color-gtw19-acc)_28%,var(--color-gtw19-s3))]"><b class="absolute inset-x-0 -top-[1.35rem] text-center font-gtw19-mono text-[0.7rem] font-medium leading-none text-gtw19-mut">0.045</b></span>
            <span class="relative block h-[68%] rounded-t-lg bg-gtw19-acc"><b class="absolute inset-x-0 -top-[1.35rem] text-center font-gtw19-mono text-[0.7rem] font-medium leading-none text-gtw19-ink">0.06</b></span>
            <span class="relative block h-[84%] rounded-t-lg bg-gtw19-acc"><b class="absolute inset-x-0 -top-[1.35rem] text-center font-gtw19-mono text-[0.7rem] font-medium leading-none text-gtw19-ink">0.075</b></span>
            <span class="relative block h-full rounded-t-lg bg-[color-mix(in_oklab,var(--color-gtw19-acc)_28%,var(--color-gtw19-s3))]"><b class="absolute inset-x-0 -top-[1.35rem] text-center font-gtw19-mono text-[0.7rem] font-medium leading-none text-gtw19-mut">0.095</b></span>
          </div>
          <p class="m-0 text-gtw19-mut text-[0.83rem] text-pretty">The marked pair is the working range for dark product UI. The same perceived texture on a light surface sits at 0.04–0.05.</p>
        </section>

        <section class="relative isolate overflow-hidden grid content-start gap-[0.8rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw19-line bg-gtw19-s2 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw19-noise)] after:[mix-blend-mode:var(--gtw19-blend)] after:opacity-[var(--gtw19-g2)]" aria-labelledby="gtw-19-h-blend">
          <div class="flex items-center justify-between gap-[0.6rem] pb-[0.6rem] border-b border-gtw19-line"><h2 id="gtw-19-h-blend" class="m-0 font-gtw19-display text-[1rem] font-semibold leading-tight tracking-[-0.015em]">Blend choice</h2></div>
          <ul class="list-none m-0 p-0 grid gap-[0.1rem]">
            <li class="grid gap-[0.1rem] py-[0.55rem]"><b class="font-gtw19-mono text-[0.88rem] font-medium leading-tight">soft-light</b><span class="text-gtw19-mut text-[0.82rem] text-pretty">Ship this. Roughly symmetric at low lightness.</span></li>
            <li class="grid gap-[0.1rem] py-[0.55rem] border-t border-gtw19-line"><b class="font-gtw19-mono text-[0.88rem] font-medium leading-tight">screen</b><span class="text-gtw19-mut text-[0.82rem] text-pretty">For true black. Can only lift, never crush.</span></li>
            <li class="grid gap-[0.1rem] py-[0.55rem] border-t border-gtw19-line"><b class="font-gtw19-mono text-[0.88rem] font-medium leading-tight">overlay</b><span class="text-gtw19-mut text-[0.82rem] text-pretty">Avoid. Only darkens below mid-grey — this is the mud.</span></li>
          </ul>
        </section>

        <section class="relative isolate overflow-hidden grid content-start gap-[0.8rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw19-line bg-gtw19-s2 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw19-noise)] after:[mix-blend-mode:var(--gtw19-blend)] after:opacity-[var(--gtw19-g2)]" aria-labelledby="gtw-19-h-contrast">
          <div class="flex items-center justify-between gap-[0.6rem] pb-[0.6rem] border-b border-gtw19-line"><h2 id="gtw-19-h-contrast" class="m-0 font-gtw19-display text-[1rem] font-semibold leading-tight tracking-[-0.015em]">Contrast, composited</h2></div>
          <p class="m-0 text-gtw19-mut text-[0.83rem] text-pretty">A 9% grain layer measurably reduces text contrast. Check the composited surface, not the flat token.</p>
          <dl class="grid gap-0 m-0">
            <div class="flex items-baseline justify-between gap-[0.6rem] py-2 border-t border-gtw19-line"><dt class="m-0 text-gtw19-mut text-[0.83rem]">Body on surface 2</dt><dd class="m-0 font-gtw19-mono text-[0.9rem] font-semibold leading-none tabular-nums">7.1:1</dd></div>
            <div class="flex items-baseline justify-between gap-[0.6rem] py-2 border-t border-gtw19-line"><dt class="m-0 text-gtw19-mut text-[0.83rem]">Same, grain applied</dt><dd class="m-0 font-gtw19-mono text-[0.9rem] font-semibold leading-none tabular-nums">6.8:1</dd></div>
            <div class="flex items-baseline justify-between gap-[0.6rem] py-2 border-t border-gtw19-line"><dt class="m-0 text-gtw19-mut text-[0.83rem]">Muted on surface 2</dt><dd class="m-0 font-gtw19-mono text-[0.9rem] font-semibold leading-none tabular-nums">4.7:1</dd></div>
          </dl>
        </section>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw19-bg: #08090b;
  --color-gtw19-bg: oklch(0.14 0.005 265);
  --color-gtw19-s1: #101216;
  --color-gtw19-s1: oklch(0.19 0.008 265);
  --color-gtw19-s2: #171a20;
  --color-gtw19-s2: oklch(0.23 0.01 265);
  --color-gtw19-s3: #20242c;
  --color-gtw19-s3: oklch(0.28 0.012 265);
  --color-gtw19-line: #262b34;
  --color-gtw19-line: oklch(0.31 0.012 265);
  --color-gtw19-ink: #eef1f6;
  --color-gtw19-ink: oklch(0.95 0.008 265);
  --color-gtw19-mut: #98a1b0;
  --color-gtw19-mut: oklch(0.7 0.02 265);
  --color-gtw19-acc: #7dd3fc;
  --color-gtw19-acc: oklch(0.84 0.1 226);
  --font-gtw19-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw19-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-19 {
  width: 100%;
  min-height: 100svh;
  --gtw19-g1: 0.055;
  --gtw19-g2: 0.075;
  --gtw19-g3: 0.095;
  --gtw19-blend: soft-light;
  --gtw19-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='gtw19n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23gtw19n)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-19-app {
  min-height: 100vh;
  min-height: 100svh;
}
/* The rail's grain fades out over the bottom 30%, where its shadow gradient lives — noise in
   the deepest shadow is what kills elevation definition on dark UI. The -webkit- twin is
   required for older Safari and has no utility form. */

.gtw-19-rail::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image: var(--gtw19-noise);
  opacity: var(--gtw19-g1);
  mix-blend-mode: var(--gtw19-blend);
  -webkit-mask-image: linear-gradient(to bottom, #000 0%, #000 70%, rgba(0, 0, 0, 0.35) 100%);
  mask-image: linear-gradient(to bottom, #000 0%, #000 70%, rgba(0, 0, 0, 0.35) 100%);
}

.gtw-19:has(.gtw-19-theme:checked) {
  --color-gtw19-bg: #f4f6fa;
  --color-gtw19-bg: oklch(0.97 0.005 265);
  --color-gtw19-s1: #ffffff;
  --color-gtw19-s1: oklch(1 0 0);
  --color-gtw19-s2: #f7f9fc;
  --color-gtw19-s2: oklch(0.98 0.004 265);
  --color-gtw19-s3: #eef2f8;
  --color-gtw19-s3: oklch(0.95 0.008 265);
  --color-gtw19-line: #dde3ec;
  --color-gtw19-line: oklch(0.9 0.01 265);
  --color-gtw19-ink: #0b0d11;
  --color-gtw19-ink: oklch(0.16 0.008 265);
  --color-gtw19-mut: #5b6474;
  --color-gtw19-mut: oklch(0.47 0.02 265);
  --color-gtw19-acc: #0369a1;
  --color-gtw19-acc: oklch(0.48 0.11 235);
  --gtw19-g1: 0.03;
  --gtw19-g2: 0.045;
  --gtw19-g3: 0.055;
  --gtw19-blend: multiply;
}

@media (prefers-color-scheme: light) {
  .gtw-19 {
    --color-gtw19-bg: #f4f6fa;
    --color-gtw19-bg: oklch(0.97 0.005 265);
    --color-gtw19-s1: #ffffff;
    --color-gtw19-s1: oklch(1 0 0);
    --color-gtw19-s2: #f7f9fc;
    --color-gtw19-s2: oklch(0.98 0.004 265);
    --color-gtw19-s3: #eef2f8;
    --color-gtw19-s3: oklch(0.95 0.008 265);
    --color-gtw19-line: #dde3ec;
    --color-gtw19-line: oklch(0.9 0.01 265);
    --color-gtw19-ink: #0b0d11;
    --color-gtw19-ink: oklch(0.16 0.008 265);
    --color-gtw19-mut: #5b6474;
    --color-gtw19-mut: oklch(0.47 0.02 265);
    --color-gtw19-acc: #0369a1;
    --color-gtw19-acc: oklch(0.48 0.11 235);
    --gtw19-g1: 0.03;
    --gtw19-g2: 0.045;
    --gtw19-g3: 0.055;
    --gtw19-blend: multiply;
  }

  .gtw-19:has(.gtw-19-theme:checked) {
    --color-gtw19-bg: #08090b;
    --color-gtw19-bg: oklch(0.14 0.005 265);
    --color-gtw19-s1: #101216;
    --color-gtw19-s1: oklch(0.19 0.008 265);
    --color-gtw19-s2: #171a20;
    --color-gtw19-s2: oklch(0.23 0.01 265);
    --color-gtw19-s3: #20242c;
    --color-gtw19-s3: oklch(0.28 0.012 265);
    --color-gtw19-line: #262b34;
    --color-gtw19-line: oklch(0.31 0.012 265);
    --color-gtw19-ink: #eef1f6;
    --color-gtw19-ink: oklch(0.95 0.008 265);
    --color-gtw19-mut: #98a1b0;
    --color-gtw19-mut: oklch(0.7 0.02 265);
    --color-gtw19-acc: #7dd3fc;
    --color-gtw19-acc: oklch(0.84 0.1 226);
    --gtw19-g1: 0.055;
    --gtw19-g2: 0.075;
    --gtw19-g3: 0.095;
    --gtw19-blend: soft-light;
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-19:has(.gtw-19-theme:checked) {
    --color-gtw19-bg: #f4f6fa;
    --color-gtw19-bg: oklch(0.97 0.005 265);
    --color-gtw19-s1: #ffffff;
    --color-gtw19-s1: oklch(1 0 0);
    --color-gtw19-s2: #f7f9fc;
    --color-gtw19-s2: oklch(0.98 0.004 265);
    --color-gtw19-s3: #eef2f8;
    --color-gtw19-s3: oklch(0.95 0.008 265);
    --color-gtw19-line: #dde3ec;
    --color-gtw19-line: oklch(0.9 0.01 265);
    --color-gtw19-ink: #0b0d11;
    --color-gtw19-ink: oklch(0.16 0.008 265);
    --color-gtw19-mut: #5b6474;
    --color-gtw19-mut: oklch(0.47 0.02 265);
    --color-gtw19-acc: #0369a1;
    --color-gtw19-acc: oklch(0.48 0.11 235);
    --gtw19-g1: 0.03;
    --gtw19-g2: 0.045;
    --gtw19-g3: 0.055;
    --gtw19-blend: multiply;
  }
}
```
