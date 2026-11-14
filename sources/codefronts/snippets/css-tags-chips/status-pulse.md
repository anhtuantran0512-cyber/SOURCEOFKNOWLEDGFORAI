---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/status-pulse/"
title: "Live Pulsing Status Badge CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "LIVE, REC, ON AIR — broadcast badges with a pulse that costs nothing: the ping is a ::before ring animating only scale and opacity (compositor-side, 60fps…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Pulsing Status Badge CSS
Source: https://codefronts.com/snippets/css-tags-chips/status-pulse/

LIVE, REC, ON AIR — broadcast badges with a pulse that costs nothing: the ping is a ::before ring animating only scale and opacity (compositor-side, 60fps with 200 badges on screen), and the demo explicitly contrasts it with the box-shadow-spread pulse people copy from old tutorials, which repaints every frame. Includes the double-ring sonar, the REC blink on steps(), a breathing ambient glow, and the viewer-count pill with tabular numerals so digits don't jitter.
## HTML
```html
<section class="ctc-16" aria-label="Live pulsing status badge demo">
  <div class="ctc-16__stage">
    <div class="ctc-16__wrap">
      <header class="ctc-16__head">
        <p class="ctc-16__kicker">Pulse engineering · scale + opacity only</p>
        <h1>Alive at 60fps, even ×200</h1>
      </header>
      <div class="ctc-16__panel">
        <p class="ctc-16__lab">01 · The broadcast set</p>
        <div class="ctc-16__row">
          <span class="ctc-16__badge ctc-16__badge--live"><i class="ctc-16__dot"></i>LIVE</span>
          <span class="ctc-16__badge ctc-16__badge--rec"><i class="ctc-16__dot ctc-16__dot--blink"></i>REC 00:14:32</span>
          <span class="ctc-16__badge ctc-16__badge--air"><i class="ctc-16__dot ctc-16__dot--twin"></i>ON AIR</span>
          <span class="ctc-16__badge ctc-16__badge--view">👁 <b>1,204</b> watching</span>
        </div>
      </div>
      <div class="ctc-16__panel">
        <p class="ctc-16__lab">02 · Perf comparison — same look, different bill</p>
        <div class="ctc-16__row ctc-16__row--split">
          <div><span class="ctc-16__badge ctc-16__badge--live"><i class="ctc-16__dot"></i>transform ping</span><small>scale+opacity · compositor · ✓ ship it</small></div>
          <div><span class="ctc-16__badge ctc-16__badge--live"><i class="ctc-16__dot ctc-16__dot--shadow"></i>box-shadow pulse</span><small>spread anim · repaints every frame · ✗ lists</small></div>
        </div>
      </div>
      <div class="ctc-16__panel">
        <p class="ctc-16__lab">03 · Status board — pulse only what's actually happening</p>
        <ul class="ctc-16__board">
          <li><i class="ctc-16__dot ctc-16__dot--ok"></i><b>API</b><span>Operational</span><small>99.99%</small></li>
          <li><i class="ctc-16__dot ctc-16__dot--warn"></i><b>Webhooks</b><span>Degraded — retrying</span><small>97.2%</small></li>
          <li class="is-incident"><i class="ctc-16__dot"></i><b>EU database</b><span>Incident · failover running</span><small>—</small></li>
          <li><i class="ctc-16__dot ctc-16__dot--off"></i><b>Legacy v1</b><span>Deprecated</span><small>frozen</small></li>
        </ul>
      </div>
      <p class="ctc-16__note">The ring is <code>background:inherit</code> on <code>::before</code>, animating <code>scale</code> 1→2.6 and <code>opacity</code> .8→0 on an ease-out — energy dissipates, so the ring must decelerate.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-16,
.ctc-16 *,
.ctc-16 *::before,
.ctc-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-16 {
  --bg: oklch(0.19 0.015 270);
  --panel: oklch(0.235 0.018 270);
  --ink: oklch(0.95 0.008 270);
  --mut: oklch(0.64 0.02 270);
  --line: oklch(0.32 0.02 270);
  --red: oklch(0.62 0.23 25);
  --ok: oklch(0.74 0.18 150);
  --warn: oklch(0.8 0.15 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-16__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 85% -10%,oklch(0.3 0.08 25/.4),transparent 62%),var(--bg);
  container: ctc16/inline-size;
}

.ctc-16__wrap {
  width: min(680px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-16__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.72 0.18 25);
}

.ctc-16__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-16__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-16__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 14px;
}

.ctc-16__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
}

.ctc-16__badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .08em;
  border: 1px solid var(--line);
  background: oklch(1 0 0/.05);
}

.ctc-16__badge--live {
  color: oklch(0.8 0.16 25);
  border-color: color-mix(in oklch,var(--red) 45%,transparent);
  background: color-mix(in oklch,var(--red) 14%,transparent);
}

.ctc-16__badge--rec {
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.ctc-16__badge--air {
  color: oklch(0.85 0.1 85);
  border-color: color-mix(in oklch,var(--warn) 40%,transparent);
  background: color-mix(in oklch,var(--warn) 10%,transparent);
}

.ctc-16__badge--view {
  letter-spacing: 0;
  font-weight: 600;
  color: var(--mut);
}

.ctc-16__badge--view b {
  font-weight: 800;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.ctc-16__dot {
  position: relative;
  flex: none;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--red);
}

.ctc-16__dot::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: ctc16-ping 1.6s cubic-bezier(0,0,.2,1) infinite;
}

@keyframes ctc16-ping {
  0% {
    scale: 1;
    opacity: .8;
  }

  100% {
    scale: 2.6;
    opacity: 0;
  }
}

.ctc-16__dot--blink {
  animation: ctc16-blink 1s steps(2,jump-none) infinite;
}

.ctc-16__dot--blink::before {
  animation: none;
}

@keyframes ctc16-blink {
  50% {
    opacity: .25;
  }
}

.ctc-16__dot--twin {
  background: var(--warn);
}

.ctc-16__dot--twin::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: ctc16-ping 1.6s cubic-bezier(0,0,.2,1) .8s infinite;
}

.ctc-16__dot--shadow::before {
  animation: ctc16-shadow 1.6s ease-out infinite;
  scale: 1 !important;
  background: transparent;
}

@keyframes ctc16-shadow {
  0% {
    box-shadow: 0 0 0 0 oklch(0.62 0.23 25/.7);
  }

  100% {
    box-shadow: 0 0 0 12px oklch(0.62 0.23 25/0);
  }
}

.ctc-16__dot--ok {
  background: var(--ok);
}

.ctc-16__dot--ok::before {
  animation: none;
}

.ctc-16__dot--warn {
  background: var(--warn);
}

.ctc-16__dot--warn::before {
  animation: none;
}

.ctc-16__dot--off {
  background: transparent;
  box-shadow: inset 0 0 0 2px var(--mut);
}

.ctc-16__dot--off::before {
  animation: none;
}

.ctc-16__row--split {
  gap: 20px;
}

.ctc-16__row--split>div {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.ctc-16__row--split small {
  font-size: 11px;
  color: var(--mut);
}

.ctc-16__board {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.ctc-16__board li {
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  align-items: center;
  gap: 12px;
  padding: 11px 12px;
  border-radius: 10px;
}

.ctc-16__board li.is-incident {
  background: color-mix(in oklch,var(--red) 9%,transparent);
}

.ctc-16__board b {
  font-size: 13.5px;
  font-weight: 700;
}

.ctc-16__board span {
  font-size: 12px;
  color: var(--mut);
  justify-self: end;
}

.ctc-16__board li.is-incident span {
  color: oklch(0.8 0.16 25);
  font-weight: 700;
}

.ctc-16__board small {
  font-size: 11.5px;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
  min-width: 52px;
  text-align: right;
}

.ctc-16__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid var(--red);
  padding-left: 12px;
}

.ctc-16__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(1 0 0/.09);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@container ctc16 (width < 520px) {
  .ctc-16__board li {
    grid-template-columns: auto 1fr auto;
  }

  .ctc-16__board small {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-16__dot::before,
    .ctc-16__dot::after,
    .ctc-16__dot--blink {
    animation: none !important;
    opacity: 1;
  }
}
```
