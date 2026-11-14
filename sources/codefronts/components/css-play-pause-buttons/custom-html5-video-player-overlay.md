---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/custom-html5-video-player-overlay/"
title: "Custom HTML5 Video Player Overlay"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "The component every video page needs: a poster-framed <video> with the native controls off, a centered glass play button over a gradient scrim, and a real…"
has_js: "true"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom HTML5 Video Player Overlay
Source: https://codefronts.com/components/css-play-pause-buttons/custom-html5-video-player-overlay/

The component every video page needs: a poster-framed <video> with the native controls off, a centered glass play button over a gradient scrim, and a real scrub bar wired to timeupdate. The overlay fades out while playing and returns on pause or hover — the behaviour users expect from YouTube-class players — and the whole control surface is keyboard operable, with Space and K bound to toggle like a native player.
## HTML
```html
<section class="pp-02" aria-label="Custom HTML5 video player overlay demo">
  <div class="pp-02__stage">
    <div class="pp-02__player" data-state="paused">
      <video class="pp-02__video" preload="none" playsinline muted
        poster="https://images.unsplash.com/photo-1478720568477-152d9b164e26?q=80&w=1200&auto=format&fit=crop"
        src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"></video>
      <div class="pp-02__scrim" aria-hidden="true"></div>
      <button class="pp-02__big" type="button" aria-pressed="false">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true">
          <path class="pp-02__i-play" d="M8 5.2v13.6L19 12z" fill="currentColor"/>
          <path class="pp-02__i-pause" d="M8 5h3.2v14H8zM12.8 5H16v14h-3.2z" fill="currentColor"/>
        </svg>
        <span class="pp-02__label">Play video</span>
      </button>
      <div class="pp-02__bar" aria-hidden="true"><span class="pp-02__fill"></span></div>
      <p class="pp-02__time" aria-hidden="true"><span class="pp-02__now">0:00</span> / <span class="pp-02__dur">0:00</span></p>
    </div>
    <p class="pp-02__chip" aria-hidden="true">preload=&quot;none&quot; + poster · media events drive state · --pp-02-progress → scaleX</p>
  </div>
</section>
```
## CSS
```css
.pp-02,
.pp-02 *,
.pp-02 *::before,
.pp-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-02-bg);
  --pp-02-bg: oklch(0.15 0.012 260);
  --pp-02-ink: oklch(0.98 0.004 250);
  --pp-02-mut: oklch(0.72 0.015 255);
  --pp-02-acc: oklch(0.72 0.17 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-02-ink);
}

.pp-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(18px,4vw,52px);
}

.pp-02__player {
  --pp-02-progress: 0;
  position: relative;
  width: min(100%,760px);
  aspect-ratio: 16/9;
  border-radius: 18px;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.32 0.05 240),oklch(0.2 0.03 280));
  box-shadow: 0 0 0 1px oklch(1 0 0/.09),0 30px 70px oklch(0 0 0/.5);
}

.pp-02__video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.pp-02__scrim {
  position: absolute;
  inset: 0;
  background: radial-gradient(60% 60% at 50% 45%,oklch(0 0 0/.28),transparent),linear-gradient(to top,oklch(0 0 0/.62),transparent 42%);
  opacity: 1;
  transition: opacity .4s;
  pointer-events: none;
}

.pp-02__player[data-state="playing"] .pp-02__scrim {
  opacity: .35;
}

.pp-02__big {
  position: absolute;
  top: 50%;
  left: 50%;
  translate: -50% -50%;
  display: grid;
  place-items: center;
  width: 88px;
  height: 88px;
  border: 1px solid oklch(1 0 0/.35);
  border-radius: 50%;
  background: oklch(1 0 0/.14);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  color: var(--pp-02-ink);
  cursor: pointer;
  transition: transform .3s cubic-bezier(.34,1.4,.5,1),opacity .35s,background .25s;
}

.pp-02__big:hover {
  background: oklch(1 0 0/.24);
  transform: translate(0,0) scale(1.07);
}

.pp-02__big:focus-visible {
  outline: 3px solid var(--pp-02-acc);
  outline-offset: 4px;
}

.pp-02__player[data-state="playing"] .pp-02__big {
  opacity: 0;
  pointer-events: none;
  scale: .86;
}

.pp-02__player[data-state="playing"]:hover .pp-02__big,
.pp-02__player[data-state="playing"]:focus-within .pp-02__big {
  opacity: 1;
  pointer-events: auto;
  scale: 1;
}

.pp-02__label {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pp-02__i-pause {
  display: none;
}

.pp-02__player[data-state="playing"] .pp-02__i-play {
  display: none;
}

.pp-02__player[data-state="playing"] .pp-02__i-pause {
  display: block;
}

.pp-02__bar {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 20px;
  height: 5px;
  border-radius: 99px;
  background: oklch(1 0 0/.25);
  overflow: hidden;
}

.pp-02__fill {
  display: block;
  height: 100%;
  border-radius: 99px;
  background: var(--pp-02-acc);
  transform: scaleX(var(--pp-02-progress));
  transform-origin: left;
  transition: transform .12s linear;
}

.pp-02__time {
  position: absolute;
  right: 18px;
  bottom: 34px;
  font-size: 12px;
  font-variant-numeric: tabular-nums;
  color: var(--pp-02-ink);
  text-shadow: 0 1px 3px oklch(0 0 0/.6);
}

.pp-02__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-02-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-02 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.pp-02__player').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const v = root.querySelector('.pp-02__video');
    const btn = root.querySelector('.pp-02__big');
    const label = root.querySelector('.pp-02__label');
    const now = root.querySelector('.pp-02__now');
    const dur = root.querySelector('.pp-02__dur');
    const fmt = (s) => (isFinite(s) ? Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0') : '0:00');
    const sync = () => {
      const playing = !v.paused && !v.ended;
      root.dataset.state = playing ? 'playing' : 'paused';
      btn.setAttribute('aria-pressed', String(playing));
      label.textContent = playing ? 'Pause video' : 'Play video';
    };
    btn.addEventListener('click', () => { v.paused ? v.play().catch(sync) : v.pause(); });
    ['play', 'pause', 'ended'].forEach((e) => v.addEventListener(e, sync));
    v.addEventListener('loadedmetadata', () => { dur.textContent = fmt(v.duration); });
    v.addEventListener('timeupdate', () => {
      root.style.setProperty('--pp-02-progress', v.duration ? v.currentTime / v.duration : 0);
      now.textContent = fmt(v.currentTime);
    });
    root.addEventListener('keydown', (e) => {
      if (e.key === ' ' || e.key.toLowerCase() === 'k') { e.preventDefault(); btn.click(); }
    });
    sync();
  });
})();
```
