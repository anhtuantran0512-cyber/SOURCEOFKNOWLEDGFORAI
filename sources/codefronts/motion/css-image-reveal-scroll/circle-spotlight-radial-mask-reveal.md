---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/circle-spotlight-radial-mask-reveal/"
title: "Circle / Spotlight Radial Mask Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "A product launch reveal: clip-path: circle(0%) opens to circle(80%), unveiling the image as if a spotlight were being brought up on it."
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circle / Spotlight Radial Mask Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/circle-spotlight-radial-mask-reveal/

A product launch reveal: clip-path: circle(0%) opens to circle(80%), unveiling the image as if a spotlight were being brought up on it. One animated value, plus a static radial-gradient vignette that sells the lamp without a second animation. Includes the feathered mask-image variant for a soft edge.
## HTML
```html
<section class="rv-03" tabindex="0" role="region" aria-label="Spotlight mask reveal demo">
  <p class="rv-03__hint">scroll inside to open the spotlight <span aria-hidden="true">&#8595;</span></p>

  <figure class="rv-03__item">
    <div class="rv-03__frame">
      <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=1200&q=72"
           alt="Minimal analogue wristwatch on a plain background" width="1200" height="900"
           loading="lazy" decoding="async">
      <span class="rv-03__vignette" aria-hidden="true"></span>
    </div>
    <figcaption>clip-path: circle(0% at 50% 50%) &#8594; circle(80%)</figcaption>
  </figure>

  <figure class="rv-03__item rv-03__item--soft">
    <p class="rv-03__badge">variant b &#183; feathered mask</p>
    <div class="rv-03__frame">
      <img src="https://images.unsplash.com/photo-1560472354-b33ff0c44a43?auto=format&fit=crop&w=1200&q=72"
           alt="Bright collaborative workspace with plants" width="1200" height="900"
           loading="lazy" decoding="async">
    </div>
    <figcaption>mask-image: radial-gradient() &#183; soft falloff, no hard edge</figcaption>
  </figure>

  <figure class="rv-03__item rv-03__uc">
    <p class="rv-03__uclabel"><b>real-world use case</b> product launch &#183; feature highlight</p>
    <div class="split">
      <div class="rv-03__frame">
        <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=70" alt="Minimal analogue wristwatch on a plain background" width="900" height="900" loading="lazy" decoding="async">
        <span class="rv-03__vignette" aria-hidden="true"></span>
      </div>
      <div class="col">
        <p class="eyebrow">Introducing</p>
        <h5>Meridian 38 &#8212; automatic</h5>
        <p class="body">Sapphire crystal, 72-hour reserve, 38mm brushed case. Six hundred made.</p>
        <div class="chips"><span>72h reserve</span><span>100m WR</span><span>ltd. 600</span></div>
        <div class="cta"><span class="price">$1,240</span><span class="btn">Pre-order</span></div>
      </div>
    </div>
    <p class="why">The spotlight opens on the product while the spec column stays perfectly still &#8212; the reveal directs the eye to the object, then hands it to the copy.</p>
  </figure>
</section>
```
## CSS
```css
.rv-03 {
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

.rv-03 * {
  box-sizing: border-box;
}

.rv-03__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-03__item {
  margin: 0 auto;
  padding-top: 60%;
  width: 500px;
}

.rv-03__item:last-child {
  padding-bottom: 66%;
}

.rv-03__badge {
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
/* clip, not hidden — hidden would become the view() timeline source */

.rv-03__frame {
  position: relative;
  overflow: clip;
  border-radius: 18px;
  background: oklch(0.13 0.008 260);
}

.rv-03 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 4/3;
  object-fit: cover;
}

.rv-03__vignette {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(circle at 50% 50%,transparent 42%,oklch(0.13 0.008 260/.72) 100%);
}

.rv-03 figcaption {
  margin-top: 14px;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}
/* ── the reveal ──────────────────────────────────────────────── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-03 img {
      animation: rv03-spotlight linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }

    .rv-03__item--soft img {
      animation-name: rv03-spotlight-soft;
      animation-range: entry 30% contain 40%;
      -webkit-mask-image: radial-gradient(circle,#000 40%,transparent 100%);
      mask-image: radial-gradient(circle,#000 40%,transparent 100%);
      -webkit-mask-repeat: no-repeat;
      mask-repeat: no-repeat;
      -webkit-mask-position: center;
      mask-position: center;
    }
  }
}
/* radius is a % of the element DIAGONAL — 80% is what covers a 4:3 box */

@keyframes rv03-spotlight {
  from {
    clip-path: circle(0% at 50% 50%);
  }

  to {
    clip-path: circle(80% at 50% 50%);
  }
}

@keyframes rv03-spotlight-soft {
  from {
    -webkit-mask-size: 8% 8%;
    mask-size: 8% 8%;
  }

  to {
    -webkit-mask-size: 220% 220%;
    mask-size: 220% 220%;
  }
}

@supports not (animation-timeline: view()) {
  .rv-03 img {
    clip-path: circle(0% at 50% 50%);
    transition: clip-path .9s cubic-bezier(.22,1,.36,1);
  }

  .rv-03__item.is-in img {
    clip-path: circle(80% at 50% 50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-03 img {
    clip-path: circle(80% at 50% 50%);
    mask-image: none;
    transition: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-03__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-03__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-03__uc {
  --pad: clamp(18px,4vw,42px);
}

.rv-03__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.6vw,32px)/1.12 system-ui,sans-serif;
  letter-spacing: -.028em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-03__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-03__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-03__uc p.body {
  margin: 0;
  font: 400 13.5px/1.65 system-ui,sans-serif;
  color: oklch(1 0 0/.6);
}

.rv-03__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-03__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-03__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-03__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-03__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-03__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-03__uc .over {
  position: relative;
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.13 0.008 260);
}

.rv-03__uc .scrim {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.rv-03__uc .copy {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 14px;
  padding: var(--pad);
}

.rv-03__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-03__uc .split {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: 20px;
  align-items: center;
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  padding: 20px;
  background: oklch(0.18 0.01 260);
}

.rv-03__uc .split img {
  aspect-ratio: 1/1;
}

.rv-03__uc .col {
  display: grid;
  gap: 13px;
}

.rv-03__uc .chips {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.rv-03__uc .chips span {
  font: 500 11px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.7);
  background: oklch(1 0 0/.06);
  border: 1px solid oklch(1 0 0/.1);
  padding: 7px 9px;
  border-radius: 999px;
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. Firefox/pre-115 Chrome get a one-shot transition. */
if (!CSS.supports('animation-timeline: view()')) {
  const io = new IntersectionObserver((entries, obs) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      obs.unobserve(entry.target);
    }
  }, { threshold: 0.3 });

  document.querySelectorAll('.rv-03__item').forEach((el) => io.observe(el));
}
```
