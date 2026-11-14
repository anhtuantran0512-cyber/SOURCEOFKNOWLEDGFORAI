---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/compact-modal/"
title: "Compact Modal"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A light pop-up auth dialog for media and membership sites: a small centred card scales in over blurred page content when triggered — accessibility-first,…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Compact Modal
Source: https://codefronts.com/components/css-login-forms/compact-modal/

A light pop-up auth dialog for media and membership sites: a small centred card scales in over blurred page content when triggered — accessibility-first, with proper focus rings and a semantic dialog structure.
## HTML
```html
<section class="lf-18">
  <input type="checkbox" class="lf-18__toggle" id="lf-18-open" aria-label="Open login dialog" checked>
  <div class="lf-18__page">
    <p class="lf-18__article" aria-hidden="true">Members-only story · 4 min read</p>
    <label class="lf-18__trigger" for="lf-18-open">Log in to read</label>
  </div>
  <div class="lf-18__overlay">
    <label class="lf-18__scrim" for="lf-18-open" aria-label="Close dialog"></label>
    <form class="lf-18__modal" role="dialog" aria-modal="true" aria-label="Log in" novalidate>
      <label class="lf-18__x" for="lf-18-open" aria-label="Close">×</label>
      <h2 class="lf-18__h">Log in</h2>
      <p class="lf-18__sub">Continue reading with your membership.</p>
      <label class="lf-18__field"><span class="lf-18__label">Email</span><input type="email" autocomplete="email" placeholder="[email protected]" required></label>
      <label class="lf-18__field"><span class="lf-18__label">Password</span><input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
      <button class="lf-18__submit" type="submit">Log in</button>
    </form>
  </div>
</section>
```
## CSS
```css
.lf-18,
.lf-18 *,
.lf-18 *::before,
.lf-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-18 {
  --accent: oklch(0.55 0.2 15);
  --radius: 12px;
  --field-h: 46px;
  position: relative;
  overflow: hidden;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #f3f2f4;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lf-18__toggle {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.lf-18__page {
  text-align: center;
  padding: 24px;
  transition: filter .35s;
}

.lf-18__article {
  color: #9a97a0;
  font-size: 14px;
  margin-bottom: 16px;
}

.lf-18__trigger {
  padding: 10px 20px;
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}

.lf-18__toggle:checked ~ .lf-18__page {
  filter: blur(4px);
}

.lf-18__overlay {
  position: absolute;
  inset: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s;
}

.lf-18__scrim {
  position: absolute;
  inset: 0;
  background: rgba(20,10,18,.4);
  cursor: pointer;
}

.lf-18__toggle:checked ~ .lf-18__overlay {
  opacity: 1;
  pointer-events: auto;
}

.lf-18__modal {
  position: relative;
  width: min(340px,100%);
  background: #fff;
  border-radius: 18px;
  padding: 30px 28px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: 0 30px 70px -34px rgba(20,10,18,.6);
  transform: scale(.94);
  transition: transform .3s cubic-bezier(.34,1.4,.5,1);
}

.lf-18__toggle:checked ~ .lf-18__overlay .lf-18__modal {
  transform: scale(1);
}

.lf-18__x {
  position: absolute;
  top: 12px;
  right: 14px;
  width: 32px;
  height: 32px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  font-size: 23px;
  line-height: 1;
  color: #8a8790;
  cursor: pointer;
}

.lf-18__x:hover {
  background: #f2f0f3;
}

.lf-18__h {
  font-size: 22px;
  font-weight: 700;
  color: #1c1720;
}

.lf-18__sub {
  font-size: 13.5px;
  color: #847f8c;
  margin-top: -6px;
  margin-bottom: 4px;
}

.lf-18__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-18__label {
  font-size: 13px;
  font-weight: 600;
  color: #453d4d;
}

.lf-18__field input {
  height: var(--field-h);
  border: 1.5px solid #e2dee6;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 14.5px;
  color: #1c1720;
  background: #fbfafc;
  transition: border-color .18s,box-shadow .18s;
}

.lf-18__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.2 15/.16);
}

.lf-18__submit {
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

.lf-18__submit:hover {
  filter: brightness(1.07);
}

.lf-18__submit:active {
  transform: scale(.985);
}

.lf-18__submit:focus-visible {
  outline: 3px solid oklch(0.55 0.2 15/.5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-18__modal,
    .lf-18__overlay,
    .lf-18__page {
    transition: opacity .2s;
  }

  .lf-18__toggle:checked ~ .lf-18__overlay .lf-18__modal {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a checkbox opens a Flexbox-centred dialog that scales + fades in over a blurred page. */
```
