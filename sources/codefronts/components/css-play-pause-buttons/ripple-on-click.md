---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/ripple-on-click/"
title: "Material Ripple Click State Toggle"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "Material Design 3 done to spec, not approximated: a state layer that handles hover, focus and pressed at the documented opacities, plus a ripple that…"
has_js: "true"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Ripple Click State Toggle
Source: https://codefronts.com/components/css-play-pause-buttons/ripple-on-click/

Material Design 3 done to spec, not approximated: a state layer that handles hover, focus and pressed at the documented opacities, plus a ripple that originates at the exact pointer coordinates and expands past the button's far corner. The maths for the radius is the part everyone gets wrong — here it is derived from the pointer's distance to the farthest corner, so the ripple always finishes filling the shape.
## HTML
```html
<section class="pp-23" aria-label="Material ripple click state toggle demo">
  <div class="pp-23__stage">
    <div class="pp-23__card">
      <p class="pp-23__eyebrow">Material 3 · state layer + ripple</p>
      <div class="pp-23__row">
        <button class="pp-23__btn pp-23__btn--filled" type="button" aria-pressed="false">
          <span class="pp-23__state" aria-hidden="true"></span>
          <span class="pp-23__content">
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
              <path class="pp-23__p" d="M9 5.6v12.8L18.8 12z" fill="currentColor"/>
              <path class="pp-23__q" d="M8.6 5.6h3.1v12.8H8.6zM12.9 5.6H16v12.8h-3.1z" fill="currentColor"/>
            </svg>
            <span class="pp-23__label">Play</span>
          </span>
        </button>
        <button class="pp-23__btn pp-23__btn--icon" type="button" aria-label="Add to queue">
          <span class="pp-23__state" aria-hidden="true"></span>
          <span class="pp-23__content"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
        </button>
      </div>
      <p class="pp-23__hint">Hover 8% · focus 10% · pressed 10% — ripple from pointer, centred for keyboard.</p>
    </div>
    <p class="pp-23__chip" aria-hidden="true">farthest-corner radius · animationend cleanup · MD3 opacities</p>
  </div>
</section>
```
## CSS
```css
.pp-23,
.pp-23 *,
.pp-23 *::before,
.pp-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-23-bg);
  --pp-23-bg: oklch(0.96 0.014 300);
  --pp-23-card: oklch(0.99 0.006 300);
  --pp-23-ink: oklch(0.25 0.03 300);
  --pp-23-mut: oklch(0.54 0.03 300);
  --pp-23-acc: oklch(0.52 0.2 295);
  --pp-23-on: oklch(0.99 0 0);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-23-ink);
}

.pp-23__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
}

.pp-23__card {
  width: min(100%,460px);
  padding: 30px;
  border-radius: 28px;
  background: var(--pp-23-card);
  box-shadow: 0 1px 3px oklch(0.3 0.04 300/.14),0 20px 48px oklch(0.3 0.04 300/.14);
}

.pp-23__eyebrow {
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--pp-23-mut);
}

.pp-23__row {
  display: flex;
  align-items: center;
  gap: 14px;
  margin: 20px 0 18px;
}

.pp-23__btn {
  position: relative;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 99px;
  cursor: pointer;
  overflow: hidden;
  font: inherit;
  transition: box-shadow .2s;
}

.pp-23__btn--filled {
  min-height: 52px;
  padding: 0 26px;
  background: var(--pp-23-acc);
  color: var(--pp-23-on);
  box-shadow: 0 1px 2px oklch(0.3 0.04 300/.3);
}

.pp-23__btn--filled:hover {
  box-shadow: 0 2px 6px oklch(0.3 0.04 300/.3);
}

.pp-23__btn--icon {
  width: 52px;
  height: 52px;
  background: color-mix(in oklch,var(--pp-23-acc) 12%,transparent);
  color: var(--pp-23-acc);
}

.pp-23__btn:focus-visible {
  outline: 3px solid var(--pp-23-acc);
  outline-offset: 2px;
}

.pp-23__state {
  position: absolute;
  inset: 0;
  background: currentColor;
  opacity: 0;
  transition: opacity .15s;
  pointer-events: none;
}

.pp-23__btn:hover .pp-23__state {
  opacity: .08;
}

.pp-23__btn:focus-visible .pp-23__state,
.pp-23__btn:active .pp-23__state {
  opacity: .1;
}

.pp-23__content {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 640;
  letter-spacing: .01em;
}

.pp-23__ripple {
  position: absolute;
  border-radius: 50%;
  background: currentColor;
  opacity: .28;
  pointer-events: none;
  scale: 0;
  animation: pp-23-ripple .55s cubic-bezier(.2,0,0,1) forwards;
}

@keyframes pp-23-ripple {
  to {
    scale: 1;
    opacity: 0;
  }
}

.pp-23__q {
  display: none;
}

.pp-23__btn[aria-pressed="true"] .pp-23__p {
  display: none;
}

.pp-23__btn[aria-pressed="true"] .pp-23__q {
  display: block;
}

.pp-23__hint {
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--pp-23-mut);
  text-wrap: pretty;
}

.pp-23__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-23-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0.25 0.03 300/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-23__ripple {
    animation-duration: .01ms;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.pp-23__btn').forEach((btn) => {
    if (btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const label = btn.querySelector('.pp-23__label');
    btn.addEventListener('pointerdown', (e) => spawn(btn, e.clientX, e.clientY));
    btn.addEventListener('keydown', (e) => {
      if (e.key === ' ' || e.key === 'Enter') { const r = btn.getBoundingClientRect(); spawn(btn, r.left + r.width / 2, r.top + r.height / 2); }
    });
    btn.addEventListener('click', () => {
      if (!btn.hasAttribute('aria-pressed')) return;
      const on = btn.getAttribute('aria-pressed') !== 'true';
      btn.setAttribute('aria-pressed', String(on));
      if (label) label.textContent = on ? 'Pause' : 'Play';
    });
  });
  function spawn(btn, cx, cy) {
    const r = btn.getBoundingClientRect();
    const x = cx - r.left, y = cy - r.top;
    const d = Math.max(Math.hypot(x, y), Math.hypot(r.width - x, y), Math.hypot(x, r.height - y), Math.hypot(r.width - x, r.height - y));
    const s = document.createElement('span');
    s.className = 'pp-23__ripple';
    s.style.cssText = 'left:' + (x - d) + 'px;top:' + (y - d) + 'px;width:' + 2 * d + 'px;height:' + 2 * d + 'px';
    s.addEventListener('animationend', () => s.remove());
    btn.appendChild(s);
  }
})();
```
