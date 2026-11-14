---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/video-upload-with-frame-preview/"
title: "Video Upload with Frame Preview"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "Upload a video and choose its poster frame — the way every serious video product does it."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Upload with Frame Preview
Source: https://codefronts.com/components/css-file-upload-button/video-upload-with-frame-preview/

Upload a video and choose its poster frame — the way every serious video product does it. The <video> element is seeked to evenly spaced timestamps and each frame is painted into a <canvas> with drawImage, producing a real filmstrip from the user's own file. Duration is formatted with Intl.NumberFormat, and the selected frame is a radio group, so arrow keys move between frames natively.
## HTML
```html
<div class="fu-13">
  <button class="fu-13__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-13__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-13__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-13__card" aria-labelledby="fu-13-h">
    <header class="fu-13__head">
      <div>
        <h2 class="fu-13__h" id="fu-13-h">Video upload</h2>
        <p class="fu-13__meta" id="fu-13-meta">MP4, WEBM or MOV <span aria-hidden="true">·</span> up to 2 GB</p>
      </div>
      <span class="fu-13__dur" id="fu-13-dur">--:--</span>
    </header>

    <div class="fu-13__stage">
      <video class="fu-13__video" id="fu-13-video" muted playsinline preload="metadata"></video>
      <span class="fu-13__idle" id="fu-13-idle">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9.6 8.4v7.2l6-3.6z" fill="currentColor"/><rect x="3.2" y="4.6" width="17.6" height="14.8" rx="2.6" stroke="currentColor" stroke-width="1.6"/></svg>
        <span>No video selected</span>
      </span>
      <canvas class="fu-13__canvas" id="fu-13-canvas" width="320" height="180" aria-hidden="true"></canvas>
    </div>

    <fieldset class="fu-13__strip" id="fu-13-strip" disabled>
      <legend class="fu-13__legend">Poster frame</legend>
      <label class="fu-13__frame"><input type="radio" name="fu-13-frame" value="0" checked><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E" alt="Frame 1"><span>0:00</span></label>
      <label class="fu-13__frame"><input type="radio" name="fu-13-frame" value="1"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E" alt="Frame 2"><span>--</span></label>
      <label class="fu-13__frame"><input type="radio" name="fu-13-frame" value="2"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E" alt="Frame 3"><span>--</span></label>
      <label class="fu-13__frame"><input type="radio" name="fu-13-frame" value="3"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E" alt="Frame 4"><span>--</span></label>
    </fieldset>

    <div class="fu-13__actions">
      <input class="fu-13__input" id="fu-13-file" type="file" accept="video/mp4,video/webm,video/quicktime">
      <label class="fu-13__pick" for="fu-13-file">Choose video</label>
      <button class="fu-13__go" id="fu-13-go" type="button" disabled>Publish</button>
    </div>
    <p class="fu-13__status" id="fu-13-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-13 {
  --bg: #08090c;
  --surface: #101218;
  --raise: #171a22;
  --ink: #eef0f5;
  --muted: #848c9d;
  --line: #232834;
  --acc: #ff2d78;
  --acc2: #38bdf8;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(70% 45% at 15% 0%, color-mix(in oklab,var(--acc) 16%,transparent), transparent 60%), radial-gradient(60% 40% at 100% 100%, color-mix(in oklab,var(--acc2) 14%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-13,
.fu-13 *,
.fu-13 *::before,
.fu-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-13 {
    --acc: oklch(64% .25 5);
    --acc2: oklch(78% .13 232);
  }
}

.fu-13__card {
  inline-size: min(32rem,100%);
  display: grid;
  gap: .9rem;
  padding: clamp(1.1rem,3.5vw,1.5rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  box-shadow: 0 40px 90px -60px #000;
}

.fu-13__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.fu-13__h {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -.03em;
}

.fu-13__meta {
  margin: .2rem 0 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
}

.fu-13__dur {
  font-family: var(--mono);
  font-size: .75rem;
  padding: .3rem .55rem;
  border-radius: .5rem;
  background: color-mix(in oklab,var(--acc2) 14%,transparent);
  color: var(--acc2);
  font-variant-numeric: tabular-nums;
  flex: none;
}

.fu-13__stage {
  position: relative;
  display: grid;
  place-items: center;
  aspect-ratio: 16/9;
  overflow: hidden;
  border-radius: 1rem;
  background: #000;
  border: 1px solid var(--line);
}

.fu-13__video {
  inline-size: 100%;
  block-size: 100%;
  object-fit: contain;
  display: block;
  background: #000;
}

.fu-13__idle {
  position: absolute;
  display: grid;
  justify-items: center;
  gap: .4rem;
  color: var(--muted);
  font-family: var(--mono);
  font-size: .75rem;
  pointer-events: none;
  background: color-mix(in oklab,#000 55%,transparent);
  padding: 1rem 1.4rem;
  border-radius: .8rem;
}

.fu-13__idle[hidden] {
  display: none;
}

.fu-13__idle svg {
  inline-size: 2rem;
  block-size: 2rem;
}

.fu-13__canvas {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.fu-13__strip {
  border: 0;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .5rem;
  transition: opacity .3s ease;
}

.fu-13__strip:disabled {
  opacity: .4;
}

.fu-13__legend {
  padding: 0;
  margin-block-end: .45rem;
  font-family: var(--mono);
  font-size: .5625rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.fu-13__frame {
  position: relative;
  display: grid;
  gap: .25rem;
  cursor: pointer;
  border-radius: .7rem;
  overflow: hidden;
}

.fu-13__frame input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.fu-13__frame img {
  inline-size: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
  display: block;
  border-radius: .6rem;
  background: var(--raise);
  border: 2px solid transparent;
  transition: border-color .2s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.fu-13__frame span {
  font-family: var(--mono);
  font-size: .5625rem;
  color: var(--muted);
  text-align: center;
  font-variant-numeric: tabular-nums;
}

.fu-13__frame:hover img {
  transform: translateY(-2px);
}

.fu-13__frame input:checked + img {
  border-color: var(--acc);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--acc) 25%,transparent);
}

.fu-13__frame input:checked ~ span {
  color: var(--acc);
}

.fu-13__frame input:focus-visible + img {
  outline: 2px solid var(--acc2);
  outline-offset: 2px;
}

.fu-13__actions {
  display: flex;
  gap: .5rem;
}

.fu-13__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: 0;
  border: 0;
  overflow: hidden;
  opacity: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
}

.fu-13__pick {
  flex: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  min-block-size: 2.85rem;
  padding: .6rem 1rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: var(--raise);
  color: var(--ink);
  font-size: .9375rem;
  font-weight: 600;
  transition: border-color .2s ease, background .2s ease;
}

.fu-13__pick:hover {
  border-color: var(--acc2);
  background: color-mix(in oklab,var(--acc2) 10%,var(--raise));
}

.fu-13__input:focus-visible + .fu-13__pick {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-13__go {
  min-block-size: 2.85rem;
  padding: .6rem 1.35rem;
  cursor: pointer;
  border: 0;
  border-radius: .8rem;
  background: var(--acc);
  color: #fff;
  font-family: var(--sans);
  font-size: .9375rem;
  font-weight: 700;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1), opacity .2s ease;
}

.fu-13__go:hover:not(:disabled) {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-13__go:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.fu-13__go:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-13__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

@media (prefers-color-scheme: light) {
  .fu-13:not([data-theme="dark"]) {
    --bg: #f3f4f7;
    --surface: #ffffff;
    --raise: #f5f6f9;
    --ink: #0c0e14;
    --muted: #5b6376;
    --line: #e3e6ec;
    --acc: #d81a5f;
    --acc2: #0b7fb5;
  }
}

.fu-13[data-theme="light"] {
  --bg: #f3f4f7;
  --surface: #ffffff;
  --raise: #f5f6f9;
  --ink: #0c0e14;
  --muted: #5b6376;
  --line: #e3e6ec;
  --acc: #d81a5f;
  --acc2: #0b7fb5;
}

@media (prefers-reduced-motion: reduce) {
  .fu-13 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-13__card,
    .fu-13__stage,
    .fu-13__pick {
    border: 1px solid CanvasText;
  }

  .fu-13__frame input:checked + img {
    border-color: Highlight;
  }

  .fu-13__go {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-13 {
  position: relative;
}

.fu-13__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.4rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.4rem);
  z-index: 20;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,currentColor 30%,transparent);
  background: color-mix(in oklab,currentColor 12%,transparent);
  color: inherit;
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.fu-13__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-13__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-13__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-13__sun {
  display: none;
}

.fu-13__theme[aria-pressed="true"] .fu-13__sun {
  display: block;
}

.fu-13__theme[aria-pressed="true"] .fu-13__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-13__theme {
    transition: none;
  }

  .fu-13__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-13__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-13');
  if (!root) return;
  const input = root.querySelector('#fu-13-file');
  const video = root.querySelector('#fu-13-video');
  const canvas = root.querySelector('#fu-13-canvas');
  const strip = root.querySelector('#fu-13-strip');
  const idle = root.querySelector('#fu-13-idle');
  const durEl = root.querySelector('#fu-13-dur');
  const metaEl = root.querySelector('#fu-13-meta');
  const go = root.querySelector('#fu-13-go');
  const status = root.querySelector('#fu-13-status');
  const ctx = canvas.getContext('2d');
  let url = null;

  const clock = (s) => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');

  const grab = (t) => new Promise(res => {
    video.addEventListener('seeked', () => {
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
      res(canvas.toDataURL('image/jpeg', 0.72));
    }, { once: true });
    video.currentTime = t;
  });

  input.addEventListener('change', async () => {
    const file = input.files && input.files[0];
    if (!file || !file.type.startsWith('video/')) return;
    if (url) URL.revokeObjectURL(url);
    url = URL.createObjectURL(file);
    video.src = url; idle.hidden = true;
    metaEl.textContent = file.name;
    status.textContent = 'Reading ' + file.name + '…';

    await new Promise(r => video.addEventListener('loadedmetadata', r, { once: true }));
    durEl.textContent = clock(video.duration);
    canvas.width = 320; canvas.height = Math.round(320 * (video.videoHeight / video.videoWidth || 0.5625));

    const frames = [...strip.querySelectorAll('.fu-13__frame')];
    for (let i = 0; i < frames.length; i++) {
      const t = (video.duration * (i + 0.5)) / frames.length;
      frames[i].querySelector('img').src = await grab(t);
      frames[i].querySelector('span').textContent = clock(t);
    }
    video.currentTime = 0;
    strip.disabled = false; go.disabled = false;
    status.textContent = file.name + ' loaded — pick a poster frame';
  });

  strip.addEventListener('change', (e) => {
    const t = Number(e.target.value);
    status.textContent = 'Poster frame ' + (t + 1) + ' of 4 selected';
  });

  go.addEventListener('click', () => {            // simulated publish
    go.disabled = true; status.textContent = 'Uploading video…';
    setTimeout(() => { status.textContent = 'Video published with the selected poster frame'; go.disabled = false; }, 2000);
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-13');
  const btn = root && root.querySelector('.fu-13__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
