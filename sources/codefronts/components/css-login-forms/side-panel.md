---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/side-panel/"
title: "Side Panel"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "Log-in as a slide-over: clicking Sign in glides a panel in from the right edge over a dimmed backdrop, without routing away from the active storefront page —…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Side Panel
Source: https://codefronts.com/components/css-login-forms/side-panel/

Log-in as a slide-over: clicking Sign in glides a panel in from the right edge over a dimmed backdrop, without routing away from the active storefront page — the e-commerce and content-hub pattern.
## HTML
```html
<section class="lf-15">
  <input type="checkbox" class="lf-15__toggle" id="lf-15-open" aria-label="Open sign-in panel">
  <div class="lf-15__page">
    <div class="lf-15__nav"><span class="lf-15__logo">◈ Marketplace</span>
      <label class="lf-15__trigger" for="lf-15-open">Sign in</label></div>
    <p class="lf-15__hint" aria-hidden="true">Your storefront stays put behind the panel.</p>
  </div>
  <label class="lf-15__backdrop" for="lf-15-open" aria-label="Close sign-in panel"></label>
  <div class="lf-15__panel" role="dialog" aria-label="Sign in">
    <label class="lf-15__close" for="lf-15-open" aria-label="Close">×</label>
    <form class="lf-15__form" novalidate>
      <h2 class="lf-15__h">Welcome back</h2>
      <label class="lf-15__field"><span class="lf-15__label">Email</span><input type="email" autocomplete="email" placeholder="[email protected]" required></label>
      <label class="lf-15__field"><span class="lf-15__label">Password</span><input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
      <button class="lf-15__submit" type="submit">Sign in</button>
    </form>
  </div>
</section>
```
## CSS
```css
.lf-15,
.lf-15 *,
.lf-15 *::before,
.lf-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-15 {
  --accent: oklch(0.55 0.15 165);
  --radius: 11px;
  --field-h: 48px;
  position: relative;
  overflow: hidden;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #f2f5f3;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lf-15__toggle {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.lf-15__page {
  width: 100%;
  height: 100%;
  padding: 26px;
}

.lf-15__nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.lf-15__logo {
  font-size: 17px;
  font-weight: 700;
  color: #173a2c;
}

.lf-15__trigger {
  padding: 9px 18px;
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: filter .16s;
}

.lf-15__trigger:hover {
  filter: brightness(1.06);
}

.lf-15__hint {
  margin-top: 40vh;
  text-align: center;
  color: #8ba296;
  font-size: 14px;
}

.lf-15__backdrop {
  position: absolute;
  inset: 0;
  background: rgba(10,30,20,.45);
  opacity: 0;
  pointer-events: none;
  transition: opacity .35s;
  cursor: pointer;
  z-index: 5;
}

.lf-15__panel {
  position: absolute;
  top: 0;
  right: 0;
  height: 100%;
  width: min(360px,92%);
  z-index: 6;
  background: #fff;
  padding: 32px 28px;
  box-shadow: -20px 0 60px -30px rgba(10,40,25,.55);
  transform: translateX(100%);
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.lf-15__close {
  position: absolute;
  top: 14px;
  right: 16px;
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  font-size: 24px;
  color: #5a6b62;
  cursor: pointer;
  line-height: 1;
}

.lf-15__close:hover {
  background: #eef2ef;
}

.lf-15__toggle:checked ~ .lf-15__backdrop {
  opacity: 1;
  pointer-events: auto;
}

.lf-15__toggle:checked ~ .lf-15__panel {
  transform: translateX(0);
}

.lf-15__toggle:focus-visible ~ .lf-15__panel {
  outline: 3px solid var(--accent);
  outline-offset: -4px;
}

.lf-15__form {
  margin-top: 26px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.lf-15__h {
  font-size: 23px;
  font-weight: 700;
  color: #173a2c;
}

.lf-15__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-15__label {
  font-size: 13px;
  font-weight: 600;
  color: #3d5a4c;
}

.lf-15__field input {
  height: var(--field-h);
  border: 1.5px solid #d3ded7;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #173a2c;
  background: #fbfdfc;
  transition: border-color .18s,box-shadow .18s;
}

.lf-15__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.15 165/.18);
}

.lf-15__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: filter .18s,transform .12s;
}

.lf-15__submit:hover {
  filter: brightness(1.06);
}

.lf-15__submit:active {
  transform: scale(.985);
}

.lf-15__submit:focus-visible {
  outline: 3px solid oklch(0.55 0.15 165/.5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-15__panel,
    .lf-15__backdrop {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a fixed panel slides in on a checkbox :checked; the backdrop label closes it. */
```
