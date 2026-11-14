---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/parallax-storytelling-with-chapter-markers/"
title: "Parallax Storytelling with Chapter Markers"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A four-chapter feature where each chapter's photograph drifts behind its text at its own rate, and a fixed rail on the left marks which chapter the reader is…"
has_js: "true"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Storytelling with Chapter Markers
Source: https://codefronts.com/motion/css-parallax-designs/parallax-storytelling-with-chapter-markers/

A four-chapter feature where each chapter's photograph drifts behind its text at its own rate, and a fixed rail on the left marks which chapter the reader is inside. The parallax is pure CSS on view() timelines; a small IntersectionObserver only sets the rail's active state, which is a state question rather than an animation one.
## HTML
```html
<div class="plx-10">
  <nav class="plx-10__rail" id="plx-10-rail" aria-label="Chapters">
    <a class="plx-10__marker is-active" href="#plx-10-c1" data-plx-10="1" aria-current="true"><span class="plx-10__num">1</span><span class="plx-10__mname">Source</span></a>
    <a class="plx-10__marker" href="#plx-10-c2" data-plx-10="2"><span class="plx-10__num">2</span><span class="plx-10__mname">The gorge</span></a>
    <a class="plx-10__marker" href="#plx-10-c3" data-plx-10="3"><span class="plx-10__num">3</span><span class="plx-10__mname">Flatwater</span></a>
    <a class="plx-10__marker" href="#plx-10-c4" data-plx-10="4"><span class="plx-10__num">4</span><span class="plx-10__mname">Mouth</span></a>
  </nav>
  <article class="plx-10__story">
    <header class="plx-10__head">
      <p class="plx-10__kicker">The Kestrel Review · Field feature</p>
      <h1 class="plx-10__h1">Eleven days on the Aurel</h1>
      <p class="plx-10__standfirst">A river read from its source to its mouth, in four chapters. Words by Priya Sharma.</p>
    </header>
    <section class="plx-10__chapter" id="plx-10-c1" data-plx-10-ch="1">
      <figure class="plx-10__figure"><img class="plx-10__plate plx-10__plate--1" src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=1400&auto=format&fit=crop" alt="Sunlight breaking over a high green valley" loading="lazy" decoding="async"></figure>
      <div class="plx-10__text">
        <p class="plx-10__chnum">Chapter one</p>
        <h2 class="plx-10__h2">Source</h2>
        <p class="plx-10__p">The Aurel begins as seepage under a bank of old snow, which means for the first two kilometres there is no river to follow, only a direction. The water is audible before it is visible.</p>
        <p class="plx-10__p">By the second morning it is wide enough to lose a boot in. The valley here holds fog until nine, and the fog is what makes the depth legible — three ridges, each a shade paler than the last.</p>
      </div>
    </section>
    <section class="plx-10__chapter" id="plx-10-c2" data-plx-10-ch="2">
      <figure class="plx-10__figure"><img class="plx-10__plate plx-10__plate--2" src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&auto=format&fit=crop" alt="Steep red rock walls narrowing to a gap" loading="lazy" decoding="async"></figure>
      <div class="plx-10__text">
        <p class="plx-10__chnum">Chapter two</p>
        <h2 class="plx-10__h2">The gorge</h2>
        <p class="plx-10__p">Four kilometres of walls close enough to shout across. The river drops sixty metres inside them and does it in a hurry, so the walking becomes scrambling and the scrambling becomes waiting for the water to decide.</p>
        <p class="plx-10__p">Two of our eleven days were spent in the gorge. Neither was planned.</p>
      </div>
    </section>
    <section class="plx-10__chapter" id="plx-10-c3" data-plx-10-ch="3">
      <figure class="plx-10__figure"><img class="plx-10__plate plx-10__plate--3" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1400&auto=format&fit=crop" alt="Green hills opening out under low cloud" loading="lazy" decoding="async"></figure>
      <div class="plx-10__text">
        <p class="plx-10__chnum">Chapter three</p>
        <h2 class="plx-10__h2">Flatwater</h2>
        <p class="plx-10__p">Below the gorge the Aurel gives up its gradient and spends sixty kilometres wandering. The map calls it flatwater; the paddling calls it work. Wind from the west, every afternoon, without exception.</p>
        <p class="plx-10__p">This is the stretch people skip, and it is the only stretch where the river is quiet enough to hear the banks.</p>
      </div>
    </section>
    <section class="plx-10__chapter" id="plx-10-c4" data-plx-10-ch="4">
      <figure class="plx-10__figure"><img class="plx-10__plate plx-10__plate--4" src="https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=1400&auto=format&fit=crop" alt="River mouth opening into a bay beside a city" loading="lazy" decoding="async"></figure>
      <div class="plx-10__text">
        <p class="plx-10__chnum">Chapter four</p>
        <h2 class="plx-10__h2">Mouth</h2>
        <p class="plx-10__p">The end is anticlimactic by design: a bay, a working port, a tide that reverses the current twice a day. The river does not arrive so much as dissolve.</p>
        <p class="plx-10__p">Eleven days, one hundred and eighty kilometres, four chapters. The rail on the left knew which one you were in the whole way down.</p>
      </div>
    </section>
  </article>
</div>
```
## CSS
```css
.plx-10 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Snell Roundhand", "Segoe Script", "Brush Script MT", cursive;
  --font-serif: "Iowan Old Style", Georgia, "Times New Roman", serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --paper: #efe6da;
  --ink: #2f241b;
  --muted: #7b6857;
  --tint: #a0522d;
  --rule: #d8c9b6;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-10 * {
  box-sizing: border-box;
}

.plx-10__rail {
  display: none;
}

.plx-10__story {
  max-inline-size: 100%;
}

.plx-10__head {
  padding: clamp(40px, 8vw, 104px) clamp(20px, 5vw, 64px) clamp(28px, 5vw, 56px);
  max-inline-size: 48rem;
}

.plx-10__kicker {
  margin: 0 0 18px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--tint);
}

.plx-10__h1 {
  margin: 0 0 16px;
  font-family: var(--font-serif);
  font-size: clamp(32px, 7vw, 66px);
  font-weight: 400;
  line-height: 1.04;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.plx-10__standfirst {
  margin: 0;
  max-inline-size: 32rem;
  font-size: clamp(15px, 3.4vw, 18px);
  line-height: 1.65;
  color: var(--muted);
}

.plx-10__chapter {
  border-top: 1px solid var(--rule);
}

.plx-10__figure {
  margin: 0;
  overflow: clip;
  block-size: clamp(260px, 62vh, 620px);
}

.plx-10__plate {
  display: block;
  inline-size: 100%;
  block-size: 118%;
  object-fit: cover;
  filter: sepia(0.32) contrast(1.04) saturate(0.86);
  will-change: transform;
}

.plx-10__text {
  padding: clamp(26px, 5vw, 60px) clamp(20px, 5vw, 64px) clamp(40px, 8vw, 90px);
  max-inline-size: 40rem;
  min-inline-size: 0;
}

.plx-10__chnum {
  margin: 0 0 6px;
  font-family: var(--font-display);
  font-size: clamp(20px, 4vw, 30px);
  color: var(--tint);
}

.plx-10__h2 {
  margin: 0 0 16px;
  font-family: var(--font-serif);
  font-size: clamp(24px, 5.2vw, 40px);
  font-weight: 400;
  line-height: 1.1;
}

.plx-10__p {
  margin: 0 0 16px;
  font-family: var(--font-serif);
  font-size: clamp(16px, 3.4vw, 18px);
  line-height: 1.78;
  color: #3f3227;
  text-wrap: pretty;
}

@media (min-width: 900px) {
  .plx-10__rail {
    display: grid;
    gap: 4px;
    position: fixed;
    inset-block-start: 50%;
    inset-inline-start: 22px;
    transform: translateY(-50%);
    z-index: 5;
    padding: 10px;
    border-radius: 14px;
    background: rgba(239,230,218,0.92);
    border: 1px solid var(--rule);
  }

  .plx-10__story {
    padding-inline-start: 132px;
  }

  .plx-10__marker {
    display: flex;
    align-items: center;
    gap: 10px;
    min-height: 44px;
    padding: 0 12px;
    border-radius: 9px;
    text-decoration: none;
    color: var(--muted);
    font-size: 13px;
  }

  .plx-10__marker:hover {
    background: rgba(160,82,45,0.1);
    color: var(--ink);
  }

  .plx-10__marker:focus-visible {
    outline: 2px solid var(--tint);
    outline-offset: 2px;
  }

  .plx-10__num {
    display: grid;
    place-items: center;
    inline-size: 26px;
    block-size: 26px;
    border-radius: 50%;
    border: 1px solid var(--rule);
    font-family: var(--font-display);
    font-size: 15px;
  }

  .plx-10__marker.is-active {
    background: var(--tint);
    color: #fff8f0;
  }

  .plx-10__marker.is-active .plx-10__num {
    border-color: rgba(255,248,240,0.7);
    background: rgba(255,255,255,0.16);
  }
}

@supports (animation-timeline: view()) {
  .plx-10__plate {
    animation-timing-function: linear;
    animation-fill-mode: both;
    animation-timeline: view();
  }

  .plx-10__plate--1 {
    animation-name: plx-10-d1;
  }

  .plx-10__plate--2 {
    animation-name: plx-10-d2;
  }

  .plx-10__plate--3 {
    animation-name: plx-10-d3;
  }

  .plx-10__plate--4 {
    animation-name: plx-10-d4;
  }
}

@keyframes plx-10-d1 {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-40px);
  }
}

@keyframes plx-10-d2 {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-72px);
  }
}

@keyframes plx-10-d3 {
  from {
    transform: translateY(-8px);
  }

  to {
    transform: translateY(-56px);
  }
}

@keyframes plx-10-d4 {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-92px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-10__plate {
    animation: none !important;
    transform: none !important;
    block-size: 100%;
    will-change: auto;
  }
}
```

## JavaScript
```js
const chapters = document.querySelectorAll('[data-plx-10-ch]');
const markers = document.querySelectorAll('[data-plx-10]');
if (chapters.length && 'IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const id = entry.target.dataset.plx10Ch;
      markers.forEach((m) => {
        const on = m.dataset.plx10 === id;
        m.classList.toggle('is-active', on);
        if (on) { m.setAttribute('aria-current', 'true'); } else { m.removeAttribute('aria-current'); }
      });
    });
  }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
  chapters.forEach((c) => io.observe(c));
}
```
