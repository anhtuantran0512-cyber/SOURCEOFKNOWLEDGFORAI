---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/draggable-fab/"
title: "Draggable Floating Action Button with Corner Snap CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A FAB the user can move out of the way — drag it anywhere, release, and it flies to the nearest corner with a spring."
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Draggable Floating Action Button with Corner Snap CSS
Source: https://codefronts.com/components/css-floating-buttons/draggable-fab/

A FAB the user can move out of the way — drag it anywhere, release, and it flies to the nearest corner with a spring. Uses Pointer Events (one code path for mouse, touch and pen), setPointerCapture so the drag survives leaving the element, keyboard arrows as a full alternative, and it remembers the chosen corner for the session.
## HTML
```html
<section class="fb-20" aria-label="Draggable floating action button demo">
  <div class="fb-20__field" id="fb-20-field">
    <div class="fb-20__page">
      <p class="fb-20__eyebrow">setPointerCapture · corner snap</p>
      <h2 class="fb-20__title">Drag it. Let go. It finds a corner.</h2>
      <p class="fb-20__sub">One pointer code path for mouse, touch and pen. Arrow keys nudge it, Shift+arrow throws it to an edge, and every move is announced.</p>
      <p class="fb-20__live" id="fb-20-live" role="status" aria-live="polite">Docked bottom right</p>
      <ul class="fb-20__keys"><li><kbd>↑</kbd><kbd>↓</kbd><kbd>←</kbd><kbd>→</kbd> nudge 24px</li><li><kbd>Shift</kbd> + arrow throw to edge</li></ul>
    </div>
    <button class="fb-20__fab" id="fb-20-fab" type="button" aria-label="Assistive menu, draggable. Use arrow keys to move." data-corner="br">
      <span class="fb-20__grip" aria-hidden="true"></span>
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="3.2" fill="currentColor"/><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-dasharray="3 4"/></svg>
    </button>
  </div>
  <p class="fb-20__chip">touch-action:none · transition on release only · 24px nudge</p>
</section>
```
## CSS
```css
.fb-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-20-bg);
  --fb-20-bg: oklch(0.96 0.01 155);
  --fb-20-brand: oklch(0.48 0.13 165);
  --fb-20-ink: oklch(0.22 0.025 165);
  --fb-20-mut: oklch(0.52 0.015 165);
  --fb-20-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-20-ink);
  display: grid;
  place-items: center;
  align-content: center;
  gap: 14px;
  padding: clamp(18px,4vw,44px);
}

.fb-20 *,
.fb-20 *::before,
.fb-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-20__field {
  position: relative;
  width: min(100%,720px);
  height: min(70svh,560px);
  border-radius: 26px;
  overflow: hidden;
  background: var(--fb-20-card);
  border: 1px solid oklch(0.22 0.025 165/.1);
  box-shadow: 0 26px 60px -34px oklch(0.22 0.025 165/.85);
  background-image: radial-gradient(oklch(0.22 0.025 165/.07) 1px,transparent 1px);
  background-size: 22px 22px;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,44px);
  touch-action: none;
}

.fb-20__page {
  width: min(100%,48ch);
  display: grid;
  gap: 12px;
  justify-items: center;
  text-align: center;
}

.fb-20__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-20-brand);
}

.fb-20__title {
  font-size: clamp(23px,4vw,38px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-20__sub {
  font-size: clamp(13.5px,1.6vw,16px);
  line-height: 1.62;
  color: var(--fb-20-mut);
  text-wrap: pretty;
}

.fb-20__live {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--fb-20-brand);
  background: oklch(0.48 0.13 165/.1);
  border: 1px dashed oklch(0.48 0.13 165/.4);
  border-radius: 10px;
  padding: 7px 14px;
}

.fb-20__keys {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  font-size: 11.5px;
  color: var(--fb-20-mut);
}

.fb-20__keys li {
  display: flex;
  align-items: center;
  gap: 4px;
  background: oklch(0.97 0.008 165);
  border: 1px solid oklch(0.22 0.025 165/.1);
  border-radius: 99px;
  padding: 5px 11px;
}

.fb-20 kbd {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  background: var(--fb-20-card);
  border: 1px solid oklch(0.22 0.025 165/.16);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 1px 5px;
}

.fb-20__fab {
  position: absolute;
  z-index: 4;
  display: grid;
  place-items: center;
  inline-size: 62px;
  block-size: 62px;
  border: 0;
  border-radius: 20px;
  cursor: grab;
  touch-action: none;
  color: oklch(0.99 0.01 165);
  background: linear-gradient(150deg,oklch(0.62 0.14 160),var(--fb-20-brand));
  box-shadow: 0 14px 30px -12px oklch(0.35 0.11 165/.9),0 2px 6px oklch(0.25 0.05 165/.3);
  transition: left .46s cubic-bezier(.2,1.3,.35,1),top .46s cubic-bezier(.2,1.3,.35,1),scale .2s ease,box-shadow .25s ease;
}

.fb-20__fab svg {
  width: 26px;
  height: 26px;
}

.fb-20__fab[data-dragging="true"] {
  cursor: grabbing;
  transition: none;
  scale: 1.08;
  box-shadow: 0 26px 50px -14px oklch(0.35 0.11 165/.95);
}

.fb-20__fab:hover {
  box-shadow: 0 18px 38px -12px oklch(0.35 0.11 165/.95);
}

.fb-20__fab:focus-visible {
  outline: 3px solid var(--fb-20-brand);
  outline-offset: 4px;
}

.fb-20__grip {
  position: absolute;
  top: 6px;
  left: 50%;
  translate: -50% 0;
  width: 22px;
  height: 3px;
  border-radius: 99px;
  background: oklch(1 0 0/.45);
}

.fb-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-20-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.22 0.025 165/.14);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .fb-20__fab {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const field = document.getElementById('fb-20-field');
  const fab = document.getElementById('fb-20-fab');
  const live = document.getElementById('fb-20-live');
  if (!field || !fab || fab.dataset.fbWired) return;
  fab.dataset.fbWired = '1';
  const PAD = 16;
  const names = { tl: 'top left', tr: 'top right', bl: 'bottom left', br: 'bottom right' };
  let drag = null, moved = 0;
  const bounds = () => {
    const f = field.getBoundingClientRect();
    return { w: f.width - fab.offsetWidth - PAD, h: f.height - fab.offsetHeight - PAD, rect: f };
  };
  const place = (x, y) => {
    const b = bounds();
    fab.style.left = Math.min(Math.max(x, PAD), b.w) + 'px';
    fab.style.top = Math.min(Math.max(y, PAD), b.h) + 'px';
  };
  const snap = (corner) => {
    const b = bounds();
    fab.dataset.corner = corner;
    fab.style.left = (corner === 'tl' || corner === 'bl' ? PAD : b.w) + 'px';
    fab.style.top = (corner === 'tl' || corner === 'tr' ? PAD : b.h) + 'px';
    live.textContent = 'Docked ' + names[corner];
  };
  const nearest = () => {
    const b = bounds();
    const x = parseFloat(fab.style.left) || 0, y = parseFloat(fab.style.top) || 0;
    return (y < b.h / 2 ? 't' : 'b') + (x < b.w / 2 ? 'l' : 'r');
  };
  fab.addEventListener('pointerdown', (e) => {
    const r = fab.getBoundingClientRect(), f = field.getBoundingClientRect();
    fab.setPointerCapture(e.pointerId);
    fab.dataset.dragging = 'true';
    moved = 0;
    drag = { dx: e.clientX - r.left, dy: e.clientY - r.top, fx: f.left, fy: f.top };
  });
  fab.addEventListener('pointermove', (e) => {
    if (!drag) return;
    moved += Math.abs(e.movementX) + Math.abs(e.movementY);
    place(e.clientX - drag.dx - drag.fx, e.clientY - drag.dy - drag.fy);
  });
  const end = () => { if (!drag) return; drag = null; fab.dataset.dragging = 'false'; snap(nearest()); };
  fab.addEventListener('pointerup', end);
  fab.addEventListener('pointercancel', end);
  fab.addEventListener('click', (e) => { if (moved > 6) { e.preventDefault(); e.stopPropagation(); moved = 0; } });
  fab.addEventListener('keydown', (e) => {
    const map = { ArrowLeft: [-24, 0], ArrowRight: [24, 0], ArrowUp: [0, -24], ArrowDown: [0, 24] };
    if (!map[e.key]) return;
    e.preventDefault();
    const b = bounds();
    if (e.shiftKey) {
      const c = fab.dataset.corner || 'br';
      const vert = c[0], horiz = c[1];
      if (e.key === 'ArrowLeft') snap(vert + 'l');
      else if (e.key === 'ArrowRight') snap(vert + 'r');
      else if (e.key === 'ArrowUp') snap('t' + horiz);
      else snap('b' + horiz);
      return;
    }
    const x = (parseFloat(fab.style.left) || b.w) + map[e.key][0];
    const y = (parseFloat(fab.style.top) || b.h) + map[e.key][1];
    place(x, y);
    live.textContent = 'Moved to ' + Math.round(parseFloat(fab.style.left)) + ', ' + Math.round(parseFloat(fab.style.top));
  });
  requestAnimationFrame(() => snap('br'));
  window.addEventListener('resize', () => snap(fab.dataset.corner || 'br'));
})();
```
