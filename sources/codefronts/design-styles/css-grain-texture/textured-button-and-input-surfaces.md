---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/textured-button-and-input-surfaces/"
title: "Textured Button and Input Surfaces"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "A complete form kit where every interactive surface is a material: buttons, inputs, a select, checkboxes, a range slider and a segmented control, all…"
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Textured Button and Input Surfaces
Source: https://codefronts.com/design-styles/css-grain-texture/textured-button-and-input-surfaces/

A complete form kit where every interactive surface is a material: buttons, inputs, a select, checkboxes, a range slider and a segmented control, all carrying the same grain token at weights tuned per state. Every control is at least 44px, every focus ring is visible, and pressing a button genuinely feels like pressing something.
## HTML
```html
<section class="grn-12" aria-labelledby="grn-12-title">
  <div class="grn-12__theme">
    <input class="grn-12__theme-input" type="checkbox" id="grn-12-theme">
    <label class="grn-12__theme-label" for="grn-12-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-12__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-12__shell">
    <header class="grn-12__head">
      <p class="grn-12__kicker">Control surfaces · 12</p>
      <h1 class="grn-12__h1" id="grn-12-title">Every control is a material</h1>
      <p class="grn-12__lede">Buttons are raised, inputs are recessed, and both carry the same grain. Press a button and three things change at once — grain weight, highlight direction, shadow depth.</p>
    </header>

    <div class="grn-12__cols">
      <section class="grn-12__card" aria-labelledby="grn-12-h-btn">
        <h2 class="grn-12__h2" id="grn-12-h-btn">Buttons</h2>
        <div class="grn-12__btn-row">
          <button class="grn-12__btn" type="button">Save changes</button>
          <button class="grn-12__btn grn-12__btn--sec" type="button">Preview</button>
          <button class="grn-12__btn grn-12__btn--ghost" type="button">Cancel</button>
          <button class="grn-12__btn" type="button" disabled>Disabled</button>
        </div>
        <div class="grn-12__seg" role="group" aria-label="Density">
          <input class="grn-12__seg-in" type="radio" name="grn-12-density" id="grn-12-d1" checked>
          <label class="grn-12__seg-lb" for="grn-12-d1">Compact</label>
          <input class="grn-12__seg-in" type="radio" name="grn-12-density" id="grn-12-d2">
          <label class="grn-12__seg-lb" for="grn-12-d2">Regular</label>
          <input class="grn-12__seg-in" type="radio" name="grn-12-density" id="grn-12-d3">
          <label class="grn-12__seg-lb" for="grn-12-d3">Roomy</label>
        </div>
        <p class="grn-12__hint">Idle 0.05 · hover 0.06 · active 0.08 with the highlight inverted.</p>
      </section>

      <section class="grn-12__card" aria-labelledby="grn-12-h-fields">
        <h2 class="grn-12__h2" id="grn-12-h-fields">Fields</h2>
        <div class="grn-12__field">
          <label class="grn-12__label" for="grn-12-name">Full name</label>
          <input class="grn-12__input" type="text" id="grn-12-name" name="grn-12-name" placeholder="Ada Lovelace" autocomplete="name">
        </div>
        <div class="grn-12__field">
          <label class="grn-12__label" for="grn-12-mail">Work email</label>
          <input class="grn-12__input" type="email" id="grn-12-mail" name="grn-12-mail" placeholder="[email protected]" autocomplete="email" required aria-describedby="grn-12-mail-hint">
          <p class="grn-12__err" id="grn-12-mail-hint">We only email about deploys. Real address required.</p>
        </div>
        <div class="grn-12__field">
          <label class="grn-12__label" for="grn-12-region">Region</label>
          <select class="grn-12__input grn-12__select" id="grn-12-region" name="grn-12-region">
            <option>eu-west-2 · London</option>
            <option>us-east-1 · Virginia</option>
            <option>ap-southeast-2 · Sydney</option>
          </select>
        </div>
      </section>

      <section class="grn-12__card" aria-labelledby="grn-12-h-misc">
        <h2 class="grn-12__h2" id="grn-12-h-misc">Toggles and ranges</h2>
        <ul class="grn-12__checks">
          <li><input class="grn-12__check" type="checkbox" id="grn-12-c1" checked><label for="grn-12-c1">Textured surfaces</label></li>
          <li><input class="grn-12__check" type="checkbox" id="grn-12-c2"><label for="grn-12-c2">Reduce transparency</label></li>
          <li><input class="grn-12__check" type="radio" name="grn-12-r" id="grn-12-r1" checked><label for="grn-12-r1">Match system theme</label></li>
          <li><input class="grn-12__check" type="radio" name="grn-12-r" id="grn-12-r2"><label for="grn-12-r2">Always dark</label></li>
        </ul>
        <div class="grn-12__field">
          <label class="grn-12__label" for="grn-12-grain">Grain weight</label>
          <input class="grn-12__range" type="range" id="grn-12-grain" name="grn-12-grain" min="0" max="20" value="6" step="1">
          <p class="grn-12__hint">Native thumb, textured track, <code>accent-color</code> for the fill.</p>
        </div>
      </section>
    </div>
  </main>
</section>
```
## CSS
```css
.grn-12 {
  --grn-12-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='150'%3E%3Cfilter id='grn12n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='150' height='150' filter='url(%23grn12n)'/%3E%3C/svg%3E");
  --grn-12-bg: #eef0f7;
  --grn-12-surf: #ffffff;
  --grn-12-sunk: #e7eaf4;
  --grn-12-line: #d3d8e8;
  --grn-12-ink: #14162a;
  --grn-12-mut: #5c6280;
  --grn-12-acc: #4f46e5;
  --grn-12-acc: oklch(52% 0.22 275);
  --grn-12-on-acc: #f2f1fe;
  --grn-12-err: #b42318;
  --grn-12-err: oklch(50% 0.18 27);
  --grn-12-g-idle: 0.05;
  --grn-12-g-hover: 0.06;
  --grn-12-g-active: 0.08;
  --grn-12-g-sunk: 0.035;
  --grn-12-blend: multiply;
  --grn-12-hl: rgba(255, 255, 255, 0.85);
  --grn-12-radius: 12px;
  --grn-12-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-12-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-12-bg);
  color: var(--grn-12-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
  accent-color: var(--grn-12-acc);
}

.grn-12 *,
.grn-12 *::before,
.grn-12 *::after {
  box-sizing: border-box;
}

.grn-12 :focus-visible {
  outline: 2px solid var(--grn-12-acc);
  outline-offset: 2px;
}

.grn-12 code {
  font-family: var(--grn-12-font-mono);
  font-size: 0.9em;
}

.grn-12__sr {
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

.grn-12:has(.grn-12__theme-input:checked) {
  --grn-12-bg: #0c0d16;
  --grn-12-surf: #15172a;
  --grn-12-sunk: #10121f;
  --grn-12-line: #262a45;
  --grn-12-ink: #ecebfb;
  --grn-12-mut: #9a9ac4;
  --grn-12-acc: #a5b4fc;
  --grn-12-acc: oklch(80% 0.11 278);
  --grn-12-on-acc: #10122a;
  --grn-12-err: #fca5a5;
  --grn-12-err: oklch(78% 0.13 22);
  --grn-12-blend: soft-light;
  --grn-12-hl: rgba(255, 255, 255, 0.12);
  --grn-12-g-idle: 0.07;
  --grn-12-g-hover: 0.085;
  --grn-12-g-active: 0.11;
  --grn-12-g-sunk: 0.05;
}

@media (prefers-color-scheme: dark) {
  .grn-12 {
    --grn-12-bg: #0c0d16;
    --grn-12-surf: #15172a;
    --grn-12-sunk: #10121f;
    --grn-12-line: #262a45;
    --grn-12-ink: #ecebfb;
    --grn-12-mut: #9a9ac4;
    --grn-12-acc: #a5b4fc;
    --grn-12-acc: oklch(80% 0.11 278);
    --grn-12-on-acc: #10122a;
    --grn-12-err: #fca5a5;
    --grn-12-err: oklch(78% 0.13 22);
    --grn-12-blend: soft-light;
    --grn-12-hl: rgba(255, 255, 255, 0.12);
    --grn-12-g-idle: 0.07;
    --grn-12-g-hover: 0.085;
    --grn-12-g-active: 0.11;
    --grn-12-g-sunk: 0.05;
  }

  .grn-12:has(.grn-12__theme-input:checked) {
    --grn-12-bg: #eef0f7;
    --grn-12-surf: #ffffff;
    --grn-12-sunk: #e7eaf4;
    --grn-12-line: #d3d8e8;
    --grn-12-ink: #14162a;
    --grn-12-mut: #5c6280;
    --grn-12-acc: #4f46e5;
    --grn-12-acc: oklch(52% 0.22 275);
    --grn-12-on-acc: #f2f1fe;
    --grn-12-err: #b42318;
    --grn-12-err: oklch(50% 0.18 27);
    --grn-12-blend: multiply;
    --grn-12-hl: rgba(255, 255, 255, 0.85);
    --grn-12-g-idle: 0.05;
    --grn-12-g-hover: 0.06;
    --grn-12-g-active: 0.08;
    --grn-12-g-sunk: 0.035;
  }
}

@media (prefers-color-scheme: light) {
  .grn-12:has(.grn-12__theme-input:checked) {
    --grn-12-bg: #0c0d16;
    --grn-12-surf: #15172a;
    --grn-12-sunk: #10121f;
    --grn-12-line: #262a45;
    --grn-12-ink: #ecebfb;
    --grn-12-mut: #9a9ac4;
    --grn-12-acc: #a5b4fc;
    --grn-12-acc: oklch(80% 0.11 278);
    --grn-12-on-acc: #10122a;
    --grn-12-err: #fca5a5;
    --grn-12-err: oklch(78% 0.13 22);
    --grn-12-blend: soft-light;
    --grn-12-hl: rgba(255, 255, 255, 0.12);
    --grn-12-g-idle: 0.07;
    --grn-12-g-hover: 0.085;
    --grn-12-g-active: 0.11;
    --grn-12-g-sunk: 0.05;
  }
}

.grn-12__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-12__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-12__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-12-line);
  border-radius: 999px;
  background: var(--grn-12-surf);
  color: var(--grn-12-ink);
  cursor: pointer;
  box-shadow: inset 0 1px 0 var(--grn-12-hl);
}

.grn-12__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-12__shell {
  inline-size: min(76rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3rem);
}

.grn-12__head {
  max-inline-size: 44rem;
  display: grid;
  gap: 0.6rem;
}

.grn-12__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-12-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-12-acc);
}

.grn-12__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.4vw, 3.3rem)/1.03 var(--grn-12-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-12__lede {
  margin: 0;
  max-inline-size: 38rem;
  color: var(--grn-12-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.08rem);
  text-wrap: pretty;
}

.grn-12__cols {
  display: grid;
  gap: clamp(1rem, 2.4vw, 1.5rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  align-items: start;
}

.grn-12__card {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  gap: 1rem;
  align-content: start;
  padding: clamp(1.2rem, 3vw, 1.7rem);
  border: 1px solid var(--grn-12-line);
  border-radius: 18px;
  background: var(--grn-12-surf);
  box-shadow: inset 0 1px 0 var(--grn-12-hl), 0 12px 30px -20px rgba(20, 22, 42, 0.3);
  min-inline-size: 0;
}

.grn-12__card::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image: var(--grn-12-noise);
  opacity: 0.04;
  mix-blend-mode: var(--grn-12-blend);
}

.grn-12__h2 {
  margin: 0;
  padding-block-end: 0.6rem;
  border-block-end: 1px solid var(--grn-12-line);
  font: 600 1.05rem/1.2 var(--grn-12-font-display);
  letter-spacing: -0.02em;
}

.grn-12__btn-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.grn-12__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 44px;
  padding-inline: 1.2rem;
  border: 0;
  border-radius: var(--grn-12-radius);
  background: var(--grn-12-acc);
  color: var(--grn-12-on-acc);
  font: 600 0.88rem/1 var(--grn-12-font-display);
  cursor: pointer;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.24), 0 2px 5px rgba(20, 22, 42, 0.22);
}

.grn-12__btn::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-12-noise);
  opacity: var(--grn-12-g-idle);
  mix-blend-mode: overlay;
}

.grn-12__btn:hover::after {
  opacity: var(--grn-12-g-hover);
}

.grn-12__btn:active::after {
  opacity: var(--grn-12-g-active);
}

.grn-12__btn:active {
  box-shadow: inset 0 -1px 0 rgba(255, 255, 255, 0.2), inset 0 2px 6px rgba(0, 0, 0, 0.3);
}

.grn-12__btn--sec {
  background: var(--grn-12-sunk);
  color: var(--grn-12-ink);
  box-shadow: inset 0 1px 0 var(--grn-12-hl), 0 1px 3px rgba(20, 22, 42, 0.14);
}

.grn-12__btn--ghost {
  background: transparent;
  color: var(--grn-12-mut);
  border: 1px solid var(--grn-12-line);
  box-shadow: none;
}

.grn-12__btn--ghost::after {
  opacity: 0;
}

.grn-12__btn[disabled] {
  opacity: 0.45;
  cursor: not-allowed;
  box-shadow: none;
}

.grn-12__seg {
  display: flex;
  flex-wrap: wrap;
  padding: 4px;
  border: 1px solid var(--grn-12-line);
  border-radius: calc(var(--grn-12-radius) + 4px);
  background: var(--grn-12-sunk);
  box-shadow: inset 0 2px 5px rgba(20, 22, 42, 0.12);
}

.grn-12__seg-in {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.grn-12__seg-lb {
  flex: 1 1 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 40px;
  padding-inline: 0.8rem;
  border-radius: var(--grn-12-radius);
  color: var(--grn-12-mut);
  font: 600 0.83rem/1 var(--grn-12-font-display);
  cursor: pointer;
}

.grn-12__seg-in:checked + .grn-12__seg-lb {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  background: var(--grn-12-surf);
  color: var(--grn-12-ink);
  box-shadow: inset 0 1px 0 var(--grn-12-hl), 0 1px 3px rgba(20, 22, 42, 0.18);
}

.grn-12__seg-in:checked + .grn-12__seg-lb::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-12-noise);
  opacity: var(--grn-12-g-idle);
  mix-blend-mode: var(--grn-12-blend);
}

.grn-12__seg-in:focus-visible + .grn-12__seg-lb {
  outline: 2px solid var(--grn-12-acc);
  outline-offset: 2px;
}

.grn-12__field {
  display: grid;
  gap: 0.35rem;
}

.grn-12__label {
  font: 500 0.82rem/1.3 var(--grn-12-font-display);
}

.grn-12__input {
  position: relative;
  min-block-size: 46px;
  padding-inline: 0.85rem;
  border: 1px solid var(--grn-12-line);
  border-radius: var(--grn-12-radius);
  background-image: var(--grn-12-noise), linear-gradient(var(--grn-12-sunk), var(--grn-12-sunk));
  background-blend-mode: var(--grn-12-blend), normal;
  color: var(--grn-12-ink);
  font: 400 0.95rem/1 system-ui, sans-serif;
  box-shadow: inset 0 2px 5px rgba(20, 22, 42, 0.13), inset 0 -1px 0 var(--grn-12-hl);
}

.grn-12__input::placeholder {
  color: color-mix(in oklab, var(--grn-12-mut) 70%, transparent);
}

.grn-12__input:hover {
  border-color: color-mix(in oklab, var(--grn-12-acc) 45%, var(--grn-12-line));
}

.grn-12__select {
  appearance: none;
  -webkit-appearance: none;
  padding-inline-end: 2.2rem;
  background-image: var(--grn-12-noise), linear-gradient(var(--grn-12-sunk), var(--grn-12-sunk));
  cursor: pointer;
}

.grn-12__input:user-invalid {
  border-color: var(--grn-12-err);
}

.grn-12__err {
  margin: 0;
  font-size: 0.8rem;
  color: var(--grn-12-mut);
}

.grn-12__input:user-invalid ~ .grn-12__err {
  color: var(--grn-12-err);
}

.grn-12__checks {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.1rem;
}

.grn-12__checks li {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-block-size: 44px;
}

.grn-12__check {
  inline-size: 20px;
  block-size: 20px;
  margin: 0;
  cursor: pointer;
}

.grn-12__checks label {
  font-size: 0.92rem;
  cursor: pointer;
}

.grn-12__range {
  inline-size: 100%;
  min-block-size: 44px;
  margin: 0;
  background: transparent;
  cursor: pointer;
}

.grn-12__hint {
  margin: 0;
  color: var(--grn-12-mut);
  font-size: 0.8rem;
  text-wrap: pretty;
}

.grn-12__btn,
.grn-12__btn::after,
.grn-12__input,
.grn-12__seg-lb {
  transition: opacity 160ms ease, box-shadow 180ms ease, border-color 180ms ease, background-color 180ms ease;
}

@media (prefers-reduced-motion: reduce) {
  .grn-12__btn,
    .grn-12__btn::after,
    .grn-12__input,
    .grn-12__seg-lb {
    transition-duration: 1ms;
  }
}
```
