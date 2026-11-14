---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/inner-glow-border-toggle-button-pressed-state/"
title: "Inner Glow Border Toggle Button (Pressed State)"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "A media-player toggle where the light physically relocates: off, the glow rings the outside of the border; press it, and the same light collapses inward as…"
has_js: "true"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inner Glow Border Toggle Button (Pressed State)
Source: https://codefronts.com/components/css-glowing-border-buttons/inner-glow-border-toggle-button-pressed-state/

A media-player toggle where the light physically relocates: off, the glow rings the outside of the border; press it, and the same light collapses inward as an inset flare — the button looks lit from within while playing. Five lines of JS manage aria-pressed; CSS does all the optics.
## HTML
```html
<section class="gbb-10" aria-label="Inner glow pressed toggle button demo">
  <button class="gbb-10__btn" type="button" aria-pressed="false">
    <span class="gbb-10__dot" aria-hidden="true"></span>
    <span class="gbb-10__off">Play Stream</span>
    <span class="gbb-10__on">Now Playing</span>
  </button>
</section>
```
## CSS
```css
.gbb-10,
.gbb-10 *,
.gbb-10 *::before,
.gbb-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-10 {
  --led: oklch(0.8 0.17 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(60% 75% at 50% 0%,oklch(0.19 0.03 200 / .6),transparent 60%),oklch(0.13 0.015 250);
}

.gbb-10 .gbb-10__btn {
  display: inline-flex;
  align-items: center;
  gap: 11px;
  cursor: pointer;
  border: 2px solid color-mix(in oklab,var(--led) 55%,transparent);
  border-radius: 999px;
  padding: 15px 30px;
  font: 700 14px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .04em;
  color: #eafff5;
  background: oklch(0.17 0.02 250);
  box-shadow: 0 0 18px color-mix(in oklab,var(--led) 30%,transparent),0 0 4px color-mix(in oklab,var(--led) 40%,transparent),inset 0 0 22px color-mix(in oklab,var(--led) 0%,transparent),inset 0 0 6px color-mix(in oklab,var(--led) 0%,transparent);
  transition: box-shadow .35s ease,transform .2s ease,background .35s ease,border-color .35s ease;
}

.gbb-10 .gbb-10__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--led);
  box-shadow: 0 0 8px var(--led);
  transition: box-shadow .35s ease;
}

.gbb-10 .gbb-10__on {
  display: none;
}

.gbb-10 .gbb-10__btn[aria-pressed="true"] {
  transform: translateY(1px);
  border-color: var(--led);
  background: color-mix(in oklab,var(--led) 8%,oklch(0.15 0.02 250));
  box-shadow: 0 0 18px color-mix(in oklab,var(--led) 6%,transparent),0 0 4px color-mix(in oklab,var(--led) 8%,transparent),inset 0 0 22px color-mix(in oklab,var(--led) 30%,transparent),inset 0 0 6px color-mix(in oklab,var(--led) 55%,transparent);
}

.gbb-10 .gbb-10__btn[aria-pressed="true"] .gbb-10__dot {
  box-shadow: 0 0 12px var(--led),0 0 26px var(--led);
  animation: gbb10-led 1.2s ease-in-out infinite;
}

.gbb-10 .gbb-10__btn[aria-pressed="true"] .gbb-10__off {
  display: none;
}

.gbb-10 .gbb-10__btn[aria-pressed="true"] .gbb-10__on {
  display: inline;
}

.gbb-10 .gbb-10__btn:focus-visible {
  outline: 2px solid var(--led);
  outline-offset: 4px;
}

@keyframes gbb10-led {
  50% {
    opacity: .55;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-10 .gbb-10__btn {
    transition: none;
  }

  .gbb-10 .gbb-10__btn[aria-pressed="true"] .gbb-10__dot {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  // aria-pressed IS the state — CSS selects on it, so ARIA and visuals can never drift.
  // querySelectorAll so multiple .gbb-10 instances on one page all wire up.
  document.querySelectorAll('.gbb-10 .gbb-10__btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      btn.setAttribute('aria-pressed', String(btn.getAttribute('aria-pressed') !== 'true'));
    });
  });
})();
```
