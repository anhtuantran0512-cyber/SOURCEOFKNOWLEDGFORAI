---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/vintage-skeuomorphic-paper-torn-tear-off-design/"
title: "Vintage Skeuomorphic / Paper-Torn Tear-off Design"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A realistic desk tear-off pad on a wood-grain wall."
has_js: "true"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vintage Skeuomorphic / Paper-Torn Tear-off Design
Source: https://codefronts.com/components/css-calendar-designs/vintage-skeuomorphic-paper-torn-tear-off-design/

A realistic desk tear-off pad on a wood-grain wall. Metal binding with 3D rings, paper depth via gradients and ruled lines, a stacked-page look, and a jagged torn bottom edge built with CSS mask. Giant serif date, typewriter weekday, and a tear-off page-rip animation.
## HTML
```html
<div class="cal24">
  <div class="cal24__pad">

    <div class="cal24__binding">
      <div class="cal24__ring"></div>
      <div class="cal24__ring"></div>
      <div class="cal24__ring"></div>
      <div class="cal24__ring"></div>
      <div class="cal24__ring"></div>
    </div>

    <div class="cal24__stack">
      <div class="cal24__page" id="cal24Page">
        <div class="cal24__top">
          <div class="cal24__month">June</div>
          <div class="cal24__year">2026</div>
        </div>

        <div class="cal24__bignum" id="cal24Num">8</div>
        <div class="cal24__weekday" id="cal24Day">Sunday</div>

        <div class="cal24__stamps">
          <div class="cal24__stamp">Sprint 10AM</div>
          <div class="cal24__stamp">Launch 2PM</div>
          <div class="cal24__stamp">Review 4PM</div>
        </div>

        <div class="cal24__note">— day 159 of 365 · 207 remaining —</div>
      </div>
    </div>

    <div class="cal24__controls">
      <button class="cal24__btn cal24__btn--ghost" id="cal24Prev">‹ Yesterday</button>
      <button class="cal24__btn" id="cal24Tear">Tear off ✂</button>
    </div>

  </div>
</div>
```
## CSS
```css
.cal24,
.cal24 *,
.cal24 *::before,
.cal24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal24 ::selection {
  background: #b23a2e;
  color: #fff;
}

.cal24 {
  --wood: #6b4f3a;
  --wood2: #543d2c;
  --paper: #f5f0e3;
  --paper2: #ebe3d0;
  --ink: #2b2620;
  --red: #b23a2e;
  --red-d: #8a2c22;
  --gold: #b8923f;
  --shadow: rgba(0,0,0,0.3);
  font-family: 'Oswald', sans-serif;
  background: repeating-linear-gradient(90deg, var(--wood) 0px, var(--wood) 38px, var(--wood2) 38px, var(--wood2) 40px), var(--wood);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

@keyframes cal24-in {
  from {
    opacity: 0;
    transform: translateY(-20px) rotate(-1deg);
  }

  to {
    opacity: 1;
    transform: translateY(0) rotate(0);
  }
}

@keyframes cal24-tear {
  0% {
    transform: rotate(0) translateY(0);
    opacity: 1;
  }

  40% {
    transform: rotate(-6deg) translateY(8px);
  }

  100% {
    transform: rotate(-14deg) translateY(420px) translateX(-60px);
    opacity: 0;
  }
}

@keyframes cal24-flutter {
  0%,
    100% {
    transform: rotate(0deg);
  }

  50% {
    transform: rotate(0.6deg);
  }
}

.cal24__pad {
  position: relative;
  width: 340px;
  animation: cal24-in 0.6s cubic-bezier(0.34,1.3,0.64,1) both;
}
/* The metal binding at top */

.cal24__binding {
  position: relative;
  height: 34px;
  background: linear-gradient(180deg, #c9c9cf 0%, #8e8e96 50%, #6a6a72 100%);
  border-radius: 8px 8px 0 0;
  box-shadow: inset 0 2px 3px rgba(255,255,255,0.5), 0 3px 6px var(--shadow);
  display: flex;
  justify-content: space-around;
  align-items: flex-end;
  padding: 0 24px 0;
  z-index: 5;
}
/* binding rings */

.cal24__ring {
  width: 14px;
  height: 26px;
  background: linear-gradient(180deg, #5a5a62, #2e2e34);
  border-radius: 7px;
  margin-bottom: -13px;
  box-shadow: inset 0 1px 1px rgba(255,255,255,0.3), 0 2px 3px rgba(0,0,0,0.4);
  position: relative;
  z-index: 6;
}
/* Stacked pages behind (depth) */

.cal24__stack {
  position: relative;
}

.cal24__stack::before,
.cal24__stack::after {
  content: '';
  position: absolute;
  left: 4px;
  right: 4px;
  background: var(--paper2);
  border-radius: 0 0 3px 3px;
}

.cal24__stack::before {
  top: 6px;
  bottom: -6px;
  box-shadow: 0 6px 10px var(--shadow);
}

.cal24__stack::after {
  top: 3px;
  bottom: -3px;
  background: #f0ead9;
}
/* ── The top (current) page ── */

.cal24__page {
  position: relative;
  z-index: 3;
  background: var(--paper);
  background-image: radial-gradient(circle at 50% 0%, rgba(255,255,255,0.6), transparent 60%), repeating-linear-gradient(0deg, transparent 0 27px, rgba(43,38,32,0.04) 27px 28px);
  padding: 18px 24px 0;
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
  animation: cal24-flutter 5s ease-in-out infinite;
  /* Torn bottom edge via mask */
  -webkit-mask: linear-gradient(#000 0 0) top/100% calc(100% - 14px) no-repeat, radial-gradient(circle at 8px -2px, transparent 7px, #000 8px) bottom left/16px 14px repeat-x;
  mask: linear-gradient(#000 0 0) top/100% calc(100% - 14px) no-repeat, radial-gradient(circle at 8px -2px, transparent 7px, #000 8px) bottom left/16px 14px repeat-x;
  padding-bottom: 22px;
}
/* Header row: month + year */

.cal24__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 2px solid var(--ink);
  padding-bottom: 8px;
}

.cal24__month {
  font-family: 'Oswald', sans-serif;
  font-weight: 700;
  font-size: 26px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--red);
}

.cal24__year {
  font-family: 'Special Elite', monospace;
  font-size: 15px;
  color: var(--ink);
}
/* The giant date numeral */

.cal24__bignum {
  font-family: 'Playfair Display', serif;
  font-weight: 900;
  font-size: 150px;
  line-height: 0.9;
  text-align: center;
  color: var(--ink);
  margin: 6px 0 -4px;
  text-shadow: 1px 1px 0 rgba(255,255,255,0.6), 3px 3px 5px rgba(0,0,0,0.12);
}

.cal24__weekday {
  text-align: center;
  font-family: 'Special Elite', monospace;
  font-size: 20px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--red);
  padding-left: 0.3em;
}

.cal24__note {
  text-align: center;
  font-family: 'Special Elite', monospace;
  font-size: 11px;
  color: var(--ink);
  opacity: 0.6;
  margin-top: 8px;
  letter-spacing: 0.05em;
}
/* tiny event stamps */

.cal24__stamps {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin: 12px 0 4px;
}

.cal24__stamp {
  font-family: 'Special Elite', monospace;
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border: 1px solid var(--red);
  color: var(--red);
  padding: 3px 7px;
  border-radius: 2px;
  transform: rotate(-2deg);
  opacity: 0.85;
}

.cal24__stamp:nth-child(2) {
  transform: rotate(1.5deg);
  border-color: var(--gold);
  color: var(--gold);
}

.cal24__stamp:nth-child(3) {
  transform: rotate(-1deg);
  border-color: var(--ink);
  color: var(--ink);
}
/* ── Tear-off button ── */

.cal24__controls {
  position: relative;
  z-index: 4;
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-top: 22px;
}

.cal24__btn {
  font-family: 'Oswald', sans-serif;
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 10px 18px;
  border-radius: 4px;
  cursor: pointer;
  border: none;
  transition: all 0.15s;
  user-select: none;
  box-shadow: 0 3px 0 var(--red-d), 0 5px 8px rgba(0,0,0,0.3);
  background: var(--red);
  color: var(--paper);
}

.cal24__btn:active {
  transform: translateY(3px);
  box-shadow: 0 0 0 var(--red-d), 0 2px 4px rgba(0,0,0,0.3);
}

.cal24__btn--ghost {
  background: var(--paper);
  color: var(--ink);
  box-shadow: 0 3px 0 #c9bfa6, 0 5px 8px rgba(0,0,0,0.25);
}

.cal24__page.tearing {
  animation: cal24-tear 0.7s ease-in forwards;
}

@media (max-width: 400px) {
  .cal24__pad {
    width: 290px;
  }

  .cal24__bignum {
    font-size: 120px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal24 * {
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const page = document.getElementById('cal24Page');
  const num  = document.getElementById('cal24Num');
  const day  = document.getElementById('cal24Day');
  const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  let date = 8; // June 8 = Sunday (index 0)

  function render() {
    num.textContent = date;
    day.textContent = days[(date - 8 + 700) % 7];
  }

  document.getElementById('cal24Tear').addEventListener('click', () => {
    page.classList.add('tearing');
    setTimeout(() => {
      date = date >= 30 ? 1 : date + 1;
      render();
      page.classList.remove('tearing');
    }, 650);
  });
  document.getElementById('cal24Prev').addEventListener('click', () => {
    date = date <= 1 ? 30 : date - 1;
    render();
  });
})();
```
