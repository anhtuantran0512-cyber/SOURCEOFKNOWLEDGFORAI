---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/podcast-episode-list-layout/"
title: "Podcast Episode List Layout"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A podcast index built for scanning: three-digit episode numbers in a mono gutter, a 44px play button that morphs to pause, duration and season chips, and a…"
has_js: "true"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Podcast Episode List Layout
Source: https://codefronts.com/layouts/css-blog-layouts/podcast-episode-list-layout/

A podcast index built for scanning: three-digit episode numbers in a mono gutter, a 44px play button that morphs to pause, duration and season chips, and a CSS-only waveform that animates only for the playing row. The waveform is 32 divs with a random --h — no canvas, no audio-analyser, no 40kb wave library.
## HTML
```html
<div class="bl-06">
  <header class="bl-06__head">
    <div class="bl-06__cover" aria-hidden="true">
      <img src="https://images.unsplash.com/photo-1478737270239-2f02b77fc618?w=600&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="600" height="600" loading="eager" decoding="async">
    </div>
    <div class="bl-06__intro">
      <p class="bl-06__eyebrow">Season 4 · Fortnightly</p>
      <h1>Signal &amp; Static</h1>
      <p>Conversations with the people who maintain the boring, load-bearing parts of the internet. Hosted by Nia Okoro.</p>
      <div class="bl-06__where">
        <a href="#">Apple Podcasts</a><a href="#">Spotify</a><a href="#">Overcast</a><a href="#">RSS</a>
      </div>
    </div>
  </header>

  <main class="bl-06__list" aria-label="Episodes">
    <article class="bl-06__row" data-state="playing" data-season="4" style="--progress:.42">
      <p class="bl-06__num">118</p>
      <button class="bl-06__play" type="button" data-play aria-pressed="true">
        <svg class="bl-06__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path class="bl-06__tri" d="M9 6.5 18 12l-9 5.5z" fill="currentColor"/><g class="bl-06__pause"><rect x="8.5" y="6.5" width="2.6" height="11" rx="1" fill="currentColor"/><rect x="13" y="6.5" width="2.6" height="11" rx="1" fill="currentColor"/></g></svg>
        <span class="bl-06__srOnly" data-play-label>Pause episode 118</span>
      </button>
      <div class="bl-06__body">
        <h2><a href="#">The team that keeps NTP honest</a></h2>
        <p class="bl-06__desc">Four volunteers, one protocol, and every timestamp you have ever trusted.</p>
        <p class="bl-06__meta"><time datetime="2026-08-05">5 Aug 2026</time> · <span>Season 4</span> · <span>Transcript</span></p>
      </div>
      <div class="bl-06__wave" aria-hidden="true">
        <i style="--h:.35;--i:0"></i><i style="--h:.7;--i:1"></i><i style="--h:.45;--i:2"></i><i style="--h:.9;--i:3"></i><i style="--h:.6;--i:4"></i><i style="--h:.3;--i:5"></i><i style="--h:.75;--i:6"></i><i style="--h:.5;--i:7"></i><i style="--h:.85;--i:8"></i><i style="--h:.4;--i:9"></i><i style="--h:.65;--i:10"></i><i style="--h:.95;--i:11"></i><i style="--h:.55;--i:12"></i><i style="--h:.25;--i:13"></i><i style="--h:.7;--i:14"></i><i style="--h:.45;--i:15"></i><i style="--h:.8;--i:16"></i><i style="--h:.35;--i:17"></i><i style="--h:.6;--i:18"></i><i style="--h:.9;--i:19"></i><i style="--h:.5;--i:20"></i><i style="--h:.3;--i:21"></i><i style="--h:.75;--i:22"></i><i style="--h:.55;--i:23"></i>
      </div>
      <p class="bl-06__dur"><span class="bl-06__srOnly">Duration </span>58:12</p>
    </article>

    <article class="bl-06__row" data-state="idle" data-season="4">
      <p class="bl-06__num">117</p>
      <button class="bl-06__play" type="button" data-play aria-pressed="false">
        <svg class="bl-06__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path class="bl-06__tri" d="M9 6.5 18 12l-9 5.5z" fill="currentColor"/><g class="bl-06__pause"><rect x="8.5" y="6.5" width="2.6" height="11" rx="1" fill="currentColor"/><rect x="13" y="6.5" width="2.6" height="11" rx="1" fill="currentColor"/></g></svg>
        <span class="bl-06__srOnly" data-play-label>Play episode 117</span>
      </button>
      <div class="bl-06__body">
        <h2><a href="#">Twenty years of one open-source maintainer</a></h2>
        <p class="bl-06__desc">On burnout, funding, and the pull request that changed her mind about governance.</p>
        <p class="bl-06__meta"><time datetime="2026-07-22">22 Jul 2026</time> · <span>Season 4</span> · <span>Transcript</span></p>
      </div>
      <div class="bl-06__wave" aria-hidden="true">
        <i style="--h:.5;--i:0"></i><i style="--h:.3;--i:1"></i><i style="--h:.8;--i:2"></i><i style="--h:.55;--i:3"></i><i style="--h:.4;--i:4"></i><i style="--h:.7;--i:5"></i><i style="--h:.9;--i:6"></i><i style="--h:.35;--i:7"></i><i style="--h:.6;--i:8"></i><i style="--h:.45;--i:9"></i><i style="--h:.75;--i:10"></i><i style="--h:.25;--i:11"></i><i style="--h:.85;--i:12"></i><i style="--h:.5;--i:13"></i><i style="--h:.65;--i:14"></i><i style="--h:.3;--i:15"></i><i style="--h:.7;--i:16"></i><i style="--h:.95;--i:17"></i><i style="--h:.4;--i:18"></i><i style="--h:.55;--i:19"></i><i style="--h:.8;--i:20"></i><i style="--h:.35;--i:21"></i><i style="--h:.6;--i:22"></i><i style="--h:.45;--i:23"></i>
      </div>
      <p class="bl-06__dur"><span class="bl-06__srOnly">Duration </span>1:04:39</p>
    </article>

    <article class="bl-06__row" data-state="idle" data-season="4">
      <p class="bl-06__num">116</p>
      <button class="bl-06__play" type="button" data-play aria-pressed="false">
        <svg class="bl-06__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path class="bl-06__tri" d="M9 6.5 18 12l-9 5.5z" fill="currentColor"/><g class="bl-06__pause"><rect x="8.5" y="6.5" width="2.6" height="11" rx="1" fill="currentColor"/><rect x="13" y="6.5" width="2.6" height="11" rx="1" fill="currentColor"/></g></svg>
        <span class="bl-06__srOnly" data-play-label>Play episode 116</span>
      </button>
      <div class="bl-06__body">
        <h2><a href="#">Why undersea cable repair takes six weeks</a></h2>
        <p class="bl-06__desc">A ship's engineer explains the queue nobody outside the industry knows about.</p>
        <p class="bl-06__meta"><time datetime="2026-07-08">8 Jul 2026</time> · <span>Season 4</span> · <span>Transcript</span></p>
      </div>
      <div class="bl-06__wave" aria-hidden="true">
        <i style="--h:.65;--i:0"></i><i style="--h:.4;--i:1"></i><i style="--h:.55;--i:2"></i><i style="--h:.85;--i:3"></i><i style="--h:.3;--i:4"></i><i style="--h:.6;--i:5"></i><i style="--h:.45;--i:6"></i><i style="--h:.9;--i:7"></i><i style="--h:.35;--i:8"></i><i style="--h:.7;--i:9"></i><i style="--h:.5;--i:10"></i><i style="--h:.8;--i:11"></i><i style="--h:.25;--i:12"></i><i style="--h:.6;--i:13"></i><i style="--h:.95;--i:14"></i><i style="--h:.4;--i:15"></i><i style="--h:.55;--i:16"></i><i style="--h:.75;--i:17"></i><i style="--h:.3;--i:18"></i><i style="--h:.65;--i:19"></i><i style="--h:.45;--i:20"></i><i style="--h:.85;--i:21"></i><i style="--h:.5;--i:22"></i><i style="--h:.35;--i:23"></i>
      </div>
      <p class="bl-06__dur"><span class="bl-06__srOnly">Duration </span>47:05</p>
    </article>

    <article class="bl-06__row" data-state="idle" data-season="3">
      <p class="bl-06__num">115</p>
      <button class="bl-06__play" type="button" data-play aria-pressed="false">
        <svg class="bl-06__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path class="bl-06__tri" d="M9 6.5 18 12l-9 5.5z" fill="currentColor"/><g class="bl-06__pause"><rect x="8.5" y="6.5" width="2.6" height="11" rx="1" fill="currentColor"/><rect x="13" y="6.5" width="2.6" height="11" rx="1" fill="currentColor"/></g></svg>
        <span class="bl-06__srOnly" data-play-label>Play episode 115</span>
      </button>
      <div class="bl-06__body">
        <h2><a href="#">The last COBOL class in the country</a></h2>
        <p class="bl-06__desc">Season finale: what happens to knowledge when nobody is left to teach it.</p>
        <p class="bl-06__meta"><time datetime="2026-06-24">24 Jun 2026</time> · <span>Season 3</span> · <span>Transcript</span></p>
      </div>
      <div class="bl-06__wave" aria-hidden="true">
        <i style="--h:.45;--i:0"></i><i style="--h:.8;--i:1"></i><i style="--h:.35;--i:2"></i><i style="--h:.6;--i:3"></i><i style="--h:.95;--i:4"></i><i style="--h:.4;--i:5"></i><i style="--h:.55;--i:6"></i><i style="--h:.7;--i:7"></i><i style="--h:.3;--i:8"></i><i style="--h:.85;--i:9"></i><i style="--h:.5;--i:10"></i><i style="--h:.65;--i:11"></i><i style="--h:.4;--i:12"></i><i style="--h:.75;--i:13"></i><i style="--h:.25;--i:14"></i><i style="--h:.6;--i:15"></i><i style="--h:.9;--i:16"></i><i style="--h:.45;--i:17"></i><i style="--h:.55;--i:18"></i><i style="--h:.35;--i:19"></i><i style="--h:.7;--i:20"></i><i style="--h:.5;--i:21"></i><i style="--h:.8;--i:22"></i><i style="--h:.4;--i:23"></i>
      </div>
      <p class="bl-06__dur"><span class="bl-06__srOnly">Duration </span>1:12:58</p>
    </article>
  </main>

  <footer class="bl-06__footer">
    <p>All 118 episodes have transcripts. <a href="#">Browse by guest →</a></p>
  </footer>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap');

.bl-06 {
  --bg: #0b0d0c;
  --surface: #141817;
  --text: #f0f4f2;
  --muted: #8d968f;
  --line: #242a28;
  --acc: #a3e635;
  --acc-fg: #0b0d0c;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}

@supports (color: oklch(50% 0 0)) {
  .bl-06 {
    --bg: oklch(15% .008 160);
    --surface: oklch(21% .01 165);
    --text: oklch(96% .01 160);
    --muted: oklch(66% .015 160);
    --line: oklch(28% .012 165);
    --acc: oklch(86% .2 128);
  }
}

@media (prefers-color-scheme: light) {
  .bl-06:not([data-theme="dark"]) {
    --bg: #f7faf8;
    --surface: #ffffff;
    --text: #0b0f0d;
    --muted: #5c6560;
    --line: #dfe6e2;
    --acc: #3f6212;
    --acc-fg: #ffffff;
  }
}

.bl-06[data-theme="light"] {
  --bg: #f7faf8;
  --surface: #ffffff;
  --text: #0b0f0d;
  --muted: #5c6560;
  --line: #dfe6e2;
  --acc: #3f6212;
  --acc-fg: #ffffff;
}

.bl-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-06,
.bl-06 *,
.bl-06 *::before,
.bl-06 *::after {
  box-sizing: border-box;
}

.bl-06 a {
  color: inherit;
  text-decoration: none;
}

.bl-06 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.bl-06__srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bl-06__head {
  display: grid;
  grid-template-columns: auto minmax(0,1fr);
  gap: clamp(1.25rem,3vw,2.5rem);
  align-items: end;
  max-width: 72rem;
  margin-inline: auto;
  padding: clamp(2.5rem,7vw,5rem) clamp(1.25rem,4vw,3rem) clamp(1.75rem,3vw,2.5rem);
}

.bl-06__cover {
  width: clamp(6rem,14vw,11rem);
  aspect-ratio: 1;
  border-radius: 1rem;
  overflow: hidden;
  background: var(--line);
  box-shadow: 0 1.5rem 3rem -1rem rgba(0,0,0,.55);
}

.bl-06__cover img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.bl-06__intro {
  display: grid;
  gap: .65rem;
}

.bl-06__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-06__intro h1 {
  margin: 0;
  font-size: clamp(2rem,5.5vw,3.5rem);
  font-weight: 700;
  line-height: .98;
  letter-spacing: -.035em;
}

.bl-06__intro p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 52ch;
  text-wrap: pretty;
}

.bl-06__where {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  margin-top: .25rem;
}

.bl-06__where a {
  display: inline-grid;
  place-items: center;
  min-height: 2.25rem;
  padding: 0 .75rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .04em;
  color: var(--muted);
  transition: border-color .18s ease, color .18s ease;
}

.bl-06__where a:hover {
  border-color: var(--acc);
  color: var(--acc);
}

.bl-06__list {
  max-width: 72rem;
  margin-inline: auto;
  padding: 0 clamp(1.25rem,4vw,3rem);
  display: grid;
  gap: .5rem;
}

.bl-06__row {
  --progress: 0;
  position: relative;
  display: grid;
  align-items: center;
  gap: .75rem 1.25rem;
  grid-template-columns: 3.25rem 2.75rem minmax(0,1fr) minmax(6rem,12rem) 4.5rem;
  padding: clamp(.875rem,2vw,1.25rem);
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--surface);
  transition: border-color .25s ease, background .25s ease;
  overflow: hidden;
}

.bl-06__row::after {
  content: "";
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: 0;
  height: 2px;
  width: 100%;
  background: var(--acc);
  transform-origin: left;
  scale: var(--progress) 1;
  opacity: 0;
  transition: scale .3s linear;
}

.bl-06__row[data-state="playing"] {
  border-color: color-mix(in oklab,var(--acc) 45%,var(--line));
  background: color-mix(in oklab,var(--acc) 7%,var(--surface));
}

.bl-06__row[data-state="playing"]::after {
  opacity: 1;
}

.bl-06__row:hover {
  border-color: color-mix(in oklab,var(--text) 22%,var(--line));
}

.bl-06__num {
  margin: 0;
  font-family: var(--mono);
  font-size: 1.125rem;
  font-weight: 600;
  color: color-mix(in oklab,var(--text) 32%,transparent);
  font-variant-numeric: tabular-nums;
  letter-spacing: -.03em;
}

.bl-06__row[data-state="playing"] .bl-06__num {
  color: var(--acc);
}

.bl-06__play {
  display: grid;
  place-items: center;
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  cursor: pointer;
  border: 1px solid color-mix(in oklab,var(--acc) 50%,var(--line));
  background: transparent;
  color: var(--text);
  transition: background .2s ease, color .2s ease, scale .2s cubic-bezier(.16,1,.3,1);
}

.bl-06__play:hover {
  background: var(--acc);
  color: var(--acc-fg);
  scale: 1.06;
}

.bl-06__row[data-state="playing"] .bl-06__play {
  background: var(--acc);
  color: var(--acc-fg);
  border-color: var(--acc);
}

.bl-06__icon {
  width: 1.25rem;
  height: 1.25rem;
}

.bl-06__pause {
  opacity: 0;
}

.bl-06__row[data-state="playing"] .bl-06__tri {
  opacity: 0;
}

.bl-06__row[data-state="playing"] .bl-06__pause {
  opacity: 1;
}

.bl-06__body {
  display: grid;
  gap: .25rem;
  min-width: 0;
}

.bl-06__body h2 {
  margin: 0;
  font-size: 1.0625rem;
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.bl-06__body h2 a:hover {
  color: var(--acc);
}

.bl-06__desc {
  margin: 0;
  font-size: .875rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
  max-width: 58ch;
}

.bl-06__meta {
  margin: .15rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  font-family: var(--mono);
  font-size: .625rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--muted) 85%,transparent);
}

.bl-06__wave {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 2.25rem;
}

.bl-06__wave i {
  flex: 1 1 0;
  min-width: 2px;
  height: calc(var(--h) * 100%);
  border-radius: 1px;
  background: color-mix(in oklab,var(--text) 22%,transparent);
  transform-origin: bottom;
}

.bl-06__row[data-state="playing"] .bl-06__wave i {
  background: var(--acc);
  animation: bl-06-wave .9s ease-in-out infinite alternate;
  animation-delay: calc(var(--i) * -60ms);
}

@keyframes bl-06-wave {
  from {
    scale: 1 .35;
  }

  to {
    scale: 1 1;
  }
}

.bl-06__dur {
  margin: 0;
  text-align: end;
  font-family: var(--mono);
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-06__footer {
  max-width: 72rem;
  margin-inline: auto;
  padding: clamp(2rem,4vw,3rem) clamp(1.25rem,4vw,3rem) clamp(3rem,7vw,5rem);
  font-size: .875rem;
  color: var(--muted);
}

.bl-06__footer p {
  margin: 0;
}

.bl-06__footer a {
  color: var(--acc);
}

@media (max-width: 60rem) {
  .bl-06__row {
    grid-template-columns: 3.25rem 2.75rem minmax(0,1fr) 4.5rem;
  }

  .bl-06__wave {
    grid-column: 3/-1;
    height: 1.75rem;
  }
}

@media (max-width: 40rem) {
  .bl-06__head {
    grid-template-columns: minmax(0,1fr);
  }

  .bl-06__row {
    grid-template-columns: 2.75rem minmax(0,1fr) auto;
    align-items: start;
  }

  .bl-06__num {
    grid-row: 2;
    grid-column: 1;
    font-size: .8125rem;
  }

  .bl-06__play {
    grid-row: 1;
    grid-column: 1;
  }

  .bl-06__body {
    grid-row: 1;
    grid-column: 2/-1;
  }

  .bl-06__wave {
    grid-row: 2;
    grid-column: 2;
    height: 1.25rem;
  }

  .bl-06__dur {
    grid-row: 2;
    grid-column: 3;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-06 * {
    animation: none !important;
    transition: none !important;
  }

  .bl-06__row[data-state="playing"] .bl-06__wave i {
    scale: 1 1;
  }
}

@media (forced-colors: active) {
  .bl-06__row[data-state="playing"] {
    forced-color-adjust: none;
    outline: 2px solid Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.bl-06');
  if (!root) return;
  const rows = [...root.querySelectorAll('.bl-06__row')];
  rows.forEach((row) => {
    const btn = row.querySelector('[data-play]');
    const label = row.querySelector('[data-play-label]');
    const n = row.querySelector('.bl-06__num').textContent.trim();
    btn.addEventListener('click', () => {
      const playing = row.dataset.state !== 'playing';
      rows.forEach((r) => {
        r.dataset.state = 'idle';
        const b = r.querySelector('[data-play]');
        b.setAttribute('aria-pressed', 'false');
        const l = r.querySelector('[data-play-label]');
        l.textContent = 'Play episode ' + r.querySelector('.bl-06__num').textContent.trim();
      });
      row.dataset.state = playing ? 'playing' : 'idle';
      btn.setAttribute('aria-pressed', String(playing));
      label.textContent = (playing ? 'Pause episode ' : 'Play episode ') + n;
    });
  });
})();
```
