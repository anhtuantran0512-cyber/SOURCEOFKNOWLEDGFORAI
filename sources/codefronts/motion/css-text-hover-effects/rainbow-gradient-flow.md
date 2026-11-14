---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/rainbow-gradient-flow/"
title: "Rainbow Gradient Flow"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "A rainbow with engineering in it: instead of hand-picking seven stops, the gradient is TWO colors and one instruction — linear-gradient(90deg in oklch longer…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rainbow Gradient Flow
Source: https://codefronts.com/motion/css-text-hover-effects/rainbow-gradient-flow/

A rainbow with engineering in it: instead of hand-picking seven stops, the gradient is TWO colors and one instruction — linear-gradient(90deg in oklch longer hue, …) — telling the browser to travel the long way around the hue wheel, generating the entire spectrum at perceptually even brightness (no muddy dark cyan, no blinding yellow spike like sRGB rainbows). At rest the headline is quiet ink; hover crossfades it out (demo 03's color→transparent trick) while background-position flows the spectrum through the glyphs on a seamless 300%-wide loop.
## HTML
```html
<section class="cth-21" aria-label="Rainbow gradient flow demo">
  <div class="cth-21__stage">
    <div class="cth-21__scene">
      <p class="cth-21__eyebrow">Brighton Pride &mdash; March 7, 2026</p>
      <h1 class="cth-21__title"><a class="cth-21__rainbow" href="#cth21-top" id="cth21-top">EVERY COLOUR<br>OUT LOUD</a></h1>
      <p class="cth-21__sub">Two oklch stops and <code>longer hue</code> generate the whole spectrum &mdash; evenly bright, endlessly looping, only when asked.</p>
      <div class="cth-21__row">
        <a class="cth-21__cta" href="#cth21-top">March with us</a>
        <a class="cth-21__ghost" href="#cth21-top">Route map</a>
      </div>
      <p class="cth-21__hint">Hover the headline or the button. The loop is seamless because travel (-300%) equals the canvas width (300%).</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-21,
.cth-21 *,
.cth-21 *::before,
.cth-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-21 {
  --bg: oklch(0.98 0.004 90);
  --ink: oklch(0.2 0.01 280);
  --mut: oklch(0.5 0.015 280);
  --line: oklch(0.9 0.006 280);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-21__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth21/inline-size;
}

.cth-21__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(16px,3cqi,26px);
}

.cth-21__eyebrow {
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-21__title {
  line-height: 1;
}

.cth-21__rainbow {
  display: inline-block;
  text-decoration: none;
  font-size: clamp(46px,10.5cqi,108px);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1.02;
  padding: .06em .08em;
  background-image: linear-gradient(90deg,#e40303,#ff8c00,#ffd700,#00a86b,#0057ff,#8a2be2,#e40303);
  background-image: linear-gradient(90deg in oklch longer hue,oklch(0.7 0.19 0),oklch(0.7 0.19 350));
  background-size: 300% 100%;
  background-position: 0% 0;
  -webkit-background-clip: text;
  background-clip: text;
  color: var(--ink);
  transition: color .45s ease;
}

.cth-21__rainbow:hover,
.cth-21__rainbow:focus-visible {
  color: transparent;
  animation: cth21-flow 3.5s linear infinite;
}

.cth-21__rainbow:focus-visible {
  outline: 3px solid oklch(0.7 0.19 300);
  outline-offset: 8px;
  border-radius: 8px;
}

@keyframes cth21-flow {
  to {
    background-position: -300% 0;
  }
}

.cth-21__sub {
  font-size: 15px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 52ch;
}

.cth-21__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.93 0.005 280);
  padding: 1px 6px;
  border-radius: 4px;
}

.cth-21__row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 14px;
  margin-top: 6px;
}

.cth-21__cta {
  display: grid;
  place-items: center;
  min-height: 56px;
  padding: 0 32px;
  border-radius: 99px;
  font-size: 16px;
  font-weight: 850;
  text-decoration: none;
  color: oklch(0.99 0.002 90);
  background-image: linear-gradient(90deg,#e40303,#ff8c00,#00a86b,#0057ff,#8a2be2,#e40303);
  background-image: linear-gradient(90deg in oklch longer hue,oklch(0.55 0.19 0),oklch(0.55 0.19 350));
  background-size: 300% 100%;
  box-shadow: 0 10px 30px oklch(0.5 0.15 320/.25);
  transition: box-shadow .3s ease,translate .3s ease;
}

.cth-21__cta:hover,
.cth-21__cta:focus-visible {
  animation: cth21-flow 2.6s linear infinite;
  translate: 0 -2px;
  box-shadow: 0 16px 40px oklch(0.5 0.15 320/.35);
}

.cth-21__cta:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.cth-21__ghost {
  display: grid;
  place-items: center;
  min-height: 56px;
  padding: 0 28px;
  border-radius: 99px;
  border: 1.5px solid color-mix(in oklch,var(--ink) 32%,transparent);
  font-size: 16px;
  font-weight: 750;
  text-decoration: none;
  color: var(--ink);
  transition: border-color .3s ease;
}

.cth-21__ghost:hover,
.cth-21__ghost:focus-visible {
  border-color: var(--ink);
}

.cth-21__ghost:focus-visible {
  outline: 3px solid oklch(0.7 0.19 300);
  outline-offset: 3px;
}

.cth-21__hint {
  font-size: 12.5px;
  color: var(--mut);
  max-width: 54ch;
  line-height: 1.7;
}

@media (prefers-reduced-motion: reduce) {
  .cth-21 * {
    animation: none !important;
    transition-duration: .25s !important;
  }

  .cth-21__rainbow:hover,
    .cth-21__rainbow:focus-visible {
    color: transparent;
  }
}
```
