---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/mission-control-timeline/"
title: "Mission Control Timeline — T-Minus Event Log with Status Dots"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "Launch-console aesthetics with dashboard discipline: a T-minus/T-plus event sequence in strict monospace, GO/HOLD/NO-GO status lights paired with text…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mission Control Timeline — T-Minus Event Log with Status Dots
Source: https://codefronts.com/layouts/css-timelines/mission-control-timeline/

Launch-console aesthetics with dashboard discipline: a T-minus/T-plus event sequence in strict monospace, GO/HOLD/NO-GO status lights paired with text labels, a phosphor-green 'now' cursor line, and scan-line texture — the high-contrast technical idiom for aerospace dashboards, infra monitoring and countdown pages.
## HTML
```html
<section class="tls-13" aria-label="Mission control timeline demo">
  <div class="tls-13__console">
    <header class="tls-13__bar"><span class="tls-13__mission">ARTEMIS-C · CREW ROTATION 4</span><span class="tls-13__clock">MET 00:02:14</span></header>
    <ol class="tls-13__log" role="list">
      <li class="tls-13__row tls-13__row--past"><span class="tls-13__t">T−00:45:00</span><span class="tls-13__light" data-s="go" aria-hidden="true"></span><span class="tls-13__ev">Crew ingress complete, hatch sealed</span><span class="tls-13__st">GO</span></li>
      <li class="tls-13__row tls-13__row--past"><span class="tls-13__t">T−00:12:00</span><span class="tls-13__light" data-s="go" aria-hidden="true"></span><span class="tls-13__ev">Propellant load complete · tanks at flight press</span><span class="tls-13__st">GO</span></li>
      <li class="tls-13__row tls-13__row--past"><span class="tls-13__t">T−00:04:00</span><span class="tls-13__light" data-s="go" aria-hidden="true"></span><span class="tls-13__ev">Final poll: all stations report</span><span class="tls-13__st">GO</span></li>
      <li class="tls-13__now" aria-hidden="true"><span>◄ NOW</span></li>
      <li class="tls-13__row"><span class="tls-13__t">T+00:02:14</span><span class="tls-13__light" data-s="go" aria-hidden="true"></span><span class="tls-13__ev">Max-Q passed · vehicle nominal</span><span class="tls-13__st">GO</span></li>
      <li class="tls-13__row"><span class="tls-13__t">T+00:08:30</span><span class="tls-13__light" data-s="hold" aria-hidden="true"></span><span class="tls-13__ev">MECO confirm awaiting downrange telemetry</span><span class="tls-13__st">HOLD</span></li>
      <li class="tls-13__row"><span class="tls-13__t">T+00:12:00</span><span class="tls-13__light" data-s="pending" aria-hidden="true"></span><span class="tls-13__ev">Orbit insertion burn</span><span class="tls-13__st">PEND</span></li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-13,
.tls-13 *,
.tls-13 *::before,
.tls-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-13 {
  min-height: 100vh;
  width: 100%;
  --tl-go: #4ade80;
  --tl-hold: #facc15;
  --tl-nogo: #f87171;
  --tl-ink: #d8e4d8;
  --tl-mut: #5c6b5c;
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
  background: #060a06;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-13__console {
  width: min(660px,100%);
  background: #0a120a;
  border: 1px solid #1c2b1c;
  border-radius: 8px;
  overflow: hidden;
  position: relative;
}

.tls-13__console::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(180deg,rgba(120,255,150,.03) 0 1px,transparent 1px 3px);
  pointer-events: none;
}

.tls-13__bar {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 20px;
  border-bottom: 1px solid #1c2b1c;
  font-size: 11px;
  letter-spacing: .14em;
  color: var(--tl-go);
}

.tls-13__clock {
  color: var(--tl-ink);
}

.tls-13__log {
  list-style: none;
  padding: 12px 20px 18px;
  display: flex;
  flex-direction: column;
}

.tls-13__row {
  display: grid;
  grid-template-columns: 10ch 14px 1fr 5ch;
  align-items: center;
  gap: 14px;
  padding-block: 9px;
  font-size: 12.5px;
}

.tls-13__row--past {
  opacity: .58;
}

.tls-13__t {
  text-align: right;
  color: var(--tl-mut);
  font-variant-numeric: tabular-nums;
}

.tls-13__row--past .tls-13__t {
  color: var(--tl-mut);
}

.tls-13__light {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.tls-13__light[data-s="go"] {
  background: var(--tl-go);
  box-shadow: 0 0 8px color-mix(in srgb,var(--tl-go),transparent 40%);
}

.tls-13__light[data-s="hold"] {
  background: var(--tl-hold);
  box-shadow: 0 0 8px color-mix(in srgb,var(--tl-hold),transparent 40%);
  animation: tls-13-blink 1s steps(1) infinite;
}

.tls-13__light[data-s="pending"] {
  background: transparent;
  border: 2px solid var(--tl-mut);
  box-shadow: none;
}

@keyframes tls-13-blink {
  50% {
    opacity: .25;
  }
}

.tls-13__ev {
  color: var(--tl-ink);
  letter-spacing: .02em;
}

.tls-13__st {
  text-align: right;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  color: var(--tl-go);
}

.tls-13__row .tls-13__light[data-s="hold"] ~ .tls-13__st {
  color: var(--tl-hold);
}

.tls-13__row .tls-13__light[data-s="pending"] ~ .tls-13__st {
  color: var(--tl-mut);
}

.tls-13__now {
  display: flex;
  align-items: center;
  gap: 10px;
  padding-block: 4px;
  color: var(--tl-go);
  font-size: 10px;
  letter-spacing: .2em;
}

.tls-13__now::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg,var(--tl-go),transparent);
}

@media (prefers-reduced-motion: reduce) {
  .tls-13__light[data-s="hold"] {
    animation: none;
  }
}

@media (max-width: 520px) {
  .tls-13__row {
    grid-template-columns: 9ch 12px 1fr;
    font-size: 11.5px;
  }

  .tls-13__st {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — column alignment is guaranteed by monospace ch grid tracks; status is triple-encoded (color, shape, text) so nothing depends on the blink or the hue. */
```
