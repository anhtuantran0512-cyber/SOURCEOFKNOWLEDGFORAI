---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/skewed-3d-ribbon-header-banner/"
title: "Skewed 3D Ribbon Header Banner"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "Match-day energy: three skewed bands stacked in real 3D space with perspective, animated hazard stripes scrolling behind the headline, and a neon edge that…"
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skewed 3D Ribbon Header Banner
Source: https://codefronts.com/snippets/css-ribbons/skewed-3d-ribbon-header-banner/

Match-day energy: three skewed bands stacked in real 3D space with perspective, animated hazard stripes scrolling behind the headline, and a neon edge that bleeds through the layers. The key move is the counter-skew — the band is skewed, the text inside is skewed back by the same angle, so the type stays upright and readable while the shape stays aggressive.
## HTML
```html
<section class="rib-07" aria-label="Skewed 3D ribbon header banner demo">
  <div class="rib-07__stage">
    <div class="rib-07__hero">
      <div class="rib-07__stack">
        <div class="rib-07__tilt">
          <span class="rib-07__band rib-07__band--back" aria-hidden="true"></span>
          <span class="rib-07__band rib-07__band--mid" aria-hidden="true"><span class="rib-07__stripes"></span></span>
          <div class="rib-07__band rib-07__band--front">
          <div class="rib-07__txt">
            <p class="rib-07__kicker"><span>Round 14</span><span class="rib-07__live">LIVE</span></p>
            <h2 class="rib-07__head" data-text="MATCH DAY">MATCH DAY</h2>
            </div>
          </div>
        </div>
      </div>
      <div class="rib-07__meta">
        <div class="rib-07__team"><span class="rib-07__code">NOR</span><span class="rib-07__score">3</span></div>
        <span class="rib-07__vs">78'</span>
        <div class="rib-07__team"><span class="rib-07__score">2</span><span class="rib-07__code">VLK</span></div>
      </div>
      <div class="rib-07__cta-row">
        <button class="rib-07__cta" type="button"><span>Watch live</span></button>
        <button class="rib-07__ghost" type="button"><span>Match centre</span></button>
      </div>
    </div>
    <p class="rib-07__chip" aria-hidden="true">skewX + inverse counter-skew · perspective translateZ · repeating-linear-gradient scroll</p>
  </div>
</section>
```
## CSS
```css
.rib-07,
.rib-07 *,
.rib-07 *::before,
.rib-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-07-bg: #07070b;
  --rib-07-bg: oklch(0.15 0.014 275);
  --rib-07-ink: #f4f6ff;
  --rib-07-ink: oklch(0.97 0.01 275);
  --rib-07-mut: #8f93a8;
  --rib-07-mut: oklch(0.66 0.024 278);
  --rib-07-acc: #c8ff2e;
  --rib-07-acc: oklch(0.9 0.21 122);
  --rib-07-hot: #ff2d6f;
  --rib-07-hot: oklch(0.66 0.25 8);
  --rib-07-skew: -10deg;
  --rib-07-h: clamp(104px,17.5vw,156px);
  background: var(--rib-07-bg);
  color: var(--rib-07-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3.4vw,34px);
  padding: clamp(18px,4vw,52px);
  overflow: hidden;
  background: radial-gradient(70% 60% at 50% 38%,color-mix(in oklch,var(--rib-07-acc) 9%,transparent),transparent 70%),repeating-linear-gradient(0deg,oklch(1 0 0/.03) 0 1px,transparent 1px 4px);
}

.rib-07__hero {
  width: min(100%,900px);
  display: grid;
  gap: clamp(20px,3.2vw,32px);
  justify-items: center;
}

.rib-07__stack {
  position: relative;
  width: 100%;
  min-height: calc(var(--rib-07-h) + 104px);
  perspective: 800px;
  perspective-origin: 58% 40%;
}

.rib-07__tilt {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
  transform: translateX(-55px) rotateX(-10deg) rotateY(-15deg) rotateZ(-1deg);
}

.rib-07__band {
  --rib-07-grow: 0px;
  position: absolute;
  inset-inline: calc(var(--rib-07-grow) * -1);
  block-size: calc(var(--rib-07-h) + var(--rib-07-grow));
  inset-block-start: calc(50% - (var(--rib-07-h) + var(--rib-07-grow)) / 2);
  transform: skewX(var(--rib-07-skew));
}

.rib-07__band--back {
  --rib-07-grow: clamp(14px,2.4vw,22px);
  background: var(--rib-07-hot);
  opacity: .55;
  filter: blur(1.4px);
  transform: skewX(var(--rib-07-skew)) translate3d(6px,44px,-95px);
}

.rib-07__band--mid {
  --rib-07-grow: clamp(14px,2.6vw,26px);
  background: oklch(0.23 0.022 275);
  overflow: hidden;
  border-block: 2px solid color-mix(in oklch,var(--rib-07-acc) 55%,transparent);
  transform: skewX(var(--rib-07-skew)) translate3d(calc(-22px - 1.2vw),-16px,-45px);
}

.rib-07__stripes {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(115deg,color-mix(in oklch,var(--rib-07-acc) 34%,transparent) 0 16px,transparent 16px 38px);
  animation: rib-07-slide 1.15s linear infinite;
}

@keyframes rib-07-slide {
  to {
    background-position: 38px 0;
  }
}

.rib-07__band--front {
  display: grid;
  place-items: center;
  transform-style: preserve-3d;
  background: linear-gradient(180deg,oklch(0.2 0.022 275),oklch(0.135 0.018 275));
  box-shadow: 0 26px 60px -24px oklch(0 0 0/.9),inset 0 2px 0 oklch(1 0 0/.09),inset 0 -3px 0 var(--rib-07-acc);
}

.rib-07__band--front::before {
  content: "";
  position: absolute;
  inset-inline: 0;
  inset-block-end: 100%;
  block-size: clamp(14px,2.4vw,22px);
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-07-acc) 72%,white) 0%,color-mix(in oklch,var(--rib-07-acc) 58%,black) 100%);
  transform-origin: 50% 100%;
  transform: rotateX(72deg);
}

.rib-07__band--front::after {
  content: "";
  position: absolute;
  inset-inline-start: 100%;
  inset-block: 0;
  inline-size: clamp(14px,2.4vw,22px);
  background: linear-gradient(90deg,oklch(0.26 0.024 275),oklch(0.17 0.02 275));
  transform-origin: 0 50%;
  transform: rotateY(72deg);
}

.rib-07__txt {
  transform: skewX(calc(var(--rib-07-skew) * -1));
  display: grid;
  justify-items: center;
  gap: 7px;
  padding-inline: 16px;
}

.rib-07__kicker {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: clamp(9.5px,1.7vw,11.5px);
  font-weight: 800;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: var(--rib-07-acc);
}

.rib-07__live {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 3px 9px;
  border-radius: 3px;
  background: #b8134a;
  background: color-mix(in oklch,var(--rib-07-hot) 76%,black);
  color: oklch(0.99 0 0);
  letter-spacing: .14em;
}

.rib-07__live::before {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  animation: rib-07-blink 1.4s steps(1,end) infinite;
}

@keyframes rib-07-blink {
  0%,
    60% {
    opacity: 1;
  }

  61%,
    100% {
    opacity: .3;
  }
}

.rib-07__head {
  position: relative;
  z-index: 0;
  white-space: nowrap;
  font-size: clamp(34px,9.4vw,80px);
  font-weight: 900;
  line-height: .9;
  letter-spacing: -.05em;
  color: oklch(0.99 0.005 275);
}

.rib-07__head::after {
  content: attr(data-text);
  position: absolute;
  z-index: -1;
  inset-block-start: 4px;
  inset-inline: 4px auto;
  white-space: nowrap;
  color: transparent;
  -webkit-text-stroke: 1.5px var(--rib-07-hot);
}

.rib-07__meta {
  display: flex;
  align-items: center;
  gap: clamp(14px,4vw,38px);
  padding: 13px clamp(18px,4vw,30px);
  background: oklch(1 0 0/.05);
  border: 1px solid oklch(1 0 0/.12);
  transform: skewX(var(--rib-07-skew));
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.rib-07__team {
  display: flex;
  align-items: center;
  gap: 12px;
  transform: skewX(calc(var(--rib-07-skew) * -1));
}

.rib-07__code {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .16em;
  color: var(--rib-07-mut);
}

.rib-07__score {
  font-size: clamp(26px,5.4vw,38px);
  font-weight: 800;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
  color: var(--rib-07-acc);
}

.rib-07__vs {
  padding: 5px 11px;
  background: color-mix(in oklch,var(--rib-07-hot) 26%,transparent);
  color: #ff8aa8;
  color: oklch(0.82 0.16 8);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .06em;
  font-variant-numeric: tabular-nums;
  transform: skewX(calc(var(--rib-07-skew) * -1));
}

.rib-07__cta-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
}

.rib-07__cta,
.rib-07__ghost {
  min-height: 48px;
  padding-inline: 26px;
  border-radius: 0;
  font: inherit;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  cursor: pointer;
  transform: skewX(var(--rib-07-skew));
  transition: translate .22s,filter .22s,background .22s;
}

.rib-07__cta>span,
.rib-07__ghost>span {
  display: inline-block;
  transform: skewX(calc(var(--rib-07-skew) * -1));
}

.rib-07__cta {
  border: 0;
  background: var(--rib-07-acc);
  color: oklch(0.2 0.05 122);
}

.rib-07__cta:hover {
  translate: 0 -2px;
  filter: brightness(1.08);
}

.rib-07__ghost {
  border: 2px solid oklch(1 0 0/.3);
  background: transparent;
  color: var(--rib-07-ink);
}

.rib-07__ghost:hover {
  background: oklch(1 0 0/.08);
  translate: 0 -2px;
}

.rib-07__cta:focus-visible,
.rib-07__ghost:focus-visible {
  outline: 3px solid var(--rib-07-hot);
  outline-offset: 4px;
}

.rib-07__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-07-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (max-width: 640px) {
  .rib-07__stack {
    perspective: none;
  }

  .rib-07__tilt {
    transform: none;
  }

  .rib-07__band--back {
    display: none;
  }

  .rib-07__band--front::before,
    .rib-07__band--front::after {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rib-07 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
