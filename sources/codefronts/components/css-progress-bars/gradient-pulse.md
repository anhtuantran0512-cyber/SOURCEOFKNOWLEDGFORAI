---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/gradient-pulse/"
title: "Gradient Pulse Progress Bar"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The onboarding bar that looks alive: a violet-to-cyan fill with a highlight sheen travelling across it and a glow that breathes on a 3s cycle."
has_js: "false"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Pulse Progress Bar
Source: https://codefronts.com/components/css-progress-bars/gradient-pulse/

The onboarding bar that looks alive: a violet-to-cyan fill with a highlight sheen travelling across it and a glow that breathes on a 3s cycle. Two ambient animations, both compositor-friendly, both switched off under reduced motion.
## HTML
```html
<div class="pb-16">
  <input class="pb-16__sr" type="checkbox" id="pb-16-light">
  <label class="pb-16__theme" for="pb-16-light" title="Switch light or dark theme">
    <svg class="pb-16__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-16__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="pb-16__vh">Switch light or dark theme</span>
  </label>

  <div class="pb-16__stage">
    <div class="pb-16__card">
      <header class="pb-16__head">
        <p class="pb-16__eyebrow"><span class="pb-16__badge">Onboarding</span><span class="pb-16__mono">3 of 4 tasks</span></p>
        <h2 class="pb-16__title">You are almost set up</h2>
        <p class="pb-16__lead">Finish the last step and your workspace goes live for the whole team.</p>
      </header>

      <div class="pb-16__hero" role="progressbar" aria-valuenow="78" aria-valuemin="0" aria-valuemax="100" aria-valuetext="78 percent of setup complete" aria-label="Workspace setup" style="--value:78">
        <span class="pb-16__heroFill"></span>
        <span class="pb-16__heroPct pb-16__mono">78%</span>
      </div>

      <ul class="pb-16__rows">
        <li class="pb-16__row">
          <span class="pb-16__rowHead"><span class="pb-16__rowName">Connect repository</span><span class="pb-16__rowVal pb-16__mono">100%</span></span>
          <span class="pb-16__bar pb-16__bar--done" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Connect repository, complete" aria-label="Connect repository" style="--value:100"><span class="pb-16__fill"></span></span>
        </li>
        <li class="pb-16__row">
          <span class="pb-16__rowHead"><span class="pb-16__rowName">Invite teammates</span><span class="pb-16__rowVal pb-16__mono">100%</span></span>
          <span class="pb-16__bar pb-16__bar--done" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Invite teammates, complete" aria-label="Invite teammates" style="--value:100"><span class="pb-16__fill"></span></span>
        </li>
        <li class="pb-16__row">
          <span class="pb-16__rowHead"><span class="pb-16__rowName">Import design tokens</span><span class="pb-16__rowVal pb-16__mono">64%</span></span>
          <span class="pb-16__bar" role="progressbar" aria-valuenow="64" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Import design tokens, 64 percent" aria-label="Import design tokens" style="--value:64"><span class="pb-16__fill"></span></span>
        </li>
        <li class="pb-16__row">
          <span class="pb-16__rowHead"><span class="pb-16__rowName">Set a deploy target</span><span class="pb-16__rowVal pb-16__mono">0%</span></span>
          <span class="pb-16__bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Set a deploy target, not started" aria-label="Set a deploy target" style="--value:0"><span class="pb-16__fill"></span></span>
        </li>
      </ul>

      <p class="pb-16__note pb-16__mono">sheen: background-position &middot; glow: box-shadow &middot; no JavaScript</p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-16 {
  --bgSolid: #070610;
  --card: #0d0b1c;
  --ink: #f2f0ff;
  --muted: rgba(242,240,255,.62);
  --line: rgba(242,240,255,.12);
  --track: rgba(242,240,255,.08);
  --a: #8b5cf6;
  --b: #22d3ee;
  --accent: #a78bfa;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bgSolid);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(70% .2 290)) {
  .pb-16 {
    --a: oklch(66% .21 293);
    --b: oklch(82% .13 199);
    --accent: oklch(76% .16 295);
  }
}

.pb-16 *,
.pb-16 *::before,
.pb-16 *::after {
  box-sizing: border-box;
}

.pb-16__sr {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pb-16__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pb-16__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(80% 55% at 15% 0%,color-mix(in srgb,var(--a) 26%,transparent),transparent 58%), radial-gradient(70% 55% at 95% 100%,color-mix(in srgb,var(--b) 20%,transparent),transparent 60%);
}

.pb-16__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-16__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-16__sr:focus-visible + .pb-16__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-16__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-16__sun {
  display: none;
}

.pb-16__moon {
  display: block;
}

.pb-16__card {
  inline-size: min(40rem,100%);
  display: grid;
  gap: clamp(1rem,2.4vw,1.5rem);
  padding: clamp(1.4rem,3.4vw,2.3rem);
  border-radius: 1.6rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 90%,transparent);
  -webkit-backdrop-filter: blur(16px);
  backdrop-filter: blur(16px);
  box-shadow: 0 1px 0 rgba(255,255,255,.06) inset,0 36px 90px -46px rgba(0,0,0,.95);
}

.pb-16__head {
  display: grid;
  gap: .45rem;
}

.pb-16__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .55rem;
  align-items: center;
}

.pb-16__badge {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .26rem .5rem;
  border-radius: .4rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--a) 20%,transparent);
  border: 1px solid color-mix(in srgb,var(--a) 36%,transparent);
}

.pb-16__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-16__title {
  margin: 0;
  font-size: clamp(1.45rem,3.5vw,2.1rem);
  line-height: 1.12;
  letter-spacing: -.024em;
  font-weight: 650;
}

.pb-16__lead {
  margin: 0;
  max-inline-size: 46ch;
  font-size: clamp(.9rem,1.5vw,1rem);
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-16__hero {
  position: relative;
  inline-size: 100%;
  block-size: 1.15rem;
  border-radius: 99px;
  overflow: hidden;
  background: var(--track);
  border: 1px solid var(--line);
  box-shadow: 0 2px 5px rgba(0,0,0,.4) inset;
  display: grid;
  align-items: center;
}

.pb-16__heroFill,
.pb-16__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background-color: var(--a);
  background-image: linear-gradient(90deg,var(--a) 0%,var(--b) 45%,rgba(255,255,255,.55) 50%,var(--b) 55%,var(--a) 100%);
  background-size: 280% 100%;
  animation: pb-16-sheen 2.6s cubic-bezier(.4,0,.2,1) infinite;
  transition: inline-size .45s cubic-bezier(.4,0,.2,1);
}

@keyframes pb-16-sheen {
  from {
    background-position: 120% 0;
  }

  to {
    background-position: -60% 0;
  }
}

.pb-16__hero {
  animation: pb-16-breathe 3s ease-in-out infinite;
}

@keyframes pb-16-breathe {
  0%,
    100% {
    box-shadow: 0 2px 5px rgba(0,0,0,.4) inset,0 0 0 0 color-mix(in srgb,var(--accent) 30%,transparent);
  }

  50% {
    box-shadow: 0 2px 5px rgba(0,0,0,.4) inset,0 0 20px 2px color-mix(in srgb,var(--accent) 45%,transparent);
  }
}

.pb-16__heroPct {
  position: relative;
  z-index: 1;
  justify-self: end;
  margin-inline-end: .6rem;
  font-size: .68rem;
  font-weight: 700;
  color: #0b0620;
  text-shadow: 0 1px 0 rgba(255,255,255,.35);
}

.pb-16__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .85rem;
}

.pb-16__row {
  display: grid;
  gap: .35rem;
}

.pb-16__rowHead {
  display: flex;
  justify-content: space-between;
  gap: .8rem;
  align-items: baseline;
}

.pb-16__rowName {
  font-size: .88rem;
  font-weight: 550;
}

.pb-16__rowVal {
  color: var(--ink);
  font-weight: 600;
}

.pb-16__bar {
  position: relative;
  display: block;
  inline-size: 100%;
  block-size: .5rem;
  border-radius: 99px;
  overflow: hidden;
  background: var(--track);
  border: 1px solid var(--line);
}

.pb-16__row:nth-child(2) .pb-16__fill {
  animation-delay: -.4s;
}

.pb-16__row:nth-child(3) .pb-16__fill {
  animation-delay: -.8s;
}

.pb-16__row:nth-child(4) .pb-16__fill {
  animation-delay: -1.2s;
}

.pb-16__bar--done .pb-16__fill {
  animation-play-state: paused;
  background-image: linear-gradient(90deg,var(--a),var(--b));
}

.pb-16__note {
  margin: 0;
  opacity: .7;
}

.pb-16[data-theme="light"],
.pb-16:has(#pb-16-light:checked) {
  --bgSolid: #f7f6ff;
  --card: #ffffff;
  --ink: #140c28;
  --muted: rgba(20,12,40,.62);
  --line: rgba(20,12,40,.1);
  --track: rgba(20,12,40,.08);
  --a: #7c3aed;
  --b: #0891b2;
  --accent: #7c3aed;
}

.pb-16:has(#pb-16-light:checked) .pb-16__theme {
  background: rgba(20,12,40,.05);
}

.pb-16:has(#pb-16-light:checked) .pb-16__sun {
  display: block;
}

.pb-16:has(#pb-16-light:checked) .pb-16__moon {
  display: none;
}

.pb-16:has(#pb-16-light:checked) .pb-16__heroPct {
  color: #fff;
  text-shadow: 0 1px 2px rgba(0,0,0,.45);
}

@media (prefers-color-scheme: light) {
  .pb-16:not([data-theme="dark"]):not(:has(#pb-16-light:checked)) {
    --bgSolid: #f7f6ff;
    --card: #ffffff;
    --ink: #140c28;
    --muted: rgba(20,12,40,.62);
    --line: rgba(20,12,40,.1);
    --track: rgba(20,12,40,.08);
    --a: #7c3aed;
    --b: #0891b2;
    --accent: #7c3aed;
  }

  .pb-16:not([data-theme="dark"]):not(:has(#pb-16-light:checked)) .pb-16__theme {
    background: rgba(20,12,40,.05);
  }

  .pb-16:not([data-theme="dark"]):not(:has(#pb-16-light:checked)) .pb-16__sun {
    display: block;
  }

  .pb-16:not([data-theme="dark"]):not(:has(#pb-16-light:checked)) .pb-16__moon {
    display: none;
  }

  .pb-16:not([data-theme="dark"]):not(:has(#pb-16-light:checked)) .pb-16__heroPct {
    color: #fff;
    text-shadow: 0 1px 2px rgba(0,0,0,.45);
  }

  .pb-16:not([data-theme="light"]):has(#pb-16-light:checked) {
    --bgSolid: #070610;
    --card: #0d0b1c;
    --ink: #f2f0ff;
    --muted: rgba(242,240,255,.62);
    --line: rgba(242,240,255,.12);
    --track: rgba(242,240,255,.08);
    --a: #8b5cf6;
    --b: #22d3ee;
    --accent: #a78bfa;
  }

  @supports (color: oklch(70% .2 290)) {
    .pb-16:not([data-theme="light"]):has(#pb-16-light:checked) {
      --a: oklch(66% .21 293);
      --b: oklch(82% .13 199);
      --accent: oklch(76% .16 295);
    }
  }

  .pb-16:not([data-theme="light"]):has(#pb-16-light:checked) .pb-16__theme {
    background: rgba(255,255,255,.06);
  }

  .pb-16:not([data-theme="light"]):has(#pb-16-light:checked) .pb-16__sun {
    display: none;
  }

  .pb-16:not([data-theme="light"]):has(#pb-16-light:checked) .pb-16__moon {
    display: block;
  }

  .pb-16:not([data-theme="light"]):has(#pb-16-light:checked) .pb-16__heroPct {
    color: #0b0620;
    text-shadow: 0 1px 0 rgba(255,255,255,.35);
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-16 *,
    .pb-16 *::before,
    .pb-16 *::after {
    animation: none !important;
    transition: none !important;
  }

  .pb-16__heroFill,
    .pb-16__fill {
    background-image: linear-gradient(90deg,var(--a),var(--b));
    background-size: 100% 100%;
  }
}

@media (forced-colors: active) {
  .pb-16__card,
    .pb-16__hero,
    .pb-16__bar,
    .pb-16__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-16__heroFill,
    .pb-16__fill {
    background: Highlight;
  }

  .pb-16__heroPct {
    color: CanvasText;
    text-shadow: none;
  }
}
```
