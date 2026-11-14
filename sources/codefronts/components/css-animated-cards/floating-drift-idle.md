---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/floating-drift-idle/"
title: "Floating Drift Idle"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "A hero card that levitates: three layers drifting on different periods so the motion never visibly loops, a shadow that tightens as the card rises, and a…"
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Drift Idle
Source: https://codefronts.com/components/css-animated-cards/floating-drift-idle/

A hero card that levitates: three layers drifting on different periods so the motion never visibly loops, a shadow that tightens as the card rises, and a hover that lifts it out of the cycle without a jump. The trick is prime-ish durations (7 s, 9 s, 11 s) — their combined cycle is long enough that the eye never catches the repeat.
## HTML
```html
<section class="ac-16" aria-label="Floating drift idle card demo">
  <div class="ac-16__stage">
    <div class="ac-16__scene">
      <span class="ac-16__shadow" aria-hidden="true"></span>
      <div class="ac-16__lift">
        <article class="ac-16__card">
          <span class="ac-16__orb ac-16__orb--a" aria-hidden="true"></span>
          <span class="ac-16__orb ac-16__orb--b" aria-hidden="true"></span>
          <div class="ac-16__chiprow"><span class="ac-16__tag">Boarding pass</span><span class="ac-16__tag ac-16__tag--dim">Gate B12</span></div>
          <div class="ac-16__route">
            <div><b>LHR</b><i>London</i></div>
            <svg viewBox="0 0 60 20" width="60" height="20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M2 10h44" stroke-dasharray="3 5"/><path d="M40 4l8 6-8 6" fill="currentColor" stroke="none"/></svg>
            <div><b>SFO</b><i>San Francisco</i></div>
          </div>
          <dl class="ac-16__facts">
            <div><dt>Passenger</dt><dd>R. Okafor</dd></div>
            <div><dt>Seat</dt><dd>14A</dd></div>
            <div><dt>Boards</dt><dd>11:20</dd></div>
          </dl>
        </article>
      </div>
      <span class="ac-16__badge" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7L9 18l-5-5"/></svg>
        Checked in
      </span>
    </div>
    <p class="ac-16__chip" aria-hidden="true">coprime 7s / 9s / 11s cycles · negative animation-delay desync · anti-phase shadow · wrapper hover lift</p>
  </div>
</section>
```
## CSS
```css
.ac-16,
.ac-16 *,
.ac-16 *::before,
.ac-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-16-bg: oklch(0.18 0.02 245);
  --ac-16-card: oklch(0.97 0.008 250);
  --ac-16-ink: oklch(0.22 0.02 255);
  --ac-16-mut: oklch(0.53 0.02 255);
  --ac-16-acc: oklch(0.62 0.17 250);
  --ac-16-line: oklch(0.22 0.02 255/.12);
  background: radial-gradient(120% 90% at 50% 10%,oklch(0.26 0.045 250),var(--ac-16-bg) 70%);
  color: var(--ac-16-card);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 44px;
  padding: clamp(24px,6vw,64px);
}

.ac-16__scene {
  position: relative;
  width: min(100%,400px);
  padding-bottom: 26px;
}

.ac-16__shadow {
  position: absolute;
  left: 50%;
  bottom: 0;
  width: 64%;
  height: 22px;
  translate: -50% 0;
  border-radius: 50%;
  background: radial-gradient(closest-side,oklch(0 0 0/.62),transparent 74%);
  filter: blur(9px);
  animation: ac-16-shadow 7s ease-in-out infinite;
}

@keyframes ac-16-shadow {
  0%,
    100% {
    scale: 1;
    opacity: .55;
  }

  50% {
    scale: .85 .8;
    opacity: .28;
  }
}

.ac-16__lift {
  transition: translate .5s cubic-bezier(.16,1,.3,1);
}

.ac-16__scene:hover .ac-16__lift {
  translate: 0 -12px;
}

.ac-16__card {
  position: relative;
  display: grid;
  gap: 16px;
  padding: 22px;
  border-radius: 22px;
  background: var(--ac-16-card);
  color: var(--ac-16-ink);
  box-shadow: 0 30px 60px -34px oklch(0 0 0/.8);
  animation: ac-16-drift 7s ease-in-out infinite;
}

@keyframes ac-16-drift {
  0%,
    100% {
    translate: 0 0;
    rotate: 0deg;
  }

  50% {
    translate: 0 -11px;
    rotate: -.5deg;
  }
}

.ac-16__orb {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  filter: blur(1px);
}

.ac-16__orb--a {
  width: 66px;
  height: 66px;
  top: -30px;
  right: -22px;
  background: radial-gradient(circle at 32% 30%,oklch(0.85 0.16 88),oklch(0.66 0.19 42));
  box-shadow: 0 12px 26px -10px oklch(0.66 0.19 42/.8);
  animation: ac-16-drift 9s ease-in-out -2s infinite;
}

.ac-16__orb--b {
  width: 34px;
  height: 34px;
  bottom: -14px;
  left: -16px;
  background: radial-gradient(circle at 34% 30%,oklch(0.86 0.13 200),oklch(0.62 0.17 250));
  box-shadow: 0 10px 22px -8px oklch(0.62 0.17 250/.8);
  animation: ac-16-drift 11s ease-in-out -5s infinite;
}

.ac-16__chiprow {
  display: flex;
  gap: 7px;
  flex-wrap: wrap;
}

.ac-16__tag {
  padding: 5px 11px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--ac-16-acc) 14%,transparent);
  color: var(--ac-16-acc);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.ac-16__tag--dim {
  background: oklch(0.22 0.02 255/.07);
  color: var(--ac-16-mut);
}

.ac-16__route {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  color: var(--ac-16-mut);
}

.ac-16__route div {
  display: grid;
  gap: 2px;
}

.ac-16__route b {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -.03em;
  color: var(--ac-16-ink);
}

.ac-16__route i {
  font-style: normal;
  font-size: 11.5px;
  color: var(--ac-16-mut);
}

.ac-16__route div:last-child {
  text-align: right;
}

.ac-16__facts {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
  padding-top: 14px;
  border-top: 1px dashed var(--ac-16-line);
}

.ac-16__facts dt {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--ac-16-mut);
}

.ac-16__facts dd {
  margin-top: 3px;
  font-size: 14.5px;
  font-weight: 650;
  letter-spacing: -.015em;
  font-variant-numeric: tabular-nums;
}

.ac-16__badge {
  position: absolute;
  top: -16px;
  left: -10px;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 9px 14px;
  border-radius: 99px;
  background: oklch(0.72 0.17 152);
  color: oklch(0.18 0.03 152);
  font-size: 12px;
  font-weight: 700;
  box-shadow: 0 14px 28px -14px oklch(0.72 0.17 152/.9);
  animation: ac-16-drift 9s ease-in-out -3.5s infinite;
}

.ac-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: oklch(0.78 0.02 250);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,720px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-16__card,
    .ac-16__orb,
    .ac-16__badge,
    .ac-16__shadow {
    animation: none;
  }

  .ac-16__lift {
    transition: none;
  }
}
```
