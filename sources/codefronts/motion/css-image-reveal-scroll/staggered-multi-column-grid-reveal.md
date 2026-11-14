---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/staggered-multi-column-grid-reveal/"
title: "Staggered Multi-Column Grid Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "A gallery that cascades in as you scroll — and the one demo that teaches the most important rule of scroll-driven animation: animation-delay does nothing,…"
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Staggered Multi-Column Grid Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/staggered-multi-column-grid-reveal/

A gallery that cascades in as you scroll — and the one demo that teaches the most important rule of scroll-driven animation: animation-delay does nothing, because there is no clock. The stagger comes from offsetting each tile's animation-range with calc() and an --i index, so the cascade is tied to scroll position rather than to time.
## HTML
```html
<section class="rv-06" tabindex="0" role="region" aria-label="Staggered gallery reveal demo">
  <p class="rv-06__hint">scroll inside to cascade the gallery <span aria-hidden="true">&#8595;</span></p>

  <ul class="rv-06__grid">
    <li style="--i:0"><img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=600&q=68" alt="Sunlight through green forest leaves" width="600" height="800" loading="lazy" decoding="async"></li>
    <li style="--i:1"><img src="https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?auto=format&fit=crop&w=600&q=68" alt="Pink flowers in soft focus" width="600" height="800" loading="lazy" decoding="async"></li>
    <li style="--i:2"><img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?auto=format&fit=crop&w=600&q=68" alt="Calm lake between mountains" width="600" height="800" loading="lazy" decoding="async"></li>
    <li style="--i:3"><img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=600&q=68" alt="Snowy mountain ridge under a night sky" width="600" height="600" loading="lazy" decoding="async"></li>
    <li style="--i:4"><img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=600&q=68" alt="Mountain range above low clouds" width="600" height="600" loading="lazy" decoding="async"></li>
    <li style="--i:5"><img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=600&q=68" alt="City street grid photographed from above" width="600" height="600" loading="lazy" decoding="async"></li>
  </ul>
  <p class="rv-06__note">stagger via animation-range offsets &#8212; delay has no meaning here</p>

  <div class="rv-06__uc">
    <p class="rv-06__uclabel"><b>real-world use case</b> editorial blog &#183; photo essay</p>
    <div class="shell pad">
      <div class="col intro">
        <p class="eyebrow">Field notes &#183; 12 min read</p>
        <h4>Six mornings above the treeline</h4>
        <p class="body">Photographs from a week spent walking the ridge before sunrise, when the valley is still holding last night's weather.</p>
      </div>
      <ul class="rv-06__grid essay">
        <li style="--i:0"><img src="https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?auto=format&fit=crop&w=500&q=65" alt="Pink flowers in soft focus" width="500" height="667" loading="lazy" decoding="async"></li>
        <li style="--i:1"><img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?auto=format&fit=crop&w=500&q=65" alt="Calm lake between mountains" width="500" height="667" loading="lazy" decoding="async"></li>
        <li style="--i:2"><img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=500&q=65" alt="Mountain range above low clouds" width="500" height="667" loading="lazy" decoding="async"></li>
        <li style="--i:3"><img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=500&q=65" alt="Snowy mountain ridge under a night sky" width="500" height="667" loading="lazy" decoding="async"></li>
      </ul>
      <p class="credit">Ridge line, 05:40 &#8212; Fujifilm X-T5, 35mm</p>
    </div>
    <p class="why">Alternating margin-top plus a 7% range step gives a masonry cascade that scrubs both ways &#8212; no library, no delay ladder.</p>
  </div>
</section>
```
## CSS
```css
.rv-06 {
  --accent: oklch(0.88 0.19 118);
  --stage: 100vh;
  --step: 8%;
  font-family: system-ui,'Segoe UI',sans-serif;
  height: var(--stage);
  overflow-y: auto;
  overflow-x: hidden;
  padding: 0 20px;
  border-radius: 16px;
  border: 1px solid oklch(1 0 0/.1);
  background: linear-gradient(oklch(0.16 0.01 260),oklch(0.19 0.012 260));
}

.rv-06 * {
  box-sizing: border-box;
}

.rv-06__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(120px,1fr));
  gap: 12px;
  list-style: none;
  margin: 60% 0 0;
  padding: 0;
}

.rv-06__grid li {
  margin: 0;
}

.rv-06__grid li:nth-child(2) {
  margin-top: 22px;
}

.rv-06 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 3/4;
  object-fit: cover;
  border-radius: 12px;
}

.rv-06__grid li:nth-child(n+4) img {
  aspect-ratio: 1/1;
}

.rv-06__note {
  margin: 14px 0 30%;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}
/* ── the cascade: the stagger is a SHIFTED RANGE, not a delay ── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-06__grid li {
      animation: rv06-rise linear both;
      animation-timeline: view();
      animation-range: entry calc(60% + var(--i) * var(--step)) contain calc(20% + var(--i) * var(--step));
    }
  }
}

@keyframes rv06-rise {
  from {
    opacity: 0;
    transform: translateY(58px) scale(.97);
  }

  to {
    opacity: 1;
    transform: none;
  }
}
/* ── fallback: here a time-based delay ladder IS correct ─────── */

@supports not (animation-timeline: view()) {
  .rv-06__grid li {
    opacity: 0;
    transform: translateY(58px);
    transition: opacity .7s ease,transform .7s cubic-bezier(.22,1,.36,1);
    transition-delay: calc(var(--i) * 70ms);
  }

  .rv-06__grid li.is-in {
    opacity: 1;
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-06__grid li {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-06__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-06__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-06__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.6vw,30px)/1.14 system-ui,sans-serif;
  letter-spacing: -.026em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-06__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-06__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-06__uc p.body {
  margin: 0;
  font: 400 13.5px/1.65 system-ui,sans-serif;
  color: oklch(1 0 0/.6);
}

.rv-06__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-06__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-06__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-06__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-06__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-06__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-06__uc .col {
  display: grid;
  gap: 6px;
}

.rv-06__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-06__uc {
  margin: 0 0 110%;
}

.rv-06__uc .shell.pad {
  padding: 22px;
}

.rv-06__uc .col.intro {
  gap: 8px;
  margin-bottom: 18px;
}

.rv-06__uc .body {
  max-width: 62ch;
}

.rv-06__uc .rv-06__grid.essay {
  grid-template-columns: repeat(auto-fit,minmax(105px,1fr));
  margin: 0;
}

.rv-06__uc .essay li:nth-child(2),
.rv-06__uc .essay li:nth-child(4) {
  margin-top: 18px;
}

.rv-06__uc .essay img {
  aspect-ratio: 3/4;
  border-radius: 10px;
}

.rv-06__uc .credit {
  margin: 14px 0 0;
  font: 400 12px/1.5 system-ui,sans-serif;
  color: oklch(1 0 0/.45);
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. On a scroll timeline the stagger is a shifted
   animation-range; in this fallback there IS a clock, so a transition-delay ladder is the
   right tool (see the @supports not block in the CSS). */
if (!CSS.supports('animation-timeline: view()')) {
  const io = new IntersectionObserver((entries, obs) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      obs.unobserve(entry.target);
    }
  }, { threshold: 0.15 });

  document.querySelectorAll('.rv-06__grid li').forEach((el) => io.observe(el));
}
```
