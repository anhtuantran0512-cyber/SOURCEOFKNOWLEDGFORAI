---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-tinted-svg-noise-fecolormatrix/"
title: "Tailwind Tinted SVG Noise with feColorMatrix"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Raw feTurbulence writes independent noise into red, green and blue, so untinted grain is colour confetti."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tinted SVG Noise with feColorMatrix
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-tinted-svg-noise-fecolormatrix/

Raw feTurbulence writes independent noise into red, green and blue, so untinted grain is colour confetti. feColorMatrix fixes it properly: flatten RGB to one hue, then move the texture into the alpha channel so the layer composites in normal blend mode over anything. Six named stocks, and the port's point is that the filter chain is the only part that cannot become a utility — so everything else does.
## HTML
```html
<section class="gtw-05 relative block w-full min-h-svh bg-gtw05-bg text-gtw05-ink" aria-labelledby="gtw-05-title">
  <svg class="absolute w-0 h-0 overflow-hidden" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="gtw-05-amber" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" seed="12" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.98  0 0 0 0 0.66  0 0 0 0 0.19  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.35 0.9"/></feComponentTransfer>
    </filter>
    <filter id="gtw-05-cyan" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="5" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.13  0 0 0 0 0.78  0 0 0 0 0.85  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.3 0.85"/></feComponentTransfer>
    </filter>
    <filter id="gtw-05-magenta" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="4" seed="19" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.86  0 0 0 0 0.12  0 0 0 0 0.55  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.4 1"/></feComponentTransfer>
    </filter>
    <filter id="gtw-05-neutral" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="31" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <filter id="gtw-05-olive" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="turbulence" baseFrequency="0.45" numOctaves="2" seed="8" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.55  0 0 0 0 0.62  0 0 0 0 0.24  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.28 0.7"/></feComponentTransfer>
    </filter>
    <filter id="gtw-05-ink" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="44" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.05  0 0 0 0 0.06  0 0 0 0 0.09  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.5 1"/></feComponentTransfer>
    </filter>
  </svg>

  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-05-theme" class="gtw-05-theme peer sr-only">
    <label for="gtw-05-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw05-line bg-gtw05-surf text-gtw05-ink cursor-pointer transition-colors duration-200 hover:border-gtw05-acc peer-focus-visible:outline-2 peer-focus-visible:outline-gtw05-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(78rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2rem,5vw,3.2rem)]">
    <header class="max-w-[46rem] grid gap-3">
      <p class="m-0 font-gtw05-mono text-[0.72rem] font-medium tracking-[0.18em] uppercase text-gtw05-acc">Stock library · 05</p>
      <h1 id="gtw-05-title" class="m-0 font-gtw05-display text-[clamp(2rem,5.4vw,3.5rem)] font-semibold leading-[1.03] tracking-[-0.035em] text-balance">Tinted grain, one hue, no confetti</h1>
      <p class="m-0 max-w-[40rem] text-gtw05-mut text-[clamp(0.95rem,1.9vw,1.09rem)] text-pretty">Six filter chains. Each flattens the noise to a single tint with <code class="font-gtw05-mono text-[0.9em]">feColorMatrix</code> and moves the texture into the alpha channel, so the grain composites in <code class="font-gtw05-mono text-[0.9em]">normal</code> blend mode over anything.</p>
    </header>

    <ul class="list-none m-0 p-0 grid gap-[clamp(1rem,2.4vw,1.5rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]">
      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-2xl border border-gtw05-line bg-gtw05-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw05-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Warm amber tinted grain over a magenta and teal gradient" class="relative h-[clamp(9rem,19vw,11.5rem)] bg-[linear-gradient(135deg,var(--color-gtw05-acc)_0%,color-mix(in_oklab,var(--color-gtw05-acc)_40%,var(--color-gtw05-acc2))_52%,var(--color-gtw05-acc2)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw05-op)] after:[filter:url(#gtw-05-amber)]"></div>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.2vw,1.35rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw05-display text-[1.05rem] font-semibold leading-tight">Amber 400</h2><span class="font-gtw05-mono text-[0.7rem] leading-none tracking-[0.1em] uppercase text-gtw05-mut">warm</span></div>
          <p class="m-0 text-gtw05-mut text-[0.87rem] text-pretty">Tungsten-balanced press texture. Reads as paper warmth on cream surfaces.</p>
          <code class="justify-self-start px-[0.55rem] py-[0.25rem] rounded-md bg-[color-mix(in_oklab,var(--color-gtw05-acc)_14%,transparent)] font-gtw05-mono text-[0.76rem] tracking-[0.04em]">0.98 0.66 0.19</code>
        </div>
      </li>
      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-2xl border border-gtw05-line bg-gtw05-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw05-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Cool cyan tinted grain over a magenta and teal gradient" class="relative h-[clamp(9rem,19vw,11.5rem)] bg-[linear-gradient(135deg,var(--color-gtw05-acc)_0%,color-mix(in_oklab,var(--color-gtw05-acc)_40%,var(--color-gtw05-acc2))_52%,var(--color-gtw05-acc2)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw05-op)] after:[filter:url(#gtw-05-cyan)]"></div>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.2vw,1.35rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw05-display text-[1.05rem] font-semibold leading-tight">Cyan 200</h2><span class="font-gtw05-mono text-[0.7rem] leading-none tracking-[0.1em] uppercase text-gtw05-mut">cool</span></div>
          <p class="m-0 text-gtw05-mut text-[0.87rem] text-pretty">Daylight stock. The safest tint for dark product UI — it lifts without yellowing.</p>
          <code class="justify-self-start px-[0.55rem] py-[0.25rem] rounded-md bg-[color-mix(in_oklab,var(--color-gtw05-acc)_14%,transparent)] font-gtw05-mono text-[0.76rem] tracking-[0.04em]">0.13 0.78 0.85</code>
        </div>
      </li>
      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-2xl border border-gtw05-line bg-gtw05-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw05-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Hot magenta tinted grain over a magenta and teal gradient" class="relative h-[clamp(9rem,19vw,11.5rem)] bg-[linear-gradient(135deg,var(--color-gtw05-acc)_0%,color-mix(in_oklab,var(--color-gtw05-acc)_40%,var(--color-gtw05-acc2))_52%,var(--color-gtw05-acc2)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw05-op)] after:[filter:url(#gtw-05-magenta)]"></div>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.2vw,1.35rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw05-display text-[1.05rem] font-semibold leading-tight">Magenta 700</h2><span class="font-gtw05-mono text-[0.7rem] leading-none tracking-[0.1em] uppercase text-gtw05-mut">hot</span></div>
          <p class="m-0 text-gtw05-mut text-[0.87rem] text-pretty">Four octaves and a hard alpha table. Editorial covers, not settings screens.</p>
          <code class="justify-self-start px-[0.55rem] py-[0.25rem] rounded-md bg-[color-mix(in_oklab,var(--color-gtw05-acc)_14%,transparent)] font-gtw05-mono text-[0.76rem] tracking-[0.04em]">0.86 0.12 0.55</code>
        </div>
      </li>
      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-2xl border border-gtw05-line bg-gtw05-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw05-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Neutral grey grain over a magenta and teal gradient" class="relative isolate h-[clamp(9rem,19vw,11.5rem)] bg-[linear-gradient(135deg,var(--color-gtw05-acc)_0%,color-mix(in_oklab,var(--color-gtw05-acc)_40%,var(--color-gtw05-acc2))_52%,var(--color-gtw05-acc2)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw05-op)] after:[filter:url(#gtw-05-neutral)] after:mix-blend-overlay"></div>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.2vw,1.35rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw05-display text-[1.05rem] font-semibold leading-tight">Neutral</h2><span class="font-gtw05-mono text-[0.7rem] leading-none tracking-[0.1em] uppercase text-gtw05-mut">saturate 0</span></div>
          <p class="m-0 text-gtw05-mut text-[0.87rem] text-pretty">The one-line version. No tint, no alpha shaping, correct for 90% of interfaces.</p>
          <code class="justify-self-start px-[0.55rem] py-[0.25rem] rounded-md bg-[color-mix(in_oklab,var(--color-gtw05-acc)_14%,transparent)] font-gtw05-mono text-[0.76rem] tracking-[0.04em]">saturate · 0</code>
        </div>
      </li>
      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-2xl border border-gtw05-line bg-gtw05-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw05-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Olive veined turbulence over a magenta and teal gradient" class="relative h-[clamp(9rem,19vw,11.5rem)] bg-[linear-gradient(135deg,var(--color-gtw05-acc)_0%,color-mix(in_oklab,var(--color-gtw05-acc)_40%,var(--color-gtw05-acc2))_52%,var(--color-gtw05-acc2)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw05-op)] after:[filter:url(#gtw-05-olive)]"></div>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.2vw,1.35rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw05-display text-[1.05rem] font-semibold leading-tight">Olive Veil</h2><span class="font-gtw05-mono text-[0.7rem] leading-none tracking-[0.1em] uppercase text-gtw05-mut">turbulence</span></div>
          <p class="m-0 text-gtw05-mut text-[0.87rem] text-pretty">Low-frequency turbulence, soft alpha table. Cloth and clay surfaces.</p>
          <code class="justify-self-start px-[0.55rem] py-[0.25rem] rounded-md bg-[color-mix(in_oklab,var(--color-gtw05-acc)_14%,transparent)] font-gtw05-mono text-[0.76rem] tracking-[0.04em]">0.55 0.62 0.24</code>
        </div>
      </li>
      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-2xl border border-gtw05-line bg-gtw05-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw05-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Near-black ink grain over a magenta and teal gradient" class="relative h-[clamp(9rem,19vw,11.5rem)] bg-[linear-gradient(135deg,var(--color-gtw05-acc)_0%,color-mix(in_oklab,var(--color-gtw05-acc)_40%,var(--color-gtw05-acc2))_52%,var(--color-gtw05-acc2)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw05-op)] after:[filter:url(#gtw-05-ink)]"></div>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.2vw,1.35rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw05-display text-[1.05rem] font-semibold leading-tight">Ink 950</h2><span class="font-gtw05-mono text-[0.7rem] leading-none tracking-[0.1em] uppercase text-gtw05-mut">dense</span></div>
          <p class="m-0 text-gtw05-mut text-[0.87rem] text-pretty">High frequency, full alpha range. The only stock that survives on white.</p>
          <code class="justify-self-start px-[0.55rem] py-[0.25rem] rounded-md bg-[color-mix(in_oklab,var(--color-gtw05-acc)_14%,transparent)] font-gtw05-mono text-[0.76rem] tracking-[0.04em]">0.05 0.06 0.09</code>
        </div>
      </li>
    </ul>

    <aside class="grid gap-[0.6rem] p-[clamp(1.2rem,3vw,1.9rem)] rounded-2xl border border-gtw05-line bg-gtw05-surf">
      <h2 class="m-0 font-gtw05-display text-[clamp(1.1rem,2.6vw,1.35rem)] font-semibold leading-tight">Why the alpha row matters</h2>
      <p class="m-0 max-w-[52rem] text-gtw05-mut text-[0.92rem] text-pretty">The alpha row <code class="font-gtw05-mono text-[0.9em]">0.33 0.33 0.33 0 0</code> computes coverage from the incoming luminance. Without it, zeroed RGB rows paint a solid rectangle of flat tint — the most common way this chain fails. With it, the noise decides where the tint lands, the hue never varies, and the layer needs no blend mode at all.</p>
    </aside>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw05-bg: #12060f;
  --color-gtw05-bg: oklch(0.16 0.04 350);
  --color-gtw05-surf: #1e0c19;
  --color-gtw05-surf: oklch(0.22 0.06 350);
  --color-gtw05-line: #3a1830;
  --color-gtw05-line: oklch(0.31 0.08 350);
  --color-gtw05-ink: #fdeaf7;
  --color-gtw05-ink: oklch(0.95 0.03 350);
  --color-gtw05-mut: #c093b3;
  --color-gtw05-mut: oklch(0.73 0.06 350);
  --color-gtw05-acc: #f472b6;
  --color-gtw05-acc: oklch(0.72 0.19 350);
  --color-gtw05-acc2: #2dd4bf;
  --color-gtw05-acc2: oklch(0.78 0.13 180);
  --font-gtw05-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw05-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-05 {
  width: 100%;
  min-height: 100svh;
  --gtw05-op: 0.7;
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-05:has(.gtw-05-theme:checked) {
  --color-gtw05-bg: #fdf2f9;
  --color-gtw05-bg: oklch(0.97 0.015 350);
  --color-gtw05-surf: #ffffff;
  --color-gtw05-surf: oklch(1 0 0);
  --color-gtw05-line: #f2d6e8;
  --color-gtw05-line: oklch(0.9 0.04 350);
  --color-gtw05-ink: #17070f;
  --color-gtw05-ink: oklch(0.2 0.03 350);
  --color-gtw05-mut: #7c5169;
  --color-gtw05-mut: oklch(0.49 0.07 350);
  --color-gtw05-acc: #be185d;
  --color-gtw05-acc: oklch(0.5 0.19 355);
  --color-gtw05-acc2: #0d9488;
  --color-gtw05-acc2: oklch(0.58 0.11 182);
  --gtw05-op: 0.5;
}

@media (prefers-color-scheme: light) {
  .gtw-05 {
    --color-gtw05-bg: #fdf2f9;
    --color-gtw05-bg: oklch(0.97 0.015 350);
    --color-gtw05-surf: #ffffff;
    --color-gtw05-surf: oklch(1 0 0);
    --color-gtw05-line: #f2d6e8;
    --color-gtw05-line: oklch(0.9 0.04 350);
    --color-gtw05-ink: #17070f;
    --color-gtw05-ink: oklch(0.2 0.03 350);
    --color-gtw05-mut: #7c5169;
    --color-gtw05-mut: oklch(0.49 0.07 350);
    --color-gtw05-acc: #be185d;
    --color-gtw05-acc: oklch(0.5 0.19 355);
    --color-gtw05-acc2: #0d9488;
    --color-gtw05-acc2: oklch(0.58 0.11 182);
    --gtw05-op: 0.5;
  }

  .gtw-05:has(.gtw-05-theme:checked) {
    --color-gtw05-bg: #12060f;
    --color-gtw05-bg: oklch(0.16 0.04 350);
    --color-gtw05-surf: #1e0c19;
    --color-gtw05-surf: oklch(0.22 0.06 350);
    --color-gtw05-line: #3a1830;
    --color-gtw05-line: oklch(0.31 0.08 350);
    --color-gtw05-ink: #fdeaf7;
    --color-gtw05-ink: oklch(0.95 0.03 350);
    --color-gtw05-mut: #c093b3;
    --color-gtw05-mut: oklch(0.73 0.06 350);
    --color-gtw05-acc: #f472b6;
    --color-gtw05-acc: oklch(0.72 0.19 350);
    --color-gtw05-acc2: #2dd4bf;
    --color-gtw05-acc2: oklch(0.78 0.13 180);
    --gtw05-op: 0.7;
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-05:has(.gtw-05-theme:checked) {
    --color-gtw05-bg: #fdf2f9;
    --color-gtw05-bg: oklch(0.97 0.015 350);
    --color-gtw05-surf: #ffffff;
    --color-gtw05-surf: oklch(1 0 0);
    --color-gtw05-line: #f2d6e8;
    --color-gtw05-line: oklch(0.9 0.04 350);
    --color-gtw05-ink: #17070f;
    --color-gtw05-ink: oklch(0.2 0.03 350);
    --color-gtw05-mut: #7c5169;
    --color-gtw05-mut: oklch(0.49 0.07 350);
    --color-gtw05-acc: #be185d;
    --color-gtw05-acc: oklch(0.5 0.19 355);
    --color-gtw05-acc2: #0d9488;
    --color-gtw05-acc2: oklch(0.58 0.11 182);
    --gtw05-op: 0.5;
  }
}
```
