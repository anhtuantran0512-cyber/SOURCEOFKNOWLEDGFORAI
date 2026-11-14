---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/z-fighting-on-coplanar-3d-surfaces/"
title: "Z Fighting on Coplanar 3D Surfaces"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Two surfaces at the same Z depth give the renderer no way to decide which is in front, so it picks per frame and the result flickers &mdash; often only on…"
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Z Fighting on Coplanar 3D Surfaces
Source: https://codefronts.com/design-styles/css-3d/z-fighting-on-coplanar-3d-surfaces/

Two surfaces at the same Z depth give the renderer no way to decide which is in front, so it picks per frame and the result flickers &mdash; often only on some GPUs, which makes it maddening to reproduce. The failure is shown next to the three fixes that actually work: a sub-pixel Z separation, z-index in a flattened context, and restructuring so nothing is coplanar.
## HTML
```html
<section class="d3-10" aria-labelledby="d3-10-title">
  <h2 class="d3-10__sr" id="d3-10-title">Z fighting on coplanar surfaces</h2>

  <div class="d3-10__theme">
    <input class="d3-10__theme-input" type="checkbox" id="d3-10-theme">
    <label class="d3-10__theme-label" for="d3-10-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-10__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-10__stage">
    <div class="d3-10__viewport">
      <header class="d3-10__head">
        <span class="d3-10__kicker">Late Show &mdash; poster wall</span>
        <strong>The stamp that flickers</strong>
        <p>Identical markup on both, one property apart. On the left the stamp sits at exactly the face's depth, so nothing decides which draws in front and the seam stitches or flickers frame to frame &mdash; how badly depends on the GPU. On the right fourteen pixels of clearance make the answer deterministic everywhere, and the stamp picks up a shadow and its own parallax as the poster turns.</p>
      </header>

      <div class="d3-10__pair">
        <article class="d3-10__slot">
          <div class="d3-10__scene">
            <div class="d3-10__poster d3-10__poster--fight">
              <span class="d3-10__face" aria-hidden="true"></span>
              <span class="d3-10__night">Fri 12 Sep</span>
              <b class="d3-10__act">Vela<br>Sound</b>
              <span class="d3-10__venue">The Foundry &middot; 21:00</span>
              <span class="d3-10__stamp">Sold out</span>
            </div>
          </div>
          <p class="d3-10__cap"><b class="d3-10__badge d3-10__badge--no">Fighting</b> same depth as the face, <code>translateZ(0)</code></p>
        </article>

        <article class="d3-10__slot">
          <div class="d3-10__scene">
            <div class="d3-10__poster d3-10__poster--fixed">
              <span class="d3-10__face" aria-hidden="true"></span>
              <span class="d3-10__night">Sat 13 Sep</span>
              <b class="d3-10__act">Halden<br>Trio</b>
              <span class="d3-10__venue">The Foundry &middot; 20:30</span>
              <span class="d3-10__stamp">Sold out</span>
            </div>
          </div>
          <p class="d3-10__cap"><b class="d3-10__badge d3-10__badge--ok">Resolved</b> lifted clear of it, <code>translateZ(14px)</code></p>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-10 {
  --d3-10-bg: #000000;
  --d3-10-surf: #0c0c0e;
  --d3-10-line: #23232a;
  --d3-10-ink: #f4f4f6;
  --d3-10-mut: #8e8e99;
  --d3-10-acc: #ff2d4f;
  --d3-10-acc: oklch(64% 0.24 22);
  --d3-10-acc2: #ffe14d;
  --d3-10-acc2: oklch(90% 0.16 100);
  --d3-10-ok: #33d17a;
  --d3-10-ok: oklch(78% 0.16 152);
  --d3-10-font-display: "Archivo Narrow", "Arial Narrow", "Oswald", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(46rem 24rem at 78% -12%, color-mix(in oklab, var(--d3-10-acc) 24%, transparent), transparent 60%), var(--d3-10-bg);
  color: var(--d3-10-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-10 *,
.d3-10 *::before,
.d3-10 *::after {
  box-sizing: border-box;
}

.d3-10__sr {
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

.d3-10:has(.d3-10__theme-input:checked) {
  --d3-10-bg: #f4f4f6;
  --d3-10-surf: #ffffff;
  --d3-10-line: #d9d9e0;
  --d3-10-ink: #0b0b0d;
  --d3-10-mut: #5d5d68;
  --d3-10-acc: #c40024;
  --d3-10-acc: oklch(48% 0.22 22);
  --d3-10-acc2: #8a6a00;
  --d3-10-acc2: oklch(56% 0.13 100);
  --d3-10-ok: #067a45;
  --d3-10-ok: oklch(50% 0.14 152);
}

@media (prefers-color-scheme: light) {
  .d3-10:has(.d3-10__theme-input:checked) {
    --d3-10-bg: #f4f4f6;
    --d3-10-surf: #ffffff;
    --d3-10-line: #d9d9e0;
    --d3-10-ink: #0b0b0d;
    --d3-10-mut: #5d5d68;
    --d3-10-acc: #c40024;
    --d3-10-acc: oklch(48% 0.22 22);
    --d3-10-acc2: #8a6a00;
    --d3-10-acc2: oklch(56% 0.13 100);
    --d3-10-ok: #067a45;
    --d3-10-ok: oklch(50% 0.14 152);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-10:has(.d3-10__theme-input:checked) {
    --d3-10-bg: #f4f4f6;
    --d3-10-surf: #ffffff;
    --d3-10-line: #d9d9e0;
    --d3-10-ink: #0b0b0d;
    --d3-10-mut: #5d5d68;
    --d3-10-acc: #c40024;
    --d3-10-acc: oklch(48% 0.22 22);
    --d3-10-acc2: #8a6a00;
    --d3-10-acc2: oklch(56% 0.13 100);
    --d3-10-ok: #067a45;
    --d3-10-ok: oklch(50% 0.14 152);
  }
}

.d3-10__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-10__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-10__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-10-line);
  border-radius: 4px;
  background: var(--d3-10-surf);
  color: var(--d3-10-ink);
  cursor: pointer;
}

.d3-10__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-10__theme-input:focus-visible + .d3-10__theme-label {
  outline: 2px solid var(--d3-10-acc);
  outline-offset: 3px;
}

.d3-10__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-10__viewport {
  inline-size: 100%;
  max-inline-size: 58rem;
  overflow: hidden;
  display: grid;
  gap: clamp(1.1rem, 3.5vw, 1.8rem);
}

.d3-10__head {
  display: grid;
  gap: 0.3rem;
  max-inline-size: 44ch;
}

.d3-10__kicker {
  font: 700 0.64rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--d3-10-acc);
}

.d3-10__head strong {
  font: 700 clamp(1.5rem, 5.4vw, 2.7rem)/1 var(--d3-10-font-display);
  letter-spacing: 0.005em;
  text-transform: uppercase;
}

.d3-10__head p {
  margin: 0.2rem 0 0;
  font: 500 clamp(0.74rem, 2vw, 0.85rem)/1.5 system-ui, sans-serif;
  color: var(--d3-10-mut);
  text-wrap: pretty;
}

.d3-10__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  gap: clamp(0.9rem, 3vw, 1.6rem);
}

.d3-10__slot {
  display: grid;
  gap: 0.6rem;
}

.d3-10__scene {
  perspective: 620px;
  perspective-origin: 50% 42%;
  block-size: clamp(15.5rem, 46vw, 22rem);
  display: grid;
  place-items: center;
}

.d3-10__poster {
  position: relative;
  inline-size: min(100%, 13.5rem);
  aspect-ratio: 0.74;
  padding: clamp(0.8rem, 2.6vw, 1.1rem);
  display: grid;
  align-content: space-between;
  transform-style: preserve-3d;
  animation: d3-10-sway 11s ease-in-out infinite;
  color: #fff;
}

.d3-10__face {
  position: absolute;
  inset: 0;
  transform: translateZ(0);
  background: linear-gradient(170deg, #14060a 0%, #2a0710 55%, #470a16 100%);
  border: 1px solid var(--d3-10-line);
  box-shadow: 0 30px 60px -28px #000;
}

.d3-10__night,
.d3-10__act,
.d3-10__venue {
  transform: translateZ(3px);
}

@keyframes d3-10-sway {
  0%,
    100% {
    transform: rotateX(11deg) rotateY(-27deg);
  }

  50% {
    transform: rotateX(2deg) rotateY(27deg);
  }
}

.d3-10__night {
  font: 600 0.62rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--d3-10-acc2);
}

.d3-10__act {
  font: 700 clamp(1.4rem, 4.6vw, 2.15rem)/0.92 var(--d3-10-font-display);
  text-transform: uppercase;
  letter-spacing: -0.01em;
}

.d3-10__venue {
  font: 500 0.66rem/1.3 ui-monospace, Menlo, monospace;
  color: rgba(255, 255, 255, 0.68);
}

.d3-10__stamp {
  position: absolute;
  inset-block-start: 68%;
  inset-inline-start: 26%;
  white-space: nowrap;
  padding: 0.3rem 0.7rem;
  border: 3px solid #ff5c74;
  border-radius: 6px;
  color: #ff8595;
  font: 800 clamp(0.72rem, 2.1vw, 0.9rem)/1 var(--d3-10-font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  transform: rotate(-11deg);
  background: #1b0308;
}

.d3-10__poster--fixed .d3-10__stamp {
  transform: translateZ(14px) rotate(-11deg);
  box-shadow: 0 12px 24px -6px #000;
}

.d3-10__cap {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.4rem;
  font: 500 clamp(0.72rem, 1.95vw, 0.8rem)/1.3 system-ui, sans-serif;
  color: var(--d3-10-mut);
}

.d3-10__cap code {
  font: 600 0.95em/1 ui-monospace, Menlo, monospace;
  color: var(--d3-10-ink);
}

.d3-10__badge {
  padding: 0.18rem 0.5rem;
  border-radius: 3px;
  font: 800 0.62rem/1.5 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #000;
}

.d3-10__badge--no {
  background: var(--d3-10-acc);
  color: #fff;
}

.d3-10__badge--ok {
  background: var(--d3-10-ok);
}

@media (prefers-reduced-motion: reduce) {
  .d3-10__poster {
    animation: none;
    transform: rotateX(9deg) rotateY(-24deg);
  }
}
```
