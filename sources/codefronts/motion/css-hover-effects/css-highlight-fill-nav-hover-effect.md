---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-highlight-fill-nav-hover-effect/"
title: "CSS Highlight Fill Nav Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Navigation links with pill, block, and gradient background fill highlights that animate in on hover — six distinct fill styles."
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Highlight Fill Nav Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-highlight-fill-nav-hover-effect/

Navigation links with pill, block, and gradient background fill highlights that animate in on hover — six distinct fill styles.
## HTML
```html
<div class="hv-26">
  <p class="hv-26__label">Highlight Fill Nav — 6 Styles</p>

  <nav class="hv-26__nav hv-26__nav--pill">
    <a class="hv-26__link" href="#">Explore</a>
    <a class="hv-26__link" href="#">Gallery</a>
    <a class="hv-26__link" href="#">Studio</a>
    <a class="hv-26__link" href="#">Contact</a>
    <span class="hv-26__sub">Pill Fill</span>
  </nav>

  <nav class="hv-26__nav hv-26__nav--block">
    <a class="hv-26__link" href="#">Explore</a>
    <a class="hv-26__link" href="#">Gallery</a>
    <a class="hv-26__link" href="#">Studio</a>
    <a class="hv-26__link" href="#">Contact</a>
    <span class="hv-26__sub">Block Fill</span>
  </nav>

  <nav class="hv-26__nav hv-26__nav--gradient">
    <a class="hv-26__link" href="#">Explore</a>
    <a class="hv-26__link" href="#">Gallery</a>
    <a class="hv-26__link" href="#">Studio</a>
    <a class="hv-26__link" href="#">Contact</a>
    <span class="hv-26__sub">Gradient Fill</span>
  </nav>

  <nav class="hv-26__nav hv-26__nav--slash">
    <a class="hv-26__link" href="#">Explore</a>
    <a class="hv-26__link" href="#">Gallery</a>
    <a class="hv-26__link" href="#">Studio</a>
    <a class="hv-26__link" href="#">Contact</a>
    <span class="hv-26__sub">Slash Clip</span>
  </nav>

  <nav class="hv-26__nav hv-26__nav--spotlight">
    <a class="hv-26__link" href="#">Explore</a>
    <a class="hv-26__link" href="#">Gallery</a>
    <a class="hv-26__link" href="#">Studio</a>
    <a class="hv-26__link" href="#">Contact</a>
    <span class="hv-26__sub">Radial Spotlight</span>
  </nav>

  <nav class="hv-26__nav hv-26__nav--invert">
    <a class="hv-26__link" href="#">Explore</a>
    <a class="hv-26__link" href="#">Gallery</a>
    <a class="hv-26__link" href="#">Studio</a>
    <a class="hv-26__link" href="#">Contact</a>
    <span class="hv-26__sub">Invert Blend</span>
  </nav>
</div>
```
## CSS
```css
.hv-26,
.hv-26 *,
.hv-26 *::before,
.hv-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-26 {
  --hl-bg: #5b4fcf;
  --hl-radius: 6px;
  font-family: system-ui, sans-serif;
  background: #0a0a10;
  padding: 3rem 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 2.6rem;
}

.hv-26__label {
  text-align: center;
  color: #444;
  font-size: .72rem;
  letter-spacing: .15em;
  text-transform: uppercase;
}

.hv-26__nav {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.hv-26__sub {
  margin-left: auto;
  color: #3a3a4a;
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.hv-26__link {
  color: #bbb;
  text-decoration: none;
  font-size: .95rem;
  font-weight: 500;
  position: relative;
  padding: .3rem .75rem;
  z-index: 0;
  transition: color .25s;
}

.hv-26__link::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: var(--hl-radius);
  transition: transform .3s cubic-bezier(.4,0,.2,1), opacity .3s;
}
/* ── 1. Pill Fill ── */

.hv-26__nav--pill .hv-26__link {
  --hl-radius: 99px;
}

.hv-26__nav--pill .hv-26__link::before {
  background: var(--hl-bg);
  transform: scaleX(.1) scaleY(.4);
  opacity: 0;
}

.hv-26__nav--pill .hv-26__link:hover {
  color: #fff;
}

.hv-26__nav--pill .hv-26__link:hover::before {
  transform: scaleX(1) scaleY(1);
  opacity: 1;
}
/* ── 2. Block Fill (slide up) ── */

.hv-26__nav--block .hv-26__link::before {
  background: var(--hl-bg);
  transform: scaleY(0);
  transform-origin: bottom;
  border-radius: 4px;
}

.hv-26__nav--block .hv-26__link:hover {
  color: #fff;
}

.hv-26__nav--block .hv-26__link:hover::before {
  transform: scaleY(1);
}
/* ── 3. Gradient Fill ── */

.hv-26__nav--gradient .hv-26__link::before {
  background: linear-gradient(135deg, #7c6af7, #f764a8);
  transform: scaleX(0);
  transform-origin: left;
  border-radius: 6px;
  opacity: .9;
}

.hv-26__nav--gradient .hv-26__link:hover {
  color: #fff;
}

.hv-26__nav--gradient .hv-26__link:hover::before {
  transform: scaleX(1);
}
/* ── 4. Slash Clip ── */

.hv-26__nav--slash .hv-26__link::before {
  background: #e8c840;
  clip-path: polygon(8% 0%, 100% 0%, 92% 100%, 0% 100%);
  transform: scaleX(0);
  transform-origin: left;
  border-radius: 0;
}

.hv-26__nav--slash .hv-26__link:hover {
  color: #111;
}

.hv-26__nav--slash .hv-26__link:hover::before {
  transform: scaleX(1);
}
/* ── 5. Radial Spotlight ── */

.hv-26__nav--spotlight .hv-26__link::before {
  background: radial-gradient(ellipse at center, rgba(124,106,247,.7) 0%, transparent 72%);
  transform: scale(0);
  border-radius: 0;
  opacity: 0;
}

.hv-26__nav--spotlight .hv-26__link:hover {
  color: #fff;
}

.hv-26__nav--spotlight .hv-26__link:hover::before {
  transform: scale(2);
  opacity: 1;
}
/* ── 6. Invert Blend ── */

.hv-26__nav--invert {
  isolation: isolate;
}

.hv-26__nav--invert .hv-26__link {
  color: #fff;
  mix-blend-mode: difference;
}

.hv-26__nav--invert .hv-26__link::before {
  background: #fff;
  transform: scaleX(0);
  transform-origin: left;
  border-radius: 4px;
  mix-blend-mode: normal;
}

.hv-26__nav--invert .hv-26__link:hover::before {
  transform: scaleX(1);
}

@media (prefers-reduced-motion: reduce) {
  .hv-26__link::before {
    transition: none !important;
  }
}
```
