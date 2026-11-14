---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/css-input-with-icon-inside-and-floating-label/"
title: "CSS Input with Icon Inside and Floating Label"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "Search, email and username fields with an inline SVG icon that never collides with the floating label: the label rests beside the icon, then floats up and…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Input with Icon Inside and Floating Label
Source: https://codefronts.com/components/css-floating-label-inputs/css-input-with-icon-inside-and-floating-label/

Search, email and username fields with an inline SVG icon that never collides with the floating label: the label rests beside the icon, then floats up and OVER it, while the icon tints to the accent on focus — the layout puzzle that breaks most copy-pasted floating label snippets. Variation: an ICON HANDOFF — on focus the icon spins out to the left while the label slides into its vacated spot, a two-actor choreography.
## HTML
```html
<section class="flb-12" aria-label="Floating label with icon demo">
  <form class="flb-12__form" novalidate>
    <h3 class="flb-12__title">Find your team</h3>
    <div class="flb-12__field">
      <svg class="flb-12__icon" aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="9" cy="9" r="6"></circle><path d="m14 14 4 4"></path></svg>
      <input class="flb-12__input" type="search" id="flb-12-search" name="q" placeholder=" ">
      <label class="flb-12__label" for="flb-12-search">Search workspaces</label>
    </div>
    <div class="flb-12__field">
      <svg class="flb-12__icon" aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="16" height="12" rx="2"></rect><path d="m2.5 5.5 7.5 6 7.5-6"></path></svg>
      <input class="flb-12__input" type="email" id="flb-12-email" name="email" placeholder=" " autocomplete="email">
      <label class="flb-12__label" for="flb-12-email">Work email</label>
    </div>
    <div class="flb-12__field">
      <svg class="flb-12__icon" aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="10" cy="7" r="3.5"></circle><path d="M3.5 17c1.2-3 3.6-4.5 6.5-4.5s5.3 1.5 6.5 4.5"></path></svg>
      <input class="flb-12__input" type="text" id="flb-12-user" name="username" placeholder=" " autocomplete="username">
      <label class="flb-12__label" for="flb-12-user">Username</label>
    </div>
    <button class="flb-12__btn" type="button">Continue</button>
  </form>
</section>
```
## CSS
```css
.flb-12,
.flb-12 *,
.flb-12 *::before,
.flb-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-12 {
  --accent: oklch(0.55 0.17 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f0f7;
  padding: 40px 20px;
}

.flb-12__form {
  width: min(390px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 32px 30px;
  box-shadow: 0 24px 60px -32px rgba(50,30,80,.35);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.flb-12__title {
  font-size: 23px;
  font-weight: 800;
  color: #221c30;
  letter-spacing: -.02em;
}

.flb-12__field {
  position: relative;
  color: #948da8;
}

.flb-12__field:focus-within {
  color: var(--accent);
}

.flb-12__icon {
  position: absolute;
  left: 15px;
  top: 50%;
  translate: 0 -50%;
  pointer-events: none;
  transition: color .2s,opacity .22s,transform .25s;
}

.flb-12__field:focus-within .flb-12__icon {
  opacity: 0;
  transform: translateX(-10px) rotate(-25deg);
}

.flb-12__input {
  width: 100%;
  height: 56px;
  padding: 22px 16px 6px 46px;
  font-size: 16px;
  color: #221c30;
  background: #fff;
  border: 1.5px solid #ded9ea;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
  appearance: none;
  -webkit-appearance: none;
}

.flb-12__input::-webkit-search-cancel-button {
  display: none;
}

.flb-12__input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.17 300 / .13);
}

.flb-12__label {
  position: absolute;
  left: 46px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #8b839e;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .18s,color .18s;
}

.flb-12__input:focus ~ .flb-12__label,
.flb-12__input:not(:placeholder-shown) ~ .flb-12__label {
  transform: translate(-30px,-13px) scale(.72);
}

.flb-12__input:focus ~ .flb-12__label {
  color: var(--accent);
}

.flb-12__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s;
}

.flb-12__btn:hover {
  filter: brightness(1.1);
}

.flb-12__btn:focus-visible,
.flb-12__input:focus-visible {
  outline: 3px solid oklch(0.55 0.17 300 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-12__label,
    .flb-12__input,
    .flb-12__icon {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the label indents past the icon at rest, then translates left AND up on float so it re-aligns with the field edge above the icon. Icons are aria-hidden currentColor SVGs tinted by :focus-within. */
```
