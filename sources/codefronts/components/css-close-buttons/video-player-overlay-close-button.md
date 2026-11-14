---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/video-player-overlay-close-button/"
title: "Video Player Overlay Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The picture-in-picture / embedded-player dismiss: a close button that fades out with the rest of the player chrome after 2.4s of inactivity and reappears the…"
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Player Overlay Close Button
Source: https://codefronts.com/components/css-close-buttons/video-player-overlay-close-button/

The picture-in-picture / embedded-player dismiss: a close button that fades out with the rest of the player chrome after 2.4s of inactivity and reappears the instant the pointer moves — YouTube's idle-hide behaviour — with a scrim gradient behind the top bar so the × survives bright footage. Keyboard focus ALWAYS reveals the chrome.
## HTML
```html
<section class="ccb-09" aria-label="Video player overlay close demo">
  <div class="ccb-09__player" id="ccb-09-player">
    <div class="ccb-09__video" aria-hidden="true"><span class="ccb-09__play">▶</span></div>
    <div class="ccb-09__topbar">
      <span class="ccb-09__title">Trail running the Dolomites</span>
      <button class="ccb-09__close" type="button" aria-label="Close player">
        <span class="ccb-09__x" aria-hidden="true"></span>
      </button>
    </div>
    <span class="ccb-09__hint" aria-hidden="true">chrome hides after 2.4s idle — move to bring it back</span>
  </div>
</section>
```
## CSS
```css
.ccb-09,
.ccb-09 *,
.ccb-09 *::before,
.ccb-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-09 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.14 0.01 260);
}

.ccb-09 .ccb-09__player {
  position: relative;
  width: min(420px,100%);
  aspect-ratio: 16/9;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 26px 60px -28px rgba(0,0,0,.9);
}

.ccb-09 .ccb-09__video {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  background: radial-gradient(80% 70% at 30% 25%,oklch(0.8 0.06 220),transparent 55%),linear-gradient(200deg,oklch(0.72 0.1 230) 0%,oklch(0.45 0.09 260) 55%,oklch(0.25 0.05 280) 100%);
}

.ccb-09 .ccb-09__play {
  display: grid;
  place-items: center;
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: rgba(0,0,0,.45);
  color: #fff;
  font-size: 20px;
  padding-inline-start: 4px;
}

.ccb-09 .ccb-09__topbar {
  position: absolute;
  inset-inline: 0;
  top: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 12px 26px 16px;
  background: linear-gradient(180deg,rgba(0,0,0,.62),transparent);
  transition: opacity .3s ease;
}

.ccb-09 .ccb-09__player.is-idle .ccb-09__topbar {
  opacity: 0;
  pointer-events: none;
}

.ccb-09 .ccb-09__player:focus-within .ccb-09__topbar {
  opacity: 1;
  pointer-events: auto;
}

.ccb-09 .ccb-09__title {
  font-size: 13px;
  color: rgba(255,255,255,.95);
  text-shadow: 0 1px 4px rgba(0,0,0,.5);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ccb-09 .ccb-09__close {
  display: grid;
  place-items: center;
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  border: 1px solid rgba(255,255,255,.16);
  border-radius: 50%;
  background: rgba(15,15,18,.55);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  cursor: pointer;
  transition: background-color .15s ease,transform .15s ease;
}

.ccb-09 .ccb-09__close:hover {
  background: rgba(15,15,18,.8);
}

.ccb-09 .ccb-09__close:active {
  transform: scale(.9);
}

.ccb-09 .ccb-09__close:focus-visible {
  outline: 2.5px solid #fff;
  outline-offset: 2px;
}

.ccb-09 .ccb-09__x {
  position: relative;
  width: 14px;
  height: 14px;
}

.ccb-09 .ccb-09__x::before,
.ccb-09 .ccb-09__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 14px;
  height: 1.8px;
  border-radius: 2px;
  background: #fff;
}

.ccb-09 .ccb-09__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-09 .ccb-09__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-09 .ccb-09__hint {
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 10.5px;
  color: rgba(255,255,255,.55);
}

@media (prefers-reduced-motion: reduce) {
  .ccb-09 .ccb-09__topbar,
    .ccb-09 .ccb-09__close {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const player = document.getElementById('ccb-09-player'); if (!player) return;
  const IDLE = 2400; let timer;
  const wake = () => {
    player.classList.remove('is-idle');
    clearTimeout(timer);
    timer = setTimeout(() => player.classList.add('is-idle'), IDLE);
  };
  player.addEventListener('pointermove', wake);
  player.addEventListener('pointerdown', wake);
  wake();                                        // arm the timer on load
})();
```
