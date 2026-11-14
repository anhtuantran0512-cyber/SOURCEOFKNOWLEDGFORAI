---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/live-badge/"
title: "Live Stream Broadcast Badge Control"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "Live video has a state ordinary players don't: pause and you fall behind the broadcast."
has_js: "true"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Stream Broadcast Badge Control
Source: https://codefronts.com/components/css-play-pause-buttons/live-badge/

Live video has a state ordinary players don't: pause and you fall behind the broadcast. This control models it properly — a pulsing LIVE badge that greys out and starts counting your delay the moment you pause, plus a 'Go live' jump-back button that appears only when you're behind. It's the difference between a play button and a live player.
## HTML
```html
<section class="pp-25" aria-label="Live stream broadcast badge control demo">
  <div class="pp-25__stage">
    <div class="pp-25__player" data-live="live">
      <img class="pp-25__frame" src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?q=80&w=1100&auto=format&fit=crop" alt="" loading="lazy">
      <span class="pp-25__scrim" aria-hidden="true"></span>
      <div class="pp-25__top">
        <span class="pp-25__badge" aria-hidden="true"><i class="pp-25__dot"></i><b class="pp-25__word">LIVE</b></span>
        <span class="pp-25__viewers"><span class="pp-25__count">12,438</span> watching</span>
      </div>
      <div class="pp-25__bar">
        <button class="pp-25__btn" type="button" aria-pressed="false">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
            <path class="pp-25__p" d="M9 5.6v12.8L18.8 12z" fill="currentColor"/>
            <path class="pp-25__q" d="M8.6 5.6h3.1v12.8H8.6zM12.9 5.6H16v12.8h-3.1z" fill="currentColor"/>
          </svg>
          <span class="pp-25__sr">Pause the live stream</span>
        </button>
        <p class="pp-25__title">Build Night · shipping the new editor</p>
        <p class="pp-25__delay" aria-hidden="true">-0:00</p>
        <button class="pp-25__golive" type="button">Go live</button>
      </div>
      <p class="pp-25__live" role="status"></p>
    </div>
    <p class="pp-25__chip" aria-hidden="true">3-state badge · pulse stops when behind · go-live jump back</p>
  </div>
</section>
```
## CSS
```css
.pp-25,
.pp-25 *,
.pp-25 *::before,
.pp-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-25-bg);
  --pp-25-bg: oklch(0.14 0.015 270);
  --pp-25-ink: oklch(0.98 0.004 260);
  --pp-25-mut: oklch(0.74 0.015 265);
  --pp-25-red: oklch(0.62 0.23 25);
  --pp-25-grey: oklch(0.6 0.01 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-25-ink);
}

.pp-25__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(18px,4vw,52px);
}

.pp-25__player {
  position: relative;
  width: min(100%,760px);
  aspect-ratio: 16/9;
  border-radius: 18px;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.3 0.05 300),oklch(0.16 0.02 270));
  box-shadow: 0 30px 70px oklch(0 0 0/.55);
}

.pp-25__frame {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: filter .4s;
}

.pp-25__player[data-live="behind"] .pp-25__frame {
  filter: grayscale(.55) brightness(.8);
}

.pp-25__scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top,oklch(0 0 0/.78),transparent 42%),linear-gradient(to bottom,oklch(0 0 0/.5),transparent 28%);
}

.pp-25__top {
  position: absolute;
  top: 16px;
  left: 18px;
  right: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.pp-25__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px 6px 10px;
  border-radius: 8px;
  background: oklch(0 0 0/.45);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .14em;
}

.pp-25__dot {
  position: relative;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--pp-25-red);
  transition: background .3s;
}

.pp-25__dot::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: pp-25-pulse 1.8s ease-out infinite;
}

.pp-25__player[data-live="behind"] .pp-25__dot {
  background: var(--pp-25-grey);
}

.pp-25__player[data-live="behind"] .pp-25__dot::after {
  animation: none;
  opacity: 0;
}

.pp-25__player[data-live="behind"] .pp-25__word::after {
  content: ' · BEHIND';
  font-weight: 600;
  opacity: .7;
}

@keyframes pp-25-pulse {
  from {
    scale: 1;
    opacity: .75;
  }

  to {
    scale: 2.7;
    opacity: 0;
  }
}

.pp-25__viewers {
  font-size: 12px;
  color: var(--pp-25-mut);
  font-variant-numeric: tabular-nums;
  text-shadow: 0 1px 4px oklch(0 0 0/.6);
}

.pp-25__bar {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 18px;
  display: flex;
  align-items: center;
  gap: 14px;
}

.pp-25__btn {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  flex: none;
  border: 0;
  border-radius: 50%;
  background: oklch(1 0 0/.16);
  border: 1px solid oklch(1 0 0/.3);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: var(--pp-25-ink);
  cursor: pointer;
  transition: background .25s,transform .2s;
}

.pp-25__btn:hover {
  background: oklch(1 0 0/.28);
  transform: scale(1.06);
}

.pp-25__btn:focus-visible {
  outline: 3px solid var(--pp-25-ink);
  outline-offset: 3px;
}

.pp-25__sr,
.pp-25__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pp-25__p {
  display: none;
}

.pp-25__player[data-live="behind"] .pp-25__p {
  display: block;
}

.pp-25__player[data-live="behind"] .pp-25__q {
  display: none;
}

.pp-25__title {
  flex: 1;
  min-width: 0;
  font-size: 14.5px;
  font-weight: 640;
  letter-spacing: -.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-shadow: 0 1px 6px oklch(0 0 0/.7);
}

.pp-25__delay {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--pp-25-mut);
  font-variant-numeric: tabular-nums;
}

.pp-25__golive {
  min-height: 40px;
  padding: 0 16px;
  border: 0;
  border-radius: 99px;
  background: var(--pp-25-red);
  color: oklch(0.99 0 0);
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .04em;
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  translate: 0 6px;
  transition: opacity .3s,translate .3s,background .2s;
}

.pp-25__golive:hover {
  background: color-mix(in oklch,var(--pp-25-red) 86%,black);
}

.pp-25__golive:focus-visible {
  outline: 3px solid var(--pp-25-ink);
  outline-offset: 3px;
}

.pp-25__player[data-live="behind"] .pp-25__golive {
  opacity: 1;
  pointer-events: auto;
  translate: 0;
}

.pp-25__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-25-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-25__dot::after {
    animation: none;
    opacity: 0;
  }

  .pp-25 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const nf = new Intl.NumberFormat('en-US');
  document.querySelectorAll('.pp-25__player').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const btn = root.querySelector('.pp-25__btn');
    const golive = root.querySelector('.pp-25__golive');
    const delay = root.querySelector('.pp-25__delay');
    const sr = root.querySelector('.pp-25__sr');
    const live = root.querySelector('.pp-25__live');
    const count = root.querySelector('.pp-25__count');
    let behind = 0, id = 0, viewers = 12438;
    const fmt = (s) => Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
    const setLive = (isLive) => {
      root.dataset.live = isLive ? 'live' : 'behind';
      btn.setAttribute('aria-pressed', String(!isLive));
      sr.textContent = isLive ? 'Pause the live stream' : 'Resume playback';
      clearInterval(id);
      if (isLive) { behind = 0; delay.textContent = '-0:00'; live.textContent = 'Playing live'; }
      else id = setInterval(() => { behind++; delay.textContent = '-' + fmt(behind); }, 1000);
      if (!isLive) live.textContent = 'Paused, falling behind live';
    };
    btn.addEventListener('click', () => setLive(root.dataset.live === 'behind'));
    golive.addEventListener('click', () => { setLive(true); live.textContent = 'Jumped to live'; });
    setInterval(() => { viewers += Math.round((Math.random() - 0.45) * 24); count.textContent = nf.format(viewers); }, 3000);
  });
})();
```
