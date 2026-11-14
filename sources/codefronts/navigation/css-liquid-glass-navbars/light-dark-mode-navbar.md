---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/light-dark-mode-navbar/"
title: "Light / Dark Mode Navbar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A liquid-glass navbar that automatically retunes its refraction and tint for light or dark contexts via prefers-color-scheme — dark glass with bright rims at…"
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Light / Dark Mode Navbar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/light-dark-mode-navbar/

A liquid-glass navbar that automatically retunes its refraction and tint for light or dark contexts via prefers-color-scheme — dark glass with bright rims at night, light frosted glass by day — and also exposes a manual override toggle. The glass recipe adapts, not just the colours.
## HTML
```html
<section class="nb-21" aria-label="Light and dark mode glass navbar demo">
  <div class="nb-21__stage">
    <input class="nb-21__toggle" type="checkbox" id="nb-21-toggle">
    <header class="nb-21__bar">
      <span class="nb-21__brand">◑ Adaptive</span>
      <nav class="nb-21__nav" aria-label="Primary">
        <a class="nb-21__link" href="#nb-21" aria-current="page">Home</a>
        <a class="nb-21__link" href="#nb-21">Notes</a>
        <a class="nb-21__link" href="#nb-21">Files</a>
      </nav>
      <label class="nb-21__switch" for="nb-21-toggle" title="Toggle theme"><span class="nb-21__knob" aria-hidden="true"></span><span class="nb-21__sr">Toggle light / dark theme</span></label>
    </header>
  </div>
</section>
```
## CSS
```css
.nb-21,
.nb-21 *,
.nb-21 *::before,
.nb-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-21 {
  --glass: rgba(255,255,255,.5);
  --rim: rgba(255,255,255,.8);
  --fg: #12131a;
  --sat: 170%;
  --field: rgba(0,0,0,.08);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.nb-21__stage {
  width: min(720px,100%);
  border-radius: 22px;
  padding: 40px 22px;
  background: linear-gradient(120deg,#dfe9f3,#ffffff);
  transition: background .4s;
}

@media (prefers-color-scheme: dark) {
  .nb-21 {
    --glass: rgba(20,22,34,.5);
    --rim: rgba(255,255,255,.4);
    --fg: #f2f3fb;
    --sat: 150%;
    --field: rgba(255,255,255,.1);
  }

  .nb-21__stage {
    background: linear-gradient(120deg,#12141f,#242a44);
  }
}

.nb-21:has(#nb-21-toggle:checked) {
  --glass: rgba(20,22,34,.5);
  --rim: rgba(255,255,255,.4);
  --fg: #f2f3fb;
  --sat: 150%;
  --field: rgba(255,255,255,.1);
}

.nb-21:has(#nb-21-toggle:checked) .nb-21__stage {
  background: linear-gradient(120deg,#12141f,#242a44);
}

.nb-21__toggle {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.nb-21__bar {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 13px 16px;
  border-radius: 16px;
  color: var(--fg);
  background: var(--glass);
  border: 1px solid var(--rim);
  box-shadow: inset 0 1px 0 var(--rim),0 16px 38px -22px rgba(0,0,0,.5);
  backdrop-filter: blur(20px) saturate(var(--sat));
  -webkit-backdrop-filter: blur(20px) saturate(var(--sat));
  transition: background .4s,color .4s,border-color .4s;
}

.nb-21__brand {
  font-size: 16px;
  font-weight: 800;
}

.nb-21__nav {
  display: flex;
  gap: 4px;
  margin-inline-start: auto;
}

.nb-21__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--fg);
  opacity: .8;
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,opacity .2s;
}

.nb-21__link:hover,
.nb-21__link[aria-current] {
  opacity: 1;
  background: var(--field);
}

.nb-21__link:focus-visible {
  outline: 2px solid var(--fg);
  outline-offset: 2px;
}

.nb-21__switch {
  width: 52px;
  height: 30px;
  border-radius: 999px;
  background: var(--field);
  border: 1px solid var(--rim);
  cursor: pointer;
  display: flex;
  align-items: center;
  padding: 3px;
  transition: background .3s;
}

.nb-21__knob {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--fg);
  transition: transform .3s cubic-bezier(.34,1.4,.5,1);
}

.nb-21:has(#nb-21-toggle:checked) .nb-21__knob,
@media (prefers-color-scheme:dark) {
}

.nb-21:has(#nb-21-toggle:checked) .nb-21__knob {
  transform: translateX(22px);
}

.nb-21__toggle:focus-visible+.nb-21__bar .nb-21__switch {
  outline: 2px solid var(--fg);
  outline-offset: 2px;
}

.nb-21__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .nb-21__bar,
    .nb-21__knob,
    .nb-21__stage {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — themed custom properties are redefined inside @media (prefers-color-scheme:dark) for automatic OS adaptation, and a native checkbox read via :has(#toggle:checked) provides a manual override. */
```
