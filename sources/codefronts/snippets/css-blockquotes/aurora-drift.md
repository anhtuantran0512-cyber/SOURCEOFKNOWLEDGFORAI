---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/aurora-drift/"
title: "Aurora Gradient Background CSS Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The aurora backdrop that headlines half the AI-product landing pages of the decade, built the performant way: three oversized radial-gradient blobs on their…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Gradient Background CSS Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/aurora-drift/

The aurora backdrop that headlines half the AI-product landing pages of the decade, built the performant way: three oversized radial-gradient blobs on their own layers, blurred once with filter: blur(70px), drifting on transform-only keyframes (never background-position — that repaints the gradient every frame), with a slow hue-rotate on the container cycling the palette through the teal-violet-magenta range. The quote floats above on a thin glass panel, and the whole sky freezes into a designed still under prefers-reduced-motion.
## HTML
```html
<section class="bq-18" aria-label="Aurora gradient background blockquote demo">
  <div class="bq-18__stage">
    <div class="bq-18__sky" aria-hidden="true">
      <i class="bq-18__blob bq-18__blob--a"></i>
      <i class="bq-18__blob bq-18__blob--b"></i>
      <i class="bq-18__blob bq-18__blob--c"></i>
    </div>
    <figure class="bq-18__panel">
      <p class="bq-18__kicker">Above the weather</p>
      <blockquote>
        <p>“Somewhere, something incredible is waiting to be known.”</p>
      </blockquote>
      <figcaption class="bq-18__by">— Carl Sagan</figcaption>
    </figure>
    <p class="bq-18__chip" aria-hidden="true">3 radial blobs · transform-only drift · one hue-rotate wrapper</p>
  </div>
</section>
```
## CSS
```css
.bq-18,
.bq-18 *,
.bq-18 *::before,
.bq-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.14 0.02 275);
  --ink: oklch(0.97 0.008 260);
  --mut: oklch(0.75 0.03 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-18__stage {
  position: relative;
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: var(--bg);
  overflow: hidden;
}

.bq-18__sky {
  position: absolute;
  inset: -10%;
  filter: hue-rotate(0deg);
  animation: bq18-hue 44s linear infinite;
  pointer-events: none;
}

.bq-18__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(70px);
  mix-blend-mode: screen;
}

.bq-18__blob--a {
  width: 55vmax;
  height: 55vmax;
  left: -12%;
  top: -18%;
  background: radial-gradient(circle,oklch(0.75 0.19 200/.5),transparent 65%);
  animation: bq18-drift 26s ease-in-out infinite alternate;
}

.bq-18__blob--b {
  width: 48vmax;
  height: 48vmax;
  right: -14%;
  top: -6%;
  background: radial-gradient(circle,oklch(0.6 0.22 290/.45),transparent 65%);
  animation: bq18-drift 31s ease-in-out infinite alternate-reverse;
}

.bq-18__blob--c {
  width: 42vmax;
  height: 42vmax;
  left: 22%;
  bottom: -28%;
  background: radial-gradient(circle,oklch(0.68 0.2 340/.4),transparent 65%);
  animation: bq18-drift 23s ease-in-out infinite alternate;
}

@keyframes bq18-drift {
  from {
    transform: translate(-8%,-6%) scale(1);
  }

  to {
    transform: translate(10%,8%) scale(1.18);
  }
}

@keyframes bq18-hue {
  to {
    filter: hue-rotate(360deg);
  }
}

.bq-18__panel {
  position: relative;
  width: min(100%,560px);
  text-align: center;
  padding: clamp(30px,5vw,48px);
  border-radius: 24px;
  background: oklch(0.2 0.03 280/.5);
  border: 1px solid oklch(1 0 0/.16);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.14),0 30px 70px oklch(0 0 0/.5);
}

@supports (backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px)) {
  .bq-18__panel {
    background: oklch(0.2 0.03 280/.32);
    -webkit-backdrop-filter: blur(14px) saturate(140%);
    backdrop-filter: blur(14px) saturate(140%);
  }
}

.bq-18__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 16px;
}

.bq-18__panel blockquote p {
  font-size: clamp(24px,3.4vw,36px);
  line-height: 1.3;
  font-weight: 700;
  letter-spacing: -.02em;
  text-wrap: balance;
  text-shadow: 0 2px 10px oklch(0 0 0/.3);
}

.bq-18__by {
  margin-top: 16px;
  font-size: 14px;
  color: var(--mut);
}

.bq-18__chip {
  position: relative;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  background: oklch(0.18 0.02 275/.5);
}

@media (prefers-reduced-motion: reduce) {
  .bq-18 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
