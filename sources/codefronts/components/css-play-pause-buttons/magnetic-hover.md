---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/magnetic-hover/"
title: "Magnetic Hover Cursor Play Button"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "The award-site micro-interaction: the button leans toward your cursor as it approaches, the icon lags slightly behind for parallax, and everything springs…"
has_js: "true"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Hover Cursor Play Button
Source: https://codefronts.com/components/css-play-pause-buttons/magnetic-hover/

The award-site micro-interaction: the button leans toward your cursor as it approaches, the icon lags slightly behind for parallax, and everything springs home when you leave. Twenty lines of pointer maths write two custom properties; CSS does all the rendering. Includes the guardrails production versions forget — pointer-type detection, reduced-motion opt-out and a full keyboard path.
## HTML
```html
<section class="pp-21" aria-label="Magnetic hover cursor play button demo">
  <div class="pp-21__stage">
    <div class="pp-21__zone">
      <button class="pp-21__btn" type="button" aria-pressed="false">
        <span class="pp-21__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="28" height="28">
            <path class="pp-21__p" d="M9 5.6v12.8L19 12z" fill="currentColor"/>
            <path class="pp-21__q" d="M8.6 5.6h3.2v12.8H8.6zM12.8 5.6H16v12.8h-3.2z" fill="currentColor"/>
          </svg>
        </span>
        <span class="pp-21__sr">Play the showreel</span>
      </button>
      <span class="pp-21__hint" aria-hidden="true">move closer</span>
    </div>
    <div class="pp-21__cap">
      <p class="pp-21__title">Showreel 2027</p>
      <p class="pp-21__sub">02:14 · sound on</p>
    </div>
    <p class="pp-21__chip" aria-hidden="true">pointermove → 2 custom props · 0.32 pull · icon parallax at 0.35</p>
  </div>
</section>
```
## CSS
```css
.pp-21,
.pp-21 *,
.pp-21 *::before,
.pp-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-21-bg);
  --pp-21-bg: oklch(0.15 0.01 100);
  --pp-21-ink: oklch(0.97 0.01 95);
  --pp-21-mut: oklch(0.66 0.02 95);
  --pp-21-acc: oklch(0.85 0.16 92);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-21-ink);
}

.pp-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(55% 45% at 50% 42%,oklch(0.24 0.05 95/.65),transparent 72%);
}

.pp-21__zone {
  position: relative;
  display: grid;
  place-items: center;
  width: min(90vw,320px);
  height: 240px;
  border-radius: 28px;
  border: 1px dashed oklch(1 0 0/.14);
}

.pp-21__hint {
  position: absolute;
  bottom: 14px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--pp-21-mut);
  opacity: .8;
  transition: opacity .3s;
}

.pp-21__zone:hover .pp-21__hint {
  opacity: 0;
}

.pp-21__btn {
  display: grid;
  place-items: center;
  width: 116px;
  height: 116px;
  border: 0;
  border-radius: 50%;
  background: var(--pp-21-acc);
  color: oklch(0.18 0.04 95);
  cursor: pointer;
  translate: var(--pp-21-x,0) var(--pp-21-y,0);
  box-shadow: 0 18px 44px oklch(0.6 0.14 92/.28);
  transition: translate .35s cubic-bezier(.22,1,.36,1),scale .3s cubic-bezier(.34,1.4,.5,1),background .3s;
}

.pp-21__btn:hover,
.pp-21__btn:focus-visible {
  scale: 1.08;
}

.pp-21__btn:active {
  scale: .96;
}

.pp-21__btn:focus-visible {
  outline: 3px solid var(--pp-21-ink);
  outline-offset: 6px;
}

.pp-21__icon {
  display: grid;
  place-items: center;
  translate: calc(var(--pp-21-x,0px) * .35) calc(var(--pp-21-y,0px) * .35);
  transition: translate .45s cubic-bezier(.22,1,.36,1);
}

.pp-21__q {
  display: none;
}

.pp-21__btn[aria-pressed="true"] {
  background: oklch(0.98 0.01 95);
}

.pp-21__btn[aria-pressed="true"] .pp-21__p {
  display: none;
}

.pp-21__btn[aria-pressed="true"] .pp-21__q {
  display: block;
}

.pp-21__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pp-21__cap {
  text-align: center;
}

.pp-21__title {
  font-size: 19px;
  font-weight: 660;
  letter-spacing: -.015em;
}

.pp-21__sub {
  font-size: 13px;
  color: var(--pp-21-mut);
  margin-top: 5px;
}

.pp-21__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-21-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  margin-top: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .pp-21__btn,
    .pp-21__icon {
    translate: 0 0 !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  const calm = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  document.querySelectorAll('.pp-21__zone').forEach((zone) => {
    if (zone.dataset.wired) return;
    zone.dataset.wired = '1';
    const btn = zone.querySelector('.pp-21__btn');
    const sr = zone.querySelector('.pp-21__sr');
    btn.addEventListener('click', () => {
      const on = btn.getAttribute('aria-pressed') !== 'true';
      btn.setAttribute('aria-pressed', String(on));
      sr.textContent = (on ? 'Pause' : 'Play') + ' the showreel';
    });
    if (!fine || calm) return;
    let box = null;
    const reset = () => { btn.style.setProperty('--pp-21-x', '0px'); btn.style.setProperty('--pp-21-y', '0px'); };
    zone.addEventListener('pointerenter', () => { box = btn.getBoundingClientRect(); });
    zone.addEventListener('pointermove', (e) => {
      if (!box) box = btn.getBoundingClientRect();
      btn.style.setProperty('--pp-21-x', (e.clientX - (box.left + box.width / 2)) * 0.32 + 'px');
      btn.style.setProperty('--pp-21-y', (e.clientY - (box.top + box.height / 2)) * 0.32 + 'px');
    });
    zone.addEventListener('pointerleave', () => { box = null; reset(); });
    btn.addEventListener('blur', reset);
  });
})();
```
