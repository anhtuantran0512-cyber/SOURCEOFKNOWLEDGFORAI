---
source: "codefronts"
url: "https://codefronts.com/snippets/css-custom-cursor/grab-drag-carousel/"
title: "Custom Grab and Grabbing Cursors for a Drag-to-Scroll Carousel with SVG Hand Icons"
section: "snippets"
category: "css-custom-cursor"
category_name: "CSS Custom Cursor Styles"
description: "The affordance that tells users 'you can drag this': a custom open-hand cursor over a horizontal card track that switches to a closed grabbing-hand the…"
has_js: "true"
---

Here's a working CSS Custom Cursor Style from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom Grab and Grabbing Cursors for a Drag-to-Scroll Carousel with SVG Hand Icons
Source: https://codefronts.com/snippets/css-custom-cursor/grab-drag-carousel/

The affordance that tells users 'you can drag this': a custom open-hand cursor over a horizontal card track that switches to a closed grabbing-hand the instant they press down. The cursors are inline-SVG data-URIs mapped to the native grab / grabbing keywords with fallbacks, and a small Pointer-Events drag-to-scroll handler makes the track actually pannable so the cursor tells the truth.
## HTML
```html
<section class="ccs-04">
  <div class="ccs-04__wrap">
    <div class="ccs-04__head">
      <h2>Drag to explore</h2>
      <p>Open hand on hover, closed hand while dragging. Grab the track and pan.</p>
    </div>
    <div class="ccs-04__track" data-track tabindex="0" role="group" aria-label="Draggable card carousel">
      <article class="ccs-04__card" style="--i:0"><span>01</span><strong>Aurora</strong><small>Brand system</small></article>
      <article class="ccs-04__card" style="--i:1"><span>02</span><strong>Monolith</strong><small>Editorial</small></article>
      <article class="ccs-04__card" style="--i:2"><span>03</span><strong>Halcyon</strong><small>E-commerce</small></article>
      <article class="ccs-04__card" style="--i:3"><span>04</span><strong>Vellum</strong><small>Portfolio</small></article>
      <article class="ccs-04__card" style="--i:4"><span>05</span><strong>Cobalt</strong><small>SaaS UI</small></article>
    </div>
  </div>
</section>
```
## CSS
```css
.ccs-04,
.ccs-04 *,
.ccs-04 *::before,
.ccs-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccs-04 {
  --bg: oklch(0.17 0.02 285);
  --surface: oklch(0.23 0.03 285);
  --text: oklch(0.96 0.01 285);
  --accent: oklch(0.75 0.15 320);
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

.ccs-04__wrap {
  width: min(620px,100%);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ccs-04__head h2 {
  font: 700 22px/1.1 system-ui,sans-serif;
  letter-spacing: -.01em;
}

.ccs-04__head p {
  font: 400 14px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.ccs-04__track {
  display: flex;
  gap: 14px;
  overflow-x: auto;
  padding: 6px 2px 16px;
  scroll-snap-type: x proximity;
  scrollbar-width: thin;
}

.ccs-04__card {
  scroll-snap-align: center;
  flex: 0 0 180px;
  height: 220px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 2px;
  padding: 18px;
  border-radius: 18px;
  border: 1px solid oklch(0.34 0.03 285);
  background: linear-gradient(160deg,oklch(from var(--accent) 0.35 calc(c*0.6) calc(h + var(--i)*22)),var(--surface));
  user-select: none;
  -webkit-user-drag: none;
}

.ccs-04__card span {
  font: 700 12px/1 ui-monospace,Menlo,monospace;
  color: var(--text);
  opacity: .65;
}

.ccs-04__card strong {
  font: 700 19px/1.1 system-ui,sans-serif;
}

.ccs-04__card small {
  font: 500 12.5px/1 system-ui,sans-serif;
  color: var(--muted);
}

.ccs-04__track:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 12px;
}

@media (hover: hover) and (pointer: fine) {
  .ccs-04__track {
    cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3E%3Cg fill='%23ffffff' stroke='%230b0b12' stroke-width='1.4' stroke-linejoin='round'%3E%3Cpath d='M11 14V7.5a1.6 1.6 0 0 1 3.2 0V13m0-1.5a1.6 1.6 0 0 1 3.2 0V13m0-1a1.6 1.6 0 0 1 3.2 0v1m0 0a1.6 1.6 0 0 1 3.2 0v4.2c0 3.4-2.4 6.3-6.4 6.3-2.6 0-4-1-5.6-2.8l-3.4-3.9a1.7 1.7 0 0 1 2.5-2.2z'/%3E%3C/g%3E%3C/svg%3E") 12 6, grab;
  }

  .ccs-04__track.is-dragging {
    cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3E%3Cpath d='M9 15v-2.2a1.5 1.5 0 0 1 3 0V13m0-.5a1.5 1.5 0 0 1 3 0V13m0-.3a1.5 1.5 0 0 1 3 0V13a1.5 1.5 0 0 1 3 0v3.6c0 3.3-2.3 6-6.1 6-2.5 0-3.8-1-5.3-2.7l-2.2-2.6a1.6 1.6 0 0 1 2.4-2.1z' fill='%23ffffff' stroke='%230b0b12' stroke-width='1.4' stroke-linejoin='round'/%3E%3C/svg%3E") 12 10, grabbing;
  }
}
```

## JavaScript
```js
(function () {
  var track = document.querySelector('.ccs-04__track');
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return; // touch → native scroll
  var down = false, startX = 0, startLeft = 0;

  track.addEventListener('pointerdown', function (e) {
    down = true; startX = e.clientX; startLeft = track.scrollLeft;
    track.classList.add('is-dragging');
    track.setPointerCapture(e.pointerId);
  });
  track.addEventListener('pointermove', function (e) {
    if (!down) return;
    track.scrollLeft = startLeft - (e.clientX - startX);
  });
  function end(e) {
    if (!down) return;
    down = false; track.classList.remove('is-dragging');
    try { track.releasePointerCapture(e.pointerId); } catch (err) {}
  }
  track.addEventListener('pointerup', end);
  track.addEventListener('pointercancel', end);
})();
```
