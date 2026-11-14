---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/corner-radial-iris-reveal/"
title: "Corner Radial Iris Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "A clip-path circle anchored off-frame at a corner, sweeping diagonally across the image like a camera iris."
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Corner Radial Iris Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/corner-radial-iris-reveal/

A clip-path circle anchored off-frame at a corner, sweeping diagonally across the image like a camera iris. Same single animated value as the centre spotlight, completely different character — and the demo that teaches the sqrt(2) radius rule that catches almost everyone who tries this.
## HTML
```html
<section class="rv-10" tabindex="0" role="region" aria-label="Corner iris reveal demo">
  <p class="rv-10__hint">scroll inside to open the iris <span aria-hidden="true">&#8595;</span></p>

  <figure class="rv-10__item">
    <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=72"
         alt="Earth at night seen from orbit" width="1200" height="750"
         loading="lazy" decoding="async">
    <figcaption>clip-path: circle(0% at 0% 0%) &#8594; circle(142%)</figcaption>
  </figure>

  <figure class="rv-10__item rv-10__item--br">
    <p class="rv-10__badge">variant b &#183; bottom-right origin</p>
    <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1200&q=72"
         alt="Soft studio light across a plain wall" width="1200" height="750"
         loading="lazy" decoding="async">
    <figcaption>clip-path: circle(0% at 100% 100%) &#8594; circle(142%)</figcaption>
  </figure>

  <div class="rv-10__item rv-10__uc">
    <p class="rv-10__uclabel"><b>real-world use case</b> app marketing &#183; feature card grid</p>
    <div class="cards">
      <div class="shell">
        <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=700&q=70" alt="Earth at night seen from orbit" width="700" height="525" loading="lazy" decoding="async">
        <div class="pad col"><p class="eyebrow">Global</p><h5>42 regions, one latency budget</h5><p class="body">Edge routing that keeps p95 under 80ms wherever your users open the app.</p></div>
      </div>
      <div class="shell mirror">
        <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=700&q=70" alt="Soft studio light across a plain wall" width="700" height="525" loading="lazy" decoding="async">
        <div class="pad col"><p class="eyebrow">Offline</p><h5>Works on the Tube</h5><p class="body">Local-first writes, conflict-free sync when signal comes back.</p></div>
      </div>
    </div>
    <p class="why">Mirroring the origin corner card-to-card gives a grid visual rhythm for the price of one extra keyframe &#8212; the irises open toward each other instead of marching in lockstep.</p>
  </div>
</section>
```
## CSS
```css
.rv-10 {
  --accent: oklch(0.88 0.19 118);
  --stage: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  height: var(--stage);
  overflow-y: auto;
  overflow-x: hidden;
  padding: 0 22px;
  border-radius: 16px;
  border: 1px solid oklch(1 0 0/.1);
  background: linear-gradient(oklch(0.16 0.01 260),oklch(0.19 0.012 260));
}

.rv-10 * {
  box-sizing: border-box;
}

.rv-10__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-10__item {
  margin: 0 auto 0%;
  padding-top: 50%;
  width: 500px;
}

.rv-10__item:last-child {
  padding-bottom: 66%;
}

.rv-10__badge {
  display: inline-block;
  margin: 0 0 10px;
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--accent);
  background: oklch(0.88 0.19 118/.1);
  border: 1px solid oklch(0.88 0.19 118/.28);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-10 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16/10;
  object-fit: cover;
  border-radius: 18px;
}

.rv-10 figcaption {
  margin-top: 14px;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-10 img {
      animation: rv10-iris linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }

    .rv-10__item--br img {
      animation-name: rv10-iris-br;
    }
  }
}
/* 142% = 100% x sqrt(2) — from a corner the disc must reach the far corner */

@keyframes rv10-iris {
  from {
    clip-path: circle(0% at 0% 0%);
  }

  to {
    clip-path: circle(142% at 0% 0%);
  }
}

@keyframes rv10-iris-br {
  from {
    clip-path: circle(0% at 100% 100%);
  }

  to {
    clip-path: circle(142% at 100% 100%);
  }
}

@supports not (animation-timeline: view()) {
  .rv-10 img {
    clip-path: circle(0% at 0% 0%);
    transition: clip-path 1s cubic-bezier(.22,1,.36,1);
  }

  .rv-10__item--br img {
    clip-path: circle(0% at 100% 100%);
  }

  .rv-10__item.is-in img {
    clip-path: circle(142% at 0% 0%);
  }

  .rv-10__item--br.is-in img {
    clip-path: circle(142% at 100% 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-10 img {
    clip-path: none;
    transition: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-10__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-10__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-10__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.8vw,34px)/1.1 system-ui,sans-serif;
  letter-spacing: -.028em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-10__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-10__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-10__uc p.body {
  margin: 0;
  font: 400 13px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.58);
}

.rv-10__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-10__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-10__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-10__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-10__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-10__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-10__uc .over {
  position: relative;
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.13 0.008 260);
}

.rv-10__uc .col {
  display: grid;
  gap: 6px;
}

.rv-10__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-10__uc {
  padding-bottom: 110%;
}

.rv-10__uc .cards {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(190px,1fr));
  gap: 14px;
}

.rv-10__uc .shell img {
  aspect-ratio: 4/3;
  border-radius: 0;
}

.rv-10__uc .pad {
  padding: 16px 18px;
  gap: 6px;
}
/* mirrored origin, alternating card to card */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-10__uc .shell img {
      animation: rv10-iris linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }

    .rv-10__uc .shell.mirror img {
      animation-name: rv10-iris-br;
      animation-range: entry 60% contain 20%;
    }
  }
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. */
if (!CSS.supports('animation-timeline: view()')) {
  const io = new IntersectionObserver((entries, obs) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      obs.unobserve(entry.target);
    }
  }, { threshold: 0.2 });

  document.querySelectorAll('.rv-10__item').forEach((el) => io.observe(el));
}
```
