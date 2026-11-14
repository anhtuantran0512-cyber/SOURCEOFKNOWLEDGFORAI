---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-shake-form-on-submit-error/"
title: "CSS Shake Form on Submit Error"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Two ways to shake an entire form on a failed submit: the production JavaScript pattern (intercept submit, shake the card, announce the error politely, settle…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shake Form on Submit Error
Source: https://codefronts.com/motion/css-shake-animation/css-shake-form-on-submit-error/

Two ways to shake an entire form on a failed submit: the production JavaScript pattern (intercept submit, shake the card, announce the error politely, settle into a success state when fixed) and a zero-JS fallback where fieldset:has(:user-invalid) recoils the moment the browser flags any field.
## HTML
```html
<div class="shk-02-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-02a" aria-label="Form card that shakes on failed submit">
  <div class="shk-02a__card" id="shk-02a-card">
    <div class="shk-02a__banner" id="shk-02a-banner" aria-live="polite"></div>
    <h2 class="shk-02a__title">Get the drop list</h2>
    <p class="shk-02a__sub">One email a month. Unsubscribe anytime.</p>
    <form class="shk-02a__form" id="shk-02a-form" novalidate>
      <label class="shk-02a__label" for="shk-02a-email">Work email</label>
      <input class="shk-02a__input" id="shk-02a-email" type="email" required placeholder="[email protected]" autocomplete="off" spellcheck="false">
      <button class="shk-02a__btn" type="submit">Subscribe →</button>
    </form>
    <p class="shk-02a__hint" aria-hidden="true">hit Subscribe while empty or malformed — the whole card recoils</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400..800&display=swap" rel="stylesheet">
<section class="shk-02b" aria-label="Form that recoils via CSS :has when any field goes invalid">
  <form class="shk-02b__card" novalidate onsubmit="return false">
    <p class="shk-02b__badge">form:has(:user-invalid) · no JS</p>
    <h2 class="shk-02b__title">RSVP</h2>
    <div class="shk-02b__grid">
      <div class="shk-02b__f"><label class="shk-02b__label" for="shk-02b-name">Full name</label><input class="shk-02b__input" id="shk-02b-name" type="text" required minlength="2" placeholder="Ada Lovelace"></div>
      <div class="shk-02b__f"><label class="shk-02b__label" for="shk-02b-mail">Email</label><input class="shk-02b__input" id="shk-02b-mail" type="email" required placeholder="[email protected]"></div>
    </div>
    <button class="shk-02b__btn" type="button">Reserve my seat</button>
    <p class="shk-02b__hint" aria-hidden="true">CSS can't hear the click — but the instant a touched field goes invalid, the whole card recoils</p>
  </form>
</section>
</div>
```
## CSS
```css
.shk-02-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-02-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-02a,
.shk-02a *,
.shk-02a *::before,
.shk-02a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-02a {
  --err: oklch(0.67 0.2 25);
  --ok: oklch(0.74 0.15 158);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 120% at 80% 0%,#101826,#0b0f17 60%);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-02a__card {
  width: min(460px,100%);
  padding: 34px;
  border-radius: 22px;
  background: linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.02));
  border: 1.5px solid rgba(150,180,255,.16);
  box-shadow: 0 50px 100px -50px rgba(0,0,0,.9);
  transition: border-color .25s;
}

.shk-02a__card.is-error {
  border-color: var(--err);
  animation: shk-02a-recoil .55s cubic-bezier(.36,.07,.19,.97);
}

.shk-02a__card.is-ok {
  border-color: var(--ok);
}

.shk-02a__banner {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .3s,margin-bottom .3s;
  font-size: 13px;
  font-weight: 600;
}

.shk-02a__banner.show {
  grid-template-rows: 1fr;
  margin-bottom: 16px;
}

.shk-02a__banner>span {
  overflow: hidden;
  display: block;
  padding: 0;
}

.shk-02a__banner.show>span {
  padding: 10px 14px;
  border-radius: 10px;
}

.shk-02a__banner.err>span {
  color: oklch(0.85 0.09 25);
  background: oklch(0.67 0.2 25 / .14);
  border: 1px solid oklch(0.67 0.2 25 / .3);
}

.shk-02a__banner.ok>span {
  color: oklch(0.88 0.09 158);
  background: oklch(0.74 0.15 158 / .12);
  border: 1px solid oklch(0.74 0.15 158 / .3);
}

.shk-02a__title {
  font-size: 25px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: #eef3ff;
}

.shk-02a__sub {
  margin-top: 7px;
  font-size: 14px;
  color: rgba(210,222,245,.55);
}

.shk-02a__form {
  margin-top: 22px;
  display: grid;
  gap: 12px;
}

.shk-02a__label {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(210,222,245,.6);
}

.shk-02a__input {
  width: 100%;
  padding: 13px 16px;
  font: inherit;
  font-size: 15px;
  color: #eef3ff;
  background: rgba(8,12,20,.6);
  border: 1.5px solid rgba(150,180,255,.18);
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.shk-02a__input:focus-visible {
  border-color: oklch(0.72 0.13 250);
  box-shadow: 0 0 0 4px oklch(0.72 0.13 250 / .18);
}

.is-error .shk-02a__input {
  border-color: var(--err);
}

.shk-02a__btn {
  margin-top: 4px;
  padding: 14px 18px;
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  color: #0b0f17;
  background: linear-gradient(180deg,#eef3ff,#c9d8f5);
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  transition: transform .15s,filter .2s;
}

.shk-02a__btn:hover {
  filter: brightness(1.06);
}

.shk-02a__btn:active {
  transform: scale(.98);
}

.shk-02a__hint {
  margin-top: 14px;
  font-size: 11.5px;
  color: rgba(210,222,245,.35);
  text-align: center;
}

@keyframes shk-02a-recoil {
  15% {
    translate: -11px 0;
    rotate: -.5deg;
  }

  30% {
    translate: 9px 0;
    rotate: .45deg;
  }

  45% {
    translate: -7px 0;
    rotate: -.35deg;
  }

  60% {
    translate: 5px 0;
    rotate: .25deg;
  }

  75% {
    translate: -3px 0;
    rotate: -.1deg;
  }

  90% {
    translate: 1px 0;
    rotate: 0deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-02a__card.is-error {
    animation: none;
  }
}

.shk-02b,
.shk-02b *,
.shk-02b *::before,
.shk-02b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-02b {
  --ink: #20242c;
  --err: oklch(0.6 0.2 25);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #eceff4;
  font-family: 'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;
}

.shk-02b__card {
  width: min(500px,100%);
  padding: 36px;
  border-radius: 18px;
  background: #fff;
  border: 1.5px solid rgba(32,36,44,.12);
  box-shadow: 0 24px 60px -30px rgba(32,36,44,.35);
  transition: border-color .25s;
}

.shk-02b__card:has(.shk-02b__input:user-invalid) {
  border-color: var(--err);
  animation: shk-02b-recoil .55s cubic-bezier(.36,.07,.19,.97);
}

.shk-02b__badge {
  display: inline-block;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: oklch(0.5 0.12 265);
  background: oklch(0.5 0.12 265 / .09);
  border: 1px solid oklch(0.5 0.12 265 / .22);
  padding: 5px 10px;
  border-radius: 999px;
}

.shk-02b__title {
  margin-top: 16px;
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--ink);
}

.shk-02b__grid {
  margin-top: 20px;
  display: grid;
  gap: 14px;
}

.shk-02b__label {
  display: block;
  font-size: 12px;
  font-weight: 600;
  color: rgba(32,36,44,.6);
  margin-bottom: 7px;
}

.shk-02b__input {
  width: 100%;
  padding: 12px 15px;
  font: inherit;
  font-size: 15px;
  color: var(--ink);
  background: #f5f7fa;
  border: 1.5px solid rgba(32,36,44,.14);
  border-radius: 11px;
  outline: none;
  transition: border-color .2s,box-shadow .2s,background .2s;
}

.shk-02b__input:focus-visible {
  background: #fff;
  border-color: var(--ink);
  box-shadow: 0 0 0 4px rgba(32,36,44,.08);
}

.shk-02b__input:user-invalid {
  border-color: var(--err);
  background: oklch(0.6 0.2 25 / .05);
}

.shk-02b__btn {
  margin-top: 20px;
  width: 100%;
  padding: 14px;
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  background: var(--ink);
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  transition: transform .15s,background .2s;
}

.shk-02b__btn:hover {
  background: #31363f;
}

.shk-02b__btn:active {
  transform: scale(.985);
}

.shk-02b__hint {
  margin-top: 16px;
  font-size: 11.5px;
  color: rgba(32,36,44,.45);
}

@keyframes shk-02b-recoil {
  15% {
    translate: -10px 0;
    rotate: -.4deg;
  }

  30% {
    translate: 8px 0;
    rotate: .35deg;
  }

  45% {
    translate: -6px 0;
    rotate: -.25deg;
  }

  60% {
    translate: 4px 0;
    rotate: .15deg;
  }

  80% {
    translate: -2px 0;
    rotate: 0deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-02b__card:has(.shk-02b__input:user-invalid) {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var form=document.getElementById('shk-02a-form'),card=document.getElementById('shk-02a-card'),banner=document.getElementById('shk-02a-banner');
  if(!form||!card||!banner) return;
  var email=document.getElementById('shk-02a-email');
  card.addEventListener('animationend',function(){ card.classList.remove('is-error'); });
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var valid=form.checkValidity();
    banner.className='shk-02a__banner show '+(valid?'ok':'err');
    banner.innerHTML='<span>'+(valid?'You are on the list. First drop lands Friday.':'Subscribe failed — enter a valid email address.')+'</span>';
    card.classList.toggle('is-ok',valid);
    email.setAttribute('aria-invalid',String(!valid));
    if(!valid){ card.classList.remove('is-error'); card.classList.add('is-error'); }
  });
})();

/* No JavaScript — form:has(input:user-invalid) recoils the card the moment any interacted field is invalid. It can't detect the submit click itself; that's the honest trade-off vs the JS variant. */
```
