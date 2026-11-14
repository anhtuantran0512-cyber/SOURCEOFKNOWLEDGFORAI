---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/magic-link/"
title: "Magic Link"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The hyper-minimalist single-field entry (Linear / Substack): one email input and a Send Magic Link button."
has_js: "true"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magic Link
Source: https://codefronts.com/components/css-login-forms/magic-link/

The hyper-minimalist single-field entry (Linear / Substack): one email input and a Send Magic Link button. On submit it swaps to a loading state and then a clean check-your-inbox confirmation — all at a fixed height so nothing jumps.
## HTML
```html
<section class="lf-07">
  <form class="lf-07__form" data-state="idle" novalidate>
    <div class="lf-07__idle">
      <h1 class="lf-07__h">Sign in</h1>
      <p class="lf-07__sub">We'll email you a magic link — no password needed.</p>
      <label class="lf-07__field">
        <span class="lf-07__vh">Email address</span>
        <input type="email" name="email" autocomplete="email" inputmode="email" placeholder="[email protected]" required>
      </label>
      <button class="lf-07__btn" type="submit"><span class="lf-07__btnlabel">Send magic link</span></button>
    </div>
    <div class="lf-07__done" role="status" aria-live="polite">
      <span class="lf-07__check" aria-hidden="true"></span>
      <h2 class="lf-07__doneh">Check your inbox</h2>
      <p class="lf-07__donep">We sent a link to <b class="lf-07__addr">[email protected]</b>. It expires in 10 minutes.</p>
    </div>
  </form>
</section>
```
## CSS
```css
.lf-07,
.lf-07 *,
.lf-07 *::before,
.lf-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-07 {
  --accent: oklch(0.6 0.2 280);
  --radius: 12px;
  --field-h: 50px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #0f1117;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-07__form {
  position: relative;
  width: min(380px,100%);
  min-height: 280px;
  background: #171a23;
  border: 1px solid #262a37;
  border-radius: 18px;
  padding: 34px 30px;
  box-shadow: 0 30px 70px -44px #000;
  overflow: hidden;
}

.lf-07__idle,
.lf-07__done {
  display: flex;
  flex-direction: column;
  gap: 14px;
  transition: opacity .35s,transform .35s;
}

.lf-07__done {
  position: absolute;
  inset: 34px 30px;
  justify-content: center;
  align-items: center;
  text-align: center;
  opacity: 0;
  transform: translateY(10px);
  pointer-events: none;
}

.lf-07__h {
  font-size: 24px;
  font-weight: 700;
  color: #f2f4fa;
  letter-spacing: -.01em;
}

.lf-07__sub {
  font-size: 14px;
  line-height: 1.5;
  color: #9aa1b5;
  margin-bottom: 4px;
}

.lf-07__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.lf-07__field input {
  width: 100%;
  height: var(--field-h);
  border: 1.5px solid #333a4c;
  border-radius: var(--radius);
  padding: 0 15px;
  font-size: 15px;
  color: #f2f4fa;
  background: #11141c;
  transition: border-color .18s,box-shadow .18s;
}

.lf-07__field input::placeholder {
  color: #5f677e;
}

.lf-07__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.6 0.2 280/.22);
}

.lf-07__btn {
  position: relative;
  height: var(--field-h);
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  overflow: hidden;
  transition: filter .18s,transform .12s;
}

.lf-07__btn:hover {
  filter: brightness(1.07);
}

.lf-07__btn:active {
  transform: scale(.985);
}

.lf-07__btn:focus-visible {
  outline: 3px solid oklch(0.6 0.2 280/.55);
  outline-offset: 3px;
}

.lf-07__btn::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 18px;
  height: 18px;
  margin: -9px 0 0 -9px;
  border: 2.5px solid rgba(255,255,255,.4);
  border-top-color: #fff;
  border-radius: 50%;
  opacity: 0;
  animation: lf-07-spin .7s linear infinite;
}

.lf-07__form[data-state="loading"] .lf-07__btnlabel {
  opacity: 0;
}

.lf-07__form[data-state="loading"] .lf-07__btn {
  pointer-events: none;
}

.lf-07__form[data-state="loading"] .lf-07__btn::after {
  opacity: 1;
}

.lf-07__form[data-state="sent"] .lf-07__idle {
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
}

.lf-07__form[data-state="sent"] .lf-07__done {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.lf-07__check {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: oklch(0.7 0.17 155);
  position: relative;
  margin-bottom: 4px;
}

.lf-07__check::after {
  content: "";
  position: absolute;
  left: 18px;
  top: 14px;
  width: 12px;
  height: 22px;
  border: solid #08210f;
  border-width: 0 3px 3px 0;
  transform: rotate(42deg);
}

.lf-07__doneh {
  font-size: 20px;
  font-weight: 700;
  color: #f2f4fa;
}

.lf-07__donep {
  font-size: 13.5px;
  line-height: 1.5;
  color: #9aa1b5;
}

.lf-07__addr {
  color: #cdd3e6;
}

@keyframes lf-07-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-07__idle,
    .lf-07__done {
    transition: none;
  }

  .lf-07__btn::after {
    animation: none;
  }
}
```

## JavaScript
```js
const form = document.querySelector('.lf-07__form');
const email = form.querySelector('input[type=email]');
const btn = form.querySelector('.lf-07__btn');
function send() {
  if (form.dataset.state !== 'idle') return;
  if (!email.checkValidity()) { email.reportValidity(); return; }
  form.querySelector('.lf-07__addr').textContent = email.value || '[email protected]';
  form.dataset.state = 'loading';
  setTimeout(() => { form.dataset.state = 'sent'; }, 1400);
}
btn.addEventListener('click', (e) => { e.preventDefault(); send(); });
email.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); send(); } });
```
