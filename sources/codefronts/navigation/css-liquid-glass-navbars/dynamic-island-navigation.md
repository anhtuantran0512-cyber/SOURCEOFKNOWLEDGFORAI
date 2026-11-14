---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/dynamic-island-navigation/"
title: "Dynamic Island Navigation"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A compact glass pill, in the spirit of the Dynamic Island, that morphs organically between states: it rests as a slim capsule, then fluidly stretches and…"
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dynamic Island Navigation
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/dynamic-island-navigation/

A compact glass pill, in the spirit of the Dynamic Island, that morphs organically between states: it rests as a slim capsule, then fluidly stretches and reveals contextual controls when activated. The width, radius and content animate on one spring so the shape feels liquid, not switched.
## HTML
```html
<section class="nb-06" aria-label="Dynamic Island navigation demo">
  <p class="nb-06__hint">Tap the island to morph it open ↑</p>
  <div class="nb-06__island" id="nb-06-island" data-state="idle">
    <button class="nb-06__trigger" id="nb-06-trigger" type="button" aria-expanded="false" aria-controls="nb-06-panel">
      <span class="nb-06__pulse" aria-hidden="true"></span><span class="nb-06__label">Lumen</span>
    </button>
    <div class="nb-06__panel" id="nb-06-panel" role="group" aria-label="Quick navigation">
      <a class="nb-06__act" href="#nb-06" aria-current="page">Home</a>
      <a class="nb-06__act" href="#nb-06">Search</a>
      <a class="nb-06__act" href="#nb-06">Alerts</a>
      <a class="nb-06__act" href="#nb-06">You</a>
    </div>
  </div>
</section>
```
## CSS
```css
.nb-06,
.nb-06 *,
.nb-06 *::before,
.nb-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-06 {
  --accent: oklch(0.7 0.18 150);
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding-top: 60px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(circle at 30% 30%,#0f3d2e,#05100b 70%),url('https://picsum.photos/seed/nb06/1000/700') center/cover;
  background-blend-mode: overlay;
}

.nb-06__hint {
  color: rgba(255,255,255,.75);
  font-size: 14px;
  margin-bottom: 20px;
}

.nb-06__island {
  position: relative;
  overflow: hidden;
  width: 184px;
  height: 46px;
  border-radius: 999px;
  isolation: isolate;
  background: color-mix(in oklab,black 40%,transparent);
  border: 1px solid rgba(255,255,255,.22);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 24px 50px -22px rgba(0,0,0,.8);
  backdrop-filter: blur(28px) saturate(160%);
  -webkit-backdrop-filter: blur(28px) saturate(160%);
  transition: width .55s cubic-bezier(.34,1.4,.5,1),height .55s cubic-bezier(.34,1.4,.5,1),border-radius .55s;
}

.nb-06__island[data-state="expanded"] {
  width: 300px;
  height: 152px;
  border-radius: 30px;
}

.nb-06__trigger {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  border: 0;
  background: none;
  color: #fff;
  font-family: inherit;
  font-size: 15px;
  font-weight: 700;
  line-height: 1;
  cursor: pointer;
  z-index: 2;
}

.nb-06__label {
  display: inline-block;
  line-height: 1;
}

.nb-06__pulse {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 12px var(--accent);
  animation: nb-06-pulse 2.4s ease-in-out infinite;
  flex: none;
}

@keyframes nb-06-pulse {
  50% {
    transform: scale(1.35);
    opacity: .6;
  }
}

.nb-06__panel {
  position: absolute;
  top: 46px;
  left: 0;
  right: 0;
  bottom: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  padding: 0 16px 16px;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s;
}

.nb-06__island[data-state="expanded"] .nb-06__panel {
  opacity: 1;
  pointer-events: auto;
  transition: opacity .3s .2s;
}

.nb-06__act {
  min-height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  text-decoration: none;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.16);
  transition: background .2s;
}

.nb-06__act[aria-current] {
  background: var(--accent);
  color: #04120b;
}

.nb-06__act:hover {
  background: rgba(255,255,255,.2);
}

.nb-06__act:focus-visible,
.nb-06__trigger:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-06__island {
    transition: none;
  }

  .nb-06__pulse {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const island = document.querySelector('#nb-06-island');
  const trigger = document.querySelector('#nb-06-trigger');
  const panel = document.querySelector('#nb-06-panel');
  if (!island || !trigger) return;
  function set(open){
    island.dataset.state = open ? 'expanded' : 'idle';
    trigger.setAttribute('aria-expanded', String(open));
    if (open) panel.querySelector('a').focus();
  }
  trigger.addEventListener('click', () => set(island.dataset.state !== 'expanded'));
  island.addEventListener('keydown', e => { if (e.key === 'Escape'){ set(false); trigger.focus(); } });
})();
```
