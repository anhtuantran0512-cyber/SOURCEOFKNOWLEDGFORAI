---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/aurora-borealis-background-animation/"
title: "Aurora Borealis Glow Background"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Northern lights as light curtains, not blurred blobs."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Borealis Glow Background
Source: https://codefronts.com/motion/css-background-animations/aurora-borealis-background-animation/

Northern lights as light curtains, not blurred blobs. Each ribbon is a tall conic-gradient sheet, skewed, masked into a vertical falloff and blended with screen, so where two ribbons cross the colour genuinely adds — the way emission spectra do. They breathe on coprime periods above a starfield and a snow-lit horizon.
## HTML
```html
<section class="bga-15" aria-label="Aurora borealis glow background demo">
  <div class="bga-15__sky" aria-hidden="true"></div>
  <div class="bga-15__stars" aria-hidden="true"></div>
  <div class="bga-15__stars bga-15__stars--far" aria-hidden="true"></div>

  <div class="bga-15__curtains" aria-hidden="true">
    <span class="bga-15__ribbon" style="--bga-15-c:oklch(0.84 0.2 152);--bga-15-x:-14%;--bga-15-d:34s;--bga-15-b:19s;--bga-15-w:27s"></span>
    <span class="bga-15__ribbon" style="--bga-15-c:oklch(0.78 0.18 196);--bga-15-x:18%;--bga-15-d:41s;--bga-15-b:23s;--bga-15-w:31s"></span>
    <span class="bga-15__ribbon" style="--bga-15-c:oklch(0.68 0.2 292);--bga-15-x:46%;--bga-15-d:29s;--bga-15-b:17s;--bga-15-w:37s"></span>
    <span class="bga-15__ribbon" style="--bga-15-c:oklch(0.72 0.19 18);--bga-15-x:72%;--bga-15-d:47s;--bga-15-b:21s;--bga-15-w:23s"></span>
  </div>

  <div class="bga-15__ridge" aria-hidden="true"></div>

  <div class="bga-15__stage">
    <div class="bga-15__copy">
      <p class="bga-15__eyebrow">Emissive layering · 15</p>
      <h1 class="bga-15__title">Light that adds<br>where it overlaps.</h1>
      <p class="bga-15__sub">Screen blending is the whole idea: two curtains crossing get brighter, never muddier — the same thing emission spectra do in the real sky.</p>
      <div class="bga-15__spectrum">
        <span style="--bga-15-s:oklch(0.84 0.2 152)">O₂ 557nm</span>
        <span style="--bga-15-s:oklch(0.78 0.18 196)">O₂ 630nm</span>
        <span style="--bga-15-s:oklch(0.68 0.2 292)">N₂ 428nm</span>
        <span style="--bga-15-s:oklch(0.72 0.19 18)">N₂⁺ arc</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-15,
.bga-15 *,
.bga-15 *::before,
.bga-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-15-bg: oklch(0.13 0.035 265);
  background: var(--bga-15-bg);
  color: oklch(0.97 0.01 220);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-15__sky {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,oklch(0.1 0.04 275) 0%,oklch(0.16 0.05 260) 52%,oklch(0.24 0.05 240) 100%);
}

.bga-15__stars {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(oklch(1 0 0/.9) .8px,transparent 1px),radial-gradient(oklch(0.9 0.04 220/.7) .6px,transparent .9px);
  background-size: 120px 120px,71px 71px;
  background-position: 0 0,32px 44px;
  animation: bga-15-twinkle 5.5s ease-in-out infinite alternate;
}

.bga-15__stars--far {
  opacity: .42;
  background-size: 53px 53px,89px 89px;
  animation-duration: 8.5s;
  animation-delay: -2s;
}

@keyframes bga-15-twinkle {
  from {
    opacity: .5;
  }

  to {
    opacity: .95;
  }
}

.bga-15__curtains {
  position: absolute;
  inset: -10% -20% 0;
  mix-blend-mode: screen;
}

.bga-15__ribbon {
  position: absolute;
  top: -16%;
  left: var(--bga-15-x);
  width: 64%;
  height: 96%;
  mix-blend-mode: screen;
  filter: blur(38px);
  opacity: .72;
  transform-origin: 50% 100%;
  background: conic-gradient(from 208deg at 50% 122%,transparent 0 6%,var(--bga-15-c) 17%,transparent 38%);
  -webkit-mask-image: linear-gradient(oklch(0 0 0) 0 30%,oklch(0 0 0/.35) 68%,transparent 94%);
  mask-image: linear-gradient(oklch(0 0 0) 0 30%,oklch(0 0 0/.35) 68%,transparent 94%);
  animation: bga-15-drift var(--bga-15-d) ease-in-out infinite alternate, bga-15-breathe var(--bga-15-b) ease-in-out infinite alternate, bga-15-wave var(--bga-15-w) ease-in-out infinite alternate;
}

@keyframes bga-15-drift {
  from {
    translate: -8% 0;
  }

  to {
    translate: 10% 0;
  }
}

@keyframes bga-15-breathe {
  from {
    scale: 1 .88;
    opacity: .5;
  }

  to {
    scale: 1.06 1.08;
    opacity: .85;
  }
}

@keyframes bga-15-wave {
  from {
    rotate: -5deg;
  }

  to {
    rotate: 6deg;
  }
}

.bga-15__ridge {
  position: absolute;
  inset-inline: -4%;
  inset-block-end: -2%;
  height: 26%;
  background: linear-gradient(180deg,transparent,oklch(0.22 0.03 250/.6) 40%,oklch(0.3 0.02 240/.9));
  -webkit-mask-image: radial-gradient(120% 100% at 20% 100%,oklch(0 0 0) 40%,transparent 72%),radial-gradient(100% 90% at 78% 100%,oklch(0 0 0) 44%,transparent 76%);
  mask-image: radial-gradient(120% 100% at 20% 100%,oklch(0 0 0) 40%,transparent 72%),radial-gradient(100% 90% at 78% 100%,oklch(0 0 0) 44%,transparent 76%);
  -webkit-mask-composite: source-over;
  mask-composite: add;
}

.bga-15__stage {
  position: relative;
  z-index: 4;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-15__copy {
  width: min(100%,660px);
  display: grid;
  gap: 16px;
  justify-items: center;
  text-align: center;
}

.bga-15__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.86 0.14 160);
}

.bga-15__title {
  font-size: clamp(30px,6.4vw,66px);
  font-weight: 600;
  line-height: 1;
  letter-spacing: -.05em;
  text-wrap: balance;
  text-shadow: 0 0 60px oklch(0.8 0.16 160/.35),0 4px 30px oklch(0.1 0.03 270/.7);
}

.bga-15__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.35vw,16.5px);
  line-height: 1.6;
  color: oklch(0.94 0.01 220/.8);
  text-wrap: pretty;
  text-shadow: 0 1px 16px oklch(0.1 0.03 270/.8);
}

.bga-15__spectrum {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 8px;
}

.bga-15__spectrum span {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 7px 13px;
  border-radius: 99px;
  color: oklch(1 0 0/.85);
  background: oklch(1 0 0/.07);
  border: 1px solid oklch(1 0 0/.16);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.bga-15__spectrum span::before {
  content: '';
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--bga-15-s);
  box-shadow: 0 0 12px -1px var(--bga-15-s);
}

@media (prefers-reduced-motion: reduce) {
  .bga-15__ribbon,
    .bga-15__stars {
    animation: none;
  }

  .bga-15__ribbon {
    opacity: .6;
  }
}
```
