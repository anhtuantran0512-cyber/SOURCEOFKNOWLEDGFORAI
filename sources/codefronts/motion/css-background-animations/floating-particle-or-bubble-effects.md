---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/floating-particle-or-bubble-effects/"
title: "Floating Bubble Background"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Soap bubbles, not circles."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Bubble Background
Source: https://codefronts.com/motion/css-background-animations/floating-particle-or-bubble-effects/

Soap bubbles, not circles. Each one gets an iridescent conic film, a bright specular kiss at the upper left, a thin refractive rim, and a wobble that deforms it slightly as it rises — because a real bubble is a flexible membrane, not a rigid ball. Sizes, speeds and horizontal sway all derive from one inline value per bubble.
## HTML
```html
<section class="bga-24" aria-label="Floating bubble background demo">
  <div class="bga-24__water" aria-hidden="true"></div>
  <div class="bga-24__caust" aria-hidden="true"></div>

  <div class="bga-24__field" aria-hidden="true">
    <span style="--bga-24-x:6%;--bga-24-s:74px;--bga-24-t:19s;--bga-24-d:-3s"></span>
    <span style="--bga-24-x:15%;--bga-24-s:32px;--bga-24-t:13s;--bga-24-d:-9s"></span>
    <span style="--bga-24-x:23%;--bga-24-s:112px;--bga-24-t:26s;--bga-24-d:-16s"></span>
    <span style="--bga-24-x:31%;--bga-24-s:46px;--bga-24-t:16s;--bga-24-d:-6s"></span>
    <span style="--bga-24-x:39%;--bga-24-s:88px;--bga-24-t:23s;--bga-24-d:-19s"></span>
    <span style="--bga-24-x:47%;--bga-24-s:26px;--bga-24-t:11s;--bga-24-d:-2s"></span>
    <span style="--bga-24-x:55%;--bga-24-s:140px;--bga-24-t:31s;--bga-24-d:-24s"></span>
    <span style="--bga-24-x:63%;--bga-24-s:58px;--bga-24-t:18s;--bga-24-d:-11s"></span>
    <span style="--bga-24-x:71%;--bga-24-s:38px;--bga-24-t:14s;--bga-24-d:-7s"></span>
    <span style="--bga-24-x:79%;--bga-24-s:96px;--bga-24-t:27s;--bga-24-d:-21s"></span>
    <span style="--bga-24-x:87%;--bga-24-s:52px;--bga-24-t:17s;--bga-24-d:-13s"></span>
    <span style="--bga-24-x:95%;--bga-24-s:68px;--bga-24-t:21s;--bga-24-d:-5s"></span>
    <span style="--bga-24-x:11%;--bga-24-s:22px;--bga-24-t:10s;--bga-24-d:-4s"></span>
    <span style="--bga-24-x:43%;--bga-24-s:64px;--bga-24-t:24s;--bga-24-d:-17s"></span>
    <span style="--bga-24-x:67%;--bga-24-s:30px;--bga-24-t:12s;--bga-24-d:-8s"></span>
    <span style="--bga-24-x:83%;--bga-24-s:120px;--bga-24-t:29s;--bga-24-d:-26s"></span>
  </div>

  <div class="bga-24__stage">
    <div class="bga-24__card">
      <p class="bga-24__eyebrow">Membranes · 24</p>
      <h1 class="bga-24__title">A bubble is a film,<br>not a ball.</h1>
      <p class="bga-24__sub">Conic iridescence, one specular kiss, a refractive rim — and a two-percent wobble that makes it flexible. Negative delays start the field mid-flight.</p>
      <div class="bga-24__notes">
        <span>conic film · alpha &lt; .3</span>
        <span>wobble 48% / 52%</span>
        <span>negative delays</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-24,
.bga-24 *,
.bga-24 *::before,
.bga-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-24-bg: oklch(0.3 0.08 236);
  background: var(--bga-24-bg);
  color: oklch(0.98 0.008 220);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-24__water {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,oklch(0.52 0.12 214) 0%,oklch(0.34 0.1 232) 46%,oklch(0.19 0.07 248) 100%);
}

.bga-24__caust {
  position: absolute;
  inset: -10%;
  opacity: .2;
  mix-blend-mode: screen;
  filter: blur(14px);
  background: repeating-radial-gradient(circle at 30% 10%,transparent 0 30px,oklch(0.95 0.05 200/.5) 30px 33px), repeating-radial-gradient(circle at 72% 4%,transparent 0 44px,oklch(0.9 0.06 190/.4) 44px 47px);
  animation: bga-24-caust 30s ease-in-out infinite alternate;
}

@keyframes bga-24-caust {
  to {
    translate: 2% 3%;
    scale: 1.08;
  }
}

.bga-24__field {
  position: absolute;
  inset: 0;
}

.bga-24__field span {
  position: absolute;
  left: var(--bga-24-x);
  bottom: -24vh;
  width: var(--bga-24-s);
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 26%,oklch(1 0 0/.78) 0 5%,oklch(1 0 0/.22) 14%,transparent 30%), conic-gradient(from 200deg,
        oklch(0.82 0.14 200/.26),oklch(0.86 0.13 320/.3),
        oklch(0.9 0.12 90/.24),oklch(0.84 0.14 160/.28),oklch(0.82 0.14 200/.26));
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.38),inset -8px -11px 22px oklch(1 0 0/.15), inset 8px 10px 24px oklch(0.4 0.08 240/.2),0 0 22px -6px oklch(0.9 0.06 200/.4);
  animation: bga-24-rise var(--bga-24-t) linear infinite, bga-24-sway calc(var(--bga-24-t) * .37) ease-in-out infinite alternate, bga-24-wobble calc(var(--bga-24-t) * .21) ease-in-out infinite alternate;
  animation-delay: var(--bga-24-d,0s),var(--bga-24-d,0s),0s;
}

@keyframes bga-24-rise {
  to {
    translate: 0 -140vh;
  }
}

@keyframes bga-24-sway {
  from {
    margin-left: -4vw;
  }

  to {
    margin-left: 4vw;
  }
}

@keyframes bga-24-wobble {
  from {
    border-radius: 48% 52% 53% 47%;
    scale: 1.02 .98;
  }

  to {
    border-radius: 53% 47% 48% 52%;
    scale: .98 1.02;
  }
}

.bga-24__stage {
  position: relative;
  z-index: 4;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-24__card {
  width: min(100%,650px);
  display: grid;
  gap: 15px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 28px;
  background: oklch(0.22 0.06 238/.42);
  border: 1px solid oklch(1 0 0/.18);
  backdrop-filter: blur(22px) saturate(1.5);
  -webkit-backdrop-filter: blur(22px) saturate(1.5);
  box-shadow: 0 44px 100px -52px oklch(0.1 0.04 240/.9),inset 0 1px 0 oklch(1 0 0/.28);
}

.bga-24__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.9 0.1 195);
}

.bga-24__title {
  font-size: clamp(26px,5.2vw,52px);
  font-weight: 620;
  line-height: 1.04;
  letter-spacing: -.05em;
  text-wrap: balance;
}

.bga-24__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.95 0.01 220/.8);
  text-wrap: pretty;
}

.bga-24__notes {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 6px;
}

.bga-24__notes span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 7px 13px;
  border-radius: 99px;
  color: oklch(1 0 0/.7);
  background: oklch(1 0 0/.07);
  border: 1px solid oklch(1 0 0/.15);
}

@media (prefers-reduced-motion: reduce) {
  .bga-24__field span,
    .bga-24__caust {
    animation: none;
  }

  .bga-24__field span {
    bottom: auto;
    top: var(--bga-24-x);
  }
}
```
