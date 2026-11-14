---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-pricing-cards/"
title: "Neon Pricing Table with Glow Tiers"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Glow used as hierarchy rather than decoration: the recommended tier carries the full three-layer stack, the neighbours keep a single dim halo, and the…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Pricing Table with Glow Tiers
Source: https://codefronts.com/design-styles/css-neon/neon-pricing-cards/

Glow used as hierarchy rather than decoration: the recommended tier carries the full three-layer stack, the neighbours keep a single dim halo, and the difference is legible from across the room. Because brightness alone cannot carry meaning, the featured tier is also labelled and marked, so the ranking survives with the light switched off.
## HTML
```html
<section class="nn-11" aria-labelledby="nn-11-heading">
  <div class="nn-11__stage">
    <div class="nn-11__theme">
      <input class="nn-11__tin" type="checkbox" id="nn-11-theme">
      <label class="nn-11__tlab" for="nn-11-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-11__head">
      <p class="nn-11__kicker">Basalt &middot; platform plans</p>
      <h2 class="nn-11__heading" id="nn-11-heading">Glow as hierarchy, not decoration</h2>
      <p class="nn-11__sub">Three intensity levels from one token. The recommended tier is also labelled, so the ranking survives without the light.</p>
    </header>

    <ul class="nn-11__grid">
      <li class="nn-11__card" style="--nn-11-i: .45;">
        <p class="nn-11__tier">Starter</p>
        <p class="nn-11__price">$0<span class="nn-11__per">/month</span></p>
        <ul class="nn-11__feats">
          <li class="nn-11__feat">1 project</li>
          <li class="nn-11__feat">7-day log retention</li>
          <li class="nn-11__feat">Community support</li>
        </ul>
        <button class="nn-11__btn" type="button">Start free</button>
      </li>

      <li class="nn-11__card nn-11__card--feature" style="--nn-11-i: 1;">
        <p class="nn-11__flag">
          <svg class="nn-11__check" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M2.5 8.5 6 12l7.5-8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
          Recommended
        </p>
        <p class="nn-11__tier">Team</p>
        <p class="nn-11__price">$48<span class="nn-11__per">/month</span></p>
        <ul class="nn-11__feats">
          <li class="nn-11__feat">Unlimited projects</li>
          <li class="nn-11__feat">90-day log retention</li>
          <li class="nn-11__feat">Sync 4 repositories</li>
          <li class="nn-11__feat">Priority support</li>
        </ul>
        <button class="nn-11__btn nn-11__btn--primary" type="button">Choose Team</button>
      </li>

      <li class="nn-11__card" style="--nn-11-i: .25;">
        <p class="nn-11__tier">Scale</p>
        <p class="nn-11__price">$180<span class="nn-11__per">/month</span></p>
        <ul class="nn-11__feats">
          <li class="nn-11__feat">Dedicated regions</li>
          <li class="nn-11__feat">1-year log retention</li>
          <li class="nn-11__feat">Named support engineer</li>
        </ul>
        <button class="nn-11__btn" type="button">Talk to sales</button>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
.nn-11 {
  --nn-11-bad: #f4a4a4;
  --nn-11-warn: #f0c88a;
  --nn-11-spec-neon: #a97bff;
}

@media (prefers-color-scheme: light) {
  .nn-11 {
    --nn-11-bad: #a12a20;
    --nn-11-warn: #78490a;
  }

  .nn-11:has(#nn-11-theme:checked) {
    --nn-11-bad: #f4a4a4;
    --nn-11-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-11:has(#nn-11-theme:checked) {
    --nn-11-bad: #a12a20;
    --nn-11-warn: #78490a;
  }
}

.nn-11[data-theme="light"] {
  --nn-11-bad: #a12a20;
  --nn-11-warn: #78490a;
}

.nn-11 {
  --nn-11-spec-ink: #f2eefc;
  --nn-11-spec-dim: #a496c4;
}

.nn-11__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-11__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-11__tlab {
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

.nn-11__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-11__tlab:hover {
  opacity: 1;
}

.nn-11__tin:focus-visible + .nn-11__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-11:has(#nn-11-theme:checked) {
    --nn-11-bg: #0f0b1c;
    --nn-11-card: #150f26;
    --nn-11-line: #2a1f45;
    --nn-11-ink: #f2eefc;
    --nn-11-muted: #a496c4;
    --nn-11-neon: #a97bff;
    background-image: radial-gradient(120% 80% at 50% 0%, #1a1233 0%, #0f0b1c 55%, #09060f 100%);
  }
}

@media (prefers-color-scheme: dark) {
  .nn-11:has(#nn-11-theme:checked) {
    --nn-11-bg: #eeebf4;
    --nn-11-card: #ffffff;
    --nn-11-line: #cdc5dd;
    --nn-11-ink: #150f26;
    --nn-11-muted: #554a70;
    --nn-11-neon: #5b2bb8;
    background-image: none;
  }
}

.nn-11 {
  --nn-11-hue: 288;
  --nn-11-bg: #0f0b1c;
  --nn-11-card: #150f26;
  --nn-11-line: #2a1f45;
  --nn-11-ink: #f2eefc;
  --nn-11-muted: #a496c4;
  --nn-11-neon: #a97bff;
  --nn-11-i: .45;
  --nn-11-core: rgba(169, 123, 255, .55);
  --nn-11-halo: rgba(169, 123, 255, .3);
  --nn-11-bloom: rgba(169, 123, 255, .16);
  --nn-11-font-display: system-ui, "Helvetica Neue", Arial, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-11-bg);
  background-image: radial-gradient(120% 80% at 50% 0%, #1a1233 0%, #0f0b1c 55%, #09060f 100%);
  color: var(--nn-11-ink);
  font-family: system-ui, sans-serif;
}

.nn-11 *,
.nn-11 *::before,
.nn-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-11 {
    --nn-11-bg: oklch(17% 0.045 300);
    --nn-11-card: oklch(21% 0.05 300);
    --nn-11-line: oklch(31% 0.06 300);
    --nn-11-ink: oklch(96% 0.016 300);
    --nn-11-muted: oklch(74% 0.04 300);
    --nn-11-neon: oklch(76% 0.18 var(--nn-11-hue));
  }
}

@supports (color: color-mix(in oklab, red, blue)) {
  .nn-11__card {
    --nn-11-core: color-mix(in oklab, oklch(78% 0.18 var(--nn-11-hue)) calc(var(--nn-11-i) * 85%), transparent);
    --nn-11-halo: color-mix(in oklab, oklch(74% 0.17 var(--nn-11-hue)) calc(var(--nn-11-i) * 45%), transparent);
    --nn-11-bloom: color-mix(in oklab, oklch(70% 0.16 var(--nn-11-hue)) calc(var(--nn-11-i) * 26%), transparent);
  }
}

@media (prefers-color-scheme: light) {
  .nn-11 {
    --nn-11-bg: #eeebf4;
    --nn-11-card: #ffffff;
    --nn-11-line: #cdc5dd;
    --nn-11-ink: #150f26;
    --nn-11-muted: #554a70;
    --nn-11-neon: #5b2bb8;
    background-image: none;
  }
}

.nn-11[data-theme="light"] {
  --nn-11-bg: #eeebf4;
  --nn-11-card: #ffffff;
  --nn-11-line: #cdc5dd;
  --nn-11-ink: #150f26;
  --nn-11-muted: #554a70;
  --nn-11-neon: #5b2bb8;
  background-image: none;
}

.nn-11[data-theme="dark"] {
  --nn-11-bad: #f4a4a4;
  --nn-11-warn: #f0c88a;
  --nn-11-bg: #0f0b1c;
  --nn-11-card: #150f26;
  --nn-11-line: #2a1f45;
  --nn-11-ink: #f2eefc;
  --nn-11-muted: #a496c4;
  --nn-11-neon: #a97bff;
  background-image: radial-gradient(120% 80% at 50% 0%, #1a1233 0%, #0f0b1c 55%, #09060f 100%);
}

.nn-11__stage {
  max-width: 70rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 4.5vw, 2.25rem) clamp(1rem, 4vw, 2rem) clamp(2rem, 5vw, 2.75rem);
  display: grid;
  gap: clamp(1.35rem, 3.5vw, 1.85rem);
}

.nn-11__kicker {
  margin: 0 0 .45rem;
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--nn-11-neon);
}

.nn-11__heading {
  margin: 0;
  font-family: var(--nn-11-font-display);
  font-size: clamp(1.4rem, 4.8vw, 2.05rem);
  font-weight: 640;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.nn-11__sub {
  margin: .55rem 0 0;
  max-width: 40rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-11-muted);
  text-wrap: pretty;
}

.nn-11__grid {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1.1rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  align-items: start;
}

.nn-11__card {
  display: grid;
  gap: .7rem;
  align-content: start;
  padding: clamp(1.1rem, 3.5vw, 1.5rem);
  border: 1px solid color-mix(in srgb, var(--nn-11-neon) 30%, var(--nn-11-line));
  border-radius: .75rem;
  background: var(--nn-11-card);
  min-inline-size: 0;
  transition: box-shadow 160ms ease;
  box-shadow: 0 0 .35rem var(--nn-11-core), 0 2px clamp(.9rem, 3.5vw, 1.35rem) var(--nn-11-halo), 0 6px clamp(1.75rem, 8vw, 3rem) var(--nn-11-bloom);
}

.nn-11__card--feature {
  border-color: var(--nn-11-neon);
}

.nn-11__card:hover {
  box-shadow: 0 0 .4rem var(--nn-11-core), 0 2px clamp(1rem, 4vw, 1.55rem) var(--nn-11-halo), 0 6px clamp(2rem, 9vw, 3.4rem) var(--nn-11-bloom);
}

.nn-11__flag {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  align-self: start;
  padding: .28rem .55rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--nn-11-neon) 20%, transparent);
  color: var(--nn-11-neon);
  font-size: .7rem;
  font-weight: 650;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.nn-11__check {
  width: .8rem;
  height: .8rem;
  display: block;
}

.nn-11__tier {
  margin: 0;
  font-size: .92rem;
  font-weight: 650;
  letter-spacing: -.01em;
}

.nn-11__price {
  margin: 0;
  font-family: var(--nn-11-font-display);
  font-size: clamp(1.6rem, 5vw, 2.1rem);
  font-weight: 650;
  letter-spacing: -.03em;
}

.nn-11__per {
  font-size: .78rem;
  font-weight: 400;
  color: var(--nn-11-muted);
  letter-spacing: 0;
}

.nn-11__feats {
  margin: .2rem 0 .4rem;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .4rem;
}

.nn-11__feat {
  font-size: .84rem;
  line-height: 1.45;
  color: var(--nn-11-muted);
  min-inline-size: 0;
}

.nn-11__card--feature .nn-11__feat {
  color: var(--nn-11-ink);
}

.nn-11__card--feature .nn-11__feat::before {
  content: "\2713\00a0";
  color: var(--nn-11-neon);
}

.nn-11__btn {
  min-height: 44px;
  padding: .7rem 1rem;
  border: 1px solid var(--nn-11-line);
  border-radius: .4rem;
  background: transparent;
  color: var(--nn-11-ink);
  font-family: inherit;
  font-size: .85rem;
  font-weight: 550;
  cursor: pointer;
  transition: border-color 140ms ease, background-color 140ms ease;
}

.nn-11__btn:hover {
  border-color: var(--nn-11-neon);
}

.nn-11__btn:focus-visible {
  outline: 2px solid var(--nn-11-ink);
  outline-offset: 2px;
}

.nn-11__btn--primary {
  border-color: var(--nn-11-neon);
  background: color-mix(in srgb, var(--nn-11-neon) 18%, transparent);
  box-shadow: 0 0 .3rem var(--nn-11-core), 0 0 1rem var(--nn-11-halo);
}

@media (prefers-reduced-motion: reduce) {
  .nn-11__card,
    .nn-11__btn {
    transition: none;
  }
}
```
