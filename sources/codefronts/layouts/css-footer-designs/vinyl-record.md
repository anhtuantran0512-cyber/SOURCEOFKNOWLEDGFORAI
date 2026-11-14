---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/vinyl-record/"
title: "CSS Audio Player & Music Website Footer"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The now-playing bar every music site lands on, built properly: a sticky bottom player with a real scrub range input styled across engines, an equaliser drawn…"
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Audio Player & Music Website Footer
Source: https://codefronts.com/layouts/css-footer-designs/vinyl-record/

The now-playing bar every music site lands on, built properly: a sticky bottom player with a real scrub range input styled across engines, an equaliser drawn in CSS, and controls that announce their state. Wire it to a real <audio> element with the four lines shown in the notes.
## HTML
```html
<section class="ft-16" aria-label="Audio player music footer demo">
  <main class="ft-16__main">
    <p class="ft-16__eyebrow">sticky bottom · range input · CSS equaliser</p>
    <h1 class="ft-16__title">Now playing, without a framework</h1>
    <p class="ft-16__sub">Press play. The clock, the scrub fill and the equaliser all run from one state flag — swap the simulated timer for an <code>&lt;audio&gt;</code> element and the same UI drives real playback.</p>
    <ul class="ft-16__tracks">
      <li class="ft-16__track"><span class="ft-16__tn">01</span><span class="ft-16__tt">Harbour Lights</span><span class="ft-16__td">3:55</span></li>
      <li class="ft-16__track"><span class="ft-16__tn">02</span><span class="ft-16__tt">Slow Ferry</span><span class="ft-16__td">4:21</span></li>
      <li class="ft-16__track"><span class="ft-16__tn">03</span><span class="ft-16__tt">Nightwatch (feat. Ora)</span><span class="ft-16__td">5:08</span></li>
    </ul>
  </main>
  <footer class="ft-16__foot">
    <div class="ft-16__player" data-playing="false" id="ft-16-player">
      <div class="ft-16__now">
        <span class="ft-16__art" aria-hidden="true"></span>
        <span class="ft-16__meta">
          <span class="ft-16__ttitle">Harbour Lights</span>
          <span class="ft-16__tartist">Kova &amp; the Long Room</span>
        </span>
        <span class="ft-16__eq" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>
      </div>
      <div class="ft-16__controls">
        <button class="ft-16__ctl" type="button" aria-label="Previous track"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true" focusable="false"><path d="M7 5h2.4v14H7zM19 5v14l-9-7z"/></svg></button>
        <button class="ft-16__play" type="button" id="ft-16-play" aria-pressed="false" aria-label="Play Harbour Lights">
          <svg class="ft-16__i-play" viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true" focusable="false"><path d="M8 5.2v13.6L19 12z"/></svg>
          <svg class="ft-16__i-pause" viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true" focusable="false"><path d="M7.5 5h3.2v14H7.5zM13.3 5h3.2v14h-3.2z"/></svg>
        </button>
        <button class="ft-16__ctl" type="button" aria-label="Next track"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true" focusable="false"><path d="M14.6 5H17v14h-2.4zM5 5v14l9-7z"/></svg></button>
      </div>
      <div class="ft-16__scrub">
        <span class="ft-16__time" id="ft-16-cur">0:00</span>
        <input class="ft-16__range" id="ft-16-range" type="range" min="0" max="235" value="0" step="1" aria-label="Seek within the track" aria-valuetext="0 seconds of 3 minutes 55 seconds">
        <span class="ft-16__time">3:55</span>
      </div>
      <div class="ft-16__extra">
        <button class="ft-16__ctl" type="button" aria-pressed="false" aria-label="Add to your library"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14"/></svg></button>
        <button class="ft-16__ctl" type="button" aria-label="Mute"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M11 5L6.5 9H3v6h3.5L11 19z"/><path d="M15.5 9.5a3.5 3.5 0 0 1 0 5M18 7a7 7 0 0 1 0 10"/></svg></button>
      </div>
      <p class="ft-16__live" id="ft-16-live" role="status" aria-live="polite"></p>
    </div>
    <div class="ft-16__links">
      <div class="ft-16__brand"><span class="ft-16__mark" aria-hidden="true"></span>Longroom</div>
      <nav class="ft-16__nav" aria-label="Footer"><a class="ft-16__link" href="#ft-16-a">Releases</a><a class="ft-16__link" href="#ft-16-a">Live dates</a><a class="ft-16__link" href="#ft-16-a">Merch</a><a class="ft-16__link" href="#ft-16-a">Licensing</a><a class="ft-16__link" href="#ft-16-a">Press</a></nav>
      <p class="ft-16__copy">© <time datetime="2026">2026</time> Longroom Recordings · all masters owned by the artists</p>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-16-bg);
  --ft-16-bg: oklch(0.15 0.02 300);
  --ft-16-foot: oklch(0.19 0.024 300);
  --ft-16-bar: oklch(0.23 0.028 300);
  --ft-16-ink: oklch(0.97 0.006 300);
  --ft-16-mut: oklch(0.73 0.016 300);
  --ft-16-acc: oklch(0.78 0.16 60);
  --ft-16-line: oklch(0.97 0.006 300/.14);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-16-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-16 *,
.ft-16 *::before,
.ft-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-16 ul {
  list-style: none;
}

.ft-16__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(38px,7.5vh,86px);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1080px)/2));
  background: radial-gradient(70% 60% at 15% 0%,oklch(0.32 0.1 60/.4),transparent);
}

.ft-16__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-16-acc);
}

.ft-16__title {
  font-size: clamp(29px,5.4vw,58px);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 14ch;
  text-wrap: balance;
}

.ft-16__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-16-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-16__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .86em;
  padding: 2px 6px;
  border-radius: 5px;
  background: oklch(0.97 0.006 300/.09);
}

.ft-16__tracks {
  display: grid;
  gap: 1px;
  margin-block-start: 10px;
  max-width: 34rem;
}

.ft-16__track {
  display: grid;
  grid-template-columns: 2.2rem 1fr auto;
  align-items: center;
  gap: 14px;
  min-height: 46px;
  padding: 0 12px;
  border-radius: 10px;
  font-size: 14.5px;
  transition: background .2s ease;
}

.ft-16__track:hover {
  background: oklch(0.97 0.006 300/.06);
}

.ft-16__track:first-child {
  background: color-mix(in oklch,var(--ft-16-acc) 12%,transparent);
  color: var(--ft-16-acc);
}

.ft-16__tn {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--ft-16-mut);
}

.ft-16__track:first-child .ft-16__tn {
  color: inherit;
}

.ft-16__tt {
  font-weight: 600;
}

.ft-16__td {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  color: var(--ft-16-mut);
}

.ft-16__foot {
  background: var(--ft-16-foot);
  border-top: 1px solid var(--ft-16-line);
}

.ft-16__player {
  position: sticky;
  bottom: 0;
  z-index: 20;
  display: grid;
  grid-template-columns: minmax(11rem,1fr) auto minmax(11rem,1.4fr) auto;
  align-items: center;
  gap: 10px clamp(12px,2vw,24px);
  padding: 12px clamp(14px,3vw,24px);
  background: color-mix(in oklch,var(--ft-16-bar) 88%,transparent);
  backdrop-filter: blur(16px) saturate(1.4);
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
  border-bottom: 1px solid var(--ft-16-line);
}

.ft-16__now {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 0;
}

.ft-16__art {
  width: 48px;
  height: 48px;
  flex: none;
  border-radius: 11px;
  background: conic-gradient(from 200deg,oklch(0.5 0.19 20),oklch(0.62 0.18 60),oklch(0.4 0.16 300),oklch(0.5 0.19 20));
  box-shadow: 0 8px 20px -10px oklch(0 0 0/.9);
}

.ft-16__meta {
  display: grid;
  min-width: 0;
}

.ft-16__ttitle {
  font-size: 14.2px;
  font-weight: 660;
  letter-spacing: -.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ft-16__tartist {
  font-size: 12.4px;
  color: var(--ft-16-mut);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ft-16__eq {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 22px;
  margin-inline-start: 4px;
}

.ft-16__eq i {
  width: 2.5px;
  height: 100%;
  border-radius: 2px;
  background: var(--ft-16-acc);
  transform-origin: bottom;
  transform: scaleY(.18);
  animation: ft-16-eq .9s ease-in-out infinite alternate;
  animation-play-state: paused;
}

.ft-16__player[data-playing="true"] .ft-16__eq i {
  animation-play-state: running;
}

.ft-16__eq i:nth-child(1) {
  animation-delay: -.1s;
}

.ft-16__eq i:nth-child(2) {
  animation-delay: -.42s;
}

.ft-16__eq i:nth-child(3) {
  animation-delay: -.66s;
}

.ft-16__eq i:nth-child(4) {
  animation-delay: -.28s;
}

.ft-16__eq i:nth-child(5) {
  animation-delay: -.55s;
}

.ft-16__eq i:nth-child(6) {
  animation-delay: -.8s;
}

.ft-16__eq i:nth-child(7) {
  animation-delay: -.36s;
}

.ft-16__eq i:nth-child(8) {
  animation-delay: -.7s;
}

@keyframes ft-16-eq {
  from {
    transform: scaleY(.18);
  }

  to {
    transform: scaleY(1);
  }
}

.ft-16__controls {
  display: flex;
  align-items: center;
  gap: 6px;
}

.ft-16__ctl {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--ft-16-mut);
  cursor: pointer;
  transition: color .2s ease,background .2s ease,transform .2s ease;
}

.ft-16__ctl:hover {
  color: var(--ft-16-ink);
  background: oklch(0.97 0.006 300/.09);
}

.ft-16__ctl[aria-pressed="true"] {
  color: var(--ft-16-acc);
}

.ft-16__play {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border: 0;
  border-radius: 50%;
  background: var(--ft-16-ink);
  color: oklch(0.16 0.02 300);
  cursor: pointer;
  transition: transform .22s cubic-bezier(.34,1.56,.64,1),background .2s ease;
}

.ft-16__play:hover {
  transform: scale(1.06);
  background: var(--ft-16-acc);
}

.ft-16__play svg {
  grid-area: 1/1;
}

.ft-16__i-pause,
.ft-16__player[data-playing="true"] .ft-16__i-play {
  display: none;
}

.ft-16__player[data-playing="true"] .ft-16__i-pause {
  display: block;
}

.ft-16__ctl:focus-visible,
.ft-16__play:focus-visible,
.ft-16__range:focus-visible,
.ft-16__link:focus-visible {
  outline: 2px solid var(--ft-16-acc);
  outline-offset: 3px;
}

.ft-16__scrub {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
}

.ft-16__time {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--ft-16-mut);
  font-variant-numeric: tabular-nums;
  flex: none;
}

.ft-16__range {
  --ft-16-p: 0%;
  flex: 1;
  min-width: 0;
  height: 6px;
  appearance: none;
  -webkit-appearance: none;
  border-radius: 99px;
  background: linear-gradient(to right,var(--ft-16-acc) var(--ft-16-p),oklch(0.97 0.006 300/.18) var(--ft-16-p));
  cursor: pointer;
}

.ft-16__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--ft-16-ink);
  border: 0;
  box-shadow: 0 2px 6px oklch(0 0 0/.5);
  transition: transform .18s ease;
}

.ft-16__range:hover::-webkit-slider-thumb {
  transform: scale(1.2);
}

.ft-16__range::-moz-range-thumb {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--ft-16-ink);
  border: 0;
  box-shadow: 0 2px 6px oklch(0 0 0/.5);
}

.ft-16__range::-moz-range-track {
  height: 6px;
  border-radius: 99px;
  background: transparent;
}

.ft-16__extra {
  display: flex;
  align-items: center;
  gap: 4px;
}

.ft-16__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ft-16__links {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px 24px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1080px)/2));
}

.ft-16__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ft-16__mark {
  width: 21px;
  height: 21px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%,var(--ft-16-acc),oklch(0.35 0.12 320) 70%);
}

.ft-16__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  margin-inline-start: auto;
}

.ft-16__link {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 11px;
  border-radius: 9px;
  font-size: 13.5px;
  color: var(--ft-16-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-16__link:hover {
  color: var(--ft-16-ink);
  background: oklch(0.97 0.006 300/.07);
}

.ft-16__copy {
  font-size: 12.4px;
  color: var(--ft-16-mut);
  width: 100%;
}

@media (max-width: 860px) {
  .ft-16__player {
    grid-template-columns: 1fr auto;
    grid-template-areas: 'now controls' 'scrub scrub';
  }

  .ft-16__now {
    grid-area: now;
  }

  .ft-16__controls {
    grid-area: controls;
  }

  .ft-16__scrub {
    grid-area: scrub;
  }

  .ft-16__extra {
    display: none;
  }
}

@media (max-width: 560px) {
  .ft-16__nav {
    margin-inline-start: 0;
  }

  .ft-16__eq {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-16__eq i {
    animation: none;
    transform: scaleY(.5);
  }

  .ft-16 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-16');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const player = root.querySelector('#ft-16-player');
  const play = root.querySelector('#ft-16-play');
  const range = root.querySelector('#ft-16-range');
  const cur = root.querySelector('#ft-16-cur');
  const live = root.querySelector('#ft-16-live');
  const DUR = 235;
  let t = 0, timer = null;
  const mmss = (s) => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
  const spoken = (s) => Math.floor(s / 60) + ' minutes ' + Math.floor(s % 60) + ' seconds';
  const paint = () => {
    range.value = String(Math.round(t));
    range.style.setProperty('--ft-16-p', (t / DUR * 100).toFixed(2) + '%');
    range.setAttribute('aria-valuetext', spoken(t) + ' of ' + spoken(DUR));
    cur.textContent = mmss(t);
  };
  const stop = () => { clearInterval(timer); timer = null; player.dataset.playing = 'false'; play.setAttribute('aria-pressed', 'false'); play.setAttribute('aria-label', 'Play Harbour Lights'); };
  const start = () => {
    player.dataset.playing = 'true';
    play.setAttribute('aria-pressed', 'true');
    play.setAttribute('aria-label', 'Pause Harbour Lights');
    timer = setInterval(() => { t = t + 1 > DUR ? 0 : t + 1; paint(); }, 1000);
  };
  play.addEventListener('click', () => {
    if (timer) { stop(); live.textContent = 'Paused at ' + mmss(t); }
    else { start(); live.textContent = 'Playing Harbour Lights by Kova and the Long Room'; }
  });
  range.addEventListener('input', () => { t = Number(range.value); paint(); });
  range.addEventListener('change', () => { live.textContent = 'Seeked to ' + mmss(t); });
  paint();
})();
```
