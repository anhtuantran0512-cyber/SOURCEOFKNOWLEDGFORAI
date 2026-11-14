---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/marker-highlighter/"
title: "CSS Highlighter / Marker Text Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Hover-activated highlighter pen for editorial sites: a clean swipe that paints across the phrase, a hand-wobbled marker blob with rotated, uneven edges (pure…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Highlighter / Marker Text Hover Effect
Source: https://codefronts.com/motion/css-link-effects/marker-highlighter/

Hover-activated highlighter pen for editorial sites: a clean swipe that paints across the phrase, a hand-wobbled marker blob with rotated, uneven edges (pure border-radius mischief — no images), and an underline that inks upward until it floods into a full highlight. Warm, tactile, and multi-line honest — the swipe variant wraps correctly with box-decoration-break.
## HTML
```html
<section class="cle-17" aria-label="Highlighter hover demo">
  <div class="cle-17__stage">
    <p class="cle-17__prose">Annotate as you read: the committee's findings on <a href="#a" class="cle-17__swipe">rural broadband coverage</a> contradict last year's audit, and the appendix quietly concedes that <a href="#b" class="cle-17__blob">the original estimates</a> were, in the auditor's own words, <a href="#c" class="cle-17__flood">optimistic beyond defense</a>.</p>
    <div class="cle-17__legend"><small class="cle-17__cap">A · clean swipe</small><small class="cle-17__cap">B · wobbly marker blob</small><small class="cle-17__cap">C · underline floods up</small></div>
  </div>
</section>
```
## CSS
```css
.cle-17,
.cle-17 *,
.cle-17 *::before,
.cle-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-17 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.3 0.02 80);
  --hl: oklch(0.9 0.17 100 / .7);
  --hl2: oklch(0.85 0.14 60 / .65);
  font-family: Georgia,'Times New Roman',serif;
}

.cle-17__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 40px;
  border: 1px solid oklch(0.9 0.02 90);
  background: linear-gradient(175deg,oklch(0.99 0.008 95),oklch(0.96 0.015 85));
  padding: 44px 36px;
  color: var(--ink);
}

.cle-17__prose {
  max-width: 54ch;
  font-size: 20px;
  line-height: 1.9;
  text-wrap: pretty;
}

.cle-17__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 32px;
}

.cle-17__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-17 a {
  color: var(--ink);
  text-decoration: none;
  font-weight: 600;
  transition: color .35s;
}

.cle-17 a:focus-visible {
  outline: 2px solid oklch(0.6 0.15 90);
  outline-offset: 3px;
  border-radius: 2px;
}

.cle-17__swipe {
  background: linear-gradient(var(--hl),var(--hl)) no-repeat 0 88% / 0% 82%;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
  transition: background-size .4s cubic-bezier(.3,.8,.2,1),color .35s;
}

.cle-17__swipe:hover,
.cle-17__swipe:focus-visible {
  background-size: 100% 82%;
  color: oklch(0.25 0.03 80);
}

.cle-17__blob {
  position: relative;
  isolation: isolate;
}

.cle-17__blob::before {
  content: "";
  position: absolute;
  inset: -.08em -.3em;
  z-index: -1;
  background: var(--hl2);
  border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
  rotate: -1.5deg;
  transform-origin: left center;
  scale: 0 1;
  transition: scale .35s cubic-bezier(.3,.9,.3,1);
}

.cle-17__blob:hover::before,
.cle-17__blob:focus-visible::before {
  scale: 1 1;
}

.cle-17__blob:hover,
.cle-17__blob:focus-visible {
  color: oklch(0.25 0.03 80);
}

.cle-17__flood {
  background: linear-gradient(oklch(0.87 0.16 100 / .75),oklch(0.87 0.16 100 / .75)) no-repeat 0 100% / 100% 3px;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
  transition: background-size .35s cubic-bezier(.3,.8,.2,1),color .35s;
}

.cle-17__flood:hover,
.cle-17__flood:focus-visible {
  background-size: 100% 85%;
  color: oklch(0.25 0.03 80);
}

@media (prefers-reduced-motion: reduce) {
  .cle-17 * {
    transition-duration: .01s !important;
  }
}
```
