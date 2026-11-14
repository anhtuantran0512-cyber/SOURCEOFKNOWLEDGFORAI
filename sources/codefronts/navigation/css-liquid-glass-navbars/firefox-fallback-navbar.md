---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/firefox-fallback-navbar/"
title: "Firefox Fallback Navbar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A liquid-glass navbar engineered to degrade gracefully where advanced glass isn't available."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Firefox Fallback Navbar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/firefox-fallback-navbar/

A liquid-glass navbar engineered to degrade gracefully where advanced glass isn't available. @supports feature queries layer three tiers: full backdrop-filter + SVG refraction for Chrome/Safari, a plain backdrop-blur tier, and a hand-tuned opaque-tint fallback (with a faux frosted gradient) for Firefox builds without backdrop-filter — so it never looks broken.
## HTML
```html
<section class="nb-19" aria-label="Firefox fallback glass navbar demo">
  <nav class="nb-19__bar" aria-label="Primary">
    <span class="nb-19__brand">⛬ Resilient</span>
    <div class="nb-19__links">
      <a class="nb-19__link" href="#nb-19" aria-current="page">Home</a>
      <a class="nb-19__link" href="#nb-19">Support</a>
      <a class="nb-19__link" href="#nb-19">Status</a>
    </div>
    <span class="nb-19__tier" aria-hidden="true">fallback tier</span>
  </nav>
</section>
```
## CSS
```css
.nb-19,
.nb-19 *,
.nb-19 *::before,
.nb-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-19 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(120deg,#134e5e,#71b280);
}
/* Base tier — opaque frosted fallback (Firefox w/o backdrop-filter) */

.nb-19__bar {
  display: flex;
  align-items: center;
  gap: 20px;
  width: min(720px,100%);
  padding: 14px 18px;
  border-radius: 16px;
  color: #fff;
  background: linear-gradient(180deg,rgba(30,50,55,.92),rgba(20,38,42,.96));
  border: 1px solid rgba(255,255,255,.22);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35),0 16px 38px -22px rgba(0,0,0,.6);
}
/* Enhanced tier — real backdrop-filter frost */

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .nb-19__bar {
    background: color-mix(in oklab,white 12%,transparent);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
  }

  .nb-19__tier::after {
    content: "backdrop-filter tier";
  }

  .nb-19__tier {
    font-size: 0;
  }
}

.nb-19__tier::after {
  font-size: 11px;
}

.nb-19__brand {
  font-size: 16px;
  font-weight: 800;
}

.nb-19__links {
  display: flex;
  gap: 4px;
  margin-inline-start: auto;
}

.nb-19__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 10px;
  text-decoration: none;
  color: rgba(255,255,255,.86);
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s;
}

.nb-19__link:hover,
.nb-19__link[aria-current] {
  color: #fff;
  background: rgba(255,255,255,.16);
}

.nb-19__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-19__tier {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: rgba(255,255,255,.6);
}
```

## JavaScript
```js
/* No JavaScript — @supports feature queries tier the design: an opaque frosted base (Firefox fallback) upgrades to real backdrop-filter frost where supported. Author the fallback first, then enhance. */
```
