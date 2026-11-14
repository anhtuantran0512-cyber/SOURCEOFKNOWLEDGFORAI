---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/vaporwave-chrome/"
title: "Vaporwave Chrome"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Release channel as marquee."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vaporwave Chrome
Source: https://codefronts.com/snippets/css-badges/vaporwave-chrome/

Release channel as marquee. Chrome lettering over a synthwave horizon, ticker tape reminding you exactly what kind of trouble you are in. The sun is striped. The grid recedes. The warning never stops scrolling.
## HTML
```html
<div class="bdg-22-stage">
  <div class="bdg-22-sun"></div>
  <div class="bdg-22-grid"></div>
  <div class="bdg-22-card">
    <div class="bdg-22-corner bdg-22-tl"></div>
    <div class="bdg-22-corner bdg-22-tr"></div>
    <div class="bdg-22-corner bdg-22-bl"></div>
    <div class="bdg-22-corner bdg-22-br"></div>

    <div class="bdg-22-eyebrow">▼ RELEASE CHANNEL ▼</div>
    <div class="bdg-22-chrome">BETA</div>
    <div class="bdg-22-divider"></div>
    <div class="bdg-22-version">v 4.18.2 // BUILD 26·05·13</div>

    <div class="bdg-22-marquee">
      <div class="bdg-22-marquee-track">
        <span>UNSTABLE</span><span>·</span>
        <span>FOR INTERNAL USE</span><span>·</span>
        <span>EXPECT TURBULENCE</span><span>·</span>
        <span>NOT FOR PRODUCTION</span><span>·</span>
        <span>UNSTABLE</span><span>·</span>
        <span>FOR INTERNAL USE</span><span>·</span>
        <span>EXPECT TURBULENCE</span><span>·</span>
        <span>NOT FOR PRODUCTION</span><span>·</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-22-stage {
  background: linear-gradient(180deg, #0c0628 0%, #2a0e58 45%, #c83a8c 100%);
  padding: 0;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.bdg-22-sun {
  position: absolute;
  width: 340px;
  height: 340px;
  bottom: 30%;
  left: 50%;
  transform: translateX(-50%);
  background: radial-gradient(circle, #ffeb3b 0%, #ff6ec7 45%, transparent 75%);
  border-radius: 50%;
  filter: blur(1px);
  z-index: 0;
}

.bdg-22-sun::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: repeating-linear-gradient(0deg,
      transparent 0px, transparent 16px,
      #0c0628 16px, #0c0628 20px);
  -webkit-mask: linear-gradient(180deg, transparent 0%, transparent 52%, #000 62%);
  mask: linear-gradient(180deg, transparent 0%, transparent 52%, #000 62%);
}

.bdg-22-grid {
  position: absolute;
  bottom: 0;
  left: -50%;
  right: -50%;
  height: 55%;
  background: linear-gradient(180deg, transparent 0%, #0c0628 90%), repeating-linear-gradient(90deg, #ff37b3 0px, #ff37b3 1px, transparent 1px, transparent 60px), repeating-linear-gradient(0deg,  #ff37b3 0px, #ff37b3 1px, transparent 1px, transparent 30px);
  transform: perspective(420px) rotateX(58deg);
  transform-origin: bottom;
  z-index: 0;
}

.bdg-22-card {
  position: relative;
  z-index: 1;
  background: rgba(20, 8, 50, 0.55);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 100, 200, 0.5);
  padding: 38px 44px 0;
  text-align: center;
  width: min(380px, calc(100% - 80px));
  margin: 60px auto;
}

.bdg-22-corner {
  position: absolute;
  width: 16px;
  height: 16px;
}

.bdg-22-tl {
  top: -1px;
  left: -1px;
  border-top: 2px solid #4dffff;
  border-left: 2px solid #4dffff;
}

.bdg-22-tr {
  top: -1px;
  right: -1px;
  border-top: 2px solid #ff37b3;
  border-right: 2px solid #ff37b3;
}

.bdg-22-bl {
  bottom: -1px;
  left: -1px;
  border-bottom: 2px solid #ff37b3;
  border-left: 2px solid #ff37b3;
}

.bdg-22-br {
  bottom: -1px;
  right: -1px;
  border-bottom: 2px solid #4dffff;
  border-right: 2px solid #4dffff;
}

.bdg-22-eyebrow {
  font-family: "Press Start 2P", ui-monospace, monospace;
  font-size: 8px;
  color: #ff77ee;
  letter-spacing: 0.18em;
  margin-bottom: 16px;
}

.bdg-22-chrome {
  font-family: "Major Mono Display", ui-monospace, monospace;
  font-size: 96px;
  line-height: 0.9;
  letter-spacing: 0.04em;
  background: linear-gradient(180deg,
      #ffffff 0%, #ffffff 18%, #ff8ce6 36%,
      #6cd1ff 50%, #ffffff 60%, #ff8ce6 78%, #4488cc 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 0 22px rgba(255, 100, 200, 0.7)) drop-shadow(0 3px 4px rgba(0,0,0,0.5));
}

.bdg-22-divider {
  width: 70%;
  margin: 12px auto 14px;
  height: 1px;
  background: linear-gradient(90deg, transparent, #ff77ee 30%, #4dffff 70%, transparent);
}

.bdg-22-version {
  font-family: "Major Mono Display", ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.18em;
  color: #6cd1ff;
  margin-bottom: 18px;
}

.bdg-22-marquee {
  overflow: hidden;
  border-top: 1px solid rgba(255,100,200,0.3);
  border-bottom: 1px solid rgba(255,100,200,0.3);
  padding: 8px 0;
  margin: 0 -44px;
}

.bdg-22-marquee-track {
  display: flex;
  gap: 14px;
  animation: bdg-22-scroll 14s linear infinite;
  white-space: nowrap;
  font-family: "Press Start 2P", ui-monospace, monospace;
  font-size: 7px;
  color: #ff8ce6;
  letter-spacing: 0.12em;
  width: max-content;
}

.bdg-22-marquee-track span {
  display: inline-block;
}

@keyframes bdg-22-scroll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-22-marquee-track {
    animation: none;
  }
}
```
