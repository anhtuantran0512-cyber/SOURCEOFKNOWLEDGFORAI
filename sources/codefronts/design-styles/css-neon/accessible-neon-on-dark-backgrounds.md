---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/accessible-neon-on-dark-backgrounds/"
title: "Accessible Neon on Dark Backgrounds"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Neon's accessibility problem is the inverse of most dark themes: the glow is decorative and carries no contrast, so a thin bright glyph on near-black can…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Neon on Dark Backgrounds
Source: https://codefronts.com/design-styles/css-neon/accessible-neon-on-dark-backgrounds/

Neon's accessibility problem is the inverse of most dark themes: the glow is decorative and carries no contrast, so a thin bright glyph on near-black can look vivid while the text itself fails. A naive heading is shown with its measured ratio, then the fix — 4.5:1 on the core colour alone, adequate stroke weight, and a reduced-motion path that stops the pulse without dimming anything.
## HTML
```html
<section class="nn-08" aria-labelledby="nn-08-heading">
  <div class="nn-08__stage">
    <div class="nn-08__theme">
      <input class="nn-08__tin" type="checkbox" id="nn-08-theme">
      <label class="nn-08__tlab" for="nn-08-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-08__head">
      <p class="nn-08__kicker">Measured, not eyeballed</p>
      <h2 class="nn-08__heading" id="nn-08-heading">The glow is decoration. The contrast has to come from the glyph.</h2>
      <p class="nn-08__sub">Both headings sit on the same ground. The ratios below are measured on the core colour alone, with the halo excluded.</p>
    </header>

    <div class="nn-08__compare">
      <figure class="nn-08__cell">
        <figcaption class="nn-08__caption">
          <span class="nn-08__tag nn-08__tag--bad">Fails</span>
          dim core, hairline weight, rescued by nothing
        </figcaption>
        <div class="nn-08__well">
          <p class="nn-08__spec nn-08__spec--bad">Open channel</p>
        </div>
        <dl class="nn-08__readout">
          <div><dt>core</dt><dd>#7a6c28</dd></div>
          <div><dt>ground</dt><dd>#14170e</dd></div>
          <div><dt>ratio</dt><dd class="nn-08__bad">3.4:1 &mdash; fails AA</dd></div>
          <div><dt>weight</dt><dd>300 at 2rem</dd></div>
        </dl>
      </figure>

      <figure class="nn-08__cell">
        <figcaption class="nn-08__caption">
          <span class="nn-08__tag nn-08__tag--good">Passes</span>
          bright core, real weight, glow purely additive
        </figcaption>
        <div class="nn-08__well">
          <p class="nn-08__spec nn-08__spec--good">Open channel</p>
        </div>
        <dl class="nn-08__readout">
          <div><dt>core</dt><dd>#ffe98a</dd></div>
          <div><dt>ground</dt><dd>#14170e</dd></div>
          <div><dt>ratio</dt><dd class="nn-08__good">14.9:1 &mdash; passes AA</dd></div>
          <div><dt>weight</dt><dd>600 at 2rem</dd></div>
        </dl>
      </figure>
    </div>

    <div class="nn-08__rules">
      <h3 class="nn-08__rtitle">Four rules this demo follows</h3>
      <ol class="nn-08__list">
        <li class="nn-08__li"><strong>Measure without the glow.</strong> If the core colour fails on its own, the heading fails.</li>
        <li class="nn-08__li"><strong>Give the glyph weight.</strong> Thin strokes are eaten by their own bloom before anyone reads them.</li>
        <li class="nn-08__li"><strong>Resolve reduced motion to full glow.</strong> Stop the pulse; never park it at the dim end.</li>
        <li class="nn-08__li"><strong>Focus is a ring, not a brighter halo.</strong> 2px at 3:1, because a blur edge cannot hold a boundary.</li>
      </ol>
      <p class="nn-08__demo">Try the focus ring: <a class="nn-08__link" href="#nn-08-heading">skip to this section's heading</a></p>
      <p class="nn-08__light">On a light ground the glow is reduced to a faint tint here rather than faked. Additive brightness has no headroom above white, so a full-strength glow on a light theme is not a design choice &mdash; it is a shadow.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.nn-08 {
  --nn-08-bad: #f4a4a4;
  --nn-08-warn: #f0c88a;
}

@media (prefers-color-scheme: light) {
  .nn-08 {
    --nn-08-bad: #a12a20;
    --nn-08-warn: #78490a;
  }

  .nn-08:has(#nn-08-theme:checked) {
    --nn-08-bad: #f4a4a4;
    --nn-08-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-08:has(#nn-08-theme:checked) {
    --nn-08-bad: #a12a20;
    --nn-08-warn: #78490a;
  }
}

.nn-08[data-theme="light"] {
  --nn-08-bad: #a12a20;
  --nn-08-warn: #78490a;
}

.nn-08 {
  --nn-08-spec-ink: #f2f3e6;
  --nn-08-spec-dim: #9ea48a;
}

.nn-08__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-08__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-08__tlab {
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

.nn-08__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-08__tlab:hover {
  opacity: 1;
}

.nn-08__tin:focus-visible + .nn-08__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-08:has(#nn-08-theme:checked) {
    --nn-08-bg: #14170e;
    --nn-08-well: #1a1e11;
    --nn-08-line: #2f3520;
    --nn-08-ink: #f2f3e6;
    --nn-08-muted: #9ea48a;
    --nn-08-core-bad: #7a6c28;
    --nn-08-core-good: #ffe98a;
    --nn-08-glow-alpha: .42;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-08:has(#nn-08-theme:checked) {
    --nn-08-bg: #eeeee6;
    --nn-08-well: #ffffff;
    --nn-08-line: #cbccbe;
    --nn-08-ink: #14170e;
    --nn-08-muted: #4f5443;
    --nn-08-core-bad: #8a7a30;
    --nn-08-core-good: #4a4207;
    --nn-08-glow-alpha: .1;
  }
}

.nn-08 {
  --nn-08-hue: 92;
  --nn-08-bg: #14170e;
  --nn-08-well: #1a1e11;
  --nn-08-line: #2f3520;
  --nn-08-ink: #f2f3e6;
  --nn-08-muted: #9ea48a;
  --nn-08-core-bad: #7a6c28;
  --nn-08-core-good: #ffe98a;
  --nn-08-glow-alpha: .42;
  --nn-08-font-display: "Iowan Old Style", Georgia, "Times New Roman", serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-08-bg);
  color: var(--nn-08-ink);
  font-family: system-ui, sans-serif;
}

.nn-08 *,
.nn-08 *::before,
.nn-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-08 {
    --nn-08-bg: oklch(18% 0.024 118);
    --nn-08-well: oklch(21.5% 0.028 118);
    --nn-08-line: oklch(31% 0.032 112);
    --nn-08-ink: oklch(96% 0.016 104);
    --nn-08-muted: oklch(71% 0.024 108);
    --nn-08-core-good: oklch(93% 0.12 var(--nn-08-hue));
  }
}

@media (prefers-color-scheme: light) {
  .nn-08 {
    --nn-08-bg: #eeeee6;
    --nn-08-well: #ffffff;
    --nn-08-line: #cbccbe;
    --nn-08-ink: #14170e;
    --nn-08-muted: #4f5443;
    --nn-08-core-bad: #8a7a30;
    --nn-08-core-good: #4a4207;
    --nn-08-glow-alpha: .1;
  }
}

.nn-08[data-theme="light"] {
  --nn-08-bg: #eeeee6;
  --nn-08-well: #ffffff;
  --nn-08-line: #cbccbe;
  --nn-08-ink: #14170e;
  --nn-08-muted: #4f5443;
  --nn-08-core-bad: #8a7a30;
  --nn-08-core-good: #4a4207;
  --nn-08-glow-alpha: .1;
}

.nn-08[data-theme="dark"] {
  --nn-08-bad: #f4a4a4;
  --nn-08-warn: #f0c88a;
  --nn-08-bg: #14170e;
  --nn-08-well: #1a1e11;
  --nn-08-line: #2f3520;
  --nn-08-ink: #f2f3e6;
  --nn-08-muted: #9ea48a;
  --nn-08-core-bad: #7a6c28;
  --nn-08-core-good: #ffe98a;
  --nn-08-glow-alpha: .42;
}

.nn-08__stage {
  max-width: 66rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 5vw, 2.25rem) clamp(1.25rem, 5vw, 2.25rem) clamp(2rem, 6vw, 2.75rem);
  display: grid;
  gap: clamp(1.5rem, 4vw, 2rem);
}

.nn-08__kicker {
  margin: 0 0 .5rem;
  font-family: var(--nn-08-font-display);
  font-size: .8rem;
  font-style: italic;
  letter-spacing: .04em;
  color: var(--nn-08-core-good);
}

.nn-08__heading {
  margin: 0;
  font-family: var(--nn-08-font-display);
  font-size: clamp(1.4rem, 4.6vw, 2.1rem);
  font-weight: 600;
  line-height: 1.15;
  text-wrap: balance;
}

.nn-08__sub {
  margin: .6rem 0 0;
  max-width: 42rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-08-muted);
  text-wrap: pretty;
}

.nn-08__compare {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: 1fr;
}

@media (min-width: 52rem) {
  .nn-08__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-08__cell {
  margin: 0;
  display: grid;
  gap: .7rem;
  min-inline-size: 0;
}

.nn-08__caption {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
  font-size: .78rem;
  color: var(--nn-08-muted);
  min-inline-size: 0;
}

.nn-08__tag {
  padding: .2rem .5rem;
  border: 1px solid var(--nn-08-line);
  font-family: var(--nn-08-font-display);
  font-size: .68rem;
  letter-spacing: .06em;
}

.nn-08__tag--bad {
  color: var(--nn-08-bad);
  border-color: #4a2a2a;
}

.nn-08__tag--good {
  color: var(--nn-08-core-good);
  border-color: color-mix(in srgb, var(--nn-08-core-good) 40%, transparent);
}

.nn-08__well {
  display: grid;
  place-items: center;
  min-height: clamp(8rem, 24vw, 11rem);
  padding: clamp(1.25rem, 5vw, 2rem);
  border: 1px solid var(--nn-08-line);
  background: var(--nn-08-bg);
  overflow: hidden;
}

.nn-08__spec {
  position: relative;
  margin: 0;
  font-family: var(--nn-08-font-display);
  font-size: clamp(1.5rem, 6vw, 2.4rem);
  line-height: 1.1;
  text-align: center;
}

.nn-08__spec--bad {
  color: var(--nn-08-core-bad);
  font-weight: 300;
  text-shadow: 0 0 .3rem rgba(255, 233, 138, var(--nn-08-glow-alpha)), 0 0 clamp(1rem, 4vw, 1.75rem) rgba(255, 233, 138, .3);
}

.nn-08__spec--good {
  color: var(--nn-08-core-good);
  font-weight: 600;
  animation: nn-08-breathe 4s ease-in-out infinite;
  text-shadow: 0 0 .3rem rgba(255, 233, 138, var(--nn-08-glow-alpha)), 0 0 clamp(1rem, 4vw, 1.75rem) rgba(255, 233, 138, .3);
}

@keyframes nn-08-breathe {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .82;
  }
}

.nn-08__readout {
  margin: 0;
  display: grid;
  gap: 0;
  border-top: 1px solid var(--nn-08-line);
}

.nn-08__readout div {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  padding: .4rem 0;
  border-bottom: 1px solid var(--nn-08-line);
  min-inline-size: 0;
}

.nn-08__readout dt {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .7rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--nn-08-muted);
}

.nn-08__readout dd {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .74rem;
  color: var(--nn-08-ink);
  text-align: right;
}

.nn-08__bad {
  color: var(--nn-08-bad);
}

.nn-08__good {
  color: var(--nn-08-core-good);
}

.nn-08__rules {
  padding: 1.25rem;
  border: 1px solid var(--nn-08-line);
  background: var(--nn-08-well);
}

.nn-08__rtitle {
  margin: 0 0 .8rem;
  font-family: var(--nn-08-font-display);
  font-size: 1.1rem;
  font-weight: 600;
}

.nn-08__list {
  margin: 0 0 1rem;
  padding-left: 1.2rem;
  display: grid;
  gap: .55rem;
}

.nn-08__li {
  font-size: .86rem;
  line-height: 1.6;
  color: var(--nn-08-muted);
  text-wrap: pretty;
}

.nn-08__li strong {
  color: var(--nn-08-ink);
}

.nn-08__li::marker {
  color: var(--nn-08-core-good);
}

.nn-08__demo {
  margin: 0 0 .8rem;
  font-size: .84rem;
  color: var(--nn-08-muted);
}

.nn-08__link {
  display: inline-block;
  min-height: 44px;
  padding: .6rem .1rem;
  color: var(--nn-08-core-good);
  text-decoration: underline;
  text-underline-offset: .2em;
}

.nn-08__link:hover {
  text-decoration-thickness: 2px;
}

.nn-08__link:focus-visible {
  outline: 2px solid var(--nn-08-ink);
  outline-offset: 3px;
  text-decoration: none;
}

.nn-08__light {
  margin: 0;
  padding-top: .8rem;
  border-top: 1px solid var(--nn-08-line);
  font-size: .82rem;
  line-height: 1.6;
  color: var(--nn-08-muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .nn-08__spec--good {
    animation: none;
    opacity: 1;
  }
}
```
