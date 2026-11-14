---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/strength-meter/"
title: "Strength Meter"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A sign-up password field with a live entropy estimate: a segmented bar and a word label update as the user types, transitioning from red through amber to…"
has_js: "true"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Strength Meter
Source: https://codefronts.com/components/css-login-forms/strength-meter/

A sign-up password field with a live entropy estimate: a segmented bar and a word label update as the user types, transitioning from red through amber to green — reassuring, standard, and accessible.
## HTML
```html
<section class="lf-26">
  <form class="lf-26__card" novalidate>
    <h1 class="lf-26__h">Create your password</h1>
    <div class="lf-26__field" data-score="0">
      <label class="lf-26__label" for="lf-26-pw">Password</label>
      <input id="lf-26-pw" class="lf-26__pw" type="password" autocomplete="new-password" placeholder="Choose a strong password" required>
      <div class="lf-26__meter" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
      <p class="lf-26__hint" role="status" aria-live="polite">Use 8+ characters with letters, numbers &amp; symbols.</p>
    </div>
    <button class="lf-26__submit" type="submit">Create account</button>
  </form>
</section>
```
## CSS
```css
.lf-26,
.lf-26 *,
.lf-26 *::before,
.lf-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-26 {
  --accent: oklch(0.55 0.17 250);
  --radius: 11px;
  --field-h: 50px;
  --s1: oklch(0.6 0.2 25);
  --s2: oklch(0.72 0.16 60);
  --s3: oklch(0.78 0.15 100);
  --s4: oklch(0.68 0.16 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #eef1f7;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-26__card {
  width: min(380px,100%);
  background: #fff;
  border: 1px solid #e5e9f2;
  border-radius: 16px;
  padding: 32px 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 22px 50px -38px rgba(16,24,60,.5);
}

.lf-26__h {
  font-size: 22px;
  font-weight: 700;
  color: #1a2237;
}

.lf-26__field {
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.lf-26__label {
  font-size: 13px;
  font-weight: 600;
  color: #3d465f;
}

.lf-26__pw {
  height: var(--field-h);
  border: 1.5px solid #d8deeb;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #1a2237;
  background: #fafbfe;
  transition: border-color .18s,box-shadow .18s;
}

.lf-26__pw:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.17 250/.16);
}

.lf-26__meter {
  display: flex;
  gap: 5px;
  height: 5px;
}

.lf-26__meter span {
  flex: 1;
  border-radius: 999px;
  background: #e2e7f0;
  transform-origin: left;
  transition: background .25s;
}

.lf-26__field[data-score="1"] .lf-26__meter span:nth-child(-n+1) {
  background: var(--s1);
}

.lf-26__field[data-score="2"] .lf-26__meter span:nth-child(-n+2) {
  background: var(--s2);
}

.lf-26__field[data-score="3"] .lf-26__meter span:nth-child(-n+3) {
  background: var(--s3);
}

.lf-26__field[data-score="4"] .lf-26__meter span:nth-child(-n+4) {
  background: var(--s4);
}

.lf-26__hint {
  font-size: 12.5px;
  color: #767d97;
  transition: color .2s;
}

.lf-26__field[data-score="1"] .lf-26__hint {
  color: var(--s1);
}

.lf-26__field[data-score="2"] .lf-26__hint {
  color: oklch(0.55 0.16 60);
}

.lf-26__field[data-score="3"] .lf-26__hint {
  color: oklch(0.5 0.14 100);
}

.lf-26__field[data-score="4"] .lf-26__hint {
  color: var(--s4);
}

.lf-26__submit {
  height: var(--field-h);
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: filter .18s,transform .12s;
}

.lf-26__submit:hover {
  filter: brightness(1.07);
}

.lf-26__submit:active {
  transform: scale(.99);
}

.lf-26__submit:focus-visible {
  outline: 3px solid oklch(0.55 0.17 250/.5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-26 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
const sec = document.querySelector('.lf-26');
const field = sec.querySelector('.lf-26__field');
const pw = sec.querySelector('.lf-26__pw');
const hint = sec.querySelector('.lf-26__hint');
const labels = ['Use 8+ characters with letters, numbers & symbols.','Very weak password','Weak password','Good password','Strong password'];
pw.addEventListener('input', () => {
  const v = pw.value; let s = 0;
  if (v.length >= 8) s++;
  if (/[A-Z]/.test(v) && /[a-z]/.test(v)) s++;
  if (/[0-9]/.test(v)) s++;
  if (/[^A-Za-z0-9]/.test(v)) s++;
  if (v.length === 0) s = 0; else if (v.length < 6) s = 1;
  field.dataset.score = String(s);
  hint.textContent = labels[s];
});
```
