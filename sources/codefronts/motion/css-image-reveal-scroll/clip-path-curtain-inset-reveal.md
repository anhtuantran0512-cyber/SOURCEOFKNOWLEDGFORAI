---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/clip-path-curtain-inset-reveal/"
title: "Clip-Path Curtain Inset Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "The signature agency-hero reveal: the image is painted at full size the whole time and only its clip window animates, opening from a slim letterbox to full…"
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clip-Path Curtain Inset Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/clip-path-curtain-inset-reveal/

The signature agency-hero reveal: the image is painted at full size the whole time and only its clip window animates, opening from a slim letterbox to full bleed like a stage curtain. One @keyframes, two clip-path values, no JavaScript — and because clip-path is composited it never reflows the text around it. Ships with a bottom-up curtain variant on the same wiring.
## HTML
```html
<section class="rv-01" tabindex="0" role="region" aria-label="Clip-path curtain reveal demo">
  <p class="rv-01__hint">scroll inside to reveal <span aria-hidden="true">&#8595;</span></p>

  <figure class="rv-01__item">
    <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1200&q=72"
         alt="Mist drifting through a pine forest at dawn" width="1200" height="750"
         loading="lazy" decoding="async">
    <figcaption>clip-path: inset(46% 22%) &#8594; inset(0%)</figcaption>
  </figure>

  <figure class="rv-01__item rv-01__item--up">
    <p class="rv-01__badge">variant b &#183; bottom-up curtain</p>
    <img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?auto=format&fit=crop&w=1200&q=72"
         alt="Calm mountain lake at first light" width="1200" height="750"
         loading="lazy" decoding="async">
    <figcaption>clip-path: inset(0 0 100% 0) &#8594; inset(0)</figcaption>
  </figure>

  <figure class="rv-01__item rv-01__uc">
    <p class="rv-01__uclabel"><b>real-world use case</b> agency landing page &#183; hero section</p>
    <div class="over">
      <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1400&q=70" alt="Snowy mountain ridge under a night sky" width="1400" height="788" loading="lazy" decoding="async">
      <span class="scrim"></span>
      <div class="copy">
        <p class="eyebrow">Studio Northline &#8212; est. 2014</p>
        <h4>We build brands that survive contact with the market.</h4>
        <div class="cta"><span class="btn">Start a project</span><span class="btn ghost">See our work</span></div>
      </div>
    </div>
    <p class="why">The curtain opens on the image, then the eyebrow, headline and buttons land on progressively later ranges &#8212; one scroll, four beats, zero JavaScript.</p>
  </figure>
</section>
```
## CSS
```css
.rv-01 {
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

.rv-01 * {
  box-sizing: border-box;
}

.rv-01__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,'JetBrains Mono',monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-01__item {
  margin: 0 auto;
  padding-top: 60%;
  width: 500px;
}

.rv-01__item:last-child {
  padding-bottom: 66%;
}

.rv-01__badge {
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

.rv-01 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16/10;
  object-fit: cover;
  border-radius: 18px;
}

.rv-01 figcaption {
  margin-top: 14px;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}
/* ── the reveal ──────────────────────────────────────────────── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-01 img {
      animation: rv01-curtain linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }

    .rv-01__item--up img {
      animation-name: rv01-curtain-up;
    }

    .rv-01 figcaption {
      animation: rv01-cap linear both;
      animation-timeline: view();
      animation-range: entry 75% contain 40%;
    }
  }
}

@keyframes rv01-curtain {
  from {
    clip-path: inset(46% 22% 46% 22% round 18px);
  }

  to {
    clip-path: inset(0% 0% 0% 0% round 18px);
  }
}

@keyframes rv01-curtain-up {
  from {
    clip-path: inset(0 0 100% 0 round 18px);
  }

  to {
    clip-path: inset(0 0 0 0 round 18px);
  }
}

@keyframes rv01-cap {
  from {
    opacity: 0;
    transform: translateY(14px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}
/* ── fallback styling for engines without scroll timelines ───── */

@supports not (animation-timeline: view()) {
  .rv-01 img {
    clip-path: inset(46% 22% round 18px);
    transition: clip-path 1s cubic-bezier(.22,1,.36,1);
  }

  .rv-01__item--up img {
    clip-path: inset(0 0 100% 0 round 18px);
  }

  .rv-01__item.is-in img {
    clip-path: inset(0 round 18px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-01 img {
    clip-path: inset(0 round 18px);
    transition: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-01__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-01__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-01__uc {
  --pad: clamp(18px,4vw,42px);
}

.rv-01__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.6vw,32px)/1.12 system-ui,sans-serif;
  letter-spacing: -.028em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-01__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-01__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-01__uc p.body {
  margin: 0;
  font: 400 13.5px/1.65 system-ui,sans-serif;
  color: oklch(1 0 0/.6);
}

.rv-01__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-01__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-01__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-01__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-01__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-01__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-01__uc .over {
  position: relative;
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.13 0.008 260);
}

.rv-01__uc .scrim {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.rv-01__uc .copy {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 14px;
  padding: var(--pad);
}

.rv-01__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-01__uc .over img {
  aspect-ratio: 16/9;
  border-radius: 0;
}

.rv-01__uc .scrim {
  background: linear-gradient(90deg,oklch(0.13 0.008 260/.88) 0%,oklch(0.13 0.008 260/.5) 52%,transparent 100%);
}

.rv-01__uc .copy {
  align-content: center;
  max-width: 62%;
}

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-01__uc .eyebrow {
      animation: rv01-cap linear both;
      animation-timeline: view();
      animation-range: entry 70% contain 30%;
    }

    .rv-01__uc h4 {
      animation: rv01-cap linear both;
      animation-timeline: view();
      animation-range: entry 75% contain 40%;
    }

    .rv-01__uc .cta {
      animation: rv01-cap linear both;
      animation-timeline: view();
      animation-range: entry 85% contain 60%;
    }
  }
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. Modern browsers run demo 01 with zero JS;
   this block exists so Firefox (and pre-115 Chrome) still get a reveal instead of a static image.
   It pairs with the @supports not (animation-timeline: view()) rules in the CSS above. */
if (!CSS.supports('animation-timeline: view()')) {
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      io.unobserve(entry.target);          // reveal once, then stop observing
    }
  }, { threshold: 0.25 });

  document.querySelectorAll('.rv-01__item').forEach((el) => io.observe(el));
}
```
