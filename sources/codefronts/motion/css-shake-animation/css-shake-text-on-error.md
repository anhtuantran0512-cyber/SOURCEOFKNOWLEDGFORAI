---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-shake-text-on-error/"
title: "CSS Shake Text on Error"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Shaking the message instead of the box: an inline field error that drops in and rattles exactly once as it lands (so the eye snaps to the words), and a full…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shake Text on Error
Source: https://codefronts.com/motion/css-shake-animation/css-shake-text-on-error/

Shaking the message instead of the box: an inline field error that drops in and rattles exactly once as it lands (so the eye snaps to the words), and a full 'ACCESS DENIED' terminal stamp with a per-word tremble that intensifies on hover.
## HTML
```html
<div class="shk-06-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-06a" aria-label="Inline error text that shakes as it appears">
  <div class="shk-06a__card">
    <h2 class="shk-06a__title">Transfer amount</h2>
    <form class="shk-06a__form" id="shk-06a-form" novalidate>
      <div class="shk-06a__inwrap"><span class="shk-06a__cur" aria-hidden="true">$</span><input class="shk-06a__input" id="shk-06a-amt" type="text" inputmode="decimal" placeholder="0.00" aria-describedby="shk-06a-err" autocomplete="off"></div>
      <button class="shk-06a__btn" type="submit">Send money</button>
    </form>
    <p class="shk-06a__err" id="shk-06a-err" aria-live="assertive"></p>
    <p class="shk-06a__hint" aria-hidden="true">balance is $250 — try sending 900, the words do the recoil</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700;800&display=swap" rel="stylesheet">
<section class="shk-06b" aria-label="Access denied stamp with trembling words">
  <div class="shk-06b__frame">
    <p class="shk-06b__code">ERR 403 · CLEARANCE LEVEL INSUFFICIENT</p>
    <h2 class="shk-06b__stamp" aria-label="Access denied"><span aria-hidden="true" style="--d:0s">ACCESS</span><span aria-hidden="true" style="--d:.09s">DENIED</span></h2>
    <p class="shk-06b__foot">hover the stamp — the tremble doubles down</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-06-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-06-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-06a,
.shk-06a *,
.shk-06a *::before,
.shk-06a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-06a {
  --err: oklch(0.62 0.21 25);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f7f7f5,#ecece8);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-06a__card {
  width: min(420px,100%);
  padding: 34px;
  border-radius: 20px;
  background: #fff;
  border: 1px solid rgba(25,28,35,.1);
  box-shadow: 0 30px 70px -40px rgba(25,28,35,.45);
}

.shk-06a__title {
  font-size: 21px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: #191c23;
}

.shk-06a__form {
  margin-top: 18px;
  display: grid;
  gap: 12px;
}

.shk-06a__inwrap {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 16px;
  border: 1.5px solid rgba(25,28,35,.15);
  border-radius: 13px;
  transition: border-color .2s;
}

.shk-06a__inwrap:focus-within {
  border-color: #191c23;
}

.shk-06a__inwrap.bad {
  border-color: var(--err);
}

.shk-06a__cur {
  font-size: 22px;
  font-weight: 700;
  color: rgba(25,28,35,.35);
}

.shk-06a__input {
  flex: 1;
  min-width: 0;
  border: 0;
  outline: none;
  font: inherit;
  font-size: 26px;
  font-weight: 700;
  color: #191c23;
  padding: 10px 4px;
  background: transparent;
}

.shk-06a__input::placeholder {
  color: rgba(25,28,35,.25);
}

.shk-06a__btn {
  padding: 14px;
  border: 0;
  border-radius: 12px;
  font: inherit;
  font-size: 15px;
  font-weight: 800;
  color: #fff;
  background: #191c23;
  cursor: pointer;
  transition: transform .15s,background .2s;
}

.shk-06a__btn:hover {
  background: #2c313d;
}

.shk-06a__btn:active {
  transform: scale(.98);
}

.shk-06a__err {
  min-height: 22px;
  margin-top: 12px;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--err);
  display: flex;
  flex-wrap: wrap;
  gap: .28em;
}

.shk-06a__err span {
  display: inline-block;
  animation: shk-06a-drop .6s cubic-bezier(.36,.07,.19,.97) both;
  animation-delay: var(--d,0s);
}

.shk-06a__hint {
  margin-top: 14px;
  font-size: 11.5px;
  font-weight: 500;
  color: rgba(25,28,35,.45);
}

@keyframes shk-06a-drop {
  0% {
    opacity: 0;
    translate: 0 -7px;
  }

  25% {
    opacity: 1;
    translate: 0 0;
  }

  40% {
    translate: -5px 0;
  }

  55% {
    translate: 4px 0;
  }

  70% {
    translate: -2px 0;
  }

  85% {
    translate: 1px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-06a__err span {
    animation: shk-06a-fade .3s ease both;
  }
}

@keyframes shk-06a-fade {
  from {
    opacity: 0;
  }
}

.shk-06b,
.shk-06b *,
.shk-06b *::before,
.shk-06b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-06b {
  --red: oklch(0.64 0.24 27);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(80% 90% at 50% 40%,#170c0d,#0a0607 70%);
  font-family: 'JetBrains Mono',ui-monospace,monospace;
}

.shk-06b__frame {
  text-align: center;
  padding: 44px 40px;
  border: 1.5px dashed oklch(0.64 0.24 27 / .45);
  border-radius: 6px;
  background: oklch(0.64 0.24 27 / .04);
}

.shk-06b__code {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .3em;
  color: oklch(0.64 0.24 27 / .75);
}

.shk-06b__stamp {
  margin-top: 18px;
  display: flex;
  gap: .4em;
  justify-content: center;
  flex-wrap: wrap;
  font-size: clamp(38px,8vw,84px);
  font-weight: 800;
  letter-spacing: .04em;
  color: var(--red);
  text-shadow: 0 0 34px oklch(0.64 0.24 27 / .5);
}

.shk-06b__stamp span {
  display: inline-block;
  animation: shk-06b-tremble .38s steps(2,jump-none) infinite;
  animation-delay: var(--d);
}

.shk-06b__frame:hover .shk-06b__stamp span {
  animation-duration: .14s;
  text-shadow: 2px 0 0 oklch(0.7 0.2 25 / .6),-2px 0 0 oklch(0.75 0.12 220 / .6);
}

.shk-06b__foot {
  margin-top: 22px;
  font-size: 11px;
  letter-spacing: .12em;
  color: rgba(255,220,220,.35);
}

@keyframes shk-06b-tremble {
  0% {
    translate: -1.5px .5px;
    rotate: -.25deg;
  }

  50% {
    translate: 1.5px -.5px;
    rotate: .25deg;
  }

  100% {
    translate: -1.5px .5px;
    rotate: -.25deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-06b__stamp span,
    .shk-06b__frame:hover .shk-06b__stamp span {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var form=document.getElementById('shk-06a-form'); if(!form) return;
  var amt=document.getElementById('shk-06a-amt'),err=document.getElementById('shk-06a-err'),wrap=form.querySelector('.shk-06a__inwrap');
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var v=parseFloat(amt.value||'0');
    var msg=null;
    if(!amt.value.trim()) msg='Enter an amount first.';
    else if(isNaN(v)) msg='Numbers only — that isn\u2019t an amount.';
    else if(v>250) msg='Insufficient funds: your balance is $250.00.';
    wrap.classList.toggle('bad',!!msg);
    err.textContent='';
    if(!msg){ err.innerHTML='<span style="color:oklch(0.55 0.14 155)">Sent. New balance: $'+(250-v).toFixed(2)+'</span>'; return; }
    // Each word its own span with a slightly irregular delay — the rattle feels organic.
    msg.split(' ').forEach(function(w,i){
      var s=document.createElement('span'); s.textContent=w;
      s.style.setProperty('--d',(i*0.045+(i%2?0.02:0)).toFixed(3)+'s');
      err.appendChild(s);
    });
  });
})();

/* No JavaScript — two words tremble on a steps(2) micro-loop, phase-shifted by --d so they never move in lockstep; hover shortens animation-duration (same frames, 2.7× the frequency) and adds a chromatic text-shadow. */
```
