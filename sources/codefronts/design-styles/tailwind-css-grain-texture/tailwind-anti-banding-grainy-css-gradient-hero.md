---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-anti-banding-grainy-css-gradient-hero/"
title: "Tailwind Anti-Banding Grainy CSS Gradient Hero"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Banding is not a bug in your gradient, it is the 8-bit display pipeline showing through — and the fix is the one film and print have used for a century: add…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Anti-Banding Grainy CSS Gradient Hero
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-anti-banding-grainy-css-gradient-hero/

Banding is not a bug in your gradient, it is the 8-bit display pipeline showing through — and the fix is the one film and print have used for a century: add noise. A full-bleed dusk hero interpolated in oklab, stopped through the dark third, dithered at 3.5%, plus a side-by-side of the same ramp treated and untreated.
## HTML
```html
<section class="gtw-07 relative block w-full min-h-svh bg-gtw07-bg text-gtw07-ink" aria-labelledby="gtw-07-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-07-theme" class="gtw-07-theme peer sr-only">
    <label for="gtw-07-theme" class="grid place-items-center w-11 h-11 rounded-full border border-white/30 bg-[oklch(0.15_0.03_280/0.4)] backdrop-blur-[6px] text-white cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw07-c4 peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative isolate overflow-hidden grid items-end min-h-[min(86svh,46rem)] bg-[radial-gradient(120%_90%_at_78%_6%,color-mix(in_oklab,var(--color-gtw07-c4)_55%,transparent)_0%,transparent_58%),linear-gradient(in_oklab_168deg,var(--color-gtw07-c1)_0%,var(--color-gtw07-c1)_14%,var(--color-gtw07-c2)_38%,var(--color-gtw07-c2)_48%,var(--color-gtw07-c3)_74%,var(--color-gtw07-c4)_100%)] after:content-[''] after:absolute after:inset-0 after:z-[1] after:pointer-events-none after:bg-[image:var(--gtw07-noise)] after:opacity-[var(--gtw07-dither)] after:mix-blend-overlay">
    <div class="relative z-[2] w-[min(70rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto py-[clamp(4rem,12vw,7rem)] grid gap-[0.85rem] max-w-[44rem]">
      <p class="m-0 font-gtw07-mono text-[0.74rem] font-medium leading-none tracking-[0.18em] uppercase text-gtw07-ink">Dusk · 21:04 · clear</p>
      <h1 id="gtw-07-title" class="m-0 font-gtw07-display text-[clamp(2.3rem,7vw,4.6rem)] font-semibold leading-[0.99] tracking-[-0.04em] text-balance">A gradient with nowhere to hide</h1>
      <p class="m-0 max-w-[34rem] text-gtw07-ink text-[clamp(0.97rem,2vw,1.14rem)] text-pretty">Deep blue to violet across a full viewport is the hardest banding case on the web. This one is interpolated in <code class="font-gtw07-mono text-[0.9em]">oklab</code>, stopped three times through the dark third, and dithered with grain at 3.5%.</p>
      <dl class="flex flex-wrap gap-2 mt-2 mb-0">
        <div class="grid gap-[0.1rem] px-[0.85rem] py-[0.55rem] rounded-[10px] border border-white/25 bg-[oklch(0.12_0.03_280/0.35)] backdrop-blur-[4px]"><dt class="m-0 font-gtw07-mono text-[0.68rem] leading-none tracking-[0.1em] uppercase text-white/80">Interpolation</dt><dd class="m-0 font-gtw07-mono text-[0.88rem] font-medium leading-tight text-white">in oklab</dd></div>
        <div class="grid gap-[0.1rem] px-[0.85rem] py-[0.55rem] rounded-[10px] border border-white/25 bg-[oklch(0.12_0.03_280/0.35)] backdrop-blur-[4px]"><dt class="m-0 font-gtw07-mono text-[0.68rem] leading-none tracking-[0.1em] uppercase text-white/80">Dither</dt><dd class="m-0 font-gtw07-mono text-[0.88rem] font-medium leading-tight text-white">0.035</dd></div>
        <div class="grid gap-[0.1rem] px-[0.85rem] py-[0.55rem] rounded-[10px] border border-white/25 bg-[oklch(0.12_0.03_280/0.35)] backdrop-blur-[4px]"><dt class="m-0 font-gtw07-mono text-[0.68rem] leading-none tracking-[0.1em] uppercase text-white/80">Stops</dt><dd class="m-0 font-gtw07-mono text-[0.88rem] font-medium leading-tight text-white">6</dd></div>
      </dl>
    </div>
  </header>

  <main class="w-[min(70rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto py-[clamp(2.5rem,7vw,4.5rem)] grid gap-[clamp(2rem,5vw,3rem)]">
    <section class="grid gap-4" aria-labelledby="gtw-07-h-ab">
      <div class="grid gap-[0.35rem] pb-[0.7rem] border-b border-gtw07-line">
        <h2 id="gtw-07-h-ab" class="m-0 font-gtw07-display text-[clamp(1.15rem,2.8vw,1.5rem)] font-semibold leading-tight tracking-[-0.02em]">The same ramp, treated and untreated</h2>
        <p class="m-0 text-gtw07-mut text-[0.88rem] text-pretty">If you cannot see the difference, turn your screen brightness down — banding lives in the shadows.</p>
      </div>
      <div class="grid gap-[clamp(0.8rem,2vw,1.3rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,17rem),1fr))]">
        <figure class="m-0 grid gap-[0.6rem] min-w-0">
          <div class="relative isolate overflow-hidden h-[clamp(11rem,26vw,17rem)] rounded-[14px] bg-[linear-gradient(168deg,var(--color-gtw07-c1),var(--color-gtw07-c3))]"></div>
          <figcaption class="grid gap-[0.15rem]"><b class="font-gtw07-display text-[0.95rem] font-semibold leading-tight">Untreated</b><span class="font-gtw07-mono text-[0.8rem] leading-[1.4] text-gtw07-mut">sRGB interpolation, two stops, no dither</span></figcaption>
        </figure>
        <figure class="m-0 grid gap-[0.6rem] min-w-0">
          <div class="relative isolate overflow-hidden h-[clamp(11rem,26vw,17rem)] rounded-[14px] bg-[linear-gradient(in_oklab_168deg,var(--color-gtw07-c1)_0%,var(--color-gtw07-c1)_12%,var(--color-gtw07-c2)_34%,var(--color-gtw07-c2)_46%,var(--color-gtw07-c3)_78%,var(--color-gtw07-c3)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw07-noise)] after:opacity-[var(--gtw07-dither)] after:mix-blend-overlay"></div>
          <figcaption class="grid gap-[0.15rem]"><b class="font-gtw07-display text-[0.95rem] font-semibold leading-tight">Treated</b><span class="font-gtw07-mono text-[0.8rem] leading-[1.4] text-gtw07-mut">oklab, six stops, 3.5% grain dither</span></figcaption>
        </figure>
      </div>
    </section>

    <section class="grid gap-[0.9rem] p-[clamp(1.2rem,3vw,1.9rem)] rounded-2xl border border-gtw07-line bg-gtw07-surf" aria-labelledby="gtw-07-h-steps">
      <h2 id="gtw-07-h-steps" class="m-0 font-gtw07-display text-[clamp(1.15rem,2.8vw,1.5rem)] font-semibold leading-tight tracking-[-0.02em]">Ship it in this order</h2>
      <ol class="m-0 pl-[1.3rem] grid gap-[0.55rem] text-gtw07-mut text-[0.92rem] marker:text-gtw07-c4">
        <li><b class="font-semibold text-gtw07-ink">Interpolate in oklab.</b> Perceptually even steps mean smaller bands before you dither anything.</li>
        <li><b class="font-semibold text-gtw07-ink">Add stops where it bands.</b> Almost always the darkest third. Two extra stops halve the step size.</li>
        <li><b class="font-semibold text-gtw07-ink">Dither with grain at 0.03.</b> Raise in 0.005 increments until the bands go. Stop there.</li>
        <li><b class="font-semibold text-gtw07-ink">Check on an OLED phone at low brightness.</b> The harshest banding test that exists, and the one nobody runs.</li>
      </ol>
    </section>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw07-c1: #060b1f;
  --color-gtw07-c1: oklch(0.18 0.06 268);
  --color-gtw07-c2: #21215c;
  --color-gtw07-c2: oklch(0.32 0.11 280);
  --color-gtw07-c3: #6d3f8f;
  --color-gtw07-c3: oklch(0.48 0.15 310);
  --color-gtw07-c4: #d97757;
  --color-gtw07-c4: oklch(0.7 0.13 40);
  --color-gtw07-bg: #08060f;
  --color-gtw07-bg: oklch(0.13 0.02 285);
  --color-gtw07-surf: #120f1d;
  --color-gtw07-surf: oklch(0.19 0.03 285);
  --color-gtw07-line: #262138;
  --color-gtw07-line: oklch(0.29 0.04 285);
  --color-gtw07-ink: #f2eefb;
  --color-gtw07-ink: oklch(0.96 0.015 290);
  --color-gtw07-mut: #a49bbd;
  --color-gtw07-mut: oklch(0.71 0.04 290);
  --font-gtw07-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw07-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-07 {
  width: 100%;
  min-height: 100svh;
  --gtw07-dither: 0.035;
  --gtw07-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='gtw07n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23gtw07n)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-07:has(.gtw-07-theme:checked) {
  --color-gtw07-bg: #f4f1fa;
  --color-gtw07-bg: oklch(0.96 0.01 290);
  --color-gtw07-surf: #ffffff;
  --color-gtw07-surf: oklch(1 0 0);
  --color-gtw07-line: #e2dcf0;
  --color-gtw07-line: oklch(0.9 0.02 290);
  --color-gtw07-ink: #120f1d;
  --color-gtw07-ink: oklch(0.19 0.03 285);
  --color-gtw07-mut: #625a7c;
  --color-gtw07-mut: oklch(0.49 0.05 290);
  --color-gtw07-c1: #dfd8f2;
  --color-gtw07-c1: oklch(0.89 0.04 290);
  --color-gtw07-c2: #a99ede;
  --color-gtw07-c2: oklch(0.74 0.09 288);
  --color-gtw07-c3: #c68fb8;
  --color-gtw07-c3: oklch(0.72 0.1 340);
  --color-gtw07-c4: #f0b083;
  --color-gtw07-c4: oklch(0.82 0.1 55);
  --gtw07-dither: 0.03;
}

@media (prefers-color-scheme: light) {
  .gtw-07 {
    --color-gtw07-bg: #f4f1fa;
    --color-gtw07-bg: oklch(0.96 0.01 290);
    --color-gtw07-surf: #ffffff;
    --color-gtw07-surf: oklch(1 0 0);
    --color-gtw07-line: #e2dcf0;
    --color-gtw07-line: oklch(0.9 0.02 290);
    --color-gtw07-ink: #120f1d;
    --color-gtw07-ink: oklch(0.19 0.03 285);
    --color-gtw07-mut: #625a7c;
    --color-gtw07-mut: oklch(0.49 0.05 290);
    --color-gtw07-c1: #dfd8f2;
    --color-gtw07-c1: oklch(0.89 0.04 290);
    --color-gtw07-c2: #a99ede;
    --color-gtw07-c2: oklch(0.74 0.09 288);
    --color-gtw07-c3: #c68fb8;
    --color-gtw07-c3: oklch(0.72 0.1 340);
    --color-gtw07-c4: #f0b083;
    --color-gtw07-c4: oklch(0.82 0.1 55);
    --gtw07-dither: 0.03;
  }

  .gtw-07:has(.gtw-07-theme:checked) {
    --color-gtw07-bg: #08060f;
    --color-gtw07-bg: oklch(0.13 0.02 285);
    --color-gtw07-surf: #120f1d;
    --color-gtw07-surf: oklch(0.19 0.03 285);
    --color-gtw07-line: #262138;
    --color-gtw07-line: oklch(0.29 0.04 285);
    --color-gtw07-ink: #f2eefb;
    --color-gtw07-ink: oklch(0.96 0.015 290);
    --color-gtw07-mut: #a49bbd;
    --color-gtw07-mut: oklch(0.71 0.04 290);
    --color-gtw07-c1: #060b1f;
    --color-gtw07-c1: oklch(0.18 0.06 268);
    --color-gtw07-c2: #21215c;
    --color-gtw07-c2: oklch(0.32 0.11 280);
    --color-gtw07-c3: #6d3f8f;
    --color-gtw07-c3: oklch(0.48 0.15 310);
    --color-gtw07-c4: #d97757;
    --color-gtw07-c4: oklch(0.7 0.13 40);
    --gtw07-dither: 0.035;
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-07:has(.gtw-07-theme:checked) {
    --color-gtw07-bg: #f4f1fa;
    --color-gtw07-bg: oklch(0.96 0.01 290);
    --color-gtw07-surf: #ffffff;
    --color-gtw07-surf: oklch(1 0 0);
    --color-gtw07-line: #e2dcf0;
    --color-gtw07-line: oklch(0.9 0.02 290);
    --color-gtw07-ink: #120f1d;
    --color-gtw07-ink: oklch(0.19 0.03 285);
    --color-gtw07-mut: #625a7c;
    --color-gtw07-mut: oklch(0.49 0.05 290);
    --color-gtw07-c1: #dfd8f2;
    --color-gtw07-c1: oklch(0.89 0.04 290);
    --color-gtw07-c2: #a99ede;
    --color-gtw07-c2: oklch(0.74 0.09 288);
    --color-gtw07-c3: #c68fb8;
    --color-gtw07-c3: oklch(0.72 0.1 340);
    --color-gtw07-c4: #f0b083;
    --color-gtw07-c4: oklch(0.82 0.1 55);
    --gtw07-dither: 0.03;
  }
}
```
