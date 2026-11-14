---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/travel-postcard-diagonal-3d-flip-card/"
title: "Travel Postcard Diagonal 3D Flip Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A travel postcard that flips along the diagonal corner-to-corner axis — rotate3d(1,1,0,180deg) instead of the conventional rotateY spin."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Travel Postcard Diagonal 3D Flip Card
Source: https://codefronts.com/components/css-flip-cards/travel-postcard-diagonal-3d-flip-card/

A travel postcard that flips along the diagonal corner-to-corner axis — rotate3d(1,1,0,180deg) instead of the conventional rotateY spin.
## HTML
```html
<div class="fc-20">
  <div class="fc-20__scene">
    <div class="fc-20__card">
      <div class="fc-20__front">
        <div class="fc-20__sky">
          <svg width="100%" height="160" viewBox="0 0 360 160" preserveAspectRatio="none">
            <defs>
              <linearGradient id="fc-20-sky" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#f7c8a0"/>
                <stop offset="60%" stop-color="#f4a87d"/>
                <stop offset="100%" stop-color="#e88e6e"/>
              </linearGradient>
              <linearGradient id="fc-20-bldg" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#fef3c7"/>
                <stop offset="100%" stop-color="#fbbf24"/>
              </linearGradient>
            </defs>
            <rect width="360" height="160" fill="url(#fc-20-sky)"/>
            <circle cx="280" cy="48" r="22" fill="#fff3cf" opacity="0.85"/>
            <g fill="url(#fc-20-bldg)">
              <rect x="20" y="92" width="34" height="68"/>
              <polygon points="20,92 37,75 54,92"/>
              <rect x="64" y="100" width="42" height="60"/>
              <polygon points="64,100 85,80 106,100"/>
              <rect x="116" y="84" width="38" height="76"/>
              <polygon points="116,84 135,68 154,84"/>
              <rect x="164" y="96" width="46" height="64"/>
              <polygon points="164,96 187,76 210,96"/>
              <rect x="220" y="78" width="40" height="82"/>
              <polygon points="220,78 240,60 260,78"/>
              <rect x="270" y="100" width="34" height="60"/>
              <polygon points="270,100 287,82 304,100"/>
              <rect x="314" y="92" width="36" height="68"/>
              <polygon points="314,92 332,75 350,92"/>
            </g>
            <g fill="#0c0a07" opacity="0.6">
              <rect x="28" y="100" width="3" height="5"/><rect x="36" y="100" width="3" height="5"/><rect x="44" y="100" width="3" height="5"/>
              <rect x="28" y="115" width="3" height="5"/><rect x="36" y="115" width="3" height="5"/><rect x="44" y="115" width="3" height="5"/>
              <rect x="72" y="110" width="3" height="5"/><rect x="80" y="110" width="3" height="5"/><rect x="88" y="110" width="3" height="5"/>
              <rect x="124" y="92" width="3" height="5"/><rect x="132" y="92" width="3" height="5"/><rect x="142" y="92" width="3" height="5"/>
              <rect x="172" y="106" width="3" height="5"/><rect x="184" y="106" width="3" height="5"/><rect x="196" y="106" width="3" height="5"/>
              <rect x="228" y="90" width="3" height="5"/><rect x="240" y="90" width="3" height="5"/><rect x="252" y="90" width="3" height="5"/>
              <rect x="320" y="100" width="3" height="5"/><rect x="332" y="100" width="3" height="5"/><rect x="342" y="100" width="3" height="5"/>
            </g>
          </svg>
        </div>
        <div class="fc-20__title-block">
          <div class="fc-20__greetings">Greetings from</div>
          <div class="fc-20__city">Lisbon</div>
          <div class="fc-20__sub">Portugal · Postcards from the road</div>
        </div>
        <div class="fc-20__stamp">
          <span class="fc-20__stamp-fig">★</span>
          <span class="fc-20__stamp-text">Par<br>Avion</span>
        </div>
        <div class="fc-20__hint">Hover to read ›</div>
      </div>
      <div class="fc-20__back">
        <div class="fc-20__back-head">
          <span class="fc-20__back-eyebrow">Postcard · 02</span>
          <span class="fc-20__back-date">June 14</span>
        </div>
        <div class="fc-20__note">
          <p>Dear friend,</p>
          <p>The pastel buildings climb every hill and at sunset the whole city turns the colour of warm bread. I am drinking ginjinha in a paper cup and listening to a man play fado outside the cathedral.</p>
          <p>Wish you were here.</p>
          <p class="fc-20__signoff">— V.</p>
        </div>
        <div class="fc-20__address-block">
          <div class="fc-20__address-line"></div>
          <div class="fc-20__address-line"></div>
          <div class="fc-20__address-line"></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-20,
.fc-20 *,
.fc-20 *::before,
.fc-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-20 ::selection {
  background: #dc2626;
  color: #fff5e6;
}

.fc-20 {
  --bg: #f5f0e6;
  --ink: #3a2f24;
  --paper: #faf6ec;
  --paper-2: #fef9ec;
  --stamp-red: #dc2626;
  --airmail-blue: #1e40af;
  --accent: #c08552;
  --card-w: 360px;
  --card-h: 480px;
  font-family: Georgia,'Times New Roman',serif;
  background: repeating-linear-gradient(45deg,#f5f0e6,#f5f0e6 12px,#efe7d6 12px,#efe7d6 24px);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

.fc-20__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
}

.fc-20__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1s cubic-bezier(.4,0,.2,1);
}

.fc-20__scene:hover .fc-20__card {
  transform: rotate3d(1,1,0,180deg);
}

.fc-20__front,
.fc-20__back {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
  box-shadow: 0 18px 40px rgba(58,47,36,.25),0 4px 10px rgba(58,47,36,.12);
}
/* FRONT — sunset city */

.fc-20__front {
  background: var(--paper);
  border: 6px solid var(--paper);
  outline: 2px dashed rgba(58,47,36,.25);
  outline-offset: -12px;
  display: flex;
  flex-direction: column;
}

.fc-20__sky {
  width: 100%;
  height: 160px;
  flex-shrink: 0;
  border-bottom: 1px solid rgba(58,47,36,.15);
}

.fc-20__title-block {
  padding: 20px 24px 12px;
  text-align: center;
}

.fc-20__greetings {
  font-size: 13px;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 6px;
}

.fc-20__city {
  font-size: 46px;
  font-weight: 900;
  color: var(--ink);
  line-height: 1;
  letter-spacing: -.02em;
  font-style: italic;
  font-family: 'Brush Script MT','Lucida Handwriting',Georgia,cursive;
}

.fc-20__sub {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: rgba(58,47,36,.5);
  margin-top: 8px;
  font-family: Georgia,serif;
}

.fc-20__stamp {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 54px;
  height: 64px;
  border: 2px dashed var(--stamp-red);
  background: var(--paper-2);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  transform: rotate(6deg);
  box-shadow: 0 2px 4px rgba(58,47,36,.18);
}

.fc-20__stamp-fig {
  font-size: 18px;
  color: var(--stamp-red);
  line-height: 1;
}

.fc-20__stamp-text {
  font-size: 8px;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--stamp-red);
  font-weight: 700;
  line-height: 1.1;
  text-align: center;
}

.fc-20__hint {
  margin-top: auto;
  padding: 14px 24px;
  text-align: center;
  font-size: 10px;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: rgba(58,47,36,.45);
  font-family: Georgia,serif;
  font-style: italic;
}
/* BACK — handwritten note */

.fc-20__back {
  background: var(--paper-2);
  transform: rotate3d(1,1,0,180deg);
  display: flex;
  flex-direction: column;
  padding: 24px 26px;
  border: 6px solid var(--paper-2);
}

.fc-20__back::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 1px;
  background: repeating-linear-gradient(to bottom,rgba(220,38,38,.35) 0 4px,transparent 4px 10px);
  pointer-events: none;
}

.fc-20__back::after {
  content: '';
  position: absolute;
  top: 8px;
  left: 8px;
  right: 8px;
  bottom: 8px;
  border: 2px solid transparent;
  background: repeating-linear-gradient(45deg,var(--airmail-blue) 0 8px,transparent 8px 16px,var(--stamp-red) 16px 24px,transparent 24px 32px);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  padding: 0;
  opacity: .5;
  pointer-events: none;
}

.fc-20__back-head {
  display: flex;
  justify-content: space-between;
  font-size: 10px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(58,47,36,.55);
  margin-bottom: 12px;
  font-family: Georgia,serif;
}

.fc-20__back-eyebrow {
  font-weight: 700;
  color: var(--accent);
}

.fc-20__note {
  flex: 1;
  padding-right: 18px;
  font-family: 'Brush Script MT','Lucida Handwriting','Snell Roundhand',cursive;
  color: var(--ink);
  font-size: 17px;
  line-height: 1.5;
}

.fc-20__note p {
  margin-bottom: 8px;
}

.fc-20__signoff {
  margin-top: 10px;
  font-size: 18px;
}

.fc-20__address-block {
  position: absolute;
  right: 22px;
  bottom: 22px;
  width: 42%;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.fc-20__address-line {
  height: 1px;
  background: rgba(58,47,36,.3);
}

@media (prefers-reduced-motion: reduce) {
  .fc-20__card {
    transition: none;
  }

  .fc-20__scene:hover .fc-20__card {
    transform: none;
  }

  .fc-20__scene:hover .fc-20__front {
    opacity: 0;
  }

  .fc-20__scene:hover .fc-20__back {
    transform: rotate3d(1,1,0,0);
  }
}
```
