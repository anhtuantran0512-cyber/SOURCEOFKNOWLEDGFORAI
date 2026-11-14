---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/modern-user-invalid-form-fields/"
title: "Modern User Invalid Form Fields"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "A side-by-side comparison of the two ways to style a failing field."
has_js: "false"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern User Invalid Form Fields
Source: https://codefronts.com/components/css-form-validation/modern-user-invalid-form-fields/

A side-by-side comparison of the two ways to style a failing field. The left column uses bare :invalid and is already red with nothing typed, because an empty required field is invalid the instant it renders. The right column uses :user-invalid and stays neutral until the field is blurred or a submit is attempted. Reach for this pattern first — it decides whether the rest of your validation styling is helpful or hostile.
## HTML
```html
<section class="fv-01" aria-labelledby="fv-01-h">
  <fieldset class="fv-01__theme">
    <legend class="fv-01__themelegend">Theme</legend>
    <input class="fv-01__themeinput" type="radio" name="fv-01-theme" id="fv-01-theme-auto" checked>
    <label class="fv-01__themeopt" for="fv-01-theme-auto">Auto</label>
    <input class="fv-01__themeinput" type="radio" name="fv-01-theme" id="fv-01-theme-light">
    <label class="fv-01__themeopt" for="fv-01-theme-light">Light</label>
    <input class="fv-01__themeinput" type="radio" name="fv-01-theme" id="fv-01-theme-dark">
    <label class="fv-01__themeopt" for="fv-01-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-01__stage">
    <header class="fv-01__head">
      <p class="fv-01__eyebrow">Validation timing</p>
      <h2 class="fv-01__h" id="fv-01-h">One pseudo-class shouts on load. The other waits its turn.</h2>
      <p class="fv-01__sub">Both columns hold the same two required fields, untouched. Only the selector differs.</p>
    </header>

    <div class="fv-01__cols">
      <form class="fv-01__col fv-01__col--legacy" aria-label="Styled with the invalid pseudo-class">
        <p class="fv-01__chip fv-01__chip--bad">
          <span class="fv-01__code">:invalid</span>
          <span class="fv-01__chiptext">Red before a keystroke</span>
        </p>
        <div class="fv-01__field">
          <label class="fv-01__label" for="fv-01-a-email">Work email</label>
          <input class="fv-01__input" id="fv-01-a-email" name="fv-01-a-email" type="email" required autocomplete="email" placeholder="[email protected]" aria-describedby="fv-01-a-email-msg">
          <p class="fv-01__msg" id="fv-01-a-email-msg">
            <svg class="fv-01__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.6"></circle><path d="M10 5.8v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Enter a valid email address, like [email protected]</span>
          </p>
        </div>
        <div class="fv-01__field">
          <label class="fv-01__label" for="fv-01-a-team">Team name</label>
          <input class="fv-01__input" id="fv-01-a-team" name="fv-01-a-team" type="text" required minlength="2" placeholder="Meridian Data" aria-describedby="fv-01-a-team-msg">
          <p class="fv-01__msg" id="fv-01-a-team-msg">
            <svg class="fv-01__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.6"></circle><path d="M10 5.8v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Team name needs at least 2 characters</span>
          </p>
        </div>
        <p class="fv-01__verdict fv-01__verdict--bad">Nothing has happened yet and the form is already accusing you.</p>
      </form>

      <form class="fv-01__col fv-01__col--modern" aria-label="Styled with the user-invalid pseudo-class">
        <p class="fv-01__chip fv-01__chip--good">
          <span class="fv-01__code">:user-invalid</span>
          <span class="fv-01__chiptext">Quiet until you leave the field</span>
        </p>
        <div class="fv-01__field">
          <label class="fv-01__label" for="fv-01-b-email">Work email</label>
          <input class="fv-01__input" id="fv-01-b-email" name="fv-01-b-email" type="email" required autocomplete="email" placeholder="[email protected]" aria-describedby="fv-01-b-email-msg">
          <p class="fv-01__msg" id="fv-01-b-email-msg">
            <svg class="fv-01__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.6"></circle><path d="M10 5.8v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Enter a valid email address, like [email protected]</span>
          </p>
        </div>
        <div class="fv-01__field">
          <label class="fv-01__label" for="fv-01-b-team">Team name</label>
          <input class="fv-01__input" id="fv-01-b-team" name="fv-01-b-team" type="text" required minlength="2" placeholder="Meridian Data" aria-describedby="fv-01-b-team-msg">
          <p class="fv-01__msg" id="fv-01-b-team-msg">
            <svg class="fv-01__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.6"></circle><path d="M10 5.8v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Team name needs at least 2 characters</span>
          </p>
        </div>
        <p class="fv-01__verdict fv-01__verdict--good">Type nothing, tab through, and it still trusts you. Blur an empty field and it speaks.</p>
      </form>
    </div>

    <aside class="fv-01__note" aria-label="Why this matters">
      <h3 class="fv-01__notetitle">What the <span class="fv-01__code">user</span> in the name buys you</h3>
      <ul class="fv-01__notelist">
        <li><strong>Bare <span class="fv-01__code">:invalid</span> is state-only.</strong> It asks "is this value legal", and an empty required field never is — so it matches at first paint, before any human input exists.</li>
        <li><strong><span class="fv-01__code">:user-invalid</span> adds a precondition.</strong> The browser tracks whether the control has been interacted with, and refuses to match until it has. No class toggling, no dirty flags to maintain.</li>
        <li><strong>The accessible layer is unchanged.</strong> Colour is paired with an icon and a sentence that says how to fix the problem, and each message is wired to its field with <span class="fv-01__code">aria-describedby</span>.</li>
      </ul>
    </aside>
  </div>
</section>
```
## CSS
```css
.fv-01 {
  --page: #ffffff;
  --surface: #ffffff;
  --ink: #0b1020;
  --muted: #5a6076;
  --rule: #e3e6ee;
  --accent: #3d3af0;
  --error: #c2183b;
  --error-ink: #9c0f2e;
  --error-bg: #fdf2f4;
  --field-h: 2.75rem;
  --radius: 0.5rem;
  --font-display: ui-sans-serif, system-ui, "Helvetica Neue", sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .fv-01 {
    --accent: oklch(0.48 0.24 274);
    --error: oklch(0.52 0.19 15);
    --error-ink: oklch(0.44 0.19 15);
    --error-bg: oklch(0.97 0.02 15);
  }
}

.fv-01 *,
.fv-01 *::before,
.fv-01 *::after {
  box-sizing: border-box;
}

.fv-01__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3.5rem) clamp(1rem, 4vw, 3rem);
}

.fv-01__head {
  max-inline-size: 46rem;
  min-inline-size: 0;
}

.fv-01__eyebrow {
  margin: 0 0 0.75rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fv-01__h {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 3.4vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.15;
  text-wrap: balance;
}

.fv-01__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.55;
  color: var(--muted);
}

.fv-01__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: 1px;
  margin-block: clamp(1.5rem, 4vw, 2.5rem);
  inline-size: min(100%, 46rem);
  background: var(--rule);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  overflow: hidden;
}

.fv-01__col {
  display: grid;
  gap: 1.125rem;
  align-content: start;
  min-inline-size: 0;
  padding: 1.25rem;
  background: var(--surface);
}

.fv-01__chip {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.5rem;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
}

.fv-01__code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 0.78em;
  padding: 0.2em 0.45em;
  border-radius: 0.25rem;
  background: #eef0f7;
  color: var(--ink);
}

.fv-01__chip--bad .fv-01__code {
  background: var(--error-bg);
  color: var(--error-ink);
}

.fv-01__chip--good .fv-01__code {
  background: #eceafe;
  color: var(--accent);
}

.fv-01__chiptext {
  color: var(--muted);
}

.fv-01__field {
  display: grid;
  gap: 0.375rem;
  min-inline-size: 0;
}

.fv-01__label {
  font-size: 0.8125rem;
  font-weight: 550;
  letter-spacing: 0.01em;
}

.fv-01__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: var(--field-h);
  padding: 0 0.75rem;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  transition: border-color 0.16s ease, background-color 0.16s ease;
}

.fv-01__input::placeholder {
  color: #a3a9bb;
}

.fv-01__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-01__msg {
  display: flex;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.4;
  color: var(--error-ink);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.16s ease;
}

.fv-01__msg span {
  min-inline-size: 0;
}

.fv-01__icon {
  flex: none;
  inline-size: 1rem;
  block-size: 1rem;
  margin-block-start: 0.05rem;
}

.fv-01__col--legacy .fv-01__input:invalid {
  border-color: var(--error);
  background: var(--error-bg);
}

.fv-01__col--legacy .fv-01__input:invalid + .fv-01__msg {
  opacity: 1;
  visibility: visible;
}

.fv-01__col--modern .fv-01__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
  background: var(--error-bg);
}

.fv-01__col--modern .fv-01__input:invalid:not(:placeholder-shown):not(:focus) + .fv-01__msg {
  opacity: 1;
  visibility: visible;
}

.fv-01__col--modern .fv-01__input:user-invalid {
  border-color: var(--error);
  background: var(--error-bg);
}

.fv-01__col--modern .fv-01__input:user-invalid + .fv-01__msg {
  opacity: 1;
  visibility: visible;
}

.fv-01__col--modern .fv-01__input:user-valid {
  border-color: #12855f;
}

.fv-01__verdict {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-01__verdict--bad {
  color: var(--error-ink);
}

.fv-01__note {
  inline-size: min(100%, 46rem);
  min-inline-size: 0;
  padding: 1.25rem 1.375rem;
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  background: #fafbfd;
}

.fv-01__notetitle {
  margin: 0 0 0.75rem;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
}

.fv-01__notelist {
  margin: 0;
  padding-inline-start: 1.1rem;
  display: grid;
  gap: 0.55rem;
}

.fv-01__notelist li {
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--muted);
  min-inline-size: 0;
}

.fv-01__notelist strong {
  color: var(--ink);
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .fv-01__input,
    .fv-01__msg {
    transition: none;
  }
}

@media (max-width: 34rem) {
  .fv-01__stage {
    padding-inline: 1rem;
  }

  .fv-01__col {
    padding: 1rem;
  }
}

@media (prefers-color-scheme: dark) {
  .fv-01:not(:has(#fv-01-theme-light:checked)) {
    --page: #08090f;
    --surface: #0f111a;
    --ink: #eef0f7;
    --muted: #979db4;
    --rule: #22252f;
    --accent: #8b88ff;
    --error: #ff6b85;
    --error-ink: #ff9aab;
    --error-bg: #22121a;
  }

  .fv-01:not(:has(#fv-01-theme-light:checked)) .fv-01__code {
    background: #1b1e28;
    color: #eef0f7;
  }

  .fv-01:not(:has(#fv-01-theme-light:checked)) .fv-01__chip--good .fv-01__code {
    background: #1a1836;
    color: #b0aeff;
  }

  .fv-01:not(:has(#fv-01-theme-light:checked)) .fv-01__note {
    background: #0c0e15;
  }

  .fv-01:not(:has(#fv-01-theme-light:checked)) .fv-01__input::placeholder {
    color: #6a7085;
  }
}

[data-theme="dark"] .fv-01:not(:has(#fv-01-theme-light:checked)) {
  --page: #08090f;
  --surface: #0f111a;
  --ink: #eef0f7;
  --muted: #979db4;
  --rule: #22252f;
  --accent: #8b88ff;
  --error: #ff6b85;
  --error-ink: #ff9aab;
  --error-bg: #22121a;
}

[data-theme="dark"] .fv-01:not(:has(#fv-01-theme-light:checked)) .fv-01__code {
  background: #1b1e28;
  color: #eef0f7;
}

[data-theme="dark"] .fv-01:not(:has(#fv-01-theme-light:checked)) .fv-01__note {
  background: #0c0e15;
}

.fv-01 {
  position: relative;
}

.fv-01__stage {
  padding-block-start: 4.75rem;
}

.fv-01__theme {
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

.fv-01__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-01__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-01__themeopt {
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

.fv-01__themeopt:hover {
  opacity: 0.85;
}

.fv-01__themeinput:checked + .fv-01__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-01__themeinput:focus-visible + .fv-01__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-01__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-01__themeinput:checked + .fv-01__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-01:has(#fv-01-theme-dark:checked) {
  --page: #08090f;
  --surface: #0f111a;
  --ink: #eef0f7;
  --muted: #979db4;
  --rule: #22252f;
  --accent: #8b88ff;
  --error: #ff6b85;
  --error-ink: #ff9aab;
  --error-bg: #22121a;
}

.fv-01:has(#fv-01-theme-dark:checked) .fv-01__code {
  background: #1b1e28;
  color: #eef0f7;
}

.fv-01:has(#fv-01-theme-dark:checked) .fv-01__chip--good .fv-01__code {
  background: #1a1836;
  color: #b0aeff;
}

.fv-01:has(#fv-01-theme-dark:checked) .fv-01__note {
  background: #0c0e15;
}

.fv-01:has(#fv-01-theme-dark:checked) .fv-01__input::placeholder {
  color: #6a7085;
}
```
