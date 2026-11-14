---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/notch-chip/"
title: "Notched Corner Cyberpunk Badge CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Sci-fi HUD badges with genuinely cut corners — clip-path polygons, not border-radius pretending."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Notched Corner Cyberpunk Badge CSS
Source: https://codefronts.com/snippets/css-tags-chips/notch-chip/

Sci-fi HUD badges with genuinely cut corners — clip-path polygons, not border-radius pretending. The 1.5px angled border is the two-layer clip trick (accent-filled element, inset pseudo-element re-clipped with the same polygon), a scanline sheet drifts over the whole console, and hovering a badge fires a two-frame RGB-split glitch. One --notch variable sizes every cut, so the geometry scales from 8px chips to hero panels.
## HTML
```html
<section class="ctc-10" aria-label="Notched corner cyberpunk badge demo">
  <div class="ctc-10__stage">
    <div class="ctc-10__wrap">
      <header class="ctc-10__head">
        <p class="ctc-10__kicker">// SECTOR 7 · ACCESS CONSOLE</p>
        <h1 data-text="Corners cut, not rounded">Corners cut, not rounded</h1>
      </header>
      <div class="ctc-10__panel">
        <p class="ctc-10__lab">01 · Rank badges — two-layer clip border, hover to glitch</p>
        <div class="ctc-10__row">
          <a class="ctc-10__badge" href="#ctc10"><span data-text="NETRUNNER">NETRUNNER</span></a>
          <a class="ctc-10__badge" href="#ctc10"><span data-text="ICE BREAKER">ICE BREAKER</span></a>
          <a class="ctc-10__badge ctc-10__badge--warn" href="#ctc10"><span data-text="WANTED ★★★">WANTED ★★★</span></a>
          <a class="ctc-10__badge ctc-10__badge--ghost" href="#ctc10"><span data-text="OFFLINE">OFFLINE</span></a>
        </div>
      </div>
      <div class="ctc-10__panel">
        <p class="ctc-10__lab">02 · Geometry — one --notch variable, four recipes</p>
        <div class="ctc-10__row">
          <span class="ctc-10__badge" style="--n:6px"><span>--n: 6px</span></span>
          <span class="ctc-10__badge" style="--n:14px"><span>--n: 14px</span></span>
          <span class="ctc-10__badge ctc-10__badge--octa"><span>all four cut</span></span>
          <span class="ctc-10__badge ctc-10__badge--tab"><span>tab / one side</span></span>
        </div>
      </div>
      <div class="ctc-10__panel">
        <p class="ctc-10__lab">03 · Loadout — badges doing real inventory work</p>
        <ul class="ctc-10__inv">
          <li><b>Mantis blades</b><span class="ctc-10__badge ctc-10__badge--sm"><span>EQUIPPED</span></span></li>
          <li><b>Cyberdeck MK.4</b><span class="ctc-10__badge ctc-10__badge--sm ctc-10__badge--warn"><span>OVERHEAT 82%</span></span></li>
          <li><b>Optical camo</b><span class="ctc-10__badge ctc-10__badge--sm ctc-10__badge--ghost"><span>COOLDOWN 12s</span></span></li>
        </ul>
      </div>
      <p class="ctc-10__note">&gt; border = element painted accent + <code>::before</code> inset 1.5px with <code>clip-path:inherit</code>. Glow = <code>filter:drop-shadow()</code> — box-shadow would draw the uncut rectangle.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-10,
.ctc-10 *,
.ctc-10 *::before,
.ctc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-10 {
  --bg: oklch(0.16 0.02 265);
  --panel: oklch(0.2 0.025 265);
  --ink: oklch(0.93 0.02 195);
  --mut: oklch(0.62 0.03 220);
  --hud: oklch(0.82 0.14 195);
  --warn: oklch(0.8 0.16 85);
  --mag: oklch(0.7 0.25 340);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-10__stage {
  position: relative;
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 80% -10%,oklch(0.28 0.06 195/.5),transparent 60%),radial-gradient(50cqi 45cqi at -5% 110%,oklch(0.26 0.08 340/.35),transparent 60%),var(--bg);
  container: ctc10/inline-size;
}

.ctc-10__stage::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(0deg,oklch(1 0 0/.04) 0 1px,transparent 1px 3px);
  animation: ctc10-scan 9s linear infinite;
}

@keyframes ctc10-scan {
  to {
    background-position: 0 60px;
  }
}

.ctc-10__wrap {
  width: min(680px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-10__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .22em;
  color: var(--hud);
}

.ctc-10__head h1 {
  font-size: clamp(22px,3.6cqi,34px);
  font-weight: 800;
  letter-spacing: -.01em;
  margin: 8px 0 8px;
  text-shadow: 0 0 24px color-mix(in oklch,var(--hud) 40%,transparent);
}

.ctc-10__panel {
  position: relative;
  background: oklch(1 0 0/.04);
  border: 1px solid oklch(0.32 0.04 220);
  padding: 16px 18px;
  clip-path: polygon(12px 0,100% 0,100% calc(100% - 12px),calc(100% - 12px) 100%,0 100%,0 12px);
}

.ctc-10__lab {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 13px;
}

.ctc-10__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
}

.ctc-10__badge {
  --n: 10px;
  --c: var(--hud);
  position: relative;
  display: inline-flex;
  filter: drop-shadow(0 0 7px color-mix(in oklch,var(--c) 35%,transparent));
  text-decoration: none;
  transition: filter .25s,translate .2s;
}

.ctc-10__badge {
  background: linear-gradient(120deg,var(--c),color-mix(in oklch,var(--c) 55%,oklch(0.3 0.02 265)));
  clip-path: polygon(var(--n) 0,100% 0,100% calc(100% - var(--n)),calc(100% - var(--n)) 100%,0 100%,0 var(--n));
}

.ctc-10__badge::before {
  content: "";
  position: absolute;
  inset: 1.5px;
  clip-path: inherit;
  background: linear-gradient(180deg,color-mix(in oklch,var(--c) 14%,var(--panel)),var(--panel) 55%);
}

.ctc-10__badge>span {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 20px;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .14em;
  color: var(--c);
}

a.ctc-10__badge:hover,
a.ctc-10__badge:focus-visible {
  filter: drop-shadow(0 0 14px color-mix(in oklch,var(--c) 65%,transparent));
  translate: 0 -2px;
}

a.ctc-10__badge:focus-visible {
  outline: 2px solid var(--c);
  outline-offset: 3px;
}

a.ctc-10__badge:hover>span,
a.ctc-10__badge:focus-visible>span {
  animation: ctc10-jit .32s steps(2,jump-none);
}

a.ctc-10__badge:hover>span::before,
a.ctc-10__badge:hover>span::after,
a.ctc-10__badge:focus-visible>span::before,
a.ctc-10__badge:focus-visible>span::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  display: inline-flex;
  align-items: center;
  padding: 0 20px;
  mix-blend-mode: screen;
  animation: ctc10-jit .32s steps(2,jump-none) reverse;
}

a.ctc-10__badge:hover>span::before,
a.ctc-10__badge:focus-visible>span::before {
  color: oklch(0.8 0.16 195);
  translate: 2px 0;
}

a.ctc-10__badge:hover>span::after,
a.ctc-10__badge:focus-visible>span::after {
  color: var(--mag);
  translate: -2px 0;
}

@keyframes ctc10-jit {
  0% {
    translate: 0 0;
  }

  25% {
    translate: -3px 1px;
  }

  50% {
    translate: 2px -1px;
  }

  75% {
    translate: -1px 0;
  }

  100% {
    translate: 0 0;
  }
}

.ctc-10__badge--warn {
  --c: var(--warn);
}

.ctc-10__badge--ghost {
  --c: var(--mut);
  filter: none;
}

.ctc-10__badge--octa {
  clip-path: polygon(var(--n) 0,calc(100% - var(--n)) 0,100% var(--n),100% calc(100% - var(--n)),calc(100% - var(--n)) 100%,var(--n) 100%,0 calc(100% - var(--n)),0 var(--n));
}

.ctc-10__badge--tab {
  clip-path: polygon(0 0,calc(100% - 16px) 0,100% 100%,0 100%);
}

.ctc-10__badge--sm>span {
  min-height: 34px;
  padding: 0 13px;
  font-size: 10.5px;
}

.ctc-10__inv {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.ctc-10__inv li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 10px 12px;
  background: oklch(1 0 0/.035);
  border-left: 2px solid oklch(0.32 0.04 220);
}

.ctc-10__inv b {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: .04em;
}

.ctc-10__note {
  font-size: 12px;
  line-height: 1.7;
  color: var(--mut);
}

.ctc-10__note code {
  background: oklch(1 0 0/.08);
  padding: 1px 5px;
  color: var(--ink);
}

@container ctc10 (width < 520px) {
  .ctc-10__inv li {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-10__stage::after {
    animation: none;
  }

  .ctc-10 * {
    animation-duration: .01ms !important;
    transition-duration: .01ms !important;
  }
}
```
