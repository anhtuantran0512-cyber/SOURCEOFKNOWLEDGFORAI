---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/shake-login-box-css/"
title: "Shake Login Box CSS"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The classic, done properly twice: a dark glassmorphism login whose card recoils with translate + rotate on wrong credentials (plus a lockout counter that…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shake Login Box CSS
Source: https://codefronts.com/motion/css-shake-animation/shake-login-box-css/

The classic, done properly twice: a dark glassmorphism login whose card recoils with translate + rotate on wrong credentials (plus a lockout counter that escalates the copy), and a minimal light version that needs zero JavaScript — the card shakes via form:has(:user-invalid) the moment either field goes bad.
## HTML
```html
<div class="shk-08-group">
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="shk-08a" aria-label="Glassmorphism login that shakes on wrong credentials">
  <div class="shk-08a__orb" aria-hidden="true"></div><div class="shk-08a__orb shk-08a__orb--2" aria-hidden="true"></div>
  <form class="shk-08a__card" id="shk-08a-form" novalidate>
    <h2 class="shk-08a__title">Sign in to Nocturne</h2>
    <p class="shk-08a__status" id="shk-08a-status" aria-live="polite">demo / demo gets you in</p>
    <label class="shk-08a__lab" for="shk-08a-user">Username</label>
    <input class="shk-08a__input" id="shk-08a-user" type="text" autocomplete="off" placeholder="demo">
    <label class="shk-08a__lab" for="shk-08a-pass">Password</label>
    <input class="shk-08a__input" id="shk-08a-pass" type="password" autocomplete="off" placeholder="demo">
    <button class="shk-08a__btn" type="submit">Sign in</button>
  </form>
</section>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-08b" aria-label="CSS-only login box shake">
  <form class="shk-08b__card" novalidate onsubmit="return false">
    <p class="shk-08b__logo" aria-hidden="true">✳</p>
    <h2 class="shk-08b__title">Welcome back</h2>
    <p class="shk-08b__note">No JavaScript here — leave a field bad and blur it.</p>
    <input class="shk-08b__input" type="email" required placeholder="Email" aria-label="Email">
    <input class="shk-08b__input" type="password" required minlength="6" placeholder="Password (6+ chars)" aria-label="Password">
    <button class="shk-08b__btn" type="button">Continue</button>
    <p class="shk-08b__fine" aria-hidden="true">form:has(input:user-invalid) → one decaying recoil</p>
  </form>
</section>
</div>
```
## CSS
```css
.shk-08-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-08-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-08a,
.shk-08a *,
.shk-08a *::before,
.shk-08a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-08a {
  --err: oklch(0.68 0.2 25);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(150deg,#0c0f1d,#151129 55%,#0a0d18);
  font-family: 'Sora','Segoe UI',system-ui,sans-serif;
}

.shk-08a__orb {
  position: absolute;
  width: 420px;
  height: 420px;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.6 0.19 285 / .5),transparent 65%);
  top: -140px;
  left: -100px;
  filter: blur(10px);
}

.shk-08a__orb--2 {
  background: radial-gradient(circle,oklch(0.7 0.15 200 / .4),transparent 65%);
  top: auto;
  left: auto;
  bottom: -160px;
  right: -120px;
}

.shk-08a__card {
  position: relative;
  width: min(380px,100%);
  padding: 36px 32px;
  border-radius: 24px;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.14);
  backdrop-filter: blur(22px);
  -webkit-backdrop-filter: blur(22px);
  box-shadow: 0 50px 100px -50px rgba(0,0,0,.9);
  display: grid;
  gap: 9px;
  transition: border-color .25s;
}

.shk-08a__card.is-denied {
  border-color: oklch(0.68 0.2 25 / .6);
  animation: shk-08a-recoil .6s cubic-bezier(.36,.07,.19,.97);
}

.shk-08a__title {
  font-size: 21px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #f1f0fb;
}

.shk-08a__status {
  font-size: 12.5px;
  color: rgba(230,228,250,.5);
  margin-bottom: 10px;
  min-height: 18px;
}

.shk-08a__status.err {
  color: oklch(0.8 0.13 25);
  font-weight: 600;
}

.shk-08a__status.ok {
  color: oklch(0.85 0.13 160);
  font-weight: 600;
}

.shk-08a__lab {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(230,228,250,.55);
}

.shk-08a__input {
  width: 100%;
  margin-bottom: 8px;
  padding: 12px 15px;
  font: inherit;
  font-size: 14.5px;
  color: #f1f0fb;
  background: rgba(10,10,24,.4);
  border: 1.5px solid rgba(255,255,255,.14);
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.shk-08a__input:focus-visible {
  border-color: oklch(0.7 0.14 285);
  box-shadow: 0 0 0 4px oklch(0.7 0.14 285 / .2);
}

.is-denied .shk-08a__input {
  border-color: oklch(0.68 0.2 25 / .55);
}

.shk-08a__btn {
  margin-top: 8px;
  padding: 14px;
  border: 0;
  border-radius: 12px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 700;
  color: #12101f;
  background: linear-gradient(180deg,#f3f1ff,#cfc8f2);
  cursor: pointer;
  transition: transform .15s,filter .2s;
}

.shk-08a__btn:hover {
  filter: brightness(1.06);
}

.shk-08a__btn:active {
  transform: scale(.98);
}

@keyframes shk-08a-recoil {
  12% {
    translate: -12px 0;
    rotate: -.6deg;
  }

  28% {
    translate: 10px 0;
    rotate: .5deg;
  }

  46% {
    translate: -7px 0;
    rotate: -.35deg;
  }

  64% {
    translate: 4px 0;
    rotate: .2deg;
  }

  82% {
    translate: -2px 0;
    rotate: 0deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-08a__card.is-denied {
    animation: none;
  }
}

.shk-08b,
.shk-08b *,
.shk-08b *::before,
.shk-08b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-08b {
  --ink: #1f1d1a;
  --err: oklch(0.58 0.19 26);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f7f4ee;
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-08b__card {
  width: min(360px,100%);
  padding: 40px 34px;
  border-radius: 22px;
  background: #fffdf9;
  border: 1.5px solid rgba(31,29,26,.12);
  box-shadow: 0 30px 70px -40px rgba(31,29,26,.5);
  display: grid;
  gap: 11px;
  text-align: center;
  transition: border-color .25s;
}

.shk-08b__card:has(.shk-08b__input:user-invalid) {
  border-color: var(--err);
  animation: shk-08b-recoil .55s cubic-bezier(.36,.07,.19,.97);
}

.shk-08b__logo {
  font-size: 30px;
  color: oklch(0.62 0.14 60);
}

.shk-08b__title {
  font-family: 'Instrument Serif',Georgia,serif;
  font-weight: 400;
  font-size: 30px;
  color: var(--ink);
}

.shk-08b__note {
  font-size: 12.5px;
  color: rgba(31,29,26,.5);
  margin-bottom: 8px;
}

.shk-08b__input {
  width: 100%;
  padding: 13px 16px;
  font: inherit;
  font-size: 14.5px;
  color: var(--ink);
  background: #f4f0e8;
  border: 1.5px solid transparent;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,background .2s;
}

.shk-08b__input:focus-visible {
  background: #fff;
  border-color: var(--ink);
}

.shk-08b__input:user-invalid {
  border-color: var(--err);
  background: oklch(0.58 0.19 26 / .06);
}

.shk-08b__btn {
  margin-top: 6px;
  padding: 14px;
  border: 0;
  border-radius: 12px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 800;
  color: #fffdf9;
  background: var(--ink);
  cursor: pointer;
  transition: background .2s,transform .15s;
}

.shk-08b__btn:hover {
  background: #38352f;
}

.shk-08b__btn:active {
  transform: scale(.98);
}

.shk-08b__fine {
  margin-top: 8px;
  font-size: 10.5px;
  letter-spacing: .04em;
  color: rgba(31,29,26,.4);
}

@keyframes shk-08b-recoil {
  12% {
    translate: -11px 0;
    rotate: -.5deg;
  }

  28% {
    translate: 9px 0;
    rotate: .4deg;
  }

  46% {
    translate: -6px 0;
    rotate: -.25deg;
  }

  64% {
    translate: 4px 0;
    rotate: .15deg;
  }

  82% {
    translate: -2px 0;
    rotate: 0deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-08b__card:has(.shk-08b__input:user-invalid) {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var form=document.getElementById('shk-08a-form'); if(!form) return;
  var user=document.getElementById('shk-08a-user'),pass=document.getElementById('shk-08a-pass'),
      status=document.getElementById('shk-08a-status'),tries=0;
  var lines=['Wrong credentials — hint: demo / demo.','Still wrong. It really is demo / demo.','Third time: type demo in BOTH fields.'];
  form.addEventListener('animationend',function(){ form.classList.remove('is-denied'); pass.select(); });
  form.addEventListener('submit',function(e){
    e.preventDefault();
    if(user.value==='demo'&&pass.value==='demo'){ status.className='shk-08a__status ok'; status.textContent='Welcome back — redirecting…'; return; }
    status.className='shk-08a__status err';
    status.textContent=lines[Math.min(tries,lines.length-1)]; tries++;
    form.classList.remove('is-denied');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ form.classList.add('is-denied'); }); });
    if(navigator.vibrate) navigator.vibrate(80);
  });
})();

/* No JavaScript — the card recoils once each time any field flips to :user-invalid. Validation, state and motion are all declared in CSS + HTML attributes. */
```
