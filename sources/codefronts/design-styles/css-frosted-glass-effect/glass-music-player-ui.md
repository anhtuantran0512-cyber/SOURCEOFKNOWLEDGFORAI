---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/glass-music-player-ui/"
title: "Glass Music Player UI"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A floating glass music player that blurs a rich purple-coral \"album art\" gradient behind it."
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Music Player UI
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/glass-music-player-ui/

A floating glass music player that blurs a rich purple-coral "album art" gradient behind it. Features a rotating vinyl disc that spins when playing, animated progress bar, track cycling with skip buttons, like toggle, and shuffle/repeat controls.
## HTML
```html
<div class="fg-13">
  <div class="fg-08__art-bg" aria-hidden="true">
    <div class="fg-08__orb fg-08__orb--1"></div>
    <div class="fg-08__orb fg-08__orb--2"></div>
    <div class="fg-08__orb fg-08__orb--3"></div>
  </div>
  <div class="fg-08__player" role="region" aria-label="Music player">
    <div class="fg-08__disc-wrap" aria-hidden="true">
      <div class="fg-08__disc" id="fg-13-disc">
        <div class="fg-08__disc-ring fg-08__disc-ring--1"></div>
        <div class="fg-08__disc-ring fg-08__disc-ring--2"></div>
        <div class="fg-08__disc-center"></div>
        <div class="fg-08__disc-dot"></div>
      </div>
    </div>
    <div class="fg-08__info">
      <div class="fg-08__track-row">
        <div>
          <p class="fg-08__track" id="fg-13-track">Neon Horizons</p>
          <p class="fg-08__artist" id="fg-13-artist">Echo Pulse</p>
        </div>
        <button class="fg-08__like" id="fg-13-like" aria-label="Like track">
          <svg class="fg-08__like-e" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
          <svg class="fg-08__like-f" width="18" height="18" viewBox="0 0 24 24" fill="#f87171" stroke="#f87171" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
        </button>
      </div>
      <div class="fg-08__prog-wrap">
        <div class="fg-08__prog-bar" aria-label="Playback progress"><div class="fg-08__prog-fill" id="fg-13-prog"></div></div>
        <div class="fg-08__times"><span id="fg-13-cur">0:00</span><span id="fg-13-dur">3:47</span></div>
      </div>
      <div class="fg-08__controls">
        <button class="fg-08__ctrl fg-08__ctrl--sm" id="fg-13-shuf" aria-label="Shuffle" aria-pressed="false">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/></svg>
        </button>
        <button class="fg-08__ctrl" id="fg-13-prev" aria-label="Previous track">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><polygon points="19 20 9 12 19 4 19 20"/><line x1="5" y1="19" x2="5" y2="5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </button>
        <button class="fg-08__ctrl fg-08__ctrl--play" id="fg-13-play" aria-label="Play" aria-pressed="false">
          <svg class="fg-08__play-icon" width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          <svg class="fg-08__pause-icon" width="22" height="22" viewBox="0 0 24 24" fill="currentColor" style="display:none"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>
        </button>
        <button class="fg-08__ctrl" id="fg-13-next" aria-label="Next track">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 4 15 12 5 20 5 4"/><line x1="19" y1="5" x2="19" y2="19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </button>
        <button class="fg-08__ctrl fg-08__ctrl--sm" id="fg-13-rep" aria-label="Repeat" aria-pressed="false">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
        </button>
      </div>
      <div class="fg-08__vol-wrap" aria-label="Volume">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>
        <div class="fg-08__vol-bar"><div class="fg-08__vol-fill"></div></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-13,
.fg-13 *,
.fg-13 *::before,
.fg-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-13 ::selection {
  background: rgba(167,139,250,.5);
  color: #fff;
}

.fg-13 {
  --c-bg: #0d0514;
  --c-a: #a855f7;
  --c-a2: #ec4899;
  --c-glass: rgba(255,255,255,.07);
  --c-border: rgba(255,255,255,.12);
  --c-text: #f0eeff;
  --c-muted: rgba(240,238,255,.5);
  --t: .25s ease;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--c-bg);
  position: relative;
  overflow: hidden;
  padding: 40px 20px;
}

.fg-08__art-bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-08__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(70px);
}

.fg-08__orb--1 {
  width: 380px;
  height: 380px;
  background: radial-gradient(circle,rgba(168,85,247,.5),transparent 70%);
  top: -80px;
  left: -60px;
  animation: fg-13-o1 18s ease-in-out infinite alternate;
}

.fg-08__orb--2 {
  width: 340px;
  height: 340px;
  background: radial-gradient(circle,rgba(236,72,153,.45),transparent 70%);
  bottom: -60px;
  right: -60px;
  animation: fg-13-o2 22s ease-in-out infinite alternate;
}

.fg-08__orb--3 {
  width: 260px;
  height: 260px;
  background: radial-gradient(circle,rgba(99,102,241,.35),transparent 70%);
  top: 40%;
  left: 40%;
  animation: fg-13-o3 15s ease-in-out infinite alternate;
}

@keyframes fg-13-o1 {
  to {
    transform: translate(60px,80px) scale(1.15);
  }
}

@keyframes fg-13-o2 {
  to {
    transform: translate(-50px,-60px) scale(1.1);
  }
}

@keyframes fg-13-o3 {
  to {
    transform: translate(-70px,50px) scale(.9);
  }
}

.fg-08__player {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 360px;
  background: var(--c-glass);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid var(--c-border);
  border-radius: 24px;
  padding: 24px;
  box-shadow: 0 8px 48px rgba(0,0,0,.5),0 1px 0 rgba(255,255,255,.12) inset;
}

.fg-08__disc-wrap {
  display: flex;
  justify-content: center;
  margin-bottom: 22px;
}

.fg-08__disc {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  background: conic-gradient(from 0deg,#1a0a2e,#2d1566,#1a0a2e,#0d0820,#2d1566,#1a0a2e);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255,255,255,.08);
  box-shadow: 0 0 40px rgba(168,85,247,.3),0 0 0 8px rgba(255,255,255,.03);
}

.fg-13.is-playing .fg-08__disc {
  animation: fg-13-spin 4s linear infinite;
}

@keyframes fg-13-spin {
  to {
    transform: rotate(360deg);
  }
}

.fg-08__disc-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,.06);
}

.fg-08__disc-ring--1 {
  width: 100px;
  height: 100px;
}

.fg-08__disc-ring--2 {
  width: 72px;
  height: 72px;
}

.fg-08__disc-center {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: radial-gradient(circle,#2a1060,#1a0840);
  border: 1px solid rgba(255,255,255,.1);
}

.fg-08__disc-dot {
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,.7);
}

.fg-08__info {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.fg-08__track-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.fg-08__track {
  font-size: 17px;
  font-weight: 800;
  color: var(--c-text);
  letter-spacing: -.2px;
  margin-bottom: 3px;
}

.fg-08__artist {
  font-size: 13px;
  color: var(--c-muted);
}

.fg-08__like {
  width: 36px;
  height: 36px;
  border: 1px solid var(--c-border);
  border-radius: 50%;
  background: rgba(255,255,255,.06);
  color: rgba(255,255,255,.6);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background var(--t),transform .15s;
  flex-shrink: 0;
}

.fg-08__like:hover {
  background: rgba(255,255,255,.12);
  transform: scale(1.08);
}

.fg-08__like-f {
  display: none;
}

.fg-08__prog-wrap {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.fg-08__prog-bar {
  height: 4px;
  border-radius: 2px;
  background: rgba(255,255,255,.1);
  cursor: pointer;
  overflow: hidden;
}

.fg-08__prog-fill {
  height: 100%;
  width: 0%;
  border-radius: 2px;
  background: linear-gradient(90deg,var(--c-a),var(--c-a2));
  transition: width .5s linear;
  box-shadow: 0 0 8px rgba(168,85,247,.5);
}

.fg-13.is-playing .fg-08__prog-fill {
  box-shadow: 0 0 12px rgba(168,85,247,.7);
}

.fg-08__times {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--c-muted);
}

.fg-08__controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.fg-08__ctrl {
  border: none;
  background: transparent;
  color: rgba(255,255,255,.6);
  cursor: pointer;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color var(--t),background var(--t),transform .15s;
}

.fg-08__ctrl:hover {
  color: var(--c-text);
  transform: scale(1.1);
}

.fg-08__ctrl--sm {
  width: 32px;
  height: 32px;
}

.fg-08__ctrl:not(.fg-08__ctrl--sm):not(.fg-08__ctrl--play) {
  width: 38px;
  height: 38px;
  background: rgba(255,255,255,.06);
  border: 1px solid var(--c-border);
}

.fg-08__ctrl--play {
  width: 52px;
  height: 52px;
  background: linear-gradient(135deg,var(--c-a),var(--c-a2));
  color: #fff;
  box-shadow: 0 4px 18px rgba(168,85,247,.5);
}

.fg-08__ctrl--play:hover {
  transform: scale(1.08);
  box-shadow: 0 6px 24px rgba(168,85,247,.65);
}

.fg-08__ctrl.is-active {
  color: var(--c-a);
}

.fg-08__vol-wrap {
  display: flex;
  align-items: center;
  gap: 10px;
}

.fg-08__vol-wrap svg {
  color: rgba(255,255,255,.4);
  flex-shrink: 0;
}

.fg-08__vol-bar {
  flex: 1;
  height: 3px;
  border-radius: 2px;
  background: rgba(255,255,255,.1);
}

.fg-08__vol-fill {
  width: 70%;
  height: 100%;
  border-radius: 2px;
  background: linear-gradient(90deg,var(--c-a),var(--c-a2));
}

@media (prefers-reduced-motion: reduce) {
  .fg-08__orb {
    animation: none;
  }

  .fg-13.is-playing .fg-08__disc {
    animation: none;
  }

  .fg-08__prog-fill,
    .fg-08__like,
    .fg-08__ctrl {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-13');
  if(!r)return;
  var tracks=[
    {title:'Neon Horizons',artist:'Echo Pulse',dur:'3:47',secs:227},
    {title:'Violet Static',artist:'Wavefold',dur:'4:12',secs:252},
    {title:'Glass Orbit',artist:'The Prism',dur:'3:28',secs:208}
  ];
  var idx=0,prog=0,playing=false,timer=null;
  var playBtn=r.querySelector('#fg-13-play');
  var playIcon=r.querySelector('.fg-08__play-icon');
  var pauseIcon=r.querySelector('.fg-08__pause-icon');
  var trackEl=r.querySelector('#fg-13-track');
  var artistEl=r.querySelector('#fg-13-artist');
  var durEl=r.querySelector('#fg-13-dur');
  var curEl=r.querySelector('#fg-13-cur');
  var fillEl=r.querySelector('#fg-13-prog');
  var likeBtn=r.querySelector('#fg-13-like');
  function fmt(s){return Math.floor(s/60)+':'+(s%60<10?'0':'')+Math.floor(s%60)}
  function loadTrack(){
    var t=tracks[idx];
    trackEl.textContent=t.title;artistEl.textContent=t.artist;
    durEl.textContent=t.dur;prog=0;fillEl.style.width='0%';curEl.textContent='0:00';
  }
  function tick(){
    prog=Math.min(prog+100/tracks[idx].secs*.5,100);
    fillEl.style.width=prog+'%';
    curEl.textContent=fmt(Math.round(prog/100*tracks[idx].secs));
    if(prog>=100){clearInterval(timer);playing=false;r.classList.remove('is-playing');playIcon.style.display='';pauseIcon.style.display='none';playBtn.setAttribute('aria-pressed','false')}
  }
  playBtn.addEventListener('click',function(){
    playing=!playing;
    if(playing){r.classList.add('is-playing');clearInterval(timer);timer=setInterval(tick,500);playIcon.style.display='none';pauseIcon.style.display=''}
    else{r.classList.remove('is-playing');clearInterval(timer);playIcon.style.display='';pauseIcon.style.display='none'}
    playBtn.setAttribute('aria-pressed',playing?'true':'false');
  });
  r.querySelector('#fg-13-next').addEventListener('click',function(){idx=(idx+1)%tracks.length;clearInterval(timer);playing=false;r.classList.remove('is-playing');playIcon.style.display='';pauseIcon.style.display='none';loadTrack()});
  r.querySelector('#fg-13-prev').addEventListener('click',function(){idx=(idx-1+tracks.length)%tracks.length;clearInterval(timer);playing=false;r.classList.remove('is-playing');playIcon.style.display='';pauseIcon.style.display='none';loadTrack()});
  r.querySelector('#fg-13-shuf').addEventListener('click',function(){this.classList.toggle('is-active')});
  r.querySelector('#fg-13-rep').addEventListener('click',function(){this.classList.toggle('is-active')});
  likeBtn.addEventListener('click',function(){
    var on=likeBtn.classList.toggle('is-liked');
    likeBtn.querySelector('.fg-08__like-e').style.display=on?'none':'';
    likeBtn.querySelector('.fg-08__like-f').style.display=on?'':'none';
  });
})();
```
