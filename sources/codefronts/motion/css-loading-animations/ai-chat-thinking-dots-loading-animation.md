---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/ai-chat-thinking-dots-loading-animation/"
title: "AI Chat Thinking Dots Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "The most-copied loader of the AI era, done properly."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: AI Chat Thinking Dots Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/ai-chat-thinking-dots-loading-animation/

The most-copied loader of the AI era, done properly. Three dots bounce inside a real assistant bubble using a linear() easing curve — a genuine spring, not a lopsided ease-in-out — while the status line cycles through the phases an agent actually goes through (reading files, searching, drafting). A gradient shimmer sweeps the label text, and the done state swaps the dots for a streamed-answer skeleton.
## HTML
```html
<div class="la-05" data-state="loading">
  <div class="la-05__chrome">
    <button class="la-05__btn la-05__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-05__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-05__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-05__btn la-05__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <div class="la-05__thread">
    <div class="la-05__msg la-05__msg--user">
      <p>Summarise the Q3 revenue deck and flag anything that contradicts the board memo.</p>
    </div>

    <div class="la-05__row">
      <span class="la-05__avatar" aria-hidden="true">
        <svg viewBox="0 0 24 24" focusable="false"><path d="M12 4.5 13.8 9l4.7 1.7-4.7 1.7L12 17l-1.8-4.6L5.5 10.7 10.2 9z"/></svg>
      </span>
      <div class="la-05__bubble" role="status" aria-live="polite" aria-label="Assistant is generating a response">
        <span class="la-05__tail" aria-hidden="true"></span>
        <span class="la-05__dots" aria-hidden="true"><i class="la-05__dot"></i><i class="la-05__dot"></i><i class="la-05__dot"></i></span>
        <p class="la-05__phase" id="la-05-phase">AI is thinking…</p>
        <div class="la-05__answer" aria-hidden="true"><i></i><i></i><i></i></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.la-05 {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --bubble: #ffffff;
  --ink: #0c1017;
  --muted: #7b8494;
  --line: #e5e8f0;
  --acc: #6d4aff;
  --user: #101623;
  --ring: #6d4aff;
  --radius: 1.15rem;
  --shadow: rgba(12,16,23,.14);
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(90% 60% at 50% 0%, color-mix(in oklab,var(--acc) 15%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-05,
.la-05 *,
.la-05 *::before,
.la-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-05 {
    --acc: oklch(58% .23 288);
  }
}

.la-05__thread {
  inline-size: min(27rem,100%);
  display: grid;
  gap: .85rem;
}

.la-05__msg {
  justify-self: end;
  max-inline-size: 80%;
  padding: .8rem 1rem;
  border-radius: var(--radius) var(--radius) .35rem var(--radius);
  background: var(--user);
  color: #fff;
}

.la-05__msg p {
  margin: 0;
  font-size: .92rem;
  line-height: 1.45;
  text-wrap: pretty;
}

.la-05__row {
  display: flex;
  gap: .65rem;
  align-items: flex-end;
}

.la-05__avatar {
  flex: none;
  inline-size: 2rem;
  block-size: 2rem;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: linear-gradient(140deg, color-mix(in oklab,var(--acc) 85%,white), var(--acc));
  color: #fff;
  box-shadow: 0 8px 16px -10px var(--acc);
}

.la-05__avatar svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  fill: currentColor;
}

.la-05__bubble {
  position: relative;
  padding: .9rem 1.1rem;
  border-radius: var(--radius) var(--radius) var(--radius) .35rem;
  background: var(--bubble);
  border: 1px solid var(--line);
  display: grid;
  gap: .55rem;
  justify-items: start;
  box-shadow: 0 20px 40px -28px var(--shadow);
  inline-size: max-content;
  min-inline-size: 11.5rem;
  max-inline-size: min(100%,18rem);
}

.la-05__bubble::after {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  pointer-events: none;
  background: linear-gradient(115deg, transparent 35%, color-mix(in oklab,var(--acc) 22%,transparent) 50%, transparent 65%) 0 0/250% 100%;
  animation: la-05-sheen 3.4s linear infinite;
  opacity: .7;
}

@keyframes la-05-sheen {
  to {
    background-position: -250% 0;
  }
}

.la-05__tail {
  position: absolute;
  inset-block-end: -1px;
  inset-inline-start: -.3rem;
  inline-size: .7rem;
  block-size: .7rem;
  background: var(--bubble);
  border-inline-start: 1px solid var(--line);
  border-block-end: 1px solid var(--line);
  border-end-start-radius: .2rem;
  rotate: 45deg;
}

.la-05__dots {
  display: flex;
  gap: .34rem;
  padding-block: .15rem;
}

.la-05__dot {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 999px;
  background: var(--acc);
  opacity: .55;
  animation: la-05-bounce 1.25s cubic-bezier(.3,0,.2,1) infinite;
}

.la-05__dot:nth-child(2) {
  animation-delay: .16s;
}

.la-05__dot:nth-child(3) {
  animation-delay: .32s;
}

@keyframes la-05-bounce {
  0%,
    60%,
    100% {
    translate: 0 0;
    opacity: .5;
  }

  30% {
    translate: 0 -.5rem;
    opacity: 1;
  }
}

@supports (animation-timing-function: linear(0,1)) {
  .la-05__dot {
    animation-timing-function: linear(0, .18 12%, .62 26%, 1 42%, .82 58%, 1 74%, .95 88%, 1);
  }
}

.la-05__phase {
  margin: 0;
  font-size: .86rem;
  font-weight: 500;
  letter-spacing: -.01em;
  background: linear-gradient(90deg, var(--muted) 28%, var(--ink) 48%, var(--muted) 68%) 0 0/220% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: la-05-shimmer 2.8s linear infinite;
}

@keyframes la-05-shimmer {
  to {
    background-position: -220% 0;
  }
}

@supports (transition-behavior: allow-discrete) {
  @starting-style {
    .la-05__phase {
      opacity: 0;
    }
  }

  .la-05__phase {
    transition: opacity .3s ease;
  }
}

.la-05__answer {
  display: none;
  gap: .4rem;
  inline-size: 13rem;
}

.la-05__answer i {
  display: block;
  block-size: .5rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 12%,transparent);
}

.la-05__answer i:nth-child(2) {
  inline-size: 88%;
}

.la-05__answer i:nth-child(3) {
  inline-size: 62%;
}

.la-05.is-ready .la-05__dots {
  display: none;
}

.la-05.is-ready .la-05__bubble::after {
  animation: none;
  opacity: 0;
}

.la-05.is-ready .la-05__phase {
  animation: none;
  background: none;
  color: var(--ink);
  -webkit-text-fill-color: currentColor;
}

.la-05.is-ready .la-05__answer {
  display: grid;
}

.la-05:has(.la-05__answer:not([hidden])) .la-05__bubble {
  min-inline-size: 14rem;
}

.la-05__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-05__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--ink) 16%,transparent);
  color: var(--ink);
  background: color-mix(in oklab,var(--surface) 72%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.la-05__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-05__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-05__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-05__sun {
  display: none;
}

.la-05__theme[aria-pressed="true"] .la-05__sun {
  display: block;
}

.la-05__theme[aria-pressed="true"] .la-05__moon {
  display: none;
}

.la-05__done[aria-pressed="true"] {
  background: var(--acc);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-05:not([data-theme="light"]) {
    --bg: #080a10;
    --surface: #12151e;
    --bubble: #151a25;
    --ink: #eef1f8;
    --muted: #8d97a8;
    --line: #242c3a;
    --acc: #9d86ff;
    --user: #232c3d;
    --ring: #9d86ff;
    --shadow: rgba(0,0,0,.7);
  }
}

.la-05[data-theme="dark"] {
  --bg: #080a10;
  --surface: #12151e;
  --bubble: #151a25;
  --ink: #eef1f8;
  --muted: #8d97a8;
  --line: #242c3a;
  --acc: #9d86ff;
  --user: #232c3d;
  --ring: #9d86ff;
  --shadow: rgba(0,0,0,.7);
}

@media (prefers-reduced-motion: reduce) {
  .la-05 * {
    animation: none !important;
    transition: none !important;
  }

  .la-05__dot {
    opacity: 1;
  }

  .la-05__dot:nth-child(2) {
    opacity: .6;
  }

  .la-05__dot:nth-child(3) {
    opacity: .35;
  }

  .la-05__phase {
    background: none;
    color: var(--ink);
    -webkit-text-fill-color: currentColor;
  }
}

@media (forced-colors: active) {
  .la-05__bubble,
    .la-05__msg {
    border: 1px solid CanvasText;
  }

  .la-05__dot {
    background: Highlight;
  }

  .la-05__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-05');
  if (!root) return;
  const theme = root.querySelector('.la-05__theme');
  const done = root.querySelector('.la-05__done');
  const phase = root.querySelector('#la-05-phase');
  const PHASES = ['AI is thinking…', 'Reading Q3-revenue.pdf', 'Cross-checking board memo', 'Drafting the summary'];
  let i = 0;
  const timer = setInterval(() => { if (!root.classList.contains('is-ready')) phase.textContent = PHASES[++i % PHASES.length]; }, 1900);
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    theme.setAttribute('aria-pressed', String(dark()));
    theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    phase.textContent = ready ? 'Answer ready — 3 sources checked' : PHASES[0];
    if (ready) clearInterval(timer);
  });
  sync();
})();
```
