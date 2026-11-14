---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-layered-depth-gradient-button/"
title: "CSS Layered Depth Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A gaming-CTA whose gradient body is split into three stacked Z-depth layers — on cursor hover the layers parallax-shift at different rates, giving the button…"
has_js: "true"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Layered Depth Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/css-layered-depth-gradient-button/

A gaming-CTA whose gradient body is split into three stacked Z-depth layers — on cursor hover the layers parallax-shift at different rates, giving the button the physical depth of a 3D dollop of jelly floating over its own drop shadow. Zero WebGL, ~12 lines of JS.
## HTML
```html
<div class="gb-10">
  <div class="gb-10__card">
    <p class="gb-10__kicker"><span class="gb-10__kicker-mark">▚</span> 3D interactions</p>
    <h3 class="gb-10__title">Depth without WebGL.</h3>
    <p class="gb-10__copy">Three CSS-only gradient layers at three different Z-depths, each parallax-shifting at a different rate on cursor move. Runs at 60fps on every device with 12 lines of JS.</p>
    <div class="gb-10__stage" id="gb-10-stage">
      <button class="gb-10__btn" type="button">
        <span class="gb-10__back" aria-hidden="true"></span>
        <span class="gb-10__face">
          <span class="gb-10__lab">Watch the demo</span>
        </span>
        <span class="gb-10__gleam" aria-hidden="true"></span>
      </button>
    </div>
    <p class="gb-10__foot">Move cursor around the button · <code>perspective</code> + <code>translateZ</code></p>
  </div>
</div>
```
## CSS
```css
.gb-10,
.gb-10 *,
.gb-10 *::before,
.gb-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-10 ::selection {
  background: #22d3ee;
  color: #04121a;
}

.gb-10 {
  --bg: #050914;
  --panel: #0e1425;
  --line: rgba(148,163,184,.14);
  --c1: #7c6cff;
  --c2: #22d3ee;
  --c3: #ec4899;
  --ink: #e2e8f0;
  --mut: #8b93ab;
  --gb-10-dx: 0;
  --gb-10-dy: 0;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(90% 120% at 20% -10%, rgba(124,108,255,.18) 0%, transparent 55%), radial-gradient(80% 100% at 100% 100%, rgba(236,72,153,.14) 0%, transparent 60%), var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  color: var(--ink);
}

.gb-10__card {
  width: min(460px,100%);
  background: linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),var(--panel);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 32px 32px 28px;
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.7);
  text-align: center;
}

.gb-10__kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--c2);
  margin-bottom: 14px;
}

.gb-10__kicker-mark {
  color: var(--c2);
  font-size: 14px;
  line-height: 1;
}

.gb-10__title {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -.01em;
  line-height: 1.15;
  margin-bottom: 10px;
}

.gb-10__copy {
  font-size: 14px;
  line-height: 1.55;
  color: var(--mut);
  margin-bottom: 28px;
}

.gb-10__stage {
  perspective: 900px;
  padding: 40px 20px;
  transform: rotateX(calc(var(--gb-10-dy) * -3deg)) rotateY(calc(var(--gb-10-dx) * 3deg));
  transition: transform .3s cubic-bezier(.4,.2,.2,1);
  transform-style: preserve-3d;
}

.gb-10__btn {
  position: relative;
  display: inline-flex;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
  font-family: inherit;
  transform-style: preserve-3d;
  width: 220px;
  height: 60px;
}

.gb-10__btn:focus-visible {
  outline: 2px solid var(--c2);
  outline-offset: 6px;
  border-radius: 16px;
}

.gb-10__back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  background: linear-gradient(135deg, #4c40b8 0%, #0e7c98 55%, #99266c 100%);
  filter: blur(6px);
  opacity: .55;
  transform: translate3d(calc(var(--gb-10-dx) * 4px), calc(var(--gb-10-dy) * 4px), -16px);
  transition: transform .2s ease-out;
  backface-visibility: hidden;
}

.gb-10__face {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  background: radial-gradient(60% 100% at 50% 0%, rgba(255,255,255,.18), transparent 55%), linear-gradient(135deg, var(--c1) 0%, var(--c2) 55%, var(--c3) 100%);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .01em;
  transform: translate3d(calc(var(--gb-10-dx) * 8px), calc(var(--gb-10-dy) * 8px), 0);
  transition: transform .18s ease-out;
  box-shadow: 0 20px 40px -18px rgba(124,108,255,.5), inset 0 1px 0 rgba(255,255,255,.25);
  backface-visibility: hidden;
}

.gb-10__gleam {
  position: absolute;
  top: 8px;
  left: 20%;
  right: 20%;
  height: 16px;
  border-radius: 999px;
  background: radial-gradient(60% 100% at 50% 50%, rgba(255,255,255,.55), transparent 70%);
  filter: blur(3px);
  transform: translate3d(calc(var(--gb-10-dx) * 14px), calc(var(--gb-10-dy) * 14px), 12px);
  transition: transform .12s ease-out;
  pointer-events: none;
  backface-visibility: hidden;
}

.gb-10__lab {
  position: relative;
  z-index: 1;
}

.gb-10__foot {
  font-size: 11.5px;
  color: var(--mut);
  letter-spacing: .02em;
  margin-top: 20px;
}

.gb-10__foot code {
  font-family: "JetBrains Mono", ui-monospace, monospace;
  font-size: 10.5px;
  background: rgba(34,211,238,.10);
  color: #67e8f9;
  padding: 1px 6px;
  border-radius: 4px;
}

.gb-10__stage.is-releasing,
.gb-10__stage.is-releasing .gb-10__back,
.gb-10__stage.is-releasing .gb-10__face,
.gb-10__stage.is-releasing .gb-10__gleam {
  transition-duration: .6s;
  transition-timing-function: cubic-bezier(.34,1.56,.64,1);
}

@media (prefers-reduced-motion: reduce) {
  .gb-10__stage,
    .gb-10__back,
    .gb-10__face,
    .gb-10__gleam {
    transition: none;
    transform: none !important;
  }

  .gb-10__back {
    opacity: 0;
  }
}
```

## JavaScript
```js
(function(){
  var stage = document.getElementById('gb-10-stage');
  if(!stage) return;
  if(!matchMedia('(pointer: fine)').matches) return;

  var rect = null;
  function refresh(){ rect = stage.getBoundingClientRect(); }

  stage.addEventListener('pointerenter', function(){
    refresh();
    stage.classList.remove('is-releasing');
  });
  stage.addEventListener('pointermove', function(e){
    if(!rect) refresh();
    var nx = ((e.clientX - rect.left) / rect.width  - .5) * 2;
    var ny = ((e.clientY - rect.top)  / rect.height - .5) * 2;
    stage.style.setProperty('--gb-10-dx', nx.toFixed(3));
    stage.style.setProperty('--gb-10-dy', ny.toFixed(3));
  });
  stage.addEventListener('pointerleave', function(){
    stage.classList.add('is-releasing');
    stage.style.setProperty('--gb-10-dx', 0);
    stage.style.setProperty('--gb-10-dy', 0);
    rect = null;
  });
  window.addEventListener('resize', function(){ rect = null; });
})();
```
