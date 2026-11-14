---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-with-parallax-background/"
title: "CSS Diagonal Section with Parallax Background"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "An angled photo band whose background moves at a different rate as you scroll."
has_js: "true"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Section with Parallax Background
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-with-parallax-background/

An angled photo band whose background moves at a different rate as you scroll. The shipped technique is a transform-driven layer inside an overflow: clip band — background-attachment: fixed is demonstrated too, with an honest note about its iOS Safari failure and its scroll cost. Under prefers-reduced-motion the layer is pinned and the band is a plain photograph.
## HTML
```html
<div class="dgs-19" data-dgs-19>
  <input class="dgs-19__sronly" type="checkbox" id="dgs-19-dark">
  <label class="dgs-19__theme" for="dgs-19-dark">
    <svg class="dgs-19__i dgs-19__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-19__i dgs-19__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-19__srtext">Toggle dark theme</span>
  </label>
  <div class="dgs-19__stage">
    <section class="dgs-19__above" aria-labelledby="dgs-19-a">
      <div class="dgs-19__wrap">
        <p class="dgs-19__eyebrow">Valsette &mdash; 2,340 m</p>
        <h2 class="dgs-19__display" id="dgs-19-a">Forty-one pistes, one funicular, no queue after ten</h2>
        <p class="dgs-19__lede">Scroll on. The photograph inside the angled band moves slower than the page, so the diagonal edge slides across the image instead of travelling with it.</p>
      </div>
    </section>

    <section class="dgs-19__band" aria-labelledby="dgs-19-b">
      <img class="dgs-19__img" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&amp;fit=crop&amp;w=2000&amp;q=70" alt="A snow-covered mountain range under a clear night sky" width="2000" height="1300" loading="lazy" decoding="async">
      <div class="dgs-19__veil" aria-hidden="true"></div>
      <div class="dgs-19__wrap dgs-19__over">
        <h2 class="dgs-19__h2" id="dgs-19-b">Parallax inside a clipped band</h2>
        <p class="dgs-19__body">The image is taller than the section and translated on the Y axis at a fraction of scroll. Because the movement is a <code class="dgs-19__code">translate</code> on a layer behind the content, it stays on the compositor — and the clip stays exactly where the section put it.</p>
        <dl class="dgs-19__facts">
          <div><dt>Top station</dt><dd>2,340 m</dd></div>
          <div><dt>Longest run</dt><dd>11.4 km</dd></div>
          <div><dt>Snow depth</dt><dd>168 cm</dd></div>
        </dl>
      </div>
    </section>

    <section class="dgs-19__below" aria-labelledby="dgs-19-c">
      <div class="dgs-19__wrap">
        <h2 class="dgs-19__h3" id="dgs-19-c">Conditions this week</h2>
        <ul class="dgs-19__cond">
          <li><strong>Mon</strong><span>Bluebird</span><em>&minus;7&deg;</em></li>
          <li><strong>Tue</strong><span>Light snow</span><em>&minus;9&deg;</em></li>
          <li><strong>Wed</strong><span>30 cm overnight</span><em>&minus;11&deg;</em></li>
          <li><strong>Thu</strong><span>Wind hold, upper</span><em>&minus;6&deg;</em></li>
        </ul>
        <p class="dgs-19__note">A parallax layer must never be the only way content is reachable: the copy above sits in normal flow, and with reduced motion the image simply holds still.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Karla:wght@400;500;600&display=swap');

.dgs-19 {
  --cut: clamp(2rem, 6.5vw, 8.5rem);
  --shift: 0px;
  --page: #f7f9fb;
  --page2: #e9eef3;
  --ink: #101822;
  --muted: #55636f;
  --line: #d5dee6;
  --deep: #0c1622;
  --on-deep: #f4f8fb;
  --ice: #7fb6d9;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'Karla', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.62;
  -webkit-font-smoothing: antialiased;
}

.dgs-19 *,
.dgs-19 *::before,
.dgs-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.08 235)) {
  .dgs-19 {
    --page: oklch(0.982 0.004 235);
    --page2: oklch(0.938 0.008 235);
    --ink: oklch(0.2 0.02 240);
    --muted: oklch(0.49 0.02 240);
    --line: oklch(0.885 0.012 235);
    --deep: oklch(0.18 0.025 245);
    --on-deep: oklch(0.972 0.006 235);
    --ice: oklch(0.755 0.075 235);
  }
}

.dgs-19__stage {
  display: flow-root;
}

.dgs-19__wrap {
  inline-size: min(72rem, 100%);
  margin-inline: auto;
}

.dgs-19__above {
  padding: clamp(3.5rem, 9vw, 6.5rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(3rem, 7vw, 5rem));
}

.dgs-19__eyebrow {
  margin: 0 0 1rem;
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
}

.dgs-19__display {
  margin: 0 0 1.1rem;
  max-inline-size: 24ch;
  font-family: 'Cormorant Garamond', ui-serif, Georgia, serif;
  font-weight: 300;
  font-size: clamp(2.4rem, 8vw, 5rem);
  line-height: 1.0;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.dgs-19__lede {
  margin: 0;
  max-inline-size: 52ch;
  font-size: clamp(1.02rem, 2vw, 1.18rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-19__band {
  position: relative;
  z-index: 1;
  isolation: isolate;
  overflow: clip;
  background: var(--deep);
  color: var(--on-deep);
  clip-path: polygon(0 var(--cut), 100% 0, 100% calc(100% - var(--cut)), 0 100%);
  margin-block: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3rem, 8vw, 5.5rem)) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(3rem, 8vw, 5.5rem));
}

.dgs-19__img {
  position: absolute;
  inset-block-start: -12%;
  inset-inline: 0;
  inline-size: 100%;
  block-size: 124%;
  object-fit: cover;
  object-position: 50% 40%;
  z-index: -2;
  translate: 0 var(--shift);
  will-change: translate;
}

.dgs-19__veil {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(100deg, rgba(8,14,22,.9) 0%, rgba(8,14,22,.6) 52%, rgba(8,14,22,.25) 100%);
}

.dgs-19__over {
  position: relative;
}

.dgs-19__h2 {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-family: 'Cormorant Garamond', ui-serif, Georgia, serif;
  font-weight: 400;
  font-size: clamp(1.9rem, 5.2vw, 3.2rem);
  line-height: 1.05;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.dgs-19__body {
  margin: 0 0 1.75rem;
  max-inline-size: 56ch;
  color: rgba(244,248,251,.85);
  text-wrap: pretty;
}

.dgs-19__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .86em;
  padding: .1em .35em;
  border-radius: 4px;
  background: rgba(255,255,255,.14);
}

.dgs-19__facts {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem clamp(1.5rem, 5vw, 3.5rem);
}

.dgs-19__facts > div {
  min-inline-size: 8rem;
  padding-block-start: .7rem;
  border-block-start: 1px solid rgba(244,248,251,.35);
}

.dgs-19__facts dt {
  font-size: .7rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(244,248,251,.7);
}

.dgs-19__facts dd {
  margin: .3rem 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(1.5rem, 4vw, 2rem);
  font-variant-numeric: tabular-nums;
}

.dgs-19__below {
  background: var(--page2);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 10vw, 7rem);
}

.dgs-19__h3 {
  margin: 0 0 1.25rem;
  font-family: 'Cormorant Garamond', ui-serif, Georgia, serif;
  font-weight: 400;
  font-size: clamp(1.5rem, 4vw, 2.2rem);
}

.dgs-19__cond {
  list-style: none;
  margin: 0 0 1.75rem;
  padding: 0;
  display: grid;
  gap: 1px;
  background: var(--line);
  border: 1px solid var(--line);
  border-radius: 10px;
  overflow: clip;
}

.dgs-19__cond li {
  display: grid;
  gap: .2rem 1.5rem;
  grid-template-columns: 4rem minmax(0, 1fr) auto;
  align-items: baseline;
  padding: .8rem 1rem;
  background: var(--page);
}

.dgs-19__cond strong {
  font-weight: 600;
  letter-spacing: .04em;
}

.dgs-19__cond span {
  color: var(--muted);
  font-size: .94rem;
}

.dgs-19__cond em {
  font-style: normal;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
}

.dgs-19__note {
  margin: 0;
  max-inline-size: 60ch;
  font-size: .95rem;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-19 {
    --shift: 0px !important;
  }

  .dgs-19 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-19__veil {
    display: none;
  }

  .dgs-19__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
  }

  .dgs-19__img {
    opacity: .2;
  }

  .dgs-19__cond,
    .dgs-19__cond li {
    border-color: CanvasText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-19__sronly,
.dgs-19__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-19__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-19__theme:hover {
  translate: 0 -1px;
}

.dgs-19__sronly:focus-visible + .dgs-19__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-19__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-19__i--sun {
  display: none;
}

.dgs-19:has(#dgs-19-dark:checked) .dgs-19__i--moon {
  display: none;
}

.dgs-19:has(#dgs-19-dark:checked) .dgs-19__i--sun {
  display: block;
}

.dgs-19:has(#dgs-19-dark:checked) {
  --page: #0b0e14;
  --page2: #131822;
  --ink: #eef1f7;
  --muted: #97a0ad;
  --line: #222934;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-19__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-19__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-dgs-19]');
  if (!root) return;
  const band = root.querySelector('.dgs-19__band');
  if (!band) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const depth = 0.16;
  let queued = false;
  const write = () => {
    queued = false;
    const r = band.getBoundingClientRect();
    const vh = window.innerHeight || 1;
    if (r.bottom < -200 || r.top > vh + 200) return;
    const centre = r.top + r.height / 2 - vh / 2;
    root.style.setProperty('--shift', (-centre * depth).toFixed(1) + 'px');
  };
  const onScroll = () => { if (!queued) { queued = true; requestAnimationFrame(write); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  write();
})();
```
