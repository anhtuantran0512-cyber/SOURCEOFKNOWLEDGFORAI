---
source: "codefronts"
url: "https://codefronts.com/snippets/css-custom-cursor/magnetic-blend-cursor/"
title: "Magnetic Blend Cursor that Expands on Hover using mix-blend-mode and the CSS :has() Selector"
section: "snippets"
category: "css-custom-cursor"
category_name: "CSS Custom Cursor Styles"
description: "The interactive-affordance cursor: a soft blob with mix-blend-mode: difference that inverts whatever it sits over, and expands dramatically when the pointer…"
has_js: "true"
---

Here's a working CSS Custom Cursor Style from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Blend Cursor that Expands on Hover using mix-blend-mode and the CSS :has() Selector
Source: https://codefronts.com/snippets/css-custom-cursor/magnetic-blend-cursor/

The interactive-affordance cursor: a soft blob with mix-blend-mode: difference that inverts whatever it sits over, and expands dramatically when the pointer enters any button or link. The clever part is that the hover-scale is 100% CSS — the modern :has() selector lets the stage react to a child being hovered, so JavaScript only ever moves the blob and never toggles classes for state.
## HTML
```html
<section class="ccs-03">
  <div class="ccs-03__stage" data-stage>
    <div class="ccs-03__blob" data-blob aria-hidden="true"></div>
    <div class="ccs-03__content">
      <h2>Magnetic blend cursor</h2>
      <p>The blob inverts whatever it covers, and grows over anything clickable — the scale is pure CSS <code>:has()</code>.</p>
      <div class="ccs-03__actions">
        <button class="ccs-03__btn" type="button" data-magnetic>Get started</button>
        <a class="ccs-03__btn ccs-03__btn--ghost" href="#" data-magnetic>Documentation</a>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ccs-03,
.ccs-03 *,
.ccs-03 *::before,
.ccs-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccs-03 {
  --bg: oklch(0.96 0.01 95);
  --ink: oklch(0.2 0.02 265);
  --accent: oklch(0.6 0.2 25);
  --muted: color-mix(in oklab,var(--ink) 60%,var(--bg));
  color-scheme: light;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 28px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
}

.ccs-03__stage {
  position: relative;
  width: min(560px,100%);
  min-height: 320px;
  display: grid;
  place-items: center;
  overflow: hidden;
  border-radius: 24px;
  background: linear-gradient(135deg,oklch(0.98 0.01 95),oklch(0.9 0.03 80));
  border: 1px solid oklch(0.85 0.02 90);
}

.ccs-03__content {
  position: relative;
  z-index: 1;
  max-width: 420px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 40px;
  text-align: center;
  align-items: center;
}

.ccs-03__content h2 {
  font: 800 clamp(24px,5vw,34px)/1.1 system-ui,sans-serif;
  letter-spacing: -.02em;
}

.ccs-03__content p {
  font: 400 14.5px/1.6 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.ccs-03__content code {
  font: 600 12.5px/1 ui-monospace,Menlo,monospace;
  padding: 2px 5px;
  border-radius: 5px;
  background: oklch(0 0 0/.06);
}

.ccs-03__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
  margin-top: 6px;
}

.ccs-03__btn {
  min-height: 48px;
  display: inline-flex;
  align-items: center;
  padding: 0 24px;
  border: none;
  border-radius: 999px;
  font: 700 14px/1 system-ui,sans-serif;
  text-decoration: none;
  color: var(--bg);
  background: var(--ink);
}

.ccs-03__btn--ghost {
  color: var(--ink);
  background: transparent;
  border: 1.5px solid var(--ink);
}

.ccs-03__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.ccs-03__blob {
  position: absolute;
  top: 0;
  left: 0;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: oklch(0.85 0 0);
  mix-blend-mode: difference;
  pointer-events: none;
  opacity: 0;
  z-index: 5;
  transition: scale .3s ease,background .3s ease,opacity .25s ease;
}

.ccs-03__stage.is-live .ccs-03__blob {
  opacity: 1;
}
/* the whole hover interaction — CSS only, powered by :has() */

@supports selector(:has(*)) {
  .ccs-03__stage:has([data-magnetic]:hover) .ccs-03__blob {
    scale: 3.4;
  }
}

@media (hover: hover) and (pointer: fine) {
  .ccs-03__stage {
    cursor: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccs-03__stage {
    cursor: auto;
  }

  .ccs-03__blob {
    display: none;
  }
}
```

## JavaScript
```js
(function () {
  var stage = document.querySelector('.ccs-03__stage');
  var blob = stage.querySelector('[data-blob]');
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion:reduce)').matches) return;

  var mx = 0, my = 0, bx = 0, by = 0, raf = 0;
  stage.addEventListener('pointerenter', function (e) {
    var r = stage.getBoundingClientRect();
    mx = bx = e.clientX - r.left; my = by = e.clientY - r.top;
    stage.classList.add('is-live');
  });
  stage.addEventListener('pointermove', function (e) {
    var r = stage.getBoundingClientRect();
    mx = e.clientX - r.left; my = e.clientY - r.top;
  });
  stage.addEventListener('pointerleave', function () { stage.classList.remove('is-live'); });

  function loop() {
    bx += (mx - bx) * 0.2; by += (my - by) * 0.2;
    blob.style.transform = 'translate(' + bx + 'px,' + by + 'px) translate(-50%,-50%)';
    raf = requestAnimationFrame(loop);
  }
  raf = requestAnimationFrame(loop);
  // NOTE: no hover class toggling here — :has() does that in pure CSS.
})();
```
