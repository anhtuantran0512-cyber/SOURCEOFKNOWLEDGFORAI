---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/8-bit-pixel-art-ui-elements-buttons/"
title: "Eight Bit Pixel Art Buttons and HUD"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A game HUD and control set built entirely from stepped box-shadow blocks: segmented health, score with tabular figures, a lives row, and buttons whose…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Eight Bit Pixel Art Buttons and HUD
Source: https://codefronts.com/design-styles/css-retro-designs/8-bit-pixel-art-ui-elements-buttons/

A game HUD and control set built entirely from stepped box-shadow blocks: segmented health, score with tabular figures, a lives row, and buttons whose notched corners are shadow offsets rather than a border image. The palette is a fixed 8-colour subset of the NES set and the demo enforces it, because palette discipline is what separates pixel art from a filter.
## HTML
```html
<section class="rt-11" aria-labelledby="rt-11-title">
  <h2 class="rt-11__sr" id="rt-11-title">Eight-bit pixel art HUD and button set</h2>

  <div class="rt-11__theme">
    <input class="rt-11__theme-input" type="checkbox" id="rt-11-theme">
    <label class="rt-11__theme-label" for="rt-11-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-11__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-11__stage">
    <p class="rt-11__badge">NES-era palette subset &middot; 8 colours, no anti-aliasing</p>

    <div class="rt-11__hud">
      <div class="rt-11__hud-row">
        <div class="rt-11__block">
          <span class="rt-11__label">HEALTH</span>
          <div class="rt-11__bar" role="meter" aria-valuenow="7" aria-valuemin="0" aria-valuemax="10" aria-label="Health, 7 of 10">
            <span class="rt-11__seg rt-11__seg--on"></span><span class="rt-11__seg rt-11__seg--on"></span>
            <span class="rt-11__seg rt-11__seg--on"></span><span class="rt-11__seg rt-11__seg--on"></span>
            <span class="rt-11__seg rt-11__seg--on"></span><span class="rt-11__seg rt-11__seg--on"></span>
            <span class="rt-11__seg rt-11__seg--on"></span><span class="rt-11__seg"></span>
            <span class="rt-11__seg"></span><span class="rt-11__seg"></span>
          </div>
          <span class="rt-11__val">7 / 10</span>
        </div>

        <div class="rt-11__block">
          <span class="rt-11__label">SCORE</span>
          <p class="rt-11__score">0128450</p>
        </div>

        <div class="rt-11__block">
          <span class="rt-11__label">LIVES</span>
          <ul class="rt-11__lives" aria-label="Three lives remaining">
            <li><span class="rt-11__life" aria-hidden="true"></span></li>
            <li><span class="rt-11__life" aria-hidden="true"></span></li>
            <li><span class="rt-11__life" aria-hidden="true"></span></li>
          </ul>
        </div>

        <div class="rt-11__block">
          <span class="rt-11__label">STAGE</span>
          <p class="rt-11__stage-n">2&ndash;4</p>
        </div>
      </div>
    </div>

    <div class="rt-11__panel">
      <h3 class="rt-11__panel-h">Controls</h3>
      <div class="rt-11__btns">
        <button class="rt-11__btn" type="button" style="--rt-11-btn: var(--rt-11-red)">START</button>
        <button class="rt-11__btn" type="button" style="--rt-11-btn: var(--rt-11-blue)">SELECT</button>
        <button class="rt-11__btn" type="button" style="--rt-11-btn: var(--rt-11-green); --rt-11-btn-ink: #101820">CONTINUE</button>
        <button class="rt-11__btn rt-11__btn--off" type="button" disabled>LOCKED</button>
      </div>

      <h3 class="rt-11__panel-h">Palette &mdash; eight entries, no ninth</h3>
      <ul class="rt-11__pal">
        <li><span style="--rt-11-c: var(--rt-11-ink)"></span>ink</li>
        <li><span style="--rt-11-c: var(--rt-11-paper)"></span>paper</li>
        <li><span style="--rt-11-c: var(--rt-11-red)"></span>red</li>
        <li><span style="--rt-11-c: var(--rt-11-orange)"></span>orange</li>
        <li><span style="--rt-11-c: var(--rt-11-yellow)"></span>yellow</li>
        <li><span style="--rt-11-c: var(--rt-11-green)"></span>green</li>
        <li><span style="--rt-11-c: var(--rt-11-blue)"></span>blue</li>
        <li><span style="--rt-11-c: var(--rt-11-sky)"></span>sky</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-11 {
  --rt-11-px: 4px;
  --rt-11-ink: #101820;
  --rt-11-paper: #f8f8f8;
  --rt-11-red: #d82800;
  --rt-11-orange: #fc9838;
  --rt-11-yellow: #fcfc54;
  --rt-11-green: #00a844;
  --rt-11-blue: #2038ec;
  --rt-11-sky: #9cd2f8;
  --rt-11-mono: ui-monospace, SFMono-Regular, "Cascadia Mono", Consolas, "DejaVu Sans Mono", monospace;
  --rt-11-bg: var(--rt-11-sky);
  --rt-11-surface: var(--rt-11-paper);
  --rt-11-acc: #1a2ba8;
  --rt-11-acc: oklch(38% 0.2 265);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-11-bg);
  color: var(--rt-11-ink);
  font-family: var(--rt-11-mono);
  -webkit-text-size-adjust: 100%;
}

.rt-11 *,
.rt-11 *::before,
.rt-11 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-11 {
    --rt-11-bg: #14203a;
    --rt-11-bg: oklch(24% 0.06 265);
    --rt-11-surface: #e4e6ec;
  }
}

.rt-11[data-theme="dark"],
.rt-11:has(.rt-11__theme-input:checked) {
  --rt-11-bg: #14203a;
  --rt-11-bg: oklch(24% 0.06 265);
  --rt-11-surface: #e4e6ec;
}

@media (prefers-color-scheme: light) {
  .rt-11:has(.rt-11__theme-input:checked) {
    --rt-11-bg: #14203a;
    --rt-11-bg: oklch(24% 0.06 265);
    --rt-11-surface: #e4e6ec;
  }
}

@media (prefers-color-scheme: dark) {
  .rt-11:has(.rt-11__theme-input:checked) {
    --rt-11-bg: var(--rt-11-sky);
    --rt-11-surface: var(--rt-11-paper);
  }
}

.rt-11__sr {
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

.rt-11__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-11__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-11__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  background: var(--rt-11-paper);
  color: var(--rt-11-ink);
  box-shadow: calc(var(--rt-11-px) * -1) 0 0 0 var(--rt-11-ink), var(--rt-11-px) 0 0 0 var(--rt-11-ink), 0 calc(var(--rt-11-px) * -1) 0 0 var(--rt-11-ink), 0 var(--rt-11-px) 0 0 var(--rt-11-ink);
}

.rt-11__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-11__theme-input:focus-visible + .rt-11__theme-label {
  outline: 2px solid var(--rt-11-acc);
  outline-offset: 6px;
}

.rt-11__stage {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: clamp(3.75rem, 3rem + 3vw, 5rem) clamp(1rem, 0.6rem + 2vw, 2.25rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.rt-11__badge {
  margin: 0;
  justify-self: start;
  min-inline-size: 0;
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  background: var(--rt-11-ink);
  color: var(--rt-11-paper);
  padding: 0.4rem 0.7rem;
}

.rt-11__hud,
.rt-11__panel {
  min-inline-size: 0;
  background: var(--rt-11-surface);
  padding: clamp(1rem, 0.7rem + 1.4vw, 1.5rem);
  box-shadow: calc(var(--rt-11-px) * -1) 0 0 0 var(--rt-11-ink), var(--rt-11-px) 0 0 0 var(--rt-11-ink), 0 calc(var(--rt-11-px) * -1) 0 0 var(--rt-11-ink), 0 var(--rt-11-px) 0 0 var(--rt-11-ink), calc(var(--rt-11-px) * -2) 0 0 0 var(--rt-11-ink), calc(var(--rt-11-px) * 2) 0 0 0 var(--rt-11-ink), 0 calc(var(--rt-11-px) * -2) 0 0 var(--rt-11-ink), 0 calc(var(--rt-11-px) * 2) 0 0 var(--rt-11-ink);
}

.rt-11__hud-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: clamp(0.85rem, 0.6rem + 1vw, 1.4rem);
}

.rt-11__block {
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  align-content: start;
}

.rt-11__label {
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  color: var(--rt-11-ink);
}

.rt-11__bar {
  display: flex;
  flex-wrap: wrap;
  gap: var(--rt-11-px);
  min-inline-size: 0;
}

.rt-11__seg {
  inline-size: 14px;
  block-size: 22px;
  flex: none;
  background: var(--rt-11-paper);
  box-shadow: inset 0 0 0 var(--rt-11-px) var(--rt-11-ink);
}

.rt-11__seg--on {
  background: var(--rt-11-red);
  box-shadow: inset 0 0 0 var(--rt-11-px) var(--rt-11-ink), inset var(--rt-11-px) var(--rt-11-px) 0 var(--rt-11-px) var(--rt-11-orange);
}

.rt-11__val {
  font-size: 0.78rem;
  font-variant-numeric: tabular-nums;
  color: var(--rt-11-ink);
}

.rt-11__score {
  margin: 0;
  font-size: clamp(1.5rem, 1rem + 3vw, 2.4rem);
  font-weight: 700;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.06em;
  color: var(--rt-11-ink);
  text-shadow: var(--rt-11-px) var(--rt-11-px) 0 var(--rt-11-yellow);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.rt-11__lives {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: 0.5rem;
}

.rt-11__life {
  display: block;
  inline-size: 8px;
  block-size: 8px;
  background: var(--rt-11-red);
  box-shadow: -8px -8px 0 0 var(--rt-11-red), 8px -8px 0 0 var(--rt-11-red), -16px 0 0 0 var(--rt-11-red), -8px 0 0 0 var(--rt-11-red), 8px 0 0 0 var(--rt-11-red), 16px 0 0 0 var(--rt-11-red), -8px 8px 0 0 var(--rt-11-red), 0 8px 0 0 var(--rt-11-red), 8px 8px 0 0 var(--rt-11-red), 0 16px 0 0 var(--rt-11-red);
  margin: 12px 20px 20px 20px;
}

.rt-11__stage-n {
  margin: 0;
  font-size: clamp(1.5rem, 1rem + 3vw, 2.4rem);
  font-weight: 700;
  line-height: 1;
  color: var(--rt-11-blue);
}

.rt-11__panel {
  display: grid;
  gap: 1rem;
  align-content: start;
}

.rt-11__panel-h {
  margin: 0;
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--rt-11-ink);
}

.rt-11__btns {
  display: flex;
  flex-wrap: wrap;
  gap: calc(var(--rt-11-px) * 3);
}

.rt-11__btn {
  --rt-11-btn: var(--rt-11-blue);
  --rt-11-btn-ink: #f8f8f8;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 0.65rem 1.2rem;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  background: var(--rt-11-btn);
  color: var(--rt-11-btn-ink, var(--rt-11-paper));
  box-shadow: calc(var(--rt-11-px) * -1) 0 0 0 var(--rt-11-ink), var(--rt-11-px) 0 0 0 var(--rt-11-ink), 0 calc(var(--rt-11-px) * -1) 0 0 var(--rt-11-ink), 0 var(--rt-11-px) 0 0 var(--rt-11-ink), inset calc(var(--rt-11-px) * -1) calc(var(--rt-11-px) * -1) 0 0 rgba(16, 24, 32, 0.55), inset var(--rt-11-px) var(--rt-11-px) 0 0 rgba(248, 248, 248, 0.5);
}

.rt-11__btn:active {
  box-shadow: calc(var(--rt-11-px) * -1) 0 0 0 var(--rt-11-ink), var(--rt-11-px) 0 0 0 var(--rt-11-ink), 0 calc(var(--rt-11-px) * -1) 0 0 var(--rt-11-ink), 0 var(--rt-11-px) 0 0 var(--rt-11-ink), inset var(--rt-11-px) var(--rt-11-px) 0 0 rgba(16, 24, 32, 0.55), inset calc(var(--rt-11-px) * -1) calc(var(--rt-11-px) * -1) 0 0 rgba(248, 248, 248, 0.5);
}

.rt-11__btn:focus-visible {
  outline: 2px solid var(--rt-11-ink);
  outline-offset: 8px;
}

.rt-11__btn--off {
  background: #9a9a9a;
  color: #2a2a2a;
  cursor: not-allowed;
}

.rt-11__pal {
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 6.5rem), 1fr));
  gap: 0.5rem;
}

.rt-11__pal li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.7rem;
  min-inline-size: 0;
}

.rt-11__pal li span {
  inline-size: 20px;
  block-size: 20px;
  flex: none;
  background: var(--rt-11-c);
  box-shadow: 0 0 0 2px var(--rt-11-ink);
}

@media (min-width: 56rem) {
  .rt-11__stage {
    grid-template-columns: minmax(0, 1fr);
  }
}
```
