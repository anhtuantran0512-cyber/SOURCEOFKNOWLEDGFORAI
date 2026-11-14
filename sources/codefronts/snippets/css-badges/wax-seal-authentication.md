---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/wax-seal-authentication/"
title: "Wax Seal Authentication"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Embossed oxblood wax disc over a written page, anchored by a gold-leaf monogram."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Wax Seal Authentication
Source: https://codefronts.com/snippets/css-badges/wax-seal-authentication/

Embossed oxblood wax disc over a written page, anchored by a gold-leaf monogram. Click the seal to press — the disc compresses, holds, releases. Drips peek out from the base.
## HTML
```html
<div class="bdg-24-stage">
  <div class="bdg-24-paper">
    <div class="bdg-24-watermark">CERTIFIED</div>
    <div class="bdg-24-eyebrow">— Certificate of Authenticity —</div>
    <div class="bdg-24-line-top">By my hand and seal, on this day —</div>
    <div class="bdg-24-signature">A. Whitmore</div>

    <div class="bdg-24-seal" id="bdg-24-seal-1">
      <div class="bdg-24-drip bdg-24-drip-1"></div>
      <div class="bdg-24-drip bdg-24-drip-2"></div>
      <div class="bdg-24-disc">
        <div class="bdg-24-monogram">
          <svg viewBox="0 0 100 100" fill="none" aria-hidden="true">
            <circle cx="50" cy="50" r="34" stroke="#3a0d11" stroke-width="0.6" opacity="0.5"/>
            <circle cx="50" cy="50" r="28" stroke="#3a0d11" stroke-width="0.4" opacity="0.4"/>
            <path d="M 28 70 L 28 30 L 50 60 L 72 30 L 72 70" stroke="#3a0d11" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="50" cy="14" r="1.6" fill="#3a0d11"/>
            <circle cx="50" cy="86" r="1.6" fill="#3a0d11"/>
            <circle cx="14" cy="50" r="1.6" fill="#3a0d11"/>
            <circle cx="86" cy="50" r="1.6" fill="#3a0d11"/>
          </svg>
        </div>
        <div class="bdg-24-highlight"></div>
      </div>
    </div>

    <div class="bdg-24-line-bottom">Document N° A-2026-0481</div>
  </div>
</div>
```
## CSS
```css
.bdg-24-stage {
  background: linear-gradient(180deg, #ece2c8 0%, #ddd0b0 100%);
  padding: 48px 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-24-paper {
  background: #f6ecd2;
  width: 100%;
  max-width: 360px;
  padding: 44px 36px 36px;
  box-shadow: 0 28px 50px -18px rgba(80,60,30,0.35), 0 10px 18px -4px rgba(80,60,30,0.18), inset 0 0 0 1px rgba(120,90,50,0.12);
  position: relative;
  text-align: center;
  transform: rotate(-1.2deg);
}

.bdg-24-watermark {
  position: absolute;
  top: 38%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-12deg);
  font-family: "Cinzel", Georgia, serif;
  font-size: 52px;
  font-weight: 700;
  color: rgba(120, 80, 40, 0.06);
  letter-spacing: 0.25em;
  pointer-events: none;
}

.bdg-24-eyebrow {
  font-family: "Cinzel", Georgia, serif;
  font-size: 9px;
  letter-spacing: 0.4em;
  color: #8a6630;
  margin-bottom: 6px;
  position: relative;
}

.bdg-24-line-top {
  font-family: "Cormorant Garamond", Georgia, serif;
  font-style: italic;
  font-size: 13px;
  color: #5a4222;
  letter-spacing: 0.04em;
  margin-bottom: 2px;
  position: relative;
}

.bdg-24-signature {
  font-family: "Tangerine", "Cormorant Garamond", cursive;
  font-size: 44px;
  color: #3a2814;
  line-height: 1;
  margin: 2px 0 22px;
  position: relative;
}

.bdg-24-seal {
  width: 178px;
  height: 178px;
  margin: 0 auto 22px;
  position: relative;
  cursor: pointer;
}

.bdg-24-disc {
  width: 100%;
  height: 100%;
  position: relative;
  border-radius: 50% 47% 53% 49% / 49% 52% 48% 51%;
  background: radial-gradient(circle at 32% 28%,
      #a83040 0%,
      #802028 22%,
      #4e121a 60%,
      #2a0a10 100%);
  box-shadow: inset 6px 8px 14px rgba(0,0,0,0.45), inset -3px -5px 10px rgba(255,180,180,0.12), inset 2px 2px 4px rgba(255,200,200,0.25), 8px 12px 22px rgba(40,8,12,0.45), 3px 5px 10px rgba(94,26,31,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.bdg-24-seal.is-pressed .bdg-24-disc {
  animation: bdg-24-press 0.55s ease-out;
}

@keyframes bdg-24-press {
  0% {
    transform: scale(1);
  }

  25% {
    transform: scale(0.94);
  }

  60% {
    transform: scale(1.015);
  }

  100% {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-24-seal.is-pressed .bdg-24-disc {
    animation: none;
  }
}

.bdg-24-disc::before {
  content: '';
  position: absolute;
  inset: 7px;
  border-radius: inherit;
  border: 1px solid rgba(255,180,180,0.12);
  pointer-events: none;
}

.bdg-24-monogram {
  width: 64%;
  height: 64%;
  position: relative;
  z-index: 2;
  filter: drop-shadow(0 -1px 0.5px rgba(255,180,180,0.5)) drop-shadow(0 1.5px 1px rgba(0,0,0,0.65));
}

.bdg-24-monogram svg {
  width: 100%;
  height: 100%;
  display: block;
}

.bdg-24-highlight {
  position: absolute;
  top: 14%;
  left: 20%;
  width: 36%;
  height: 24%;
  border-radius: 50%;
  background: radial-gradient(ellipse, rgba(255,200,200,0.5), transparent 70%);
  filter: blur(8px);
  pointer-events: none;
  z-index: 3;
}

.bdg-24-drip {
  position: absolute;
  background: radial-gradient(circle at 30% 30%, #802028 0%, #4e121a 60%, #2a0a10 100%);
  box-shadow: inset 2px 3px 5px rgba(0,0,0,0.4), 2px 4px 7px rgba(40,8,12,0.5);
  z-index: 1;
}

.bdg-24-drip-1 {
  width: 20px;
  height: 26px;
  bottom: -6px;
  right: 26px;
  border-radius: 42% 58% 50% 50% / 60% 60% 40% 40%;
}

.bdg-24-drip-2 {
  width: 12px;
  height: 14px;
  bottom: -10px;
  right: 14px;
  border-radius: 50%;
}

.bdg-24-line-bottom {
  font-family: "Cinzel", Georgia, serif;
  font-size: 9px;
  letter-spacing: 0.32em;
  color: #6a4a22;
  text-transform: uppercase;
  position: relative;
  margin-top: 8px;
}
```

## JavaScript
```js
// Click the wax seal to play the press animation. Toggling the class
// via re-flow ensures the keyframe restarts on every click instead of
// only firing once.
var seal = document.getElementById('bdg-24-seal-1');
if (seal) {
  seal.addEventListener('click', function () {
    seal.classList.remove('is-pressed');
    void seal.offsetWidth;
    seal.classList.add('is-pressed');
  });
}
```
