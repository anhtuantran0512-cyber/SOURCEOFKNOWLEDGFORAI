---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/rainbow-neon-text/"
title: "Multi Hue Neon Gradient Glow"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "A glow whose hue shifts across the element, built two ways on the same surface: layered box-shadows in different hues offset around the edges, and a blurred…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi Hue Neon Gradient Glow
Source: https://codefronts.com/design-styles/css-neon/rainbow-neon-text/

A glow whose hue shifts across the element, built two ways on the same surface: layered box-shadows in different hues offset around the edges, and a blurred gradient layer sitting behind the panel. Both are labelled with what they cost and where each one wins.
## HTML
```html
<section class="nn-20" aria-labelledby="nn-20-heading">
  <div class="nn-20__stage">
    <div class="nn-20__theme">
      <input class="nn-20__tin" type="checkbox" id="nn-20-theme">
      <label class="nn-20__tlab" for="nn-20-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-20__head">
      <p class="nn-20__kicker">Two routes to a hue sweep</p>
      <h2 class="nn-20__heading" id="nn-20-heading">A glow that changes colour across the surface</h2>
      <p class="nn-20__sub">Stacked shadows in separate hues, or one blurred gradient layer. The first is cheap and stepped; the second is smooth and costs a rasterised layer.</p>
    </header>

    <div class="nn-20__compare">
      <figure class="nn-20__cell">
        <figcaption class="nn-20__caption">
          <span class="nn-20__tag">Stacked shadows</span>
          four hues, offset per edge &mdash; stepped, one property
        </figcaption>
        <div class="nn-20__well">
          <div class="nn-20__panel nn-20__panel--shadow">
            <p class="nn-20__ptitle">Prism release</p>
            <p class="nn-20__pbody">Four shadow layers, each in its own hue, offset a few pixels so the overlaps mix.</p>
          </div>
        </div>
      </figure>

      <figure class="nn-20__cell">
        <figcaption class="nn-20__caption">
          <span class="nn-20__tag nn-20__tag--good">Blurred gradient</span>
          the glow is the gradient &mdash; smooth, one extra layer
        </figcaption>
        <div class="nn-20__well">
          <div class="nn-20__panel nn-20__panel--grad">
            <p class="nn-20__ptitle">Prism release</p>
            <p class="nn-20__pbody">A duplicate of this shape, filled with the gradient, scaled up and blurred behind the surface.</p>
          </div>
        </div>
      </figure>
    </div>

    <dl class="nn-20__facts">
      <div><dt>hue path</dt><dd>interpolated in oklch, chroma held through the middle</dd></div>
      <div><dt>widening</dt><dd>scale the pre-blurred layer, not the blur radius</dd></div>
      <div><dt>contrast</dt><dd>opaque surface keeps the glow outside the reading area</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
.nn-20 {
  --nn-20-bad: #f4a4a4;
  --nn-20-warn: #f0c88a;
}

@media (prefers-color-scheme: light) {
  .nn-20 {
    --nn-20-bad: #a12a20;
    --nn-20-warn: #78490a;
  }

  .nn-20:has(#nn-20-theme:checked) {
    --nn-20-bad: #f4a4a4;
    --nn-20-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-20:has(#nn-20-theme:checked) {
    --nn-20-bad: #a12a20;
    --nn-20-warn: #78490a;
  }
}

.nn-20[data-theme="light"] {
  --nn-20-bad: #a12a20;
  --nn-20-warn: #78490a;
}

.nn-20 {
  --nn-20-spec-ink: #f4f4f7;
  --nn-20-spec-dim: #9a9aa6;
}

.nn-20__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-20__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-20__tlab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 44px;
  padding: 0 .8rem;
  border: 1px solid currentColor;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: .7;
}

.nn-20__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-20__tlab:hover {
  opacity: 1;
}

.nn-20__tin:focus-visible + .nn-20__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-20:has(#nn-20-theme:checked) {
    --nn-20-bg: #0a0a0c;
    --nn-20-surface: #121216;
    --nn-20-line: #26262e;
    --nn-20-ink: #f4f4f7;
    --nn-20-muted: #9a9aa6;
    background-image: radial-gradient(rgba(255, 255, 255, .022) 1px, transparent 1px);
    background-size: .5rem .5rem;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-20:has(#nn-20-theme:checked) {
    --nn-20-bg: #ececef;
    --nn-20-surface: #ffffff;
    --nn-20-line: #c8c8d0;
    --nn-20-ink: #121216;
    --nn-20-muted: #4d4d58;
    background-image: none;
  }
}

.nn-20 {
  --nn-20-bg: #0a0a0c;
  --nn-20-surface: #121216;
  --nn-20-line: #26262e;
  --nn-20-ink: #f4f4f7;
  --nn-20-muted: #9a9aa6;
  --nn-20-h1: #ff5ec4;
  --nn-20-h2: #7b8cff;
  --nn-20-h3: #35e6ff;
  --nn-20-h4: #ffc247;
  --nn-20-font-display: "Bookman Old Style", "Rockwell", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-20-bg);
  background-image: radial-gradient(rgba(255, 255, 255, .022) 1px, transparent 1px);
  background-size: .5rem .5rem;
  color: var(--nn-20-ink);
  font-family: system-ui, sans-serif;
}

.nn-20 *,
.nn-20 *::before,
.nn-20 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-20 {
    --nn-20-bg: oklch(14% 0.006 285);
    --nn-20-surface: oklch(19% 0.008 285);
    --nn-20-line: oklch(28% 0.01 285);
    --nn-20-ink: oklch(97% 0.006 285);
    --nn-20-muted: oklch(72% 0.012 285);
    --nn-20-h1: oklch(76% 0.21 330);
    --nn-20-h2: oklch(78% 0.19 268);
    --nn-20-h3: oklch(88% 0.15 200);
    --nn-20-h4: oklch(86% 0.16 68);
  }
}

@media (prefers-color-scheme: light) {
  .nn-20 {
    --nn-20-bg: #ececef;
    --nn-20-surface: #ffffff;
    --nn-20-line: #c8c8d0;
    --nn-20-ink: #121216;
    --nn-20-muted: #4d4d58;
    background-image: none;
  }
}

.nn-20[data-theme="light"] {
  --nn-20-bg: #ececef;
  --nn-20-surface: #ffffff;
  --nn-20-line: #c8c8d0;
  --nn-20-ink: #121216;
  --nn-20-muted: #4d4d58;
  background-image: none;
}

.nn-20[data-theme="dark"] {
  --nn-20-bad: #f4a4a4;
  --nn-20-warn: #f0c88a;
  --nn-20-bg: #0a0a0c;
  --nn-20-surface: #121216;
  --nn-20-line: #26262e;
  --nn-20-ink: #f4f4f7;
  --nn-20-muted: #9a9aa6;
  background-image: radial-gradient(rgba(255, 255, 255, .022) 1px, transparent 1px);
  background-size: .5rem .5rem;
}

.nn-20__stage {
  max-width: 68rem;
  margin: 0 auto;
  padding: clamp(1.75rem, 5vw, 2.5rem) clamp(1.25rem, 5vw, 2.25rem) clamp(2.25rem, 6vw, 3rem);
  display: grid;
  gap: clamp(1.5rem, 4vw, 2rem);
}

.nn-20__kicker {
  margin: 0 0 .5rem;
  font-family: var(--nn-20-font-display);
  font-size: .8rem;
  letter-spacing: .08em;
  color: var(--nn-20-h3);
}

.nn-20__heading {
  margin: 0;
  font-family: var(--nn-20-font-display);
  font-size: clamp(1.4rem, 4.8vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -.01em;
  text-wrap: balance;
}

.nn-20__sub {
  margin: .6rem 0 0;
  max-width: 42rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-20-muted);
  text-wrap: pretty;
}

.nn-20__compare {
  display: grid;
  gap: 1.75rem;
  grid-template-columns: 1fr;
}

@media (min-width: 54rem) {
  .nn-20__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-20__cell {
  margin: 0;
  display: grid;
  gap: .7rem;
  min-inline-size: 0;
}

.nn-20__caption {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
  font-size: .78rem;
  color: var(--nn-20-muted);
  min-inline-size: 0;
}

.nn-20__tag {
  padding: .2rem .5rem;
  border: 1px solid var(--nn-20-line);
  border-radius: .2rem;
  font-family: var(--nn-20-font-display);
  font-size: .68rem;
  letter-spacing: .04em;
}

.nn-20__tag--good {
  color: var(--nn-20-h3);
  border-color: color-mix(in srgb, var(--nn-20-h3) 45%, transparent);
}

.nn-20__well {
  display: grid;
  place-items: center;
  min-height: clamp(12rem, 34vw, 16rem);
  padding: clamp(1.75rem, 7vw, 3rem);
  border: 1px solid var(--nn-20-line);
  border-radius: .5rem;
  background: rgba(0, 0, 0, .25);
  overflow: hidden;
}

.nn-20__panel {
  position: relative;
  width: 100%;
  max-width: 20rem;
  display: grid;
  gap: .4rem;
  padding: clamp(1rem, 4vw, 1.4rem);
  border: 1px solid var(--nn-20-line);
  border-radius: .75rem;
  background: var(--nn-20-surface);
  isolation: isolate;
}

.nn-20__panel--shadow {
  box-shadow: -.4rem -.4rem clamp(1rem, 4vw, 1.5rem) color-mix(in srgb, var(--nn-20-h1) 45%, transparent), .4rem .4rem clamp(1rem, 4vw, 1.5rem) color-mix(in srgb, var(--nn-20-h3) 45%, transparent), -.4rem .4rem clamp(1.25rem, 5vw, 1.9rem) color-mix(in srgb, var(--nn-20-h4) 35%, transparent), .4rem -.4rem clamp(1.25rem, 5vw, 1.9rem) color-mix(in srgb, var(--nn-20-h2) 35%, transparent);
}

.nn-20__panel--grad::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(115deg, var(--nn-20-h1), var(--nn-20-h2) 38%, var(--nn-20-h3) 68%, var(--nn-20-h4));
  filter: blur(clamp(.75rem, 3.5vw, 1.35rem));
  transform: scale(1.06);
  opacity: .85;
  z-index: -1;
}

@supports (background: linear-gradient(in oklch, red, blue)) {
  .nn-20__panel--grad::before {
    background: linear-gradient(115deg in oklch, var(--nn-20-h1), var(--nn-20-h2) 38%, var(--nn-20-h3) 68%, var(--nn-20-h4));
  }
}

.nn-20__ptitle {
  margin: 0;
  font-family: var(--nn-20-font-display);
  font-size: 1.05rem;
  font-weight: 600;
}

.nn-20__pbody {
  margin: 0;
  font-size: .82rem;
  line-height: 1.55;
  color: var(--nn-20-muted);
  text-wrap: pretty;
}

.nn-20__facts {
  margin: 0;
  display: grid;
  gap: 0;
  border-top: 1px solid var(--nn-20-line);
}

.nn-20__facts div {
  display: grid;
  gap: .2rem .9rem;
  padding: .6rem 0;
  border-bottom: 1px solid var(--nn-20-line);
  grid-template-columns: 1fr;
}

@media (min-width: 40rem) {
  .nn-20__facts div {
    grid-template-columns: 9rem minmax(0, 1fr);
    align-items: baseline;
  }
}

.nn-20__facts dt {
  font-family: var(--nn-20-font-display);
  font-size: .74rem;
  letter-spacing: .06em;
  color: var(--nn-20-h3);
}

.nn-20__facts dd {
  margin: 0;
  font-size: .84rem;
  line-height: 1.5;
  color: var(--nn-20-muted);
  min-inline-size: 0;
}
```
