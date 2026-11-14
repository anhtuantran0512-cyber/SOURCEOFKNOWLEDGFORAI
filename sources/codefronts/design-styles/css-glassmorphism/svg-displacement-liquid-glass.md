---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/svg-displacement-liquid-glass/"
title: "SVG Displacement Liquid Glass"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "Real refraction, not a blur: an inline <filter> chains feTurbulence into feDisplacementMap and the panel passes its backdrop through it, so the background…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG Displacement Liquid Glass
Source: https://codefronts.com/design-styles/css-glassmorphism/svg-displacement-liquid-glass/

Real refraction, not a blur: an inline <filter> chains feTurbulence into feDisplacementMap and the panel passes its backdrop through it, so the background warps at the glass edges the way it does through a physical lens. This is the WWDC 2025 liquid-glass look done with web primitives — and it degrades to a plain frosted panel wherever the filter reference is not honoured.
## HTML
```html
<div class="gm-05">
  <svg class="gm-05__defs" aria-hidden="true" focusable="false">
    <filter id="gm-05-refract" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.015" numOctaves="2" seed="7" result="noise"/>
      <feGaussianBlur in="noise" stdDeviation="1.4" result="soft"/>
      <feDisplacementMap in="SourceGraphic" in2="soft" scale="30" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <filter id="gm-05-refract-strong" x="-25%" y="-25%" width="150%" height="150%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="3" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="52" xChannelSelector="R" yChannelSelector="B"/>
    </filter>
  </svg>

  <input class="gm-05__sr" type="checkbox" id="gm-05-theme">
  <label class="gm-05__theme" for="gm-05-theme" title="Switch theme">
    <svg class="gm-05__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-05__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-05__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-05__stage">
    <div class="gm-05__grid-lines" aria-hidden="true"></div>
    <section class="gm-05__wrap" aria-labelledby="gm-05-h">
      <header class="gm-05__head">
        <p class="gm-05__eyebrow">feTurbulence → feDisplacementMap</p>
        <h2 class="gm-05__h" id="gm-05-h">Glass that bends light, not just blurs it</h2>
        <p class="gm-05__sub">The grid behind the panel is straight. Look at it through the rim.</p>
      </header>

      <div class="gm-05__panels">
        <article class="gm-05__panel">
          <div class="gm-05__lens" aria-hidden="true"></div>
          <div class="gm-05__body">
            <p class="gm-05__pill">scale 30 · baseFrequency 0.015</p>
            <h3 class="gm-05__title">Liquid rim</h3>
            <p class="gm-05__copy">Displacement is masked to the edges, so the centre stays crisp enough for real copy while the border refracts the grid behind it.</p>
            <p class="gm-05__meta">blur(3px) saturate(160%) url(#gm-05-refract)</p>
          </div>
        </article>
        <article class="gm-05__panel gm-05__panel--strong">
          <div class="gm-05__lens gm-05__lens--strong" aria-hidden="true"></div>
          <div class="gm-05__body">
            <p class="gm-05__pill">scale 52 · baseFrequency 0.022</p>
            <h3 class="gm-05__title">Heavy lens</h3>
            <p class="gm-05__copy">Push the scale and the panel behaves like thick cast glass — beautiful for hero chrome, unusable behind body text.</p>
            <p class="gm-05__meta">xChannel R · yChannel B</p>
          </div>
        </article>
      </div>

      <aside class="gm-05__note">
        <p class="gm-05__nhead">WWDC 2025 recipe</p>
        <p class="gm-05__ncopy">Turbulence makes the noise field, a small Gaussian blur softens it, displacement reads R and G as x/y offsets. Chromium applies it through <span class="gm-05__code">backdrop-filter</span>; other engines fall back to blur and the layout never breaks.</p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-05 {
  --a1: rgba(139,92,246,.6);
  --a2: rgba(45,212,191,.5);
  --a3: rgba(244,63,94,.45);
  --a4: rgba(59,130,246,.5);
  --base: #05060f;
  --base2: #12112e;
  --ink: #f8f9ff;
  --muted: rgba(248,249,255,.7);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.55);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.2);
  --line: rgba(255,255,255,.11);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(54% 44% at 16% 14%, var(--a1) 0%, transparent 62%), radial-gradient(46% 40% at 86% 18%, var(--a2) 0%, transparent 58%), radial-gradient(50% 44% at 80% 86%, var(--a3) 0%, transparent 60%), radial-gradient(48% 42% at 14% 88%, var(--a4) 0%, transparent 60%), linear-gradient(165deg, var(--base) 0%, var(--base2) 54%, var(--base) 100%);
}

.gm-05 *,
.gm-05 *::before,
.gm-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-05 {
    --a1: oklch(0.62 0.24 295 / .62);
    --a2: oklch(0.82 0.15 180 / .52);
    --a3: oklch(0.66 0.22 12 / .46);
    --a4: oklch(0.66 0.19 255 / .52);
    --base: oklch(0.13 0.028 275);
    --base2: oklch(0.22 0.09 292);
  }
}

.gm-05__defs {
  position: absolute;
  inline-size: 0;
  block-size: 0;
  overflow: hidden;
}

.gm-05__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-05__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 8;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(10px) saturate(160%);
  backdrop-filter: blur(10px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), 0 10px 24px -14px rgba(0,0,0,.7);
  transition: scale .18s ease;
}

.gm-05__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-05__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-05__theme:hover {
  scale: 1.06;
}

.gm-05__sr:focus-visible + .gm-05__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-05__moon {
  display: none;
}

.gm-05__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}
/* straight rulings so the refraction is measurable, not vibes */

.gm-05__grid-lines {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background-image: repeating-linear-gradient(90deg, var(--line) 0 1px, transparent 1px 2.75rem), repeating-linear-gradient(0deg, var(--line) 0 1px, transparent 1px 2.75rem);
  mask-image: radial-gradient(120% 100% at 50% 45%, #000 25%, transparent 82%);
}

.gm-05__wrap {
  position: relative;
  z-index: 1;
  inline-size: min(72rem,100%);
}

.gm-05__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 42rem;
  margin-block-end: clamp(1.5rem,3.5vw,2.5rem);
}

.gm-05__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-05__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-05__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
}

.gm-05__panels {
  display: grid;
  gap: clamp(1rem,2vw,1.6rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.gm-05__panel {
  position: relative;
  isolation: isolate;
  border-radius: 1.6rem;
  overflow: hidden;
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 30px 66px -28px rgba(0,0,0,.7);
}
/* lens layer: warps the backdrop only — never the text */

.gm-05__lens {
  position: absolute;
  inset: 0;
  z-index: 0;
  border-radius: inherit;
  background: rgba(255,255,255,.09);
  -webkit-backdrop-filter: blur(3px) saturate(160%);
  backdrop-filter: blur(3px) saturate(160%);
}

@supports (backdrop-filter: url(#gm-05-refract)) {
  .gm-05__lens {
    backdrop-filter: blur(3px) saturate(160%) url(#gm-05-refract);
  }

  .gm-05__lens--strong {
    backdrop-filter: blur(2px) saturate(170%) url(#gm-05-refract-strong);
  }
}

.gm-05__lens {
  mask-image: radial-gradient(120% 120% at 50% 50%, transparent 52%, #000 88%);
  -webkit-mask-image: radial-gradient(120% 120% at 50% 50%, transparent 52%, #000 88%);
}

.gm-05__lens--strong {
  mask-image: radial-gradient(120% 120% at 50% 50%, transparent 40%, #000 82%);
  -webkit-mask-image: radial-gradient(120% 120% at 50% 50%, transparent 40%, #000 82%);
}

.gm-05__body {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: .6rem;
  padding: clamp(1.2rem,2.2vw,1.75rem);
  background: rgba(255,255,255,.08);
  -webkit-backdrop-filter: blur(14px) saturate(150%);
  backdrop-filter: blur(14px) saturate(150%);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-05__body {
    background: color-mix(in oklab, var(--tint) 12%, transparent);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-05__body {
    background: rgba(16,14,42,.86);
  }
}

.gm-05__pill {
  margin: 0;
  align-self: flex-start;
  padding: .3rem .58rem;
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .7rem;
  font-variant-numeric: tabular-nums;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
}

.gm-05__title {
  margin: .2rem 0 0;
  font-size: clamp(1.25rem,2.2vw,1.55rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.gm-05__copy {
  margin: 0;
  font-size: .94rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-05__meta {
  margin: .35rem 0 0;
  padding-block-start: .7rem;
  border-block-start: 1px solid var(--rim2);
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .03em;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.gm-05__note {
  margin-block-start: clamp(1rem,2vw,1.5rem);
  padding: clamp(1rem,1.8vw,1.35rem);
  border-radius: 1.15rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.08);
  -webkit-backdrop-filter: blur(20px) saturate(150%);
  backdrop-filter: blur(20px) saturate(150%);
  box-shadow: inset 0 1px 0 var(--rim2);
  display: grid;
  gap: .4rem;
  max-inline-size: 44rem;
}

.gm-05__nhead {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ink);
}

.gm-05__ncopy {
  margin: 0;
  font-size: .9rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-05__code {
  font-family: var(--mono);
  font-size: .8rem;
  padding: .12rem .38rem;
  border-radius: .35rem;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  color: var(--ink);
}

.gm-05[data-theme="light"],
.gm-05:has(#gm-05-theme:checked) {
  --a1: rgba(196,181,253,.55);
  --a2: rgba(153,246,228,.55);
  --a3: rgba(254,205,211,.5);
  --a4: rgba(147,197,253,.5);
  --base: #eff2fa;
  --base2: #e0e7fb;
  --ink: #0f1120;
  --muted: rgba(15,17,32,.66);
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,17,32,.1);
  --line: rgba(15,17,32,.1);
}

.gm-05:has(#gm-05-theme:checked) .gm-05__sun {
  display: none;
}

.gm-05:has(#gm-05-theme:checked) .gm-05__moon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .gm-05 *,
    .gm-05 *::before,
    .gm-05 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-05__panel,
    .gm-05__note,
    .gm-05__theme,
    .gm-05__pill {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
  }

  .gm-05__lens {
    display: none;
  }

  .gm-05__body {
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
