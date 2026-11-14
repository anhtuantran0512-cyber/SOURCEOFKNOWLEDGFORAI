---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-form-validation-failure-shake/"
title: "CSS Form Validation Failure Shake"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Validation failure as choreography: a checkout form that shakes only its invalid fields — staggered 70ms apart so the eye is led down the fixlist in order —…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Form Validation Failure Shake
Source: https://codefronts.com/motion/css-shake-animation/css-form-validation-failure-shake/

Validation failure as choreography: a checkout form that shakes only its invalid fields — staggered 70ms apart so the eye is led down the fixlist in order — and a pure-CSS counterpart where the submit button itself wobbles and refuses while the form still contains an invalid field.
## HTML
```html
<div class="shk-07-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&display=swap" rel="stylesheet">
<section class="shk-07a" aria-label="Checkout form with staggered validation shakes">
  <form class="shk-07a__card" id="shk-07a-form" novalidate>
    <div class="shk-07a__head"><h2 class="shk-07a__title">Shipping details</h2><p class="shk-07a__sum" id="shk-07a-sum" aria-live="polite"></p></div>
    <div class="shk-07a__field"><label class="shk-07a__label" for="shk-07a-name">Full name</label><input class="shk-07a__input" id="shk-07a-name" type="text" required placeholder="Riley Chen"></div>
    <div class="shk-07a__field"><label class="shk-07a__label" for="shk-07a-street">Street address</label><input class="shk-07a__input" id="shk-07a-street" type="text" required placeholder="410 Fern Ave"></div>
    <div class="shk-07a__two">
      <div class="shk-07a__field"><label class="shk-07a__label" for="shk-07a-city">City</label><input class="shk-07a__input" id="shk-07a-city" type="text" required placeholder="Portland"></div>
      <div class="shk-07a__field"><label class="shk-07a__label" for="shk-07a-zip">ZIP</label><input class="shk-07a__input" id="shk-07a-zip" type="text" required pattern="[0-9]{5}" placeholder="97201"></div>
    </div>
    <button class="shk-07a__btn" type="submit">Continue to payment</button>
    <p class="shk-07a__hint" aria-hidden="true">submit empty — failures shake one after another, top to bottom</p>
  </form>
</section>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400..800&display=swap" rel="stylesheet">
<section class="shk-07b" aria-label="Submit button that wobbles while the form is invalid">
  <form class="shk-07b__card" novalidate onsubmit="return false">
    <p class="shk-07b__badge">form:has(:user-invalid) · no JS</p>
    <h2 class="shk-07b__title">Create workspace</h2>
    <div class="shk-07b__field"><label class="shk-07b__label" for="shk-07b-ws">Workspace name <span>· 3+ characters</span></label><input class="shk-07b__input" id="shk-07b-ws" type="text" required minlength="3" placeholder="northwind-labs"></div>
    <button class="shk-07b__btn" type="button"><span>Create workspace</span></button>
    <p class="shk-07b__hint" aria-hidden="true">type 1 character, click away, then hover the button — it shakes its head until the form is valid</p>
  </form>
</section>
</div>
```
## CSS
```css
.shk-07-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-07-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-07a,
.shk-07a *,
.shk-07a *::before,
.shk-07a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-07a {
  --err: oklch(0.63 0.2 25);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(165deg,#141821,#0d1017);
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-07a__card {
  width: min(470px,100%);
  padding: 32px;
  border-radius: 20px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(160,185,225,.15);
  box-shadow: 0 45px 90px -50px rgba(0,0,0,.9);
  display: grid;
  gap: 15px;
}

.shk-07a__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
}

.shk-07a__title {
  font-size: 21px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: #edf2fb;
}

.shk-07a__sum {
  font-size: 12px;
  font-weight: 700;
  color: var(--err);
  min-height: 16px;
  text-align: right;
}

.shk-07a__two {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 12px;
}

.shk-07a__field.is-fail {
  animation: shk-07a-shake .5s var(--d,0s) cubic-bezier(.36,.07,.19,.97) both;
}

.shk-07a__field.is-fail .shk-07a__input {
  border-color: var(--err);
  box-shadow: 0 0 0 3px oklch(0.63 0.2 25 / .15);
}

.shk-07a__label {
  display: block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(220,230,250,.55);
  margin-bottom: 7px;
}

.shk-07a__input {
  width: 100%;
  padding: 12px 15px;
  font: inherit;
  font-size: 14.5px;
  color: #edf2fb;
  background: rgba(8,11,18,.55);
  border: 1.5px solid rgba(160,185,225,.18);
  border-radius: 11px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.shk-07a__input:focus-visible {
  border-color: oklch(0.74 0.12 250);
  box-shadow: 0 0 0 3px oklch(0.74 0.12 250 / .18);
}

.shk-07a__btn {
  margin-top: 4px;
  padding: 14px;
  border: 0;
  border-radius: 12px;
  font: inherit;
  font-size: 15px;
  font-weight: 800;
  color: #0d1017;
  background: linear-gradient(180deg,#f2f6ff,#ccd9f2);
  cursor: pointer;
  transition: transform .15s,filter .2s;
}

.shk-07a__btn:hover {
  filter: brightness(1.05);
}

.shk-07a__btn:active {
  transform: scale(.985);
}

.shk-07a__hint {
  font-size: 11.5px;
  color: rgba(220,230,250,.35);
  text-align: center;
}

@keyframes shk-07a-shake {
  15% {
    translate: -8px 0;
  }

  30% {
    translate: 7px 0;
  }

  45% {
    translate: -5px 0;
  }

  60% {
    translate: 3px 0;
  }

  80% {
    translate: -1px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-07a__field.is-fail {
    animation: none;
  }
}

.shk-07b,
.shk-07b *,
.shk-07b *::before,
.shk-07b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-07b {
  --ink: #242526;
  --err: oklch(0.6 0.2 25);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f3f1ec;
  font-family: 'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;
}

.shk-07b__card {
  width: min(440px,100%);
  padding: 36px;
  border-radius: 20px;
  background: #fff;
  border: 1.5px solid rgba(36,37,38,.12);
  box-shadow: 0 26px 60px -32px rgba(36,37,38,.4);
  display: grid;
  gap: 18px;
}

.shk-07b__badge {
  justify-self: start;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: oklch(0.5 0.12 265);
  background: oklch(0.5 0.12 265 / .08);
  border: 1px solid oklch(0.5 0.12 265 / .22);
  padding: 5px 10px;
  border-radius: 999px;
}

.shk-07b__title {
  font-size: 28px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--ink);
}

.shk-07b__label {
  display: block;
  font-size: 12.5px;
  font-weight: 600;
  color: rgba(36,37,38,.65);
  margin-bottom: 8px;
}

.shk-07b__label span {
  font-weight: 400;
  color: rgba(36,37,38,.4);
}

.shk-07b__input {
  width: 100%;
  padding: 13px 16px;
  font: inherit;
  font-size: 15px;
  color: var(--ink);
  background: #f6f5f1;
  border: 1.5px solid rgba(36,37,38,.14);
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.shk-07b__input:focus-visible {
  border-color: var(--ink);
  box-shadow: 0 0 0 4px rgba(36,37,38,.08);
  background: #fff;
}

.shk-07b__input:user-invalid {
  border-color: var(--err);
  background: oklch(0.6 0.2 25 / .05);
}

.shk-07b__btn {
  padding: 15px;
  border: 0;
  border-radius: 13px;
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  background: var(--ink);
  cursor: pointer;
  transition: background .2s,opacity .2s;
  overflow: hidden;
}

.shk-07b__btn span {
  display: inline-block;
}

.shk-07b__card:has(.shk-07b__input:user-invalid) .shk-07b__btn {
  cursor: not-allowed;
  opacity: .75;
  background: color-mix(in oklab,var(--ink) 80%,var(--err));
}

.shk-07b__card:has(.shk-07b__input:user-invalid) .shk-07b__btn:hover span {
  animation: shk-07b-refuse .4s cubic-bezier(.36,.07,.19,.97);
}

.shk-07b__card:not(:has(.shk-07b__input:user-invalid)) .shk-07b__btn:hover {
  background: #3a3b3d;
}

.shk-07b__hint {
  font-size: 11.5px;
  color: rgba(36,37,38,.45);
}

@keyframes shk-07b-refuse {
  20% {
    translate: -6px 0;
  }

  40% {
    translate: 5px 0;
  }

  60% {
    translate: -3px 0;
  }

  80% {
    translate: 2px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-07b__card:has(.shk-07b__input:user-invalid) .shk-07b__btn:hover span {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var form=document.getElementById('shk-07a-form'); if(!form) return;
  var sum=document.getElementById('shk-07a-sum');
  form.addEventListener('animationend',function(e){ var f=e.target.closest('.shk-07a__field'); if(f) f.classList.remove('is-fail'); },true);
  form.addEventListener('input',function(e){ var f=e.target.closest('.shk-07a__field'); if(f) f.classList.remove('is-fail'); });
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var fails=[].filter.call(form.elements,function(el){ return el.willValidate&&!el.checkValidity(); });
    if(!fails.length){ sum.style.color='oklch(0.78 0.14 158)'; sum.textContent='All good — onward.'; return; }
    sum.style.color=''; sum.textContent=fails.length+(fails.length===1?' field needs':' fields need')+' attention';
    fails.forEach(function(el,i){
      var f=el.closest('.shk-07a__field'); if(!f) return;
      f.style.setProperty('--d',(i*70)+'ms');
      f.classList.remove('is-fail'); void 0; f.classList.add('is-fail');
    });
    fails[0].focus({preventScroll:true});
  });
})();

/* No JavaScript — while any field is :user-invalid, :has() flips the button into refusal mode: not-allowed cursor, desaturated blend via color-mix(), and a head-shake on hover. Fix the field and the same selector releases everything. */
```
