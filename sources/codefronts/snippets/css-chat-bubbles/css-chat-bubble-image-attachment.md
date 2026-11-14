---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/css-chat-bubble-image-attachment/"
title: "CSS Chat Bubble Image Attachment"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "Five media bubbles that cover almost every attachment a messenger has to render: a single photo with an overlaid caption, a mosaic grid that collapses extra…"
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Chat Bubble Image Attachment
Source: https://codefronts.com/snippets/css-chat-bubbles/css-chat-bubble-image-attachment/

Five media bubbles that cover almost every attachment a messenger has to render: a single photo with an overlaid caption, a mosaic grid that collapses extra images into a +N tile, a video preview with duration and play affordance, a file card with a conic progress ring, and a link preview. Clicking any photo opens it in a native <dialog> lightbox with Escape, backdrop dismiss and focus return handled by the platform.
## HTML
```html
<div class="cb-10">
  <button class="cb-10__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-10__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-10__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <ol class="cb-10__thread" aria-label="Conversation with attachments">
    <li class="cb-10__turn cb-10__turn--in">
      <div class="cb-10__bubble cb-10__bubble--media">
        <button class="cb-10__shot" type="button" data-full="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1600&q=80" aria-label="Open photo: ridge above the treeline at sunrise">
          <img class="cb-10__photo" src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=720&q=70" width="720" height="540" alt="Ridge above the treeline at sunrise" loading="lazy" decoding="async">
          <span class="cb-10__scrim" aria-hidden="true"></span>
          <span class="cb-10__cap">Made it to the ridge before the light did</span>
        </button>
        <span class="cb-10__meta"><time datetime="2027-06-14T05:52">05:52</time></span>
      </div>
    </li>

    <li class="cb-10__turn cb-10__turn--out">
      <div class="cb-10__bubble cb-10__bubble--media">
        <div class="cb-10__grid">
          <button class="cb-10__shot cb-10__shot--a" type="button" data-full="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1600&q=80" aria-label="Open photo: sunlight through a beech forest">
            <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=560&q=70" width="560" height="560" alt="Sunlight through a beech forest" loading="lazy" decoding="async">
          </button>
          <button class="cb-10__shot cb-10__shot--b" type="button" data-full="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1600&q=80" aria-label="Open photo: fog rolling over a valley">
            <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=420&q=70" width="420" height="280" alt="Fog rolling over a valley" loading="lazy" decoding="async">
          </button>
          <button class="cb-10__shot cb-10__shot--c" type="button" data-full="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1600&q=80" aria-label="Open photo: night sky over a mountain lake, plus 3 more attachments">
            <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=420&q=70" width="420" height="280" alt="Night sky over a mountain lake" loading="lazy" decoding="async">
            <span class="cb-10__more" aria-hidden="true">+3</span>
          </button>
        </div>
        <span class="cb-10__meta"><time datetime="2027-06-14T06:10">06:10</time></span>
      </div>
    </li>

    <li class="cb-10__turn cb-10__turn--in">
      <div class="cb-10__bubble cb-10__bubble--media">
        <div class="cb-10__video">
          <img class="cb-10__photo" src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=720&q=70" width="720" height="405" alt="Video: the last of the ramen at the summit hut" loading="lazy" decoding="async">
          <span class="cb-10__scrim" aria-hidden="true"></span>
          <button class="cb-10__play" type="button" aria-label="Play video, 42 seconds">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5.5 19 12 8 18.5z" fill="currentColor"/></svg>
          </button>
          <span class="cb-10__dur">0:42</span>
        </div>
        <span class="cb-10__meta"><time datetime="2027-06-14T06:22">06:22</time></span>
      </div>
    </li>

    <li class="cb-10__turn cb-10__turn--out">
      <div class="cb-10__bubble">
        <div class="cb-10__file">
          <span class="cb-10__ring" id="cb-10-ring" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Uploading route file">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M14 3.5H7.5A1.5 1.5 0 0 0 6 5v14a1.5 1.5 0 0 0 1.5 1.5h9A1.5 1.5 0 0 0 18 19V7.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M13.8 3.6V7.4h4" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
          </span>
          <span class="cb-10__file-text">
            <b>north-ridge-route.gpx</b>
            <small id="cb-10-size">1.8 MB · uploading</small>
          </span>
        </div>
        <span class="cb-10__meta"><time datetime="2027-06-14T06:25">06:25</time></span>
      </div>
    </li>

    <li class="cb-10__turn cb-10__turn--in">
      <div class="cb-10__bubble cb-10__bubble--media">
        <a class="cb-10__link" href="https://unsplash.com" target="_blank" rel="noreferrer noopener">
          <img src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=560&q=70" width="560" height="240" alt="" loading="lazy" decoding="async">
          <span class="cb-10__link-body">
            <b>Hut-to-hut: the classic four-day traverse</b>
            <small>Two nights up high, one long descent, and the best coffee on the route.</small>
            <em>trailnotes.example</em>
          </span>
        </a>
        <span class="cb-10__meta"><time datetime="2027-06-14T06:31">06:31</time></span>
      </div>
    </li>
  </ol>

  <dialog class="cb-10__lightbox" id="cb-10-lightbox" aria-label="Photo viewer">
    <img id="cb-10-lightbox-img" alt="">
    <button class="cb-10__close" type="button" aria-label="Close photo viewer">
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>
    </button>
  </dialog>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;500;600;700&display=swap');

@property --cb-10-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.cb-10 {
  --bg: #f3f2ef;
  --surface: #ffffff;
  --ink: #141310;
  --muted: #6a675f;
  --line: #e5e3dc;
  --in: #ffffff;
  --in-ink: #141310;
  --out: #2b2a26;
  --out-ink: #f7f6f2;
  --acc: #e0533f;
  --ph: #d8d6cf;
  --shadow: rgba(20,19,16,.16);
  --radius: 1.35rem;
  --sans: "Bricolage Grotesque",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(80% 50% at 15% 0%, color-mix(in oklab,var(--acc) 10%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-10,
.cb-10 *,
.cb-10 *::before,
.cb-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-10 {
    --bg: oklch(96% .006 95);
    --surface: oklch(100% 0 0);
    --ink: oklch(17% .015 80);
    --muted: oklch(52% .015 85);
    --line: oklch(91% .008 90);
    --out: oklch(27% .01 85);
    --acc: oklch(60% .17 35);
  }
}

.cb-10 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cb-10 a {
  color: var(--acc);
}

.cb-10 a:hover {
  color: color-mix(in oklab,var(--acc) 75%,var(--ink));
}

.cb-10__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  z-index: 3;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-10__theme:hover {
  transform: translateY(-2px);
}

.cb-10__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-10__sun {
  display: none;
}

.cb-10__thread {
  list-style: none;
  margin: 0;
  inline-size: min(100%,30rem);
  max-block-size: min(90svh,48rem);
  padding: clamp(.9rem,3vw,1.4rem);
  display: grid;
  gap: .7rem;
  align-content: start;
  overflow-y: auto;
  overflow-x: clip;
  scrollbar-width: thin;
  border-radius: calc(var(--radius) + .5rem);
  background: color-mix(in oklab,var(--surface) 62%,transparent);
  border: 1px solid var(--line);
  box-shadow: 0 40px 90px -60px var(--shadow);
  backdrop-filter: blur(14px);
}

.cb-10__turn {
  display: flex;
}

.cb-10__turn--out {
  justify-content: flex-end;
}

.cb-10__bubble {
  position: relative;
  max-inline-size: min(21rem,86%);
  padding: .5rem .55rem .35rem;
  border-radius: var(--radius);
  background: var(--in);
  color: var(--in-ink);
  box-shadow: 0 2px 8px -4px var(--shadow);
  animation: cb-10-in .45s cubic-bezier(.16,1,.3,1) backwards;
}

.cb-10__turn--out .cb-10__bubble {
  background: var(--out);
  color: var(--out-ink);
}

.cb-10__turn--in .cb-10__bubble {
  border-end-start-radius: .45rem;
}

.cb-10__turn--out .cb-10__bubble {
  border-end-end-radius: .45rem;
}

@keyframes cb-10-in {
  from {
    opacity: 0;
    translate: 0 10px;
    scale: .97;
  }

  to {
    opacity: 1;
    translate: 0;
    scale: 1;
  }
}

.cb-10__meta {
  display: block;
  padding: .3rem .45rem .15rem;
  text-align: end;
  font-size: .66rem;
  font-weight: 500;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cb-10__turn--out .cb-10__meta {
  color: color-mix(in oklab,var(--out-ink) 65%,transparent);
}
/* single photo */

.cb-10__shot {
  position: relative;
  display: block;
  inline-size: 100%;
  padding: 0;
  border: 0;
  cursor: pointer;
  background: var(--ph);
  border-radius: 1rem;
  overflow: hidden;
  transition: transform .3s cubic-bezier(.16,1,.3,1);
}

.cb-10__shot:hover {
  transform: scale(1.012);
}

.cb-10__shot img,
.cb-10__photo {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  background: var(--ph);
}

.cb-10__bubble--media > .cb-10__shot > .cb-10__photo {
  aspect-ratio: 4/3;
}

.cb-10__scrim {
  position: absolute;
  inset: auto 0 0 0;
  block-size: 55%;
  pointer-events: none;
  background: linear-gradient(to top, rgb(0 0 0 / .62), rgb(0 0 0 / .12) 55%, transparent);
}

.cb-10__cap {
  position: absolute;
  inset: auto .85rem .7rem;
  color: #fff;
  text-align: start;
  font-size: .88rem;
  font-weight: 500;
  line-height: 1.35;
  letter-spacing: -.01em;
  text-wrap: balance;
}
/* mosaic */

.cb-10__grid {
  display: grid;
  gap: 2px;
  grid-template-areas: 'a b' 'a c';
  grid-template-columns: 1.35fr 1fr;
  aspect-ratio: 1.15;
  border-radius: 1rem;
  overflow: hidden;
}

.cb-10__grid .cb-10__shot {
  border-radius: 0;
  block-size: 100%;
}

.cb-10__shot--a {
  grid-area: a;
}

.cb-10__shot--b {
  grid-area: b;
}

.cb-10__shot--c {
  grid-area: c;
}

.cb-10__more {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  background: rgb(0 0 0 / .5);
  color: #fff;
  font-size: 1.35rem;
  font-weight: 600;
  backdrop-filter: blur(2px);
}
/* video */

.cb-10__video {
  position: relative;
  border-radius: 1rem;
  overflow: hidden;
  background: var(--ph);
}

.cb-10__video .cb-10__photo {
  aspect-ratio: 16/9;
}

.cb-10__play {
  position: absolute;
  inset: 50% auto auto 50%;
  translate: -50% -50%;
  inline-size: 56px;
  block-size: 56px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  background: rgb(255 255 255 / .92);
  color: #111;
  box-shadow: 0 10px 30px -12px rgb(0 0 0 / .6);
  transition: transform .3s cubic-bezier(.16,1,.3,1), background .25s;
}

.cb-10__play svg {
  inline-size: 26px;
  block-size: 26px;
  margin-inline-start: 2px;
}

.cb-10__play:hover {
  transform: translate(-50%,-50%) scale(1.08);
  background: #fff;
}

.cb-10__dur {
  position: absolute;
  inset: auto .6rem .6rem auto;
  padding: .15rem .45rem;
  border-radius: .4rem;
  background: rgb(0 0 0 / .62);
  color: #fff;
  font-size: .7rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}
/* file card + conic ring */

.cb-10__file {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .5rem .55rem;
}

.cb-10__ring {
  position: relative;
  flex: 0 0 auto;
  inline-size: 2.9rem;
  block-size: 2.9rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: conic-gradient(var(--acc) var(--cb-10-p), color-mix(in oklab,var(--out-ink) 22%,transparent) 0);
  animation: cb-10-fill 3.2s cubic-bezier(.16,1,.3,1) forwards;
}

.cb-10__ring::before {
  content: '';
  position: absolute;
  inset: 3px;
  border-radius: 50%;
  background: var(--out);
}

.cb-10__ring svg {
  position: relative;
  inline-size: 20px;
  block-size: 20px;
  color: var(--out-ink);
}

@keyframes cb-10-fill {
  from {
    --cb-10-p: 0%;
  }

  to {
    --cb-10-p: 100%;
  }
}

.cb-10__file-text {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
}

.cb-10__file-text b {
  font-size: .92rem;
  font-weight: 600;
  letter-spacing: -.01em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.cb-10__file-text small {
  font-size: .72rem;
  color: color-mix(in oklab,var(--out-ink) 65%,transparent);
  font-variant-numeric: tabular-nums;
}
/* link preview */

.cb-10__link {
  display: grid;
  text-decoration: none;
  color: inherit;
  border-radius: 1rem;
  overflow: hidden;
  background: color-mix(in oklab,var(--ink) 5%,transparent);
  transition: transform .3s cubic-bezier(.16,1,.3,1);
}

.cb-10__link:hover {
  transform: translateY(-2px);
}

.cb-10__link img {
  aspect-ratio: 21/9;
  inline-size: 100%;
  object-fit: cover;
}

.cb-10__link-body {
  display: grid;
  gap: .2rem;
  padding: .7rem .85rem .8rem;
}

.cb-10__link-body b {
  font-size: .92rem;
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.cb-10__link-body small {
  font-size: .78rem;
  line-height: 1.4;
  color: var(--muted);
}

.cb-10__link-body em {
  font-style: normal;
  font-size: .68rem;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--acc);
}
/* lightbox */

.cb-10__lightbox {
  margin: auto;
  padding: 0;
  border: 0;
  max-inline-size: min(94vw,64rem);
  max-block-size: 90svh;
  background: transparent;
  overflow: visible;
  opacity: 0;
  scale: .94;
  transition: opacity .3s, scale .3s, display .3s allow-discrete, overlay .3s allow-discrete;
}

.cb-10__lightbox[open] {
  opacity: 1;
  scale: 1;
}

@starting-style {
  .cb-10__lightbox[open] {
    opacity: 0;
    scale: .94;
  }
}

.cb-10__lightbox::backdrop {
  background: rgb(6 6 6 / .74);
  backdrop-filter: blur(8px) saturate(1.2);
}

.cb-10__lightbox img {
  display: block;
  inline-size: 100%;
  block-size: auto;
  max-block-size: 90svh;
  object-fit: contain;
  border-radius: 1rem;
}

.cb-10__close {
  position: absolute;
  inset-block-start: -3.25rem;
  inset-inline-end: 0;
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  background: rgb(255 255 255 / .14);
  color: #fff;
  backdrop-filter: blur(10px);
}

.cb-10__close:hover {
  background: rgb(255 255 255 / .26);
}

.cb-10__close svg {
  inline-size: 20px;
  block-size: 20px;
}
/* dark */

.cb-10[data-theme="dark"] {
  --bg: #0d0c0a;
  --surface: #171613;
  --ink: #f4f2ec;
  --muted: #9b978d;
  --line: #242220;
  --in: #1d1b18;
  --in-ink: #f4f2ec;
  --out: #f0eee7;
  --out-ink: #16150f;
  --ph: #2a2825;
  --shadow: rgba(0,0,0,.72);
}

.cb-10[data-theme="dark"] .cb-10__moon {
  display: none;
}

.cb-10[data-theme="dark"] .cb-10__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .cb-10:not([data-theme="light"]) {
    --bg: #0d0c0a;
    --surface: #171613;
    --ink: #f4f2ec;
    --muted: #9b978d;
    --line: #242220;
    --in: #1d1b18;
    --in-ink: #f4f2ec;
    --out: #f0eee7;
    --out-ink: #16150f;
    --ph: #2a2825;
    --shadow: rgba(0,0,0,.72);
  }

  .cb-10:not([data-theme="light"]) .cb-10__moon {
    display: none;
  }

  .cb-10:not([data-theme="light"]) .cb-10__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-10 *,
    .cb-10 *::before,
    .cb-10 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cb-10__ring {
    --cb-10-p: 100%;
  }
}

@media (forced-colors: active) {
  .cb-10__bubble,
    .cb-10__link,
    .cb-10__shot {
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-10');
  if (!root) return;
  const box = root.querySelector('#cb-10-lightbox');
  const img = root.querySelector('#cb-10-lightbox-img');
  const close = root.querySelector('.cb-10__close');
  const size = root.querySelector('#cb-10-size');
  const ring = root.querySelector('#cb-10-ring');

  /* lightbox — the platform handles focus trap, Escape and focus return */
  root.querySelectorAll('.cb-10__shot').forEach((shot) => {
    shot.addEventListener('click', () => {
      const thumb = shot.querySelector('img');
      img.src = shot.dataset.full || thumb.src;
      img.alt = thumb.alt || '';
      box.showModal();
    });
  });
  close.addEventListener('click', () => box.close());
  box.addEventListener('click', (e) => { if (e.target === box) box.close(); });   /* backdrop dismiss */
  box.addEventListener('close', () => { img.removeAttribute('src'); });

  /* upload progress mirrored into the progressbar role */
  let p = 0;
  const tick = setInterval(() => {
    p = Math.min(100, p + 4);
    ring.setAttribute('aria-valuenow', p);
    size.textContent = p < 100 ? '1.8 MB · ' + p + '%' : '1.8 MB · sent';
    if (p >= 100) clearInterval(tick);
  }, 128);

  /* play button: swap in a real <video> in production */
  const play = root.querySelector('.cb-10__play');
  play.addEventListener('click', () => {
    play.animate([{ transform: 'translate(-50%,-50%) scale(1)' }, { transform: 'translate(-50%,-50%) scale(.86)' }, { transform: 'translate(-50%,-50%) scale(1)' }], { duration: 320, easing: 'cubic-bezier(.16,1,.3,1)' });
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.cb-10');
  const btn = root && root.querySelector('.cb-10__theme');
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
