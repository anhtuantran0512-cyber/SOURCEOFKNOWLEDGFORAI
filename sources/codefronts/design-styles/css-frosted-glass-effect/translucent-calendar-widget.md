---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/translucent-calendar-widget/"
title: "Translucent Calendar Widget"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A compact glass calendar with JS-generated date grid, month navigation, clickable date selection, today highlight ring, event dot indicators on specific…"
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Translucent Calendar Widget
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/translucent-calendar-widget/

A compact glass calendar with JS-generated date grid, month navigation, clickable date selection, today highlight ring, event dot indicators on specific dates, and a live upcoming-events chip list that updates per selected date.
## HTML
```html
<div class="fg-14">
  <div class="fg-09__bg" aria-hidden="true">
    <div class="fg-09__glow fg-09__glow--1"></div>
    <div class="fg-09__glow fg-09__glow--2"></div>
  </div>
  <div class="fg-09__cal" role="application" aria-label="Calendar widget">
    <div class="fg-09__hd">
      <button class="fg-09__nav" id="fg-14-prev" aria-label="Previous month">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
      </button>
      <div class="fg-09__month-wrap">
        <p class="fg-09__month" id="fg-14-month"></p>
        <p class="fg-09__year" id="fg-14-year"></p>
      </div>
      <button class="fg-09__nav" id="fg-14-next" aria-label="Next month">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
      </button>
    </div>
    <div class="fg-09__weekdays" aria-hidden="true">
      <span>Su</span><span>Mo</span><span>Tu</span><span>We</span><span>Th</span><span>Fr</span><span>Sa</span>
    </div>
    <div class="fg-09__grid" id="fg-14-grid" role="grid" aria-label="Calendar dates"></div>
    <div class="fg-09__events-hd">Upcoming</div>
    <div class="fg-09__events" id="fg-14-events" aria-live="polite"></div>
  </div>
</div>
```
## CSS
```css
.fg-14,
.fg-14 *,
.fg-14 *::before,
.fg-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-14 ::selection {
  background: rgba(99,102,241,.5);
  color: #fff;
}

.fg-14 {
  --c-bg: #080820;
  --c-a: #6366f1;
  --c-a2: #8b5cf6;
  --c-glass: rgba(255,255,255,.07);
  --c-border: rgba(255,255,255,.1);
  --c-text: #eef0ff;
  --c-muted: rgba(238,240,255,.5);
  --t: .2s ease;
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

.fg-09__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-09__glow {
  position: absolute;
  border-radius: 50%;
}

.fg-09__glow--1 {
  width: 420px;
  height: 420px;
  background: radial-gradient(circle,rgba(99,102,241,.25),transparent 70%);
  top: -100px;
  left: -80px;
  animation: fg-14-g1 22s ease-in-out infinite alternate;
}

.fg-09__glow--2 {
  width: 340px;
  height: 340px;
  background: radial-gradient(circle,rgba(139,92,246,.2),transparent 70%);
  bottom: -80px;
  right: -60px;
  animation: fg-14-g2 18s ease-in-out infinite alternate;
}

@keyframes fg-14-g1 {
  to {
    transform: translate(60px,80px) scale(1.15);
  }
}

@keyframes fg-14-g2 {
  to {
    transform: translate(-50px,-60px) scale(1.1);
  }
}

.fg-09__cal {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 360px;
  background: var(--c-glass);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid var(--c-border);
  border-radius: 24px;
  padding: 22px;
  box-shadow: 0 8px 48px rgba(0,0,0,.5),0 1px 0 rgba(255,255,255,.1) inset;
}

.fg-09__hd {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
}

.fg-09__nav {
  width: 32px;
  height: 32px;
  border: 1px solid var(--c-border);
  border-radius: 8px;
  background: rgba(255,255,255,.06);
  color: var(--c-text);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background var(--t);
}

.fg-09__nav:hover {
  background: rgba(255,255,255,.12);
}

.fg-09__month-wrap {
  text-align: center;
}

.fg-09__month {
  font-size: 16px;
  font-weight: 800;
  color: var(--c-text);
  letter-spacing: -.2px;
}

.fg-09__year {
  font-size: 12px;
  color: var(--c-muted);
  margin-top: 1px;
}

.fg-09__weekdays {
  display: grid;
  grid-template-columns: repeat(7,1fr);
  gap: 2px;
  margin-bottom: 8px;
}

.fg-09__weekdays span {
  text-align: center;
  font-size: 11px;
  font-weight: 600;
  color: var(--c-muted);
  letter-spacing: .3px;
  padding: 4px 0;
}

.fg-09__grid {
  display: grid;
  grid-template-columns: repeat(7,1fr);
  gap: 2px;
  margin-bottom: 18px;
}

.fg-09__cell {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  color: var(--c-muted);
  cursor: pointer;
  background: transparent;
  border: none;
  position: relative;
  transition: background var(--t),color var(--t);
}

.fg-09__cell:hover {
  background: rgba(255,255,255,.08);
  color: var(--c-text);
}

.fg-09__cell.other-month {
  opacity: .25;
  pointer-events: none;
}

.fg-09__cell.is-today {
  color: var(--c-text);
  box-shadow: 0 0 0 2px var(--c-a);
}

.fg-09__cell.is-sel {
  background: rgba(99,102,241,.25);
  color: var(--c-text);
  box-shadow: 0 0 0 1px rgba(99,102,241,.5);
}

.fg-09__cell.is-today.is-sel {
  background: rgba(99,102,241,.35);
}

.fg-09__dot {
  position: absolute;
  bottom: 3px;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--c-a);
}

.fg-09__events-hd {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .5px;
  text-transform: uppercase;
  color: var(--c-muted);
  margin-bottom: 10px;
}

.fg-09__events {
  display: flex;
  flex-direction: column;
  gap: 7px;
  min-height: 60px;
}

.fg-09__ev {
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 10px;
  padding: 9px 12px;
  border-left-width: 3px;
}

.fg-09__ev-time {
  font-size: 11px;
  font-weight: 700;
  color: var(--c-muted);
  white-space: nowrap;
  min-width: 42px;
}

.fg-09__ev-name {
  font-size: 12px;
  font-weight: 600;
  color: var(--c-text);
}

.fg-09__ev-none {
  font-size: 12px;
  color: var(--c-muted);
  text-align: center;
  padding: 12px 0;
  opacity: .6;
}

@media (prefers-reduced-motion: reduce) {
  .fg-09__glow {
    animation: none;
  }

  .fg-09__cell,
    .fg-09__nav {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-14');
  if(!r)return;
  var MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];
  var now=new Date();
  var cur={y:now.getFullYear(),m:now.getMonth()};
  var today={y:now.getFullYear(),m:now.getMonth(),d:now.getDate()};
  var sel={y:today.y,m:today.m,d:today.d};
  var EVENTS={};
  (function(){
    var y=today.y,m=String(today.m+1).padStart(2,'0');
    EVENTS[y+'-'+m+'-'+String(today.d).padStart(2,'0')]=[{t:'9:00 AM',n:'Team Standup',c:'#6366f1'},{t:'2:30 PM',n:'Design Review',c:'#8b5cf6'}];
    var nd=new Date(today.y,today.m,today.d+2);
    var nm=String(nd.getMonth()+1).padStart(2,'0');
    EVENTS[nd.getFullYear()+'-'+nm+'-'+String(nd.getDate()).padStart(2,'0')]=[{t:'11:00 AM',n:'Client Sync',c:'#10b981'},{t:'4:00 PM',n:'Sprint Retro',c:'#f59e0b'}];
    var nd2=new Date(today.y,today.m,today.d+5);
    var nm2=String(nd2.getMonth()+1).padStart(2,'0');
    EVENTS[nd2.getFullYear()+'-'+nm2+'-'+String(nd2.getDate()).padStart(2,'0')]=[{t:'10:00 AM',n:'Product Demo',c:'#ec4899'}];
  })();
  var grid=r.querySelector('#fg-14-grid');
  var evs=r.querySelector('#fg-14-events');
  var mEl=r.querySelector('#fg-14-month');
  var yEl=r.querySelector('#fg-14-year');
  function key(y,m,d){return y+'-'+String(m+1).padStart(2,'0')+'-'+String(d).padStart(2,'0')}
  function render(){
    mEl.textContent=MONTHS[cur.m];yEl.textContent=cur.y;
    grid.innerHTML='';
    var first=new Date(cur.y,cur.m,1).getDay();
    var days=new Date(cur.y,cur.m+1,0).getDate();
    var prevDays=new Date(cur.y,cur.m,0).getDate();
    for(var i=0;i<first;i++){var b=document.createElement('button');b.className='fg-09__cell other-month';b.textContent=prevDays-first+1+i;grid.appendChild(b)}
    for(var d=1;d<=days;d++){
      var c=document.createElement('button');
      c.className='fg-09__cell';c.textContent=d;
      c.setAttribute('aria-label',MONTHS[cur.m]+' '+d+', '+cur.y);
      var k=key(cur.y,cur.m,d);
      if(cur.y===today.y&&cur.m===today.m&&d===today.d)c.classList.add('is-today');
      if(cur.y===sel.y&&cur.m===sel.m&&d===sel.d)c.classList.add('is-sel');
      if(EVENTS[k]){var dot=document.createElement('span');dot.className='fg-09__dot';dot.style.background=EVENTS[k][0].c;c.appendChild(dot)}
      c.addEventListener('click',(function(dd){return function(){sel={y:cur.y,m:cur.m,d:dd};render()}})(d));
      grid.appendChild(c);
    }
    var total=first+days;var trailing=(7-total%7)%7;
    for(var i=0;i<trailing;i++){var b=document.createElement('button');b.className='fg-09__cell other-month';b.textContent=i+1;grid.appendChild(b)}
    renderEvents();
  }
  function renderEvents(){
    evs.innerHTML='';
    var k=key(sel.y,sel.m,sel.d);
    var list=EVENTS[k];
    if(!list||!list.length){var n=document.createElement('p');n.className='fg-09__ev-none';n.textContent='No events for this day';evs.appendChild(n);return}
    list.forEach(function(ev){
      var d=document.createElement('div');d.className='fg-09__ev';d.style.borderLeftColor=ev.c;
      d.innerHTML='<span class="fg-09__ev-time">'+ev.t+'</span><span class="fg-09__ev-name">'+ev.n+'</span>';
      evs.appendChild(d);
    });
  }
  r.querySelector('#fg-14-prev').addEventListener('click',function(){if(cur.m===0){cur.m=11;cur.y--}else cur.m--;render()});
  r.querySelector('#fg-14-next').addEventListener('click',function(){if(cur.m===11){cur.m=0;cur.y++}else cur.m++;render()});
  render();
})();
```
