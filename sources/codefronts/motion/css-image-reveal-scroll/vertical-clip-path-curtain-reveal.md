---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/vertical-clip-path-curtain-reveal/"
title: "Vertical Clip-Path Curtain Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "Two barn doors parting from the centre line: clip-path: inset(0 50% 0 50%) relaxes to inset(0) as the image scrolls into view."
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Clip-Path Curtain Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/vertical-clip-path-curtain-reveal/

Two barn doors parting from the centre line: clip-path: inset(0 50% 0 50%) relaxes to inset(0) as the image scrolls into view. The same one-property discipline as demo 01 rotated 90 degrees, and the better choice on wide heroes because parting doors expose full-height content immediately. Single-door left-to-right variant included.
## HTML
```html
<section class="rv-09" tabindex="0" role="region" aria-label="Vertical curtain reveal demo">
  <p class="rv-09__hint">scroll inside to part the curtain <span aria-hidden="true">&#8595;</span></p>

  <figure class="rv-09__item">
    <img src="https://images.unsplash.com/photo-1514306191717-452ec28c7814?auto=format&fit=crop&w=1200&q=72"
         alt="Empty theatre auditorium lit from the stage" width="1200" height="750"
         loading="lazy" decoding="async">
    <figcaption>clip-path: inset(0 50% 0 50%) &#8594; inset(0)</figcaption>
  </figure>

  <figure class="rv-09__item rv-09__item--door">
    <p class="rv-09__badge">variant b &#183; single door, left to right</p>
    <img src="https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?auto=format&fit=crop&w=1200&q=72"
         alt="Crowd silhouetted against stage lights at a festival" width="1200" height="750"
         loading="lazy" decoding="async">
    <figcaption>clip-path: inset(0 100% 0 0) &#8594; inset(0)</figcaption>
  </figure>

  <figure class="rv-09__item rv-09__uc">
    <p class="rv-09__uclabel"><b>real-world use case</b> event site &#183; festival announcement hero</p>
    <div class="over">
      <img src="https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?auto=format&fit=crop&w=1400&q=70" alt="Festival stage at dusk with the crowd in silhouette" width="1400" height="788" loading="lazy" decoding="async">
      <span class="scrim" aria-hidden="true"></span>
      <div class="copy">
        <p class="eyebrow">Northline Live &#183; 4&#8211;6 September 2026</p>
        <h4>Three nights. One field. Bring a coat.</h4>
        <div class="cta"><span class="btn">Tickets from &#163;68</span><span class="btn ghost">Full line-up</span></div>
      </div>
    </div>
    <p class="why">The barn-door parting is a literal curtain-up, which is why it reads so strongly for live events &#8212; and the headline lands on a later range, exactly as a spotlight would follow the reveal.</p>
  </figure>
</section>
```
## CSS
```css
.rv-09 {
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

.rv-09 * {
  box-sizing: border-box;
}

.rv-09__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-09__item {
  margin: 0 auto;
  padding-top: 60%;
  width: 500px;
}

.rv-09__item:last-child {
  padding-bottom: 66%;
}

.rv-09__badge {
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

.rv-09 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16/10;
  object-fit: cover;
  border-radius: 18px;
}

.rv-09 figcaption {
  margin-top: 14px;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-09 img {
      animation: rv09-barn linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }

    .rv-09__item--door img {
      animation-name: rv09-door;
    }
  }
}
/* inset() takes margin order: top right bottom left */

@keyframes rv09-barn {
  from {
    clip-path: inset(0 50% 0 50% round 18px);
  }

  to {
    clip-path: inset(0 0 0 0 round 18px);
  }
}

@keyframes rv09-door {
  from {
    clip-path: inset(0 100% 0 0 round 18px);
  }

  to {
    clip-path: inset(0 0 0 0 round 18px);
  }
}

@supports not (animation-timeline: view()) {
  .rv-09 img {
    clip-path: inset(0 50% 0 50% round 18px);
    transition: clip-path 1s cubic-bezier(.22,1,.36,1);
  }

  .rv-09__item--door img {
    clip-path: inset(0 100% 0 0 round 18px);
  }

  .rv-09__item.is-in img {
    clip-path: inset(0 round 18px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-09 img {
    clip-path: inset(0 round 18px);
    transition: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-09__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-09__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-09__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.8vw,34px)/1.1 system-ui,sans-serif;
  letter-spacing: -.028em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-09__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-09__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-09__uc p.body {
  margin: 0;
  font: 400 13px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.58);
}

.rv-09__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-09__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-09__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-09__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-09__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-09__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-09__uc .over {
  position: relative;
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.13 0.008 260);
}

.rv-09__uc .col {
  display: grid;
  gap: 6px;
}

.rv-09__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-09__uc .over img {
  aspect-ratio: 16/9;
  border-radius: 0;
}

.rv-09__uc .scrim {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(0deg,oklch(0.13 0.008 260/.9) 0%,oklch(0.13 0.008 260/.36) 55%,transparent 100%);
}

.rv-09__uc .copy {
  position: absolute;
  inset: 0;
  display: grid;
  align-content: end;
  gap: 14px;
  padding: clamp(18px,4vw,42px);
}

@keyframes rv09-cap {
  from {
    opacity: 0;
    transform: translateY(14px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-09__uc .eyebrow {
      animation: rv09-cap linear both;
      animation-timeline: view();
      animation-range: entry 26% entry 74%;
    }

    .rv-09__uc h4 {
      animation: rv09-cap linear both;
      animation-timeline: view();
      animation-range: entry 32% entry 84%;
    }

    .rv-09__uc .cta {
      animation: rv09-cap linear both;
      animation-timeline: view();
      animation-range: entry 44% entry 96%;
    }
  }
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. Modern browsers run demo 09 with zero JS. */
if (!CSS.supports('animation-timeline: view()')) {
  const io = new IntersectionObserver((entries, obs) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      obs.unobserve(entry.target);
    }
  }, { threshold: 0.25 });

  document.querySelectorAll('.rv-09__item').forEach((el) => io.observe(el));
}
```
