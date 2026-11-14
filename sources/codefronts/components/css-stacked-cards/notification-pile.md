---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/notification-pile/"
title: "Notification Pile"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "An OS-style alert stack: fresh notifications spring onto the top of the pile while older ones compress into a neat deck below."
has_js: "true"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Notification Pile
Source: https://codefronts.com/components/css-stacked-cards/notification-pile/

An OS-style alert stack: fresh notifications spring onto the top of the pile while older ones compress into a neat deck below. Tap the stack to expand every alert, swipe or dismiss the top one, and watch the pile re-settle.
## HTML
```html
<section class="scd-25" aria-label="Notification pile">
  <div class="scd-25__panel">
    <div class="scd-25__head"><b>Notifications</b><button id="scd-25-exp" aria-expanded="false">Expand</button></div>
    <div class="scd-25__pile" id="scd-25-pile" aria-live="polite">
      <article class="scd-25__note" style="--c:oklch(0.66 0.15 250)"><b>New comment</b><span>Dana replied to your thread.</span></article>
      <article class="scd-25__note" style="--c:oklch(0.68 0.15 150)"><b>Build passed</b><span>main deployed in 2m 14s.</span></article>
      <article class="scd-25__note" style="--c:oklch(0.7 0.15 60)"><b>Reminder</b><span>Standup starts in 10 minutes.</span></article>
    </div>
    <div class="scd-25__foot"><button id="scd-25-add">Simulate alert</button><button id="scd-25-dismiss">Dismiss top</button></div>
  </div>
</section>
```
## CSS
```css
.scd-25,
.scd-25 *,
.scd-25 *::before,
.scd-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-25 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background: #0e0f16;
}

.scd-25__panel {
  width: min(340px,100%);
}

.scd-25__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  color: #eef0f6;
}

.scd-25__head b {
  font-size: 16px;
  font-weight: 800;
}

.scd-25__head button {
  background: none;
  border: 1px solid #333a4e;
  color: #c3c7de;
  padding: 6px 12px;
  border-radius: 9px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
}

.scd-25__pile {
  position: relative;
  height: 120px;
  transition: height .4s ease;
}

.scd-25__pile.scd-25__open {
  height: auto;
}

.scd-25__note {
  padding: 16px 18px;
  border-radius: 14px;
  background: #1b1e2a;
  border: 1px solid #2a2e3c;
  border-left: 4px solid var(--c);
  color: #eef0f6;
  box-shadow: 0 14px 30px -18px rgba(0,0,0,.8);
  display: flex;
  flex-direction: column;
  gap: 4px;
  transform: translateY(calc(var(--d,0) * 12px)) scale(calc(1 - var(--d,0) * .05));
  z-index: calc(20 - var(--d,0));
  transition: transform .45s cubic-bezier(.34,1.4,.5,1),opacity .4s;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
}

.scd-25__pile.scd-25__open .scd-25__note {
  position: relative;
  transform: none;
  margin-bottom: 10px;
  opacity: 1!important;
}

.scd-25__note[style*="--d: 0"],
.scd-25__note {
  --dummy: 0;
}

.scd-25__note.scd-25__hidden {
  opacity: 0;
}

.scd-25__note.scd-25__enter {
  animation: scd-25-pop .5s cubic-bezier(.34,1.56,.5,1);
}

@keyframes scd-25-pop {
  from {
    transform: translateY(-40px) scale(.9);
    opacity: 0;
  }
}

.scd-25__note b {
  font-size: 14px;
  font-weight: 800;
}

.scd-25__note span {
  font-size: 13px;
  color: #a9adc0;
}

.scd-25__foot {
  display: flex;
  gap: 10px;
  margin-top: 16px;
}

.scd-25__foot button {
  flex: 1;
  padding: 11px;
  border-radius: 11px;
  border: none;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  background: #242838;
  color: #fff;
  transition: background .2s;
}

.scd-25__foot button:hover {
  background: #2e3346;
}

.scd-25__head button:focus-visible,
.scd-25__foot button:focus-visible {
  outline: 3px solid oklch(0.66 0.15 250);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-25__note {
    transition: opacity .2s;
  }

  .scd-25__note.scd-25__enter {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.scd-25');
  const pile = root.querySelector('#scd-25-pile');
  const samples = [['New follower','Sam started following you.','oklch(0.66 0.15 300)'],['Payment received','$49 from Acme Co.','oklch(0.68 0.15 150)'],['Mention','You were tagged in #design.','oklch(0.66 0.15 250)'],['Storage low','92% of your quota used.','oklch(0.7 0.16 40)']];
  let s = 0;
  const paint = () => [...pile.children].forEach((n,i) => n.style.setProperty('--d', Math.min(i,4)));
  function add(){
    const [t,d,c] = samples[s++ % samples.length];
    const el = document.createElement('article');
    el.className = 'scd-25__note scd-25__enter'; el.style.setProperty('--c', c);
    el.innerHTML = '<b>'+t+'</b><span>'+d+'</span>';
    pile.insertBefore(el, pile.firstElementChild); paint();
    el.addEventListener('animationend', () => el.classList.remove('scd-25__enter'), {once:true});
  }
  function dismiss(){ const top = pile.firstElementChild; if(!top) return; top.classList.add('scd-25__hidden'); top.addEventListener('transitionend', () => { top.remove(); paint(); }, {once:true}); }
  root.querySelector('#scd-25-add').addEventListener('click', add);
  root.querySelector('#scd-25-dismiss').addEventListener('click', dismiss);
  root.querySelector('#scd-25-exp').addEventListener('click', e => { const open = pile.classList.toggle('scd-25__open'); e.target.textContent = open ? 'Collapse' : 'Expand'; e.target.setAttribute('aria-expanded', open); });
  root.addEventListener('keydown', e => { if(e.key==='Escape') dismiss(); });
  paint();
})();
```
