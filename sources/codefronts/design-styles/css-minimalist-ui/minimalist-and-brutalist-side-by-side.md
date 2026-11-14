---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/minimalist-and-brutalist-side-by-side/"
title: "Minimalist and Brutalist Side by Side"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "The same signup card built twice, with the decisions labelled on each side: restraint budget against deliberate excess, hairline against 4px border, tonal…"
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist and Brutalist Side by Side
Source: https://codefronts.com/design-styles/css-minimalist-ui/minimalist-and-brutalist-side-by-side/

The same signup card built twice, with the decisions labelled on each side: restraint budget against deliberate excess, hairline against 4px border, tonal elevation against a hard offset shadow. Neither is more correct &mdash; they optimise for different things, and the demo says which is which.
## HTML
```html
<section class="mu-14" aria-labelledby="mu-14-title">
  <h2 class="mu-14__sr" id="mu-14-title">Minimalist and brutalist comparison</h2>
  <div class="mu-14__theme">
    <input class="mu-14__theme-input" type="checkbox" id="mu-14-theme">
    <label class="mu-14__theme-label" for="mu-14-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-14__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-14__stage">

    <div class="mu-14__split">
      <article class="mu-14__side mu-14__side--min" aria-labelledby="mu-14-a">
        <header class="mu-14__side-head">
          <h3 class="mu-14__side-title" id="mu-14-a">Minimalist</h3>
          <p class="mu-14__side-sub">1 accent &middot; 1px hairline &middot; +4% tonal raise</p>
        </header>

        <div class="mu-14__card">
          <p class="mu-14__card-kicker">Meridian</p>
          <h4 class="mu-14__card-title">Start a 14-day trial</h4>
          <p class="mu-14__card-text">Every workspace feature, no card required. Cancel from the billing page in one click.</p>
          <div class="mu-14__field">
            <label class="mu-14__label" for="mu-14-m-mail">Work email</label>
            <input class="mu-14__input" id="mu-14-m-mail" type="email" placeholder="[email protected]" autocomplete="email">
          </div>
          <button class="mu-14__btn" type="button">Create workspace</button>
          <p class="mu-14__card-fine">No credit card. SOC 2 Type II.</p>
        </div>

        <dl class="mu-14__decisions">
          <div><dt>Elevation</dt><dd>Tone step plus top hairline</dd></div>
          <div><dt>Border</dt><dd>1px at 3:1</dd></div>
          <div><dt>Colour budget</dt><dd>One accent, on the action</dd></div>
          <div><dt>Hierarchy</dt><dd>Size, weight, space</dd></div>
          <div><dt>Optimises for</dt><dd>Calm, repeat use, content first</dd></div>
          <div><dt>Fails by</dt><dd>Becoming generic; hiding affordances</dd></div>
        </dl>
      </article>

      <article class="mu-14__side mu-14__side--brut" aria-labelledby="mu-14-b">
        <header class="mu-14__side-head">
          <h3 class="mu-14__side-title" id="mu-14-b">Brutalist</h3>
          <p class="mu-14__side-sub">3 colours &middot; 4px border &middot; 8px hard offset</p>
        </header>

        <div class="mu-14__card">
          <p class="mu-14__card-kicker">Meridian</p>
          <h4 class="mu-14__card-title">Start a 14-day trial</h4>
          <p class="mu-14__card-text">Every workspace feature, no card required. Cancel from the billing page in one click.</p>
          <div class="mu-14__field">
            <label class="mu-14__label" for="mu-14-b-mail">Work email</label>
            <input class="mu-14__input" id="mu-14-b-mail" type="email" placeholder="[email protected]" autocomplete="email">
          </div>
          <button class="mu-14__btn" type="button">Create workspace</button>
          <p class="mu-14__card-fine">No credit card. SOC 2 Type II.</p>
        </div>

        <dl class="mu-14__decisions">
          <div><dt>Elevation</dt><dd>Hard offset shadow, no blur</dd></div>
          <div><dt>Border</dt><dd>4px, maximum contrast</dd></div>
          <div><dt>Colour budget</dt><dd>Three, used deliberately</dd></div>
          <div><dt>Hierarchy</dt><dd>Scale and mass</dd></div>
          <div><dt>Optimises for</dt><dd>Memorability, character, voice</dd></div>
          <div><dt>Fails by</dt><dd>Becoming exhausting; hurting legibility</dd></div>
        </dl>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-14 {
  --mu-14-m-font: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-14-b-font: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-14-m-raise: 4%;
  --mu-14-b-border: 4px;
  --mu-14-b-shadow: 8px;
  --mu-14-bg: #f6f4ef;
  --mu-14-bg: oklch(96.5% 0.008 90);
  --mu-14-ink: #17150f;
  --mu-14-ink: oklch(19.5% 0.008 80);
  --mu-14-ink-2: #55503f;
  --mu-14-ink-2: oklch(44% 0.016 85);
  --mu-14-m-surface: #ffffff;
  --mu-14-m-surface: oklch(100% 0 0);
  --mu-14-m-line: #cfc9b9;
  --mu-14-m-line: oklch(84% 0.016 88);
  --mu-14-m-acc: #1f4ea8;
  --mu-14-m-acc: oklch(43% 0.15 262);
  --mu-14-m-acc-ink: #ffffff;
  --mu-14-m-acc-ink: oklch(100% 0 0);
  --mu-14-b-surface: #fff8e6;
  --mu-14-b-surface: oklch(97.5% 0.045 95);
  --mu-14-b-line: #0d0b06;
  --mu-14-b-line: oklch(13% 0.008 80);
  --mu-14-b-acc: #d12817;
  --mu-14-b-acc: oklch(51% 0.19 29);
  --mu-14-b-acc2: #2f4cff;
  --mu-14-b-acc2: oklch(52% 0.25 268);
  --mu-14-b-acc-ink: #fffdf5;
  --mu-14-b-acc-ink: oklch(99% 0.012 95);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-14-bg);
  color: var(--mu-14-ink);
  font-family: var(--mu-14-m-font);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-14 *,
.mu-14 *::before,
.mu-14 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-14 {
    --mu-14-bg: #14120e;
    --mu-14-bg: oklch(18% 0.008 80);
    --mu-14-ink: #f4f1e8;
    --mu-14-ink: oklch(96% 0.01 90);
    --mu-14-ink-2: #b0a993;
    --mu-14-ink-2: oklch(75% 0.018 88);
    --mu-14-m-surface: #1d1a15;
    --mu-14-m-surface: oklch(22.5% 0.009 82);
    --mu-14-m-line: #3b352a;
    --mu-14-m-line: oklch(33% 0.014 85);
    --mu-14-m-acc: #8fb4ff;
    --mu-14-m-acc: oklch(80% 0.12 262);
    --mu-14-m-acc-ink: #0d1526;
    --mu-14-m-acc-ink: oklch(18% 0.03 258);
    --mu-14-b-surface: #241f10;
    --mu-14-b-surface: oklch(25% 0.05 95);
    --mu-14-b-line: #ffe9a3;
    --mu-14-b-line: oklch(92% 0.1 95);
    --mu-14-b-acc: #ff6a5c;
    --mu-14-b-acc: oklch(72% 0.19 30);
    --mu-14-b-acc2: #8ea0ff;
    --mu-14-b-acc2: oklch(76% 0.15 268);
    --mu-14-b-acc-ink: #1a0f0c;
    --mu-14-b-acc-ink: oklch(18% 0.03 30);
  }
}

.mu-14[data-theme="dark"],
.mu-14:has(.mu-14__theme-input:checked) {
  --mu-14-bg: #14120e;
  --mu-14-bg: oklch(18% 0.008 80);
  --mu-14-ink: #f4f1e8;
  --mu-14-ink: oklch(96% 0.01 90);
  --mu-14-ink-2: #b0a993;
  --mu-14-ink-2: oklch(75% 0.018 88);
  --mu-14-m-surface: #1d1a15;
  --mu-14-m-surface: oklch(22.5% 0.009 82);
  --mu-14-m-line: #3b352a;
  --mu-14-m-line: oklch(33% 0.014 85);
  --mu-14-m-acc: #8fb4ff;
  --mu-14-m-acc: oklch(80% 0.12 262);
  --mu-14-m-acc-ink: #0d1526;
  --mu-14-m-acc-ink: oklch(18% 0.03 258);
  --mu-14-b-surface: #241f10;
  --mu-14-b-surface: oklch(25% 0.05 95);
  --mu-14-b-line: #ffe9a3;
  --mu-14-b-line: oklch(92% 0.1 95);
  --mu-14-b-acc: #ff6a5c;
  --mu-14-b-acc: oklch(72% 0.19 30);
  --mu-14-b-acc2: #8ea0ff;
  --mu-14-b-acc2: oklch(76% 0.15 268);
  --mu-14-b-acc-ink: #1a0f0c;
  --mu-14-b-acc-ink: oklch(18% 0.03 30);
}

@media (prefers-color-scheme: light) {
  .mu-14:has(.mu-14__theme-input:checked) {
    --mu-14-bg: #14120e;
    --mu-14-bg: oklch(18% 0.008 80);
    --mu-14-ink: #f4f1e8;
    --mu-14-ink: oklch(96% 0.01 90);
    --mu-14-ink-2: #b0a993;
    --mu-14-ink-2: oklch(75% 0.018 88);
    --mu-14-m-surface: #1d1a15;
    --mu-14-m-surface: oklch(22.5% 0.009 82);
    --mu-14-m-line: #3b352a;
    --mu-14-m-line: oklch(33% 0.014 85);
    --mu-14-m-acc: #8fb4ff;
    --mu-14-m-acc: oklch(80% 0.12 262);
    --mu-14-m-acc-ink: #0d1526;
    --mu-14-m-acc-ink: oklch(18% 0.03 258);
    --mu-14-b-surface: #241f10;
    --mu-14-b-surface: oklch(25% 0.05 95);
    --mu-14-b-line: #ffe9a3;
    --mu-14-b-line: oklch(92% 0.1 95);
    --mu-14-b-acc: #ff6a5c;
    --mu-14-b-acc: oklch(72% 0.19 30);
    --mu-14-b-acc2: #8ea0ff;
    --mu-14-b-acc2: oklch(76% 0.15 268);
    --mu-14-b-acc-ink: #1a0f0c;
    --mu-14-b-acc-ink: oklch(18% 0.03 30);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-14:has(.mu-14__theme-input:checked) {
    --mu-14-bg: #f6f4ef;
    --mu-14-bg: oklch(96.5% 0.008 90);
    --mu-14-ink: #17150f;
    --mu-14-ink: oklch(19.5% 0.008 80);
    --mu-14-ink-2: #55503f;
    --mu-14-ink-2: oklch(44% 0.016 85);
    --mu-14-m-surface: #ffffff;
    --mu-14-m-surface: oklch(100% 0 0);
    --mu-14-m-line: #cfc9b9;
    --mu-14-m-line: oklch(84% 0.016 88);
    --mu-14-m-acc: #1f4ea8;
    --mu-14-m-acc: oklch(43% 0.15 262);
    --mu-14-m-acc-ink: #ffffff;
    --mu-14-m-acc-ink: oklch(100% 0 0);
    --mu-14-b-surface: #fff8e6;
    --mu-14-b-surface: oklch(97.5% 0.045 95);
    --mu-14-b-line: #0d0b06;
    --mu-14-b-line: oklch(13% 0.008 80);
    --mu-14-b-acc: #d12817;
    --mu-14-b-acc: oklch(51% 0.19 29);
    --mu-14-b-acc2: #2f4cff;
    --mu-14-b-acc2: oklch(52% 0.25 268);
    --mu-14-b-acc-ink: #fffdf5;
    --mu-14-b-acc-ink: oklch(99% 0.012 95);
  }
}

.mu-14__sr {
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

.mu-14__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-14__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-14__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-14-m-line);
  border-radius: 50%;
  background: var(--mu-14-m-surface);
  color: var(--mu-14-ink-2);
  cursor: pointer;
}

.mu-14__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-14__theme-input:focus-visible + .mu-14__theme-label {
  outline: 2px solid var(--mu-14-m-acc);
  outline-offset: 2px;
}

.mu-14__stage {
  max-inline-size: 74rem;
  margin-inline: auto;
  padding: 4rem 1.25rem 5rem;
  display: grid;
  gap: 2.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-14__split {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-14__side {
  min-inline-size: 0;
  display: grid;
  gap: 1.25rem;
  align-content: start;
}

.mu-14__side-head {
  display: grid;
  gap: 2px;
  min-inline-size: 0;
}

.mu-14__side-title {
  margin: 0;
  font-size: 0.8125rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.mu-14__side-sub {
  margin: 0;
  font-size: 0.75rem;
  color: var(--mu-14-ink-2);
  font-variant-numeric: tabular-nums;
}

.mu-14__card {
  min-inline-size: 0;
  display: grid;
  gap: 0.875rem;
  align-content: start;
}

.mu-14__card p,
.mu-14__card h4 {
  margin: 0;
  min-inline-size: 0;
}

.mu-14__card-kicker {
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.mu-14__card-title {
  font-size: 1.375rem;
  line-height: 1.15;
  font-weight: 600;
  letter-spacing: -0.018em;
}

.mu-14__card-text {
  font-size: 0.9375rem;
  text-wrap: pretty;
}

.mu-14__card-fine {
  font-size: 0.75rem;
}

.mu-14__field {
  display: grid;
  gap: 0.375rem;
  min-inline-size: 0;
}

.mu-14__label {
  font-size: 0.8125rem;
  font-weight: 600;
}

.mu-14__input {
  inline-size: 100%;
  min-inline-size: 0;
  min-block-size: 44px;
  padding-inline: 0.75rem;
  font: inherit;
  font-size: 0.9375rem;
}

.mu-14__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  justify-self: start;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding-inline: 1.25rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
}

.mu-14__decisions {
  margin: 0;
  display: grid;
  gap: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
}

.mu-14__decisions > div {
  display: grid;
  gap: 0.125rem 1rem;
  grid-template-columns: minmax(0, 8rem) minmax(0, 1fr);
  padding-block: 0.5rem;
  min-inline-size: 0;
}

.mu-14__decisions dt {
  margin: 0;
  font-weight: 600;
  min-inline-size: 0;
}

.mu-14__decisions dd {
  margin: 0;
  color: var(--mu-14-ink-2);
  min-inline-size: 0;
}

.mu-14__side--min .mu-14__card {
  padding: 1.5rem;
  background: var(--mu-14-m-surface);
  border: 1px solid var(--mu-14-m-line);
  border-radius: 6px;
}

.mu-14__side--min .mu-14__card-kicker {
  color: var(--mu-14-ink-2);
}

.mu-14__side--min .mu-14__card-text {
  color: var(--mu-14-ink-2);
}

.mu-14__side--min .mu-14__card-fine {
  color: var(--mu-14-ink-2);
}

.mu-14__side--min .mu-14__input {
  border: 1px solid var(--mu-14-m-line);
  border-radius: 4px;
  background: var(--mu-14-m-surface);
  color: var(--mu-14-ink);
}

.mu-14__side--min .mu-14__input:focus-visible {
  outline: 2px solid var(--mu-14-m-acc);
  outline-offset: 2px;
  border-color: var(--mu-14-m-acc);
}

.mu-14__side--min .mu-14__btn {
  background: var(--mu-14-m-acc);
  border: 1px solid var(--mu-14-m-acc);
  color: var(--mu-14-m-acc-ink);
  border-radius: 4px;
}

.mu-14__side--min .mu-14__btn:focus-visible {
  outline: 2px solid var(--mu-14-ink);
  outline-offset: 2px;
}

.mu-14__side--min .mu-14__decisions > div {
  border-block-end: 1px solid var(--mu-14-m-line);
}

.mu-14__side--brut {
  font-family: var(--mu-14-b-font);
}

.mu-14__side--brut .mu-14__card {
  padding: 1.25rem;
  background: var(--mu-14-b-surface);
  border: var(--mu-14-b-border) solid var(--mu-14-b-line);
  box-shadow: var(--mu-14-b-shadow) var(--mu-14-b-shadow) 0 var(--mu-14-b-line);
}

.mu-14__side--brut .mu-14__card-kicker {
  color: var(--mu-14-b-acc);
  font-weight: 700;
}

.mu-14__side--brut .mu-14__card-title {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--mu-14-b-line);
}

.mu-14__side--brut .mu-14__card-text,
.mu-14__side--brut .mu-14__card-fine,
.mu-14__side--brut .mu-14__label {
  color: var(--mu-14-b-line);
}

.mu-14__side--brut .mu-14__input {
  border: var(--mu-14-b-border) solid var(--mu-14-b-line);
  border-radius: 0;
  background: var(--mu-14-b-surface);
  color: var(--mu-14-b-line);
}

.mu-14__side--brut .mu-14__input:focus-visible {
  outline: 2px solid var(--mu-14-b-acc2);
  outline-offset: 2px;
}

.mu-14__side--brut .mu-14__btn {
  background: var(--mu-14-b-acc);
  border: var(--mu-14-b-border) solid var(--mu-14-b-line);
  color: var(--mu-14-b-acc-ink);
  border-radius: 0;
  letter-spacing: 0.02em;
  box-shadow: 4px 4px 0 var(--mu-14-b-line);
}

.mu-14__side--brut .mu-14__btn:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--mu-14-b-line);
}

.mu-14__side--brut .mu-14__btn:focus-visible {
  outline: 2px solid var(--mu-14-b-acc2);
  outline-offset: 3px;
}

.mu-14__side--brut .mu-14__decisions > div {
  border-block-end: 2px solid var(--mu-14-b-line);
}

.mu-14__side--brut .mu-14__side-title {
  color: var(--mu-14-b-acc);
  font-weight: 700;
}

@media (prefers-reduced-motion: reduce) {
  .mu-14__side--brut .mu-14__btn:active {
    translate: none;
  }
}

@media (min-width: 52rem) {
  .mu-14__split {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2.5rem;
  }

  .mu-14__stage {
    padding-inline: 3rem;
  }

  .mu-14__side--min .mu-14__card {
    padding: 2rem;
  }

  .mu-14__side--brut .mu-14__card {
    padding: 1.75rem;
  }
}
```
