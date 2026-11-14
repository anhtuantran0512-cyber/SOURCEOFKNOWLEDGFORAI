---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/dark-mode-noise-without-muddy-shadows/"
title: "Dark Mode Noise Without Muddy Shadows"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Grain that looks refined on a light surface looks like a dirty screen on a dark one."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Noise Without Muddy Shadows
Source: https://codefronts.com/design-styles/css-grain-texture/dark-mode-noise-without-muddy-shadows/

Grain that looks refined on a light surface looks like a dirty screen on a dark one. The reasons are measurable — perceptual contrast, shadow crush, and the fact that overlay is not symmetric — and the fixes are specific. This is a full dark dashboard with the corrected recipe, plus the exact per-theme numbers to copy.
## HTML
```html
<section class="grn-19" aria-labelledby="grn-19-title">
  <div class="grn-19__theme">
    <input class="grn-19__theme-input" type="checkbox" id="grn-19-theme">
    <label class="grn-19__theme-label" for="grn-19-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-19__sr">Toggle light theme</span>
    </label>
  </div>

  <div class="grn-19__app">
    <aside class="grn-19__rail" aria-label="Sections">
      <p class="grn-19__logo">◐ Umbra</p>
      <nav class="grn-19__nav">
        <a class="grn-19__nav-a" href="#grn-19-title" aria-current="page">Overview</a>
        <a class="grn-19__nav-a" href="#grn-19-title">Surfaces</a>
        <a class="grn-19__nav-a" href="#grn-19-title">Elevation</a>
        <a class="grn-19__nav-a" href="#grn-19-title">Contrast</a>
        <a class="grn-19__nav-a" href="#grn-19-title">Tokens</a>
      </nav>
      <p class="grn-19__rail-note">Grain weight climbs with elevation. Shadows do almost nothing here.</p>
    </aside>

    <main class="grn-19__main">
      <header class="grn-19__head">
        <p class="grn-19__kicker">Dark surface recipe · 19</p>
        <h1 class="grn-19__h1" id="grn-19-title">Texture in the dark, without the mud</h1>
        <p class="grn-19__lede">Two grain weights, <code>soft-light</code> instead of <code>overlay</code>, and a mask that keeps noise out of the deepest shadows. Toggle the theme and watch both numbers change.</p>
      </header>

      <ul class="grn-19__stats">
        <li class="grn-19__stat grn-19__stat--e1"><span class="grn-19__stat-k">Surface 1</span><span class="grn-19__stat-v">8% L</span><span class="grn-19__stat-m">grain 0.055</span></li>
        <li class="grn-19__stat grn-19__stat--e2"><span class="grn-19__stat-k">Surface 2</span><span class="grn-19__stat-v">12% L</span><span class="grn-19__stat-m">grain 0.075</span></li>
        <li class="grn-19__stat grn-19__stat--e3"><span class="grn-19__stat-k">Surface 3</span><span class="grn-19__stat-v">17% L</span><span class="grn-19__stat-m">grain 0.095</span></li>
      </ul>

      <div class="grn-19__panels">
        <section class="grn-19__panel grn-19__panel--wide" aria-labelledby="grn-19-h-chart">
          <div class="grn-19__panel-head">
            <h2 class="grn-19__h2" id="grn-19-h-chart">Perceived texture vs opacity</h2>
            <span class="grn-19__pill">measured</span>
          </div>
          <div class="grn-19__chart" role="img" aria-label="Bar chart showing dark surfaces need roughly 1.6 times the grain opacity of light surfaces for equal perceived texture">
            <span class="grn-19__bar" style="--grn-19-h: 32%"><b>0.03</b></span>
            <span class="grn-19__bar" style="--grn-19-h: 48%"><b>0.045</b></span>
            <span class="grn-19__bar grn-19__bar--mark" style="--grn-19-h: 68%"><b>0.06</b></span>
            <span class="grn-19__bar grn-19__bar--mark" style="--grn-19-h: 84%"><b>0.075</b></span>
            <span class="grn-19__bar" style="--grn-19-h: 100%"><b>0.095</b></span>
          </div>
          <p class="grn-19__panel-note">The marked pair is the working range for dark product UI. The same perceived texture on a light surface sits at 0.04–0.05.</p>
        </section>

        <section class="grn-19__panel" aria-labelledby="grn-19-h-blend">
          <div class="grn-19__panel-head"><h2 class="grn-19__h2" id="grn-19-h-blend">Blend choice</h2></div>
          <ul class="grn-19__blends">
            <li><b>soft-light</b><span>Ship this. Roughly symmetric at low lightness.</span></li>
            <li><b>screen</b><span>For true black. Can only lift, never crush.</span></li>
            <li><b>overlay</b><span>Avoid. Only darkens below mid-grey — this is the mud.</span></li>
          </ul>
        </section>

        <section class="grn-19__panel" aria-labelledby="grn-19-h-contrast">
          <div class="grn-19__panel-head"><h2 class="grn-19__h2" id="grn-19-h-contrast">Contrast, composited</h2></div>
          <p class="grn-19__panel-note">A 9% grain layer measurably reduces text contrast. Check the composited surface, not the flat token.</p>
          <dl class="grn-19__ratios">
            <div><dt>Body on surface 2</dt><dd>7.1:1</dd></div>
            <div><dt>Same, grain applied</dt><dd>6.8:1</dd></div>
            <div><dt>Muted on surface 2</dt><dd>4.7:1</dd></div>
          </dl>
        </section>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.grn-19 {
  --grn-19-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='grn19n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23grn19n)'/%3E%3C/svg%3E");
  --grn-19-bg: #08090b;
  --grn-19-s1: #101216;
  --grn-19-s2: #171a20;
  --grn-19-s3: #20242c;
  --grn-19-line: #262b34;
  --grn-19-ink: #eef1f6;
  --grn-19-mut: #98a1b0;
  --grn-19-acc: #7dd3fc;
  --grn-19-acc: oklch(84% 0.1 226);
  --grn-19-g1: 0.055;
  --grn-19-g2: 0.075;
  --grn-19-g3: 0.095;
  --grn-19-blend: soft-light;
  --grn-19-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-19-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-19-bg);
  color: var(--grn-19-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-19 *,
.grn-19 *::before,
.grn-19 *::after {
  box-sizing: border-box;
}

.grn-19 :focus-visible {
  outline: 2px solid var(--grn-19-acc);
  outline-offset: 3px;
}

.grn-19 code {
  font-family: var(--grn-19-font-mono);
  font-size: 0.9em;
}

.grn-19__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.grn-19:has(.grn-19__theme-input:checked) {
  --grn-19-bg: #f4f6fa;
  --grn-19-s1: #ffffff;
  --grn-19-s2: #f7f9fc;
  --grn-19-s3: #eef2f8;
  --grn-19-line: #dde3ec;
  --grn-19-ink: #0b0d11;
  --grn-19-mut: #5b6474;
  --grn-19-acc: #0369a1;
  --grn-19-acc: oklch(48% 0.11 235);
  --grn-19-g1: 0.03;
  --grn-19-g2: 0.045;
  --grn-19-g3: 0.055;
  --grn-19-blend: multiply;
}

@media (prefers-color-scheme: light) {
  .grn-19 {
    --grn-19-bg: #f4f6fa;
    --grn-19-s1: #ffffff;
    --grn-19-s2: #f7f9fc;
    --grn-19-s3: #eef2f8;
    --grn-19-line: #dde3ec;
    --grn-19-ink: #0b0d11;
    --grn-19-mut: #5b6474;
    --grn-19-acc: #0369a1;
    --grn-19-acc: oklch(48% 0.11 235);
    --grn-19-g1: 0.03;
    --grn-19-g2: 0.045;
    --grn-19-g3: 0.055;
    --grn-19-blend: multiply;
  }

  .grn-19:has(.grn-19__theme-input:checked) {
    --grn-19-bg: #08090b;
    --grn-19-s1: #101216;
    --grn-19-s2: #171a20;
    --grn-19-s3: #20242c;
    --grn-19-line: #262b34;
    --grn-19-ink: #eef1f6;
    --grn-19-mut: #98a1b0;
    --grn-19-acc: #7dd3fc;
    --grn-19-acc: oklch(84% 0.1 226);
    --grn-19-g1: 0.055;
    --grn-19-g2: 0.075;
    --grn-19-g3: 0.095;
    --grn-19-blend: soft-light;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-19:has(.grn-19__theme-input:checked) {
    --grn-19-bg: #f4f6fa;
    --grn-19-s1: #ffffff;
    --grn-19-s2: #f7f9fc;
    --grn-19-s3: #eef2f8;
    --grn-19-line: #dde3ec;
    --grn-19-ink: #0b0d11;
    --grn-19-mut: #5b6474;
    --grn-19-acc: #0369a1;
    --grn-19-acc: oklch(48% 0.11 235);
    --grn-19-g1: 0.03;
    --grn-19-g2: 0.045;
    --grn-19-g3: 0.055;
    --grn-19-blend: multiply;
  }
}

.grn-19__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 60;
}

.grn-19__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-19__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-19-line);
  border-radius: 999px;
  background: var(--grn-19-s3);
  color: var(--grn-19-ink);
  cursor: pointer;
}

.grn-19__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-19__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  min-block-size: 100vh;
  min-block-size: 100svh;
}

@media (min-width: 62rem) {
  .grn-19__app {
    grid-template-columns: 16rem minmax(0, 1fr);
  }
}

.grn-19__rail {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  align-content: start;
  gap: 1.2rem;
  padding: clamp(1.2rem, 3vw, 1.8rem);
  border-inline-end: 1px solid var(--grn-19-line);
  background: var(--grn-19-s1);
}

.grn-19__rail::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image: var(--grn-19-noise);
  opacity: var(--grn-19-g1);
  mix-blend-mode: var(--grn-19-blend);
  -webkit-mask-image: linear-gradient(to bottom, #000 0%, #000 70%, rgba(0, 0, 0, 0.35) 100%);
  mask-image: linear-gradient(to bottom, #000 0%, #000 70%, rgba(0, 0, 0, 0.35) 100%);
}

.grn-19__logo {
  margin: 0;
  font: 600 1.05rem/1 var(--grn-19-font-display);
  letter-spacing: -0.01em;
}

.grn-19__nav {
  display: grid;
  gap: 0.15rem;
}

.grn-19__nav-a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.75rem;
  border-radius: 9px;
  color: var(--grn-19-mut);
  text-decoration: none;
  font-size: 0.92rem;
}

.grn-19__nav-a:hover {
  background: var(--grn-19-s2);
  color: var(--grn-19-ink);
}

.grn-19__nav-a[aria-current="page"] {
  background: var(--grn-19-s3);
  color: var(--grn-19-ink);
  box-shadow: inset 2px 0 0 var(--grn-19-acc);
}

.grn-19__rail-note {
  margin: 0;
  padding-block-start: 1rem;
  border-block-start: 1px solid var(--grn-19-line);
  color: var(--grn-19-mut);
  font-size: 0.8rem;
  text-wrap: pretty;
}

.grn-19__main {
  padding: clamp(1.5rem, 4vw, 2.6rem);
  display: grid;
  gap: clamp(1.4rem, 3.5vw, 2.2rem);
  align-content: start;
  padding-inline-end: clamp(4rem, 8vw, 5rem);
}

.grn-19__head {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.55rem;
}

.grn-19__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-19-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-19-acc);
}

.grn-19__h1 {
  margin: 0;
  font: 600 clamp(1.8rem, 4.6vw, 2.9rem)/1.05 var(--grn-19-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-19__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-19-mut);
  font-size: clamp(0.93rem, 1.8vw, 1.04rem);
  text-wrap: pretty;
}

.grn-19__stats {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(0.7rem, 1.8vw, 1.1rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
}

.grn-19__stat {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  gap: 0.15rem;
  padding: 1rem 1.15rem;
  border: 1px solid var(--grn-19-line);
  border-radius: 14px;
  min-inline-size: 0;
}

.grn-19__stat::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image: var(--grn-19-noise);
  mix-blend-mode: var(--grn-19-blend);
}

.grn-19__stat--e1 {
  background: var(--grn-19-s1);
}

.grn-19__stat--e1::after {
  opacity: var(--grn-19-g1);
}

.grn-19__stat--e2 {
  background: var(--grn-19-s2);
}

.grn-19__stat--e2::after {
  opacity: var(--grn-19-g2);
}

.grn-19__stat--e3 {
  background: var(--grn-19-s3);
}

.grn-19__stat--e3::after {
  opacity: var(--grn-19-g3);
}

.grn-19__stat-k {
  font: 400 0.7rem/1 var(--grn-19-font-mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--grn-19-mut);
}

.grn-19__stat-v {
  font: 600 1.5rem/1.1 var(--grn-19-font-display);
  letter-spacing: -0.03em;
}

.grn-19__stat-m {
  font: 400 0.76rem/1 var(--grn-19-font-mono);
  color: var(--grn-19-acc);
}

.grn-19__panels {
  display: grid;
  gap: clamp(0.8rem, 2vw, 1.2rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  align-items: start;
}

.grn-19__panel {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  gap: 0.8rem;
  align-content: start;
  padding: clamp(1.1rem, 2.6vw, 1.5rem);
  border: 1px solid var(--grn-19-line);
  border-radius: 16px;
  background: var(--grn-19-s2);
  min-inline-size: 0;
}

.grn-19__panel::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image: var(--grn-19-noise);
  opacity: var(--grn-19-g2);
  mix-blend-mode: var(--grn-19-blend);
}

.grn-19__panel--wide {
  grid-column: 1 / -1;
}

.grn-19__panel-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.6rem;
  padding-block-end: 0.6rem;
  border-block-end: 1px solid var(--grn-19-line);
}

.grn-19__h2 {
  margin: 0;
  font: 600 1rem/1.2 var(--grn-19-font-display);
  letter-spacing: -0.015em;
}

.grn-19__pill {
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  background: color-mix(in oklab, var(--grn-19-acc) 18%, transparent);
  color: var(--grn-19-acc);
  font: 500 0.66rem/1.6 var(--grn-19-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.grn-19__panel-note {
  margin: 0;
  color: var(--grn-19-mut);
  font-size: 0.83rem;
  text-wrap: pretty;
}

.grn-19__chart {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  align-items: end;
  gap: clamp(0.4rem, 1.5vw, 0.9rem);
  block-size: clamp(7rem, 16vw, 10rem);
  padding-block-start: 0.5rem;
}

.grn-19__bar {
  position: relative;
  display: block;
  block-size: var(--grn-19-h);
  border-radius: 8px 8px 0 0;
  background: color-mix(in oklab, var(--grn-19-acc) 28%, var(--grn-19-s3));
}

.grn-19__bar--mark {
  background: var(--grn-19-acc);
}

.grn-19__bar b {
  position: absolute;
  inset-inline: 0;
  inset-block-start: -1.35rem;
  text-align: center;
  font: 500 0.7rem/1 var(--grn-19-font-mono);
  color: var(--grn-19-mut);
}

.grn-19__bar--mark b {
  color: var(--grn-19-ink);
}

.grn-19__blends {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.1rem;
}

.grn-19__blends li {
  display: grid;
  gap: 0.1rem;
  padding-block: 0.55rem;
  border-block-start: 1px solid var(--grn-19-line);
}

.grn-19__blends li:first-child {
  border-block-start: 0;
}

.grn-19__blends b {
  font: 500 0.88rem/1.2 var(--grn-19-font-mono);
}

.grn-19__blends span {
  color: var(--grn-19-mut);
  font-size: 0.82rem;
  text-wrap: pretty;
}

.grn-19__ratios {
  display: grid;
  gap: 0;
  margin: 0;
}

.grn-19__ratios > div {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.6rem;
  padding-block: 0.5rem;
  border-block-start: 1px solid var(--grn-19-line);
}

.grn-19__ratios dt {
  margin: 0;
  color: var(--grn-19-mut);
  font-size: 0.83rem;
}

.grn-19__ratios dd {
  margin: 0;
  font: 600 0.9rem/1 var(--grn-19-font-mono);
  font-variant-numeric: tabular-nums;
}

.grn-19__stat,
.grn-19__panel {
  transition: transform 260ms cubic-bezier(0.22, 1, 0.36, 1);
}

@media (hover: hover) and (pointer: fine) {
  .grn-19__stat:hover {
    transform: translateY(-3px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-19__stat,
    .grn-19__panel {
    transition-duration: 1ms;
    transform: none;
  }
}
```
