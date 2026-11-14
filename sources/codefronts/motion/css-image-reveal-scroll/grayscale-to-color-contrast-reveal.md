---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-reveal-scroll/grayscale-to-color-contrast-reveal/"
title: "Grayscale-to-Color Contrast Reveal"
section: "motion"
category: "css-image-reveal-scroll"
category_name: "CSS Image Reveal on Scroll"
description: "Team bios and client logo walls that bloom into colour as they reach the middle of the viewport."
has_js: "true"
---

Here's a working CSS Image Reveal on Scroll from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Grayscale-to-Color Contrast Reveal
Source: https://codefronts.com/motion/css-image-reveal-scroll/grayscale-to-color-contrast-reveal/

Team bios and client logo walls that bloom into colour as they reach the middle of the viewport. The demo that teaches the cover range — colour peaks mid-screen rather than on arrival — plus the filter-list interpolation rule that breaks most hand-written filter animations, and hover parity so pointer users get the same payoff.
## HTML
```html
<section class="rv-08" tabindex="0" role="region" aria-label="Grayscale to colour reveal demo">
  <p class="rv-08__hint">scroll inside &#8212; colour peaks mid-viewport <span aria-hidden="true">&#8595;</span></p>

  <ul class="rv-08__team">
    <li style="--i:0">
      <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=560&q=70"
           alt="Portrait of Maya, design lead" width="560" height="700" loading="lazy" decoding="async">
      <span>Maya &#183; design</span>
    </li>
    <li style="--i:1">
      <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=560&q=70"
           alt="Portrait of Tom, engineering lead" width="560" height="700" loading="lazy" decoding="async">
      <span>Tom &#183; engineering</span>
    </li>
    <li style="--i:2">
      <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=560&q=70"
           alt="Portrait of Ada, research lead" width="560" height="700" loading="lazy" decoding="async">
      <span>Ada &#183; research</span>
    </li>
  </ul>
  <p class="rv-08__note">range: cover 30% &#8594; 55% &#183; not entry</p>

  <div class="rv-08__uc">
    <p class="rv-08__uclabel"><b>real-world use case</b> about page &#183; team &amp; leadership</p>
    <div class="shell pad">
      <div class="head">
        <div class="col"><p class="eyebrow">The team</p><h4>Fourteen people. No account managers.</h4></div>
        <span class="where">Bristol &#183; remote-first</span>
      </div>
      <ul class="rv-08__team roster">
        <li style="--i:0"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=440&q=68" alt="Portrait of Maya Okonjo, design lead" width="440" height="550" loading="lazy" decoding="async"><b>Maya Okonjo</b><span>Design lead &#183; 9 yrs</span></li>
        <li style="--i:1"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=440&q=68" alt="Portrait of Tom Reyes, engineering lead" width="440" height="550" loading="lazy" decoding="async"><b>Tom Reyes</b><span>Engineering &#183; 12 yrs</span></li>
        <li style="--i:2"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=440&q=68" alt="Portrait of Ada Lindqvist, research lead" width="440" height="550" loading="lazy" decoding="async"><b>Ada Lindqvist</b><span>Research &#183; 7 yrs</span></li>
        <li style="--i:3"><img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=440&q=68" alt="Portrait of Sam Herrera, delivery lead" width="440" height="550" loading="lazy" decoding="async"><b>Sam Herrera</b><span>Delivery &#183; 6 yrs</span></li>
      </ul>
    </div>
    <p class="why">Colour peaks as each face reaches the middle of the screen, so attention and saturation move together &#8212; and the names carry the information, never the colour.</p>
  </div>
</section>
```
## CSS
```css
.rv-08 {
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

.rv-08 * {
  box-sizing: border-box;
}

.rv-08__hint {
  position: sticky;
  top: 150px;
  margin: 0;
  height: 0;
  text-align: center;
  font: 400 11.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0/.45);
}

.rv-08__team {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(120px,1fr));
  gap: 12px;
  list-style: none;
  margin: 60% 0 0;
  padding: 0;
}

.rv-08__team li {
  display: grid;
  gap: 8px;
}

.rv-08 img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 4/5;
  object-fit: cover;
  border-radius: 12px;
}

.rv-08__team span {
  font: 500 11px/1.3 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}

.rv-08__note {
  margin: 14px 0 30%;
  font: 500 13px/1.5 ui-monospace,monospace;
  color: oklch(1 0 0/.5);
}
/* ── the bloom: COVER range, so colour peaks mid-viewport ────── */

@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .rv-08 img {
      animation: rv08-colour linear both;
      animation-timeline: view();
      animation-range: cover calc(30% + var(--i) * 2%) cover calc(55% + var(--i) * 2%);
    }
  }
}
/* filter lists interpolate POSITIONALLY — same functions, same order, both keyframes */

@keyframes rv08-colour {
  from {
    filter: grayscale(1) brightness(.72) contrast(1.08);
  }

  to {
    filter: grayscale(0) brightness(1) contrast(1);
  }
}
/* pointer users get the same payoff; hover query keeps touch clean */

@media (hover: hover) {
  .rv-08 img:hover {
    filter: grayscale(0) brightness(1.03) contrast(1);
  }
}
/* ── fallback: --c is distance from viewport centre, written below ── */

@supports not (animation-timeline: view()) {
  .rv-08 img {
    filter: grayscale(calc(1 - var(--c,0))) brightness(calc(.72 + .28 * var(--c,0))) contrast(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .rv-08 img {
    filter: none;
  }
}
/* ── real-world use case block ────────────────────────────────── */

.rv-08__uclabel {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font: 400 11.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-08__uclabel b {
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 6px 8px;
  border-radius: 6px;
}

.rv-08__uc h4 {
  margin: 0;
  font: 600 clamp(19px,2.6vw,30px)/1.14 system-ui,sans-serif;
  letter-spacing: -.026em;
  color: oklch(0.97 0 0);
  text-wrap: balance;
}

.rv-08__uc h5 {
  margin: 0;
  font: 600 15.5px/1.28 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-08__uc p.eyebrow {
  margin: 0;
  font: 500 10.5px/1 ui-monospace,monospace;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--accent);
}

.rv-08__uc p.body {
  margin: 0;
  font: 400 13px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.58);
}

.rv-08__uc .cta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.rv-08__uc .btn {
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.16 0.01 260);
  background: var(--accent);
  padding: 12px 16px;
  border-radius: 9px;
}

.rv-08__uc .btn.ghost {
  color: oklch(0.94 0 0);
  background: none;
  border: 1px solid oklch(1 0 0/.2);
}

.rv-08__uc .price {
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-08__uc .why {
  margin: 12px 0 0;
  font: 400 12.5px/1.6 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}

.rv-08__uc .shell {
  border: 1px solid oklch(1 0 0/.1);
  border-radius: 20px;
  overflow: clip;
  background: oklch(0.18 0.01 260);
}

.rv-08__uc .col {
  display: grid;
  gap: 6px;
}

.rv-08__uc .meta {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font: 400 12.5px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.55);
}

.rv-08__uc {
  margin: 0 0 110%;
}

.rv-08__uc .shell.pad {
  padding: 22px;
}

.rv-08__uc .head {
  display: flex;
  gap: 16px;
  align-items: baseline;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.rv-08__uc .where {
  font: 400 12px/1 ui-monospace,monospace;
  color: oklch(1 0 0/.45);
}

.rv-08__uc .roster {
  grid-template-columns: repeat(auto-fit,minmax(125px,1fr));
  gap: 14px;
  margin: 0;
}

.rv-08__uc .roster li {
  gap: 10px;
}

.rv-08__uc .roster b {
  font: 600 13.5px/1.3 system-ui,sans-serif;
  color: oklch(0.97 0 0);
}

.rv-08__uc .roster span {
  font: 400 11.5px/1.3 system-ui,sans-serif;
  color: oklch(1 0 0/.5);
}
```

## JavaScript
```js
/* OPTIONAL — progressive enhancement only. Reproduces the cover-range behaviour by writing a
   0-1 value based on distance from the scroller's vertical centre. */
if (!CSS.supports('animation-timeline: view()')) {
  const scroller = document.querySelector('.rv-08');
  const imgs = [...scroller.querySelectorAll('img')];
  let queued = false;

  const update = () => {
    queued = false;
    const box = scroller.getBoundingClientRect();
    const mid = box.top + box.height / 2;
    for (const img of imgs) {
      const r = img.getBoundingClientRect();
      const dist = Math.abs((r.top + r.height / 2) - mid) / (box.height / 2);
      img.style.setProperty('--c', (1 - Math.min(1, dist)).toFixed(3));
    }
  };

  const onScroll = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };
  scroller.addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  update();
}
```
