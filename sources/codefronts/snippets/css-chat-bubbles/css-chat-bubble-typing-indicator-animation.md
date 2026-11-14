---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/css-chat-bubble-typing-indicator-animation/"
title: "CSS Chat Bubble Typing Indicator Animation"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "Four production typing indicators in one switchable demo — bounce dots, a travelling wave, a soundwave meter and a shimmer skeleton — all pure CSS, all built…"
has_js: "false"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Chat Bubble Typing Indicator Animation
Source: https://codefronts.com/snippets/css-chat-bubbles/css-chat-bubble-typing-indicator-animation/

Four production typing indicators in one switchable demo — bounce dots, a travelling wave, a soundwave meter and a shimmer skeleton — all pure CSS, all built from the same three-span markup, all staggered by a single inline --i custom property instead of four hand-written delay rules. Each one respects prefers-reduced-motion by falling back to a non-animated resting state that still reads as "waiting".
## HTML
```html
<div class="cb-05">
  <input class="cb-05__sr" type="checkbox" id="cb-05-dark">
  <label class="cb-05__theme" for="cb-05-dark">
    <svg class="cb-05__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-05__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="cb-05__sr-text">Dark theme</span>
  </label>

  <input class="cb-05__sr" type="radio" name="cb-05-kind" id="cb-05-bounce" checked>
  <input class="cb-05__sr" type="radio" name="cb-05-kind" id="cb-05-wave">
  <input class="cb-05__sr" type="radio" name="cb-05-kind" id="cb-05-meter">
  <input class="cb-05__sr" type="radio" name="cb-05-kind" id="cb-05-skeleton">

  <div class="cb-05__stage">
    <ol class="cb-05__thread" aria-label="Conversation">
      <li class="cb-05__turn cb-05__turn--out"><p class="cb-05__msg">Did the migration finish?</p></li>
      <li class="cb-05__turn cb-05__turn--in">
        <img class="cb-05__avatar" src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=facearea&facepad=2.8&w=120&h=120&q=70" width="36" height="36" alt="Maya Okonkwo" loading="lazy" decoding="async">
        <div class="cb-05__typing" aria-hidden="true">
          <span class="cb-05__dot" style="--i:0"></span>
          <span class="cb-05__dot" style="--i:1"></span>
          <span class="cb-05__dot" style="--i:2"></span>
          <span class="cb-05__bar" style="--i:0"></span>
          <span class="cb-05__bar" style="--i:1"></span>
          <span class="cb-05__bar" style="--i:2"></span>
          <span class="cb-05__bar" style="--i:3"></span>
          <span class="cb-05__bar" style="--i:4"></span>
          <span class="cb-05__line" style="--i:0"></span>
          <span class="cb-05__line" style="--i:1"></span>
        </div>
      </li>
    </ol>
    <p class="cb-05__live" role="status" aria-live="polite">Maya is typing</p>

    <div class="cb-05__switch" role="radiogroup" aria-label="Indicator style">
      <label class="cb-05__chip" for="cb-05-bounce">Bounce</label>
      <label class="cb-05__chip" for="cb-05-wave">Wave</label>
      <label class="cb-05__chip" for="cb-05-meter">Meter</label>
      <label class="cb-05__chip" for="cb-05-skeleton">Skeleton</label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

@property --cb-05-sweep {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.cb-05 {
  --bg: #0e1014;
  --surface: #171a21;
  --ink: #f0f2f7;
  --muted: #8f99a9;
  --line: #242833;
  --in: #1d212b;
  --out: #5b4bff;
  --out-ink: #ffffff;
  --dot: #8f7bff;
  --hi: #3a3f52;
  --ring: #8f7bff;
  --shadow: rgba(0,0,0,.6);
  --size: .5rem;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(90% 60% at 50% 0%, color-mix(in oklab,var(--out) 22%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-05,
.cb-05 *,
.cb-05 *::before,
.cb-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-05 {
    --bg: oklch(16% .015 275);
    --surface: oklch(22% .018 275);
    --ink: oklch(96% .006 275);
    --muted: oklch(70% .02 275);
    --line: oklch(29% .02 275);
    --in: oklch(25% .02 275);
    --out: oklch(56% .22 285);
    --dot: oklch(74% .15 288);
    --hi: oklch(38% .03 275);
  }
}

.cb-05__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  opacity: 0;
}

.cb-05__sr-text {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-05__live {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-05__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-05__theme:hover {
  transform: translateY(-2px);
}

.cb-05__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-05__moon {
  display: none;
}

.cb-05__sun {
  display: block;
}

.cb-05__sr:focus-visible + .cb-05__theme {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.cb-05__stage {
  inline-size: min(100%,34rem);
  display: grid;
  gap: clamp(1.25rem,4vw,2rem);
}

.cb-05__thread {
  list-style: none;
  margin: 0;
  padding: clamp(1rem,3vw,1.6rem);
  display: grid;
  gap: .75rem;
  border-radius: 1.75rem;
  background: color-mix(in oklab,var(--surface) 70%,transparent);
  border: 1px solid var(--line);
  backdrop-filter: blur(16px);
  box-shadow: 0 30px 70px -50px var(--shadow);
}

.cb-05__turn {
  display: flex;
  align-items: flex-end;
  gap: .55rem;
}

.cb-05__turn--out {
  justify-content: flex-end;
}

.cb-05__msg {
  margin: 0;
  padding: .7rem 1.05rem;
  border-radius: 1.3rem .4rem 1.3rem 1.3rem;
  background: var(--out);
  color: var(--out-ink);
  font-size: 1rem;
  line-height: 1.45;
  letter-spacing: -.01em;
}

.cb-05__avatar {
  inline-size: 36px;
  block-size: 36px;
  border-radius: 50%;
  object-fit: cover;
  background: var(--in);
}
/* ── the indicator bubble ── */

.cb-05__typing {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: .32rem;
  min-block-size: 2.75rem;
  padding: .8rem 1.05rem;
  border-radius: 1.3rem 1.3rem 1.3rem .4rem;
  background: var(--in);
}

.cb-05__typing::after {
  content: '';
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: -8px;
  border-block: 9px solid transparent;
  border-inline-end: 10px solid var(--in);
}

.cb-05__dot,
.cb-05__bar,
.cb-05__line {
  background: var(--dot);
  display: none;
}

.cb-05__dot {
  inline-size: var(--size);
  block-size: var(--size);
  border-radius: 50%;
  display: block;
}
/* ═══ 1 · BOUNCE (default) ═══ */

.cb-05__dot {
  animation: cb-05-bounce 1.25s ease-in-out infinite;
  animation-delay: calc(var(--i) * 140ms);
}

@keyframes cb-05-bounce {
  0%,
    80%,
    100% {
    translate: 0 0;
    opacity: .42;
    scale: .85;
  }

  35% {
    translate: 0 -60%;
    opacity: 1;
    scale: 1;
  }
}
/* ═══ 2 · WAVE ═══ */

.cb-05:has(#cb-05-wave:checked) .cb-05__dot {
  animation: cb-05-wave 1.05s cubic-bezier(.4,0,.2,1) infinite;
  animation-delay: calc(var(--i) * 110ms);
  opacity: 1;
}

@keyframes cb-05-wave {
  0%,
    55%,
    100% {
    translate: 0 0;
  }

  28% {
    translate: 0 -80%;
  }
}
/* ═══ 3 · METER ═══ */

.cb-05:has(#cb-05-meter:checked) .cb-05__dot {
  display: none;
}

.cb-05:has(#cb-05-meter:checked) .cb-05__bar {
  display: block;
  inline-size: .28rem;
  block-size: 1.15rem;
  border-radius: 999px;
  transform-origin: 50% 100%;
  animation: cb-05-meter .95s steps(6,jump-none) infinite alternate;
  animation-delay: calc(var(--i) * -170ms);
}

@keyframes cb-05-meter {
  from {
    scale: 1 .3;
    opacity: .5;
  }

  to {
    scale: 1 1;
    opacity: 1;
  }
}
/* ═══ 4 · SKELETON ═══ */

.cb-05:has(#cb-05-skeleton:checked) .cb-05__typing {
  display: grid;
  gap: .45rem;
  inline-size: min(16rem,60vw);
  align-content: center;
}

.cb-05:has(#cb-05-skeleton:checked) .cb-05__dot {
  display: none;
}

.cb-05:has(#cb-05-skeleton:checked) .cb-05__line {
  display: block;
  block-size: .6rem;
  border-radius: 999px;
  background: linear-gradient(90deg,var(--line) 0 35%,var(--hi) 50%,var(--line) 65% 100%);
  background-size: 250% 100%;
  background-position: 0 0;
  animation: cb-05-sweep 1.5s linear infinite;
  animation-delay: calc(var(--i) * 180ms);
}

.cb-05:has(#cb-05-skeleton:checked) .cb-05__line:nth-of-type(2) {
  inline-size: 64%;
}

@supports (background-position: var(--cb-05-sweep) 0) {
  .cb-05:has(#cb-05-skeleton:checked) .cb-05__line {
    background-position: var(--cb-05-sweep) 0;
  }
}

@keyframes cb-05-sweep {
  from {
    --cb-05-sweep: 120%;
    background-position: 120% 0;
  }

  to {
    --cb-05-sweep: -20%;
    background-position: -20% 0;
  }
}
/* ── switch ── */

.cb-05__switch {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  justify-content: center;
  padding: .4rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: color-mix(in oklab,var(--surface) 60%,transparent);
}

.cb-05__chip {
  min-block-size: 44px;
  display: grid;
  place-items: center;
  padding: .5rem 1.05rem;
  cursor: pointer;
  border-radius: .75rem;
  color: var(--muted);
  font-size: .86rem;
  font-weight: 600;
  letter-spacing: -.01em;
  transition: background .22s, color .22s, transform .22s cubic-bezier(.16,1,.3,1);
}

.cb-05__chip:hover {
  color: var(--ink);
  transform: translateY(-1px);
}

#cb-05-bounce:checked ~ .cb-05__stage .cb-05__chip[for="cb-05-bounce"],
#cb-05-wave:checked ~ .cb-05__stage .cb-05__chip[for="cb-05-wave"],
#cb-05-meter:checked ~ .cb-05__stage .cb-05__chip[for="cb-05-meter"],
#cb-05-skeleton:checked ~ .cb-05__stage .cb-05__chip[for="cb-05-skeleton"] {
  background: var(--out);
  color: var(--out-ink);
}

#cb-05-bounce:focus-visible ~ .cb-05__stage .cb-05__chip[for="cb-05-bounce"],
#cb-05-wave:focus-visible ~ .cb-05__stage .cb-05__chip[for="cb-05-wave"],
#cb-05-meter:focus-visible ~ .cb-05__stage .cb-05__chip[for="cb-05-meter"],
#cb-05-skeleton:focus-visible ~ .cb-05__stage .cb-05__chip[for="cb-05-skeleton"] {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
/* ── light ── */

.cb-05:has(#cb-05-dark:checked) {
  --bg: #f2f3f7;
  --surface: #ffffff;
  --ink: #0d1016;
  --muted: #5d6675;
  --line: #e3e6ee;
  --in: #eceef4;
  --dot: #5b4bff;
  --hi: #ffffff;
  --shadow: rgba(13,16,22,.18);
}

.cb-05:has(#cb-05-dark:checked) .cb-05__moon {
  display: block;
}

.cb-05:has(#cb-05-dark:checked) .cb-05__sun {
  display: none;
}

@media (prefers-color-scheme: light) {
  .cb-05:not(:has(#cb-05-dark:checked)) {
    --bg: #f2f3f7;
    --surface: #ffffff;
    --ink: #0d1016;
    --muted: #5d6675;
    --line: #e3e6ee;
    --in: #eceef4;
    --dot: #5b4bff;
    --hi: #ffffff;
    --shadow: rgba(13,16,22,.18);
  }

  .cb-05:not(:has(#cb-05-dark:checked)) .cb-05__moon {
    display: block;
  }

  .cb-05:not(:has(#cb-05-dark:checked)) .cb-05__sun {
    display: none;
  }
}
/* ── reduced motion: keep a readable resting state, not blank dots ── */

@media (prefers-reduced-motion: reduce) {
  .cb-05 *,
    .cb-05 *::before,
    .cb-05 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cb-05__dot {
    opacity: 1;
    scale: 1;
    translate: none;
  }

  .cb-05__dot[style*="--i:1"] {
    opacity: .66;
  }

  .cb-05__dot[style*="--i:2"] {
    opacity: .38;
  }

  .cb-05__bar {
    scale: 1 .6;
  }

  .cb-05__bar[style*="--i:1"] {
    scale: 1 1;
  }

  .cb-05__bar[style*="--i:3"] {
    scale: 1 .85;
  }

  .cb-05__line {
    background: var(--line);
  }
}

@media (forced-colors: active) {
  .cb-05__typing {
    border: 1px solid CanvasText;
  }

  .cb-05__dot,
    .cb-05__bar,
    .cb-05__line {
    background: CanvasText;
    forced-color-adjust: none;
  }
}
```
