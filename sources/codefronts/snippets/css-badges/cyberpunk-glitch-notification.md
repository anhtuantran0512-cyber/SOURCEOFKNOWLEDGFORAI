---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/cyberpunk-glitch-notification/"
title: "Cyberpunk Glitch Notification"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Notification counter with perpetual chromatic aberration."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Glitch Notification
Source: https://codefronts.com/snippets/css-badges/cyberpunk-glitch-notification/

Notification counter with perpetual chromatic aberration. Hover triggers a full RGB-split glitch storm; click scrambles the digits hex-style before settling. Scanline drifts top-to-bottom continuously.
## HTML
```html
<div class="bdg-27-wrap">
  <div class="bdg-27-header">
    <span>NET://INCOMING [ACTIVE]</span>
    <span>UPLINK <span class="bdg-27-blink">▮</span></span>
  </div>
  <div class="bdg-27-card bdg-27-urgent">
    <div class="bdg-27-scanline"></div>
    <div class="bdg-27-label">[alerts.crit]</div>
    <div class="bdg-27-count">03</div>
    <div class="bdg-27-meta"><span>system</span><span class="bdg-27-tag">PRIORITY</span></div>
  </div>
  <div class="bdg-27-card">
    <div class="bdg-27-scanline"></div>
    <div class="bdg-27-label">[unread.msg]</div>
    <div class="bdg-27-count">247</div>
    <div class="bdg-27-meta"><span>direct</span><span class="bdg-27-tag">+12 NEW</span></div>
  </div>
</div>
```
## CSS
```css
.bdg-27-wrap {
  background: #0a0e0a;
  padding: 36px 32px;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 24px;
  width: 100%;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
}

.bdg-27-wrap::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg,
      transparent 0px, transparent 3px,
      rgba(0,255,140,0.025) 3px, rgba(0,255,140,0.025) 4px);
  pointer-events: none;
}

.bdg-27-wrap::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 30% 20%, rgba(255,0,140,0.1), transparent 50%), radial-gradient(circle at 70% 80%, rgba(0,255,200,0.1), transparent 50%);
  pointer-events: none;
}

.bdg-27-header {
  font-family: "VT323", ui-monospace, monospace;
  color: #00ff8c;
  font-size: 18px;
  display: flex;
  justify-content: space-between;
  letter-spacing: 0.05em;
  position: relative;
  z-index: 1;
}

.bdg-27-blink {
  animation: bdg-27-blink 1s steps(2) infinite;
}

@keyframes bdg-27-blink {
  50% {
    opacity: 0;
  }
}

.bdg-27-card {
  background: rgba(10, 20, 14, 0.6);
  border: 1px solid #00ff8c;
  padding: 24px 22px;
  position: relative;
  transition: all 0.3s;
  cursor: pointer;
  z-index: 1;
}

.bdg-27-card::before {
  content: '';
  position: absolute;
  top: -1px;
  left: -1px;
  width: 12px;
  height: 12px;
  border-top: 2px solid #ff0099;
  border-left: 2px solid #ff0099;
}

.bdg-27-card::after {
  content: '';
  position: absolute;
  bottom: -1px;
  right: -1px;
  width: 12px;
  height: 12px;
  border-bottom: 2px solid #ff0099;
  border-right: 2px solid #ff0099;
}

.bdg-27-label {
  font-family: "Major Mono Display", ui-monospace, monospace;
  color: #00ff8c;
  font-size: 10px;
  letter-spacing: 0.25em;
  margin-bottom: 8px;
  text-transform: lowercase;
}

.bdg-27-count {
  font-family: "VT323", ui-monospace, monospace;
  color: #fff;
  font-size: 64px;
  line-height: 1;
  text-shadow: 2px 0 #ff0099, -2px 0 #00d4ff, 0 0 20px rgba(255,255,255,0.3);
  margin-bottom: 14px;
  transition: text-shadow 0.2s;
}

.bdg-27-card:hover .bdg-27-count {
  animation: bdg-27-glitch 0.4s infinite;
}

@keyframes bdg-27-glitch {
  0% {
    text-shadow: 3px 0 #ff0099, -3px 0 #00d4ff, 0 0 20px rgba(255,255,255,0.5);
    transform: translateX(0);
  }

  25% {
    text-shadow: -3px 0 #ff0099, 3px 0 #00d4ff;
    transform: translateX(-1px);
  }

  50% {
    text-shadow: 3px 0 #ff0099, -3px 0 #00d4ff;
    transform: translateX(1px);
  }

  75% {
    text-shadow: 0 3px #ff0099, 0 -3px #00d4ff;
    transform: translateX(0);
  }

  100% {
    text-shadow: 3px 0 #ff0099, -3px 0 #00d4ff;
  }
}

.bdg-27-meta {
  font-family: "VT323", ui-monospace, monospace;
  color: rgba(0,255,140,0.6);
  font-size: 14px;
  letter-spacing: 0.05em;
  border-top: 1px dashed rgba(0,255,140,0.3);
  padding-top: 10px;
  display: flex;
  justify-content: space-between;
}

.bdg-27-tag {
  color: #ff0099;
}

.bdg-27-urgent {
  border-color: #ff0099;
  animation: bdg-27-urgent 2s ease-in-out infinite;
}

.bdg-27-urgent::before,
.bdg-27-urgent::after {
  border-color: #00ff8c;
}

@keyframes bdg-27-urgent {
  0%,
    100% {
    box-shadow: 0 0 0 rgba(255,0,153,0.4);
  }

  50% {
    box-shadow: 0 0 20px rgba(255,0,153,0.4);
  }
}

.bdg-27-scanline {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #00ff8c, transparent);
  opacity: 0.6;
  animation: bdg-27-scan 3s linear infinite;
}

@keyframes bdg-27-scan {
  0% {
    top: 0;
  }

  100% {
    top: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-27-blink,
    .bdg-27-scanline,
    .bdg-27-urgent {
    animation: none;
  }

  .bdg-27-card:hover .bdg-27-count {
    animation: none;
  }
}
```

## JavaScript
```js
// Click any counter card to scramble the digits hex-style before
// settling back to the real value. Mirrors the glitch aesthetic
// applied via CSS on hover.
document.querySelectorAll('.bdg-27-card').forEach(function (card) {
  card.addEventListener('click', function () {
    var countEl = card.querySelector('.bdg-27-count');
    var original = countEl.textContent;
    var chars = '0123456789ABCDEF';
    var i = 0;
    var scramble = setInterval(function () {
      countEl.textContent = Array.from(original).map(function (c) {
        return /[\dA-Za-z]/.test(c)
          ? chars[Math.floor(Math.random() * chars.length)]
          : c;
      }).join('');
      if (++i > 8) {
        clearInterval(scramble);
        countEl.textContent = original;
      }
    }, 50);
  });
});
```
