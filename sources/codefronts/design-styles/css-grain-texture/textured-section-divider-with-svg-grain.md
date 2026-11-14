---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/textured-section-divider-with-svg-grain/"
title: "Textured Section Divider with SVG Grain"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Two coloured sections meeting at a hard line is the most obvious seam in web design."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Textured Section Divider with SVG Grain
Source: https://codefronts.com/design-styles/css-grain-texture/textured-section-divider-with-svg-grain/

Two coloured sections meeting at a hard line is the most obvious seam in web design. This divider replaces it with a torn, grained transition: a mask driven by feTurbulence so the edge dissolves irregularly instead of stepping, and a grain band that carries texture across the join. Three divider variants — torn, fade, and ruled — in one page.
## HTML
```html
<section class="grn-13" aria-labelledby="grn-13-title">
  <svg class="grn-13__defs" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="grn-13-tear" x="-20%" y="-40%" width="140%" height="180%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.012 0.34" numOctaves="3" seed="23" result="grn13noise"/>
      <feDisplacementMap in="SourceGraphic" in2="grn13noise" scale="18" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </svg>

  <div class="grn-13__theme">
    <input class="grn-13__theme-input" type="checkbox" id="grn-13-theme">
    <label class="grn-13__theme-label" for="grn-13-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-13__sr">Toggle dark theme</span>
    </label>
  </div>

  <section class="grn-13__band grn-13__band--top" aria-labelledby="grn-13-title">
    <div class="grn-13__inner">
      <p class="grn-13__kicker">Field guide · issue 12</p>
      <h1 class="grn-13__h1" id="grn-13-title">Sections should meet like materials, not like divs</h1>
      <p class="grn-13__lede">Below this paragraph the edge is torn by an SVG displacement map, and the grain band runs straight across the join. That continuity is what makes it read as one surface.</p>
    </div>
    <span class="grn-13__tear" aria-hidden="true"></span>
    <span class="grn-13__band-grain" aria-hidden="true"></span>
  </section>

  <section class="grn-13__band grn-13__band--mid" aria-labelledby="grn-13-h-fade">
    <span class="grn-13__band-grain" aria-hidden="true"></span>
    <div class="grn-13__inner">
      <h2 class="grn-13__h2" id="grn-13-h-fade">The grained fade</h2>
      <p class="grn-13__body">The workhorse. A <code>linear-gradient</code> mask dissolves the section boundary over 8rem while the grain layer continues at identical weight on both sides. Use it in long documents where you want sections to breathe without adding visual events. It costs one mask and no extra DOM.</p>
      <ul class="grn-13__facts">
        <li><b>Mask</b><span>linear-gradient, 8rem</span></li>
        <li><b>Grain</b><span>continuous, 0.05</span></li>
        <li><b>DOM added</b><span>none</span></li>
      </ul>
    </div>
    <span class="grn-13__fade" aria-hidden="true"></span>
  </section>

  <section class="grn-13__band grn-13__band--bottom" aria-labelledby="grn-13-h-rule">
    <span class="grn-13__band-grain" aria-hidden="true"></span>
    <div class="grn-13__inner">
      <h2 class="grn-13__h2" id="grn-13-h-rule">The ruled divider that does not look like a border</h2>
      <p class="grn-13__body">A hairline with a grain wash spilling past it in both directions. Utilitarian, appropriate in dashboards and documentation, and the only one of the three that survives being used a dozen times on one page.</p>
      <p class="grn-13__foot-note">Pick one divider per page. This demo shows all three because it is a specimen sheet — shipping all three would be a design failure, not a feature.</p>
    </div>
  </section>
</section>
```
## CSS
```css
.grn-13 {
  --grn-13-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='170' height='170'%3E%3Cfilter id='grn13n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='170' height='170' filter='url(%23grn13n)'/%3E%3C/svg%3E");
  --grn-13-top: #e9ecdf;
  --grn-13-top: oklch(93% 0.02 120);
  --grn-13-mid: #47543a;
  --grn-13-mid: oklch(42% 0.05 130);
  --grn-13-bottom: #f4f5ee;
  --grn-13-bottom: oklch(96% 0.01 120);
  --grn-13-ink: #1f2418;
  --grn-13-ink-on-mid: #eef2e4;
  --grn-13-mut: #616a55;
  --grn-13-acc: #7f9b3f;
  --grn-13-acc: oklch(62% 0.13 128);
  --grn-13-grain: 0.05;
  --grn-13-tear-h: clamp(3rem, 8vw, 6rem);
  --grn-13-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-13-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-13-bottom);
  color: var(--grn-13-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}

.grn-13 *,
.grn-13 *::before,
.grn-13 *::after {
  box-sizing: border-box;
}

.grn-13 :focus-visible {
  outline: 2px solid var(--grn-13-acc);
  outline-offset: 3px;
}

.grn-13 code {
  font-family: var(--grn-13-font-mono);
  font-size: 0.9em;
}

.grn-13__sr {
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

.grn-13__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.grn-13:has(.grn-13__theme-input:checked) {
  --grn-13-top: #171a13;
  --grn-13-top: oklch(20% 0.02 125);
  --grn-13-mid: #2b3324;
  --grn-13-mid: oklch(28% 0.04 130);
  --grn-13-bottom: #101208;
  --grn-13-bottom: oklch(16% 0.02 118);
  --grn-13-ink: #e8eddd;
  --grn-13-ink-on-mid: #e8eddd;
  --grn-13-mut: #9aa68c;
  --grn-13-acc: #b6d16a;
  --grn-13-acc: oklch(83% 0.15 122);
  --grn-13-grain: 0.075;
}

@media (prefers-color-scheme: dark) {
  .grn-13 {
    --grn-13-top: #171a13;
    --grn-13-top: oklch(20% 0.02 125);
    --grn-13-mid: #2b3324;
    --grn-13-mid: oklch(28% 0.04 130);
    --grn-13-bottom: #101208;
    --grn-13-bottom: oklch(16% 0.02 118);
    --grn-13-ink: #e8eddd;
    --grn-13-ink-on-mid: #e8eddd;
    --grn-13-mut: #9aa68c;
    --grn-13-acc: #b6d16a;
    --grn-13-acc: oklch(83% 0.15 122);
    --grn-13-grain: 0.075;
  }

  .grn-13:has(.grn-13__theme-input:checked) {
    --grn-13-top: #e9ecdf;
    --grn-13-top: oklch(93% 0.02 120);
    --grn-13-mid: #47543a;
    --grn-13-mid: oklch(42% 0.05 130);
    --grn-13-bottom: #f4f5ee;
    --grn-13-bottom: oklch(96% 0.01 120);
    --grn-13-ink: #1f2418;
    --grn-13-ink-on-mid: #eef2e4;
    --grn-13-mut: #616a55;
    --grn-13-acc: #7f9b3f;
    --grn-13-acc: oklch(62% 0.13 128);
    --grn-13-grain: 0.05;
  }
}

@media (prefers-color-scheme: light) {
  .grn-13:has(.grn-13__theme-input:checked) {
    --grn-13-top: #171a13;
    --grn-13-top: oklch(20% 0.02 125);
    --grn-13-mid: #2b3324;
    --grn-13-mid: oklch(28% 0.04 130);
    --grn-13-bottom: #101208;
    --grn-13-bottom: oklch(16% 0.02 118);
    --grn-13-ink: #e8eddd;
    --grn-13-ink-on-mid: #e8eddd;
    --grn-13-mut: #9aa68c;
    --grn-13-acc: #b6d16a;
    --grn-13-acc: oklch(83% 0.15 122);
    --grn-13-grain: 0.075;
  }
}

.grn-13__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 60;
}

.grn-13__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-13__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid color-mix(in oklab, var(--grn-13-ink) 22%, transparent);
  border-radius: 999px;
  background: var(--grn-13-bottom);
  color: var(--grn-13-ink);
  cursor: pointer;
}

.grn-13__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-13__band {
  position: relative;
  isolation: isolate;
}

.grn-13__band--top {
  background: var(--grn-13-top);
  padding-block: clamp(3.5rem, 9vw, 6rem) calc(var(--grn-13-tear-h) + clamp(2rem, 5vw, 3.5rem));
}

.grn-13__band--mid {
  background: var(--grn-13-mid);
  color: var(--grn-13-ink-on-mid);
  padding-block: clamp(3rem, 8vw, 5rem) clamp(5rem, 12vw, 8rem);
  margin-block-start: calc(var(--grn-13-tear-h) * -1);
}

.grn-13__band--bottom {
  background: var(--grn-13-bottom);
  padding-block: clamp(3rem, 8vw, 5rem) clamp(3.5rem, 9vw, 6rem);
}

.grn-13__band--bottom::before {
  content: "";
  display: block;
  block-size: 1px;
  inline-size: min(64rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin: 0 auto clamp(2rem, 5vw, 3rem);
  background: color-mix(in oklab, var(--grn-13-ink) 20%, transparent);
}

.grn-13__band-grain {
  position: absolute;
  inset: calc(var(--grn-13-tear-h) * -1) 0;
  z-index: 1;
  pointer-events: none;
  background-image: var(--grn-13-noise);
  opacity: var(--grn-13-grain);
  mix-blend-mode: overlay;
}

.grn-13__tear {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  z-index: 2;
  block-size: var(--grn-13-tear-h);
  background: var(--grn-13-top);
  filter: url(#grn-13-tear);
  pointer-events: none;
}

.grn-13__fade {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  z-index: 2;
  block-size: clamp(5rem, 12vw, 8rem);
  background: var(--grn-13-bottom);
  pointer-events: none;
  -webkit-mask-image: linear-gradient(to bottom, transparent, #000 82%);
  mask-image: linear-gradient(to bottom, transparent, #000 82%);
}

.grn-13__inner {
  position: relative;
  z-index: 3;
  inline-size: min(64rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  display: grid;
  gap: 0.75rem;
  max-inline-size: 46rem;
}

.grn-13__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-13-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-13-acc);
}

.grn-13__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.6vw, 3.5rem)/1.03 var(--grn-13-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-13__h2 {
  margin: 0;
  font: 600 clamp(1.4rem, 3.6vw, 2.1rem)/1.1 var(--grn-13-font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.grn-13__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-13-mut);
  font-size: clamp(0.97rem, 2vw, 1.1rem);
  text-wrap: pretty;
}

.grn-13__body {
  margin: 0;
  max-inline-size: 42rem;
  font-size: clamp(0.95rem, 1.9vw, 1.05rem);
  text-wrap: pretty;
  color: color-mix(in oklab, currentColor 82%, transparent);
}

.grn-13__facts {
  list-style: none;
  margin: 0.4rem 0 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.8rem;
}

.grn-13__facts li {
  display: grid;
  gap: 0.1rem;
}

.grn-13__facts b {
  font: 600 0.8rem/1.2 var(--grn-13-font-display);
}

.grn-13__facts span {
  font: 400 0.78rem/1.2 var(--grn-13-font-mono);
  opacity: 0.75;
}

.grn-13__foot-note {
  margin: 0.5rem 0 0;
  padding-block-start: 0.8rem;
  border-block-start: 1px solid color-mix(in oklab, var(--grn-13-ink) 16%, transparent);
  color: var(--grn-13-mut);
  font-size: 0.85rem;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .grn-13 * {
    transition-duration: 1ms !important;
    animation-duration: 1ms !important;
  }
}
```
