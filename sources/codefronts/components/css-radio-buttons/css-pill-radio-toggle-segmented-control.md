---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/css-pill-radio-toggle-segmented-control/"
title: "CSS Pill Radio Toggle (Segmented Control)"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "An iOS-style segmented control built from radio buttons: a rounded pill track with a white thumb that glides under whichever option you pick."
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pill Radio Toggle (Segmented Control)
Source: https://codefronts.com/components/css-radio-buttons/css-pill-radio-toggle-segmented-control/

An iOS-style segmented control built from radio buttons: a rounded pill track with a white thumb that glides under whichever option you pick. The classic billing toggle (Monthly / Yearly + save badge) — pure CSS, the sliding thumb is driven entirely by :has() and nth-child, no JavaScript state.
## HTML
```html
<div class="crb-02-group">
<section class="crb-02a" aria-label="Pill radio toggle segmented control">
  <fieldset class="crb-02a__group">
    <legend class="crb-02a__legend">Billing period</legend>
    <div class="crb-02a__track">
      <label class="crb-02a__seg">
        <input class="crb-02a__input" type="radio" name="crb-02a" value="monthly" checked>
        <span class="crb-02a__text">Monthly</span>
      </label>
      <label class="crb-02a__seg">
        <input class="crb-02a__input" type="radio" name="crb-02a" value="yearly">
        <span class="crb-02a__text">Yearly <em class="crb-02a__badge">−20%</em></span>
      </label>
    </div>
    <p class="crb-02a__hint">Arrow keys work too — it's a native radio group</p>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-02-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-02-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-02a,
.crb-02a *,
.crb-02a *::before,
.crb-02a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-02a {
  --accent: oklch(0.55 0.19 155);
  --track: #e9ebf2;
  --ink: #1c2130;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f7f8fb;
}

.crb-02a__group {
  border: none;
  display: grid;
  justify-items: center;
  gap: 18px;
}

.crb-02a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
  text-align: center;
  margin-bottom: 4px;
}

.crb-02a__track {
  position: relative;
  isolation: isolate;
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  padding: 5px;
  background: var(--track);
  border-radius: 9999px;
  box-shadow: inset 0 1px 3px rgba(20,25,45,.08);
}

.crb-02a__track::before {
  content: "";
  position: absolute;
  z-index: 0;
  top: 5px;
  left: 5px;
  width: calc(50% - 5px);
  height: calc(100% - 10px);
  background: #fff;
  border-radius: 9999px;
  box-shadow: 0 2px 8px rgba(20,25,45,.16);
  transition: transform .35s cubic-bezier(.22,1,.36,1);
}

.crb-02a__track:has(.crb-02a__seg:nth-child(2) .crb-02a__input:checked)::before {
  transform: translateX(100%);
}

.crb-02a__seg {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  min-width: 150px;
  min-height: 46px;
  padding: 0 22px;
  border-radius: 9999px;
  cursor: pointer;
}

.crb-02a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-02a__text {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 650;
  color: #69708a;
  transition: color .3s;
}

.crb-02a__badge {
  font-style: normal;
  font-size: 11px;
  font-weight: 750;
  padding: 2px 8px;
  border-radius: 9999px;
  background: color-mix(in oklab,var(--accent) 16%,white);
  color: var(--accent);
}

.crb-02a__seg:has(.crb-02a__input:checked) .crb-02a__text {
  color: var(--ink);
}

.crb-02a__seg:has(.crb-02a__input:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.crb-02a__hint {
  font-size: 13px;
  color: #8a90a5;
}

@media (prefers-reduced-motion: reduce) {
  .crb-02a__track::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the white thumb is a ::before on the track; :has(label:nth-child(2) input:checked) translates it 100% so the slide is pure CSS state. */
```
