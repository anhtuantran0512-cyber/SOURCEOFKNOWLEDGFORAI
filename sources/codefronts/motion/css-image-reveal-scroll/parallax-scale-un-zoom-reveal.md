---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/parallax-scale-un-zoom-reveal/"
title: "Parallax Scale & Un-Zoom Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "The GSAP hero effect in ten lines of CSS: the frame's clip window grows outward while the image inside scales down from 1.34 to 1 on the same timeline. The…"
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Scale & Un-Zoom Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/parallax-scale-un-zoom-reveal/

The GSAP hero effect in ten lines of CSS: the frame's clip window grows outward while the image inside scales down from 1.34 to 1 on the same timeline. The counter-motion reads as a camera lens pulling focus rather than a flat scale — the single most requested e-commerce banner reveal, with no animation library.
## HTML
```html
<section class="rv-02" tabindex="0" role="region" aria-label="Parallax un-zoom reveal demo">
  <p class="rv-02__hint">scroll inside to un-zoom <span aria-hidden="true">&#8595;</span></p>

  <figure class="rv-02__item">
    <div class="rv-02__frame">
      <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1400&q=72"
           alt="Aerial view of a coastline with turquoise water" width="1400" height="788"
           loading="lazy" decoding="async">
    </div>
    <figcaption>frame: inset(10% 16%) &#8594; 0 &#183; img: scale(1.34) &#8594; 1</figcaption>
  </figure>

  <figure class="rv-02__item rv-02__item--offset">
    <p class="rv-02__badge">variant b &#183; off-centre origin</p>
    <div class="rv-02__frame">
      <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1400&q=72"
           alt="Mountain range rising above low cloud" width="1400" height="788"
           loading="lazy" decoding="async">
    </div>
    <figcaption>same keyframes &#183; transform-origin: 28% 78%</figcaption>
  </figure>

  <figure class="rv-02__item rv-02__uc">
    <p class="rv-02__uclabel"><b>real-world use case</b> e-commerce &#183; featured collection banner</p>
    <div class="shell">
      <div class="rv-02__frame">
        <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1400&q=70" alt="Sunlight through green forest leaves" width="1400" height="600" loading="lazy" decoding="async">
      </div>
      <div class="row">
        <div class="col">
          <p class="eyebrow">New in &#183; SS26</p>
          <h5>The Trailhead Edit</h5>
          <p class="body">32 pieces &#183; built for weather that changes its mind</p>
        </div>
        <div class="cta"><span class="price">from &#163;128</span><span class="btn">Shop the edit</span></div>
      </div>
    </div>
    <p class="why">A 21:9 banner un-zooms into its frame while the product row stays static &#8212; the motion is entirely in the imagery, so nothing reflows around the price or the CTA.</p>
  </figure>
</section>
```
## CSS
```css
.rv-02 {
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

.rv-02 * {
  box-sizing: border-box;
}

.rv-02__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-02__item {
  margin: 0 auto;
  padding-top: 60%;
  width: 500px;
}

.rv-02__item:last-child {
  padding-bottom: 66%;
}

.rv-02__badge {
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
/* clip, NOT hidden — a hidden box is a scroll container and would hijack view() */

.rv-02__frame {
  overflow: clip;
  border-radius: 10px;
}

.rv-02 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16/9;
  object-fit: cover;
  transform-origin: 50% 50%;
}

.rv-02__item--offset img {
  transform-origin: 28% 78%;
}

.rv-02 figcaption {
  margin-top: 14px;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}
/* ── the reveal: frame opens out, image scales down, same timeline ─ */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-02__frame {
      animation: rv02-frame linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }

    .rv-02 img {
      animation: rv02-unzoom linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }
  }
}

@keyframes rv02-frame {
  from {
    clip-path: inset(10% 16% round 26px);
  }

  to {
    clip-path: inset(0% round 10px);
  }
}

@keyframes rv02-unzoom {
  from {
    transform: scale(1.34);
  }

  to {
    transform: scale(1);
  }
}
/* ── fallback: --p is written by the js field below ──────────── */

@supports not (animation-timeline: view()) {
  .rv-02 img {
    transform: scale(calc(1 + .34 * (1 - var(--p,0))));
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-02 img {
    transform: none;
  }

  .rv-02__frame {
    clip-path: inset(0 round 10px);
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-02__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-02__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-02__uc {
  --pad: clamp(18px,4vw,42px);
}

.rv-02__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.6vw,32px)/1.12 system-ui,sans-serif;
  letter-spacing: -.028em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-02__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-02__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-02__uc p.body {
  margin: 0;
  font: 400 13.5px/1.65 system-ui,sans-serif;
  color: oklch(1 0 0/.6);
}

.rv-02__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-02__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-02__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-02__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-02__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-02__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-02__uc .over {
  position: relative;
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.13 0.008 260);
}

.rv-02__uc .scrim {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.rv-02__uc .copy {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 14px;
  padding: var(--pad);
}

.rv-02__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-02__uc .shell .rv-02__frame {
  border-radius: 0;
}

.rv-02__uc .shell img {
  aspect-ratio: 21/9;
}

.rv-02__uc .row {
  display: flex;
  gap: 18px;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  padding: 20px 22px;
}

.rv-02__uc .col {
  display: grid;
  gap: 6px;
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. Writes a 0-1 scroll progress custom property so
   Firefox gets the same un-zoom the CSS does natively elsewhere. rAF-throttled + passive. */
if (!CSS.supports('animation-timeline: view()')) {
  const frames = [...document.querySelectorAll('.rv-02__item')];
  let queued = false;

  const update = () => {
    queued = false;
    for (const el of frames) {
      const r = el.getBoundingClientRect();
      const p = 1 - Math.min(1, Math.max(0, r.top / window.innerHeight));
      el.style.setProperty('--p', p.toFixed(3));
    }
  };

  const onScroll = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  update();
}
```
