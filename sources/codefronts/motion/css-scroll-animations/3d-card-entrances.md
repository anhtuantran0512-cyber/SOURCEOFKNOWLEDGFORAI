---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/3d-card-entrances/"
title: "Perspective and Transform on a Scroll Timeline"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Binding rotateX and translateZ to a view timeline gives a card that turns as it arrives — but only if the two properties that make 3D work are on the right…"
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Perspective and Transform on a Scroll Timeline
Source: https://codefronts.com/motion/css-scroll-animations/3d-card-entrances/

Binding rotateX and translateZ to a view timeline gives a card that turns as it arrives — but only if the two properties that make 3D work are on the right elements. perspective belongs to the parent, transform-style: preserve-3d to the transformed element, and getting either wrong flattens the whole scene.
## HTML
```html
<section class="sa-19" aria-labelledby="sa-19-h">
  <fieldset class="sa-19__theme">
    <legend class="sa-19__themelegend">Theme</legend>
    <input class="sa-19__themeinput" type="radio" name="sa-19-theme" id="sa-19-theme-auto" checked>
    <label class="sa-19__themeopt" for="sa-19-theme-auto">Auto</label>
    <input class="sa-19__themeinput" type="radio" name="sa-19-theme" id="sa-19-theme-light">
    <label class="sa-19__themeopt" for="sa-19-theme-light">Light</label>
    <input class="sa-19__themeinput" type="radio" name="sa-19-theme" id="sa-19-theme-dark">
    <label class="sa-19__themeopt" for="sa-19-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-19__stage">
    <header class="sa-19__head">
      <p class="sa-19__eyebrow">perspective · preserve-3d</p>
      <h2 class="sa-19__h" id="sa-19-h">Depth bound to a view timeline</h2>
      <p class="sa-19__sub">Two properties on two different elements. <span class="sa-19__mono">perspective</span> on the scene, <span class="sa-19__mono">transform-style: preserve-3d</span> on the card. The crosshair marks <span class="sa-19__mono">perspective-origin</span>.</p>
    </header>

    <div class="sa-19__scroller" tabindex="0" role="region" aria-label="Scroll driven 3D cards, scrollable">
      <div class="sa-19__scene">
        <span class="sa-19__origin" aria-hidden="true"></span>
        <div class="sa-19__cards">
          <article class="sa-19__card">
            <p class="sa-19__ck">Nova · api-edge</p>
            <p class="sa-19__cv">99.982%</p>
            <p class="sa-19__cm">30-day availability</p>
            <span class="sa-19__badge">preserve-3d</span>
          </article>
          <article class="sa-19__card">
            <p class="sa-19__ck">Talon · queue depth</p>
            <p class="sa-19__cv">412</p>
            <p class="sa-19__cm">peak, last 24h</p>
            <span class="sa-19__badge">preserve-3d</span>
          </article>
          <article class="sa-19__card">
            <p class="sa-19__ck">Sable · deploys</p>
            <p class="sa-19__cv">37</p>
            <p class="sa-19__cm">this week · Jordan Lee</p>
            <span class="sa-19__badge">preserve-3d</span>
          </article>
          <article class="sa-19__card">
            <p class="sa-19__ck">Quill · error budget</p>
            <p class="sa-19__cv">68%</p>
            <p class="sa-19__cm">remaining this quarter</p>
            <span class="sa-19__badge">preserve-3d</span>
          </article>
          <article class="sa-19__card">
            <p class="sa-19__ck">Fern · build time</p>
            <p class="sa-19__cv">4m 12s</p>
            <p class="sa-19__cm">median, main branch</p>
            <span class="sa-19__badge">preserve-3d</span>
          </article>
          <article class="sa-19__card">
            <p class="sa-19__ck">Vale · invoice run</p>
            <p class="sa-19__cv">1,204</p>
            <p class="sa-19__cm">accounts settled · Priya Sharma</p>
            <span class="sa-19__badge">preserve-3d</span>
          </article>
        </div>
        <p class="sa-19__foot"><span class="sa-19__mono">animation-range: entry 10% cover 55%</span> — steepest on arrival, flat once landed.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-19 {
  --page: #0a0616;
  --surface: #140c2a;
  --ink: #f0eaff;
  --muted: #9c8cd4;
  --rule: #2a1c52;
  --accent: #b06cff;
  --accent2: #2ee6ff;
  --page: oklch(13% 0.05 300);
  --surface: oklch(20% 0.07 300);
  --ink: oklch(94% 0.02 300);
  --muted: oklch(68% 0.09 300);
  --rule: oklch(30% 0.08 300);
  --accent: oklch(70% 0.2 305);
  --accent2: oklch(85% 0.15 200);
  --sa-19-persp: 900px;
  --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 4rem 1rem 3rem;
  background: var(--page);
  background-image: radial-gradient(45rem 22rem at 80% 0%, color-mix(in srgb, var(--accent) 18%, transparent), transparent 65%);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-19 *,
.sa-19 *::before,
.sa-19 *::after {
  box-sizing: border-box;
}

.sa-19__stage {
  max-inline-size: 54rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.sa-19__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-19__eyebrow {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent2);
}

.sa-19__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 4vw, 2rem);
  font-weight: 500;
  letter-spacing: -0.03em;
  line-height: 1.12;
  text-shadow: 0 0 2rem color-mix(in srgb, var(--accent) 55%, transparent);
}

.sa-19__sub {
  margin: 0;
  max-inline-size: 44rem;
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-19__mono {
  font-family: var(--font-display);
  font-size: 0.85em;
  color: var(--accent2);
}

.sa-19__scroller {
  block-size: 60vh;
  min-block-size: 20rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  background: color-mix(in srgb, var(--surface) 70%, transparent);
  box-shadow: inset 0 0 4rem color-mix(in srgb, var(--accent) 12%, transparent);
  scroll-timeline: --sa-19-track block;
}

.sa-19__scroller:focus-visible {
  outline: 2px solid var(--accent2);
  outline-offset: 2px;
}

.sa-19__scene {
  position: relative;
  min-block-size: calc(100% + 4rem);
  padding: 3rem 1.25rem 4rem;
  perspective: var(--sa-19-persp);
  perspective-origin: 50% 40%;
}

.sa-19__origin {
  position: absolute;
  inset-block-start: 40%;
  inset-inline-start: 50%;
  inline-size: 1.5rem;
  block-size: 1.5rem;
  margin: -0.75rem 0 0 -0.75rem;
  border-radius: 999px;
  border: 1px dashed var(--accent2);
}

.sa-19__origin::before,
.sa-19__origin::after {
  content: "";
  position: absolute;
  background: var(--accent2);
}

.sa-19__origin::before {
  inset-block: -0.5rem;
  inset-inline-start: 50%;
  inline-size: 1px;
}

.sa-19__origin::after {
  inset-inline: -0.5rem;
  inset-block-start: 50%;
  block-size: 1px;
}

.sa-19__cards {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

.sa-19__card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding: 1.25rem 1.25rem 1.5rem;
  border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent);
  border-radius: 0.75rem;
  background: linear-gradient(160deg, color-mix(in srgb, var(--accent) 18%, var(--surface)), var(--surface));
  box-shadow: 0 0 2.5rem -0.5rem color-mix(in srgb, var(--accent) 50%, transparent);
  transform-style: preserve-3d;
  backface-visibility: hidden;
  transform: none;
  min-inline-size: 0;
}

.sa-19__ck {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-19__cv {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 6vw, 2.5rem);
  font-weight: 500;
  letter-spacing: -0.04em;
  color: var(--ink);
}

.sa-19__cm {
  margin: 0;
  font-size: 0.8125rem;
  color: var(--muted);
}

.sa-19__badge {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  padding: 0.1875rem 0.5rem;
  border-radius: 0.25rem;
  background: var(--accent2);
  color: #06121a;
  font-family: var(--font-display);
  font-size: 0.5625rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  transform: translateZ(2.5rem);
}

.sa-19__foot {
  margin: 2.5rem 0 0;
  font-size: 0.75rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-19-turn {
  from {
    transform: rotateX(24deg) translateZ(-4rem);
    opacity: 0.35;
  }

  to {
    transform: rotateX(0deg) translateZ(0);
    opacity: 1;
  }
}

@supports (animation-timeline: view()) {
  .sa-19__card {
    animation: sa-19-turn linear both;
    animation-timeline: view(block);
    animation-range: entry 10% cover 55%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-19__card {
    animation: none;
    transform: none;
    opacity: 1;
  }
}

.sa-19__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  background: var(--surface);
}

.sa-19__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-19__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-19__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.625rem;
  border-radius: 0.375rem;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-19__themeinput:checked + .sa-19__themeopt {
  color: var(--page);
  background: var(--accent);
}

.sa-19__themeinput:focus-visible + .sa-19__themeopt {
  outline: 2px solid var(--accent2);
  outline-offset: 2px;
}

@media (max-width: 34rem) {
  .sa-19 {
    --sa-19-persp: 600px;
    padding-block-start: 4.5rem;
  }

  .sa-19__cards {
    gap: 1.75rem;
  }
}

@media (forced-colors: active) {
  .sa-19__card {
    border: 1px solid CanvasText;
    box-shadow: none;
  }
}

@media (prefers-color-scheme: light) {
  .sa-19:not(:has(#sa-19-theme-dark:checked)) {
    --page: #f6f2ff;
    --surface: #ffffff;
    --ink: #17102c;
    --muted: #61548c;
    --rule: #ded4f6;
    --accent: #7b3fe4;
    --accent2: #0a7f96;
  }

  .sa-19:not(:has(#sa-19-theme-dark:checked)) .sa-19__badge {
    color: #ffffff;
  }

  .sa-19:not(:has(#sa-19-theme-dark:checked)) .sa-19__themeinput:checked + .sa-19__themeopt {
    color: #ffffff;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-19:has(#sa-19-theme-light:checked) {
    --page: #f6f2ff;
    --surface: #ffffff;
    --ink: #17102c;
    --muted: #61548c;
    --rule: #ded4f6;
    --accent: #7b3fe4;
    --accent2: #0a7f96;
  }

  .sa-19:has(#sa-19-theme-light:checked) .sa-19__badge,
    .sa-19:has(#sa-19-theme-light:checked) .sa-19__themeinput:checked + .sa-19__themeopt {
    color: #ffffff;
  }
}

[data-theme="light"] .sa-19:not(:has(#sa-19-theme-dark:checked)) {
  --page: #f6f2ff;
  --surface: #ffffff;
  --ink: #17102c;
  --muted: #61548c;
  --rule: #ded4f6;
  --accent: #7b3fe4;
  --accent2: #0a7f96;
}

.sa-19:has(#sa-19-theme-light:checked) {
  --page: #f6f2ff;
  --surface: #ffffff;
  --ink: #17102c;
  --muted: #61548c;
  --rule: #ded4f6;
  --accent: #7b3fe4;
  --accent2: #0a7f96;
}

.sa-19:has(#sa-19-theme-light:checked) .sa-19__badge,
.sa-19:has(#sa-19-theme-light:checked) .sa-19__themeinput:checked + .sa-19__themeopt {
  color: #ffffff;
}

.sa-19:has(#sa-19-theme-dark:checked) {
  --page: #0a0616;
  --surface: #140c2a;
  --ink: #f0eaff;
  --muted: #9c8cd4;
  --rule: #2a1c52;
  --accent: #b06cff;
  --accent2: #2ee6ff;
}

.sa-19:has(#sa-19-theme-dark:checked) .sa-19__badge {
  color: #06121a;
}
```
