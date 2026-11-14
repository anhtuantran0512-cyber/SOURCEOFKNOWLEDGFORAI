---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/holographic-collectible/"
title: "Holographic Collectible"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Pentagonal collectible badge with a cursor-tracked conic-gradient foil and a tier glyph."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Holographic Collectible
Source: https://codefronts.com/snippets/css-badges/holographic-collectible/

Pentagonal collectible badge with a cursor-tracked conic-gradient foil and a tier glyph. The Mythic tier carries its own ambient pulse — visible across the room.
## HTML
```html
<div class="bdg-30-card">
  <div class="bdg-30-badge bdg-30-mythic">
    <div class="bdg-30-face bdg-30-base"></div>
    <div class="bdg-30-face bdg-30-foil"></div>
    <div class="bdg-30-face bdg-30-sheen"></div>
    <div class="bdg-30-face bdg-30-edge"></div>
    <div class="bdg-30-glyph">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
        <path d="M12 1l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z"/>
      </svg>
      <div class="bdg-30-rarity">RARITY</div>
      <div class="bdg-30-tier">MYTHIC</div>
    </div>
    <div class="bdg-30-serial">#00007 / 00050</div>
  </div>
  <div class="bdg-30-name">The Ascendant</div>
  <div class="bdg-30-pop">POP 44</div>
</div>
```
## CSS
```css
.bdg-30-card {
  background: radial-gradient(ellipse at 50% 50%, #0e0a1a 0%, #050208 100%);
  padding: 56px 40px;
  font-family: 'Geist Mono', ui-monospace, monospace;
  text-align: center;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.bdg-30-badge {
  width: 200px;
  height: 230px;
  margin: 0 auto 24px;
  position: relative;
  cursor: pointer;
  --mx: 50%;
  --my: 50%;
}

.bdg-30-face {
  position: absolute;
  inset: 0;
  clip-path: polygon(50% 0%, 95% 25%, 95% 75%, 50% 100%, 5% 75%, 5% 25%);
}

.bdg-30-base {
  background: linear-gradient(135deg, #1a1230 0%, #0a0815 100%);
  box-shadow: inset 0 0 20px rgba(255,255,255,0.05);
}

.bdg-30-foil {
  background: conic-gradient(from var(--angle, 0deg) at var(--mx) var(--my),
        #ff0080, #ff8c00, #ffd700, #00ff88, #00bfff, #8a2be2, #ff0080);
  mix-blend-mode: screen;
  opacity: 0.75;
  transition: opacity 0.4s;
  filter: saturate(1.3) blur(0.4px);
}

.bdg-30-sheen {
  background: radial-gradient(circle 80px at var(--mx) var(--my),
      rgba(255,255,255,0.6), transparent 70%);
  mix-blend-mode: overlay;
  opacity: 0;
  transition: opacity 0.4s;
}

.bdg-30-edge {
  background: linear-gradient(135deg,
      rgba(255,215,140,0.6) 0%,
      rgba(180,140,255,0.4) 50%,
      rgba(120,200,255,0.6) 100%);
  clip-path: polygon(
      50% 0%, 95% 25%, 95% 75%, 50% 100%, 5% 75%, 5% 25%,
      5% 27%, 7% 26%, 7% 74%, 50% 97%, 93% 74%, 93% 26%, 50% 3%
    );
}

.bdg-30-badge:hover .bdg-30-foil {
  opacity: 1;
}

.bdg-30-badge:hover .bdg-30-sheen {
  opacity: 1;
}

.bdg-30-glyph {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #fff;
  z-index: 2;
  text-shadow: 0 0 12px rgba(255,255,255,0.3);
  pointer-events: none;
}

.bdg-30-glyph svg {
  width: 56px;
  height: 56px;
  margin-bottom: 8px;
}

.bdg-30-rarity {
  font-size: 10px;
  letter-spacing: 0.3em;
  opacity: 0.85;
  margin-bottom: 2px;
}

.bdg-30-tier {
  font-size: 16px;
  letter-spacing: 0.18em;
  font-weight: 600;
}

.bdg-30-serial {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 8px;
  letter-spacing: 0.2em;
  color: rgba(255,255,255,0.6);
  z-index: 2;
}

.bdg-30-name {
  font-family: Georgia, serif;
  color: #f5f0e0;
  font-size: 20px;
  font-style: italic;
  margin-bottom: 4px;
}

.bdg-30-pop {
  font-size: 10px;
  letter-spacing: 0.2em;
  color: rgba(255,255,255,0.4);
  text-transform: uppercase;
}

.bdg-30-mythic .bdg-30-base {
  animation: bdg-30-mythic-pulse 3s ease-in-out infinite;
}

@keyframes bdg-30-mythic-pulse {
  0%,
    100% {
    box-shadow: inset 0 0 20px rgba(255,100,255,0.2), 0 0 30px rgba(255,100,255,0.2);
  }

  50% {
    box-shadow: inset 0 0 40px rgba(255,100,255,0.5), 0 0 60px rgba(255,100,255,0.4);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-30-mythic .bdg-30-base {
    animation: none;
  }
}
```

## JavaScript
```js
// Cursor-tracked foil. Updates two CSS custom properties on the
// .bdg-30-badge so the conic gradient and the sheen highlight follow
// the pointer. mouseleave resets so the badge isn't stuck mid-tilt.
document.querySelectorAll('.bdg-30-badge').forEach(function (badge) {
  badge.addEventListener('mousemove', function (e) {
    var r = badge.getBoundingClientRect();
    var x = ((e.clientX - r.left) / r.width) * 100;
    var y = ((e.clientY - r.top) / r.height) * 100;
    badge.style.setProperty('--mx', x + '%');
    badge.style.setProperty('--my', y + '%');
    badge.style.setProperty('--angle', (x * 3.6) + 'deg');
  });
  badge.addEventListener('mouseleave', function () {
    badge.style.setProperty('--mx', '50%');
    badge.style.setProperty('--my', '50%');
  });
});
```
