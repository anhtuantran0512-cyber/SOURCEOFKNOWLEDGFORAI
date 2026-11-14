---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/animating-glow-intensity-with-at-property/"
title: "Animating Glow Intensity with at-property"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "An unregistered custom property cannot interpolate, so animating --glow steps between values instead of easing between them — the single most common \"why…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animating Glow Intensity with at-property
Source: https://codefronts.com/design-styles/css-neon/animating-glow-intensity-with-at-property/

An unregistered custom property cannot interpolate, so animating --glow steps between values instead of easing between them — the single most common "why won't my neon pulse" question. Registering it with @property and a typed syntax makes intensity animatable independently of hue. The broken version sits beside the working one.
## HTML
```html
<section class="nn-05" aria-labelledby="nn-05-heading">
  <div class="nn-05__stage">
    <div class="nn-05__theme">
      <input class="nn-05__tin" type="checkbox" id="nn-05-theme">
      <label class="nn-05__tlab" for="nn-05-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-05__head">
      <p class="nn-05__kicker">Typed tokens</p>
      <h2 class="nn-05__heading" id="nn-05-heading">A custom property has to be typed before it can breathe</h2>
      <p class="nn-05__sub">Both lamps run the same keyframes on the same token name. Only one of them registered it.</p>
    </header>

    <div class="nn-05__compare">
      <figure class="nn-05__cell">
        <figcaption class="nn-05__caption">
          <span class="nn-05__tag nn-05__tag--bad">Unregistered</span>
          Steps at the midpoint &mdash; reads as nothing happening
        </figcaption>
        <div class="nn-05__well">
          <div class="nn-05__lamp nn-05__lamp--raw">
            <span class="nn-05__label">Sync 4 repositories</span>
          </div>
        </div>
        <p class="nn-05__mono">--nn-05-raw: .35 &rarr; 1 &nbsp;/&nbsp; no @property</p>
      </figure>

      <figure class="nn-05__cell">
        <figcaption class="nn-05__caption">
          <span class="nn-05__tag nn-05__tag--good">Registered</span>
          Interpolates &mdash; a real breath, hue unchanged
        </figcaption>
        <div class="nn-05__well">
          <div class="nn-05__lamp nn-05__lamp--reg">
            <span class="nn-05__label">Sync 4 repositories</span>
          </div>
        </div>
        <p class="nn-05__mono">@property --nn-05-i &#123; syntax: '&lt;number&gt;' &#125;</p>
      </figure>
    </div>

    <div class="nn-05__code">
      <p class="nn-05__clabel">The registration</p>
      <pre class="nn-05__pre"><code>@property --nn-05-i &#123;
  syntax: '&lt;number&gt;';
  initial-value: 1;
  inherits: false;
&#125;</code></pre>
      <p class="nn-05__cnote">The token drives <strong>opacity on a glow layer that is built once</strong> &mdash; not the blur radius, and not the shadow colour. Intensity animates; the expensive part never repaints.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --nn-05-i {
  syntax: '<number>';
  initial-value: 1;
  inherits: false;
}

.nn-05 {
  --nn-05-bad: #f4a4a4;
  --nn-05-warn: #f0c88a;
  --nn-05-spec-neon: #c2f24a;
}

@media (prefers-color-scheme: light) {
  .nn-05 {
    --nn-05-bad: #a12a20;
    --nn-05-warn: #78490a;
  }

  .nn-05:has(#nn-05-theme:checked) {
    --nn-05-bad: #f4a4a4;
    --nn-05-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-05:has(#nn-05-theme:checked) {
    --nn-05-bad: #a12a20;
    --nn-05-warn: #78490a;
  }
}

.nn-05[data-theme="light"] {
  --nn-05-bad: #a12a20;
  --nn-05-warn: #78490a;
}

.nn-05 {
  --nn-05-spec-ink: #f4ecf7;
  --nn-05-spec-dim: #a894b2;
}

.nn-05__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-05__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-05__tlab {
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

.nn-05__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-05__tlab:hover {
  opacity: 1;
}

.nn-05__tin:focus-visible + .nn-05__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-05:has(#nn-05-theme:checked) {
    --nn-05-bg: #150d1a;
    --nn-05-well: #1c1224;
    --nn-05-line: #33203f;
    --nn-05-ink: #f4ecf7;
    --nn-05-muted: #a894b2;
    --nn-05-neon: #c2f24a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-05:has(#nn-05-theme:checked) {
    --nn-05-bg: #eceaef;
    --nn-05-well: #241a2c;
    --nn-05-line: #c8c2ce;
    --nn-05-ink: #171320;
    --nn-05-muted: #554b5e;
    --nn-05-neon: #4f6b0a;
  }
}

.nn-05 {
  --nn-05-hue: 122;
  --nn-05-dur: 3.6s;
  --nn-05-bg: #150d1a;
  --nn-05-well: #1c1224;
  --nn-05-line: #33203f;
  --nn-05-ink: #f4ecf7;
  --nn-05-muted: #a894b2;
  --nn-05-neon: #c2f24a;
  --nn-05-core: rgba(194, 242, 74, .9);
  --nn-05-halo: rgba(194, 242, 74, .48);
  --nn-05-bloom: rgba(194, 242, 74, .26);
  --nn-05-raw: 1;
  --nn-05-font-display: system-ui, "Helvetica Neue", Arial, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-05-bg);
  color: var(--nn-05-ink);
  font-family: system-ui, sans-serif;
}

.nn-05 *,
.nn-05 *::before,
.nn-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-05 {
    --nn-05-bg: oklch(17% 0.035 310);
    --nn-05-well: oklch(21% 0.045 310);
    --nn-05-line: oklch(31% 0.055 310);
    --nn-05-ink: oklch(96% 0.014 310);
    --nn-05-muted: oklch(74% 0.03 310);
    --nn-05-neon: oklch(90% 0.2 var(--nn-05-hue));
    --nn-05-core: oklch(92% 0.2 var(--nn-05-hue) / .9);
    --nn-05-halo: oklch(88% 0.19 var(--nn-05-hue) / .48);
    --nn-05-bloom: oklch(84% 0.18 var(--nn-05-hue) / .26);
  }
}

@media (prefers-color-scheme: light) {
  .nn-05 {
    --nn-05-bg: #eceaef;
    --nn-05-well: #241a2c;
    --nn-05-line: #c8c2ce;
    --nn-05-ink: #171320;
    --nn-05-muted: #554b5e;
    --nn-05-neon: #4f6b0a;
  }
}

.nn-05[data-theme="light"] {
  --nn-05-bg: #eceaef;
  --nn-05-well: #241a2c;
  --nn-05-line: #c8c2ce;
  --nn-05-ink: #171320;
  --nn-05-muted: #554b5e;
  --nn-05-neon: #4f6b0a;
}

.nn-05[data-theme="dark"] {
  --nn-05-bad: #f4a4a4;
  --nn-05-warn: #f0c88a;
  --nn-05-bg: #150d1a;
  --nn-05-well: #1c1224;
  --nn-05-line: #33203f;
  --nn-05-ink: #f4ecf7;
  --nn-05-muted: #a894b2;
  --nn-05-neon: #c2f24a;
}

.nn-05__stage {
  max-width: 66rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 5vw, 2.25rem) clamp(1.25rem, 5vw, 2.25rem) clamp(2rem, 6vw, 2.75rem);
  display: grid;
  gap: clamp(1.5rem, 4vw, 2rem);
}

.nn-05__kicker {
  margin: 0 0 .5rem;
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--nn-05-neon);
}

.nn-05__heading {
  margin: 0;
  font-family: var(--nn-05-font-display);
  font-size: clamp(1.4rem, 4.8vw, 2.1rem);
  font-weight: 650;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.nn-05__sub {
  margin: .6rem 0 0;
  max-width: 40rem;
  font-size: .92rem;
  line-height: 1.6;
  color: var(--nn-05-muted);
  text-wrap: pretty;
}

.nn-05__compare {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: 1fr;
}

@media (min-width: 52rem) {
  .nn-05__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-05__cell {
  margin: 0;
  display: grid;
  gap: .7rem;
  min-inline-size: 0;
}

.nn-05__caption {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
  font-size: .78rem;
  color: var(--nn-05-muted);
  min-inline-size: 0;
}

.nn-05__tag {
  padding: .22rem .5rem;
  border-radius: .35rem;
  border: 1px solid var(--nn-05-line);
  font-size: .64rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.nn-05__tag--bad {
  color: var(--nn-05-bad);
  border-color: #4b2833;
}

.nn-05__tag--good {
  color: var(--nn-05-neon);
  border-color: color-mix(in srgb, var(--nn-05-neon) 40%, transparent);
}

.nn-05__well {
  display: grid;
  place-items: center;
  min-height: clamp(10rem, 28vw, 13rem);
  padding: clamp(1.5rem, 6vw, 2.75rem);
  border-radius: .75rem;
  border: 1px solid var(--nn-05-line);
  background: var(--nn-05-well);
  overflow: hidden;
}

.nn-05__lamp {
  position: relative;
  padding: 1rem 1.4rem;
  border-radius: .6rem;
  border: 1px solid var(--nn-05-spec-neon);
  background: #191125;
  isolation: isolate;
}

.nn-05__lamp::after {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  box-shadow: 0 0 .35rem var(--nn-05-core), 0 0 clamp(.8rem, 3.5vw, 1.25rem) var(--nn-05-halo), 0 0 clamp(1.75rem, 8vw, 3rem) .2rem var(--nn-05-bloom);
  z-index: -1;
}

.nn-05__lamp--raw::after {
  opacity: var(--nn-05-raw);
  animation: nn-05-raw var(--nn-05-dur) ease-in-out infinite;
}

.nn-05__lamp--reg::after {
  opacity: var(--nn-05-i);
  animation: nn-05-reg var(--nn-05-dur) ease-in-out infinite;
}

@keyframes nn-05-raw {
  0%,
    100% {
    --nn-05-raw: .35;
  }

  50% {
    --nn-05-raw: 1;
  }
}

@keyframes nn-05-reg {
  0%,
    100% {
    --nn-05-i: .35;
  }

  50% {
    --nn-05-i: 1;
  }
}

.nn-05__label {
  font-family: ui-monospace, Menlo, monospace;
  font-size: clamp(.8rem, 2.6vw, .92rem);
  color: var(--nn-05-spec-ink);
  letter-spacing: .02em;
}

.nn-05__mono {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
  line-height: 1.5;
  color: var(--nn-05-muted);
  overflow-wrap: anywhere;
}

.nn-05__code {
  display: grid;
  gap: .6rem;
  padding: 1.1rem 1.25rem;
  border-radius: .75rem;
  border: 1px solid var(--nn-05-line);
}

.nn-05__clabel {
  margin: 0;
  font-size: .7rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--nn-05-muted);
}

.nn-05__pre {
  margin: 0;
  overflow-x: auto;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .74rem;
  line-height: 1.7;
  color: var(--nn-05-neon);
}

.nn-05__cnote {
  margin: 0;
  font-size: .84rem;
  line-height: 1.6;
  color: var(--nn-05-muted);
  text-wrap: pretty;
}

.nn-05__cnote strong {
  color: var(--nn-05-ink);
}

@media (prefers-reduced-motion: reduce) {
  .nn-05__lamp--raw::after,
    .nn-05__lamp--reg::after {
    animation: none;
    opacity: 1;
  }
}
```
