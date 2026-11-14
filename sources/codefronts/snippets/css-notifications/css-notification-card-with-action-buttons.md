---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-notification-card-with-action-buttons/"
title: "CSS Notification Card With Action Buttons"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Notifications as conversations: an invitation card with Accept/Decline whose answer morphs the card in place (accept collapses the buttons and stamps a…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Notification Card With Action Buttons
Source: https://codefronts.com/snippets/css-notifications/css-notification-card-with-action-buttons/

Notifications as conversations: an invitation card with Accept/Decline whose answer morphs the card in place (accept collapses the buttons and stamps a confirmation; decline fades the card out through a grid-rows collapse), and a zero-JavaScript swipe-to-act row where scroll-snap physics reveal archive/delete actions under the card — the mobile gesture rebuilt from standard CSS.
## HTML
```html
<div class="ntf-26-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-26a" aria-label="Invitation card with accept and decline actions">
  <div class="ntf-26a__card" id="ntf-26a-card" data-state="open">
    <div class="ntf-26a__head">
      <img class="ntf-26a__ava" src="https://i.pravatar.cc/80?img=26" alt="" width="44" height="44">
      <span class="ntf-26a__tx"><b>Nadia invited you to <em>Payments v2</em></b><small>as editor · 4 people inside · 2m ago</small></span>
    </div>
    <div class="ntf-26a__actions"><div class="ntf-26a__clip">
      <div class="ntf-26a__row">
        <button class="ntf-26a__accept" id="ntf-26a-accept" type="button">Accept</button>
        <button class="ntf-26a__decline" id="ntf-26a-decline" type="button">Decline</button>
      </div>
    </div></div>
    <div class="ntf-26a__stamp"><div class="ntf-26a__clip">
      <p class="ntf-26a__stamptx" id="ntf-26a-stamp" role="status"></p>
    </div></div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-26b" aria-label="Notification rows with swipe-revealed actions">
  <div class="ntf-26b__list">
    <p class="ntf-26b__lead">drag a card left (touch, trackpad, or shift + wheel) — scroll-snap does the physics</p>
    <div class="ntf-26b__swipe">
      <div class="ntf-26b__row"><img src="https://i.pravatar.cc/64?img=14" alt="" width="36" height="36"><span><b>Leo shared “brand-refresh.fig”</b><small>can edit · 12m</small></span></div>
      <div class="ntf-26b__acts"><button class="ntf-26b__act" type="button" aria-label="Archive">&#128229;</button><button class="ntf-26b__act ntf-26b__act--del" type="button" aria-label="Delete">&#10005;</button></div>
    </div>
    <div class="ntf-26b__swipe">
      <div class="ntf-26b__row"><img src="https://i.pravatar.cc/64?img=41" alt="" width="36" height="36"><span><b>Standup notes are ready</b><small>#team-frontend · 1h</small></span></div>
      <div class="ntf-26b__acts"><button class="ntf-26b__act" type="button" aria-label="Archive">&#128229;</button><button class="ntf-26b__act ntf-26b__act--del" type="button" aria-label="Delete">&#10005;</button></div>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-26-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-26-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-26a,
.ntf-26a *,
.ntf-26a *::before,
.ntf-26a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-26a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#151a26,#0b0e15);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-26a__card {
  width: min(390px,100%);
  padding: 18px;
  border-radius: 18px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(165,190,230,.18);
  box-shadow: 0 30px 65px -35px rgba(0,0,0,.9);
  transition: opacity .45s,translate .45s,scale .45s;
}

.ntf-26a__card[data-state=declined] {
  opacity: 0;
  translate: 0 10px;
  scale: .97;
}

.ntf-26a__head {
  display: flex;
  gap: 13px;
  align-items: center;
}

.ntf-26a__ava {
  flex: none;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  background: #232a3b;
}

.ntf-26a__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-26a__tx b {
  font-size: 14px;
  font-weight: 600;
  color: #edf2fc;
  line-height: 1.4;
}

.ntf-26a__tx em {
  font-style: normal;
  color: oklch(0.78 0.12 200);
}

.ntf-26a__tx small {
  font-size: 12px;
  color: rgba(212,224,246,.5);
}

.ntf-26a__actions,
.ntf-26a__stamp {
  display: grid;
  transition: grid-template-rows .4s cubic-bezier(.4,0,.2,1),opacity .3s;
}

.ntf-26a__actions {
  grid-template-rows: 1fr;
  opacity: 1;
}

.ntf-26a__stamp {
  grid-template-rows: 0fr;
  opacity: 0;
}

.ntf-26a__card[data-state=accepted] .ntf-26a__actions {
  grid-template-rows: 0fr;
  opacity: 0;
  pointer-events: none;
}

.ntf-26a__card[data-state=accepted] .ntf-26a__stamp {
  grid-template-rows: 1fr;
  opacity: 1;
}

.ntf-26a__clip {
  overflow: hidden;
}

.ntf-26a__row {
  display: flex;
  gap: 9px;
  padding-top: 15px;
}

.ntf-26a__accept {
  flex: 1;
  padding: 12px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  color: #0d1a12;
  background: oklch(0.8 0.15 160);
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  transition: filter .15s,scale .12s;
}

.ntf-26a__accept:hover {
  filter: brightness(1.07);
}

.ntf-26a__decline {
  flex: 1;
  padding: 12px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  color: #edf2fc;
  background: transparent;
  border: 1.5px solid rgba(165,190,230,.3);
  border-radius: 11px;
  cursor: pointer;
  transition: background .15s,scale .12s;
}

.ntf-26a__decline:hover {
  background: rgba(255,255,255,.06);
}

.ntf-26a__accept:active,
.ntf-26a__decline:active {
  scale: .97;
}

.ntf-26a__accept:disabled,
.ntf-26a__decline:disabled {
  opacity: .5;
  cursor: default;
}

.ntf-26a__stamptx {
  padding-top: 15px;
  font-size: 13px;
  font-weight: 600;
  color: oklch(0.8 0.15 160);
}

.ntf-26a__stamptx::before {
  content: "✓ ";
  font-weight: 800;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-26a__card,
    .ntf-26a__actions,
    .ntf-26a__stamp {
    transition-duration: .01s;
  }
}

.ntf-26b,
.ntf-26b *,
.ntf-26b *::before,
.ntf-26b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-26b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f3ec,#ebe4d3);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-26b__list {
  width: min(400px,100%);
  display: grid;
  gap: 12px;
}

.ntf-26b__lead {
  font-size: 12px;
  line-height: 1.6;
  color: rgba(36,31,23,.5);
  text-align: center;
  margin-bottom: 6px;
  text-wrap: pretty;
}

.ntf-26b__swipe {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
  border-radius: 16px;
}

.ntf-26b__swipe::-webkit-scrollbar {
  display: none;
}

.ntf-26b__row {
  flex: 0 0 100%;
  scroll-snap-align: start;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 16px;
  background: #fffdf7;
  border: 1px solid rgba(36,31,23,.11);
  box-shadow: 0 16px 36px -24px rgba(36,31,23,.5);
}

.ntf-26b__row img {
  flex: none;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
  background: #ddd6c6;
}

.ntf-26b__row span {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-26b__row b {
  font-size: 13px;
  font-weight: 600;
  color: #241f17;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ntf-26b__row small {
  font-size: 11.5px;
  color: rgba(36,31,23,.5);
}

.ntf-26b__acts {
  flex: 0 0 124px;
  scroll-snap-align: end;
  display: flex;
  gap: 8px;
}

.ntf-26b__act {
  flex: 1;
  display: grid;
  place-items: center;
  font-size: 17px;
  border: 0;
  border-radius: 14px;
  color: #241f17;
  background: rgba(36,31,23,.1);
  cursor: pointer;
  transition: background .15s,scale .12s;
}

.ntf-26b__act:hover {
  background: rgba(36,31,23,.18);
}

.ntf-26b__act:active {
  scale: .95;
}

.ntf-26b__act--del {
  color: #fff;
  background: oklch(0.62 0.19 25);
}

.ntf-26b__act--del:hover {
  background: oklch(0.56 0.19 25);
}

.ntf-26b__act:focus-visible {
  outline: 2px solid #241f17;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-26b__swipe {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
(function(){
  var card=document.getElementById('ntf-26a-card'); if(!card) return;
  var accept=document.getElementById('ntf-26a-accept'),decline=document.getElementById('ntf-26a-decline'),
      stamp=document.getElementById('ntf-26a-stamp');
  function lock(){ accept.disabled=true; decline.disabled=true; }
  accept.addEventListener('click',function(){
    lock(); stamp.textContent='Accepted — Payments v2 is now in your sidebar.';
    card.setAttribute('data-state','accepted');
  });
  decline.addEventListener('click',function(){
    lock(); card.setAttribute('data-state','declined');
    card.addEventListener('transitionend',function(e){ if(e.propertyName==='opacity') card.remove(); });
  });
})();

/* No JavaScript — each row is a 2-item scroll-snap carousel: the card (100% wide, snaps closed) and the action panel (124px, snaps open). Browser scroll physics provide momentum and settling; the buttons stay real and keyboard-reachable. */
```
