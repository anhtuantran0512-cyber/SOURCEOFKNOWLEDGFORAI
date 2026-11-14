---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-shake-animation-on-invalid-input/"
title: "CSS Shake Animation on Invalid Input"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The definitive invalid-input shake, three ways: a zero-JavaScript version driven entirely by the :user-invalid pseudo-class, a re-triggerable JavaScript…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shake Animation on Invalid Input
Source: https://codefronts.com/motion/css-shake-animation/css-shake-animation-on-invalid-input/

The definitive invalid-input shake, three ways: a zero-JavaScript version driven entirely by the :user-invalid pseudo-class, a re-triggerable JavaScript pattern with proper ARIA wiring, and a playful shake-no / nod-yes field that answers invalid AND valid input with motion.
## HTML
```html
<div class="shk-01-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-01a" aria-label="Shake on invalid input with :user-invalid, zero JavaScript">
  <form class="shk-01a__card" novalidate onsubmit="return false">
    <p class="shk-01a__badge">:user-invalid · 0 lines of JS</p>
    <h2 class="shk-01a__title">Payout email</h2>
    <p class="shk-01a__sub">Type <b>abc</b>, then click anywhere outside the field.</p>
    <div class="shk-01a__field">
      <label class="shk-01a__label" for="shk-01a-email">Email address</label>
      <input class="shk-01a__input" id="shk-01a-email" type="email" required placeholder="[email protected]" autocomplete="off" spellcheck="false">
      <p class="shk-01a__msg"><span>That doesn't look like an email — check for a typo.</span></p>
    </div>
  </form>
</section>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<section class="shk-01b" aria-label="Re-triggerable shake on invalid input with ARIA">
  <div class="shk-01b__card">
    <h2 class="shk-01b__title">Claim your <em>handle</em></h2>
    <p class="shk-01b__sub">Lowercase letters, digits and dashes. At least 3 characters.</p>
    <form class="shk-01b__row" novalidate>
      <span class="shk-01b__at" aria-hidden="true">@</span>
      <input class="shk-01b__input" id="shk-01b-handle" type="text" placeholder="your-name" autocomplete="off" spellcheck="false" aria-describedby="shk-01b-msg">
      <button class="shk-01b__btn" type="submit">Check</button>
    </form>
    <p class="shk-01b__msg" id="shk-01b-msg" aria-live="polite"></p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="shk-01c" aria-label="Field that shakes horizontally when invalid and nods vertically when valid">
  <div class="shk-01c__card">
    <p class="shk-01c__eyebrow">Body language for forms</p>
    <h2 class="shk-01c__title">Shake “no”, nod “yes”</h2>
    <div class="shk-01c__field">
      <label class="shk-01c__label" for="shk-01c-code">Invite code <span>· exactly 6 digits</span></label>
      <input class="shk-01c__input" id="shk-01c-code" type="text" inputmode="numeric" pattern="[0-9]{6}" required placeholder="000000" maxlength="6" autocomplete="off">
      <p class="shk-01c__verdict" aria-hidden="true"><span class="shk-01c__no">✕ shakes side-to-side</span><span class="shk-01c__yes">✓ nods up-and-down</span></p>
    </div>
    <p class="shk-01c__hint" aria-hidden="true">try “12ab” then “123456” — blur the field between tries</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-01-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-01-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-01a,
.shk-01a *,
.shk-01a *::before,
.shk-01a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-01a {
  --err: oklch(0.68 0.21 25);
  --line: rgba(148,180,255,.16);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 90% at 50% 0%,#141b28,#0a0e16);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-01a__card {
  width: min(430px,100%);
  padding: 34px 32px 30px;
  border-radius: 20px;
  background: linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.02));
  border: 1px solid var(--line);
  box-shadow: 0 40px 80px -40px rgba(0,0,0,.8);
}

.shk-01a__badge {
  display: inline-block;
  font-size: 10.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  font-weight: 600;
  color: oklch(0.8 0.14 160);
  background: oklch(0.8 0.14 160 / .1);
  border: 1px solid oklch(0.8 0.14 160 / .25);
  padding: 5px 10px;
  border-radius: 999px;
  margin-bottom: 18px;
}

.shk-01a__title {
  font-size: 24px;
  font-weight: 600;
  color: #eef3ff;
  letter-spacing: -.01em;
}

.shk-01a__sub {
  margin-top: 6px;
  font-size: 13.5px;
  color: rgba(210,222,245,.55);
}

.shk-01a__sub b {
  color: rgba(230,238,255,.85);
}

.shk-01a__field {
  margin-top: 24px;
}

.shk-01a__field:has(.shk-01a__input:user-invalid) {
  animation: shk-01a-no .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-01a__label {
  display: block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: rgba(210,222,245,.6);
  margin-bottom: 8px;
}

.shk-01a__input {
  width: 100%;
  padding: 13px 16px;
  font: inherit;
  font-size: 15px;
  color: #eef3ff;
  background: rgba(10,14,22,.6);
  border: 1.5px solid var(--line);
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
  caret-color: oklch(0.8 0.14 160);
}

.shk-01a__input::placeholder {
  color: rgba(210,222,245,.3);
}

.shk-01a__input:focus-visible {
  border-color: oklch(0.75 0.12 250);
  box-shadow: 0 0 0 4px oklch(0.75 0.12 250 / .18);
}

.shk-01a__input:user-invalid {
  border-color: var(--err);
  box-shadow: 0 0 0 4px oklch(0.68 0.21 25 / .16);
}

.shk-01a__msg {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .3s ease,margin-top .3s ease;
}

.shk-01a__msg span {
  overflow: hidden;
  font-size: 13px;
  color: var(--err);
}

.shk-01a__field:has(.shk-01a__input:user-invalid) .shk-01a__msg {
  grid-template-rows: 1fr;
  margin-top: 8px;
}

@keyframes shk-01a-no {
  20% {
    translate: -9px 0;
  }

  40% {
    translate: 7px 0;
  }

  60% {
    translate: -5px 0;
  }

  80% {
    translate: 3px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-01a__field:has(.shk-01a__input:user-invalid) {
    animation: none;
  }
}

.shk-01b,
.shk-01b *,
.shk-01b *::before,
.shk-01b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-01b {
  --ink: #231f1a;
  --err: oklch(0.55 0.19 27);
  --ok: oklch(0.55 0.14 155);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#faf7f0,#f1ebdd);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.shk-01b__card {
  width: min(480px,100%);
  text-align: center;
}

.shk-01b__title {
  font-family: 'Instrument Serif',Georgia,serif;
  font-weight: 400;
  font-size: clamp(34px,5vw,46px);
  color: var(--ink);
  letter-spacing: -.01em;
}

.shk-01b__title em {
  font-style: italic;
  color: oklch(0.6 0.13 55);
}

.shk-01b__sub {
  margin-top: 10px;
  font-size: 14px;
  color: rgba(35,31,26,.55);
}

.shk-01b__row {
  margin-top: 26px;
  display: flex;
  align-items: center;
  gap: 0;
  background: #fff;
  border: 1.5px solid rgba(35,31,26,.16);
  border-radius: 14px;
  padding: 6px 6px 6px 18px;
  box-shadow: 0 12px 30px -18px rgba(35,31,26,.35);
  transition: border-color .2s,box-shadow .2s;
}

.shk-01b__row:focus-within {
  border-color: var(--ink);
  box-shadow: 0 0 0 4px rgba(35,31,26,.08);
}

.shk-01b__row.is-error {
  border-color: var(--err);
  animation: shk-01b-shake .46s cubic-bezier(.36,.07,.19,.97);
}

.shk-01b__row.is-ok {
  border-color: var(--ok);
}

.shk-01b__at {
  font-weight: 700;
  color: rgba(35,31,26,.4);
  margin-right: 6px;
}

.shk-01b__input {
  flex: 1;
  min-width: 0;
  border: 0;
  outline: none;
  font: inherit;
  font-size: 16px;
  color: var(--ink);
  background: transparent;
  padding: 10px 4px;
}

.shk-01b__btn {
  flex: none;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: #faf7f0;
  background: var(--ink);
  border: 0;
  border-radius: 9px;
  padding: 11px 20px;
  cursor: pointer;
  transition: transform .15s,background .2s;
}

.shk-01b__btn:hover {
  background: #3a342c;
}

.shk-01b__btn:active {
  transform: scale(.96);
}

.shk-01b__msg {
  min-height: 22px;
  margin-top: 12px;
  font-size: 13.5px;
  color: var(--err);
}

.shk-01b__msg.is-ok {
  color: var(--ok);
}

@keyframes shk-01b-shake {
  20% {
    translate: -8px 0;
  }

  40% {
    translate: 7px 0;
  }

  60% {
    translate: -4px 0;
  }

  80% {
    translate: 2px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-01b__row.is-error {
    animation: none;
  }
}

.shk-01c,
.shk-01c *,
.shk-01c *::before,
.shk-01c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-01c {
  --err: oklch(0.66 0.21 22);
  --ok: oklch(0.75 0.16 160);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(160deg,#12101d,#1c1030);
  font-family: 'Sora','Segoe UI',system-ui,sans-serif;
}

.shk-01c__card {
  width: min(440px,100%);
  padding: 36px 34px;
  border-radius: 22px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(190,170,255,.16);
  box-shadow: 0 40px 90px -45px rgba(0,0,0,.9);
}

.shk-01c__eyebrow {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: oklch(0.75 0.14 300);
}

.shk-01c__title {
  margin-top: 10px;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: #f2eeff;
}

.shk-01c__field {
  margin-top: 26px;
}

.shk-01c__label {
  display: block;
  font-size: 12.5px;
  font-weight: 600;
  color: rgba(230,222,255,.75);
  margin-bottom: 9px;
}

.shk-01c__label span {
  font-weight: 400;
  color: rgba(230,222,255,.4);
}

.shk-01c__input {
  width: 100%;
  padding: 14px 18px;
  font: inherit;
  font-size: 22px;
  letter-spacing: .35em;
  color: #f2eeff;
  background: rgba(10,8,20,.55);
  border: 1.5px solid rgba(190,170,255,.2);
  border-radius: 14px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.shk-01c__input:focus-visible {
  border-color: oklch(0.75 0.14 300);
  box-shadow: 0 0 0 4px oklch(0.75 0.14 300 / .2);
}

.shk-01c__input:user-invalid {
  border-color: var(--err);
  animation: shk-01c-no .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-01c__input:user-valid {
  border-color: var(--ok);
  animation: shk-01c-yes .55s cubic-bezier(.34,1.56,.64,1);
}

.shk-01c__verdict {
  display: flex;
  gap: 18px;
  margin-top: 12px;
  font-size: 12px;
}

.shk-01c__no {
  color: var(--err);
  opacity: .35;
  transition: opacity .2s;
}

.shk-01c__yes {
  color: var(--ok);
  opacity: .35;
  transition: opacity .2s;
}

.shk-01c__field:has(:user-invalid) .shk-01c__no {
  opacity: 1;
}

.shk-01c__field:has(:user-valid) .shk-01c__yes {
  opacity: 1;
}

.shk-01c__hint {
  margin-top: 22px;
  font-size: 11.5px;
  color: rgba(230,222,255,.35);
}

@keyframes shk-01c-no {
  20% {
    translate: -9px 0;
  }

  40% {
    translate: 8px 0;
  }

  60% {
    translate: -5px 0;
  }

  80% {
    translate: 3px 0;
  }
}

@keyframes shk-01c-yes {
  25% {
    translate: 0 7px;
  }

  55% {
    translate: 0 -4px;
  }

  80% {
    translate: 0 2px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-01c__input:user-invalid,
    .shk-01c__input:user-valid {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the browser validates type="email" + required; :user-invalid matches only after real interaction, :has() lifts the state onto the wrapper, and the animation plays once per invalid flip. */

(function(){
  var form=document.querySelector('.shk-01b__row'); if(!form) return;
  var input=form.querySelector('.shk-01b__input');
  var msg=document.getElementById('shk-01b-msg');
  // Remove the class when the animation finishes so the NEXT failure can replay it.
  form.addEventListener('animationend',function(){ form.classList.remove('is-error'); });
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var ok=/^[a-z0-9-]{3,}$/.test(input.value);
    form.classList.toggle('is-ok',ok);
    msg.classList.toggle('is-ok',ok);
    input.setAttribute('aria-invalid',String(!ok));
    if(ok){ msg.textContent='@'+input.value+' is available — nice pick.'; return; }
    // Message updates on every invalid submit; the shake only replays after
    // the previous one finishes (animationend removes is-error). One shake
    // per ~460ms submit-attempt window — the animation IS the feedback, so
    // hammering the button faster than the shake completes shouldn't stack
    // shakes on top of each other.
    msg.textContent=input.value.trim()===''?'Type a handle first.':'Only a–z, 0–9 and dashes (3+ characters).';
    if(form.classList.contains('is-error')) return;
    form.classList.add('is-error');
  });
})();

/* No JavaScript — :user-invalid plays a horizontal “no” shake, :user-valid a vertical “yes” nod. Both re-evaluate on blur, so each attempt answers with fresh body language. */
```
