---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/fade-slide-and-zoom-reveal/"
title: "Fade, Slide and Zoom Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "The everyday reveal that most sites install a 14 KB library for: opacity, a small translate and a small scale, on one timeline."
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fade, Slide and Zoom Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/fade-slide-and-zoom-reveal/

The everyday reveal that most sites install a 14 KB library for: opacity, a small translate and a small scale, on one timeline. Nine lines of CSS with no data attributes, no fire-once state machine, and — unlike a class-toggle implementation — it scrubs backwards when the user scrolls up.
## HTML
```html
<section class="rv-12" tabindex="0" role="region" aria-label="Fade slide and zoom reveal demo">
  <p class="rv-12__hint">scroll inside &#183; fade + slide + zoom <span aria-hidden="true">&#8595;</span></p>

  <ul class="rv-12__list">
    <li style="--i:0">
      <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=600&q=68"
           alt="Sunlight through green forest leaves" width="600" height="450" loading="lazy" decoding="async">
      <div><span>Performance</span><h5>We deleted 14 KB of scroll library and shipped it anyway</h5><time>8 min &#183; 21 Jul 2026</time></div>
    </li>
    <li style="--i:1">
      <img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?auto=format&fit=crop&w=600&q=68"
           alt="Calm lake between mountains" width="600" height="450" loading="lazy" decoding="async">
      <div><span>CSS</span><h5>animation-range is the only timing API you need</h5><time>6 min &#183; 14 Jul 2026</time></div>
    </li>
    <li style="--i:2">
      <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=600&q=68"
           alt="Snowy mountain ridge under a night sky" width="600" height="450" loading="lazy" decoding="async">
      <div><span>Accessibility</span><h5>Reduced motion is a feature, not a fallback</h5><time>5 min &#183; 02 Jul 2026</time></div>
    </li>
  </ul>

  <div class="rv-12__uc">
    <p class="rv-12__uclabel"><b>real-world use case</b> content site &#183; related posts rail</p>
    <div class="shell pad">
      <div class="col head"><p class="eyebrow">Keep reading</p><h4>More on scroll-driven CSS</h4></div>
      <ul class="rv-12__list rail">
        <li style="--i:0">
          <img src="https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?auto=format&fit=crop&w=600&q=68" alt="Pink flowers in soft focus" width="600" height="450" loading="lazy" decoding="async">
          <div><span>Tutorial</span><h5>Six ways to stagger without a delay ladder</h5><time>7 min &#183; 28 Jun 2026</time></div>
        </li>
        <li style="--i:1">
          <img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=600&q=68" alt="City street grid photographed from above" width="600" height="450" loading="lazy" decoding="async">
          <div><span>Deep dive</span><h5>entry, exit and cover: picking the right range</h5><time>9 min &#183; 19 Jun 2026</time></div>
        </li>
      </ul>
      <p class="body">Every example on this page ships a pure-CSS version and an IntersectionObserver fallback.</p>
    </div>
    <p class="why">This is what most sites reach for AOS to do. Nine lines of CSS, offset ranges instead of data attributes, scrubs in both directions, and nothing is hidden if the JavaScript never arrives.</p>
  </div>
</section>
```
## CSS
```css
.rv-12 {
  --accent: oklch(0.88 0.19 118);
  --stage: 100vh;
  --step: 7%;
  font-family: system-ui,'Segoe UI',sans-serif;
  height: var(--stage);
  overflow-y: auto;
  overflow-x: hidden;
  padding: 0 22px;
  border-radius: 16px;
  border: 1px solid oklch(1 0 0/.1);
  background: linear-gradient(oklch(0.16 0.01 260),oklch(0.19 0.012 260));
}

.rv-12 * {
  box-sizing: border-box;
}

.rv-12__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-12__list {
  display: grid;
  gap: 12px;
  list-style: none;
  margin: 60% auto 50%;
  padding: 0;
  width: 500px;
}

.rv-12__list li {
  display: grid;
  grid-template-columns: minmax(90px,132px) 1fr;
  gap: 16px;
  align-items: center;
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 16px;
  padding: 14px;
  background: oklch(0.18 0.01 260);
}

.rv-12 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 4/3;
  object-fit: cover;
  border-radius: 11px;
}

.rv-12__list div {
  display: grid;
  gap: 5px;
}

.rv-12__list span {
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-12__list h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-12__list time {
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}
/* ── the reveal — stagger is a SHIFTED RANGE, never a delay ──── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-12__list li {
      animation: rv12-fsz linear both;
      animation-timeline: view();
      animation-range: entry calc(60% + var(--i) * var(--step)) contain calc(20% + var(--i) * var(--step));
    }
  }
}

@keyframes rv12-fsz {
  from {
    opacity: 0;
    transform: translateY(46px) scale(.92);
  }

  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
/* variant — slide in from the side */

@keyframes rv12-fsz-x {
  from {
    opacity: 0;
    transform: translateX(-56px) scale(.94);
  }

  to {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
}
/* ── fallback: here a time-based delay ladder IS correct ─────── */

@supports not (animation-timeline: view()) {
  .rv-12__list li {
    opacity: 0;
    transform: translateY(46px) scale(.92);
    transition: opacity .7s ease,transform .7s cubic-bezier(.22,1,.36,1);
    transition-delay: calc(var(--i) * 70ms);
  }

  .rv-12__list li.is-in {
    opacity: 1;
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-12__list li {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-12__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-12__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-12__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.8vw,34px)/1.1 system-ui,sans-serif;
  letter-spacing: -.028em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-12__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-12__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-12__uc p.body {
  margin: 0;
  font: 400 13px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.58);
}

.rv-12__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-12__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-12__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-12__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-12__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-12__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-12__uc .over {
  position: relative;
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.13 0.008 260);
}

.rv-12__uc .col {
  display: grid;
  gap: 6px;
}

.rv-12__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-12__uc {
  margin: 0 auto 110%;
  width: 500px;
}

.rv-12__uc .shell.pad {
  padding: 22px;
}

.rv-12__uc .col.head {
  gap: 8px;
  margin-bottom: 18px;
}

.rv-12__uc .rv-12__list.rail {
  margin: 0 0 16px;
}
/* the rail uses the sideways variant, staggered by shifted range */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-12__uc .rail li {
      animation-name: rv12-fsz-x;
    }
  }
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. This is the classic AOS pattern in twelve lines;
   modern browsers never run it because the CSS above already scrubs with scroll position. */
if (!CSS.supports('animation-timeline: view()')) {
  const io = new IntersectionObserver((entries, obs) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      obs.unobserve(entry.target);
    }
  }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });

  document.querySelectorAll('.rv-12__list li').forEach((el) => io.observe(el));
}
```
