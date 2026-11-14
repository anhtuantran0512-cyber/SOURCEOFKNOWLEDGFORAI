---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/custom-emoji-mood-selector/"
title: "Custom Emoji Mood Selector"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "An interactive feedback slider that transitions between five emoji states from sad to ecstatic, with a pulsing ring animation, smooth background color…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom Emoji Mood Selector
Source: https://codefronts.com/components/css-range-sliders/custom-emoji-mood-selector/

An interactive feedback slider that transitions between five emoji states from sad to ecstatic, with a pulsing ring animation, smooth background color shifts, and a live star rating synced to the mood.
## HTML
```html
<div class="rs-04">
  <div class="rs-04__card">
    <div class="rs-04__heading">How do you feel today?</div>
    <div class="rs-04__sub">Drag to rate your experience</div>
    <div class="rs-04__emoji-wrap">
      <div class="rs-04__pulse" id="rs-04-pulse"></div>
      <div class="rs-04__face" id="rs-04-face">😐</div>
    </div>
    <div class="rs-04__mood-text" id="rs-04-mood-text" style="color:#f6d365">Neutral</div>
    <div class="rs-04__mood-sub" id="rs-04-mood-sub">Could be better, could be worse</div>
    <div class="rs-04__track-wrap">
      <div class="rs-04__track-bg"></div>
      <input class="rs-04__input" type="range" min="0" max="100" value="50" id="rs-04-inp">
    </div>
    <div class="rs-04__emojis-row">
      <span>😢</span><span>😕</span><span>😐</span><span>😊</span><span>😎</span>
    </div>
    <div class="rs-04__star-row" id="rs-04-stars">
      <span class="rs-04__star">⭐</span>
      <span class="rs-04__star">⭐</span>
      <span class="rs-04__star">⭐</span>
      <span class="rs-04__star">⭐</span>
      <span class="rs-04__star">⭐</span>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-04,
.rs-04 *,
.rs-04 *::before,
.rs-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-04 ::selection {
  background: #ff6b35;
  color: #fff;
}

.rs-04 {
  --bg: #1a0a2e;
  --card: #241242;
  --border: #3d2070;
  --sad: #667eea;
  --ok: #f6d365;
  --happy: #ff6b35;
  --text: #f0e6ff;
  --muted: #7c5cad;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-04__card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 36px 32px;
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.rs-04__heading {
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.rs-04__sub {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 36px;
}

.rs-04__emoji-wrap {
  position: relative;
  width: 100px;
  height: 100px;
  margin: 0 auto 28px;
}

.rs-04__face {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 62px;
  line-height: 1;
  transition: background 0.4s, transform 0.3s;
  background: rgba(255,255,255,0.06);
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
  position: relative;
}

.rs-04__pulse {
  position: absolute;
  inset: -8px;
  border-radius: 50%;
  border: 2px solid currentColor;
  opacity: 0;
  transition: color 0.4s;
  animation: rs-04-pulse 1.8s ease-out infinite;
}

@keyframes rs-04-pulse {
  0% {
    transform: scale(0.9);
    opacity: 0.6;
  }

  100% {
    transform: scale(1.3);
    opacity: 0;
  }
}

.rs-04__mood-text {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -0.5px;
  transition: color 0.4s;
  margin-bottom: 4px;
}

.rs-04__mood-sub {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 32px;
}

.rs-04__track-wrap {
  position: relative;
  padding: 14px 0;
  margin-bottom: 16px;
}

.rs-04__track-bg {
  height: 10px;
  border-radius: 99px;
  background: linear-gradient(90deg, var(--sad), var(--ok), var(--happy));
  opacity: 0.3;
}

.rs-04__input {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  -webkit-appearance: none;
  appearance: none;
  background: transparent;
  cursor: pointer;
  outline: none;
}

.rs-04__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid #ccc;
  box-shadow: 0 4px 16px rgba(0,0,0,0.4);
  transition: border-color 0.3s, transform 0.15s;
}

.rs-04__input:active::-webkit-slider-thumb {
  transform: scale(1.2);
}

.rs-04__input::-moz-range-thumb {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 3px solid #ccc;
  background: #fff;
  box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}

.rs-04__emojis-row {
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  opacity: 0.5;
}

.rs-04__star-row {
  display: flex;
  justify-content: center;
  gap: 6px;
  margin-top: 20px;
}

.rs-04__star {
  font-size: 20px;
  filter: grayscale(1);
  transition: filter 0.3s, transform 0.2s;
}

.rs-04__star.on {
  filter: grayscale(0);
  transform: scale(1.2);
}

@media (prefers-reduced-motion: reduce) {
  .rs-04__pulse {
    animation: none;
  }

  .rs-04__face,
    .rs-04__mood-text,
    .rs-04__star {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-04-inp');
  const face = document.getElementById('rs-04-face');
  const pulse = document.getElementById('rs-04-pulse');
  const moodText = document.getElementById('rs-04-mood-text');
  const moodSub = document.getElementById('rs-04-mood-sub');
  const stars = document.querySelectorAll('.rs-04__star');
  const moods = [
    { emoji:'😢', text:'Terrible', sub:'This really isn\'t my day', color:'#667eea' },
    { emoji:'😕', text:'Not Great', sub:'Struggling a bit today', color:'#a78bfa' },
    { emoji:'😐', text:'Neutral', sub:'Could be better, could be worse', color:'#f6d365' },
    { emoji:'😊', text:'Good', sub:'Things are looking up!', color:'#fb923c' },
    { emoji:'😎', text:'Amazing!', sub:'Absolutely crushing it today', color:'#ff6b35' },
  ];
  function update(){
    const v = +inp.value;
    const idx = Math.min(4, Math.floor(v/100*5));
    const m = moods[idx];
    face.textContent = m.emoji;
    face.style.background = m.color+'22';
    pulse.style.color = m.color;
    moodText.style.color = m.color;
    moodText.textContent = m.text;
    moodSub.textContent = m.sub;
    const activeStars = Math.round(v/100*5);
    stars.forEach((s,i)=> s.classList.toggle('on', i < activeStars));
  }
  inp.addEventListener('input', update);
  update();
})();
```
