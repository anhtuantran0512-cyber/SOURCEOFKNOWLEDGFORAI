---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/typography-outline-stroke-fill/"
title: "Typography Outline / Stroke Fill"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Hollow type that pours full on hover — and it's ONE element, no duplicate layers: the glyphs are transparent with a 1.5px -webkit-text-stroke, and the fill…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Typography Outline / Stroke Fill
Source: https://codefronts.com/motion/css-text-hover-effects/typography-outline-stroke-fill/

Hollow type that pours full on hover — and it's ONE element, no duplicate layers: the glyphs are transparent with a 1.5px -webkit-text-stroke, and the fill is a background-image clipped to the text whose background-size grows 0%→100% from the baseline up. Because stroke and fill are separate paint channels on the same glyphs, they never misalign by a subpixel the way stacked-copy builds do. The wordmark fills bottom-up like poured metal; the nav links fill left-to-right like a gauge; the stroke itself warms color mid-pour.
## HTML
```html
<section class="cth-16" aria-label="Outline to fill text demo">
  <div class="cth-16__stage">
    <div class="cth-16__scene">
      <header class="cth-16__head">
        <p class="cth-16__eyebrow">Grade 900 &mdash; a display face in 5 weights</p>
        <span class="cth-16__chip">background-size: 100% 0% &rarr; 100% 100%</span>
      </header>
      <a class="cth-16__hollow" href="#cth16-top" id="cth16-top">FORGE</a>
      <nav class="cth-16__nav" aria-label="Foundry">
        <a class="cth-16__bar" href="#cth16-top">Trial fonts</a>
        <a class="cth-16__bar" href="#cth16-top">Licensing</a>
        <a class="cth-16__bar" href="#cth16-top">Specimens</a>
      </nav>
      <p class="cth-16__hint">Hover the wordmark: the fill pours up from the baseline through <code>background-clip:text</code> &mdash; one element, stroke and fill on separate paint channels.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-16,
.cth-16 *,
.cth-16 *::before,
.cth-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-16 {
  --bg: oklch(0.18 0.008 60);
  --ink: oklch(0.93 0.008 75);
  --mut: oklch(0.6 0.015 70);
  --heat1: oklch(0.72 0.18 45);
  --heat2: oklch(0.85 0.15 80);
  --line: oklch(0.32 0.012 65);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-16__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(90% 70% at 50% 100%,oklch(0.22 0.015 55),var(--bg) 70%);
  padding: clamp(20px,4vw,56px);
  container: cth16/inline-size;
}

.cth-16__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(20px,3.6cqi,32px);
  width: min(100%,760px);
}

.cth-16__head {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--line);
}

.cth-16__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--heat2);
  border: 1px solid color-mix(in oklch,var(--heat2) 40%,transparent);
  border-radius: 99px;
  padding: 5px 11px;
}

.cth-16__hollow {
  display: inline-block;
  text-decoration: none;
  font-size: clamp(72px,17cqi,180px);
  font-weight: 900;
  letter-spacing: .01em;
  line-height: 1;
  padding: .08em .06em;
  color: transparent;
  -webkit-text-stroke: 1.5px color-mix(in oklch,var(--ink) 65%,transparent);
  background-image: linear-gradient(15deg,var(--heat1),var(--heat2));
  background-repeat: no-repeat;
  background-position: 0 100%;
  background-size: 100% 0%;
  -webkit-background-clip: text;
  background-clip: text;
  transition: background-size .6s cubic-bezier(.3,.85,.2,1),-webkit-text-stroke-color .6s ease;
}

.cth-16__hollow:hover,
.cth-16__hollow:focus-visible {
  background-size: 100% 100%;
  -webkit-text-stroke-color: color-mix(in oklch,var(--heat1) 60%,transparent);
}

.cth-16__hollow:focus-visible {
  outline: 2px solid var(--heat2);
  outline-offset: 10px;
  border-radius: 6px;
}

.cth-16__nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(10px,2.4cqi,20px);
}

.cth-16__bar {
  display: grid;
  place-items: center;
  min-height: 48px;
  padding: 0 24px;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .04em;
  text-transform: uppercase;
  text-decoration: none;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  color: transparent;
  -webkit-text-stroke: 1px color-mix(in oklch,var(--ink) 70%,transparent);
  background-image: linear-gradient(90deg,var(--heat1),var(--heat2));
  background-repeat: no-repeat;
  background-position: 0 0;
  background-size: 0% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  transition: background-size .45s cubic-bezier(.3,.85,.2,1),border-color .3s;
}

.cth-16__bar:hover,
.cth-16__bar:focus-visible {
  background-size: 100% 100%;
  border-color: color-mix(in oklch,var(--heat1) 50%,var(--line));
}

.cth-16__bar:focus-visible {
  outline: 2px solid var(--heat2);
  outline-offset: 3px;
}

.cth-16__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 56ch;
}

.cth-16__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.26 0.01 60);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--heat2);
}

@media (prefers-reduced-motion: reduce) {
  .cth-16 * {
    transition-duration: .01ms !important;
  }
}
```
