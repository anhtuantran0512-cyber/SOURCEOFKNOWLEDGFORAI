---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/avatar-picker/"
title: "User Profile Avatar Selector"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "The \"who's watching?\" screen as a proper form control: a row of profile avatars where the active profile scales up, gains a bright ring and full colour,…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: User Profile Avatar Selector
Source: https://codefronts.com/components/css-radio-buttons/avatar-picker/

The "who's watching?" screen as a proper form control: a row of profile avatars where the active profile scales up, gains a bright ring and full colour, while the others rest slightly dimmed. Real photos, real radio buttons, real names — the streaming-app pattern for account and reviewer pickers.
## HTML
```html
<div class="crb-21-group">
<section class="crb-21a" aria-label="User profile avatar selector">
  <fieldset class="crb-21a__group">
    <legend class="crb-21a__legend">Who's watching?</legend>
    <div class="crb-21a__row">
      <label class="crb-21a__opt">
        <input class="crb-21a__input" type="radio" name="crb-21a" value="amara" checked>
        <img class="crb-21a__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=300&q=80&auto=format&fit=crop" alt="Amara" loading="lazy">
        <span class="crb-21a__name">Amara</span>
      </label>
      <label class="crb-21a__opt">
        <input class="crb-21a__input" type="radio" name="crb-21a" value="jonas">
        <img class="crb-21a__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&q=80&auto=format&fit=crop" alt="Jonas" loading="lazy">
        <span class="crb-21a__name">Jonas</span>
      </label>
      <label class="crb-21a__opt">
        <input class="crb-21a__input" type="radio" name="crb-21a" value="sofia">
        <img class="crb-21a__img" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300&q=80&auto=format&fit=crop" alt="Sofia" loading="lazy">
        <span class="crb-21a__name">Sofia</span>
      </label>
      <label class="crb-21a__opt">
        <input class="crb-21a__input" type="radio" name="crb-21a" value="mateo">
        <img class="crb-21a__img" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300&q=80&auto=format&fit=crop" alt="Mateo" loading="lazy">
        <span class="crb-21a__name">Mateo</span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-21-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-21-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-21a,
.crb-21a *,
.crb-21a *::before,
.crb-21a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-21a {
  --accent: oklch(0.72 0.17 25);
  --size: 92px;
  --bg: #101014;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: var(--bg);
}

.crb-21a__group {
  border: none;
}

.crb-21a__legend {
  font-size: 28px;
  font-weight: 750;
  color: #f2f2f5;
  letter-spacing: -.02em;
  text-align: center;
}

.crb-21a__row {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;
  margin-top: 34px;
}

.crb-21a__opt {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 12px;
  cursor: pointer;
}

.crb-21a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-21a__img {
  width: var(--size);
  height: var(--size);
  border-radius: 50%;
  object-fit: cover;
  filter: saturate(.7) brightness(.8);
  transform: scale(1);
  transition: transform .35s cubic-bezier(.34,1.56,.64,1),filter .35s,box-shadow .35s;
}

.crb-21a__name {
  font-size: 14.5px;
  font-weight: 650;
  color: #84848f;
  transition: color .3s;
}

.crb-21a__opt:hover .crb-21a__img {
  filter: saturate(1) brightness(1);
}

.crb-21a__opt:has(.crb-21a__input:checked) .crb-21a__img {
  filter: none;
  transform: scale(1.12);
  box-shadow: 0 0 0 4px var(--bg),0 0 0 7px var(--accent),0 16px 34px -12px rgba(0,0,0,.8);
}

.crb-21a__opt:has(.crb-21a__input:checked) .crb-21a__name {
  color: #fff;
}

.crb-21a__opt:has(.crb-21a__input:focus-visible) .crb-21a__img {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-21a__img {
    transition: filter .2s,box-shadow .2s;
  }

  .crb-21a__opt:has(.crb-21a__input:checked) .crb-21a__img {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a double box-shadow (background-gap ring + accent ring) marks the checked avatar; :has() also lifts the photo and removes its resting desaturation. */
```
