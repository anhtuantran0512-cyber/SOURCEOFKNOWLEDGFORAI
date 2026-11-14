---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/horizontal-carousel-scroll-progress-bar/"
title: "Horizontal Carousel Scroll Progress Bar"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "Native scroll-snap carousels are the right way to build a slider in 2026 — no library, no transform maths, real momentum on touch."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Carousel Scroll Progress Bar
Source: https://codefronts.com/motion/css-scroll-progress-bar/horizontal-carousel-scroll-progress-bar/

Native scroll-snap carousels are the right way to build a slider in 2026 — no library, no transform maths, real momentum on touch. The one thing they lack is a sense of position, and that is exactly what an inline-axis scroll timeline restores: a progress bar underneath the track that is impossible to desynchronise, because it is the scroll position.
## HTML
```html
<section class="sp-11" aria-label="Horizontal carousel scroll progress bar demo">
  <header class="sp-11__bar">
    <a class="sp-11__brand" href="#sp-11-track"><span class="sp-11__logo" aria-hidden="true"></span>Atelier</a>
    <p class="sp-11__meta">scroll-timeline-axis: inline</p>
  </header>
  <div class="sp-11__intro">
    <p class="sp-11__intro-eyebrow">snap · inline axis · no library</p>
    <h2 class="sp-11__intro-title">A carousel that knows where it is</h2>
    <p class="sp-11__intro-sub">Drag, flick or use the arrows. The bar under the track is bound to the track's own inline-axis timeline — it cannot drift out of sync.</p>
  </div>
  <section class="sp-11__carousel" aria-labelledby="sp-11-ctitle">
    <div class="sp-11__chead">
      <h3 class="sp-11__ctitle" id="sp-11-ctitle">New this season</h3>
      <div class="sp-11__btns">
        <button class="sp-11__nav" type="button" id="sp-11-prev" aria-label="Previous items" aria-controls="sp-11-track" disabled><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg></button>
        <button class="sp-11__nav" type="button" id="sp-11-next" aria-label="Next items" aria-controls="sp-11-track"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg></button>
      </div>
    </div>
    <ul class="sp-11__track" id="sp-11-track" tabindex="0" role="list" aria-label="Products, scrollable horizontally">
      <li class="sp-11__card"><img class="sp-11__img" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="A minimal analogue wristwatch on a pale background" loading="lazy" decoding="async"><div class="sp-11__cbody"><p class="sp-11__cname">Field Watch 38</p><p class="sp-11__cprice">£240</p></div></li>
      <li class="sp-11__card"><img class="sp-11__img" src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="Over-ear headphones resting on a plain surface" loading="lazy" decoding="async"><div class="sp-11__cbody"><p class="sp-11__cname">Studio Cans</p><p class="sp-11__cprice">£185</p></div></li>
      <li class="sp-11__card"><img class="sp-11__img" src="https://images.unsplash.com/photo-1560769629-975ec94e6a86?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="A pair of running shoes on a light backdrop" loading="lazy" decoding="async"><div class="sp-11__cbody"><p class="sp-11__cname">Trail Runner</p><p class="sp-11__cprice">£120</p></div></li>
      <li class="sp-11__card"><img class="sp-11__img" src="https://images.unsplash.com/photo-1572635196237-14b3f281503f?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="Sunglasses laid flat on a neutral surface" loading="lazy" decoding="async"><div class="sp-11__cbody"><p class="sp-11__cname">Reader Frames</p><p class="sp-11__cprice">£95</p></div></li>
      <li class="sp-11__card"><img class="sp-11__img" src="https://images.unsplash.com/photo-1560343090-f0409e92791a?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="A leather satchel photographed from above" loading="lazy" decoding="async"><div class="sp-11__cbody"><p class="sp-11__cname">Day Satchel</p><p class="sp-11__cprice">£310</p></div></li>
      <li class="sp-11__card"><img class="sp-11__img" src="https://images.unsplash.com/photo-1546868871-7041f2fbc7cd?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="A smartwatch with a fabric strap" loading="lazy" decoding="async"><div class="sp-11__cbody"><p class="sp-11__cname">Pulse Band</p><p class="sp-11__cprice">£150</p></div></li>
    </ul>
    <div class="sp-11__progwrap">
      <div class="sp-11__prog" role="progressbar" aria-label="Carousel position" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="sp-11-prog"><i class="sp-11__thumb"></i></div>
      <p class="sp-11__readout" id="sp-11-readout">Card 1 of 6 <span class="sp-11__hint">drag, flick or use the arrows</span></p>
    </div>
  </section>
  <section class="sp-11__notes">
    <p class="sp-11__kicker">Why it holds up</p>
    <h3 class="sp-11__h">The indicator is the scroll position</h3>
    <p class="sp-11__p">Transform-based sliders keep a separate index in JavaScript and reconcile it with the DOM. A snap carousel has no index to desynchronise: the browser owns the position, and the timeline reads it directly.</p>
    <p class="sp-11__p">The thumb is sized proportionally to the visible fraction of the track, so its width tells you how much content exists — the one piece of information a percentage readout throws away.</p>
    <p class="sp-11__chip">0 slider libraries · real momentum on touch</p>
  </section>
  <footer class="sp-11__pagefoot"><p class="sp-11__pagefootin">Scroll progress pattern 11 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-11-bg);
  --sp-11-bg: oklch(0.972 0.006 85);
  --sp-11-surface: oklch(1 0 0);
  --sp-11-ink: oklch(0.19 0.014 70);
  --sp-11-mut: oklch(0.52 0.012 70);
  --sp-11-acc: oklch(0.48 0.11 40);
  --sp-11-line: oklch(0.19 0.014 70/.12);
  --sp-11-p: 0;
  --sp-11-vis: .4;
  timeline-scope: --sp-11-tl;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-11-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-11 *,
.sp-11 *::before,
.sp-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-11__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  background: color-mix(in oklch,var(--sp-11-surface) 84%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-11-line);
}

.sp-11__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-11__brand:focus-visible,
.sp-11__nav:focus-visible,
.sp-11__track:focus-visible {
  outline: 2px solid var(--sp-11-acc);
  outline-offset: 3px;
}

.sp-11__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 5px;
  background: var(--sp-11-acc);
}

.sp-11__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--sp-11-mut);
}

.sp-11__intro {
  display: grid;
  gap: 14px;
  padding-block: clamp(44px,10vh,110px) clamp(24px,5vh,50px);
}

.sp-11__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-11-acc);
}

.sp-11__intro-title {
  font-size: clamp(32px,6vw,70px);
  line-height: .98;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 16ch;
  text-wrap: balance;
}

.sp-11__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-11-mut);
  max-inline-size: 54ch;
  text-wrap: pretty;
}

.sp-11__carousel {
  display: grid;
  gap: 14px;
  padding-block: clamp(10px,2vh,20px) clamp(30px,6vh,60px);
}

.sp-11__chead {
  display: flex;
  align-items: center;
  gap: 14px;
}

.sp-11__ctitle {
  font-size: clamp(17px,2.2vw,22px);
  font-weight: 700;
  letter-spacing: -.02em;
}

.sp-11__btns {
  display: flex;
  gap: 6px;
  margin-inline-start: auto;
}

.sp-11__nav {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--sp-11-line);
  border-radius: 12px;
  background: var(--sp-11-surface);
  color: var(--sp-11-ink);
  cursor: pointer;
  transition: background .2s ease,color .2s ease,scale .2s ease;
}

.sp-11__nav svg {
  inline-size: 18px;
  block-size: 18px;
}

.sp-11__nav:hover:not(:disabled) {
  background: var(--sp-11-ink);
  color: var(--sp-11-surface);
}

.sp-11__nav:active:not(:disabled) {
  scale: .93;
}

.sp-11__nav:disabled {
  opacity: .35;
  cursor: not-allowed;
}

.sp-11__track {
  list-style: none;
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: min(76%,300px);
  gap: clamp(12px,2vw,20px);
  overflow-x: auto;
  overscroll-behavior-inline: contain;
  scroll-snap-type: inline mandatory;
  scrollbar-width: none;
  padding-block-end: 4px;
}

.sp-11__track::-webkit-scrollbar {
  display: none;
}

@supports (animation-timeline: scroll()) {
  .sp-11__track {
    scroll-timeline-name: --sp-11-tl;
    scroll-timeline-axis: inline;
  }

  .sp-11__thumb {
    animation: sp-11-slide linear;
    animation-timeline: --sp-11-tl;
  }
}

@keyframes sp-11-slide {
  from {
    transform: translateX(0) scaleX(var(--sp-11-vis));
  }

  to {
    transform: translateX(calc(100% - var(--sp-11-vis) * 100%)) scaleX(var(--sp-11-vis));
  }
}

.sp-11__card {
  scroll-snap-align: start;
  display: grid;
  gap: 0;
  border: 1px solid var(--sp-11-line);
  border-radius: 16px;
  background: var(--sp-11-surface);
  overflow: hidden;
  transition: box-shadow .25s ease,translate .25s ease;
}

.sp-11__card:hover {
  box-shadow: 0 18px 40px -26px oklch(0.19 0.014 70/.7);
  translate: 0 -3px;
}

.sp-11__img {
  inline-size: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  display: block;
  background: linear-gradient(135deg,oklch(0.85 0.03 70),oklch(0.7 0.04 40));
}

.sp-11__cbody {
  display: flex;
  align-items: baseline;
  gap: 10px;
  padding: 13px 15px 15px;
}

.sp-11__cname {
  font-size: 14.4px;
  font-weight: 650;
  letter-spacing: -.01em;
}

.sp-11__cprice {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  color: var(--sp-11-acc);
  font-weight: 650;
}

.sp-11__progwrap {
  display: grid;
  gap: 9px;
  padding-block-start: 6px;
}

.sp-11__prog {
  position: relative;
  block-size: 8px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-11-ink) 12%,transparent);
  box-shadow: inset 0 0 0 1px var(--sp-11-line);
  overflow: hidden;
}

.sp-11__thumb {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: 100%;
  transform-origin: 0 50%;
  transform: translateX(calc(var(--sp-11-p) * (100% - var(--sp-11-vis) * 100%))) scaleX(var(--sp-11-vis));
  border-radius: 99px;
  background: linear-gradient(90deg,var(--sp-11-acc),oklch(0.62 0.13 55));
}

.sp-11__readout {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 10px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .06em;
  color: var(--sp-11-acc);
  font-variant-numeric: tabular-nums;
}

.sp-11__hint {
  color: var(--sp-11-mut);
  letter-spacing: .02em;
  text-transform: none;
}

.sp-11__notes {
  display: grid;
  gap: 12px;
  padding-block: clamp(30px,6vh,66px);
}

.sp-11__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-11-acc);
}

.sp-11__h {
  font-size: clamp(21px,3vw,31px);
  line-height: 1.12;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-11__p {
  max-inline-size: 62ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-11-mut);
  text-wrap: pretty;
}

.sp-11__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-11-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-11-acc) 10%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-11-acc) 24%,transparent);
}

.sp-11__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(40px,8vh,100px) 24px;
  border-block-start: 1px solid var(--sp-11-line);
}

.sp-11__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-11-mut);
  text-align: center;
}

.sp-11__bar,
.sp-11__intro,
.sp-11__carousel,
.sp-11__notes {
  padding-inline: max(clamp(18px,4vw,40px),calc((100% - 1120px)/2));
}

.sp-11__track {
  scroll-padding-inline-start: 0;
}

@media (max-width: 640px) {
  .sp-11__track {
    grid-auto-columns: min(82%,300px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-11 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-11');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const track = root.querySelector('#sp-11-track');
  const prog = root.querySelector('#sp-11-prog');
  const readout = root.querySelector('#sp-11-readout');
  const cards = [...root.querySelectorAll('.sp-11__card')];
  const prev = root.querySelector('#sp-11-prev');
  const next = root.querySelector('#sp-11-next');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const max = track.scrollWidth - track.clientWidth;
    const p = max > 0 ? Math.min(1, Math.max(0, track.scrollLeft / max)) : 0;
    const vis = track.scrollWidth > 0 ? Math.max(0.12, track.clientWidth / track.scrollWidth) : 1;
    root.style.setProperty('--sp-11-vis', vis.toFixed(4));
    // always written: harmless under the native path (the animation wins) and the safety net if the timeline name fails to resolve
    root.style.setProperty('--sp-11-p', p.toFixed(4));
    prog.setAttribute('aria-valuenow', String(Math.round(p * 100)));
    const card = cards[0];
    const gap = parseFloat(getComputedStyle(track).columnGap) || 16;
    const step = card ? card.getBoundingClientRect().width + gap : 1;
    const idx = Math.min(cards.length, Math.round(track.scrollLeft / step) + 1);
    readout.firstChild.nodeValue = 'Card ' + idx + ' of ' + cards.length + ' ';
    prev.disabled = track.scrollLeft <= 2;
    next.disabled = track.scrollLeft >= max - 2;
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  track.addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  const step = (dir) => {
    const card = track.querySelector('.sp-11__card');
    const gap = parseFloat(getComputedStyle(track).columnGap) || 16;
    const w = card ? card.getBoundingClientRect().width + gap : track.clientWidth * 0.8;
    const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
    track.scrollBy({ left: dir * w, behavior: calm ? 'auto' : 'smooth' });
  };
  prev.addEventListener('click', () => step(-1));
  next.addEventListener('click', () => step(1));
  paint();
})();
```
