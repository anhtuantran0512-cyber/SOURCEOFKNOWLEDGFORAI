---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/chevron-companion/"
title: "CSS Arrow / Chevron Slide Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Arrows that behave like good typography: a chevron whose column literally doesn't exist until you hover (animating grid-template-columns from 0fr to 1fr —…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Arrow / Chevron Slide Hover Effect
Source: https://codefronts.com/motion/css-link-effects/chevron-companion/

Arrows that behave like good typography: a chevron whose column literally doesn't exist until you hover (animating grid-template-columns from 0fr to 1fr — the modern reveal, no magic paddings), the fly-through arrow that exits right and re-enters left, and the diagonal swap for external links. Built as a link list, the way you'll actually ship it.
## HTML
```html
<section class="cle-11" aria-label="Arrow slide hover demo">
  <div class="cle-11__stage">
    <ul class="cle-11__list">
      <li>
        <a href="#a" class="cle-11__reveal"><span class="cle-11__t">Read the field guide</span><span class="cle-11__arr" aria-hidden="true">→</span></a>
        <small class="cle-11__cap">A · 0fr → 1fr track reveal</small>
      </li>
      <li>
        <a href="#b" class="cle-11__fly"><span class="cle-11__t">Browse all essays</span><span class="cle-11__arr2" aria-hidden="true">→</span></a>
        <small class="cle-11__cap">B · fly through and return</small>
      </li>
      <li>
        <a href="#c" class="cle-11__ext"><span class="cle-11__t">Open the changelog</span><span class="cle-11__box" aria-hidden="true"><span class="cle-11__d1">↗</span><span class="cle-11__d2">↗</span></span></a>
        <small class="cle-11__cap">C · diagonal swap (external)</small>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
.cle-11,
.cle-11 *,
.cle-11 *::before,
.cle-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-11 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.25 0.02 250);
  --brand: oklch(0.55 0.19 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-11__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  border: 1px solid oklch(0.9 0.012 250);
  background: linear-gradient(170deg,oklch(0.98 0.005 250),oklch(0.95 0.014 250));
  padding: 44px 36px;
}

.cle-11__list {
  list-style: none;
  display: grid;
  gap: 34px;
  justify-items: start;
}

.cle-11__list li {
  display: grid;
  gap: 10px;
}

.cle-11__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 250);
}

.cle-11 a {
  color: var(--ink);
  text-decoration: none;
  font-size: 22px;
  font-weight: 650;
  letter-spacing: -.01em;
  transition: color .3s;
}

.cle-11 a:hover,
.cle-11 a:focus-visible {
  color: var(--brand);
}

.cle-11 a:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 5px;
  border-radius: 3px;
}

.cle-11__reveal {
  display: inline-grid;
  grid-template-columns: auto 0fr;
  align-items: baseline;
  gap: 0;
  transition: grid-template-columns .35s cubic-bezier(.3,.9,.3,1),gap .35s,color .3s;
}

.cle-11__reveal .cle-11__arr {
  overflow: hidden;
  min-width: 0;
  translate: -6px 0;
  opacity: 0;
  transition: translate .35s cubic-bezier(.3,1.3,.4,1),opacity .25s;
}

.cle-11__reveal:hover,
.cle-11__reveal:focus-visible {
  grid-template-columns: auto 1fr;
  gap: .5ch;
}

.cle-11__reveal:hover .cle-11__arr,
.cle-11__reveal:focus-visible .cle-11__arr {
  translate: 0 0;
  opacity: 1;
}

.cle-11__fly {
  display: inline-flex;
  align-items: baseline;
  gap: .5ch;
}

.cle-11__fly .cle-11__arr2 {
  display: inline-block;
}

.cle-11__fly:hover .cle-11__arr2,
.cle-11__fly:focus-visible .cle-11__arr2 {
  animation: clh11-fly .5s cubic-bezier(.4,0,.3,1) forwards;
}

@keyframes clh11-fly {
  0% {
    translate: 0 0;
    opacity: 1;
  }

  42% {
    translate: 20px 0;
    opacity: 0;
  }

  43% {
    translate: -16px 0;
    opacity: 0;
  }

  100% {
    translate: 0 0;
    opacity: 1;
  }
}

.cle-11__ext {
  display: inline-flex;
  align-items: baseline;
  gap: .5ch;
}

.cle-11__box {
  position: relative;
  display: inline-block;
  width: 1.05em;
  height: 1.05em;
  overflow: hidden;
}

.cle-11__box span {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  transition: translate .35s cubic-bezier(.35,1.2,.4,1);
}

.cle-11__d2 {
  translate: -105% 105%;
}

.cle-11__ext:hover .cle-11__d1,
.cle-11__ext:focus-visible .cle-11__d1 {
  translate: 105% -105%;
}

.cle-11__ext:hover .cle-11__d2,
.cle-11__ext:focus-visible .cle-11__d2 {
  translate: 0 0;
}

@media (prefers-reduced-motion: reduce) {
  .cle-11 * {
    transition-duration: .01s !important;
    animation: none !important;
  }
}
```
