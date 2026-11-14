---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/cursor-spotlight/"
title: "Cursor Spotlight"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A sophisticated dark CTA with a soft circle of light that follows the cursor across its surface — the button appears lit by a moving spotlight."
has_js: "true"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cursor Spotlight
Source: https://codefronts.com/motion/css-button-hover-effects/cursor-spotlight/

A sophisticated dark CTA with a soft circle of light that follows the cursor across its surface — the button appears lit by a moving spotlight.
## HTML
```html
<div class="bhe-32-group">
<section class="bhe-32a" aria-label="Cursor spotlight button">
  <button class="bhe-32a__btn" id="bhe-32a-btn" type="button"><span>Explore features</span></button>
</section>
<section class="bhe-32b" aria-label="Cursor glow border button">
  <button class="bhe-32b__btn" id="bhe-32b-btn" type="button"><span>View pricing</span></button>
</section>
</div>
```
## CSS
```css
.bhe-32-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-32-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-32a,
.bhe-32a *,
.bhe-32a *::before,
.bhe-32a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-32a {
  --base: #14131c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #08070d;
}

.bhe-32a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 700;
  color: #f4f3ff;
  padding: 18px 42px;
  border: 1px solid rgba(255,255,255,.14);
  border-radius: 12px;
  cursor: pointer;
  background: var(--base);
}

.bhe-32a__btn span {
  position: relative;
  z-index: 1;
}

.bhe-32a__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(160px 160px at var(--mx,50%) var(--my,50%),rgba(140,120,255,.55),rgba(140,120,255,0) 60%);
  opacity: var(--lit,0);
  transition: opacity .3s;
  z-index: 0;
}

.bhe-32a__btn:hover,
.bhe-32a__btn:focus-visible {
  border-color: rgba(255,255,255,.3);
}

.bhe-32a__btn:focus-visible {
  outline: 3px solid #8c78ff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-32a__btn::before {
    transition: none;
  }
}

.bhe-32b,
.bhe-32b *,
.bhe-32b *::before,
.bhe-32b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-32b {
  --base: #0f1a1c;
  --glow: oklch(0.75 0.15 190);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #060d0e;
}

.bhe-32b__btn {
  position: relative;
  isolation: isolate;
  font-size: 16px;
  font-weight: 700;
  color: #eafffb;
  padding: 18px 42px;
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 12px;
  cursor: pointer;
  background: var(--base);
}

.bhe-32b__btn span {
  position: relative;
  z-index: 1;
}

.bhe-32b__btn::before {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: 13px;
  padding: 1px;
  background: radial-gradient(120px 120px at var(--mx,50%) var(--my,50%),var(--glow),transparent 70%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: var(--lit,0);
  transition: opacity .3s;
  z-index: 0;
}

.bhe-32b__btn:focus-visible {
  outline: 3px solid var(--glow);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-32b__btn::before {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('#bhe-32a-btn'); if (!btn) return;
  btn.addEventListener('pointermove', e => { const r=btn.getBoundingClientRect(); btn.style.setProperty('--mx',(e.clientX-r.left)+'px'); btn.style.setProperty('--my',(e.clientY-r.top)+'px'); btn.style.setProperty('--lit','1'); });
  btn.addEventListener('pointerleave', () => btn.style.setProperty('--lit','0'));
  btn.addEventListener('focus', () => { btn.style.setProperty('--mx','50%'); btn.style.setProperty('--my','50%'); btn.style.setProperty('--lit','1'); });
  btn.addEventListener('blur', () => btn.style.setProperty('--lit','0'));
})();
(() => {
  const btn = document.querySelector('#bhe-32b-btn'); if (!btn) return;
  btn.addEventListener('pointermove', e => { const r=btn.getBoundingClientRect(); btn.style.setProperty('--mx',(e.clientX-r.left)+'px'); btn.style.setProperty('--my',(e.clientY-r.top)+'px'); btn.style.setProperty('--lit','1'); });
  btn.addEventListener('pointerleave', () => btn.style.setProperty('--lit','0'));
  btn.addEventListener('focus', () => { btn.style.setProperty('--mx','50%'); btn.style.setProperty('--my','50%'); btn.style.setProperty('--lit','1'); });
  btn.addEventListener('blur', () => btn.style.setProperty('--lit','0'));
})();
```
