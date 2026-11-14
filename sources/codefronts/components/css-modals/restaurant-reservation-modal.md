---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/restaurant-reservation-modal/"
title: "Restaurant Reservation Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A restaurant reservation booking modal (OpenTable/Resy-inspired) with a signature Origami Fan Deploy entrance — three horizontal panels (date, time, party…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Restaurant Reservation Modal
Source: https://codefronts.com/components/css-modals/restaurant-reservation-modal/

A restaurant reservation booking modal (OpenTable/Resy-inspired) with a signature Origami Fan Deploy entrance — three horizontal panels (date, time, party size) cascade in from top like origami fans unfolding. Warm hospitality palette (cream + burgundy + gold accents), date picker + time slot grid + party size selector + Reserve CTA. Medium intensity — hospitality contexts warrant warmth and theater without frivolity.
## HTML
```html
<div class="md-14">
  <button class="md-14__trigger" id="md-14-open">Reserve a table</button>
  <div class="md-14__backdrop" id="md-14-dialog" role="dialog" aria-modal="true" aria-labelledby="md-14-title">
    <div class="md-14__stage">
      <div class="md-14__modal">
        <button class="md-14__x md-14__close" aria-label="Close">✕</button>
        <div class="md-14__header">
          <p class="md-14__eyebrow">Osteria Bellini</p>
          <h2 class="md-14__title" id="md-14-title">Reserve your table</h2>
        </div>
        <div class="md-14__panel">
          <h3>Choose a date</h3>
          <div class="md-14__dates" role="radiogroup" aria-label="Date">
            <button class="md-14__date" role="radio" aria-checked="false"><span>Thu</span><strong>28</strong></button>
            <button class="md-14__date md-14__date--sel" role="radio" aria-checked="true"><span>Fri</span><strong>29</strong></button>
            <button class="md-14__date" role="radio" aria-checked="false"><span>Sat</span><strong>30</strong></button>
            <button class="md-14__date" role="radio" aria-checked="false"><span>Sun</span><strong>31</strong></button>
            <button class="md-14__date" role="radio" aria-checked="false"><span>Mon</span><strong>1</strong></button>
            <button class="md-14__date" role="radio" aria-checked="false"><span>Tue</span><strong>2</strong></button>
            <button class="md-14__date" role="radio" aria-checked="false"><span>Wed</span><strong>3</strong></button>
          </div>
        </div>
        <div class="md-14__panel">
          <h3>Choose a time</h3>
          <div class="md-14__times" role="radiogroup" aria-label="Time">
            <button class="md-14__time" role="radio" aria-checked="false">6:00 PM</button>
            <button class="md-14__time" role="radio" aria-checked="false">6:30 PM</button>
            <button class="md-14__time md-14__time--sel" role="radio" aria-checked="true">7:00 PM</button>
            <button class="md-14__time" role="radio" aria-checked="false">7:30 PM</button>
            <button class="md-14__time" role="radio" aria-checked="false">8:00 PM</button>
            <button class="md-14__time" role="radio" aria-checked="false">8:30 PM</button>
            <button class="md-14__time md-14__time--out" role="radio" aria-checked="false" disabled>9:00 PM</button>
            <button class="md-14__time" role="radio" aria-checked="false">9:30 PM</button>
          </div>
        </div>
        <div class="md-14__panel">
          <div class="md-14__party">
            <div>
              <h3>Party size</h3>
              <p>Larger parties call the maître d'</p>
            </div>
            <div class="md-14__party-picker" role="radiogroup" aria-label="Party size">
              <button role="radio" aria-checked="false">2</button>
              <button role="radio" aria-checked="false">3</button>
              <button role="radio" aria-checked="true" class="md-14__party-sel">4</button>
              <button role="radio" aria-checked="false">5</button>
              <button role="radio" aria-checked="false">6</button>
            </div>
          </div>
          <button class="md-14__cta md-14__close">Reserve · Fri Jul 29, 7:00 PM · Party of 4</button>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-14 {
  --page-bg: #f5efe0;
  --card: #faf6ec;
  --ink: #2a1a10;
  --sub: #6b5a45;
  --brand: #8b1a1a;
  --gold: #c9a961;
  --line: #e8dcc4;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(60% 100% at 50% 0%, rgba(139,26,26,.06) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-14 *,
.md-14 *::before,
.md-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-14 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-14__trigger {
  padding: 12px 26px;
  border: 1px solid var(--brand);
  border-radius: 6px;
  background: transparent;
  color: var(--brand);
  font-family: 'Playfair Display',Georgia,serif;
  font-size: .95rem;
  font-weight: 700;
  cursor: pointer;
  letter-spacing: .02em;
  transition: background .18s ease,color .18s ease;
}

.md-14__trigger:hover {
  background: var(--brand);
  color: var(--card);
}

.md-14__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(42,26,16,.55);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

.md-14__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .3s ease,visibility 0s linear 0s;
}

.md-14__stage {
  width: min(480px,100%);
  perspective: 1400px;
}

.md-14__modal {
  position: relative;
  padding: 0;
  border-radius: 14px;
  overflow: hidden;
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(42,26,16,.4);
  opacity: 0;
  transition: opacity .3s ease;
}

.md-14__backdrop.is-open .md-14__modal {
  opacity: 1;
}

.md-14__x {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 2;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 8px;
  background: rgba(255,255,255,.6);
  color: var(--sub);
  font-family: inherit;
  font-size: 15px;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-14__x:hover {
  background: #fff;
  color: var(--ink);
}

.md-14__header {
  padding: 26px 28px 20px;
  text-align: center;
  border-bottom: 1px solid var(--line);
}

.md-14__eyebrow {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 6px;
}

.md-14__title {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.15;
}
/* Signature entrance: Origami Fan Deploy — panels cascade from top */

.md-14__panel {
  padding: 20px 28px;
  border-bottom: 1px solid var(--line);
  opacity: 0;
  transform: rotateX(-90deg);
  transform-origin: top center;
  backface-visibility: hidden;
}

.md-14__panel:last-of-type {
  border-bottom: none;
}

.md-14__backdrop.is-open .md-14__panel {
  animation: md-14-fan .5s cubic-bezier(.22,1,.36,1) forwards;
}

.md-14__backdrop.is-open .md-14__panel:nth-of-type(1) {
  animation-delay: .15s;
}

.md-14__backdrop.is-open .md-14__panel:nth-of-type(2) {
  animation-delay: .32s;
}

.md-14__backdrop.is-open .md-14__panel:nth-of-type(3) {
  animation-delay: .49s;
}

@keyframes md-14-fan {
  to {
    opacity: 1;
    transform: rotateX(0);
  }
}

.md-14__panel h3 {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 12px;
}

.md-14__dates {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding-bottom: 2px;
}

.md-14__date {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 52px;
  padding: 8px 10px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  cursor: pointer;
  font-family: inherit;
  transition: border-color .18s ease,background .18s ease,color .18s ease;
}

.md-14__date span {
  font-size: .66rem;
  font-weight: 600;
  color: var(--sub);
  text-transform: uppercase;
  letter-spacing: .04em;
  margin-bottom: 2px;
}

.md-14__date strong {
  font-size: 1rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.md-14__date:hover {
  border-color: var(--brand);
}

.md-14__date--sel {
  background: var(--brand);
  border-color: var(--brand);
  color: #fff;
}

.md-14__date--sel span {
  color: rgba(255,255,255,.8);
}

.md-14__times {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 6px;
}

@media (max-width: 400px) {
  .md-14__times {
    grid-template-columns: repeat(3,1fr);
  }
}

.md-14__time {
  padding: 9px 6px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #fff;
  color: var(--ink);
  font-family: inherit;
  font-size: .78rem;
  font-weight: 600;
  cursor: pointer;
  transition: border-color .18s ease,background .18s ease,color .18s ease;
}

.md-14__time:hover:not(:disabled) {
  border-color: var(--brand);
}

.md-14__time--sel {
  background: var(--brand);
  border-color: var(--brand);
  color: #fff;
}

.md-14__time--out {
  opacity: .35;
  text-decoration: line-through;
  cursor: not-allowed;
}

.md-14__party {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  margin-bottom: 16px;
}

.md-14__party > div:first-child p {
  font-size: .72rem;
  color: var(--sub);
  margin-top: 3px;
}

.md-14__party-picker {
  display: flex;
  gap: 5px;
}

.md-14__party-picker button {
  width: 34px;
  height: 34px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #fff;
  color: var(--ink);
  font-family: inherit;
  font-size: .85rem;
  font-weight: 700;
  cursor: pointer;
  transition: border-color .18s ease,background .18s ease,color .18s ease;
}

.md-14__party-picker button:hover {
  border-color: var(--brand);
}

.md-14__party-sel {
  background: var(--brand)!important;
  border-color: var(--brand)!important;
  color: #fff!important;
}

.md-14__cta {
  width: 100%;
  padding: 14px 20px;
  border: none;
  border-radius: 8px;
  background: var(--ink);
  color: var(--card);
  font-family: inherit;
  font-size: .85rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
}

.md-14__cta:hover {
  background: #000;
  transform: translateY(-1px);
}

.md-14__cta:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .md-14__backdrop,
    .md-14__modal,
    .md-14__panel {
    transition: opacity .2s ease!important;
    animation: none!important;
  }

  .md-14__panel {
    opacity: 1!important;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-14');
  if (!root) return;
  var openBtn = root.querySelector('#md-14-open');
  var dialog = root.querySelector('#md-14-dialog');
  var closeBtns = root.querySelectorAll('.md-14__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus selected date chip — users start by confirming or changing date
    var date = dialog.querySelector('.md-14__date--sel');
    if (date) date.focus();
    document.addEventListener('keydown', onKey);
  }
  function close() {
    dialog.classList.remove('is-open');
    document.documentElement.style.overflow = '';
    document.removeEventListener('keydown', onKey);
    if (lastFocus) lastFocus.focus();
  }
  function onKey(e) { if (e.key === 'Escape') close(); }

  openBtn.addEventListener('click', open);
  closeBtns.forEach(function(b){ b.addEventListener('click', close); });
  dialog.addEventListener('click', function(e){ if (e.target === dialog) close(); });
})();
```
