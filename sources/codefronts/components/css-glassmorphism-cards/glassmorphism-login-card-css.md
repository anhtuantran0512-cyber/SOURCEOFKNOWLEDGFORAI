---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-login-card-css/"
title: "Glassmorphism Login Card CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "The most-searched glass component, done properly: an aurora login card with floating labels driven by :placeholder-shown, and a split-panel version pairing a…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Login Card CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-login-card-css/

The most-searched glass component, done properly: an aurora login card with floating labels driven by :placeholder-shown, and a split-panel version pairing a vivid brand slab with a frosted form. Labels float, focus glows, errors have a home — all without a line of JS.
## HTML
```html
<div class="glz-06-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="glz-06a" aria-label="Glassmorphism login card demo">
  <form class="glz-06a__card" onsubmit="return false">
    <div class="glz-06a__logo" aria-hidden="true">✦</div>
    <h2 class="glz-06a__title">Welcome back</h2>
    <p class="glz-06a__sub">Sign in to your Lumen workspace</p>
    <div class="glz-06a__field"><input id="glz-06a-em" type="email" placeholder=" " autocomplete="email" required><label for="glz-06a-em">Email address</label></div>
    <div class="glz-06a__field"><input id="glz-06a-pw" type="password" placeholder=" " autocomplete="current-password" required><label for="glz-06a-pw">Password</label></div>
    <div class="glz-06a__row"><label class="glz-06a__rem"><input type="checkbox" checked><i aria-hidden="true"></i>Remember me</label><a href="#" onclick="return false">Forgot password?</a></div>
    <button type="submit" class="glz-06a__cta">Sign in</button>
    <div class="glz-06a__div"><span>or continue with</span></div>
    <div class="glz-06a__social"><button type="button" aria-label="Continue with Google"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="#EA4335" d="M12 10.2v3.9h5.5c-.24 1.4-1.66 4.1-5.5 4.1-3.31 0-6.01-2.74-6.01-6.13S8.69 5.94 12 5.94c1.88 0 3.14.8 3.86 1.5l2.63-2.54C16.83 3.38 14.62 2.4 12 2.4 6.86 2.4 2.7 6.55 2.7 11.7s4.16 9.3 9.3 9.3c5.37 0 8.93-3.77 8.93-9.08 0-.61-.07-1.08-.16-1.55H12z"/></svg></button><button type="button" aria-label="Continue with Apple"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/></svg></button><button type="button" aria-label="Continue with GitHub"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 .3a12 12 0 0 0-3.79 23.4c.6.11.82-.26.82-.58v-2.03c-3.34.72-4.04-1.6-4.04-1.6-.55-1.39-1.34-1.76-1.34-1.76-1.09-.75.08-.73.08-.73 1.21.09 1.84 1.24 1.84 1.24 1.07 1.84 2.81 1.3 3.5 1 .11-.78.42-1.3.76-1.6-2.66-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.14-.3-.54-1.52.1-3.18 0 0 1-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.28-1.55 3.29-1.23 3.29-1.23.65 1.66.24 2.88.12 3.18a4.65 4.65 0 0 1 1.23 3.22c0 4.61-2.81 5.63-5.48 5.92.42.36.81 1.1.81 2.22v3.29c0 .32.21.7.82.58A12 12 0 0 0 12 .3"/></svg></button></div>
  </form>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="glz-06b" aria-label="Split panel glassmorphism login">
  <div class="glz-06b__shell">
    <aside class="glz-06b__brand" aria-hidden="true">
      <b>north★</b>
      <p>“The calmest way to run a studio.”</p>
      <span>4.9 on G2 · 12k teams</span>
    </aside>
    <form class="glz-06b__form" onsubmit="return false">
      <h2>Sign in</h2>
      <label class="glz-06b__lab" for="glz-06b-em">Work email</label>
      <input id="glz-06b-em" type="email" placeholder="[email protected]" autocomplete="email" required>
      <label class="glz-06b__lab" for="glz-06b-pw">Password</label>
      <input id="glz-06b-pw" type="password" placeholder="••••••••" autocomplete="current-password" required>
      <button type="submit">Continue →</button>
      <p class="glz-06b__alt">New here? <a href="#" onclick="return false">Create an account</a></p>
    </form>
  </div>
</section>
</div>
```
## CSS
```css
.glz-06-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-06-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-06a,
.glz-06a *,
.glz-06a *::before,
.glz-06a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-06a {
  --acc: oklch(0.78 0.14 200);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0a0d18;
  font-family: 'Outfit',system-ui,sans-serif;
}

.glz-06a::before,
.glz-06a::after {
  content: "";
  position: absolute;
  width: 50vmin;
  height: 50vmin;
  border-radius: 50%;
  filter: blur(80px);
  opacity: .65;
  animation: glz-06a-float 16s ease-in-out infinite alternate;
}

.glz-06a::before {
  background: oklch(0.55 0.22 300);
  top: -8%;
  left: 8%;
}

.glz-06a::after {
  background: oklch(0.65 0.16 200);
  bottom: -10%;
  right: 6%;
  animation-delay: -8s;
}

.glz-06a__card {
  position: relative;
  z-index: 1;
  width: min(380px,100%);
  padding: 34px 30px 30px;
  border-radius: 26px;
  color: #eef2fd;
  background: linear-gradient(160deg,rgba(255,255,255,.13),rgba(255,255,255,.04));
  backdrop-filter: blur(24px) saturate(170%);
  -webkit-backdrop-filter: blur(24px) saturate(170%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 34px 70px -26px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.24);
}

.glz-06a__logo {
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 14px;
  font-size: 20px;
  color: #0a0d18;
  background: linear-gradient(135deg,oklch(0.85 0.12 200),oklch(0.75 0.17 300));
  box-shadow: 0 10px 24px -8px oklch(0.75 0.17 300/.8);
}

.glz-06a__title {
  margin-top: 18px;
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.glz-06a__sub {
  margin-top: 5px;
  font-size: 13.5px;
  color: rgba(238,242,253,.55);
}

.glz-06a__field {
  position: relative;
  margin-top: 22px;
}

.glz-06a__field input {
  width: 100%;
  padding: 15px 16px 13px;
  font: 500 16px 'Outfit',sans-serif;
  color: #fff;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.18);
  background: rgba(255,255,255,.06);
  transition: border-color .25s ease,box-shadow .25s ease;
}

.glz-06a__field input:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px oklch(0.78 0.14 200/.22);
}

.glz-06a__field input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0 60px #1a2233 inset;
  -webkit-text-fill-color: #fff;
}

.glz-06a__field label {
  position: absolute;
  left: 16px;
  top: 15px;
  font-size: 14.5px;
  color: rgba(238,242,253,.5);
  pointer-events: none;
  transform-origin: left top;
  transition: transform .22s ease,color .22s ease;
  background: transparent;
  padding: 0 4px;
}

.glz-06a__field input:focus + label,
.glz-06a__field input:not(:placeholder-shown) + label {
  transform: translateY(-24px) scale(.72);
  color: var(--acc);
}

.glz-06a__row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 16px;
  font-size: 12.5px;
}

.glz-06a__rem {
  display: flex;
  align-items: center;
  gap: 8px;
  color: rgba(238,242,253,.7);
  cursor: pointer;
}

.glz-06a__rem input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.glz-06a__rem i {
  width: 17px;
  height: 17px;
  border-radius: 6px;
  border: 1.5px solid rgba(255,255,255,.4);
  display: grid;
  place-items: center;
  transition: background .2s ease,border-color .2s ease;
}

.glz-06a__rem i::after {
  content: "✓";
  font-size: 11px;
  font-weight: 800;
  color: #0a0d18;
  opacity: 0;
}

.glz-06a__rem:has(input:checked) i {
  background: var(--acc);
  border-color: var(--acc);
}

.glz-06a__rem:has(input:checked) i::after {
  opacity: 1;
}

.glz-06a__rem:has(input:focus-visible) i {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.glz-06a__row a {
  color: var(--acc);
  text-decoration: none;
  font-weight: 600;
}

.glz-06a__row a:hover {
  text-decoration: underline;
}

.glz-06a__cta {
  width: 100%;
  margin-top: 22px;
  padding: 15px;
  border: none;
  border-radius: 14px;
  background: linear-gradient(120deg,oklch(0.78 0.14 200),oklch(0.68 0.18 290));
  color: #071018;
  font: 700 15px 'Outfit',sans-serif;
  cursor: pointer;
  box-shadow: 0 16px 34px -12px oklch(0.7 0.17 250/.8);
  transition: transform .2s ease,filter .2s ease;
}

.glz-06a__cta:hover {
  transform: translateY(-2px);
  filter: brightness(1.07);
}

.glz-06a__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.glz-06a__div {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 22px;
  font-size: 11px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(238,242,253,.4);
}

.glz-06a__div::before,
.glz-06a__div::after {
  content: "";
  flex: 1;
  height: 1px;
  background: rgba(255,255,255,.14);
}

.glz-06a__social {
  display: flex;
  gap: 10px;
  margin-top: 16px;
}

.glz-06a__social button {
  flex: 1;
  padding: 12px 0;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,.18);
  background: rgba(255,255,255,.06);
  color: #eef2fd;
  font-size: 15px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: background .2s ease,transform .2s ease;
}

.glz-06a__social svg {
  display: block;
}

.glz-06a__social button:hover {
  background: rgba(255,255,255,.14);
  transform: translateY(-2px);
}

.glz-06a__social button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@keyframes glz-06a-float {
  to {
    transform: translate(7vmin,-5vmin) scale(1.12);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-06a__card {
    background: rgba(18,23,40,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-06a::before,
    .glz-06a::after {
    animation: none;
  }

  .glz-06a__field label,
    .glz-06a__cta,
    .glz-06a__social button {
    transition: none;
  }
}

.glz-06b,
.glz-06b *,
.glz-06b *::before,
.glz-06b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-06b {
  --acc: oklch(0.72 0.19 35);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 85% 10%,oklch(0.86 0.09 35),transparent 55%),radial-gradient(110% 90% at 10% 95%,oklch(0.85 0.08 300),transparent 60%),#f4f0ea;
  font-family: 'Outfit',system-ui,sans-serif;
}

.glz-06b__shell {
  display: flex;
  flex-wrap: wrap;
  width: min(720px,100%);
  border-radius: 28px;
  overflow: hidden;
  background: linear-gradient(160deg,rgba(255,255,255,.6),rgba(255,255,255,.3));
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid rgba(255,255,255,.85);
  box-shadow: 0 34px 70px -30px rgba(120,70,40,.5),inset 0 1px 0 rgba(255,255,255,.95);
}

.glz-06b__brand {
  flex: 1 1 260px;
  min-height: 280px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 32px;
  color: #fff7f2;
  background: linear-gradient(150deg,oklch(0.62 0.21 35),oklch(0.5 0.19 320) 80%);
}

.glz-06b__brand b {
  font-size: 20px;
  letter-spacing: -.02em;
}

.glz-06b__brand p {
  font-size: clamp(19px,2.6vw,24px);
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -.02em;
  max-width: 16ch;
}

.glz-06b__brand span {
  font-size: 11.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(255,247,242,.7);
}

.glz-06b__form {
  flex: 1 1 300px;
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  color: #2b2018;
}

.glz-06b__form h2 {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.02em;
  margin-bottom: 8px;
}

.glz-06b__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(43,32,24,.55);
  margin: 16px 0 7px;
}

.glz-06b__form input {
  padding: 13px 15px;
  font: 500 16px 'Outfit',sans-serif;
  color: #2b2018;
  border-radius: 12px;
  border: 1px solid rgba(43,32,24,.18);
  background: rgba(255,255,255,.55);
  transition: border-color .2s ease,box-shadow .2s ease;
}

.glz-06b__form input::placeholder {
  color: rgba(43,32,24,.35);
}

.glz-06b__form input:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px oklch(0.72 0.19 35/.2);
}

.glz-06b__form button {
  margin-top: 22px;
  padding: 14px;
  border: none;
  border-radius: 13px;
  background: #2b2018;
  color: #fff8f0;
  font: 700 14.5px 'Outfit',sans-serif;
  cursor: pointer;
  transition: transform .2s ease,box-shadow .2s ease;
}

.glz-06b__form button:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 26px -12px rgba(43,32,24,.6);
}

.glz-06b__form button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.glz-06b__alt {
  margin-top: 16px;
  font-size: 13px;
  color: rgba(43,32,24,.6);
}

.glz-06b__alt a {
  color: oklch(0.55 0.19 35);
  font-weight: 700;
  text-decoration: none;
}

.glz-06b__alt a:hover {
  text-decoration: underline;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-06b__shell {
    background: rgba(255,255,255,.93);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-06b__form button,
    .glz-06b__form input {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — labels float via :focus / :not(:placeholder-shown); the custom checkbox and its ✓ are :has()-driven. */

/* No JavaScript — a flex-wrap two-panel card: opaque brand slab + frosted form, collapsing to one column when the playground narrows. */
```
