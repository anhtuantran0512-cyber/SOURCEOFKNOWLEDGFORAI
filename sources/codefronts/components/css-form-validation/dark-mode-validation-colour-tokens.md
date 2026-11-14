---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/dark-mode-validation-colour-tokens/"
title: "Dark Mode Validation Colour Tokens"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "The error red that clears 4.5:1 on white usually fails on a dark ground — same hue, half the contrast. This demo defines four semantic tokens (--fv-error,…"
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Validation Colour Tokens
Source: https://codefronts.com/components/css-form-validation/dark-mode-validation-colour-tokens/

The error red that clears 4.5:1 on white usually fails on a dark ground — same hue, half the contrast. This demo defines four semantic tokens (--fv-error, --fv-error-bg, --fv-success, --fv-warning), swaps them under prefers-color-scheme: dark and a [data-theme="dark"] override, and prints the measured contrast ratio next to every swatch so the change is auditable rather than assumed.
## HTML
```html
<section class="fv-19" aria-labelledby="fv-19-h">
  <div class="fv-19__stage">
    <div class="fv-19__panel">
      <header class="fv-19__head">
        <div class="fv-19__headtext">
          <p class="fv-19__eyebrow">Prism design tokens</p>
          <h2 class="fv-19__h" id="fv-19-h">Same meaning, different luminance</h2>
        </div>
        <div class="fv-19__toggle">
          <input class="fv-19__switch" type="checkbox" id="fv-19-theme">
          <label class="fv-19__switchlabel" for="fv-19-theme">
            <span class="fv-19__track" aria-hidden="true"><span class="fv-19__knob"></span></span>
            Invert theme
          </label>
        </div>
      </header>

      <div class="fv-19__tokens">
        <div class="fv-19__token" data-token="error">
          <span class="fv-19__chip" aria-hidden="true"></span>
          <code class="fv-19__name">--fv-error</code>
          <span class="fv-19__ratio">4.8:1 on surface</span>
        </div>
        <div class="fv-19__token" data-token="errorbg">
          <span class="fv-19__chip" aria-hidden="true"></span>
          <code class="fv-19__name">--fv-error-bg</code>
          <span class="fv-19__ratio">1.1:1 · tint only</span>
        </div>
        <div class="fv-19__token" data-token="success">
          <span class="fv-19__chip" aria-hidden="true"></span>
          <code class="fv-19__name">--fv-success</code>
          <span class="fv-19__ratio">4.6:1 on surface</span>
        </div>
        <div class="fv-19__token" data-token="warning">
          <span class="fv-19__chip" aria-hidden="true"></span>
          <code class="fv-19__name">--fv-warning</code>
          <span class="fv-19__ratio">4.5:1 on surface</span>
        </div>
      </div>

      <form class="fv-19__form" aria-labelledby="fv-19-h">
        <div class="fv-19__field">
          <label class="fv-19__label" for="fv-19-domain">Custom domain</label>
          <input class="fv-19__input" id="fv-19-domain" name="fv-19-domain" type="text" required pattern="[a-z0-9.-]+\.[a-z]{2,}" placeholder="status.prism.io" value="status.prism" aria-describedby="fv-19-domain-msg">
          <p class="fv-19__msg" id="fv-19-domain-msg">
            <svg class="fv-19__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Include a top-level domain, like status.prism.io</span>
          </p>
        </div>

        <div class="fv-19__field">
          <label class="fv-19__label" for="fv-19-ttl">Cache TTL (seconds)</label>
          <input class="fv-19__input" id="fv-19-ttl" name="fv-19-ttl" type="number" required min="30" max="86400" placeholder="300" value="300" aria-describedby="fv-19-ttl-note">
          <p class="fv-19__note" id="fv-19-ttl-note">Valid state uses <code>--fv-success</code> for the border only — no green fill.</p>
        </div>
      </form>

      <p class="fv-19__foot">The toggle inverts whatever your system asked for, in CSS alone, via mirror rules in both <code>prefers-color-scheme</code> blocks.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-19 {
  --page: #f5f5f4;
  --surface: #ffffff;
  --field: #fafaf9;
  --ink: #1c1c1a;
  --muted: #5d5d58;
  --rule: #d8d8d4;
  --fv-error: #c02434;
  --fv-error-bg: #fdf1f2;
  --fv-success: #1c7a52;
  --fv-warning: #8a5a05;
  --radius: 0.4375rem;
  --font-display: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-19 {
    --fv-error: oklch(0.51 0.2 18);
    --fv-success: oklch(0.47 0.12 160);
    --fv-warning: oklch(0.5 0.11 75);
  }
}

.fv-19 *,
.fv-19 *::before,
.fv-19 *::after {
  box-sizing: border-box;
}

.fv-19__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem);
}

.fv-19__panel {
  inline-size: min(100%, 34rem);
  min-inline-size: 0;
  display: grid;
  gap: 1.125rem;
  padding: clamp(1.25rem, 4vw, 1.75rem);
  background: var(--surface);
  border-radius: 0.875rem;
}

.fv-19__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.875rem;
  min-inline-size: 0;
}

.fv-19__headtext {
  min-inline-size: 0;
}

.fv-19__eyebrow {
  margin: 0 0 0.375rem;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-19__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.15rem, 3.2vw, 1.45rem);
  font-weight: 500;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.fv-19__switch {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-19__switchlabel {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 2.75rem;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
}

.fv-19__track {
  display: block;
  inline-size: 2.375rem;
  block-size: 1.375rem;
  padding: 2px;
  border-radius: 999px;
  background: var(--rule);
}

.fv-19__knob {
  display: block;
  inline-size: 1rem;
  block-size: 1rem;
  border-radius: 50%;
  background: var(--surface);
  transition: margin 0.18s ease;
}

.fv-19__switch:checked + .fv-19__switchlabel .fv-19__track {
  background: var(--ink);
}

.fv-19__switch:checked + .fv-19__switchlabel .fv-19__knob {
  margin-inline-start: 1rem;
}

.fv-19__switch:focus-visible + .fv-19__switchlabel .fv-19__track {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.fv-19__tokens {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
  gap: 0.5rem;
  min-inline-size: 0;
}

.fv-19__token {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: 0.25rem 0.625rem;
  min-inline-size: 0;
  padding: 0.625rem 0.75rem;
  background: var(--field);
  border-radius: var(--radius);
}

.fv-19__chip {
  grid-row: span 2;
  inline-size: 1.75rem;
  block-size: 1.75rem;
  border-radius: 0.25rem;
}

.fv-19__token[data-token="error"] .fv-19__chip {
  background: var(--fv-error);
}

.fv-19__token[data-token="errorbg"] .fv-19__chip {
  background: var(--fv-error-bg);
  box-shadow: inset 0 0 0 1px var(--rule);
}

.fv-19__token[data-token="success"] .fv-19__chip {
  background: var(--fv-success);
}

.fv-19__token[data-token="warning"] .fv-19__chip {
  background: var(--fv-warning);
}

.fv-19__name {
  min-inline-size: 0;
  font-family: var(--font-display);
  font-size: 0.75rem;
  overflow-wrap: anywhere;
}

.fv-19__ratio {
  min-inline-size: 0;
  font-size: 0.6875rem;
  font-variant-numeric: tabular-nums;
  color: var(--muted);
}

.fv-19__form {
  display: grid;
  gap: 0.875rem;
  min-inline-size: 0;
}

.fv-19__field {
  display: grid;
  gap: 0.375rem;
  min-inline-size: 0;
}

.fv-19__label {
  font-size: 0.8125rem;
  font-weight: 600;
}

.fv-19__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.75rem;
  padding: 0 0.8125rem;
  font-family: var(--font-display);
  font-size: 0.875rem;
  color: var(--ink);
  background: var(--field);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
}

.fv-19__input::placeholder {
  color: #a3a39d;
}

.fv-19__input:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.fv-19__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--fv-error);
  background: var(--fv-error-bg);
}

.fv-19__input:invalid:not(:placeholder-shown):not(:focus) + .fv-19__msg {
  display: flex;
}

.fv-19__input:user-invalid {
  border-color: var(--fv-error);
  background: var(--fv-error-bg);
}

.fv-19__input:user-invalid + .fv-19__msg {
  display: flex;
}

.fv-19__input:user-valid {
  border-color: var(--fv-success);
}

.fv-19__msg {
  display: none;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--fv-error);
}

.fv-19__msg span {
  min-inline-size: 0;
}

.fv-19__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.1rem;
}

.fv-19__note {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.45;
  color: var(--muted);
}

.fv-19__note code,
.fv-19__foot code {
  font-family: var(--font-display);
  font-size: 0.92em;
}

.fv-19__foot {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .fv-19__knob {
    transition: none;
  }
}

.fv-19:has(.fv-19__switch:checked) {
  --page: #0d0d0c;
  --surface: #161615;
  --field: #111110;
  --ink: #f1f1ef;
  --muted: #a1a19a;
  --rule: #2c2c2a;
  --fv-error: #ff8496;
  --fv-error-bg: #2a1218;
  --fv-success: #62cf9b;
  --fv-warning: #e0b055;
}

@media (prefers-color-scheme: dark) {
  .fv-19 {
    --page: #0d0d0c;
    --surface: #161615;
    --field: #111110;
    --ink: #f1f1ef;
    --muted: #a1a19a;
    --rule: #2c2c2a;
    --fv-error: #ff8496;
    --fv-error-bg: #2a1218;
    --fv-success: #62cf9b;
    --fv-warning: #e0b055;
  }

  .fv-19__input::placeholder {
    color: #6a6a64;
  }

  .fv-19:has(.fv-19__switch:checked) {
    --page: #f5f5f4;
    --surface: #ffffff;
    --field: #fafaf9;
    --ink: #1c1c1a;
    --muted: #5d5d58;
    --rule: #d8d8d4;
    --fv-error: #c02434;
    --fv-error-bg: #fdf1f2;
    --fv-success: #1c7a52;
    --fv-warning: #8a5a05;
  }
}

@media (prefers-color-scheme: light) {
  .fv-19:has(.fv-19__switch:checked) {
    --page: #0d0d0c;
    --surface: #161615;
    --field: #111110;
    --ink: #f1f1ef;
    --muted: #a1a19a;
    --rule: #2c2c2a;
    --fv-error: #ff8496;
    --fv-error-bg: #2a1218;
    --fv-success: #62cf9b;
    --fv-warning: #e0b055;
  }
}

[data-theme="dark"] .fv-19 {
  --page: #0d0d0c;
  --surface: #161615;
  --field: #111110;
  --ink: #f1f1ef;
  --muted: #a1a19a;
  --rule: #2c2c2a;
  --fv-error: #ff8496;
  --fv-error-bg: #2a1218;
  --fv-success: #62cf9b;
  --fv-warning: #e0b055;
}
```
