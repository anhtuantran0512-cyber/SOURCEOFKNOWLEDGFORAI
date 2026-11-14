---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/css-parallax-image-grid-gallery/"
title: "Parallax Image Grid Asymmetric Gallery"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A lookbook grid where every frame drifts at a slightly different rate according to its column, so the whole gallery breathes as it passes rather than…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Image Grid Asymmetric Gallery
Source: https://codefronts.com/motion/css-parallax-designs/css-parallax-image-grid-gallery/

A lookbook grid where every frame drifts at a slightly different rate according to its column, so the whole gallery breathes as it passes rather than scrolling as one slab. Columns are offset vertically to break the grid line, and the captions stay put while the photographs move inside their frames.
## HTML
```html
<div class="plx-17">
  <header class="plx-17__head">
    <p class="plx-17__label">Lookbook · Autumn</p>
    <h1 class="plx-17__h1">Stone, chalk, and one navy</h1>
    <p class="plx-17__lede">Fourteen pieces photographed in daylight over two afternoons. Styling by Priya Sharma.</p>
  </header>
  <div class="plx-17__grid">
    <div class="plx-17__col plx-17__col--a">
      <figure class="plx-17__item">
        <div class="plx-17__frame plx-17__frame--tall"><img class="plx-17__plate" src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&auto=format&fit=crop" alt="Row of garments hanging on a rail in daylight" loading="lazy" decoding="async"></div>
        <figcaption class="plx-17__cap">01 · Rail, morning light</figcaption>
      </figure>
      <figure class="plx-17__item">
        <div class="plx-17__frame"><img class="plx-17__plate" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=900&auto=format&fit=crop" alt="Two watches arranged on a pale surface" loading="lazy" decoding="async"></div>
        <figcaption class="plx-17__cap">02 · Accessories</figcaption>
      </figure>
    </div>
    <div class="plx-17__col plx-17__col--b">
      <figure class="plx-17__item">
        <div class="plx-17__frame"><img class="plx-17__plate" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=900&auto=format&fit=crop" alt="Portrait in a hooded knit against a painted door" loading="lazy" decoding="async"></div>
        <figcaption class="plx-17__cap">03 · Knit, oversized</figcaption>
      </figure>
      <figure class="plx-17__item">
        <div class="plx-17__frame plx-17__frame--tall"><img class="plx-17__plate" src="https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1000&auto=format&fit=crop" alt="Shop interior with folded garments and warm lighting" loading="lazy" decoding="async"></div>
        <figcaption class="plx-17__cap">04 · Store, Rue Bertin</figcaption>
      </figure>
    </div>
    <div class="plx-17__col plx-17__col--c">
      <figure class="plx-17__item">
        <div class="plx-17__frame plx-17__frame--tall"><img class="plx-17__plate" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=1000&auto=format&fit=crop" alt="Portrait lit in cool violet light" loading="lazy" decoding="async"></div>
        <figcaption class="plx-17__cap">05 · Evening trial</figcaption>
      </figure>
      <figure class="plx-17__item">
        <div class="plx-17__frame"><img class="plx-17__plate" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=900&auto=format&fit=crop" alt="Portrait laughing in soft daylight" loading="lazy" decoding="async"></div>
        <figcaption class="plx-17__cap">06 · Between takes</figcaption>
      </figure>
    </div>
  </div>
  <footer class="plx-17__foot">
    <p class="plx-17__lede">Every frame drifts at its column's rate — 4.3%, 9.5% and 6.6% of its own height. The captions never move.</p>
  </footer>
</div>
```
## CSS
```css
.plx-17 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Didot", "Playfair Display", "Hoefler Text", Georgia, serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --stone: #eae7e1;
  --paper: #f7f6f3;
  --ink: #1e1c19;
  --muted: #77726a;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-17 * {
  box-sizing: border-box;
}

.plx-17__head {
  padding: clamp(40px, 8vw, 108px) clamp(20px, 5vw, 66px) clamp(28px, 5vw, 58px);
  max-inline-size: 46rem;
}

.plx-17__label {
  margin: 0 0 20px;
  font: 500 10px/1 var(--font-body);
  letter-spacing: 0.4em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-17__h1 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(30px, 6.6vw, 62px);
  font-weight: 400;
  line-height: 1.04;
  letter-spacing: 0.01em;
}

.plx-17__lede {
  margin: 0;
  max-inline-size: 28rem;
  font-size: clamp(14px, 3.2vw, 16px);
  line-height: 1.66;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-17__grid {
  display: grid;
  gap: clamp(16px, 3vw, 34px);
  padding-inline: clamp(20px, 5vw, 66px);
  padding-block-end: clamp(40px, 7vw, 80px);
  grid-template-columns: 1fr;
}

.plx-17__col {
  display: grid;
  gap: clamp(16px, 3vw, 34px);
  min-inline-size: 0;
  align-content: start;
}

.plx-17__item {
  margin: 0;
  min-inline-size: 0;
}

.plx-17__frame {
  position: relative;
  overflow: clip;
  aspect-ratio: 4 / 5;
  background: var(--stone);
}

.plx-17__frame--tall {
  aspect-ratio: 3 / 4.4;
}

.plx-17__plate {
  position: absolute;
  inset-block-start: 0;
  inset-inline: 0;
  display: block;
  inline-size: 100%;
  block-size: 116%;
  object-fit: cover;
  will-change: transform;
}

.plx-17__cap {
  margin: 12px 0 0;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-17__foot {
  padding: clamp(30px, 6vw, 70px) clamp(20px, 5vw, 66px) 130px;
  border-top: 1px solid #e1ded8;
}

@media (min-width: 780px) {
  .plx-17__grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    align-items: start;
  }

  .plx-17__col--b {
    margin-block-start: 52px;
  }

  .plx-17__col--c {
    margin-block-start: 24px;
  }
}

@supports (animation-timeline: view()) {
  .plx-17__plate {
    animation-timing-function: linear;
    animation-fill-mode: both;
    animation-timeline: view();
  }

  .plx-17__col--a .plx-17__plate {
    animation-name: plx-17-slow;
  }

  .plx-17__col--b .plx-17__plate {
    animation-name: plx-17-fast;
  }

  .plx-17__col--c .plx-17__plate {
    animation-name: plx-17-mid;
  }
}

@keyframes plx-17-slow {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-4.3%);
  }
}

@keyframes plx-17-fast {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-9.5%);
  }
}

@keyframes plx-17-mid {
  from {
    transform: translateY(-0.6%);
  }

  to {
    transform: translateY(-7.2%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-17__plate {
    animation: none !important;
    transform: none !important;
    inset-block: 0;
    block-size: 100%;
    will-change: auto;
  }
}
```
