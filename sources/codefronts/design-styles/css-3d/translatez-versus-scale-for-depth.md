---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/translatez-versus-scale-for-depth/"
title: "TranslateZ Versus Scale for Depth"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Both make an element look bigger and they are not interchangeable."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: TranslateZ Versus Scale for Depth
Source: https://codefronts.com/design-styles/css-3d/translatez-versus-scale-for-depth/

Both make an element look bigger and they are not interchangeable. scale multiplies rendered size on a flat plane; translateZ moves the element towards the camera so it grows because it is nearer &mdash; and parallaxes correctly against its neighbours. Two panels matched to identical apparent size, then the camera moves and the difference is unmistakable.
## HTML
```html
<section class="d3-09" aria-labelledby="d3-09-title">
  <h2 class="d3-09__sr" id="d3-09-title">TranslateZ versus scale</h2>

  <div class="d3-09__theme">
    <input class="d3-09__theme-input" type="checkbox" id="d3-09-theme">
    <label class="d3-09__theme-label" for="d3-09-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-09__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-09__stage">
    <div class="d3-09__viewport">
      <header class="d3-09__head">
        <span class="d3-09__kicker">Quarterly &mdash; cover study</span>
        <strong>Same final size.<br>Only one of them moved.</strong>
      </header>

      <div class="d3-09__pair">
        <figure class="d3-09__slot">
          <div class="d3-09__scene">
            <article class="d3-09__cover d3-09__cover--z">
              <span class="d3-09__issue">Issue 14</span>
              <b>Depth</b>
              <span class="d3-09__strap">A field guide to space in flat media</span>
              <span class="d3-09__rule" aria-hidden="true"></span>
            </article>
          </div>
          <figcaption><b>translateZ</b><code>translateZ(140px)</code><span>Moves through the frustum. Perspective re-projects it, so edges shift and the whole cover parallaxes against the page.</span></figcaption>
        </figure>

        <figure class="d3-09__slot">
          <div class="d3-09__scene">
            <article class="d3-09__cover d3-09__cover--s">
              <span class="d3-09__issue">Issue 14</span>
              <b>Scale</b>
              <span class="d3-09__strap">A field guide to space in flat media</span>
              <span class="d3-09__rule" aria-hidden="true"></span>
            </article>
          </div>
          <figcaption><b>scale</b><code>scale(1.24)</code><span>Stays on the Z&nbsp;=&nbsp;0 plane. It gets bigger, nothing else changes, and the eye reads growth rather than approach.</span></figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-09 {
  --d3-09-bg: #f7f4ef;
  --d3-09-surf: #ffffff;
  --d3-09-line: #e0d8cd;
  --d3-09-ink: #16120f;
  --d3-09-mut: #6b6157;
  --d3-09-acc: #c8106e;
  --d3-09-acc: oklch(52% 0.22 355);
  --d3-09-acc2: #f2a03d;
  --d3-09-acc2: oklch(78% 0.14 62);
  --d3-09-beat: 7s;
  --d3-09-font-display: "Playfair Display", "Iowan Old Style", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(48rem 26rem at 88% -10%, color-mix(in oklab, var(--d3-09-acc) 14%, transparent), transparent 62%), var(--d3-09-bg);
  color: var(--d3-09-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-09 *,
.d3-09 *::before,
.d3-09 *::after {
  box-sizing: border-box;
}

.d3-09__sr {
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

.d3-09:has(.d3-09__theme-input:checked) {
  --d3-09-bg: #14100e;
  --d3-09-surf: #1d1815;
  --d3-09-line: #362e28;
  --d3-09-ink: #f6f1ea;
  --d3-09-mut: #a99c8f;
  --d3-09-acc: #ff77b4;
  --d3-09-acc: oklch(76% 0.16 355);
  --d3-09-acc2: #f8c078;
  --d3-09-acc2: oklch(84% 0.11 62);
}

@media (prefers-color-scheme: dark) {
  .d3-09 {
    --d3-09-bg: #14100e;
    --d3-09-surf: #1d1815;
    --d3-09-line: #362e28;
    --d3-09-ink: #f6f1ea;
    --d3-09-mut: #a99c8f;
    --d3-09-acc: #ff77b4;
    --d3-09-acc: oklch(76% 0.16 355);
    --d3-09-acc2: #f8c078;
    --d3-09-acc2: oklch(84% 0.11 62);
  }

  .d3-09:has(.d3-09__theme-input:checked) {
    --d3-09-bg: #f7f4ef;
    --d3-09-surf: #ffffff;
    --d3-09-line: #e0d8cd;
    --d3-09-ink: #16120f;
    --d3-09-mut: #6b6157;
    --d3-09-acc: #c8106e;
    --d3-09-acc: oklch(52% 0.22 355);
    --d3-09-acc2: #f2a03d;
    --d3-09-acc2: oklch(78% 0.14 62);
  }
}

@media (prefers-color-scheme: light) {
  .d3-09:has(.d3-09__theme-input:checked) {
    --d3-09-bg: #14100e;
    --d3-09-surf: #1d1815;
    --d3-09-line: #362e28;
    --d3-09-ink: #f6f1ea;
    --d3-09-mut: #a99c8f;
    --d3-09-acc: #ff77b4;
    --d3-09-acc: oklch(76% 0.16 355);
    --d3-09-acc2: #f8c078;
    --d3-09-acc2: oklch(84% 0.11 62);
  }
}

.d3-09__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-09__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-09__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-09-line);
  border-radius: 999px;
  background: var(--d3-09-surf);
  color: var(--d3-09-ink);
  cursor: pointer;
}

.d3-09__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-09__theme-input:focus-visible + .d3-09__theme-label {
  outline: 2px solid var(--d3-09-acc);
  outline-offset: 3px;
}

.d3-09__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-09__viewport {
  inline-size: 100%;
  max-inline-size: 60rem;
  overflow: hidden;
  display: grid;
  gap: clamp(1.2rem, 3.5vw, 2rem);
}

.d3-09__head {
  display: grid;
  gap: 0.3rem;
}

.d3-09__kicker {
  font: 700 0.64rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--d3-09-acc);
}

.d3-09__head strong {
  font: 400 clamp(1.5rem, 5.6vw, 2.9rem)/1.05 var(--d3-09-font-display);
  letter-spacing: -0.01em;
}

.d3-09__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: clamp(1rem, 3.5vw, 2rem);
}

.d3-09__slot {
  margin: 0;
  display: grid;
  gap: 0.75rem;
}

.d3-09__scene {
  perspective: 900px;
  perspective-origin: 50% 45%;
  block-size: clamp(14rem, 38vw, 18rem);
  display: grid;
  place-items: center;
  border-block-end: 1px solid var(--d3-09-line);
}

.d3-09__cover {
  inline-size: clamp(8rem, 22vw, 10.5rem);
  aspect-ratio: 0.72;
  padding: clamp(0.7rem, 2.2vw, 1rem);
  display: grid;
  align-content: space-between;
  border-radius: 4px;
  color: #fff;
  background: linear-gradient(165deg, #241023 0%, #3b1230 42%, #7a1147 100%);
  box-shadow: 0 30px 50px -26px rgba(0, 0, 0, 0.65);
  overflow: hidden;
}

.d3-09__cover::before {
  content: "";
  position: absolute;
}

.d3-09__issue {
  font: 600 0.6rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--d3-09-acc2);
}

.d3-09__cover b {
  font: 400 clamp(1.6rem, 5vw, 2.4rem)/0.95 var(--d3-09-font-display);
}

.d3-09__strap {
  font: 500 clamp(0.6rem, 1.7vw, 0.68rem)/1.35 system-ui, sans-serif;
  color: rgba(255, 255, 255, 0.72);
}

.d3-09__rule {
  display: block;
  block-size: 3px;
  inline-size: 42%;
  background: var(--d3-09-acc);
}

.d3-09__cover--z {
  animation: d3-09-dolly var(--d3-09-beat) ease-in-out infinite;
}

.d3-09__cover--s {
  animation: d3-09-swell var(--d3-09-beat) ease-in-out infinite;
}

@keyframes d3-09-dolly {
  0%,
    100% {
    transform: translateZ(0);
  }

  50% {
    transform: translateZ(140px);
  }
}

@keyframes d3-09-swell {
  0%,
    100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.24);
  }
}

.d3-09__slot figcaption {
  display: grid;
  gap: 0.25rem;
}

.d3-09__slot figcaption b {
  font: 700 clamp(0.9rem, 2.4vw, 1.05rem)/1.1 system-ui, sans-serif;
}

.d3-09__slot figcaption code {
  font: 600 0.72rem/1.2 ui-monospace, Menlo, monospace;
  color: var(--d3-09-acc);
}

.d3-09__slot figcaption span {
  font: 500 clamp(0.72rem, 1.95vw, 0.8rem)/1.5 system-ui, sans-serif;
  color: var(--d3-09-mut);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .d3-09__cover--z {
    animation: none;
    transform: translateZ(140px);
  }

  .d3-09__cover--s {
    animation: none;
    transform: scale(1.24);
  }
}
```
