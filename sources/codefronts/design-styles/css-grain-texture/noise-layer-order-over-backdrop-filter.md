---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/noise-layer-order-over-backdrop-filter/"
title: "Noise Layer Order Over backdrop-filter"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Frosted glass looks fake because real glass has surface imperfection and backdrop-filter: blur() has none."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Noise Layer Order Over backdrop-filter
Source: https://codefronts.com/design-styles/css-grain-texture/noise-layer-order-over-backdrop-filter/

Frosted glass looks fake because real glass has surface imperfection and backdrop-filter: blur() has none. Adding grain fixes it — but only if the grain sits above the blur. This demo ships both orders side by side over the same photograph so the difference is impossible to miss, plus a full glass panel set you can lift straight into a product.
## HTML
```html
<section class="grn-11" aria-labelledby="grn-11-title">
  <img class="grn-11__bg" src="https://picsum.photos/id/1029/2000/1300" alt="" aria-hidden="true" width="2000" height="1300">
  <span class="grn-11__bg-wash" aria-hidden="true"></span>

  <div class="grn-11__theme">
    <input class="grn-11__theme-input" type="checkbox" id="grn-11-theme">
    <label class="grn-11__theme-label" for="grn-11-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-11__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-11__shell">
    <header class="grn-11__head">
      <p class="grn-11__kicker">Layer order · 11</p>
      <h1 class="grn-11__h1" id="grn-11-title">Glass needs grain, and grain needs to be on top</h1>
      <p class="grn-11__lede">Both panels below use the same blur and the same noise token. One puts the grain behind the glass, where the blur destroys it. The other puts it in front, where it becomes surface.</p>
    </header>

    <div class="grn-11__ab">
      <article class="grn-11__panel grn-11__panel--under">
        <p class="grn-11__flag grn-11__flag--bad">Grain behind the blur</p>
        <h2 class="grn-11__panel-h">Smooth and synthetic</h2>
        <p class="grn-11__panel-b">The noise is a background on the glass itself, so <code>backdrop-filter</code> averages it away. What is left is a plastic sheet.</p>
      </article>

      <article class="grn-11__panel grn-11__panel--over">
        <span class="grn-11__grain" aria-hidden="true"></span>
        <p class="grn-11__flag grn-11__flag--good">Grain above the blur</p>
        <h2 class="grn-11__panel-h">Etched and physical</h2>
        <p class="grn-11__panel-b">The noise is a child layer painted after the filter, so it survives intact and reads as imperfection in the glass.</p>
      </article>
    </div>

    <section class="grn-11__player" aria-labelledby="grn-11-h-player">
      <span class="grn-11__grain" aria-hidden="true"></span>
      <div class="grn-11__player-body">
        <div class="grn-11__now">
          <p class="grn-11__eyebrow">Now playing</p>
          <h2 class="grn-11__track" id="grn-11-h-player">Rue des Trois Frères</h2>
          <p class="grn-11__artist">Sylvie Marchand · Nocturnes vol. II</p>
        </div>
        <div class="grn-11__scrub">
          <span class="grn-11__bar"><span class="grn-11__played"></span></span>
          <div class="grn-11__times"><span>2:41</span><span>5:08</span></div>
        </div>
        <div class="grn-11__transport">
          <button class="grn-11__tbtn" type="button" aria-label="Previous track">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M18 6v12L9 12ZM7 6v12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
          </button>
          <button class="grn-11__tbtn grn-11__tbtn--play" type="button" aria-label="Pause">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6v12M15 6v12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          </button>
          <button class="grn-11__tbtn" type="button" aria-label="Next track">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6v12l9-6ZM17 6v12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
          </button>
        </div>
      </div>
    </section>

    <ul class="grn-11__tiles">
      <li class="grn-11__tile"><span class="grn-11__grain" aria-hidden="true"></span><span class="grn-11__tile-k">blur</span><span class="grn-11__tile-v">18px</span></li>
      <li class="grn-11__tile"><span class="grn-11__grain" aria-hidden="true"></span><span class="grn-11__tile-k">saturate</span><span class="grn-11__tile-v">1.4</span></li>
      <li class="grn-11__tile"><span class="grn-11__grain" aria-hidden="true"></span><span class="grn-11__tile-k">grain</span><span class="grn-11__tile-v">0.08</span></li>
      <li class="grn-11__tile"><span class="grn-11__grain" aria-hidden="true"></span><span class="grn-11__tile-k">fallback</span><span class="grn-11__tile-v">@supports</span></li>
    </ul>
  </main>
</section>
```
## CSS
```css
.grn-11 {
  --grn-11-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='grn11n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23grn11n)'/%3E%3C/svg%3E");
  --grn-11-blur: 18px;
  --grn-11-grain: 0.08;
  --grn-11-glass: rgba(14, 16, 24, 0.34);
  --grn-11-glass-solid: rgba(14, 16, 24, 0.9);
  --grn-11-rim: rgba(255, 255, 255, 0.26);
  --grn-11-ink: #f4f6fb;
  --grn-11-mut: rgba(244, 246, 251, 0.72);
  --grn-11-acc: #7dd3fc;
  --grn-11-acc: oklch(84% 0.1 226);
  --grn-11-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-11-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  background: #0a0d14;
  color: var(--grn-11-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-11 *,
.grn-11 *::before,
.grn-11 *::after {
  box-sizing: border-box;
}

.grn-11 :focus-visible {
  outline: 2px solid var(--grn-11-acc);
  outline-offset: 3px;
}

.grn-11 code {
  font-family: var(--grn-11-font-mono);
  font-size: 0.9em;
}

.grn-11__sr {
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

.grn-11:has(.grn-11__theme-input:checked) {
  --grn-11-glass: rgba(250, 250, 252, 0.42);
  --grn-11-glass-solid: rgba(250, 250, 252, 0.94);
  --grn-11-rim: rgba(255, 255, 255, 0.8);
  --grn-11-ink: #0d1016;
  --grn-11-mut: rgba(13, 16, 22, 0.7);
  --grn-11-acc: #0369a1;
  --grn-11-acc: oklch(48% 0.11 235);
  --grn-11-grain: 0.06;
}

@media (prefers-color-scheme: light) {
  .grn-11 {
    --grn-11-glass: rgba(250, 250, 252, 0.42);
    --grn-11-glass-solid: rgba(250, 250, 252, 0.94);
    --grn-11-rim: rgba(255, 255, 255, 0.8);
    --grn-11-ink: #0d1016;
    --grn-11-mut: rgba(13, 16, 22, 0.7);
    --grn-11-acc: #0369a1;
    --grn-11-acc: oklch(48% 0.11 235);
    --grn-11-grain: 0.06;
  }

  .grn-11:has(.grn-11__theme-input:checked) {
    --grn-11-glass: rgba(14, 16, 24, 0.34);
    --grn-11-glass-solid: rgba(14, 16, 24, 0.9);
    --grn-11-rim: rgba(255, 255, 255, 0.26);
    --grn-11-ink: #f4f6fb;
    --grn-11-mut: rgba(244, 246, 251, 0.72);
    --grn-11-acc: #7dd3fc;
    --grn-11-acc: oklch(84% 0.1 226);
    --grn-11-grain: 0.08;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-11:has(.grn-11__theme-input:checked) {
    --grn-11-glass: rgba(250, 250, 252, 0.42);
    --grn-11-glass-solid: rgba(250, 250, 252, 0.94);
    --grn-11-rim: rgba(255, 255, 255, 0.8);
    --grn-11-ink: #0d1016;
    --grn-11-mut: rgba(13, 16, 22, 0.7);
    --grn-11-acc: #0369a1;
    --grn-11-acc: oklch(48% 0.11 235);
    --grn-11-grain: 0.06;
  }
}

.grn-11__bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

.grn-11__bg-wash {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: linear-gradient(190deg, rgba(6, 10, 20, 0.4), rgba(6, 10, 20, 0.66));
}

.grn-11__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 60;
}

.grn-11__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-11__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-11-rim);
  border-radius: 999px;
  background: var(--grn-11-glass);
  color: var(--grn-11-ink);
  cursor: pointer;
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.grn-11__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-11__theme-input:focus-visible + .grn-11__theme-label {
  outline: 2px solid var(--grn-11-acc);
  outline-offset: 3px;
}

.grn-11__shell {
  position: relative;
  z-index: 5;
  inline-size: min(72rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(1.4rem, 3.5vw, 2.2rem);
}

.grn-11__head {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.6rem;
}

.grn-11__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-11-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-11-acc);
}

.grn-11__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.4vw, 3.4rem)/1.03 var(--grn-11-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-11__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-11-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.08rem);
  text-wrap: pretty;
}

.grn-11__grain {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  background-image: var(--grn-11-noise);
  opacity: var(--grn-11-grain);
  mix-blend-mode: overlay;
  border-radius: inherit;
}

.grn-11__ab {
  display: grid;
  gap: clamp(0.9rem, 2.2vw, 1.4rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
}

.grn-11__panel {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  align-content: start;
  gap: 0.45rem;
  padding: clamp(1.2rem, 3vw, 1.8rem);
  border: 1px solid var(--grn-11-rim);
  border-radius: 18px;
  background: var(--grn-11-glass-solid);
  box-shadow: inset 0 1px 0 var(--grn-11-rim), 0 24px 60px -34px rgba(0, 0, 0, 0.7);
  min-inline-size: 0;
}

@supports ((-webkit-backdrop-filter: blur(1px)) or (backdrop-filter: blur(1px))) {
  .grn-11__panel,
    .grn-11__player,
    .grn-11__tile {
    background: var(--grn-11-glass);
    -webkit-backdrop-filter: blur(var(--grn-11-blur)) saturate(1.4);
    backdrop-filter: blur(var(--grn-11-blur)) saturate(1.4);
  }
}

.grn-11__panel--under {
  background-image: var(--grn-11-noise);
  background-blend-mode: overlay;
}

.grn-11__flag {
  margin: 0;
  justify-self: start;
  padding: 0.25rem 0.6rem;
  border-radius: 999px;
  font: 600 0.68rem/1.5 var(--grn-11-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.grn-11__flag--bad {
  background: rgba(248, 113, 113, 0.24);
  color: #fecaca;
}

.grn-11__flag--good {
  background: rgba(125, 211, 252, 0.24);
  color: #e0f2fe;
}

.grn-11__panel-h {
  margin: 0.2rem 0 0;
  font: 600 1.15rem/1.2 var(--grn-11-font-display);
  letter-spacing: -0.02em;
}

.grn-11__panel-b {
  margin: 0;
  color: var(--grn-11-mut);
  font-size: 0.9rem;
  text-wrap: pretty;
}

.grn-11__player {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  border: 1px solid var(--grn-11-rim);
  border-radius: 22px;
  background: var(--grn-11-glass-solid);
  box-shadow: inset 0 1px 0 var(--grn-11-rim), 0 30px 80px -40px rgba(0, 0, 0, 0.75);
}

.grn-11__player-body {
  position: relative;
  z-index: 3;
  display: grid;
  gap: 1.1rem;
  padding: clamp(1.3rem, 3.4vw, 2rem);
}

.grn-11__eyebrow {
  margin: 0;
  font: 500 0.68rem/1 var(--grn-11-font-mono);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--grn-11-acc);
}

.grn-11__track {
  margin: 0.3rem 0 0.15rem;
  font: 600 clamp(1.3rem, 3.4vw, 1.9rem)/1.1 var(--grn-11-font-display);
  letter-spacing: -0.03em;
}

.grn-11__artist {
  margin: 0;
  color: var(--grn-11-mut);
  font-size: 0.9rem;
}

.grn-11__scrub {
  display: grid;
  gap: 0.4rem;
}

.grn-11__bar {
  display: block;
  block-size: 6px;
  border-radius: 999px;
  overflow: hidden;
  background: color-mix(in oklab, var(--grn-11-ink) 22%, transparent);
}

.grn-11__played {
  display: block;
  inline-size: 52%;
  block-size: 100%;
  border-radius: 999px;
  background: var(--grn-11-acc);
}

.grn-11__times {
  display: flex;
  justify-content: space-between;
  font: 400 0.75rem/1 var(--grn-11-font-mono);
  color: var(--grn-11-mut);
}

.grn-11__transport {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.grn-11__tbtn {
  display: grid;
  place-items: center;
  inline-size: 48px;
  block-size: 48px;
  border: 1px solid var(--grn-11-rim);
  border-radius: 999px;
  background: color-mix(in oklab, var(--grn-11-ink) 8%, transparent);
  color: var(--grn-11-ink);
  cursor: pointer;
}

.grn-11__tbtn svg {
  inline-size: 22px;
  block-size: 22px;
}

.grn-11__tbtn--play {
  inline-size: 58px;
  block-size: 58px;
  background: var(--grn-11-acc);
  border-color: transparent;
  color: #06202c;
}

.grn-11__tbtn:hover {
  filter: brightness(1.12);
}

.grn-11__tiles {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(0.6rem, 1.6vw, 1rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 8.5rem), 1fr));
}

.grn-11__tile {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  gap: 0.2rem;
  padding: 0.85rem 1rem;
  border: 1px solid var(--grn-11-rim);
  border-radius: 14px;
  background: var(--grn-11-glass-solid);
  box-shadow: inset 0 1px 0 var(--grn-11-rim);
  min-inline-size: 0;
}

.grn-11__tile-k {
  position: relative;
  z-index: 3;
  font: 400 0.68rem/1 var(--grn-11-font-mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--grn-11-mut);
}

.grn-11__tile-v {
  position: relative;
  z-index: 3;
  font: 600 1.05rem/1.2 var(--grn-11-font-mono);
}

.grn-11__panel,
.grn-11__tile,
.grn-11__tbtn {
  transition: transform 280ms cubic-bezier(0.22, 1, 0.36, 1), filter 200ms ease;
}

@media (hover: hover) and (pointer: fine) {
  .grn-11__panel:hover,
    .grn-11__tile:hover {
    transform: translateY(-3px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-11__panel,
    .grn-11__tile,
    .grn-11__tbtn {
    transition-duration: 1ms;
    transform: none;
  }
}
```
