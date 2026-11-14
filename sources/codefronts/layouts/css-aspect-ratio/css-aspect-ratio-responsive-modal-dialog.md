---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-responsive-modal-dialog/"
title: "CSS Aspect Ratio Responsive Modal Dialog"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "A trailer lightbox on the native <dialog> element, sized by one honest equation: width:min(92vw, 88svh × 16/9, 1080px) plus aspect-ratio:16/9 — so the modal…"
has_js: "true"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Responsive Modal Dialog
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-responsive-modal-dialog/

A trailer lightbox on the native <dialog> element, sized by one honest equation: width:min(92vw, 88svh × 16/9, 1080px) plus aspect-ratio:16/9 — so the modal is always the largest 16:9 rectangle that fits the screen, portrait or landscape, phone or ultrawide. ::backdrop gets real blur, @starting-style animates the open, form method='dialog' closes without JavaScript, and the 9 lines of JS do exactly two things: showModal() and light-dismiss. The poster wall behind it runs 2:3 — movie-jacket ratio — for free contrast.
## HTML
```html
<section class="car-11" aria-label="Responsive modal dialog demo">
  <div class="car-11__stage" id="car11-top">
    <header class="car-11__bar">
      <a class="car-11__brand" href="#car11-top">HALCYON<span>PICTURES</span></a>
      <span class="car-11__chip">dialog = largest 16:9 that fits</span>
    </header>
    <main class="car-11__main">
      <div class="car-11__feature">
        <p class="car-11__kicker">In cinemas October 2026</p>
        <h1>Signal Fade</h1>
        <p class="car-11__sub">A radio operator on a decommissioned lighthouse hears tomorrow's weather — one broadcast too early. The trailer opens in a native <code>&lt;dialog&gt;</code> sized by <code>aspect-ratio</code>, never by JavaScript.</p>
        <div class="car-11__row">
          <button class="car-11__btn car-11__btn--solid" type="button" data-open="car11-trailer"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>Watch trailer</button>
          <a class="car-11__btn" href="#car11-top">Tickets</a>
        </div>
      </div>
      <ul class="car-11__posters" aria-label="Also playing — posters are 2:3">
        <li><button type="button" data-open="car11-trailer" style="--img:url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=700&h=1050&auto=format&fit=crop')"><b>Redline Hour</b><span>2:3 poster · opens the 16:9 dialog</span></button></li>
        <li><button type="button" data-open="car11-trailer" style="--img:url('https://images.unsplash.com/photo-1478720568477-152d9b164e26?q=80&w=700&h=1050&auto=format&fit=crop')"><b>The Projectionist</b><span>2:3 poster · opens the 16:9 dialog</span></button></li>
        <li><button type="button" data-open="car11-trailer" style="--img:url('https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=700&h=1050&auto=format&fit=crop')"><b>Matinee</b><span>2:3 poster · opens the 16:9 dialog</span></button></li>
      </ul>
    </main>
    <footer class="car-11__foot">Resize the pane, then reopen the dialog: <code>min(92vw, 88svh×16/9, 1080px)</code> re-picks the binding constraint every time. A demo from the CodeFronts aspect-ratio collection.</footer>
    <dialog class="car-11__dialog" id="car11-trailer" aria-label="Trailer: Signal Fade">
      <div class="car-11__dialog-media" style="--img:url('https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=1600&h=900&auto=format&fit=crop')">
        <header>
          <h2>Signal Fade — official trailer</h2>
          <button type="button" class="car-11__close" data-close="car11-trailer" aria-label="Close trailer">✕</button>
        </header>
        <p class="car-11__dialog-note"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>Your player embed goes here — the box is already a perfect 16:9 at every screen size. Press <kbd>Esc</kbd> or click outside to close.</p>
      </div>
    </dialog>
  </div>
</section>
```
## CSS
```css
.car-11,
.car-11 *,
.car-11 *::before,
.car-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-11 {
  --bg: oklch(0.16 0.025 290);
  --ink: oklch(0.95 0.008 290);
  --mut: oklch(0.68 0.02 290);
  --line: oklch(0.32 0.03 290);
  --acc: oklch(0.78 0.14 70);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-11__stage {
  width: 100%;
  container: car11/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  background: radial-gradient(100cqi 70cqi at 15% -10%,oklch(0.3 0.07 320/.45),transparent 65%),var(--bg);
}

.car-11__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 18px clamp(16px,4cqi,44px);
}

.car-11__brand {
  font-size: 14px;
  font-weight: 800;
  letter-spacing: .3em;
  color: inherit;
  text-decoration: none;
}

.car-11__brand span {
  display: block;
  font-size: 8.5px;
  letter-spacing: .52em;
  color: var(--acc);
}

.car-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--mut);
  border: 1px solid var(--line);
  padding: 7px 11px;
  border-radius: 99px;
}

.car-11__main {
  flex: 1;
  display: grid;
  grid-template-columns: minmax(0,5fr) minmax(0,6fr);
  gap: clamp(20px,4cqi,52px);
  align-items: center;
  padding: clamp(16px,3cqi,32px) clamp(16px,4cqi,44px);
}

.car-11__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc);
}

.car-11__feature h1 {
  font-size: clamp(36px,6.5cqi,64px);
  letter-spacing: -.03em;
  font-weight: 800;
  line-height: 1;
  margin-top: 10px;
}

.car-11__sub {
  margin-top: 14px;
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 46ch;
}

.car-11__sub code,
.car-11__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: oklch(0.26 0.03 290);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.car-11__row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 24px;
}

.car-11__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 48px;
  padding: 0 22px;
  border-radius: 12px;
  font: inherit;
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  color: var(--ink);
  border: 1.5px solid var(--line);
  background: oklch(0.22 0.03 290/.6);
  cursor: pointer;
  transition: border-color .2s,translate .2s,background .2s;
}

.car-11__btn:hover,
.car-11__btn:focus-visible {
  border-color: var(--acc);
  translate: 0 -2px;
}

.car-11__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.car-11__btn--solid {
  background: var(--acc);
  border-color: var(--acc);
  color: oklch(0.22 0.05 70);
}

.car-11__btn--solid:hover,
.car-11__btn--solid:focus-visible {
  background: color-mix(in oklch,var(--acc) 87%,white);
}

.car-11__posters {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: clamp(10px,2cqi,18px);
  align-items: end;
}

.car-11__posters button {
  position: relative;
  width: 100%;
  aspect-ratio: 2/3;
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 3px;
  padding: 14px;
  text-align: left;
  color: oklch(0.97 0 0);
  font: inherit;
  background-color: oklch(0.28 0.04 290);
  background-image: linear-gradient(to bottom,oklch(0.2 0.03 290/.05) 45%,oklch(0.13 0.03 290/.88)),var(--img);
  background-size: cover;
  background-position: center;
  transition: translate .3s cubic-bezier(.2,.7,.2,1),box-shadow .3s,border-color .3s;
}

.car-11__posters li:nth-child(2) button {
  translate: 0 -14px;
}

.car-11__posters button:hover,
.car-11__posters button:focus-visible {
  translate: 0 -8px;
  border-color: var(--acc);
  box-shadow: 0 18px 44px oklch(0.08 0.03 290/.6);
}

.car-11__posters li:nth-child(2) button:hover,
.car-11__posters li:nth-child(2) button:focus-visible {
  translate: 0 -20px;
}

.car-11__posters button:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.car-11__posters b {
  font-size: clamp(12px,1.8cqi,15px);
  letter-spacing: -.01em;
}

.car-11__posters span {
  font-size: clamp(9px,1.4cqi,10.5px);
  color: oklch(0.85 0.02 290/.85);
}

.car-11__foot {
  padding: 14px clamp(16px,4cqi,44px) 26px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
}

.car-11__dialog {
  margin: auto;
  padding: 0;
  border: 0;
  border-radius: 18px;
  width: min(92vw,1080px);
  width: min(92vw,calc(88svh * (16 / 9)),1080px);
  aspect-ratio: 16/9;
  background: oklch(0.14 0.02 290);
  color: var(--ink);
  box-shadow: 0 40px 120px oklch(0.05 0.02 290/.7);
  opacity: 1;
  scale: 1;
  transition: opacity .3s,scale .3s cubic-bezier(.2,.7,.2,1),display .3s allow-discrete,overlay .3s allow-discrete;
}

.car-11__dialog::backdrop {
  background: oklch(0.13 0.02 290/.62);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: opacity .3s,display .3s allow-discrete,overlay .3s allow-discrete;
}

@starting-style {
  .car-11__dialog[open] {
    opacity: 0;
    scale: .9;
  }

  .car-11__dialog[open]::backdrop {
    opacity: 0;
  }
}

.car-11__dialog:not([open]) {
  opacity: 0;
  scale: .94;
}

.car-11__dialog-media {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-image: linear-gradient(to bottom,oklch(0.12 0.02 290/.72),oklch(0.12 0.02 290/.15) 35%,oklch(0.12 0.02 290/.6)),var(--img);
  background-size: cover;
  background-position: center;
}

.car-11__dialog-media header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 14px 0 20px;
}

.car-11__dialog-media h2 {
  font-size: clamp(13px,2cqi,17px);
  font-weight: 700;
  letter-spacing: -.01em;
}

.car-11__close {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  border: 1px solid oklch(0.9 0.01 290/.3);
  background: oklch(0.15 0.02 290/.55);
  color: var(--ink);
  font-size: 16px;
  cursor: pointer;
  transition: background .2s,rotate .2s;
}

.car-11__close:hover,
.car-11__close:focus-visible {
  background: oklch(0.3 0.04 290/.8);
  rotate: 90deg;
}

.car-11__close:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.car-11__dialog-note {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 20px 18px;
  font-size: clamp(11px,1.6cqi,13px);
  line-height: 1.5;
  color: oklch(0.9 0.01 290);
  max-width: 56ch;
}

.car-11__dialog-note svg {
  flex: none;
  padding: 8px;
  box-sizing: content-box;
  border-radius: 50%;
  background: var(--acc);
  color: oklch(0.22 0.05 70);
}

.car-11__dialog-note kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  border: 1px solid var(--line);
  border-radius: 5px;
  padding: 1px 5px;
  background: oklch(0.22 0.03 290);
}

@container car11 (width < 720px) {
  .car-11__main {
    grid-template-columns: 1fr;
    align-content: start;
  }

  .car-11__posters {
    align-items: stretch;
  }

  .car-11__posters li:nth-child(2) button {
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-11__dialog,
    .car-11__dialog::backdrop {
    transition-duration: .01ms;
  }

  .car-11 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const dlg = document.getElementById('car11-trailer');
  if (!dlg || dlg.dataset.wired) return;
  dlg.dataset.wired = '1';
  // Open triggers (main CTA + poster wall).
  document.querySelectorAll('[data-open="car11-trailer"]').forEach((btn) =>
    btn.addEventListener('click', () => dlg.showModal())
  );
  // Close button — explicit click handler instead of relying on
  // <form method="dialog">, which historically failed in the /try/
  // playground iframe when the sandbox lacked allow-forms. The 2026-08-04
  // sandbox lift added allow-forms to every iframe surface, so
  // <form method="dialog"> would now work — but the explicit handler
  // stays because it's the more portable pattern (works in any host
  // environment regardless of sandbox policy) and doesn't rely on a
  // browser-implicit form-submission side effect.
  document.querySelectorAll('[data-close="car11-trailer"]').forEach((btn) => {
    btn.addEventListener('click', () => dlg.close());
    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); dlg.close(); }
    });
  });
  // Light dismiss: click outside dialog content (backdrop click).
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
})();
```
