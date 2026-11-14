---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/horizontal-swiper-deck-tinder-style/"
title: "Horizontal Swiper Deck (Tinder-style)"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "The classic decision deck: cards sit flush on top of one another; drag the top card left or right — or tap the action buttons — and it flies off with a…"
has_js: "true"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Swiper Deck (Tinder-style)
Source: https://codefronts.com/components/css-stacked-cards/horizontal-swiper-deck-tinder-style/

The classic decision deck: cards sit flush on top of one another; drag the top card left or right — or tap the action buttons — and it flies off with a natural rotation, snapping the next card into focus. Lightweight pointer events, no gesture library.
## HTML
```html
<section class="scd-02" aria-label="Swipeable card deck">
  <div class="scd-02__deck" id="scd-02-deck">
    <article class="scd-02__card" tabindex="0"><img src="https://picsum.photos/seed/swipe-1/400/460" width="400" height="460" alt="Mountain lake"><div class="scd-02__meta"><h3>Aria, 27</h3><p>Trail runner · Portland</p></div></article>
    <article class="scd-02__card" tabindex="0"><img src="https://picsum.photos/seed/swipe-2/400/460" width="400" height="460" alt="City rooftop"><div class="scd-02__meta"><h3>Devon, 31</h3><p>Coffee nerd · Austin</p></div></article>
    <article class="scd-02__card" tabindex="0"><img src="https://picsum.photos/seed/swipe-3/400/460" width="400" height="460" alt="Desert road"><div class="scd-02__meta"><h3>Sky, 24</h3><p>Van-lifer · Denver</p></div></article>
    <article class="scd-02__card" tabindex="0"><img src="https://picsum.photos/seed/swipe-4/400/460" width="400" height="460" alt="Forest path"><div class="scd-02__meta"><h3>Rowan, 29</h3><p>Botanist · Seattle</p></div></article>
    <div class="scd-02__empty">That's everyone for now 🎉</div>
  </div>
  <div class="scd-02__controls">
    <button class="scd-02__btn scd-02__btn--no" id="scd-02-no" aria-label="Pass">✕</button>
    <button class="scd-02__btn scd-02__btn--yes" id="scd-02-yes" aria-label="Like">♥</button>
  </div>
  <p class="scd-02__count" id="scd-02-count" aria-live="polite"></p>
</section>
```
## CSS
```css
.scd-02,
.scd-02 *,
.scd-02 *::before,
.scd-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-02 {
  --yes: oklch(0.7 0.17 150);
  --no: oklch(0.65 0.2 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(circle at 50% 0%,#2a2340,#15121f);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  padding: 40px 20px;
}

.scd-02__deck {
  position: relative;
  width: min(320px,86vw);
  height: 420px;
}

.scd-02__empty {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #b6b0cc;
  font-size: 16px;
  text-align: center;
  padding: 30px;
}

.scd-02__card {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  overflow: hidden;
  background: #241f36;
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.75);
  cursor: grab;
  user-select: none;
  touch-action: none;
  transition: transform .5s cubic-bezier(.2,.9,.2,1),opacity .5s;
}

.scd-02__card:nth-last-child(2) {
  transform: scale(.94) translateY(16px);
}

.scd-02__card:nth-last-child(3) {
  transform: scale(.88) translateY(32px);
}

.scd-02__card:nth-last-child(n+4) {
  transform: scale(.82) translateY(46px);
  opacity: 0;
}

.scd-02__card.scd-02__is-top {
  cursor: grab;
}

.scd-02__card.scd-02__dragging {
  transition: none;
  cursor: grabbing;
}

.scd-02__card.scd-02__gone--yes {
  transform: translate(140%,-10%) rotate(22deg)!important;
  opacity: 0;
}

.scd-02__card.scd-02__gone--no {
  transform: translate(-140%,-10%) rotate(-22deg)!important;
  opacity: 0;
}

.scd-02__card img {
  width: 100%;
  height: 74%;
  object-fit: cover;
  display: block;
  pointer-events: none;
}

.scd-02__meta {
  padding: 16px 18px;
  color: #fff;
}

.scd-02__meta h3 {
  font-size: 20px;
  font-weight: 800;
}

.scd-02__meta p {
  font-size: 13px;
  color: #c3bdd8;
  margin-top: 3px;
}

.scd-02__card::before,
.scd-02__card::after {
  position: absolute;
  top: 22px;
  padding: 6px 12px;
  border: 3px solid;
  border-radius: 8px;
  font-weight: 800;
  font-size: 15px;
  letter-spacing: .08em;
  opacity: 0;
  transition: opacity .15s;
}

.scd-02__card::before {
  content: "LIKE";
  left: 18px;
  color: var(--yes);
  border-color: var(--yes);
  transform: rotate(-14deg);
}

.scd-02__card::after {
  content: "NOPE";
  right: 18px;
  color: var(--no);
  border-color: var(--no);
  transform: rotate(14deg);
}

.scd-02__card.scd-02__hint-yes::before {
  opacity: 1;
}

.scd-02__card.scd-02__hint-no::after {
  opacity: 1;
}

.scd-02__controls {
  display: flex;
  gap: 24px;
}

.scd-02__btn {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: none;
  font-size: 22px;
  cursor: pointer;
  color: #fff;
  box-shadow: 0 10px 24px -10px rgba(0,0,0,.6);
  transition: transform .15s;
}

.scd-02__btn:hover {
  transform: translateY(-3px) scale(1.06);
}

.scd-02__btn:active {
  transform: scale(.94);
}

.scd-02__btn--no {
  background: var(--no);
}

.scd-02__btn--yes {
  background: var(--yes);
}

.scd-02__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.scd-02__count {
  color: #9c96b4;
  font-size: 13px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-02__card {
    transition: opacity .2s;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.scd-02');
  const deck = root.querySelector('#scd-02-deck');
  const countEl = root.querySelector('#scd-02-count');
  const THRESHOLD = 90;
  const cards = () => [...deck.querySelectorAll('.scd-02__card')];
  const top = () => cards()[cards().length - 1] || null;
  function refresh(){
    cards().forEach(c => c.classList.remove('scd-02__is-top'));
    const t = top();
    if (t){ t.classList.add('scd-02__is-top'); bind(t); }
    const n = cards().length;
    countEl.textContent = n ? n + ' card' + (n>1?'s':'') + ' left' : 'Deck empty — reload to reshuffle';
  }
  function fling(card, dir){
    card.classList.add(dir>0 ? 'scd-02__gone--yes' : 'scd-02__gone--no');
    card.addEventListener('transitionend', () => { card.remove(); refresh(); }, {once:true});
  }
  function bind(card){
    if (card.dataset.bound) return; card.dataset.bound = '1';
    let startX=0, dx=0, dragging=false;
    card.addEventListener('pointerdown', e => { if (card !== top()) return; dragging=true; startX=e.clientX; card.setPointerCapture(e.pointerId); card.classList.add('scd-02__dragging'); });
    card.addEventListener('pointermove', e => { if(!dragging) return; dx=e.clientX-startX; card.style.transform='translateX('+dx+'px) rotate('+(dx/18)+'deg)'; card.classList.toggle('scd-02__hint-yes', dx>30); card.classList.toggle('scd-02__hint-no', dx<-30); });
    card.addEventListener('pointerup', () => { if(!dragging) return; dragging=false; card.classList.remove('scd-02__dragging'); if(Math.abs(dx)>THRESHOLD){ fling(card, dx>0?1:-1); } else { card.style.transform=''; card.classList.remove('scd-02__hint-yes','scd-02__hint-no'); } dx=0; });
    card.addEventListener('keydown', e => { if(e.key==='ArrowRight'){ fling(card,1);} if(e.key==='ArrowLeft'){ fling(card,-1);} });
  }
  root.querySelector('#scd-02-yes').addEventListener('click', () => { const t=top(); if(t) fling(t,1); });
  root.querySelector('#scd-02-no').addEventListener('click', () => { const t=top(); if(t) fling(t,-1); });
  refresh();
})();
```
