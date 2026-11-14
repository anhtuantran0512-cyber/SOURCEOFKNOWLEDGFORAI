---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/pixel-art-scaling-with-image-rendering/"
title: "Pixel Art Scaling with Image Rendering"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "The same 12&times;12 sprite rendered at 1&times;, 4&times; and 8&times; with default smoothing on the left and image-rendering: pixelated on the right, both…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pixel Art Scaling with Image Rendering
Source: https://codefronts.com/design-styles/css-retro-designs/pixel-art-scaling-with-image-rendering/

The same 12&times;12 sprite rendered at 1&times;, 4&times; and 8&times; with default smoothing on the left and image-rendering: pixelated on the right, both sides labelled. It also shows the two things people get wrong: a non-integer scale factor reintroduces blur even with the property set, and the property does nothing at all to a shape drawn in CSS rather than sampled from a bitmap.
## HTML
```html
<section class="rt-02" aria-labelledby="rt-02-title">
  <h2 class="rt-02__sr" id="rt-02-title">Pixel art scaling comparison</h2>

  <div class="rt-02__theme">
    <input class="rt-02__theme-input" type="checkbox" id="rt-02-theme">
    <label class="rt-02__theme-label" for="rt-02-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-02__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-02__stage">
    <header class="rt-02__head">
      <p class="rt-02__kicker">Source bitmap &middot; 12 &times; 12 px &middot; 5-colour</p>
      <h3 class="rt-02__h">Nearest-neighbour against the default sampler</h3>
    </header>

    <div class="rt-02__board">
      <article class="rt-02__col" aria-labelledby="rt-02-a">
        <h4 class="rt-02__col-h" id="rt-02-a"><span class="rt-02__pill rt-02__pill--off">image-rendering: auto</span> smoothed</h4>
        <ul class="rt-02__row">
          <li class="rt-02__cell"><span class="rt-02__scale">1&times;</span><img class="rt-02__img rt-02__img--1" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at original size, smoothed"></li>
          <li class="rt-02__cell"><span class="rt-02__scale">4&times;</span><img class="rt-02__img rt-02__img--4" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at four times size, smoothed"></li>
          <li class="rt-02__cell"><span class="rt-02__scale">8&times;</span><img class="rt-02__img rt-02__img--8" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at eight times size, smoothed"></li>
        </ul>
      </article>

      <article class="rt-02__col rt-02__col--sharp" aria-labelledby="rt-02-b">
        <h4 class="rt-02__col-h" id="rt-02-b"><span class="rt-02__pill rt-02__pill--on">image-rendering: pixelated</span> nearest-neighbour</h4>
        <ul class="rt-02__row">
          <li class="rt-02__cell"><span class="rt-02__scale">1&times;</span><img class="rt-02__img rt-02__img--1" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at original size, nearest-neighbour"></li>
          <li class="rt-02__cell"><span class="rt-02__scale">4&times;</span><img class="rt-02__img rt-02__img--4" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at four times size, nearest-neighbour"></li>
          <li class="rt-02__cell"><span class="rt-02__scale">8&times;</span><img class="rt-02__img rt-02__img--8" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at eight times size, nearest-neighbour"></li>
        </ul>
      </article>
    </div>

    <div class="rt-02__traps">
      <article class="rt-02__trap" aria-labelledby="rt-02-t1">
        <h4 class="rt-02__trap-h" id="rt-02-t1">Trap 1 &middot; fractional scale</h4>
        <div class="rt-02__trap-pair">
          <figure class="rt-02__fig">
            <img class="rt-02__img rt-02__img--8 rt-02__img--sharp" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite scaled by a whole number">
            <figcaption>8.0&times; &mdash; integer, clean</figcaption>
          </figure>
          <figure class="rt-02__fig">
            <img class="rt-02__img rt-02__img--bad rt-02__img--sharp" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite scaled by a fractional factor">
            <figcaption>5.7&times; &mdash; fractional, resampled</figcaption>
          </figure>
        </div>
        <p class="rt-02__note">Both have <code>image-rendering: pixelated</code>. The property cannot invent a fractional device pixel.</p>
      </article>

      <article class="rt-02__trap" aria-labelledby="rt-02-t2">
        <h4 class="rt-02__trap-h" id="rt-02-t2">Trap 2 &middot; CSS-drawn shapes</h4>
        <div class="rt-02__trap-pair">
          <figure class="rt-02__fig">
            <span class="rt-02__disc" aria-hidden="true"></span>
            <figcaption>border-radius disc &mdash; property ignored</figcaption>
          </figure>
          <figure class="rt-02__fig">
            <span class="rt-02__stepped" aria-hidden="true"></span>
            <figcaption>stepped box-shadow &mdash; real pixels</figcaption>
          </figure>
        </div>
        <p class="rt-02__note"><code>image-rendering</code> is a hint to the image sampler. A painted shape never reaches it.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-02 {
  --rt-02-px: 4px;
  --rt-02-bad: 5.7;
  --rt-02-sans: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --rt-02-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --rt-02-bg: #efece4;
  --rt-02-bg: oklch(94% 0.011 90);
  --rt-02-surface: #fffdf8;
  --rt-02-surface: oklch(99% 0.006 90);
  --rt-02-cell: #e4e0d5;
  --rt-02-cell: oklch(90% 0.013 90);
  --rt-02-ink: #191712;
  --rt-02-ink: oklch(19% 0.01 80);
  --rt-02-ink-2: #555044;
  --rt-02-ink-2: oklch(45% 0.015 80);
  --rt-02-line: #b8b2a3;
  --rt-02-line: oklch(77% 0.017 90);
  --rt-02-acc: #b4321e;
  --rt-02-acc: oklch(50% 0.17 32);
  --rt-02-ok: #1c6b3a;
  --rt-02-ok: oklch(47% 0.12 152);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-02-bg);
  color: var(--rt-02-ink);
  font-family: var(--rt-02-sans);
  -webkit-text-size-adjust: 100%;
}

.rt-02 *,
.rt-02 *::before,
.rt-02 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-02 {
    --rt-02-bg: #16150f;
    --rt-02-bg: oklch(19% 0.008 90);
    --rt-02-surface: #201e17;
    --rt-02-surface: oklch(25% 0.01 90);
    --rt-02-cell: #2b291f;
    --rt-02-cell: oklch(30% 0.012 90);
    --rt-02-ink: #f3f0e8;
    --rt-02-ink: oklch(96% 0.006 90);
    --rt-02-ink-2: #aca597;
    --rt-02-ink-2: oklch(74% 0.012 90);
    --rt-02-line: #454134;
    --rt-02-line: oklch(38% 0.014 90);
    --rt-02-acc: #ff8f74;
    --rt-02-acc: oklch(76% 0.13 36);
    --rt-02-ok: #6fd396;
    --rt-02-ok: oklch(78% 0.13 152);
  }
}

.rt-02[data-theme="dark"],
.rt-02:has(.rt-02__theme-input:checked) {
  --rt-02-bg: #16150f;
  --rt-02-bg: oklch(19% 0.008 90);
  --rt-02-surface: #201e17;
  --rt-02-surface: oklch(25% 0.01 90);
  --rt-02-cell: #2b291f;
  --rt-02-cell: oklch(30% 0.012 90);
  --rt-02-ink: #f3f0e8;
  --rt-02-ink: oklch(96% 0.006 90);
  --rt-02-ink-2: #aca597;
  --rt-02-ink-2: oklch(74% 0.012 90);
  --rt-02-line: #454134;
  --rt-02-line: oklch(38% 0.014 90);
  --rt-02-acc: #ff8f74;
  --rt-02-acc: oklch(76% 0.13 36);
  --rt-02-ok: #6fd396;
  --rt-02-ok: oklch(78% 0.13 152);
}

@media (prefers-color-scheme: light) {
  .rt-02:has(.rt-02__theme-input:checked) {
    --rt-02-bg: #16150f;
    --rt-02-bg: oklch(19% 0.008 90);
    --rt-02-surface: #201e17;
    --rt-02-surface: oklch(25% 0.01 90);
    --rt-02-cell: #2b291f;
    --rt-02-cell: oklch(30% 0.012 90);
    --rt-02-ink: #f3f0e8;
    --rt-02-ink: oklch(96% 0.006 90);
    --rt-02-ink-2: #aca597;
    --rt-02-ink-2: oklch(74% 0.012 90);
    --rt-02-line: #454134;
    --rt-02-line: oklch(38% 0.014 90);
    --rt-02-acc: #ff8f74;
    --rt-02-acc: oklch(76% 0.13 36);
    --rt-02-ok: #6fd396;
    --rt-02-ok: oklch(78% 0.13 152);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-02:has(.rt-02__theme-input:checked) {
    --rt-02-bg: #efece4;
    --rt-02-bg: oklch(94% 0.011 90);
    --rt-02-surface: #fffdf8;
    --rt-02-surface: oklch(99% 0.006 90);
    --rt-02-cell: #e4e0d5;
    --rt-02-cell: oklch(90% 0.013 90);
    --rt-02-ink: #191712;
    --rt-02-ink: oklch(19% 0.01 80);
    --rt-02-ink-2: #555044;
    --rt-02-ink-2: oklch(45% 0.015 80);
    --rt-02-line: #b8b2a3;
    --rt-02-line: oklch(77% 0.017 90);
    --rt-02-acc: #b4321e;
    --rt-02-acc: oklch(50% 0.17 32);
    --rt-02-ok: #1c6b3a;
    --rt-02-ok: oklch(47% 0.12 152);
  }
}

.rt-02__sr {
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

.rt-02__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-02__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-02__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-02-line);
  border-radius: 50%;
  background: var(--rt-02-surface);
  color: var(--rt-02-ink-2);
  cursor: pointer;
}

.rt-02__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-02__theme-input:focus-visible + .rt-02__theme-label {
  outline: 2px solid var(--rt-02-acc);
  outline-offset: 2px;
}

.rt-02__stage {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.85rem, 0.5rem + 2vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: clamp(1.5rem, 1rem + 2vw, 2.5rem);
}

.rt-02__head {
  min-inline-size: 0;
  display: grid;
  gap: 0.4rem;
}

.rt-02__kicker {
  margin: 0;
  font-family: var(--rt-02-mono);
  font-size: 0.7rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--rt-02-ink-2);
}

.rt-02__h {
  margin: 0;
  font-size: clamp(1.25rem, 1rem + 1.6vw, 2rem);
  line-height: 1.12;
  letter-spacing: -0.02em;
  font-weight: 650;
  text-wrap: balance;
  min-inline-size: 0;
}

.rt-02__board {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1rem;
}

.rt-02__col {
  min-inline-size: 0;
  background: var(--rt-02-surface);
  border: 1px solid var(--rt-02-line);
  border-radius: 4px;
  padding: clamp(0.85rem, 0.6rem + 1vw, 1.25rem);
  display: grid;
  gap: 0.9rem;
  align-content: start;
}

.rt-02__col-h {
  margin: 0;
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--rt-02-ink-2);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.45rem;
  min-inline-size: 0;
}

.rt-02__pill {
  font-family: var(--rt-02-mono);
  font-size: 0.68rem;
  letter-spacing: 0.01em;
  padding: 0.2rem 0.45rem;
  border-radius: 2px;
  border: 1px solid currentColor;
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.rt-02__pill--off {
  color: var(--rt-02-acc);
}

.rt-02__pill--on {
  color: var(--rt-02-ok);
}

.rt-02__row {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-items: flex-end;
}

.rt-02__cell {
  position: relative;
  min-inline-size: 0;
  flex: none;
  background: var(--rt-02-cell);
  border: 1px solid var(--rt-02-line);
  padding: 0.75rem;
  display: grid;
  place-items: center;
  gap: 0.4rem;
  background-image: linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25% 75%, rgba(0,0,0,0.05) 75%), linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25% 75%, rgba(0,0,0,0.05) 75%);
  background-size: 12px 12px;
  background-position: 0 0, 6px 6px;
}

.rt-02__scale {
  font-family: var(--rt-02-mono);
  font-size: 0.65rem;
  color: var(--rt-02-ink-2);
  letter-spacing: 0.08em;
}

.rt-02__img {
  display: block;
  image-rendering: auto;
}

.rt-02__img--1 {
  inline-size: 12px;
  block-size: 12px;
}

.rt-02__img--4 {
  inline-size: calc(12 * var(--rt-02-px));
  block-size: calc(12 * var(--rt-02-px));
}

.rt-02__img--8 {
  inline-size: calc(24 * var(--rt-02-px));
  block-size: calc(24 * var(--rt-02-px));
}

.rt-02__img--bad {
  inline-size: calc(12 * 1px * var(--rt-02-bad) * 1.4);
  block-size: calc(12 * 1px * var(--rt-02-bad) * 1.4);
}

.rt-02__col--sharp .rt-02__img,
.rt-02__img--sharp {
  image-rendering: crisp-edges;
  image-rendering: pixelated;
}

.rt-02__traps {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1rem;
}

.rt-02__trap {
  min-inline-size: 0;
  background: var(--rt-02-surface);
  border: 1px solid var(--rt-02-line);
  border-radius: 4px;
  padding: clamp(0.85rem, 0.6rem + 1vw, 1.25rem);
  display: grid;
  gap: 0.85rem;
  align-content: start;
}

.rt-02__trap-h {
  margin: 0;
  font-family: var(--rt-02-mono);
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rt-02-acc);
}

.rt-02__trap-pair {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.rt-02__fig {
  margin: 0;
  min-inline-size: 0;
  display: grid;
  justify-items: center;
  gap: 0.5rem;
  padding: 0.85rem;
  background: var(--rt-02-cell);
  border: 1px solid var(--rt-02-line);
}

.rt-02__fig figcaption {
  font-family: var(--rt-02-mono);
  font-size: 0.65rem;
  color: var(--rt-02-ink-2);
  text-align: center;
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.rt-02__disc {
  inline-size: 96px;
  block-size: 96px;
  border-radius: 50%;
  background: #2ce8f5;
  border: 4px solid #0b0f14;
  image-rendering: pixelated;
}

.rt-02__stepped {
  inline-size: 8px;
  block-size: 8px;
  margin: 44px;
  background: transparent;
  box-shadow: -24px -40px 0 0 #0b0f14, -16px -40px 0 0 #0b0f14, -8px -40px 0 0 #0b0f14, 0 -40px 0 0 #0b0f14, 8px -40px 0 0 #0b0f14, -40px -32px 0 0 #0b0f14, -32px -32px 0 0 #2ce8f5, -24px -32px 0 0 #2ce8f5, -16px -32px 0 0 #2ce8f5, -8px -32px 0 0 #2ce8f5, 0 -32px 0 0 #2ce8f5, 8px -32px 0 0 #2ce8f5, 16px -32px 0 0 #0b0f14, -48px -24px 0 0 #0b0f14, -40px -24px 0 0 #2ce8f5, -32px -24px 0 0 #2ce8f5, -24px -24px 0 0 #2ce8f5, -16px -24px 0 0 #2ce8f5, -8px -24px 0 0 #2ce8f5, 0 -24px 0 0 #2ce8f5, 8px -24px 0 0 #2ce8f5, 16px -24px 0 0 #2ce8f5, 24px -24px 0 0 #0b0f14, -48px -16px 0 0 #0b0f14, -40px -16px 0 0 #2ce8f5, -32px -16px 0 0 #2ce8f5, -24px -16px 0 0 #2ce8f5, -16px -16px 0 0 #2ce8f5, -8px -16px 0 0 #2ce8f5, 0 -16px 0 0 #2ce8f5, 8px -16px 0 0 #2ce8f5, 16px -16px 0 0 #2ce8f5, 24px -16px 0 0 #0b0f14, -48px -8px 0 0 #0b0f14, -40px -8px 0 0 #2ce8f5, -32px -8px 0 0 #2ce8f5, -24px -8px 0 0 #2ce8f5, -16px -8px 0 0 #2ce8f5, -8px -8px 0 0 #2ce8f5, 0 -8px 0 0 #2ce8f5, 8px -8px 0 0 #2ce8f5, 16px -8px 0 0 #2ce8f5, 24px -8px 0 0 #0b0f14, -48px 0 0 0 #0b0f14, -40px 0 0 0 #2ce8f5, -32px 0 0 0 #2ce8f5, -24px 0 0 0 #2ce8f5, -16px 0 0 0 #2ce8f5, -8px 0 0 0 #2ce8f5, 0 0 0 0 #2ce8f5, 8px 0 0 0 #2ce8f5, 16px 0 0 0 #2ce8f5, 24px 0 0 0 #0b0f14, -40px 8px 0 0 #0b0f14, -32px 8px 0 0 #2ce8f5, -24px 8px 0 0 #2ce8f5, -16px 8px 0 0 #2ce8f5, -8px 8px 0 0 #2ce8f5, 0 8px 0 0 #2ce8f5, 8px 8px 0 0 #2ce8f5, 16px 8px 0 0 #0b0f14, -32px 16px 0 0 #0b0f14, -24px 16px 0 0 #0b0f14, -16px 16px 0 0 #0b0f14, -8px 16px 0 0 #0b0f14, 0 16px 0 0 #0b0f14, 8px 16px 0 0 #0b0f14;
}

.rt-02__note {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--rt-02-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-02__note code,
.rt-02__col-h code {
  font-family: var(--rt-02-mono);
  font-size: 0.92em;
  background: var(--rt-02-cell);
  padding: 0.05em 0.3em;
  border-radius: 2px;
}

@media (min-width: 52rem) {
  .rt-02__board {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .rt-02__traps {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```
