---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/text-scrim-reveal-focal-point-highlight/"
title: "Text Scrim Reveal / Focal Point Highlight"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The Apple-keynote reading experience: each line of copy sits dimmed at low contrast until it scrolls into a focal band mid-screen, where it blooms to full…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Text Scrim Reveal / Focal Point Highlight
Source: https://codefronts.com/motion/css-animation-timeline/text-scrim-reveal-focal-point-highlight/

The Apple-keynote reading experience: each line of copy sits dimmed at low contrast until it scrolls into a focal band mid-screen, where it blooms to full brightness — then dims again as it leaves. Line-by-line view() timelines with a contain-range focal window; the GSAP SplitText upsell, free.
## HTML
```html
<section class="sda-09" aria-label="Scroll to highlight text line by line" role="region" tabindex="0">
  <div class="sda-09__flow">
    <p class="sda-09__kicker">Manifesto · scroll to read</p>
    <p class="sda-09__line">We believe motion is grammar, not decoration.</p>
    <p class="sda-09__line">A line of text deserves the reader's full attention —</p>
    <p class="sda-09__line">so we give it a stage, one line at a time.</p>
    <p class="sda-09__line">The page dims what you have read,</p>
    <p class="sda-09__line">holds what you are reading in perfect focus,</p>
    <p class="sda-09__line">and keeps what comes next in quiet reserve.</p>
    <p class="sda-09__line">No observers. No thresholds. No timeouts.</p>
    <p class="sda-09__line">Just your scroll position, mapped to light.</p>
    <p class="sda-09__line sda-09__line--em">Read at your own speed. The page keeps up.</p>
  </div>
</section>
```
## CSS
```css
.sda-09,
.sda-09 *,
.sda-09 *::before,
.sda-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-09 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: oklch(0.17 0.02 280);
  color: oklch(0.95 0.01 280);
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}

.sda-09__flow {
  width: min(680px,100%);
  margin: 0 auto;
  padding: 44vh 28px 52vh;
}

.sda-09__kicker {
  font: 700 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: oklch(0.65 0.12 300);
  margin-bottom: 7vh;
}

.sda-09__line {
  font-size: clamp(24px,3.6vw,38px);
  font-weight: 700;
  line-height: 1.35;
  letter-spacing: -.015em;
  margin-bottom: 5.5vh;
  text-wrap: pretty;
}

.sda-09__line--em {
  color: oklch(0.8 0.14 300);
}

.sda-09:focus-visible {
  outline: 3px solid oklch(0.65 0.12 300);
  outline-offset: -3px;
}

@supports (animation-timeline: view()) {
  .sda-09__line {
    opacity: .32;
    transform: translateX(0);
    animation: sda-09-bloom linear both;
    animation-timeline: view();
    animation-range: contain 20% contain 55%;
  }
}

@keyframes sda-09-bloom {
  from {
    opacity: .32;
    color: oklch(0.6 0.02 280);
    transform: translateX(0);
  }

  50% {
    opacity: 1;
    color: oklch(0.98 0.01 280);
    transform: translateX(10px);
  }

  to {
    opacity: .45;
    color: oklch(0.7 0.02 280);
    transform: translateX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-09__line {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — each line owns a view() timeline restricted to a focal band via animation-range: contain 20% contain 55%; color and opacity bloom exactly while the line crosses it. */
```
