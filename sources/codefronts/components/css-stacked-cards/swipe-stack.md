---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/swipe-stack/"
title: "Swipe Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A mobile-first media deck built for touch: the top card tracks your finger with translate3d for buttery 60fps, and a committed swipe sends it cycling to the…"
has_js: "true"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Swipe Stack
Source: https://codefronts.com/components/css-stacked-cards/swipe-stack/

A mobile-first media deck built for touch: the top card tracks your finger with translate3d for buttery 60fps, and a committed swipe sends it cycling to the back of the stack — a looping gallery you flick through with your thumb.
## HTML
```html
<section class="scd-20" aria-label="Touch swipe media stack">
  <div class="scd-20__deck" id="scd-20-deck">
    <article class="scd-20__card"><img src="https://picsum.photos/seed/sw-1/360/440" width="360" height="440" alt="Kyoto lane"><span>Kyoto · JP</span></article>
    <article class="scd-20__card"><img src="https://picsum.photos/seed/sw-2/360/440" width="360" height="440" alt="Lofoten"><span>Lofoten · NO</span></article>
    <article class="scd-20__card"><img src="https://picsum.photos/seed/sw-3/360/440" width="360" height="440" alt="Atacama"><span>Atacama · CL</span></article>
    <article class="scd-20__card"><img src="https://picsum.photos/seed/sw-4/360/440" width="360" height="440" alt="Queenstown"><span>Queenstown · NZ</span></article>
  </div>
  <div class="scd-20__ctl"><button id="scd-20-prev" aria-label="Previous">‹</button><p id="scd-20-live" aria-live="polite"></p><button id="scd-20-next" aria-label="Next">›</button></div>
</section>
```
## CSS
```css
.scd-20,
.scd-20 *,
.scd-20 *::before,
.scd-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-20 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  padding: 40px 20px;
  background: #12131b;
}

.scd-20__deck {
  position: relative;
  width: min(300px,84vw);
  height: 380px;
}

.scd-20__card {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  overflow: hidden;
  background: #1d1f2a;
  box-shadow: 0 24px 50px -26px rgba(0,0,0,.85);
  transform: translate3d(0,calc(var(--d,0) * 14px),0) scale(calc(1 - var(--d,0) * .05));
  z-index: calc(10 - var(--d,0));
  transition: transform .45s cubic-bezier(.3,.9,.3,1),opacity .45s;
  touch-action: none;
  cursor: grab;
  will-change: transform;
}

.scd-20__card.scd-20__drag {
  transition: none;
  cursor: grabbing;
}

.scd-20__card.scd-20__fly {
  opacity: 0;
}

.scd-20__card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  pointer-events: none;
}

.scd-20__card span {
  position: absolute;
  left: 16px;
  bottom: 14px;
  color: #fff;
  font-weight: 800;
  font-size: 16px;
  text-shadow: 0 2px 10px rgba(0,0,0,.6);
}

.scd-20__ctl {
  display: flex;
  align-items: center;
  gap: 18px;
}

.scd-20__ctl button {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  border: 1px solid #333a4e;
  background: #20232f;
  color: #fff;
  font-size: 22px;
  cursor: pointer;
  transition: background .2s;
}

.scd-20__ctl button:hover {
  background: #2b2f3e;
}

.scd-20__ctl button:focus-visible {
  outline: 3px solid oklch(0.68 0.15 250);
  outline-offset: 2px;
}

.scd-20__ctl p {
  color: #9aa0b4;
  font-size: 13px;
  min-width: 60px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .scd-20__card {
    transition: transform .2s,opacity .2s;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.scd-20');
  const deck = root.querySelector('#scd-20-deck');
  const live = root.querySelector('#scd-20-live');
  const total = deck.children.length;
  const THRESHOLD = 80;
  const paint = () => { [...deck.children].forEach((c,i) => c.style.setProperty('--d', i)); const t=deck.firstElementChild.querySelector('span'); live.textContent=(t?t.textContent:'')+''; bind(deck.firstElementChild); };
  function sendBack(card){ card.classList.add('scd-20__fly'); card.addEventListener('transitionend',()=>{ card.classList.remove('scd-20__fly'); card.style.transform=''; deck.appendChild(card); paint(); },{once:true}); }
  function bringFront(){ const last=deck.lastElementChild; deck.insertBefore(last, deck.firstElementChild); paint(); }
  function bind(card){
    if(card.dataset.b) return; card.dataset.b='1';
    let sx=0,dy=0,dx=0,drag=false;
    card.addEventListener('pointerdown',e=>{ if(card!==deck.firstElementChild) return; drag=true; sx=e.clientX; card.setPointerCapture(e.pointerId); card.classList.add('scd-20__drag'); });
    card.addEventListener('pointermove',e=>{ if(!drag) return; dx=e.clientX-sx; card.style.transform='translate3d('+dx+'px,0,0) rotate('+(dx/22)+'deg)'; });
    card.addEventListener('pointerup',()=>{ if(!drag) return; drag=false; card.classList.remove('scd-20__drag'); if(Math.abs(dx)>THRESHOLD){ card.style.transform='translate3d('+(dx>0?1:-1)*140+'%,0,0) rotate('+(dx>0?18:-18)+'deg)'; sendBack(card);} else card.style.transform=''; dx=0; });
  }
  root.querySelector('#scd-20-next').addEventListener('click',()=>{ const c=deck.firstElementChild; c.style.transform='translate3d(-140%,0,0) rotate(-16deg)'; sendBack(c); });
  root.querySelector('#scd-20-prev').addEventListener('click',bringFront);
  deck.addEventListener('keydown',e=>{ if(e.key==='ArrowLeft'){const c=deck.firstElementChild;c.style.transform='translate3d(-140%,0,0)';sendBack(c);} if(e.key==='ArrowRight')bringFront(); });
  deck.firstElementChild.setAttribute('tabindex','0');
  paint();
})();
```
