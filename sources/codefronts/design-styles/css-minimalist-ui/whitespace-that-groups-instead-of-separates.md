---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/whitespace-that-groups-instead-of-separates/"
title: "Whitespace That Groups Instead of Separates"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "A form where every label sits the same distance from its own field and the next one, so nothing is grouped &mdash; then the corrected version, where the gap…"
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Whitespace That Groups Instead of Separates
Source: https://codefronts.com/design-styles/css-minimalist-ui/whitespace-that-groups-instead-of-separates/

A form where every label sits the same distance from its own field and the next one, so nothing is grouped &mdash; then the corrected version, where the gap between groups clearly exceeds the gap inside them. Both sides carry their measurements, so proximity stops being a feeling and becomes a number you can check.
## HTML
```html
<section class="mu-06" aria-labelledby="mu-06-title">
  <h2 class="mu-06__sr" id="mu-06-title">Form grouping comparison</h2>
  <div class="mu-06__theme">
    <input class="mu-06__theme-input" type="checkbox" id="mu-06-theme">
    <label class="mu-06__theme-label" for="mu-06-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-06__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-06__stage">

    <div class="mu-06__pair">
      <article class="mu-06__side mu-06__side--flat" aria-labelledby="mu-06-a">
        <header class="mu-06__side-head">
          <h3 class="mu-06__side-title" id="mu-06-a">Equal spacing</h3>
          <p class="mu-06__side-metric">16px everywhere &middot; ratio 1:1</p>
        </header>
        <div class="mu-06__form">
          <fieldset class="mu-06__set">
            <legend class="mu-06__legend">Billing contact</legend>
            <div class="mu-06__field">
              <label class="mu-06__label" for="mu-06-a-name">Full name</label>
              <input class="mu-06__input" id="mu-06-a-name" type="text" value="Sam Rivera" autocomplete="name">
            </div>
            <div class="mu-06__field">
              <label class="mu-06__label" for="mu-06-a-mail">Work email</label>
              <input class="mu-06__input" id="mu-06-a-mail" type="email" value="[email protected]" autocomplete="email">
            </div>
          </fieldset>
          <fieldset class="mu-06__set">
            <legend class="mu-06__legend">Card</legend>
            <div class="mu-06__field">
              <label class="mu-06__label" for="mu-06-a-card">Card number</label>
              <input class="mu-06__input" id="mu-06-a-card" type="text" inputmode="numeric" value="4242 4242 4242 4242">
            </div>
            <div class="mu-06__field">
              <label class="mu-06__label" for="mu-06-a-exp">Expiry</label>
              <input class="mu-06__input" id="mu-06-a-exp" type="text" inputmode="numeric" value="09 / 29">
            </div>
          </fieldset>
        </div>
      </article>

      <article class="mu-06__side mu-06__side--good" aria-labelledby="mu-06-b">
        <header class="mu-06__side-head">
          <h3 class="mu-06__side-title" id="mu-06-b">Proximity applied</h3>
          <p class="mu-06__side-metric">8px inside &middot; 32px between &middot; ratio 1:4</p>
        </header>
        <div class="mu-06__form mu-06__form--grouped">
          <fieldset class="mu-06__set">
            <legend class="mu-06__legend">Billing contact</legend>
            <div class="mu-06__field">
              <label class="mu-06__label" for="mu-06-b-name">Full name</label>
              <input class="mu-06__input" id="mu-06-b-name" type="text" value="Sam Rivera" autocomplete="name">
            </div>
            <div class="mu-06__field">
              <label class="mu-06__label" for="mu-06-b-mail">Work email</label>
              <input class="mu-06__input" id="mu-06-b-mail" type="email" value="[email protected]" autocomplete="email">
            </div>
          </fieldset>
          <fieldset class="mu-06__set">
            <legend class="mu-06__legend">Card</legend>
            <div class="mu-06__field">
              <label class="mu-06__label" for="mu-06-b-card">Card number</label>
              <input class="mu-06__input" id="mu-06-b-card" type="text" inputmode="numeric" value="4242 4242 4242 4242">
            </div>
            <div class="mu-06__field">
              <label class="mu-06__label" for="mu-06-b-exp">Expiry</label>
              <input class="mu-06__input" id="mu-06-b-exp" type="text" inputmode="numeric" value="09 / 29">
            </div>
          </fieldset>
          <button class="mu-06__submit" type="button">Continue to payment</button>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-06 {
  --mu-06-gap-in: 0.5rem;
  --mu-06-gap-out: 2rem;
  --mu-06-label-gap: 0.375rem;
  --mu-06-field-h: 44px;
  --mu-06-bar: 3px;
  --mu-06-font: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
  --mu-06-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-06-bg: #1c1a18;
  --mu-06-bg: oklch(23% 0.008 60);
  --mu-06-surface: #262320;
  --mu-06-surface: oklch(27.5% 0.009 60);
  --mu-06-field: #322e2a;
  --mu-06-field: oklch(32% 0.01 60);
  --mu-06-ink: #f6f3f0;
  --mu-06-ink: oklch(96.5% 0.006 70);
  --mu-06-ink-2: #b6afa7;
  --mu-06-ink-2: oklch(77% 0.012 70);
  --mu-06-line: #45403a;
  --mu-06-line: oklch(37% 0.011 65);
  --mu-06-acc: #f0a35c;
  --mu-06-acc: oklch(78% 0.13 62);
  --mu-06-acc-ink: #201408;
  --mu-06-acc-ink: oklch(18% 0.03 60);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-06-bg);
  color: var(--mu-06-ink);
  font-family: var(--mu-06-font);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-06 *,
.mu-06 *::before,
.mu-06 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .mu-06 {
    --mu-06-bg: #f6f4f1;
    --mu-06-bg: oklch(96.5% 0.006 70);
    --mu-06-surface: #ffffff;
    --mu-06-surface: oklch(100% 0 0);
    --mu-06-field: #ffffff;
    --mu-06-field: oklch(100% 0 0);
    --mu-06-ink: #1c1a18;
    --mu-06-ink: oklch(23% 0.008 60);
    --mu-06-ink-2: #55504a;
    --mu-06-ink-2: oklch(45% 0.012 65);
    --mu-06-line: #d5cfc7;
    --mu-06-line: oklch(85.5% 0.012 70);
    --mu-06-acc: #8a4a06;
    --mu-06-acc: oklch(45% 0.12 58);
    --mu-06-acc-ink: #ffffff;
    --mu-06-acc-ink: oklch(100% 0 0);
  }
}

.mu-06[data-theme="light"],
.mu-06:has(.mu-06__theme-input:checked) {
  --mu-06-bg: #f6f4f1;
  --mu-06-bg: oklch(96.5% 0.006 70);
  --mu-06-surface: #ffffff;
  --mu-06-surface: oklch(100% 0 0);
  --mu-06-field: #ffffff;
  --mu-06-field: oklch(100% 0 0);
  --mu-06-ink: #1c1a18;
  --mu-06-ink: oklch(23% 0.008 60);
  --mu-06-ink-2: #55504a;
  --mu-06-ink-2: oklch(45% 0.012 65);
  --mu-06-line: #d5cfc7;
  --mu-06-line: oklch(85.5% 0.012 70);
  --mu-06-acc: #8a4a06;
  --mu-06-acc: oklch(45% 0.12 58);
  --mu-06-acc-ink: #ffffff;
  --mu-06-acc-ink: oklch(100% 0 0);
}

@media (prefers-color-scheme: dark) {
  .mu-06:has(.mu-06__theme-input:checked) {
    --mu-06-bg: #f6f4f1;
    --mu-06-bg: oklch(96.5% 0.006 70);
    --mu-06-surface: #ffffff;
    --mu-06-surface: oklch(100% 0 0);
    --mu-06-field: #ffffff;
    --mu-06-field: oklch(100% 0 0);
    --mu-06-ink: #1c1a18;
    --mu-06-ink: oklch(23% 0.008 60);
    --mu-06-ink-2: #55504a;
    --mu-06-ink-2: oklch(45% 0.012 65);
    --mu-06-line: #d5cfc7;
    --mu-06-line: oklch(85.5% 0.012 70);
    --mu-06-acc: #8a4a06;
    --mu-06-acc: oklch(45% 0.12 58);
    --mu-06-acc-ink: #ffffff;
    --mu-06-acc-ink: oklch(100% 0 0);
  }
}

@media (prefers-color-scheme: light) {
  .mu-06:has(.mu-06__theme-input:checked) {
    --mu-06-bg: #1c1a18;
    --mu-06-bg: oklch(23% 0.008 60);
    --mu-06-surface: #262320;
    --mu-06-surface: oklch(27.5% 0.009 60);
    --mu-06-field: #322e2a;
    --mu-06-field: oklch(32% 0.01 60);
    --mu-06-ink: #f6f3f0;
    --mu-06-ink: oklch(96.5% 0.006 70);
    --mu-06-ink-2: #b6afa7;
    --mu-06-ink-2: oklch(77% 0.012 70);
    --mu-06-line: #45403a;
    --mu-06-line: oklch(37% 0.011 65);
    --mu-06-acc: #f0a35c;
    --mu-06-acc: oklch(78% 0.13 62);
    --mu-06-acc-ink: #201408;
    --mu-06-acc-ink: oklch(18% 0.03 60);
  }
}

.mu-06__sr {
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

.mu-06__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-06__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-06__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-06-line);
  border-radius: 50%;
  background: var(--mu-06-surface);
  color: var(--mu-06-ink-2);
  cursor: pointer;
}

.mu-06__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-06__theme-input:focus-visible + .mu-06__theme-label {
  outline: 2px solid var(--mu-06-acc);
  outline-offset: 2px;
}

.mu-06__stage {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: 4rem 1.5rem 5rem;
  display: grid;
  gap: 3rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-06__pair {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-06__side {
  min-inline-size: 0;
  display: grid;
  gap: 1.5rem;
  align-content: start;
  padding: 1.5rem;
  background: var(--mu-06-surface);
  border-radius: 6px;
}

.mu-06__side--good {
  box-shadow: inset var(--mu-06-bar) 0 0 var(--mu-06-acc);
}

.mu-06__side-head {
  display: grid;
  gap: 2px;
  min-inline-size: 0;
}

.mu-06__side-title {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.mu-06__side-metric {
  margin: 0;
  font-family: var(--mu-06-mono);
  font-size: 0.75rem;
  color: var(--mu-06-ink-2);
  font-variant-numeric: tabular-nums;
}

.mu-06__form {
  display: grid;
  gap: 1rem;
  min-inline-size: 0;
}

.mu-06__form--grouped {
  gap: var(--mu-06-gap-out);
}

.mu-06__set {
  margin: 0;
  padding: 0;
  border: 0;
  min-inline-size: 0;
  display: grid;
  gap: 1rem;
}

.mu-06__form--grouped .mu-06__set {
  gap: var(--mu-06-gap-in);
}

.mu-06__legend {
  padding: 0;
  margin-block-end: 0.25rem;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mu-06-ink-2);
}

.mu-06__field {
  display: grid;
  gap: 1rem;
  min-inline-size: 0;
}

.mu-06__form--grouped .mu-06__field {
  gap: var(--mu-06-label-gap);
}

.mu-06__label {
  font-size: 0.875rem;
  font-weight: 500;
}

.mu-06__input {
  min-inline-size: 0;
  inline-size: 100%;
  min-block-size: var(--mu-06-field-h);
  padding-inline: 0.75rem;
  border: 1px solid var(--mu-06-line);
  border-radius: 4px;
  background: var(--mu-06-field);
  color: var(--mu-06-ink);
  font: inherit;
  font-size: 0.9375rem;
}

.mu-06__input:focus-visible {
  outline: 2px solid var(--mu-06-acc);
  outline-offset: 2px;
  border-color: var(--mu-06-acc);
}

.mu-06__submit {
  min-block-size: var(--mu-06-field-h);
  min-inline-size: 44px;
  justify-self: start;
  padding-inline: 1.25rem;
  border: 1px solid var(--mu-06-acc);
  border-radius: 4px;
  background: var(--mu-06-acc);
  color: var(--mu-06-acc-ink);
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
}

.mu-06__submit:focus-visible {
  outline: 2px solid var(--mu-06-ink);
  outline-offset: 2px;
}

@media (min-width: 52rem) {
  .mu-06__pair {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .mu-06__stage {
    padding-inline: 3rem;
  }

  .mu-06__side {
    padding: 2rem;
  }
}
```
