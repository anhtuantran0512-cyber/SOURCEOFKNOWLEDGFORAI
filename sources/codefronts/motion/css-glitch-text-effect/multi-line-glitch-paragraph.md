---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/multi-line-glitch-paragraph/"
title: "Multi-Line Glitch Paragraph"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "A three-line block-quote where synchronized horizontal slice cuts jump across all lines simultaneously using clip-path bands on pseudo-elements -- no…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Line Glitch Paragraph
Source: https://codefronts.com/motion/css-glitch-text-effect/multi-line-glitch-paragraph/

A three-line block-quote where synchronized horizontal slice cuts jump across all lines simultaneously using clip-path bands on pseudo-elements -- no single-word isolation needed.
## HTML
```html
<div class="gt-09">
  <div class="gt-09__quote-card">
    <p class="gt-09__para" data-text="The signal breaks across every line simultaneously — a synchronized disruption that no single word can contain or predict.">The signal breaks across every line simultaneously — a synchronized disruption that no single word can contain or predict.</p>
    <div class="gt-09__attr">Codefronts, 2027</div>
  </div>
</div>
```
## CSS
```css
.gt-09,
.gt-09 *,
.gt-09 *::before,
.gt-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-09 ::selection {
  background: #4f46e5;
  color: #fff;
}

.gt-09 {
  --indigo: #4f46e5;
  --violet: #7c3aed;
  --pink: #ec4899;
  --bg: #0e0e16;
  --text: #e2e8f0;
  --muted: rgba(226,232,240,0.5);
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  font-family: 'Georgia', serif;
}

.gt-09__quote-card {
  max-width: 540px;
  position: relative;
  padding: 36px 40px;
  border-left: 3px solid var(--indigo);
  background: rgba(79,70,229,0.06);
  border-radius: 0 12px 12px 0;
}
/* Quote mark */

.gt-09__quote-card::before {
  content: '\201C';
  position: absolute;
  top: -12px;
  left: 28px;
  font-size: 80px;
  color: rgba(79,70,229,0.3);
  font-family: Georgia, serif;
  line-height: 1;
}
/* The multi-line glitch paragraph */

.gt-09__para {
  position: relative;
  font-size: clamp(17px, 2.5vw, 22px);
  line-height: 1.65;
  color: var(--text);
  font-style: italic;
  /* Baseline RGB-split on the paragraph itself so every line shows
       chromatic separation at every animation frame, not just during
       the 8% slice-burst window. The pseudo-elements still layer their
       band-displacement slices on top for the active glitch. */
  text-shadow: -1.5px 0 rgba(236,72,153,0.55), 1.5px 0 rgba(6,182,212,0.55);
}
/* Slice A — upper band across all lines simultaneously. Baseline
   opacity 0.55 + 6px constant offset so the slice is always
   visible; the keyframe amplifies the displacement during the
   burst. */

.gt-09__para::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  font-style: italic;
  color: var(--pink);
  clip-path: polygon(0 28%, 100% 28%, 100% 46%, 0 46%);
  opacity: 0.55;
  transform: translateX(-6px);
  animation: gt-09-slice-a 5s steps(1) infinite;
  white-space: pre-wrap;
}
/* Slice B — lower band, same baseline visibility recipe. */

.gt-09__para::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  font-style: italic;
  color: #00e5ff;
  clip-path: polygon(0 58%, 100% 58%, 100% 74%, 0 74%);
  opacity: 0.55;
  transform: translateX(6px);
  animation: gt-09-slice-b 5s steps(1) infinite;
  white-space: pre-wrap;
}

@keyframes gt-09-slice-a {
  0%,
    82%,
    100% {
    opacity: 0.55;
    transform: translateX(-6px);
  }

  84% {
    opacity: 1;
    transform: translateX(-16px);
    clip-path: polygon(0 25%, 100% 25%, 100% 44%, 0 44%);
  }

  86% {
    opacity: 0.9;
    transform: translateX(12px);
    clip-path: polygon(0 30%, 100% 30%, 100% 48%, 0 48%);
  }

  88% {
    opacity: 1;
    transform: translateX(-9px);
    clip-path: polygon(0 27%, 100% 27%, 100% 43%, 0 43%);
  }

  90% {
    opacity: 0.55;
    transform: translateX(-6px);
  }
}

@keyframes gt-09-slice-b {
  0%,
    82%,
    100% {
    opacity: 0.55;
    transform: translateX(6px);
  }

  84% {
    opacity: 1;
    transform: translateX(18px);
    clip-path: polygon(0 56%, 100% 56%, 100% 72%, 0 72%);
  }

  86% {
    opacity: 0.9;
    transform: translateX(-12px);
    clip-path: polygon(0 60%, 100% 60%, 100% 76%, 0 76%);
  }

  88% {
    opacity: 1;
    transform: translateX(10px);
    clip-path: polygon(0 57%, 100% 57%, 100% 73%, 0 73%);
  }

  90% {
    opacity: 0.55;
    transform: translateX(6px);
  }
}

.gt-09__attr {
  margin-top: 20px;
  font-size: 12px;
  letter-spacing: 3px;
  color: var(--muted);
  text-transform: uppercase;
  font-family: 'Inter', system-ui, sans-serif;
  font-style: normal;
}

.gt-09__attr::before {
  content: '— ';
  color: var(--indigo);
}

@media (prefers-reduced-motion: reduce) {
  .gt-09__para::before,
    .gt-09__para::after {
    animation: none;
    opacity: 0;
  }
}
```
