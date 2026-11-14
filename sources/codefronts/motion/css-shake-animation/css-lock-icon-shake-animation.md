---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-lock-icon-shake-animation/"
title: "CSS Lock Icon Shake Animation"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "A padlock with opinions: poke the vault lock and it shakes the attempt off (shackle rattling harder than the body, like metal on metal), flip the access…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Lock Icon Shake Animation
Source: https://codefronts.com/motion/css-shake-animation/css-lock-icon-shake-animation/

A padlock with opinions: poke the vault lock and it shakes the attempt off (shackle rattling harder than the body, like metal on metal), flip the access toggle and the shackle swings open with a gold glow — plus a pure-CSS paywall card whose corner lock wiggles a polite 'members only' on hover.
## HTML
```html
<div class="shk-17-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-17a" aria-label="Vault lock that rattles when denied and opens when granted">
  <div class="shk-17a__panel">
    <button class="shk-17a__lockbtn" id="shk-17a-lock" type="button" aria-label="Vault — locked. Activate to attempt access.">
      <svg class="shk-17a__svg" viewBox="0 0 48 48" aria-hidden="true">
        <g class="shk-17a__shackle"><path d="M15 22v-7a9 9 0 0 1 18 0v7" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"></path></g>
        <g class="shk-17a__body"><rect x="10" y="21" width="28" height="21" rx="5" fill="currentColor"></rect><circle cx="24" cy="30.5" r="3" fill="var(--shk17a-bg)"></circle><rect x="22.7" y="31.5" width="2.6" height="6" rx="1.3" fill="var(--shk17a-bg)"></rect></g>
      </svg>
    </button>
    <p class="shk-17a__state" id="shk-17a-state" aria-live="polite">Locked — click the lock to try it</p>
    <label class="shk-17a__toggle"><input type="checkbox" id="shk-17a-grant"><span class="shk-17a__track" aria-hidden="true"><span class="shk-17a__thumb"></span></span>Grant access</label>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-17b" aria-label="Members-only article card with wiggling lock on hover">
  <article class="shk-17b__card" tabindex="0">
    <div class="shk-17b__locktip">
      <svg class="shk-17b__lock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2.5"></rect><path d="M8 11V7a4 4 0 0 1 8 0v4"></path></svg>
      <span class="shk-17b__tip" role="tooltip">Members only</span>
    </div>
    <p class="shk-17b__kicker">Essay · 14 min</p>
    <h2 class="shk-17b__title">The interface is the argument</h2>
    <p class="shk-17b__teaser">Every layout is a claim about what matters. When a screen shakes, nods, or resists, it is speaking in the oldest language we have — and most products are mumbling. The&nbsp;craft&hellip;</p>
    <p class="shk-17b__cta">Continue reading — join Meridian</p>
  </article>
  <p class="shk-17b__hint" aria-hidden="true">hover (or focus) the card — the lock objects, softly</p>
</section>
</div>
```
## CSS
```css
.shk-17-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-17-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-17a,
.shk-17a *,
.shk-17a *::before,
.shk-17a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-17a {
  --shk17a-bg: #12141c;
  --gold: oklch(0.8 0.13 85);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 100% at 50% 0%,#1a1d29,#12141c 65%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-17a__panel {
  display: grid;
  justify-items: center;
  gap: 20px;
}

.shk-17a__lockbtn {
  width: 132px;
  height: 132px;
  display: grid;
  place-items: center;
  border-radius: 28px;
  border: 1px solid rgba(200,210,235,.16);
  background: rgba(255,255,255,.05);
  color: #c8cee0;
  cursor: pointer;
  transition: color .3s,border-color .3s,box-shadow .3s;
}

.shk-17a__lockbtn:hover {
  border-color: rgba(200,210,235,.3);
}

.shk-17a__svg {
  width: 64px;
  height: 64px;
  overflow: visible;
}

.shk-17a__shackle {
  transform-origin: 15px 22px;
  transform-box: view-box;
  transition: rotate .38s cubic-bezier(.34,1.4,.64,1),translate .38s cubic-bezier(.34,1.4,.64,1);
}

.shk-17a__lockbtn.is-denied .shk-17a__body {
  animation: shk-17a-jolt .45s cubic-bezier(.36,.07,.19,.97);
}

.shk-17a__lockbtn.is-denied .shk-17a__shackle {
  animation: shk-17a-rattle .45s cubic-bezier(.36,.07,.19,.97);
}

.shk-17a__lockbtn.is-open {
  color: var(--gold);
  border-color: oklch(0.8 0.13 85 / .55);
  animation: shk-17a-glow .9s ease-out;
}

.shk-17a__lockbtn.is-open .shk-17a__shackle {
  rotate: -35deg;
  translate: -2px -3px;
}

.shk-17a__state {
  font-size: 13.5px;
  color: rgba(200,206,224,.6);
  min-height: 20px;
}

.shk-17a__state.ok {
  color: var(--gold);
  font-weight: 600;
}

.shk-17a__toggle {
  display: flex;
  align-items: center;
  gap: 11px;
  font-size: 14px;
  color: #c8cee0;
  cursor: pointer;
  user-select: none;
}

.shk-17a__toggle input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.shk-17a__track {
  width: 46px;
  height: 26px;
  border-radius: 999px;
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(200,210,235,.2);
  display: flex;
  align-items: center;
  padding: 2px;
  transition: background .25s;
}

.shk-17a__thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #c8cee0;
  transition: translate .25s,background .25s;
}

.shk-17a__toggle input:checked+.shk-17a__track {
  background: oklch(0.8 0.13 85 / .35);
}

.shk-17a__toggle input:checked+.shk-17a__track .shk-17a__thumb {
  translate: 20px 0;
  background: var(--gold);
}

.shk-17a__toggle input:focus-visible+.shk-17a__track {
  outline: 2px solid #c8cee0;
  outline-offset: 3px;
}

@keyframes shk-17a-jolt {
  25% {
    translate: -3px 0;
  }

  50% {
    translate: 2.5px 0;
  }

  75% {
    translate: -1.5px 0;
  }
}

@keyframes shk-17a-rattle {
  18% {
    translate: -1px -2px;
    rotate: -4.5deg;
  }

  42% {
    translate: 1px 0;
    rotate: 3.5deg;
  }

  66% {
    translate: -.5px -1px;
    rotate: -2deg;
  }

  85% {
    rotate: 1deg;
  }
}

@keyframes shk-17a-glow {
  0% {
    box-shadow: 0 0 0 0 oklch(0.8 0.13 85 / .55);
  }

  100% {
    box-shadow: 0 0 60px 8px oklch(0.8 0.13 85 / 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-17a__lockbtn.is-denied .shk-17a__body,
    .shk-17a__lockbtn.is-denied .shk-17a__shackle,
    .shk-17a__lockbtn.is-open {
    animation: none;
  }
}

.shk-17b,
.shk-17b *,
.shk-17b *::before,
.shk-17b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-17b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 18px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f8f5ef,#efe9dd);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-17b__card {
  position: relative;
  width: min(420px,88vw);
  padding: 34px 34px 28px;
  background: #fffdf8;
  border: 1.5px solid rgba(43,37,27,.14);
  border-radius: 6px;
  box-shadow: 0 30px 60px -38px rgba(43,37,27,.55);
  cursor: pointer;
  outline: none;
  transition: translate .2s,box-shadow .2s;
}

.shk-17b__card:hover,
.shk-17b__card:focus-visible {
  translate: 0 -3px;
  box-shadow: 0 40px 70px -40px rgba(43,37,27,.6);
}

.shk-17b__card:focus-visible {
  outline: 2px solid #2b251b;
  outline-offset: 4px;
}

.shk-17b__locktip {
  position: absolute;
  top: 18px;
  right: 18px;
  display: grid;
  justify-items: center;
}

.shk-17b__lock {
  width: 22px;
  height: 22px;
  color: oklch(0.55 0.12 60);
}

.shk-17b__card:hover .shk-17b__lock,
.shk-17b__card:focus-visible .shk-17b__lock {
  animation: shk-17b-object .55s ease-in-out;
}

.shk-17b__tip {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  white-space: nowrap;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #fffdf8;
  background: #2b251b;
  padding: 5px 10px;
  border-radius: 6px;
  opacity: 0;
  translate: 0 -4px;
  transition: opacity .2s,translate .2s;
  pointer-events: none;
}

.shk-17b__card:hover .shk-17b__tip,
.shk-17b__card:focus-visible .shk-17b__tip {
  opacity: 1;
  translate: 0 0;
}

.shk-17b__kicker {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: oklch(0.55 0.12 60);
}

.shk-17b__title {
  margin-top: 12px;
  font-family: 'Instrument Serif',Georgia,serif;
  font-weight: 400;
  font-size: 31px;
  line-height: 1.12;
  color: #2b251b;
  max-width: 300px;
}

.shk-17b__teaser {
  margin-top: 14px;
  font-size: 14px;
  line-height: 1.65;
  color: rgba(43,37,27,.65);
}

.shk-17b__cta {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1.5px dashed rgba(43,37,27,.2);
  font-size: 13px;
  font-weight: 800;
  color: #2b251b;
}

.shk-17b__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(43,37,27,.45);
}

@keyframes shk-17b-object {
  15% {
    rotate: -9deg;
  }

  35% {
    rotate: 8deg;
  }

  55% {
    rotate: -5deg;
  }

  75% {
    rotate: 3deg;
  }

  90% {
    rotate: -1deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-17b__card:hover .shk-17b__lock,
    .shk-17b__card:focus-visible .shk-17b__lock {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var lock=document.getElementById('shk-17a-lock'); if(!lock) return;
  var grant=document.getElementById('shk-17a-grant'),state=document.getElementById('shk-17a-state');
  lock.addEventListener('animationend',function(){ lock.classList.remove('is-denied'); },true);
  lock.addEventListener('click',function(){
    if(grant.checked) return;
    lock.classList.remove('is-denied');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ lock.classList.add('is-denied'); }); });
    state.className='shk-17a__state'; state.textContent='Access denied — flip “Grant access” below.';
  });
  grant.addEventListener('change',function(){
    lock.classList.remove('is-denied');           // never rattle and open at once
    lock.classList.toggle('is-open',grant.checked);
    lock.setAttribute('aria-label',grant.checked?'Vault — unlocked':'Vault — locked. Activate to attempt access.');
    state.className='shk-17a__state'+(grant.checked?' ok':'');
    state.textContent=grant.checked?'Unlocked — shackle swings on a transition, not an animation.':'Locked — click the lock to try it';
  });
})();

/* No JavaScript — the lock's rotate-decay plays on card :hover/:focus-visible while a tooltip names the reason. Motion attracts, words explain: never ship the wiggle without the label. */
```
