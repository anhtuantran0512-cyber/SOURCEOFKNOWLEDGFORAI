---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/vaporwave-aesthetic-website-theme-design/"
title: "Vaporwave Aesthetic Scene"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A perspective grid running to a banded sunset, with chrome lettering and a palm silhouette &mdash; the outrun scene built from a rotated grid plane, a…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vaporwave Aesthetic Scene
Source: https://codefronts.com/design-styles/css-retro-designs/vaporwave-aesthetic-website-theme-design/

A perspective grid running to a banded sunset, with chrome lettering and a palm silhouette &mdash; the outrun scene built from a rotated grid plane, a repeating gradient and a stacked text fill, no images. It also names what it is: this aesthetic comes from 1980s marketing and album art, not from 1980s computers, which makes it the odd one out here on purpose.
## HTML
```html
<section class="rt-14" aria-labelledby="rt-14-title">
  <h2 class="rt-14__sr" id="rt-14-title">Vaporwave grid horizon scene</h2>

  <div class="rt-14__theme">
    <input class="rt-14__theme-input" type="checkbox" id="rt-14-theme">
    <label class="rt-14__theme-label" for="rt-14-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-14__sr">Toggle night scene</span>
    </label>
  </div>

  <div class="rt-14__scene">
    <div class="rt-14__sky" aria-hidden="true">
      <span class="rt-14__sun"></span>
      <span class="rt-14__stars"></span>
    </div>
    <div class="rt-14__floor" aria-hidden="true"><span class="rt-14__plane"></span></div>
    <span class="rt-14__palm" aria-hidden="true"></span>

    <div class="rt-14__content">
      <p class="rt-14__kicker">Airbrush, chrome and grid &middot; 1984 record sleeve</p>
      <p class="rt-14__title">NIGHT DRIVE</p>
      <div class="rt-14__card">
        <h3 class="rt-14__card-h">Not an interface</h3>
        <p class="rt-14__card-p">This is how the decade advertised computing, not how it looked to use one. Everything else in this collection reproduces a system someone sat in front of. Treat this as a title card or a splash, and put the working interface somewhere else.</p>
        <div class="rt-14__actions">
          <button class="rt-14__btn" type="button">Enter</button>
          <button class="rt-14__btn rt-14__btn--ghost" type="button">Track list</button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-14 {
  --rt-14-magenta: #ff2fb4;
  --rt-14-cyan: #35e8ff;
  --rt-14-violet: #6d2bd9;
  --rt-14-amber: #ffb24d;
  --rt-14-deep: #16062e;
  --rt-14-geo: ui-rounded, "Avenir Next", "Century Gothic", "Futura", system-ui, sans-serif;
  --rt-14-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --rt-14-sky-a: #2a0a4a;
  --rt-14-sky-b: #a3247f;
  --rt-14-sky-c: #ff7a4d;
  --rt-14-travel: 3.2s;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-14-deep);
  color: #ffffff;
  font-family: var(--rt-14-geo);
  overflow: hidden;
  -webkit-text-size-adjust: 100%;
}

.rt-14 *,
.rt-14 *::before,
.rt-14 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-14 {
    --rt-14-sky-a: #0a0320;
    --rt-14-sky-b: #4c1152;
    --rt-14-sky-c: #b8433f;
    --rt-14-deep: #08021a;
  }
}

.rt-14[data-theme="dark"],
.rt-14:has(.rt-14__theme-input:checked) {
  --rt-14-sky-a: #0a0320;
  --rt-14-sky-b: #4c1152;
  --rt-14-sky-c: #b8433f;
  --rt-14-deep: #08021a;
}

@media (prefers-color-scheme: light) {
  .rt-14:has(.rt-14__theme-input:checked) {
    --rt-14-sky-a: #0a0320;
    --rt-14-sky-b: #4c1152;
    --rt-14-sky-c: #b8433f;
    --rt-14-deep: #08021a;
  }
}

@media (prefers-color-scheme: dark) {
  .rt-14:has(.rt-14__theme-input:checked) {
    --rt-14-sky-a: #2a0a4a;
    --rt-14-sky-b: #a3247f;
    --rt-14-sky-c: #ff7a4d;
    --rt-14-deep: #16062e;
  }
}

.rt-14__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-14__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.rt-14__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-14__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  border-radius: 50%;
  background: rgba(10, 3, 32, 0.65);
  color: var(--rt-14-cyan);
  border: 1px solid rgba(53, 232, 255, 0.55);
}

.rt-14__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-14__theme-input:focus-visible + .rt-14__theme-label {
  outline: 2px solid var(--rt-14-cyan);
  outline-offset: 3px;
}

.rt-14__scene {
  position: relative;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  align-content: center;
  padding: clamp(4rem, 3rem + 4vw, 6rem) clamp(1rem, 0.6rem + 3vw, 3rem);
  isolation: isolate;
}

.rt-14__sky {
  position: absolute;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 62%;
  z-index: 0;
  background: linear-gradient(180deg, var(--rt-14-sky-a) 0%, var(--rt-14-sky-b) 62%, var(--rt-14-sky-c) 100%);
}

.rt-14__stars {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(1.5px 1.5px at 12% 18%, rgba(255,255,255,0.9), transparent), radial-gradient(1.5px 1.5px at 28% 9%, rgba(255,255,255,0.7), transparent), radial-gradient(1.5px 1.5px at 47% 22%, rgba(255,255,255,0.85), transparent), radial-gradient(1.5px 1.5px at 68% 12%, rgba(255,255,255,0.6), transparent), radial-gradient(1.5px 1.5px at 82% 26%, rgba(255,255,255,0.8), transparent), radial-gradient(1.5px 1.5px at 92% 8%, rgba(255,255,255,0.65), transparent);
}

.rt-14__sun {
  position: absolute;
  inset-block-end: -6%;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: min(360px, 62vw);
  aspect-ratio: 1 / 1;
  border-radius: 50%;
  background: repeating-linear-gradient(180deg,
        rgba(0,0,0,0) 0 46%,
        rgba(22, 6, 46, 0.92) 46% 48%,
        rgba(0,0,0,0) 48% 54%,
        rgba(22, 6, 46, 0.92) 54% 57%,
        rgba(0,0,0,0) 57% 64%,
        rgba(22, 6, 46, 0.92) 64% 68%,
        rgba(0,0,0,0) 68% 76%,
        rgba(22, 6, 46, 0.92) 76% 81%,
        rgba(0,0,0,0) 81% 89%,
        rgba(22, 6, 46, 0.92) 89% 95%), linear-gradient(180deg, #ffe66b 0%, var(--rt-14-amber) 42%, var(--rt-14-magenta) 100%);
  filter: drop-shadow(0 0 44px rgba(255, 122, 77, 0.55));
}

.rt-14__floor {
  position: absolute;
  inset-block-end: 0;
  inset-inline: -20%;
  block-size: 44%;
  z-index: 1;
  perspective: 240px;
  perspective-origin: 50% 0%;
  overflow: hidden;
  background: linear-gradient(180deg, #1c0736 0%, #0b0220 100%);
}

.rt-14__plane {
  position: absolute;
  inset: -60% -10% -30%;
  transform: rotateX(72deg);
  transform-origin: 50% 0%;
  background-image: repeating-linear-gradient(90deg, rgba(53, 232, 255, 0.85) 0 2px, rgba(0,0,0,0) 2px 60px), repeating-linear-gradient(0deg, rgba(255, 47, 180, 0.75) 0 2px, rgba(0,0,0,0) 2px 60px);
  animation: rt-14-travel var(--rt-14-travel) linear infinite;
}

@keyframes rt-14-travel {
  from {
    background-position: 0 0, 0 0;
  }

  to {
    background-position: 0 0, 0 60px;
  }
}

.rt-14__palm {
  position: absolute;
  inset-block-end: 30%;
  inset-inline-start: clamp(0.5rem, 3vw, 4rem);
  z-index: 2;
  inline-size: clamp(60px, 12vw, 120px);
  block-size: clamp(140px, 26vw, 260px);
  background: #12042a;
  clip-path: polygon(47% 100%, 44% 46%, 22% 40%, 6% 24%, 26% 30%, 40% 36%, 22% 12%, 44% 28%, 50% 4%, 56% 28%, 78% 12%, 60% 36%, 76% 30%, 94% 24%, 78% 40%, 56% 46%, 53% 100%);
}

.rt-14__content {
  position: relative;
  z-index: 3;
  min-inline-size: 0;
  max-inline-size: 46rem;
  margin-inline: auto;
  display: grid;
  gap: clamp(0.9rem, 0.6rem + 1.5vw, 1.5rem);
  justify-items: center;
  text-align: center;
}

.rt-14__kicker {
  margin: 0;
  font-family: var(--rt-14-mono);
  font-size: 0.68rem;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--rt-14-cyan);
  min-inline-size: 0;
}

.rt-14__title {
  margin: 0;
  font-size: clamp(2.4rem, 1rem + 9vw, 6rem);
  line-height: 0.92;
  font-weight: 800;
  letter-spacing: 0.02em;
  min-inline-size: 0;
  color: #eef4ff;
  text-shadow: 0 3px 0 #7a2c96, 0 6px 18px rgba(0,0,0,0.55);
}

@supports ((-webkit-background-clip: text) or (background-clip: text)) {
  .rt-14__title {
    background-image: linear-gradient(180deg, #d9f6ff 0%, #6fb7ff 49.9%, #2b1a6b 50%, #ffb6e6 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

.rt-14__card {
  min-inline-size: 0;
  max-inline-size: 36rem;
  text-align: start;
  background: rgba(9, 3, 26, 0.82);
  border: 1px solid rgba(53, 232, 255, 0.4);
  border-radius: 4px;
  padding: clamp(1rem, 0.75rem + 1.4vw, 1.6rem);
  display: grid;
  gap: 0.75rem;
  box-shadow: 0 0 0 1px rgba(255, 47, 180, 0.22), 0 24px 44px -24px rgba(0,0,0,0.8);
}

.rt-14__card-h {
  margin: 0;
  font-size: 0.78rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--rt-14-cyan);
}

.rt-14__card-p {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.65;
  color: #e6e2f5;
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-14__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.rt-14__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 0.65rem 1.3rem;
  cursor: pointer;
  border: 0;
  font: inherit;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  border-radius: 3px;
  background: linear-gradient(180deg, var(--rt-14-magenta), #b3157f);
  color: #ffffff;
  box-shadow: 0 2px 0 #6b0d4c, 0 0 20px rgba(255, 47, 180, 0.4);
}

.rt-14__btn--ghost {
  background: transparent;
  color: var(--rt-14-cyan);
  box-shadow: inset 0 0 0 2px rgba(53, 232, 255, 0.75);
}

.rt-14__btn:active {
  transform: translateY(2px);
  box-shadow: 0 0 0 #6b0d4c;
}

.rt-14__btn:focus-visible {
  outline: 2px solid #ffffff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .rt-14__plane {
    animation: none;
  }

  .rt-14__btn {
    transition: none;
  }
}
```
