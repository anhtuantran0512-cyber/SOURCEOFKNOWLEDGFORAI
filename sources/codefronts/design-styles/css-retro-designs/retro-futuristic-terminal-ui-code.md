---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/retro-futuristic-terminal-ui-code/"
title: "Retro Futuristic Terminal Interface"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A command console that boots: staggered POST lines, a typed command, and a live status column, all under the layered CRT treatment &mdash; scanlines,…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Futuristic Terminal Interface
Source: https://codefronts.com/design-styles/css-retro-designs/retro-futuristic-terminal-ui-code/

A command console that boots: staggered POST lines, a typed command, and a live status column, all under the layered CRT treatment &mdash; scanlines, curvature, bloom. The boot reveal is pure CSS animation with the text present in the DOM from the start, which is the difference between a decorative sequence and one that traps an assistive-technology user in a stream of updates.
## HTML
```html
<section class="rt-10" aria-labelledby="rt-10-title">
  <h2 class="rt-10__sr" id="rt-10-title">Retro futuristic terminal console</h2>

  <div class="rt-10__theme">
    <input class="rt-10__theme-input" type="checkbox" id="rt-10-theme">
    <label class="rt-10__theme-label" for="rt-10-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-10__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-10__stage">
    <p class="rt-10__badge">DEC VT-series &middot; 80-column serial console</p>

    <div class="rt-10__console">
      <div class="rt-10__screen">
        <div class="rt-10__grid">
          <div class="rt-10__main">
            <h3 class="rt-10__h">ORION-7 SYSTEM CONSOLE</h3>
            <ol class="rt-10__boot">
              <li style="--rt-10-i: 0">POST . . . . . . . . . . . . . <b>OK</b></li>
              <li style="--rt-10-i: 1">CPU 0 &nbsp;33 MHz &nbsp;CACHE 8K &nbsp; <b>OK</b></li>
              <li style="--rt-10-i: 2">RAM 0000&mdash;FFFF &nbsp;16384K &nbsp; <b>OK</b></li>
              <li style="--rt-10-i: 3">CONTROLLER SCSI ID 7 . . . . . <b>OK</b></li>
              <li style="--rt-10-i: 4">MOUNT /dev/rd0 &nbsp;READ ONLY &nbsp;<b>OK</b></li>
              <li style="--rt-10-i: 5">LINK ETH0 &nbsp;10BASE-T &nbsp; . . <b>UP</b></li>
              <li style="--rt-10-i: 6">CLOCK SYNC &nbsp;DRIFT 0.004s . <b>OK</b></li>
              <li style="--rt-10-i: 7" class="rt-10__warn">SENSOR 4 &nbsp;OUT OF RANGE . . <b>CHECK</b></li>
              <li style="--rt-10-i: 8">KERNEL 2.0.34 &nbsp;LOADED . . . <b>OK</b></li>
            </ol>
            <p class="rt-10__prompt">
              <span class="rt-10__ps1">orion:~$</span>
              <span class="rt-10__typed">status --all --verbose</span>
              <span class="rt-10__caret" aria-hidden="true"></span>
            </p>
          </div>

          <aside class="rt-10__rail" aria-label="System status">
            <h4 class="rt-10__rail-h">STATUS</h4>
            <dl class="rt-10__stats">
              <div><dt>LOAD</dt><dd>0.42</dd></div>
              <div><dt>MEM</dt><dd>11208K</dd></div>
              <div><dt>SWAP</dt><dd>0K</dd></div>
              <div><dt>PROC</dt><dd>37</dd></div>
              <div><dt>UPTIME</dt><dd>04:11</dd></div>
              <div><dt>TEMP</dt><dd>41C</dd></div>
            </dl>
            <div class="rt-10__meter" role="img" aria-label="Bus utilisation, 62 percent">
              <span class="rt-10__meter-l">BUS</span>
              <span class="rt-10__meter-t"><span class="rt-10__meter-f"></span></span>
              <span class="rt-10__meter-v">62%</span>
            </div>
          </aside>
        </div>

        <div class="rt-10__scan" aria-hidden="true"></div>
        <div class="rt-10__vig" aria-hidden="true"></div>
      </div>

      <div class="rt-10__chin">
        <span>VT-320 / SERIAL A</span>
        <span class="rt-10__led" aria-hidden="true"></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-10 {
  --rt-10-scan: 3px;
  --rt-10-curve: 20px;
  --rt-10-fg: #7dfab0;
  --rt-10-fg-dim: #3f9f6d;
  --rt-10-warn: #ffd166;
  --rt-10-tube: #04120c;
  --rt-10-mono: ui-monospace, SFMono-Regular, "Cascadia Mono", Menlo, Consolas, monospace;
  --rt-10-bg: #0c1013;
  --rt-10-bg: oklch(16% 0.008 210);
  --rt-10-surface: #171c20;
  --rt-10-surface: oklch(23% 0.009 210);
  --rt-10-ink: #eaeff1;
  --rt-10-ink: oklch(95% 0.004 210);
  --rt-10-ink-2: #9ba5aa;
  --rt-10-ink-2: oklch(71% 0.009 210);
  --rt-10-line: #333c41;
  --rt-10-line: oklch(33% 0.01 210);
  --rt-10-acc: #6ee7b7;
  --rt-10-acc: oklch(85% 0.12 165);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-10-bg);
  color: var(--rt-10-ink);
  font-family: var(--rt-10-mono);
  -webkit-text-size-adjust: 100%;
}

.rt-10 *,
.rt-10 *::before,
.rt-10 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .rt-10 {
    --rt-10-bg: #d8dcde;
    --rt-10-bg: oklch(88% 0.005 210);
    --rt-10-surface: #eef1f2;
    --rt-10-surface: oklch(95% 0.003 210);
    --rt-10-ink: #14181a;
    --rt-10-ink: oklch(19% 0.006 210);
    --rt-10-ink-2: #4a5257;
    --rt-10-ink-2: oklch(43% 0.01 210);
    --rt-10-line: #a6aeb2;
    --rt-10-line: oklch(74% 0.008 210);
    --rt-10-acc: #0c6b4d;
    --rt-10-acc: oklch(46% 0.11 165);
  }
}

.rt-10[data-theme="dark"] {
  --rt-10-bg: #0c1013;
  --rt-10-bg: oklch(16% 0.008 210);
  --rt-10-surface: #171c20;
  --rt-10-surface: oklch(23% 0.009 210);
  --rt-10-ink: #eaeff1;
  --rt-10-ink: oklch(95% 0.004 210);
  --rt-10-ink-2: #9ba5aa;
  --rt-10-ink-2: oklch(71% 0.009 210);
  --rt-10-line: #333c41;
  --rt-10-line: oklch(33% 0.01 210);
  --rt-10-acc: #6ee7b7;
  --rt-10-acc: oklch(85% 0.12 165);
}

@media (prefers-color-scheme: light) {
  .rt-10:has(.rt-10__theme-input:checked) {
    --rt-10-bg: #0c1013;
    --rt-10-bg: oklch(16% 0.008 210);
    --rt-10-surface: #171c20;
    --rt-10-surface: oklch(23% 0.009 210);
    --rt-10-ink: #eaeff1;
    --rt-10-ink: oklch(95% 0.004 210);
    --rt-10-ink-2: #9ba5aa;
    --rt-10-ink-2: oklch(71% 0.009 210);
    --rt-10-line: #333c41;
    --rt-10-line: oklch(33% 0.01 210);
    --rt-10-acc: #6ee7b7;
    --rt-10-acc: oklch(85% 0.12 165);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-10:has(.rt-10__theme-input:checked) {
    --rt-10-bg: #d8dcde;
    --rt-10-bg: oklch(88% 0.005 210);
    --rt-10-surface: #eef1f2;
    --rt-10-surface: oklch(95% 0.003 210);
    --rt-10-ink: #14181a;
    --rt-10-ink: oklch(19% 0.006 210);
    --rt-10-ink-2: #4a5257;
    --rt-10-ink-2: oklch(43% 0.01 210);
    --rt-10-line: #a6aeb2;
    --rt-10-line: oklch(74% 0.008 210);
    --rt-10-acc: #0c6b4d;
    --rt-10-acc: oklch(46% 0.11 165);
  }
}

.rt-10__sr {
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

.rt-10__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-10__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-10__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-10-line);
  border-radius: 4px;
  background: var(--rt-10-surface);
  color: var(--rt-10-ink-2);
  cursor: pointer;
}

.rt-10__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-10__theme-input:focus-visible + .rt-10__theme-label {
  outline: 2px solid var(--rt-10-acc);
  outline-offset: 2px;
}

.rt-10__stage {
  max-inline-size: 76rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.6rem, 0.4rem + 1.5vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1rem;
}

.rt-10__badge {
  margin: 0;
  justify-self: start;
  min-inline-size: 0;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--rt-10-ink-2);
  border: 1px solid var(--rt-10-line);
  padding: 0.35rem 0.7rem;
  border-radius: 3px;
}

.rt-10__console {
  min-inline-size: 0;
  background: #23282b;
  border-radius: calc(var(--rt-10-curve) + 14px);
  padding: clamp(0.7rem, 0.5rem + 1.2vw, 1.3rem);
  box-shadow: inset 0 2px 0 rgba(255,255,255,0.18), inset 0 -3px 0 rgba(0,0,0,0.55), 0 20px 44px -22px rgba(0,0,0,0.8);
}

.rt-10__screen {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  border-radius: var(--rt-10-curve);
  background: radial-gradient(120% 100% at 50% 42%, #082018 0%, var(--rt-10-tube) 76%);
  padding: clamp(0.9rem, 0.6rem + 1.6vw, 1.8rem);
  box-shadow: inset 0 0 0 2px #04100b, inset 0 0 32px 8px rgba(0,0,0,0.8);
}

.rt-10__grid {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

.rt-10__main {
  min-inline-size: 0;
  display: grid;
  gap: 0.9rem;
  align-content: start;
}

.rt-10__h {
  margin: 0;
  color: var(--rt-10-fg);
  font-size: clamp(0.95rem, 0.75rem + 1.2vw, 1.35rem);
  letter-spacing: 0.16em;
  font-weight: 700;
  min-inline-size: 0;
  text-shadow: 0 0 6px rgba(125, 250, 176, 0.55);
}

.rt-10__boot {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.22rem;
  min-inline-size: 0;
  font-size: clamp(0.66rem, 0.55rem + 0.65vw, 0.85rem);
  color: var(--rt-10-fg-dim);
}

.rt-10__boot li {
  min-inline-size: 0;
  overflow-wrap: anywhere;
  opacity: 0;
  animation: rt-10-in 320ms ease-out forwards;
  animation-delay: calc(var(--rt-10-i) * 140ms);
}

.rt-10__boot b {
  color: var(--rt-10-fg);
  font-weight: 700;
}

.rt-10__warn b {
  color: var(--rt-10-warn);
}

@keyframes rt-10-in {
  from {
    opacity: 0;
    transform: translateY(2px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.rt-10__prompt {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5ch;
  color: var(--rt-10-fg);
  font-size: clamp(0.7rem, 0.58rem + 0.7vw, 0.9rem);
  min-inline-size: 0;
}

.rt-10__ps1 {
  color: var(--rt-10-acc);
}

.rt-10__typed {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  inline-size: 0;
  animation: rt-10-type 1.6s steps(22, end) forwards;
  animation-delay: 1.4s;
}

@keyframes rt-10-type {
  to {
    inline-size: 22ch;
  }
}

.rt-10__caret {
  inline-size: 0.6em;
  block-size: 1.1em;
  background: var(--rt-10-fg);
  display: inline-block;
  animation: rt-10-blink 1.1s steps(1, end) infinite;
}

@keyframes rt-10-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

.rt-10__rail {
  min-inline-size: 0;
  border: 1px solid rgba(125, 250, 176, 0.28);
  border-radius: 4px;
  padding: 0.75rem 0.85rem;
  display: grid;
  gap: 0.6rem;
  align-content: start;
  background: rgba(125, 250, 176, 0.04);
}

.rt-10__rail-h {
  margin: 0;
  font-size: 0.66rem;
  letter-spacing: 0.2em;
  color: var(--rt-10-acc);
}

.rt-10__stats {
  margin: 0;
  display: grid;
  gap: 0.22rem;
  font-size: 0.72rem;
  color: var(--rt-10-fg-dim);
}

.rt-10__stats > div {
  display: flex;
  justify-content: space-between;
  gap: 0.75rem;
  min-inline-size: 0;
}

.rt-10__stats dt {
  margin: 0;
}

.rt-10__stats dd {
  margin: 0;
  color: var(--rt-10-fg);
  font-variant-numeric: tabular-nums;
}

.rt-10__meter {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.7rem;
  color: var(--rt-10-fg-dim);
  min-inline-size: 0;
}

.rt-10__meter-t {
  flex: 1 1 auto;
  min-inline-size: 0;
  block-size: 10px;
  border: 1px solid rgba(125,250,176,0.4);
  padding: 1px;
}

.rt-10__meter-f {
  display: block;
  block-size: 100%;
  inline-size: 62%;
  background: repeating-linear-gradient(90deg, var(--rt-10-fg) 0 4px, rgba(0,0,0,0) 4px 6px);
}

.rt-10__meter-v {
  color: var(--rt-10-fg);
  font-variant-numeric: tabular-nums;
}

.rt-10__scan {
  position: absolute;
  inset: 0;
  z-index: 4;
  pointer-events: none;
  opacity: 0.5;
  background: repeating-linear-gradient(to bottom, rgba(0,0,0,0) 0, rgba(0,0,0,0) calc(var(--rt-10-scan) - 1px), rgba(0,0,0,0.7) calc(var(--rt-10-scan) - 1px), rgba(0,0,0,0.7) var(--rt-10-scan));
}

@media (min-resolution: 1.5dppx) {
  .rt-10__scan {
    background: repeating-linear-gradient(to bottom, rgba(0,0,0,0) 0, rgba(0,0,0,0.6) calc(var(--rt-10-scan) * 0.5), rgba(0,0,0,0) calc(var(--rt-10-scan) * 1.34));
  }
}

.rt-10__vig {
  position: absolute;
  inset: -1px;
  z-index: 5;
  pointer-events: none;
  background: radial-gradient(118% 106% at 50% 50%, rgba(0,0,0,0) 54%, rgba(0,0,0,0.5) 86%, rgba(0,0,0,0.88) 100%);
}

.rt-10__chin {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.7rem 0.35rem 0.1rem;
  font-size: 0.62rem;
  letter-spacing: 0.2em;
  color: #8d9498;
  min-inline-size: 0;
}

.rt-10__led {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  flex: none;
  background: #63f0a0;
  box-shadow: 0 0 8px 2px rgba(99,240,160,0.65);
}

@media (prefers-reduced-motion: reduce) {
  .rt-10__boot li {
    animation: none;
    opacity: 1;
  }

  .rt-10__typed {
    animation: none;
    inline-size: 22ch;
  }

  .rt-10__caret {
    animation: none;
  }
}

@media (min-width: 52rem) {
  .rt-10__grid {
    grid-template-columns: minmax(0, 1fr) minmax(0, 15rem);
  }
}
```
