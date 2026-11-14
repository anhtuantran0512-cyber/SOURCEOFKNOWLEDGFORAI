---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/dark-mode-glowing-input-submit-focus-states/"
title: "Dark Mode Glowing Input & Submit Focus States"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "A checkout-grade mini form where the glow is UX, not decoration: the email field breathes a violet halo on focus, flips to a green glow once the address is…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Glowing Input & Submit Focus States
Source: https://codefronts.com/components/css-glowing-border-buttons/dark-mode-glowing-input-submit-focus-states/

A checkout-grade mini form where the glow is UX, not decoration: the email field breathes a violet halo on focus, flips to a green glow once the address is valid and red only after you've actually typed something wrong — via :user-valid/:user-invalid — and the submit button answers with its own glow on hover and focus.
## HTML
```html
<section class="gbb-05" aria-label="Dark mode glowing form focus states demo">
  <form class="gbb-05__form" novalidate="">
    <label class="gbb-05__label" for="gbb-05-email">Work email</label>
    <input class="gbb-05__input" id="gbb-05-email" type="email" name="email" required placeholder="[email protected]" autocomplete="email">
    <button class="gbb-05__btn" type="button">Create account</button>
    <p class="gbb-05__hint">Glow turns green when the address parses &middot; red only after you type</p>
  </form>
</section>
```
## CSS
```css
.gbb-05,
.gbb-05 *,
.gbb-05 *::before,
.gbb-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-05 {
  --idle: oklch(0.68 0.18 292);
  --ok: oklch(0.78 0.15 158);
  --bad: oklch(0.68 0.2 22);
  --surface: oklch(0.17 0.015 285);
  --ease: cubic-bezier(0.16,1,0.3,1);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(55% 65% at 78% -5%,oklch(0.28 0.08 292 / .45),transparent 60%),radial-gradient(45% 55% at 12% 110%,oklch(0.24 0.06 200 / .3),transparent 60%),oklch(0.12 0.012 280);
}

.gbb-05 .gbb-05__form {
  width: min(360px,100%);
  display: grid;
  gap: 12px;
}

.gbb-05 .gbb-05__label {
  font: 600 11.5px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(255,255,255,.5);
}

.gbb-05 .gbb-05__input {
  --glow: var(--idle);
  height: 50px;
  padding: 0 16px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,.08);
  background: var(--surface);
  color: #f6f5ff;
  font: 400 15px 'Segoe UI',system-ui,sans-serif;
  caret-color: var(--glow);
  outline: none;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04),inset 0 0 0 1px rgba(255,255,255,.02);
  transition: border-color .35s var(--ease),box-shadow .35s var(--ease),background .35s var(--ease);
}

.gbb-05 .gbb-05__input::placeholder {
  color: rgba(255,255,255,.28);
}

.gbb-05 .gbb-05__input:focus-visible {
  border-color: color-mix(in oklab,var(--glow) 80%,transparent);
  background: color-mix(in oklab,var(--glow) 4%,var(--surface));
  box-shadow: inset 0 1px 0 color-mix(in oklab,var(--glow) 22%,transparent),0 0 0 1px color-mix(in oklab,var(--glow) 55%,transparent),0 0 0 5px color-mix(in oklab,var(--glow) 14%,transparent),0 6px 24px -4px color-mix(in oklab,var(--glow) 40%,transparent),0 0 44px color-mix(in oklab,var(--glow) 20%,transparent);
}

.gbb-05 .gbb-05__input:user-valid {
  --glow: var(--ok);
  border-color: color-mix(in oklab,var(--glow) 60%,transparent);
  box-shadow: inset 0 1px 0 color-mix(in oklab,var(--glow) 18%,transparent),0 0 0 1px color-mix(in oklab,var(--glow) 40%,transparent),0 0 24px -4px color-mix(in oklab,var(--glow) 35%,transparent);
}

.gbb-05 .gbb-05__input:user-invalid {
  --glow: var(--bad);
  border-color: color-mix(in oklab,var(--glow) 70%,transparent);
  box-shadow: inset 0 1px 0 color-mix(in oklab,var(--glow) 20%,transparent),0 0 0 1px color-mix(in oklab,var(--glow) 50%,transparent),0 0 0 4px color-mix(in oklab,var(--glow) 12%,transparent),0 0 28px -4px color-mix(in oklab,var(--glow) 40%,transparent);
}

.gbb-05 .gbb-05__btn {
  position: relative;
  margin-top: 6px;
  height: 50px;
  border: 1px solid color-mix(in oklab,var(--idle) 45%,transparent);
  border-radius: 12px;
  cursor: pointer;
  font: 600 15px 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .005em;
  color: #fff;
  background: linear-gradient(180deg,color-mix(in oklab,var(--idle) 82%,#000) 0%,color-mix(in oklab,var(--idle) 62%,#000) 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22),inset 0 -1px 0 rgba(0,0,0,.25),0 1px 0 rgba(0,0,0,.4),0 0 0 1px color-mix(in oklab,var(--idle) 35%,transparent),0 12px 28px -12px color-mix(in oklab,var(--idle) 60%,transparent),0 0 40px -8px color-mix(in oklab,var(--idle) 45%,transparent);
  transition: box-shadow .35s var(--ease),transform .25s var(--ease),background .35s var(--ease);
}

.gbb-05 .gbb-05__btn:hover {
  background: linear-gradient(180deg,color-mix(in oklab,var(--idle) 92%,#000) 0%,color-mix(in oklab,var(--idle) 72%,#000) 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.28),inset 0 -1px 0 rgba(0,0,0,.28),0 1px 0 rgba(0,0,0,.5),0 0 0 1px color-mix(in oklab,var(--idle) 55%,transparent),0 16px 34px -10px color-mix(in oklab,var(--idle) 70%,transparent),0 0 56px -6px color-mix(in oklab,var(--idle) 55%,transparent);
  transform: translateY(-1px);
}

.gbb-05 .gbb-05__btn:focus-visible {
  outline: 2px solid rgba(255,255,255,.85);
  outline-offset: 3px;
}

.gbb-05 .gbb-05__btn:active {
  transform: translateY(0);
  transition-duration: .1s;
}

.gbb-05 .gbb-05__hint {
  font: 400 11.5px/1.5 'Segoe UI',system-ui,sans-serif;
  color: rgba(255,255,255,.36);
  text-wrap: pretty;
  letter-spacing: .005em;
}

@media (prefers-reduced-motion: reduce) {
  .gbb-05 .gbb-05__input,
    .gbb-05 .gbb-05__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :focus-visible drives the halo; :user-valid / :user-invalid recolor it only after real user input (unlike :valid/:invalid). Submit is a no-op button so form doesn't navigate away in preview. */
```
