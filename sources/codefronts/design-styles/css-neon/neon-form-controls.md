---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-form-controls/"
title: "Neon Form Inputs and Focus Glow"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Inputs where focus produces a glow, built so the glow is never the thing doing the work."
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Form Inputs and Focus Glow
Source: https://codefronts.com/design-styles/css-neon/neon-form-controls/

Inputs where focus produces a glow, built so the glow is never the thing doing the work. A real 2px ring carries the focus requirement, the glow carries the character, and validity is signalled with text and a mark as well as light. No script and no <form> element &mdash; only :focus-visible, :has() and native validity.
## HTML
```html
<section class="nn-13" aria-labelledby="nn-13-heading">
  <div class="nn-13__stage">
    <div class="nn-13__theme">
      <input class="nn-13__tin" type="checkbox" id="nn-13-theme">
      <label class="nn-13__tlab" for="nn-13-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-13__head">
      <p class="nn-13__kicker">Ring first, glow second</p>
      <h2 class="nn-13__heading" id="nn-13-heading">Focus glow that still passes focus appearance</h2>
      <p class="nn-13__sub">Tab through the fields. The 2px ring is the indicator; the glow is decoration sitting outside it.</p>
    </header>

    <div class="nn-13__panel">
      <div class="nn-13__field">
        <label class="nn-13__label" for="nn-13-name">Workspace name</label>
        <input class="nn-13__input" id="nn-13-name" type="text" value="Meridian" autocomplete="off" spellcheck="false">
        <p class="nn-13__help">Lowercase letters, numbers and hyphens.</p>
      </div>

      <div class="nn-13__field">
        <label class="nn-13__label" for="nn-13-mail">Notification address</label>
        <input class="nn-13__input" id="nn-13-mail" type="email" required value="priya@" autocomplete="off">
        <p class="nn-13__err">
          <svg class="nn-13__mark" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 2v8M8 13.2v.6" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path></svg>
          Needs a full address, such as [email protected]
        </p>
      </div>

      <div class="nn-13__field">
        <label class="nn-13__label" for="nn-13-region">Region</label>
        <select class="nn-13__input nn-13__input--select" id="nn-13-region">
          <option>eu-west-1</option>
          <option>us-east-2</option>
          <option>ap-south-1</option>
        </select>
        <p class="nn-13__help">Log retention follows the region's policy.</p>
      </div>

      <div class="nn-13__row">
        <button class="nn-13__btn" type="button">Save workspace</button>
        <p class="nn-13__note">No <span class="nn-13__code">&lt;form&gt;</span>, no submit handler, no script.</p>
      </div>
    </div>

    <ul class="nn-13__facts">
      <li class="nn-13__fact"><span class="nn-13__fkey">ring</span> 2px solid, 2px offset, 3:1 against the ground</li>
      <li class="nn-13__fact"><span class="nn-13__fkey">glow</span> hard 8px core plus one 20px halo, outside the ring</li>
      <li class="nn-13__fact"><span class="nn-13__fkey">invalid</span> hue shift <em>and</em> a message with a mark</li>
      <li class="nn-13__fact"><span class="nn-13__fkey">target</span> 44px minimum on every control</li>
    </ul>
  </div>
</section>
```
## CSS
```css
.nn-13 {
  --nn-13-bad: #f4a4a4;
  --nn-13-warn: #f0c88a;
  --nn-13-spec-neon: #8ef56a;
}

@media (prefers-color-scheme: light) {
  .nn-13 {
    --nn-13-bad: #a12a20;
    --nn-13-warn: #78490a;
  }

  .nn-13:has(#nn-13-theme:checked) {
    --nn-13-bad: #f4a4a4;
    --nn-13-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-13:has(#nn-13-theme:checked) {
    --nn-13-bad: #a12a20;
    --nn-13-warn: #78490a;
  }
}

.nn-13[data-theme="light"] {
  --nn-13-bad: #a12a20;
  --nn-13-warn: #78490a;
}

.nn-13 {
  --nn-13-spec-ink: #f2f4ee;
  --nn-13-spec-dim: #9c9e94;
}

.nn-13__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-13__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-13__tlab {
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

.nn-13__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-13__tlab:hover {
  opacity: 1;
}

.nn-13__tin:focus-visible + .nn-13__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-13:has(#nn-13-theme:checked) {
    --nn-13-bg: #131311;
    --nn-13-panel: #191917;
    --nn-13-line: #2e2e29;
    --nn-13-ink: #f2f4ee;
    --nn-13-muted: #9c9e94;
    --nn-13-neon: #8ef56a;
    --nn-13-warn: #ff8f6b;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-13:has(#nn-13-theme:checked) {
    --nn-13-bg: #eceee8;
    --nn-13-panel: #ffffff;
    --nn-13-line: #c9cbc2;
    --nn-13-ink: #14160f;
    --nn-13-muted: #4e5147;
    --nn-13-neon: #2b6b13;
    --nn-13-warn: #9a3908;
  }
}

.nn-13 {
  --nn-13-hue: 138;
  --nn-13-bg: #131311;
  --nn-13-panel: #191917;
  --nn-13-line: #2e2e29;
  --nn-13-ink: #f2f4ee;
  --nn-13-muted: #9c9e94;
  --nn-13-neon: #8ef56a;
  --nn-13-core: rgba(142, 245, 106, .75);
  --nn-13-halo: rgba(142, 245, 106, .3);
  --nn-13-warn: #ff8f6b;
  --nn-13-font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-13-bg);
  color: var(--nn-13-ink);
  font-family: system-ui, sans-serif;
}

.nn-13 *,
.nn-13 *::before,
.nn-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-13 {
    --nn-13-bg: oklch(17% 0.006 100);
    --nn-13-panel: oklch(20.5% 0.008 100);
    --nn-13-line: oklch(30% 0.01 100);
    --nn-13-ink: oklch(96% 0.012 110);
    --nn-13-muted: oklch(72% 0.014 110);
    --nn-13-neon: oklch(89% 0.19 var(--nn-13-hue));
    --nn-13-core: oklch(89% 0.19 var(--nn-13-hue) / .75);
    --nn-13-halo: oklch(85% 0.18 var(--nn-13-hue) / .3);
    --nn-13-warn: oklch(78% 0.14 42);
  }
}

@media (prefers-color-scheme: light) {
  .nn-13 {
    --nn-13-bg: #eceee8;
    --nn-13-panel: #ffffff;
    --nn-13-line: #c9cbc2;
    --nn-13-ink: #14160f;
    --nn-13-muted: #4e5147;
    --nn-13-neon: #2b6b13;
    --nn-13-warn: #9a3908;
  }
}

.nn-13[data-theme="light"] {
  --nn-13-bg: #eceee8;
  --nn-13-panel: #ffffff;
  --nn-13-line: #c9cbc2;
  --nn-13-ink: #14160f;
  --nn-13-muted: #4e5147;
  --nn-13-neon: #2b6b13;
  --nn-13-warn: #9a3908;
}

.nn-13[data-theme="dark"] {
  --nn-13-bad: #f4a4a4;
  --nn-13-warn: #f0c88a;
  --nn-13-bg: #131311;
  --nn-13-panel: #191917;
  --nn-13-line: #2e2e29;
  --nn-13-ink: #f2f4ee;
  --nn-13-muted: #9c9e94;
  --nn-13-neon: #8ef56a;
  --nn-13-warn: #ff8f6b;
}

.nn-13__stage {
  max-width: 56rem;
  margin: 0 auto;
  padding: clamp(1rem, 3vw, 1.35rem) clamp(.75rem, 3vw, 1.35rem) clamp(1.5rem, 4vw, 1.85rem);
  display: grid;
  gap: clamp(.9rem, 2.5vw, 1.15rem);
}

.nn-13__kicker {
  margin: 0 0 .3rem;
  font-family: var(--nn-13-font-display);
  font-size: .68rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--nn-13-neon);
}

.nn-13__heading {
  margin: 0;
  font-family: var(--nn-13-font-display);
  font-size: clamp(1.2rem, 4.2vw, 1.7rem);
  font-weight: 500;
  letter-spacing: -.01em;
  text-wrap: balance;
}

.nn-13__sub {
  margin: .4rem 0 0;
  max-width: 38rem;
  font-size: .85rem;
  line-height: 1.55;
  color: var(--nn-13-muted);
  text-wrap: pretty;
}

.nn-13__panel {
  display: grid;
  gap: .75rem;
  padding: clamp(.85rem, 3vw, 1.15rem);
  border: 1px solid var(--nn-13-line);
  border-radius: .25rem;
  background: var(--nn-13-panel);
}

.nn-13__field {
  display: grid;
  gap: .3rem;
  min-inline-size: 0;
}

.nn-13__label {
  font-family: var(--nn-13-font-display);
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--nn-13-muted);
}

.nn-13__input {
  min-height: 44px;
  width: 100%;
  padding: .6rem .7rem;
  border: 1px solid var(--nn-13-line);
  border-radius: .2rem;
  background: #101010;
  color: var(--nn-13-spec-ink);
  font-family: var(--nn-13-font-display);
  font-size: .85rem;
  transition: box-shadow 120ms ease, border-color 120ms ease;
}

.nn-13__input--select {
  appearance: none;
  background-image: linear-gradient(45deg, transparent 49%, var(--nn-13-muted) 50%), linear-gradient(-45deg, transparent 49%, var(--nn-13-muted) 50%);
  background-size: .35rem .35rem;
  background-position: right 1rem center, right .65rem center;
  background-repeat: no-repeat;
}

.nn-13__input:hover {
  border-color: color-mix(in srgb, var(--nn-13-neon) 45%, var(--nn-13-line));
}

.nn-13__input:focus-visible {
  outline: 2px solid var(--nn-13-neon);
  outline-offset: 2px;
  border-color: var(--nn-13-neon);
  box-shadow: 0 0 .5rem var(--nn-13-core), 0 0 clamp(.9rem, 4vw, 1.25rem) var(--nn-13-halo);
}

.nn-13__input:user-invalid {
  border-color: var(--nn-13-warn);
  box-shadow: 0 0 .4rem color-mix(in srgb, var(--nn-13-warn) 55%, transparent);
}

.nn-13__input:user-invalid:focus-visible {
  outline-color: var(--nn-13-warn);
}

.nn-13__help {
  margin: 0;
  font-size: .74rem;
  line-height: 1.45;
  color: var(--nn-13-muted);
}

.nn-13__err {
  margin: 0;
  display: none;
  align-items: center;
  gap: .35rem;
  font-size: .74rem;
  line-height: 1.45;
  color: var(--nn-13-warn);
}

.nn-13__mark {
  width: .85rem;
  height: .85rem;
  flex: none;
}

.nn-13__field:has(.nn-13__input:user-invalid) .nn-13__err {
  display: flex;
}

.nn-13__field:has(.nn-13__input:focus-visible) .nn-13__label {
  color: var(--nn-13-neon);
}

.nn-13__row {
  display: flex;
  align-items: center;
  gap: .75rem;
  flex-wrap: wrap;
  padding-top: .35rem;
  border-top: 1px solid var(--nn-13-line);
}

.nn-13__btn {
  min-height: 44px;
  padding: 0 1rem;
  border: 1px solid var(--nn-13-neon);
  border-radius: .2rem;
  background: #101010;
  color: var(--nn-13-spec-ink);
  font-family: var(--nn-13-font-display);
  font-size: .8rem;
  cursor: pointer;
  box-shadow: 0 0 .35rem var(--nn-13-core);
}

.nn-13__btn:hover {
  box-shadow: 0 0 .5rem var(--nn-13-core), 0 0 1.1rem var(--nn-13-halo);
}

.nn-13__btn:focus-visible {
  outline: 2px solid var(--nn-13-ink);
  outline-offset: 2px;
}

.nn-13__note {
  margin: 0;
  font-size: .74rem;
  color: var(--nn-13-muted);
  min-inline-size: 0;
}

.nn-13__code {
  font-family: var(--nn-13-font-display);
  color: var(--nn-13-neon);
}

.nn-13__facts {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0;
  border-top: 1px solid var(--nn-13-line);
}

.nn-13__fact {
  display: flex;
  gap: .6rem;
  align-items: baseline;
  flex-wrap: wrap;
  padding: .5rem 0;
  border-bottom: 1px solid var(--nn-13-line);
  font-size: .78rem;
  color: var(--nn-13-muted);
  min-inline-size: 0;
}

.nn-13__fkey {
  font-family: var(--nn-13-font-display);
  font-size: .66rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--nn-13-neon);
}

@media (prefers-reduced-motion: reduce) {
  .nn-13__input {
    transition: none;
  }
}
```
