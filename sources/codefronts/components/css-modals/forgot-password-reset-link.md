---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/forgot-password-reset-link/"
title: "Forgot Password / Reset Link"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A minimal single-input recovery dialog that swaps in place to a 'check your inbox' success state after submit — the focused account-recovery flow, with a…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Forgot Password / Reset Link
Source: https://codefronts.com/components/css-modals/forgot-password-reset-link/

A minimal single-input recovery dialog that swaps in place to a 'check your inbox' success state after submit — the focused account-recovery flow, with a security-conscious neutral confirmation message.
## HTML
```html
<div class="cm-02">
  <button class="cm-02__open" type="button">Forgot password?</button>

  <dialog class="cm-02__dlg" aria-labelledby="cm-02-title" aria-describedby="cm-02-desc">
    <div class="cm-02__card">
      <button class="cm-02__x" type="button" aria-label="Close dialog">&times;</button>

      <div class="cm-02__view cm-02__view--form">
        <div class="cm-02__icon" aria-hidden="true">&#9993;</div>
        <h2 id="cm-02-title" class="cm-02__title">Reset your password</h2>
        <p id="cm-02-desc" class="cm-02__desc">Enter the email tied to your account and we&#39;ll send a secure reset link.</p>
        <form class="cm-02__form" novalidate>
          <div class="cm-02__field">
            <input type="email" id="cm-02-email" class="cm-02__input" placeholder=" " required autocomplete="email">
            <label for="cm-02-email" class="cm-02__label">Email address</label>
          </div>
          <button type="submit" class="cm-02__submit">Send reset link</button>
        </form>
      </div>

      <div class="cm-02__view cm-02__view--done" hidden>
        <div class="cm-02__check" aria-hidden="true">&#10003;</div>
        <h2 class="cm-02__title">Check your inbox</h2>
        <p class="cm-02__desc">If an account exists for <b class="cm-02__mail">that address</b>, a reset link is on its way. It expires in 30&nbsp;minutes.</p>
        <button type="button" class="cm-02__submit cm-02__done-btn">Got it</button>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-02,
.cm-02 *,
.cm-02 *::before,
.cm-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-02 {
  --accent: oklch(0.74 0.15 200);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#0e1518,#07090b);
}

.cm-02__open {
  cursor: pointer;
  padding: 13px 26px;
  border-radius: 11px;
  color: #e6f2f5;
  font: 600 14px system-ui;
  border: 1px solid #263238;
  background: #111a1d;
  transition: background .2s,border-color .2s;
}

.cm-02__open:hover {
  border-color: var(--accent);
  background: #152226;
}

.cm-02__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-02__dlg {
  margin: auto;
  width: min(400px,94vw);
  padding: 0;
  border: none;
  border-radius: 18px;
  color: #e7eef0;
  text-align: center;
  background: linear-gradient(180deg,#131b1e,#0e1416);
  box-shadow: 0 30px 80px -30px #000,0 0 0 1px #223035;
  opacity: 0;
  transform: scale(.96);
  transition: opacity .26s,transform .26s,overlay .26s allow-discrete,display .26s allow-discrete;
}

.cm-02__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-02__dlg[open] {
    opacity: 0;
    transform: scale(.96);
  }
}

.cm-02__dlg::backdrop {
  background: rgba(4,8,9,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-02__dlg[open]::backdrop {
  background: rgba(4,8,9,.6);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-02__dlg[open]::backdrop {
    background: rgba(4,8,9,0);
    backdrop-filter: blur(0);
  }
}

.cm-02__card {
  position: relative;
  padding: 36px 32px 32px;
}

.cm-02__x {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #7c8a8e;
  font-size: 22px;
  cursor: pointer;
  transition: background .2s,color .2s;
}

.cm-02__x:hover {
  background: #1a2529;
  color: #e7eef0;
}

.cm-02__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-02__icon,
.cm-02__check {
  width: 60px;
  height: 60px;
  margin: 4px auto 18px;
  border-radius: 16px;
  display: grid;
  place-items: center;
  font-size: 28px;
}

.cm-02__icon {
  background: color-mix(in oklch,var(--accent) 16%,#0d1416);
  color: var(--accent);
  box-shadow: 0 0 0 1px color-mix(in oklch,var(--accent) 30%,transparent),0 0 34px -8px var(--accent);
}

.cm-02__check {
  background: color-mix(in oklch,oklch(0.8 0.18 150) 18%,#0d1416);
  color: oklch(0.85 0.18 150);
  box-shadow: 0 0 0 1px color-mix(in oklch,oklch(0.8 0.18 150) 34%,transparent),0 0 40px -8px oklch(0.8 0.18 150);
  animation: cm-02-pop .4s cubic-bezier(.2,1.4,.4,1) both;
}

@keyframes cm-02-pop {
  0% {
    transform: scale(.4);
    opacity: 0;
  }

  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.cm-02__title {
  font-size: 21px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #f0f6f7;
  margin-bottom: 10px;
}

.cm-02__desc {
  font-size: 14px;
  line-height: 1.6;
  color: #95a3a7;
  margin-bottom: 22px;
}

.cm-02__mail {
  color: #dfe9eb;
}

.cm-02__field {
  position: relative;
  text-align: left;
  margin-bottom: 14px;
}

.cm-02__input {
  width: 100%;
  padding: 18px 14px 8px;
  border-radius: 10px;
  border: 1px solid #26343a;
  background: #0c1315;
  color: #eef4f5;
  font: 15px system-ui;
  transition: border-color .2s,box-shadow .2s;
}

.cm-02__input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--accent) 28%,transparent);
}

.cm-02__label {
  position: absolute;
  left: 14px;
  top: 15px;
  color: #7f8d91;
  font-size: 15px;
  pointer-events: none;
  transition: transform .18s,font-size .18s,color .18s;
  transform-origin: left;
}

.cm-02__input:focus+.cm-02__label,
.cm-02__input:not(:placeholder-shown)+.cm-02__label {
  transform: translateY(-10px);
  font-size: 11px;
  color: var(--accent);
}

.cm-02__submit {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 10px;
  background: var(--accent);
  color: #04161a;
  font: 700 15px system-ui;
  cursor: pointer;
  transition: filter .2s,transform .1s;
}

.cm-02__submit:hover {
  filter: brightness(1.08);
}

.cm-02__submit:active {
  transform: translateY(1px);
}

.cm-02__submit:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cm-02__dlg,
    .cm-02__dlg::backdrop,
    .cm-02__check {
    transition-duration: .001s;
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-02');
  var dlg = root.querySelector('.cm-02__dlg');
  var form = root.querySelector('.cm-02__view--form');
  var done = root.querySelector('.cm-02__view--done');
  var email = root.querySelector('#cm-02-email');
  function reset(){ form.hidden = false; done.hidden = true; }
  root.querySelector('.cm-02__open').addEventListener('click', function(){ reset(); dlg.showModal(); });
  root.querySelector('.cm-02__x').addEventListener('click', function(){ dlg.close(); });
  root.querySelector('.cm-02__done-btn').addEventListener('click', function(){ dlg.close(); });
  root.querySelector('.cm-02__form').addEventListener('submit', function(e){
    e.preventDefault();
    if(!email.checkValidity()){ email.reportValidity(); return; }
    root.querySelector('.cm-02__mail').textContent = email.value;
    form.hidden = true; done.hidden = false;
    root.querySelector('.cm-02__done-btn').focus();
  });
  dlg.addEventListener('close', reset);
})();
```
