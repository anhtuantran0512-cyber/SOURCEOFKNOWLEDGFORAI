---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-audio-player-ui/"
title: "Liquid Glass Audio Player UI"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "The 'Apple Music' floating playbar: a compact glass player sitting over blurred album art that it samples, with frosted play/pause/skip buttons and a…"
has_js: "true"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Audio Player UI
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-audio-player-ui/

The 'Apple Music' floating playbar: a compact glass player sitting over blurred album art that it samples, with frosted play/pause/skip buttons and a translucent progress bar. The backdrop tint shifts to match the current track's art. Light Vanilla JS drives playback state.
## HTML
```html
<section class="lg-12" id="lg-12-root" aria-label="Liquid glass audio player">
  <div class="lg-12__player">
    <div class="lg-12__art" id="lg-12-art" aria-hidden="true"></div>
    <div class="lg-12__body">
      <p class="lg-12__track" id="lg-12-track" aria-live="polite">Neon Tide — Aurora</p>
      <input class="lg-12__seek" id="lg-12-seek" type="range" min="0" max="100" value="30" aria-label="Seek">
      <div class="lg-12__times"><span id="lg-12-cur">1:04</span><span>3:32</span></div>
      <div class="lg-12__ctrls">
        <button class="lg-12__btn" id="lg-12-prev" type="button" aria-label="Previous track">⏮</button>
        <button class="lg-12__btn lg-12__btn--play" id="lg-12-play" type="button" aria-label="Play" aria-pressed="false">▶</button>
        <button class="lg-12__btn" id="lg-12-next" type="button" aria-label="Next track">⏭</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.lg-12,
.lg-12 *,
.lg-12 *::before,
.lg-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-12 {
  --accent: oklch(0.68 0.18 300);
  --art: url('https://picsum.photos/seed/lgaudio1/400/400');
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #0c0a16;
}

.lg-12__player {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: flex;
  gap: 18px;
  align-items: center;
  width: min(440px,94vw);
  padding: 18px;
  border-radius: 26px;
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 30px 60px -30px rgba(0,0,0,.7);
  background: color-mix(in oklab,white 8%,transparent);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
}

.lg-12__player::before {
  content: "";
  position: absolute;
  inset: -40%;
  z-index: -1;
  background: var(--art) center/cover;
  filter: blur(40px) saturate(160%) brightness(.7);
  transform: scale(1.2);
}

.lg-12__art {
  width: 84px;
  height: 84px;
  flex: none;
  border-radius: 16px;
  background: var(--art) center/cover;
  box-shadow: 0 10px 24px -10px rgba(0,0,0,.7),inset 0 0 0 1px rgba(255,255,255,.25);
}

.lg-12__body {
  flex: 1;
  min-width: 0;
}

.lg-12__track {
  font-size: 15px;
  font-weight: 800;
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 10px;
}

.lg-12__seek {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 6px;
  border-radius: 999px;
  background: linear-gradient(90deg,#fff calc(var(--p,30)*1%),rgba(255,255,255,.25) 0);
  cursor: pointer;
  outline: none;
}

.lg-12__seek::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,.5),0 0 0 4px color-mix(in oklab,var(--accent) 60%,transparent);
}

.lg-12__seek::-moz-range-thumb {
  width: 15px;
  height: 15px;
  border: none;
  border-radius: 50%;
  background: #fff;
}

.lg-12__seek:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

.lg-12__times {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: rgba(255,255,255,.7);
  margin: 6px 0 12px;
}

.lg-12__ctrls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}

.lg-12__btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,.3);
  cursor: pointer;
  font-size: 15px;
  color: #fff;
  background: rgba(255,255,255,.14);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transition: transform .15s,background .2s;
}

.lg-12__btn--play {
  width: 52px;
  height: 52px;
  font-size: 18px;
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 85%,white),var(--accent));
  border-color: color-mix(in oklab,var(--accent) 40%,white);
}

.lg-12__btn:hover {
  transform: scale(1.08);
  background: rgba(255,255,255,.24);
}

.lg-12__btn--play:hover {
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 75%,white),var(--accent));
}

.lg-12__btn:active {
  transform: scale(.94);
}

.lg-12__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-12__btn {
    transition: background .2s;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lg-12-root');
  const play = root.querySelector('#lg-12-play');
  const seek = root.querySelector('#lg-12-seek');
  const cur = root.querySelector('#lg-12-cur');
  const trackEl = root.querySelector('#lg-12-track');
  const player = root.querySelector('.lg-12__player');
  const tracks = [
    {t:'Neon Tide — Aurora', art:"url('https://picsum.photos/seed/lgaudio1/400/400')", a:'oklch(0.68 0.18 300)'},
    {t:'Slow Static — Kioto', art:"url('https://picsum.photos/seed/lgaudio2/400/400')", a:'oklch(0.7 0.17 200)'},
    {t:'Amber Room — Vell', art:"url('https://picsum.photos/seed/lgaudio3/400/400')", a:'oklch(0.72 0.17 60)'}
  ];
  let i = 0, playing = false, p = 30, timer = null;
  const DUR = 212;
  const fmt = s => Math.floor(s/60)+':'+String(Math.floor(s%60)).padStart(2,'0');
  function paint(){ root.style.setProperty('--p', p); seek.value = p; cur.textContent = fmt(p/100*DUR); }
  function tick(){ p = Math.min(100, p + 100/DUR); paint(); if (p>=100){ next(); } }
  function toggle(){ playing = !playing; play.textContent = playing ? '❚❚' : '▶'; play.setAttribute('aria-label', playing?'Pause':'Play'); play.setAttribute('aria-pressed', playing); clearInterval(timer); if (playing) timer = setInterval(tick, 1000); }
  function load(){ const tk = tracks[i]; trackEl.textContent = tk.t; root.style.setProperty('--art', tk.art); root.style.setProperty('--accent', tk.a); p = 0; paint(); }
  function next(){ i = (i+1)%tracks.length; load(); }
  function prev(){ i = (i-1+tracks.length)%tracks.length; load(); }
  play.addEventListener('click', toggle);
  root.querySelector('#lg-12-next').addEventListener('click', next);
  root.querySelector('#lg-12-prev').addEventListener('click', prev);
  seek.addEventListener('input', () => { p = +seek.value; paint(); });
  paint();
})();
```
