---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/expandable-notification-panel-css/"
title: "Expandable Notification Panel CSS"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Two platform-native dropdown panels: a <details> notification center whose open/close animates through ::details-content + allow-discrete (zero JS, state…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Notification Panel CSS
Source: https://codefronts.com/snippets/css-notifications/expandable-notification-panel-css/

Two platform-native dropdown panels: a <details> notification center whose open/close animates through ::details-content + allow-discrete (zero JS, state included), and a popover-API panel that lives in the top layer — light-dismiss, Esc-to-close and focus handling free — scaling in from the bell via @starting-style with a tiny position sync.
## HTML
```html
<div class="ntf-22-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-22a" aria-label="Notification panel built on the details element">
  <div class="ntf-22a__anchor">
    <details class="ntf-22a__dd">
      <summary class="ntf-22a__bell" aria-label="Notifications, 3 unread">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg>
        <i class="ntf-22a__dot" aria-hidden="true"></i>
      </summary>
      <div class="ntf-22a__panel">
        <header class="ntf-22a__head"><b>Notifications</b><span>3 new</span></header>
        <a class="ntf-22a__item" href="#" onclick="return false"><img src="https://i.pravatar.cc/64?img=21" alt="" width="32" height="32"><span><b>Rosa approved your PR</b><small>design-tokens #142 · 2m</small></span><i class="ntf-22a__new" aria-hidden="true"></i></a>
        <a class="ntf-22a__item" href="#" onclick="return false"><img src="https://i.pravatar.cc/64?img=59" alt="" width="32" height="32"><span><b>Kenji mentioned you</b><small>“ping @you re: the badge mask” · 14m</small></span><i class="ntf-22a__new" aria-hidden="true"></i></a>
        <a class="ntf-22a__item" href="#" onclick="return false"><img src="https://i.pravatar.cc/64?img=36" alt="" width="32" height="32"><span><b>Build finished</b><small>deploy-preview ready · 1h</small></span><i class="ntf-22a__new" aria-hidden="true"></i></a>
        <a class="ntf-22a__all" href="#" onclick="return false">View all</a>
      </div>
    </details>
    <p class="ntf-22a__hint">a &lt;details&gt; element — state, toggling and keyboard for free; ::details-content animates the reveal</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-22b" aria-label="Notification panel using the Popover API">
  <div class="ntf-22b__bar">
    <span class="ntf-22b__brand">console</span>
    <button class="ntf-22b__bell" id="ntf-22b-bell" type="button" popovertarget="ntf-22b-pop" aria-label="Notifications, 2 unread">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg>
      <i class="ntf-22b__dot" aria-hidden="true"></i>
    </button>
  </div>
  <div class="ntf-22b__pop" id="ntf-22b-pop" popover>
    <header class="ntf-22b__head"><b>Activity</b><button class="ntf-22b__clear" type="button" popovertarget="ntf-22b-pop" popovertargetaction="hide">Close</button></header>
    <a class="ntf-22b__item" href="#" onclick="return false"><i class="ntf-22b__glyph" style="--c:oklch(0.62 0.14 155)" aria-hidden="true">&#10003;</i><span><b>Payout sent</b><small>$1,840.00 → checking ···4092</small></span></a>
    <a class="ntf-22b__item" href="#" onclick="return false"><i class="ntf-22b__glyph" style="--c:oklch(0.6 0.12 250)" aria-hidden="true">&#64;</i><span><b>New follower</b><small>@margins.dev follows your snippets</small></span></a>
    <p class="ntf-22b__foot">click anywhere outside, or press Esc — the platform closes it</p>
  </div>
  <p class="ntf-22b__hint">the panel is a <b>[popover]</b>: top layer, light-dismiss and Esc handling with no listeners</p>
</section>
</div>
```
## CSS
```css
.ntf-22-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-22-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-22a,
.ntf-22a *,
.ntf-22a *::before,
.ntf-22a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-22a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#161b27,#0c0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-22a__anchor {
  display: grid;
  gap: 20px;
  justify-items: center;
  min-height: 400px;
  align-content: start;
}

.ntf-22a__dd {
  position: relative;
}

.ntf-22a__bell {
  position: relative;
  list-style: none;
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  border-radius: 16px;
  color: #d7e1f5;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(165,190,230,.2);
  cursor: pointer;
  transition: background .2s;
}

.ntf-22a__bell::-webkit-details-marker {
  display: none;
}

.ntf-22a__bell:hover {
  background: rgba(255,255,255,.11);
}

.ntf-22a__bell:focus-visible {
  outline: 2px solid #d7e1f5;
  outline-offset: 2px;
}

.ntf-22a__bell svg {
  width: 23px;
  height: 23px;
}

.ntf-22a__dot {
  position: absolute;
  top: 11px;
  inset-inline-end: 11px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: oklch(0.68 0.21 25);
  border: 2px solid #161b27;
  transition: scale .2s;
}

.ntf-22a__dd[open] .ntf-22a__dot {
  scale: 0;
}

.ntf-22a__dd::details-content {
  opacity: 0;
  translate: 0 -8px;
  transition: opacity .28s ease,translate .28s cubic-bezier(.22,1.2,.36,1),content-visibility .28s allow-discrete;
}

.ntf-22a__dd[open]::details-content {
  opacity: 1;
  translate: 0 0;
}

.ntf-22a__panel {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  translate: -50% 0;
  width: min(330px,calc(100vw - 48px));
  padding: 8px;
  border-radius: 16px;
  background: #171c29;
  border: 1px solid rgba(165,190,230,.2);
  box-shadow: 0 30px 65px -25px rgba(0,0,0,.95);
  z-index: 10;
}

.ntf-22a__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 10px 12px 8px;
}

.ntf-22a__head b {
  font-size: 14px;
  font-weight: 600;
  color: #edf2fc;
}

.ntf-22a__head span {
  font-size: 11.5px;
  color: oklch(0.75 0.15 25);
}

.ntf-22a__item {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 10px 12px;
  border-radius: 11px;
  text-decoration: none;
  transition: background .15s;
}

.ntf-22a__item:hover {
  background: rgba(255,255,255,.05);
}

.ntf-22a__item img {
  flex: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #242b3d;
}

.ntf-22a__item span {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-22a__item b {
  font-size: 12.5px;
  font-weight: 600;
  color: #edf2fc;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ntf-22a__item small {
  font-size: 11px;
  color: rgba(212,224,246,.5);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ntf-22a__new {
  margin-left: auto;
  flex: none;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: oklch(0.72 0.15 200);
}

.ntf-22a__all {
  display: block;
  text-align: center;
  padding: 10px;
  margin-top: 2px;
  border-top: 1px solid rgba(165,190,230,.12);
  font-size: 12.5px;
  font-weight: 600;
  color: oklch(0.75 0.13 200);
  text-decoration: none;
}

.ntf-22a__all:hover {
  color: oklch(0.85 0.1 200);
}

.ntf-22a__hint {
  font-size: 12px;
  color: rgba(212,224,246,.4);
  text-align: center;
  max-inline-size: 40ch;
  line-height: 1.6;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-22a__dd::details-content {
    transition-duration: .01s;
  }
}

.ntf-22b,
.ntf-22b *,
.ntf-22b *::before,
.ntf-22b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-22b {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f3ec,#ece5d5);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-22b__bar {
  width: min(430px,100%);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 13px 18px;
  border-radius: 16px;
  background: #fffdf7;
  border: 1px solid rgba(36,31,23,.11);
  box-shadow: 0 20px 46px -26px rgba(36,31,23,.5);
}

.ntf-22b__brand {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #241f17;
}

.ntf-22b__bell {
  position: relative;
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 12px;
  color: #241f17;
  background: rgba(36,31,23,.06);
  cursor: pointer;
  transition: background .15s;
}

.ntf-22b__bell:hover {
  background: rgba(36,31,23,.12);
}

.ntf-22b__bell:focus-visible {
  outline: 2px solid #241f17;
  outline-offset: 2px;
}

.ntf-22b__bell svg {
  width: 20px;
  height: 20px;
}

.ntf-22b__dot {
  position: absolute;
  top: 8px;
  inset-inline-end: 8px;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.63 0.21 25);
  border: 2px solid #fffdf7;
}

.ntf-22b__pop {
  position: fixed;
  margin: 0;
  width: min(320px,calc(100vw - 32px));
  padding: 8px;
  border: 1px solid rgba(36,31,23,.13);
  border-radius: 16px;
  background: #fffdf7;
  box-shadow: 0 34px 70px -28px rgba(36,31,23,.6);
  opacity: 0;
  scale: .94;
  transform-origin: top right;
  transition: opacity .25s ease,scale .3s cubic-bezier(.22,1.3,.36,1),display .3s allow-discrete,overlay .3s allow-discrete;
}

.ntf-22b__pop:popover-open {
  opacity: 1;
  scale: 1;
}

@starting-style {
  .ntf-22b__pop:popover-open {
    opacity: 0;
    scale: .94;
  }
}

.ntf-22b__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px 6px;
}

.ntf-22b__head b {
  font-size: 14px;
  font-weight: 700;
  color: #241f17;
}

.ntf-22b__clear {
  padding: 6px 12px;
  font: inherit;
  font-size: 11.5px;
  font-weight: 700;
  color: #241f17;
  background: rgba(36,31,23,.07);
  border: 0;
  border-radius: 8px;
  cursor: pointer;
  transition: background .15s;
}

.ntf-22b__clear:hover {
  background: rgba(36,31,23,.14);
}

.ntf-22b__item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 12px;
  border-radius: 11px;
  text-decoration: none;
  transition: background .15s;
}

.ntf-22b__item:hover {
  background: rgba(36,31,23,.05);
}

.ntf-22b__glyph {
  flex: none;
  width: 32px;
  height: 32px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  font-style: normal;
  font-size: 13px;
  font-weight: 700;
  color: #fffdf7;
  background: var(--c);
}

.ntf-22b__item span {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-22b__item b {
  font-size: 13px;
  font-weight: 600;
  color: #241f17;
}

.ntf-22b__item small {
  font-size: 11.5px;
  color: rgba(36,31,23,.55);
}

.ntf-22b__foot {
  padding: 10px 12px 8px;
  border-top: 1px solid rgba(36,31,23,.09);
  margin-top: 4px;
  font-size: 11px;
  color: rgba(36,31,23,.45);
}

.ntf-22b__hint {
  font-size: 12px;
  color: rgba(36,31,23,.5);
  text-align: center;
  max-inline-size: 44ch;
  line-height: 1.6;
  text-wrap: pretty;
}

.ntf-22b__hint b {
  color: #241f17;
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-22b__pop {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — details/summary owns the open state (space/enter toggle it), ::details-content + allow-discrete animate the reveal both ways, and [open] clears the unread dot because opening IS seeing. */

(function(){
  var pop=document.getElementById('ntf-22b-pop'); if(!pop||!pop.showPopover) return;
  var bell=document.getElementById('ntf-22b-bell');
  /* Until CSS anchor positioning is everywhere: pin the top-layer panel under the bell. */
  pop.addEventListener('toggle',function(e){
    if(e.newState!=='open') return;
    var r=bell.getBoundingClientRect();
    pop.style.top=(r.bottom+10)+'px';
    pop.style.left=Math.max(16,Math.min(r.right-pop.offsetWidth,innerWidth-pop.offsetWidth-16))+'px';
    bell.querySelector('.ntf-22b__dot').style.scale='0';   /* opened = seen */
    bell.setAttribute('aria-label','Notifications');
  });
})();
```
