---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/obsidian-vault/"
title: "Nested 3D Contexts in a Pointer Steered Scene"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Four levels of 3D nested inside each other: a perspective root, a scene the pointer steers, three cards floating on their own keyframes, and a two-sided face…"
has_js: "true"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nested 3D Contexts in a Pointer Steered Scene
Source: https://codefronts.com/design-styles/css-3d/obsidian-vault/

Four levels of 3D nested inside each other: a perspective root, a scene the pointer steers, three cards floating on their own keyframes, and a two-sided face that flips on hover &mdash; each level's transform composing with the ones above it. A gem built from layered elements sits inside the innermost context, and a generated particle field sits deliberately outside all of them.
## HTML
```html
<section class="d3-19" aria-label="Obsidian Vault luxury cards demo">

  <div class="d3-19__theme">
    <input class="d3-19__theme-input" type="checkbox" id="d3-19-theme">
    <label class="d3-19__theme-label" for="d3-19-theme" aria-label="Toggle light and dark theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg>
    </label>
  </div>

  <div class="card">
    <div class="d3-19__bg" aria-hidden="true"></div>
    <div class="d3-19__floor" aria-hidden="true"></div>

    <div class="scene" data-d3-19-scene>

      <article class="obs-card">
        <div class="obs-inner">
        <div class="face front">
          <span class="series-label">Collection I</span>
          <div class="gem-stage">
            <div class="gem-body">
              <div class="gem-table"></div>
              <div class="gem-crown-left"></div>
              <div class="gem-crown-right"></div>
            </div>
          </div>
          <div class="gem-name">Amethyst<br />Nocturne</div>
          <div class="gem-divider"></div>
          <div class="gem-price">$ 4,200</div>
          <div class="gem-dots">
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
            <div class="gem-dot"></div>
            <div class="gem-dot"></div>
          </div>
        </div>
        <div class="face back">
          <span class="back-ornament">◈</span>
          <span class="back-brand">Obsidian</span>
          <div class="back-rule"></div>
          <p class="back-description">A rare Zambian amethyst, set in cold-forged 18k white gold. Each stone selected for its violet depth and natural clarity.</p>
          <button class="back-cta" type="button">Acquire</button>
          <span class="back-sub">Limited Edition · No. 12 of 30</span>
        </div>
        </div>
      </article>

      <article class="obs-card">
        <div class="obs-inner">
        <div class="face front">
          <span class="series-label">Collection II</span>
          <div class="gem-stage">
            <div class="gem-body">
              <div class="gem-table"></div>
              <div class="gem-crown-left"></div>
              <div class="gem-crown-right"></div>
            </div>
          </div>
          <div class="gem-name">Sapphire<br />Meridian</div>
          <div class="gem-divider"></div>
          <div class="gem-price">$ 7,800</div>
          <div class="gem-dots">
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
            <div class="gem-dot"></div>
          </div>
        </div>
        <div class="face back">
          <span class="back-ornament">◈</span>
          <span class="back-brand">Obsidian</span>
          <div class="back-rule"></div>
          <p class="back-description">Ceylon blue sapphire, untreated and certified. Suspended in a hand-finished platinum bezel, worn by the extraordinarily few.</p>
          <button class="back-cta" type="button">Acquire</button>
          <span class="back-sub">Limited Edition · No. 7 of 20</span>
        </div>
        </div>
      </article>

      <article class="obs-card">
        <div class="obs-inner">
        <div class="face front">
          <span class="series-label">Collection III</span>
          <div class="gem-stage">
            <div class="gem-body">
              <div class="gem-table"></div>
              <div class="gem-crown-left"></div>
              <div class="gem-crown-right"></div>
            </div>
          </div>
          <div class="gem-name">Ruby<br />Solstice</div>
          <div class="gem-divider"></div>
          <div class="gem-price">$ 12,400</div>
          <div class="gem-dots">
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
            <div class="gem-dot active"></div>
          </div>
        </div>
        <div class="face back">
          <span class="back-ornament">◈</span>
          <span class="back-brand">Obsidian</span>
          <div class="back-rule"></div>
          <p class="back-description">Burmese pigeon-blood ruby of extraordinary rarity. Each stone handpicked, individually documented, and signed by the master craftsman.</p>
          <button class="back-cta" type="button">Acquire</button>
          <span class="back-sub">Singular Edition · No. 1 of 8</span>
        </div>
        </div>
      </article>

    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Cinzel:wght@400;600;700&display=swap');

.d3-19 {
  --d3-19-ground: #060309;
  --d3-19-atm-violet: rgba(90,25,150,0.18);
  --d3-19-atm-amber: rgba(170,80,15,0.13);
  --d3-19-atm-blue: rgba(15,50,90,0.10);
  --d3-19-floor: rgba(212,168,52,0.04);
  --d3-19-particle: #d4a834;
  --d3-19-gold: rgba(212,168,52,0.85);
  --d3-19-gold-hair: rgba(212,168,52,0.22);
  --d3-19-gold-faint: rgba(212,168,52,0.05);
  --d3-19-gold-inner: rgba(212,168,52,0.20);
  --d3-19-gold-line: rgba(212,168,52,0.90);
  --d3-19-gold-wash: rgba(212,168,52,0.08);
  --d3-19-gold-label: rgba(212,168,52,0.72);
  --d3-19-gold-divider: rgba(212,168,52,0.75);
  --d3-19-gold-price: rgba(232,208,135,0.88);
  --d3-19-gold-dot: rgba(212,168,52,0.50);
  --d3-19-gold-dot-on: rgba(212,168,52,0.95);
  --d3-19-gold-dot-glow: rgba(212,168,52,0.80);
  --d3-19-gold-brand: rgba(212,168,52,0.62);
  --d3-19-gold-rule: rgba(212,168,52,0.35);
  --d3-19-gold-frame: rgba(212,168,52,0.09);
  --d3-19-gold-ornament: rgba(212,168,52,0.40);
  --d3-19-cta-line: rgba(212,168,52,0.38);
  --d3-19-cta-bg: rgba(212,168,52,0.04);
  --d3-19-cta-ink: rgba(212,168,52,0.88);
  --d3-19-cta-bg-hover: rgba(212,168,52,0.10);
  --d3-19-cta-line-hover: rgba(212,168,52,0.60);
  --d3-19-surf-1: #140c20;
  --d3-19-surf-2: #0c091a;
  --d3-19-surf-3: #160c22;
  --d3-19-back-1: #100c1e;
  --d3-19-back-2: #0c0818;
  --d3-19-back-3: #140a20;
  --d3-19-shadow-deep: rgba(0,0,0,0.85);
  --d3-19-shadow-mid: rgba(0,0,0,0.60);
  --d3-19-inset-lo: rgba(0,0,0,0.50);
  --d3-19-name-ink: #ede4f8;
  --d3-19-desc-ink: rgba(210,198,228,0.70);
  --d3-19-sub-ink: rgba(180,170,200,0.40);
  --d3-19-facet-a: rgba(255,255,255,0.14);
  --d3-19-facet-b: rgba(255,255,255,0.03);
  --d3-19-facet-c: rgba(255,255,255,0.08);
  --d3-19-facet-table-1: rgba(255,255,255,0.35);
  --d3-19-facet-table-2: rgba(255,255,255,0.08);
  --d3-19-facet-crown: rgba(255,255,255,0.09);
  --d3-19-gem-a-glow: rgba(148,80,230,0.85);
  --d3-19-gem-a-light: #c8a0f8;
  --d3-19-gem-a-mid: #8844e0;
  --d3-19-gem-a-dark: #4820a8;
  --d3-19-gem-b-glow: rgba(30,140,240,0.85);
  --d3-19-gem-b-light: #80d0ff;
  --d3-19-gem-b-mid: #2888d8;
  --d3-19-gem-b-dark: #0c4a98;
  --d3-19-gem-c-glow: rgba(228,55,50,0.85);
  --d3-19-gem-c-light: #ff9888;
  --d3-19-gem-c-mid: #d83030;
  --d3-19-gem-c-dark: #7a1018;
  --d3-19-ui-face: rgba(212,168,52,0.06);
  --d3-19-ui-line: rgba(212,168,52,0.30);
  --d3-19-ui-ink: rgba(232,208,135,0.92);
  width: 100%;
  min-height: max(100vh, 560px);
  display: block;
  position: relative;
  background: var(--d3-19-ground);
  font-family: 'Cormorant Garamond', serif;
  overflow: hidden;
  perspective: 1600px;
  box-sizing: border-box;
}

.d3-19 *,
.d3-19 *::before,
.d3-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.d3-19:has(.d3-19__theme-input:checked) {
  --d3-19-ground: #efe7db;
  --d3-19-atm-violet: rgba(120,60,190,0.14);
  --d3-19-atm-amber: rgba(200,130,40,0.14);
  --d3-19-atm-blue: rgba(60,110,170,0.10);
  --d3-19-floor: rgba(150,110,30,0.10);
  --d3-19-particle: #8a6110;
  --d3-19-gold: rgba(122,84,14,0.92);
  --d3-19-gold-hair: rgba(122,84,14,0.30);
  --d3-19-gold-faint: rgba(122,84,14,0.10);
  --d3-19-gold-inner: rgba(255,255,255,0.85);
  --d3-19-gold-line: rgba(140,98,20,0.75);
  --d3-19-gold-wash: rgba(160,116,30,0.10);
  --d3-19-gold-label: rgba(104,70,10,0.95);
  --d3-19-gold-divider: rgba(140,98,20,0.70);
  --d3-19-gold-price: #6a4708;
  --d3-19-gold-dot: rgba(122,84,14,0.35);
  --d3-19-gold-dot-on: rgba(122,84,14,0.95);
  --d3-19-gold-dot-glow: rgba(196,148,40,0.55);
  --d3-19-gold-brand: rgba(104,70,10,0.95);
  --d3-19-gold-rule: rgba(140,98,20,0.50);
  --d3-19-gold-frame: rgba(140,98,20,0.18);
  --d3-19-gold-ornament: rgba(140,98,20,0.55);
  --d3-19-cta-line: rgba(122,84,14,0.50);
  --d3-19-cta-bg: rgba(160,116,30,0.08);
  --d3-19-cta-ink: #5e3f06;
  --d3-19-cta-bg-hover: rgba(160,116,30,0.16);
  --d3-19-cta-line-hover: rgba(122,84,14,0.85);
  --d3-19-surf-1: #fffdf8;
  --d3-19-surf-2: #f7f1e6;
  --d3-19-surf-3: #fffcf5;
  --d3-19-back-1: #fdf9f1;
  --d3-19-back-2: #f6efe3;
  --d3-19-back-3: #fdfaf3;
  --d3-19-shadow-deep: rgba(70,52,20,0.22);
  --d3-19-shadow-mid: rgba(70,52,20,0.14);
  --d3-19-inset-lo: rgba(120,95,50,0.10);
  --d3-19-name-ink: #1c1224;
  --d3-19-desc-ink: rgba(48,36,58,0.92);
  --d3-19-sub-ink: rgba(70,58,80,0.78);
  --d3-19-gem-a-glow: rgba(112,44,196,0.55);
  --d3-19-gem-a-light: #b487ee;
  --d3-19-gem-a-mid: #6f2ccc;
  --d3-19-gem-a-dark: #3a1287;
  --d3-19-gem-b-glow: rgba(16,96,190,0.55);
  --d3-19-gem-b-light: #63bdf5;
  --d3-19-gem-b-mid: #1268bd;
  --d3-19-gem-b-dark: #08386f;
  --d3-19-gem-c-glow: rgba(186,28,34,0.55);
  --d3-19-gem-c-light: #f57f6f;
  --d3-19-gem-c-mid: #bb2026;
  --d3-19-gem-c-dark: #630c12;
  --d3-19-ui-face: rgba(255,255,255,0.70);
  --d3-19-ui-line: rgba(122,84,14,0.35);
  --d3-19-ui-ink: #5e3f06;
}

@media (prefers-color-scheme: light) {
  .d3-19:has(.d3-19__theme-input:checked) {
    --d3-19-ground: #efe7db;
    --d3-19-atm-violet: rgba(120,60,190,0.14);
    --d3-19-atm-amber: rgba(200,130,40,0.14);
    --d3-19-atm-blue: rgba(60,110,170,0.10);
    --d3-19-floor: rgba(150,110,30,0.10);
    --d3-19-particle: #8a6110;
    --d3-19-gold: rgba(122,84,14,0.92);
    --d3-19-gold-hair: rgba(122,84,14,0.30);
    --d3-19-gold-faint: rgba(122,84,14,0.10);
    --d3-19-gold-inner: rgba(255,255,255,0.85);
    --d3-19-gold-line: rgba(140,98,20,0.75);
    --d3-19-gold-wash: rgba(160,116,30,0.10);
    --d3-19-gold-label: rgba(104,70,10,0.95);
    --d3-19-gold-divider: rgba(140,98,20,0.70);
    --d3-19-gold-price: #6a4708;
    --d3-19-gold-dot: rgba(122,84,14,0.35);
    --d3-19-gold-dot-on: rgba(122,84,14,0.95);
    --d3-19-gold-dot-glow: rgba(196,148,40,0.55);
    --d3-19-gold-brand: rgba(104,70,10,0.95);
    --d3-19-gold-rule: rgba(140,98,20,0.50);
    --d3-19-gold-frame: rgba(140,98,20,0.18);
    --d3-19-gold-ornament: rgba(140,98,20,0.55);
    --d3-19-cta-line: rgba(122,84,14,0.50);
    --d3-19-cta-bg: rgba(160,116,30,0.08);
    --d3-19-cta-ink: #5e3f06;
    --d3-19-cta-bg-hover: rgba(160,116,30,0.16);
    --d3-19-cta-line-hover: rgba(122,84,14,0.85);
    --d3-19-surf-1: #fffdf8;
    --d3-19-surf-2: #f7f1e6;
    --d3-19-surf-3: #fffcf5;
    --d3-19-back-1: #fdf9f1;
    --d3-19-back-2: #f6efe3;
    --d3-19-back-3: #fdfaf3;
    --d3-19-shadow-deep: rgba(70,52,20,0.22);
    --d3-19-shadow-mid: rgba(70,52,20,0.14);
    --d3-19-inset-lo: rgba(120,95,50,0.10);
    --d3-19-name-ink: #1c1224;
    --d3-19-desc-ink: rgba(48,36,58,0.92);
    --d3-19-sub-ink: rgba(70,58,80,0.78);
    --d3-19-gem-a-glow: rgba(112,44,196,0.55);
    --d3-19-gem-a-light: #b487ee;
    --d3-19-gem-a-mid: #6f2ccc;
    --d3-19-gem-a-dark: #3a1287;
    --d3-19-gem-b-glow: rgba(16,96,190,0.55);
    --d3-19-gem-b-light: #63bdf5;
    --d3-19-gem-b-mid: #1268bd;
    --d3-19-gem-b-dark: #08386f;
    --d3-19-gem-c-glow: rgba(186,28,34,0.55);
    --d3-19-gem-c-light: #f57f6f;
    --d3-19-gem-c-mid: #bb2026;
    --d3-19-gem-c-dark: #630c12;
    --d3-19-ui-face: rgba(255,255,255,0.70);
    --d3-19-ui-line: rgba(122,84,14,0.35);
    --d3-19-ui-ink: #5e3f06;
  }
}

@media (prefers-color-scheme: dark) {
  .d3-19:has(.d3-19__theme-input:checked) {
    --d3-19-ground: #efe7db;
    --d3-19-atm-violet: rgba(120,60,190,0.14);
    --d3-19-atm-amber: rgba(200,130,40,0.14);
    --d3-19-atm-blue: rgba(60,110,170,0.10);
    --d3-19-floor: rgba(150,110,30,0.10);
    --d3-19-particle: #8a6110;
    --d3-19-gold: rgba(122,84,14,0.92);
    --d3-19-gold-hair: rgba(122,84,14,0.30);
    --d3-19-gold-faint: rgba(122,84,14,0.10);
    --d3-19-gold-inner: rgba(255,255,255,0.85);
    --d3-19-gold-line: rgba(140,98,20,0.75);
    --d3-19-gold-wash: rgba(160,116,30,0.10);
    --d3-19-gold-label: rgba(104,70,10,0.95);
    --d3-19-gold-divider: rgba(140,98,20,0.70);
    --d3-19-gold-price: #6a4708;
    --d3-19-gold-dot: rgba(122,84,14,0.35);
    --d3-19-gold-dot-on: rgba(122,84,14,0.95);
    --d3-19-gold-dot-glow: rgba(196,148,40,0.55);
    --d3-19-gold-brand: rgba(104,70,10,0.95);
    --d3-19-gold-rule: rgba(140,98,20,0.50);
    --d3-19-gold-frame: rgba(140,98,20,0.18);
    --d3-19-gold-ornament: rgba(140,98,20,0.55);
    --d3-19-cta-line: rgba(122,84,14,0.50);
    --d3-19-cta-bg: rgba(160,116,30,0.08);
    --d3-19-cta-ink: #5e3f06;
    --d3-19-cta-bg-hover: rgba(160,116,30,0.16);
    --d3-19-cta-line-hover: rgba(122,84,14,0.85);
    --d3-19-surf-1: #fffdf8;
    --d3-19-surf-2: #f7f1e6;
    --d3-19-surf-3: #fffcf5;
    --d3-19-back-1: #fdf9f1;
    --d3-19-back-2: #f6efe3;
    --d3-19-back-3: #fdfaf3;
    --d3-19-shadow-deep: rgba(70,52,20,0.22);
    --d3-19-shadow-mid: rgba(70,52,20,0.14);
    --d3-19-inset-lo: rgba(120,95,50,0.10);
    --d3-19-name-ink: #1c1224;
    --d3-19-desc-ink: rgba(48,36,58,0.92);
    --d3-19-sub-ink: rgba(70,58,80,0.78);
    --d3-19-gem-a-glow: rgba(112,44,196,0.55);
    --d3-19-gem-a-light: #b487ee;
    --d3-19-gem-a-mid: #6f2ccc;
    --d3-19-gem-a-dark: #3a1287;
    --d3-19-gem-b-glow: rgba(16,96,190,0.55);
    --d3-19-gem-b-light: #63bdf5;
    --d3-19-gem-b-mid: #1268bd;
    --d3-19-gem-b-dark: #08386f;
    --d3-19-gem-c-glow: rgba(186,28,34,0.55);
    --d3-19-gem-c-light: #f57f6f;
    --d3-19-gem-c-mid: #bb2026;
    --d3-19-gem-c-dark: #630c12;
    --d3-19-ui-face: rgba(255,255,255,0.70);
    --d3-19-ui-line: rgba(122,84,14,0.35);
    --d3-19-ui-ink: #5e3f06;
  }
}

.d3-19 .d3-19__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 30;
}

.d3-19 .d3-19__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 1;
}

.d3-19 .d3-19__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-19-ui-line);
  border-radius: 2px;
  background: var(--d3-19-ui-face);
  color: var(--d3-19-ui-ink);
  pointer-events: none;
}

.d3-19 .d3-19__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-19 .d3-19__theme-input:focus-visible + .d3-19__theme-label {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.d3-19 .card {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.d3-19 .d3-19__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.d3-19 .d3-19__bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 55% 55% at 18% 38%, var(--d3-19-atm-violet) 0%, transparent 65%), radial-gradient(ellipse 45% 45% at 82% 62%, var(--d3-19-atm-amber) 0%, transparent 65%), radial-gradient(ellipse 35% 50% at 50% 85%, var(--d3-19-atm-blue) 0%, transparent 70%);
}

.d3-19 .d3-19__bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
  opacity: 0.028;
  background-size: 300px 300px;
}

.d3-19 .d3-19__floor {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 180px;
  background: linear-gradient(to top, var(--d3-19-floor) 0%, transparent 100%);
  pointer-events: none;
}

.d3-19 .scene {
  display: flex;
  gap: 30px;
  align-items: center;
  transform-style: preserve-3d;
  position: relative;
  z-index: 1;
  will-change: transform;
}

.d3-19 .obs-card {
  width: 196px;
  height: 288px;
  position: relative;
  transform-style: preserve-3d;
  cursor: pointer;
}

.d3-19 .obs-inner {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
  transition: transform 1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.d3-19 .obs-card:nth-child(1) {
  animation: d3-19-float-a 6.4s ease-in-out infinite;
  --d3-19-glow: var(--d3-19-gem-a-glow);
  --d3-19-gem-light: var(--d3-19-gem-a-light);
  --d3-19-gem-mid: var(--d3-19-gem-a-mid);
  --d3-19-gem-dark: var(--d3-19-gem-a-dark);
}

.d3-19 .obs-card:nth-child(2) {
  animation: d3-19-float-b 7.6s ease-in-out infinite -2.1s;
  --d3-19-glow: var(--d3-19-gem-b-glow);
  --d3-19-gem-light: var(--d3-19-gem-b-light);
  --d3-19-gem-mid: var(--d3-19-gem-b-mid);
  --d3-19-gem-dark: var(--d3-19-gem-b-dark);
}

.d3-19 .obs-card:nth-child(3) {
  animation: d3-19-float-c 5.8s ease-in-out infinite -1.4s;
  --d3-19-glow: var(--d3-19-gem-c-glow);
  --d3-19-gem-light: var(--d3-19-gem-c-light);
  --d3-19-gem-mid: var(--d3-19-gem-c-mid);
  --d3-19-gem-dark: var(--d3-19-gem-c-dark);
}

@keyframes d3-19-float-a {
  0%,
    100% {
    transform: translateY(0) translateZ(0);
  }

  50% {
    transform: translateY(-18px) translateZ(10px);
  }
}

@keyframes d3-19-float-b {
  0%,
    100% {
    transform: translateY(-8px) translateZ(0);
  }

  50% {
    transform: translateY(-24px) translateZ(12px);
  }
}

@keyframes d3-19-float-c {
  0%,
    100% {
    transform: translateY(-4px) translateZ(0);
  }

  50% {
    transform: translateY(-20px) translateZ(8px);
  }
}

.d3-19 .obs-card:hover {
  animation-play-state: paused;
}

.d3-19 .obs-card:hover .obs-inner {
  transform: rotateY(180deg) translateZ(30px);
}

.d3-19 .face {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  overflow: hidden;
}

.d3-19 .front {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 26px 20px 22px;
  background: linear-gradient(148deg, var(--d3-19-surf-1) 0%, var(--d3-19-surf-2) 42%, var(--d3-19-surf-3) 100%);
  border: 1px solid var(--d3-19-gold-hair);
  box-shadow: 0 0 0 1px var(--d3-19-gold-faint), 0 50px 100px var(--d3-19-shadow-deep), 0 25px 50px var(--d3-19-shadow-mid), inset 0 1.5px 0 var(--d3-19-gold-inner), inset 0 -1px 0 var(--d3-19-inset-lo);
}

.d3-19 .front::before {
  content: '';
  position: absolute;
  top: 0;
  left: 14%;
  right: 14%;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--d3-19-gold-line), transparent);
}

.d3-19 .front::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 20px;
  background: radial-gradient(ellipse 90% 55% at 50% 18%, var(--d3-19-gold-wash) 0%, transparent 60%);
  pointer-events: none;
}

.d3-19 .series-label {
  font-family: 'Cinzel', serif;
  font-size: 9px;
  letter-spacing: 4.5px;
  color: var(--d3-19-gold-label);
  text-transform: uppercase;
  z-index: 1;
}

.d3-19 .gem-stage {
  width: 88px;
  height: 100px;
  margin: 16px auto 12px;
  position: relative;
  z-index: 1;
  animation: d3-19-gem-breathe 3.5s ease-in-out infinite;
}

@keyframes d3-19-gem-breathe {
  0%,
    100% {
    filter: drop-shadow(0 0 10px var(--d3-19-glow)) drop-shadow(0 0 25px var(--d3-19-glow));
    transform: scale(1);
  }

  50% {
    filter: drop-shadow(0 0 18px var(--d3-19-glow)) drop-shadow(0 0 42px var(--d3-19-glow));
    transform: scale(1.04);
  }
}

.d3-19 .gem-body {
  width: 88px;
  height: 100px;
  background: linear-gradient(162deg, var(--d3-19-gem-light) 0%, var(--d3-19-gem-mid) 38%, var(--d3-19-gem-dark) 100%);
  clip-path: polygon(50% 0%, 88% 32%, 100% 56%, 50% 100%, 0% 56%, 12% 32%);
  position: relative;
}

.d3-19 .gem-body::before {
  content: '';
  position: absolute;
  inset: 0;
  clip-path: polygon(50% 0%, 88% 32%, 100% 56%, 50% 100%, 0% 56%, 12% 32%);
  background: linear-gradient(42deg, transparent 28%, var(--d3-19-facet-a) 46%, var(--d3-19-facet-b) 56%, transparent 68%);
  animation: d3-19-shimmer-a 4.2s ease-in-out infinite;
}

.d3-19 .gem-body::after {
  content: '';
  position: absolute;
  inset: 0;
  clip-path: polygon(50% 0%, 88% 32%, 100% 56%, 50% 100%, 0% 56%, 12% 32%);
  background: linear-gradient(210deg, transparent 30%, var(--d3-19-facet-c) 48%, transparent 62%);
  animation: d3-19-shimmer-b 5.8s ease-in-out infinite;
}

@keyframes d3-19-shimmer-a {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.4;
  }
}

@keyframes d3-19-shimmer-b {
  0%,
    100% {
    opacity: 0.3;
  }

  50% {
    opacity: 1;
  }
}

.d3-19 .gem-table {
  position: absolute;
  top: 14%;
  left: 50%;
  transform: translateX(-50%);
  width: 44px;
  height: 14px;
  clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
  background: linear-gradient(to bottom, var(--d3-19-facet-table-1), var(--d3-19-facet-table-2));
}

.d3-19 .gem-crown-left,
.d3-19 .gem-crown-right {
  position: absolute;
  top: 0;
  width: 0;
  height: 0;
}

.d3-19 .gem-crown-left {
  left: 12%;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 22px solid var(--d3-19-facet-crown);
}

.d3-19 .gem-crown-right {
  right: 12%;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 22px solid var(--d3-19-facet-crown);
}

.d3-19 .gem-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  font-weight: 300;
  color: var(--d3-19-name-ink);
  text-align: center;
  line-height: 1.3;
  letter-spacing: 0.4px;
  z-index: 1;
}

.d3-19 .gem-divider {
  width: 38px;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--d3-19-gold-divider), transparent);
  margin: 12px 0 10px;
  z-index: 1;
}

.d3-19 .gem-price {
  font-family: 'Cinzel', serif;
  font-size: 12px;
  letter-spacing: 2.5px;
  color: var(--d3-19-gold-price);
  z-index: 1;
}

.d3-19 .gem-dots {
  display: flex;
  gap: 5px;
  margin-top: 8px;
  z-index: 1;
}

.d3-19 .gem-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--d3-19-gold-dot);
}

.d3-19 .gem-dot.active {
  background: var(--d3-19-gold-dot-on);
  box-shadow: 0 0 6px var(--d3-19-gold-dot-glow);
}

.d3-19 .back {
  transform: rotateY(180deg);
  background: linear-gradient(152deg, var(--d3-19-back-1) 0%, var(--d3-19-back-2) 52%, var(--d3-19-back-3) 100%);
  border: 1px solid var(--d3-19-gold-hair);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 28px 24px;
  gap: 0;
}

.d3-19 .back::before {
  content: '';
  position: absolute;
  inset: 10px;
  border: 1px solid var(--d3-19-gold-frame);
  border-radius: 12px;
}

.d3-19 .back-ornament {
  font-size: 8px;
  color: var(--d3-19-gold-ornament);
  position: absolute;
  top: 20px;
  left: 24px;
}

.d3-19 .back-brand {
  font-family: 'Cinzel', serif;
  font-size: 9px;
  letter-spacing: 7px;
  color: var(--d3-19-gold-brand);
  margin-bottom: 20px;
}

.d3-19 .back-rule {
  width: 28px;
  height: 1px;
  background: var(--d3-19-gold-rule);
  margin-bottom: 20px;
}

.d3-19 .back-description {
  font-family: 'Cormorant Garamond', serif;
  font-size: 13.5px;
  font-weight: 300;
  font-style: italic;
  color: var(--d3-19-desc-ink);
  text-align: center;
  line-height: 1.82;
  margin-bottom: 22px;
}

.d3-19 .back-cta {
  padding: 9px 26px;
  border: 1px solid var(--d3-19-cta-line);
  background: var(--d3-19-cta-bg);
  color: var(--d3-19-cta-ink);
  font-family: 'Cinzel', serif;
  font-size: 9px;
  letter-spacing: 4px;
  cursor: pointer;
  border-radius: 2px;
  transition: background 0.35s, border-color 0.35s;
  margin-bottom: 16px;
}

.d3-19 .back-cta:hover {
  background: var(--d3-19-cta-bg-hover);
  border-color: var(--d3-19-cta-line-hover);
}

.d3-19 .back-sub {
  font-family: 'Cormorant Garamond', serif;
  font-size: 11px;
  color: var(--d3-19-sub-ink);
  letter-spacing: 1.5px;
  font-style: italic;
}

.d3-19 .d3-19__particle {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
  animation: d3-19-p-rise var(--d3-19-pd) linear infinite var(--d3-19-dl);
}

@keyframes d3-19-p-rise {
  0% {
    transform: translateY(20px) scale(0);
    opacity: 0;
  }

  8% {
    opacity: var(--d3-19-op);
    transform: translateY(0) scale(1);
  }

  85% {
    opacity: calc(var(--d3-19-op) * 0.4);
  }

  100% {
    transform: translateY(-90px) scale(0.4);
    opacity: 0;
  }
}

@media (max-width: 720px) {
  .d3-19 {
    min-height: max(100vh, 640px);
  }

  .d3-19 .scene {
    flex-direction: column;
    gap: 18px;
  }

  .d3-19 .obs-card {
    width: 168px;
    height: 248px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .d3-19 .obs-card,
    .d3-19 .gem-stage,
    .d3-19 .gem-body::before,
    .d3-19 .gem-body::after,
    .d3-19 .d3-19__particle {
    animation: none !important;
  }

  .d3-19 .obs-inner {
    transition: none !important;
  }

  .d3-19 .scene {
    transform: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.d3-19');
  if (!root) return;
  const scene = root.querySelector('[data-d3-19-scene]');
  if (!scene) return;

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!prefersReduced) {
    for (let i = 0; i < 36; i++) {
      const p = document.createElement('div');
      p.className = 'd3-19__particle';
      const sz = Math.random() * 2.2 + 0.4;
      const tint = Math.round(Math.random() * 50 + 10);
      p.style.cssText = [
        'width:' + sz + 'px',
        'height:' + sz + 'px',
        'left:' + (Math.random() * 100) + '%',
        'top:' + (Math.random() * 100) + '%',
        'background: color-mix(in srgb, var(--d3-19-particle) ' + tint + '%, transparent)',
        '--d3-19-pd:' + (Math.random() * 12 + 8) + 's',
        '--d3-19-dl:' + (-Math.random() * 20) + 's',
        '--d3-19-op:' + (Math.random() * 0.55 + 0.1)
      ].join(';');
      root.appendChild(p);
    }
  }

  let tRx = 0, tRy = 0, cRx = 0, cRy = 0, rafId = null;

  root.addEventListener('mousemove', e => {
    const rect = root.getBoundingClientRect();
    tRx = ((e.clientY - rect.top) / rect.height - 0.5) * 18;
    tRy = ((e.clientX - rect.left) / rect.width - 0.5) * 24;
    if (!rafId && !prefersReduced) rafId = requestAnimationFrame(animate);
  });
  root.addEventListener('mouseleave', () => {
    tRx = 0; tRy = 0;
  });

  function animate() {
    cRx += (tRx - cRx) * 0.06;
    cRy += (tRy - cRy) * 0.06;
    scene.style.transform = 'rotateX(' + cRx + 'deg) rotateY(' + cRy + 'deg)';
    if (Math.abs(tRx - cRx) > 0.05 || Math.abs(tRy - cRy) > 0.05) {
      rafId = requestAnimationFrame(animate);
    } else {
      rafId = null;
    }
  }
})();
```
