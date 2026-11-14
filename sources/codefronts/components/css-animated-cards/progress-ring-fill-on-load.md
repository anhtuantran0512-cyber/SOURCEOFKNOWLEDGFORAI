---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/progress-ring-fill-on-load/"
title: "Progress Ring Fill on Load"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Circular progress done two ways, side by side: a conic-gradient ring animated with a registered @property angle (no SVG at all), and the classic SVG…"
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Progress Ring Fill on Load
Source: https://codefronts.com/components/css-animated-cards/progress-ring-fill-on-load/

Circular progress done two ways, side by side: a conic-gradient ring animated with a registered @property angle (no SVG at all), and the classic SVG stroke-dasharray arc. Both fill on load with an ease that decelerates into the target, both carry role="meter" with real values, and both re-theme from a single hue token.
## HTML
```html
<section class="ac-14" aria-label="Progress ring fill on load demo">
  <div class="ac-14__stage">
    <header class="ac-14__head">
      <p class="ac-14__eyebrow">Two routes, same ring</p>
      <h2 class="ac-14__title">Circular progress that fills on load</h2>
    </header>
    <div class="ac-14__grid">
      <article class="ac-14__card">
        <div class="ac-14__wrap" role="meter" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100" aria-label="Storage used, 72 percent">
          <span class="ac-14__ring" aria-hidden="true"></span>
          <span class="ac-14__hole ac-14__hole--abs"><b class="ac-14__n" aria-hidden="true"></b><i class="ac-14__pct" aria-hidden="true">%</i></span>
        </div>
        <div class="ac-14__meta"><h3 class="ac-14__name">Storage used</h3><p class="ac-14__sub">1.44 TB of 2 TB · conic-gradient + @property</p></div>
      </article>
      <article class="ac-14__card">
        <div class="ac-14__svgwrap" role="meter" aria-valuenow="66" aria-valuemin="0" aria-valuemax="100" aria-label="Course completion, 66 percent">
          <svg viewBox="0 0 120 120" class="ac-14__svg" aria-hidden="true">
            <circle class="ac-14__track" cx="60" cy="60" r="50"/>
            <circle class="ac-14__arc" cx="60" cy="60" r="50" pathLength="100"/>
          </svg>
          <span class="ac-14__hole ac-14__hole--abs"><b class="ac-14__n2" aria-hidden="true"></b><i class="ac-14__pct">%</i></span>
        </div>
        <div class="ac-14__meta"><h3 class="ac-14__name">Course completion</h3><p class="ac-14__sub">22 of 33 lessons · SVG stroke-dasharray</p></div>
      </article>
      <article class="ac-14__card">
        <div class="ac-14__wrap" role="meter" aria-valuenow="41" aria-valuemin="0" aria-valuemax="100" aria-label="Monthly goal, 41 percent">
          <span class="ac-14__ring ac-14__ring--alt" aria-hidden="true"></span>
          <span class="ac-14__hole ac-14__hole--abs"><b class="ac-14__n3" aria-hidden="true"></b><i class="ac-14__pct" aria-hidden="true">%</i></span>
        </div>
        <div class="ac-14__meta"><h3 class="ac-14__name">Monthly goal</h3><p class="ac-14__sub">$8,200 of $20,000 · segmented mask</p></div>
      </article>
    </div>
    <p class="ac-14__chip" aria-hidden="true">@property &lt;angle&gt; · conic-gradient sweep · radial mask donut · pathLength circle · role=meter</p>
  </div>
</section>
```
## CSS
```css
@property --ac-14-ang {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@property --ac-14-ang3 {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@property --ac-14-a {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --ac-14-b {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --ac-14-c {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.ac-14,
.ac-14 *,
.ac-14 *::before,
.ac-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-14-bg: oklch(0.16 0.014 285);
  --ac-14-card: oklch(0.21 0.017 285);
  --ac-14-ink: oklch(0.97 0.004 280);
  --ac-14-mut: oklch(0.69 0.02 285);
  --ac-14-acc: oklch(0.75 0.17 300);
  --ac-14-track: oklch(1 0 0/.09);
  --ac-14-line: oklch(1 0 0/.11);
  background: var(--ac-14-bg);
  color: var(--ac-14-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.6vw,28px);
  padding: clamp(20px,5vw,58px);
  background: radial-gradient(90% 60% at 50% 0%,color-mix(in oklch,var(--ac-14-acc) 12%,transparent),transparent 62%);
}

.ac-14__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.ac-14__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-14-acc);
}

.ac-14__title {
  font-size: clamp(22px,3.2vw,36px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-14__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
  gap: 14px;
  width: min(100%,860px);
}

.ac-14__card {
  display: grid;
  justify-items: center;
  gap: 15px;
  padding: 22px 18px;
  border: 1px solid var(--ac-14-line);
  border-radius: 20px;
  background: var(--ac-14-card);
  text-align: center;
  animation: ac-14-rise .8s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--ac-14-i,0) * 110ms);
}

.ac-14__card:nth-child(2) {
  --ac-14-i: 1;
}

.ac-14__card:nth-child(3) {
  --ac-14-i: 2;
}

@keyframes ac-14-rise {
  from {
    opacity: 0;
    transform: translateY(16px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.ac-14__wrap {
  position: relative;
  display: grid;
  place-items: center;
  width: 132px;
  height: 132px;
}

.ac-14__ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(from 0deg,var(--ac-14-acc) var(--ac-14-ang),var(--ac-14-track) 0);
  -webkit-mask: radial-gradient(farthest-side,transparent 67%,#000 68%);
  mask: radial-gradient(farthest-side,transparent 67%,#000 68%);
  animation: ac-14-fill 1.7s cubic-bezier(.16,1,.3,1) .2s both;
}

@keyframes ac-14-fill {
  from {
    --ac-14-ang: 0deg;
  }

  to {
    --ac-14-ang: 259deg;
  }
}

.ac-14__ring--alt {
  background: conic-gradient(from 0deg,oklch(0.82 0.16 88) var(--ac-14-ang3),var(--ac-14-track) 0);
  -webkit-mask: radial-gradient(farthest-side,transparent 67%,#000 68%) ,repeating-conic-gradient(#000 0 8deg,transparent 8deg 10deg);
  mask: radial-gradient(farthest-side,transparent 67%,#000 68%),repeating-conic-gradient(#000 0 8deg,transparent 8deg 10deg);
  -webkit-mask-composite: source-in;
  mask-composite: intersect;
  animation: ac-14-fill3 1.7s cubic-bezier(.16,1,.3,1) .42s both;
}

@keyframes ac-14-fill3 {
  from {
    --ac-14-ang3: 0deg;
  }

  to {
    --ac-14-ang3: 148deg;
  }
}

.ac-14__hole {
  position: absolute;
  display: grid;
  grid-auto-flow: column;
  place-content: center;
  justify-items: center;
  align-items: baseline;
  gap: 1px;
  font-variant-numeric: tabular-nums;
  font-weight: 700;
  letter-spacing: -.04em;
  line-height: 1;
}

.ac-14__hole--abs {
  inset: 0;
}

.ac-14__n,
.ac-14__n2,
.ac-14__n3 {
  font-size: 32px;
}

.ac-14__pct {
  font-style: normal;
  font-size: 15px;
  color: var(--ac-14-mut);
  font-weight: 640;
}

.ac-14__n {
  counter-reset: ac-14-a var(--ac-14-a);
  animation: ac-14-ka 1.7s cubic-bezier(.16,1,.3,1) .2s both;
}

.ac-14__n::after {
  content: counter(ac-14-a);
}

.ac-14__n2 {
  counter-reset: ac-14-b var(--ac-14-b);
  animation: ac-14-kb 1.7s cubic-bezier(.16,1,.3,1) .31s both;
}

.ac-14__n2::after {
  content: counter(ac-14-b);
}

.ac-14__n3 {
  counter-reset: ac-14-c var(--ac-14-c);
  animation: ac-14-kc 1.7s cubic-bezier(.16,1,.3,1) .42s both;
}

.ac-14__n3::after {
  content: counter(ac-14-c);
}

@keyframes ac-14-ka {
  from {
    --ac-14-a: 0;
  }

  to {
    --ac-14-a: 72;
  }
}

@keyframes ac-14-kb {
  from {
    --ac-14-b: 0;
  }

  to {
    --ac-14-b: 66;
  }
}

@keyframes ac-14-kc {
  from {
    --ac-14-c: 0;
  }

  to {
    --ac-14-c: 41;
  }
}

.ac-14__svgwrap {
  position: relative;
  display: grid;
  place-items: center;
  width: 132px;
  height: 132px;
}

.ac-14__svg {
  width: 132px;
  height: 132px;
  rotate: -90deg;
}

.ac-14__track {
  fill: none;
  stroke: var(--ac-14-track);
  stroke-width: 11;
}

.ac-14__arc {
  fill: none;
  stroke: oklch(0.80 0.15 195);
  stroke-width: 11;
  stroke-linecap: round;
  stroke-dasharray: 100;
  stroke-dashoffset: 100;
  animation: ac-14-arc 1.7s cubic-bezier(.16,1,.3,1) .31s forwards;
  filter: drop-shadow(0 0 8px color-mix(in oklch,oklch(0.80 0.15 195) 45%,transparent));
}

@keyframes ac-14-arc {
  to {
    stroke-dashoffset: 34;
  }
}

.ac-14__meta {
  display: grid;
  gap: 4px;
}

.ac-14__name {
  font-size: 15px;
  font-weight: 640;
  letter-spacing: -.02em;
}

.ac-14__sub {
  font-size: 11.5px;
  color: var(--ac-14-mut);
  font-variant-numeric: tabular-nums;
  text-wrap: pretty;
}

.ac-14__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-14-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-14-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,700px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-14 * {
    animation-duration: 1ms !important;
  }
}
```
