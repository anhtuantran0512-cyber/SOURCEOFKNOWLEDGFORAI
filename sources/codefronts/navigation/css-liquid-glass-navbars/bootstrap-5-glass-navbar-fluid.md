---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/bootstrap-5-glass-navbar-fluid/"
title: "Bootstrap 5 Glass Navbar (Fluid)"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "The liquid-glass look retro-fitted onto a Bootstrap 5 navbar structure — brand, toggler and a fluid container of nav-items — so enterprise apps already on…"
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 Glass Navbar (Fluid)
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/bootstrap-5-glass-navbar-fluid/

The liquid-glass look retro-fitted onto a Bootstrap 5 navbar structure — brand, toggler and a fluid container of nav-items — so enterprise apps already on Bootstrap can drop in the frosted aesthetic without leaving their component conventions. The demo mirrors Bootstrap's class semantics; production just adds these overrides to your bundle.
## HTML
```html
<section class="nb-12" aria-label="Bootstrap 5 glassmorphism navbar demo">
  <nav class="nb-12__navbar" aria-label="Primary">
    <a class="nb-12__brand" href="#nb-12">✦ Enterprise</a>
    <button class="nb-12__toggler" type="button" aria-label="Toggle navigation"><span aria-hidden="true">≡</span></button>
    <div class="nb-12__collapse">
      <ul class="nb-12__nav">
        <li><a class="nb-12__navlink" href="#nb-12" aria-current="page">Dashboard</a></li>
        <li><a class="nb-12__navlink" href="#nb-12">Projects</a></li>
        <li><a class="nb-12__navlink" href="#nb-12">Team</a></li>
        <li><a class="nb-12__navlink" href="#nb-12">Billing</a></li>
      </ul>
      <button class="nb-12__btn" type="button">Log in</button>
    </div>
  </nav>
</section>
```
## CSS
```css
.nb-12,
.nb-12 *,
.nb-12 *::before,
.nb-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-12 {
  --accent: oklch(0.6 0.2 255);
  display: grid;
  place-items: start center;
  width: 100%;
  min-height: 100vh;
  padding: 26px 18px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: linear-gradient(120deg,#2b5876,#4e4376 60%,#c94b4b);
  background-size: 180% 180%;
  animation: nb-12-bg 18s ease-in-out infinite;
}

@keyframes nb-12-bg {
  50% {
    background-position: 100% 100%;
  }
}

.nb-12__navbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px;
  width: min(900px,100%);
  padding: 12px 18px;
  border-radius: 14px;
  color: #fff;
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.32);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 16px 38px -22px rgba(0,0,0,.6);
  backdrop-filter: blur(18px) saturate(170%);
  -webkit-backdrop-filter: blur(18px) saturate(170%);
}

.nb-12__brand {
  font-size: 18px;
  font-weight: 800;
  text-decoration: none;
  color: #fff;
  letter-spacing: -.01em;
}

.nb-12__toggler {
  display: none;
  margin-inline-start: auto;
  width: 44px;
  height: 38px;
  border-radius: 9px;
  border: 1px solid rgba(255,255,255,.4);
  background: rgba(255,255,255,.14);
  color: #fff;
  font-size: 20px;
  cursor: pointer;
}

.nb-12__collapse {
  display: flex;
  flex: 1;
  align-items: center;
  gap: 14px;
}

.nb-12__nav {
  display: flex;
  gap: 4px;
  list-style: none;
  margin-inline-start: auto;
}

.nb-12__navlink {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 9px;
  text-decoration: none;
  color: rgba(255,255,255,.86);
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,color .2s;
}

.nb-12__navlink:hover {
  color: #fff;
  background: rgba(255,255,255,.16);
}

.nb-12__navlink[aria-current] {
  color: #fff;
  background: rgba(255,255,255,.24);
}

.nb-12__navlink:focus-visible,
.nb-12__btn:focus-visible,
.nb-12__toggler:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-12__btn {
  min-height: 40px;
  padding: 0 18px;
  border-radius: 9px;
  border: 1px solid color-mix(in oklab,var(--accent) 40%,white);
  background: var(--accent);
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
}

@media (max-width: 640px) {
  .nb-12__toggler {
    display: block;
  }

  .nb-12__collapse {
    flex-basis: 100%;
    flex-direction: column;
    align-items: stretch;
  }

  .nb-12__nav {
    flex-direction: column;
    margin: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nb-12 {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript in the demo — glass is a pure CSS override layer on Bootstrap 5 markup (.navbar/.navbar-brand/.nav-link). In production, keep Bootstrap's collapse JS for the toggler. */
```
