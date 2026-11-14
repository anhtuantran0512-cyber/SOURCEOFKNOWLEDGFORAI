---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/css-parallax-background-blur-transition/"
title: "Parallax Background Blur Transition"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "Two photographic sections that trade focus: as you scroll from the first to the second, section A's background blurs out and section B's blurs in from soft…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Background Blur Transition
Source: https://codefronts.com/motion/css-parallax-designs/css-parallax-background-blur-transition/

Two photographic sections that trade focus: as you scroll from the first to the second, section A's background blurs out and section B's blurs in from soft to sharp, with glass cards riding on top of both. The blur amount is tied to scroll position, so the handoff runs in reverse when you scroll back.
## HTML
```html
<div class="plx-22">
  <section class="plx-22__sec plx-22__sec--a" aria-labelledby="plx-22-a">
    <img class="plx-22__plate plx-22__plate--a" src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1600&auto=format&fit=crop" alt="City avenue in low afternoon sun" loading="eager" decoding="async">
    <div class="plx-22__card">
      <p class="plx-22__eyebrow">Aperture OS · 12.4</p>
      <h2 class="plx-22__h2" id="plx-22-a">Focus stays where you left it</h2>
      <p class="plx-22__p">Windows remember which display they were on, which space they belonged to, and which app had the keyboard. Wake and it is all where you left it.</p>
      <p class="plx-22__hint">Keep scrolling — this section is about to lose focus.</p>
    </div>
  </section>
  <section class="plx-22__sec plx-22__sec--b" aria-labelledby="plx-22-b">
    <img class="plx-22__plate plx-22__plate--b" src="https://images.unsplash.com/photo-1511818966892-d7d671e672a2?w=1600&auto=format&fit=crop" alt="Glass towers seen from street level at dusk" loading="lazy" decoding="async">
    <div class="plx-22__card">
      <p class="plx-22__eyebrow">And then</p>
      <h2 class="plx-22__h2" id="plx-22-b">The next thing arrives sharp</h2>
      <p class="plx-22__p">Handoff is a focus pull, not a cut: the outgoing scene softens while the incoming one resolves, and both are tied to your scroll position rather than to a timer.</p>
      <ul class="plx-22__list">
        <li>Blur out: 12% to 46% of page scroll</li>
        <li>Blur in: 40% to 74%</li>
        <li>Four points of deliberate overlap</li>
      </ul>
    </div>
  </section>
  <footer class="plx-22__foot">
    <p class="plx-22__p">Scroll up again and the two sections trade focus in the opposite direction. Written up by Sam Rivera.</p>
  </footer>
</div>
```
## CSS
```css
.plx-22 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "SF Pro Display", "Geist", system-ui, -apple-system, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --bg: #06060a;
  --ink: #f4f5fb;
  --muted: #b3b7cc;
  --accent: #8b90ff;
  --edge: rgba(255,255,255,0.22);
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-22 * {
  box-sizing: border-box;
}

.plx-22__sec {
  position: relative;
  min-block-size: 118svh;
  overflow: clip;
  display: flex;
  align-items: center;
  padding: clamp(24px, 6vw, 84px);
  isolation: isolate;
}

.plx-22__plate {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 112%;
  object-fit: cover;
  z-index: -2;
  will-change: transform, filter;
}

.plx-22__sec::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(200deg, rgba(6,6,10,0.5) 0%, rgba(6,6,10,0.72) 100%);
}

.plx-22__card {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
  padding: clamp(20px, 4vw, 34px);
  border-radius: 24px;
  border: 1px solid var(--edge);
  background: rgba(18,18,30,0.82);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.28), 0 34px 70px -40px rgba(0,0,0,0.95);
}

@supports (backdrop-filter: blur(2px)) {
  .plx-22__card {
    background: rgba(22,22,38,0.42);
    backdrop-filter: blur(18px) saturate(1.3);
  }
}

.plx-22__eyebrow {
  margin: 0 0 14px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-22__h2 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(26px, 5.6vw, 46px);
  font-weight: 620;
  line-height: 1.06;
  letter-spacing: -0.03em;
}

.plx-22__p {
  margin: 0 0 14px;
  font-size: clamp(15px, 3.2vw, 17px);
  line-height: 1.66;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-22__hint {
  margin: 0;
  font-size: 13px;
  color: rgba(180,185,210,0.8);
}

.plx-22__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 8px;
  font-size: 14px;
  color: #d3d7ea;
}

.plx-22__list li {
  padding-inline-start: 18px;
  position: relative;
  min-inline-size: 0;
}

.plx-22__list li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  top: 0.55em;
  inline-size: 7px;
  block-size: 7px;
  border-radius: 50%;
  background: var(--accent);
}

.plx-22__foot {
  padding: clamp(44px, 8vw, 100px) clamp(24px, 6vw, 84px) 130px;
  background: var(--bg);
}

.plx-22__foot .plx-22__p {
  max-inline-size: 34rem;
  margin: 0;
}

@supports (animation-timeline: scroll()) {
  .plx-22__plate--a {
    animation: plx-22-out linear both;
    animation-timeline: scroll(root);
    animation-range: 12% 46%;
  }

  .plx-22__plate--b {
    animation: plx-22-in linear both;
    animation-timeline: scroll(root);
    animation-range: 40% 74%;
  }
}

@keyframes plx-22-out {
  from {
    filter: blur(0px) brightness(1);
    transform: translateY(0) scale(1);
  }

  to {
    filter: blur(16px) brightness(0.8);
    transform: translateY(-48px) scale(1.05);
  }
}

@keyframes plx-22-in {
  from {
    filter: blur(20px) brightness(0.78);
    transform: translateY(-40px) scale(1.06);
  }

  to {
    filter: blur(0px) brightness(1);
    transform: translateY(0) scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-22__plate {
    animation: none !important;
    filter: none !important;
    transform: none !important;
    block-size: 100%;
    will-change: auto;
  }
}
```
