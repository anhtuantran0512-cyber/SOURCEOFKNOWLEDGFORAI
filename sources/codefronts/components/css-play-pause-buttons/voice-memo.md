---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/voice-memo/"
title: "Voice Note Audio Player Control"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "The messaging-app voice note, rebuilt as a clean component: a chat bubble with a play button, a bar waveform that fills left-to-right as the message plays,…"
has_js: "true"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Voice Note Audio Player Control
Source: https://codefronts.com/components/css-play-pause-buttons/voice-memo/

The messaging-app voice note, rebuilt as a clean component: a chat bubble with a play button, a bar waveform that fills left-to-right as the message plays, and a live timer. The waveform progress is a single custom property — each bar decides its own colour by comparing its index to the progress, which means one number drives forty elements with no per-bar DOM writes.
## HTML
```html
<section class="pp-18" aria-label="Voice note audio player control demo">
  <div class="pp-18__stage">
    <div class="pp-18__thread">
      <div class="pp-18__bubble" style="--pp-18-progress:0">
        <img class="pp-18__avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=160&auto=format&fit=crop" alt="" width="40" height="40" loading="lazy">
        <button class="pp-18__btn" type="button" aria-pressed="false">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
            <path class="pp-18__p" d="M9 5.8v12.4L18.6 12z" fill="currentColor"/>
            <path class="pp-18__q" d="M8.6 5.8h3.1v12.4H8.6zM13 5.8h3.1v12.4H13z" fill="currentColor"/>
          </svg>
          <span class="pp-18__sr">Play voice message from Mira, 34 seconds</span>
        </button>
        <span class="pp-18__wave" aria-hidden="true">
          <i style="--pp-18-at:.02;--pp-18-h:34%"></i><i style="--pp-18-at:.07;--pp-18-h:58%"></i><i style="--pp-18-at:.12;--pp-18-h:82%"></i><i style="--pp-18-at:.17;--pp-18-h:46%"></i><i style="--pp-18-at:.22;--pp-18-h:96%"></i><i style="--pp-18-at:.27;--pp-18-h:64%"></i><i style="--pp-18-at:.32;--pp-18-h:38%"></i><i style="--pp-18-at:.37;--pp-18-h:74%"></i><i style="--pp-18-at:.42;--pp-18-h:52%"></i><i style="--pp-18-at:.47;--pp-18-h:88%"></i><i style="--pp-18-at:.52;--pp-18-h:42%"></i><i style="--pp-18-at:.57;--pp-18-h:70%"></i><i style="--pp-18-at:.62;--pp-18-h:100%"></i><i style="--pp-18-at:.67;--pp-18-h:56%"></i><i style="--pp-18-at:.72;--pp-18-h:30%"></i><i style="--pp-18-at:.77;--pp-18-h:66%"></i><i style="--pp-18-at:.82;--pp-18-h:48%"></i><i style="--pp-18-at:.87;--pp-18-h:78%"></i><i style="--pp-18-at:.92;--pp-18-h:36%"></i><i style="--pp-18-at:.97;--pp-18-h:26%"></i>
        </span>
        <span class="pp-18__time">0:34</span>
      </div>
      <p class="pp-18__stamp">Mira · 09:41 · delivered</p>
    </div>
    <p class="pp-18__chip" aria-hidden="true">one --progress property · per-bar background-size clamp · zero per-bar writes</p>
  </div>
</section>
```
## CSS
```css
.pp-18,
.pp-18 *,
.pp-18 *::before,
.pp-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-18-bg);
  --pp-18-bg: oklch(0.94 0.015 150);
  --pp-18-bubble: oklch(1 0 0);
  --pp-18-ink: oklch(0.26 0.02 160);
  --pp-18-mut: oklch(0.56 0.02 160);
  --pp-18-acc: oklch(0.6 0.15 155);
  --pp-18-idle: oklch(0.85 0.02 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-18-ink);
}

.pp-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 0%,oklch(0.9 0.05 150/.6),transparent 70%);
}

.pp-18__thread {
  width: min(100%,470px);
}

.pp-18__bubble {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px 12px 12px;
  border-radius: 20px 20px 20px 6px;
  background: var(--pp-18-bubble);
  box-shadow: 0 8px 24px oklch(0.4 0.04 160/.16);
}

.pp-18__avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: linear-gradient(135deg,var(--pp-18-acc),oklch(0.5 0.1 190));
}

.pp-18__btn {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  flex: none;
  border: 0;
  border-radius: 50%;
  background: var(--pp-18-acc);
  color: oklch(0.99 0 0);
  cursor: pointer;
  transition: transform .2s,background .2s;
}

.pp-18__btn:hover {
  background: color-mix(in oklch,var(--pp-18-acc) 88%,black);
}

.pp-18__btn:active {
  transform: scale(.93);
}

.pp-18__btn:focus-visible {
  outline: 3px solid var(--pp-18-ink);
  outline-offset: 2px;
}

.pp-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pp-18__q {
  display: none;
}

.pp-18__bubble[data-state="playing"] .pp-18__p {
  display: none;
}

.pp-18__bubble[data-state="playing"] .pp-18__q {
  display: block;
}

.pp-18__wave {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 2.5px;
  height: 34px;
  min-width: 0;
}

.pp-18__wave i {
  flex: 1;
  height: var(--pp-18-h);
  min-width: 2px;
  border-radius: 99px;
  background-color: var(--pp-18-idle);
  background-image: linear-gradient(var(--pp-18-acc) 0 0);
  background-repeat: no-repeat;
  background-size: calc((var(--pp-18-progress) - var(--pp-18-at)) * 10000%) 100%;
  transition: background-size .12s linear;
}

.pp-18__time {
  font-size: 12px;
  font-variant-numeric: tabular-nums;
  color: var(--pp-18-mut);
  flex: none;
}

.pp-18__stamp {
  margin-top: 9px;
  padding-left: 6px;
  font-size: 11.5px;
  color: var(--pp-18-mut);
}

.pp-18__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-18-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0.26 0.02 160/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-18 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.pp-18__bubble').forEach((bubble) => {
    if (bubble.dataset.wired) return;
    bubble.dataset.wired = '1';
    const btn = bubble.querySelector('.pp-18__btn');
    const time = bubble.querySelector('.pp-18__time');
    const sr = bubble.querySelector('.pp-18__sr');
    const total = 34;
    let t = 0, id = 0;
    const fmt = (s) => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
    const stop = (reset) => {
      clearInterval(id); id = 0;
      bubble.dataset.state = 'paused';
      btn.setAttribute('aria-pressed', 'false');
      sr.textContent = 'Play voice message from Mira, 34 seconds';
      if (reset) { t = 0; bubble.style.setProperty('--pp-18-progress', 0); time.textContent = fmt(total); }
    };
    btn.addEventListener('click', () => {
      if (id) return stop(false);
      bubble.dataset.state = 'playing';
      btn.setAttribute('aria-pressed', 'true');
      sr.textContent = 'Pause voice message';
      id = setInterval(() => {
        t += 0.1;
        if (t >= total) return stop(true);
        bubble.style.setProperty('--pp-18-progress', (t / total).toFixed(3));
        time.textContent = fmt(t);
      }, 100);
    });
  });
})();
```
