---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/custom-radio-button-cards-selectable-cards/"
title: "Custom Radio Button Cards (Selectable Cards)"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "The most-requested radio pattern in modern checkout and onboarding UIs: full selectable cards that act as radio buttons."
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom Radio Button Cards (Selectable Cards)
Source: https://codefronts.com/components/css-radio-buttons/custom-radio-button-cards-selectable-cards/

The most-requested radio pattern in modern checkout and onboarding UIs: full selectable cards that act as radio buttons. Each shipping option is a real <input type="radio"> wrapped in a card label — click anywhere on the card to select it, and the chosen card lifts, tints and reveals a springy check dot. Pure CSS via :has(), no JavaScript.
## HTML
```html
<div class="crb-01-group">
<section class="crb-01a" aria-label="Selectable card radio buttons">
  <fieldset class="crb-01a__group">
    <legend class="crb-01a__legend">Shipping speed</legend>
    <p class="crb-01a__hint">Every card is a real radio input — click anywhere on it</p>
    <div class="crb-01a__cards">
      <label class="crb-01a__card">
        <input class="crb-01a__input" type="radio" name="crb-01a" value="standard" checked>
        <span class="crb-01a__dot" aria-hidden="true"></span>
        <svg class="crb-01a__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7h11v8H3zM14 10h4l3 3v2h-7z"/><circle cx="7" cy="17" r="1.8"/><circle cx="17" cy="17" r="1.8"/></svg>
        <span class="crb-01a__title">Standard</span>
        <span class="crb-01a__meta">4–6 business days</span>
        <span class="crb-01a__price">Free</span>
      </label>
      <label class="crb-01a__card">
        <input class="crb-01a__input" type="radio" name="crb-01a" value="express">
        <span class="crb-01a__dot" aria-hidden="true"></span>
        <svg class="crb-01a__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg>
        <span class="crb-01a__title">Express</span>
        <span class="crb-01a__meta">2–3 business days</span>
        <span class="crb-01a__price">$9</span>
      </label>
      <label class="crb-01a__card">
        <input class="crb-01a__input" type="radio" name="crb-01a" value="overnight">
        <span class="crb-01a__dot" aria-hidden="true"></span>
        <svg class="crb-01a__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>
        <span class="crb-01a__title">Overnight</span>
        <span class="crb-01a__meta">Next business day</span>
        <span class="crb-01a__price">$24</span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-01-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-01-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-01a,
.crb-01a *,
.crb-01a *::before,
.crb-01a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-01a {
  --accent: oklch(0.55 0.2 262);
  --ink: #1c2130;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f3f4fa;
}

.crb-01a__group {
  border: none;
}

.crb-01a__legend {
  font-size: 26px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
}

.crb-01a__hint {
  margin-top: 6px;
  font-size: 14px;
  color: #6a7186;
}

.crb-01a__cards {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 26px;
}

.crb-01a__card {
  position: relative;
  width: 206px;
  display: grid;
  gap: 4px;
  padding: 24px 20px 20px;
  background: #fff;
  border: 2px solid #e3e6f0;
  border-radius: 18px;
  cursor: pointer;
  transition: border-color .25s,transform .25s,box-shadow .25s;
}

.crb-01a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-01a__icon {
  width: 26px;
  height: 26px;
  color: #8b93a9;
  margin-bottom: 8px;
  transition: color .25s;
}

.crb-01a__title {
  font-size: 16px;
  font-weight: 700;
  color: var(--ink);
}

.crb-01a__meta {
  font-size: 13px;
  color: #6a7186;
}

.crb-01a__price {
  margin-top: 10px;
  font-size: 15px;
  font-weight: 750;
  color: var(--ink);
}

.crb-01a__dot {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid #ccd2e2;
  display: grid;
  place-items: center;
  transition: border-color .25s,background .25s;
}

.crb-01a__dot::after {
  content: "";
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #fff;
  transform: scale(0);
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
}

.crb-01a__card:hover {
  border-color: color-mix(in oklab,var(--accent) 40%,#e3e6f0);
  transform: translateY(-2px);
}

.crb-01a__card:has(.crb-01a__input:checked) {
  border-color: var(--accent);
  transform: translateY(-3px);
  box-shadow: 0 16px 30px -18px color-mix(in oklab,var(--accent) 60%,transparent);
}

.crb-01a__card:has(.crb-01a__input:checked) .crb-01a__icon {
  color: var(--accent);
}

.crb-01a__card:has(.crb-01a__input:checked) .crb-01a__dot {
  background: var(--accent);
  border-color: var(--accent);
}

.crb-01a__card:has(.crb-01a__input:checked) .crb-01a__dot::after {
  transform: scale(1);
}

.crb-01a__card:has(.crb-01a__input:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-01a__card,
    .crb-01a__dot,
    .crb-01a__dot::after,
    .crb-01a__icon {
    transition: none;
  }

  .crb-01a__card:hover,
    .crb-01a__card:has(.crb-01a__input:checked) {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the whole card is a <label> around a hidden radio; :has(input:checked) styles the parent card, and :has(input:focus-visible) re-projects the keyboard focus ring onto the card. */
```
