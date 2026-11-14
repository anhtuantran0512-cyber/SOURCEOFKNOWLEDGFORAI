---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/newsletter-email-pattern-validation/"
title: "Newsletter Email Pattern Validation"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "A single email field inline with its button, and an honest account of what type=\"email\" does and does not check."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Newsletter Email Pattern Validation
Source: https://codefronts.com/components/css-form-validation/newsletter-email-pattern-validation/

A single email field inline with its button, and an honest account of what type="email" does and does not check. The native type accepts a@b — no dot required — so a pattern tightens it to something with a real domain. The demo also argues the other side: over-strict email regexes reject plus-addressing, long new TLDs and unicode local parts, and those rejections cost you real subscribers.
## HTML
```html
<section class="fv-17" aria-labelledby="fv-17-h">
  <fieldset class="fv-17__theme">
    <legend class="fv-17__themelegend">Theme</legend>
    <input class="fv-17__themeinput" type="radio" name="fv-17-theme" id="fv-17-theme-auto" checked>
    <label class="fv-17__themeopt" for="fv-17-theme-auto">Auto</label>
    <input class="fv-17__themeinput" type="radio" name="fv-17-theme" id="fv-17-theme-light">
    <label class="fv-17__themeopt" for="fv-17-theme-light">Light</label>
    <input class="fv-17__themeinput" type="radio" name="fv-17-theme" id="fv-17-theme-dark">
    <label class="fv-17__themeopt" for="fv-17-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-17__stage">
    <div class="fv-17__col">
      <p class="fv-17__kicker">The Vale Dispatch · Thursdays</p>
      <h2 class="fv-17__h" id="fv-17-h">One field, two arguments about it</h2>
      <p class="fv-17__lede">The native email type will happily accept <code>alex@b</code>. A pattern fixes that — and a stricter one starts throwing away real subscribers.</p>

      <form class="fv-17__form" aria-labelledby="fv-17-h">
        <label class="fv-17__label" for="fv-17-email">Email address</label>
        <div class="fv-17__unit">
          <input class="fv-17__input" id="fv-17-email" name="fv-17-email" type="email" required autocomplete="email" pattern="[^@\s]+@[^@\s]+\.[a-zA-Z][a-zA-Z]+" placeholder="[email protected]" value="alex@vale" title="Include a domain with a dot, like vale.co" aria-describedby="fv-17-msg">
          <button class="fv-17__btn" type="button">Subscribe</button>
        </div>
        <p class="fv-17__msg" id="fv-17-msg">
          <svg class="fv-17__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Include a domain with a dot, like [email protected] — the address as typed has no top-level domain</span>
        </p>
        <p class="fv-17__ok">Thanks. Confirm the address from the email we just sent.</p>
      </form>

      <div class="fv-17__table">
        <div class="fv-17__trow fv-17__trow--head"><span>Address</span><span>This pattern</span><span>An over-strict one</span></div>
        <div class="fv-17__trow"><span><code>[email protected]</code></span><span data-v="pass">Accepted</span><span data-v="fail">Rejected — plus sign</span></div>
        <div class="fv-17__trow"><span><code>[email protected]</code></span><span data-v="pass">Accepted</span><span data-v="fail">Rejected — long TLD</span></div>
        <div class="fv-17__trow"><span><code>sam@vale</code></span><span data-v="fail">Rejected — no dot</span><span data-v="fail">Rejected</span></div>
        <div class="fv-17__trow"><span><code>[email protected]</code></span><span data-v="pass">Accepted</span><span data-v="pass">Accepted</span></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.fv-17 {
  --page: #faf8f4;
  --ink: #131210;
  --muted: #5d564d;
  --rule: #ddd7cc;
  --accent: #1a1917;
  --error: #a03118;
  --error-ink: #872710;
  --ok: #2f6140;
  --display-size: clamp(1.9rem, 6vw, 3.4rem);
  --font-display: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-17 {
    --error: oklch(0.46 0.16 35);
    --error-ink: oklch(0.39 0.16 35);
    --ok: oklch(0.46 0.1 155);
  }
}

.fv-17 *,
.fv-17 *::before,
.fv-17 *::after {
  box-sizing: border-box;
}

.fv-17__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.75rem, 6vw, 5rem) clamp(1rem, 5vw, 3rem);
}

.fv-17__col {
  inline-size: min(100%, 44rem);
  min-inline-size: 0;
}

.fv-17__kicker {
  margin: 0 0 1rem;
  padding-block-end: 1rem;
  border-block-end: 1px solid var(--rule);
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-17__h {
  margin: 0 0 0.75rem;
  font-family: var(--font-display);
  font-size: var(--display-size);
  font-weight: 400;
  line-height: 1.05;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fv-17__lede {
  margin: 0 0 2rem;
  max-inline-size: 34rem;
  font-size: 1.0625rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fv-17__lede code,
.fv-17__trow code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.86em;
  color: var(--ink);
}

.fv-17__form {
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
  max-inline-size: 34rem;
}

.fv-17__label {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-17__unit {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  align-items: stretch;
  min-inline-size: 0;
  border: 1px solid var(--ink);
  background: transparent;
}

.fv-17__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 3.25rem;
  padding: 0 1rem;
  font: inherit;
  font-size: 1rem;
  color: var(--ink);
  background: transparent;
  border: 0;
}

.fv-17__input::placeholder {
  color: #a29a8d;
}

.fv-17__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fv-17__btn {
  min-block-size: 3.25rem;
  min-inline-size: 44px;
  padding: 0 1.5rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  letter-spacing: 0.01em;
  color: var(--page);
  background: var(--accent);
  border: 0;
  cursor: pointer;
}

.fv-17__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-17__msg,
.fv-17__ok {
  display: none;
  gap: 0.4375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.875rem;
  line-height: 1.5;
}

.fv-17__msg {
  color: var(--error-ink);
}

.fv-17__ok {
  color: var(--ok);
  font-weight: 600;
}

.fv-17__msg span {
  min-inline-size: 0;
}

.fv-17__icon {
  flex: none;
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
  margin-block-start: 0.12rem;
}

.fv-17__unit:has(.fv-17__input:invalid:not(:placeholder-shown):not(:focus)) {
  border-color: var(--error);
}

.fv-17__input:invalid:not(:placeholder-shown):not(:focus) ~ .fv-17__btn {
  background: var(--error);
}

.fv-17__form:has(.fv-17__input:invalid:not(:placeholder-shown):not(:focus)) .fv-17__msg {
  display: flex;
}

.fv-17__unit:has(.fv-17__input:user-invalid) {
  border-color: var(--error);
}

.fv-17__input:user-invalid ~ .fv-17__btn {
  background: var(--error);
}

.fv-17__form:has(.fv-17__input:user-invalid) .fv-17__msg {
  display: flex;
}

.fv-17__form:has(.fv-17__input:user-valid) .fv-17__ok {
  display: flex;
}

.fv-17__table {
  display: grid;
  gap: 0;
  margin-block-start: 2.5rem;
  min-inline-size: 0;
  border-block-start: 1px solid var(--ink);
}

.fv-17__trow {
  display: grid;
  grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr) minmax(0, 1fr);
  gap: 0.5rem 1rem;
  padding-block: 0.75rem;
  border-block-end: 1px solid var(--rule);
  font-size: 0.8125rem;
  line-height: 1.45;
  min-inline-size: 0;
}

.fv-17__trow span {
  min-inline-size: 0;
}

.fv-17__trow--head {
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-17__trow [data-v="pass"] {
  color: var(--ok);
  font-weight: 600;
}

.fv-17__trow [data-v="fail"] {
  color: var(--error-ink);
  font-weight: 600;
}

@media (max-width: 30rem) {
  .fv-17__unit {
    grid-template-columns: minmax(0, 1fr);
  }

  .fv-17__btn {
    border-block-start: 1px solid var(--ink);
  }

  .fv-17__trow {
    grid-template-columns: minmax(0, 1fr);
    gap: 0.25rem;
  }

  .fv-17__trow--head {
    display: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-17:not(:has(#fv-17-theme-light:checked)) {
    --page: #100f0d;
    --ink: #f4f1ea;
    --muted: #a09789;
    --rule: #2e2a24;
    --accent: #f4f1ea;
    --error: #ff8256;
    --error-ink: #ffa07d;
    --ok: #6fc38b;
  }

  .fv-17:not(:has(#fv-17-theme-light:checked)) .fv-17__input::placeholder {
    color: #6b6459;
  }

  .fv-17:not(:has(#fv-17-theme-light:checked)) .fv-17__btn {
    color: #100f0d;
  }

  .fv-17:not(:has(#fv-17-theme-light:checked)) .fv-17__input:invalid:not(:placeholder-shown):not(:focus) ~ .fv-17__btn,
    .fv-17:not(:has(#fv-17-theme-light:checked)) .fv-17__input:user-invalid ~ .fv-17__btn {
    color: #1a0d08;
  }
}

[data-theme="dark"] .fv-17:not(:has(#fv-17-theme-light:checked)) {
  --page: #100f0d;
  --ink: #f4f1ea;
  --muted: #a09789;
  --rule: #2e2a24;
  --accent: #f4f1ea;
  --error: #ff8256;
  --error-ink: #ffa07d;
  --ok: #6fc38b;
}

[data-theme="dark"] .fv-17:not(:has(#fv-17-theme-light:checked)) .fv-17__btn {
  color: #100f0d;
}

.fv-17 {
  position: relative;
}

.fv-17__stage {
  padding-block-start: 4.75rem;
}

.fv-17__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 6;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 7%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.fv-17__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-17__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-17__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 1.875rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.fv-17__themeopt:hover {
  opacity: 0.85;
}

.fv-17__themeinput:checked + .fv-17__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-17__themeinput:focus-visible + .fv-17__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-17__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-17__themeinput:checked + .fv-17__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-17:has(#fv-17-theme-dark:checked) {
  --page: #100f0d;
  --ink: #f4f1ea;
  --muted: #a09789;
  --rule: #2e2a24;
  --accent: #f4f1ea;
  --error: #ff8256;
  --error-ink: #ffa07d;
  --ok: #6fc38b;
}

.fv-17:has(#fv-17-theme-dark:checked) .fv-17__input::placeholder {
  color: #6b6459;
}

.fv-17:has(#fv-17-theme-dark:checked) .fv-17__btn {
  color: #100f0d;
}

.fv-17:has(#fv-17-theme-dark:checked) .fv-17__input:invalid:not(:placeholder-shown):not(:focus) ~ .fv-17__btn,
.fv-17:has(#fv-17-theme-dark:checked) .fv-17__input:user-invalid ~ .fv-17__btn {
  color: #1a0d08;
}
```
