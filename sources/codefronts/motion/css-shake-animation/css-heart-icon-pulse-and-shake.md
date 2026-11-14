---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-heart-icon-pulse-and-shake/"
title: "CSS Heart Icon Pulse and Shake"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "A heart with a pulse: the like button idles on a double-beat (lub-dub, like a real heartbeat), shakes eagerly when hovered, and on click bursts — scale pop,…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Heart Icon Pulse and Shake
Source: https://codefronts.com/motion/css-shake-animation/css-heart-icon-pulse-and-shake/

A heart with a pulse: the like button idles on a double-beat (lub-dub, like a real heartbeat), shakes eagerly when hovered, and on click bursts — scale pop, particle ring, count bump — then rests filled. Plus a pure-CSS 'save' pill where pulse and shake chain on hover alone.
## HTML
```html
<div class="shk-20-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-20a" aria-label="Like button with heartbeat, hover shake and click burst">
  <div class="shk-20a__card">
    <img class="shk-20a__img" src="https://picsum.photos/id/237/520/340" alt="A black puppy looking up" loading="lazy">
    <div class="shk-20a__row">
      <div class="shk-20a__meta"><p class="shk-20a__title">Intern's first standup</p><p class="shk-20a__sub">@goodboy · 2h</p></div>
      <button class="shk-20a__like" id="shk-20a-like" type="button" aria-pressed="false" aria-label="Like, 2148 likes">
        <span class="shk-20a__heartwrap" id="shk-20a-wrap">
          <svg class="shk-20a__heart" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-6.7-4.2-9.3-8.1C.8 10 1.6 6.4 4.5 5.1 6.6 4.2 9 4.9 10.4 6.7L12 8.6l1.6-1.9C15 4.9 17.4 4.2 19.5 5.1c2.9 1.3 3.7 4.9 1.8 7.8C18.7 16.8 12 21 12 21z"></path></svg>
          <span class="shk-20a__parts" id="shk-20a-parts" aria-hidden="true"></span>
        </span>
        <span class="shk-20a__count" id="shk-20a-count">2,148</span>
      </button>
    </div>
  </div>
  <p class="shk-20a__hint" aria-hidden="true">idle: lub-dub · hover: eager shake · click: burst + count bump at the peak</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400..800&display=swap" rel="stylesheet">
<section class="shk-20b" aria-label="Save pill whose heart pulses then shakes on hover">
  <div class="shk-20b__stage">
    <button class="shk-20b__pill" type="button">
      <svg class="shk-20b__h" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-6.7-4.2-9.3-8.1C.8 10 1.6 6.4 4.5 5.1 6.6 4.2 9 4.9 10.4 6.7L12 8.6l1.6-1.9C15 4.9 17.4 4.2 19.5 5.1c2.9 1.3 3.7 4.9 1.8 7.8C18.7 16.8 12 21 12 21z" fill="none" stroke="currentColor" stroke-width="2"></path></svg>
      Save to favourites
    </button>
    <p class="shk-20b__hint" aria-hidden="true">hover and hold — two beats, then it can't contain itself (one animation, chained phases)</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-20-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-20-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-20a,
.shk-20a *,
.shk-20a *::before,
.shk-20a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-20a {
  --pink: oklch(0.66 0.22 15);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 18px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#faf8f6,#f0ebe6);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-20a__card {
  width: min(400px,90vw);
  border-radius: 20px;
  background: #fff;
  border: 1px solid rgba(30,26,24,.1);
  box-shadow: 0 30px 60px -35px rgba(30,26,24,.5);
  overflow: hidden;
}

.shk-20a__img {
  display: block;
  width: 100%;
  height: 220px;
  object-fit: cover;
}

.shk-20a__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 16px 18px;
}

.shk-20a__title {
  font-size: 15.5px;
  font-weight: 800;
  color: #1e1a18;
}

.shk-20a__sub {
  margin-top: 2px;
  font-size: 12.5px;
  color: rgba(30,26,24,.5);
}

.shk-20a__like {
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 10px 16px;
  border: 1.5px solid rgba(30,26,24,.14);
  border-radius: 999px;
  background: #fff;
  cursor: pointer;
  transition: border-color .2s,background .2s;
  font: inherit;
}

.shk-20a__like:hover {
  border-color: var(--pink);
}

.shk-20a__heartwrap {
  position: relative;
  display: grid;
  place-items: center;
}

.shk-20a__heart {
  width: 22px;
  height: 22px;
  fill: none;
  stroke: #1e1a18;
  stroke-width: 1.8;
  transition: fill .25s,stroke .25s;
  animation: shk-20a-lubdub 1.6s ease-in-out infinite;
}

.shk-20a__like:hover .shk-20a__heartwrap {
  animation: shk-20a-eager .5s ease-in-out infinite;
}

.shk-20a__like.is-liked .shk-20a__heart {
  fill: var(--pink);
  stroke: var(--pink);
  animation: shk-20a-burst .55s cubic-bezier(.34,1.56,.64,1);
}

.shk-20a__like.is-liked:hover .shk-20a__heartwrap {
  animation: none;
}

.shk-20a__count {
  font-size: 14px;
  font-weight: 800;
  color: #1e1a18;
  font-variant-numeric: tabular-nums;
}

.shk-20a__parts {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.shk-20a__parts i {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 5px;
  height: 5px;
  margin: -2.5px;
  border-radius: 50%;
  background: var(--pink);
  opacity: 0;
  animation: shk-20a-part .55s ease-out forwards;
}

.shk-20a__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(30,26,24,.45);
}

@keyframes shk-20a-lubdub {
  0%,
    60%,
    100% {
    scale: 1;
  }

  8% {
    scale: 1.14;
  }

  16% {
    scale: 1;
  }

  24% {
    scale: 1.1;
  }
}

@keyframes shk-20a-eager {
  0%,
    100% {
    rotate: 0deg;
  }

  25% {
    rotate: 7deg;
  }

  75% {
    rotate: -7deg;
  }
}

@keyframes shk-20a-burst {
  0% {
    scale: .3;
  }

  55% {
    scale: 1.28;
  }

  100% {
    scale: 1;
  }
}

@keyframes shk-20a-part {
  0% {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }

  80% {
    opacity: 0;
  }

  100% {
    opacity: 0;
    translate: calc(cos(var(--a)) * 20px) calc(sin(var(--a)) * -20px);
    scale: .4;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-20a__heart,
    .shk-20a__like:hover .shk-20a__heartwrap,
    .shk-20a__like.is-liked .shk-20a__heart {
    animation: none;
  }

  .shk-20a__parts i {
    display: none;
  }
}

.shk-20b,
.shk-20b *,
.shk-20b *::before,
.shk-20b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-20b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 110% at 50% 100%,#2a1420,#140a10 60%);
  font-family: 'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;
}

.shk-20b__stage {
  text-align: center;
}

.shk-20b__pill {
  display: inline-flex;
  align-items: center;
  gap: 11px;
  padding: 16px 30px;
  font: inherit;
  font-size: 16px;
  font-weight: 700;
  color: #ffe8f0;
  background: rgba(255,255,255,.06);
  border: 1.5px solid oklch(0.7 0.19 5 / .45);
  border-radius: 999px;
  cursor: pointer;
  transition: background .2s,border-color .2s;
}

.shk-20b__pill:hover {
  background: oklch(0.7 0.19 5 / .12);
  border-color: oklch(0.7 0.19 5 / .8);
}

.shk-20b__h {
  width: 21px;
  height: 21px;
  color: oklch(0.75 0.18 10);
}

.shk-20b__pill:hover .shk-20b__h {
  animation: shk-20b-chain 1.5s ease-in-out infinite;
}

.shk-20b__pill:active {
  scale: .97;
}

.shk-20b__pill:focus-visible {
  outline: 2px solid oklch(0.75 0.18 10);
  outline-offset: 4px;
}

.shk-20b__hint {
  margin-top: 22px;
  font-size: 12px;
  color: rgba(255,232,240,.4);
  max-width: 400px;
}

@keyframes shk-20b-chain {
  0% {
    scale: 1;
    rotate: 0deg;
  }

  7% {
    scale: 1.18;
  }

  14% {
    scale: 1;
  }

  21% {
    scale: 1.12;
  }

  28% {
    scale: 1;
    rotate: 0deg;
  }

  38% {
    rotate: 9deg;
  }

  48% {
    rotate: -8deg;
  }

  58% {
    rotate: 6deg;
  }

  68% {
    rotate: -4deg;
  }

  76% {
    rotate: 2deg;
  }

  84%,
    100% {
    rotate: 0deg;
    scale: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-20b__pill:hover .shk-20b__h {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('shk-20a-like'); if(!btn) return;
  var parts=document.getElementById('shk-20a-parts'),count=document.getElementById('shk-20a-count'),
      base=2148,liked=false;
  btn.addEventListener('click',function(){
    liked=!liked;
    btn.classList.toggle('is-liked',liked);
    btn.setAttribute('aria-pressed',String(liked));
    parts.innerHTML='';
    if(liked){
      for(var i=0;i<6;i++){ var p=document.createElement('i'); p.style.setProperty('--a',(i*60)+'deg'); parts.appendChild(p); }
      setTimeout(function(){ if(liked) count.textContent='2,149'; },280);   // bump at burst peak
    } else count.textContent='2,148';
    btn.setAttribute('aria-label','Like, '+(liked?'2149':'2148')+' likes');
  });
})();

/* No JavaScript — pulse and shake are PHASES of one keyframe timeline (beats own 0–28%, shake owns 38–84%), so the chain loops seamlessly with no JS sequencing. */
```
