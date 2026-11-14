---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-glow-paint-cost-and-what-to-animate/"
title: "Neon Glow Paint Cost and What to Animate"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Large blur radii are among the most expensive things a browser repaints, and neon uses several per element by construction."
has_js: "true"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Paint Cost and What to Animate
Source: https://codefronts.com/design-styles/css-neon/neon-glow-paint-cost-and-what-to-animate/

Large blur radii are among the most expensive things a browser repaints, and neon uses several per element by construction. Animating the shadow repaints the full blurred area every frame; animating opacity on a pre-built glow layer composites instead. Both run side by side under a deliberate main-thread load, with a live frame counter, so the difference is measured rather than asserted.
## HTML
```html
<section class="nn-07" aria-labelledby="nn-07-heading">
  <div class="nn-07__stage">
    <div class="nn-07__theme">
      <input class="nn-07__tin" type="checkbox" id="nn-07-theme">
      <label class="nn-07__tlab" for="nn-07-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-07__head">
      <p class="nn-07__kicker">paint vs composite</p>
      <h2 class="nn-07__heading" id="nn-07-heading">Build the glow once. Animate opacity.</h2>
      <p class="nn-07__sub">Two identical-looking pulses. One repaints a large blurred area every frame; the other fades a layer that was rasterised once.</p>
      <div class="nn-07__controls">
        <button class="nn-07__btn" type="button" id="nn-07-load" aria-pressed="false">Add main-thread load</button>
        <p class="nn-07__fps" id="nn-07-fps" role="status" aria-live="polite">measuring</p>
      </div>
    </header>

    <div class="nn-07__compare">
      <figure class="nn-07__cell">
        <figcaption class="nn-07__caption">
          <span class="nn-07__tag nn-07__tag--bad">Animates box-shadow</span>
          repaints the full blur area, every frame
        </figcaption>
        <div class="nn-07__well">
          <div class="nn-07__lamp nn-07__lamp--paint">
            <span class="nn-07__label">deploy &middot; main</span>
          </div>
        </div>
        <p class="nn-07__mono">@keyframes &#123; box-shadow: 0 0 6px, 0 0 52px &#8594; dim &#125;</p>
      </figure>

      <figure class="nn-07__cell">
        <figcaption class="nn-07__caption">
          <span class="nn-07__tag nn-07__tag--good">Animates opacity</span>
          one rasterised glow layer, composited
        </figcaption>
        <div class="nn-07__well">
          <div class="nn-07__lamp nn-07__lamp--comp">
            <span class="nn-07__label">deploy &middot; main</span>
          </div>
        </div>
        <p class="nn-07__mono">::after &#123; box-shadow: built once &#125; @keyframes &#123; opacity &#125;</p>
      </figure>
    </div>

    <dl class="nn-07__facts">
      <div class="nn-07__fact"><dt>Blurred region</dt><dd>~380 &times; 140px for a 40px blur on a 300 &times; 60 element</dd></div>
      <div class="nn-07__fact"><dt>Per-frame budget</dt><dd>16.7ms at 60Hz, shared with script, layout and paint</dd></div>
      <div class="nn-07__fact"><dt>Synthetic load</dt><dd>~9ms of main-thread work per frame while enabled</dd></div>
      <div class="nn-07__fact"><dt>Cheap properties</dt><dd>opacity, transform &mdash; compositor, no repaint</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
.nn-07 {
  --nn-07-bad: #f4a4a4;
  --nn-07-warn: #f0c88a;
  --nn-07-spec-neon: #eaf4ff;
}

@media (prefers-color-scheme: light) {
  .nn-07 {
    --nn-07-bad: #a12a20;
    --nn-07-warn: #78490a;
  }

  .nn-07:has(#nn-07-theme:checked) {
    --nn-07-bad: #f4a4a4;
    --nn-07-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-07:has(#nn-07-theme:checked) {
    --nn-07-bad: #a12a20;
    --nn-07-warn: #78490a;
  }
}

.nn-07[data-theme="light"] {
  --nn-07-bad: #a12a20;
  --nn-07-warn: #78490a;
}

.nn-07 {
  --nn-07-spec-ink: #f2f4f7;
  --nn-07-spec-dim: #949aa4;
}

.nn-07__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-07__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-07__tlab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 44px;
  padding: 0 .8rem;
  border: 1px solid currentColor;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: .7;
}

.nn-07__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-07__tlab:hover {
  opacity: 1;
}

.nn-07__tin:focus-visible + .nn-07__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-07:has(#nn-07-theme:checked) {
    --nn-07-bg: #070708;
    --nn-07-well: #0d0e10;
    --nn-07-line: #22242a;
    --nn-07-ink: #f2f4f7;
    --nn-07-muted: #949aa4;
    --nn-07-neon: #eaf4ff;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-07:has(#nn-07-theme:checked) {
    --nn-07-bg: #eceef1;
    --nn-07-well: #1b1d21;
    --nn-07-line: #c6c9cf;
    --nn-07-ink: #14161a;
    --nn-07-muted: #4d525a;
    --nn-07-neon: #2c3138;
  }
}

.nn-07 {
  --nn-07-hue: 210;
  --nn-07-bg: #070708;
  --nn-07-well: #0d0e10;
  --nn-07-line: #22242a;
  --nn-07-ink: #f2f4f7;
  --nn-07-muted: #949aa4;
  --nn-07-neon: #eaf4ff;
  --nn-07-core: rgba(234, 244, 255, .95);
  --nn-07-halo: rgba(214, 232, 255, .42);
  --nn-07-bloom: rgba(200, 224, 255, .22);
  --nn-07-font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-07-bg);
  background-image: linear-gradient(to right, rgba(255, 255, 255, .028) 1px, transparent 1px), linear-gradient(to bottom, rgba(255, 255, 255, .028) 1px, transparent 1px);
  background-size: 3rem 3rem;
  color: var(--nn-07-ink);
  font-family: var(--nn-07-font-display);
}

.nn-07 *,
.nn-07 *::before,
.nn-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-07 {
    --nn-07-bg: oklch(13% 0.004 260);
    --nn-07-well: oklch(17% 0.006 260);
    --nn-07-line: oklch(27% 0.008 260);
    --nn-07-ink: oklch(97% 0.006 260);
    --nn-07-muted: oklch(71% 0.01 260);
    --nn-07-neon: oklch(98% 0.02 var(--nn-07-hue));
    --nn-07-core: oklch(98% 0.02 var(--nn-07-hue) / .95);
    --nn-07-halo: oklch(94% 0.035 var(--nn-07-hue) / .42);
    --nn-07-bloom: oklch(90% 0.045 var(--nn-07-hue) / .22);
  }
}

@media (prefers-color-scheme: light) {
  .nn-07 {
    --nn-07-bg: #eceef1;
    --nn-07-well: #1b1d21;
    --nn-07-line: #c6c9cf;
    --nn-07-ink: #14161a;
    --nn-07-muted: #4d525a;
    --nn-07-neon: #2c3138;
  }
}

.nn-07[data-theme="light"] {
  --nn-07-bg: #eceef1;
  --nn-07-well: #1b1d21;
  --nn-07-line: #c6c9cf;
  --nn-07-ink: #14161a;
  --nn-07-muted: #4d525a;
  --nn-07-neon: #2c3138;
}

.nn-07[data-theme="dark"] {
  --nn-07-bad: #f4a4a4;
  --nn-07-warn: #f0c88a;
  --nn-07-bg: #070708;
  --nn-07-well: #0d0e10;
  --nn-07-line: #22242a;
  --nn-07-ink: #f2f4f7;
  --nn-07-muted: #949aa4;
  --nn-07-neon: #eaf4ff;
}

.nn-07__stage {
  max-width: 64rem;
  margin: 0 auto;
  padding: clamp(1rem, 3vw, 1.35rem) clamp(.75rem, 3vw, 1.35rem) clamp(1.5rem, 4vw, 1.85rem);
  display: grid;
  gap: clamp(.9rem, 2.5vw, 1.2rem);
}

.nn-07__kicker {
  margin: 0 0 .3rem;
  font-size: .68rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--nn-07-muted);
}

.nn-07__heading {
  margin: 0;
  font-size: clamp(1.25rem, 4.4vw, 1.8rem);
  font-weight: 500;
  letter-spacing: -.01em;
  text-wrap: balance;
}

.nn-07__sub {
  margin: .4rem 0 0;
  max-width: 40rem;
  font-family: system-ui, sans-serif;
  font-size: .86rem;
  line-height: 1.55;
  color: var(--nn-07-muted);
  text-wrap: pretty;
}

.nn-07__controls {
  margin-top: .8rem;
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
}

.nn-07__btn {
  min-height: 44px;
  padding: 0 .9rem;
  border: 1px solid var(--nn-07-line);
  border-radius: 2px;
  background: transparent;
  color: var(--nn-07-ink);
  font-family: inherit;
  font-size: .74rem;
  letter-spacing: .04em;
  cursor: pointer;
}

.nn-07__btn:hover {
  border-color: var(--nn-07-neon);
}

.nn-07__btn[aria-pressed="true"] {
  border-color: var(--nn-07-neon);
  box-shadow: inset 0 0 0 1px var(--nn-07-neon);
}

.nn-07__btn:focus-visible {
  outline: 2px solid var(--nn-07-neon);
  outline-offset: 2px;
}

.nn-07__fps {
  margin: 0;
  min-width: 6rem;
  padding: .35rem .6rem;
  border: 1px solid var(--nn-07-line);
  border-radius: 2px;
  font-size: .74rem;
  color: var(--nn-07-neon);
}

.nn-07__compare {
  display: grid;
  gap: .8rem;
  grid-template-columns: 1fr;
}

@media (min-width: 50rem) {
  .nn-07__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-07__cell {
  margin: 0;
  display: grid;
  gap: .45rem;
  min-inline-size: 0;
}

.nn-07__caption {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex-wrap: wrap;
  font-family: system-ui, sans-serif;
  font-size: .76rem;
  color: var(--nn-07-muted);
  min-inline-size: 0;
}

.nn-07__tag {
  padding: .18rem .4rem;
  border: 1px solid var(--nn-07-line);
  border-radius: 2px;
  font-size: .64rem;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.nn-07__tag--bad {
  color: var(--nn-07-bad);
  border-color: #44262c;
}

.nn-07__tag--good {
  color: var(--nn-07-neon);
  border-color: color-mix(in srgb, var(--nn-07-neon) 35%, transparent);
}

.nn-07__well {
  display: grid;
  place-items: center;
  min-height: clamp(8rem, 22vw, 10rem);
  padding: clamp(1rem, 4vw, 1.75rem);
  border: 1px solid var(--nn-07-line);
  background: var(--nn-07-well);
  overflow: hidden;
}

.nn-07__lamp {
  position: relative;
  padding: .7rem 1.1rem;
  border: 1px solid var(--nn-07-spec-neon);
  background: #0f1114;
  isolation: isolate;
}

.nn-07__lamp--paint {
  animation: nn-07-paint 2.4s ease-in-out infinite;
}

.nn-07__lamp--comp::after {
  content: "";
  position: absolute;
  inset: -1px;
  box-shadow: 0 0 .38rem var(--nn-07-core), 0 0 clamp(.9rem, 4vw, 1.4rem) var(--nn-07-halo), 0 0 clamp(2rem, 9vw, 3.25rem) .25rem var(--nn-07-bloom);
  animation: nn-07-comp 2.4s ease-in-out infinite;
  z-index: -1;
}

@keyframes nn-07-paint {
  0%,
    100% {
    box-shadow: 0 0 .2rem var(--nn-07-halo), 0 0 1rem var(--nn-07-bloom);
  }

  50% {
    box-shadow: 0 0 .38rem var(--nn-07-core), 0 0 1.4rem var(--nn-07-halo), 0 0 3.25rem .25rem var(--nn-07-bloom);
  }
}

@keyframes nn-07-comp {
  0%,
    100% {
    opacity: .35;
  }

  50% {
    opacity: 1;
  }
}

.nn-07[data-load="on"] .nn-07__well {
  border-color: color-mix(in srgb, var(--nn-07-neon) 30%, var(--nn-07-line));
}

.nn-07__label {
  font-size: clamp(.76rem, 2.4vw, .86rem);
  letter-spacing: .06em;
  color: var(--nn-07-spec-ink);
}

.nn-07__mono {
  margin: 0;
  font-size: .66rem;
  line-height: 1.5;
  color: var(--nn-07-muted);
  overflow-wrap: anywhere;
}

.nn-07__facts {
  margin: 0;
  display: grid;
  gap: 0;
  border-top: 1px solid var(--nn-07-line);
}

.nn-07__fact {
  display: grid;
  gap: .15rem .75rem;
  padding: .6rem 0;
  border-bottom: 1px solid var(--nn-07-line);
}

@media (min-width: 38rem) {
  .nn-07__fact {
    grid-template-columns: 12rem minmax(0, 1fr);
    align-items: baseline;
  }
}

.nn-07__fact dt {
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--nn-07-muted);
}

.nn-07__fact dd {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: .82rem;
  line-height: 1.5;
  color: var(--nn-07-ink);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .nn-07__lamp--paint {
    animation: none;
    box-shadow: 0 0 .38rem var(--nn-07-core), 0 0 1.4rem var(--nn-07-halo), 0 0 3.25rem .25rem var(--nn-07-bloom);
  }

  .nn-07__lamp--comp::after {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.nn-07');
  if (!root || root.dataset.nn07) return;
  root.dataset.nn07 = 'on';
  const out = root.querySelector('#nn-07-fps');
  const btn = root.querySelector('#nn-07-load');
  let load = false, frames = 0, t0 = performance.now();
  btn.addEventListener('click', () => {
    load = !load;
    btn.setAttribute('aria-pressed', String(load));
    btn.textContent = load ? 'Stop main-thread load' : 'Add main-thread load';
    root.dataset.load = load ? 'on' : 'off';
  });
  const tick = (now) => {
    frames += 1;
    if (now - t0 >= 500) {
      out.textContent = Math.round((frames * 1000) / (now - t0)) + ' fps' + (load ? ' under load' : '');
      frames = 0; t0 = now;
    }
    if (load) { const end = performance.now() + 9; while (performance.now() < end) { /* occupy */ } }
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
})();
```
