---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/feature-section-with-autoplay-product-video/"
title: "Feature Section with Autoplay Product Video"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "A feature block built around a silent looping product clip sitting inside a browser-chrome frame, with the copy and three supporting points alongside it."
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section with Autoplay Product Video
Source: https://codefronts.com/layouts/css-feature-sections/feature-section-with-autoplay-product-video/

A feature block built around a silent looping product clip sitting inside a browser-chrome frame, with the copy and three supporting points alongside it. The video is pure markup — autoplay, muted, loop, playsinline and an inline SVG poster — so it starts without script, without a play button on iOS, and without a layout shift while it downloads.
## HTML
```html
<section class="fs-05" aria-labelledby="fs-05-heading">
  <div class="fs-05__hero" aria-hidden="true">
    <span class="fs-05__wordmark">Prism</span>
    <span class="fs-05__heronav">Editor · Templates · Community</span>
  </div>

  <div class="fs-05__stage">
    <div class="fs-05__split">
      <div class="fs-05__copy">
        <p class="fs-05__eyebrow">Motion, without the timeline</p>
        <h2 class="fs-05__heading" id="fs-05-heading">Describe the transition. Prism builds the curve.</h2>
        <p class="fs-05__prose">Drop two states on the canvas and Prism interpolates everything between them — spring, stagger, and the easing your designers keep asking for by name. Export as CSS, or as a component your codebase already understands.</p>
        <ul class="fs-05__points">
          <li><b>Spring physics by default</b><span>Mass, tension and damping, not four bezier handles.</span></li>
          <li><b>Stagger any collection</b><span>One control drives the delay across a list of children.</span></li>
          <li><b>Export as real CSS</b><span>Keyframes and custom properties, readable in review.</span></li>
        </ul>
        <div class="fs-05__actions">
          <a class="fs-05__cta" href="#fs-05-heading">Open the editor</a>
          <a class="fs-05__ghost" href="#fs-05-heading">Watch the 90-second tour</a>
        </div>
      </div>

      <figure class="fs-05__figure">
        <div class="fs-05__frame">
          <div class="fs-05__chrome" aria-hidden="true">
            <span class="fs-05__light"></span><span class="fs-05__light"></span><span class="fs-05__light"></span>
            <span class="fs-05__url">prism.studio/canvas</span>
          </div>
          <div class="fs-05__viewport">
            <video class="fs-05__video" autoplay muted loop playsinline preload="metadata" poster="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 640 400'%3E%3Crect width='640' height='400' fill='%23241c2b'/%3E%3Ccircle cx='300' cy='190' r='96' fill='%23f4a08a' opacity='0.5'/%3E%3Ccircle cx='390' cy='240' r='70' fill='%23b79ae0' opacity='0.55'/%3E%3C/svg%3E">
              <source src="https://mdn.github.io/shared-assets/videos/flower.webm" type="video/webm">
              <source src="https://mdn.github.io/shared-assets/videos/flower.mp4" type="video/mp4">
            </video>
          </div>
        </div>
        <figcaption class="fs-05__caption">Silent loop · 12s · no controls, no sound, no script</figcaption>
      </figure>
    </div>
  </div>

  <div class="fs-05__below" aria-hidden="true">Templates gallery · Pricing</div>
</section>
```
## CSS
```css
.fs-05 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #fdf3ec;
  --page: oklch(0.965 0.022 55);
  --page2: #f0e6fb;
  --page2: oklch(0.93 0.036 300);
  --card: #ffffff;
  --ink: #2b1f2c;
  --ink: oklch(0.28 0.032 320);
  --muted: #6f6272;
  --muted: oklch(0.52 0.026 320);
  --rule: #ecdcdf;
  --rule: oklch(0.9 0.017 20);
  --accent: #f2704f;
  --accent: oklch(0.7 0.16 35);
  --radius: 18px;
  --font-display: "SF Pro Rounded", ui-rounded, "Trebuchet MS", system-ui, sans-serif;
  background: linear-gradient(160deg, var(--page) 0%, var(--page2) 100%);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-05 *,
.fs-05 *::before,
.fs-05 *::after {
  box-sizing: border-box;
}

.fs-05__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 20px 24px;
}

.fs-05__wordmark {
  font: 700 17px/1 var(--font-display);
  letter-spacing: -0.01em;
}

.fs-05__heronav {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-05__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  padding: clamp(28px, 5vw, 64px) 18px clamp(36px, 6vw, 72px);
}

.fs-05__split {
  inline-size: 100%;
  max-inline-size: 70rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr);
  gap: clamp(28px, 5vw, 60px);
  align-items: center;
}

.fs-05__copy {
  min-inline-size: 0;
}

.fs-05__eyebrow {
  margin: 0 0 14px;
  padding: 6px 12px;
  display: inline-block;
  font: 700 11px/1 system-ui, sans-serif;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #a83c1f;
  color: color-mix(in oklab, var(--accent) 75%, black);
  background: color-mix(in oklab, var(--accent) 15%, var(--card));
  border-radius: 999px;
}

.fs-05__heading {
  margin: 0 0 16px;
  font: 600 clamp(27px, 4.8vw, 42px)/1.1 var(--font-display);
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.fs-05__prose {
  margin: 0 0 24px;
  max-inline-size: 48ch;
  font-size: 15.5px;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-05__points {
  display: grid;
  gap: 16px;
  margin: 0 0 28px;
  padding: 0;
  list-style: none;
}

.fs-05__points li {
  display: grid;
  gap: 3px;
  padding-inline-start: 30px;
  position: relative;
  min-inline-size: 0;
}

.fs-05__points li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: 2px;
  inline-size: 18px;
  block-size: 18px;
  border-radius: 50%;
  background: color-mix(in oklab, var(--accent) 22%, var(--card));
  box-shadow: inset 0 0 0 2px color-mix(in oklab, var(--accent) 70%, var(--card));
}

.fs-05__points b {
  font-size: 14.5px;
  font-weight: 650;
}

.fs-05__points span {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--muted);
}

.fs-05__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.fs-05__cta {
  display: inline-flex;
  align-items: center;
  min-height: 46px;
  padding: 0 22px;
  font: 650 14px/1 var(--font-display);
  color: #fff;
  background: var(--accent);
  border-radius: 999px;
  text-decoration: none;
  box-shadow: 0 10px 26px -8px color-mix(in oklab, var(--accent) 60%, transparent);
}

.fs-05__cta:hover {
  background: color-mix(in oklab, var(--accent) 85%, black);
}

.fs-05__ghost {
  display: inline-flex;
  align-items: center;
  min-height: 46px;
  padding: 0 18px;
  font: 600 14px/1 var(--font-display);
  color: var(--ink);
  background: var(--card);
  border-radius: 999px;
  text-decoration: none;
}

.fs-05__ghost:hover {
  background: color-mix(in oklab, var(--ink) 6%, var(--card));
}

.fs-05__cta:focus-visible,
.fs-05__ghost:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.fs-05__figure {
  margin: 0;
  min-inline-size: 0;
}

.fs-05__frame {
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--card);
  border: 1px solid var(--rule);
  box-shadow: 0 30px 70px -30px color-mix(in oklab, var(--accent) 45%, transparent), 0 4px 12px -6px rgba(43, 31, 44, 0.2);
}

.fs-05__chrome {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 11px 14px;
  background: color-mix(in oklab, var(--ink) 5%, var(--card));
  border-block-end: 1px solid var(--rule);
}

.fs-05__light {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: var(--rule);
  flex: none;
}

.fs-05__light:first-child {
  background: color-mix(in oklab, var(--accent) 60%, var(--rule));
}

.fs-05__url {
  margin-inline-start: 8px;
  padding: 4px 12px;
  font-size: 11px;
  color: var(--muted);
  background: var(--card);
  border-radius: 999px;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fs-05__viewport {
  aspect-ratio: 16 / 10;
  background: #241c2b;
}

.fs-05__video {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

.fs-05__caption {
  margin: 12px 4px 0;
  font-size: 11.5px;
  letter-spacing: 0.02em;
  color: var(--muted);
}

.fs-05__below {
  padding: 16px 24px;
  font-size: 12px;
  color: var(--muted);
  border-block-start: 1px solid color-mix(in oklab, var(--ink) 8%, transparent);
}

@media (max-width: 860px) {
  .fs-05__split {
    grid-template-columns: minmax(0, 1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fs-05__video {
    display: none;
  }

  .fs-05__viewport {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 640 400'%3E%3Crect width='640' height='400' fill='%23241c2b'/%3E%3Ccircle cx='300' cy='190' r='96' fill='%23f4a08a' opacity='0.5'/%3E%3Ccircle cx='390' cy='240' r='70' fill='%23b79ae0' opacity='0.55'/%3E%3C/svg%3E");
    background-size: cover;
    background-position: center;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-05 {
    --page: #241b26;
    --page2: #1a1622;
    --card: #2c2333;
    --ink: #f8eef4;
    --muted: #b8a5b8;
    --rule: #3d3145;
    --accent: #ff8b62;
  }

  .fs-05__cta {
    color: #241b26;
  }

  .fs-05__eyebrow {
    color: #ffd6c6;
  }
}

[data-theme="dark"] .fs-05 {
  --page: #241b26;
  --page2: #1a1622;
  --card: #2c2333;
  --ink: #f8eef4;
  --muted: #b8a5b8;
  --rule: #3d3145;
  --accent: #ff8b62;
}

[data-theme="dark"] .fs-05 .fs-05__cta {
  color: #241b26;
}
```
