---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/scroll-linked-typography-scale-parallax/"
title: "Scroll Linked Typography Scale Parallax"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A display headline pinned to the viewport that grows from a modest 1x to roughly 2.8x as the reader scrolls past it, with the word tracking tightening and a…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Linked Typography Scale Parallax
Source: https://codefronts.com/motion/css-parallax-designs/scroll-linked-typography-scale-parallax/

A display headline pinned to the viewport that grows from a modest 1x to roughly 2.8x as the reader scrolls past it, with the word tracking tightening and a sub-line receding behind it. The base size stays a clamp() so the type is responsive first and animated second — the scroll only multiplies what the viewport already decided.
## HTML
```html
<div class="plx-06">
  <div class="plx-06__runway">
    <div class="plx-06__stage">
      <p class="plx-06__meta">Aperture Review · No. 12</p>
      <h1 class="plx-06__word">SLOWER</h1>
      <p class="plx-06__sub">A working argument for shooting one frame a day, by Alex Chen</p>
    </div>
  </div>
  <main class="plx-06__body">
    <section class="plx-06__section">
      <h2 class="plx-06__h2">One frame</h2>
      <p class="plx-06__p">The rule was arbitrary and that is why it worked. One exposure a day for a year, no bracketing, no second attempt, and no deleting until December. What changes is not the pictures — it is the amount of time spent looking before the shutter.</p>
    </section>
    <section class="plx-06__section">
      <h2 class="plx-06__h2">The count</h2>
      <p class="plx-06__p">Three hundred and sixty-five frames. Forty-one usable. Nine that still hold up two years later, which is roughly the same hit rate as a year of shooting six thousand.</p>
    </section>
    <section class="plx-06__section">
      <h2 class="plx-06__h2">After</h2>
      <p class="plx-06__p">The habit did not survive contact with paid work. The looking did.</p>
    </section>
  </main>
</div>
```
## CSS
```css
.plx-06 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Helvetica Neue", "Arial Narrow", ui-sans-serif, system-ui, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --void: #000000;
  --ink: #ffffff;
  --muted: #8a8a8a;
  background: var(--void);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-06 * {
  box-sizing: border-box;
}

.plx-06__runway {
  block-size: 260svh;
  position: relative;
}

.plx-06__stage {
  position: sticky;
  top: 0;
  block-size: 100svh;
  overflow: clip;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: 24px;
  text-align: center;
}

.plx-06__meta {
  margin: 0;
  font: 500 10px/1 var(--font-body);
  letter-spacing: 0.4em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-06__word {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(44px, 13vw, 138px);
  font-weight: 700;
  line-height: 0.9;
  letter-spacing: -0.01em;
  text-transform: uppercase;
  transform-origin: 50% 42%;
  will-change: transform, letter-spacing;
  text-shadow: 0 0 1px rgba(255,255,255,0.4), 0 0 34px rgba(255,255,255,0.18), 0 0 90px rgba(255,255,255,0.08);
}

.plx-06__sub {
  margin: 0;
  max-inline-size: 26rem;
  min-inline-size: 0;
  font-size: clamp(13px, 3vw, 16px);
  line-height: 1.6;
  color: var(--muted);
  will-change: transform, opacity;
  text-wrap: pretty;
}

.plx-06__body {
  position: relative;
  padding: clamp(48px, 9vw, 120px) clamp(22px, 6vw, 80px) 140px;
  display: grid;
  gap: clamp(40px, 7vw, 82px);
  border-top: 1px solid #1a1a1a;
}

.plx-06__section {
  max-inline-size: 38rem;
  min-inline-size: 0;
}

.plx-06__h2 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(20px, 4.2vw, 30px);
  font-weight: 700;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.plx-06__p {
  margin: 0;
  font-size: clamp(15px, 3.4vw, 17px);
  line-height: 1.76;
  color: #b9b9b9;
  text-wrap: pretty;
}

@supports (animation-timeline: scroll()) {
  .plx-06__word {
    animation: plx-06-grow linear both;
    animation-timeline: scroll(root);
    animation-range: 0 62%;
  }

  .plx-06__sub {
    animation: plx-06-recede linear both;
    animation-timeline: scroll(root);
    animation-range: 0 44%;
  }
}

@keyframes plx-06-grow {
  from {
    transform: scale(1);
    letter-spacing: -0.01em;
  }

  to {
    transform: scale(2.8);
    letter-spacing: -0.045em;
  }
}

@keyframes plx-06-recede {
  from {
    transform: translateY(0) scale(1);
    opacity: 1;
  }

  to {
    transform: translateY(26px) scale(0.86);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-06__word,
    .plx-06__sub {
    animation: none !important;
    transform: none !important;
    opacity: 1 !important;
    letter-spacing: -0.01em;
    will-change: auto;
  }
}
```
