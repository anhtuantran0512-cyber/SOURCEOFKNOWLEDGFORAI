---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/sparkline-draw-on-enter/"
title: "Sparkline Draw-On-Enter"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "An analytics card whose trendline draws itself, its area fill wipes in behind, and its end-point dot lands last — the classic SVG line-draw, but with the…"
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sparkline Draw-On-Enter
Source: https://codefronts.com/components/css-animated-cards/sparkline-draw-on-enter/

An analytics card whose trendline draws itself, its area fill wipes in behind, and its end-point dot lands last — the classic SVG line-draw, but with the pathLength trick that removes the getTotalLength() measuring step entirely. Pure CSS, three coordinated animations, and a live crosshair on hover.
## HTML
```html
<section class="ac-13" aria-label="Sparkline draw on enter demo">
  <div class="ac-13__stage">
    <article class="ac-13__card">
      <header class="ac-13__top">
        <div>
          <p class="ac-13__key">Weekly active users</p>
          <p class="ac-13__val">64,802 <span class="ac-13__delta">+9.1%</span></p>
        </div>
        <span class="ac-13__range">Last 9 weeks</span>
      </header>
      <div class="ac-13__chart">
        <svg class="ac-13__svg" viewBox="0 0 420 96" preserveAspectRatio="none" role="img" aria-labelledby="ac-13-t ac-13-d">
          <title id="ac-13-t">Weekly active users trend</title>
          <desc id="ac-13-d">Rising from 41,200 in week one to 64,802 in week nine, with a dip in week three.</desc>
          <defs>
            <linearGradient id="ac-13-g" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="oklch(0.78 0.16 258)" stop-opacity="0.42"/>
              <stop offset="100%" stop-color="oklch(0.78 0.16 258)" stop-opacity="0"/>
            </linearGradient>
          </defs>
          <path class="ac-13__area" d="M0 68 L52.5 60 L105 74 L157.5 52 L210 58 L262.5 38 L315 44 L367.5 22 L420 12 L420 96 L0 96 Z" fill="url(#ac-13-g)"/>
          <path class="ac-13__line" pathLength="100" d="M0 68 L52.5 60 L105 74 L157.5 52 L210 58 L262.5 38 L315 44 L367.5 22 L420 12"/>
        </svg>
        <span class="ac-13__dot" aria-hidden="true"></span>
        <div class="ac-13__cols" aria-hidden="true">
          <span style="--ac-13-y:68"><b>41.2k</b></span><span style="--ac-13-y:60"><b>44.8k</b></span><span style="--ac-13-y:74"><b>38.9k</b></span>
          <span style="--ac-13-y:52"><b>49.6k</b></span><span style="--ac-13-y:58"><b>46.1k</b></span><span style="--ac-13-y:38"><b>55.4k</b></span>
          <span style="--ac-13-y:44"><b>52.0k</b></span><span style="--ac-13-y:22"><b>61.3k</b></span><span style="--ac-13-y:12"><b>64.8k</b></span>
        </div>
      </div>
      <footer class="ac-13__foot">
        <span class="ac-13__wk">W1</span><span class="ac-13__wk">W5</span><span class="ac-13__wk">W9</span>
      </footer>
    </article>
    <p class="ac-13__chip" aria-hidden="true">pathLength=&quot;100&quot; · stroke-dashoffset draw · clip-path area wipe · :has() hover readout · role=img + desc</p>
  </div>
</section>
```
## CSS
```css
.ac-13,
.ac-13 *,
.ac-13 *::before,
.ac-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-13-bg: oklch(0.17 0.017 268);
  --ac-13-card: oklch(0.22 0.02 268);
  --ac-13-ink: oklch(0.97 0.004 260);
  --ac-13-mut: oklch(0.69 0.02 268);
  --ac-13-acc: oklch(0.78 0.16 258);
  --ac-13-line: oklch(1 0 0/.11);
  background: var(--ac-13-bg);
  color: var(--ac-13-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 16px;
  padding: clamp(20px,5vw,58px);
  background: radial-gradient(90% 60% at 50% 0%,color-mix(in oklch,var(--ac-13-acc) 12%,transparent),transparent 62%);
}

.ac-13__card {
  width: min(100%,460px);
  display: grid;
  gap: 16px;
  padding: 20px;
  border: 1px solid var(--ac-13-line);
  border-radius: 22px;
  background: var(--ac-13-card);
  box-shadow: 0 34px 70px -44px oklch(0 0 0/.9);
  animation: ac-13-in .8s cubic-bezier(.16,1,.3,1) both;
}

@keyframes ac-13-in {
  from {
    opacity: 0;
    transform: translateY(16px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.ac-13__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 14px;
}

.ac-13__key {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--ac-13-mut);
}

.ac-13__val {
  margin-top: 6px;
  font-size: 30px;
  font-weight: 700;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
  display: flex;
  align-items: baseline;
  gap: 9px;
}

.ac-13__delta {
  font-size: 12.5px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--ac-13-acc) 18%,transparent);
  color: var(--ac-13-acc);
  letter-spacing: 0;
  animation: ac-13-pill .6s cubic-bezier(.16,1,.3,1) 1.5s both;
}

@keyframes ac-13-pill {
  from {
    opacity: 0;
    transform: translateY(-5px) scale(.9);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.ac-13__range {
  flex: none;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--ac-13-mut);
  padding: 5px 10px;
  border: 1px solid var(--ac-13-line);
  border-radius: 99px;
}

.ac-13__chart {
  position: relative;
  height: 96px;
}

.ac-13__svg {
  width: 100%;
  height: 96px;
  display: block;
  overflow: visible;
}

.ac-13__line {
  fill: none;
  stroke: var(--ac-13-acc);
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 100;
  stroke-dashoffset: 100;
  animation: ac-13-draw 1.7s cubic-bezier(.55,0,.2,1) .15s forwards;
  filter: drop-shadow(0 3px 10px color-mix(in oklch,var(--ac-13-acc) 45%,transparent));
}

@keyframes ac-13-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.ac-13__area {
  clip-path: inset(0 100% 0 0);
  animation: ac-13-wipe 1.6s cubic-bezier(.55,0,.2,1) .33s forwards;
}

@keyframes ac-13-wipe {
  to {
    clip-path: inset(0 0 0 0);
  }
}

.ac-13__dot {
  position: absolute;
  left: 100%;
  top: 12.5%;
  translate: -50% -50%;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--ac-13-acc);
  box-shadow: 0 0 0 4px color-mix(in oklch,var(--ac-13-acc) 22%,transparent);
  scale: 0;
  animation: ac-13-land .55s cubic-bezier(.2,.7,.3,1) 1.55s forwards;
}

@keyframes ac-13-land {
  0% {
    scale: 0;
  }

  60% {
    scale: 1.4;
  }

  100% {
    scale: 1;
  }
}

.ac-13__cols {
  position: absolute;
  inset: 0;
  display: flex;
}

.ac-13__cols span {
  position: relative;
  flex: 1;
  cursor: crosshair;
}

.ac-13__cols span::before {
  content: '';
  position: absolute;
  left: 50%;
  top: calc(var(--ac-13-y) * 1%);
  width: 8px;
  height: 8px;
  margin: -4px 0 0 -4px;
  border-radius: 50%;
  background: var(--ac-13-ink);
  opacity: 0;
  transition: opacity .18s,scale .18s;
  scale: .5;
}

.ac-13__cols span::after {
  content: '';
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 1px;
  background: linear-gradient(oklch(1 0 0/.28),transparent);
  opacity: 0;
  transition: opacity .18s;
}

.ac-13__cols span:hover::before,
.ac-13__cols span:hover::after {
  opacity: 1;
  scale: 1;
}

.ac-13__cols b {
  position: absolute;
  left: 50%;
  top: calc(var(--ac-13-y) * 1% - 34px);
  translate: -50% 4px;
  padding: 4px 9px;
  border-radius: 8px;
  background: oklch(0.98 0 0);
  color: oklch(0.2 0.02 268);
  font-size: 11.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity .18s,translate .18s;
}

.ac-13__cols span:hover b {
  opacity: 1;
  translate: -50% 0;
}

.ac-13__foot {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  color: var(--ac-13-mut);
}

.ac-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-13-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-13-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,700px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-13__line {
    animation: none;
    stroke-dashoffset: 0;
  }

  .ac-13__area {
    animation: none;
    clip-path: none;
  }

  .ac-13__dot {
    animation: none;
    scale: 1;
  }

  .ac-13__card,
    .ac-13__delta {
    animation-duration: 1ms;
  }
}
```
