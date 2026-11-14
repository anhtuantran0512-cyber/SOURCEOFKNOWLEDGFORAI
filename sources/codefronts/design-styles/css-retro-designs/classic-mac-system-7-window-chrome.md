---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/classic-mac-system-7-window-chrome/"
title: "Classic Mac System 7 Window Chrome"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "The other great desktop metaphor, and a deliberate contrast to the bevelled 16-bit look: horizontal pinstripe title bar, square close box on the left, grow…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Classic Mac System 7 Window Chrome
Source: https://codefronts.com/design-styles/css-retro-designs/classic-mac-system-7-window-chrome/

The other great desktop metaphor, and a deliberate contrast to the bevelled 16-bit look: horizontal pinstripe title bar, square close box on the left, grow box bottom-right, one-pixel black outline everywhere and no colour at all. It also answers the question a 1-bit interface forces &mdash; how do you show state when there is no second colour to reach for?
## HTML
```html
<section class="rt-05" aria-labelledby="rt-05-title">
  <h2 class="rt-05__sr" id="rt-05-title">Classic Macintosh System 7 window chrome</h2>

  <div class="rt-05__theme">
    <input class="rt-05__theme-input" type="checkbox" id="rt-05-theme">
    <label class="rt-05__theme-label" for="rt-05-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-05__sr">Toggle dark desktop pattern</span>
    </label>
  </div>

  <div class="rt-05__menubar">
    <span class="rt-05__apple" aria-hidden="true"></span>
    <nav class="rt-05__menu" aria-label="System 7 menu bar">
      <ul class="rt-05__menu-list">
        <li><button class="rt-05__menu-item" type="button">File</button></li>
        <li><button class="rt-05__menu-item" type="button">Edit</button></li>
        <li><button class="rt-05__menu-item" type="button">View</button></li>
        <li><button class="rt-05__menu-item" type="button">Label</button></li>
        <li><button class="rt-05__menu-item" type="button">Special</button></li>
      </ul>
    </nav>
    <span class="rt-05__clockline">System 7.1</span>
  </div>

  <div class="rt-05__stage">
    <div class="rt-05__win rt-05__win--active">
      <div class="rt-05__bar">
        <span class="rt-05__box rt-05__box--close" role="img" aria-label="Close box"><span class="rt-05__box-in" aria-hidden="true"></span></span>
        <span class="rt-05__bar-t">Macintosh HD</span>
        <span class="rt-05__box rt-05__box--zoom" role="img" aria-label="Zoom box"><span class="rt-05__box-in" aria-hidden="true"></span></span>
      </div>
      <div class="rt-05__info">
        <span>4 items</span>
        <span>18.2 MB in disk</span>
        <span>21.6 MB available</span>
      </div>
      <ul class="rt-05__list">
        <li class="rt-05__row">
          <span class="rt-05__ic" aria-hidden="true"></span>
          <span class="rt-05__nm">System Folder</span>
          <span class="rt-05__sz">6,144K</span>
          <span class="rt-05__dt">Tue, Mar 4</span>
        </li>
        <li class="rt-05__row rt-05__row--sel" aria-current="true">
          <span class="rt-05__ic rt-05__ic--doc" aria-hidden="true"></span>
          <span class="rt-05__nm">Read Me First</span>
          <span class="rt-05__sz">12K</span>
          <span class="rt-05__dt">Tue, Mar 4</span>
        </li>
        <li class="rt-05__row">
          <span class="rt-05__ic rt-05__ic--doc" aria-hidden="true"></span>
          <span class="rt-05__nm">Scrapbook File</span>
          <span class="rt-05__sz">88K</span>
          <span class="rt-05__dt">Fri, Feb 28</span>
        </li>
        <li class="rt-05__row rt-05__row--off" aria-disabled="true">
          <span class="rt-05__ic rt-05__ic--doc" aria-hidden="true"></span>
          <span class="rt-05__nm">Locked Archive <span class="rt-05__sr">(unavailable)</span></span>
          <span class="rt-05__sz">1,204K</span>
          <span class="rt-05__dt">Sun, Jan 12</span>
        </li>
      </ul>
      <div class="rt-05__foot">
        <div class="rt-05__scroll" aria-hidden="true"><span class="rt-05__thumb"></span></div>
        <button class="rt-05__grow" type="button" aria-label="Resize window"><span class="rt-05__grow-in" aria-hidden="true"></span></button>
      </div>
    </div>

    <div class="rt-05__win rt-05__win--small">
      <div class="rt-05__bar">
        <span class="rt-05__box rt-05__box--close" role="img" aria-label="Close box (window inactive)"></span>
        <span class="rt-05__bar-t">Inactive Window</span>
        <span class="rt-05__box rt-05__box--zoom"></span>
      </div>
      <div class="rt-05__note">
        <p>No stripes, empty boxes. That is the entire focus indicator &mdash; there is no second colour to dim.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-05 {
  --rt-05-stripe: 2px;
  --rt-05-hit: 44px;
  --rt-05-k: #000000;
  --rt-05-w: #ffffff;
  --rt-05-sans: system-ui, -apple-system, "Lucida Grande", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --rt-05-mono: ui-monospace, SFMono-Regular, Monaco, Menlo, Consolas, monospace;
  --rt-05-desk-a: #ffffff;
  --rt-05-desk-b: #b9b9b9;
  --rt-05-acc: #0b4fd0;
  --rt-05-acc: oklch(45% 0.2 262);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--rt-05-desk-a);
  background-image: repeating-conic-gradient(var(--rt-05-desk-b) 0% 25%, var(--rt-05-desk-a) 0% 50%);
  background-size: 4px 4px;
  color: var(--rt-05-k);
  font-family: var(--rt-05-sans);
  -webkit-text-size-adjust: 100%;
}

.rt-05 *,
.rt-05 *::before,
.rt-05 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-05 {
    --rt-05-desk-a: #2a2a2a;
    --rt-05-desk-b: #000000;
  }
}

.rt-05[data-theme="dark"],
.rt-05:has(.rt-05__theme-input:checked) {
  --rt-05-desk-a: #2a2a2a;
  --rt-05-desk-b: #000000;
}

@media (prefers-color-scheme: light) {
  .rt-05:has(.rt-05__theme-input:checked) {
    --rt-05-desk-a: #2a2a2a;
    --rt-05-desk-b: #000000;
  }
}

@media (prefers-color-scheme: dark) {
  .rt-05:has(.rt-05__theme-input:checked) {
    --rt-05-desk-a: #ffffff;
    --rt-05-desk-b: #b9b9b9;
  }
}

.rt-05__sr {
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

.rt-05__theme {
  position: absolute;
  inset-block-start: calc(var(--rt-05-hit) + 0.75rem);
  inset-inline-end: 1rem;
  z-index: 8;
}

.rt-05__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-05__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  background: var(--rt-05-w);
  color: var(--rt-05-k);
  border: 1px solid var(--rt-05-k);
  border-radius: 4px;
  box-shadow: 2px 2px 0 0 var(--rt-05-k);
}

.rt-05__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-05__theme-input:focus-visible + .rt-05__theme-label {
  outline: 2px solid var(--rt-05-acc);
  outline-offset: 2px;
}

.rt-05__menubar {
  position: relative;
  z-index: 4;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: var(--rt-05-hit);
  padding-inline: 0.5rem;
  background: var(--rt-05-w);
  border-block-end: 1px solid var(--rt-05-k);
  overflow-x: auto;
  scrollbar-width: thin;
}

.rt-05__apple {
  inline-size: 14px;
  block-size: 16px;
  flex: none;
  margin-inline: 0.35rem;
  background: var(--rt-05-k);
  clip-path: polygon(52% 0, 62% 9%, 55% 14%, 78% 20%, 96% 44%, 82% 62%, 92% 86%, 68% 100%, 50% 92%, 32% 100%, 8% 86%, 4% 50%, 20% 20%, 44% 15%);
}

.rt-05__menu {
  min-inline-size: 0;
}

.rt-05__menu-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: 0;
}

.rt-05__menu-item {
  min-block-size: var(--rt-05-hit);
  min-inline-size: 44px;
  padding-inline: 0.7rem;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: 0.85rem;
  color: var(--rt-05-k);
  cursor: pointer;
  white-space: nowrap;
}

.rt-05__menu-item:hover {
  background: var(--rt-05-k);
  color: var(--rt-05-w);
}

.rt-05__menu-item:focus-visible {
  outline: 2px solid var(--rt-05-acc);
  outline-offset: -3px;
}

.rt-05__clockline {
  margin-inline-start: auto;
  padding-inline: 0.6rem;
  font-size: 0.78rem;
  white-space: nowrap;
  font-family: var(--rt-05-mono);
}

.rt-05__stage {
  padding: clamp(1.25rem, 1rem + 2vw, 3rem) clamp(0.6rem, 0.4rem + 1.5vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
  max-inline-size: 62rem;
  margin-inline: auto;
  align-items: start;
}

.rt-05__win {
  min-inline-size: 0;
  background: var(--rt-05-w);
  border: 1px solid var(--rt-05-k);
  box-shadow: 2px 2px 0 0 var(--rt-05-k);
}

.rt-05__bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: var(--rt-05-hit);
  padding-inline: 0.35rem;
  border-block-end: 1px solid var(--rt-05-k);
  min-inline-size: 0;
}

.rt-05__win--active .rt-05__bar {
  background: repeating-linear-gradient(
      to bottom,
      var(--rt-05-k) 0 1px,
      var(--rt-05-w) 1px var(--rt-05-stripe)
    );
}

.rt-05__bar-t {
  flex: 1 1 auto;
  min-inline-size: 0;
  text-align: center;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.01em;
  background: var(--rt-05-w);
  padding: 0.15rem 0.7rem;
  margin-inline: 0.25rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.rt-05__box {
  inline-size: var(--rt-05-hit);
  block-size: var(--rt-05-hit);
  flex: none;
  display: grid;
  place-items: center;
}

.rt-05__box-in,
.rt-05__box::before {
  content: "";
  inline-size: 15px;
  block-size: 15px;
  border: 1px solid var(--rt-05-k);
  background: var(--rt-05-w);
}

.rt-05__box-in {
  position: absolute;
  inline-size: 7px;
  block-size: 7px;
  border: 1px solid var(--rt-05-k);
  background: var(--rt-05-w);
}

.rt-05__box {
  position: relative;
}

.rt-05__win:not(.rt-05__win--active) .rt-05__box::before {
  border-color: var(--rt-05-k);
}

.rt-05__box--zoom .rt-05__box-in {
  inline-size: 9px;
  block-size: 9px;
}

.rt-05__info {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem 1.25rem;
  padding: 0.55rem 0.75rem;
  font-size: 0.78rem;
  border-block-end: 1px solid var(--rt-05-k);
  min-inline-size: 0;
}

.rt-05__list {
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.rt-05__row {
  display: grid;
  grid-template-columns: 28px minmax(0, 1fr) auto;
  gap: 0 0.6rem;
  align-items: center;
  min-block-size: 44px;
  padding: 0.35rem 0.75rem;
  font-size: 0.85rem;
  border-block-end: 1px solid var(--rt-05-k);
}

.rt-05__row:last-child {
  border-block-end: 0;
}

.rt-05__row--sel {
  background: var(--rt-05-k);
  color: var(--rt-05-w);
}

.rt-05__row--sel .rt-05__ic {
  background: var(--rt-05-w);
}

.rt-05__row--off {
  color: #6b6b6b;
}

.rt-05__row--off .rt-05__ic {
  opacity: 0.45;
}

.rt-05__ic {
  inline-size: 20px;
  block-size: 16px;
  background: var(--rt-05-k);
  clip-path: polygon(0 18%, 40% 18%, 48% 4%, 100% 4%, 100% 100%, 0 100%);
}

.rt-05__ic--doc {
  clip-path: polygon(0 0, 72% 0, 100% 26%, 100% 100%, 0 100%);
  inline-size: 16px;
}

.rt-05__nm {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.rt-05__sz {
  font-family: var(--rt-05-mono);
  font-size: 0.75rem;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.rt-05__dt {
  display: none;
  font-family: var(--rt-05-mono);
  font-size: 0.75rem;
  white-space: nowrap;
}

.rt-05__foot {
  display: flex;
  align-items: stretch;
  border-block-start: 1px solid var(--rt-05-k);
  min-inline-size: 0;
}

.rt-05__scroll {
  flex: 1 1 auto;
  min-inline-size: 0;
  min-block-size: 20px;
  background-color: var(--rt-05-w);
  background-image: repeating-conic-gradient(#8a8a8a 0% 25%, var(--rt-05-w) 0% 50%);
  background-size: 2px 2px;
  display: flex;
  align-items: center;
  padding: 2px;
}

.rt-05__thumb {
  display: block;
  inline-size: 38%;
  block-size: 14px;
  background: var(--rt-05-w);
  border: 1px solid var(--rt-05-k);
}

.rt-05__grow {
  inline-size: var(--rt-05-hit);
  block-size: var(--rt-05-hit);
  flex: none;
  padding: 0;
  border: 0;
  border-inline-start: 1px solid var(--rt-05-k);
  background: var(--rt-05-w);
  cursor: nwse-resize;
  display: grid;
  place-items: center;
}

.rt-05__grow:focus-visible {
  outline: 2px solid var(--rt-05-acc);
  outline-offset: -3px;
}

.rt-05__grow-in {
  inline-size: 15px;
  block-size: 15px;
  border: 1px solid var(--rt-05-k);
  background: linear-gradient(135deg, rgba(0,0,0,0) 48%, var(--rt-05-k) 48% 56%, rgba(0,0,0,0) 56%), linear-gradient(135deg, rgba(0,0,0,0) 68%, var(--rt-05-k) 68% 76%, rgba(0,0,0,0) 76%), var(--rt-05-w);
}

.rt-05__win--small {
  max-inline-size: 30rem;
}

.rt-05__note {
  padding: 0.9rem 0.85rem;
  min-inline-size: 0;
}

.rt-05__note p {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.55;
  text-wrap: pretty;
  min-inline-size: 0;
}

@media (min-width: 34rem) {
  .rt-05__row {
    grid-template-columns: 28px minmax(0, 1fr) 5.5rem 7rem;
  }

  .rt-05__dt {
    display: block;
  }
}

@media (min-width: 60rem) {
  .rt-05__stage {
    grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr);
  }
}
```
