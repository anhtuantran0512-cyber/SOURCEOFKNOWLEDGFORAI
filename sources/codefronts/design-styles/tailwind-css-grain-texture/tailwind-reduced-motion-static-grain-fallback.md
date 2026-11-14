---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-reduced-motion-static-grain-fallback/"
title: "Tailwind Reduced Motion Static Grain Fallback"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Animated grain is the single most likely thing in a texture collection to make somebody feel ill — rapid luminance change across a large area is exactly the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Reduced Motion Static Grain Fallback
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-reduced-motion-static-grain-fallback/

Animated grain is the single most likely thing in a texture collection to make somebody feel ill — rapid luminance change across a large area is exactly the trigger for vestibular disorders, migraine and photosensitivity. This demo animates a film gate properly (compositor transforms, steps(8)), and then designs the reduced-motion version instead of switching the animation off.
## HTML
```html
<section class="gtw-20 relative block w-full min-h-svh bg-gtw20-bg text-gtw20-ink" aria-labelledby="gtw-20-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-60">
    <input type="checkbox" id="gtw-20-theme" class="gtw-20-theme peer sr-only">
    <label for="gtw-20-theme" class="grid place-items-center w-11 h-11 rounded-full border border-white/30 bg-[oklch(0.14_0.004_85/0.5)] backdrop-blur-[8px] text-white cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw20-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <div class="relative isolate overflow-hidden grid items-end min-h-[min(82svh,42rem)] bg-[#0b0b0c]">
    <img src="https://picsum.photos/id/1016/2000/1200" alt="" aria-hidden="true" width="2000" height="1200" class="absolute inset-0 z-0 w-full h-full object-cover [filter:grayscale(0.55)_contrast(1.12)_brightness(0.86)_sepia(0.12)] motion-reduce:[filter:grayscale(0.7)_contrast(1.18)_brightness(0.82)_sepia(0.16)]">
    <span aria-hidden="true" class="absolute inset-0 z-[1] pointer-events-none opacity-70 motion-reduce:opacity-45 bg-[repeating-linear-gradient(0deg,rgba(255,255,255,0.035)_0_1px,transparent_1px_3px)]"></span>
    <span aria-hidden="true" class="absolute -inset-[25%] z-[2] pointer-events-none bg-[image:var(--gtw20-noise)] opacity-[var(--gtw20-anim)] mix-blend-overlay animate-gtw20-gate will-change-transform motion-reduce:animate-none motion-reduce:inset-0 motion-reduce:opacity-[var(--gtw20-static)] motion-reduce:mix-blend-soft-light motion-reduce:will-change-auto"></span>
    <span aria-hidden="true" class="absolute inset-0 z-[3] pointer-events-none bg-[radial-gradient(122%_100%_at_50%_44%,transparent_42%,oklch(0.12_0.003_85/0.35)_78%,oklch(0.12_0.003_85/0.66)_100%)] motion-reduce:bg-[radial-gradient(118%_100%_at_50%_42%,transparent_34%,oklch(0.12_0.003_85/0.44)_74%,oklch(0.12_0.003_85/0.78)_100%)]"></span>

    <div class="relative z-[5] w-[min(72rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto grid gap-[0.8rem] max-w-[42rem] py-[clamp(2.5rem,8vw,4.5rem)] text-white">
      <p class="m-0 justify-self-start px-3 py-[0.35rem] rounded-full border border-white/30 bg-[oklch(0.12_0.003_85/0.5)] backdrop-blur-[5px] font-gtw20-mono text-[0.72rem] font-medium leading-[1.4] tracking-[0.1em] uppercase">
        <span class="inline motion-reduce:hidden">Projector running · animated grain</span>
        <span class="hidden motion-reduce:inline">Reduced motion · static frame held</span>
      </p>
      <h1 id="gtw-20-title" class="m-0 font-gtw20-display text-[clamp(2.2rem,7vw,4.4rem)] font-semibold leading-[0.98] tracking-[-0.04em] text-balance">Reel four, gate check</h1>
      <p class="m-0 max-w-[34rem] text-white text-[clamp(0.96rem,2vw,1.11rem)] text-pretty">The grain layer translates on the compositor in eight discrete steps. If your system asks for reduced motion, it stops — and a heavier, deliberately composed static treatment takes over.</p>
    </div>
  </div>

  <main class="w-[min(72rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto py-[clamp(2.5rem,7vw,4rem)] grid gap-[clamp(1.6rem,4vw,2.4rem)]">
    <section class="grid gap-4" aria-labelledby="gtw-20-h-rules">
      <h2 id="gtw-20-h-rules" class="m-0 pb-[0.7rem] border-b border-gtw20-line font-gtw20-display text-[clamp(1.2rem,3vw,1.6rem)] font-semibold leading-tight tracking-[-0.025em]">Four rules for animated texture</h2>
      <ul class="list-none m-0 p-0 grid gap-[clamp(0.7rem,1.8vw,1.1rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))]">
        <li class="relative isolate overflow-hidden grid content-start gap-[0.3rem] min-w-0 p-[clamp(1rem,2.4vw,1.4rem)] rounded-[14px] border border-gtw20-line bg-gtw20-surf after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw20-noise)] after:opacity-[0.05] after:mix-blend-overlay">
          <span class="font-gtw20-mono text-[0.7rem] font-medium leading-none tracking-[0.14em] text-gtw20-acc">01</span>
          <b class="font-gtw20-display text-[0.98rem] font-semibold leading-[1.25] tracking-[-0.01em] text-balance">Translate, never background-position</b>
          <span class="text-gtw20-mut text-[0.85rem] text-pretty">One is a compositor transform. The other repaints a viewport-sized background every frame.</span>
        </li>
        <li class="relative isolate overflow-hidden grid content-start gap-[0.3rem] min-w-0 p-[clamp(1rem,2.4vw,1.4rem)] rounded-[14px] border border-gtw20-line bg-gtw20-surf after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw20-noise)] after:opacity-[0.05] after:mix-blend-overlay">
          <span class="font-gtw20-mono text-[0.7rem] font-medium leading-none tracking-[0.14em] text-gtw20-acc">02</span>
          <b class="font-gtw20-display text-[0.98rem] font-semibold leading-[1.25] tracking-[-0.01em] text-balance">steps(), never linear</b>
          <span class="text-gtw20-mut text-[0.85rem] text-pretty">Film grain jumps between frames. A smooth slide reads as sandpaper being dragged.</span>
        </li>
        <li class="relative isolate overflow-hidden grid content-start gap-[0.3rem] min-w-0 p-[clamp(1rem,2.4vw,1.4rem)] rounded-[14px] border border-gtw20-line bg-gtw20-surf after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw20-noise)] after:opacity-[0.05] after:mix-blend-overlay">
          <span class="font-gtw20-mono text-[0.7rem] font-medium leading-none tracking-[0.14em] text-gtw20-acc">03</span>
          <b class="font-gtw20-display text-[0.98rem] font-semibold leading-[1.25] tracking-[-0.01em] text-balance">Never animate filter: url()</b>
          <span class="text-gtw20-mut text-[0.85rem] text-pretty">The turbulence re-evaluates every frame. Animate a static texture layer instead.</span>
        </li>
        <li class="relative isolate overflow-hidden grid content-start gap-[0.3rem] min-w-0 p-[clamp(1rem,2.4vw,1.4rem)] rounded-[14px] border border-gtw20-line bg-gtw20-surf after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw20-noise)] after:opacity-[0.05] after:mix-blend-overlay">
          <span class="font-gtw20-mono text-[0.7rem] font-medium leading-none tracking-[0.14em] text-gtw20-acc">04</span>
          <b class="font-gtw20-display text-[0.98rem] font-semibold leading-[1.25] tracking-[-0.01em] text-balance">Design the fallback</b>
          <span class="text-gtw20-mut text-[0.85rem] text-pretty">Not <code class="font-gtw20-mono text-[0.9em]">animation: none</code>. Heavier grain, a vignette, one composed frame — a real design.</span>
        </li>
      </ul>
    </section>

    <aside class="grid gap-2 p-[clamp(1.2rem,3vw,1.8rem)] rounded-[14px] border border-gtw20-line bg-[color-mix(in_oklab,var(--color-gtw20-acc)_8%,transparent)]">
      <h2 class="m-0 font-gtw20-display text-[1.05rem] font-semibold leading-tight">Why flicker is the specific risk</h2>
      <p class="m-0 max-w-[52rem] text-gtw20-mut text-[0.92rem] text-pretty">Vestibular disorders, migraine and photosensitivity respond to rapid luminance change over large areas more reliably than to movement. Animated grain is precisely that. If it flickers across a large surface, honour <code class="font-gtw20-mono text-[0.9em]">prefers-reduced-motion</code> without exception — and give those users a treatment you would be happy to ship as the only one.</p>
    </aside>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw20-bg: #0b0b0c;
  --color-gtw20-bg: oklch(0.16 0.003 85);
  --color-gtw20-surf: #16161a;
  --color-gtw20-surf: oklch(0.22 0.005 85);
  --color-gtw20-line: #292930;
  --color-gtw20-line: oklch(0.31 0.008 85);
  --color-gtw20-ink: #f2f1ee;
  --color-gtw20-ink: oklch(0.96 0.005 85);
  --color-gtw20-mut: #9b988f;
  --color-gtw20-mut: oklch(0.69 0.01 85);
  --color-gtw20-acc: #e5c07b;
  --color-gtw20-acc: oklch(0.83 0.11 88);
  --font-gtw20-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw20-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  /* The gate animation as a token: mints animate-gtw20-gate, keyframes below. */
  --animate-gtw20-gate: gtw-20-gate 0.9s steps(8) infinite;
}

@keyframes gtw-20-gate {
  0% {
    transform: translate3d(0, 0, 0);
  }

  12% {
    transform: translate3d(-3%, 2%, 0);
  }

  25% {
    transform: translate3d(4%, -3%, 0);
  }

  37% {
    transform: translate3d(-5%, -1%, 0);
  }

  50% {
    transform: translate3d(2%, 4%, 0);
  }

  62% {
    transform: translate3d(-2%, -4%, 0);
  }

  75% {
    transform: translate3d(5%, 1%, 0);
  }

  87% {
    transform: translate3d(-4%, 3%, 0);
  }

  100% {
    transform: translate3d(0, 0, 0);
  }
}

.gtw-20 {
  width: 100%;
  min-height: 100svh;
  --gtw20-anim: 0.11;
  --gtw20-static: 0.17;
  --gtw20-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='gtw20n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23gtw20n)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-20:has(.gtw-20-theme:checked) {
  --color-gtw20-bg: #f3f2ef;
  --color-gtw20-bg: oklch(0.96 0.004 85);
  --color-gtw20-surf: #ffffff;
  --color-gtw20-surf: oklch(1 0 0);
  --color-gtw20-line: #dedbd4;
  --color-gtw20-line: oklch(0.89 0.008 85);
  --color-gtw20-ink: #0b0b0c;
  --color-gtw20-ink: oklch(0.16 0.003 85);
  --color-gtw20-mut: #615e57;
  --color-gtw20-mut: oklch(0.47 0.01 85);
  --color-gtw20-acc: #8a6314;
  --color-gtw20-acc: oklch(0.5 0.1 78);
}

@media (prefers-color-scheme: light) {
  .gtw-20 {
    --color-gtw20-bg: #f3f2ef;
    --color-gtw20-bg: oklch(0.96 0.004 85);
    --color-gtw20-surf: #ffffff;
    --color-gtw20-surf: oklch(1 0 0);
    --color-gtw20-line: #dedbd4;
    --color-gtw20-line: oklch(0.89 0.008 85);
    --color-gtw20-ink: #0b0b0c;
    --color-gtw20-ink: oklch(0.16 0.003 85);
    --color-gtw20-mut: #615e57;
    --color-gtw20-mut: oklch(0.47 0.01 85);
    --color-gtw20-acc: #8a6314;
    --color-gtw20-acc: oklch(0.5 0.1 78);
  }

  .gtw-20:has(.gtw-20-theme:checked) {
    --color-gtw20-bg: #0b0b0c;
    --color-gtw20-bg: oklch(0.16 0.003 85);
    --color-gtw20-surf: #16161a;
    --color-gtw20-surf: oklch(0.22 0.005 85);
    --color-gtw20-line: #292930;
    --color-gtw20-line: oklch(0.31 0.008 85);
    --color-gtw20-ink: #f2f1ee;
    --color-gtw20-ink: oklch(0.96 0.005 85);
    --color-gtw20-mut: #9b988f;
    --color-gtw20-mut: oklch(0.69 0.01 85);
    --color-gtw20-acc: #e5c07b;
    --color-gtw20-acc: oklch(0.83 0.11 88);
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-20:has(.gtw-20-theme:checked) {
    --color-gtw20-bg: #f3f2ef;
    --color-gtw20-bg: oklch(0.96 0.004 85);
    --color-gtw20-surf: #ffffff;
    --color-gtw20-surf: oklch(1 0 0);
    --color-gtw20-line: #dedbd4;
    --color-gtw20-line: oklch(0.89 0.008 85);
    --color-gtw20-ink: #0b0b0c;
    --color-gtw20-ink: oklch(0.16 0.003 85);
    --color-gtw20-mut: #615e57;
    --color-gtw20-mut: oklch(0.47 0.01 85);
    --color-gtw20-acc: #8a6314;
    --color-gtw20-acc: oklch(0.5 0.1 78);
  }
}
```
