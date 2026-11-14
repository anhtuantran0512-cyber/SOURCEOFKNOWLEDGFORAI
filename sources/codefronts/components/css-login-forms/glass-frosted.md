---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/glass-frosted/"
title: "Glass Frosted"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The glassmorphism login for high-end creative apps: a frosted translucent card floating over a rich image-style backdrop, with a real blur, a fine light-edge…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Frosted
Source: https://codefronts.com/components/css-login-forms/glass-frosted/

The glassmorphism login for high-end creative apps: a frosted translucent card floating over a rich image-style backdrop, with a real blur, a fine light-edge border, and text layers kept readable.
## HTML
```html
<section class="lf-19">
  <div class="lf-19__bg" aria-hidden="true"></div>
  <form class="lf-19__glass" novalidate>
    <h1 class="lf-19__h">Sign in</h1>
    <p class="lf-19__sub">Welcome back to Studio.</p>
    <label class="lf-19__field"><span class="lf-19__label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
    <label class="lf-19__field"><span class="lf-19__label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
    <button class="lf-19__submit" type="submit">Enter studio</button>
    <p class="lf-19__foot"><a href="#">Forgot password?</a></p>
  </form>
</section>
```
## CSS
```css
.lf-19,
.lf-19 *,
.lf-19 *::before,
.lf-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-19 {
  --accent: oklch(0.72 0.16 210);
  --radius: 14px;
  --field-h: 48px;
  position: relative;
  overflow: hidden;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-19__bg {
  position: absolute;
  inset: 0;
  background: radial-gradient(50% 60% at 20% 25%,oklch(0.72 0.2 20),transparent 60%), radial-gradient(55% 55% at 80% 20%,oklch(0.7 0.19 300),transparent 60%), radial-gradient(60% 60% at 60% 90%,oklch(0.72 0.18 210),transparent 60%), linear-gradient(135deg,#1a1440,#0e2036);
}

.lf-19__glass {
  position: relative;
  z-index: 1;
  width: min(360px,100%);
  border-radius: 22px;
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  color: #fff;
  background: rgba(255,255,255,.12);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: 0 30px 70px -30px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.35);
}

.lf-19__h {
  font-size: 26px;
  font-weight: 700;
  text-shadow: 0 1px 12px rgba(0,0,0,.25);
}

.lf-19__sub {
  font-size: 14px;
  color: rgba(255,255,255,.82);
  margin-top: -6px;
  margin-bottom: 4px;
}

.lf-19__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-19__label {
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,.9);
}

.lf-19__field input {
  height: var(--field-h);
  border: 1px solid rgba(255,255,255,.35);
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #fff;
  background: rgba(255,255,255,.14);
  transition: border-color .18s,box-shadow .18s,background .18s;
}

.lf-19__field input::placeholder {
  color: rgba(255,255,255,.6);
}

.lf-19__field input:focus-visible {
  outline: none;
  border-color: #fff;
  background: rgba(255,255,255,.22);
  box-shadow: 0 0 0 4px rgba(255,255,255,.22);
}

.lf-19__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: rgba(255,255,255,.92);
  color: #132038;
  font-size: 15px;
  font-weight: 700;
  transition: filter .18s,transform .12s;
}

.lf-19__submit:hover {
  filter: brightness(1.05);
}

.lf-19__submit:active {
  transform: scale(.985);
}

.lf-19__submit:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lf-19__foot {
  text-align: center;
  font-size: 13px;
}

.lf-19__foot a {
  color: #fff;
  text-decoration: none;
}

.lf-19__foot a:hover {
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .lf-19 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — backdrop-filter blur over a translucent card; text kept high-contrast for legibility. */
```
