---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-hover-reveal-gradient-text-effect/"
title: "CSS Hover Reveal Gradient Text Effect"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Each line of text sits in a muted grey state until hovered, triggering a smooth transition that unveils a distinct gradient per line using…"
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hover Reveal Gradient Text Effect
Source: https://codefronts.com/design-styles/css-gradient-text/css-hover-reveal-gradient-text-effect/

Each line of text sits in a muted grey state until hovered, triggering a smooth transition that unveils a distinct gradient per line using -webkit-text-fill-color toggling.
## HTML
```html
<div class="gt-13">
  <span class="gt-13__label">Hover to reveal gradient</span>
  <span class="gt-13__hint">↓ mouse over each line ↓</span>
  <div class="gt-13__line gt-13__line--a">CREATIVITY</div>
  <div class="gt-13__line gt-13__line--b">EXPLORATION</div>
  <div class="gt-13__line gt-13__line--c">INNOVATION</div>
  <div class="gt-13__line gt-13__line--d">EXPRESSION</div>
  <div class="gt-13__line gt-13__line--e">INSPIRATION</div>
  <div class="gt-13__line gt-13__line--f">MOMENTUM</div>
</div>
```
## CSS
```css
.gt-13,
.gt-13 *,
.gt-13 *::before,
.gt-13 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-13 {
  --bg: #0f0f14;
  --plain: #888;
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  padding: 3rem 2rem;
  cursor: default;
}

.gt-13__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #333;
  margin-bottom: 1rem;
}

.gt-13__hint {
  font-size: .75rem;
  letter-spacing: .1em;
  color: #444;
  margin-bottom: 1rem;
}
/* Each line transitions from plain → gradient on hover */

.gt-13__line {
  font-size: clamp(2.5rem, 9vw, 6rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -.01em;
  position: relative;
  display: inline-block;
  cursor: pointer;
  /* Plain state */
  color: var(--plain);
  transition: color .4s ease;
  /* Gradient hidden under colour */
  background: linear-gradient(90deg, #f093fb, #f5576c, #fda085);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
}

.gt-13__line:hover {
  -webkit-text-fill-color: transparent;
  color: transparent;
  background-position: 100% center;
  transition: background-position .6s ease, color .1s;
  animation: gt-13-flow .6s ease forwards;
}

.gt-13__line--b {
  background-image: linear-gradient(90deg, #43e97b, #38f9d7, #4facfe);
}

.gt-13__line--c {
  background-image: linear-gradient(90deg, #fa709a, #fee140, #a18cd1);
}

.gt-13__line--d {
  background-image: linear-gradient(90deg, #30cfd0, #330867, #e0c3fc);
}

.gt-13__line--e {
  background-image: linear-gradient(90deg, #ff9a9e, #fecfef, #ffecd2);
}

.gt-13__line--f {
  background-image: linear-gradient(90deg, #a1c4fd, #c2e9fb, #d4fc79);
}

@keyframes gt-13-flow {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 100% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-13__line:hover {
    animation: none;
    background-position: 0% center;
  }
}
```
