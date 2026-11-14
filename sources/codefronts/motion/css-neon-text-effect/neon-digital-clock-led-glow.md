---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/neon-digital-clock-led-glow/"
title: "Neon Digital Clock LED Glow"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A retro 7-segment LED clock glowing on true black — the loading-screen / dashboard timepiece look."
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Digital Clock LED Glow
Source: https://codefronts.com/motion/css-neon-text-effect/neon-digital-clock-led-glow/

A retro 7-segment LED clock glowing on true black — the loading-screen / dashboard timepiece look. A ghost '88:88' backplate sells the LED realism; five lines of JS keep real time.
## HTML
```html
<div class="cnt-10">
  <div class="cnt-10__display">
    <span class="cnt-10__ghost" aria-hidden="true">88:88</span>
    <span class="cnt-10__time" id="cnt-10-time">10:24</span>
    <span class="cnt-10__label">SYSTEM TIME</span>
  </div>
</div>
```
## CSS
```css
.cnt-10,
.cnt-10 *,
.cnt-10 *::before,
.cnt-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-10 ::selection {
  background: oklch(0.86 0.2 160);
  color: #03130c;
}

.cnt-10 {
  --accent: oklch(0.86 0.2 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(100% 100% at 50% 40%,#0a0f0c,#040605);
}

.cnt-10__display {
  position: relative;
  padding: 40px 56px;
  border-radius: 14px;
  background: #050807;
  border: 1px solid #14201a;
  box-shadow: inset 0 0 40px rgba(0,0,0,.8),0 30px 60px -40px #000;
  text-align: center;
}

.cnt-10__ghost,
.cnt-10__time {
  font-family: 'Courier New',ui-monospace,monospace;
  font-weight: 700;
  font-size: clamp(56px,15vw,120px);
  letter-spacing: .06em;
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

.cnt-10__ghost {
  color: color-mix(in oklch,var(--accent) 12%,#0c1410);
  display: block;
}

.cnt-10__time {
  position: absolute;
  left: 0;
  right: 0;
  top: 40px;
  color: var(--accent);
  text-shadow: 0 0 6px #eafff4,0 0 16px var(--accent),0 0 40px var(--accent),0 0 80px color-mix(in oklch,var(--accent) 60%,transparent);
}

.cnt-10__time::after {
  content: "";
  position: absolute;
}

.cnt-10__label {
  display: block;
  margin-top: 18px;
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .42em;
  color: color-mix(in oklch,var(--accent) 45%,#3a5245);
}

.cnt-10__time {
  animation: cnt-10-colon 1s steps(1,end) infinite;
}

@keyframes cnt-10-colon {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .86;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-10__time {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var el = document.getElementById('cnt-10-time');
  if(!el) return;
  function tick(){
    var d = new Date();
    var hh = String(d.getHours()).padStart(2,'0');
    var mm = String(d.getMinutes()).padStart(2,'0');
    el.textContent = hh + ':' + mm;
  }
  tick();
  setInterval(tick, 1000);
})();
```
