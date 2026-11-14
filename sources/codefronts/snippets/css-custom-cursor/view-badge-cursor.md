---
source: "codefronts"
url: "https://codefronts.com/snippets/css-custom-cursor/view-badge-cursor/"
title: "Dynamic Cursor Text Badge (View / Play / Read) That Follows the Mouse over a Gallery"
section: "snippets"
category: "css-custom-cursor"
category_name: "CSS Custom Cursor Styles"
description: "The e-commerce and portfolio favourite: hovering a product or project card reveals a pill — 'View', 'Play', 'Read' — that glides along with the pointer,…"
has_js: "true"
---

Here's a working CSS Custom Cursor Style from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dynamic Cursor Text Badge (View / Play / Read) That Follows the Mouse over a Gallery
Source: https://codefronts.com/snippets/css-custom-cursor/view-badge-cursor/

The e-commerce and portfolio favourite: hovering a product or project card reveals a pill — 'View', 'Play', 'Read' — that glides along with the pointer, replacing the native cursor. The label is driven by a data-attribute per card, so one handler powers a whole grid, and the badge scales in with a spring while staying perfectly readable against imagery.
## HTML
```html
<section class="ccs-05">
  <div class="ccs-05__wrap">
    <div class="ccs-05__grid" data-grid>
      <div class="ccs-05__badge" data-badge aria-hidden="true">View</div>
      <a class="ccs-05__card ccs-05__card--a" href="#" data-cursor-label="View"><span>Case study</span><strong>Northwind rebrand</strong></a>
      <a class="ccs-05__card ccs-05__card--b" href="#" data-cursor-label="Play"><span>Motion reel</span><strong>Kinetic titles</strong></a>
      <a class="ccs-05__card ccs-05__card--c" href="#" data-cursor-label="Read"><span>Journal</span><strong>Designing in oklch</strong></a>
      <a class="ccs-05__card ccs-05__card--d" href="#" data-cursor-label="View"><span>Case study</span><strong>Halcyon store</strong></a>
    </div>
  </div>
</section>
```
## CSS
```css
.ccs-05,
.ccs-05 *,
.ccs-05 *::before,
.ccs-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccs-05 {
  --bg: oklch(0.15 0.01 265);
  --text: oklch(0.96 0.005 265);
  --accent: oklch(0.82 0.15 90);
  --muted: color-mix(in oklab,var(--text) 55%,var(--bg));
  color-scheme: dark;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 28px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
}

.ccs-05__wrap {
  width: min(600px,100%);
}

.ccs-05__grid {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.ccs-05__card {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 3px;
  min-height: 150px;
  padding: 20px;
  border-radius: 18px;
  text-decoration: none;
  color: #fff;
  overflow: hidden;
  isolation: isolate;
}

.ccs-05__card span {
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .08em;
  text-transform: uppercase;
  opacity: .85;
}

.ccs-05__card strong {
  font: 700 18px/1.15 system-ui,sans-serif;
}

.ccs-05__card--a {
  background: linear-gradient(150deg,oklch(0.55 0.18 25),oklch(0.3 0.1 25));
}

.ccs-05__card--b {
  background: linear-gradient(150deg,oklch(0.55 0.16 285),oklch(0.3 0.1 285));
}

.ccs-05__card--c {
  background: linear-gradient(150deg,oklch(0.55 0.15 155),oklch(0.3 0.09 155));
}

.ccs-05__card--d {
  background: linear-gradient(150deg,oklch(0.6 0.16 220),oklch(0.32 0.1 220));
}

.ccs-05__card:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.ccs-05__badge {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 10;
  display: grid;
  place-items: center;
  min-width: 64px;
  height: 64px;
  padding: 0 12px;
  border-radius: 999px;
  font: 700 13px/1 system-ui,sans-serif;
  letter-spacing: .02em;
  color: oklch(0.2 0.02 90);
  background: var(--accent);
  box-shadow: 0 8px 24px oklch(0 0 0/.4);
  pointer-events: none;
  opacity: 0;
  scale: .6;
  transition: opacity .2s ease,scale .2s ease;
}

.ccs-05__grid.is-live .ccs-05__badge {
  opacity: 1;
  scale: 1;
}

@media (hover: hover) and (pointer: fine) {
  .ccs-05__grid.is-live {
    cursor: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccs-05__grid.is-live {
    cursor: auto;
  }

  .ccs-05__badge {
    transition: opacity .2s ease;
  }
}
```

## JavaScript
```js
(function () {
  var grid = document.querySelector('.ccs-05__grid');
  var badge = grid.querySelector('[data-badge]');
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  var reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;

  var mx = 0, my = 0, bx = 0, by = 0, raf = 0, running = false;

  grid.addEventListener('pointerover', function (e) {
    var card = e.target.closest('[data-cursor-label]');
    if (!card) return;
    badge.textContent = card.dataset.cursorLabel;
    grid.classList.add('is-live');
    if (!running) { running = true; raf = requestAnimationFrame(loop); }
  });
  grid.addEventListener('pointermove', function (e) {
    var r = grid.getBoundingClientRect();
    mx = e.clientX - r.left; my = e.clientY - r.top;
    if (reduce) badge.style.transform = 'translate(' + mx + 'px,' + my + 'px) translate(-50%,-50%)';
  });
  grid.addEventListener('pointerout', function (e) {
    if (e.relatedTarget && grid.contains(e.relatedTarget)) return;
    grid.classList.remove('is-live');
    running = false; cancelAnimationFrame(raf);
  });

  function loop() {
    bx += (mx - bx) * 0.22; by += (my - by) * 0.22;
    badge.style.transform = 'translate(' + bx + 'px,' + by + 'px) translate(-50%,-50%)';
    if (running) raf = requestAnimationFrame(loop);
  }
})();
```
