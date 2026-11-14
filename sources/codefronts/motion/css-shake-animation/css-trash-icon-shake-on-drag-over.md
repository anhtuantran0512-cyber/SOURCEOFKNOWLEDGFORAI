---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-trash-icon-shake-on-drag-over/"
title: "CSS Trash Icon Shake on Drag Over"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The hungriest trash can on the web: drag a file chip over the drop zone and the lid swings open while the can rattles in anticipation; drop, and the chip is…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Trash Icon Shake on Drag Over
Source: https://codefronts.com/motion/css-shake-animation/css-trash-icon-shake-on-drag-over/

The hungriest trash can on the web: drag a file chip over the drop zone and the lid swings open while the can rattles in anticipation; drop, and the chip is swallowed with a gulp squash. Plus a list variant where hovering a row's delete button flaps the lid — a one-hover preview of what the click will do.
## HTML
```html
<div class="shk-21-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-21a" aria-label="Drag files onto a trash can that opens and rattles">
  <div class="shk-21a__desk">
    <div class="shk-21a__files" id="shk-21a-files">
      <div class="shk-21a__chip" draggable="true" tabindex="0">draft-v1.fig</div>
      <div class="shk-21a__chip" draggable="true" tabindex="0">notes-old.md</div>
      <div class="shk-21a__chip" draggable="true" tabindex="0">unused.png</div>
    </div>
    <div class="shk-21a__zone" id="shk-21a-zone" aria-label="Delete drop zone">
      <svg class="shk-21a__can" viewBox="0 0 48 48" aria-hidden="true">
        <g class="shk-21a__lid"><rect x="10" y="10" width="28" height="5" rx="2.5" fill="currentColor"></rect><rect x="19" y="5.5" width="10" height="5" rx="2" fill="currentColor"></rect></g>
        <g class="shk-21a__body"><path d="M13 18h22l-1.8 21a3 3 0 0 1-3 2.8H17.8a3 3 0 0 1-3-2.8z" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linejoin="round"></path><line x1="20" y1="24" x2="20.6" y2="35" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"></line><line x1="28" y1="24" x2="27.4" y2="35" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"></line></g>
      </svg>
      <p class="shk-21a__label" id="shk-21a-label">Drag here to delete</p>
    </div>
  </div>
  <p class="shk-21a__hint" aria-hidden="true">lid transitions open (state) · can rattles (anticipation) · drop gulps (payoff)</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-21b" aria-label="List rows whose trash button flaps its lid on hover">
  <div class="shk-21b__panel">
    <p class="shk-21b__head">Uploads</p>
    <ul class="shk-21b__list" id="shk-21b-list">
      <li class="shk-21b__row"><span class="shk-21b__dot" style="--c:oklch(0.75 0.14 250)" aria-hidden="true"></span><span class="shk-21b__name">hero-final-FINAL.webp</span><span class="shk-21b__size">1.2 MB</span><button class="shk-21b__del" type="button" aria-label="Delete hero-final-FINAL.webp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><g class="shk-21b__lid"><path d="M3 6h18"></path><path d="M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2"></path></g><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg></button></li>
      <li class="shk-21b__row"><span class="shk-21b__dot" style="--c:oklch(0.78 0.14 85)" aria-hidden="true"></span><span class="shk-21b__name">brand-tokens.json</span><span class="shk-21b__size">18 KB</span><button class="shk-21b__del" type="button" aria-label="Delete brand-tokens.json"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><g class="shk-21b__lid"><path d="M3 6h18"></path><path d="M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2"></path></g><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg></button></li>
      <li class="shk-21b__row"><span class="shk-21b__dot" style="--c:oklch(0.72 0.16 340)" aria-hidden="true"></span><span class="shk-21b__name">interview-notes.pdf</span><span class="shk-21b__size">640 KB</span><button class="shk-21b__del" type="button" aria-label="Delete interview-notes.pdf"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><g class="shk-21b__lid"><path d="M3 6h18"></path><path d="M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2"></path></g><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg></button></li>
    </ul>
    <p class="shk-21b__hint" aria-hidden="true">hover a trash button — the lid flaps a preview; click removes the row</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-21-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-21-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-21a,
.shk-21a *,
.shk-21a *::before,
.shk-21a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-21a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 22px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f5f4f1,#e9e7e1);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-21a__desk {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 56px;
}

.shk-21a__files {
  display: grid;
  gap: 12px;
}

.shk-21a__chip {
  padding: 13px 20px;
  background: #fff;
  border: 1.5px solid rgba(32,30,26,.16);
  border-radius: 12px;
  font-size: 14px;
  font-weight: 600;
  color: #201e1a;
  cursor: grab;
  box-shadow: 0 8px 18px -10px rgba(32,30,26,.35);
  transition: opacity .3s,scale .3s,box-shadow .2s;
  user-select: none;
}

.shk-21a__chip:hover {
  box-shadow: 0 12px 22px -10px rgba(32,30,26,.45);
}

.shk-21a__chip:active {
  cursor: grabbing;
}

.shk-21a__chip.is-gone {
  opacity: 0;
  scale: .6;
  pointer-events: none;
}

.shk-21a__zone {
  display: grid;
  justify-items: center;
  gap: 12px;
  padding: 34px 42px;
  border: 2.5px dashed rgba(32,30,26,.3);
  border-radius: 22px;
  color: #201e1a;
  transition: border-color .25s,background .25s,color .25s;
}

.shk-21a__zone.is-hungry {
  border-color: oklch(0.6 0.21 25);
  background: oklch(0.6 0.21 25 / .07);
  color: oklch(0.52 0.2 25);
}

.shk-21a__zone * {
  pointer-events: none;
}

.shk-21a__can {
  width: 60px;
  height: 60px;
  overflow: visible;
}

.shk-21a__lid {
  transform-origin: 10px 12px;
  transform-box: view-box;
  transition: rotate .28s cubic-bezier(.34,1.4,.64,1),translate .28s cubic-bezier(.34,1.4,.64,1);
}

.shk-21a__zone.is-hungry .shk-21a__lid {
  rotate: -28deg;
  translate: -3px -7px;
}

.shk-21a__zone.is-hungry .shk-21a__body {
  animation: shk-21a-rattle .4s ease-in-out infinite;
}

.shk-21a__zone.is-gulping .shk-21a__can {
  animation: shk-21a-gulp .5s cubic-bezier(.34,1.56,.64,1);
}

.shk-21a__label {
  font-size: 13px;
  font-weight: 700;
}

.shk-21a__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(32,30,26,.5);
}

@keyframes shk-21a-rattle {
  0%,
    100% {
    translate: 0 0;
    rotate: 0deg;
  }

  25% {
    translate: -1.5px 0;
    rotate: -2.5deg;
  }

  75% {
    translate: 1.5px 0;
    rotate: 2.5deg;
  }
}

@keyframes shk-21a-gulp {
  0% {
    scale: 1 1;
  }

  30% {
    scale: 1.15 .82;
  }

  60% {
    scale: .94 1.08;
  }

  100% {
    scale: 1 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-21a__zone.is-hungry .shk-21a__body,
    .shk-21a__zone.is-gulping .shk-21a__can {
    animation: none;
  }
}

.shk-21b,
.shk-21b *,
.shk-21b *::before,
.shk-21b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-21b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,#12141a,#0c0e12);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-21b__panel {
  width: min(460px,100%);
  padding: 24px;
  border-radius: 18px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(165,185,220,.14);
  box-shadow: 0 40px 80px -45px rgba(0,0,0,.95);
}

.shk-21b__head {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(220,230,248,.55);
  padding: 0 6px 12px;
}

.shk-21b__list {
  list-style: none;
  display: grid;
  gap: 8px;
}

.shk-21b__row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  background: rgba(8,10,15,.5);
  border: 1px solid rgba(165,185,220,.12);
  border-radius: 12px;
  transition: opacity .35s,translate .35s,scale .35s;
}

.shk-21b__row.is-going {
  opacity: 0;
  translate: 24px 0;
  scale: .96;
}

.shk-21b__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--c);
}

.shk-21b__name {
  flex: 1;
  font-size: 14px;
  font-weight: 600;
  color: #e6ecf8;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.shk-21b__size {
  font-size: 12px;
  color: rgba(220,230,248,.45);
}

.shk-21b__del {
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 9px;
  background: transparent;
  color: rgba(220,230,248,.55);
  cursor: pointer;
  transition: background .15s,color .15s;
}

.shk-21b__del svg {
  width: 18px;
  height: 18px;
  overflow: visible;
}

.shk-21b__del:hover {
  background: oklch(0.6 0.21 25 / .15);
  color: oklch(0.78 0.14 25);
}

.shk-21b__lid {
  transform-origin: 12px 5px;
  transform-box: view-box;
}

.shk-21b__del:hover .shk-21b__lid {
  animation: shk-21b-flap .6s ease-in-out infinite;
}

.shk-21b__del:focus-visible {
  outline: 2px solid oklch(0.78 0.14 25);
  outline-offset: 2px;
}

.shk-21b__hint {
  padding: 14px 6px 0;
  font-size: 11.5px;
  color: rgba(220,230,248,.4);
}

@keyframes shk-21b-flap {
  0%,
    100% {
    rotate: 0deg;
    translate: 0 0;
  }

  30% {
    rotate: -14deg;
    translate: -1px -2px;
  }

  60% {
    rotate: -6deg;
    translate: -.5px -1px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-21b__del:hover .shk-21b__lid {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var zone=document.getElementById('shk-21a-zone'),files=document.getElementById('shk-21a-files'),
      label=document.getElementById('shk-21a-label'); if(!zone) return;
  var dragged=null,depth=0,eaten=0;
  files.addEventListener('dragstart',function(e){ dragged=e.target.closest('.shk-21a__chip'); if(e.dataTransfer) e.dataTransfer.effectAllowed='move'; });
  files.addEventListener('dragend',function(){ dragged=null; depth=0; zone.classList.remove('is-hungry'); });
  zone.addEventListener('dragenter',function(){ depth++; zone.classList.add('is-hungry'); });
  zone.addEventListener('dragleave',function(){ if(--depth<=0){ depth=0; zone.classList.remove('is-hungry'); } });
  zone.addEventListener('dragover',function(e){ e.preventDefault(); });      // without this, drop never fires
  zone.addEventListener('animationend',function(){ zone.classList.remove('is-gulping'); });
  zone.addEventListener('drop',function(e){
    e.preventDefault(); depth=0; zone.classList.remove('is-hungry');
    if(!dragged) return;
    dragged.classList.add('is-gone');                                        // chip fades first…
    zone.classList.add('is-gulping');                                        // …then the can gulps
    eaten++; label.textContent=eaten+(eaten===1?' file':' files')+' deleted';
  });
})();

(function(){
  var list=document.getElementById('shk-21b-list'); if(!list) return;
  list.addEventListener('click',function(e){
    var btn=e.target.closest('.shk-21b__del'); if(!btn) return;
    var row=btn.closest('.shk-21b__row');
    row.classList.add('is-going');
    row.addEventListener('transitionend',function once(){ row.remove(); },{once:true});
  });
})();
```
