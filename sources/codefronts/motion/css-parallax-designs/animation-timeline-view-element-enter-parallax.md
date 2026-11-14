---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/animation-timeline-view-element-enter-parallax/"
title: "Animation Timeline View Element Enter Parallax"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "An editorial card grid where every card owns its own timeline: as it crosses the viewport it lifts, scales and settles, driven by animation-timeline: view()…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animation Timeline View Element Enter Parallax
Source: https://codefronts.com/motion/css-parallax-designs/animation-timeline-view-element-enter-parallax/

An editorial card grid where every card owns its own timeline: as it crosses the viewport it lifts, scales and settles, driven by animation-timeline: view() rather than a shared page scroll. Because each element measures its own entry, cards at different heights animate independently — the grid breathes instead of moving as one block.
## HTML
```html
<div class="plx-02">
  <header class="plx-02__masthead">
    <p class="plx-02__kicker">The Long Exposure · Issue 46</p>
    <h1 class="plx-02__h1">Rooms that were built for the light</h1>
    <p class="plx-02__standfirst">Eight architects on the single window they would keep if the rest of the building had to go. Reported by Priya Sharma and Jordan Lee.</p>
  </header>
  <main class="plx-02__grid">
    <article class="plx-02__card plx-02__card--wide">
      <figure class="plx-02__figure"><img class="plx-02__plate" src="https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=1400&auto=format&fit=crop" alt="Upper landing of a white house lit from a high window, pendant lamps in the foreground" loading="lazy" decoding="async"></figure>
      <div class="plx-02__text">
        <p class="plx-02__tag">Interiors</p>
        <h2 class="plx-02__h2">The clerestory argument</h2>
        <p class="plx-02__dek">Why a strip of glass nine feet up does more for a room than a wall of it at eye level.</p>
      </div>
    </article>
    <article class="plx-02__card">
      <figure class="plx-02__figure"><img class="plx-02__plate" src="https://images.unsplash.com/photo-1487958449943-2429e8be8625?w=1000&auto=format&fit=crop" alt="Faceted white concrete building against an overcast sky" loading="lazy" decoding="async"></figure>
      <div class="plx-02__text">
        <p class="plx-02__tag">Housing</p>
        <h2 class="plx-02__h2">A house with two north faces</h2>
        <p class="plx-02__dek">Notes on building for grey weather instead of against it.</p>
      </div>
    </article>
    <article class="plx-02__card">
      <figure class="plx-02__figure"><img class="plx-02__plate" src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1000&auto=format&fit=crop" alt="City avenue in low sun, traffic between tall blocks" loading="lazy" decoding="async"></figure>
      <div class="plx-02__text">
        <p class="plx-02__tag">Cities</p>
        <h2 class="plx-02__h2">Courtyards, recounted</h2>
        <p class="plx-02__dek">Six blocks in Lisbon, measured at noon and again at four.</p>
      </div>
    </article>
    <article class="plx-02__card plx-02__card--wide">
      <figure class="plx-02__figure"><img class="plx-02__plate" src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=1400&auto=format&fit=crop" alt="Curved glass facade rising into flat daylight" loading="lazy" decoding="async"></figure>
      <div class="plx-02__text">
        <p class="plx-02__tag">Galleries</p>
        <h2 class="plx-02__h2">The skylight tax</h2>
        <p class="plx-02__dek">What museums pay, in square metres and in maintenance, for daylight from above.</p>
      </div>
    </article>
    <article class="plx-02__card">
      <figure class="plx-02__figure"><img class="plx-02__plate" src="https://images.unsplash.com/photo-1511818966892-d7d671e672a2?w=1000&auto=format&fit=crop" alt="Dark towers seen from street level at night" loading="lazy" decoding="async"></figure>
      <div class="plx-02__text">
        <p class="plx-02__tag">Reprint</p>
        <h2 class="plx-02__h2">One window, 1963</h2>
        <p class="plx-02__dek">An essay on restraint, reprinted with the original plans.</p>
      </div>
    </article>
    <article class="plx-02__card">
      <figure class="plx-02__figure"><img class="plx-02__plate" src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=1000&auto=format&fit=crop" alt="Instant camera resting on a plain white surface" loading="lazy" decoding="async"></figure>
      <div class="plx-02__text">
        <p class="plx-02__tag">Studio visit</p>
        <h2 class="plx-02__h2">Bounced, never direct</h2>
        <p class="plx-02__dek">A painter's studio that has not seen a sunbeam in thirty years.</p>
      </div>
    </article>
  </main>
  <footer class="plx-02__foot"><p>Each card runs its own view() timeline — scroll slowly and the grid staggers itself.</p></footer>
</div>
```
## CSS
```css
.plx-02 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Iowan Old Style", "Palatino Linotype", Georgia, "Times New Roman", serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --paper: #f7f5f0;
  --ink: #16150f;
  --muted: #6a6558;
  --rule: #d9d4c6;
  --lift: 30px;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
}

.plx-02 * {
  box-sizing: border-box;
}

.plx-02__masthead {
  padding: clamp(40px, 8vw, 96px) clamp(20px, 5vw, 64px) clamp(28px, 5vw, 56px);
  border-bottom: 1px solid var(--rule);
  max-inline-size: 62rem;
}

.plx-02__kicker {
  margin: 0 0 18px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-02__h1 {
  margin: 0 0 18px;
  font-family: var(--font-display);
  font-size: clamp(32px, 7vw, 68px);
  font-weight: 400;
  line-height: 1.02;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.plx-02__standfirst {
  margin: 0;
  max-inline-size: 34rem;
  font-size: clamp(15px, 3.4vw, 18px);
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-02__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
  gap: 1px;
  background: var(--rule);
  border-bottom: 1px solid var(--rule);
}

.plx-02__card {
  min-inline-size: 0;
  background: var(--paper);
  padding: clamp(18px, 3vw, 30px);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.plx-02__figure {
  margin: 0;
  overflow: clip;
  aspect-ratio: 4 / 3;
}

.plx-02__card--wide .plx-02__figure {
  aspect-ratio: 16 / 9;
}

.plx-02__plate {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  background: #ddd8cb;
  will-change: transform;
  transform-origin: 50% 60%;
}

.plx-02__text {
  min-inline-size: 0;
  will-change: transform, opacity;
}

.plx-02__tag {
  margin: 0 0 10px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-02__h2 {
  margin: 0 0 8px;
  font-family: var(--font-display);
  font-size: clamp(20px, 3.6vw, 28px);
  font-weight: 400;
  line-height: 1.15;
  letter-spacing: -0.01em;
}

.plx-02__dek {
  margin: 0;
  font-size: 15px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-02__foot {
  padding: clamp(40px, 8vw, 90px) clamp(20px, 5vw, 64px) 110px;
}

.plx-02__foot p {
  margin: 0;
  max-inline-size: 30rem;
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted);
}

@media (min-width: 900px) {
  .plx-02__grid {
    grid-template-columns: repeat(6, 1fr);
  }

  .plx-02__card {
    grid-column: span 2;
  }

  .plx-02__card--wide {
    grid-column: span 3;
  }
}

@supports (animation-timeline: view()) {
  .plx-02__plate {
    animation: plx-02-plate linear both;
    animation-timeline: view(block 40% 20%);
  }

  .plx-02__text {
    animation: plx-02-text linear both;
    animation-timeline: view(block 40% 20%);
  }
}

@keyframes plx-02-plate {
  from {
    transform: scale(1.14) translateY(3%);
  }

  to {
    transform: scale(1) translateY(0);
  }
}

@keyframes plx-02-text {
  from {
    transform: translateY(var(--lift));
    opacity: 0.35;
  }

  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-02__plate,
    .plx-02__text {
    animation: none !important;
    transform: none !important;
    opacity: 1 !important;
    will-change: auto;
  }
}
```
