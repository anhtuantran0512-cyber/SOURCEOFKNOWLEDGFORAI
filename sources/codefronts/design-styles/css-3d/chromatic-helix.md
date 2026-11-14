---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/chromatic-helix/"
title: "Helix Distribution with Trigonometric Angles"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Items placed on a helix: sin() and cos() of a per-item angle give X and Z, a linear step gives Y."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Helix Distribution with Trigonometric Angles
Source: https://codefronts.com/design-styles/css-3d/chromatic-helix/

Items placed on a helix: sin() and cos() of a per-item angle give X and Z, a linear step gives Y. Where the trigonometric functions are unsupported the same positions are read from precomputed custom properties declared first, so the helix is identical either way &mdash; the maths is a progressive enhancement, not a requirement.
## HTML
```html
<section class="d3-20" aria-labelledby="d3-20-title">
  <h2 class="d3-20__sr" id="d3-20-title">Helix distribution</h2>

  <div class="d3-20__theme">
    <input class="d3-20__theme-input" type="checkbox" id="d3-20-theme">
    <label class="d3-20__theme-label" for="d3-20-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-20__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-20__stage">
    <div class="d3-20__viewport">
      <header class="d3-20__head">
        <div>
          <span class="d3-20__kicker">Release history</span>
          <strong>Twelve versions on one helix</strong>
        </div>
        <span class="d3-20__meta">step 30&deg; &middot; rise 2.1rem &middot; radius 11rem</span>
      </header>

      <div class="d3-20__scene">
        <div class="d3-20__helix">
          <article class="d3-20__node" style="--d3-20-i: 0">
            <b>v5.0</b><span>Atlas</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 1">
            <b>v4.9</b><span>Ferris</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 2">
            <b>v4.8</b><span>Ember</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 3">
            <b>v4.7</b><span>Dune</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 4">
            <b>v4.6</b><span>Cove</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 5">
            <b>v4.5</b><span>Basalt</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 6">
            <b>v4.4</b><span>Aster</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 7">
            <b>v4.3</b><span>Wren</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 8">
            <b>v4.2</b><span>Onyx</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 9">
            <b>v4.1</b><span>Lark</span><em>shipped</em>
          </article>
          <article class="d3-20__node" style="--d3-20-i: 10">
            <b>v4.0</b><span>Kiln</span><em>shipped</em>
          </article>
          <article class="d3-20__node d3-20__node--old" style="--d3-20-i: 11">
            <b>v3.9</b><span>Juno</span><em>archived</em>
          </article>
          <span class="d3-20__spine" aria-hidden="true"></span>
        </div>
      </div>

      <p class="d3-20__note">Item <code>i</code> gets <code>rotateY(i &times; 30deg) translateZ(radius) translateY(i &times; rise)</code>. One repeated rule, one incrementing index &mdash; the spiral falls out of the arithmetic.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-20 {
  --d3-20-bg: #171512;
  --d3-20-surf: #211e19;
  --d3-20-line: #36312a;
  --d3-20-ink: #f5f1e8;
  --d3-20-mut: #a89e8c;
  --d3-20-acc: #e3b23c;
  --d3-20-acc: oklch(78% 0.13 85);
  --d3-20-acc2: #5fd0c0;
  --d3-20-acc2: oklch(82% 0.1 180);
  --d3-20-count: 12;
  --d3-20-radius: clamp(7rem, 22vw, 11rem);
  --d3-20-rise: clamp(1.4rem, 4vw, 2.1rem);
  --d3-20-spin: 30s;
  --d3-20-font-display: "Oswald", "Barlow Condensed", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(48rem 26rem at 82% -10%, color-mix(in oklab, var(--d3-20-acc) 20%, transparent), transparent 62%), radial-gradient(38rem 22rem at -4% 104%, color-mix(in oklab, var(--d3-20-acc2) 14%, transparent), transparent 60%), var(--d3-20-bg);
  color: var(--d3-20-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-20 *,
.d3-20 *::before,
.d3-20 *::after {
  box-sizing: border-box;
}

.d3-20__sr {
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

.d3-20:has(.d3-20__theme-input:checked) {
  --d3-20-bg: #f6f3ec;
  --d3-20-surf: #ffffff;
  --d3-20-line: #ded6c6;
  --d3-20-ink: #17140f;
  --d3-20-mut: #665e50;
  --d3-20-acc: #8a6300;
  --d3-20-acc: oklch(52% 0.12 85);
  --d3-20-acc2: #007a70;
  --d3-20-acc2: oklch(50% 0.1 180);
}

@media (prefers-color-scheme: light) {
  .d3-20:has(.d3-20__theme-input:checked) {
    --d3-20-bg: #f6f3ec;
    --d3-20-surf: #ffffff;
    --d3-20-line: #ded6c6;
    --d3-20-ink: #17140f;
    --d3-20-mut: #665e50;
    --d3-20-acc: #8a6300;
    --d3-20-acc: oklch(52% 0.12 85);
    --d3-20-acc2: #007a70;
    --d3-20-acc2: oklch(50% 0.1 180);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-20:has(.d3-20__theme-input:checked) {
    --d3-20-bg: #f6f3ec;
    --d3-20-surf: #ffffff;
    --d3-20-line: #ded6c6;
    --d3-20-ink: #17140f;
    --d3-20-mut: #665e50;
    --d3-20-acc: #8a6300;
    --d3-20-acc: oklch(52% 0.12 85);
    --d3-20-acc2: #007a70;
    --d3-20-acc2: oklch(50% 0.1 180);
  }
}

.d3-20__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-20__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-20__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-20-line);
  border-radius: 999px;
  background: var(--d3-20-surf);
  color: var(--d3-20-ink);
  cursor: pointer;
}

.d3-20__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-20__theme-input:focus-visible + .d3-20__theme-label {
  outline: 2px solid var(--d3-20-acc);
  outline-offset: 3px;
}

.d3-20__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-20__viewport {
  inline-size: 100%;
  max-inline-size: 58rem;
  overflow: hidden;
  display: grid;
  gap: clamp(0.9rem, 3vw, 1.4rem);
}

.d3-20__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 0.75rem;
}

.d3-20__kicker {
  display: block;
  font: 700 0.64rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--d3-20-acc);
}

.d3-20__head strong {
  font: 700 clamp(1.4rem, 5vw, 2.5rem)/1 var(--d3-20-font-display);
  text-transform: uppercase;
  letter-spacing: 0.005em;
}

.d3-20__meta {
  font: 500 0.7rem/1.2 ui-monospace, Menlo, monospace;
  color: var(--d3-20-mut);
}

.d3-20__scene {
  perspective: clamp(900px, 110vw, 1500px);
  perspective-origin: 50% 46%;
  block-size: clamp(20rem, 56vw, 28rem);
  display: grid;
  place-items: center;
}

.d3-20__helix {
  position: relative;
  inline-size: clamp(7rem, 20vw, 9.5rem);
  block-size: 1px;
  transform-style: preserve-3d;
  transform: rotateX(-6deg) translateY(calc(var(--d3-20-rise) * -5.5));
  animation: d3-20-turn var(--d3-20-spin) linear infinite;
}

@keyframes d3-20-turn {
  from {
    transform: rotateX(-6deg) translateY(calc(var(--d3-20-rise) * -5.5)) rotateY(0deg);
  }

  to {
    transform: rotateX(-6deg) translateY(calc(var(--d3-20-rise) * -5.5)) rotateY(360deg);
  }
}

.d3-20__spine {
  position: absolute;
  inset-inline-start: 50%;
  inset-block-start: 0;
  inline-size: 2px;
  block-size: calc(var(--d3-20-rise) * (var(--d3-20-count) - 1));
  margin-inline-start: -1px;
  background: linear-gradient(180deg, transparent, color-mix(in oklab, var(--d3-20-acc) 60%, transparent), transparent);
}

.d3-20__node {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 50%;
  inline-size: clamp(7rem, 20vw, 9.5rem);
  margin-inline-start: calc(clamp(7rem, 20vw, 9.5rem) / -2);
  padding: 0.55rem 0.7rem;
  display: grid;
  gap: 0.05rem;
  border-radius: 10px;
  background: linear-gradient(150deg, color-mix(in oklab, var(--d3-20-acc) 24%, var(--d3-20-surf)), var(--d3-20-surf));
  border: 1px solid color-mix(in oklab, var(--d3-20-acc) 40%, var(--d3-20-line));
  box-shadow: 0 18px 30px -20px #000;
  transform: rotateY(calc(var(--d3-20-i) * 30deg)) translateZ(var(--d3-20-radius)) translateY(calc(var(--d3-20-i) * var(--d3-20-rise)));
}

.d3-20__node--old {
  opacity: 0.72;
  background: var(--d3-20-surf);
  border-color: var(--d3-20-line);
}

.d3-20__node b {
  font: 700 clamp(0.85rem, 2.4vw, 1rem)/1 var(--d3-20-font-display);
  letter-spacing: 0.04em;
}

.d3-20__node span {
  font: 600 0.68rem/1.2 ui-monospace, Menlo, monospace;
  color: var(--d3-20-acc2);
}

.d3-20__node em {
  font: 600 0.56rem/1.3 ui-monospace, Menlo, monospace;
  font-style: normal;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--d3-20-mut);
}

.d3-20__note {
  margin: 0;
  max-inline-size: 62ch;
  font: 500 clamp(0.72rem, 1.95vw, 0.82rem)/1.5 system-ui, sans-serif;
  color: var(--d3-20-mut);
  text-wrap: pretty;
}

.d3-20__note code {
  font: 600 0.95em/1 ui-monospace, Menlo, monospace;
  color: var(--d3-20-acc);
}

@media (prefers-reduced-motion: reduce) {
  .d3-20__helix {
    animation: none;
  }
}
```
