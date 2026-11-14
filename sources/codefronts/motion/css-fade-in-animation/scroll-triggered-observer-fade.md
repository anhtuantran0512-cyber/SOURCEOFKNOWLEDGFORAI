---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/scroll-triggered-observer-fade/"
title: "Scroll-Triggered Observer Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "An activity feed list where items observe viewport entry via IntersectionObserver and acquire a .fi-05--visible class, triggering CSS transitions to slide…"
has_js: "true"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Triggered Observer Fade
Source: https://codefronts.com/motion/css-fade-in-animation/scroll-triggered-observer-fade/

An activity feed list where items observe viewport entry via IntersectionObserver and acquire a .fi-05--visible class, triggering CSS transitions to slide and fade in staggered.
## HTML
```html
<div class="fi-05" id="fi-05-root">
  <div class="fi-05__title">Activity Feed</div>
  <div class="fi-05__items">
    <div class="fi-05__item"><div class="fi-05__dot"></div><div class="fi-05__body"><div class="fi-05__name">Deployment successful</div><div class="fi-05__meta">production · 2 min ago</div></div><span class="fi-05__badge">Live</span></div>
    <div class="fi-05__item"><div class="fi-05__dot"></div><div class="fi-05__body"><div class="fi-05__name">Pull request merged</div><div class="fi-05__meta">feature/auth · 14 min ago</div></div><span class="fi-05__badge">Done</span></div>
    <div class="fi-05__item"><div class="fi-05__dot"></div><div class="fi-05__body"><div class="fi-05__name">Build failed on main</div><div class="fi-05__meta">CI pipeline · 1 hr ago</div></div><span class="fi-05__badge">Error</span></div>
    <div class="fi-05__item"><div class="fi-05__dot"></div><div class="fi-05__body"><div class="fi-05__name">New user signup spike</div><div class="fi-05__meta">analytics · 3 hr ago</div></div><span class="fi-05__badge">Alert</span></div>
    <div class="fi-05__item"><div class="fi-05__dot"></div><div class="fi-05__body"><div class="fi-05__name">Database backup complete</div><div class="fi-05__meta">storage · 6 hr ago</div></div><span class="fi-05__badge">Done</span></div>
  </div>
</div>
```
## CSS
```css
.fi-05 {
  --bg: #0b1120;
  --sky: #38bdf8;
  --emerald: #34d399;
  --rose: #fb7185;
  --text: #f0f9ff;
  font-family: 'Inter',sans-serif;
  min-height: 360px;
  border-radius: 20px;
  padding: 32px;
  overflow: hidden;
}

.fi-05 *,
.fi-05 *::before,
.fi-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-05 ::selection {
  background: var(--sky);
  color: #000;
}

.fi-05__title {
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: rgba(240,249,255,.35);
  margin-bottom: 24px;
}

.fi-05__items {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
/* Items start hidden; JS adds .fi-05--visible via IntersectionObserver */

.fi-05__item {
  display: flex;
  gap: 16px;
  align-items: center;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
  padding: 16px 20px;
  opacity: 0;
  transform: translateX(-24px);
  transition: opacity .6s cubic-bezier(.16,1,.3,1),transform .6s cubic-bezier(.16,1,.3,1);
}

.fi-05__item.fi-05--visible {
  opacity: 1;
  transform: translateX(0);
}

.fi-05__item:hover {
  background: rgba(255,255,255,.06);
  border-color: rgba(56,189,248,.2);
}

.fi-05__dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}

.fi-05__item:nth-child(1) .fi-05__dot {
  background: var(--sky);
  box-shadow: 0 0 8px rgba(56,189,248,.5);
}

.fi-05__item:nth-child(2) .fi-05__dot {
  background: var(--emerald);
  box-shadow: 0 0 8px rgba(52,211,153,.5);
}

.fi-05__item:nth-child(3) .fi-05__dot {
  background: var(--rose);
  box-shadow: 0 0 8px rgba(251,113,133,.5);
}

.fi-05__item:nth-child(4) .fi-05__dot {
  background: var(--sky);
  box-shadow: 0 0 8px rgba(56,189,248,.5);
}

.fi-05__item:nth-child(5) .fi-05__dot {
  background: var(--emerald);
  box-shadow: 0 0 8px rgba(52,211,153,.5);
}

.fi-05__body {
  flex: 1;
}

.fi-05__name {
  font-size: .9rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 3px;
}

.fi-05__meta {
  font-size: .75rem;
  color: rgba(240,249,255,.4);
}

.fi-05__badge {
  font-size: .68rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 8px;
}

.fi-05__item:nth-child(1) .fi-05__badge {
  background: rgba(56,189,248,.15);
  color: var(--sky);
}

.fi-05__item:nth-child(2) .fi-05__badge {
  background: rgba(52,211,153,.15);
  color: var(--emerald);
}

.fi-05__item:nth-child(3) .fi-05__badge {
  background: rgba(251,113,133,.15);
  color: var(--rose);
}

.fi-05__item:nth-child(4) .fi-05__badge {
  background: rgba(56,189,248,.15);
  color: var(--sky);
}

.fi-05__item:nth-child(5) .fi-05__badge {
  background: rgba(52,211,153,.15);
  color: var(--emerald);
}

@media (prefers-reduced-motion: reduce) {
  .fi-05__item {
    transition: none;
    opacity: 1;
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  const items = document.querySelectorAll('#fi-05-root .fi-05__item');
  const obs = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        const el = e.target;
        const idx = [...items].indexOf(el);
        setTimeout(()=>el.classList.add('fi-05--visible'), idx * 100);
        obs.unobserve(el);
      }
    });
  },{threshold:0.2});
  items.forEach(el=>obs.observe(el));
})();
```
