---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/refractive-music-player-widget/"
title: "Refractive Music Player Widget"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A now-playing media widget where the album art is blown up and blurred as the backdrop, then bleeds through a frosted Liquid Glass front panel that holds the…"
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Refractive Music Player Widget
Source: https://codefronts.com/components/css-liquid-glass-cards/refractive-music-player-widget/

A now-playing media widget where the album art is blown up and blurred as the backdrop, then bleeds through a frosted Liquid Glass front panel that holds the controls — the exact 'album art through glass' look from iOS lock-screen players. A working progress scrubber and play/pause morph included.
## HTML
```html
<section class="lg-07" aria-label="Refractive music player widget demo">
  <article class="lg-07__card">
    <div class="lg-07__bg" aria-hidden="true"></div>
    <div class="lg-07__panel">
      <div class="lg-07__art" role="img" aria-label="Album art: Neon Tides by Halcyon"><span class="lg-07__note" aria-hidden="true">♫</span></div>
      <div class="lg-07__meta"><h3 class="lg-07__track">Neon Tides</h3><p class="lg-07__artist">Halcyon</p></div>
      <div class="lg-07__scrub" id="lg-07-scrub" role="slider" tabindex="0" aria-label="Seek" aria-valuemin="0" aria-valuemax="100" aria-valuenow="30"><span class="lg-07__fill"></span></div>
      <div class="lg-07__time"><span id="lg-07-cur">1:12</span><span>3:58</span></div>
      <div class="lg-07__ctrls">
        <button class="lg-07__b" type="button" aria-label="Previous">⏮</button>
        <button class="lg-07__b lg-07__b--play" id="lg-07-play" type="button" aria-pressed="false" aria-label="Play">▶</button>
        <button class="lg-07__b" type="button" aria-label="Next">⏭</button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-07,
.lg-07 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-07 {
  --accent: oklch(0.75 0.16 20);
  --art: repeating-linear-gradient(135deg,#f43f5e,#f43f5e 16px,#fb7185 16px,#fb7185 32px,#a21caf 32px,#a21caf 48px);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #1a1024;
}

.lg-07__card {
  position: relative;
  width: min(300px,100%);
  border-radius: 28px;
  overflow: hidden;
  isolation: isolate;
  box-shadow: 0 34px 70px -28px rgba(0,0,0,.85);
  border: 1px solid rgba(255,255,255,.2);
}

.lg-07__bg {
  position: absolute;
  inset: -30%;
  background: var(--art);
  filter: blur(34px) saturate(160%) brightness(.9);
  transform: scale(1.3);
}

.lg-07__panel {
  position: relative;
  padding: 22px;
  background: color-mix(in oklab,black 22%,transparent);
  backdrop-filter: blur(24px) saturate(200%);
  -webkit-backdrop-filter: blur(24px) saturate(200%);
  border-top: 1px solid rgba(255,255,255,.18);
}

.lg-07__art {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 16px;
  background: var(--art);
  display: grid;
  place-items: center;
  box-shadow: 0 16px 34px -14px rgba(0,0,0,.7);
  border: 1px solid rgba(255,255,255,.25);
}

.lg-07__note {
  font-size: 44px;
  color: rgba(255,255,255,.85);
}

.lg-07__meta {
  margin: 16px 0 12px;
}

.lg-07__track {
  color: #fff;
  font-size: 20px;
  font-weight: 800;
}

.lg-07__artist {
  color: rgba(255,255,255,.75);
  font-size: 14px;
  margin-top: 2px;
}

.lg-07__scrub {
  position: relative;
  height: 6px;
  border-radius: 999px;
  background: rgba(255,255,255,.22);
  cursor: pointer;
}

.lg-07__scrub:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

.lg-07__fill {
  position: absolute;
  inset: 0;
  width: calc(var(--prog,30%) );
  max-width: 100%;
  border-radius: 999px;
  background: var(--accent);
  box-shadow: 0 0 10px color-mix(in oklab,var(--accent) 70%,transparent);
}

.lg-07__time {
  display: flex;
  justify-content: space-between;
  color: rgba(255,255,255,.7);
  font-size: 12px;
  margin-top: 7px;
  font-variant-numeric: tabular-nums;
}

.lg-07__ctrls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  margin-top: 14px;
}

.lg-07__b {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  border: 0;
  cursor: pointer;
  font-size: 18px;
  color: #fff;
  background: rgba(255,255,255,.14);
  display: grid;
  place-items: center;
  transition: transform .2s,background .2s;
}

.lg-07__b:hover {
  background: rgba(255,255,255,.24);
  transform: scale(1.06);
}

.lg-07__b:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-07__b--play {
  width: 58px;
  height: 58px;
  font-size: 22px;
  background: var(--accent);
  box-shadow: 0 10px 24px -8px var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .lg-07__b {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const play = document.querySelector('#lg-07-play');
  const scrub = document.querySelector('#lg-07-scrub');
  const fill = scrub && scrub.querySelector('.lg-07__fill');
  const cur = document.querySelector('#lg-07-cur');
  if (!play) return;
  let playing = false, prog = 30, timer;
  const DUR = 238;
  const fmt = (s) => Math.floor(s/60) + ':' + String(Math.floor(s%60)).padStart(2,'0');
  const render = () => { fill.style.setProperty('--prog', prog + '%'); scrub.setAttribute('aria-valuenow', Math.round(prog)); cur.textContent = fmt(prog/100*DUR); };
  play.addEventListener('click', () => {
    playing = !playing;
    play.setAttribute('aria-pressed', String(playing));
    play.setAttribute('aria-label', playing ? 'Pause' : 'Play');
    play.textContent = playing ? '❚❚' : '▶';
    clearInterval(timer);
    if (playing) timer = setInterval(() => { prog = (prog + 0.4) % 100; render(); }, 100);
  });
  const seek = (e) => { const r = scrub.getBoundingClientRect(); prog = Math.max(0, Math.min(100, (e.clientX - r.left)/r.width*100)); render(); };
  scrub.addEventListener('pointerdown', seek);
  scrub.addEventListener('keydown', (e) => { if (e.key==='ArrowRight'){prog=Math.min(100,prog+5);render();} if (e.key==='ArrowLeft'){prog=Math.max(0,prog-5);render();} });
  render();
})();
```
