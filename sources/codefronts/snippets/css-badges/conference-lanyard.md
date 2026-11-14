---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/conference-lanyard/"
title: "Conference Lanyard"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Physical badge with ambient sway, hanging from its own clip."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Conference Lanyard
Source: https://codefronts.com/snippets/css-badges/conference-lanyard/

Physical badge with ambient sway, hanging from its own clip. Click flips it — front holds the role band and name, back holds the QR. Each card swings at a slightly different frequency.
## HTML
```html
<div class="bdg-25-card" style="--bdg-25-role-color: #b8442d">
  <div class="bdg-25-lanyard">
    <svg viewBox="0 0 24 80" aria-hidden="true"><path d="M0 0 L8 80 M24 0 L16 80" stroke="#b8442d" stroke-width="6" fill="none"/></svg>
  </div>
  <div class="bdg-25-clip"></div>
  <div class="bdg-25-badge">
    <div class="bdg-25-face bdg-25-front">
      <span class="bdg-25-role-band">Speaker</span>
      <div class="bdg-25-name-block">
        <div class="bdg-25-name">Amara <em>Okonkwo</em></div>
        <div class="bdg-25-title-line">Principal · Form &amp; Function</div>
      </div>
      <div class="bdg-25-footer-front">
        <span>#A-2026</span>
        <span>14:30 / Hall A</span>
      </div>
    </div>
    <div class="bdg-25-face bdg-25-back">
      <div class="bdg-25-qr"></div>
      <div class="bdg-25-back-name">Amara Okonkwo</div>
      <div class="bdg-25-back-hint">Tap to view profile</div>
    </div>
  </div>
  <div class="bdg-25-caption">Click to flip</div>
</div>
```
## CSS
```css
.bdg-25-card {
  background: linear-gradient(170deg, #2a2724 0%, #1a1815 100%);
  padding: 100px 32px 60px;
  perspective: 1200px;
  text-align: center;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.bdg-25-lanyard {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 24px;
  height: 80px;
  z-index: 2;
  pointer-events: none;
}

.bdg-25-lanyard svg {
  width: 100%;
  height: 100%;
  display: block;
}

.bdg-25-clip {
  position: absolute;
  top: 94px;
  left: 50%;
  transform: translateX(-50%);
  width: 32px;
  height: 16px;
  background: linear-gradient(180deg, #d4d4d4 0%, #888 50%, #666 100%);
  border-radius: 2px;
  z-index: 3;
  box-shadow: 0 2px 4px rgba(0,0,0,0.4);
}

.bdg-25-clip::before {
  content: '';
  position: absolute;
  top: 4px;
  left: 50%;
  transform: translateX(-50%);
  width: 14px;
  height: 6px;
  border: 1.5px solid #333;
  border-radius: 50%;
}

.bdg-25-badge {
  position: relative;
  width: 220px;
  margin: 110px auto 18px;
  aspect-ratio: 3 / 4.4;
  background: #f5f1e8;
  border-radius: 6px;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: top center;
  box-shadow: 0 20px 30px -10px rgba(0,0,0,0.5), 0 4px 8px rgba(0,0,0,0.3);
  cursor: pointer;
  animation: bdg-25-sway 6s ease-in-out infinite;
}

@keyframes bdg-25-sway {
  0%,
    100% {
    transform: rotateZ(-1deg) rotateY(0deg);
  }

  50% {
    transform: rotateZ(1deg) rotateY(0deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-25-badge {
    animation: none;
  }
}

.bdg-25-card.is-flipped .bdg-25-badge {
  transform: rotateY(180deg);
  animation: none;
}

.bdg-25-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  border-radius: 6px;
  overflow: hidden;
  padding: 22px 18px;
  display: flex;
  flex-direction: column;
}

.bdg-25-front {
  background: linear-gradient(180deg, #f8f5ed 0%, #ede8da 100%);
}

.bdg-25-back {
  background: var(--bdg-25-role-color, #1a1815);
  color: #f5f1e8;
  transform: rotateY(180deg);
  align-items: center;
  justify-content: center;
}

.bdg-25-role-band {
  display: inline-block;
  padding: 4px 10px;
  font-family: system-ui, sans-serif;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  background: var(--bdg-25-role-color, #1a1815);
  color: #f5f1e8;
  align-self: flex-start;
}

.bdg-25-name-block {
  margin-top: auto;
}

.bdg-25-name {
  font-family: Georgia, "Fraunces", serif;
  font-size: 26px;
  line-height: 1;
  font-weight: 400;
  color: #1a1815;
  margin-bottom: 4px;
  letter-spacing: -0.02em;
}

.bdg-25-name em {
  font-style: italic;
  font-weight: 300;
}

.bdg-25-title-line {
  font-family: system-ui, sans-serif;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #4a4239;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.bdg-25-footer-front {
  border-top: 1px dashed #999;
  padding-top: 10px;
  display: flex;
  justify-content: space-between;
  font-family: system-ui, sans-serif;
  font-size: 8px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #4a4239;
}

.bdg-25-qr {
  width: 80px;
  height: 80px;
  background-image: linear-gradient(0deg, var(--bdg-25-role-color) 50%, transparent 50%), linear-gradient(90deg, var(--bdg-25-role-color) 50%, transparent 50%);
  background-size: 8px 8px;
  background-color: #f5f1e8;
  border: 8px solid #f5f1e8;
  margin-bottom: 16px;
  box-shadow: 0 0 0 1px var(--bdg-25-role-color);
}

.bdg-25-back-name {
  font-family: Georgia, "Fraunces", serif;
  font-style: italic;
  font-size: 18px;
  margin-bottom: 4px;
}

.bdg-25-back-hint {
  font-family: system-ui, sans-serif;
  font-size: 8px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  opacity: 0.6;
}

.bdg-25-caption {
  margin-top: 8px;
  font-family: system-ui, sans-serif;
  color: rgba(255,255,255,0.4);
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
}
```

## JavaScript
```js
// Click the badge to flip front ↔ back. Stops the ambient sway while
// flipped so the back-side QR doesn't wobble away from the user's eye.
document.querySelectorAll('.bdg-25-card').forEach(function (card) {
  var badge = card.querySelector('.bdg-25-badge');
  if (!badge) return;
  badge.addEventListener('click', function () {
    card.classList.toggle('is-flipped');
  });
});
```
