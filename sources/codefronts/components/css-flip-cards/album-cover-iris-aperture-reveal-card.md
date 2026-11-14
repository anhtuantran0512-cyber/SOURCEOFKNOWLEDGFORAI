---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/album-cover-iris-aperture-reveal-card/"
title: "Album Cover Iris Aperture Reveal Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front face shrinks via clip-path circle while back expands from center — a camera-aperture reveal with zero 3D rotation, proving 'flip card' can mean visual…"
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Album Cover Iris Aperture Reveal Card
Source: https://codefronts.com/components/css-flip-cards/album-cover-iris-aperture-reveal-card/

Front face shrinks via clip-path circle while back expands from center — a camera-aperture reveal with zero 3D rotation, proving 'flip card' can mean visual swap, not just axis spin.
## HTML
```html
<div class="fc-21">
  <div class="fc-21__scene">
    <div class="fc-21__card">
      <div class="fc-21__front">
        <div class="fc-21__cover">
          <svg width="220" height="220" viewBox="0 0 220 220" fill="none">
            <defs>
              <radialGradient id="fc-21-cover-bg" cx="0.4" cy="0.35" r="0.7">
                <stop offset="0%" stop-color="#ec4899"/>
                <stop offset="40%" stop-color="#a21caf"/>
                <stop offset="100%" stop-color="#1e1b4b"/>
              </radialGradient>
              <linearGradient id="fc-21-vinyl" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="#1c1c1c"/>
                <stop offset="100%" stop-color="#0a0a0a"/>
              </linearGradient>
            </defs>
            <rect width="220" height="220" fill="url(#fc-21-cover-bg)"/>
            <circle cx="110" cy="110" r="78" fill="url(#fc-21-vinyl)"/>
            <circle cx="110" cy="110" r="78" fill="none" stroke="#3a3a3a" stroke-width="0.5"/>
            <circle cx="110" cy="110" r="68" fill="none" stroke="#2a2a2a" stroke-width="0.5"/>
            <circle cx="110" cy="110" r="58" fill="none" stroke="#2a2a2a" stroke-width="0.5"/>
            <circle cx="110" cy="110" r="48" fill="none" stroke="#2a2a2a" stroke-width="0.5"/>
            <circle cx="110" cy="110" r="38" fill="none" stroke="#2a2a2a" stroke-width="0.5"/>
            <circle cx="110" cy="110" r="28" fill="#ec4899"/>
            <circle cx="110" cy="110" r="4" fill="#0a0a0a"/>
            <g opacity="0.4">
              <circle cx="170" cy="50" r="2" fill="#fef3c7"/>
              <circle cx="180" cy="180" r="1.5" fill="#fef3c7"/>
              <circle cx="40" cy="170" r="2" fill="#fef3c7"/>
              <circle cx="30" cy="40" r="1.5" fill="#fef3c7"/>
            </g>
          </svg>
        </div>
        <div class="fc-21__cover-meta">
          <div class="fc-21__artist">VANTABLACK</div>
          <div class="fc-21__album">After Midnight Drives</div>
          <div class="fc-21__pill-row">
            <span class="fc-21__pill">SYNTHWAVE</span>
            <span class="fc-21__pill">2026 · LP</span>
          </div>
        </div>
        <div class="fc-21__hint">Hover for the tracklist ◐</div>
      </div>
      <div class="fc-21__back">
        <div class="fc-21__back-head">
          <span class="fc-21__back-side">SIDE A</span>
          <span class="fc-21__back-runtime">38 : 12</span>
        </div>
        <div class="fc-21__tracklist">
          <div class="fc-21__track"><span class="fc-21__t-num">01</span><span class="fc-21__t-name">Neon Highway</span><span class="fc-21__t-time">4:18</span></div>
          <div class="fc-21__track"><span class="fc-21__t-num">02</span><span class="fc-21__t-name">Cassette Memory</span><span class="fc-21__t-time">5:42</span></div>
          <div class="fc-21__track"><span class="fc-21__t-num">03</span><span class="fc-21__t-name">Static Bloom</span><span class="fc-21__t-time">3:55</span></div>
          <div class="fc-21__track"><span class="fc-21__t-num">04</span><span class="fc-21__t-name">2 AM in Tokyo</span><span class="fc-21__t-time">6:08</span></div>
          <div class="fc-21__track"><span class="fc-21__t-num">05</span><span class="fc-21__t-name">Lavender Static</span><span class="fc-21__t-time">4:33</span></div>
          <div class="fc-21__track"><span class="fc-21__t-num">06</span><span class="fc-21__t-name">After Midnight</span><span class="fc-21__t-time">13:36</span></div>
        </div>
        <button class="fc-21__play">▶  Play full album</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-21,
.fc-21 *,
.fc-21 *::before,
.fc-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-21 ::selection {
  background: #ec4899;
  color: #0a0a0a;
}

.fc-21 {
  --bg: #0a0612;
  --neon: #ec4899;
  --violet: #a21caf;
  --cream: #fef3c7;
  --ink: #f5e8ff;
  --card-w: 360px;
  --card-h: 500px;
  font-family: 'Inter',system-ui,-apple-system,sans-serif;
  background: radial-gradient(ellipse at 30% 20%,#1e0b3b,#0a0612 70%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ink);
}

.fc-21__scene {
  width: var(--card-w);
  height: var(--card-h);
}

.fc-21__card {
  width: 100%;
  height: 100%;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 24px 60px rgba(0,0,0,.6),0 0 0 1px rgba(236,72,153,.2);
}

.fc-21__front,
.fc-21__back {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 28px;
  transition: clip-path .65s cubic-bezier(.7,0,.3,1);
}

.fc-21__front {
  background: linear-gradient(160deg,#1e0b3b 0%,#0a0612 100%);
  clip-path: circle(150% at 50% 50%);
  -webkit-clip-path: circle(150% at 50% 50%);
  z-index: 1;
}

.fc-21__back {
  background: linear-gradient(160deg,#0a0612 0%,#1e0b3b 100%);
  clip-path: circle(0% at 50% 50%);
  -webkit-clip-path: circle(0% at 50% 50%);
  z-index: 2;
}

.fc-21__scene:hover .fc-21__front {
  clip-path: circle(0% at 50% 50%);
  -webkit-clip-path: circle(0% at 50% 50%);
}

.fc-21__scene:hover .fc-21__back {
  clip-path: circle(150% at 50% 50%);
  -webkit-clip-path: circle(150% at 50% 50%);
}
/* FRONT — album cover */

.fc-21__cover {
  margin-top: 6px;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 14px 30px rgba(0,0,0,.5);
}

.fc-21__cover-meta {
  margin-top: 22px;
  text-align: center;
  width: 100%;
}

.fc-21__artist {
  font-size: 11px;
  letter-spacing: .45em;
  color: var(--neon);
  font-weight: 700;
}

.fc-21__album {
  font-size: 23px;
  font-weight: 800;
  color: var(--ink);
  margin-top: 6px;
  letter-spacing: -.02em;
  font-family: 'Playfair Display',Georgia,serif;
  font-style: italic;
}

.fc-21__pill-row {
  display: flex;
  justify-content: center;
  gap: 6px;
  margin-top: 12px;
}

.fc-21__pill {
  padding: 4px 11px;
  border: 1px solid rgba(236,72,153,.4);
  border-radius: 999px;
  font-size: 9px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(245,232,255,.7);
  font-weight: 600;
}

.fc-21__hint {
  margin-top: auto;
  font-size: 10px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(245,232,255,.4);
}
/* BACK — tracklist */

.fc-21__back-head {
  display: flex;
  justify-content: space-between;
  width: 100%;
  padding-bottom: 14px;
  margin-bottom: 14px;
  border-bottom: 1px solid rgba(236,72,153,.25);
  font-size: 10px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--neon);
  font-weight: 700;
}

.fc-21__back-runtime {
  color: rgba(245,232,255,.55);
  font-family: ui-monospace,monospace;
  letter-spacing: .1em;
}

.fc-21__tracklist {
  display: flex;
  flex-direction: column;
  gap: 1px;
  width: 100%;
  flex: 1;
}

.fc-21__track {
  display: grid;
  grid-template-columns: 28px 1fr auto;
  align-items: center;
  gap: 12px;
  padding: 10px 8px;
  border-radius: 6px;
  transition: background .15s;
  cursor: pointer;
}

.fc-21__track:hover {
  background: rgba(236,72,153,.08);
}

.fc-21__t-num {
  font-family: ui-monospace,monospace;
  font-size: 10px;
  color: rgba(245,232,255,.4);
  letter-spacing: .1em;
}

.fc-21__t-name {
  font-size: 13px;
  color: var(--ink);
  font-weight: 500;
}

.fc-21__t-time {
  font-family: ui-monospace,monospace;
  font-size: 11px;
  color: rgba(245,232,255,.4);
  letter-spacing: .05em;
}

.fc-21__play {
  margin-top: 14px;
  width: 100%;
  padding: 13px 0;
  border: 1px solid rgba(236,72,153,.5);
  border-radius: 8px;
  background: linear-gradient(135deg,rgba(236,72,153,.18),rgba(162,28,175,.12));
  color: var(--neon);
  font-size: 12px;
  letter-spacing: .25em;
  text-transform: uppercase;
  font-weight: 700;
  cursor: pointer;
  transition: background .2s,box-shadow .2s;
  font-family: inherit;
}

.fc-21__play:hover {
  background: linear-gradient(135deg,rgba(236,72,153,.3),rgba(162,28,175,.2));
  box-shadow: 0 8px 24px rgba(236,72,153,.25);
}

@media (prefers-reduced-motion: reduce) {
  .fc-21__front,
    .fc-21__back {
    transition: none;
  }
}
```
