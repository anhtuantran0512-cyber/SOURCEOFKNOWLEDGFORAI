---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/waving-flag-ribbon-animation/"
title: "Waving Flag Ribbon Animation"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "A flag that actually ripples: fourteen vertical slices, each running the same keyframe with a progressively offset animation-delay, so a wave travels along…"
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Waving Flag Ribbon Animation
Source: https://codefronts.com/snippets/css-ribbons/waving-flag-ribbon-animation/

A flag that actually ripples: fourteen vertical slices, each running the same keyframe with a progressively offset animation-delay, so a wave travels along the cloth. Shading is part of the animation — every slice brightens as it rises and darkens as it falls — which is what turns a row of moving rectangles into fabric catching light.
## HTML
```html
<section class="rib-19" aria-label="Waving flag ribbon animation demo">
  <div class="rib-19__stage">
    <div class="rib-19__scene">
      <span class="rib-19__pole" aria-hidden="true"></span>
      <div class="rib-19__flag" role="img" aria-label="Waving ribbon flag reading: Now shipping worldwide">
        <div class="rib-19__cloth" aria-hidden="true">
          <span class="rib-19__slice" style="--rib-19-i:0"></span><span class="rib-19__slice" style="--rib-19-i:1"></span>
          <span class="rib-19__slice" style="--rib-19-i:2"></span><span class="rib-19__slice" style="--rib-19-i:3"></span>
          <span class="rib-19__slice" style="--rib-19-i:4"></span><span class="rib-19__slice" style="--rib-19-i:5"></span>
          <span class="rib-19__slice" style="--rib-19-i:6"></span><span class="rib-19__slice" style="--rib-19-i:7"></span>
          <span class="rib-19__slice" style="--rib-19-i:8"></span><span class="rib-19__slice" style="--rib-19-i:9"></span>
          <span class="rib-19__slice" style="--rib-19-i:10"></span><span class="rib-19__slice" style="--rib-19-i:11"></span>
          <span class="rib-19__slice" style="--rib-19-i:12"></span><span class="rib-19__slice" style="--rib-19-i:13"></span>
        </div>
        <p class="rib-19__label"><span class="rib-19__kicker">Now shipping</span><span class="rib-19__big">Worldwide</span></p>
      </div>
    </div>
    <p class="rib-19__caption">14 slices · one keyframe · negative <code>animation-delay</code> per slice · amplitude grows toward the fly edge</p>
    <p class="rib-19__chip" aria-hidden="true">translate + scale + brightness in one keyframe · calc() phase offsets</p>
  </div>
</section>
```
## CSS
```css
.rib-19,
.rib-19 *,
.rib-19 *::before,
.rib-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-19-bg: #0d1522;
  --rib-19-bg: oklch(0.2 0.024 250);
  --rib-19-ink: #eef4ff;
  --rib-19-ink: oklch(0.96 0.012 250);
  --rib-19-mut: #8996ad;
  --rib-19-mut: oklch(0.66 0.026 250);
  --rib-19-a: #3b82f6;
  --rib-19-a: oklch(0.62 0.19 258);
  --rib-19-b: #22d3ee;
  --rib-19-b: oklch(0.79 0.14 205);
  --rib-19-h: clamp(110px,20vw,168px);
  background: var(--rib-19-bg);
  color: var(--rib-19-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(18px,3vw,28px);
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(75% 60% at 50% 40%,color-mix(in oklch,var(--rib-19-a) 16%,transparent),transparent 72%);
}

.rib-19__scene {
  position: relative;
  display: flex;
  align-items: flex-start;
  width: min(100%,720px);
  padding-block: clamp(16px,4vw,32px);
}

.rib-19__pole {
  flex: none;
  inline-size: 9px;
  block-size: calc(var(--rib-19-h) + 76px);
  border-radius: 99px 99px 3px 3px;
  background: linear-gradient(90deg,oklch(0.42 0.02 250),oklch(0.72 0.02 250) 40%,oklch(0.38 0.02 250));
  box-shadow: 0 10px 20px -10px oklch(0 0 0/.8);
}

.rib-19__pole::before {
  content: '';
  position: absolute;
  inset-block-start: -9px;
  inset-inline-start: -4px;
  inline-size: 17px;
  block-size: 17px;
  border-radius: 50%;
  background: radial-gradient(circle at 34% 30%,oklch(0.92 0.05 90),oklch(0.62 0.1 88));
}

.rib-19__flag {
  position: relative;
  flex: 1;
  block-size: var(--rib-19-h);
  display: grid;
  place-items: center;
  margin-inline-start: -1px;
  filter: drop-shadow(0 16px 26px oklch(0.12 0.05 250/.6));
}

.rib-19__cloth {
  position: absolute;
  inset: 0;
  display: flex;
}

.rib-19__slice {
  flex: 1;
  margin-inline-end: -1px;
  background-image: linear-gradient(115deg,var(--rib-19-a),var(--rib-19-b));
  background-size: 1400% 100%;
  background-position: calc(var(--rib-19-i) * 7.7%) 0;
  animation: rib-19-wave 1.9s ease-in-out infinite;
  animation-delay: calc(var(--rib-19-i) * -0.11s);
  --rib-19-amp: calc(3px + var(--rib-19-i) * 0.85px);
}

@keyframes rib-19-wave {
  0%,
    100% {
    translate: 0 0;
    scale: 1 1;
    filter: brightness(1);
  }

  25% {
    translate: 0 calc(var(--rib-19-amp) * -1);
    scale: 1 .972;
    filter: brightness(1.17);
  }

  50% {
    translate: 0 0;
    scale: 1 1;
    filter: brightness(1);
  }

  75% {
    translate: 0 var(--rib-19-amp);
    scale: 1 1.03;
    filter: brightness(.85);
  }
}

.rib-19__label {
  position: relative;
  z-index: 1;
  display: grid;
  justify-items: center;
  gap: 2px;
  text-align: center;
  padding-inline: 14px;
  color: oklch(0.17 0.05 250);
  animation: rib-19-ride 1.9s ease-in-out infinite;
  animation-delay: -0.77s;
}

@keyframes rib-19-ride {
  0%,
    100% {
    translate: 0 0;
    rotate: 0deg;
  }

  25% {
    translate: 0 -3px;
    rotate: -.5deg;
  }

  75% {
    translate: 0 3px;
    rotate: .5deg;
  }
}

.rib-19__kicker {
  font-size: clamp(11px,2.2vw,13px);
  font-weight: 800;
  letter-spacing: .28em;
  text-transform: uppercase;
  opacity: .72;
}

.rib-19__big {
  font-size: clamp(28px,6.4vw,52px);
  font-weight: 850;
  letter-spacing: -.045em;
  line-height: 1;
  text-shadow: 0 1px 0 oklch(1 0 0/.28);
}

.rib-19__caption {
  max-width: 56ch;
  text-align: center;
  font-size: 13px;
  line-height: 1.6;
  color: var(--rib-19-mut);
  text-wrap: pretty;
}

.rib-19__caption code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  padding: 1px 5px;
  border-radius: 5px;
  background: oklch(1 0 0/.08);
}

.rib-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-19-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-19__slice,
    .rib-19__label {
    animation: none;
  }
}
```
