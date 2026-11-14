---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/gradient-link-underline-animation/"
title: "Gradient Link Underline Animation"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A readable long-form article block where every link demonstrates a different gradient underline: grow-from-left, center-out bloom, thick highlighter swell,…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Link Underline Animation
Source: https://codefronts.com/design-styles/css-gradient-ui/gradient-link-underline-animation/

A readable long-form article block where every link demonstrates a different gradient underline: grow-from-left, center-out bloom, thick highlighter swell, and a nav row with a sliding shared underline — the patterns that replaced text-decoration.
## HTML
```html
<div class="cgu-14-group">
<section class="cgu-14" aria-label="Gradient link underline animation demos">
  <div class="cgu-14__inner">
    <nav class="cgu-14__nav" aria-label="Article sections">
      <a class="cgu-14__navlink" href="#specimens">Specimens</a>
      <a class="cgu-14__navlink" href="#foundries">Foundries</a>
      <a class="cgu-14__navlink" href="#licensing">Licensing</a>
      <a class="cgu-14__navlink" href="#colophon">Colophon</a>
    </nav>
    <article class="cgu-14__article">
      <p class="cgu-14__eyebrow">14 · Gradient underlines</p>
      <h2 class="cgu-14__title">Underlines that behave like ink</h2>
      <p class="cgu-14__p">The humble underline is a link's handshake. A <a class="cgu-14__link cgu-14__link--grow" href="#grow">grow-from-left line</a> confirms direction the moment the cursor arrives, while a <a class="cgu-14__link cgu-14__link--center" href="#center">center-out bloom</a> feels more like a press than a swipe. When a reference deserves emphasis rather than navigation, a <a class="cgu-14__link cgu-14__link--marker" href="#marker">highlighter swell</a> rises behind the words like a marker stroke — translucent, so the text underneath keeps its contrast.</p>
      <p class="cgu-14__p">Because these lines are painted as backgrounds, they wrap across line breaks with the text itself — try it on this deliberately long <a class="cgu-14__link cgu-14__link--grow" href="#wrap">multi-word link that will almost certainly wrap onto a second line at narrow widths</a> — something a pseudo-element underline can never do.</p>
    </article>
    <p class="cgu-14__foot">Nav above uses the same trick per-link — the "slider" is each link's own background-size, not a moving element.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-14-group {
  display: block;
  width: 100%;
}

.cgu-14,
.cgu-14 *,
.cgu-14 *::before,
.cgu-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-14 {
  --u1: #22d3ee;
  --u2: #e879f9;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: Georgia,'Times New Roman',serif;
  color: #e8e6f0;
  background: linear-gradient(180deg,#100f1a 0%,#0b0a12 100%);
}

.cgu-14__inner {
  width: min(680px,100%);
  display: grid;
  gap: 34px;
}

.cgu-14__nav {
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
  justify-content: center;
  padding-bottom: 18px;
  border-bottom: 1px solid rgba(255,255,255,.1);
}

.cgu-14__navlink {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 13.5px;
  font-weight: 650;
  letter-spacing: .04em;
  color: #b9b6cc;
  text-decoration: none;
  padding-bottom: 6px;
  background: linear-gradient(90deg,var(--u1),var(--u2)) no-repeat center bottom / 0% 2px;
  transition: background-size .35s cubic-bezier(.2,.8,.3,1),color .3s;
}

.cgu-14__navlink:hover,
.cgu-14__navlink:focus-visible {
  color: #fff;
  background-size: 100% 2px;
}

.cgu-14__navlink:focus-visible {
  outline: 2px solid var(--u1);
  outline-offset: 4px;
  border-radius: 4px;
}

.cgu-14__article {
  display: grid;
  gap: 18px;
}

.cgu-14__eyebrow {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #8f8bb0;
}

.cgu-14__title {
  font-size: clamp(30px,5vw,50px);
  font-weight: 750;
  letter-spacing: -.015em;
  line-height: 1.08;
  text-wrap: balance;
}

.cgu-14__p {
  font-size: 17.5px;
  line-height: 1.85;
  color: #c9c6da;
  text-wrap: pretty;
}

.cgu-14__link {
  color: #f2f0fa;
  text-decoration: none;
  padding-bottom: 2px;
}

.cgu-14__link:focus-visible {
  outline: 2px solid var(--u1);
  outline-offset: 3px;
  border-radius: 3px;
}

.cgu-14__link--grow {
  background: linear-gradient(90deg,var(--u1),var(--u2)) no-repeat left bottom / 100% 1px;
  transition: background-size .4s cubic-bezier(.2,.8,.3,1);
}

.cgu-14__link--grow:hover,
.cgu-14__link--grow:focus-visible {
  background-size: 100% 3px;
}

.cgu-14__link--center {
  background: linear-gradient(90deg,#fbbf24,#fb7185) no-repeat center bottom / 12% 2px;
  transition: background-size .4s cubic-bezier(.2,.8,.3,1);
}

.cgu-14__link--center:hover,
.cgu-14__link--center:focus-visible {
  background-size: 100% 2px;
}

.cgu-14__link--marker {
  background: linear-gradient(100deg,rgba(52,211,153,.4),rgba(163,230,53,.4)) no-repeat left bottom / 100% .12em;
  transition: background-size .35s cubic-bezier(.2,.8,.3,1);
}

.cgu-14__link--marker:hover,
.cgu-14__link--marker:focus-visible {
  background-size: 100% .55em;
}

.cgu-14__foot {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 13px;
  color: #8f8bb0;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .cgu-14__navlink,
    .cgu-14__link--grow,
    .cgu-14__link--center,
    .cgu-14__link--marker {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — every underline is a background-image whose background-size animates; backgrounds wrap across line breaks, pseudo-elements can't. */
```
