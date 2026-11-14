---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-typing-presence-pulse-avatar/"
title: "CSS Typing Presence Pulse Avatar"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "\"Alex is typing\" as an avatar state rather than a line of text: two offset pulse rings expand out of the avatar on a 2.4s loop, animating only scale and…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typing Presence Pulse Avatar
Source: https://codefronts.com/components/css-avatars/css-typing-presence-pulse-avatar/

"Alex is typing" as an avatar state rather than a line of text: two offset pulse rings expand out of the avatar on a 2.4s loop, animating only scale and opacity so the whole effect stays on the compositor. The three typing dots use the same staggered timing, presence is still announced in words for assistive tech, and everything stops completely under prefers-reduced-motion — a slower pulse is still a pulse.
## HTML
```html
<div class="av-09">
  <input class="av-09__sr" type="checkbox" id="av-09-dark">
  <label class="av-09__theme" for="av-09-dark">
    <svg class="av-09__i av-09__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-09__i av-09__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-09__vh">Dark theme</span>
  </label>

  <div class="av-09__stage">
    <section class="av-09__wrap" aria-labelledby="av-09-h">
      <header class="av-09__head">
        <p class="av-09__eyebrow">Presence · Live activity</p>
        <h2 class="av-09__h" id="av-09-h">Typing pulse</h2>
        <p class="av-09__sub">Two rings, one negative delay, zero layout work per frame.</p>
      </header>

      <div class="av-09__hero">
        <span class="av-09__fig av-09__fig--lg">
          <img class="av-09__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async">
        </span>
        <div class="av-09__heroinfo">
          <p class="av-09__name">Alex Chen</p>
          <p class="av-09__status" aria-live="polite">
            is typing
            <span class="av-09__dots" aria-hidden="true">
              <span class="av-09__dot" style="--i:0"></span>
              <span class="av-09__dot" style="--i:1"></span>
              <span class="av-09__dot" style="--i:2"></span>
            </span>
          </p>
        </div>
      </div>

      <ul class="av-09__thread">
        <li class="av-09__msg">
          <span class="av-09__fig av-09__fig--calm">
            <img class="av-09__img" src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=200&auto=format&fit=facearea&facepad=2.5" alt="Hannah Wright" width="200" height="200" loading="lazy" decoding="async">
          </span>
          <span class="av-09__body"><strong>Hannah Wright</strong> Pushed the presence service to staging — ready for review. <time datetime="2027-03-04T14:02">14:02</time></span>
        </li>
        <li class="av-09__msg">
          <span class="av-09__fig av-09__fig--calm">
            <img class="av-09__img" src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Sam Rivera" width="200" height="200" loading="lazy" decoding="async">
          </span>
          <span class="av-09__body"><strong>Sam Rivera</strong> Looking now. The websocket reconnect looks much cleaner. <time datetime="2027-03-04T14:05">14:05</time></span>
        </li>
        <li class="av-09__msg av-09__msg--typing">
          <span class="av-09__fig">
            <img class="av-09__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async">
          </span>
          <span class="av-09__body av-09__body--muted"><strong>Alex Chen</strong> is typing<span class="av-09__vh"> a message</span>
            <span class="av-09__dots" aria-hidden="true">
              <span class="av-09__dot" style="--i:0"></span>
              <span class="av-09__dot" style="--i:1"></span>
              <span class="av-09__dot" style="--i:2"></span>
            </span>
          </span>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-09 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
    --pulse: oklch(68% .17 195);
  }
}

.av-09 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --pulse: #22b8cf;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  width: 100%;
  inline-size: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.av-09 *,
.av-09 *::before,
.av-09 *::after {
  box-sizing: border-box;
}

.av-09__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.av-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-09__theme {
  position: absolute;
  inset-block-start: clamp(.85rem,2.2vw,1.5rem);
  inset-inline-end: clamp(.85rem,2.2vw,1.5rem);
  z-index: 20;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--glass);
  color: var(--ink);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.av-09__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-09__theme:hover {
  translate: 0 -1px;
}

.av-09__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-09__i--sun {
  display: none;
}

.av-09__sr:focus-visible + .av-09__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-09__wrap {
  inline-size: min(52rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-09__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-09__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-09__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-09__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-09__hero {
  display: flex;
  align-items: center;
  gap: clamp(1.5rem,5vw,3rem);
  padding: clamp(2rem,5vw,3rem) clamp(1.5rem,4vw,2.5rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-09__fig {
  --size: 2.6rem;
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  flex: none;
  isolation: isolate;
}

.av-09__fig--lg {
  --size: clamp(5rem,14vw,7rem);
}

.av-09__fig::before,
.av-09__fig::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  z-index: 0;
  box-shadow: 0 0 0 2px var(--pulse);
  animation: av-09-pulse 2.4s cubic-bezier(.2,.6,.4,1) infinite;
}

.av-09__fig::after {
  animation-delay: -1.2s;
}

.av-09__fig--calm::before,
.av-09__fig--calm::after {
  display: none;
}

.av-09__img {
  position: relative;
  z-index: 1;
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 3px var(--panel), 0 0 0 4px var(--line);
}

@keyframes av-09-pulse {
  from {
    scale: 1;
    opacity: .55;
  }

  to {
    scale: 1.7;
    opacity: 0;
  }
}

.av-09__heroinfo {
  display: flex;
  flex-direction: column;
  gap: .15rem;
  min-inline-size: 0;
}

.av-09__name {
  margin: 0;
  font-size: clamp(1.15rem,3vw,1.55rem);
  font-weight: 650;
  letter-spacing: -.025em;
}

.av-09__status {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .95rem;
  color: var(--muted);
}

.av-09__dots {
  display: inline-flex;
  align-items: center;
  gap: .22rem;
}

.av-09__dot {
  inline-size: .36rem;
  block-size: .36rem;
  border-radius: 50%;
  background: var(--pulse);
  animation: av-09-bob 1.2s ease-in-out calc(var(--i) * .14s) infinite;
}

@keyframes av-09-bob {
  0%,
    100% {
    translate: 0 0;
    opacity: .45;
  }

  50% {
    translate: 0 -.28rem;
    opacity: 1;
  }
}

.av-09__thread {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: .5rem;
}

.av-09__msg {
  display: flex;
  align-items: center;
  gap: .85rem;
  padding: .75rem .95rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-09__msg--typing {
  background: var(--panel-2);
}

.av-09__body {
  font-size: .9rem;
  line-height: 1.5;
  color: var(--muted);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .4rem;
}

.av-09__body strong {
  color: var(--ink);
  font-weight: 650;
}

.av-09__body time {
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.av-09__body--muted {
  font-style: normal;
}

.av-09:has(#av-09-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --pulse: #38bdf8;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-09:has(#av-09-dark:checked) .av-09__i--moon {
  display: none;
}

.av-09:has(#av-09-dark:checked) .av-09__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-09:not(:has(#av-09-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --pulse: #38bdf8;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-09:not(:has(#av-09-dark:checked)) .av-09__i--moon {
    display: none;
  }

  .av-09:not(:has(#av-09-dark:checked)) .av-09__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-09 *,
    .av-09 *::before,
    .av-09 *::after {
    transition: none !important;
    animation: none !important;
  }

  .av-09__fig::before {
    opacity: .32;
    scale: 1.14;
  }

  .av-09__fig::after {
    display: none;
  }

  .av-09__dot {
    opacity: .8;
  }
}

@media (forced-colors: active) {
  .av-09__fig::before,
    .av-09__fig::after {
    box-shadow: 0 0 0 2px CanvasText;
  }

  .av-09__dot {
    background: CanvasText;
  }

  .av-09__hero,
    .av-09__msg,
    .av-09__theme {
    border-color: CanvasText;
  }
}
```
