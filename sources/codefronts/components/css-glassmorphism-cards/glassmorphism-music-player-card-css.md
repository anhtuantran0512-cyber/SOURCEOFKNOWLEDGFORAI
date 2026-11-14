---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-music-player-card-css/"
title: "Glassmorphism Music Player Card CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "A now-playing card with a spinning vinyl album (pausable via a real play/pause checkbox), animated equalizer bars and a shimmer progress track — plus a queue…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Music Player Card CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-music-player-card-css/

A now-playing card with a spinning vinyl album (pausable via a real play/pause checkbox), animated equalizer bars and a shimmer progress track — plus a queue variant where the active row pulses its own mini EQ and rows light on hover.
## HTML
```html
<div class="glz-13-group">
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="glz-13a" aria-label="Glassmorphism music player demo">
  <article class="glz-13a__player">
    <input type="checkbox" id="glz-13a-play" class="glz-13a__state">
    <div class="glz-13a__vinyl" aria-hidden="true"><img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=520&auto=format&fit=crop" alt=""><i></i></div>
    <div class="glz-13a__info">
      <p class="glz-13a__eyebrow">Now playing</p>
      <h3>Midnight Interchange</h3>
      <p class="glz-13a__artist">Neon Palms</p>
      <div class="glz-13a__bar" aria-hidden="true"><i></i></div>
      <div class="glz-13a__time" aria-hidden="true"><span>1:24</span><span>3:30</span></div>
      <div class="glz-13a__controls">
        <button type="button" aria-label="Previous track">⏮</button>
        <label class="glz-13a__play" for="glz-13a-play" role="button" aria-label="Play or pause" tabindex="0"><span class="glz-13a__ic-play">▶</span><span class="glz-13a__ic-pause">⏸</span></label>
        <button type="button" aria-label="Next track">⏭</button>
        <div class="glz-13a__eq" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
      </div>
    </div>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="glz-13b" aria-label="Glassmorphism playlist queue card">
  <article class="glz-13b__card">
    <header class="glz-13b__head"><h3>Up next</h3><span>Focus mix · 12 tracks</span></header>
    <ol class="glz-13b__list">
      <li class="glz-13b__row glz-13b__row--live" aria-current="true"><img src="https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?q=80&w=200&auto=format&fit=crop" alt="" loading="lazy"><span class="glz-13b__t"><b>Glasshouse</b><em>Cobalt Era</em></span><span class="glz-13b__meq" aria-hidden="true"><i></i><i></i><i></i></span></li>
      <li class="glz-13b__row"><img src="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?q=80&w=200&auto=format&fit=crop" alt="" loading="lazy"><span class="glz-13b__t"><b>Terminal Sunrise</b><em>Ferry Lights</em></span><b class="glz-13b__len">3:58</b></li>
      <li class="glz-13b__row"><img src="https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?q=80&w=200&auto=format&fit=crop" alt="" loading="lazy"><span class="glz-13b__t"><b>Latency</b><em>Null Pointer Club</em></span><b class="glz-13b__len">2:47</b></li>
      <li class="glz-13b__row"><img src="https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=200&auto=format&fit=crop" alt="" loading="lazy"><span class="glz-13b__t"><b>Overcast Sundays</b><em>Mild Peril</em></span><b class="glz-13b__len">4:12</b></li>
    </ol>
    <button type="button" class="glz-13b__shuffle">⇄ Shuffle queue</button>
  </article>
</section>
</div>
```
## CSS
```css
.glz-13-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-13-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-13a,
.glz-13a *,
.glz-13a *::before,
.glz-13a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-13a {
  --pk: oklch(0.72 0.19 350);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #120c18;
  font-family: 'Sora',system-ui,sans-serif;
}

.glz-13a::before {
  content: "";
  position: absolute;
  width: 60vmin;
  height: 60vmin;
  border-radius: 50%;
  background: oklch(0.5 0.2 350);
  filter: blur(95px);
  opacity: .55;
  top: -14%;
  right: -8%;
}

.glz-13a::after {
  content: "";
  position: absolute;
  width: 48vmin;
  height: 48vmin;
  border-radius: 50%;
  background: oklch(0.5 0.17 260);
  filter: blur(95px);
  opacity: .5;
  bottom: -12%;
  left: -6%;
}

.glz-13a__player {
  position: relative;
  z-index: 1;
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  align-items: center;
  width: min(460px,100%);
  padding: 26px;
  border-radius: 26px;
  color: #f6effa;
  background: linear-gradient(165deg,rgba(255,255,255,.13),rgba(255,255,255,.04));
  backdrop-filter: blur(24px) saturate(170%);
  -webkit-backdrop-filter: blur(24px) saturate(170%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 34px 70px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.24);
}

.glz-13a__state {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.glz-13a__vinyl {
  position: relative;
  width: 132px;
  height: 132px;
  flex: none;
  margin: 0 auto;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 18px 40px -14px rgba(0,0,0,.8);
  animation: glz-13a-spin 6s linear infinite;
  animation-play-state: paused;
}

.glz-13a__vinyl img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #2a2136;
}

.glz-13a__vinyl i {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: repeating-radial-gradient(circle,transparent 0 3px,rgba(0,0,0,.22) 3px 4px);
  -webkit-mask: radial-gradient(circle,transparent 0 13px,#000 14px);
  mask: radial-gradient(circle,transparent 0 13px,#000 14px);
}

.glz-13a__vinyl::after {
  content: "";
  position: absolute;
  inset: calc(50% - 7px);
  border-radius: 50%;
  background: #f6effa;
  box-shadow: 0 0 0 5px rgba(0,0,0,.6);
}

.glz-13a__player:has(.glz-13a__state:checked) .glz-13a__vinyl {
  animation-play-state: running;
}

.glz-13a__info {
  flex: 1 1 220px;
  min-width: 0;
}

.glz-13a__eyebrow {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--pk);
}

.glz-13a__info h3 {
  margin-top: 7px;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.glz-13a__artist {
  margin-top: 3px;
  font-size: 13px;
  color: rgba(246,239,250,.6);
}

.glz-13a__bar {
  margin-top: 16px;
  height: 5px;
  border-radius: 99px;
  background: rgba(255,255,255,.14);
  overflow: hidden;
}

.glz-13a__bar i {
  display: block;
  height: 100%;
  width: 40%;
  border-radius: inherit;
  background: linear-gradient(90deg,var(--pk),oklch(0.75 0.16 260));
}

.glz-13a__time {
  display: flex;
  justify-content: space-between;
  margin-top: 7px;
  font-size: 10.5px;
  color: rgba(246,239,250,.5);
  font-variant-numeric: tabular-nums;
}

.glz-13a__controls {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 16px;
}

.glz-13a__controls button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,.2);
  background: rgba(255,255,255,.08);
  color: #f6effa;
  font-size: 13px;
  cursor: pointer;
  transition: background .2s ease;
}

.glz-13a__controls button:hover {
  background: rgba(255,255,255,.16);
}

.glz-13a__play {
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  cursor: pointer;
  background: linear-gradient(135deg,var(--pk),oklch(0.62 0.2 300));
  box-shadow: 0 14px 30px -10px oklch(0.72 0.19 350/.8);
  font-size: 16px;
  color: #fff;
  transition: transform .2s ease;
}

.glz-13a__play:hover {
  transform: scale(1.06);
}

.glz-13a__play span {
  grid-area: 1/1;
  transition: opacity .2s ease;
}

.glz-13a__ic-pause {
  opacity: 0;
}

.glz-13a__player:has(.glz-13a__state:checked) .glz-13a__ic-play {
  opacity: 0;
}

.glz-13a__player:has(.glz-13a__state:checked) .glz-13a__ic-pause {
  opacity: 1;
}

.glz-13a__controls button:focus-visible,
.glz-13a__play:focus-visible,
.glz-13a__player:has(.glz-13a__state:focus-visible) .glz-13a__play {
  outline: 2px solid var(--pk);
  outline-offset: 3px;
}

.glz-13a__eq {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 22px;
  margin-left: auto;
}

.glz-13a__eq i {
  width: 4px;
  height: 100%;
  border-radius: 99px;
  background: linear-gradient(180deg,var(--pk),oklch(0.75 0.16 260));
  transform-origin: bottom;
  transform: scaleY(.2);
  animation: glz-13a-eq 1s ease-in-out infinite alternate;
  animation-play-state: paused;
}

.glz-13a__eq i:nth-child(1) {
  animation-delay: -.2s;
}

.glz-13a__eq i:nth-child(2) {
  animation-delay: -.6s;
}

.glz-13a__eq i:nth-child(3) {
  animation-delay: -.4s;
}

.glz-13a__eq i:nth-child(4) {
  animation-delay: -.8s;
}

.glz-13a__eq i:nth-child(5) {
  animation-delay: -.1s;
}

.glz-13a__player:has(.glz-13a__state:checked) .glz-13a__eq i {
  animation-play-state: running;
}

@keyframes glz-13a-spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes glz-13a-eq {
  from {
    transform: scaleY(.15);
  }

  to {
    transform: scaleY(1);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-13a__player {
    background: rgba(28,20,38,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-13a__vinyl,
    .glz-13a__eq i {
    animation: none;
  }
}

.glz-13b,
.glz-13b *,
.glz-13b *::before,
.glz-13b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-13b {
  --pk: oklch(0.75 0.17 330);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: linear-gradient(210deg,#131022,#0b0f1c);
}

.glz-13b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(44% 40% at 20% 18%,oklch(0.55 0.2 330/.4),transparent 70%),radial-gradient(40% 36% at 84% 80%,oklch(0.55 0.16 230/.4),transparent 70%);
}

.glz-13b__card {
  position: relative;
  z-index: 1;
  width: min(390px,100%);
  padding: 24px;
  border-radius: 24px;
  color: #f2edf9;
  font-family: 'Sora',system-ui,sans-serif;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  border: 1px solid rgba(255,255,255,.18);
  box-shadow: 0 32px 66px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.22);
}

.glz-13b__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.glz-13b__head h3 {
  font-size: 17px;
  font-weight: 700;
}

.glz-13b__head span {
  font-size: 11px;
  color: rgba(242,237,249,.5);
}

.glz-13b__list {
  list-style: none;
  margin-top: 16px;
  display: grid;
  gap: 6px;
}

.glz-13b__row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 15px;
  border: 1px solid transparent;
  transition: background .2s ease,border-color .2s ease,transform .2s ease;
}

.glz-13b__row:hover {
  background: rgba(255,255,255,.08);
  border-color: rgba(255,255,255,.14);
  transform: translateX(4px);
}

.glz-13b__row img {
  width: 42px;
  height: 42px;
  border-radius: 11px;
  object-fit: cover;
  background: #251d38;
}

.glz-13b__t {
  flex: 1;
  min-width: 0;
}

.glz-13b__t b {
  display: block;
  font-size: 13.5px;
  font-weight: 700;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.glz-13b__t em {
  display: block;
  font-style: normal;
  font-size: 11.5px;
  color: rgba(242,237,249,.55);
  margin-top: 2px;
}

.glz-13b__len {
  font-size: 11.5px;
  color: rgba(242,237,249,.5);
  font-variant-numeric: tabular-nums;
}

.glz-13b__row--live {
  background: linear-gradient(120deg,oklch(0.75 0.17 330/.16),rgba(255,255,255,.05));
  border-color: oklch(0.75 0.17 330/.4);
}

.glz-13b__meq {
  display: flex;
  align-items: flex-end;
  gap: 2.5px;
  height: 16px;
}

.glz-13b__meq i {
  width: 3px;
  height: 100%;
  border-radius: 99px;
  background: var(--pk);
  transform-origin: bottom;
  animation: glz-13b-eq .9s ease-in-out infinite alternate;
}

.glz-13b__meq i:nth-child(2) {
  animation-delay: -.5s;
}

.glz-13b__meq i:nth-child(3) {
  animation-delay: -.25s;
}

.glz-13b__shuffle {
  width: 100%;
  margin-top: 16px;
  padding: 13px;
  border-radius: 13px;
  border: 1px solid rgba(255,255,255,.2);
  background: rgba(255,255,255,.07);
  color: #f2edf9;
  font: 700 13px 'Sora',sans-serif;
  cursor: pointer;
  transition: background .2s ease;
}

.glz-13b__shuffle:hover {
  background: rgba(255,255,255,.14);
}

.glz-13b__shuffle:focus-visible {
  outline: 2px solid var(--pk);
  outline-offset: 3px;
}

@keyframes glz-13b-eq {
  from {
    transform: scaleY(.2);
  }

  to {
    transform: scaleY(1);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-13b__card {
    background: rgba(24,20,38,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-13b__meq i {
    animation: none;
    transform: scaleY(.6);
  }

  .glz-13b__row {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hidden checkbox is the transport: :has(:checked) flips play/pause glyphs and sets animation-play-state on the vinyl and EQ bars. */

/* No JavaScript — the active row is marked with aria-current and its mini-EQ runs on negative-delay desynced bars; hover states are pure transitions. */
```
