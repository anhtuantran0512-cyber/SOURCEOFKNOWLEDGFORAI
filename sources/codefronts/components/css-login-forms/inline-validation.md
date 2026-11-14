---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/inline-validation/"
title: "Inline Validation"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "Enterprise-grade instant feedback: each field shows a green tick when valid and a red hint when not — driven entirely by native CSS validation…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Validation
Source: https://codefronts.com/components/css-login-forms/inline-validation/

Enterprise-grade instant feedback: each field shows a green tick when valid and a red hint when not — driven entirely by native CSS validation pseudo-classes, so no keystroke JavaScript is needed.
## HTML
```html
<section class="lf-28">
  <form class="lf-28__card" novalidate>
    <h1 class="lf-28__h">Create account</h1>
    <div class="lf-28__field">
      <label class="lf-28__label" for="lf-28-email">Work email</label>
      <div class="lf-28__wrap"><input id="lf-28-email" type="email" autocomplete="email" placeholder="[email protected]" required aria-describedby="lf-28-email-hint"><span class="lf-28__mark" aria-hidden="true"></span></div>
      <p class="lf-28__hint" id="lf-28-email-hint">Enter a valid email address.</p>
    </div>
    <div class="lf-28__field">
      <label class="lf-28__label" for="lf-28-user">Username</label>
      <div class="lf-28__wrap"><input id="lf-28-user" type="text" autocomplete="username" placeholder="min 4 characters" required minlength="4" pattern="[a-zA-Z0-9_]+" aria-describedby="lf-28-user-hint"><span class="lf-28__mark" aria-hidden="true"></span></div>
      <p class="lf-28__hint" id="lf-28-user-hint">4+ letters, numbers or underscore.</p>
    </div>
    <div class="lf-28__field">
      <label class="lf-28__label" for="lf-28-pw">Password</label>
      <div class="lf-28__wrap"><input id="lf-28-pw" type="password" autocomplete="new-password" placeholder="min 8 characters" required minlength="8" aria-describedby="lf-28-pw-hint"><span class="lf-28__mark" aria-hidden="true"></span></div>
      <p class="lf-28__hint" id="lf-28-pw-hint">At least 8 characters.</p>
    </div>
    <button class="lf-28__submit" type="submit">Sign up</button>
  </form>
</section>
```
## CSS
```css
.lf-28,
.lf-28 *,
.lf-28 *::before,
.lf-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-28 {
  --accent: oklch(0.55 0.16 255);
  --ok: oklch(0.62 0.15 155);
  --bad: oklch(0.6 0.2 25);
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

.lf-28__card {
  width: min(380px,100%);
  background: #fff;
  border: 1px solid #e5e9f2;
  border-radius: 16px;
  padding: 32px 28px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  box-shadow: 0 22px 50px -38px rgba(16,24,60,.5);
}

.lf-28__h {
  font-size: 22px;
  font-weight: 700;
  color: #1a2237;
  margin-bottom: 2px;
}

.lf-28__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-28__label {
  font-size: 13px;
  font-weight: 600;
  color: #3d465f;
}

.lf-28__wrap {
  position: relative;
}

.lf-28__wrap input {
  width: 100%;
  height: var(--field-h);
  border: 1.5px solid #d8deeb;
  border-radius: var(--radius);
  padding: 0 42px 0 14px;
  font-size: 15px;
  color: #1a2237;
  background: #fafbfe;
  transition: border-color .18s,box-shadow .18s;
}

.lf-28__wrap input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.16 255/.16);
}

.lf-28__mark {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%) scale(.4);
  width: 20px;
  height: 20px;
  opacity: 0;
  transition: opacity .2s,transform .2s;
}

.lf-28__mark::before,
.lf-28__mark::after {
  content: "";
  position: absolute;
}

.lf-28__hint {
  font-size: 12px;
  color: #8a91a8;
  overflow: hidden;
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .25s,color .2s;
}

.lf-28__hint::after {
  content: "";
  min-height: 0;
}

.lf-28__wrap input:user-valid {
  border-color: var(--ok);
}

.lf-28__wrap input:user-valid ~ .lf-28__mark {
  opacity: 1;
  transform: translateY(-50%) scale(1);
}

.lf-28__wrap input:user-valid ~ .lf-28__mark::before {
  left: 6px;
  top: 3px;
  width: 6px;
  height: 11px;
  border: solid var(--ok);
  border-width: 0 2.5px 2.5px 0;
  transform: rotate(42deg);
}

.lf-28__wrap input:user-invalid {
  border-color: var(--bad);
}

.lf-28__wrap input:user-invalid ~ .lf-28__mark {
  opacity: 1;
  transform: translateY(-50%) scale(1);
}

.lf-28__wrap input:user-invalid ~ .lf-28__mark::before {
  left: 9px;
  top: 4px;
  width: 2.5px;
  height: 13px;
  background: var(--bad);
  transform: rotate(45deg);
}

.lf-28__wrap input:user-invalid ~ .lf-28__mark::after {
  left: 9px;
  top: 4px;
  width: 2.5px;
  height: 13px;
  background: var(--bad);
  transform: rotate(-45deg);
}

.lf-28__field:has(input:user-invalid) .lf-28__hint {
  grid-template-rows: 1fr;
  color: var(--bad);
  padding-top: 2px;
}

.lf-28__submit {
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

.lf-28__submit:hover {
  filter: brightness(1.07);
}

.lf-28__submit:active {
  transform: scale(.99);
}

.lf-28__submit:focus-visible {
  outline: 3px solid oklch(0.55 0.16 255/.5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-28 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — native :user-valid / :user-invalid drive the tick, cross and revealed hint. */
```
