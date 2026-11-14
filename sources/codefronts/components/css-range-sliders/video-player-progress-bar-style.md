---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/video-player-progress-bar-style/"
title: "Video Player Progress Bar Style"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A premium streaming-style video seekbar with a hidden thumb that blooms on hover, a translucent timecode tooltip that tracks the thumb, a buffer indicator…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Player Progress Bar Style
Source: https://codefronts.com/components/css-range-sliders/video-player-progress-bar-style/

A premium streaming-style video seekbar with a hidden thumb that blooms on hover, a translucent timecode tooltip that tracks the thumb, a buffer indicator layer, and a full player control bar.
## HTML
```html
<div class="rs-06">
  <div class="rs-06__player">
    <div class="rs-06__thumbnail">
      <div class="rs-06__play-btn" id="rs-06-playbtn">
        <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
      </div>
      <div class="rs-06__film-title">Neon Horizon</div>
      <div class="rs-06__film-sub">2024 · Drama · 2h 07m</div>
    </div>
    <div class="rs-06__controls">
      <div class="rs-06__seekbar" id="rs-06-seekbar">
        <div class="rs-06__track-bg"></div>
        <div class="rs-06__track-buffer" id="rs-06-buffer"></div>
        <div class="rs-06__track-fill" id="rs-06-fill" style="width:32%"></div>
        <input class="rs-06__input" type="range" min="0" max="7620" value="2438" id="rs-06-inp">
        <div class="rs-06__thumb" id="rs-06-thumb" style="left:32%"></div>
        <div class="rs-06__tooltip" id="rs-06-tip" style="left:32%">00:40:38</div>
      </div>
      <div class="rs-06__bottom">
        <div class="rs-06__left-ctrl">
          <button class="rs-06__ctrl-btn" aria-label="Play">
            <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
          </button>
          <button class="rs-06__ctrl-btn" aria-label="Skip">
            <svg viewBox="0 0 24 24"><polygon points="5,4 15,12 5,20"/><line x1="19" y1="5" x2="19" y2="19" stroke="currentColor" stroke-width="2"/></svg>
          </button>
          <div class="rs-06__vol-wrap">
            <button class="rs-06__ctrl-btn" aria-label="Volume">
              <svg viewBox="0 0 24 24"><polygon points="11,5 6,9 2,9 2,15 6,15 11,19"/><path d="M19.07,4.93a10,10,0,0,1,0,14.14M15.54,8.46a5,5,0,0,1,0,7.07" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>
            </button>
            <input class="rs-06__vol-input" type="range" min="0" max="100" value="80">
          </div>
          <div class="rs-06__time"><span id="rs-06-cur">40:38</span> / 2:07:00</div>
        </div>
        <button class="rs-06__ctrl-btn" aria-label="Fullscreen">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15,3 21,3 21,9"/><polyline points="9,21 3,21 3,15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-06,
.rs-06 *,
.rs-06 *::before,
.rs-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-06 ::selection {
  background: #e50914;
  color: #fff;
}

.rs-06 {
  --bg: #141414;
  --card: #1f1f1f;
  --red: #e50914;
  --red-glow: rgba(229,9,20,0.4);
  --text: #ffffff;
  --muted: #808080;
  --track-h: 4px;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-06__player {
  width: 100%;
  max-width: 520px;
  background: var(--card);
  border-radius: 12px;
  overflow: hidden;
}

.rs-06__thumbnail {
  width: 100%;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #0d0d0d 0%, #1a0a0a 40%, #2d0000 70%, #0d0d0d 100%);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  overflow: hidden;
}

.rs-06__thumbnail::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at center, rgba(229,9,20,0.06) 0%, transparent 70%);
}

.rs-06__film-title {
  position: absolute;
  bottom: 20px;
  left: 20px;
  color: #fff;
  font-size: 20px;
  font-weight: 800;
  text-shadow: 0 2px 12px rgba(0,0,0,0.8);
}

.rs-06__film-sub {
  position: absolute;
  bottom: 6px;
  left: 20px;
  color: var(--muted);
  font-size: 12px;
}

.rs-06__play-btn {
  width: 64px;
  height: 64px;
  background: rgba(229,9,20,0.85);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s, transform 0.2s;
  cursor: pointer;
  box-shadow: 0 0 40px var(--red-glow);
}

.rs-06__play-btn:hover {
  background: var(--red);
  transform: scale(1.08);
}

.rs-06__play-btn svg {
  width: 26px;
  height: 26px;
  fill: #fff;
  margin-left: 4px;
}

.rs-06__controls {
  padding: 12px 16px 16px;
}

.rs-06__seekbar {
  position: relative;
  height: 20px;
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  cursor: pointer;
}

.rs-06__seekbar:hover .rs-06__track-fill {
  background: var(--red);
}

.rs-06__seekbar:hover .rs-06__thumb {
  opacity: 1;
  transform: translateY(-50%) translateX(-50%) scale(1);
}

.rs-06__track-bg {
  position: absolute;
  width: 100%;
  height: var(--track-h);
  background: rgba(255,255,255,0.2);
  border-radius: 99px;
}

.rs-06__track-buffer {
  position: absolute;
  left: 0;
  height: var(--track-h);
  background: rgba(255,255,255,0.35);
  border-radius: 99px;
  width: 60%;
}

.rs-06__track-fill {
  position: absolute;
  left: 0;
  height: var(--track-h);
  background: var(--muted);
  border-radius: 99px;
  transition: background 0.2s, width 0.05s;
}

.rs-06__input {
  position: absolute;
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  height: 20px;
  background: transparent;
  cursor: pointer;
  outline: none;
  z-index: 2;
}

.rs-06__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 0;
  height: 0;
}

.rs-06__thumb {
  position: absolute;
  width: 14px;
  height: 14px;
  background: #fff;
  border-radius: 50%;
  top: 50%;
  left: 0;
  transform: translateY(-50%) translateX(-50%) scale(0);
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s, transform 0.2s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.5);
}

.rs-06__tooltip {
  position: absolute;
  bottom: calc(100% + 8px);
  transform: translateX(-50%);
  background: rgba(20,20,20,0.9);
  color: #fff;
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 4px;
  pointer-events: none;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.2s;
  backdrop-filter: blur(4px);
}

.rs-06__seekbar:hover .rs-06__tooltip {
  opacity: 1;
}

.rs-06__bottom {
  display: flex;
  align-items: center;
  gap: 12px;
  justify-content: space-between;
}

.rs-06__left-ctrl {
  display: flex;
  align-items: center;
  gap: 10px;
}

.rs-06__ctrl-btn {
  background: none;
  border: none;
  color: #fff;
  cursor: pointer;
  padding: 4px;
  opacity: 0.8;
  transition: opacity 0.15s;
  display: flex;
  align-items: center;
}

.rs-06__ctrl-btn:hover {
  opacity: 1;
}

.rs-06__ctrl-btn svg {
  width: 20px;
  height: 20px;
  fill: currentColor;
}

.rs-06__time {
  font-size: 12px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.rs-06__time span {
  color: #fff;
}

.rs-06__vol-wrap {
  display: flex;
  align-items: center;
  gap: 6px;
}

.rs-06__vol-input {
  width: 60px;
  -webkit-appearance: none;
  appearance: none;
  height: 3px;
  background: rgba(255,255,255,0.3);
  border-radius: 99px;
  outline: none;
  cursor: pointer;
}

.rs-06__vol-input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .rs-06__track-fill,
    .rs-06__thumb,
    .rs-06__tooltip {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-06-inp');
  const fill = document.getElementById('rs-06-fill');
  const thumb = document.getElementById('rs-06-thumb');
  const tip = document.getElementById('rs-06-tip');
  const cur = document.getElementById('rs-06-cur');
  function fmt(s){ const m=Math.floor(s/60), sec=Math.floor(s%60); return m+':'+(sec<10?'0':'')+sec; }
  function update(){
    const v = +inp.value;
    const pct = v/inp.max*100;
    fill.style.width = pct+'%';
    thumb.style.left = pct+'%';
    tip.style.left = pct+'%';
    tip.textContent = fmt(v);
    cur.textContent = fmt(v);
  }
  inp.addEventListener('input', update);
  update();
})();
```
