---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/sliding-capsule-active-tab/"
title: "Sliding Capsule Active Tab"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A segmented glass tab bar where a frosted capsule physically slides behind the selected item — no JavaScript."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Capsule Active Tab
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/sliding-capsule-active-tab/

A segmented glass tab bar where a frosted capsule physically slides behind the selected item — no JavaScript. Native radio inputs hold the state and modern CSS :has() reads which is checked to translate the capsule, so the active highlight glides between tabs on a spring.
## HTML
```html
<section class="nb-17" aria-label="Sliding capsule active tab demo">
  <div class="nb-17__bar" role="tablist" aria-label="Views">
    <span class="nb-17__cap" aria-hidden="true"></span>
    <input class="nb-17__r" type="radio" name="nb-17" id="nb-17-1" checked>
    <label class="nb-17__tab" for="nb-17-1">Day</label>
    <input class="nb-17__r" type="radio" name="nb-17" id="nb-17-2">
    <label class="nb-17__tab" for="nb-17-2">Week</label>
    <input class="nb-17__r" type="radio" name="nb-17" id="nb-17-3">
    <label class="nb-17__tab" for="nb-17-3">Month</label>
    <input class="nb-17__r" type="radio" name="nb-17" id="nb-17-4">
    <label class="nb-17__tab" for="nb-17-4">Year</label>
  </div>
</section>
```
## CSS
```css
.nb-17,
.nb-17 *,
.nb-17 *::before,
.nb-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-17 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 200deg at 50% 50%,#00c2ff,#8e2de2,#ff6a88,#00c2ff);
  background-size: 200% 200%;
  animation: nb-17-bg 20s ease-in-out infinite;
}

@keyframes nb-17-bg {
  50% {
    background-position: 100% 100%;
  }
}

.nb-17__bar {
  position: relative;
  display: flex;
  padding: 7px;
  border-radius: 9999px;
  isolation: isolate;
  background: color-mix(in oklab,white 14%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 20px 44px -24px rgba(0,0,0,.55);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.nb-17__cap {
  position: absolute;
  top: 7px;
  bottom: 7px;
  left: 7px;
  width: 86px;
  border-radius: 9999px;
  background: rgba(255,255,255,.26);
  border: 1px solid rgba(255,255,255,.55);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.7);
  z-index: 0;
  transition: transform .45s cubic-bezier(.34,1.56,.5,1);
}

.nb-17__r {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.nb-17__tab {
  position: relative;
  z-index: 1;
  width: 86px;
  min-height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 9999px;
  cursor: pointer;
  color: rgba(255,255,255,.85);
  font-size: 14.5px;
  font-weight: 600;
  transition: color .25s;
}

.nb-17__bar:has(#nb-17-2:checked) .nb-17__cap {
  transform: translateX(86px);
}

.nb-17__bar:has(#nb-17-3:checked) .nb-17__cap {
  transform: translateX(172px);
}

.nb-17__bar:has(#nb-17-4:checked) .nb-17__cap {
  transform: translateX(258px);
}

#nb-17-1:checked~label[for="nb-17-1"],
#nb-17-2:checked~label[for="nb-17-2"],
#nb-17-3:checked~label[for="nb-17-3"],
#nb-17-4:checked~label[for="nb-17-4"] {
  color: #fff;
}

.nb-17__r:focus-visible+.nb-17__tab {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-17,
    .nb-17__cap {
    animation: none;
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hidden radio inputs hold the selected tab and CSS :has(#tab:checked) translates the frosted capsule behind it. Arrow keys move between tabs natively. */
```
