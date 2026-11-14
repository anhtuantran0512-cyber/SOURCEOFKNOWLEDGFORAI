---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-password-error-shake-effect/"
title: "CSS Password Error Shake Effect"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The two password shakes every product ends up needing: a desktop unlock screen whose field recoils on a wrong password (with a caps-lock warning, because…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Password Error Shake Effect
Source: https://codefronts.com/motion/css-shake-animation/css-password-error-shake-effect/

The two password shakes every product ends up needing: a desktop unlock screen whose field recoils on a wrong password (with a caps-lock warning, because that's why half of all passwords fail), and a mobile-style 4-digit PIN pad whose dots rattle and flush red before clearing for another try.
## HTML
```html
<div class="shk-03-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-03a" aria-label="Unlock screen with wrong-password shake">
  <div class="shk-03a__panel">
    <div class="shk-03a__avatar" id="shk-03a-avatar" aria-hidden="true"><span>KM</span></div>
    <p class="shk-03a__name">Kai Moreau</p>
    <form class="shk-03a__row" id="shk-03a-form">
      <input class="shk-03a__input" id="shk-03a-pass" type="password" placeholder="Enter password" aria-label="Password" autocomplete="off">
      <button class="shk-03a__go" type="submit" aria-label="Unlock">→</button>
    </form>
    <p class="shk-03a__caps" id="shk-03a-caps" hidden>⇪ Caps Lock is on</p>
    <p class="shk-03a__status" id="shk-03a-status" aria-live="polite">Hint: the password is <b>demo123</b></p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-03b" aria-label="PIN pad with wrong-code shake">
  <div class="shk-03b__phone">
    <p class="shk-03b__label" id="shk-03b-label" aria-live="polite">Enter passcode · try 2468</p>
    <div class="shk-03b__dots" id="shk-03b-dots" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
    <div class="shk-03b__pad" id="shk-03b-pad">
      <button type="button">1</button><button type="button">2</button><button type="button">3</button>
      <button type="button">4</button><button type="button">5</button><button type="button">6</button>
      <button type="button">7</button><button type="button">8</button><button type="button">9</button>
      <span></span><button type="button">0</button><button type="button" data-del aria-label="Delete">⌫</button>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.shk-03-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-03-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-03a,
.shk-03a *,
.shk-03a *::before,
.shk-03a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-03a {
  --err: oklch(0.68 0.2 25);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(90% 120% at 50% 110%,#2b3040,#101320 55%);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-03a__panel {
  display: grid;
  justify-items: center;
  gap: 12px;
  text-align: center;
}

.shk-03a__avatar {
  width: 88px;
  height: 88px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: linear-gradient(150deg,oklch(0.7 0.13 260),oklch(0.55 0.16 300));
  border: 2px solid rgba(255,255,255,.25);
  box-shadow: 0 20px 50px -20px rgba(0,0,0,.8);
}

.shk-03a__avatar span {
  font-size: 26px;
  font-weight: 800;
  color: #fff;
  letter-spacing: .02em;
}

.shk-03a__avatar.is-wrong {
  animation: shk-03a-head .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-03a__name {
  font-size: 16px;
  font-weight: 700;
  color: #eef1fa;
}

.shk-03a__row {
  display: flex;
  align-items: center;
  gap: 8px;
  width: min(300px,84vw);
  padding: 5px 5px 5px 16px;
  background: rgba(255,255,255,.09);
  border: 1.5px solid rgba(255,255,255,.14);
  border-radius: 999px;
  backdrop-filter: blur(10px);
  transition: border-color .2s;
}

.shk-03a__row:focus-within {
  border-color: rgba(255,255,255,.4);
}

.shk-03a__row.is-wrong {
  border-color: var(--err);
  animation: shk-03a-shake .45s cubic-bezier(.36,.07,.19,.97);
}

.shk-03a__input {
  flex: 1;
  min-width: 0;
  background: transparent;
  border: 0;
  outline: none;
  font: inherit;
  font-size: 14.5px;
  color: #eef1fa;
  letter-spacing: .08em;
}

.shk-03a__input::placeholder {
  color: rgba(238,241,250,.4);
  letter-spacing: 0;
}

.shk-03a__go {
  flex: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 0;
  cursor: pointer;
  font-size: 15px;
  color: #101320;
  background: #eef1fa;
  transition: transform .15s;
}

.shk-03a__go:active {
  transform: scale(.92);
}

.shk-03a__caps {
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.83 0.14 85);
  background: oklch(0.83 0.14 85 / .12);
  border: 1px solid oklch(0.83 0.14 85 / .3);
  padding: 4px 12px;
  border-radius: 999px;
}

.shk-03a__status {
  font-size: 12.5px;
  color: rgba(238,241,250,.5);
  min-height: 18px;
}

.shk-03a__status b {
  color: rgba(238,241,250,.8);
}

.shk-03a__status.err {
  color: oklch(0.8 0.12 25);
}

.shk-03a__status.ok {
  color: oklch(0.85 0.12 158);
}

@keyframes shk-03a-shake {
  20% {
    translate: -10px 0;
  }

  40% {
    translate: 8px 0;
  }

  60% {
    translate: -6px 0;
  }

  80% {
    translate: 3px 0;
  }
}

@keyframes shk-03a-head {
  20% {
    rotate: -6deg;
  }

  40% {
    rotate: 5deg;
  }

  60% {
    rotate: -3deg;
  }

  80% {
    rotate: 2deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-03a__row.is-wrong,
    .shk-03a__avatar.is-wrong {
    animation: none;
  }
}

.shk-03b,
.shk-03b *,
.shk-03b *::before,
.shk-03b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-03b {
  --err: oklch(0.68 0.21 25);
  --ok: oklch(0.78 0.16 160);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #07080c;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-03b__phone {
  display: grid;
  justify-items: center;
  gap: 26px;
  padding: 44px 38px;
  border-radius: 34px;
  background: linear-gradient(180deg,#0e1018,#0a0c12);
  border: 1px solid rgba(160,180,220,.14);
  box-shadow: 0 60px 120px -60px rgba(0,0,0,1);
}

.shk-03b__label {
  font-size: 13.5px;
  color: rgba(225,232,248,.65);
  letter-spacing: .02em;
  min-height: 20px;
}

.shk-03b__label.err {
  color: oklch(0.8 0.13 25);
}

.shk-03b__label.ok {
  color: var(--ok);
}

.shk-03b__dots {
  display: flex;
  gap: 18px;
}

.shk-03b__dots i {
  width: 13px;
  height: 13px;
  border-radius: 50%;
  border: 1.5px solid rgba(225,232,248,.45);
  transition: background .15s,border-color .15s,scale .15s;
}

.shk-03b__dots i.fill {
  background: #e1e8f8;
  border-color: #e1e8f8;
  scale: 1.1;
}

.shk-03b__dots.wrong {
  animation: shk-03b-rattle .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-03b__dots.wrong i {
  background: var(--err);
  border-color: var(--err);
}

.shk-03b__dots.right i {
  background: var(--ok);
  border-color: var(--ok);
}

.shk-03b__pad {
  display: grid;
  grid-template-columns: repeat(3,72px);
  gap: 14px;
}

.shk-03b__pad button {
  height: 72px;
  border-radius: 50%;
  border: 1px solid rgba(160,180,220,.16);
  background: rgba(255,255,255,.05);
  color: #e1e8f8;
  font: inherit;
  font-size: 24px;
  font-weight: 500;
  cursor: pointer;
  transition: background .12s,scale .12s;
}

.shk-03b__pad button:hover {
  background: rgba(255,255,255,.1);
}

.shk-03b__pad button:active {
  background: rgba(255,255,255,.22);
  scale: .94;
}

.shk-03b__pad [data-del] {
  font-size: 19px;
}

@keyframes shk-03b-rattle {
  15% {
    translate: -12px 0;
  }

  30% {
    translate: 10px 0;
  }

  45% {
    translate: -8px 0;
  }

  60% {
    translate: 6px 0;
  }

  75% {
    translate: -3px 0;
  }

  90% {
    translate: 1px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-03b__dots.wrong {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var form=document.getElementById('shk-03a-form'); if(!form) return;
  var row=form,input=document.getElementById('shk-03a-pass'),caps=document.getElementById('shk-03a-caps'),
      status=document.getElementById('shk-03a-status'),avatar=document.getElementById('shk-03a-avatar'),tries=0;
  function retrigger(el,cls){ el.classList.remove(cls); requestAnimationFrame(function(){ requestAnimationFrame(function(){ el.classList.add(cls); }); }); }
  row.addEventListener('animationend',function(){ row.classList.remove('is-wrong'); avatar.classList.remove('is-wrong'); });
  input.addEventListener('keyup',function(e){ if(e.getModifierState) caps.hidden=!e.getModifierState('CapsLock'); });
  form.addEventListener('submit',function(e){
    e.preventDefault();
    if(input.value==='demo123'){ status.className='shk-03a__status ok'; status.textContent='Welcome back, Kai.'; return; }
    tries++;
    retrigger(row,'is-wrong'); retrigger(avatar,'is-wrong');
    status.className='shk-03a__status err';
    status.textContent='Wrong password ('+tries+(tries===1?' try':' tries')+'). Hint: demo123';
    input.select();
  });
})();

(function(){
  var pad=document.getElementById('shk-03b-pad'); if(!pad) return;
  var dots=document.getElementById('shk-03b-dots'),label=document.getElementById('shk-03b-label'),
      pins=dots.querySelectorAll('i'),buf='',locked=false;
  function paint(){ pins.forEach(function(d,i){ d.classList.toggle('fill',i<buf.length); }); }
  dots.addEventListener('animationend',function(){
    dots.classList.remove('wrong'); buf=''; paint(); locked=false;   // clear AFTER the rattle
  });
  pad.addEventListener('click',function(e){
    var b=e.target.closest('button'); if(!b||locked) return;
    if(b.hasAttribute('data-del')){ buf=buf.slice(0,-1); paint(); return; }
    if(buf.length>=4) return;
    buf+=b.textContent.trim(); paint();
    if(buf.length<4) return;
    if(buf==='2468'){ dots.classList.add('right'); label.className='shk-03b__label ok'; label.textContent='Unlocked. Welcome back.'; locked=true; return; }
    locked=true; dots.classList.add('wrong');
    label.className='shk-03b__label err'; label.textContent='Wrong passcode — try 2468';
  });
})();
```
