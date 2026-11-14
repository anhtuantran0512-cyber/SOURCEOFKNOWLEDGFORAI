---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/art-deco-medallion/"
title: "Art Deco Medallion"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Conic-gradient brass ring rotating against a slow ray pattern. Crest in Cinzel display type. Sweep of shine on hover, gentle lift on the whole medallion."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Art Deco Medallion
Source: https://codefronts.com/snippets/css-badges/art-deco-medallion/

Conic-gradient brass ring rotating against a slow ray pattern. Crest in Cinzel display type. Sweep of shine on hover, gentle lift on the whole medallion.
## HTML
```html
<div class="bdg-28-wrap">
  <div class="bdg-28-medallion">
    <div class="bdg-28-ring-outer"></div>
    <div class="bdg-28-rays"></div>
    <div class="bdg-28-ring-inner">
      <div class="bdg-28-crest">
        <svg viewBox="0 0 50 50" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
          <path d="M25 5 L29 18 L43 18 L32 26 L36 40 L25 32 L14 40 L18 26 L7 18 L21 18 Z" fill="currentColor" fill-opacity="0.15"/>
          <path d="M25 5 L29 18 L43 18 L32 26 L36 40 L25 32 L14 40 L18 26 L7 18 L21 18 Z"/>
        </svg>
        <div class="bdg-28-label">First Star</div>
      </div>
    </div>
    <div class="bdg-28-shine"></div>
  </div>
  <div class="bdg-28-name">Centurion</div>
  <div class="bdg-28-annotation">For one hundred contributions of merit</div>
</div>
```
## CSS
```css
.bdg-28-wrap {
  background: radial-gradient(ellipse at center, #2a1d12 0%, #14100a 100%);
  padding: 60px 40px;
  text-align: center;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.bdg-28-medallion {
  width: 200px;
  height: 200px;
  margin: 0 auto 28px;
  position: relative;
  cursor: pointer;
  transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.bdg-28-medallion:hover {
  transform: translateY(-8px) scale(1.04);
}

.bdg-28-ring-outer {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(from 0deg,
        #d4af5a 0deg, #f5d782 8deg, #d4af5a 16deg,
        #8b6f2a 24deg, #d4af5a 32deg, #f5d782 40deg, #d4af5a 48deg,
        #8b6f2a 56deg, #d4af5a 64deg, #f5d782 72deg, #d4af5a 80deg,
        #8b6f2a 88deg, #d4af5a 96deg, #f5d782 104deg, #d4af5a 112deg,
        #8b6f2a 120deg, #d4af5a 128deg, #f5d782 136deg, #d4af5a 144deg,
        #8b6f2a 152deg, #d4af5a 160deg, #f5d782 168deg, #d4af5a 176deg,
        #8b6f2a 184deg, #d4af5a 192deg, #f5d782 200deg, #d4af5a 208deg,
        #8b6f2a 216deg, #d4af5a 224deg, #f5d782 232deg, #d4af5a 240deg,
        #8b6f2a 248deg, #d4af5a 256deg, #f5d782 264deg, #d4af5a 272deg,
        #8b6f2a 280deg, #d4af5a 288deg, #f5d782 296deg, #d4af5a 304deg,
        #8b6f2a 312deg, #d4af5a 320deg, #f5d782 328deg, #d4af5a 336deg,
        #8b6f2a 344deg, #d4af5a 360deg);
  animation: bdg-28-rotate 24s linear infinite;
  box-shadow: 0 0 30px rgba(212,175,90,0.3), inset 0 0 20px rgba(0,0,0,0.4);
}

@keyframes bdg-28-rotate {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-28-ring-outer,
    .bdg-28-rays {
    animation: none;
  }
}

.bdg-28-ring-inner {
  position: absolute;
  inset: 14px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #3a2614 0%, #1c1408 100%);
  border: 2px solid #8b6f2a;
  box-shadow: inset 0 4px 12px rgba(0,0,0,0.6), inset 0 -2px 6px rgba(212,175,90,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
}

.bdg-28-rays {
  position: absolute;
  inset: 14px;
  border-radius: 50%;
  background: conic-gradient(from 0deg,
        transparent 0deg, rgba(212,175,90,0.15) 5deg, transparent 10deg,
        transparent 30deg, rgba(212,175,90,0.15) 35deg, transparent 40deg,
        transparent 60deg, rgba(212,175,90,0.15) 65deg, transparent 70deg,
        transparent 90deg, rgba(212,175,90,0.15) 95deg, transparent 100deg,
        transparent 120deg, rgba(212,175,90,0.15) 125deg, transparent 130deg,
        transparent 150deg, rgba(212,175,90,0.15) 155deg, transparent 160deg,
        transparent 180deg, rgba(212,175,90,0.15) 185deg, transparent 190deg,
        transparent 210deg, rgba(212,175,90,0.15) 215deg, transparent 220deg,
        transparent 240deg, rgba(212,175,90,0.15) 245deg, transparent 250deg,
        transparent 270deg, rgba(212,175,90,0.15) 275deg, transparent 280deg,
        transparent 300deg, rgba(212,175,90,0.15) 305deg, transparent 310deg,
        transparent 330deg, rgba(212,175,90,0.15) 335deg, transparent 340deg,
        transparent 360deg);
  animation: bdg-28-rotate 60s linear infinite reverse;
  pointer-events: none;
}

.bdg-28-crest {
  position: relative;
  z-index: 2;
  text-align: center;
  color: #d4af5a;
}

.bdg-28-crest svg {
  width: 50px;
  height: 50px;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,0.5));
}

.bdg-28-label {
  font-family: "Cinzel", Georgia, serif;
  font-size: 9px;
  letter-spacing: 0.32em;
  margin-top: 6px;
  text-transform: uppercase;
  color: #e8c878;
}

.bdg-28-shine {
  position: absolute;
  top: 14px;
  left: 14px;
  width: calc(100% - 28px);
  height: calc(100% - 28px);
  border-radius: 50%;
  background: linear-gradient(135deg, transparent 30%, rgba(255,255,255,0.4) 50%, transparent 70%);
  opacity: 0;
  transition: opacity 0.6s, transform 0.8s;
  transform: translateX(-100%);
  pointer-events: none;
}

.bdg-28-medallion:hover .bdg-28-shine {
  opacity: 1;
  transform: translateX(100%);
}

.bdg-28-name {
  font-family: "Cinzel", Georgia, serif;
  color: #d4af5a;
  font-size: 14px;
  letter-spacing: 0.32em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.bdg-28-annotation {
  font-family: "Cormorant Garamond", Georgia, serif;
  color: rgba(212,175,90,0.65);
  font-size: 14px;
  font-style: italic;
  letter-spacing: 0.02em;
}
```
