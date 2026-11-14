---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-obsidian-glass-shard-button/"
title: "CSS Obsidian Glass Shard Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A shard of volcanic glass: an asymmetric faceted silhouette from clip-path, near-black translucency over a blurred backdrop, two facet planes shaded by…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Obsidian Glass Shard Button
Source: https://codefronts.com/components/css-buttons/css-obsidian-glass-shard-button/

A shard of volcanic glass: an asymmetric faceted silhouette from clip-path, near-black translucency over a blurred backdrop, two facet planes shaded by overlapping gradients, and a razor of light that runs along the leading edge on hover.
## HTML
```html
<div class="cb-34">
  <div class="cb-34__stage">
    <span class="cb-34__wrap">
      <button class="cb-34__btn" type="button">
        <span class="cb-34__rim" aria-hidden="true"></span>
        <span class="cb-34__edge" aria-hidden="true"></span>
        <span class="cb-34__label">Enter the vault</span>
      </button>
    </span>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&display=swap');

.cb-34 {
  --bg: #07070a;
  --glass: rgba(16,17,22,.82);
  --ink: #eef2f8;
  --glow: #bfe3ff;
  --shape: polygon(4% 0,100% 6%,96% 82%,88% 100%,0 94%,3% 18%);
  --sans: "Syne",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(38rem 22rem at 50% 45%, #14161d, transparent 74%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: light) {
  .cb-34:not([data-theme="dark"]) {
    --bg: #101218;
  }
}

.cb-34[data-theme="light"] {
  --bg: #101218;
}

.cb-34,
.cb-34 *,
.cb-34 *::before,
.cb-34 *::after {
  box-sizing: border-box;
}

.cb-34__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-34__wrap {
  display: inline-block;
  border-radius: .2rem;
  filter: drop-shadow(0 18px 28px rgba(0,0,0,.75)) drop-shadow(0 0 1px rgba(190,225,255,.25));
  transition: translate .35s cubic-bezier(.16,1,.3,1), filter .35s ease;
}

.cb-34__wrap:has(:hover) {
  translate: 0 -3px;
  filter: drop-shadow(0 26px 34px rgba(0,0,0,.8)) drop-shadow(0 0 2px rgba(190,225,255,.45));
}

.cb-34__wrap:has(:focus-visible) {
  outline: 2px solid var(--glow);
  outline-offset: 6px;
}

.cb-34__btn {
  position: relative;
  overflow: hidden;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 3.75rem;
  padding: 0 3rem;
  border: 0;
  clip-path: var(--shape);
  font: inherit;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: .02em;
  color: var(--ink);
  background-image: linear-gradient(122deg, rgba(255,255,255,.1) 0 38%, transparent 38.5%), linear-gradient(-58deg, rgba(255,255,255,.05) 0 30%, transparent 30.5%), linear-gradient(160deg, rgba(52,58,74,.95), rgba(14,16,22,.97));
  background-color: var(--glass);
  -webkit-backdrop-filter: blur(10px) saturate(1.2);
  backdrop-filter: blur(10px) saturate(1.2);
  transition: scale .2s cubic-bezier(.16,1,.3,1);
}

.cb-34__label {
  position: relative;
  z-index: 3;
  text-shadow: 0 1px 10px rgba(0,0,0,.7);
}

.cb-34__rim {
  position: absolute;
  inset: 1px;
  z-index: 1;
  pointer-events: none;
  clip-path: var(--shape);
  box-shadow: inset 0 0 0 1px rgba(190,225,255,.3);
}

.cb-34__edge {
  position: absolute;
  inset: -30% -40%;
  z-index: 2;
  pointer-events: none;
  background: linear-gradient(100deg, transparent 44%, rgba(190,225,255,.85) 50%, transparent 56%);
  translate: -70% 0;
  transition: translate .85s cubic-bezier(.16,1,.3,1);
}

.cb-34__btn:is(:hover,:focus-visible) .cb-34__edge {
  translate: 70% 0;
}

.cb-34__btn:focus-visible {
  outline: none;
}

.cb-34__btn:active {
  scale: .985;
}

.cb-34__btn:disabled {
  cursor: not-allowed;
  color: #7c8494;
}

@media (prefers-reduced-motion: reduce) {
  .cb-34__wrap,
    .cb-34__btn,
    .cb-34__edge {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-34__btn {
    clip-path: none;
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }

  .cb-34__rim,
    .cb-34__edge {
    display: none;
  }

  .cb-34__wrap {
    filter: none;
  }
}
```
