---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/animated-dot-grid-pattern/"
title: "Animated Dot Grid Pattern"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "The dotted canvas that every modern dev-tool site now uses as its default surface — but with depth."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Dot Grid Pattern
Source: https://codefronts.com/motion/css-background-animations/animated-dot-grid-pattern/

The dotted canvas that every modern dev-tool site now uses as its default surface — but with depth. Three tiled radial-gradient layers scroll at different speeds and different dot sizes for real parallax, a radial mask fades the field into the page edges, and a slow luminance wave crosses the grid so the dots twinkle in a band rather than all at once. Density, dot size and drift are switchable in-page.
## HTML
```html
<section class="bga-03" aria-label="Animated dot grid pattern background demo">
  <div class="bga-03__field" aria-hidden="true"></div>
  <div class="bga-03__wave" aria-hidden="true"></div>
  <div class="bga-03__glow" aria-hidden="true"></div>

  <div class="bga-03__stage">
    <div class="bga-03__card">
      <span class="bga-03__badge">03 · Dot matrix surface</span>
      <h1 class="bga-03__title">Three tiled layers.<br>Zero DOM nodes.</h1>
      <p class="bga-03__sub">Parallax dots painted entirely by <code>radial-gradient</code> tiling — the whole field costs three paint layers, not three thousand divs.</p>
      <div class="bga-03__row" role="group" aria-label="Dot grid options">
        <input class="bga-03__sr" type="radio" name="bga-03-d" id="bga-03-d1">
        <label class="bga-03__chip" for="bga-03-d1">Sparse</label>
        <input class="bga-03__sr" type="radio" name="bga-03-d" id="bga-03-d2" checked>
        <label class="bga-03__chip" for="bga-03-d2">Balanced</label>
        <input class="bga-03__sr" type="radio" name="bga-03-d" id="bga-03-d3">
        <label class="bga-03__chip" for="bga-03-d3">Dense</label>
        <span class="bga-03__sep" aria-hidden="true"></span>
        <input class="bga-03__sr" type="radio" name="bga-03-m" id="bga-03-m1" checked>
        <label class="bga-03__chip" for="bga-03-m1">Drift</label>
        <input class="bga-03__sr" type="radio" name="bga-03-m" id="bga-03-m2">
        <label class="bga-03__chip" for="bga-03-m2">Still</label>
      </div>
      <p class="bga-03__spec">tile-multiple translation · masked twinkle sweep · radial edge fade</p>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-03,
.bga-03 *,
.bga-03 *::before,
.bga-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-03-bg: oklch(0.15 0.014 258);
  --bga-03-dot: oklch(0.78 0.05 250);
  --bga-03-acc: oklch(0.8 0.15 195);
  --bga-03-t: 26px;
  --bga-03-r: 1.5px;
  --bga-03-dur: 26s;
  background: var(--bga-03-bg);
  color: oklch(0.96 0.008 250);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-03__field,
.bga-03__wave {
  position: absolute;
  inset: -8%;
  background-image: radial-gradient(color-mix(in oklab,var(--bga-03-dot) 52%,transparent) var(--bga-03-r),transparent calc(var(--bga-03-r) + .5px)), radial-gradient(color-mix(in oklab,var(--bga-03-dot) 30%,transparent) calc(var(--bga-03-r) * .72),transparent calc(var(--bga-03-r) * .72 + .5px)), radial-gradient(color-mix(in oklab,var(--bga-03-acc) 26%,transparent) calc(var(--bga-03-r) * .55),transparent calc(var(--bga-03-r) * .55 + .5px));
  background-size: var(--bga-03-t) var(--bga-03-t),calc(var(--bga-03-t) * 1.7) calc(var(--bga-03-t) * 1.7),calc(var(--bga-03-t) * 2.6) calc(var(--bga-03-t) * 2.6);
  animation: bga-03-drift var(--bga-03-dur) linear infinite;
  -webkit-mask-image: radial-gradient(120% 100% at 50% 45%,oklch(0 0 0) 30%,transparent 100%);
  mask-image: radial-gradient(120% 100% at 50% 45%,oklch(0 0 0) 30%,transparent 100%);
}

@keyframes bga-03-drift {
  to {
    background-position: var(--bga-03-t) var(--bga-03-t), calc(var(--bga-03-t) * -1.7) calc(var(--bga-03-t) * 1.7), calc(var(--bga-03-t) * 2.6) calc(var(--bga-03-t) * -2.6);
  }
}

.bga-03__wave {
  filter: brightness(2.6) saturate(1.6);
  -webkit-mask-image: linear-gradient(115deg,transparent 42%,oklch(0 0 0) 50%,transparent 58%);
  mask-image: linear-gradient(115deg,transparent 42%,oklch(0 0 0) 50%,transparent 58%);
  -webkit-mask-size: 320% 100%;
  mask-size: 320% 100%;
  animation: bga-03-drift var(--bga-03-dur) linear infinite,bga-03-sweep 9s linear infinite;
}

@keyframes bga-03-sweep {
  from {
    -webkit-mask-position: 120% 0;
    mask-position: 120% 0;
  }

  to {
    -webkit-mask-position: -120% 0;
    mask-position: -120% 0;
  }
}

.bga-03__glow {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(60% 46% at 50% 44%,color-mix(in oklab,var(--bga-03-acc) 12%,transparent),transparent 70%);
}

.bga-03__stage {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-03__card {
  width: min(100%,700px);
  display: grid;
  gap: 15px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.6vw,46px);
  border-radius: 24px;
  background: linear-gradient(oklch(0.2 0.018 258/.82),oklch(0.16 0.016 258/.9));
  border: 1px solid oklch(1 0 0/.1);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  box-shadow: 0 40px 100px -50px oklch(0 0 0/.95);
}

.bga-03__badge {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--bga-03-acc);
  padding: 6px 13px;
  border-radius: 99px;
  border: 1px solid color-mix(in oklab,var(--bga-03-acc) 34%,transparent);
  background: color-mix(in oklab,var(--bga-03-acc) 10%,transparent);
}

.bga-03__title {
  font-size: clamp(27px,5.2vw,52px);
  font-weight: 640;
  line-height: 1.06;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.bga-03__sub {
  max-width: 46ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.88 0.01 250/.76);
  text-wrap: pretty;
}

.bga-03__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  padding: 1px 5px;
  border-radius: 5px;
  background: oklch(1 0 0/.08);
}

.bga-03__row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  align-items: center;
  margin-top: 4px;
}

.bga-03__sep {
  width: 1px;
  height: 22px;
  background: oklch(1 0 0/.16);
}

.bga-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.bga-03__chip {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  padding: 0 15px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 12.5px;
  font-weight: 550;
  color: oklch(0.9 0.01 250/.72);
  background: oklch(1 0 0/.05);
  border: 1px solid oklch(1 0 0/.12);
  transition: background .25s,color .25s,border-color .25s;
}

.bga-03__chip:hover {
  background: oklch(1 0 0/.11);
}

.bga-03__sr:checked + .bga-03__chip {
  background: var(--bga-03-acc);
  color: oklch(0.16 0.02 200);
  border-color: transparent;
  font-weight: 650;
}

.bga-03__sr:focus-visible + .bga-03__chip {
  outline: 3px solid var(--bga-03-acc);
  outline-offset: 3px;
}

.bga-03__spec {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: oklch(0.8 0.01 250/.45);
}

.bga-03:has(#bga-03-d1:checked) {
  --bga-03-t: 44px;
  --bga-03-r: 1.8px;
}

.bga-03:has(#bga-03-d3:checked) {
  --bga-03-t: 15px;
  --bga-03-r: 1.1px;
}

.bga-03:has(#bga-03-m2:checked) .bga-03__field {
  animation: none;
}

.bga-03:has(#bga-03-m2:checked) .bga-03__wave {
  animation: bga-03-sweep 9s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .bga-03__field,
    .bga-03__wave {
    animation: none;
  }
}
```
