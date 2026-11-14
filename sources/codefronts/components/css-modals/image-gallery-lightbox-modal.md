---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/image-gallery-lightbox-modal/"
title: "Image Gallery Lightbox Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A portfolio/photography image lightbox modal with a signature Clip-Path Diamond Reveal entrance — the modal reveals through a diamond-shaped clip-path…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Image Gallery Lightbox Modal
Source: https://codefronts.com/components/css-modals/image-gallery-lightbox-modal/

A portfolio/photography image lightbox modal with a signature Clip-Path Diamond Reveal entrance — the modal reveals through a diamond-shaped clip-path expanding from center, creating a distinctive geometric aperture unlike any standard fade or slide. Full-screen dark backdrop, centered image with caption + navigation arrows + image counter. Full intensity — image galleries are visual-first contexts where decorative entrance is expected and welcomed.
## HTML
```html
<div class="md-09">
  <button class="md-09__trigger" id="md-09-open">Open gallery · 12 photos</button>
  <div class="md-09__backdrop" id="md-09-dialog" role="dialog" aria-modal="true" aria-labelledby="md-09-title">
    <button class="md-09__x md-09__close" aria-label="Close gallery">✕</button>
    <button class="md-09__nav md-09__nav--prev" aria-label="Previous image">◄</button>
    <button class="md-09__nav md-09__nav--next" aria-label="Next image">►</button>
    <div class="md-09__stage">
      <h2 class="md-09__title" id="md-09-title">Portfolio · 2026 selections</h2>
      <div class="md-09__image" style="--g:linear-gradient(135deg,#7c6cff,#ec4899,#f97316)">
        <span class="md-09__counter">3 / 12</span>
      </div>
      <div class="md-09__caption">
        <p><strong>Northlight fintech dashboard · Q3 2026</strong></p>
        <p>Design system refresh · 200+ components migrated · 4× ship velocity</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-09 {
  --page-bg: #0a0a0f;
  --white: #f5f5fa;
  --sub: #94a3b8;
  --brand: #a78bfa;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: var(--page-bg);
  color: var(--white);
}

.md-09 *,
.md-09 *::before,
.md-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-09 ::selection {
  background: var(--brand);
  color: #0a0a0f;
}

.md-09__trigger {
  padding: 12px 26px;
  border: 1px solid var(--brand);
  border-radius: 8px;
  background: transparent;
  color: var(--brand);
  font-family: inherit;
  font-size: .92rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-09__trigger:hover {
  background: var(--brand);
  color: #0a0a0f;
}

.md-09__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: rgba(0,0,0,.94);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

.md-09__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .3s ease,visibility 0s linear 0s;
}

.md-09__x,
.md-09__nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 44px;
  height: 44px;
  border: 1px solid rgba(245,245,250,.2);
  border-radius: 50%;
  background: rgba(255,255,255,.06);
  color: var(--white);
  font-family: inherit;
  font-size: 16px;
  cursor: pointer;
  transition: background .18s ease,transform .18s ease;
}

.md-09__x {
  top: 20px;
  right: 24px;
  transform: none;
}

.md-09__x:hover {
  background: rgba(255,255,255,.14);
  transform: rotate(90deg);
}

.md-09__nav--prev {
  left: 24px;
}

.md-09__nav--next {
  right: 24px;
}

.md-09__nav:hover {
  background: rgba(255,255,255,.14);
}

.md-09__stage {
  position: relative;
  width: min(820px,100%);
  /* Signature entrance: Clip-Path Diamond Reveal */
  opacity: 0;
  clip-path: polygon(50% 50%, 50% 50%, 50% 50%, 50% 50%);
  transition: opacity .3s ease .1s,clip-path .6s cubic-bezier(.65,0,.35,1) .1s;
}

.md-09__backdrop.is-open .md-09__stage {
  opacity: 1;
  clip-path: polygon(50% -50%, 150% 50%, 50% 150%, -50% 50%);
}

.md-09__title {
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 14px;
  text-align: center;
}

.md-09__image {
  position: relative;
  aspect-ratio: 16/10;
  background: var(--g);
  border-radius: 6px;
  overflow: hidden;
}

.md-09__counter {
  position: absolute;
  top: 14px;
  right: 14px;
  padding: 5px 12px;
  border-radius: 999px;
  background: rgba(0,0,0,.5);
  color: var(--white);
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .06em;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}

.md-09__caption {
  text-align: center;
  margin-top: 16px;
}

.md-09__caption p {
  font-size: .85rem;
  color: var(--sub);
  line-height: 1.5;
}

.md-09__caption p strong {
  color: var(--white);
  font-weight: 600;
  display: block;
  margin-bottom: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .md-09__backdrop,
    .md-09__stage {
    transition: none!important;
  }

  .md-09__stage {
    clip-path: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-09');
  if (!root) return;
  var openBtn = root.querySelector('#md-09-open');
  var dialog = root.querySelector('#md-09-dialog');
  var closeBtns = root.querySelectorAll('.md-09__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus next arrow — gallery contexts expect keyboard nav to arrow keys
    var next = dialog.querySelector('.md-09__nav--next');
    if (next) next.focus();
    document.addEventListener('keydown', onKey);
  }
  function close() {
    dialog.classList.remove('is-open');
    document.documentElement.style.overflow = '';
    document.removeEventListener('keydown', onKey);
    if (lastFocus) lastFocus.focus();
  }
  function onKey(e) { if (e.key === 'Escape') close(); }

  openBtn.addEventListener('click', open);
  closeBtns.forEach(function(b){ b.addEventListener('click', close); });
  dialog.addEventListener('click', function(e){ if (e.target === dialog) close(); });
})();
```
