---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/split-screen-dual-axis-parallax-scroll/"
title: "Split Screen Dual Axis Parallax Scroll"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "Two columns that travel in opposite directions: the portrait side rises while the prose side sinks, so the spread shears apart as the reader scrolls and…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split Screen Dual Axis Parallax Scroll
Source: https://codefronts.com/motion/css-parallax-designs/split-screen-dual-axis-parallax-scroll/

Two columns that travel in opposite directions: the portrait side rises while the prose side sinks, so the spread shears apart as the reader scrolls and closes again on the way back. Built for fashion and interview features where the pairing of image and text is the layout, and it collapses to a plain single column below 720px.
## HTML
```html
<div class="plx-04">
  <header class="plx-04__head">
    <p class="plx-04__issue">Maison Verrier — Autumn dossier</p>
    <h1 class="plx-04__h1">Sam Rivera on cutting a coat that has to last nine winters</h1>
  </header>
  <section class="plx-04__stage">
    <div class="plx-04__col plx-04__col--up">
      <figure class="plx-04__figure">
        <img class="plx-04__plate" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1000&auto=format&fit=crop" alt="Studio portrait against a dark grey backdrop" loading="lazy" decoding="async">
        <figcaption class="plx-04__caption">Sam Rivera, fitting room, Rue Bertin.</figcaption>
      </figure>
      <blockquote class="plx-04__quote">
        <p>"A coat is not a season. If it looks like this year, it will look like this year forever."</p>
      </blockquote>
    </div>
    <div class="plx-04__col plx-04__col--down">
      <p class="plx-04__p">The workroom keeps two patterns for every coat: the one the client is measured against, and the one it will be let out to in five years. Rivera considers the second the real garment.</p>
      <p class="plx-04__p">"The shoulder is where you decide," they say. "Everything else can be argued with later. A shoulder that is wrong is wrong for the life of the cloth."</p>
      <p class="plx-04__p">The house cuts eleven coats a month, which is fewer than it made in 1996 and, Rivera insists, more than it should. Each takes about thirty hours across three fittings, and the third fitting exists mostly to be told that nothing needs changing.</p>
      <p class="plx-04__p">Wool arrives from two mills, both in the same valley, and is rested for a season before it is touched. "Cloth has an opinion when it is new," Rivera says. "You wait for it to calm down."</p>
    </div>
  </section>
  <footer class="plx-04__foot">
    <p class="plx-04__p">Continued in the print dossier. Interview by Priya Sharma.</p>
  </footer>
</div>
```
## CSS
```css
.plx-04 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Didot", "Playfair Display", "Hoefler Text", Georgia, serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --paper: #fbfbfa;
  --ink: #0b0b0b;
  --muted: #6e6e6e;
  --rule: #e0dedb;
  --accent: #b0121f;
  --shear: clamp(40px, 9vw, 150px);
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-04 * {
  box-sizing: border-box;
}

.plx-04__head {
  padding: clamp(40px, 8vw, 110px) clamp(20px, 5vw, 72px) clamp(30px, 5vw, 60px);
  max-inline-size: 52rem;
}

.plx-04__issue {
  margin: 0 0 22px;
  font: 500 10px/1 var(--font-body);
  letter-spacing: 0.34em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-04__h1 {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(30px, 6.4vw, 62px);
  font-weight: 400;
  line-height: 1.06;
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.plx-04__stage {
  position: relative;
  overflow: clip;
  display: grid;
  gap: clamp(28px, 5vw, 64px);
  padding: calc(var(--shear) + 24px) clamp(20px, 5vw, 72px);
  border-block: 1px solid var(--rule);
}

.plx-04__col {
  min-inline-size: 0;
  will-change: transform;
}

.plx-04__figure {
  margin: 0 0 28px;
}

.plx-04__plate {
  display: block;
  inline-size: 100%;
  aspect-ratio: 3 / 4;
  object-fit: cover;
  background: #1a1816;
}

.plx-04__caption {
  margin: 12px 0 0;
  font-size: 12px;
  line-height: 1.5;
  letter-spacing: 0.02em;
  color: var(--muted);
}

.plx-04__quote {
  margin: 0;
}

.plx-04__quote p {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(20px, 4.4vw, 32px);
  font-style: italic;
  line-height: 1.24;
  color: var(--accent);
  text-wrap: pretty;
}

.plx-04__p {
  margin: 0 0 20px;
  max-inline-size: 34rem;
  font-size: clamp(15px, 3.4vw, 17px);
  line-height: 1.78;
  color: #262625;
  text-wrap: pretty;
}

.plx-04__col--down .plx-04__p:first-child::first-letter {
  float: left;
  font-family: var(--font-display);
  font-size: 3.4em;
  line-height: 0.82;
  padding-inline-end: 0.08em;
  color: var(--ink);
}

.plx-04__foot {
  padding: clamp(40px, 8vw, 96px) clamp(20px, 5vw, 72px) 120px;
}

.plx-04__foot .plx-04__p {
  color: var(--muted);
}

@media (min-width: 720px) {
  .plx-04__stage {
    grid-template-columns: minmax(0, 5fr) minmax(0, 6fr);
  }

  @supports (animation-timeline: scroll()) {
    .plx-04__col--up {
      animation: plx-04-up linear both;
      animation-timeline: scroll(root);
    }

    .plx-04__col--down {
      animation: plx-04-down linear both;
      animation-timeline: scroll(root);
    }
  }
}

@keyframes plx-04-up {
  from {
    transform: translateY(var(--shear));
  }

  to {
    transform: translateY(calc(var(--shear) * -1));
  }
}

@keyframes plx-04-down {
  from {
    transform: translateY(calc(var(--shear) * -1));
  }

  to {
    transform: translateY(var(--shear));
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-04__col {
    animation: none !important;
    transform: none !important;
    will-change: auto;
  }
}
```
