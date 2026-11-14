---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/retro-cassette-player-ui-web-component/"
title: "Skeuomorphic Cassette Player"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A portable tape deck with turning reels, a mechanical counter, and transport keys that travel when pressed."
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeuomorphic Cassette Player
Source: https://codefronts.com/design-styles/css-retro-designs/retro-cassette-player-ui-web-component/

A portable tape deck with turning reels, a mechanical counter, and transport keys that travel when pressed. It is the counterpoint to the one-bit bevel: skeuomorphic depth models a light source and a material, so it needs graded shadows, inner reflections and a surface texture, where the bevel needs exactly four flat insets and nothing else.
## HTML
```html
<section class="rt-13" aria-labelledby="rt-13-title">
  <h2 class="rt-13__sr" id="rt-13-title">Skeuomorphic portable cassette deck</h2>

  <div class="rt-13__theme">
    <input class="rt-13__theme-input" type="checkbox" id="rt-13-theme">
    <label class="rt-13__theme-label" for="rt-13-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-13__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-13__stage">
    <p class="rt-13__badge">Portable stereo cassette deck &middot; type II tape</p>

    <div class="rt-13__deck">
      <div class="rt-13__lid">
        <div class="rt-13__tape">
          <div class="rt-13__label-strip">
            <span class="rt-13__side">A</span>
            <span class="rt-13__title">NIGHT DRIVE MIX</span>
            <span class="rt-13__len">C-60</span>
          </div>
          <div class="rt-13__reels">
            <span class="rt-13__reel rt-13__reel--l" aria-hidden="true"><span class="rt-13__hub"></span></span>
            <span class="rt-13__window" aria-hidden="true"></span>
            <span class="rt-13__reel rt-13__reel--r" aria-hidden="true"><span class="rt-13__hub"></span></span>
          </div>
          <div class="rt-13__shell-holes" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></div>
        </div>
      </div>

      <div class="rt-13__panel">
        <div class="rt-13__meta">
          <div class="rt-13__counter" role="img" aria-label="Tape counter reading 0 3 7">
            <span class="rt-13__digit">0</span><span class="rt-13__digit">3</span><span class="rt-13__digit">7</span>
          </div>
          <div class="rt-13__vu" aria-hidden="true">
            <span style="--rt-13-h: 40%"></span><span style="--rt-13-h: 62%"></span><span style="--rt-13-h: 88%"></span>
            <span style="--rt-13-h: 71%"></span><span style="--rt-13-h: 46%"></span><span style="--rt-13-h: 30%"></span>
          </div>
        </div>

        <div class="rt-13__transport">
          <input class="rt-13__play-cb" type="checkbox" id="rt-13-play" checked>
          <label class="rt-13__key rt-13__key--play" for="rt-13-play">
            <span class="rt-13__gl rt-13__gl--play" aria-hidden="true"></span>
            <span class="rt-13__key-t">Play / Pause</span>
          </label>
          <button class="rt-13__key" type="button"><span class="rt-13__gl rt-13__gl--rew" aria-hidden="true"></span><span class="rt-13__key-t">Rewind</span></button>
          <button class="rt-13__key" type="button"><span class="rt-13__gl rt-13__gl--ff" aria-hidden="true"></span><span class="rt-13__key-t">Forward</span></button>
          <button class="rt-13__key" type="button"><span class="rt-13__gl rt-13__gl--stop" aria-hidden="true"></span><span class="rt-13__key-t">Stop</span></button>
          <button class="rt-13__key rt-13__key--rec" type="button"><span class="rt-13__gl rt-13__gl--rec" aria-hidden="true"></span><span class="rt-13__key-t">Record</span></button>
        </div>

        <p class="rt-13__hint">Depth here is graded and blurred because it models a light source and a material. The bevelled chrome elsewhere in this collection is four flat insets and nothing else.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-13 {
  --rt-13-case: #cfc9bd;
  --rt-13-case-d: #a49c8e;
  --rt-13-case-k: #4a463f;
  --rt-13-ink: #211f1b;
  --rt-13-red: #c0392b;
  --rt-13-cond: ui-sans-serif, "Helvetica Neue", "Arial Narrow", Helvetica, Arial, sans-serif;
  --rt-13-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --rt-13-bg: #e6e1d7;
  --rt-13-bg: oklch(91% 0.013 88);
  --rt-13-surface: #f7f4ee;
  --rt-13-surface: oklch(97% 0.008 88);
  --rt-13-ink-2: #58524a;
  --rt-13-ink-2: oklch(45% 0.014 80);
  --rt-13-line: #b2aa9c;
  --rt-13-line: oklch(74% 0.017 88);
  --rt-13-acc: #9c3a10;
  --rt-13-acc: oklch(45% 0.15 45);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-13-bg);
  color: var(--rt-13-ink);
  font-family: var(--rt-13-cond);
  -webkit-text-size-adjust: 100%;
}

.rt-13 *,
.rt-13 *::before,
.rt-13 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-13 {
    --rt-13-bg: #18160f;
    --rt-13-bg: oklch(20% 0.012 88);
    --rt-13-surface: #232019;
    --rt-13-surface: oklch(26% 0.014 88);
    --rt-13-ink-2: #b0a897;
    --rt-13-ink-2: oklch(75% 0.016 88);
    --rt-13-line: #46413a;
    --rt-13-line: oklch(38% 0.015 88);
    --rt-13-acc: #ff9469;
    --rt-13-acc: oklch(78% 0.13 45);
  }
}

.rt-13[data-theme="dark"],
.rt-13:has(.rt-13__theme-input:checked) {
  --rt-13-bg: #18160f;
  --rt-13-bg: oklch(20% 0.012 88);
  --rt-13-surface: #232019;
  --rt-13-surface: oklch(26% 0.014 88);
  --rt-13-ink-2: #b0a897;
  --rt-13-ink-2: oklch(75% 0.016 88);
  --rt-13-line: #46413a;
  --rt-13-line: oklch(38% 0.015 88);
  --rt-13-acc: #ff9469;
  --rt-13-acc: oklch(78% 0.13 45);
}

@media (prefers-color-scheme: light) {
  .rt-13:has(.rt-13__theme-input:checked) {
    --rt-13-bg: #18160f;
    --rt-13-bg: oklch(20% 0.012 88);
    --rt-13-surface: #232019;
    --rt-13-surface: oklch(26% 0.014 88);
    --rt-13-ink-2: #b0a897;
    --rt-13-ink-2: oklch(75% 0.016 88);
    --rt-13-line: #46413a;
    --rt-13-line: oklch(38% 0.015 88);
    --rt-13-acc: #ff9469;
    --rt-13-acc: oklch(78% 0.13 45);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-13:has(.rt-13__theme-input:checked) {
    --rt-13-bg: #e6e1d7;
    --rt-13-bg: oklch(91% 0.013 88);
    --rt-13-surface: #f7f4ee;
    --rt-13-surface: oklch(97% 0.008 88);
    --rt-13-ink-2: #58524a;
    --rt-13-ink-2: oklch(45% 0.014 80);
    --rt-13-line: #b2aa9c;
    --rt-13-line: oklch(74% 0.017 88);
    --rt-13-acc: #9c3a10;
    --rt-13-acc: oklch(45% 0.15 45);
  }
}

.rt-13__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-13__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-13__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-13__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  border-radius: 10px;
  background: var(--rt-13-surface);
  color: var(--rt-13-ink-2);
  box-shadow: 0 1px 0 rgba(255,255,255,0.8) inset, 0 -1px 0 rgba(0,0,0,0.12) inset, 0 2px 5px rgba(0,0,0,0.2);
}

.rt-13__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-13__theme-input:focus-visible + .rt-13__theme-label {
  outline: 2px solid var(--rt-13-acc);
  outline-offset: 3px;
}

.rt-13__stage {
  max-inline-size: 58rem;
  margin-inline: auto;
  padding: clamp(3.75rem, 3rem + 3vw, 5rem) clamp(0.85rem, 0.5rem + 2vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

.rt-13__badge {
  margin: 0;
  justify-self: start;
  min-inline-size: 0;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--rt-13-ink-2);
  border: 1px solid var(--rt-13-line);
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
}

.rt-13__deck {
  min-inline-size: 0;
  border-radius: 18px;
  padding: clamp(0.9rem, 0.6rem + 1.5vw, 1.6rem);
  background: repeating-linear-gradient(135deg, rgba(255,255,255,0.05) 0 1px, rgba(0,0,0,0.045) 1px 3px), linear-gradient(180deg, #ddd7cb 0%, var(--rt-13-case) 42%, var(--rt-13-case-d) 100%);
  box-shadow: inset 0 2px 1px rgba(255,255,255,0.85), inset 0 -3px 2px rgba(0,0,0,0.22), 0 1px 2px rgba(0,0,0,0.3), 0 26px 48px -26px rgba(0,0,0,0.6);
  display: grid;
  gap: clamp(0.9rem, 0.6rem + 1.4vw, 1.4rem);
}

.rt-13__lid {
  min-inline-size: 0;
  border-radius: 12px;
  padding: clamp(0.6rem, 0.4rem + 1vw, 1rem);
  background: linear-gradient(180deg, rgba(0,0,0,0.28), rgba(0,0,0,0.14));
  box-shadow: inset 0 3px 8px rgba(0,0,0,0.45), inset 0 -1px 0 rgba(255,255,255,0.35);
}

.rt-13__tape {
  min-inline-size: 0;
  border-radius: 6px;
  padding: clamp(0.6rem, 0.4rem + 1vw, 0.9rem);
  background: linear-gradient(180deg, #2f3238 0%, #1d2024 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.18), 0 2px 6px rgba(0,0,0,0.5);
  display: grid;
  gap: 0.7rem;
}

.rt-13__label-strip {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-inline-size: 0;
  background: linear-gradient(180deg, #f4efe2, #ded7c6);
  border-radius: 3px;
  padding: 0.45rem 0.6rem;
  box-shadow: inset 0 -1px 0 rgba(0,0,0,0.16);
}

.rt-13__side {
  inline-size: 22px;
  block-size: 22px;
  flex: none;
  display: grid;
  place-items: center;
  background: var(--rt-13-red);
  color: #fff;
  border-radius: 3px;
  font-size: 0.72rem;
  font-weight: 800;
}

.rt-13__title {
  flex: 1 1 auto;
  min-inline-size: 0;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #2a2620;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.rt-13__len {
  font-family: var(--rt-13-mono);
  font-size: 0.68rem;
  color: #5d564a;
  flex: none;
}

.rt-13__reels {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(0.5rem, 0.3rem + 2vw, 1.6rem);
  min-inline-size: 0;
}

.rt-13__reel {
  inline-size: clamp(58px, 14vw, 86px);
  aspect-ratio: 1 / 1;
  flex: none;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: repeating-conic-gradient(from 0deg, rgba(255,255,255,0.06) 0deg 6deg, rgba(0,0,0,0.3) 6deg 12deg), radial-gradient(circle, #3b3f45 0 34%, #17191c 34% 100%);
  box-shadow: inset 0 0 0 2px rgba(255,255,255,0.1), inset 0 3px 7px rgba(0,0,0,0.7);
  animation: rt-13-spin 3.4s linear infinite;
  animation-play-state: paused;
}

.rt-13__reel--r {
  inline-size: clamp(46px, 11vw, 68px);
  animation-duration: 2.1s;
}

.rt-13:has(.rt-13__play-cb:checked) .rt-13__reel {
  animation-play-state: running;
}

@keyframes rt-13-spin {
  to {
    transform: rotate(360deg);
  }
}

.rt-13__hub {
  inline-size: 34%;
  block-size: 34%;
  border-radius: 50%;
  background: #d8d3c8;
  box-shadow: inset 0 -2px 3px rgba(0,0,0,0.35), 0 0 0 3px rgba(0,0,0,0.5);
}

.rt-13__window {
  flex: 1 1 auto;
  min-inline-size: 0;
  max-inline-size: 6rem;
  block-size: 34px;
  border-radius: 4px;
  background: linear-gradient(180deg, rgba(190,200,210,0.32), rgba(120,132,145,0.2));
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.4), inset 0 -1px 3px rgba(0,0,0,0.5);
}

.rt-13__shell-holes {
  display: flex;
  justify-content: space-between;
  padding-inline: 0.6rem;
}

.rt-13__shell-holes span {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: #0e1012;
  box-shadow: inset 0 1px 1px rgba(0,0,0,0.9), 0 1px 0 rgba(255,255,255,0.14);
}

.rt-13__panel {
  display: grid;
  gap: clamp(0.8rem, 0.6rem + 1vw, 1.2rem);
  min-inline-size: 0;
}

.rt-13__meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 0.9rem;
  min-inline-size: 0;
}

.rt-13__counter {
  display: flex;
  gap: 3px;
  padding: 4px;
  border-radius: 4px;
  background: #2b2822;
  box-shadow: inset 0 2px 5px rgba(0,0,0,0.7), 0 1px 0 rgba(255,255,255,0.5);
}

.rt-13__digit {
  inline-size: 26px;
  block-size: 34px;
  display: grid;
  place-items: center;
  border-radius: 2px;
  background: linear-gradient(180deg, #f2ede1 0 48%, #d9d2c2 48% 100%);
  color: #201d18;
  font-family: var(--rt-13-mono);
  font-size: 1.15rem;
  font-variant-numeric: tabular-nums;
  box-shadow: inset 0 -1px 2px rgba(0,0,0,0.35);
}

.rt-13__vu {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  block-size: 38px;
  padding: 4px 6px;
  border-radius: 4px;
  background: #2b2822;
  box-shadow: inset 0 2px 5px rgba(0,0,0,0.7);
}

.rt-13__vu span {
  inline-size: 7px;
  block-size: var(--rt-13-h);
  background: linear-gradient(180deg, #ffd166, #e2703a);
  border-radius: 1px;
}

.rt-13__transport {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  min-inline-size: 0;
}

.rt-13__play-cb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
}

.rt-13__key {
  min-block-size: 48px;
  min-inline-size: 48px;
  flex: 1 1 6.5rem;
  cursor: pointer;
  border: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.45rem;
  padding: 0.6rem 0.7rem;
  border-radius: 5px;
  font: inherit;
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  color: #2c2822;
  background: linear-gradient(180deg, #efeade 0%, #cfc8ba 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), inset 0 -2px 0 rgba(0,0,0,0.16), 0 3px 0 var(--rt-13-case-k), 0 5px 8px rgba(0,0,0,0.32);
  transition: transform 70ms ease-out, box-shadow 70ms ease-out;
}

.rt-13__key:active,
.rt-13__play-cb:checked + .rt-13__key {
  transform: translateY(3px);
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.32), inset 0 -1px 0 rgba(255,255,255,0.5), 0 0 0 rgba(0,0,0,0);
}

.rt-13__key:focus-visible,
.rt-13__play-cb:focus-visible + .rt-13__key {
  outline: 2px solid var(--rt-13-acc);
  outline-offset: 3px;
}

.rt-13__key-t {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.rt-13__gl {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  background: #2c2822;
}

.rt-13__gl--play {
  clip-path: polygon(0 0, 100% 50%, 0 100%);
}

.rt-13__gl--stop {
  clip-path: inset(0);
}

.rt-13__gl--rew {
  clip-path: polygon(50% 0, 50% 100%, 0 50%, 50% 0, 100% 0, 100% 100%, 50% 100%, 50% 50%);
}

.rt-13__gl--ff {
  clip-path: polygon(0 0, 50% 50%, 0 100%, 0 0, 50% 0, 100% 50%, 50% 100%, 50% 0);
}

.rt-13__gl--rec {
  border-radius: 50%;
  background: var(--rt-13-red);
}

.rt-13__key--rec {
  color: #6d2117;
}

.rt-13__hint {
  margin: 0;
  font-size: 0.82rem;
  line-height: 1.55;
  color: #4a453d;
  min-inline-size: 0;
  text-wrap: pretty;
  max-inline-size: 60ch;
}

@media (prefers-reduced-motion: reduce) {
  .rt-13__reel {
    animation: none;
  }

  .rt-13__key {
    transition: none;
  }
}
```
