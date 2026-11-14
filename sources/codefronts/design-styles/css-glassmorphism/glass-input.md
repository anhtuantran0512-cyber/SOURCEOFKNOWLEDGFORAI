---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/glass-input/"
title: "Glassmorphism Text Input Field"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "Form fields are where glassmorphism usually breaks: a translucent input with a low-contrast border is unusable."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Text Input Field
Source: https://codefronts.com/design-styles/css-glassmorphism/glass-input/

Form fields are where glassmorphism usually breaks: a translucent input with a low-contrast border is unusable. This demo does it properly — a frosted surface with an inner shadow for depth, a 2px :focus-visible ring that survives any backdrop, a real <label>, helper text, and both empty and filled states side by side.
## HTML
```html
<div class="gm-17">
  <input class="gm-17__sr" type="checkbox" id="gm-17-theme">
  <label class="gm-17__theme" for="gm-17-theme" title="Switch theme">
    <svg class="gm-17__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-17__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-17__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-17__stage">
    <section class="gm-17__card" aria-labelledby="gm-17-h">
      <header class="gm-17__head">
        <p class="gm-17__eyebrow">Form controls on glass</p>
        <h2 class="gm-17__h" id="gm-17-h">Deploy hook</h2>
        <p class="gm-17__sub">Both states, same recipe: recessed frosted surface, 2px focus ring, real labels.</p>
      </header>

      <div class="gm-17__grid">
        <div class="gm-17__row">
          <label class="gm-17__label" for="gm-17-empty">Hook name</label>
          <input class="gm-17__field" id="gm-17-empty" type="text" placeholder="production-edge" aria-describedby="gm-17-help1" autocomplete="off" spellcheck="false">
          <p class="gm-17__help" id="gm-17-help1">Empty state — placeholder sits at 60% ink so it stays legible over the mesh.</p>
        </div>

        <div class="gm-17__row">
          <label class="gm-17__label" for="gm-17-filled">Endpoint</label>
          <input class="gm-17__field gm-17__field--filled" id="gm-17-filled" type="url" value="https://api.atlas.dev/hooks/4f2c" aria-describedby="gm-17-help2" autocomplete="off" spellcheck="false">
          <p class="gm-17__help" id="gm-17-help2">Filled state — the rim brightens and the film lifts to 16% once there is content.</p>
        </div>

        <div class="gm-17__row">
          <label class="gm-17__label" for="gm-17-req">Signing secret <span class="gm-17__req">required</span></label>
          <input class="gm-17__field" id="gm-17-req" type="text" placeholder="whsec_…" required aria-describedby="gm-17-help3" autocomplete="off" spellcheck="false">
          <p class="gm-17__help" id="gm-17-help3">Type and clear this field to see <code>:user-invalid</code> — validation waits for interaction.</p>
        </div>

        <div class="gm-17__row">
          <label class="gm-17__label" for="gm-17-note">Notes</label>
          <textarea class="gm-17__field gm-17__field--area" id="gm-17-note" rows="3" placeholder="Who owns this hook, and what should happen when it fails?" aria-describedby="gm-17-help4"></textarea>
          <p class="gm-17__help" id="gm-17-help4">Grows with content where <code>field-sizing</code> is supported.</p>
        </div>
      </div>

      <div class="gm-17__actions">
        <button class="gm-17__btn gm-17__btn--primary" type="button">Save hook</button>
        <button class="gm-17__btn" type="button">Send test event</button>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-17 {
  --a1: rgba(125,211,252,.5);
  --a2: rgba(196,181,253,.55);
  --a3: rgba(110,231,183,.5);
  --a4: rgba(249,168,212,.5);
  --base: #f0f3fb;
  --base2: #e2e8fc;
  --ink: #0f1120;
  --muted: rgba(15,17,32,.68);
  --tint: #ffffff;
  --accent: #0284c7;
  --danger: #be123c;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,17,32,.16);
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
  background: radial-gradient(52% 44% at 12% 16%, var(--a1) 0%, transparent 60%), radial-gradient(52% 44% at 88% 14%, var(--a2) 0%, transparent 60%), radial-gradient(46% 40% at 80% 88%, var(--a3) 0%, transparent 58%), radial-gradient(44% 38% at 16% 90%, var(--a4) 0%, transparent 58%), linear-gradient(160deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-17 *,
.gm-17 *::before,
.gm-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-17 {
    --a1: oklch(0.78 0.16 220 / .56);
    --a2: oklch(0.7 0.19 292 / .56);
    --a3: oklch(0.8 0.15 165 / .46);
    --a4: oklch(0.74 0.19 5 / .46);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
    --accent: oklch(0.85 0.11 220);
    --danger: oklch(0.78 0.14 15);
  }
}

.gm-17__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-17__theme {
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

.gm-17__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-17__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-17__theme:hover {
  scale: 1.06;
}

.gm-17__sr:focus-visible + .gm-17__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-17__moon {
  display: none;
}

.gm-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-17__card {
  inline-size: min(38rem,100%);
  display: grid;
  gap: 1.35rem;
  padding: clamp(1.4rem,3vw,2.1rem);
  border-radius: 1.75rem;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.2);
  -webkit-backdrop-filter: blur(26px) saturate(175%);
  backdrop-filter: blur(26px) saturate(175%);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 34px 74px -32px rgba(0,0,0,.7);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-17__card {
    background: color-mix(in oklab, var(--tint) 14%, transparent);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-17__card {
    background: rgba(16,16,42,.92);
  }
}

.gm-17__head {
  display: grid;
  gap: .35rem;
}

.gm-17__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-17__h {
  margin: 0;
  font-size: clamp(1.5rem,3.2vw,2rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.1;
}

.gm-17__sub {
  margin: 0;
  font-size: .94rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-17__grid {
  display: grid;
  gap: 1.1rem;
}

.gm-17__row {
  display: grid;
  gap: .4rem;
}

.gm-17__label {
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .88rem;
  font-weight: 500;
  letter-spacing: -.005em;
}

.gm-17__req {
  padding: .12rem .38rem;
  border-radius: .35rem;
  font-family: var(--mono);
  font-size: .6rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  background: rgba(255,255,255,.12);
  border: 1px solid var(--rim2);
}

.gm-17__field {
  inline-size: 100%;
  min-block-size: 2.75rem;
  padding: .75rem .9rem;
  border-radius: .85rem;
  font: inherit;
  font-size: .95rem;
  color: var(--ink);
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  box-shadow: inset 0 2px 6px rgba(0,0,0,.28), inset 0 -1px 0 rgba(255,255,255,.14);
  transition: background .18s ease, border-color .18s ease;
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-17__field {
    background: color-mix(in oklab, var(--tint) 12%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-17__field {
    -webkit-backdrop-filter: blur(18px) saturate(165%);
    backdrop-filter: blur(18px) saturate(165%);
  }
}

.gm-17__field::placeholder {
  color: var(--ink);
  opacity: .6;
}

.gm-17__field:hover {
  border-color: rgba(255,255,255,.34);
}

.gm-17__field:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  background: rgba(255,255,255,.18);
  border-color: rgba(255,255,255,.4);
}

.gm-17__field--filled {
  background: rgba(255,255,255,.16);
  border-color: rgba(255,255,255,.34);
  font-family: var(--mono);
  font-size: .88rem;
}

.gm-17__field--area {
  min-block-size: 5.5rem;
  resize: vertical;
  line-height: 1.55;
}

@supports (field-sizing: content) {
  .gm-17__field--area {
    field-sizing: content;
    max-block-size: 12rem;
  }
}

.gm-17__field:user-invalid {
  border-color: var(--danger);
  box-shadow: inset 0 2px 6px rgba(0,0,0,.28), 0 0 0 1px var(--danger);
}

.gm-17__field:user-invalid + .gm-17__help {
  color: var(--danger);
}

.gm-17__help {
  margin: 0;
  font-size: .8rem;
  line-height: 1.45;
  color: var(--muted);
}

.gm-17__help code {
  font-family: var(--mono);
  font-size: .76rem;
  padding: .08rem .3rem;
  border-radius: .3rem;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--rim2);
}

.gm-17__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  padding-block-start: .2rem;
}

.gm-17__btn {
  min-block-size: 2.75rem;
  padding: .75rem 1.15rem;
  border-radius: .85rem;
  cursor: pointer;
  font: inherit;
  font-size: .94rem;
  font-weight: 500;
  color: var(--ink);
  background: rgba(255,255,255,.13);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  box-shadow: inset 0 1px 0 var(--rim2);
  transition: translate .18s ease, background .18s ease;
}

.gm-17__btn--primary {
  color: #06202c;
  background: var(--accent);
  border-color: transparent;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 14px 30px -16px rgba(0,0,0,.7);
}

.gm-17__btn:hover {
  translate: 0 -2px;
}

.gm-17__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-17[data-theme="light"],
.gm-17:has(#gm-17-theme:checked) {
  --a1: rgba(56,189,248,.55);
  --a2: rgba(167,139,250,.55);
  --a3: rgba(52,211,153,.45);
  --a4: rgba(244,114,182,.45);
  --base: #05070f;
  --base2: #111634;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.68);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.22);
  --accent: #7dd3fc;
  --danger: #fda4af;
}

.gm-17:has(#gm-17-theme:checked) .gm-17__sun {
  display: none;
}

.gm-17:has(#gm-17-theme:checked) .gm-17__moon {
  display: block;
}

.gm-17[data-theme="light"] .gm-17__field,
.gm-17:has(#gm-17-theme:checked) .gm-17__field {
  box-shadow: inset 0 2px 5px rgba(16,20,45,.12), inset 0 -1px 0 rgba(255,255,255,.7);
}

.gm-17[data-theme="light"] .gm-17__btn--primary,
.gm-17:has(#gm-17-theme:checked) .gm-17__btn--primary {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .gm-17 *,
    .gm-17 *::before,
    .gm-17 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-17__card,
    .gm-17__field,
    .gm-17__btn,
    .gm-17__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
