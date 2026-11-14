---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/dark-mode-glassmorphism-card-tailwind/"
title: "Dark Mode Glassmorphism Card Tailwind"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "The same card audited in both schemes: a side-by-side light/dark pair driven entirely by custom properties (each side maps 1:1 to Tailwind's dark: variants),…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Glassmorphism Card Tailwind
Source: https://codefronts.com/components/css-glassmorphism-cards/dark-mode-glassmorphism-card-tailwind/

The same card audited in both schemes: a side-by-side light/dark pair driven entirely by custom properties (each side maps 1:1 to Tailwind's dark: variants), and a live toggle version where one :has() checkbox re-themes the card with a soft cross-fade — the exact pattern behind class-strategy dark mode.
## HTML
```html
<div class="glz-23-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-23a" aria-label="Same glass card in light and dark schemes">
  <div class="glz-23a__pair">
    <div class="glz-23a__scheme glz-23a__scheme--light">
      <span class="glz-23a__lab">light · bg-white/55</span>
      <article class="glz-23a__card"><span class="glz-23a__chip">Starter</span><h3>Glass holds both ways</h3><p>High-alpha white fill, bright border, soft shadow.</p><button type="button">Continue</button></article>
    </div>
    <div class="glz-23a__scheme glz-23a__scheme--dark">
      <span class="glz-23a__lab">dark · bg-slate-900/50</span>
      <article class="glz-23a__card"><span class="glz-23a__chip">Starter</span><h3>Glass holds both ways</h3><p>Low-alpha fill, faint border, stronger inner highlight.</p><button type="button">Continue</button></article>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="glz-23b" aria-label="Glass card with CSS-only theme toggle">
  <div class="glz-23b__stage">
    <input type="checkbox" id="glz-23b-dm" class="glz-23b__check">
    <label class="glz-23b__toggle" for="glz-23b-dm"><span class="glz-23b__sun" aria-hidden="true">☀</span><i aria-hidden="true"></i><span class="glz-23b__moon" aria-hidden="true">☾</span><b class="glz-23b__sr">Toggle dark mode</b></label>
    <article class="glz-23b__card">
      <h3>Scheme-aware glass</h3>
      <p>Flip the switch — fill, ink, border and backdrop all re-resolve from six custom properties.</p>
      <div class="glz-23b__row"><span>Contrast (body)</span><b>AA 7.1:1</b></div>
      <div class="glz-23b__row"><span>Blur budget</span><b>20px · 1 layer</b></div>
    </article>
  </div>
</section>
</div>
```
## CSS
```css
.glz-23-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.glz-23-group > section {
  width: 100%;
}

.glz-23a,
.glz-23a *,
.glz-23a *::before,
.glz-23a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-23a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101218;
  font-family: 'Manrope',system-ui,sans-serif;
}

.glz-23a__pair {
  display: flex;
  flex-wrap: wrap;
  gap: 0;
  width: min(860px,100%);
  border-radius: 28px;
  overflow: hidden;
  box-shadow: 0 40px 80px -34px rgba(0,0,0,.9);
}

.glz-23a__scheme {
  flex: 1 1 320px;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: 52px 34px;
  position: relative;
}

.glz-23a__scheme--light {
  --fill: rgba(255,255,255,.55);
  --ink: #232838;
  --sub: rgba(35,40,56,.6);
  --line: rgba(255,255,255,.8);
  --btn: #232838;
  --btn-ink: #f4f6fd;
  background: radial-gradient(120% 100% at 20% 0%,oklch(0.9 0.06 230),transparent 60%),radial-gradient(110% 90% at 90% 100%,oklch(0.88 0.07 320),transparent 60%),#eef0f6;
}

.glz-23a__scheme--dark {
  --fill: rgba(18,22,36,.5);
  --ink: #edf1fb;
  --sub: rgba(237,241,251,.6);
  --line: rgba(255,255,255,.18);
  --btn: #edf1fb;
  --btn-ink: #171c2c;
  background: radial-gradient(120% 100% at 20% 0%,oklch(0.4 0.12 265/.7),transparent 60%),radial-gradient(110% 90% at 90% 100%,oklch(0.42 0.14 320/.6),transparent 60%),#0c0f1a;
}

.glz-23a__lab {
  font: 600 10.5px 'JetBrains Mono',monospace;
  letter-spacing: .12em;
  color: var(--sub);
}

.glz-23a__card {
  width: min(300px,100%);
  padding: 26px;
  border-radius: 22px;
  color: var(--ink);
  background: var(--fill);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid var(--line);
  box-shadow: 0 24px 48px -22px rgba(10,14,30,.45),inset 0 1px 0 var(--line);
}

.glz-23a__chip {
  display: inline-block;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .2em;
  text-transform: uppercase;
  padding: 5px 11px;
  border-radius: 99px;
  color: var(--ink);
  border: 1px solid var(--line);
  background: rgba(255,255,255,.14);
}

.glz-23a__card h3 {
  margin-top: 14px;
  font-size: 19px;
  font-weight: 800;
  letter-spacing: -.015em;
}

.glz-23a__card p {
  margin-top: 8px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--sub);
}

.glz-23a__card button {
  margin-top: 18px;
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 12px;
  background: var(--btn);
  color: var(--btn-ink);
  font: 700 13px 'Manrope',sans-serif;
  cursor: pointer;
  transition: transform .2s ease;
}

.glz-23a__card button:hover {
  transform: translateY(-2px);
}

.glz-23a__card button:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-23a__scheme--light .glz-23a__card {
    background: rgba(255,255,255,.92);
  }

  .glz-23a__scheme--dark .glz-23a__card {
    background: rgba(20,24,40,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-23a__card button {
    transition: none;
  }
}

.glz-23b,
.glz-23b *,
.glz-23b *::before,
.glz-23b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-23b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
}

.glz-23b__stage {
  --fill: rgba(255,255,255,.55);
  --ink: #242a3c;
  --sub: rgba(36,42,60,.62);
  --line: rgba(255,255,255,.8);
  --acc: oklch(0.62 0.19 265);
  width: 100%;
  min-height: 100vh;
  margin: -48px -24px;
  padding: 48px 24px;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  background: radial-gradient(120% 100% at 16% 0%,oklch(0.9 0.07 250),transparent 55%),radial-gradient(110% 90% at 88% 100%,oklch(0.88 0.08 40),transparent 55%),#edeff5;
  transition: background .5s ease;
  font-family: 'Manrope',system-ui,sans-serif;
}

.glz-23b__stage:has(.glz-23b__check:checked) {
  --fill: rgba(16,20,34,.5);
  --ink: #ecf0fc;
  --sub: rgba(236,240,252,.6);
  --line: rgba(255,255,255,.16);
  --acc: oklch(0.8 0.14 210);
  background: radial-gradient(120% 100% at 16% 0%,oklch(0.38 0.13 275/.8),transparent 55%),radial-gradient(110% 90% at 88% 100%,oklch(0.4 0.14 330/.7),transparent 55%),#0a0d17;
}

.glz-23b__check {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.glz-23b__toggle {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
  font-size: 14px;
  color: var(--ink);
}

.glz-23b__toggle i {
  width: 52px;
  height: 28px;
  border-radius: 99px;
  background: var(--fill);
  border: 1px solid var(--line);
  position: relative;
  transition: background .5s ease;
}

.glz-23b__toggle i::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--acc);
  box-shadow: 0 2px 8px rgba(0,0,0,.35);
  transition: translate .35s cubic-bezier(.3,1.4,.4,1),background .5s ease;
}

.glz-23b__stage:has(.glz-23b__check:checked) .glz-23b__toggle i::after {
  translate: 24px 0;
}

.glz-23b__stage:has(.glz-23b__check:focus-visible) .glz-23b__toggle i {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.glz-23b__sun,
.glz-23b__moon {
  transition: opacity .4s ease;
}

.glz-23b__stage:has(.glz-23b__check:checked) .glz-23b__sun {
  opacity: .35;
}

.glz-23b__stage:not(:has(.glz-23b__check:checked)) .glz-23b__moon {
  opacity: .35;
}

.glz-23b__card {
  width: min(360px,100%);
  padding: 28px;
  border-radius: 24px;
  color: var(--ink);
  background: var(--fill);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid var(--line);
  box-shadow: 0 30px 60px -26px rgba(8,12,26,.5),inset 0 1px 0 var(--line);
  transition: background .5s ease,color .5s ease,border-color .5s ease;
}

.glz-23b__card h3 {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -.02em;
}

.glz-23b__card>p {
  margin-top: 9px;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--sub);
  transition: color .5s ease;
}

.glz-23b__row {
  display: flex;
  justify-content: space-between;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--line);
  font-size: 12.5px;
  color: var(--sub);
  transition: border-color .5s ease,color .5s ease;
}

.glz-23b__row b {
  color: var(--acc);
  font-weight: 800;
  transition: color .5s ease;
}

.glz-23b__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-23b__card {
    background: rgba(255,255,255,.92);
  }

  .glz-23b__stage:has(.glz-23b__check:checked) .glz-23b__card {
    background: rgba(18,22,38,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-23b__stage,
    .glz-23b__card,
    .glz-23b__card>p,
    .glz-23b__row,
    .glz-23b__row b,
    .glz-23b__toggle i,
    .glz-23b__toggle i::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one card markup, two wrapper classes flipping ~6 custom properties; each maps 1:1 to a Tailwind utility + its dark: twin. */

/* No JavaScript — :has(checkbox:checked) on the stage swaps the six theme properties; consumers (fills, ink, borders, background) transition, the properties don't. */
```
