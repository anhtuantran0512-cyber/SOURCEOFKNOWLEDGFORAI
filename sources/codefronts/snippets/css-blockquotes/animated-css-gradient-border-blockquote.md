---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/animated-css-gradient-border-blockquote/"
title: "Animated CSS Gradient Border Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "A quote card wrapped in a slowly rotating conic-gradient border — the effect every 'top CSS tricks' video promises, done the 2026 way: a registered @property…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated CSS Gradient Border Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/animated-css-gradient-border-blockquote/

A quote card wrapped in a slowly rotating conic-gradient border — the effect every 'top CSS tricks' video promises, done the 2026 way: a registered @property custom property (--bq06-angle) makes the gradient's angle itself animatable, so the colors orbit the card with zero JavaScript and zero pseudo-element hacks. The border is painted by a two-layer background (padding-box fill over border-box gradient), which — unlike outline or box-shadow tricks — respects border-radius perfectly and costs one element.
## HTML
```html
<section class="bq-06" aria-label="Animated gradient border blockquote demo">
  <div class="bq-06__stage">
    <figure class="bq-06__card">
      <blockquote>
        <p>“We shipped the redesign in six weeks. The border animation in this quote card took two of them — and it was worth every hour.”</p>
      </blockquote>
      <figcaption class="bq-06__by">
        <span class="bq-06__dot" aria-hidden="true"></span>
        <span><strong>Marcus Webb</strong> · Design Engineer, Meridian</span>
      </figcaption>
    </figure>
    <p class="bq-06__chip" aria-hidden="true">@property &lt;angle&gt; · conic-gradient border-box · 0 JS</p>
  </div>
</section>
```
## CSS
```css
@property --bq06-angle {
  syntax: '<angle>';
  initial-value: 40deg;
  inherits: false;
}

.bq-06,
.bq-06 *,
.bq-06 *::before,
.bq-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.15 0.012 270);
  --card: oklch(0.2 0.015 270);
  --ink: oklch(0.96 0.008 270);
  --mut: oklch(0.66 0.02 270);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-06__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 55% at 50% 120%,oklch(0.24 0.05 300/.5),transparent),var(--bg);
  overflow-y: auto;
}

.bq-06__card {
  width: min(100%,520px);
  padding: clamp(24px,4vw,36px);
  border: 1.5px solid transparent;
  border-radius: 20px;
  background: linear-gradient(var(--card),var(--card)) padding-box,conic-gradient(from var(--bq06-angle),oklch(0.72 0.17 25),oklch(0.75 0.15 320),oklch(0.7 0.14 250),oklch(0.72 0.17 25)) border-box;
  animation: bq06-spin 7s linear infinite;
  box-shadow: 0 24px 60px oklch(0 0 0/.45);
}

@keyframes bq06-spin {
  to {
    --bq06-angle: 400deg;
  }
}

.bq-06__card blockquote p {
  font-size: clamp(17px,2.2vw,21px);
  line-height: 1.6;
  font-weight: 550;
  letter-spacing: -.01em;
  text-wrap: pretty;
}

.bq-06__by {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 20px;
  font-size: 13.5px;
  color: var(--mut);
}

.bq-06__by strong {
  color: var(--ink);
  font-weight: 650;
}

.bq-06__dot {
  width: 9px;
  height: 9px;
  border-radius: 99px;
  background: conic-gradient(oklch(0.72 0.17 25),oklch(0.75 0.15 320),oklch(0.7 0.14 250),oklch(0.72 0.17 25));
  flex: none;
}

.bq-06__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(1 0 0/.12);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .bq-06 * {
    transition-duration: .01ms !important;
  }

  .bq-06__card {
    animation: none;
  }
}
```
