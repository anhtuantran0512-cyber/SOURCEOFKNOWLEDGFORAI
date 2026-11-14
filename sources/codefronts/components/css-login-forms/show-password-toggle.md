---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/show-password-toggle/"
title: "Show Password Toggle"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The everyday accessibility win: an eye button inside the password field flips it between hidden and visible so users can catch typos — with the icon…"
has_js: "true"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Show Password Toggle
Source: https://codefronts.com/components/css-login-forms/show-password-toggle/

The everyday accessibility win: an eye button inside the password field flips it between hidden and visible so users can catch typos — with the icon absolutely positioned so typed characters never slide under it.
## HTML
```html
<section class="lf-24">
  <form class="lf-24__card" novalidate>
    <h1 class="lf-24__h">Log in</h1>
    <label class="lf-24__field"><span class="lf-24__label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
    <div class="lf-24__field">
      <label class="lf-24__label" for="lf-24-pw">Password</label>
      <div class="lf-24__wrap">
        <input id="lf-24-pw" class="lf-24__pw" type="password" autocomplete="current-password" placeholder="••••••••" required>
        <button class="lf-24__eye" type="button" aria-pressed="false" aria-label="Show password"><span class="lf-24__glyph" aria-hidden="true"></span></button>
      </div>
    </div>
    <button class="lf-24__submit" type="submit">Continue</button>
  </form>
</section>
```
## CSS
```css
.lf-24,
.lf-24 *,
.lf-24 *::before,
.lf-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-24 {
  --accent: oklch(0.55 0.17 250);
  --radius: 11px;
  --field-h: 50px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #eef1f7;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-24__card {
  width: min(360px,100%);
  background: #fff;
  border: 1px solid #e5e9f2;
  border-radius: 16px;
  padding: 32px 28px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  box-shadow: 0 22px 50px -38px rgba(16,24,60,.5);
}

.lf-24__h {
  font-size: 23px;
  font-weight: 700;
  color: #1a2237;
}

.lf-24__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-24__label {
  font-size: 13px;
  font-weight: 600;
  color: #3d465f;
}

.lf-24__field input,
.lf-24__wrap input {
  height: var(--field-h);
  width: 100%;
  border: 1.5px solid #d8deeb;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #1a2237;
  background: #fafbfe;
  transition: border-color .18s,box-shadow .18s;
}

.lf-24__wrap {
  position: relative;
}

.lf-24__pw {
  padding-right: 50px;
}

.lf-24__field input:focus-visible,
.lf-24__pw:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.17 250/.16);
}

.lf-24__eye {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  width: 36px;
  height: 36px;
  border: 0;
  border-radius: 9px;
  background: transparent;
  cursor: pointer;
  display: grid;
  place-items: center;
  color: #8a91a8;
  transition: background .16s,color .16s;
}

.lf-24__eye:hover {
  background: #eef1f7;
  color: var(--accent);
}

.lf-24__eye:focus-visible {
  outline: 3px solid oklch(0.55 0.17 250/.5);
  outline-offset: 1px;
}

.lf-24__glyph {
  position: relative;
  width: 22px;
  height: 14px;
  border: 2px solid currentColor;
  border-radius: 50% 50% 50% 50%/ 60% 60% 60% 60%;
}

.lf-24__glyph::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 6px;
  height: 6px;
  transform: translate(-50%,-50%);
  border-radius: 50%;
  background: currentColor;
}

.lf-24__eye[aria-pressed="true"] .lf-24__glyph::before {
  content: "";
  position: absolute;
  left: -3px;
  top: 5px;
  width: 28px;
  height: 2px;
  background: currentColor;
  transform: rotate(-30deg);
  transform-origin: center;
}

.lf-24__submit {
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

.lf-24__submit:hover {
  filter: brightness(1.07);
}

.lf-24__submit:active {
  transform: scale(.985);
}

.lf-24__submit:focus-visible {
  outline: 3px solid oklch(0.55 0.17 250/.5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-24 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
const sec = document.querySelector('.lf-24');
const btn = sec.querySelector('.lf-24__eye');
const pw = sec.querySelector('.lf-24__pw');
btn.addEventListener('click', () => {
  const show = pw.type === 'password';
  pw.type = show ? 'text' : 'password';
  btn.setAttribute('aria-pressed', String(show));
  btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
  pw.focus();
});
```
