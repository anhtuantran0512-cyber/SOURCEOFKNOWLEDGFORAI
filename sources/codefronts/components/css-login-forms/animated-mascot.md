---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/animated-mascot/"
title: "Animated Mascot"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A playful character sits above the form and reacts to the user: its eyes follow the email field and its hands shoot up to cover its eyes the moment the…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Mascot
Source: https://codefronts.com/components/css-login-forms/animated-mascot/

A playful character sits above the form and reacts to the user: its eyes follow the email field and its hands shoot up to cover its eyes the moment the password field is focused — the friendly, conversion-boosting login, all in CSS.
## HTML
```html
<section class="lf-17">
  <form class="lf-17__card" novalidate>
    <div class="lf-17__mascot" aria-hidden="true">
      <svg viewBox="0 0 120 120">
        <circle class="lf-17__body" cx="60" cy="60" r="44"/>
        <circle class="lf-17__ear" cx="30" cy="26" r="12"/><circle class="lf-17__ear" cx="90" cy="26" r="12"/>
        <circle class="lf-17__eye" cx="46" cy="56" r="7"/><circle class="lf-17__eye" cx="74" cy="56" r="7"/>
        <ellipse class="lf-17__nose" cx="60" cy="72" rx="7" ry="5"/>
        <path class="lf-17__arm lf-17__arm--l" d="M22 96 q10 -14 26 -8"/>
        <path class="lf-17__arm lf-17__arm--r" d="M98 96 q-10 -14 -26 -8"/>
      </svg>
    </div>
    <h1 class="lf-17__h">Hey there!</h1>
    <label class="lf-17__field lf-17__field--email"><span class="lf-17__label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
    <label class="lf-17__field lf-17__field--pw"><span class="lf-17__label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
    <button class="lf-17__submit" type="submit">Log in</button>
  </form>
</section>
```
## CSS
```css
.lf-17,
.lf-17 *,
.lf-17 *::before,
.lf-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-17 {
  --accent: oklch(0.62 0.17 40);
  --radius: 12px;
  --field-h: 48px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #fdf3ea;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-17__card {
  position: relative;
  width: min(340px,100%);
  background: #fff;
  border: 1px solid #f0e2d5;
  border-radius: 20px;
  padding: 64px 30px 32px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  box-shadow: 0 24px 56px -38px rgba(120,60,20,.5);
}

.lf-17__mascot {
  position: absolute;
  top: -46px;
  left: 50%;
  transform: translateX(-50%);
  width: 96px;
  height: 96px;
}

.lf-17__mascot svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}

.lf-17__body {
  fill: oklch(0.7 0.13 55);
}

.lf-17__ear {
  fill: oklch(0.66 0.14 50);
}

.lf-17__eye {
  fill: #2a1a10;
  transition: transform .2s;
}

.lf-17__nose {
  fill: #3a2418;
}

.lf-17__arm {
  stroke: oklch(0.66 0.14 50);
  stroke-width: 12;
  stroke-linecap: round;
  fill: none;
  transform-origin: center;
  transition: transform .28s cubic-bezier(.4,0,.2,1);
}

.lf-17__h {
  font-size: 22px;
  font-weight: 700;
  color: #4a2c15;
  text-align: center;
}

.lf-17__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-17__label {
  font-size: 13px;
  font-weight: 600;
  color: #7a5638;
}

.lf-17__field input {
  height: var(--field-h);
  border: 1.5px solid #ecd9c7;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #4a2c15;
  background: #fffdfb;
  transition: border-color .18s,box-shadow .18s;
}

.lf-17__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.62 0.17 40/.18);
}

.lf-17__submit {
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

.lf-17__submit:hover {
  filter: brightness(1.06);
}

.lf-17__submit:active {
  transform: scale(.985);
}

.lf-17__submit:focus-visible {
  outline: 3px solid oklch(0.62 0.17 40/.5);
  outline-offset: 2px;
}

.lf-17__field--email:focus-within ~ * .lf-17__eye,
.lf-17__card:has(.lf-17__field--email:focus-within) .lf-17__eye {
  transform: translateY(3px);
}

.lf-17__card:has(.lf-17__field--pw:focus-within) .lf-17__arm--l {
  transform: rotate(-62deg) translate(6px,-30px);
}

.lf-17__card:has(.lf-17__field--pw:focus-within) .lf-17__arm--r {
  transform: rotate(62deg) translate(-6px,-30px);
}

.lf-17__card:has(.lf-17__field--pw:focus-within) .lf-17__eye {
  transform: scaleY(.15);
}

@media (prefers-reduced-motion: reduce) {
  .lf-17__arm,
    .lf-17__eye {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :has() + :focus-within move the mascot's SVG arms and eyes on field focus. */
```
