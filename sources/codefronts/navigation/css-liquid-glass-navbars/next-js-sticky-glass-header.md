---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/next-js-sticky-glass-header/"
title: "Next.js Sticky Glass Header"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A performance-first sticky header engineered for Next.js / SSR: it renders its final glass state on the server (no un-styled flash of a transparent bar),…"
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Next.js Sticky Glass Header
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/next-js-sticky-glass-header/

A performance-first sticky header engineered for Next.js / SSR: it renders its final glass state on the server (no un-styled flash of a transparent bar), then progressively enhances with a scroll flag that deepens the frost and shadow once you leave the hero. Zero layout shift, no hydration flicker.
## HTML
```html
<section class="nb-09" aria-label="Next.js sticky glass header demo">
  <div class="nb-09__scroll" id="nb-09-scroll">
    <header class="nb-09__bar" id="nb-09-bar" data-scrolled="false">
      <a class="nb-09__brand" href="#nb-09">▲ next-glass</a>
      <nav class="nb-09__nav" aria-label="Primary">
        <a class="nb-09__link" href="#nb-09" aria-current="page">Home</a>
        <a class="nb-09__link" href="#nb-09">Showcase</a>
        <a class="nb-09__link" href="#nb-09">Docs</a>
      </nav>
      <button class="nb-09__cta" type="button">Deploy</button>
    </header>
    <div class="nb-09__hero"><h2 class="nb-09__ht">Scroll — the header deepens</h2></div>
    <p class="nb-09__p">Server-rendered glass state means no flash of an unstyled transparent bar on hydration. The initial HTML already ships with the light glass tint applied, so the first frame the browser paints matches the final render.</p>
    <p class="nb-09__p">Past the hero the frost, tint and shadow intensify via a single <code>data-scrolled</code> attribute set by a tiny scroll handler. All the visual weight comes from CSS.</p>
    <p class="nb-09__p">In Next.js, the header is a Client Component wrapping just the scroll flag — the markup is server-rendered so search crawlers and reduced-JS browsers see the same header the hydrated JS build produces.</p>
    <p class="nb-09__p"><code>position:sticky</code> keeps CLS at 0 — the header reserves its box before scroll begins, so nothing shifts when the tint deepens on scroll past 120px.</p>
    <p class="nb-09__p">The scroll handler uses <code>requestAnimationFrame</code> throttling so the attribute write stays under 16ms per frame — INP-friendly even on mid-tier Android.</p>
    <p class="nb-09__p">Now try scrolling back up. Once <code>scrollTop &lt; 120</code>, <code>data-scrolled</code> flips back to false and the header returns to its light glass state — no jarring snap, all CSS transitions.</p>
    <p class="nb-09__p">The transition targets <code>background</code>, <code>backdrop-filter</code>, <code>box-shadow</code>, and <code>border-color</code> — everything the eye reads as "deeper glass". No layout properties, no INP hits.</p>
    <p class="nb-09__p">Change the 120px threshold in the JS to match your actual hero height, or bind <code>data-scrolled</code> to an IntersectionObserver on the hero element for a pixel-exact transition point.</p>
    <p class="nb-09__p">That's the whole recipe. One attribute, two states, four CSS transitions, zero flash on hydration.</p>
  </div>
</section>
```
## CSS
```css
.nb-09,
.nb-09 *,
.nb-09 *::before,
.nb-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-09 {
  --accent: oklch(0.55 0 0);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0b0b10;
}

.nb-09__bar {
  position: sticky;
  top: 0;
  z-index: 6;
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 14px 20px;
  color: #fff;
  background: rgba(20,20,28,.35);
  border-bottom: 1px solid rgba(255,255,255,.08);
  backdrop-filter: blur(10px) saturate(140%);
  -webkit-backdrop-filter: blur(10px) saturate(140%);
  box-shadow: 0 0 0 rgba(0,0,0,0);
  transition: background .3s,backdrop-filter .3s,box-shadow .3s,border-color .3s;
}

.nb-09__bar[data-scrolled="true"] {
  background: rgba(14,14,20,.72);
  border-color: rgba(255,255,255,.14);
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  box-shadow: 0 14px 34px -20px rgba(0,0,0,.8);
}

.nb-09__brand {
  font-size: 16px;
  font-weight: 800;
  text-decoration: none;
  color: #fff;
}

.nb-09__nav {
  display: flex;
  gap: 2px;
  margin-inline-start: auto;
}

.nb-09__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 10px;
  text-decoration: none;
  color: rgba(255,255,255,.78);
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,color .2s;
}

.nb-09__link:hover,
.nb-09__link[aria-current] {
  color: #fff;
  background: rgba(255,255,255,.1);
}

.nb-09__link:focus-visible,
.nb-09__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-09__cta {
  min-height: 40px;
  padding: 0 18px;
  border-radius: 10px;
  border: 0;
  background: #fff;
  color: #0b0b10;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
}

.nb-09__scroll {
  position: absolute;
  inset: 0;
  overflow-y: auto;
}

.nb-09__hero {
  height: 300px;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 50% 30%,#2a2350,#0b0b10 70%);
}

.nb-09__ht {
  color: #fff;
  font-size: 24px;
  font-weight: 800;
  text-align: center;
  padding: 0 20px;
}

.nb-09__p {
  color: rgba(255,255,255,.82);
  font-size: 15px;
  line-height: 1.7;
  max-width: 46ch;
  padding: 24px 24px;
  margin: 0 auto;
}

@media (prefers-reduced-motion: reduce) {
  .nb-09__bar {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const scroll = document.querySelector('#nb-09-scroll');
  const bar = document.querySelector('#nb-09-bar');
  if (!scroll || !bar) return;
  let ticking = false;
  scroll.addEventListener('scroll', () => {
    if (ticking) return; ticking = true;
    requestAnimationFrame(() => {
      bar.dataset.scrolled = String(scroll.scrollTop > 120);
      ticking = false;
    });
  }, { passive: true });
})();
```
