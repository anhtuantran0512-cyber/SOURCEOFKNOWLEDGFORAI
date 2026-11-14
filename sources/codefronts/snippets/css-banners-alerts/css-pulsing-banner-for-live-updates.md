---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/css-pulsing-banner-for-live-updates/"
title: "Live Event Announcement Banner"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "A live bar that behaves like a broadcast lower-third: a pulsing LIVE badge built from two rings on one element, a seamless CSS ticker that pauses on hover…"
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Event Announcement Banner
Source: https://codefronts.com/snippets/css-banners-alerts/css-pulsing-banner-for-live-updates/

A live bar that behaves like a broadcast lower-third: a pulsing LIVE badge built from two rings on one element, a seamless CSS ticker that pauses on hover and on keyboard focus, a viewer counter with tabular-nums so it never jitters, and new updates flipping into a polite live region — with a static, fully readable fallback under prefers-reduced-motion.
## HTML
```html
<div class="ba-09">
  <div class="ba-09__bar" role="region" aria-labelledby="ba-09-h">
    <div class="ba-09__top">
      <p class="ba-09__badge">
        <span class="ba-09__live" aria-hidden="true"></span>
        <span>Live</span>
      </p>
      <div class="ba-09__headline">
        <h2 class="ba-09__h" id="ba-09-h">Frontend Summit 2026 · Keynote stage</h2>
        <p class="ba-09__sub">Session 3 of 9 · <span data-elapsed>00:42:18</span> elapsed · <span data-viewers>4,182</span> watching</p>
      </div>
      <div class="ba-09__acts">
        <a class="ba-09__watch" href="#ba-09-h">
          <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M7.5 6.2 14 10l-6.5 3.8z" fill="currentColor"/></svg>
          Watch now
        </a>
        <button class="ba-09__remind" type="button" data-remind aria-pressed="false">Remind me</button>
        <button class="ba-09__x" type="button" data-close aria-label="Dismiss live banner">
          <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m6 6 8 8m0-8-8 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </button>
      </div>
    </div>

    <div class="ba-09__ticker">
      <div class="ba-09__track" data-track>
        <ul class="ba-09__set" data-set>
          <li><b>Now</b> Scroll-driven animations in production — Yuki Tanaka</li>
          <li><b>11:20</b> The CSS you no longer need JavaScript for</li>
          <li><b>11:55</b> Panel: shipping design systems without a rewrite</li>
          <li><b>12:40</b> Anchor positioning, popovers and the end of tooltip libraries</li>
          <li><b>13:15</b> Container queries at scale: 40 teams, one grid</li>
        </ul>
        <ul class="ba-09__set" aria-hidden="true">
          <li><b>Now</b> Scroll-driven animations in production — Yuki Tanaka</li>
          <li><b>11:20</b> The CSS you no longer need JavaScript for</li>
          <li><b>11:55</b> Panel: shipping design systems without a rewrite</li>
          <li><b>12:40</b> Anchor positioning, popovers and the end of tooltip libraries</li>
          <li><b>13:15</b> Container queries at scale: 40 teams, one grid</li>
        </ul>
      </div>
    </div>

    <ol class="ba-09__feed" data-feed aria-live="polite" aria-label="Live updates">
      <li><time datetime="2026-08-10T10:41">10:41</time> Q&amp;A opens in the chat — questions are up-voted, top three get answered on stage.</li>
      <li><time datetime="2026-08-10T10:33">10:33</time> Slides for session 3 are now on the resources page.</li>
    </ol>
  </div>

  <main class="ba-09__page">
    <div class="ba-09__stage" aria-hidden="true"></div>
    <div class="ba-09__meta" aria-hidden="true"><span></span><span></span><span></span></div>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter+Tight:wght@400;500;600&display=swap');

@property --ba-09-glow {
  syntax: '<length>';
  inherits: false;
  initial-value: 0px;
}

.ba-09 {
  --bg: #07080a;
  --surface: #0f1114;
  --ink: #f5f6f8;
  --muted: #8f96a1;
  --line: #1f2329;
  --live: #ff2d55;
  --acc: #00e0a4;
  --display: "Space Grotesk",ui-sans-serif,system-ui,sans-serif;
  --sans: "Inter Tight",ui-sans-serif,system-ui,-apple-system,sans-serif;
  container-type: inline-size;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto 1fr;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-09 *,
.ba-09 *::before,
.ba-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-09 {
    --bg: oklch(13% .008 265);
    --surface: oklch(18% .01 265);
    --ink: oklch(97% .004 265);
    --muted: oklch(68% .014 265);
    --line: oklch(26% .012 265);
    --live: oklch(62% .24 15);
    --acc: oklch(82% .17 165);
  }
}

@media (prefers-color-scheme: light) {
  .ba-09:not([data-theme="dark"]) {
    --bg: #f5f6f8;
    --surface: #ffffff;
    --ink: #0b0d10;
    --muted: #5c636e;
    --line: #e3e6ea;
  }
}

.ba-09[data-theme="light"] {
  --bg: #f5f6f8;
  --surface: #ffffff;
  --ink: #0b0d10;
  --muted: #5c636e;
  --line: #e3e6ea;
}

.ba-09__bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: grid;
  background: linear-gradient(180deg, color-mix(in oklab,var(--live) 12%,var(--surface)), var(--surface));
  border-block-end: 1px solid var(--line);
  box-shadow: 0 1.5rem 3rem -2rem rgb(0 0 0 / .7);
}

.ba-09__bar[hidden] {
  display: none;
}

.ba-09__top {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: clamp(.85rem,2.5cqw,2rem);
  align-items: center;
  padding: clamp(.85rem,2vw,1.15rem) clamp(1rem,4vw,2rem);
}

.ba-09__badge {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding: .4rem .7rem .4rem .55rem;
  border-radius: 999px;
  font-family: var(--display);
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #fff;
  background: var(--live);
  box-shadow: 0 0 var(--ba-09-glow,0px) color-mix(in oklab,var(--live) 70%,transparent);
  animation: ba-09-glow 2.8s ease-in-out infinite;
}

@keyframes ba-09-glow {
  0%,
    100% {
    --ba-09-glow: 6px;
  }

  50% {
    --ba-09-glow: 22px;
  }
}

.ba-09__live {
  position: relative;
  width: .5rem;
  height: .5rem;
  border-radius: 999px;
  background: #fff;
  flex: none;
}

.ba-09__live::before,
.ba-09__live::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 999px;
  border: 1.5px solid #fff;
  animation: ba-09-ping 2.4s cubic-bezier(.2,.6,.3,1) infinite;
}

.ba-09__live::after {
  animation-delay: 1.2s;
}

@keyframes ba-09-ping {
  0% {
    scale: 1;
    opacity: .85;
  }

  80%,
    100% {
    scale: 3.6;
    opacity: 0;
  }
}

.ba-09__headline {
  min-width: 0;
  display: grid;
  gap: .2rem;
}

.ba-09__h {
  margin: 0;
  font-family: var(--display);
  font-size: clamp(.9375rem,2.2cqw,1.3125rem);
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ba-09__sub {
  margin: 0;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.ba-09__acts {
  display: flex;
  align-items: center;
  gap: .45rem;
}

.ba-09__watch {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-height: 2.5rem;
  padding: .55rem 1rem;
  border-radius: .75rem;
  text-decoration: none;
  font-family: var(--display);
  font-size: .8125rem;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #0a0b0d;
  background: var(--acc);
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .2s ease;
}

.ba-09__watch svg {
  width: 1rem;
  height: 1rem;
}

.ba-09__watch:hover {
  translate: 0 -1px;
  box-shadow: 0 .7rem 1.5rem -.7rem color-mix(in oklab,var(--acc) 70%,transparent);
}

.ba-09__remind {
  min-height: 2.5rem;
  padding: .55rem .9rem;
  border-radius: .75rem;
  cursor: pointer;
  font: inherit;
  font-size: .8125rem;
  font-weight: 600;
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--line);
  transition: border-color .2s ease, background .2s ease;
}

.ba-09__remind:hover {
  border-color: var(--muted);
}

.ba-09__remind[aria-pressed="true"] {
  border-color: var(--acc);
  color: var(--acc);
}

.ba-09__x {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .7rem;
  cursor: pointer;
  border: 0;
  background: transparent;
  color: var(--muted);
}

.ba-09__x:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.ba-09__x svg {
  width: 1.125rem;
  height: 1.125rem;
}

.ba-09__ticker {
  position: relative;
  overflow: hidden;
  padding-block: .55rem;
  border-block-start: 1px solid var(--line);
  background: color-mix(in oklab,var(--bg) 55%,transparent);
  mask-image: linear-gradient(90deg,transparent,black 4rem,black calc(100% - 4rem),transparent);
}

.ba-09__track {
  display: flex;
  width: max-content;
  animation: ba-09-run 26s linear infinite;
}

@keyframes ba-09-run {
  to {
    translate: -50% 0;
  }
}

.ba-09__ticker:hover .ba-09__track,
.ba-09__ticker:focus-within .ba-09__track {
  animation-play-state: paused;
}

.ba-09__set {
  display: flex;
  align-items: center;
  gap: clamp(1.5rem,4cqw,3rem);
  margin: 0;
  padding-inline: clamp(.75rem,2cqw,1.5rem);
  list-style: none;
}

.ba-09__set li {
  display: flex;
  align-items: center;
  gap: .5rem;
  white-space: nowrap;
  font-size: .8125rem;
  color: var(--muted);
}

.ba-09__set b {
  font-family: var(--display);
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--live);
  padding: .18rem .4rem;
  border-radius: .3rem;
  background: color-mix(in oklab,var(--live) 16%,transparent);
  font-variant-numeric: tabular-nums;
}

.ba-09__feed {
  margin: 0;
  padding: .7rem clamp(1rem,4vw,2rem) .85rem;
  list-style: none;
  display: grid;
  gap: .35rem;
  border-block-start: 1px solid var(--line);
  max-block-size: 6.5rem;
  overflow: auto;
  overscroll-behavior: contain;
}

.ba-09__feed li {
  display: flex;
  gap: .55rem;
  font-size: .8125rem;
  line-height: 1.5;
  color: var(--muted);
  transition: opacity .35s ease, translate .35s cubic-bezier(.16,1,.3,1);
}

@starting-style {
  .ba-09__feed li {
    opacity: 0;
    translate: 0 -.4rem;
  }
}

.ba-09__feed time {
  flex: none;
  font-family: var(--display);
  font-size: .6875rem;
  font-weight: 700;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  padding-block-start: .1rem;
}

.ba-09__page {
  padding: clamp(1rem,4vw,2rem);
  display: grid;
  gap: 1rem;
  align-content: start;
}

.ba-09__stage {
  aspect-ratio: 16/9;
  border-radius: 1.25rem;
  overflow: hidden;
  border: 1px solid var(--line);
  background: radial-gradient(60% 70% at 50% 118%, color-mix(in oklab,var(--live) 22%,transparent), transparent 70%), radial-gradient(40% 50% at 50% -10%, color-mix(in oklab,var(--acc) 14%,transparent), transparent 70%), var(--surface);
}

.ba-09__meta {
  display: grid;
  gap: .75rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,12rem),1fr));
}

.ba-09__meta span {
  display: block;
  height: 4.5rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: var(--surface);
}

.ba-09 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-09 a {
  color: var(--acc);
}

.ba-09 a:hover {
  color: color-mix(in oklab,var(--acc) 75%,var(--ink));
}

@container (max-width: 48rem) {
  .ba-09__top {
    grid-template-columns: auto 1fr;
    row-gap: .75rem;
  }

  .ba-09__acts {
    grid-column: 1 / -1;
  }

  .ba-09__watch {
    flex: 1;
    justify-content: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-09 * {
    animation: none !important;
    transition: none !important;
  }

  .ba-09__ticker {
    mask-image: none;
    overflow: visible;
  }

  .ba-09__track {
    width: auto;
    flex-wrap: wrap;
  }

  .ba-09__track > [aria-hidden="true"] {
    display: none;
  }

  .ba-09__set {
    flex-wrap: wrap;
    row-gap: .4rem;
  }

  .ba-09__set li {
    white-space: normal;
  }
}

@media (forced-colors: active) {
  .ba-09__badge {
    background: Highlight;
    color: HighlightText;
  }

  .ba-09__bar {
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-09');
  if (!root) return;
  const feed = root.querySelector('[data-feed]');
  const viewers = root.querySelector('[data-viewers]');
  const elapsed = root.querySelector('[data-elapsed]');
  const fmt = new Intl.NumberFormat('en-GB');
  let count = 4182, t = 42 * 60 + 18;

  const UPDATES = [
    'Yuki is demoing scroll() and view() timelines — code link in the chat.',
    'Captions are live in 6 languages via the CC button.',
    'Next session moves to Stage B; the stream switches automatically.',
    'Recording will be available to ticket holders within 2 hours.',
  ];
  let n = 0;

  setInterval(() => {
    t += 1;
    const h = String(Math.floor(t / 3600)).padStart(2, '0');
    const m = String(Math.floor(t / 60) % 60).padStart(2, '0');
    elapsed.textContent = h + ':' + m + ':' + String(t % 60).padStart(2, '0');
  }, 1000);

  setInterval(() => {
    count += Math.round((Math.random() - 0.42) * 40);
    viewers.textContent = fmt.format(Math.max(1200, count));
  }, 4000);

  setInterval(() => {
    const li = document.createElement('li');
    const now = new Date();
    const time = document.createElement('time');
    time.dateTime = now.toISOString();
    time.textContent = String(now.getHours()).padStart(2, '0') + ':' + String(now.getMinutes()).padStart(2, '0');
    li.append(time, document.createTextNode(' ' + UPDATES[n % UPDATES.length]));
    feed.prepend(li);
    while (feed.children.length > 6) feed.lastElementChild.remove();
    n += 1;
  }, 9000);

  root.addEventListener('click', (e) => {
    const r = e.target.closest('[data-remind]');
    if (r) {
      const on = r.getAttribute('aria-pressed') === 'false';
      r.setAttribute('aria-pressed', String(on));
      r.textContent = on ? 'Reminder set' : 'Remind me';
    }
    if (e.target.closest('[data-close]')) root.querySelector('.ba-09__bar').hidden = true;
  });
})();
```
