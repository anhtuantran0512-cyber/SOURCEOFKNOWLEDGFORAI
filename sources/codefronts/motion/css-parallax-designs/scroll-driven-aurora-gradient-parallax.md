---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/scroll-driven-aurora-gradient-parallax/"
title: "Scroll Driven Aurora Gradient Parallax"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "An ambient aurora that lives behind the content: three blurred gradient planes drift and hue-shift on scroll while the copy stays completely still, so the…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Driven Aurora Gradient Parallax
Source: https://codefronts.com/motion/css-parallax-designs/scroll-driven-aurora-gradient-parallax/

An ambient aurora that lives behind the content: three blurred gradient planes drift and hue-shift on scroll while the copy stays completely still, so the page feels alive without anything the reader is trying to read moving. Ships a pure-CSS dawn/dusk switch because the same gradient reads as two entirely different products.
## HTML
```html
<div class="plx-11">
  <div class="plx-11__field" aria-hidden="true">
    <span class="plx-11__plane plx-11__plane--1"></span>
    <span class="plx-11__plane plx-11__plane--2"></span>
    <span class="plx-11__plane plx-11__plane--3"></span>
  </div>
  <div class="plx-11__switch">
    <input class="plx-11__box" type="checkbox" id="plx-11-theme">
    <label class="plx-11__label" for="plx-11-theme">
      <span class="plx-11__dot" aria-hidden="true"></span>
      <span class="plx-11__t plx-11__t--dusk">Dusk</span><span class="plx-11__t plx-11__t--dawn">Dawn</span>
    </label>
  </div>
  <header class="plx-11__hero">
    <p class="plx-11__eyebrow">Meridian · Ship 04</p>
    <h1 class="plx-11__h1">Ambient depth, no moving text</h1>
    <p class="plx-11__lede">Three gradient planes drift and hue-shift behind the page. Everything you are reading stays exactly where it is.</p>
    <div class="plx-11__actions">
      <a class="plx-11__cta" href="#plx-11-notes">Release notes</a>
      <a class="plx-11__ghost" href="#plx-11-notes">Watch the keynote</a>
    </div>
  </header>
  <main class="plx-11__main" id="plx-11-notes">
    <section class="plx-11__block">
      <h2 class="plx-11__h2">Edge compute, regional by default</h2>
      <p class="plx-11__p">Functions now deploy to the three regions closest to your traffic without a configuration change. Cold starts land under 40ms at p95 across all of them.</p>
    </section>
    <section class="plx-11__block">
      <h2 class="plx-11__h2">Queues that survive a bad deploy</h2>
      <p class="plx-11__p">Messages are held for twelve hours and replayed in order once health checks pass. There is no dead-letter step to babysit.</p>
    </section>
    <section class="plx-11__block">
      <h2 class="plx-11__h2">Observability without an agent</h2>
      <p class="plx-11__p">Traces are collected at the runtime boundary, so nothing is installed inside your image. Retention is thirty days on every plan.</p>
    </section>
    <p class="plx-11__foot">Keep scrolling — the hue rotation is bound to scroll position, so the palette at the bottom of the page is not the palette at the top.</p>
  </main>
</div>
```
## CSS
```css
.plx-11 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "IBM Plex Mono", "JetBrains Mono", ui-monospace, monospace;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --bg: #0a0618;
  --ink: #f2ecff;
  --muted: #a394c9;
  --accent: #7df0e0;
  --card: rgba(28,18,52,0.62);
  --edge: rgba(180,150,255,0.24);
  --a1: #2de2c0;
  --a2: #7b5cff;
  --a3: #ff5fc8;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
  isolation: isolate;
}

.plx-11 * {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.15 200)) {
  .plx-11 {
    --a1: oklch(0.84 0.14 178);
    --a2: oklch(0.62 0.22 288);
    --a3: oklch(0.74 0.2 344);
  }
}

.plx-11__field {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: clip;
}

.plx-11__plane {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  will-change: transform, filter;
}

.plx-11__plane--1 {
  inline-size: 78vmax;
  aspect-ratio: 1.2;
  top: -26vmax;
  left: -18vmax;
  background: radial-gradient(closest-side, var(--a1), transparent 72%);
  opacity: 0.55;
}

.plx-11__plane--2 {
  inline-size: 66vmax;
  aspect-ratio: 1;
  top: 18vh;
  right: -22vmax;
  background: radial-gradient(closest-side, var(--a2), transparent 70%);
  opacity: 0.6;
}

.plx-11__plane--3 {
  inline-size: 58vmax;
  aspect-ratio: 1.4;
  bottom: -22vmax;
  left: 12vw;
  background: radial-gradient(closest-side, var(--a3), transparent 74%);
  opacity: 0.45;
}

.plx-11__switch {
  position: absolute;
  z-index: 4;
  top: 18px;
  right: 18px;
}

.plx-11__box {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: clip;
}

.plx-11__label {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 999px;
  border: 1px solid var(--edge);
  background: var(--card);
  color: var(--ink);
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  cursor: pointer;
}

.plx-11__box:focus-visible + .plx-11__label {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.plx-11__dot {
  inline-size: 10px;
  block-size: 10px;
  border-radius: 50%;
  background: currentColor;
  opacity: 0.85;
}

.plx-11__t--dawn {
  display: none;
}

.plx-11__hero {
  position: relative;
  z-index: 2;
  min-block-size: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 18px;
  padding: clamp(26px, 6vw, 84px);
  max-inline-size: 58rem;
}

.plx-11__eyebrow {
  margin: 0;
  font: 600 10px/1 var(--font-display);
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-11__h1 {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(28px, 6.4vw, 62px);
  font-weight: 500;
  line-height: 1.04;
  letter-spacing: -0.03em;
}

.plx-11__lede {
  margin: 0;
  max-inline-size: 32rem;
  font-size: clamp(15px, 3.2vw, 18px);
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-11__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.plx-11__cta,
.plx-11__ghost {
  display: inline-flex;
  align-items: center;
  min-height: 46px;
  padding: 0 20px;
  border-radius: 10px;
  font: 600 13px/1 var(--font-display);
  letter-spacing: 0.06em;
  text-decoration: none;
}

.plx-11__cta {
  background: var(--accent);
  color: #04211d;
}

.plx-11__ghost {
  border: 1px solid var(--edge);
  color: var(--ink);
  background: var(--card);
}

.plx-11__cta:hover {
  filter: brightness(1.08);
}

.plx-11__ghost:hover {
  border-color: var(--accent);
}

.plx-11__cta:focus-visible,
.plx-11__ghost:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.plx-11__main {
  position: relative;
  z-index: 2;
  padding: clamp(30px, 6vw, 84px);
  display: grid;
  gap: 18px;
  max-inline-size: 62rem;
}

.plx-11__block {
  min-inline-size: 0;
  padding: clamp(18px, 3vw, 28px);
  border-radius: 18px;
  border: 1px solid var(--edge);
  background: var(--card);
  box-shadow: 0 0 60px -30px var(--a2);
}

.plx-11__h2 {
  margin: 0 0 10px;
  font-family: var(--font-display);
  font-size: clamp(18px, 3.4vw, 26px);
  font-weight: 500;
  letter-spacing: -0.02em;
}

.plx-11__p {
  margin: 0;
  font-size: 15px;
  line-height: 1.68;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-11__foot {
  margin: 20px 0 60px;
  max-inline-size: 34rem;
  font-size: 13px;
  line-height: 1.7;
  color: var(--muted);
}

.plx-11:has(.plx-11__box:checked) {
  --bg: #fdf3f0;
  --ink: #22132c;
  --muted: #6b5470;
  --accent: #d6407f;
  --card: rgba(255,255,255,0.66);
  --edge: rgba(120,70,130,0.18);
  --a1: #ffd7a8;
  --a2: #ffa7c4;
  --a3: #b7c7ff;
}

.plx-11:has(.plx-11__box:checked) .plx-11__t--dusk {
  display: none;
}

.plx-11:has(.plx-11__box:checked) .plx-11__t--dawn {
  display: inline;
}

.plx-11[data-theme="light"] {
  --bg: #fdf3f0;
  --ink: #22132c;
  --muted: #6b5470;
  --accent: #d6407f;
  --card: rgba(255,255,255,0.66);
  --edge: rgba(120,70,130,0.18);
  --a1: #ffd7a8;
  --a2: #ffa7c4;
  --a3: #b7c7ff;
}

.plx-11[data-theme="dark"] {
  --bg: #0a0618;
  --ink: #f2ecff;
  --muted: #a394c9;
  --accent: #7df0e0;
  --card: rgba(28,18,52,0.62);
  --edge: rgba(180,150,255,0.24);
  --a1: #2de2c0;
  --a2: #7b5cff;
  --a3: #ff5fc8;
}

@media (prefers-color-scheme: light) {
  .plx-11 {
    --bg: #fdf3f0;
    --ink: #22132c;
    --muted: #6b5470;
    --accent: #d6407f;
    --card: rgba(255,255,255,0.66);
    --edge: rgba(120,70,130,0.18);
    --a1: #ffd7a8;
    --a2: #ffa7c4;
    --a3: #b7c7ff;
  }

  .plx-11 .plx-11__t--dusk {
    display: none;
  }

  .plx-11 .plx-11__t--dawn {
    display: inline;
  }

  .plx-11:has(.plx-11__box:checked) {
    --bg: #0a0618;
    --ink: #f2ecff;
    --muted: #a394c9;
    --accent: #7df0e0;
    --card: rgba(28,18,52,0.62);
    --edge: rgba(180,150,255,0.24);
    --a1: #2de2c0;
    --a2: #7b5cff;
    --a3: #ff5fc8;
  }

  .plx-11:has(.plx-11__box:checked) .plx-11__t--dawn {
    display: none;
  }

  .plx-11:has(.plx-11__box:checked) .plx-11__t--dusk {
    display: inline;
  }
}

@media (prefers-color-scheme: dark) {
  .plx-11 {
    --bg: #0a0618;
    --ink: #f2ecff;
    --muted: #a394c9;
    --accent: #7df0e0;
    --card: rgba(28,18,52,0.62);
    --edge: rgba(180,150,255,0.24);
    --a1: #2de2c0;
    --a2: #7b5cff;
    --a3: #ff5fc8;
  }

  .plx-11 .plx-11__t--dawn {
    display: none;
  }

  .plx-11 .plx-11__t--dusk {
    display: inline;
  }

  .plx-11:has(.plx-11__box:checked) {
    --bg: #fdf3f0;
    --ink: #22132c;
    --muted: #6b5470;
    --accent: #d6407f;
    --card: rgba(255,255,255,0.66);
    --edge: rgba(120,70,130,0.18);
    --a1: #ffd7a8;
    --a2: #ffa7c4;
    --a3: #b7c7ff;
  }

  .plx-11:has(.plx-11__box:checked) .plx-11__t--dusk {
    display: none;
  }

  .plx-11:has(.plx-11__box:checked) .plx-11__t--dawn {
    display: inline;
  }
}

@supports (animation-timeline: scroll()) {
  .plx-11__plane--1 {
    animation: plx-11-p1 linear both;
    animation-timeline: scroll(root);
  }

  .plx-11__plane--2 {
    animation: plx-11-p2 linear both;
    animation-timeline: scroll(root);
  }

  .plx-11__plane--3 {
    animation: plx-11-p3 linear both;
    animation-timeline: scroll(root);
  }
}

@keyframes plx-11-p1 {
  to {
    transform: translate3d(6vw, 14vh, 0) scale(1.12);
    filter: blur(60px) hue-rotate(38deg);
  }
}

@keyframes plx-11-p2 {
  to {
    transform: translate3d(-9vw, -12vh, 0) scale(1.18);
    filter: blur(60px) hue-rotate(-30deg);
  }
}

@keyframes plx-11-p3 {
  to {
    transform: translate3d(12vw, -20vh, 0) scale(1.06);
    filter: blur(60px) hue-rotate(46deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-11__plane {
    animation: none !important;
    transform: none !important;
    filter: blur(60px) !important;
    will-change: auto;
  }
}
```
