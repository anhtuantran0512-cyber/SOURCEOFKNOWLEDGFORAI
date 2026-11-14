---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/scroll-reveal-suite/"
title: "Named Scroll Timelines Across Elements"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "An anonymous scroll() resolves to whichever scroll container happens to be nearest."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Named Scroll Timelines Across Elements
Source: https://codefronts.com/motion/css-scroll-animations/scroll-reveal-suite/

An anonymous scroll() resolves to whichever scroll container happens to be nearest. A named timeline is explicit instead: the scroller publishes its progress as scroll-timeline-name: --sa-10-feed and any descendant consumes it with animation-timeline: --sa-10-feed. Two elements in different branches of the tree, driven by one binding.
## HTML
```html
<section class="sa-10" aria-labelledby="sa-10-h">
  <fieldset class="sa-10__theme">
    <legend class="sa-10__themelegend">Theme</legend>
    <input class="sa-10__themeinput" type="radio" name="sa-10-theme" id="sa-10-theme-auto" checked>
    <label class="sa-10__themeopt" for="sa-10-theme-auto">Auto</label>
    <input class="sa-10__themeinput" type="radio" name="sa-10-theme" id="sa-10-theme-light">
    <label class="sa-10__themeopt" for="sa-10-theme-light">Light</label>
    <input class="sa-10__themeinput" type="radio" name="sa-10-theme" id="sa-10-theme-dark">
    <label class="sa-10__themeopt" for="sa-10-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-10__stage">
    <header class="sa-10__head">
      <p class="sa-10__eyebrow">One name, two consumers</p>
      <h2 class="sa-10__h" id="sa-10-h">The scroller publishes, descendants subscribe</h2>
      <p class="sa-10__sub">Both moving parts below reference <span class="sa-10__mono">--sa-10-feed</span>. Neither knows which element the scroller is, and neither needs to.</p>
    </header>

    <div class="sa-10__feed" id="sa-10-feed">
      <div class="sa-10__bar">
        <p class="sa-10__owner">Timeline owner · <span class="sa-10__mono">scroll-timeline: --sa-10-feed block</span></p>
        <div class="sa-10__consumers">
          <p class="sa-10__tag">Consumer A · branch 1</p>
          <div class="sa-10__meter"><span class="sa-10__meterfill"></span></div>
        </div>
      </div>

      <div class="sa-10__scroller" tabindex="0" role="region" aria-label="Basalt deployment activity, scrollable">
        <div class="sa-10__rail">
          <p class="sa-10__tag sa-10__tag--b">Consumer B · branch 2</p>
          <div class="sa-10__dots" aria-hidden="true"><span class="sa-10__dotmark"></span></div>
        </div>
        <ol class="sa-10__list">
          <li class="sa-10__card"><p class="sa-10__ct">Deploy to production</p><p class="sa-10__cm">Basalt · api-gateway · Alex Chen · 2m ago</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Sync 4 repositories</p><p class="sa-10__cm">Fern, Talon, Vale, Orbit · webhook queue drained</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Rotate signing key</p><p class="sa-10__cm">Meridian · scheduled · Priya Sharma approved</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Invite teammate</p><p class="sa-10__cm">3 invitations sent to the Nova workspace</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Roll back release 4.1.7</p><p class="sa-10__cm">Sable · migration check failed · Jordan Lee</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Archive stale branches</p><p class="sa-10__cm">Quill · 41 branches older than 90 days</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Publish changelog</p><p class="sa-10__cm">Prism · 4.2 notes · Sam Rivera</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Rebuild search index</p><p class="sa-10__cm">Aperture · incremental · 4m 12s</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Expire access tokens</p><p class="sa-10__cm">Ranger · 18 tokens older than a year</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Promote replica to primary</p><p class="sa-10__cm">Vale · eu-west · manual failover</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Approve invoice run</p><p class="sa-10__cm">Meridian · 1,204 accounts · Priya Sharma</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Retry parked webhooks</p><p class="sa-10__cm">Talon · 6 deliveries · queued</p></li>
          <li class="sa-10__card"><p class="sa-10__ct">Close change ticket</p><p class="sa-10__cm">Nova · CHG-4471 · Alex Chen</p></li>
        </ol>
      </div>
    </div>

    <p class="sa-10__note">Both consumers sit inside <span class="sa-10__mono">.sa-10__feed</span>, the element that declares the name. Move either one outside it and the name stops resolving — silently.</p>
  </div>
</section>
```
## CSS
```css
.sa-10 {
  --page: #1a1613;
  --surface: #241e19;
  --ink: #f6efe6;
  --muted: #b09c88;
  --rule: #3a3028;
  --accent: #f0a52c;
  --page: oklch(20% 0.014 60);
  --surface: oklch(25% 0.018 62);
  --ink: oklch(95% 0.015 80);
  --muted: oklch(72% 0.038 70);
  --rule: oklch(32% 0.02 62);
  --accent: oklch(78% 0.155 72);
  --font-display: "Avenir Next Condensed", "Roboto Condensed", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 4rem 1.25rem 3.5rem;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-10 *,
.sa-10 *::before,
.sa-10 *::after {
  box-sizing: border-box;
}

.sa-10__stage {
  max-inline-size: 58rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.sa-10__head {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
}

.sa-10__eyebrow {
  margin: 0;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-10__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.625rem, 5vw, 2.625rem);
  font-weight: 600;
  letter-spacing: 0.005em;
  line-height: 1.08;
}

.sa-10__sub {
  margin: 0;
  max-inline-size: 42rem;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-10__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.82em;
  color: var(--accent);
}

.sa-10__feed {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.sa-10__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1.25rem;
  background: var(--surface);
  border: 2px solid var(--ink);
  box-shadow: 8px 8px 0 var(--accent);
}

.sa-10__owner {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  letter-spacing: 0.02em;
  color: var(--muted);
}

.sa-10__consumers {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  min-inline-size: 11rem;
}

.sa-10__tag {
  margin: 0;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink);
}

.sa-10__tag--b {
  color: var(--accent);
  writing-mode: horizontal-tb;
}

.sa-10__meter {
  block-size: 0.75rem;
  background: color-mix(in srgb, var(--ink) 14%, transparent);
  overflow: hidden;
}

.sa-10__meterfill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  background: var(--accent);
  transform-origin: left center;
  transform: scaleX(1);
}

.sa-10__scroller {
  position: relative;
  display: grid;
  grid-template-columns: 3.25rem minmax(0, 1fr);
  block-size: 58vh;
  min-block-size: 19rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  scroll-timeline: --sa-10-feed block;
  border: 2px solid var(--ink);
  background: var(--surface);
}

.sa-10__scroller:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.sa-10__rail {
  position: sticky;
  inset-block-start: 0;
  align-self: start;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 0;
  border-inline-end: 1px solid var(--rule);
}

.sa-10__rail .sa-10__tag--b {
  writing-mode: vertical-rl;
  font-size: 0.5625rem;
  letter-spacing: 0.14em;
}

.sa-10__dots {
  position: relative;
  inline-size: 0.5rem;
  block-size: 8rem;
  background: color-mix(in srgb, var(--ink) 12%, transparent);
}

.sa-10__dotmark {
  position: absolute;
  inset-inline: -0.3125rem;
  block-size: 1.125rem;
  background: var(--accent);
  border-radius: 999px;
  inset-block-start: 0;
  transform: translateY(6.875rem);
}

.sa-10__list {
  margin: 0;
  min-block-size: 26rem;
  padding: 1rem 1.25rem 3rem;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.sa-10__card {
  padding: 0.9375rem 1rem;
  background: color-mix(in srgb, var(--ink) 5%, transparent);
  border-inline-start: 3px solid var(--rule);
  min-inline-size: 0;
}

.sa-10__ct {
  margin: 0 0 0.25rem;
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 600;
}

.sa-10__cm {
  margin: 0;
  font-size: 0.8125rem;
  color: var(--muted);
}

.sa-10__note {
  margin: 0;
  padding-block-start: 1rem;
  border-block-start: 1px solid var(--rule);
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-10-meter {
  from {
    transform: scaleX(0.04);
  }

  to {
    transform: scaleX(1);
  }
}

@keyframes sa-10-dot {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(6.875rem);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-10__meterfill {
    animation: sa-10-meter linear both;
    animation-timeline: --sa-10-feed;
    animation-range: 0% 70%;
  }

  .sa-10__dotmark {
    animation: sa-10-dot linear both;
    animation-timeline: --sa-10-feed;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-10__meterfill,
    .sa-10__dotmark {
    animation: none;
  }

  .sa-10__meterfill {
    transform: scaleX(1);
  }

  .sa-10__dotmark {
    transform: translateY(6.875rem);
  }
}

.sa-10__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 2px solid var(--ink);
  background: var(--surface);
}

.sa-10__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-10__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-10__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.625rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-10__themeinput:checked + .sa-10__themeopt {
  color: var(--page);
  background: var(--accent);
}

.sa-10__themeinput:focus-visible + .sa-10__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 34rem) {
  .sa-10__bar {
    box-shadow: 5px 5px 0 var(--accent);
  }

  .sa-10__scroller {
    grid-template-columns: 2.5rem minmax(0, 1fr);
  }
}

@media (forced-colors: active) {
  .sa-10__meterfill,
    .sa-10__dotmark {
    background: Highlight;
  }
}

@media (prefers-color-scheme: light) {
  .sa-10:not(:has(#sa-10-theme-dark:checked)) {
    --page: #fdf8f0;
    --surface: #ffffff;
    --ink: #1e1813;
    --muted: #6f5f4e;
    --rule: #e2d5c3;
    --accent: #b46a05;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-10:has(#sa-10-theme-light:checked) {
    --page: #fdf8f0;
    --surface: #ffffff;
    --ink: #1e1813;
    --muted: #6f5f4e;
    --rule: #e2d5c3;
    --accent: #b46a05;
  }
}

[data-theme="light"] .sa-10:not(:has(#sa-10-theme-dark:checked)) {
  --page: #fdf8f0;
  --surface: #ffffff;
  --ink: #1e1813;
  --muted: #6f5f4e;
  --rule: #e2d5c3;
  --accent: #b46a05;
}

.sa-10:has(#sa-10-theme-light:checked) {
  --page: #fdf8f0;
  --surface: #ffffff;
  --ink: #1e1813;
  --muted: #6f5f4e;
  --rule: #e2d5c3;
  --accent: #b46a05;
}

.sa-10:has(#sa-10-theme-dark:checked) {
  --page: #1a1613;
  --surface: #241e19;
  --ink: #f6efe6;
  --muted: #b09c88;
  --rule: #3a3028;
  --accent: #f0a52c;
}
```
