---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-toast-notification/"
title: "Liquid Glass Toast Notification"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "Native-feeling system alerts: frosted glass toasts slide in from the top-right and stack cleanly on top of each other, each blurring the app state behind it…"
has_js: "true"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Toast Notification
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-toast-notification/

Native-feeling system alerts: frosted glass toasts slide in from the top-right and stack cleanly on top of each other, each blurring the app state behind it without stacking-blur artifacts. Auto-dismiss with a glass progress rim, or dismiss by hand — polite, layered, and out of the way.
## HTML
```html
<section class="lg-14" id="lg-14-root" aria-label="Liquid glass toast notifications">
  <img class="lg-14__bg" src="https://picsum.photos/seed/lgtoast/1100/750" width="1100" height="750" alt="Dashboard backdrop">
  <div class="lg-14__controls">
    <button class="lg-14__spawn" data-type="success" type="button">Success toast</button>
    <button class="lg-14__spawn" data-type="info" type="button">Info toast</button>
    <button class="lg-14__spawn" data-type="error" type="button">Error toast</button>
  </div>
  <div class="lg-14__region" id="lg-14-region" role="region" aria-label="Notifications" aria-live="polite"></div>
</section>
```
## CSS
```css
.lg-14,
.lg-14 *,
.lg-14 *::before,
.lg-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-14 {
  --ok: oklch(0.72 0.16 160);
  --info: oklch(0.7 0.16 250);
  --err: oklch(0.65 0.2 25);
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

.lg-14__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.lg-14__controls {
  position: relative;
  z-index: 1;
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.lg-14__spawn {
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  padding: 12px 20px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,.35);
  cursor: pointer;
  background: color-mix(in oklab,white 14%,transparent);
  backdrop-filter: blur(14px) saturate(160%);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  transition: transform .15s;
}

.lg-14__spawn:hover {
  transform: translateY(-2px);
}

.lg-14__spawn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-14__region {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 50;
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: min(320px,86vw);
  pointer-events: none;
}

.lg-14__toast {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  pointer-events: auto;
  display: flex;
  gap: 12px;
  align-items: flex-start;
  padding: 14px 40px 14px 14px;
  border-radius: 16px;
  color: #fff;
  background: color-mix(in oklab,white 14%,transparent);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 20px 40px -20px rgba(0,0,0,.7);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  animation: lg-14-in .4s cubic-bezier(.2,.9,.2,1);
}

.lg-14__toast.lg-14__out {
  animation: lg-14-out .3s ease forwards;
}

.lg-14__ico {
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 14px;
  font-weight: 900;
  color: #fff;
}

.lg-14__toast--success .lg-14__ico {
  background: var(--ok);
}

.lg-14__toast--info .lg-14__ico {
  background: var(--info);
}

.lg-14__toast--error .lg-14__ico {
  background: var(--err);
}

.lg-14__msg {
  font-size: 14px;
  line-height: 1.4;
}

.lg-14__msg strong {
  display: block;
  font-weight: 800;
  margin-bottom: 2px;
}

.lg-14__close {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: none;
  cursor: pointer;
  color: #fff;
  background: rgba(255,255,255,.16);
  font-size: 13px;
}

.lg-14__close:hover {
  background: rgba(255,255,255,.3);
}

.lg-14__close:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 1px;
}

.lg-14__toast::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 3px;
  width: 100%;
  transform-origin: left;
  background: rgba(255,255,255,.7);
  animation: lg-14-rim var(--life,4000ms) linear forwards;
}

@keyframes lg-14-in {
  from {
    opacity: 0;
    transform: translateX(110%);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes lg-14-out {
  to {
    opacity: 0;
    transform: translateX(110%);
  }
}

@keyframes lg-14-rim {
  from {
    transform: scaleX(1);
  }

  to {
    transform: scaleX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-14__toast {
    animation: none;
  }

  .lg-14__toast.lg-14__out {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lg-14-root');
  const region = root.querySelector('#lg-14-region');
  const LIFE = 4000;
  const copy = {
    success:{ico:'✓',title:'Saved',body:'Your changes are live.'},
    info:{ico:'i',title:'Heads up',body:'A new version is available.'},
    error:{ico:'!',title:'Upload failed',body:'Check your connection and retry.'}
  };
  function toast(type){
    const c = copy[type] || copy.info;
    const el = document.createElement('div');
    el.className = 'lg-14__toast lg-14__toast--' + type;
    el.style.setProperty('--life', LIFE + 'ms');
    el.innerHTML = '<span class="lg-14__ico">'+c.ico+'</span><div class="lg-14__msg"><strong>'+c.title+'</strong>'+c.body+'</div><button class="lg-14__close" aria-label="Dismiss">✕</button>';
    region.appendChild(el);
    const kill = () => { el.classList.add('lg-14__out'); el.addEventListener('animationend', () => el.remove(), {once:true}); setTimeout(()=>el.remove(),350); };
    const t = setTimeout(kill, LIFE);
    el.querySelector('.lg-14__close').addEventListener('click', () => { clearTimeout(t); kill(); });
  }
  root.querySelectorAll('.lg-14__spawn').forEach(b => b.addEventListener('click', () => toast(b.dataset.type)));
})();
```
