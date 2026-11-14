---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/aurora-drift/"
title: "CSS Footer with Animated Gradient Background"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "A footer that breathes: a slow mesh of coloured light drifting behind the content, built from registered custom properties so the gradient itself animates…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Footer with Animated Gradient Background
Source: https://codefronts.com/layouts/css-footer-designs/aurora-drift/

A footer that breathes: a slow mesh of coloured light drifting behind the content, built from registered custom properties so the gradient itself animates instead of the old trick of sliding an oversized background-position. Roughly 1KB, no images, no canvas, and it stops dead under prefers-reduced-motion.
## HTML
```html
<section class="ft-11" aria-label="Animated gradient background footer demo">
  <main class="ft-11__main">
    <p class="ft-11__eyebrow">@property · conic-gradient · feTurbulence</p>
    <h1 class="ft-11__title">Light that moves, text that doesn't flicker</h1>
    <p class="ft-11__sub">A registered angle property makes the gradient itself animate. Three drifting blobs on coprime durations keep it from looping visibly, and a grain layer kills the banding.</p>
  </main>
  <footer class="ft-11__foot">
    <div class="ft-11__aurora" aria-hidden="true"><span></span><span></span><span></span></div>
    <div class="ft-11__grain" aria-hidden="true"></div>
    <div class="ft-11__content">
      <div class="ft-11__lead">
        <div class="ft-11__brand"><span class="ft-11__mark" aria-hidden="true"></span>Nocturne</div>
        <p class="ft-11__blurb">Sound design and generative visuals for people who build strange, beautiful things on the internet.</p>
        <a class="ft-11__cta" href="#ft-11-a">Start a project<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
      </div>
      <nav class="ft-11__col" aria-labelledby="ft-11-c1"><h2 class="ft-11__ch" id="ft-11-c1">Studio</h2><ul class="ft-11__list"><li><a class="ft-11__link" href="#ft-11-a">Work</a></li><li><a class="ft-11__link" href="#ft-11-a">Process</a></li><li><a class="ft-11__link" href="#ft-11-a">Team</a></li><li><a class="ft-11__link" href="#ft-11-a">Rates</a></li></ul></nav>
      <nav class="ft-11__col" aria-labelledby="ft-11-c2"><h2 class="ft-11__ch" id="ft-11-c2">Playground</h2><ul class="ft-11__list"><li><a class="ft-11__link" href="#ft-11-a">Shader garden</a></li><li><a class="ft-11__link" href="#ft-11-a">Field recordings</a></li><li><a class="ft-11__link" href="#ft-11-a">Open source</a></li></ul></nav>
      <nav class="ft-11__col" aria-labelledby="ft-11-c3"><h2 class="ft-11__ch" id="ft-11-c3">Elsewhere</h2><ul class="ft-11__list"><li><a class="ft-11__link" href="#ft-11-a">Instagram</a></li><li><a class="ft-11__link" href="#ft-11-a">Are.na</a></li><li><a class="ft-11__link" href="#ft-11-a">Newsletter</a></li></ul></nav>
    </div>
    <div class="ft-11__bar">
      <p class="ft-11__copy">© <time datetime="2026">2026</time> Nocturne Studio · Lisbon &amp; Montréal</p>
      <p class="ft-11__note">Motion pauses automatically when you prefer reduced motion.</p>
    </div>
  </footer>
</section>
```
## CSS
```css
@property --ft-11-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.ft-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-11-bg);
  --ft-11-bg: oklch(0.14 0.03 285);
  --ft-11-ink: oklch(0.97 0.01 285);
  --ft-11-mut: oklch(0.77 0.02 285);
  --ft-11-c1: oklch(0.6 0.22 295);
  --ft-11-c2: oklch(0.68 0.19 200);
  --ft-11-c3: oklch(0.66 0.21 345);
  --ft-11-line: oklch(0.97 0.01 285/.16);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-11-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-11 *,
.ft-11 *::before,
.ft-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-11 ul {
  list-style: none;
}

.ft-11__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(40px,8vh,90px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1160px)/2));
}

.ft-11__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-11-c2);
}

.ft-11__title {
  font-size: clamp(29px,5.4vw,58px);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-11__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-11-mut);
  max-width: 58ch;
  text-wrap: pretty;
}

.ft-11__foot {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  background: conic-gradient(from var(--ft-11-angle) at 30% 120%,var(--ft-11-c1),var(--ft-11-c2),var(--ft-11-c3),var(--ft-11-c1));
  animation: ft-11-spin 22s linear infinite;
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1160px)/2));
}

@keyframes ft-11-spin {
  to {
    --ft-11-angle: 360deg;
  }
}

.ft-11__foot::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(180deg,oklch(0.14 0.03 285/.72),oklch(0.14 0.03 285/.9));
}

.ft-11__aurora {
  position: absolute;
  inset: -20%;
  z-index: -2;
  filter: blur(60px);
}

.ft-11__aurora span {
  position: absolute;
  border-radius: 50%;
  opacity: .55;
  mix-blend-mode: screen;
}

.ft-11__aurora span:nth-child(1) {
  width: 46%;
  height: 120%;
  left: 4%;
  top: -30%;
  background: radial-gradient(circle,var(--ft-11-c1),transparent 68%);
  animation: ft-11-d1 17s ease-in-out infinite alternate;
}

.ft-11__aurora span:nth-child(2) {
  width: 52%;
  height: 130%;
  left: 38%;
  top: -10%;
  background: radial-gradient(circle,var(--ft-11-c2),transparent 66%);
  animation: ft-11-d2 23s ease-in-out infinite alternate;
}

.ft-11__aurora span:nth-child(3) {
  width: 40%;
  height: 110%;
  left: 66%;
  top: -24%;
  background: radial-gradient(circle,var(--ft-11-c3),transparent 68%);
  animation: ft-11-d3 31s ease-in-out infinite alternate;
}

@keyframes ft-11-d1 {
  to {
    transform: translate3d(14%,8%,0) scale(1.18);
  }
}

@keyframes ft-11-d2 {
  to {
    transform: translate3d(-16%,-6%,0) scale(1.1);
  }
}

@keyframes ft-11-d3 {
  to {
    transform: translate3d(10%,-10%,0) scale(1.22);
  }
}

.ft-11__grain {
  position: absolute;
  inset: 0;
  z-index: -1;
  opacity: .05;
  mix-blend-mode: overlay;
  pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23n)'/%3E%3C/svg%3E");
}

.ft-11__content {
  position: relative;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: clamp(26px,3.4vw,42px) clamp(18px,2.4vw,32px);
  padding-block: clamp(34px,5vw,60px);
}

.ft-11__lead {
  display: grid;
  align-content: start;
  gap: 14px;
  min-width: 0;
  grid-column: span 2;
}

.ft-11__brand {
  display: flex;
  align-items: center;
  gap: 11px;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -.03em;
}

.ft-11__mark {
  width: 26px;
  height: 26px;
  border-radius: 9px;
  background: conic-gradient(from 40deg,var(--ft-11-c1),var(--ft-11-c2),var(--ft-11-c3),var(--ft-11-c1));
  box-shadow: 0 0 26px -4px var(--ft-11-c1);
}

.ft-11__blurb {
  font-size: 14.6px;
  line-height: 1.6;
  color: var(--ft-11-mut);
  max-width: 34ch;
  text-wrap: pretty;
}

.ft-11__cta {
  display: inline-flex;
  align-items: center;
  justify-self: start;
  gap: 9px;
  min-height: 46px;
  padding: 0 20px;
  border-radius: 99px;
  background: oklch(0.97 0.01 285);
  color: oklch(0.16 0.03 285);
  font-size: 14.5px;
  font-weight: 660;
  text-decoration: none;
  transition: transform .25s cubic-bezier(.34,1.56,.64,1),box-shadow .25s ease;
}

.ft-11__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 30px -14px oklch(0.97 0.01 285/.8);
}

.ft-11__cta:hover svg {
  translate: 3px 0;
}

.ft-11__cta svg {
  transition: translate .25s ease;
}

.ft-11__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-11__ch {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  margin-block-end: 8px;
  color: var(--ft-11-ink);
}

.ft-11__list {
  display: grid;
  gap: 1px;
}

.ft-11__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14.2px;
  color: var(--ft-11-mut);
  text-decoration: none;
  width: fit-content;
  position: relative;
  transition: color .2s ease;
}

.ft-11__link::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 7px;
  width: 100%;
  height: 1px;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .3s cubic-bezier(.2,.8,.2,1);
}

.ft-11__link:hover {
  color: var(--ft-11-ink);
}

.ft-11__link:hover::after {
  transform: scaleX(1);
}

.ft-11__link:focus-visible,
.ft-11__cta:focus-visible {
  outline: 2px solid var(--ft-11-ink);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-11__bar {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px 22px;
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-11-line);
}

.ft-11__copy,
.ft-11__note {
  font-size: 12.6px;
  color: var(--ft-11-mut);
}

.ft-11__note {
  margin-inline-start: auto;
}

@media (max-width: 700px) {
  .ft-11__lead {
    grid-column: auto;
  }

  .ft-11__note {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-11__foot {
    animation: none;
    --ft-11-angle: 140deg;
  }

  .ft-11__aurora span {
    animation: none;
  }

  .ft-11 * {
    transition-duration: .01ms !important;
  }
}
```
