---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/paper-stock-and-letterpress-press-effect/"
title: "Paper Stock and Letterpress Press Effect"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Letterpress is ink pressed into paper, and it comes down to two things: a paper surface with fibre, and type that is debossed with a single consistent light…"
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Paper Stock and Letterpress Press Effect
Source: https://codefronts.com/design-styles/css-grain-texture/paper-stock-and-letterpress-press-effect/

Letterpress is ink pressed into paper, and it comes down to two things: a paper surface with fibre, and type that is debossed with a single consistent light source. This is a stationery set — invitation, business card and specimen sheet — built with turbulence for the stock and a two-value text-shadow for the press.
## HTML
```html
<section class="grn-16" aria-labelledby="grn-16-title">
  <svg class="grn-16__defs" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="grn-16-fibre" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.04 0.7" numOctaves="4" seed="14" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <filter id="grn-16-deckle" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.02 0.4" numOctaves="3" seed="7" result="grn16n"/>
      <feDisplacementMap in="SourceGraphic" in2="grn16n" scale="9" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </svg>

  <div class="grn-16__theme">
    <input class="grn-16__theme-input" type="checkbox" id="grn-16-theme">
    <label class="grn-16__theme-label" for="grn-16-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-16__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-16__shell">
    <header class="grn-16__head">
      <p class="grn-16__kicker">Stock No. 4 · 600gsm cotton rag</p>
      <h1 class="grn-16__h1" id="grn-16-title">Pressed, not printed</h1>
      <p class="grn-16__lede">Directional fibre for the stock, a two-value <code>text-shadow</code> for the press, and one light source shared by every layer.</p>
    </header>

    <article class="grn-16__invite">
      <div class="grn-16__invite-inner">
        <p class="grn-16__ornament" aria-hidden="true">✦</p>
        <p class="grn-16__invite-pre">Aleksandra &amp; Tomás</p>
        <h2 class="grn-16__invite-h">request the pleasure of your company</h2>
        <p class="grn-16__invite-when">Saturday, the fourteenth of June<br>Two thousand and twenty-seven</p>
        <div class="grn-16__hair" aria-hidden="true"></div>
        <p class="grn-16__invite-where">Bracken Hall · Northumberland · 4 o'clock</p>
      </div>
    </article>

    <div class="grn-16__row">
      <article class="grn-16__bcard">
        <p class="grn-16__bcard-name">Rowan Ellis</p>
        <p class="grn-16__bcard-role">Compositor &amp; Press Operator</p>
        <dl class="grn-16__bcard-meta">
          <div><dt>Studio</dt><dd>Unit 7, Sackville Yard</dd></div>
          <div><dt>Post</dt><dd>[email protected]</dd></div>
        </dl>
      </article>

      <section class="grn-16__spec" aria-labelledby="grn-16-h-spec">
        <h2 class="grn-16__h2" id="grn-16-h-spec">Press specification</h2>
        <dl class="grn-16__spec-list">
          <div><dt>Stock</dt><dd>600gsm cotton rag, deckle edge</dd></div>
          <div><dt>Fibre</dt><dd>anisotropic turbulence · 0.04 0.7</dd></div>
          <div><dt>Impression</dt><dd>text-shadow · 1px above, 1px below</dd></div>
          <div><dt>Ink bleed</dt><dd>0 0 1px at 18% ink</dd></div>
          <div><dt>Light</dt><dd>above, consistent across all layers</dd></div>
        </dl>
        <p class="grn-16__spec-note">Deboss below 13px hurts legibility. Cap the impression at your body size and drop it entirely for captions.</p>
      </section>
    </div>
  </main>
</section>
```
## CSS
```css
.grn-16 {
  --grn-16-stock: #efe9dc;
  --grn-16-stock: oklch(92% 0.02 84);
  --grn-16-stock-2: #f8f4ea;
  --grn-16-ink: #221f1a;
  --grn-16-ink: oklch(24% 0.01 70);
  --grn-16-mut: #6b6355;
  --grn-16-line: #d8cfbc;
  --grn-16-acc: #8c2f39;
  --grn-16-acc: oklch(42% 0.13 20);
  --grn-16-press: 1px;
  --grn-16-fibre: 0.06;
  --grn-16-up: rgba(34, 31, 26, 0.24);
  --grn-16-down: rgba(255, 255, 255, 0.92);
  --grn-16-font-display: "Instrument Serif", "Cormorant Garamond", "Playfair Display", Georgia, serif;
  --grn-16-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-16-stock);
  color: var(--grn-16-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}

.grn-16 *,
.grn-16 *::before,
.grn-16 *::after {
  box-sizing: border-box;
}

.grn-16 :focus-visible {
  outline: 2px solid var(--grn-16-acc);
  outline-offset: 3px;
}

.grn-16 code {
  font-family: var(--grn-16-font-mono);
  font-size: 0.9em;
}

.grn-16__sr {
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

.grn-16__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.grn-16::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  filter: url(#grn-16-fibre);
  opacity: var(--grn-16-fibre);
  mix-blend-mode: multiply;
}

.grn-16:has(.grn-16__theme-input:checked) {
  --grn-16-stock: #171512;
  --grn-16-stock: oklch(19% 0.01 70);
  --grn-16-stock-2: #201d19;
  --grn-16-ink: #f0e9da;
  --grn-16-ink: oklch(93% 0.02 82);
  --grn-16-mut: #a49a86;
  --grn-16-line: #322c24;
  --grn-16-acc: #d9a04a;
  --grn-16-acc: oklch(75% 0.12 74);
  --grn-16-up: rgba(0, 0, 0, 0.6);
  --grn-16-down: rgba(255, 255, 255, 0.14);
  --grn-16-fibre: 0.09;
}

@media (prefers-color-scheme: dark) {
  .grn-16 {
    --grn-16-stock: #171512;
    --grn-16-stock: oklch(19% 0.01 70);
    --grn-16-stock-2: #201d19;
    --grn-16-ink: #f0e9da;
    --grn-16-ink: oklch(93% 0.02 82);
    --grn-16-mut: #a49a86;
    --grn-16-line: #322c24;
    --grn-16-acc: #d9a04a;
    --grn-16-acc: oklch(75% 0.12 74);
    --grn-16-up: rgba(0, 0, 0, 0.6);
    --grn-16-down: rgba(255, 255, 255, 0.14);
    --grn-16-fibre: 0.09;
  }

  .grn-16:has(.grn-16__theme-input:checked) {
    --grn-16-stock: #efe9dc;
    --grn-16-stock: oklch(92% 0.02 84);
    --grn-16-stock-2: #f8f4ea;
    --grn-16-ink: #221f1a;
    --grn-16-ink: oklch(24% 0.01 70);
    --grn-16-mut: #6b6355;
    --grn-16-line: #d8cfbc;
    --grn-16-acc: #8c2f39;
    --grn-16-acc: oklch(42% 0.13 20);
    --grn-16-up: rgba(34, 31, 26, 0.24);
    --grn-16-down: rgba(255, 255, 255, 0.92);
    --grn-16-fibre: 0.06;
  }
}

@media (prefers-color-scheme: light) {
  .grn-16:has(.grn-16__theme-input:checked) {
    --grn-16-stock: #171512;
    --grn-16-stock: oklch(19% 0.01 70);
    --grn-16-stock-2: #201d19;
    --grn-16-ink: #f0e9da;
    --grn-16-ink: oklch(93% 0.02 82);
    --grn-16-mut: #a49a86;
    --grn-16-line: #322c24;
    --grn-16-acc: #d9a04a;
    --grn-16-acc: oklch(75% 0.12 74);
    --grn-16-up: rgba(0, 0, 0, 0.6);
    --grn-16-down: rgba(255, 255, 255, 0.14);
    --grn-16-fibre: 0.09;
  }
}

.grn-16__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-16__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-16__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-16-line);
  border-radius: 999px;
  background: var(--grn-16-stock-2);
  color: var(--grn-16-ink);
  cursor: pointer;
  box-shadow: inset 0 1px 0 var(--grn-16-down);
}

.grn-16__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-16__shell {
  position: relative;
  z-index: 1;
  inline-size: min(72rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3rem);
}

.grn-16__head {
  max-inline-size: 44rem;
  display: grid;
  gap: 0.5rem;
}

.grn-16__kicker {
  margin: 0;
  font: 400 0.72rem/1 var(--grn-16-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-16-mut);
}

.grn-16__h1 {
  margin: 0;
  font: 400 clamp(2.4rem, 7vw, 4.4rem)/0.98 var(--grn-16-font-display);
  letter-spacing: -0.02em;
  text-shadow: 0 calc(var(--grn-16-press) * -1) 0 var(--grn-16-up), 0 var(--grn-16-press) 0 var(--grn-16-down), 0 0 1px color-mix(in oklab, var(--grn-16-ink) 18%, transparent);
}

.grn-16__lede {
  margin: 0;
  max-inline-size: 38rem;
  color: var(--grn-16-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.06rem);
  text-wrap: pretty;
}

.grn-16__invite {
  position: relative;
  padding: clamp(0.5rem, 2vw, 1rem);
}

.grn-16__invite-inner {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 0.7rem;
  padding: clamp(2.2rem, 6vw, 4rem) clamp(1.4rem, 5vw, 3.5rem);
  background: var(--grn-16-stock-2);
  box-shadow: inset 0 1px 0 var(--grn-16-down), 0 22px 50px -30px rgba(40, 30, 16, 0.45);
  filter: url(#grn-16-deckle);
  text-align: center;
}

.grn-16__ornament {
  margin: 0;
  font-size: 1.1rem;
  color: var(--grn-16-acc);
}

.grn-16__invite-pre {
  margin: 0;
  font: 400 clamp(1.6rem, 5vw, 2.8rem)/1.1 var(--grn-16-font-display);
  letter-spacing: 0.01em;
  text-shadow: 0 calc(var(--grn-16-press) * -1) 0 var(--grn-16-up), 0 var(--grn-16-press) 0 var(--grn-16-down);
}

.grn-16__invite-h {
  margin: 0;
  max-inline-size: 26rem;
  font: 400 clamp(0.95rem, 2.2vw, 1.15rem)/1.5 system-ui, sans-serif;
  letter-spacing: 0.06em;
  text-transform: lowercase;
  color: var(--grn-16-mut);
}

.grn-16__invite-when {
  margin: 0.3rem 0 0;
  font: 400 clamp(1.05rem, 2.6vw, 1.35rem)/1.5 var(--grn-16-font-display);
  text-shadow: 0 calc(var(--grn-16-press) * -1) 0 var(--grn-16-up), 0 var(--grn-16-press) 0 var(--grn-16-down);
}

.grn-16__hair {
  inline-size: 3rem;
  block-size: 1px;
  background: var(--grn-16-acc);
}

.grn-16__invite-where {
  margin: 0;
  font: 400 0.78rem/1.6 var(--grn-16-font-mono);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--grn-16-mut);
}

.grn-16__row {
  display: grid;
  gap: clamp(1.2rem, 3vw, 2rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  align-items: start;
}

.grn-16__bcard {
  display: grid;
  align-content: center;
  gap: 0.4rem;
  aspect-ratio: 85 / 55;
  padding: clamp(1.1rem, 3vw, 1.6rem);
  background: var(--grn-16-stock-2);
  border-radius: 2px;
  box-shadow: inset 0 1px 0 var(--grn-16-down), 0 12px 30px -20px rgba(40, 30, 16, 0.4);
}

.grn-16__bcard-name {
  margin: 0;
  font: 400 clamp(1.3rem, 3.4vw, 1.8rem)/1.1 var(--grn-16-font-display);
  text-shadow: 0 calc(var(--grn-16-press) * -1) 0 var(--grn-16-up), 0 var(--grn-16-press) 0 var(--grn-16-down);
}

.grn-16__bcard-role {
  margin: 0;
  font: 400 0.72rem/1.4 var(--grn-16-font-mono);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--grn-16-acc);
}

.grn-16__bcard-meta {
  display: grid;
  gap: 0.1rem;
  margin: 0.5rem 0 0;
  padding-block-start: 0.6rem;
  border-block-start: 1px solid var(--grn-16-line);
}

.grn-16__bcard-meta > div {
  display: flex;
  gap: 0.5rem;
}

.grn-16__bcard-meta dt {
  margin: 0;
  min-inline-size: 3.4rem;
  font: 400 0.7rem/1.6 var(--grn-16-font-mono);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--grn-16-mut);
}

.grn-16__bcard-meta dd {
  margin: 0;
  font-size: 0.85rem;
}

.grn-16__spec {
  display: grid;
  gap: 0.7rem;
  padding: clamp(1.1rem, 3vw, 1.7rem);
  border: 1px solid var(--grn-16-line);
  border-radius: 2px;
  background: color-mix(in oklab, var(--grn-16-stock-2) 60%, transparent);
}

.grn-16__h2 {
  margin: 0;
  font: 400 clamp(1.2rem, 3vw, 1.6rem)/1.15 var(--grn-16-font-display);
  text-shadow: 0 calc(var(--grn-16-press) * -1) 0 var(--grn-16-up), 0 var(--grn-16-press) 0 var(--grn-16-down);
}

.grn-16__spec-list {
  display: grid;
  gap: 0;
  margin: 0;
}

.grn-16__spec-list > div {
  display: grid;
  grid-template-columns: minmax(6rem, 8rem) minmax(0, 1fr);
  gap: 0.6rem;
  padding-block: 0.5rem;
  border-block-start: 1px solid var(--grn-16-line);
}

.grn-16__spec-list dt {
  margin: 0;
  font: 400 0.7rem/1.7 var(--grn-16-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--grn-16-mut);
}

.grn-16__spec-list dd {
  margin: 0;
  font-size: 0.88rem;
}

.grn-16__spec-note {
  margin: 0;
  color: var(--grn-16-mut);
  font-size: 0.83rem;
  text-wrap: pretty;
}

.grn-16__invite-inner,
.grn-16__bcard {
  transition: transform 380ms cubic-bezier(0.22, 1, 0.36, 1), box-shadow 380ms ease;
}

@media (hover: hover) and (pointer: fine) {
  .grn-16__bcard:hover {
    transform: translateY(-3px) rotate(-0.4deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-16__invite-inner,
    .grn-16__bcard {
    transition-duration: 1ms;
    transform: none;
  }
}
```
