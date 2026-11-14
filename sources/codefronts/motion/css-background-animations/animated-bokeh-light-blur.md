---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/animated-bokeh-light-blur/"
title: "Animated Bokeh Light Blur"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Out-of-focus lights drifting through a dark frame, with real optical logic: the nearer a light is, the larger, blurrier and faster it moves, and the more it…"
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Bokeh Light Blur
Source: https://codefronts.com/motion/css-background-animations/animated-bokeh-light-blur/

Out-of-focus lights drifting through a dark frame, with real optical logic: the nearer a light is, the larger, blurrier and faster it moves, and the more it overexposes to white in the centre. That single rule — size, blur, speed and core brightness all keyed to one depth token — is what separates convincing bokeh from a pile of blurred circles.
## HTML
```html
<section class="bga-09" aria-label="Animated bokeh light blur background demo">
  <div class="bga-09__dark" aria-hidden="true">
    <img class="bga-09__photo" src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?q=80&w=1800&auto=format&fit=crop" alt="" width="1800" height="1200" loading="lazy" decoding="async">
  </div>
  <div class="bga-09__lights" aria-hidden="true">
    <span style="--bga-09-d:.15;--bga-09-x:8%;--bga-09-y:74%;--bga-09-h:210"></span>
    <span style="--bga-09-d:.85;--bga-09-x:22%;--bga-09-y:30%;--bga-09-h:32"></span>
    <span style="--bga-09-d:.4;--bga-09-x:36%;--bga-09-y:86%;--bga-09-h:320"></span>
    <span style="--bga-09-d:.62;--bga-09-x:52%;--bga-09-y:18%;--bga-09-h:200"></span>
    <span style="--bga-09-d:.25;--bga-09-x:64%;--bga-09-y:62%;--bga-09-h:44"></span>
    <span style="--bga-09-d:.95;--bga-09-x:78%;--bga-09-y:44%;--bga-09-h:340"></span>
    <span style="--bga-09-d:.35;--bga-09-x:90%;--bga-09-y:78%;--bga-09-h:190"></span>
    <span style="--bga-09-d:.7;--bga-09-x:14%;--bga-09-y:54%;--bga-09-h:280"></span>
    <span style="--bga-09-d:.2;--bga-09-x:46%;--bga-09-y:48%;--bga-09-h:60"></span>
    <span style="--bga-09-d:.5;--bga-09-x:70%;--bga-09-y:88%;--bga-09-h:220"></span>
    <span style="--bga-09-d:.9;--bga-09-x:88%;--bga-09-y:14%;--bga-09-h:26"></span>
    <span style="--bga-09-d:.3;--bga-09-x:30%;--bga-09-y:8%;--bga-09-h:300"></span>
    <span style="--bga-09-d:.55;--bga-09-x:6%;--bga-09-y:20%;--bga-09-h:180"></span>
    <span style="--bga-09-d:.12;--bga-09-x:58%;--bga-09-y:70%;--bga-09-h:40"></span>
  </div>

  <div class="bga-09__stage">
    <div class="bga-09__frame">
      <p class="bga-09__eyebrow">Optics · 09</p>
      <h1 class="bga-09__title">One depth value.<br>Four correlated properties.</h1>
      <p class="bga-09__sub">Size, blur radius, opacity and orbital speed all derive from <code>--d</code>. Add a light by copying one span — the CSS never changes.</p>
      <div class="bga-09__scale" aria-hidden="true">
        <span>near</span>
        <i class="bga-09__ramp"></i>
        <span>far</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-09,
.bga-09 *,
.bga-09 *::before,
.bga-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-09-bg: oklch(0.15 0.03 274);
  background: var(--bga-09-bg);
  color: oklch(0.98 0.008 270);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-09__dark {
  position: absolute;
  inset: 0;
  background: radial-gradient(120% 100% at 50% 30%,oklch(0.24 0.06 285),oklch(0.11 0.03 270) 72%);
}

.bga-09__photo {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: .34;
  filter: blur(16px) saturate(1.25);
}

.bga-09__lights {
  position: absolute;
  inset: 0;
  animation: bga-09-hue 60s linear infinite;
}

@keyframes bga-09-hue {
  to {
    filter: hue-rotate(360deg);
  }
}

.bga-09__lights span {
  position: absolute;
  left: var(--bga-09-x);
  top: var(--bga-09-y);
  width: calc(56px + var(--bga-09-d) * 200px);
  aspect-ratio: 1;
  border-radius: 50%;
  translate: -50% -50%;
  mix-blend-mode: screen;
  filter: blur(calc(2px + var(--bga-09-d) * 24px));
  opacity: calc(.86 - var(--bga-09-d) * .42);
  background: radial-gradient(circle,
      oklch(1 0 0/.92) 0 16%,
      oklch(0.78 0.17 var(--bga-09-h)/.78) 38% 70%,
      oklch(0.6 0.2 var(--bga-09-h)/.3) 76%,transparent 80%);
  animation: bga-09-rise calc(52s - var(--bga-09-d) * 30s) ease-in-out infinite alternate, bga-09-sway calc(31s - var(--bga-09-d) * 14s) ease-in-out infinite alternate, bga-09-pulse calc(9s + var(--bga-09-d) * 7s) ease-in-out infinite alternate;
}

@keyframes bga-09-rise {
  from {
    translate: -50% -20%;
  }

  to {
    translate: -50% -86%;
  }
}

@keyframes bga-09-sway {
  from {
    margin-left: -5vmin;
  }

  to {
    margin-left: 6vmin;
  }
}

@keyframes bga-09-pulse {
  from {
    scale: .9;
  }

  to {
    scale: 1.12;
  }
}

.bga-09__stage {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-09__frame {
  width: min(100%,680px);
  display: grid;
  gap: 16px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 20px;
  background: oklch(0.12 0.025 275/.55);
  border: 1px solid oklch(1 0 0/.13);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 0 44px 100px -50px oklch(0 0 0/.95);
}

.bga-09__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.84 0.12 220);
}

.bga-09__title {
  font-size: clamp(26px,5vw,50px);
  font-weight: 640;
  line-height: 1.05;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.bga-09__sub {
  max-width: 48ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.93 0.01 270/.76);
  text-wrap: pretty;
}

.bga-09__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  padding: 1px 5px;
  border-radius: 5px;
  background: oklch(1 0 0/.1);
}

.bga-09__scale {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 6px;
  font-size: 10.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(1 0 0/.5);
}

.bga-09__ramp {
  width: min(46vw,220px);
  height: 8px;
  border-radius: 99px;
  background: linear-gradient(90deg,oklch(0.95 0.05 220),oklch(0.55 0.1 280));
  filter: blur(.4px);
}

@media (prefers-reduced-motion: reduce) {
  .bga-09__lights,
    .bga-09__lights span {
    animation: none;
  }
}
```
