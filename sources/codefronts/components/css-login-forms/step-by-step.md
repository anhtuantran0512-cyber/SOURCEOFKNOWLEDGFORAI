---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/step-by-step/"
title: "Step-by-Step"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A multi-stage sign-in that lowers upfront resistance: step 1 takes the email, step 2 the password, step 3 a security code — inactive cards slide off-screen…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Step-by-Step
Source: https://codefronts.com/components/css-login-forms/step-by-step/

A multi-stage sign-in that lowers upfront resistance: step 1 takes the email, step 2 the password, step 3 a security code — inactive cards slide off-screen smoothly, all driven by radios and a translated track.
## HTML
```html
<section class="lf-20">
  <form class="lf-20__card" novalidate>
    <input type="radio" name="lf-20-step" id="lf-20-s1" class="lf-20__r" checked>
    <input type="radio" name="lf-20-step" id="lf-20-s2" class="lf-20__r">
    <input type="radio" name="lf-20-step" id="lf-20-s3" class="lf-20__r">
    <div class="lf-20__bar" aria-hidden="true"><span class="lf-20__fill"></span></div>
    <div class="lf-20__viewport">
      <div class="lf-20__track">
        <fieldset class="lf-20__step"><legend class="lf-20__h">Your email</legend>
          <input type="email" autocomplete="email" placeholder="[email protected]" required>
          <label class="lf-20__next" for="lf-20-s2">Continue</label></fieldset>
        <fieldset class="lf-20__step"><legend class="lf-20__h">Your password</legend>
          <input type="password" autocomplete="current-password" placeholder="••••••••" required>
          <div class="lf-20__row"><label class="lf-20__back" for="lf-20-s1">Back</label><label class="lf-20__next" for="lf-20-s3">Continue</label></div></fieldset>
        <fieldset class="lf-20__step"><legend class="lf-20__h">Security code</legend>
          <input type="text" inputmode="numeric" autocomplete="one-time-code" placeholder="6-digit code" required>
          <div class="lf-20__row"><label class="lf-20__back" for="lf-20-s2">Back</label><button type="submit" class="lf-20__done">Sign in</button></div></fieldset>
      </div>
    </div>
  </form>
</section>
```
## CSS
```css
.lf-20,
.lf-20 *,
.lf-20 *::before,
.lf-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-20 {
  --accent: oklch(0.56 0.18 255);
  --radius: 11px;
  --field-h: 48px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #eef1f7;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-20__card {
  width: min(360px,100%);
  background: #fff;
  border: 1px solid #e5e9f2;
  border-radius: 18px;
  padding: 26px 26px 30px;
  box-shadow: 0 24px 56px -38px rgba(16,24,60,.5);
  overflow: hidden;
}

.lf-20__r {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.lf-20__bar {
  height: 5px;
  border-radius: 999px;
  background: #e6eaf3;
  overflow: hidden;
  margin-bottom: 22px;
}

.lf-20__fill {
  display: block;
  height: 100%;
  width: 33%;
  border-radius: 999px;
  background: var(--accent);
  transition: width .4s cubic-bezier(.4,0,.2,1);
}

.lf-20__r:nth-of-type(2):checked ~ .lf-20__bar .lf-20__fill {
  width: 66%;
}

.lf-20__r:nth-of-type(3):checked ~ .lf-20__bar .lf-20__fill {
  width: 100%;
}

.lf-20__viewport {
  overflow: hidden;
}

.lf-20__track {
  display: flex;
  width: 300%;
  transition: transform .45s cubic-bezier(.4,0,.2,1);
}

.lf-20__r:nth-of-type(2):checked ~ .lf-20__viewport .lf-20__track {
  transform: translateX(-33.333%);
}

.lf-20__r:nth-of-type(3):checked ~ .lf-20__viewport .lf-20__track {
  transform: translateX(-66.666%);
}

.lf-20__step {
  width: 33.333%;
  border: 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 0 2px;
}

.lf-20__h {
  font-size: 19px;
  font-weight: 700;
  color: #1a2237;
  padding: 0;
  margin-bottom: 2px;
}

.lf-20__step input {
  height: var(--field-h);
  border: 1.5px solid #d8deeb;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #1a2237;
  background: #fafbfe;
  transition: border-color .18s,box-shadow .18s;
}

.lf-20__step input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.56 0.18 255/.16);
}

.lf-20__row {
  display: flex;
  gap: 10px;
}

.lf-20__next,
.lf-20__done {
  flex: 1;
  height: var(--field-h);
  display: grid;
  place-items: center;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: filter .18s;
}

.lf-20__next:hover,
.lf-20__done:hover {
  filter: brightness(1.07);
}

.lf-20__next:focus-visible,
.lf-20__done:focus-visible {
  outline: 3px solid oklch(0.56 0.18 255/.5);
  outline-offset: 2px;
}

.lf-20__back {
  flex: 0 0 90px;
  height: var(--field-h);
  display: grid;
  place-items: center;
  border: 1.5px solid #d8deeb;
  border-radius: var(--radius);
  cursor: pointer;
  background: #fff;
  color: #54607c;
  font-size: 15px;
  font-weight: 600;
  transition: background .16s;
}

.lf-20__back:hover {
  background: #f2f5fb;
}

.lf-20__back:focus-visible {
  outline: 3px solid oklch(0.56 0.18 255/.4);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-20__track,
    .lf-20__fill {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — three step radios shift a translateX track; Next/Back are labels bound to them. */
```
