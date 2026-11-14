---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/high-contrast-accessible-navbar/"
title: "High-Contrast Accessible Navbar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A liquid-glass navbar that refuses to trade beauty for accessibility."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: High-Contrast Accessible Navbar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/high-contrast-accessible-navbar/

A liquid-glass navbar that refuses to trade beauty for accessibility. It layers a solid contrast scrim under the text, dual specular borders for physical edge definition, tuned text-shadows and a bold :focus-visible ring — so it passes WCAG 2.2 AA (4.5:1 body / 3:1 large) even over a bright, busy background. It also honours forced-colors mode.
## HTML
```html
<section class="nb-20" aria-label="High contrast accessible glass navbar demo">
  <nav class="nb-20__bar" aria-label="Primary">
    <span class="nb-20__brand">◆ Access</span>
    <div class="nb-20__links">
      <a class="nb-20__link" href="#nb-20" aria-current="page">Home</a>
      <a class="nb-20__link" href="#nb-20">Guides</a>
      <a class="nb-20__link" href="#nb-20">Tools</a>
      <a class="nb-20__link" href="#nb-20">Contact</a>
    </div>
    <button class="nb-20__cta" type="button">Get help</button>
  </nav>
</section>
```
## CSS
```css
.nb-20,
.nb-20 *,
.nb-20 *::before,
.nb-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-20 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(120deg,#f7971e,#ffd200 60%,#f7f7f7),url('https://picsum.photos/seed/nb20bright/1000/700') center/cover;
  background-blend-mode: overlay;
}

.nb-20__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: 20px;
  width: min(760px,100%);
  padding: 14px 18px;
  border-radius: 16px;
  color: #fff;
  background: rgba(18,20,28,.66);
  border: 1px solid rgba(255,255,255,.5);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),inset 0 0 0 1px rgba(0,0,0,.25),0 18px 40px -22px rgba(0,0,0,.7);
  backdrop-filter: blur(16px) saturate(150%);
  -webkit-backdrop-filter: blur(16px) saturate(150%);
}

.nb-20__brand {
  font-size: 16px;
  font-weight: 800;
  text-shadow: 0 1px 2px rgba(0,0,0,.6);
}

.nb-20__links {
  display: flex;
  gap: 4px;
  margin-inline-start: auto;
}

.nb-20__link {
  min-height: 44px;
  display: flex;
  align-items: center;
  padding: 0 15px;
  border-radius: 10px;
  text-decoration: none;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  text-shadow: 0 1px 2px rgba(0,0,0,.55);
  transition: background .2s;
}

.nb-20__link:hover {
  background: rgba(255,255,255,.18);
}

.nb-20__link[aria-current] {
  background: rgba(255,255,255,.24);
  text-decoration: underline;
  text-underline-offset: 4px;
}

.nb-20__link:focus-visible,
.nb-20__cta:focus-visible {
  outline: 4px solid #ffe000;
  outline-offset: 2px;
  border-radius: 10px;
}

.nb-20__cta {
  min-height: 44px;
  padding: 0 18px;
  border-radius: 10px;
  border: 2px solid #fff;
  background: #fff;
  color: #101018;
  font-size: 15px;
  font-weight: 800;
  cursor: pointer;
}

@media (forced-colors: active) {
  .nb-20__bar {
    background: Canvas;
    border-color: CanvasText;
  }

  .nb-20__link {
    color: LinkText;
  }

  .nb-20__cta {
    background: ButtonFace;
    color: ButtonText;
    border-color: ButtonText;
  }
}

@media (prefers-contrast: more) {
  .nb-20__bar {
    background: rgba(10,10,16,.9);
  }
}
```

## JavaScript
```js
/* No JavaScript — a solid contrast scrim under the frost guarantees WCAG AA over bright backgrounds; dual borders define the glass edge; a 4px :focus-visible ring plus forced-colors + prefers-contrast blocks cover accessibility modes. */
```
