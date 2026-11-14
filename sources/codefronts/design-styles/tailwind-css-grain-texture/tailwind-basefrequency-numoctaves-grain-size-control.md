---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-basefrequency-numoctaves-grain-size-control/"
title: "Tailwind baseFrequency and numOctaves Grain Size Control"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "A specimen sheet for the only two attributes that decide whether grain reads as expensive film stock or as a broken JPEG: seven baseFrequency steps, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind baseFrequency and numOctaves Grain Size Control
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-basefrequency-numoctaves-grain-size-control/

A specimen sheet for the only two attributes that decide whether grain reads as expensive film stock or as a broken JPEG: seven baseFrequency steps, a four-step octave ramp, the two-value anisotropic form, and the min-resolution: 2dppx correction almost nobody ships. The port's interesting problem is the blend mode — it has to differ per theme, so it stays a custom property read back through an arbitrary utility.
## HTML
```html
<section class="gtw-02 relative block w-full min-h-svh bg-gtw02-bg text-gtw02-ink" aria-labelledby="gtw-02-title">
  <svg class="absolute w-0 h-0 overflow-hidden" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="gtw-02-f005" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="gtw-02-f015" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.15" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="gtw-02-f030" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.3" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="gtw-02-f050" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="gtw-02-f080" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="gtw-02-f120" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.2" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="gtw-02-f160" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="gtw-02-o1" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="1" seed="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
    <filter id="gtw-02-o2" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="2" seed="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
    <filter id="gtw-02-o4" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="4" seed="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
    <filter id="gtw-02-aniso-v" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.02 0.9" numOctaves="3" seed="6" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
    <filter id="gtw-02-aniso-h" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9 0.02" numOctaves="3" seed="6" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
  </svg>

  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-02-theme" class="gtw-02-theme peer sr-only">
    <label for="gtw-02-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw02-line bg-gtw02-surf text-gtw02-ink cursor-pointer transition-colors duration-200 hover:border-gtw02-acc peer-focus-visible:outline-2 peer-focus-visible:outline-gtw02-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(74rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2.2rem,5vw,3.5rem)]">
    <header class="max-w-[46rem] grid gap-3">
      <p class="m-0 font-gtw02-mono text-[0.72rem] font-medium tracking-[0.18em] uppercase text-gtw02-acc">Specimen sheet · 02</p>
      <h1 id="gtw-02-title" class="m-0 font-gtw02-display text-[clamp(2rem,5.2vw,3.3rem)] font-medium leading-[1.06] tracking-[-0.02em] text-balance">Grain size is one number, and most people guess it</h1>
      <p class="m-0 max-w-[40rem] text-gtw02-mut text-[clamp(0.95rem,1.9vw,1.08rem)] text-pretty">Seven frequency steps, an octave ramp, and the two-value form that streaks the lattice. Everything else — type, seed, blend mode, opacity — is held constant.</p>
    </header>

    <section class="grid gap-4" aria-labelledby="gtw-02-h-freq">
      <div class="flex flex-wrap items-baseline gap-x-4 gap-y-[0.4rem] pb-[0.6rem] border-b border-gtw02-line">
        <h2 id="gtw-02-h-freq" class="m-0 font-gtw02-display text-[clamp(1.1rem,2.6vw,1.4rem)] font-medium leading-[1.15]">baseFrequency ramp</h2>
        <p class="m-0 text-gtw02-mut text-[0.85rem]">Bigger number, smaller grain. <code class="font-gtw02-mono text-[0.9em]">numOctaves</code> pinned at 3.</p>
      </div>
      <ol class="list-none m-0 p-0 grid gap-[clamp(0.5rem,1.4vw,0.85rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,7.5rem),1fr))]">
        <li class="group grid gap-[0.35rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-f005)]"></span>
          <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none tracking-[0.02em]">0.05</span>
          <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">cloud</span>
        </li>
        <li class="group grid gap-[0.35rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-f015)]"></span>
          <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none tracking-[0.02em]">0.15</span>
          <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">blotch</span>
        </li>
        <li class="group grid gap-[0.35rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-f030)]"></span>
          <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none tracking-[0.02em]">0.30</span>
          <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">coarse</span>
        </li>
        <li class="group grid gap-[0.35rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-f050)]"></span>
          <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none tracking-[0.02em]">0.50</span>
          <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">sand</span>
        </li>
        <li class="group grid gap-[0.35rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-acc shadow-[0_0_0_2px_color-mix(in_oklab,var(--color-gtw02-acc)_25%,transparent)] bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-f080)]"></span>
          <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none tracking-[0.02em]">0.80</span>
          <span class="text-[0.74rem] font-semibold tracking-[0.08em] uppercase text-gtw02-acc">ship this</span>
        </li>
        <li class="group grid gap-[0.35rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-f120)]"></span>
          <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none tracking-[0.02em]">1.20</span>
          <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">fine</span>
        </li>
        <li class="group grid gap-[0.35rem] min-w-0">
          <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-f160)]"></span>
          <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none tracking-[0.02em]">1.60</span>
          <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">aliases</span>
        </li>
      </ol>
    </section>

    <div class="grid gap-[clamp(1.5rem,4vw,2.5rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,20rem),1fr))]">
      <section class="grid gap-4" aria-labelledby="gtw-02-h-oct">
        <div class="flex flex-wrap items-baseline gap-x-4 gap-y-[0.4rem] pb-[0.6rem] border-b border-gtw02-line">
          <h2 id="gtw-02-h-oct" class="m-0 font-gtw02-display text-[clamp(1.1rem,2.6vw,1.4rem)] font-medium leading-[1.15]">numOctaves ramp</h2>
          <p class="m-0 text-gtw02-mut text-[0.85rem]">Same size, different character. <code class="font-gtw02-mono text-[0.9em]">baseFrequency</code> pinned at 0.75.</p>
        </div>
        <ol class="list-none m-0 p-0 grid gap-[clamp(0.5rem,1.4vw,0.85rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,8.5rem),1fr))]">
          <li class="group grid gap-[0.35rem] min-w-0">
            <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-o1)]"></span>
            <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none">1</span>
            <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">smooth</span>
          </li>
          <li class="group grid gap-[0.35rem] min-w-0">
            <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-o2)]"></span>
            <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none">2</span>
            <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">soft</span>
          </li>
          <li class="group grid gap-[0.35rem] min-w-0">
            <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-acc shadow-[0_0_0_2px_color-mix(in_oklab,var(--color-gtw02-acc)_25%,transparent)] bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-f080)]"></span>
            <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none">3</span>
            <span class="text-[0.74rem] font-semibold tracking-[0.08em] uppercase text-gtw02-acc">organic</span>
          </li>
          <li class="group grid gap-[0.35rem] min-w-0">
            <span class="relative isolate block h-[clamp(6rem,13vw,8rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-[var(--gtw02-op)] after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-o4)]"></span>
            <span class="font-gtw02-mono text-[0.9rem] font-medium leading-none">4</span>
            <span class="text-[0.74rem] tracking-[0.08em] uppercase text-gtw02-mut">crunchy</span>
          </li>
        </ol>
      </section>

      <section class="grid gap-4" aria-labelledby="gtw-02-h-aniso">
        <div class="flex flex-wrap items-baseline gap-x-4 gap-y-[0.4rem] pb-[0.6rem] border-b border-gtw02-line">
          <h2 id="gtw-02-h-aniso" class="m-0 font-gtw02-display text-[clamp(1.1rem,2.6vw,1.4rem)] font-medium leading-[1.15]">Two values, one streak</h2>
          <p class="m-0 text-gtw02-mut text-[0.85rem]"><code class="font-gtw02-mono text-[0.9em]">baseFrequency="0.02 0.9"</code> stretches the lattice.</p>
        </div>
        <div class="grid gap-[clamp(0.6rem,1.6vw,1rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,9rem),1fr))]">
          <figure class="group m-0 grid gap-[0.4rem] min-w-0">
            <span class="relative isolate block h-[clamp(7rem,16vw,9.5rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-85 after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-aniso-v)]"></span>
            <figcaption class="font-gtw02-mono text-[0.74rem] leading-[1.3] text-gtw02-mut">0.02 0.9 · vertical rain</figcaption>
          </figure>
          <figure class="group m-0 grid gap-[0.4rem] min-w-0">
            <span class="relative isolate block h-[clamp(7rem,16vw,9.5rem)] overflow-hidden rounded-[10px] border border-gtw02-line bg-[linear-gradient(160deg,var(--color-gtw02-surf),var(--color-gtw02-bg))] transition-[translate] duration-300 group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:opacity-85 after:[mix-blend-mode:var(--gtw02-blend)] after:[filter:url(#gtw-02-aniso-h)]"></span>
            <figcaption class="font-gtw02-mono text-[0.74rem] leading-[1.3] text-gtw02-mut">0.9 0.02 · brushed metal</figcaption>
          </figure>
        </div>
      </section>
    </div>

    <aside class="grid gap-[0.8rem] p-[clamp(1.1rem,3vw,1.8rem)] rounded-[14px] border border-gtw02-line bg-gtw02-surf" aria-labelledby="gtw-02-h-dpr">
      <h2 id="gtw-02-h-dpr" class="m-0 font-gtw02-display text-[clamp(1.1rem,2.6vw,1.4rem)] font-medium leading-[1.15]">The retina correction</h2>
      <p class="m-0 max-w-[48rem] text-gtw02-mut text-[0.92rem] text-pretty"><code class="font-gtw02-mono text-[0.9em]">baseFrequency</code> resolves in user space, not device pixels — so grain tuned on a 1x monitor spreads across three times as many pixels on a 3x phone and reads as dirt. This sheet ships the fix: a <code class="font-gtw02-mono text-[0.9em]">min-resolution: 2dppx</code> query that raises the frequency on dense displays. The tile below is running whichever value your current screen asked for.</p>
      <div class="gtw-02-dpr relative isolate grid items-end h-[clamp(6rem,14vw,8.5rem)] px-[0.9rem] py-[0.7rem] overflow-hidden rounded-[10px] bg-[linear-gradient(120deg,var(--color-gtw02-acc),color-mix(in_oklab,var(--color-gtw02-acc)_35%,var(--color-gtw02-surf)))] after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-overlay">
        <span class="relative z-[1] font-gtw02-mono text-[0.72rem] font-medium leading-none tracking-[0.14em] uppercase text-white">live on this display</span>
      </div>
    </aside>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw02-bg: #f5f1e8;
  --color-gtw02-bg: oklch(0.95 0.015 85);
  --color-gtw02-surf: #fffdf8;
  --color-gtw02-surf: oklch(0.99 0.008 90);
  --color-gtw02-line: #ddd5c4;
  --color-gtw02-line: oklch(0.87 0.02 85);
  --color-gtw02-ink: #1d1a14;
  --color-gtw02-ink: oklch(0.22 0.01 75);
  --color-gtw02-mut: #6f6857;
  --color-gtw02-mut: oklch(0.49 0.02 80);
  --color-gtw02-acc: #b4531f;
  --color-gtw02-acc: oklch(0.52 0.14 45);
  --font-gtw02-display: 'Fraunces', 'Playfair Display', Georgia, 'Times New Roman', serif;
  --font-gtw02-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-02 {
  width: 100%;
  min-height: 100svh;
  --gtw02-op: 0.72;
  --gtw02-blend: multiply;
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}
/* Grain layer on the retina tile: the filter reference is swapped by resolution, which is why
   this one lives in CSS rather than in a utility. */

.gtw-02-dpr::after {
  filter: url(#gtw-02-f080);
  opacity: 0.55;
}

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 2dppx) {
  .gtw-02-dpr::after {
    filter: url(#gtw-02-f120);
    opacity: 0.62;
  }
}
/* Theme flip: re-point the @theme tokens in scope. The blend mode flips with them — grain
   multiplies on cream and screens on near-black. */

.gtw-02:has(.gtw-02-theme:checked) {
  --color-gtw02-bg: #14120e;
  --color-gtw02-bg: oklch(0.18 0.01 75);
  --color-gtw02-surf: #1d1a15;
  --color-gtw02-surf: oklch(0.23 0.01 75);
  --color-gtw02-line: #35301f;
  --color-gtw02-line: oklch(0.32 0.02 85);
  --color-gtw02-ink: #f3eee2;
  --color-gtw02-ink: oklch(0.95 0.01 85);
  --color-gtw02-mut: #a89e88;
  --color-gtw02-mut: oklch(0.72 0.02 85);
  --color-gtw02-acc: #f0844a;
  --color-gtw02-acc: oklch(0.74 0.14 48);
  --gtw02-op: 0.6;
  --gtw02-blend: screen;
}

@media (prefers-color-scheme: dark) {
  .gtw-02 {
    --color-gtw02-bg: #14120e;
    --color-gtw02-bg: oklch(0.18 0.01 75);
    --color-gtw02-surf: #1d1a15;
    --color-gtw02-surf: oklch(0.23 0.01 75);
    --color-gtw02-line: #35301f;
    --color-gtw02-line: oklch(0.32 0.02 85);
    --color-gtw02-ink: #f3eee2;
    --color-gtw02-ink: oklch(0.95 0.01 85);
    --color-gtw02-mut: #a89e88;
    --color-gtw02-mut: oklch(0.72 0.02 85);
    --color-gtw02-acc: #f0844a;
    --color-gtw02-acc: oklch(0.74 0.14 48);
    --gtw02-op: 0.6;
    --gtw02-blend: screen;
  }

  .gtw-02:has(.gtw-02-theme:checked) {
    --color-gtw02-bg: #f5f1e8;
    --color-gtw02-bg: oklch(0.95 0.015 85);
    --color-gtw02-surf: #fffdf8;
    --color-gtw02-surf: oklch(0.99 0.008 90);
    --color-gtw02-line: #ddd5c4;
    --color-gtw02-line: oklch(0.87 0.02 85);
    --color-gtw02-ink: #1d1a14;
    --color-gtw02-ink: oklch(0.22 0.01 75);
    --color-gtw02-mut: #6f6857;
    --color-gtw02-mut: oklch(0.49 0.02 80);
    --color-gtw02-acc: #b4531f;
    --color-gtw02-acc: oklch(0.52 0.14 45);
    --gtw02-op: 0.72;
    --gtw02-blend: multiply;
  }
}

@media (prefers-color-scheme: light) {
  .gtw-02:has(.gtw-02-theme:checked) {
    --color-gtw02-bg: #14120e;
    --color-gtw02-bg: oklch(0.18 0.01 75);
    --color-gtw02-surf: #1d1a15;
    --color-gtw02-surf: oklch(0.23 0.01 75);
    --color-gtw02-line: #35301f;
    --color-gtw02-line: oklch(0.32 0.02 85);
    --color-gtw02-ink: #f3eee2;
    --color-gtw02-ink: oklch(0.95 0.01 85);
    --color-gtw02-mut: #a89e88;
    --color-gtw02-mut: oklch(0.72 0.02 85);
    --color-gtw02-acc: #f0844a;
    --color-gtw02-acc: oklch(0.74 0.14 48);
    --gtw02-op: 0.6;
    --gtw02-blend: screen;
  }
}
```
