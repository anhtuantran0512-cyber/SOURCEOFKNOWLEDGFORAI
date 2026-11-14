---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/inner-glow-and-faked-light-emission/"
title: "Inner Glow and Faked Light Emission"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Outer glow makes an object look lit from outside; inner glow makes the surface itself look like the light source."
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inner Glow and Faked Light Emission
Source: https://codefronts.com/design-styles/css-neon/inner-glow-and-faked-light-emission/

Outer glow makes an object look lit from outside; inner glow makes the surface itself look like the light source. A stack of inset shadows plus a bright core colour fakes emission on a tube, a bar or a panel edge. A tube built from inset layers sits beside one built only from outer shadows, both labelled, so the difference between a lit object and a light source is visible.
## HTML
```html
<section class="nn-04" aria-labelledby="nn-04-heading">
  <div class="nn-04__stage">
    <div class="nn-04__theme">
      <input class="nn-04__tin" type="checkbox" id="nn-04-theme">
      <label class="nn-04__tlab" for="nn-04-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-04__head">
      <p class="nn-04__kicker">Lit object vs light source</p>
      <h2 class="nn-04__heading" id="nn-04-heading">Inner glow is what makes a tube look on</h2>
      <p class="nn-04__sub">Outer shadows light the surroundings. Inset shadows light the surface itself &mdash; and only one of those reads as emission.</p>
    </header>

    <div class="nn-04__compare">
      <figure class="nn-04__cell">
        <figcaption class="nn-04__caption">
          <span class="nn-04__tag nn-04__tag--bad">Outer only</span>
          Flat fill with a halo &mdash; a lit object
        </figcaption>
        <div class="nn-04__well">
          <div class="nn-04__tube nn-04__tube--outer"></div>
        </div>
        <p class="nn-04__mono">box-shadow: 0 0 8px, 0 0 28px</p>
      </figure>

      <figure class="nn-04__cell">
        <figcaption class="nn-04__caption">
          <span class="nn-04__tag nn-04__tag--good">Inset stack</span>
          Hot core fading to a saturated rim &mdash; a light source
        </figcaption>
        <div class="nn-04__well">
          <div class="nn-04__tube nn-04__tube--inner"></div>
        </div>
        <p class="nn-04__mono">inset 0 0 18px hue, inset 0 0 8px light, inset 0 0 3px white + one outer bloom</p>
      </figure>
    </div>

    <div class="nn-04__layers">
      <h3 class="nn-04__ltitle">Reading the stack from the rim inward</h3>
      <ol class="nn-04__list">
        <li class="nn-04__li"><span class="nn-04__key">inset 18px</span> saturated hue at the rim &mdash; the gas you are looking through</li>
        <li class="nn-04__li"><span class="nn-04__key">inset 8px</span> lifted lightness &mdash; the transition the eye reads as depth</li>
        <li class="nn-04__li"><span class="nn-04__key">inset 3px</span> near-white core &mdash; real emission desaturates when it is hottest</li>
        <li class="nn-04__li"><span class="nn-04__key">outer 30px</span> one low-alpha bloom &mdash; the light landing on the wall behind</li>
      </ol>
    </div>

    <div class="nn-04__panel">
      <p class="nn-04__plabel">One-sided inset: a panel edge that emits upward</p>
      <div class="nn-04__edge">
        <span class="nn-04__edgetext">Vale &middot; channel open</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nn-04 {
  --nn-04-bad: #f4a4a4;
  --nn-04-warn: #f0c88a;
  --nn-04-spec-neon: #ff5a3c;
}

@media (prefers-color-scheme: light) {
  .nn-04 {
    --nn-04-bad: #a12a20;
    --nn-04-warn: #78490a;
  }

  .nn-04:has(#nn-04-theme:checked) {
    --nn-04-bad: #f4a4a4;
    --nn-04-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-04:has(#nn-04-theme:checked) {
    --nn-04-bad: #a12a20;
    --nn-04-warn: #78490a;
  }
}

.nn-04[data-theme="light"] {
  --nn-04-bad: #a12a20;
  --nn-04-warn: #78490a;
}

.nn-04 {
  --nn-04-spec-ink: #e9f6f2;
  --nn-04-spec-dim: #8aa8a1;
}

.nn-04__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-04__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-04__tlab {
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

.nn-04__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-04__tlab:hover {
  opacity: 1;
}

.nn-04__tin:focus-visible + .nn-04__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-04:has(#nn-04-theme:checked) {
    --nn-04-bg: #06110f;
    --nn-04-well: #081815;
    --nn-04-line: #16302b;
    --nn-04-ink: #e9f6f2;
    --nn-04-muted: #8aa8a1;
    --nn-04-neon: #ff5a3c;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-04:has(#nn-04-theme:checked) {
    --nn-04-bg: #e6ecea;
    --nn-04-well: #14231f;
    --nn-04-line: #c1ccc9;
    --nn-04-ink: #101a18;
    --nn-04-muted: #4a5a56;
    --nn-04-neon: #a92c12;
  }
}

.nn-04 {
  --nn-04-hue: 22;
  --nn-04-bg: #06110f;
  --nn-04-well: #081815;
  --nn-04-line: #16302b;
  --nn-04-ink: #e9f6f2;
  --nn-04-muted: #8aa8a1;
  --nn-04-neon: #ff5a3c;
  --nn-04-rim: rgba(255, 90, 60, .85);
  --nn-04-mid: rgba(255, 150, 120, .8);
  --nn-04-core: rgba(255, 236, 226, .95);
  --nn-04-bloom: rgba(255, 90, 60, .3);
  --nn-04-font-display: ui-rounded, "SF Pro Rounded", "Nunito", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-04-bg);
  color: var(--nn-04-ink);
  font-family: system-ui, sans-serif;
}

.nn-04 *,
.nn-04 *::before,
.nn-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-04 {
    --nn-04-bg: oklch(16% 0.02 175);
    --nn-04-well: oklch(20% 0.025 175);
    --nn-04-line: oklch(30% 0.03 175);
    --nn-04-ink: oklch(96% 0.014 175);
    --nn-04-muted: oklch(74% 0.02 175);
    --nn-04-neon: oklch(70% 0.2 var(--nn-04-hue));
    --nn-04-rim: oklch(68% 0.21 var(--nn-04-hue) / .85);
    --nn-04-mid: oklch(82% 0.14 var(--nn-04-hue) / .8);
    --nn-04-core: oklch(97% 0.03 var(--nn-04-hue) / .95);
    --nn-04-bloom: oklch(68% 0.2 var(--nn-04-hue) / .3);
  }
}

@media (prefers-color-scheme: light) {
  .nn-04 {
    --nn-04-bg: #e6ecea;
    --nn-04-well: #14231f;
    --nn-04-line: #c1ccc9;
    --nn-04-ink: #101a18;
    --nn-04-muted: #4a5a56;
    --nn-04-neon: #a92c12;
  }
}

.nn-04[data-theme="light"] {
  --nn-04-bg: #e6ecea;
  --nn-04-well: #14231f;
  --nn-04-line: #c1ccc9;
  --nn-04-ink: #101a18;
  --nn-04-muted: #4a5a56;
  --nn-04-neon: #a92c12;
}

.nn-04[data-theme="dark"] {
  --nn-04-bad: #f4a4a4;
  --nn-04-warn: #f0c88a;
  --nn-04-bg: #06110f;
  --nn-04-well: #081815;
  --nn-04-line: #16302b;
  --nn-04-ink: #e9f6f2;
  --nn-04-muted: #8aa8a1;
  --nn-04-neon: #ff5a3c;
}

.nn-04__stage {
  max-width: 64rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 1.75rem) clamp(1rem, 4vw, 1.75rem) clamp(1.75rem, 5vw, 2.25rem);
  display: grid;
  gap: clamp(1.25rem, 3.5vw, 1.75rem);
}

.nn-04__kicker {
  margin: 0 0 .4rem;
  font-family: var(--nn-04-font-display);
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--nn-04-neon);
}

.nn-04__heading {
  margin: 0;
  font-family: var(--nn-04-font-display);
  font-size: clamp(1.4rem, 5vw, 2.15rem);
  font-weight: 700;
  letter-spacing: -.01em;
  text-wrap: balance;
}

.nn-04__sub {
  margin: .5rem 0 0;
  max-width: 40rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-04-muted);
  text-wrap: pretty;
}

.nn-04__compare {
  display: grid;
  gap: 1.1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 52rem) {
  .nn-04__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-04__cell {
  margin: 0;
  display: grid;
  gap: .6rem;
  min-inline-size: 0;
}

.nn-04__caption {
  display: flex;
  align-items: center;
  gap: .55rem;
  flex-wrap: wrap;
  font-size: .78rem;
  color: var(--nn-04-muted);
  min-inline-size: 0;
}

.nn-04__tag {
  padding: .2rem .5rem;
  border-radius: 999px;
  border: 1px solid var(--nn-04-line);
  font-family: var(--nn-04-font-display);
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.nn-04__tag--bad {
  color: var(--nn-04-bad);
  border-color: #4a2820;
}

.nn-04__tag--good {
  color: var(--nn-04-neon);
  border-color: color-mix(in srgb, var(--nn-04-neon) 45%, transparent);
}

.nn-04__well {
  display: grid;
  place-items: center;
  min-height: clamp(9rem, 26vw, 12rem);
  padding: clamp(1.25rem, 5vw, 2.25rem);
  border-radius: 1rem;
  border: 1px solid var(--nn-04-line);
  background: var(--nn-04-well);
  overflow: hidden;
}

.nn-04__tube {
  width: 100%;
  max-width: 16rem;
  height: clamp(2.25rem, 8vw, 3rem);
  border-radius: 999px;
}

.nn-04__tube--outer {
  background: var(--nn-04-spec-neon);
  box-shadow: 0 0 .5rem var(--nn-04-rim), 0 0 clamp(1rem, 5vw, 1.75rem) var(--nn-04-bloom);
}

.nn-04__tube--inner {
  background: linear-gradient(180deg, var(--nn-04-mid), var(--nn-04-spec-neon) 45%, var(--nn-04-rim));
  box-shadow: inset 0 0 clamp(.75rem, 3vw, 1.15rem) var(--nn-04-rim), inset 0 0 clamp(.4rem, 1.6vw, .55rem) var(--nn-04-mid), inset 0 0 .2rem var(--nn-04-core), 0 0 clamp(1.25rem, 6vw, 2rem) var(--nn-04-bloom);
}

.nn-04__mono {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
  line-height: 1.5;
  color: var(--nn-04-muted);
  overflow-wrap: anywhere;
}

.nn-04__layers {
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  border: 1px solid var(--nn-04-line);
}

.nn-04__ltitle {
  margin: 0 0 .7rem;
  font-family: var(--nn-04-font-display);
  font-size: 1rem;
  font-weight: 700;
}

.nn-04__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .55rem;
}

.nn-04__li {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  align-items: baseline;
  font-size: .82rem;
  line-height: 1.5;
  color: var(--nn-04-muted);
  min-inline-size: 0;
}

.nn-04__key {
  padding: .15rem .45rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--nn-04-neon) 18%, transparent);
  color: var(--nn-04-neon);
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
}

.nn-04__panel {
  display: grid;
  gap: .6rem;
}

.nn-04__plabel {
  margin: 0;
  font-size: .78rem;
  color: var(--nn-04-muted);
}

.nn-04__edge {
  display: flex;
  align-items: center;
  min-height: 4.5rem;
  padding: 1rem 1.25rem;
  border-radius: .75rem;
  background: var(--nn-04-well);
  box-shadow: inset 0 3px clamp(.75rem, 3vw, 1.15rem) var(--nn-04-bloom), inset 0 2px 0 var(--nn-04-spec-neon);
}

.nn-04__edgetext {
  font-family: var(--nn-04-font-display);
  font-size: .92rem;
  font-weight: 600;
  color: var(--nn-04-spec-ink);
}
```
