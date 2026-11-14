---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/magnetic-hover-fab/"
title: "Magnetic Cursor Follower Floating Button CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "The award-site magnetic button, built properly: the button leans toward the pointer within a proximity field, the icon lags slightly behind the shell for…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Cursor Follower Floating Button CSS
Source: https://codefronts.com/components/css-floating-buttons/magnetic-hover-fab/

The award-site magnetic button, built properly: the button leans toward the pointer within a proximity field, the icon lags slightly behind the shell for parallax depth, and everything springs home on exit. Pointer-only by design — it detects fine pointers and hover capability and skips the whole effect on touch, where it would just be dead weight.
## HTML
```html
<section class="fb-23" aria-label="Magnetic cursor follower button demo">
  <div class="fb-23__stage">
    <p class="fb-23__eyebrow">proximity field · linear falloff</p>
    <h2 class="fb-23__title">It leans toward you</h2>
    <p class="fb-23__sub">Move the pointer near the button — not onto it. The shell follows at 34%, the icon at 16%, and the difference is what gives it depth.</p>
    <div class="fb-23__field" id="fb-23-field">
      <span class="fb-23__halo" aria-hidden="true"></span>
      <button class="fb-23__fab" id="fb-23-fab" type="button" aria-label="Start a project">
        <span class="fb-23__ico" id="fb-23-ico" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      </button>
    </div>
    <p class="fb-23__chip" id="fb-23-chip">pointer: fine · pull 0.34 / 0.16 · spring return 520ms</p>
  </div>
</section>
```
## CSS
```css
.fb-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-23-bg);
  --fb-23-bg: radial-gradient(90% 70% at 50% 42%,oklch(0.29 0.03 285),oklch(0.14 0.015 285) 70%);
  --fb-23-accent: oklch(0.86 0.18 95);
  --fb-23-ink: oklch(0.97 0.008 285);
  --fb-23-mut: oklch(0.74 0.015 285);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-23-ink);
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
}

.fb-23 *,
.fb-23 *::before,
.fb-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-23__stage {
  width: min(100%,58ch);
  display: grid;
  gap: clamp(16px,3vw,26px);
  justify-items: center;
  text-align: center;
}

.fb-23__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-23-accent);
}

.fb-23__title {
  font-size: clamp(27px,5vw,48px);
  line-height: 1.04;
  letter-spacing: -.035em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-23__sub {
  max-width: 48ch;
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-23-mut);
  text-wrap: pretty;
}

.fb-23__field {
  position: relative;
  display: grid;
  place-items: center;
  width: min(88vw,340px);
  height: min(38svh,240px);
  border-radius: 28px;
}

.fb-23__halo {
  position: absolute;
  width: 230px;
  height: 230px;
  border-radius: 50%;
  border: 1px dashed oklch(1 0 0/.14);
  opacity: .7;
}

.fb-23__halo::after {
  content: "";
  position: absolute;
  inset: 44px;
  border-radius: 50%;
  border: 1px dashed oklch(1 0 0/.1);
}

.fb-23__fab {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 96px;
  block-size: 96px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.17 0.04 95);
  background: radial-gradient(120% 120% at 32% 26%,oklch(0.96 0.13 100),var(--fb-23-accent));
  box-shadow: 0 22px 60px -18px oklch(0.86 0.18 95/.5),0 3px 10px oklch(0.08 0.01 285/.7);
  transition: translate .52s cubic-bezier(.2,1.5,.35,1),scale .3s cubic-bezier(.2,1.4,.4,1),box-shadow .3s ease;
}

.fb-23__fab[data-following="true"] {
  transition: scale .3s cubic-bezier(.2,1.4,.4,1),box-shadow .3s ease;
}

.fb-23__fab svg {
  width: 32px;
  height: 32px;
}

.fb-23__ico {
  display: grid;
  place-items: center;
  transition: translate .52s cubic-bezier(.2,1.5,.35,1);
}

.fb-23__fab[data-following="true"] .fb-23__ico {
  transition: none;
}

.fb-23__fab:hover {
  scale: 1.06;
  box-shadow: 0 30px 76px -18px oklch(0.86 0.18 95/.6),0 3px 10px oklch(0.08 0.01 285/.7);
}

.fb-23__fab:active {
  scale: .95;
}

.fb-23__fab:focus-visible {
  outline: 3px solid var(--fb-23-accent);
  outline-offset: 8px;
}

.fb-23__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-23-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .fb-23__fab,
    .fb-23__ico {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const field = document.getElementById('fb-23-field');
  const fab = document.getElementById('fb-23-fab');
  const ico = document.getElementById('fb-23-ico');
  const chip = document.getElementById('fb-23-chip');
  if (!field || !fab || fab.dataset.fbWired) return;
  fab.dataset.fbWired = '1';
  const fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  const calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!fine || calm) {
    chip.textContent = calm ? 'reduced motion — magnetism disabled' : 'coarse pointer — magnetism disabled on touch';
    return;
  }
  const RADIUS = 165;
  let box = null;
  const measure = () => { box = fab.getBoundingClientRect(); };
  field.addEventListener('pointerenter', measure);
  window.addEventListener('resize', () => { box = null; });
  field.addEventListener('pointermove', (e) => {
    if (!box) measure();
    const cx = box.left + box.width / 2, cy = box.top + box.height / 2;
    const dx = e.clientX - cx, dy = e.clientY - cy;
    const pull = Math.max(0, 1 - Math.hypot(dx, dy) / RADIUS);
    if (pull <= 0) return;
    fab.dataset.following = 'true';
    fab.style.translate = (dx * pull * 0.34).toFixed(1) + 'px ' + (dy * pull * 0.34).toFixed(1) + 'px';
    ico.style.translate = (dx * pull * 0.16).toFixed(1) + 'px ' + (dy * pull * 0.16).toFixed(1) + 'px';
  });
  field.addEventListener('pointerleave', () => {
    fab.dataset.following = 'false';
    fab.style.translate = '';
    ico.style.translate = '';
    box = null;
  });
})();
```
