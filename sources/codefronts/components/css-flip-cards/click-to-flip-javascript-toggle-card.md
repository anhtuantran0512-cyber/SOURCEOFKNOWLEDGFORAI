---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/click-to-flip-javascript-toggle-card/"
title: "Click-to-Flip JavaScript Toggle Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A card that flips strictly on a click event using a JS-toggled helper class rather than a hover pseudo-class — ideal for touch and keyboard interfaces."
has_js: "true"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Click-to-Flip JavaScript Toggle Card
Source: https://codefronts.com/components/css-flip-cards/click-to-flip-javascript-toggle-card/

A card that flips strictly on a click event using a JS-toggled helper class rather than a hover pseudo-class — ideal for touch and keyboard interfaces.
## HTML
```html
<div class="fc-16">
  <div class="fc-16__meta">
    <h2>Click-to-Flip · JavaScript Toggle</h2>
    <p>Uses a CSS class toggle — no hover required</p>
    <div class="fc-16__click-pill"><span class="fc-16__click-dot"></span>Click anywhere on the card</div>
  </div>
  <div class="fc-16__scene" id="fc-16-scene">
    <div class="fc-16__card" id="fc-16-card">
      <div class="fc-16__front">
        <div class="fc-16__click-icon">
          <svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </div>
        <div class="fc-16__label">Click Trigger · JS Toggle</div>
        <div class="fc-16__title">Click to Flip</div>
        <div class="fc-16__sub">This card flips on click, not hover — great for mobile touch interfaces where hover states don't exist.</div>
        <button class="fc-16__click-cta" id="fc-16-flip-btn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="m9 18 6-6-6-6"/></svg>
          Click to Reveal
        </button>
      </div>
      <div class="fc-16__back">
        <div class="fc-16__back-icon">
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="1.8"><polyline points="20 6 9 17 4 12"/></svg>
        </div>
        <div class="fc-16__back-title">Flip Complete ✓</div>
        <div class="fc-16__back-sub">The JS toggles <code style="color:#4ade80;background:rgba(0,0,0,.3);padding:1px 5px;border-radius:4px">.is-flipped</code> on the card element — no hover pseudo-class needed.</div>
        <div class="fc-16__code-block">
          <span class="fc-16__cmt">// toggle flip on click</span><br>
          card.<span class="fc-16__kw">classList</span>.<br>
          &nbsp;&nbsp;<span class="fc-16__str">toggle</span>(<span class="fc-16__str">'is-flipped'</span>);
        </div>
        <button class="fc-16__flip-back-btn" id="fc-16-back-btn">← Flip Back</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-16,
.fc-16 *,
.fc-16 *::before,
.fc-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-16 ::selection {
  background: #f97316;
  color: #fff;
}

.fc-16 {
  --bg: #0c0800;
  --orange: #f97316;
  --yellow: #fbbf24;
  --white: #fffbf0;
  --card-w: 340px;
  --card-h: 420px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 40%,#1a0e00,#0c0800 65%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 20px;
  color: var(--white);
}

.fc-16__meta {
  text-align: center;
}

.fc-16__meta h2 {
  font-size: 16px;
  font-weight: 700;
  color: var(--white);
}

.fc-16__meta p {
  font-size: 11px;
  color: rgba(255,251,240,.4);
  margin-top: 4px;
}

.fc-16__click-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 8px;
  padding: 6px 14px;
  border-radius: 20px;
  background: rgba(249,115,22,.12);
  border: 1px solid rgba(249,115,22,.25);
  font-size: 11px;
  color: var(--orange);
  cursor: default;
}

.fc-16__click-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--orange);
  animation: fc-16-pulse 1.5s ease-in-out infinite;
}

@keyframes fc-16-pulse {
  0%,
    100% {
    opacity: .4;
    transform: scale(.8);
  }

  50% {
    opacity: 1;
    transform: scale(1);
  }
}
/* Card */

.fc-16__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
  flex-shrink: 0;
}

.fc-16__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}
/* JS toggle via class */

.fc-16__card.is-flipped {
  transform: rotateY(180deg);
}

.fc-16__front,
.fc-16__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-16__front {
  background: linear-gradient(145deg,#1a0e00,#0f0900);
  border: 1px solid rgba(249,115,22,.25);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 36px 28px;
}

.fc-16__front::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 40%,rgba(249,115,22,.08),transparent 60%);
}

.fc-16__click-icon {
  width: 80px;
  height: 80px;
  border-radius: 24px;
  background: linear-gradient(135deg,rgba(249,115,22,.15),rgba(251,191,36,.08));
  border: 1px solid rgba(249,115,22,.25);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
  box-shadow: 0 0 30px rgba(249,115,22,.12);
}

.fc-16__click-icon svg {
  width: 36px;
  height: 36px;
  stroke: var(--orange);
  stroke-width: 1.8;
  fill: none;
}

.fc-16__label {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--orange);
  font-weight: 700;
  position: relative;
  z-index: 1;
}

.fc-16__title {
  font-size: 24px;
  font-weight: 900;
  color: var(--white);
  text-align: center;
  position: relative;
  z-index: 1;
}

.fc-16__sub {
  font-size: 13px;
  color: rgba(255,251,240,.45);
  text-align: center;
  position: relative;
  z-index: 1;
  line-height: 1.6;
}

.fc-16__click-cta {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 8px;
  padding: 12px 24px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  background: linear-gradient(135deg,var(--orange),var(--yellow));
  color: #000;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .04em;
  transition: transform .15s,box-shadow .15s;
  box-shadow: 0 4px 20px rgba(249,115,22,.3);
}

.fc-16__click-cta:hover {
  box-shadow: 0 8px 30px rgba(249,115,22,.5);
  filter: brightness(1.08);
}

.fc-16__click-cta:active {
  filter: brightness(.95);
}
/* BACK */

.fc-16__back {
  background: linear-gradient(145deg,#0e1a0a,#081008);
  border: 1px solid rgba(74,222,128,.25);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 36px 28px;
}

.fc-16__back::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 40%,rgba(74,222,128,.06),transparent 60%);
}

.fc-16__back-icon {
  width: 80px;
  height: 80px;
  border-radius: 24px;
  background: rgba(74,222,128,.1);
  border: 1px solid rgba(74,222,128,.2);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
}

.fc-16__back-title {
  font-size: 22px;
  font-weight: 900;
  color: var(--white);
  text-align: center;
  position: relative;
  z-index: 1;
}

.fc-16__back-sub {
  font-size: 13px;
  color: rgba(255,251,240,.5);
  text-align: center;
  position: relative;
  z-index: 1;
  line-height: 1.6;
}

.fc-16__code-block {
  position: relative;
  z-index: 1;
  background: rgba(0,0,0,.4);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 10px;
  padding: 12px 16px;
  font-family: 'Courier New',monospace;
  font-size: 11px;
  color: rgba(255,251,240,.6);
  line-height: 1.8;
  width: 100%;
  text-align: left;
}

.fc-16__kw {
  color: #4ade80;
}

.fc-16__str {
  color: #fb923c;
}

.fc-16__cmt {
  color: rgba(255,251,240,.3);
}

.fc-16__flip-back-btn {
  position: relative;
  z-index: 1;
  padding: 11px 24px;
  border-radius: 12px;
  border: 1px solid rgba(74,222,128,.3);
  background: rgba(74,222,128,.1);
  color: #4ade80;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: background .2s;
}

.fc-16__flip-back-btn:hover {
  background: rgba(74,222,128,.18);
}

@media (prefers-reduced-motion: reduce) {
  .fc-16__card {
    transition: none;
  }

  .fc-16__click-dot {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var card=document.getElementById('fc-16-card');
  var scene=document.getElementById('fc-16-scene');
  var backBtn=document.getElementById('fc-16-back-btn');
  scene.addEventListener('click',function(){card.classList.toggle('is-flipped')});
  backBtn.addEventListener('click',function(e){e.stopPropagation();card.classList.remove('is-flipped')});
})();
```
