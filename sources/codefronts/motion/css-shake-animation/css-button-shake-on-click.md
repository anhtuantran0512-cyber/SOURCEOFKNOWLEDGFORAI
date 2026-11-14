---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-button-shake-on-click/"
title: "CSS Button Shake on Click"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Click-shake both ways: a pure-CSS :active vibration you feel for exactly as long as the button is held (zero JS, zero cleanup), and the production JavaScript…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Button Shake on Click
Source: https://codefronts.com/motion/css-shake-animation/css-button-shake-on-click/

Click-shake both ways: a pure-CSS :active vibration you feel for exactly as long as the button is held (zero JS, zero cleanup), and the production JavaScript pattern — every click replays a decaying shake via the animationend cleanup, with a live counter proving that attempt #14 shakes exactly like attempt #1.
## HTML
```html
<div class="shk-10-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&display=swap" rel="stylesheet">
<section class="shk-10a" aria-label="Button that vibrates while pressed">
  <div class="shk-10a__stage">
    <p class="shk-10a__eyebrow">:active · zero JavaScript</p>
    <h2 class="shk-10a__title">Press &amp; hold</h2>
    <button class="shk-10a__btn" type="button"><span class="shk-10a__in">HOLD ME</span></button>
    <p class="shk-10a__hint" aria-hidden="true">the buzz lives exactly as long as your press — release = cleanup</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&family=JetBrains+Mono:wght@600&display=swap" rel="stylesheet">
<section class="shk-10b" aria-label="Button whose shake replays on every click">
  <div class="shk-10b__card">
    <h2 class="shk-10b__title">Seat 14C</h2>
    <p class="shk-10b__sub">Already taken — every click gets rejected, and every rejection shakes.</p>
    <button class="shk-10b__btn" id="shk-10b-btn" type="button" aria-describedby="shk-10b-count"><span class="shk-10b__in" id="shk-10b-in">Book this seat</span></button>
    <p class="shk-10b__count" id="shk-10b-count" aria-live="polite">0 attempts — attempt #1 will shake exactly like #100</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-10-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-10-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-10a,
.shk-10a *,
.shk-10a *::before,
.shk-10a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-10a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 100% at 50% 0%,#181d16,#0c0f0b);
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-10a__stage {
  text-align: center;
}

.shk-10a__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: oklch(0.82 0.17 130);
}

.shk-10a__title {
  margin-top: 10px;
  font-size: clamp(30px,4.6vw,44px);
  font-weight: 900;
  letter-spacing: -.02em;
  color: #eef4e8;
}

.shk-10a__btn {
  margin-top: 28px;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.shk-10a__in {
  display: inline-block;
  padding: 20px 46px;
  border-radius: 16px;
  font: inherit;
  font-size: 18px;
  font-weight: 900;
  letter-spacing: .1em;
  color: #0c0f0b;
  background: linear-gradient(180deg,oklch(0.87 0.19 130),oklch(0.74 0.18 132));
  box-shadow: 0 8px 0 oklch(0.5 0.12 132),0 22px 40px -16px oklch(0.74 0.18 132 / .5);
  transition: translate .1s,box-shadow .1s;
}

.shk-10a__btn:active .shk-10a__in {
  translate: 0 6px;
  box-shadow: 0 2px 0 oklch(0.5 0.12 132),0 10px 20px -12px oklch(0.74 0.18 132 / .5);
  animation: shk-10a-buzz .09s steps(2,jump-none) infinite;
}

.shk-10a__btn:focus-visible {
  outline: none;
}

.shk-10a__btn:focus-visible .shk-10a__in {
  outline: 3px solid oklch(0.87 0.19 130);
  outline-offset: 4px;
}

.shk-10a__hint {
  margin-top: 24px;
  font-size: 12px;
  color: rgba(238,244,232,.4);
}

@keyframes shk-10a-buzz {
  0% {
    translate: -1.5px 6px;
  }

  100% {
    translate: 1.5px 6px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-10a__btn:active .shk-10a__in {
    animation: none;
  }
}

.shk-10b,
.shk-10b *,
.shk-10b *::before,
.shk-10b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-10b {
  --err: oklch(0.64 0.21 25);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f5f6f8,#e9ebf0);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-10b__card {
  width: min(420px,100%);
  padding: 36px;
  border-radius: 20px;
  background: #fff;
  border: 1px solid rgba(28,32,42,.1);
  box-shadow: 0 30px 70px -40px rgba(28,32,42,.45);
  text-align: center;
}

.shk-10b__title {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: #1c202a;
}

.shk-10b__sub {
  margin-top: 8px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(28,32,42,.55);
}

.shk-10b__btn {
  margin-top: 24px;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
  width: 100%;
}

.shk-10b__in {
  display: block;
  padding: 16px;
  border-radius: 13px;
  font: inherit;
  font-size: 15.5px;
  font-weight: 800;
  color: #fff;
  background: #1c202a;
  transition: background .2s;
}

.shk-10b__in.is-shaking {
  background: var(--err);
  animation: shk-10b-shake .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-10b__btn:active .shk-10b__in {
  scale: .98;
}

.shk-10b__btn:focus-visible {
  outline: none;
}

.shk-10b__btn:focus-visible .shk-10b__in {
  outline: 3px solid #1c202a;
  outline-offset: 3px;
}

.shk-10b__count {
  margin-top: 14px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 11.5px;
  color: rgba(28,32,42,.5);
}

@keyframes shk-10b-shake {
  12% {
    translate: -9px 0;
  }

  28% {
    translate: 8px 0;
  }

  46% {
    translate: -6px 0;
  }

  64% {
    translate: 4px 0;
  }

  82% {
    translate: -2px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-10b__in.is-shaking {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :active starts an infinite 90ms steps(2) buzz and releasing the press removes the pseudo-class, which IS the cleanup. Note the buzz keyframes keep the 6px pressed translate so the two states compose. */

(function(){
  var btn=document.getElementById('shk-10b-btn'),inner=document.getElementById('shk-10b-in'),
      count=document.getElementById('shk-10b-count'); if(!btn) return;
  var n=0;
  inner.addEventListener('animationend',function(){ inner.classList.remove('is-shaking'); });
  btn.addEventListener('click',function(){
    n++;
    count.textContent=n+(n===1?' attempt':' attempts')+' — seat 14C is still taken';
    inner.classList.remove('is-shaking');
    // Double rAF: the removal must PAINT before we re-add, or rapid clicks coalesce and skip the restart.
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ inner.classList.add('is-shaking'); }); });
  });
})();
```
