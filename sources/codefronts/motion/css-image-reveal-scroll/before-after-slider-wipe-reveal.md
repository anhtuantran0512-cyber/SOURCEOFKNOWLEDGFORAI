---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/before-after-slider-wipe-reveal/"
title: "Before After Slider Wipe Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "A before/after comparison that plays itself: the 'before' layer slides out of frame with translateX(101%) as you scroll, uncovering the 'after' image beneath."
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Before After Slider Wipe Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/before-after-slider-wipe-reveal/

A before/after comparison that plays itself: the 'before' layer slides out of frame with translateX(101%) as you scroll, uncovering the 'after' image beneath. All the visual language of a drag-handle comparison slider — including the accent bar on the wipe edge — with none of the pointer-event logic. Vertical curtain variant included.
## HTML
```html
<section class="rv-04" tabindex="0" role="region" aria-label="Before and after wipe reveal demo">
  <p class="rv-04__hint">scroll inside to wipe the overlay away <span aria-hidden="true">&#8595;</span></p>

  <figure class="rv-04__item">
    <div class="rv-04__frame">
      <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=1200&q=72"
           alt="Living room after renovation, bright and furnished" width="1200" height="750"
           loading="lazy" decoding="async">
      <div class="rv-04__cover">
        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=72"
             alt="The same living room before renovation" width="1200" height="750"
             loading="lazy" decoding="async">
        <span class="rv-04__chip">before</span>
      </div>
      <span class="rv-04__chip rv-04__chip--after">after</span>
    </div>
    <figcaption>overlay: translateX(0) &#8594; translateX(101%)</figcaption>
  </figure>

  <figure class="rv-04__item rv-04__item--vertical">
    <p class="rv-04__badge">variant b &#183; vertical curtain</p>
    <div class="rv-04__frame">
      <img src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1200&q=72"
           alt="Finished office interior, after state" width="1200" height="750"
           loading="lazy" decoding="async">
      <div class="rv-04__cover">
        <img src="https://images.unsplash.com/photo-1487958449943-2429e8be8625?auto=format&fit=crop&w=1200&q=72"
             alt="Bare concrete shell of the same space, before state" width="1200" height="750"
             loading="lazy" decoding="async">
      </div>
    </div>
    <figcaption>overlay: translateY(0) &#8594; translateY(-101%)</figcaption>
  </figure>

  <figure class="rv-04__item rv-04__uc">
    <p class="rv-04__uclabel"><b>real-world use case</b> case study &#183; before &amp; after proof</p>
    <div class="shell">
      <div class="head">
        <div class="col"><p class="eyebrow">Client &#183; Harbour &amp; Co</p><h5>Retail refit, Bristol</h5></div>
        <span class="when">14 weeks &#183; 2026</span>
      </div>
      <div class="rv-04__frame">
        <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=1400&q=70" alt="Renovated retail interior, after state" width="1400" height="788" loading="lazy" decoding="async">
        <div class="rv-04__cover">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1400&q=70" alt="The same interior before renovation" width="1400" height="788" loading="lazy" decoding="async">
          <span class="rv-04__chip">before</span>
        </div>
        <span class="rv-04__chip rv-04__chip--after">after</span>
      </div>
      <div class="stats">
        <div><b>+38%</b><span>footfall, first quarter</span></div>
        <div><b>2.4&#215;</b><span>dwell time</span></div>
        <div><b>&#163;0</b><span>over budget</span></div>
      </div>
    </div>
    <p class="why">The wipe does the arguing: the reader scrolls, the old space slides away, and the results row is already on screen to catch the reaction.</p>
  </figure>
</section>
```
## CSS
```css
.rv-04 {
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

.rv-04 * {
  box-sizing: border-box;
}

.rv-04__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-04__item {
  margin: 0 auto;
  padding-top: 60%;
  width: 500px;
}

.rv-04__item:last-child {
  padding-bottom: 66%;
}

.rv-04__badge {
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

.rv-04__frame {
  position: relative;
  overflow: clip;
  border-radius: 18px;
}

.rv-04 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16/10;
  object-fit: cover;
}

.rv-04__cover {
  position: absolute;
  inset: 0;
}

.rv-04__cover img {
  height: 100%;
  filter: saturate(.68);
}
/* the wipe edge — travels with the layer, reads as a slider handle */

.rv-04__cover::after {
  content: "";
  position: absolute;
  inset-block: 0;
  right: 0;
  width: 3px;
  background: var(--accent);
}

.rv-04__item--vertical .rv-04__cover::after {
  inset: auto 0 0 0;
  width: auto;
  height: 3px;
}

.rv-04__chip {
  position: absolute;
  top: 12px;
  left: 12px;
  font: 600 11px/1 ui-monospace,monospace;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-04__chip--after {
  top: auto;
  left: auto;
  right: 12px;
  bottom: 12px;
  color: oklch(0.96 0 0);
  background: oklch(0.16 0.01 260/.72);
  border: 1px solid oklch(1 0 0/.16);
}

.rv-04 figcaption {
  margin-top: 14px;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}
/* ── the wipe ────────────────────────────────────────────────── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-04__cover {
      animation: rv04-wipe linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }

    .rv-04__item--vertical .rv-04__cover {
      animation-name: rv04-wipe-up;
    }
  }
}
/* 101%, not 100% — fractional DPRs leave a 1px seam at exactly 100% */

@keyframes rv04-wipe {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(101%);
  }
}

@keyframes rv04-wipe-up {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-101%);
  }
}

@supports not (animation-timeline: view()) {
  .rv-04__cover {
    transition: transform 1s cubic-bezier(.76,0,.24,1);
  }

  .rv-04__item.is-in .rv-04__cover {
    transform: translateX(101%);
  }

  .rv-04__item--vertical.is-in .rv-04__cover {
    transform: translateY(-101%);
  }
}
/* motion-sensitive users get the AFTER image — that's the content */

@media (prefers-reduced-motion: reduce) {
  .rv-04__cover {
    transform: translateX(101%);
    transition: none;
  }

  .rv-04__item--vertical .rv-04__cover {
    transform: translateY(-101%);
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-04__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-04__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-04__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.6vw,30px)/1.14 system-ui,sans-serif;
  letter-spacing: -.026em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-04__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-04__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-04__uc p.body {
  margin: 0;
  font: 400 13.5px/1.65 system-ui,sans-serif;
  color: oklch(1 0 0/.6);
}

.rv-04__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-04__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-04__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-04__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-04__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-04__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-04__uc .col {
  display: grid;
  gap: 6px;
}

.rv-04__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-04__uc .head {
  display: flex;
  gap: 12px;
  align-items: baseline;
  justify-content: space-between;
  flex-wrap: wrap;
  padding: 18px 20px 14px;
}

.rv-04__uc .when {
  font: 400 12px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-04__uc .rv-04__frame {
  border-radius: 0;
}

.rv-04__uc .shell img {
  aspect-ratio: 16/9;
}

.rv-04__uc .stats {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(120px,1fr));
  gap: 1px;
  background: oklch(1 0 0/.09);
  margin-top: 1px;
}

.rv-04__uc .stats div {
  background: oklch(0.18 0.01 260);
  padding: 16px 18px;
  display: grid;
  gap: 5px;
}

.rv-04__uc .stats b {
  font: 600 clamp(19px,2.4vw,26px)/1 system-ui,sans-serif;
  color: var(--accent);
}

.rv-04__uc .stats span {
  font: 400 11.5px/1.4 system-ui,sans-serif;
  color: oklch(1 0 0/.55);
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. Toggles (not one-shots) so the comparison can
   replay as the section re-enters the viewport, which suits before/after content. */
if (!CSS.supports('animation-timeline: view()')) {
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      entry.target.classList.toggle('is-in', entry.isIntersecting);
    }
  }, { threshold: 0.35 });

  document.querySelectorAll('.rv-04__item').forEach((el) => io.observe(el));
}
```
