---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/full-bleed-hero-section-noise-background/"
title: "Full-Bleed Hero Section Noise Background"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "A production landing hero: photograph, colour wash, two grain layers at different scales, and a text scrim that guarantees contrast."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Bleed Hero Section Noise Background
Source: https://codefronts.com/design-styles/css-grain-texture/full-bleed-hero-section-noise-background/

A production landing hero: photograph, colour wash, two grain layers at different scales, and a text scrim that guarantees contrast. Full-bleed, 100svh-correct on mobile, and built so the treatment survives every image you swap in — which is the actual requirement, since you do not control the photo the marketing team picks.
## HTML
```html
<section class="grn-10" aria-labelledby="grn-10-title">
  <div class="grn-10__theme">
    <input class="grn-10__theme-input" type="checkbox" id="grn-10-theme">
    <label class="grn-10__theme-label" for="grn-10-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-10__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="grn-10__hero">
    <img class="grn-10__photo" src="https://picsum.photos/id/1018/2000/1200" alt="" aria-hidden="true" width="2000" height="1200">
    <span class="grn-10__wash" aria-hidden="true"></span>
    <span class="grn-10__grain grn-10__grain--coarse" aria-hidden="true"></span>
    <span class="grn-10__grain grn-10__grain--fine" aria-hidden="true"></span>
    <span class="grn-10__scrim" aria-hidden="true"></span>

    <nav class="grn-10__nav" aria-label="Primary">
      <a class="grn-10__brand" href="#grn-10-title">Northline</a>
      <ul class="grn-10__links">
        <li><a href="#grn-10-title">Expeditions</a></li>
        <li><a href="#grn-10-title">Field notes</a></li>
        <li><a href="#grn-10-title">Kit</a></li>
      </ul>
      <a class="grn-10__nav-cta" href="#grn-10-title">Book a slot</a>
    </nav>

    <div class="grn-10__copy">
      <p class="grn-10__kicker">Season opens 14 March · 9 departures</p>
      <h1 class="grn-10__h1" id="grn-10-title">Ten days above the treeline</h1>
      <p class="grn-10__lede">Guided high routes across the northern ranges. Small groups, real weather, no helicopters. The photograph is unedited — everything you see over it is four layers of CSS.</p>
      <div class="grn-10__actions">
        <a class="grn-10__cta" href="#grn-10-title">See the routes</a>
        <a class="grn-10__cta grn-10__cta--ghost" href="#grn-10-title">Read the kit list</a>
      </div>
      <dl class="grn-10__stats">
        <div><dt>Layers</dt><dd>4</dd></div>
        <div><dt>Grain scales</dt><dd>2</dd></div>
        <div><dt>Requests added</dt><dd>0</dd></div>
      </dl>
    </div>
  </div>

  <section class="grn-10__below" aria-labelledby="grn-10-h-below">
    <h2 class="grn-10__h2" id="grn-10-h-below">Why two grain scales</h2>
    <p class="grn-10__below-body">One fine layer over a photo reads as sensor noise. A second layer at a fifth of the frequency and a twentieth of the opacity adds unevenness the eye interprets as atmosphere. The fine layer gives the surface tooth; the coarse layer gives the frame weather. Together they cost two composites and no requests.</p>
  </section>
</section>
```
## CSS
```css
.grn-10 {
  --grn-10-fine: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='170' height='170'%3E%3Cfilter id='grn10a'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='170' height='170' filter='url(%23grn10a)'/%3E%3C/svg%3E");
  --grn-10-coarse: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='420' height='420'%3E%3Cfilter id='grn10b'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.14' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='420' height='420' filter='url(%23grn10b)'/%3E%3C/svg%3E");
  --grn-10-bg: #06100f;
  --grn-10-surf: #0d1a19;
  --grn-10-line: #1e3230;
  --grn-10-ink: #ecf6f4;
  --grn-10-mut: #9ab5b1;
  --grn-10-acc: #5eead4;
  --grn-10-acc: oklch(86% 0.13 175);
  --grn-10-on-acc: #04211d;
  --grn-10-wash-col: #062b28;
  --grn-10-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-10-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-10-bg);
  color: var(--grn-10-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-10 *,
.grn-10 *::before,
.grn-10 *::after {
  box-sizing: border-box;
}

.grn-10 :focus-visible {
  outline: 2px solid var(--grn-10-acc);
  outline-offset: 3px;
}

.grn-10 code {
  font-family: var(--grn-10-font-mono);
  font-size: 0.9em;
}

.grn-10__sr {
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

.grn-10:has(.grn-10__theme-input:checked) {
  --grn-10-bg: #eef5f3;
  --grn-10-surf: #ffffff;
  --grn-10-line: #d3e3e0;
  --grn-10-ink: #06100f;
  --grn-10-mut: #52706c;
  --grn-10-acc: #0f766e;
  --grn-10-acc: oklch(50% 0.1 180);
  --grn-10-on-acc: #ecfdf5;
  --grn-10-wash-col: #0d3b36;
}

@media (prefers-color-scheme: light) {
  .grn-10 {
    --grn-10-bg: #eef5f3;
    --grn-10-surf: #ffffff;
    --grn-10-line: #d3e3e0;
    --grn-10-ink: #06100f;
    --grn-10-mut: #52706c;
    --grn-10-acc: #0f766e;
    --grn-10-acc: oklch(50% 0.1 180);
    --grn-10-on-acc: #ecfdf5;
    --grn-10-wash-col: #0d3b36;
  }

  .grn-10:has(.grn-10__theme-input:checked) {
    --grn-10-bg: #06100f;
    --grn-10-surf: #0d1a19;
    --grn-10-line: #1e3230;
    --grn-10-ink: #ecf6f4;
    --grn-10-mut: #9ab5b1;
    --grn-10-acc: #5eead4;
    --grn-10-acc: oklch(86% 0.13 175);
    --grn-10-on-acc: #04211d;
    --grn-10-wash-col: #062b28;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-10:has(.grn-10__theme-input:checked) {
    --grn-10-bg: #eef5f3;
    --grn-10-surf: #ffffff;
    --grn-10-line: #d3e3e0;
    --grn-10-ink: #06100f;
    --grn-10-mut: #52706c;
    --grn-10-acc: #0f766e;
    --grn-10-acc: oklch(50% 0.1 180);
    --grn-10-on-acc: #ecfdf5;
    --grn-10-wash-col: #0d3b36;
  }
}

.grn-10__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 60;
}

.grn-10__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-10__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 999px;
  background: rgba(4, 14, 13, 0.45);
  color: #ecf6f4;
  cursor: pointer;
  backdrop-filter: blur(8px);
}

.grn-10__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-10__theme-input:focus-visible + .grn-10__theme-label {
  outline: 2px solid var(--grn-10-acc);
  outline-offset: 3px;
}

.grn-10__hero {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  grid-template-rows: auto 1fr;
  min-block-size: 100vh;
  min-block-size: 100svh;
}

.grn-10__photo {
  position: absolute;
  inset: 0;
  z-index: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

.grn-10__wash {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: linear-gradient(200deg, color-mix(in oklab, var(--grn-10-wash-col) 74%, transparent) 0%, color-mix(in oklab, var(--grn-10-wash-col) 42%, transparent) 55%, transparent 100%);
}

.grn-10__grain {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.grn-10__grain--coarse {
  z-index: 2;
  background-image: var(--grn-10-coarse);
  opacity: 0.07;
  mix-blend-mode: overlay;
}

.grn-10__grain--fine {
  z-index: 3;
  background-image: var(--grn-10-fine);
  opacity: 0.1;
  mix-blend-mode: luminosity;
}

.grn-10__scrim {
  position: absolute;
  inset: 0;
  z-index: 4;
  background: linear-gradient(to top, rgba(3, 12, 11, 0.88) 0%, rgba(3, 12, 11, 0.62) 34%, rgba(3, 12, 11, 0.12) 68%, transparent 100%);
}

.grn-10__nav {
  position: relative;
  z-index: 6;
  inline-size: min(78rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem clamp(1rem, 3vw, 2rem);
  padding-block: clamp(1rem, 3vw, 1.6rem);
  padding-inline-end: 60px;
  color: #ecf6f4;
}

.grn-10__brand {
  color: inherit;
  text-decoration: none;
  font: 600 1.05rem/1 var(--grn-10-font-display);
  letter-spacing: -0.02em;
}

.grn-10__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem;
}

.grn-10__links a {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.8rem;
  color: rgba(236, 246, 244, 0.82);
  text-decoration: none;
  font-size: 0.9rem;
}

.grn-10__links a:hover {
  color: #fff;
}

.grn-10__nav-cta {
  margin-inline-start: auto;
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.32);
  border-radius: 999px;
  color: #ecf6f4;
  text-decoration: none;
  font: 600 0.84rem/1 var(--grn-10-font-display);
  backdrop-filter: blur(6px);
}

.grn-10__nav-cta:hover {
  background: rgba(255, 255, 255, 0.12);
}

.grn-10__copy {
  position: relative;
  z-index: 6;
  inline-size: min(78rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  align-self: end;
  display: grid;
  gap: 0.9rem;
  max-inline-size: 44rem;
  padding-block: clamp(2.5rem, 8vw, 5rem);
  color: #f2fbf9;
}

.grn-10__kicker {
  margin: 0;
  font: 500 0.74rem/1 var(--grn-10-font-mono);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--grn-10-acc);
}

.grn-10__h1 {
  margin: 0;
  font: 600 clamp(2.4rem, 8vw, 5.2rem)/0.97 var(--grn-10-font-display);
  letter-spacing: -0.045em;
  text-wrap: balance;
}

.grn-10__lede {
  margin: 0;
  max-inline-size: 36rem;
  color: rgba(242, 251, 249, 0.85);
  font-size: clamp(0.97rem, 2vw, 1.13rem);
  text-wrap: pretty;
}

.grn-10__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-block-start: 0.4rem;
}

.grn-10__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 50px;
  padding-inline: 1.4rem;
  border-radius: 999px;
  background-image: var(--grn-10-fine), linear-gradient(var(--grn-10-acc), var(--grn-10-acc));
  background-blend-mode: soft-light, normal;
  color: var(--grn-10-on-acc);
  text-decoration: none;
  font: 600 0.92rem/1 var(--grn-10-font-display);
}

.grn-10__cta--ghost {
  background-image: none;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #f2fbf9;
  backdrop-filter: blur(6px);
}

.grn-10__cta:hover {
  filter: brightness(1.06);
}

.grn-10__stats {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.6rem;
  margin: 0.9rem 0 0;
  padding-block-start: 0.9rem;
  border-block-start: 1px solid rgba(255, 255, 255, 0.18);
}

.grn-10__stats > div {
  display: grid;
  gap: 0.1rem;
}

.grn-10__stats dt {
  margin: 0;
  font: 400 0.68rem/1 var(--grn-10-font-mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(242, 251, 249, 0.6);
}

.grn-10__stats dd {
  margin: 0;
  font: 600 1.15rem/1 var(--grn-10-font-mono);
}

.grn-10__below {
  inline-size: min(78rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 7vw, 4.5rem);
  display: grid;
  gap: 0.7rem;
  max-inline-size: 56rem;
}

.grn-10__h2 {
  margin: 0;
  font: 600 clamp(1.2rem, 3vw, 1.6rem)/1.2 var(--grn-10-font-display);
  letter-spacing: -0.02em;
}

.grn-10__below-body {
  margin: 0;
  color: var(--grn-10-mut);
  font-size: 0.96rem;
  text-wrap: pretty;
}

@keyframes grn-10-rise {
  from {
    opacity: 0;
    translate: 0 14px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.grn-10__copy > * {
  animation: grn-10-rise 720ms cubic-bezier(0.22, 1, 0.36, 1) both;
}

.grn-10__copy > *:nth-child(1) {
  animation-delay: 60ms;
}

.grn-10__copy > *:nth-child(2) {
  animation-delay: 130ms;
}

.grn-10__copy > *:nth-child(3) {
  animation-delay: 200ms;
}

.grn-10__copy > *:nth-child(4) {
  animation-delay: 270ms;
}

.grn-10__copy > *:nth-child(5) {
  animation-delay: 340ms;
}

@media (prefers-reduced-motion: reduce) {
  .grn-10__copy > * {
    animation-duration: 1ms;
    animation-delay: 0s;
  }
}
```
