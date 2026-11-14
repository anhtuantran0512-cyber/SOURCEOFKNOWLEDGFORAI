---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/video-lightbox-modal/"
title: "Video Lightbox Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A YouTube/Vimeo video lightbox modal with a signature Glitch/Corrupt Materialize entrance — the modal appears through a chromatic RGB-split glitch flicker…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Lightbox Modal
Source: https://codefronts.com/components/css-modals/video-lightbox-modal/

A YouTube/Vimeo video lightbox modal with a signature Glitch/Corrupt Materialize entrance — the modal appears through a chromatic RGB-split glitch flicker (matches the Terminal 404 aesthetic from the Slide-In collection Demo #18). Full-screen dark backdrop, centered video container with 16:9 aspect ratio, play button overlay. Distinctive dev-culture entrance for media contexts where technical aesthetic works (streaming platforms, dev tool demos, portfolio reels).
## HTML
```html
<div class="md-08">
  <button class="md-08__trigger" id="md-08-open">▶ Watch demo · 2:14</button>
  <div class="md-08__backdrop" id="md-08-dialog" role="dialog" aria-modal="true" aria-labelledby="md-08-title">
    <button class="md-08__x md-08__close" aria-label="Close video">✕</button>
    <div class="md-08__stage">
      <h2 class="md-08__title" id="md-08-title">Product demo · 2:14</h2>
      <div class="md-08__video" data-text="Video player">
        <div class="md-08__play" aria-hidden="true">▶</div>
      </div>
      <p class="md-08__meta">
        <span>How Northlight ships design updates in hours</span>
        <a href="#">Transcript</a>
      </p>
    </div>
  </div>
</div>
```
## CSS
```css
.md-08 {
  --page-bg: #0a0a0f;
  --red: #ff3d40;
  --cyan: #00fff9;
  --white: #e2e8f0;
  --sub: #94a3b8;
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

.md-08 *,
.md-08 *::before,
.md-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-08 ::selection {
  background: var(--cyan);
  color: #0a0a0f;
}

.md-08__trigger {
  padding: 14px 28px;
  border: 1px solid var(--white);
  border-radius: 8px;
  background: transparent;
  color: var(--white);
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: .02em;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-08__trigger:hover {
  background: var(--white);
  color: var(--page-bg);
}

.md-08__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: rgba(0,0,0,.92);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

.md-08__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .3s ease,visibility 0s linear 0s;
}

.md-08__x {
  position: absolute;
  top: 20px;
  right: 24px;
  width: 40px;
  height: 40px;
  border: 1px solid rgba(226,232,240,.24);
  border-radius: 50%;
  background: transparent;
  color: var(--white);
  font-family: inherit;
  font-size: 18px;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
}

.md-08__x:hover {
  background: rgba(226,232,240,.1);
  transform: rotate(90deg);
}

.md-08__stage {
  position: relative;
  width: min(820px,100%);
  /* Signature entrance: Glitch/Corrupt Materialize */
  opacity: 0;
  transition: opacity .1s steps(4) .1s;
}

.md-08__backdrop.is-open .md-08__stage {
  opacity: 1;
}

.md-08__title {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 14px;
}

.md-08__video {
  position: relative;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg,#1a1a2e,#0f0f1a);
  border: 1px solid rgba(226,232,240,.14);
  border-radius: 6px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* Chromatic aberration pseudo-elements */

.md-08__backdrop.is-open .md-08__video::before,
.md-08__backdrop.is-open .md-08__video::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,#1a1a2e,#0f0f1a);
  animation: md-08-glitch .5s steps(2) forwards;
  pointer-events: none;
  mix-blend-mode: screen;
}

.md-08__backdrop.is-open .md-08__video::before {
  background: linear-gradient(135deg,rgba(255,61,64,.35),rgba(255,61,64,.15));
  clip-path: polygon(0 15%, 100% 15%, 100% 35%, 0 35%);
  transform: translate(-4px, 0);
}

.md-08__backdrop.is-open .md-08__video::after {
  background: linear-gradient(135deg,rgba(0,255,249,.35),rgba(0,255,249,.15));
  clip-path: polygon(0 60%, 100% 60%, 100% 80%, 0 80%);
  transform: translate(4px, 0);
}

@keyframes md-08-glitch {
  0% {
    opacity: .9;
    transform: translate(-4px, 0);
  }

  25% {
    opacity: .7;
    transform: translate(4px, 0);
  }

  50% {
    opacity: .5;
    transform: translate(-2px, 0);
  }

  75% {
    opacity: .3;
    transform: translate(2px, 0);
  }

  100% {
    opacity: 0;
    transform: translate(0, 0);
  }
}

.md-08__play {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: rgba(226,232,240,.14);
  border: 1px solid rgba(226,232,240,.24);
  color: var(--white);
  font-size: 28px;
  padding-left: 6px;
  cursor: pointer;
  box-shadow: 0 0 40px rgba(226,232,240,.16);
  transition: background .18s ease,transform .18s ease;
}

.md-08__play:hover {
  background: rgba(226,232,240,.24);
  transform: scale(1.08);
}

.md-08__meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  margin-top: 14px;
  font-size: .85rem;
  color: var(--sub);
}

.md-08__meta a {
  color: var(--cyan);
  text-decoration: none;
  font-weight: 600;
}

.md-08__meta a:hover {
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .md-08__backdrop,
    .md-08__stage,
    .md-08__video::before,
    .md-08__video::after {
    transition: none!important;
    animation: none!important;
  }

  .md-08__video::before,
    .md-08__video::after {
    display: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-08');
  if (!root) return;
  var openBtn = root.querySelector('#md-08-open');
  var dialog = root.querySelector('#md-08-dialog');
  var closeBtns = root.querySelectorAll('.md-08__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus close button — video contexts users often want to close quickly
    var closeBtn = dialog.querySelector('.md-08__x');
    if (closeBtn) closeBtn.focus();
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
