---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-form-layout/"
title: "CSS Two Column Form Layout"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "A production-grade two column form layout: First/Last name, City/Postcode and Email/Phone pairs on a CSS Grid, full-width rows via grid-column: 1/-1,…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Form Layout
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-form-layout/

A production-grade two column form layout: First/Last name, City/Postcode and Email/Phone pairs on a CSS Grid, full-width rows via grid-column: 1/-1, floating focus rings, live :user-invalid validation styling and a one-column mobile collapse — the exact pattern checkout and signup flows need.
## HTML
```html
<section class="tcl-06" aria-label="Two column form layout demo">
  <form class="tcl-06__form" novalidate>
    <header class="tcl-06__head">
      <h2>Create your account</h2>
      <p>Paired fields share a row on desktop and stack on mobile.</p>
    </header>
    <label class="tcl-06__field"><span>First name</span>
      <input type="text" name="fname" autocomplete="given-name" placeholder="Avery" required>
      <small class="tcl-06__hint">First name is required.</small>
    </label>
    <label class="tcl-06__field"><span>Last name</span>
      <input type="text" name="lname" autocomplete="family-name" placeholder="Whitfield" required>
      <small class="tcl-06__hint">Last name is required.</small>
    </label>
    <label class="tcl-06__field"><span>City</span>
      <input type="text" name="city" autocomplete="address-level2" placeholder="Wellington" required>
      <small class="tcl-06__hint">Enter your city.</small>
    </label>
    <label class="tcl-06__field"><span>Postcode</span>
      <input type="text" name="zip" autocomplete="postal-code" inputmode="numeric" placeholder="6011" required>
      <small class="tcl-06__hint">Enter a valid postcode.</small>
    </label>
    <label class="tcl-06__field tcl-06__field--full"><span>Email address</span>
      <input type="email" name="email" autocomplete="email" placeholder="[email protected]" required>
      <small class="tcl-06__hint">That doesn’t look like a valid email.</small>
    </label>
    <label class="tcl-06__field tcl-06__field--full"><span>What are you building? <em>(optional)</em></span>
      <textarea name="about" rows="3" placeholder="A portfolio, a store, a SaaS…"></textarea>
    </label>
    <label class="tcl-06__check tcl-06__field--full"><input type="checkbox" name="news"><span>Send me one useful email a month — no spam, ever.</span></label>
    <div class="tcl-06__actions tcl-06__field--full">
      <button class="tcl-06__submit" type="submit">Create account</button>
      <span class="tcl-06__note">Free forever · no card required</span>
    </div>
  </form>
</section>
```
## CSS
```css
.tcl-06,
.tcl-06 *,
.tcl-06 *::before,
.tcl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-06 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.55 0.17 160);
  --ink: oklch(0.25 0.02 160);
  --line: oklch(0.88 0.01 160);
  --bad: oklch(0.55 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  background: oklch(0.965 0.01 160);
  padding: clamp(24px,4vw,52px);
  display: grid;
  place-items: center;
}

.tcl-06__form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px 20px;
  width: min(640px,100%);
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: clamp(22px,4vw,36px);
  box-shadow: 0 24px 48px -32px oklch(0.4 0.06 160 / .5);
}

.tcl-06__head {
  grid-column: 1/-1;
  display: grid;
  gap: 6px;
  margin-bottom: 4px;
}

.tcl-06__head h2 {
  font-size: clamp(21px,2.6vw,26px);
  letter-spacing: -.02em;
}

.tcl-06__head p {
  font-size: 13.5px;
  color: color-mix(in oklab,var(--ink) 60%,transparent);
}

.tcl-06__field {
  display: grid;
  gap: 6px;
  min-width: 0;
}

.tcl-06__field--full {
  grid-column: 1/-1;
}

.tcl-06__field>span {
  font: 600 12.5px/1 inherit;
}

.tcl-06__field em {
  font-style: normal;
  font-weight: 400;
  color: color-mix(in oklab,var(--ink) 50%,transparent);
}

.tcl-06__field input,
.tcl-06__field textarea {
  font: inherit;
  font-size: 14.5px;
  color: var(--ink);
  background: oklch(0.98 0.003 160);
  border: 1.5px solid var(--line);
  border-radius: 10px;
  padding: 12px 14px;
  min-height: 46px;
  width: 100%;
  transition: border-color .15s,box-shadow .15s;
}

.tcl-06__field textarea {
  resize: vertical;
  min-height: 80px;
}

.tcl-06__field input::placeholder,
.tcl-06__field textarea::placeholder {
  color: color-mix(in oklab,var(--ink) 35%,transparent);
}

.tcl-06__field input:focus-visible,
.tcl-06__field textarea:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 18%,transparent);
}

.tcl-06__hint {
  display: none;
  font-size: 12px;
  color: var(--bad);
}

.tcl-06__field input:user-invalid {
  border-color: var(--bad);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--bad) 14%,transparent);
}

.tcl-06__field input:user-invalid~.tcl-06__hint {
  display: block;
}

.tcl-06__check {
  display: flex;
  gap: 10px;
  align-items: center;
  font-size: 13.5px;
  cursor: pointer;
}

.tcl-06__check input {
  width: 18px;
  height: 18px;
  accent-color: var(--accent);
  cursor: pointer;
}

.tcl-06__check input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.tcl-06__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  margin-top: 4px;
}

.tcl-06__submit {
  font: 600 15px/1 inherit;
  color: #fff;
  background: var(--accent);
  border: none;
  border-radius: 11px;
  padding: 15px 26px;
  min-height: 48px;
  cursor: pointer;
  transition: transform .15s,box-shadow .2s;
}

.tcl-06__submit:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 22px -10px var(--accent);
}

.tcl-06__submit:active {
  transform: translateY(0);
}

.tcl-06__submit:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.tcl-06__note {
  font-size: 12.5px;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
}

@media (max-width: 560px) {
  .tcl-06__form {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tcl-06__submit {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the <form> itself is the grid (1fr 1fr), full-width rows use grid-column:1/-1, and :user-invalid handles inline validation styling natively. */
```
