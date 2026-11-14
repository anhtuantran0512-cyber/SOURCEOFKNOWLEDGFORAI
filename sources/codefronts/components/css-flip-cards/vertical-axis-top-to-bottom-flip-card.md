---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/vertical-axis-top-to-bottom-flip-card/"
title: "Vertical Axis Top-to-Bottom Flip Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A layout variation using rotateX instead of rotateY to produce a top-to-bottom vertical card-flip interaction."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Axis Top-to-Bottom Flip Card
Source: https://codefronts.com/components/css-flip-cards/vertical-axis-top-to-bottom-flip-card/

A layout variation using rotateX instead of rotateY to produce a top-to-bottom vertical card-flip interaction.
## HTML
```html
<div class="fc-15">
  <div class="fc-15__heading">
    <h2>Vertical Axis (rotateX) Flip</h2>
    <p>Card flips top-to-bottom instead of side-to-side</p>
    <div class="fc-15__code-tag">transform: rotateX(180deg)</div>
  </div>
  <div class="fc-15__scene">
    <div class="fc-15__card">
      <div class="fc-15__front">
        <div class="fc-15__icon-box">
          <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
        </div>
        <div class="fc-15__front-text">
          <div class="fc-15__front-label">Feature · Flip Axis</div>
          <div class="fc-15__front-title">Vertical Card Flip</div>
          <div class="fc-15__front-sub">Hover to flip top-to-bottom via rotateX</div>
        </div>
        <div class="fc-15__axis-arrow">
          <span>▲</span>
          <span style="writing-mode:vertical-rl;letter-spacing:0">flip</span>
          <span>▼</span>
        </div>
      </div>
      <div class="fc-15__back">
        <div class="fc-15__back-icon">✅</div>
        <div>
          <div class="fc-15__back-label">Back Face · Revealed</div>
          <div class="fc-15__back-title">rotateX Flip Complete</div>
          <div class="fc-15__pill-list">
            <span class="fc-15__pill">rotateX(180deg)</span>
            <span class="fc-15__pill">backface-visibility:hidden</span>
            <span class="fc-15__pill">perspective:1200px</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-15,
.fc-15 *,
.fc-15 *::before,
.fc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-15 ::selection {
  background: #0d9488;
  color: #fff;
}

.fc-15 {
  --bg: #04100e;
  --teal: #0d9488;
  --emerald: #10b981;
  --white: #f0fdf4;
  --card-w: 360px;
  --card-h: 240px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 50%,#061a16,#04100e 65%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 20px;
  color: var(--white);
}

.fc-15__heading {
  text-align: center;
}

.fc-15__heading h2 {
  font-size: 18px;
  font-weight: 800;
  color: var(--white);
}

.fc-15__heading p {
  font-size: 12px;
  color: rgba(240,253,244,.4);
  margin-top: 4px;
}

.fc-15__code-tag {
  display: inline-block;
  font-family: 'Courier New',monospace;
  font-size: 11px;
  background: rgba(13,148,136,.15);
  border: 1px solid rgba(13,148,136,.3);
  color: var(--teal);
  padding: 2px 8px;
  border-radius: 4px;
  margin-top: 6px;
}

.fc-15__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-15__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  /* KEY: rotateX instead of rotateY = vertical flip */
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fc-15__scene:hover .fc-15__card {
  transform: rotateX(180deg);
}

.fc-15__front,
.fc-15__back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-15__front {
  background: linear-gradient(160deg,#071a16,#04100e);
  border: 1px solid rgba(13,148,136,.25);
  display: flex;
  align-items: center;
  padding: 28px 32px;
  gap: 20px;
}

.fc-15__icon-box {
  width: 64px;
  height: 64px;
  border-radius: 18px;
  flex-shrink: 0;
  background: linear-gradient(135deg,rgba(13,148,136,.2),rgba(16,185,129,.1));
  border: 1px solid rgba(13,148,136,.3);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 20px rgba(13,148,136,.15);
}

.fc-15__icon-box svg {
  stroke: var(--teal);
  stroke-width: 1.8;
  fill: none;
  width: 28px;
  height: 28px;
}

.fc-15__front-text {
  flex: 1;
}

.fc-15__front-label {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--teal);
  font-weight: 700;
  margin-bottom: 6px;
}

.fc-15__front-title {
  font-size: 20px;
  font-weight: 800;
  color: var(--white);
  line-height: 1.2;
}

.fc-15__front-sub {
  font-size: 12px;
  color: rgba(240,253,244,.45);
  margin-top: 6px;
}

.fc-15__axis-arrow {
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  opacity: .35;
}

.fc-15__axis-arrow span {
  font-size: 10px;
  color: var(--teal);
  letter-spacing: .08em;
}
/* BACK — rotateX(180deg) on the element itself means it starts face-down */

.fc-15__back {
  background: linear-gradient(160deg,#031a14,#040e0c);
  border: 1px solid rgba(16,185,129,.25);
  transform: rotateX(180deg);
  display: flex;
  align-items: center;
  padding: 28px 32px;
  gap: 20px;
}

.fc-15__back-icon {
  width: 64px;
  height: 64px;
  border-radius: 18px;
  flex-shrink: 0;
  background: linear-gradient(135deg,rgba(16,185,129,.2),rgba(13,148,136,.1));
  border: 1px solid rgba(16,185,129,.3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
}

.fc-15__back-label {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--emerald);
  font-weight: 700;
  margin-bottom: 6px;
}

.fc-15__back-title {
  font-size: 18px;
  font-weight: 800;
  color: var(--white);
}

.fc-15__pill-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}

.fc-15__pill {
  font-size: 11px;
  padding: 4px 10px;
  border-radius: 20px;
  background: rgba(16,185,129,.1);
  border: 1px solid rgba(16,185,129,.2);
  color: rgba(240,253,244,.7);
}

@media (prefers-reduced-motion: reduce) {
  .fc-15__card {
    transition: none;
  }
}
```
