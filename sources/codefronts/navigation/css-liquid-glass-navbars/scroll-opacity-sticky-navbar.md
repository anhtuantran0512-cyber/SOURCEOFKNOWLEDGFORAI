---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/scroll-opacity-sticky-navbar/"
title: "Scroll Opacity Sticky Navbar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A sticky navbar that starts fully transparent over a hero image — letting the artwork breathe — then progressively fades in its glass tint, blur and border…"
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Opacity Sticky Navbar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/scroll-opacity-sticky-navbar/

A sticky navbar that starts fully transparent over a hero image — letting the artwork breathe — then progressively fades in its glass tint, blur and border as the user scrolls, until it's a solid frosted bar over the content. The opacity is mapped continuously to scroll position, not a hard toggle.
## HTML
```html
<section class="nb-13" aria-label="Scroll opacity sticky navbar demo">
  <div class="nb-13__scroll" id="nb-13-scroll">
    <header class="nb-13__bar" id="nb-13-bar" style="--p:0">
      <a class="nb-13__brand" href="#nb-13">☼ Vista</a>
      <nav class="nb-13__nav" aria-label="Primary">
        <a class="nb-13__link" href="#nb-13" aria-current="page">Stays</a>
        <a class="nb-13__link" href="#nb-13">Trips</a>
        <a class="nb-13__link" href="#nb-13">Guides</a>
      </nav>
      <button class="nb-13__cta" type="button">Book</button>
    </header>
    <div class="nb-13__hero"><h2 class="nb-13__ht">Transparent over the hero</h2></div>
    <p class="nb-13__p">Scroll and the bar fades from fully transparent to a solid frosted glass panel — opacity mapped continuously to scroll position via a <code>--p</code> custom property.</p>
    <p class="nb-13__p">The link text keeps a fading text-shadow so it stays legible the whole way from transparent to frosted.</p>
    <p class="nb-13__p">Fill alpha, blur radius and border opacity all interpolate with <code>color-mix</code> + <code>calc()</code> so the bar dissolves in as one gesture — no jarring class toggle at a breakpoint.</p>
    <p class="nb-13__p">The scroll handler is throttled with <code>requestAnimationFrame</code> so the property write stays under 16ms per frame — INP-friendly on mid-tier mobile.</p>
    <p class="nb-13__p">The bar uses <code>position:sticky</code> so CLS stays at 0 — the header reserves its space in-flow and never pushes content when it changes appearance.</p>
    <p class="nb-13__p">Keep scrolling to see the fully solidified state. The frost, border and background tint all reach 100% around the ~220px mark.</p>
    <p class="nb-13__p">Now scroll back up. The bar dissolves back to fully transparent, revealing the hero image behind it.</p>
    <p class="nb-13__p">Every stage keeps the links legible thanks to a text-shadow that fades in inverse to the frost — full shadow when transparent, no shadow when solid.</p>
    <p class="nb-13__p">Try adjusting the <code>divisor</code> constant in the JS (currently 220) to make the fade happen faster or slower. Higher = slower fade over more scroll distance.</p>
    <p class="nb-13__p">That's the whole demo. One custom property, six lines of JS, zero CSS transitions — the fade is a continuous computed value, not an animation.</p>
  </div>
</section>
```
## CSS
```css
.nb-13,
.nb-13 *,
.nb-13 *::before,
.nb-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-13 {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0c1418;
}

.nb-13__bar {
  position: sticky;
  top: 0;
  z-index: 6;
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 16px 22px;
  color: #fff;
  background: color-mix(in oklab,#0e1a22 calc(var(--p)*82%),transparent);
  border-bottom: 1px solid color-mix(in oklab,white calc(var(--p)*22%),transparent);
  backdrop-filter: blur(calc(var(--p)*22px)) saturate(160%);
  -webkit-backdrop-filter: blur(calc(var(--p)*22px)) saturate(160%);
  text-shadow: 0 2px 10px rgba(0,0,0,calc(.5 - var(--p)*.5));
}

.nb-13__brand {
  font-size: 17px;
  font-weight: 800;
  text-decoration: none;
  color: #fff;
}

.nb-13__nav {
  display: flex;
  gap: 2px;
  margin-inline-start: auto;
}

.nb-13__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 10px;
  text-decoration: none;
  color: #fff;
  opacity: .9;
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,opacity .2s;
}

.nb-13__link:hover,
.nb-13__link[aria-current] {
  opacity: 1;
  background: rgba(255,255,255,.14);
}

.nb-13__link:focus-visible,
.nb-13__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-13__cta {
  min-height: 40px;
  padding: 0 18px;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,.5);
  background: rgba(255,255,255,.18);
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
}

.nb-13__scroll {
  position: absolute;
  inset: 0;
  overflow-y: auto;
}

.nb-13__hero {
  height: 330px;
  background: linear-gradient(180deg,rgba(0,0,0,.15),rgba(0,0,0,.4)),url('https://picsum.photos/seed/nb13/1000/700') center/cover;
  display: grid;
  place-items: center;
}

.nb-13__ht {
  color: #fff;
  font-size: 26px;
  font-weight: 800;
  text-shadow: 0 2px 16px rgba(0,0,0,.5);
  text-align: center;
  padding: 0 20px;
}

.nb-13__p {
  color: #dfe7ec;
  font-size: 15px;
  line-height: 1.7;
  max-width: 46ch;
  padding: 24px;
  margin: 0 auto;
}

@media (prefers-reduced-motion: reduce) {
  .nb-13__bar {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const scroll = document.querySelector('#nb-13-scroll');
  const bar = document.querySelector('#nb-13-bar');
  if (!scroll || !bar) return;
  let ticking = false;
  scroll.addEventListener('scroll', () => {
    if (ticking) return; ticking = true;
    requestAnimationFrame(() => {
      const p = Math.min(1, Math.max(0, scroll.scrollTop / 220));
      bar.style.setProperty('--p', p.toFixed(3));
      ticking = false;
    });
  }, { passive: true });
})();
```
