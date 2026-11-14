---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-svg-feturbulence-noise-parameter-breakdown/"
title: "Tailwind SVG feTurbulence Noise Parameter Breakdown"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Every grain effect on the modern web comes out of one SVG primitive: <feTurbulence>."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SVG feTurbulence Noise Parameter Breakdown
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-svg-feturbulence-noise-parameter-breakdown/

Every grain effect on the modern web comes out of one SVG primitive: <feTurbulence>. This is the parameter sheet for it — six live plates, each changing exactly one attribute, plus a zero-JS strength rail that re-tunes all six at once. The port's win is that the entire grain layer (content, inset, filter, blend mode, opacity) reads as one after: class list on the surface that owns it.
## HTML
```html
<section class="gtw-01 relative block w-full min-h-svh bg-gtw01-bg text-gtw01-ink antialiased has-[#gtw-01-op2:checked]:[--gtw01-op:0.2]! has-[#gtw-01-op4:checked]:[--gtw01-op:0.38]! has-[#gtw-01-op6:checked]:[--gtw01-op:0.55]! has-[#gtw-01-op9:checked]:[--gtw01-op:0.8]!" aria-labelledby="gtw-01-title">
  <svg class="absolute w-0 h-0 overflow-hidden" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="gtw-01-fine" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="4" stitchTiles="stitch"/>
    </filter>
    <filter id="gtw-01-coarse" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.16" numOctaves="3" seed="4" stitchTiles="stitch"/>
    </filter>
    <filter id="gtw-01-turb" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="turbulence" baseFrequency="0.55" numOctaves="2" seed="9" stitchTiles="stitch"/>
    </filter>
    <filter id="gtw-01-oct1" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="1" seed="4" stitchTiles="stitch"/>
    </filter>
    <filter id="gtw-01-oct5" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="5" seed="4" stitchTiles="stitch"/>
    </filter>
    <filter id="gtw-01-mono" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="21" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
  </svg>

  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-01-theme" class="gtw-01-theme peer sr-only">
    <label for="gtw-01-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw01-line bg-gtw01-surf text-gtw01-ink cursor-pointer transition-colors duration-200 hover:border-gtw01-acc peer-focus-visible:outline-2 peer-focus-visible:outline-gtw01-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(76rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)]">
    <header class="max-w-[44rem] grid gap-3">
      <p class="m-0 font-gtw01-mono text-[0.72rem] font-medium tracking-[0.18em] uppercase text-gtw01-acc">Texture lab · 01</p>
      <h1 id="gtw-01-title" class="m-0 font-gtw01-display text-[clamp(2rem,5.4vw,3.4rem)] font-semibold leading-[1.04] tracking-[-0.03em] text-balance">Every grain on the web starts here</h1>
      <p class="m-0 max-w-[38rem] text-gtw01-mut text-[clamp(0.95rem,1.9vw,1.09rem)] text-pretty">Six plates. One <code class="font-gtw01-mono text-[0.92em]">&lt;feTurbulence&gt;</code> attribute changed per plate, everything else held constant. Read it as a decision table, not a gallery.</p>
    </header>

    <fieldset class="mt-[clamp(1.6rem,4vw,2.4rem)] m-0 p-0 border-0 flex flex-wrap items-center gap-2">
      <legend class="w-full mb-2 p-0 font-gtw01-mono text-[0.72rem] tracking-[0.14em] uppercase text-gtw01-mut">Composited grain strength</legend>
      <div class="flex flex-wrap gap-2">
        <div class="relative">
          <input type="radio" name="gtw-01-op" id="gtw-01-op2" class="peer sr-only">
          <label for="gtw-01-op2" class="flex items-center justify-center min-w-11 min-h-11 px-4 rounded-xl border border-gtw01-line bg-gtw01-surf font-gtw01-mono text-[0.8rem] text-gtw01-mut cursor-pointer transition-colors duration-200 hover:border-gtw01-acc hover:text-gtw01-ink peer-checked:border-gtw01-acc peer-checked:text-gtw01-ink peer-checked:bg-gtw01-tint peer-focus-visible:outline-2 peer-focus-visible:outline-gtw01-acc peer-focus-visible:outline-offset-2">2%</label>
        </div>
        <div class="relative">
          <input type="radio" name="gtw-01-op" id="gtw-01-op4" class="peer sr-only">
          <label for="gtw-01-op4" class="flex items-center justify-center min-w-11 min-h-11 px-4 rounded-xl border border-gtw01-line bg-gtw01-surf font-gtw01-mono text-[0.8rem] text-gtw01-mut cursor-pointer transition-colors duration-200 hover:border-gtw01-acc hover:text-gtw01-ink peer-checked:border-gtw01-acc peer-checked:text-gtw01-ink peer-checked:bg-gtw01-tint peer-focus-visible:outline-2 peer-focus-visible:outline-gtw01-acc peer-focus-visible:outline-offset-2">4%</label>
        </div>
        <div class="relative">
          <input type="radio" name="gtw-01-op" id="gtw-01-op6" class="peer sr-only" checked>
          <label for="gtw-01-op6" class="flex items-center justify-center min-w-11 min-h-11 px-4 rounded-xl border border-gtw01-line bg-gtw01-surf font-gtw01-mono text-[0.8rem] text-gtw01-mut cursor-pointer transition-colors duration-200 hover:border-gtw01-acc hover:text-gtw01-ink peer-checked:border-gtw01-acc peer-checked:text-gtw01-ink peer-checked:bg-gtw01-tint peer-focus-visible:outline-2 peer-focus-visible:outline-gtw01-acc peer-focus-visible:outline-offset-2">6%</label>
        </div>
        <div class="relative">
          <input type="radio" name="gtw-01-op" id="gtw-01-op9" class="peer sr-only">
          <label for="gtw-01-op9" class="flex items-center justify-center min-w-11 min-h-11 px-4 rounded-xl border border-gtw01-line bg-gtw01-surf font-gtw01-mono text-[0.8rem] text-gtw01-mut cursor-pointer transition-colors duration-200 hover:border-gtw01-acc hover:text-gtw01-ink peer-checked:border-gtw01-acc peer-checked:text-gtw01-ink peer-checked:bg-gtw01-tint peer-focus-visible:outline-2 peer-focus-visible:outline-gtw01-acc peer-focus-visible:outline-offset-2">9%</label>
        </div>
      </div>
    </fieldset>

    <ul class="list-none mt-[clamp(1.4rem,3vw,2rem)] mb-0 p-0 grid gap-[clamp(1rem,2.4vw,1.6rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,17rem),1fr))]">
      <li class="group relative grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw01-line bg-gtw01-surf transition-[border-color,translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:border-gtw01-acc hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Fine even film grain covering a cyan gradient" class="relative isolate h-[clamp(9rem,20vw,12rem)] bg-[linear-gradient(148deg,var(--color-gtw01-acc)_0%,var(--color-gtw01-deep)_58%,var(--color-gtw01-bg)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-overlay after:opacity-[var(--gtw01-op)] after:[filter:url(#gtw-01-fine)] after:transition-opacity after:duration-300 group-hover:after:opacity-[calc(var(--gtw01-op)+0.18)] motion-reduce:after:transition-none"></div>
        <div class="grid content-start gap-[0.6rem] p-[clamp(0.95rem,2vw,1.25rem)]">
          <h2 class="m-0 font-gtw01-display text-[1.02rem] font-semibold leading-tight tracking-[-0.01em]">Fine film grain</h2>
          <dl class="grid grid-cols-[auto_1fr] gap-x-[0.6rem] gap-y-[0.15rem] m-0 py-2 border-y border-gtw01-line font-gtw01-mono text-[0.76rem] leading-[1.5]">
            <dt class="m-0 text-gtw01-mut">type</dt><dd class="m-0 text-gtw01-ink">fractalNoise</dd>
            <dt class="m-0 text-gtw01-mut">baseFrequency</dt><dd class="m-0 text-gtw01-ink">0.9</dd>
            <dt class="m-0 text-gtw01-mut">numOctaves</dt><dd class="m-0 text-gtw01-ink">3</dd>
          </dl>
          <p class="m-0 text-gtw01-mut text-[0.86rem] text-pretty">The production default. Reads as photographic tooth at any size.</p>
        </div>
      </li>

      <li class="group relative grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw01-line bg-gtw01-surf transition-[border-color,translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:border-gtw01-acc hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Coarse cloudy noise covering a cyan gradient" class="relative isolate h-[clamp(9rem,20vw,12rem)] bg-[linear-gradient(148deg,var(--color-gtw01-acc)_0%,var(--color-gtw01-deep)_58%,var(--color-gtw01-bg)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-overlay after:opacity-[var(--gtw01-op)] after:[filter:url(#gtw-01-coarse)] after:transition-opacity after:duration-300 group-hover:after:opacity-[calc(var(--gtw01-op)+0.18)] motion-reduce:after:transition-none"></div>
        <div class="grid content-start gap-[0.6rem] p-[clamp(0.95rem,2vw,1.25rem)]">
          <h2 class="m-0 font-gtw01-display text-[1.02rem] font-semibold leading-tight tracking-[-0.01em]">Coarse cloud</h2>
          <dl class="grid grid-cols-[auto_1fr] gap-x-[0.6rem] gap-y-[0.15rem] m-0 py-2 border-y border-gtw01-line font-gtw01-mono text-[0.76rem] leading-[1.5]">
            <dt class="m-0 text-gtw01-mut">type</dt><dd class="m-0 text-gtw01-ink">fractalNoise</dd>
            <dt class="m-0 text-gtw01-mut">baseFrequency</dt><dd class="m-0 text-gtw01-ink">0.16</dd>
            <dt class="m-0 text-gtw01-mut">numOctaves</dt><dd class="m-0 text-gtw01-ink">3</dd>
          </dl>
          <p class="m-0 text-gtw01-mut text-[0.86rem] text-pretty">Same filter, one dial. Low frequency stops being grain and becomes weather.</p>
        </div>
      </li>

      <li class="group relative grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw01-line bg-gtw01-surf transition-[border-color,translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:border-gtw01-acc hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Veined marble-like turbulence over a cyan gradient" class="relative isolate h-[clamp(9rem,20vw,12rem)] bg-[linear-gradient(148deg,var(--color-gtw01-acc)_0%,var(--color-gtw01-deep)_58%,var(--color-gtw01-bg)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-overlay after:opacity-[var(--gtw01-op)] after:[filter:url(#gtw-01-turb)] after:transition-opacity after:duration-300 group-hover:after:opacity-[calc(var(--gtw01-op)+0.18)] motion-reduce:after:transition-none"></div>
        <div class="grid content-start gap-[0.6rem] p-[clamp(0.95rem,2vw,1.25rem)]">
          <h2 class="m-0 font-gtw01-display text-[1.02rem] font-semibold leading-tight tracking-[-0.01em]">Veined turbulence</h2>
          <dl class="grid grid-cols-[auto_1fr] gap-x-[0.6rem] gap-y-[0.15rem] m-0 py-2 border-y border-gtw01-line font-gtw01-mono text-[0.76rem] leading-[1.5]">
            <dt class="m-0 text-gtw01-mut">type</dt><dd class="m-0 text-gtw01-ink">turbulence</dd>
            <dt class="m-0 text-gtw01-mut">baseFrequency</dt><dd class="m-0 text-gtw01-ink">0.55</dd>
            <dt class="m-0 text-gtw01-mut">numOctaves</dt><dd class="m-0 text-gtw01-ink">2</dd>
          </dl>
          <p class="m-0 text-gtw01-mut text-[0.86rem] text-pretty"><code class="font-gtw01-mono text-[0.92em]">turbulence</code> takes absolute values, so it creases. Marble, smoke, ink.</p>
        </div>
      </li>

      <li class="group relative grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw01-line bg-gtw01-surf transition-[border-color,translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:border-gtw01-acc hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Smooth single-octave noise over a cyan gradient" class="relative isolate h-[clamp(9rem,20vw,12rem)] bg-[linear-gradient(148deg,var(--color-gtw01-acc)_0%,var(--color-gtw01-deep)_58%,var(--color-gtw01-bg)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-overlay after:opacity-[var(--gtw01-op)] after:[filter:url(#gtw-01-oct1)] after:transition-opacity after:duration-300 group-hover:after:opacity-[calc(var(--gtw01-op)+0.18)] motion-reduce:after:transition-none"></div>
        <div class="grid content-start gap-[0.6rem] p-[clamp(0.95rem,2vw,1.25rem)]">
          <h2 class="m-0 font-gtw01-display text-[1.02rem] font-semibold leading-tight tracking-[-0.01em]">One octave</h2>
          <dl class="grid grid-cols-[auto_1fr] gap-x-[0.6rem] gap-y-[0.15rem] m-0 py-2 border-y border-gtw01-line font-gtw01-mono text-[0.76rem] leading-[1.5]">
            <dt class="m-0 text-gtw01-mut">numOctaves</dt><dd class="m-0 text-gtw01-ink">1</dd>
            <dt class="m-0 text-gtw01-mut">character</dt><dd class="m-0 text-gtw01-ink">smooth</dd>
            <dt class="m-0 text-gtw01-mut">cost</dt><dd class="m-0 text-gtw01-ink">lowest</dd>
          </dl>
          <p class="m-0 text-gtw01-mut text-[0.86rem] text-pretty">A single pass is soft and cheap. Good for large hero fields.</p>
        </div>
      </li>

      <li class="group relative grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw01-line bg-gtw01-surf transition-[border-color,translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:border-gtw01-acc hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Crunchy five-octave noise over a cyan gradient" class="relative isolate h-[clamp(9rem,20vw,12rem)] bg-[linear-gradient(148deg,var(--color-gtw01-acc)_0%,var(--color-gtw01-deep)_58%,var(--color-gtw01-bg)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-overlay after:opacity-[var(--gtw01-op)] after:[filter:url(#gtw-01-oct5)] after:transition-opacity after:duration-300 group-hover:after:opacity-[calc(var(--gtw01-op)+0.18)] motion-reduce:after:transition-none"></div>
        <div class="grid content-start gap-[0.6rem] p-[clamp(0.95rem,2vw,1.25rem)]">
          <h2 class="m-0 font-gtw01-display text-[1.02rem] font-semibold leading-tight tracking-[-0.01em]">Five octaves</h2>
          <dl class="grid grid-cols-[auto_1fr] gap-x-[0.6rem] gap-y-[0.15rem] m-0 py-2 border-y border-gtw01-line font-gtw01-mono text-[0.76rem] leading-[1.5]">
            <dt class="m-0 text-gtw01-mut">numOctaves</dt><dd class="m-0 text-gtw01-ink">5</dd>
            <dt class="m-0 text-gtw01-mut">character</dt><dd class="m-0 text-gtw01-ink">crunchy</dd>
            <dt class="m-0 text-gtw01-mut">cost</dt><dd class="m-0 text-gtw01-ink">steep</dd>
          </dl>
          <p class="m-0 text-gtw01-mut text-[0.86rem] text-pretty">Detail you cannot see at 6% opacity, paid for at every repaint.</p>
        </div>
      </li>

      <li class="group relative grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw01-line bg-gtw01-surf transition-[border-color,translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:border-gtw01-acc hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div role="img" aria-label="Desaturated monochrome grain over a cyan gradient" class="relative isolate h-[clamp(9rem,20vw,12rem)] bg-[linear-gradient(148deg,var(--color-gtw01-acc)_0%,var(--color-gtw01-deep)_58%,var(--color-gtw01-bg)_100%)] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-soft-light after:opacity-[calc(var(--gtw01-op)+0.2)] after:[filter:url(#gtw-01-mono)] after:transition-opacity after:duration-300 group-hover:after:opacity-[calc(var(--gtw01-op)+0.38)] motion-reduce:after:transition-none"></div>
        <div class="grid content-start gap-[0.6rem] p-[clamp(0.95rem,2vw,1.25rem)]">
          <h2 class="m-0 font-gtw01-display text-[1.02rem] font-semibold leading-tight tracking-[-0.01em]">Desaturated</h2>
          <dl class="grid grid-cols-[auto_1fr] gap-x-[0.6rem] gap-y-[0.15rem] m-0 py-2 border-y border-gtw01-line font-gtw01-mono text-[0.76rem] leading-[1.5]">
            <dt class="m-0 text-gtw01-mut">chain</dt><dd class="m-0 text-gtw01-ink">+ feColorMatrix</dd>
            <dt class="m-0 text-gtw01-mut">saturate</dt><dd class="m-0 text-gtw01-ink">0</dd>
            <dt class="m-0 text-gtw01-mut">result</dt><dd class="m-0 text-gtw01-ink">neutral</dd>
          </dl>
          <p class="m-0 text-gtw01-mut text-[0.86rem] text-pretty">Kills the colour confetti. Almost always what you want on UI.</p>
        </div>
      </li>
    </ul>

    <footer class="mt-[clamp(2rem,5vw,3rem)] pt-5 border-t border-gtw01-line">
      <p class="m-0 max-w-[46rem] text-gtw01-mut text-[0.9rem] text-pretty">Copy the <code class="font-gtw01-mono text-[0.92em]">&lt;svg&gt;</code> block once per document. Reference its filter ids from as many <code class="font-gtw01-mono text-[0.92em]">after:[filter:url(#…)]</code> utilities as you like — the noise is generated, so extra references cost nothing over the network.</p>
    </footer>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw01-bg: #0d1418;
  --color-gtw01-bg: oklch(0.19 0.02 220);
  --color-gtw01-surf: #131e24;
  --color-gtw01-surf: oklch(0.24 0.02 220);
  --color-gtw01-line: #26383f;
  --color-gtw01-line: oklch(0.33 0.02 215);
  --color-gtw01-tint: #16262d;
  --color-gtw01-tint: oklch(0.27 0.03 215);
  --color-gtw01-ink: #e8f2f5;
  --color-gtw01-ink: oklch(0.95 0.01 210);
  --color-gtw01-mut: #8ba6af;
  --color-gtw01-mut: oklch(0.72 0.03 215);
  --color-gtw01-acc: #22d3ee;
  --color-gtw01-acc: oklch(0.82 0.13 200);
  --color-gtw01-deep: #0e7490;
  --color-gtw01-deep: oklch(0.5 0.1 218);
  --font-gtw01-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw01-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}
/* Root rule: the full-bleed contract (also stated in the markup as w-full min-h-svh, so the
   stage is sized before the browser build has compiled) plus the non-design-scale scalars.
   --gtw01-op is grain strength: not a design token, so it stays a plain property and is read
   back through after:opacity-[var(--gtw01-op)]. */

.gtw-01 {
  width: 100%;
  min-height: 100svh;
  --gtw01-op: 0.55;
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}
/* THEME FLIP — every utility compiles to var(--color-gtw01-*), so re-pointing the tokens inside
   this scope reskins all of them at once. No dark: variant on a single element. */

.gtw-01:has(.gtw-01-theme:checked) {
  --color-gtw01-bg: #eef4f6;
  --color-gtw01-bg: oklch(0.96 0.008 215);
  --color-gtw01-surf: #ffffff;
  --color-gtw01-surf: oklch(1 0 0);
  --color-gtw01-line: #cddde2;
  --color-gtw01-line: oklch(0.88 0.015 215);
  --color-gtw01-tint: #e2eff3;
  --color-gtw01-tint: oklch(0.93 0.02 210);
  --color-gtw01-ink: #0d1418;
  --color-gtw01-ink: oklch(0.19 0.02 220);
  --color-gtw01-mut: #5a747d;
  --color-gtw01-mut: oklch(0.52 0.03 215);
  --color-gtw01-acc: #0891b2;
  --color-gtw01-acc: oklch(0.62 0.12 213);
  --color-gtw01-deep: #a5f3fc;
  --color-gtw01-deep: oklch(0.92 0.07 197);
  --gtw01-op: 0.4;
}

@media (prefers-color-scheme: light) {
  .gtw-01 {
    --color-gtw01-bg: #eef4f6;
    --color-gtw01-bg: oklch(0.96 0.008 215);
    --color-gtw01-surf: #ffffff;
    --color-gtw01-surf: oklch(1 0 0);
    --color-gtw01-line: #cddde2;
    --color-gtw01-line: oklch(0.88 0.015 215);
    --color-gtw01-tint: #e2eff3;
    --color-gtw01-tint: oklch(0.93 0.02 210);
    --color-gtw01-ink: #0d1418;
    --color-gtw01-ink: oklch(0.19 0.02 220);
    --color-gtw01-mut: #5a747d;
    --color-gtw01-mut: oklch(0.52 0.03 215);
    --color-gtw01-acc: #0891b2;
    --color-gtw01-acc: oklch(0.62 0.12 213);
    --color-gtw01-deep: #a5f3fc;
    --color-gtw01-deep: oklch(0.92 0.07 197);
    --gtw01-op: 0.4;
  }

  .gtw-01:has(.gtw-01-theme:checked) {
    --color-gtw01-bg: #0d1418;
    --color-gtw01-bg: oklch(0.19 0.02 220);
    --color-gtw01-surf: #131e24;
    --color-gtw01-surf: oklch(0.24 0.02 220);
    --color-gtw01-line: #26383f;
    --color-gtw01-line: oklch(0.33 0.02 215);
    --color-gtw01-tint: #16262d;
    --color-gtw01-tint: oklch(0.27 0.03 215);
    --color-gtw01-ink: #e8f2f5;
    --color-gtw01-ink: oklch(0.95 0.01 210);
    --color-gtw01-mut: #8ba6af;
    --color-gtw01-mut: oklch(0.72 0.03 215);
    --color-gtw01-acc: #22d3ee;
    --color-gtw01-acc: oklch(0.82 0.13 200);
    --color-gtw01-deep: #0e7490;
    --color-gtw01-deep: oklch(0.5 0.1 218);
    --gtw01-op: 0.55;
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-01:has(.gtw-01-theme:checked) {
    --color-gtw01-bg: #eef4f6;
    --color-gtw01-bg: oklch(0.96 0.008 215);
    --color-gtw01-surf: #ffffff;
    --color-gtw01-surf: oklch(1 0 0);
    --color-gtw01-line: #cddde2;
    --color-gtw01-line: oklch(0.88 0.015 215);
    --color-gtw01-tint: #e2eff3;
    --color-gtw01-tint: oklch(0.93 0.02 210);
    --color-gtw01-ink: #0d1418;
    --color-gtw01-ink: oklch(0.19 0.02 220);
    --color-gtw01-mut: #5a747d;
    --color-gtw01-mut: oklch(0.52 0.03 215);
    --color-gtw01-acc: #0891b2;
    --color-gtw01-acc: oklch(0.62 0.12 213);
    --color-gtw01-deep: #a5f3fc;
    --color-gtw01-deep: oklch(0.92 0.07 197);
    --gtw01-op: 0.4;
  }
}
```
