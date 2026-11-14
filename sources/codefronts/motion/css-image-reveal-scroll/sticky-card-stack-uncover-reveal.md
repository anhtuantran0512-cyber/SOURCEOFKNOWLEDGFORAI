---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/sticky-card-stack-uncover-reveal/"
title: "Sticky Card Stack & Uncover Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "The case-study walkthrough pattern: each image pins with position: sticky while the next scrolls up over it, and the pinned card scales down and dims as it…"
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Card Stack & Uncover Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/sticky-card-stack-uncover-reveal/

The case-study walkthrough pattern: each image pins with position: sticky while the next scrolls up over it, and the pinned card scales down and dims as it leaves so the stack reads as depth instead of a flat overlap. This is the demo that teaches the exit range — the one thing entry cannot do.
## HTML
```html
<section class="rv-07" tabindex="0" role="region" aria-label="Sticky card stack reveal demo">
  <p class="rv-07__hint">scroll inside &#8212; cards pin, then peel <span aria-hidden="true">&#8595;</span></p>

  <div class="rv-07__stack">
    <figure>
      <img src="https://images.unsplash.com/photo-1487958449943-2429e8be8625?auto=format&fit=crop&w=1000&q=70"
           alt="Case study one: white concrete building facade" width="1000" height="625"
           loading="lazy" decoding="async">
      <figcaption>01 &#183; discovery</figcaption>
    </figure>
    <figure>
      <img src="https://images.unsplash.com/photo-1560472354-b33ff0c44a43?auto=format&fit=crop&w=1000&q=70"
           alt="Case study two: bright collaborative workspace" width="1000" height="625"
           loading="lazy" decoding="async">
      <figcaption>02 &#183; build</figcaption>
    </figure>
    <figure>
      <img src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1000&q=70"
           alt="Case study three: finished office interior" width="1000" height="625"
           loading="lazy" decoding="async">
      <figcaption>03 &#183; launch</figcaption>
    </figure>
  </div>

  <div class="rv-07__uc">
    <div class="rv-07__stack">
      <p class="rv-07__uclabel"><b>real-world use case</b> agency site &#183; how-we-work walkthrough</p>
      <figure class="card">
        <img src="https://images.unsplash.com/photo-1487958449943-2429e8be8625?auto=format&fit=crop&w=1000&q=70" alt="Architectural survey of a white concrete facade" width="1000" height="562" loading="lazy" decoding="async">
        <figcaption class="bar"><span class="step">01</span><span class="col"><h5>Survey &amp; strategy</h5><p class="body">Two weeks on site and in the data. We leave with a scope you can hold someone to &#8212; not a mood board.</p></span></figcaption>
      </figure>
      <figure class="card">
        <img src="https://images.unsplash.com/photo-1560472354-b33ff0c44a43?auto=format&fit=crop&w=1000&q=70" alt="Bright collaborative workspace mid-project" width="1000" height="562" loading="lazy" decoding="async">
        <figcaption class="bar"><span class="step">02</span><span class="col"><h5>Build in the open</h5><p class="body">Weekly staging links, one shared backlog. You see the work the same day we do.</p></span></figcaption>
      </figure>
      <figure class="card">
        <img src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1000&q=70" alt="Finished office interior at handover" width="1000" height="562" loading="lazy" decoding="async">
        <figcaption class="bar"><span class="step">03</span><span class="col"><h5>Handover that sticks</h5><p class="body">Documented components, a recorded walkthrough, and a team that can ship without us.</p></span></figcaption>
      </figure>
    </div>
    <p class="why">Each stage pins long enough to be read, then recedes as the next arrives &#8212; a three-step process explained by scroll position rather than by a numbered list.</p>
  </div>
</section>
```
## CSS
```css
.rv-07 {
  --accent: oklch(0.88 0.19 118);
  --stage: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  height: var(--stage);
  overflow-y: auto;
  overflow-x: hidden;
  padding: 0 20px;
  border-radius: 16px;
  border: 1px solid oklch(1 0 0/.1);
  background: linear-gradient(oklch(0.16 0.01 260),oklch(0.19 0.012 260));
}

.rv-07 * {
  box-sizing: border-box;
}

.rv-07__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}
/* NB: no overflow:hidden anywhere up this tree — it kills sticky AND hijacks view() */

.rv-07__stack {
  display: grid;
  gap: 26px;
  margin: 60% auto 70%;
  width: 600px;
}

.rv-07__stack figure {
  position: sticky;
  top: 18px;
  margin: 0;
  border-radius: 16px;
  overflow: clip;
  box-shadow: 0 24px 50px oklch(0 0 0/.5);
}

.rv-07 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16/10;
  object-fit: cover;
}

.rv-07 figcaption {
  position: absolute;
  left: 14px;
  bottom: 12px;
  font: 600 12px/1 ui-monospace,monospace;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 7px 9px;
  border-radius: 7px;
}
/* ── the peel: EXIT range, because a pinned card is already 'in' ── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-07__stack figure:not(:last-child) {
      animation: rv07-peel linear both;
      animation-timeline: view();
      animation-range: exit 0% exit 100%;
    }
  }
}

@keyframes rv07-peel {
  from {
    transform: scale(1) translateY(0);
    opacity: 1;
  }

  to {
    transform: scale(.9) translateY(-7%);
    opacity: .28;
  }
}
/* ── fallback: sticky already works; only the peel needs --out ── */

@supports not (animation-timeline: view()) {
  .rv-07__stack figure {
    transform: scale(calc(1 - .1 * var(--out,0)));
    opacity: calc(1 - .72 * var(--out,0));
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-07__stack figure {
    transform: none;
    opacity: 1;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-07__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-07__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-07__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.6vw,30px)/1.14 system-ui,sans-serif;
  letter-spacing: -.026em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-07__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-07__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-07__uc p.body {
  margin: 0;
  font: 400 13px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.58);
}

.rv-07__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-07__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-07__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-07__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-07__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-07__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-07__uc .col {
  display: grid;
  gap: 6px;
}

.rv-07__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-07__uc {
  margin: 0 0 110%;
}

.rv-07__uc .card {
  border: 1px solid oklch(1 0 0/.1);
  background: oklch(0.18 0.01 260);
}

.rv-07__uc .bar {
  position: static;
  display: flex;
  gap: 16px;
  align-items: flex-start;
  flex-wrap: wrap;
  padding: 18px 20px;
  background: none;
  color: inherit;
  border-radius: 0;
}

.rv-07__uc .step {
  font: 600 11px/1 ui-monospace,monospace;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 7px 9px;
  border-radius: 7px;
  white-space: nowrap;
}

.rv-07__uc .col {
  flex: 1 1 200px;
  gap: 5px;
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. position: sticky needs no JS at all; this only
   reproduces the scale/dim peel for engines without scroll timelines. */
if (!CSS.supports('animation-timeline: view()')) {
  const cards = [...document.querySelectorAll('.rv-07__stack figure')].slice(0, -1); // last card never peels
  const scroller = document.querySelector('.rv-07');
  let queued = false;

  const update = () => {
    queued = false;
    const stickyTop = scroller.getBoundingClientRect().top + 18;
    for (const card of cards) {
      const r = card.getBoundingClientRect();
      const out = Math.min(1, Math.max(0, (stickyTop - r.top) / r.height));
      card.style.setProperty('--out', out.toFixed(3));
    }
  };

  const onScroll = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };
  scroller.addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  update();
}
```
