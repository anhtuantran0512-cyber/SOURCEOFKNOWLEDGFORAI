---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/frosted-glass-credit-card-payment-ui/"
title: "Frosted Glass Credit Card Payment UI"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A hyper-realistic glass credit card with holographic shimmer, EMV chip, contactless icon, card number, and 3D CSS flip to reveal the signature strip back —…"
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Credit Card Payment UI
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/frosted-glass-credit-card-payment-ui/

A hyper-realistic glass credit card with holographic shimmer, EMV chip, contactless icon, card number, and 3D CSS flip to reveal the signature strip back — plus a spend progress bar and freeze toggle below.
## HTML
```html
<div class="fg-09">
  <div class="fg-04__bg" aria-hidden="true">
    <div class="fg-04__glow fg-04__glow--1"></div>
    <div class="fg-04__glow fg-04__glow--2"></div>
  </div>
  <div class="fg-04__wrap">
    <div class="fg-04__scene" id="fg-09-scene" role="button" aria-label="Flip card" tabindex="0">
      <div class="fg-04__card">
        <div class="fg-04__face fg-04__face--front">
          <div class="fg-04__face-top">
            <svg class="fg-04__chip" width="38" height="30" viewBox="0 0 38 30" aria-label="EMV chip">
              <defs><linearGradient id="fg-09-cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#d4a843"/><stop offset="50%" stop-color="#f5c842"/><stop offset="100%" stop-color="#b8860b"/></linearGradient></defs>
              <rect width="38" height="30" rx="4" fill="url(#fg-09-cg)"/>
              <line x1="12" y1="0" x2="12" y2="30" stroke="rgba(0,0,0,.18)" stroke-width=".8"/><line x1="26" y1="0" x2="26" y2="30" stroke="rgba(0,0,0,.18)" stroke-width=".8"/>
              <line x1="0" y1="10" x2="38" y2="10" stroke="rgba(0,0,0,.18)" stroke-width=".8"/><line x1="0" y1="20" x2="38" y2="20" stroke="rgba(0,0,0,.18)" stroke-width=".8"/>
              <rect x="12" y="10" width="14" height="10" rx="1" fill="rgba(0,0,0,.1)"/>
            </svg>
            <svg class="fg-04__nfc" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="1.5" aria-label="Contactless"><path d="M4.5 4.5a14 14 0 0 1 0 15M9 7a9 9 0 0 1 0 10M13.5 9.5a5 5 0 0 1 0 5M18 12h.01"/></svg>
          </div>
          <p class="fg-04__number">&#x2022;&#x2022;&#x2022;&#x2022;&nbsp;&nbsp;&#x2022;&#x2022;&#x2022;&#x2022;&nbsp;&nbsp;&#x2022;&#x2022;&#x2022;&#x2022;&nbsp;&nbsp;4821</p>
          <div class="fg-04__face-bot">
            <div><span class="fg-04__meta-lbl">VALID THRU</span><span class="fg-04__meta-val">09 / 27</span></div>
            <span class="fg-04__holder">ALEX CHEN</span>
            <svg class="fg-04__net" viewBox="0 0 50 32" width="50" height="32" aria-label="Payment network">
              <circle cx="19" cy="16" r="13" fill="rgba(235,0,27,.85)"/>
              <circle cx="31" cy="16" r="13" fill="rgba(255,163,25,.85)" style="mix-blend-mode:multiply"/>
            </svg>
          </div>
        </div>
        <div class="fg-04__face fg-04__face--back">
          <div class="fg-04__stripe" aria-hidden="true"></div>
          <div class="fg-04__sig-row">
            <div class="fg-04__sig-box" aria-label="Signature area"></div>
            <div class="fg-04__cvv-box"><span class="fg-04__cvv-lbl">CVV</span><span class="fg-04__cvv-val">***</span></div>
          </div>
          <p class="fg-04__back-note">This card is property of Nexus Bank N.A. If found, return to any branch.</p>
        </div>
      </div>
    </div>
    <div class="fg-04__controls">
      <div class="fg-04__spend-panel">
        <div class="fg-04__spend-hd">
          <span class="fg-04__spend-lbl">Monthly Spend</span>
          <span class="fg-04__spend-amt">$2,340 <small>/ $5,000</small></span>
        </div>
        <div class="fg-04__spend-track"><div class="fg-04__spend-fill"></div></div>
      </div>
      <div class="fg-04__action-row">
        <label class="fg-04__freeze" aria-label="Freeze card">
          <input type="checkbox" id="fg-09-freeze">
          <span class="fg-04__sw-track"><span class="fg-04__sw-thumb"></span></span>
          <span>Freeze Card</span>
        </label>
        <div class="fg-04__quick">
          <button class="fg-04__qbtn">+ Add Money</button>
          <button class="fg-04__qbtn">&#8594; Send</button>
          <button class="fg-04__qbtn">&#128196; History</button>
        </div>
      </div>
    </div>
    <p class="fg-04__hint">Tap card to flip &bull; Tap freeze to lock</p>
  </div>
</div>
```
## CSS
```css
.fg-09,
.fg-09 *,
.fg-09 *::before,
.fg-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-09 ::selection {
  background: rgba(212,168,67,.4);
  color: #fff;
}

.fg-09 {
  --c-bg: #06071a;
  --c-gold: #d4a843;
  --c-gold2: #f5c842;
  --c-glass: rgba(255,255,255,.06);
  --c-border: rgba(255,255,255,.12);
  --c-text: #e8e8ff;
  --c-muted: rgba(232,232,255,.5);
  --t: .3s ease;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--c-bg);
  position: relative;
  overflow: hidden;
  padding: 40px 20px;
}

.fg-04__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-04__glow {
  position: absolute;
  border-radius: 50%;
}

.fg-04__glow--1 {
  width: 460px;
  height: 460px;
  background: radial-gradient(circle,rgba(212,168,67,.22),transparent 70%);
  top: -140px;
  left: -100px;
  animation: fg-09-g1 22s ease-in-out infinite alternate;
}

.fg-04__glow--2 {
  width: 360px;
  height: 360px;
  background: radial-gradient(circle,rgba(99,102,241,.18),transparent 70%);
  bottom: -100px;
  right: -80px;
  animation: fg-09-g2 18s ease-in-out infinite alternate;
}

@keyframes fg-09-g1 {
  to {
    transform: translate(80px,100px) scale(1.2);
  }
}

@keyframes fg-09-g2 {
  to {
    transform: translate(-60px,-80px) scale(1.15);
  }
}

.fg-04__wrap {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 26px;
  width: 100%;
  max-width: 420px;
}

.fg-04__scene {
  width: 380px;
  height: 230px;
  perspective: 900px;
  cursor: pointer;
}

.fg-04__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fg-04__card.is-flipped {
  transform: rotateY(180deg);
}

.fg-04__face {
  position: absolute;
  inset: 0;
  border-radius: 18px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}

.fg-04__face--front {
  background: linear-gradient(135deg,rgba(12,12,38,.92) 0%,rgba(28,18,58,.88) 45%,rgba(18,28,58,.92) 100%);
  backdrop-filter: blur(20px) saturate(150%);
  -webkit-backdrop-filter: blur(20px) saturate(150%);
  border: 1px solid rgba(212,168,67,.22);
  box-shadow: 0 20px 60px rgba(0,0,0,.65),0 0 0 1px rgba(255,255,255,.05) inset,0 1px 0 rgba(212,168,67,.18) inset;
  padding: 22px 24px 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.fg-04__face--front::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(105deg,transparent 22%,rgba(147,197,253,.05) 32%,rgba(196,181,253,.08) 42%,rgba(252,165,165,.05) 52%,transparent 62%);
  animation: fg-09-holo 3.5s linear infinite;
  pointer-events: none;
  mix-blend-mode: screen;
}

@keyframes fg-09-holo {
  0% {
    transform: translateX(-100%) skewX(-8deg);
  }

  100% {
    transform: translateX(260%) skewX(-8deg);
  }
}

.fg-04__face-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.fg-04__chip {
  filter: drop-shadow(0 2px 6px rgba(212,168,67,.5));
}

.fg-04__number {
  font-family: 'Courier New',Courier,monospace;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: .16em;
  color: rgba(255,255,255,.92);
  text-shadow: 0 0 18px rgba(255,255,255,.18);
}

.fg-04__face-bot {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
}

.fg-04__meta-lbl {
  display: block;
  font-size: 7.5px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(255,255,255,.45);
  margin-bottom: 2px;
}

.fg-04__meta-val {
  display: block;
  font-size: 13px;
  font-weight: 700;
  color: rgba(255,255,255,.9);
  letter-spacing: .1em;
}

.fg-04__holder {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .12em;
  color: rgba(255,255,255,.85);
}

.fg-04__net {
  filter: drop-shadow(0 0 8px rgba(235,0,27,.3));
}

.fg-04__face--back {
  background: linear-gradient(155deg,rgba(12,12,38,.96),rgba(18,22,52,.92));
  border: 1px solid rgba(212,168,67,.18);
  box-shadow: 0 20px 60px rgba(0,0,0,.65);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.fg-04__stripe {
  height: 46px;
  background: linear-gradient(to bottom,#111,#050505);
  margin-top: 28px;
}

.fg-04__sig-row {
  display: flex;
  gap: 10px;
  padding: 12px 24px;
}

.fg-04__sig-box {
  flex: 1;
  background: repeating-linear-gradient(0deg,rgba(255,255,255,.06) 0,rgba(255,255,255,.06) 1px,transparent 1px,transparent 6px);
  border-radius: 4px;
  height: 32px;
}

.fg-04__cvv-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,.92);
  border-radius: 4px;
  padding: 4px 14px;
  gap: 1px;
  min-width: 54px;
}

.fg-04__cvv-lbl {
  font-size: 7px;
  color: #333;
  font-weight: 800;
  letter-spacing: .12em;
}

.fg-04__cvv-val {
  font-size: 14px;
  font-weight: 800;
  color: #111;
  letter-spacing: .2em;
}

.fg-04__back-note {
  padding: 0 24px;
  font-size: 9.5px;
  color: rgba(255,255,255,.3);
  line-height: 1.5;
  margin-top: auto;
  padding-bottom: 16px;
}

.fg-04__controls {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.fg-04__spend-panel {
  background: var(--c-glass);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--c-border);
  border-radius: 14px;
  padding: 16px 18px;
}

.fg-04__spend-hd {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  font-size: 13px;
}

.fg-04__spend-lbl {
  color: var(--c-muted);
}

.fg-04__spend-amt {
  color: var(--c-text);
  font-weight: 700;
}

.fg-04__spend-amt small {
  font-weight: 400;
  color: var(--c-muted);
}

.fg-04__spend-track {
  height: 6px;
  border-radius: 3px;
  background: rgba(255,255,255,.08);
}

.fg-04__spend-fill {
  height: 100%;
  width: 46.8%;
  border-radius: 3px;
  background: linear-gradient(90deg,var(--c-gold),var(--c-gold2));
  box-shadow: 0 0 10px rgba(212,168,67,.5);
  animation: fg-09-bar .9s ease-out both;
}

@keyframes fg-09-bar {
  from {
    width: 0;
  }
}

.fg-04__action-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
}

.fg-04__freeze {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  font-size: 13px;
  color: var(--c-text);
  user-select: none;
}

.fg-04__freeze input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.fg-04__sw-track {
  display: flex;
  align-items: center;
  width: 42px;
  height: 24px;
  border-radius: 12px;
  background: rgba(255,255,255,.1);
  border: 1px solid var(--c-border);
  padding: 2px;
  transition: background .3s,border-color .3s;
}

.fg-04__freeze input:checked~.fg-04__sw-track {
  background: rgba(99,102,241,.5);
  border-color: rgba(99,102,241,.6);
}

.fg-04__sw-thumb {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0,0,0,.3);
  transition: transform .3s;
}

.fg-04__freeze input:checked~.fg-04__sw-track .fg-04__sw-thumb {
  transform: translateX(18px);
}

.fg-04__quick {
  display: flex;
  gap: 6px;
}

.fg-04__qbtn {
  padding: 7px 12px;
  border: 1px solid var(--c-border);
  border-radius: 20px;
  background: rgba(255,255,255,.06);
  color: var(--c-text);
  font-size: 11.5px;
  font-weight: 500;
  cursor: pointer;
  transition: background var(--t),transform .15s;
  white-space: nowrap;
}

.fg-04__qbtn:hover {
  background: rgba(255,255,255,.12);
  transform: translateY(-1px);
}

.fg-04__hint {
  font-size: 11px;
  color: var(--c-muted);
  letter-spacing: .3px;
  opacity: .55;
}

@media (prefers-reduced-motion: reduce) {
  .fg-04__glow,
    .fg-04__face--front::before,
    .fg-04__spend-fill {
    animation: none;
  }

  .fg-04__card,
    .fg-04__sw-track,
    .fg-04__sw-thumb,
    .fg-04__qbtn {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-09');
  if(!r)return;
  var scene=r.querySelector('#fg-09-scene');
  var card=r.querySelector('.fg-04__card');
  if(scene&&card){
    function flip(){card.classList.toggle('is-flipped')}
    scene.addEventListener('click',flip);
    scene.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();flip()}});
  }
})();
```
