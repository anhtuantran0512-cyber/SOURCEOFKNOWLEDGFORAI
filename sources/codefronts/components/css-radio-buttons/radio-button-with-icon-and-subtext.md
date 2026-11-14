---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/radio-button-with-icon-and-subtext/"
title: "Radio Button with Icon and Subtext"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "The settings-page staple: a vertical radio option list where every row carries an icon tile, a title, and a one-line description — plus a proper custom radio…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Radio Button with Icon and Subtext
Source: https://codefronts.com/components/css-radio-buttons/radio-button-with-icon-and-subtext/

The settings-page staple: a vertical radio option list where every row carries an icon tile, a title, and a one-line description — plus a proper custom radio circle on the right. The exact pattern used for notification preferences, privacy levels and deployment targets in modern SaaS dashboards.
## HTML
```html
<div class="crb-03-group">
<section class="crb-03a" aria-label="Radio options with icon and description">
  <fieldset class="crb-03a__group">
    <legend class="crb-03a__legend">Notifications</legend>
    <div class="crb-03a__list">
      <label class="crb-03a__row">
        <input class="crb-03a__input" type="radio" name="crb-03a" value="all" checked>
        <span class="crb-03a__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6"/><path d="M10 19a2 2 0 0 0 4 0"/></svg></span>
        <span class="crb-03a__text"><span class="crb-03a__title">All activity</span><span class="crb-03a__desc">Every comment, mention and follow — delivered instantly.</span></span>
        <span class="crb-03a__radio" aria-hidden="true"></span>
      </label>
      <label class="crb-03a__row">
        <input class="crb-03a__input" type="radio" name="crb-03a" value="mentions">
        <span class="crb-03a__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-4 8"/></svg></span>
        <span class="crb-03a__text"><span class="crb-03a__title">Mentions only</span><span class="crb-03a__desc">Stay focused — only direct @mentions get through.</span></span>
        <span class="crb-03a__radio" aria-hidden="true"></span>
      </label>
      <label class="crb-03a__row">
        <input class="crb-03a__input" type="radio" name="crb-03a" value="muted">
        <span class="crb-03a__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5a3 3 0 0 1 6 0c3 1 3 4 3 6 0 2 1 4 1 4H5s1-2 1-4c0-2 0-5 3-6Z" opacity=".35"/><path d="m4 4 16 16"/></svg></span>
        <span class="crb-03a__text"><span class="crb-03a__title">Muted</span><span class="crb-03a__desc">Nothing until you turn notifications back on.</span></span>
        <span class="crb-03a__radio" aria-hidden="true"></span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-03-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-03-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-03a,
.crb-03a *,
.crb-03a *::before,
.crb-03a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-03a {
  --accent: oklch(0.58 0.2 285);
  --ink: #1d2233;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f5f5f9;
}

.crb-03a__group {
  border: none;
  width: min(460px,100%);
}

.crb-03a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
}

.crb-03a__list {
  display: grid;
  gap: 10px;
  margin-top: 20px;
}

.crb-03a__row {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 14px;
  padding: 16px;
  background: #fff;
  border: 1.5px solid #e5e7f0;
  border-radius: 14px;
  cursor: pointer;
  transition: border-color .25s,background .25s;
}

.crb-03a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-03a__tile {
  width: 42px;
  height: 42px;
  border-radius: 11px;
  display: grid;
  place-items: center;
  background: #eef0f6;
  color: #7c84a0;
  transition: background .25s,color .25s;
}

.crb-03a__tile svg {
  width: 22px;
  height: 22px;
}

.crb-03a__text {
  display: grid;
  gap: 2px;
}

.crb-03a__title {
  font-size: 15px;
  font-weight: 700;
  color: var(--ink);
}

.crb-03a__desc {
  font-size: 13px;
  line-height: 1.45;
  color: #6d7389;
}

.crb-03a__radio {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid #c7cddd;
  display: grid;
  place-items: center;
  transition: border-color .25s,background .25s;
}

.crb-03a__radio::after {
  content: "";
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #fff;
  transform: scale(0);
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
}

.crb-03a__row:hover {
  border-color: color-mix(in oklab,var(--accent) 35%,#e5e7f0);
}

.crb-03a__row:has(.crb-03a__input:checked) {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 5%,white);
}

.crb-03a__row:has(.crb-03a__input:checked) .crb-03a__tile {
  background: color-mix(in oklab,var(--accent) 14%,white);
  color: var(--accent);
}

.crb-03a__row:has(.crb-03a__input:checked) .crb-03a__radio {
  border-color: var(--accent);
  background: var(--accent);
}

.crb-03a__row:has(.crb-03a__input:checked) .crb-03a__radio::after {
  transform: scale(1);
}

.crb-03a__row:has(.crb-03a__input:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-03a__row,
    .crb-03a__tile,
    .crb-03a__radio,
    .crb-03a__radio::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a three-column grid label (icon tile / title+description / indicator); :has(input:checked) tints the row and springs the dot in. */
```
