---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/squiggly-underline/"
title: "CSS Wavy / Squiggly Underline Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Squiggles, three ways: the one-line native route (text-decoration-style: wavy fading in — wraps across lines for free), a marching squiggle that scrolls…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Wavy / Squiggly Underline Hover Effect
Source: https://codefronts.com/motion/css-link-effects/squiggly-underline/

Squiggles, three ways: the one-line native route (text-decoration-style: wavy fading in — wraps across lines for free), a marching squiggle that scrolls under the link for as long as you hover, and a rainbow squiggle that drifts through hues while it marches. The SVG wave is a 200-byte data-URI, no assets.
## HTML
```html
<section class="cle-07" aria-label="Wavy underline hover demo">
  <div class="cle-07__stage">
    <p class="cle-07__prose">Field notes from the print room — <a href="#a" class="cle-07__native">the overprint experiments</a> ran long, but the riso drum forgave us. Next week we ink <a href="#a2" class="cle-07__native">a two-color zine</a>.</p>
    <div class="cle-07__row">
      <div class="cle-07__var"><a href="#b" class="cle-07__march">Marching squiggle</a><small class="cle-07__cap">B · scrolls while hovered</small></div>
      <div class="cle-07__var"><a href="#c" class="cle-07__rainbow">Rainbow drift</a><small class="cle-07__cap">C · march + hue-rotate</small></div>
    </div>
  </div>
</section>
```
## CSS
```css
.cle-07,
.cle-07 *,
.cle-07 *::before,
.cle-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-07 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.3 0.04 340);
  --brand: oklch(0.62 0.19 20);
  font-family: Georgia,'Times New Roman',serif;
}

.cle-07__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 52px;
  border: 1px solid oklch(0.9 0.02 60);
  background: linear-gradient(170deg,oklch(0.98 0.012 75),oklch(0.95 0.02 60));
  padding: 44px 36px;
  color: var(--ink);
}

.cle-07__prose {
  max-width: 52ch;
  font-size: 19px;
  line-height: 1.75;
  text-wrap: pretty;
}

.cle-07__row {
  display: flex;
  flex-wrap: wrap;
  gap: 40px 64px;
  justify-content: center;
}

.cle-07__var {
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cle-07__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.04 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-07 a {
  color: var(--ink);
  text-decoration: none;
  font-weight: 600;
}

.cle-07__row a {
  font-size: 22px;
}

.cle-07 a:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 4px;
  border-radius: 2px;
}

.cle-07__native {
  text-decoration: underline;
  text-decoration-style: wavy;
  text-decoration-color: transparent;
  text-decoration-thickness: 1.5px;
  text-underline-offset: 4px;
  transition: text-decoration-color .35s,text-underline-offset .35s,color .3s;
}

.cle-07__native:hover,
.cle-07__native:focus-visible {
  text-decoration-color: var(--brand);
  text-underline-offset: 5px;
  color: oklch(0.45 0.16 20);
}

.cle-07__march {
  padding-bottom: 9px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 8'%3E%3Cpath d='M0 4 Q5 0 10 4 T20 4' fill='none' stroke='%23d64545' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E") repeat-x 0 100% / 20px 0;
  animation: clh07-march .7s linear infinite;
  transition: background-size .3s;
}

.cle-07__march:hover,
.cle-07__march:focus-visible {
  background-size: 20px 7px;
}

.cle-07__rainbow {
  position: relative;
  padding-bottom: 9px;
}

.cle-07__rainbow::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 7px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 8'%3E%3Cpath d='M0 4 Q5 0 10 4 T20 4' fill='none' stroke='%23d64545' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E") repeat-x 0 50% / 20px 7px;
  opacity: 0;
  translate: 0 -3px;
  transition: opacity .3s,translate .3s;
  animation: clh07-march .7s linear infinite,clh07-hue 2.4s linear infinite;
}

.cle-07__rainbow:hover::after,
.cle-07__rainbow:focus-visible::after {
  opacity: 1;
  translate: 0 0;
}

@keyframes clh07-march {
  to {
    background-position-x: 20px;
  }
}

@keyframes clh07-hue {
  to {
    filter: hue-rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-07 *,
    .cle-07 *::after {
    animation: none !important;
    transition-duration: .01s !important;
  }
}
```
