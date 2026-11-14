---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/dynamic-form-layout-adaptation/"
title: "Dynamic Form Layout Adaptation"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "The same form rendered in a page, a modal and a drawer at one viewport width: field rows sit side by side where there is room, stack where there is not, and…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dynamic Form Layout Adaptation
Source: https://codefronts.com/layouts/css-container-queries/dynamic-form-layout-adaptation/

The same form rendered in a page, a modal and a drawer at one viewport width: field rows sit side by side where there is room, stack where there is not, and labels move from beside the control to above it. Forms are the clearest case for container queries because a form's context changes far more often than the window does. Layout only &mdash; no validation styling, no submission.
## HTML
```html
<section class="cq-13" aria-labelledby="cq-13-h">
  <fieldset class="cq-13__theme">
    <legend class="cq-13__themelegend">Theme</legend>
    <input class="cq-13__themeinput" type="radio" name="cq-13-theme" id="cq-13-theme-auto" checked>
    <label class="cq-13__themeopt" for="cq-13-theme-auto">Auto</label>
    <input class="cq-13__themeinput" type="radio" name="cq-13-theme" id="cq-13-theme-light">
    <label class="cq-13__themeopt" for="cq-13-theme-light">Light</label>
    <input class="cq-13__themeinput" type="radio" name="cq-13-theme" id="cq-13-theme-dark">
    <label class="cq-13__themeopt" for="cq-13-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-13__stage">
    <header class="cq-13__head">
      <p class="cq-13__kicker">Prism Billing</p>
      <h2 class="cq-13__h" id="cq-13-h">One form, three hosts</h2>
      <p class="cq-13__lede">Page, modal and drawer at the same viewport width. The form lays itself out from the space it was given.</p>
    </header>

    <div class="cq-13__row">
      <section class="cq-13__host cq-13__host--page" aria-label="Form in a page">
        <p class="cq-13__hostlabel">Page &middot; full width</p>
        <form class="cq-13__form">
          <div class="cq-13__fieldrow">
            <p class="cq-13__field"><label for="cq-13-a1">Legal name</label><input class="cq-13__input" id="cq-13-a1" type="text" value="Vale Provisions Ltd"></p>
            <p class="cq-13__field"><label for="cq-13-a2">Trading name</label><input class="cq-13__input" id="cq-13-a2" type="text" value="Vale"></p>
          </div>
          <div class="cq-13__fieldrow">
            <p class="cq-13__field"><label for="cq-13-a3">Billing email</label><input class="cq-13__input" id="cq-13-a3" type="email" value="[email protected]"></p>
            <p class="cq-13__field"><label for="cq-13-a4">VAT number</label><input class="cq-13__input" id="cq-13-a4" type="text" value="GB 418 2290 61"></p>
          </div>
          <div class="cq-13__fieldrow">
            <p class="cq-13__field cq-13__field--full"><label for="cq-13-a5">Billing address</label><input class="cq-13__input" id="cq-13-a5" type="text" value="Unit 4, Basalt Yard, Sheffield"></p>
          </div>
          <div class="cq-13__actions">
            <button class="cq-13__btn" type="button">Save details</button>
            <button class="cq-13__btn cq-13__btn--ghost" type="button">Cancel</button>
          </div>
        </form>
      </section>

      <div class="cq-13__stack">
        <section class="cq-13__host cq-13__host--modal" aria-label="Form in a modal">
          <p class="cq-13__hostlabel">Modal &middot; 28rem</p>
          <form class="cq-13__form">
            <div class="cq-13__fieldrow">
              <p class="cq-13__field"><label for="cq-13-b1">Legal name</label><input class="cq-13__input" id="cq-13-b1" type="text" value="Vale Provisions Ltd"></p>
              <p class="cq-13__field"><label for="cq-13-b2">Trading name</label><input class="cq-13__input" id="cq-13-b2" type="text" value="Vale"></p>
            </div>
            <div class="cq-13__fieldrow">
              <p class="cq-13__field cq-13__field--full"><label for="cq-13-b3">Billing email</label><input class="cq-13__input" id="cq-13-b3" type="email" value="[email protected]"></p>
            </div>
            <div class="cq-13__actions">
              <button class="cq-13__btn" type="button">Save details</button>
            </div>
          </form>
        </section>

        <section class="cq-13__host cq-13__host--drawer" aria-label="Form in a drawer">
          <p class="cq-13__hostlabel">Drawer &middot; 17rem</p>
          <form class="cq-13__form">
            <div class="cq-13__fieldrow">
              <p class="cq-13__field"><label for="cq-13-c1">Legal name</label><input class="cq-13__input" id="cq-13-c1" type="text" value="Vale Provisions"></p>
            </div>
            <div class="cq-13__fieldrow">
              <p class="cq-13__field"><label for="cq-13-c2">Billing email</label><input class="cq-13__input" id="cq-13-c2" type="email" value="[email protected]"></p>
            </div>
            <div class="cq-13__actions">
              <button class="cq-13__btn" type="button">Save</button>
            </div>
          </form>
        </section>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.cq-13,
.cq-13[data-theme="light"] {
  --bg: #f6f7f9;
  --surf: #ffffff;
  --surf2: #eef0f4;
  --line: #d8dce4;
  --ink: #171a21;
  --mut: #5c6473;
  --acc: #4f46e5;
  --sh: 0 1px 2px rgba(23, 26, 33, 0.05), 0 6px 18px rgba(23, 26, 33, 0.06);
}

.cq-13[data-theme="dark"] {
  --bg: #101218;
  --surf: #191c24;
  --surf2: #20242e;
  --line: #2c313d;
  --ink: #eceef4;
  --mut: #9aa2b4;
  --acc: #a5a1ff;
  --sh: 0 1px 2px rgba(0, 0, 0, 0.5), 0 8px 22px rgba(0, 0, 0, 0.42);
}

@media (prefers-color-scheme: dark) {
  .cq-13:not([data-theme="light"]) {
    --bg: #101218;
    --surf: #191c24;
    --surf2: #20242e;
    --line: #2c313d;
    --ink: #eceef4;
    --mut: #9aa2b4;
    --acc: #a5a1ff;
    --sh: 0 1px 2px rgba(0, 0, 0, 0.5), 0 8px 22px rgba(0, 0, 0, 0.42);
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-13,
    .cq-13[data-theme="light"] {
    --acc: oklch(0.52 0.23 285);
  }

  .cq-13[data-theme="dark"] {
    --acc: oklch(0.78 0.13 285);
  }

  @media (prefers-color-scheme: dark) {
    .cq-13:not([data-theme="light"]) {
      --acc: oklch(0.78 0.13 285);
    }
  }
}

.cq-13 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", Helvetica, sans-serif;
  line-height: 1.5;
}

.cq-13 *,
.cq-13 *::before,
.cq-13 *::after {
  box-sizing: border-box;
}

.cq-13__stage {
  max-width: 76rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.5rem);
  display: grid;
  gap: 1.5rem;
}

.cq-13__kicker {
  margin: 0 0 0.35rem;
  font-size: 0.74rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--acc);
}

.cq-13__h {
  margin: 0;
  font-size: clamp(1.35rem, 1.1rem + 1.6vw, 1.95rem);
  font-weight: 650;
  letter-spacing: -0.02em;
}

.cq-13__lede {
  margin: 0.35rem 0 0;
  color: var(--mut);
  font-size: 0.88rem;
  max-width: 56ch;
}

.cq-13__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  align-items: start;
}

.cq-13__stack {
  flex: 1 1 100%;
  min-inline-size: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  align-items: start;
}

.cq-13__host {
  container: cq-13-form / inline-size;
  min-inline-size: 0;
  padding: 1.1rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 12px;
  box-shadow: var(--sh);
}

.cq-13__host--page {
  flex: 1 1 100%;
}

.cq-13__host--modal {
  flex: 0 1 28rem;
  max-inline-size: 28rem;
}

.cq-13__host--drawer {
  flex: 0 1 17rem;
  max-inline-size: 17rem;
}

.cq-13__hostlabel {
  margin: 0 0 0.9rem;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mut);
  font-weight: 600;
}

.cq-13__form {
  display: grid;
  gap: 0.85rem;
}

.cq-13__fieldrow {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.85rem;
}

.cq-13__field {
  margin: 0;
  min-inline-size: 0;
  display: grid;
  gap: 0.3rem;
}

.cq-13__field label {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--mut);
}

.cq-13__input {
  min-inline-size: 0;
  min-block-size: 2.75rem;
  padding: 0 0.7rem;
  background: var(--surf2);
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: 8px;
  font: inherit;
  font-size: 0.88rem;
}

.cq-13__input:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 1px;
  border-color: var(--acc);
}

.cq-13__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  padding-top: 0.35rem;
}

.cq-13__btn {
  min-block-size: 2.75rem;
  padding-inline: 1.1rem;
  border: 1px solid transparent;
  border-radius: 8px;
  background: var(--acc);
  color: #fff;
  font: inherit;
  font-size: 0.86rem;
  font-weight: 600;
  cursor: pointer;
}

.cq-13__btn--ghost {
  background: transparent;
  color: var(--acc);
  border-color: var(--line);
}

.cq-13__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

@container cq-13-form (min-width: 26em) {
  .cq-13__fieldrow {
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  }

  .cq-13__field--full {
    grid-column: 1 / -1;
  }
}

@container cq-13-form (min-width: 40em) {
  .cq-13__field {
    grid-template-columns: 9rem minmax(0, 1fr);
    align-items: center;
    gap: 0.75rem;
  }

  .cq-13__field label {
    text-align: end;
  }

  .cq-13__fieldrow {
    gap: 0.85rem 1.5rem;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-13 {
  position: relative;
}

.cq-13__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.cq-13__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-13__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-13__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
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

.cq-13__themeopt:hover {
  opacity: 0.85;
}

.cq-13__themeinput:checked + .cq-13__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-13__themeinput:focus-visible + .cq-13__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-13:has(#cq-13-theme-light:checked) {
  --bg: #f6f7f9;
  --surf: #ffffff;
  --surf2: #eef0f4;
  --line: #d8dce4;
  --ink: #171a21;
  --mut: #5c6473;
  --acc: #4f46e5;
  --sh: 0 1px 2px rgba(23, 26, 33, 0.05), 0 6px 18px rgba(23, 26, 33, 0.06);
}

.cq-13:has(#cq-13-theme-dark:checked) {
  --bg: #101218;
  --surf: #191c24;
  --surf2: #20242e;
  --line: #2c313d;
  --ink: #eceef4;
  --mut: #9aa2b4;
  --acc: #a5a1ff;
  --sh: 0 1px 2px rgba(0, 0, 0, 0.5), 0 8px 22px rgba(0, 0, 0, 0.42);
}
```
