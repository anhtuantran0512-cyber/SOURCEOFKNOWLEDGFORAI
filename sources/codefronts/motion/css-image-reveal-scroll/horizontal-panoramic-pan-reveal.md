---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/horizontal-panoramic-pan-reveal/"
title: "Horizontal Panoramic Pan Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "Axis conversion: the visitor scrolls vertically and the image pans horizontally, so a wide interior or landscape reads as a continuous camera move."
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Panoramic Pan Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/horizontal-panoramic-pan-reveal/

Axis conversion: the visitor scrolls vertically and the image pans horizontally, so a wide interior or landscape reads as a continuous camera move. Two implementations — an animated object-position (one property, no wrapper, recommended) and an oversized translateX inside a clipped frame when you also want parallax depth.
## HTML
```html
<section class="rv-11" tabindex="0" role="region" aria-label="Panoramic pan reveal demo">
  <p class="rv-11__hint">scroll inside to pan the panorama <span aria-hidden="true">&#8595;</span></p>

  <figure class="rv-11__item">
    <div class="rv-11__frame">
      <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=2000&q=72"
           alt="Wide panorama of a snowy mountain ridge at night" width="2000" height="857"
           loading="lazy" decoding="async">
    </div>
    <figcaption>transform: translateX(-24%) &#8594; 0 &#183; img is 132% wide</figcaption>
  </figure>

  <figure class="rv-11__item rv-11__item--transform">
    <p class="rv-11__badge">variant b &#183; oversized translateX (adds parallax)</p>
    <div class="rv-11__frame">
      <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=2000&q=72"
           alt="Mountain range above low cloud, panoramic crop" width="2000" height="857"
           loading="lazy" decoding="async">
    </div>
    <figcaption>transform: translateX(-24%) &#8594; 0 &#183; img is 132% wide</figcaption>
  </figure>

  <figure class="rv-11__item rv-11__uc">
    <p class="rv-11__uclabel"><b>real-world use case</b> property listing &#183; gallery hero</p>
    <div class="shell">
      <div class="rv-11__frame">
        <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=1600&q=70" alt="Panoramic interior of a renovated apartment" width="1600" height="686" loading="lazy" decoding="async">
      </div>
      <div class="row">
        <div class="col">
          <p class="eyebrow">Just listed &#183; Clifton, Bristol</p>
          <h5>Two-bed garden flat, Georgian conversion</h5>
          <div class="meta"><span>2 bed</span><span>1 bath</span><span>81 m&#178;</span><span>EPC C</span></div>
        </div>
        <div class="cta"><span class="price">&#163;425,000</span><span class="btn">Book a viewing</span></div>
      </div>
    </div>
    <p class="why">Property galleries live or die on wide interiors. Panning the crop as the visitor scrolls shows the whole room without a carousel, without a drag interaction, and without stealing the scroll.</p>
  </figure>
</section>
```
## CSS
```css
.rv-11 {
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

.rv-11 * {
  box-sizing: border-box;
}

.rv-11__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}
/* cover ranges need a runway TALLER than the stage before and after each subject.
   % margins are width-relative, so the min-height floors guarantee it in narrow embeds. */

.rv-11__item {
  margin: 0 auto 20%;
  padding-top: 20%;
  width: 620px;
  min-height: 710px;
}

.rv-11__item:last-child {
  padding-bottom: 20%;
}

.rv-11__badge {
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

.rv-11 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16/10;
  object-fit: cover;
  border-radius: 18px;
}
/* clip, not hidden — hidden would become the view() timeline source */

.rv-11__frame {
  overflow: clip;
  border-radius: 18px;
}

.rv-11__frame img {
  width: 132%;
  border-radius: 0;
}

.rv-11 figcaption {
  margin-top: 14px;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}
/* ── COVER range: a pan needs the element's whole journey ────── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-11__frame img {
      animation: rv11-pan-tf linear both;
      animation-timeline: view();
      animation-range: entry 40% exit 20%;
    }
  }
}

@keyframes rv11-pan-obj {
  from {
    object-position: 0% 50%;
  }

  to {
    object-position: 100% 50%;
  }
}

@keyframes rv11-pan-tf {
  from {
    transform: translateX(-24%);
  }

  to {
    transform: translateX(0);
  }
}

@supports not (animation-timeline: view()) {
  .rv-11__frame img {
    transform: translateX(calc(-24% * (1 - var(--p,0))));
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-11 img {
    object-position: 50% 50%;
    transform: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-11__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-11__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-11__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.8vw,34px)/1.1 system-ui,sans-serif;
  letter-spacing: -.028em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-11__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-11__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-11__uc p.body {
  margin: 0;
  font: 400 13px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.58);
}

.rv-11__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-11__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-11__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-11__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-11__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-11__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-11__uc .over {
  position: relative;
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.13 0.008 260);
}

.rv-11__uc .col {
  display: grid;
  gap: 6px;
}

.rv-11__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-11__uc .shell img {
  border-radius: 0;
}

.rv-11__uc .row {
  display: flex;
  gap: 18px;
  align-items: flex-end;
  justify-content: space-between;
  flex-wrap: wrap;
  padding: 20px 22px;
}

.rv-11__uc .col {
  gap: 7px;
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. Writes a 0-1 journey progress so Firefox pans too. */
if (!CSS.supports('animation-timeline: view()')) {
  const items = [...document.querySelectorAll('.rv-11__item')];
  let queued = false;

  const update = () => {
    queued = false;
    for (const el of items) {
      const r = el.getBoundingClientRect();
      const span = window.innerHeight + r.height;     // the full cover journey
      const p = Math.min(1, Math.max(0, (window.innerHeight - r.top) / span));
      el.style.setProperty('--p', p.toFixed(3));
    }
  };

  const onScroll = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  update();
}
```
