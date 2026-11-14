---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/dark-mode-glowing-radio-button/"
title: "Dark Mode Glowing Radio Button"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Radio buttons designed for dark UI: each option is a slim dark row whose custom radio ignites with a layered cyan glow when checked — an inner core, a soft…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Glowing Radio Button
Source: https://codefronts.com/components/css-radio-buttons/dark-mode-glowing-radio-button/

Radio buttons designed for dark UI: each option is a slim dark row whose custom radio ignites with a layered cyan glow when checked — an inner core, a soft halo and a faint ambient bloom that breathes with a slow pulse. The look developers want for dark-mode dashboards, dev tools and gaming settings.
## HTML
```html
<div class="crb-04-group">
<section class="crb-04a" aria-label="Dark mode glowing radio buttons">
  <fieldset class="crb-04a__group">
    <legend class="crb-04a__legend">Terminal theme</legend>
    <div class="crb-04a__list">
      <label class="crb-04a__row">
        <input class="crb-04a__input" type="radio" name="crb-04a" value="midnight" checked>
        <span class="crb-04a__radio" aria-hidden="true"></span>
        <span class="crb-04a__name">Midnight</span>
        <span class="crb-04a__meta">OLED black</span>
      </label>
      <label class="crb-04a__row">
        <input class="crb-04a__input" type="radio" name="crb-04a" value="dim">
        <span class="crb-04a__radio" aria-hidden="true"></span>
        <span class="crb-04a__name">Dim</span>
        <span class="crb-04a__meta">Soft slate</span>
      </label>
      <label class="crb-04a__row">
        <input class="crb-04a__input" type="radio" name="crb-04a" value="auto">
        <span class="crb-04a__radio" aria-hidden="true"></span>
        <span class="crb-04a__name">Sync with system</span>
        <span class="crb-04a__meta">Auto</span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-04-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-04-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-04a,
.crb-04a *,
.crb-04a *::before,
.crb-04a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-04a {
  --glow: oklch(0.8 0.15 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 120% at 50% 0%,#101625,#07090f);
}

.crb-04a__group {
  border: none;
  width: min(400px,100%);
}

.crb-04a__legend {
  font-size: 24px;
  font-weight: 750;
  color: #eef2fb;
  letter-spacing: -.02em;
}

.crb-04a__list {
  display: grid;
  gap: 10px;
  margin-top: 20px;
}

.crb-04a__row {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 14px;
  min-height: 56px;
  padding: 0 18px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.09);
  border-radius: 13px;
  cursor: pointer;
  transition: border-color .25s,background .25s;
}

.crb-04a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-04a__radio {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid #4a5470;
  display: grid;
  place-items: center;
  transition: border-color .25s;
}

.crb-04a__radio::after {
  content: "";
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--glow);
  transform: scale(0);
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
}

.crb-04a__name {
  font-size: 15px;
  font-weight: 650;
  color: #dfe5f3;
}

.crb-04a__meta {
  font-size: 12.5px;
  color: #6a7490;
}

.crb-04a__row:hover {
  border-color: color-mix(in oklab,var(--glow) 40%,transparent);
}

.crb-04a__row:has(.crb-04a__input:checked) {
  border-color: color-mix(in oklab,var(--glow) 65%,transparent);
  background: color-mix(in oklab,var(--glow) 7%,transparent);
}

.crb-04a__row:has(.crb-04a__input:checked) .crb-04a__radio {
  border-color: var(--glow);
  animation: crb-04a-breathe 2.6s ease-in-out infinite;
}

.crb-04a__row:has(.crb-04a__input:checked) .crb-04a__radio::after {
  transform: scale(1);
}

.crb-04a__row:has(.crb-04a__input:focus-visible) {
  outline: 3px solid var(--glow);
  outline-offset: 2px;
}

@keyframes crb-04a-breathe {
  0%,
    100% {
    box-shadow: 0 0 4px var(--glow),0 0 14px color-mix(in oklab,var(--glow) 55%,transparent),0 0 34px color-mix(in oklab,var(--glow) 30%,transparent);
  }

  50% {
    box-shadow: 0 0 6px var(--glow),0 0 22px color-mix(in oklab,var(--glow) 65%,transparent),0 0 48px color-mix(in oklab,var(--glow) 40%,transparent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .crb-04a__radio,
    .crb-04a__radio::after,
    .crb-04a__row {
    transition: none;
  }

  .crb-04a__row:has(.crb-04a__input:checked) .crb-04a__radio {
    animation: none;
    box-shadow: 0 0 6px var(--glow),0 0 18px color-mix(in oklab,var(--glow) 55%,transparent);
  }
}
```

## JavaScript
```js
/* No JavaScript — three stacked box-shadow layers on the checked indicator, breathing via a slow keyframe; :has() tints the row. */
```
