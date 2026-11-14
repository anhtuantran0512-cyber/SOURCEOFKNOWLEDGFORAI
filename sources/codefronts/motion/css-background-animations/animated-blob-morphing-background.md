---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/animated-blob-morphing-background/"
title: "Morphing Organic Blob Animation"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Two morphing techniques side by side, because they solve different problems."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Morphing Organic Blob Animation
Source: https://codefronts.com/motion/css-background-animations/animated-blob-morphing-background/

Two morphing techniques side by side, because they solve different problems. The big shapes use the eight-value border-radius trick — cheap, GPU-friendly, infinitely loopable. The precise foreground shape uses SVG <animate> path morphing, which can hit exact silhouettes the radius trick can never make. Both run without a line of JavaScript.
## HTML
```html
<section class="bga-18" aria-label="Morphing organic blob background demo">
  <div class="bga-18__wash" aria-hidden="true"></div>

  <div class="bga-18__blobs" aria-hidden="true">
    <span class="bga-18__blob" style="--bga-18-t:22s;--bga-18-x:12%;--bga-18-y:16%;--bga-18-s:44vmin;--bga-18-h:340"></span>
    <span class="bga-18__blob" style="--bga-18-t:30s;--bga-18-x:70%;--bga-18-y:24%;--bga-18-s:36vmin;--bga-18-h:212"></span>
    <span class="bga-18__blob" style="--bga-18-t:26s;--bga-18-x:56%;--bga-18-y:74%;--bga-18-s:50vmin;--bga-18-h:38"></span>
  </div>

  <svg class="bga-18__svg" viewBox="0 0 200 200" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid meet">
    <defs>
      <linearGradient id="bga-18-g" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="oklch(0.78 0.19 12)"/>
        <stop offset="1" stop-color="oklch(0.7 0.2 300)"/>
      </linearGradient>
    </defs>
    <path fill="url(#bga-18-g)" d="M45,-58C58,-47,68,-33,71,-17C74,-1,70,17,60,32C50,47,34,59,15,66C-4,73,-25,75,-42,66C-59,57,-72,37,-75,16C-78,-5,-71,-27,-58,-42C-45,-57,-26,-65,-7,-63C12,-61,32,-69,45,-58Z" transform="translate(100 100)">
      <animate attributeName="d" dur="18s" repeatCount="indefinite" calcMode="spline"
        keyTimes="0;0.33;0.66;1" keySplines="0.45 0 0.55 1;0.45 0 0.55 1;0.45 0 0.55 1"
        values="M45,-58C58,-47,68,-33,71,-17C74,-1,70,17,60,32C50,47,34,59,15,66C-4,73,-25,75,-42,66C-59,57,-72,37,-75,16C-78,-5,-71,-27,-58,-42C-45,-57,-26,-65,-7,-63C12,-61,32,-69,45,-58Z;
                M53,-64C67,-52,73,-31,74,-11C75,9,71,29,59,44C47,59,27,69,5,71C-17,73,-41,67,-57,53C-73,39,-81,17,-78,-4C-75,-25,-61,-45,-45,-57C-29,-69,-11,-73,7,-74C25,-75,39,-76,53,-64Z;
                M39,-51C52,-40,64,-29,70,-14C76,1,76,19,68,33C60,47,44,57,26,64C8,71,-12,75,-31,69C-50,63,-68,47,-74,28C-80,9,-74,-13,-63,-30C-52,-47,-36,-59,-19,-64C-2,-69,17,-62,39,-51Z;
                M45,-58C58,-47,68,-33,71,-17C74,-1,70,17,60,32C50,47,34,59,15,66C-4,73,-25,75,-42,66C-59,57,-72,37,-75,16C-78,-5,-71,-27,-58,-42C-45,-57,-26,-65,-7,-63C12,-61,32,-69,45,-58Z"/>
    </path>
  </svg>

  <div class="bga-18__stage">
    <div class="bga-18__card">
      <p class="bga-18__eyebrow">Two techniques · 18</p>
      <h1 class="bga-18__title">Radii for cheap.<br>Paths for precise.</h1>
      <p class="bga-18__sub">Eight-value <code>border-radius</code> morphs anything convex almost for free. SVG <code>d</code> interpolation hits exact silhouettes — as long as every keyframe has the same command count.</p>
      <div class="bga-18__split">
        <div><b>A</b><span>border-radius<br>62% 38% 46% 54% / 58% 42% 58% 42%</span></div>
        <div><b>B</b><span>SMIL animate d<br>4 keyframes · spline easing</span></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-18,
.bga-18 *,
.bga-18 *::before,
.bga-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-18-bg: oklch(0.97 0.008 300);
  --bga-18-ink: oklch(0.22 0.03 300);
  background: var(--bga-18-bg);
  color: var(--bga-18-ink);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-18__wash {
  position: absolute;
  inset: 0;
  background: radial-gradient(120% 100% at 50% 0%,oklch(0.99 0.01 320),oklch(0.93 0.02 290) 80%);
}

.bga-18__blobs {
  position: absolute;
  inset: 0;
  filter: blur(26px) saturate(1.2);
  opacity: .72;
}

.bga-18__blob {
  position: absolute;
  left: var(--bga-18-x);
  top: var(--bga-18-y);
  width: var(--bga-18-s);
  aspect-ratio: 1;
  translate: -50% -50%;
  background: conic-gradient(from 140deg,
      oklch(0.8 0.17 var(--bga-18-h)),
      oklch(0.86 0.12 calc(var(--bga-18-h) + 40)),
      oklch(0.74 0.19 calc(var(--bga-18-h) - 30)),
      oklch(0.8 0.17 var(--bga-18-h)));
  mix-blend-mode: multiply;
  animation: bga-18-morph var(--bga-18-t) ease-in-out infinite, bga-18-turn calc(var(--bga-18-t) * 2.3) linear infinite;
}

@keyframes bga-18-morph {
  0% {
    border-radius: 62% 38% 46% 54% / 58% 42% 58% 42%;
  }

  34% {
    border-radius: 38% 62% 63% 37% / 41% 44% 56% 59%;
  }

  67% {
    border-radius: 45% 55% 37% 63% / 63% 57% 43% 37%;
  }

  100% {
    border-radius: 62% 38% 46% 54% / 58% 42% 58% 42%;
  }
}

@keyframes bga-18-turn {
  to {
    rotate: 360deg;
  }
}

.bga-18__svg {
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  width: min(74vmin,660px);
  height: min(74vmin,660px);
  opacity: .2;
  filter: blur(.4px);
}

.bga-18__stage {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-18__card {
  width: min(100%,660px);
  display: grid;
  gap: 16px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 30px;
  background: oklch(1 0 0/.66);
  border: 1px solid oklch(1 0 0/.9);
  backdrop-filter: blur(24px) saturate(1.6);
  -webkit-backdrop-filter: blur(24px) saturate(1.6);
  box-shadow: 0 40px 90px -50px oklch(0.3 0.06 300/.5),inset 0 1px 0 oklch(1 0 0);
}

.bga-18__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.58 0.19 340);
}

.bga-18__title {
  font-size: clamp(27px,5.4vw,54px);
  font-weight: 640;
  line-height: 1.02;
  letter-spacing: -.05em;
  text-wrap: balance;
}

.bga-18__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: color-mix(in oklab,var(--bga-18-ink) 78%,transparent);
  text-wrap: pretty;
}

.bga-18__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  padding: 1px 5px;
  border-radius: 5px;
  background: oklch(0.3 0.04 300/.09);
}

.bga-18__split {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-top: 6px;
}

.bga-18__split div {
  display: flex;
  gap: 11px;
  align-items: flex-start;
  text-align: left;
  min-width: 210px;
  padding: 13px 16px;
  border-radius: 16px;
  background: oklch(0.3 0.04 300/.05);
  border: 1px solid oklch(0.3 0.04 300/.1);
}

.bga-18__split b {
  display: grid;
  place-items: center;
  width: 24px;
  height: 24px;
  flex: none;
  border-radius: 8px;
  font-size: 12px;
  background: oklch(0.58 0.19 340);
  color: oklch(0.99 0 0);
}

.bga-18__split span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  line-height: 1.5;
  color: color-mix(in oklab,var(--bga-18-ink) 62%,transparent);
}

@media (prefers-reduced-motion: reduce) {
  .bga-18__blob {
    animation: none;
  }
}
```
