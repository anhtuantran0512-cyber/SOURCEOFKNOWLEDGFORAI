---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/mask-spotlight-text-reveal/"
title: "Mask / Spotlight Text Reveal"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "A torch beam through typography: the headline exists twice in one element's layers — dim outlined glyphs everyone sees, and a photograph clipped inside the…"
has_js: "true"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mask / Spotlight Text Reveal
Source: https://codefronts.com/motion/css-text-hover-effects/mask-spotlight-text-reveal/

A torch beam through typography: the headline exists twice in one element's layers — dim outlined glyphs everyone sees, and a photograph clipped inside the letters (background-clip:text) that only shows where a radial-gradient mask says so. Twelve lines of JS feed the cursor into --x/--y; a registered @property tweens the beam's radius from 0 up on entry, so the light blooms instead of popping. No JS? The beam still opens dead-center on hover. Keyboard? :focus-visible floods the whole image. Everyone gets a version.
## HTML
```html
<section class="cth-11" aria-label="Spotlight text reveal demo">
  <div class="cth-11__stage">
    <div class="cth-11__scene">
      <p class="cth-11__eyebrow">Night photography walks &mdash; booking winter 2026</p>
      <a class="cth-11__wrap" href="#cth11-top" id="cth11-top">
        <span class="cth-11__beam" style="--photo:url('https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=1600&auto=format&fit=crop')" aria-hidden="true">MIDNIGHT<br>ATLAS</span>
        <span class="cth-11__base">MIDNIGHT<br>ATLAS</span>
      </a>
      <p class="cth-11__hint">Sweep the cursor across the letters &mdash; the photo lives inside the glyphs; a radial <code>mask</code> at <code>var(--x) var(--y)</code> is the torch. <kbd>Tab</kbd> floods it fully lit.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --cth11-r {
  syntax: '<length>';
  inherits: true;
  initial-value: 0px;
}

.cth-11,
.cth-11 *,
.cth-11 *::before,
.cth-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-11 {
  --bg: oklch(0.15 0.012 265);
  --ink: oklch(0.94 0.01 250);
  --mut: oklch(0.58 0.02 255);
  --acc: oklch(0.8 0.13 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-11__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(100% 80% at 50% 100%,oklch(0.19 0.02 270),var(--bg) 65%);
  padding: clamp(20px,4vw,56px);
  container: cth11/inline-size;
}

.cth-11__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(18px,3.4cqi,28px);
}

.cth-11__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-11__wrap {
  position: relative;
  display: inline-block;
  text-decoration: none;
  font-size: clamp(52px,11.5cqi,118px);
  font-weight: 900;
  letter-spacing: -.02em;
  line-height: 1.02;
  padding: .1em .12em;
  --cth11-r: 0px;
}

.cth-11__wrap:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 8px;
  border-radius: 6px;
}

.cth-11__base {
  display: block;
  color: transparent;
  -webkit-text-stroke: 1.5px color-mix(in oklch,var(--ink) 45%,transparent);
}

.cth-11__beam {
  position: absolute;
  inset: 0;
  padding: .1em .12em;
  display: block;
  background-image: linear-gradient(oklch(0.5 0.1 260/.35),oklch(0.5 0.1 260/.35)),var(--photo);
  background-size: cover;
  background-position: center;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-mask-image: radial-gradient(circle var(--cth11-r) at var(--x,50%) var(--y,50%),#000 38%,transparent 100%);
  mask-image: radial-gradient(circle var(--cth11-r) at var(--x,50%) var(--y,50%),#000 38%,transparent 100%);
  transition: --cth11-r .55s cubic-bezier(.3,.9,.2,1);
}

.cth-11__wrap:hover .cth-11__beam {
  --cth11-r: 170px;
}

.cth-11__wrap:focus-visible .cth-11__beam {
  --cth11-r: 60em;
}

.cth-11__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 56ch;
}

.cth-11__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .92em;
  background: oklch(0.23 0.015 265);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--acc);
}

.cth-11__hint kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  border: 1px solid oklch(0.35 0.02 260);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 2px 6px;
  background: oklch(0.22 0.015 265);
}

@media (prefers-reduced-motion: reduce) {
  .cth-11 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function(){
  var wrap=document.querySelector('.cth-11__wrap');
  if(!wrap)return;
  wrap.addEventListener('pointermove',function(e){
    var r=wrap.getBoundingClientRect();
    wrap.style.setProperty('--x',(e.clientX-r.left)+'px');
    wrap.style.setProperty('--y',(e.clientY-r.top)+'px');
  });
  wrap.addEventListener('pointerleave',function(){
    wrap.style.removeProperty('--x');
    wrap.style.removeProperty('--y');
  });
})();
```
