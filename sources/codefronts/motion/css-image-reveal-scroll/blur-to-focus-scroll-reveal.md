---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/blur-to-focus-scroll-reveal/"
title: "Blur-to-Focus Scroll Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "The quiet, expensive-feeling entrance used by luxury SaaS and high-end hardware pages: the image resolves out of an 18px blur while fading up and settling…"
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blur-to-Focus Scroll Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/blur-to-focus-scroll-reveal/

The quiet, expensive-feeling entrance used by luxury SaaS and high-end hardware pages: the image resolves out of an 18px blur while fading up and settling from a 1.05 scale. Three properties on one timeline. Includes the LCP-safe variant that animates blur only, so your hero never pays a paint penalty.
## HTML
```html
<section class="rv-05" tabindex="0" role="region" aria-label="Blur to focus reveal demo">
  <p class="rv-05__hint">scroll inside to bring it into focus <span aria-hidden="true">&#8595;</span></p>

  <figure class="rv-05__item">
    <img src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=1200&q=72"
         alt="Laptop on a clean desk in soft daylight" width="1200" height="750"
         loading="lazy" decoding="async">
    <figcaption>filter: blur(18px) &#8594; blur(0) &#183; opacity 0 &#8594; 1</figcaption>
  </figure>

  <figure class="rv-05__item rv-05__item--lcp">
    <p class="rv-05__badge">variant b &#183; blur only, LCP-safe</p>
    <img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=1200&q=72"
         alt="City street grid photographed from above" width="1200" height="750"
         loading="lazy" decoding="async">
    <figcaption>filter: blur(22px) saturate(1.4) &#8594; blur(0) &#183; opacity untouched</figcaption>
  </figure>

  <figure class="rv-05__item rv-05__uc">
    <p class="rv-05__uclabel"><b>real-world use case</b> saas landing page &#183; feature section</p>
    <div class="split">
      <div class="col wide">
        <p class="eyebrow">Reporting</p>
        <h4>Every number, one source of truth.</h4>
        <p class="body">Pipeline, spend and margin reconciled nightly &#8212; so the Monday meeting starts with agreement instead of arithmetic.</p>
        <ul>
          <li>Nightly reconciliation across 40+ sources</li>
          <li>Audit trail on every restated figure</li>
          <li>SOC 2 Type II, EU data residency</li>
        </ul>
        <div class="cta"><span class="btn">Book a walkthrough</span><span class="btn ghost">Read the docs</span></div>
      </div>
      <img class="rv-05__item--lcp-img" src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=1000&q=70" alt="Laptop showing a reporting dashboard on a clean desk" width="1000" height="750" loading="lazy" decoding="async">
    </div>
    <p class="why">Blur-only (opacity untouched) is the LCP-safe choice for a feature screenshot: it paints instantly, so the effect costs nothing in field data.</p>
  </figure>
</section>
```
## CSS
```css
.rv-05 {
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

.rv-05 * {
  box-sizing: border-box;
}

.rv-05__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-05__item {
  margin: 0 auto;
  padding-top: 55%;
  width: 500px;
}

.rv-05__item:last-child {
  padding-bottom: 66%;
}

.rv-05__badge {
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

.rv-05 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16/10;
  object-fit: cover;
  border-radius: 18px;
}

.rv-05 figcaption {
  margin-top: 14px;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}
/* ── the reveal ──────────────────────────────────────────────── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-05 img {
      will-change: filter,opacity,transform;
      animation: rv05-focus linear both;
      animation-timeline: view();
      animation-range: entry 60% contain 20%;
    }

    .rv-05__item--lcp img {
      animation-name: rv05-focus-lcp;
      will-change: filter;
    }
  }
}
/* the 1.05 scale stops the blur sampling transparent pixels at the frame edge */

@keyframes rv05-focus {
  from {
    filter: blur(18px);
    opacity: 0;
    transform: scale(1.05);
  }

  to {
    filter: blur(0);
    opacity: 1;
    transform: scale(1);
  }
}
/* LCP-safe: opacity is never touched, so the image paints immediately */

@keyframes rv05-focus-lcp {
  from {
    filter: blur(22px) saturate(1.4);
  }

  to {
    filter: blur(0) saturate(1);
  }
}

@supports not (animation-timeline: view()) {
  .rv-05 img {
    filter: blur(18px);
    opacity: 0;
    transition: filter .9s ease,opacity .9s ease,transform .9s ease;
  }

  .rv-05__item--lcp img {
    opacity: 1;
    filter: blur(22px) saturate(1.4);
  }

  .rv-05__item.is-in img {
    filter: blur(0) saturate(1);
    opacity: 1;
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-05 img {
    filter: none;
    opacity: 1;
    transform: none;
    transition: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-05__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-05__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-05__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.6vw,30px)/1.14 system-ui,sans-serif;
  letter-spacing: -.026em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-05__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-05__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-05__uc p.body {
  margin: 0;
  font: 400 13.5px/1.65 system-ui,sans-serif;
  color: oklch(1 0 0/.6);
}

.rv-05__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-05__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-05__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-05__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-05__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-05__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-05__uc .col {
  display: grid;
  gap: 6px;
}

.rv-05__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-05__uc .split {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(240px,1fr));
  gap: 22px;
  align-items: center;
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  padding: 22px;
  background: oklch(0.18 0.01 260);
}

.rv-05__uc .col.wide {
  gap: 13px;
}

.rv-05__uc .split img {
  aspect-ratio: 4/3;
  border-radius: 16px;
}

.rv-05__uc ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 8px;
}

.rv-05__uc li {
  display: flex;
  gap: 9px;
  align-items: baseline;
  font: 400 13px/1.5 system-ui,sans-serif;
  color: oklch(1 0 0/.62);
}

.rv-05__uc li::before {
  content: "\2192";
  color: var(--accent);
}
/* the use-case screenshot uses the LCP-safe keyframes: blur only, no fade */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-05__uc .split img {
      will-change: filter;
      animation: rv05-focus-lcp linear both;
      animation-timeline: view();
      animation-range: entry 0% entry 100%;
    }
  }
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. Note the will-change cleanup: leaving the hint on
   keeps a promoted GPU layer alive for the life of the page, which wastes memory. */
if (!CSS.supports('animation-timeline: view()')) {
  const io = new IntersectionObserver((entries, obs) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      const item = entry.target;
      item.classList.add('is-in');

      const img = item.querySelector('img');
      img?.addEventListener('transitionend', () => { img.style.willChange = 'auto'; }, { once: true });

      obs.unobserve(item);
    }
  }, { rootMargin: '0px 0px -12% 0px' });

  document.querySelectorAll('.rv-05__item').forEach((el) => io.observe(el));
}
```
