---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-modal-dialog-window/"
title: "Liquid Glass Modal / Dialog Window"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A focus dialog that feels light instead of heavy: opening it blurs the entire page behind a glass scrim, then a translucent panel scales up into place."
has_js: "true"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Modal / Dialog Window
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-modal-dialog-window/

A focus dialog that feels light instead of heavy: opening it blurs the entire page behind a glass scrim, then a translucent panel scales up into place. Built on the native <dialog> element so it's accessible by default — focus is trapped, Escape closes, and the backdrop is real.
## HTML
```html
<section class="lg-05" aria-label="Liquid glass modal demo">
  <img class="lg-05__bg" src="https://picsum.photos/seed/lgmodal/1200/800" width="1200" height="800" alt="Studio workspace">
  <button class="lg-05__open" id="lg-05-open" type="button">Open glass dialog</button>
  <dialog class="lg-05__dialog" id="lg-05-dialog" aria-labelledby="lg-05-title">
    <h3 class="lg-05__title" id="lg-05-title">Confirm upgrade</h3>
    <p class="lg-05__text">You're switching to the Studio plan. Your new features unlock immediately and billing adjusts on your next cycle.</p>
    <div class="lg-05__actions">
      <button class="lg-05__btn" id="lg-05-cancel" type="button">Cancel</button>
      <button class="lg-05__btn lg-05__btn--go" id="lg-05-confirm" type="button">Upgrade</button>
    </div>
  </dialog>
</section>
```
## CSS
```css
.lg-05,
.lg-05 *,
.lg-05 *::before,
.lg-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-05 {
  --accent: oklch(0.62 0.2 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: #0e0b1a;
}

.lg-05__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
}

.lg-05__open {
  position: relative;
  z-index: 1;
  font-size: 16px;
  font-weight: 700;
  color: #fff;
  padding: 15px 30px;
  border-radius: 9999px;
  border: 1px solid rgba(255,255,255,.4);
  cursor: pointer;
  background: color-mix(in oklab,white 16%,transparent);
  backdrop-filter: blur(14px) saturate(160%);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 14px 30px -16px rgba(0,0,0,.6);
  transition: transform .18s;
}

.lg-05__open:hover {
  transform: translateY(-2px);
}

.lg-05__open:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-05__dialog {
  border: none;
  padding: 0;
  background: transparent;
  color: #fff;
  max-width: min(420px,92vw);
}

.lg-05__dialog::backdrop {
  background: rgba(10,8,20,.4);
  backdrop-filter: blur(14px) saturate(140%);
  -webkit-backdrop-filter: blur(14px) saturate(140%);
}

.lg-05__dialog[open] {
  animation: lg-05-in .35s cubic-bezier(.2,.9,.2,1);
}

.lg-05__dialog.lg-05__closing {
  animation: lg-05-out .2s ease forwards;
}

.lg-05__dialog>* {
  position: relative;
}

.lg-05__dialog {
  padding: 30px;
  border-radius: 26px;
  background: color-mix(in oklab,white 16%,transparent);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 40px 80px -30px rgba(0,0,0,.7);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
}

.lg-05__title {
  font-size: 22px;
  font-weight: 800;
  margin-bottom: 10px;
}

.lg-05__text {
  font-size: 15px;
  line-height: 1.6;
  color: rgba(255,255,255,.92);
  text-shadow: 0 1px 6px rgba(0,0,0,.3);
}

.lg-05__actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 24px;
}

.lg-05__btn {
  font-size: 14px;
  font-weight: 700;
  padding: 11px 20px;
  border-radius: 999px;
  cursor: pointer;
  color: #fff;
  border: 1px solid rgba(255,255,255,.35);
  background: rgba(255,255,255,.12);
  transition: background .2s,transform .15s;
}

.lg-05__btn:hover {
  background: rgba(255,255,255,.22);
}

.lg-05__btn--go {
  background: var(--accent);
  border-color: color-mix(in oklab,var(--accent) 40%,white);
}

.lg-05__btn:active {
  transform: scale(.96);
}

.lg-05__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

@keyframes lg-05-in {
  from {
    transform: scale(.9);
    opacity: 0;
  }

  to {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes lg-05-out {
  to {
    transform: scale(.95);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-05__dialog[open],
    .lg-05__dialog.lg-05__closing {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.lg-05');
  const dlg = root.querySelector('#lg-05-dialog');
  const open = root.querySelector('#lg-05-open');
  const close = () => {
    dlg.classList.add('lg-05__closing');
    dlg.addEventListener('animationend', () => { dlg.classList.remove('lg-05__closing'); dlg.close(); }, {once:true});
    if (matchMedia('(prefers-reduced-motion: reduce)').matches){ dlg.classList.remove('lg-05__closing'); dlg.close(); }
  };
  open.addEventListener('click', () => dlg.showModal());
  root.querySelector('#lg-05-cancel').addEventListener('click', close);
  root.querySelector('#lg-05-confirm').addEventListener('click', close);
  dlg.addEventListener('click', e => { const r = dlg.getBoundingClientRect(); if (e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom) close(); });
  dlg.addEventListener('cancel', e => { e.preventDefault(); close(); });
})();
```
