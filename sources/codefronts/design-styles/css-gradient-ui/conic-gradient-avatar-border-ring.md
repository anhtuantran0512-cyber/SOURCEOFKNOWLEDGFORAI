---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/conic-gradient-avatar-border-ring/"
title: "Conic Gradient Avatar Border / Ring"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A \"team activity\" strip of avatar rings: static conic story rings for unseen updates, a slow-rotating live ring for members currently online, a segmented…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Conic Gradient Avatar Border / Ring
Source: https://codefronts.com/design-styles/css-gradient-ui/conic-gradient-avatar-border-ring/

A "team activity" strip of avatar rings: static conic story rings for unseen updates, a slow-rotating live ring for members currently online, a segmented progress ring, and a stacked-avatar group — real photos, all pure CSS.
## HTML
```html
<div class="cgu-17-group">
<section class="cgu-17" aria-label="Conic gradient avatar ring demos">
  <div class="cgu-17__inner">
    <header class="cgu-17__head">
      <p class="cgu-17__eyebrow">17 · Avatar rings</p>
      <h2 class="cgu-17__title">Rings that carry state</h2>
      <p class="cgu-17__sub">Unseen, live, progress, and group — four conic-ring patterns on one roster. Only the gradients animate; the photos never move.</p>
    </header>
    <div class="cgu-17__roster">
      <figure class="cgu-17__person">
        <div class="cgu-17__ring cgu-17__ring--story"><img class="cgu-17__img" src="https://i.pravatar.cc/144?img=32" alt="Maya Chen"></div>
        <figcaption class="cgu-17__who">Maya<span class="cgu-17__state">2 updates</span></figcaption>
      </figure>
      <figure class="cgu-17__person">
        <div class="cgu-17__ring cgu-17__ring--live"><img class="cgu-17__img" src="https://i.pravatar.cc/144?img=12" alt="Jonas Weber"><i class="cgu-17__dot" aria-hidden="true"></i></div>
        <figcaption class="cgu-17__who">Jonas<span class="cgu-17__state">live now</span></figcaption>
      </figure>
      <figure class="cgu-17__person">
        <div class="cgu-17__ring cgu-17__ring--seg"><img class="cgu-17__img" src="https://i.pravatar.cc/144?img=47" alt="Priya Nair"></div>
        <figcaption class="cgu-17__who">Priya<span class="cgu-17__state">3 of 4 reviews</span></figcaption>
      </figure>
      <figure class="cgu-17__person">
        <div class="cgu-17__ring cgu-17__ring--seen"><img class="cgu-17__img" src="https://i.pravatar.cc/144?img=68" alt="Tom Alvarez"></div>
        <figcaption class="cgu-17__who">Tom<span class="cgu-17__state">all seen</span></figcaption>
      </figure>
      <figure class="cgu-17__person cgu-17__person--group">
        <div class="cgu-17__stack">
          <div class="cgu-17__ring cgu-17__ring--story cgu-17__ring--sm"><img class="cgu-17__img" src="https://i.pravatar.cc/96?img=5" alt="Ana Duarte"></div>
          <div class="cgu-17__ring cgu-17__ring--story cgu-17__ring--sm"><img class="cgu-17__img" src="https://i.pravatar.cc/96?img=15" alt="Liam O'Shea"></div>
          <div class="cgu-17__ring cgu-17__ring--sm cgu-17__more">+6</div>
        </div>
        <figcaption class="cgu-17__who">Design guild<span class="cgu-17__state">8 members</span></figcaption>
      </figure>
    </div>
    <p class="cgu-17__foot">Close the conic loop — last stop repeats the first — or a seam appears at 12 o'clock.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-17-group {
  display: block;
  width: 100%;
}

.cgu-17,
.cgu-17 *,
.cgu-17 *::before,
.cgu-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --cgu17-a {
  syntax: '<angle>';
  initial-value: 210deg;
  inherits: false;
}

.cgu-17 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: radial-gradient(90% 70% at 50% -10%,#171226 0%,#0c0a14 60%);
}

.cgu-17__inner {
  width: min(920px,100%);
  display: grid;
  gap: 44px;
}

.cgu-17__head {
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cgu-17__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #f0abfc;
}

.cgu-17__title {
  font-size: clamp(27px,4.2vw,46px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.08;
  text-wrap: balance;
}

.cgu-17__sub {
  max-width: 56ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
  text-wrap: pretty;
}

.cgu-17__roster {
  display: flex;
  gap: clamp(20px,4vw,44px);
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
}

.cgu-17__person {
  display: grid;
  gap: 12px;
  justify-items: center;
}

.cgu-17__ring {
  position: relative;
  width: 96px;
  aspect-ratio: 1;
  border-radius: 50%;
  padding: 7px;
}

.cgu-17__ring::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  padding: 3.5px;
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}

.cgu-17__ring--story::before {
  background: conic-gradient(from 210deg,#f59e0b,#ef4444,#d946ef,#8b5cf6,#f59e0b);
}

.cgu-17__ring--live::before {
  background: conic-gradient(from var(--cgu17-a),#34d399,#22d3ee,#818cf8,#34d399);
  animation: cgu17-turn 8s linear infinite;
}

.cgu-17__ring--seg::before {
  background: conic-gradient(#34d399 0 22%,transparent 22% 25%,#34d399 25% 47%,transparent 47% 50%,#34d399 50% 72%,transparent 72% 75%,#2b2f45 75% 97%,transparent 97% 100%);
}

.cgu-17__ring--seen::before {
  background: conic-gradient(#3a3f58 0 100%);
}

.cgu-17__img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

.cgu-17__dot {
  position: absolute;
  right: 4px;
  bottom: 4px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: linear-gradient(140deg,#6ee7b7,#10b981);
  box-shadow: 0 0 0 3px #0c0a14;
}

.cgu-17__who {
  display: grid;
  gap: 2px;
  justify-items: center;
  font-size: 14px;
  font-weight: 700;
}

.cgu-17__state {
  font-size: 11.5px;
  font-weight: 600;
  color: #8b90b0;
}

.cgu-17__stack {
  display: flex;
  padding-left: 14px;
}

.cgu-17__ring--sm {
  width: 68px;
  margin-left: -14px;
  padding: 5px;
}

.cgu-17__ring--sm::before {
  padding: 2.5px;
}

.cgu-17__more {
  display: grid;
  place-items: center;
  font-size: 14px;
  font-weight: 800;
  color: #c7d2fe;
  background: #1a1e33;
  border-radius: 50%;
  box-shadow: inset 0 0 0 2.5px #3a3f58;
}

.cgu-17__foot {
  text-align: center;
  font-size: 13px;
  color: #7c81a3;
}

@keyframes cgu17-turn {
  to {
    --cgu17-a: 570deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-17__ring--live::before {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — every ring is a conic-gradient on a mask-composite donut; the live ring rotates its @property-registered angle so the photo never spins. */
```
