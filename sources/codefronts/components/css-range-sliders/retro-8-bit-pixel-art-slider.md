---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/retro-8-bit-pixel-art-slider/"
title: "Retro 8-Bit Pixel Art Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A nostalgic arcade-style health meter where the slider thumb is a pixelated gold gem, the fill uses a segmented dotted-line pattern, the character sprite…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro 8-Bit Pixel Art Slider
Source: https://codefronts.com/components/css-range-sliders/retro-8-bit-pixel-art-slider/

A nostalgic arcade-style health meter where the slider thumb is a pixelated gold gem, the fill uses a segmented dotted-line pattern, the character sprite changes emoji based on HP level, and gold coin indicators fill up like lives.
## HTML
```html
<div class="rs-14">
  <div class="rs-14__arcade">
    <div class="rs-14__screen rs-14__scanlines">
      <div class="rs-14__sprite" id="rs-14-sprite">⚔️</div>
      <div class="rs-14__hud">
        <div class="rs-14__hud-row">
          <span class="rs-14__hud-label">HP</span>
          <span class="rs-14__hud-val" id="rs-14-hp">75 / 100</span>
        </div>
        <div class="rs-14__hp-bar-wrap">
          <div class="rs-14__hp-bar" id="rs-14-bar" style="width:75%"></div>
        </div>
      </div>
    </div>
    <div class="rs-14__pixels-label">⬛ POWER LEVEL ⬛</div>
    <div class="rs-14__track-wrap">
      <div class="rs-14__track-bg">
        <div class="rs-14__track-fill" id="rs-14-fill" style="width:75%"></div>
      </div>
      <input class="rs-14__input" type="range" min="0" max="100" value="75" id="rs-14-inp">
    </div>
    <div class="rs-14__coins" id="rs-14-coins"></div>
    <div class="rs-14__btns">
      <button class="rs-14__btn rs-14__btn--red" onclick="document.getElementById('rs-14-inp').value=0;document.getElementById('rs-14-inp').dispatchEvent(new Event('input'))">☠ DEAD</button>
      <button class="rs-14__btn rs-14__btn--gold" onclick="document.getElementById('rs-14-inp').value=100;document.getElementById('rs-14-inp').dispatchEvent(new Event('input'))">★ MAX HP</button>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-14,
.rs-14 *,
.rs-14 *::before,
.rs-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  image-rendering: pixelated;
}

.rs-14 ::selection {
  background: #ff0044;
  color: #fff;
}

.rs-14 {
  --bg: #1a1c2c;
  --card: #29293d;
  --border: #44445a;
  --gold: #f5a623;
  --red: #ff0044;
  --green: #00e676;
  --blue: #29adff;
  --text: #ffffff;
  --muted: #8080a0;
  --pixel: 3px;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: 'Courier New', 'Press Start 2P', monospace;
}

.rs-14__arcade {
  background: var(--card);
  border: var(--pixel) solid var(--border);
  box-shadow: var(--pixel) 0 0 var(--border), 0 var(--pixel) 0 var(--border), calc(var(--pixel)*2) var(--pixel) 0 rgba(0,0,0,0.5);
  max-width: 420px;
  width: 100%;
  padding: 28px;
}

.rs-14__scanlines {
  position: relative;
}

.rs-14__scanlines::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px);
  pointer-events: none;
  z-index: 1;
}

.rs-14__screen {
  background: #0d0d1a;
  border: 3px solid #000;
  box-shadow: inset 0 0 20px rgba(0,0,0,0.8), 0 0 30px rgba(41,173,255,0.15);
  padding: 20px;
  margin-bottom: 20px;
  min-height: 80px;
  display: flex;
  align-items: center;
  gap: 16px;
}

.rs-14__sprite {
  font-size: 40px;
  line-height: 1;
  flex-shrink: 0;
  animation: rs-14-bob 0.6s steps(2) infinite;
}

@keyframes rs-14-bob {
  0% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-4px);
  }

  100% {
    transform: translateY(0);
  }
}

.rs-14__hud {
  flex: 1;
}

.rs-14__hud-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}

.rs-14__hud-label {
  font-size: 10px;
  color: var(--muted);
  letter-spacing: 1px;
  text-transform: uppercase;
}

.rs-14__hud-val {
  font-size: 16px;
  font-weight: 700;
  color: var(--gold);
  font-variant-numeric: tabular-nums;
}

.rs-14__hp-bar-wrap {
  background: #000;
  border: 2px solid #333;
  height: 14px;
  position: relative;
  overflow: hidden;
}

.rs-14__hp-bar {
  height: 100%;
  background: var(--green);
  transition: width 0.05s steps(1), background 0.15s;
  box-shadow: inset 0 2px 0 rgba(255,255,255,0.3);
}

.rs-14__pixels-label {
  font-size: 9px;
  color: var(--muted);
  text-align: center;
  letter-spacing: 2px;
  margin-bottom: 12px;
  text-transform: uppercase;
}

.rs-14__track-wrap {
  position: relative;
  margin-bottom: 12px;
}

.rs-14__track-bg {
  height: 20px;
  background: #000;
  border: 3px solid #333;
  position: relative;
  overflow: hidden;
}

.rs-14__track-fill {
  height: 100%;
  background: repeating-linear-gradient(
      90deg,
      var(--blue) 0px,
      var(--blue) 12px,
      transparent 12px,
      transparent 16px
    );
  transition: width 0.05s steps(1);
}

.rs-14__input {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  -webkit-appearance: none;
  appearance: none;
  background: transparent;
  cursor: pointer;
  outline: none;
  z-index: 2;
}

.rs-14__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 26px;
  background: var(--gold);
  border: none;
  box-shadow: 3px 3px 0 #000, -1px -1px 0 rgba(255,255,255,0.5);
  cursor: ew-resize;
  clip-path: polygon(20% 0, 80% 0, 100% 20%, 100% 80%, 80% 100%, 20% 100%, 0 80%, 0 20%);
}

.rs-14__input::-moz-range-thumb {
  width: 20px;
  height: 26px;
  border-radius: 0;
  background: var(--gold);
  border: 3px solid #000;
  cursor: ew-resize;
}

.rs-14__coins {
  display: flex;
  gap: 6px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 16px;
}

.rs-14__coin {
  font-size: 18px;
  filter: grayscale(1) brightness(0.5);
  transition: filter 0.15s;
}

.rs-14__coin.on {
  filter: grayscale(0) drop-shadow(0 0 4px var(--gold));
}

.rs-14__btns {
  display: flex;
  gap: 8px;
  margin-top: 16px;
}

.rs-14__btn {
  flex: 1;
  padding: 10px 8px;
  font-family: inherit;
  font-size: 9px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  border: 3px solid #000;
  box-shadow: 3px 3px 0 #000;
  cursor: pointer;
  transition: transform 0.1s, box-shadow 0.1s;
  color: #fff;
}

.rs-14__btn:active {
  transform: translate(2px,2px);
  box-shadow: 1px 1px 0 #000;
}

.rs-14__btn--red {
  background: var(--red);
}

.rs-14__btn--gold {
  background: var(--gold);
  color: #000;
}

@media (prefers-reduced-motion: reduce) {
  .rs-14__sprite {
    animation: none;
  }

  .rs-14__track-fill,
    .rs-14__hp-bar {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-14-inp');
  const fill = document.getElementById('rs-14-fill');
  const bar = document.getElementById('rs-14-bar');
  const hp = document.getElementById('rs-14-hp');
  const sprite = document.getElementById('rs-14-sprite');
  const coinsEl = document.getElementById('rs-14-coins');
  const COINS = 10;
  const spriteMap = [[0,20,'💀'],[21,40,'😵'],[41,60,'😤'],[61,80,'⚔️'],[81,100,'🔱']];
  for(let i=0;i<COINS;i++){
    const c = document.createElement('div');
    c.className='rs-14__coin'; c.textContent='🪙';
    coinsEl.appendChild(c);
  }
  function update(){
    const v = +inp.value;
    fill.style.width = v+'%';
    bar.style.width = v+'%';
    hp.textContent = v+' / 100';
    bar.style.background = v<30 ? 'var(--red)' : v<60 ? 'var(--gold)' : 'var(--green)';
    const sp = spriteMap.find(([mn,mx])=>v>=mn&&v<=mx);
    if(sp) sprite.textContent = sp[2];
    const activeCoins = Math.round(v/100*COINS);
    coinsEl.querySelectorAll('.rs-14__coin').forEach((c,i)=>c.classList.toggle('on',i<activeCoins));
  }
  inp.addEventListener('input', update);
  update();
})();
```
