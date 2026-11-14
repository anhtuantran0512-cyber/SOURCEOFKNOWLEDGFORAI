---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/magnetic-cursor-tracking-text/"
title: "Magnetic / Cursor-Tracking Text"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "The Awwwards handshake: links that lean toward your cursor while it's near, with the label inside drifting a beat further than its pill — two-layer parallax…"
has_js: "true"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic / Cursor-Tracking Text
Source: https://codefronts.com/motion/css-text-hover-effects/magnetic-cursor-tracking-text/

The Awwwards handshake: links that lean toward your cursor while it's near, with the label inside drifting a beat further than its pill — two-layer parallax that makes the element feel soft. The physics is split honestly between languages: 22 lines of JS do the measuring (pointer offset from center × pull strength, written to --mx/--my), and CSS does ALL the moving — a short ease during tracking, and on release a long overshooting bezier snaps everything home like elastic. Keyboard users get a focus ring and working links; the magnetism is pointer-only garnish by design.
## HTML
```html
<section class="cth-14" aria-label="Magnetic cursor tracking text demo">
  <div class="cth-14__stage">
    <div class="cth-14__scene">
      <p class="cth-14__eyebrow">Bureau Nocturne &mdash; digital practice, Toronto</p>
      <div class="cth-14__row">
        <a class="cth-14__magnet cth-14__pill" href="#cth14-top" id="cth14-top" data-pull="0.42"><span class="cth-14__inner">View work</span></a>
        <a class="cth-14__magnet cth-14__pill" href="#cth14-top" data-pull="0.42"><span class="cth-14__inner">Process</span></a>
        <a class="cth-14__magnet cth-14__pill cth-14__pill--ghost" href="#cth14-top" data-pull="0.42"><span class="cth-14__inner">About</span></a>
      </div>
      <a class="cth-14__magnet cth-14__mail" href="#cth14-top" data-pull="0.2"><span class="cth-14__inner">[email protected]</span><span class="cth-14__arrow cth-14__inner" aria-hidden="true">&#8599;</span></a>
      <p class="cth-14__hint">Circle the cursor around a pill &mdash; it leans in, the label leans further, release snaps back on an elastic bezier. JS measures; CSS moves.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-14,
.cth-14 *,
.cth-14 *::before,
.cth-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-14 {
  --bg: oklch(0.16 0.01 290);
  --ink: oklch(0.95 0.005 290);
  --mut: oklch(0.6 0.015 290);
  --acc: oklch(0.78 0.16 70);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-14__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(80% 60% at 50% 40%,oklch(0.2 0.015 295),var(--bg) 75%);
  padding: clamp(20px,4vw,56px);
  container: cth14/inline-size;
}

.cth-14__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(26px,5cqi,44px);
}

.cth-14__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-14__magnet {
  translate: var(--mx,0) var(--my,0);
  transition: translate .15s ease-out;
  text-decoration: none;
  color: inherit;
  will-change: translate;
}

.cth-14__magnet:not(:hover) {
  transition: translate .6s cubic-bezier(.22,1.6,.36,1);
}

.cth-14__inner {
  display: inline-block;
  translate: calc(var(--mx,0px)*.55) calc(var(--my,0px)*.55);
  transition: inherit;
}

.cth-14__row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(14px,3cqi,26px);
}

.cth-14__pill {
  display: grid;
  place-items: center;
  min-height: 56px;
  padding: 0 30px;
  border-radius: 99px;
  background: var(--acc);
  color: oklch(0.2 0.03 70);
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .01em;
}

.cth-14__pill--ghost {
  background: transparent;
  color: var(--ink);
  border: 1.5px solid color-mix(in oklch,var(--ink) 35%,transparent);
}

.cth-14__pill:focus-visible,
.cth-14__mail:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 5px;
}

.cth-14__mail {
  display: inline-flex;
  align-items: baseline;
  gap: .35em;
  font-size: clamp(26px,5.6cqi,52px);
  font-weight: 850;
  letter-spacing: -.025em;
  border-bottom: 2px solid color-mix(in oklch,var(--ink) 25%,transparent);
  padding-bottom: .12em;
}

.cth-14__mail:hover {
  border-bottom-color: var(--acc);
}

.cth-14__arrow {
  color: var(--acc);
}

.cth-14__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 54ch;
}

@media (prefers-reduced-motion: reduce) {
  .cth-14__magnet,
    .cth-14__inner {
    translate: 0 0 !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function(){
  var magnets=document.querySelectorAll('.cth-14__magnet');
  if(!magnets.length)return;
  var reduced=matchMedia('(prefers-reduced-motion: reduce)');
  magnets.forEach(function(el){
    var pull=parseFloat(el.getAttribute('data-pull'))||0.35;
    el.addEventListener('pointermove',function(e){
      if(reduced.matches)return;
      var r=el.getBoundingClientRect();
      var x=(e.clientX-r.left-r.width/2)*pull;
      var y=(e.clientY-r.top-r.height/2)*pull;
      el.style.setProperty('--mx',x.toFixed(1)+'px');
      el.style.setProperty('--my',y.toFixed(1)+'px');
    });
    el.addEventListener('pointerleave',function(){
      el.style.setProperty('--mx','0px');
      el.style.setProperty('--my','0px');
    });
  });
})();
```
