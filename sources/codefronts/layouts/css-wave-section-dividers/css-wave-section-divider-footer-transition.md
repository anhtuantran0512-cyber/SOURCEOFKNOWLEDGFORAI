---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/css-wave-section-divider-footer-transition/"
title: "CSS wave section divider footer transition"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "The seamless hand-off into a dark footer: a curved cutout at the top of the footer scoops the page content into it, so the footer feels like the bottom of a…"
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS wave section divider footer transition
Source: https://codefronts.com/layouts/css-wave-section-dividers/css-wave-section-divider-footer-transition/

The seamless hand-off into a dark footer: a curved cutout at the top of the footer scoops the page content into it, so the footer feels like the bottom of a single continuous surface instead of a bolted-on slab.
## HTML
```html
<div class="wsd-05-group">
<section class="wsd-05a">
  <div class="wsd-05a__page"><p class="wsd-05a__copy">Last content section of the page.</p></div>
  <footer class="wsd-05a__footer">
    <svg class="wsd-05a__wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,64 C240,120 480,8 720,40 C960,72 1200,120 1440,72 L1440,0 L0,0 Z"></path>
    </svg>
    <nav class="wsd-05a__cols" aria-label="Footer">
      <div><h3 class="wsd-05a__h">Product</h3><a href="#0">Features</a><a href="#0">Pricing</a><a href="#0">Changelog</a></div>
      <div><h3 class="wsd-05a__h">Resources</h3><a href="#0">Docs</a><a href="#0">Snippets</a><a href="#0">Support</a></div>
      <div><h3 class="wsd-05a__h">Company</h3><a href="#0">About</a><a href="#0">Careers</a><a href="#0">Contact</a></div>
    </nav>
    <p class="wsd-05a__fine">© 2027 codefronts.com — wave divider snippets.</p>
  </footer>
</section>
<section class="wsd-05b">
  <div class="wsd-05b__page"><p class="wsd-05b__copy">Newsletter, testimonials, whatever sits above your footer.</p></div>
  <footer class="wsd-05b__footer">
    <p class="wsd-05b__brand">codefronts</p>
    <p class="wsd-05b__fine">Scallops read friendlier than a single deep curve — good for consumer and education sites.</p>
  </footer>
</section>
</div>
```
## CSS
```css
.wsd-05-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-05-group > section {
  width: 100%;
}

.wsd-05a,
.wsd-05a *,
.wsd-05a *::before,
.wsd-05a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-05a {
  --page: oklch(0.96 0.01 250);
  --footer: oklch(0.2 0.03 250);
  --accent: oklch(0.78 0.14 180);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-05a__page {
  background: var(--page);
  color: oklch(0.34 0.03 250);
  padding: 56px 24px 40px;
  text-align: center;
}

.wsd-05a__copy {
  font-size: 15px;
  opacity: .72;
}

.wsd-05a__footer {
  position: relative;
  overflow: hidden;
  background: var(--footer);
  color: #fff;
  padding: clamp(100px,14vw,160px) 24px 30px;
}

.wsd-05a__wave {
  position: absolute;
  left: 0;
  right: 0;
  top: -1px;
  display: block;
  width: 100%;
  height: clamp(56px,9vw,110px);
  color: var(--page);
  pointer-events: none;
}

.wsd-05a__wave path {
  fill: currentColor;
}

.wsd-05a__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(140px,1fr));
  gap: 26px;
  max-width: 760px;
  margin: 0 auto;
}

.wsd-05a__cols div {
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.wsd-05a__h {
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.wsd-05a__cols a {
  font-size: 14.5px;
  color: rgba(255,255,255,.86);
  text-decoration: none;
  width: fit-content;
}

.wsd-05a__cols a:hover {
  color: #fff;
  text-decoration: underline;
  text-underline-offset: 4px;
}

.wsd-05a__cols a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 3px;
}

.wsd-05a__fine {
  margin-top: 30px;
  text-align: center;
  font-size: 12.5px;
  color: rgba(255,255,255,.6);
}

.wsd-05b,
.wsd-05b *,
.wsd-05b *::before,
.wsd-05b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-05b {
  --page: oklch(0.97 0.02 60);
  --footer: oklch(0.26 0.06 22);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-05b__page {
  background: var(--page);
  color: oklch(0.34 0.05 30);
  padding: 54px 24px 34px;
  text-align: center;
}

.wsd-05b__copy {
  font-size: 15px;
  opacity: .74;
}

.wsd-05b__footer {
  position: relative;
  background: var(--footer);
  color: #fff;
  padding: 78px 24px 44px;
  text-align: center;
}

.wsd-05b__footer::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: -1px;
  height: 34px;
  background: var(--page);
  -webkit-mask: radial-gradient(28px at 50% 100%,transparent 98%,#000) repeat-x 0 0/56px 34px;
  mask: radial-gradient(28px at 50% 100%,transparent 98%,#000) repeat-x 0 0/56px 34px;
  pointer-events: none;
}

.wsd-05b__brand {
  font-size: clamp(22px,3.4vw,32px);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 8px;
}

.wsd-05b__fine {
  font-size: 14px;
  color: rgba(255,255,255,.72);
  max-width: 52ch;
  margin: 0 auto;
}
```

## JavaScript
```js
/* No JavaScript — the wave is pinned to the footer's top edge and filled with the page colour, so it cuts into the dark footer. */

/* No JavaScript — a repeating radial-gradient mask carves scallops out of a page-coloured strip on the footer's top edge (no SVG at all). */
```
