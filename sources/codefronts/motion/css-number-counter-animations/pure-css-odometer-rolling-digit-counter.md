---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/pure-css-odometer-rolling-digit-counter/"
title: "Pure CSS Odometer Rolling Digit Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A mechanical odometer with no JavaScript at all: six digit columns, each a 0–9 strip translated by its own keyframe animation, with per-column durations in a…"
has_js: "false"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Odometer Rolling Digit Counter
Source: https://codefronts.com/motion/css-number-counter-animations/pure-css-odometer-rolling-digit-counter/

A mechanical odometer with no JavaScript at all: six digit columns, each a 0–9 strip translated by its own keyframe animation, with per-column durations in a 10:1 cascade so the units wheel spins ten times faster than the tens — the actual gearing of a physical counter. The blur streak on fast columns and the metal gradient sell the illusion.
## HTML
```html
<section class="cnc-08" aria-label="Pure CSS odometer rolling digit counter demo">
  <div class="cnc-08__stage">
    <p class="cnc-08__title">Total distance logged</p>
    <div class="cnc-08__meter" aria-hidden="true">
      <span class="cnc-08__col" style="--cnc-08-dur:640s"><span class="cnc-08__strip"><i>0</i><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i><i>0</i></span></span>
      <span class="cnc-08__col" style="--cnc-08-dur:64s"><span class="cnc-08__strip"><i>0</i><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i><i>0</i></span></span>
      <span class="cnc-08__col" style="--cnc-08-dur:6.4s"><span class="cnc-08__strip"><i>0</i><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i><i>0</i></span></span>
      <span class="cnc-08__sep">,</span>
      <span class="cnc-08__col" style="--cnc-08-dur:2.4s"><span class="cnc-08__strip"><i>0</i><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i><i>0</i></span></span>
      <span class="cnc-08__col" style="--cnc-08-dur:.9s"><span class="cnc-08__strip"><i>0</i><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i><i>0</i></span></span>
      <span class="cnc-08__col cnc-08__col--fast" style="--cnc-08-dur:.32s"><span class="cnc-08__strip"><i>0</i><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i><i>0</i></span></span>
      <span class="cnc-08__unit">km</span>
    </div>
    <p class="cnc-08__sr">Approximately 138,402 kilometres logged</p>
    <p class="cnc-08__chip" aria-hidden="true">10 : 1 gearing per place value · steps(10,end) · translateY(-100%) loop · zero JS</p>
  </div>
</section>
```
## CSS
```css
.cnc-08,
.cnc-08 *,
.cnc-08 *::before,
.cnc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-08-bg: oklch(0.14 0.012 60);
  --cnc-08-face: oklch(0.24 0.015 60);
  --cnc-08-ink: oklch(0.96 0.01 85);
  --cnc-08-mut: oklch(0.64 0.02 70);
  --cnc-08-acc: oklch(0.82 0.15 75);
  background: var(--cnc-08-bg);
  color: var(--cnc-08-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,48px);
  background: radial-gradient(60% 50% at 50% 40%,oklch(0.28 0.03 70/.6),transparent 72%);
}

.cnc-08__title {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--cnc-08-mut);
}

.cnc-08__meter {
  display: flex;
  align-items: center;
  gap: 3px;
  padding: 16px 18px;
  border-radius: 14px;
  background: linear-gradient(180deg,oklch(0.3 0.015 60),oklch(0.18 0.012 60));
  box-shadow: inset 0 2px 0 oklch(1 0 0/.12),inset 0 -2px 6px oklch(0 0 0/.6),0 22px 50px oklch(0 0 0/.55);
  font-size: clamp(38px,8vw,64px);
  font-weight: 700;
  letter-spacing: .02em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-08__col {
  position: relative;
  display: block;
  height: 1em;
  width: .66em;
  overflow: hidden;
  border-radius: 4px;
  background: linear-gradient(180deg,oklch(0.1 0.01 60),oklch(0.2 0.012 60) 45%,oklch(0.08 0.01 60));
  box-shadow: inset 0 0 0 1px oklch(0 0 0/.6);
}

.cnc-08__col::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(180deg,oklch(0 0 0/.75),transparent 26%,transparent 74%,oklch(0 0 0/.75));
}

.cnc-08__strip {
  display: block;
  animation: cnc-08-roll var(--cnc-08-dur,1s) steps(10,end) infinite;
  will-change: transform;
}

.cnc-08__col--fast .cnc-08__strip {
  animation-timing-function: linear;
  filter: blur(.4px);
}

.cnc-08__strip i {
  display: block;
  height: 1em;
  line-height: 1;
  font-style: normal;
  text-align: center;
  color: var(--cnc-08-ink);
  text-shadow: 0 1px 0 oklch(0 0 0/.8);
}

@keyframes cnc-08-roll {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-100%);
  }
}

.cnc-08__sep {
  color: var(--cnc-08-acc);
  padding: 0 2px;
  transform: translateY(.12em);
}

.cnc-08__unit {
  margin-left: 10px;
  font-size: .32em;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--cnc-08-acc);
}

.cnc-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-08__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-08-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,480px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-08__strip {
    animation: none;
  }

  .cnc-08__col--fast .cnc-08__strip {
    filter: none;
  }
}
```
