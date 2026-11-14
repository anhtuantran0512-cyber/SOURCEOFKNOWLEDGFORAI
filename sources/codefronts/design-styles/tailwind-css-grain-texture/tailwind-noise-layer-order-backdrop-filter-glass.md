---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-noise-layer-order-backdrop-filter-glass/"
title: "Tailwind Noise Layer Order Over backdrop-filter Glass"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Glass panels look synthetic because the blur averages everything underneath into smoothness — including any grain you put there."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Noise Layer Order Over backdrop-filter Glass
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-noise-layer-order-backdrop-filter-glass/

Glass panels look synthetic because the blur averages everything underneath into smoothness — including any grain you put there. This demo is the A/B proof: same blur, same noise token, one panel with the grain behind the filter and one with it in front, then a real glass music player built the correct way.
## HTML
```html
<section class="gtw-11 relative block w-full min-h-svh overflow-hidden bg-[#0a0d14] text-gtw11-ink" aria-labelledby="gtw-11-title">
  <img src="https://picsum.photos/id/1029/2000/1300" alt="" aria-hidden="true" width="2000" height="1300" class="absolute inset-0 z-0 w-full h-full object-cover">
  <span aria-hidden="true" class="absolute inset-0 z-[1] bg-[linear-gradient(190deg,oklch(0.15_0.02_265/0.4),oklch(0.15_0.02_265/0.66))]"></span>

  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-60">
    <input type="checkbox" id="gtw-11-theme" class="gtw-11-theme peer sr-only">
    <label for="gtw-11-theme" class="gtw-11-glass grid place-items-center w-11 h-11 rounded-full border border-gtw11-rim text-gtw11-ink cursor-pointer backdrop-blur-[10px] peer-focus-visible:outline-2 peer-focus-visible:outline-gtw11-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="relative z-[5] w-[min(72rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(1.4rem,3.5vw,2.2rem)]">
    <header class="max-w-[46rem] grid gap-[0.6rem]">
      <p class="m-0 font-gtw11-mono text-[0.72rem] font-medium leading-none tracking-[0.18em] uppercase text-gtw11-acc">Layer order · 11</p>
      <h1 id="gtw-11-title" class="m-0 font-gtw11-display text-[clamp(2rem,5.4vw,3.4rem)] font-semibold leading-[1.03] tracking-[-0.035em] text-balance">Glass needs grain, and grain needs to be on top</h1>
      <p class="m-0 max-w-[40rem] text-gtw11-ink text-[clamp(0.95rem,1.9vw,1.08rem)] text-pretty">Both panels below use the same blur and the same noise token. One puts the grain behind the glass, where the blur destroys it. The other puts it in front, where it becomes surface.</p>
    </header>

    <div class="grid gap-[clamp(0.9rem,2.2vw,1.4rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]">
      <article class="gtw-11-glass relative isolate overflow-hidden grid content-start gap-[0.45rem] min-w-0 p-[clamp(1.2rem,3vw,1.8rem)] rounded-[18px] border border-gtw11-rim shadow-[inset_0_1px_0_var(--gtw11-rim),0_24px_60px_-34px_oklch(0_0_0/0.7)] [background-image:var(--gtw11-noise)] [background-blend-mode:overlay] transition-[translate] duration-[280ms] ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <p class="m-0 justify-self-start px-[0.6rem] py-[0.25rem] rounded-full bg-[oklch(0.7_0.19_25/0.3)] text-white font-gtw11-mono text-[0.68rem] font-semibold leading-[1.5] tracking-[0.1em] uppercase">Grain behind the blur</p>
        <h2 class="mt-[0.2rem] mb-0 font-gtw11-display text-[1.15rem] font-semibold leading-tight tracking-[-0.02em]">Smooth and synthetic</h2>
        <p class="m-0 text-gtw11-ink text-[0.9rem] text-pretty">The noise is a background on the glass itself, so <code class="font-gtw11-mono text-[0.9em]">backdrop-filter</code> averages it away. What is left is a plastic sheet.</p>
      </article>

      <article class="gtw-11-glass relative isolate overflow-hidden grid content-start gap-[0.45rem] min-w-0 p-[clamp(1.2rem,3vw,1.8rem)] rounded-[18px] border border-gtw11-rim shadow-[inset_0_1px_0_var(--gtw11-rim),0_24px_60px_-34px_oklch(0_0_0/0.7)] transition-[translate] duration-[280ms] ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="absolute inset-0 z-[2] pointer-events-none rounded-[inherit] bg-[image:var(--gtw11-noise)] opacity-[var(--gtw11-grain)] mix-blend-overlay"></span>
        <p class="relative z-[3] m-0 justify-self-start px-[0.6rem] py-[0.25rem] rounded-full bg-[oklch(0.7_0.12_226/0.32)] text-white font-gtw11-mono text-[0.68rem] font-semibold leading-[1.5] tracking-[0.1em] uppercase">Grain above the blur</p>
        <h2 class="relative z-[3] mt-[0.2rem] mb-0 font-gtw11-display text-[1.15rem] font-semibold leading-tight tracking-[-0.02em]">Etched and physical</h2>
        <p class="relative z-[3] m-0 text-gtw11-ink text-[0.9rem] text-pretty">The noise is a child layer painted after the filter, so it survives intact and reads as imperfection in the glass.</p>
      </article>
    </div>

    <section class="gtw-11-glass relative isolate overflow-hidden rounded-[22px] border border-gtw11-rim shadow-[inset_0_1px_0_var(--gtw11-rim),0_30px_80px_-40px_oklch(0_0_0/0.75)]" aria-labelledby="gtw-11-h-player">
      <span aria-hidden="true" class="absolute inset-0 z-[2] pointer-events-none rounded-[inherit] bg-[image:var(--gtw11-noise)] opacity-[var(--gtw11-grain)] mix-blend-overlay"></span>
      <div class="relative z-[3] grid gap-[1.1rem] p-[clamp(1.3rem,3.4vw,2rem)]">
        <div>
          <p class="m-0 font-gtw11-mono text-[0.68rem] font-medium leading-none tracking-[0.16em] uppercase text-gtw11-acc">Now playing</p>
          <h2 id="gtw-11-h-player" class="mt-[0.3rem] mb-[0.15rem] font-gtw11-display text-[clamp(1.3rem,3.4vw,1.9rem)] font-semibold leading-[1.1] tracking-[-0.03em]">Rue des Trois Frères</h2>
          <p class="m-0 text-gtw11-ink text-[0.9rem]">Sylvie Marchand · Nocturnes vol. II</p>
        </div>
        <div class="grid gap-[0.4rem]">
          <span class="block h-[6px] rounded-full overflow-hidden bg-[color-mix(in_oklab,var(--color-gtw11-ink)_22%,transparent)]"><span class="block w-[52%] h-full rounded-full bg-gtw11-acc"></span></span>
          <div class="flex justify-between font-gtw11-mono text-[0.75rem] leading-none text-gtw11-ink"><span>2:41</span><span>5:08</span></div>
        </div>
        <div class="flex items-center gap-[0.6rem]">
          <button type="button" aria-label="Previous track" class="grid place-items-center w-12 h-12 rounded-full border border-gtw11-rim bg-[color-mix(in_oklab,var(--color-gtw11-ink)_8%,transparent)] text-gtw11-ink cursor-pointer transition-[filter] duration-200 hover:brightness-[1.12] focus-visible:outline-2 focus-visible:outline-gtw11-acc focus-visible:outline-offset-[3px]">
            <svg viewBox="0 0 24 24" class="w-[22px] h-[22px]" aria-hidden="true" focusable="false"><path d="M18 6v12L9 12ZM7 6v12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
          </button>
          <button type="button" aria-label="Pause" class="grid place-items-center w-[58px] h-[58px] rounded-full border border-transparent bg-gtw11-acc text-[#06202c] cursor-pointer transition-[filter] duration-200 hover:brightness-[1.12] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px]">
            <svg viewBox="0 0 24 24" class="w-[22px] h-[22px]" aria-hidden="true" focusable="false"><path d="M9 6v12M15 6v12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          </button>
          <button type="button" aria-label="Next track" class="grid place-items-center w-12 h-12 rounded-full border border-gtw11-rim bg-[color-mix(in_oklab,var(--color-gtw11-ink)_8%,transparent)] text-gtw11-ink cursor-pointer transition-[filter] duration-200 hover:brightness-[1.12] focus-visible:outline-2 focus-visible:outline-gtw11-acc focus-visible:outline-offset-[3px]">
            <svg viewBox="0 0 24 24" class="w-[22px] h-[22px]" aria-hidden="true" focusable="false"><path d="M6 6v12l9-6ZM17 6v12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
          </button>
        </div>
      </div>
    </section>

    <ul class="list-none m-0 p-0 grid gap-[clamp(0.6rem,1.6vw,1rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,8.5rem),1fr))]">
      <li class="gtw-11-glass relative isolate overflow-hidden grid gap-[0.2rem] min-w-0 px-4 py-[0.85rem] rounded-[14px] border border-gtw11-rim shadow-[inset_0_1px_0_var(--gtw11-rim)] transition-[translate] duration-[280ms] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="absolute inset-0 z-[2] pointer-events-none rounded-[inherit] bg-[image:var(--gtw11-noise)] opacity-[var(--gtw11-grain)] mix-blend-overlay"></span>
        <span class="relative z-[3] font-gtw11-mono text-[0.68rem] leading-none tracking-[0.12em] uppercase text-gtw11-ink">blur</span>
        <span class="relative z-[3] font-gtw11-mono text-[1.05rem] font-semibold leading-tight">18px</span>
      </li>
      <li class="gtw-11-glass relative isolate overflow-hidden grid gap-[0.2rem] min-w-0 px-4 py-[0.85rem] rounded-[14px] border border-gtw11-rim shadow-[inset_0_1px_0_var(--gtw11-rim)] transition-[translate] duration-[280ms] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="absolute inset-0 z-[2] pointer-events-none rounded-[inherit] bg-[image:var(--gtw11-noise)] opacity-[var(--gtw11-grain)] mix-blend-overlay"></span>
        <span class="relative z-[3] font-gtw11-mono text-[0.68rem] leading-none tracking-[0.12em] uppercase text-gtw11-ink">saturate</span>
        <span class="relative z-[3] font-gtw11-mono text-[1.05rem] font-semibold leading-tight">1.4</span>
      </li>
      <li class="gtw-11-glass relative isolate overflow-hidden grid gap-[0.2rem] min-w-0 px-4 py-[0.85rem] rounded-[14px] border border-gtw11-rim shadow-[inset_0_1px_0_var(--gtw11-rim)] transition-[translate] duration-[280ms] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="absolute inset-0 z-[2] pointer-events-none rounded-[inherit] bg-[image:var(--gtw11-noise)] opacity-[var(--gtw11-grain)] mix-blend-overlay"></span>
        <span class="relative z-[3] font-gtw11-mono text-[0.68rem] leading-none tracking-[0.12em] uppercase text-gtw11-ink">grain</span>
        <span class="relative z-[3] font-gtw11-mono text-[1.05rem] font-semibold leading-tight">0.08</span>
      </li>
      <li class="gtw-11-glass relative isolate overflow-hidden grid gap-[0.2rem] min-w-0 px-4 py-[0.85rem] rounded-[14px] border border-gtw11-rim shadow-[inset_0_1px_0_var(--gtw11-rim)] transition-[translate] duration-[280ms] hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <span aria-hidden="true" class="absolute inset-0 z-[2] pointer-events-none rounded-[inherit] bg-[image:var(--gtw11-noise)] opacity-[var(--gtw11-grain)] mix-blend-overlay"></span>
        <span class="relative z-[3] font-gtw11-mono text-[0.68rem] leading-none tracking-[0.12em] uppercase text-gtw11-ink">fallback</span>
        <span class="relative z-[3] font-gtw11-mono text-[1.05rem] font-semibold leading-tight">@supports</span>
      </li>
    </ul>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw11-ink: #f4f6fb;
  --color-gtw11-ink: oklch(0.97 0.008 265);
  --color-gtw11-rim: rgba(255, 255, 255, 0.26);
  --color-gtw11-acc: #7dd3fc;
  --color-gtw11-acc: oklch(0.84 0.1 226);
  --font-gtw11-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw11-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-11 {
  width: 100%;
  min-height: 100svh;
  --gtw11-blur: 18px;
  --gtw11-grain: 0.08;
  --gtw11-rim: rgba(255, 255, 255, 0.26);
  --gtw11-glass: oklch(0.18 0.02 265 / 0.34);
  --gtw11-glass-solid: oklch(0.18 0.02 265 / 0.9);
  --gtw11-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='gtw11n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23gtw11n)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}
/* Capability check, inverted on purpose: the base rule is nearly opaque so text stays legible
   without a blur, and only engines that support backdrop-filter get the translucent glass.
   Tailwind has no @supports variant worth writing here, and no -webkit- prefixed property. */

.gtw-11-glass {
  background: var(--gtw11-glass-solid);
}

@supports ((-webkit-backdrop-filter: blur(1px)) or (backdrop-filter: blur(1px))) {
  .gtw-11-glass {
    background: var(--gtw11-glass);
    -webkit-backdrop-filter: blur(var(--gtw11-blur)) saturate(1.4);
    backdrop-filter: blur(var(--gtw11-blur)) saturate(1.4);
  }
}

.gtw-11:has(.gtw-11-theme:checked) {
  --color-gtw11-ink: #0d1016;
  --color-gtw11-ink: oklch(0.19 0.015 265);
  --color-gtw11-acc: #0369a1;
  --color-gtw11-acc: oklch(0.48 0.11 235);
  --color-gtw11-rim: rgba(255, 255, 255, 0.8);
  --gtw11-rim: rgba(255, 255, 255, 0.8);
  --gtw11-glass: oklch(0.98 0.003 265 / 0.42);
  --gtw11-glass-solid: oklch(0.98 0.003 265 / 0.94);
  --gtw11-grain: 0.06;
}

@media (prefers-color-scheme: light) {
  .gtw-11 {
    --color-gtw11-ink: #0d1016;
    --color-gtw11-ink: oklch(0.19 0.015 265);
    --color-gtw11-acc: #0369a1;
    --color-gtw11-acc: oklch(0.48 0.11 235);
    --color-gtw11-rim: rgba(255, 255, 255, 0.8);
    --gtw11-rim: rgba(255, 255, 255, 0.8);
    --gtw11-glass: oklch(0.98 0.003 265 / 0.42);
    --gtw11-glass-solid: oklch(0.98 0.003 265 / 0.94);
    --gtw11-grain: 0.06;
  }

  .gtw-11:has(.gtw-11-theme:checked) {
    --color-gtw11-ink: #f4f6fb;
    --color-gtw11-ink: oklch(0.97 0.008 265);
    --color-gtw11-acc: #7dd3fc;
    --color-gtw11-acc: oklch(0.84 0.1 226);
    --color-gtw11-rim: rgba(255, 255, 255, 0.26);
    --gtw11-rim: rgba(255, 255, 255, 0.26);
    --gtw11-glass: oklch(0.18 0.02 265 / 0.34);
    --gtw11-glass-solid: oklch(0.18 0.02 265 / 0.9);
    --gtw11-grain: 0.08;
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-11:has(.gtw-11-theme:checked) {
    --color-gtw11-ink: #0d1016;
    --color-gtw11-ink: oklch(0.19 0.015 265);
    --color-gtw11-acc: #0369a1;
    --color-gtw11-acc: oklch(0.48 0.11 235);
    --color-gtw11-rim: rgba(255, 255, 255, 0.8);
    --gtw11-rim: rgba(255, 255, 255, 0.8);
    --gtw11-glass: oklch(0.98 0.003 265 / 0.42);
    --gtw11-glass-solid: oklch(0.98 0.003 265 / 0.94);
    --gtw11-grain: 0.06;
  }
}
```
