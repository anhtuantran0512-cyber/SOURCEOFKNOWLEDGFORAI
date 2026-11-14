---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/brutalist-stamp/"
title: "Brutalist Stamp"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "Raw neo-brutalism for agencies and portfolios: thick black borders, hard offset drop shadows with zero blur, monospace type, and a satisfying press effect…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Stamp
Source: https://codefronts.com/components/css-login-forms/brutalist-stamp/

Raw neo-brutalism for agencies and portfolios: thick black borders, hard offset drop shadows with zero blur, monospace type, and a satisfying press effect where the card slams down onto its shadow.
## HTML
```html
<section class="lf-23">
  <form class="lf-23__card" novalidate>
    <span class="lf-23__stamp" aria-hidden="true">MEMBERS</span>
    <h1 class="lf-23__h">LOG&nbsp;IN</h1>
    <label class="lf-23__field"><span class="lf-23__label">EMAIL</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
    <label class="lf-23__field"><span class="lf-23__label">PASSWORD</span>
      <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
    <button class="lf-23__submit" type="submit">ENTER →</button>
  </form>
</section>
```
## CSS
```css
.lf-23,
.lf-23 *,
.lf-23 *::before,
.lf-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-23 {
  --accent: #ffe600;
  --ink: #0a0a0a;
  --field-h: 52px;
  font-family: ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  width: 100%;
  min-height: 100vh;
  background: #f0efe9;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-23__card {
  position: relative;
  width: min(360px,100%);
  background: #fff;
  border: 3px solid var(--ink);
  border-radius: 0;
  padding: 36px 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 9px 9px 0 var(--ink);
}

.lf-23__stamp {
  position: absolute;
  top: -14px;
  right: 16px;
  background: var(--accent);
  border: 3px solid var(--ink);
  padding: 4px 12px;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .12em;
  transform: rotate(4deg);
}

.lf-23__h {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--ink);
}

.lf-23__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-23__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .1em;
  color: var(--ink);
}

.lf-23__field input {
  height: var(--field-h);
  border: 3px solid var(--ink);
  border-radius: 0;
  padding: 0 14px;
  font-family: inherit;
  font-size: 15px;
  color: var(--ink);
  background: #fff;
  transition: box-shadow .12s,transform .12s;
}

.lf-23__field input::placeholder {
  color: #9a9a90;
}

.lf-23__field input:focus-visible {
  outline: none;
  box-shadow: 5px 5px 0 var(--accent),0 0 0 3px var(--ink);
}

.lf-23__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 3px solid var(--ink);
  border-radius: 0;
  cursor: pointer;
  background: var(--accent);
  color: var(--ink);
  font-family: inherit;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .04em;
  box-shadow: 5px 5px 0 var(--ink);
  transition: transform .1s,box-shadow .1s;
}

.lf-23__submit:hover {
  transform: translate(-1px,-1px);
  box-shadow: 6px 6px 0 var(--ink);
}

.lf-23__submit:active {
  transform: translate(5px,5px);
  box-shadow: 0 0 0 var(--ink);
}

.lf-23__submit:focus-visible {
  outline: 3px solid #000;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-23 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — hard 0-blur offset shadows; the button stamps down on :active via matched translate. */
```
