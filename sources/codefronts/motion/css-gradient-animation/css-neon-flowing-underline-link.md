---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-neon-flowing-underline-link/"
title: "CSS Neon Flowing Underline Link"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "Navigation links and inline prose anchors where hover activates a flowing multi-colour gradient underline that sweeps in from the left and then animates…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Flowing Underline Link
Source: https://codefronts.com/motion/css-gradient-animation/css-neon-flowing-underline-link/

Navigation links and inline prose anchors where hover activates a flowing multi-colour gradient underline that sweeps in from the left and then animates infinitely, replacing the static underline with a living neon ribbon.
## HTML
```html
<div class="ga-08">

  <nav class="ga-08__nav">
    <span class="ga-08__link ga-08__link--active">Home</span>
    <span class="ga-08__link">Features</span>
    <span class="ga-08__link">Pricing</span>
    <span class="ga-08__link">Blog</span>
    <span class="ga-08__link">Contact</span>
  </nav>

  <div class="ga-08__prose">
    <h2 class="ga-08__prose-head">Links that feel alive</h2>
    <p class="ga-08__prose-body">
      Hover the navigation above to see each link reveal its own unique
      <span class="ga-08__inline">flowing gradient underline</span>. In body copy,
      the same technique works at a smaller scale — try hovering
      <span class="ga-08__inline">this inline link</span> or
      <span class="ga-08__inline" style="--ul-c1:#a855f7;--ul-c2:#f97316;--ul-c3:#eab308;">this one</span>
      to see the neon line slide in from the left and animate infinitely.
    </p>
  </div>

  <div class="ga-08__speed">
    <span class="ga-08__speed-label">Flow speed:</span>
    <button class="ga-08__speed-btn" data-dur="4s">Slow</button>
    <button class="ga-08__speed-btn active" data-dur="2s">Normal</button>
    <button class="ga-08__speed-btn" data-dur="1s">Fast</button>
  </div>

</div>
```
## CSS
```css
.ga-08,
.ga-08 *,
.ga-08 *::before,
.ga-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-08 ::selection {
  background: rgba(6,182,212,.4);
  color: #fff;
}

.ga-08 {
  --bg: #080c12;
  --dur: 2s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0;
  padding: 48px 24px;
}
/* ── Realistic nav bar ── */

.ga-08__nav {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 12px 24px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 14px;
  margin-bottom: 56px;
}
/* ── Core underline link technique ── */

.ga-08__link {
  position: relative;
  display: inline-block;
  padding: 6px 14px;
  font-size: .9rem;
  font-weight: 500;
  color: rgba(255,255,255,.45);
  text-decoration: none;
  cursor: pointer;
  transition: color .3s ease;
  border-radius: 8px;
  white-space: nowrap;
}
/* Underline via ::after using gradient background-size trick */

.ga-08__link::after {
  content: '';
  position: absolute;
  bottom: 2px;
  left: 14px;
  right: 14px;
  height: 2px;
  border-radius: 999px;
  background: linear-gradient(
      90deg,
      var(--ul-c1, #06b6d4),
      var(--ul-c2, #818cf8),
      var(--ul-c3, #ec4899),
      var(--ul-c1, #06b6d4)
    );
  background-size: 200% 100%;
  background-position: 100% 0;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform .35s cubic-bezier(.22,1,.36,1), background-position var(--dur) linear;
}

.ga-08__link:hover {
  color: rgba(255,255,255,.92);
}

.ga-08__link:hover::after {
  transform: scaleX(1);
  transform-origin: left;
  background-position: -100% 0;
  animation: ga-08-flow var(--dur) linear infinite;
}

@keyframes ga-08-flow {
  0% {
    background-position: 100% 0;
  }

  100% {
    background-position: -100% 0;
  }
}
/* Active nav item — always underlined */

.ga-08__link--active {
  color: rgba(255,255,255,.9);
}

.ga-08__link--active::after {
  transform: scaleX(1);
  animation: ga-08-flow var(--dur) linear infinite;
}
/* Custom colour variants per link */

.ga-08__link:nth-child(2) {
  --ul-c1: #a855f7;
  --ul-c2: #ec4899;
  --ul-c3: #f97316;
}

.ga-08__link:nth-child(3) {
  --ul-c1: #10b981;
  --ul-c2: #06b6d4;
  --ul-c3: #6366f1;
}

.ga-08__link:nth-child(4) {
  --ul-c1: #f97316;
  --ul-c2: #eab308;
  --ul-c3: #ef4444;
}

.ga-08__link:nth-child(5) {
  --ul-c1: #ec4899;
  --ul-c2: #a855f7;
  --ul-c3: #6366f1;
}
/* ── Prose section showing links in copy ── */

.ga-08__prose {
  max-width: 560px;
  text-align: center;
}

.ga-08__prose-head {
  font-size: clamp(1.6rem, 3.5vw, 2.2rem);
  font-weight: 800;
  color: #f1f5f9;
  letter-spacing: -.025em;
  margin-bottom: 20px;
  line-height: 1.2;
}

.ga-08__prose-body {
  font-size: .95rem;
  color: rgba(255,255,255,.45);
  line-height: 1.8;
}
/* Inline prose links */

.ga-08__inline {
  position: relative;
  display: inline;
  color: rgba(255,255,255,.8);
  text-decoration: none;
  cursor: pointer;
  padding-bottom: 2px;
}

.ga-08__inline::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: 1.5px;
  border-radius: 999px;
  background: linear-gradient(90deg, #06b6d4, #818cf8, #ec4899, #06b6d4);
  background-size: 300% 100%;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform .3s cubic-bezier(.22,1,.36,1);
}

.ga-08__inline:hover {
  color: #fff;
}

.ga-08__inline:hover::after {
  transform: scaleX(1);
  transform-origin: left;
  animation: ga-08-flow-inline 1.8s linear infinite;
}

@keyframes ga-08-flow-inline {
  0% {
    background-position: 100% 0;
  }

  100% {
    background-position: -100% 0;
  }
}
/* Speed control */

.ga-08__speed {
  margin-top: 40px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.ga-08__speed-label {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,255,255,.25);
}

.ga-08__speed-btn {
  padding: 4px 12px;
  font-size: .72rem;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,.1);
  background: transparent;
  color: rgba(255,255,255,.35);
  cursor: pointer;
  transition: all .2s;
}

.ga-08__speed-btn.active,
.ga-08__speed-btn:hover {
  background: rgba(6,182,212,.15);
  border-color: rgba(6,182,212,.35);
  color: #67e8f9;
}

@media (prefers-reduced-motion: reduce) {
  .ga-08__link:hover::after,
    .ga-08__link--active::after,
    .ga-08__inline:hover::after {
    animation: none;
  }

  .ga-08__link::after,
    .ga-08__inline::after {
    transition: transform .3s ease;
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-08');
  w.querySelectorAll('.ga-08__speed-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-08__speed-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.style.setProperty('--dur', btn.dataset.dur);
    });
  });
})();
```
