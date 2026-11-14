---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/gradient-glow/"
title: "Gradient Glow Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "For the surfaces users paid for: a rotating conic-gradient glow around the loading container, driven by a real animated angle via @property."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Glow Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/gradient-glow/

For the surfaces users paid for: a rotating conic-gradient glow around the loading container, driven by a real animated angle via @property. Registering the custom property with syntax: '<angle>' is what makes it interpolate at all — without registration the browser treats it as a string and the rotation simply never happens.
## HTML
```html
<div class="sk-20">
  <div class="sk-20__stage">
    <section class="sk-20__wrap" aria-labelledby="sk-20-h">
      <header class="sk-20__head">
        <p class="sk-20__eyebrow">@property · conic-gradient</p>
        <h2 class="sk-20__h" id="sk-20-h">A glow that can only animate once you register it</h2>
        <p class="sk-20__sub">Declaring <code>syntax: '&lt;angle&gt;'</code> is what lets the browser interpolate a custom property. Without it, the keyframes snap and the border never moves.</p>
      </header>

      <article class="sk-20__card" role="status" aria-live="polite">
        <span class="sk-20__vh">Loading premium workspace…</span>
        <header class="sk-20__chead">
          <p class="sk-20__plan">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 3.2 14.6 9l6.2.6-4.7 4.2 1.4 6.1L12 16.7 6.5 19.9l1.4-6.1L3.2 9.6 9.4 9 12 3.2Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
            Pro workspace
          </p>
          <p class="sk-20__sync">syncing 4 sources</p>
        </header>
        <div class="sk-20__bars" aria-hidden="true">
          <span class="sk-20__bar sk-20__bar--title"></span>
          <span class="sk-20__bar"></span>
          <span class="sk-20__bar" style="inline-size:84%"></span>
          <span class="sk-20__bar" style="inline-size:56%"></span>
          <div class="sk-20__pair"><span class="sk-20__bar sk-20__bar--block"></span><span class="sk-20__bar sk-20__bar--block"></span></div>
        </div>
        <footer class="sk-20__cfoot">
          <span class="sk-20__bar sk-20__bar--pill" aria-hidden="true"></span>
          <span class="sk-20__bar sk-20__bar--pill" style="inline-size:5.5rem" aria-hidden="true"></span>
        </footer>
      </article>

      <aside class="sk-20__spec" aria-label="Recipe">
        <p class="sk-20__srow"><span class="sk-20__skey">register</span><span class="sk-20__sval">@property --sk20-angle { syntax: '&lt;angle&gt;'; inherits: false; initial-value: 0deg }</span></p>
        <p class="sk-20__srow"><span class="sk-20__skey">paint</span><span class="sk-20__sval">conic-gradient(from var(--sk20-angle), …) on ::before at inset: -1.5px</span></p>
        <p class="sk-20__srow"><span class="sk-20__skey">halo</span><span class="sk-20__sval">a second copy at filter: blur(14px); opacity: .55 behind it</span></p>
        <p class="sk-20__srow"><span class="sk-20__skey">speed</span><span class="sk-20__sval">4s linear infinite — ambience, not the loading signal</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --sk20-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.sk-20 {
  --bg: #05050a;
  --bg2: #0b0a16;
  --surface: rgba(255,255,255,.035);
  --line: rgba(255,255,255,.1);
  --ink: #f4f3fb;
  --muted: rgba(244,243,251,.62);
  --faint: rgba(244,243,251,.42);
  --accent: #c084fc;
  --glow: #c084fc;
  --glow2: #22d3ee;
  --sk: rgba(244,243,251,.1);
  --sheen: rgba(244,243,251,.17);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(60% 42% at 50% -8%, rgba(192,132,252,.16) 0%, transparent 62%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-20 *,
.sk-20 *::before,
.sk-20 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .sk-20 {
    --ink: oklch(0.97 0.006 300);
    --muted: oklch(0.97 0.006 300 / .62);
    --faint: oklch(0.97 0.006 300 / .42);
    --accent: oklch(0.79 0.16 305);
    --glow: oklch(0.79 0.16 305);
    --glow2: oklch(0.83 0.13 205);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-20 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 17%, transparent);
  }
}

.sk-20__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-20__wrap {
  inline-size: min(54rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-20__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 44rem;
}

.sk-20__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-20__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.4rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.07;
  text-wrap: balance;
}

.sk-20__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-20__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-20__card {
  position: relative;
  isolation: isolate;
  display: grid;
  gap: 1.1rem;
  padding: clamp(1.2rem,2.4vw,1.8rem);
  border-radius: 18px;
  background: #0a0913;
  border: 1px solid var(--line);
}

@supports (color: color-mix(in oklab, white 10%, black)) {
  .sk-20__card {
    background: color-mix(in oklab, var(--bg) 88%, var(--glow) 12%);
  }
}

.sk-20__card::before,
.sk-20__card::after {
  content: '';
  position: absolute;
  inset: -1.5px;
  border-radius: inherit;
  pointer-events: none;
  background: conic-gradient(from var(--sk20-angle),
      transparent 0turn, var(--glow) .1turn, transparent .3turn,
      transparent .6turn, var(--glow2) .72turn, transparent .9turn);
}

.sk-20__card::before {
  z-index: -1;
}

.sk-20__card::after {
  z-index: -2;
  filter: blur(14px);
  opacity: .55;
}

@supports at-rule(@property) {
  .sk-20__card::before,
    .sk-20__card::after {
    animation: sk-20-spin 4s linear infinite;
  }
}

@keyframes sk-20-spin {
  to {
    --sk20-angle: 360deg;
  }
}

.sk-20__chead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.sk-20__plan {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  padding: .35rem .75rem;
  border-radius: 999px;
  border: 1px solid rgba(192,132,252,.32);
  background: rgba(192,132,252,.12);
  font-size: .82rem;
  color: var(--accent);
}

.sk-20__plan svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.sk-20__sync {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--faint);
}

.sk-20__bars {
  display: grid;
  gap: .7rem;
}

.sk-20__pair {
  display: grid;
  gap: .7rem;
  grid-template-columns: repeat(auto-fit,minmax(9rem,1fr));
  margin-block-start: .3rem;
}

.sk-20__cfoot {
  display: flex;
  gap: .6rem;
  flex-wrap: wrap;
  padding-block-start: 1rem;
  border-block-start: 1px solid var(--line);
}

.sk-20__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-20__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-20-sheen 1.4s linear infinite;
}

@keyframes sk-20-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-20__bar--title {
  block-size: 1.4rem;
  inline-size: 64%;
  border-radius: 8px;
}

.sk-20__bar--block {
  block-size: clamp(3.5rem,8vw,5rem);
  border-radius: 10px;
}

.sk-20__bar--pill {
  inline-size: 7rem;
  block-size: 2rem;
  border-radius: 999px;
}

.sk-20__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-20__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-20__skey {
  min-inline-size: 4.6rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-20__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-20[data-theme="light"] {
  --bg: #f8f7fd;
  --bg2: #fff;
  --surface: rgba(10,8,20,.026);
  --line: rgba(10,8,20,.11);
  --ink: #0a0814;
  --muted: rgba(10,8,20,.62);
  --faint: rgba(10,8,20,.44);
  --accent: #7c3aed;
  --glow: #7c3aed;
  --glow2: #0891b2;
  background: linear-gradient(178deg,#fff 0%,#efedfa 100%);
}

.sk-20[data-theme="light"] .sk-20__card {
  background: #fff;
}

@media (prefers-color-scheme: light) {
  .sk-20:not([data-theme="dark"]) {
    --bg: #f8f7fd;
    --bg2: #fff;
    --surface: rgba(10,8,20,.026);
    --line: rgba(10,8,20,.11);
    --ink: #0a0814;
    --muted: rgba(10,8,20,.62);
    --faint: rgba(10,8,20,.44);
    --accent: #7c3aed;
    --glow: #7c3aed;
    --glow2: #0891b2;
    background: linear-gradient(178deg,#fff 0%,#efedfa 100%);
  }

  .sk-20:not([data-theme="dark"]) .sk-20__card {
    background: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-20__card::before,
    .sk-20__card::after {
    animation: none;
    --sk20-angle: 135deg;
  }

  .sk-20__bar::after {
    animation: none;
    background: none;
  }

  .sk-20__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-20__card::before,
    .sk-20__card::after {
    display: none;
  }

  .sk-20__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-20__bar::after {
    animation: none;
    background: none;
  }

  .sk-20__card,
    .sk-20__spec,
    .sk-20__plan {
    border-color: CanvasText;
  }
}
```
