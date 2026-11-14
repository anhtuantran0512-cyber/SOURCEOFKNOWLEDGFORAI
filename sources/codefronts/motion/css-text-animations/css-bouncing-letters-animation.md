---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-bouncing-letters-animation/"
title: "CSS Text Hover Underline Stretch Animation"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "The two production-grade underline systems: a directional scaleX rule that enters left and exits right on a real glass navbar, and the single-property…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Hover Underline Stretch Animation
Source: https://codefronts.com/motion/css-text-animations/css-bouncing-letters-animation/

The two production-grade underline systems: a directional scaleX rule that enters left and exits right on a real glass navbar, and the single-property background-size gradient underline that survives multi-line wrapping — plus a marker-highlight modifier.
## HTML
```html
<div class="cat-14-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-14a" aria-label="Navbar underline stretch hover">
  <nav class="cat-14a__nav" aria-label="Demo navigation">
    <span class="cat-14a__logo" aria-hidden="true">◆ studio</span>
    <ul class="cat-14a__links">
      <li><a href="#" aria-current="page">Work</a></li>
      <li><a href="#">Studio</a></li>
      <li><a href="#">Journal</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
  <p class="cat-14a__hint" aria-hidden="true">enters from the left · exits to the right — transform-origin swap</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="cat-14b" aria-label="Multi-line gradient underline hover">
  <article class="cat-14b__card">
    <p class="cat-14b__eyebrow">From the journal</p>
    <p class="cat-14b__prose">Good hover states are honest. <a class="cat-14b__link" href="#">This underline is a background gradient stretching from zero to full width</a>, so it flows across line wraps — and the same declaration, fattened, becomes <a class="cat-14b__link cat-14b__link--mark" href="#">a marker highlight</a>.</p>
  </article>
</section>
</div>
```
## CSS
```css
.cat-14-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-14-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-14a,
.cat-14a *,
.cat-14a *::before,
.cat-14a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-14a {
  --accent: oklch(0.84 0.16 165);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#131722,#0a0d14);
}

.cat-14a__nav {
  display: flex;
  align-items: center;
  gap: clamp(24px,6vw,72px);
  padding: 18px 30px;
  border-radius: 18px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.08);
  backdrop-filter: blur(12px);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-14a__logo {
  font-weight: 700;
  color: #eef3fc;
  letter-spacing: .02em;
}

.cat-14a__links {
  display: flex;
  gap: clamp(16px,3.4vw,38px);
  list-style: none;
}

.cat-14a__links a {
  position: relative;
  display: inline-block;
  padding: 6px 2px;
  font-size: 15px;
  font-weight: 500;
  color: rgba(225,235,250,.72);
  text-decoration: none;
  transition: color .3s;
}

.cat-14a__links a::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2px;
  border-radius: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: right;
  transition: transform .35s cubic-bezier(.2,.8,.2,1);
}

.cat-14a__links a:hover,
.cat-14a__links a:focus-visible {
  color: #fff;
}

.cat-14a__links a:hover::after,
.cat-14a__links a:focus-visible::after {
  transform: scaleX(1);
  transform-origin: left;
}

.cat-14a__links a[aria-current="page"] {
  color: #fff;
}

.cat-14a__links a[aria-current="page"]::after {
  transform: scaleX(1);
}

.cat-14a__links a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
  border-radius: 4px;
}

.cat-14a__hint {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .14em;
  color: rgba(170,190,225,.38);
}

@media (prefers-reduced-motion: reduce) {
  .cat-14a__links a::after {
    transition: none;
  }
}

.cat-14b,
.cat-14b *,
.cat-14b *::before,
.cat-14b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-14b {
  --ink: #211c16;
  --accent: oklch(0.62 0.15 40);
  --mark: oklch(0.88 0.16 95);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f5efe4;
  font-family: 'Playfair Display',Georgia,serif;
}

.cat-14b__card {
  max-width: 560px;
  background: #fffdf8;
  border: 1px solid rgba(33,28,22,.1);
  border-radius: 18px;
  padding: 42px 44px;
  box-shadow: 0 24px 60px -30px rgba(60,45,20,.35);
}

.cat-14b__eyebrow {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: rgba(33,28,22,.45);
  margin-bottom: 16px;
}

.cat-14b__prose {
  font-size: clamp(19px,2.6vw,24px);
  line-height: 1.66;
  color: var(--ink);
}

.cat-14b__link {
  color: inherit;
  text-decoration: none;
  background-image: linear-gradient(var(--accent),var(--accent));
  background-repeat: no-repeat;
  background-position: 0 100%;
  background-size: 0% 2px;
  transition: background-size .45s cubic-bezier(.2,.8,.2,1),color .3s;
}

.cat-14b__link:hover,
.cat-14b__link:focus-visible {
  background-size: 100% 2px;
  color: var(--accent);
}

.cat-14b__link--mark {
  background-image: linear-gradient(color-mix(in oklab,var(--mark) 70%,transparent),color-mix(in oklab,var(--mark) 70%,transparent));
  background-size: 0% 42%;
  transition: background-size .45s cubic-bezier(.2,.8,.2,1);
}

.cat-14b__link--mark:hover,
.cat-14b__link--mark:focus-visible {
  background-size: 100% 42%;
  color: var(--ink);
}

.cat-14b__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cat-14b__link,
    .cat-14b__link--mark {
    transition: color .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the rest state parks transform-origin on the right, hover swaps it to the left, so one scaleX transition wipes in and out directionally. */

/* No JavaScript — the underline is a background gradient animating background-size 0%→100%; backgrounds slice across wrapped lines, so it works on paragraphs. */
```
