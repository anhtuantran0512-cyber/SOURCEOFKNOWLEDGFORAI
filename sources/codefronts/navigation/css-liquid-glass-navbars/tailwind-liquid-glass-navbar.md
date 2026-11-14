---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/tailwind-liquid-glass-navbar/"
title: "Tailwind Liquid Glass Navbar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A clean, utility-first top navbar built to map 1:1 onto Tailwind classes: backdrop-blur-xl, bg-white/10, ring-1 ring-white/20, rounded-full."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Navbar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/tailwind-liquid-glass-navbar/

A clean, utility-first top navbar built to map 1:1 onto Tailwind classes: backdrop-blur-xl, bg-white/10, ring-1 ring-white/20, rounded-full. Brand, centred link group and a primary CTA — the canonical Tailwind glass header, shown here in both raw CSS and pure utilities.
## HTML
```html
<section class="nb-07" aria-label="Tailwind liquid glass navbar demo">
  <header class="nb-07__bar">
    <a class="nb-07__brand" href="#nb-07">◆ Utility</a>
    <nav class="nb-07__nav" aria-label="Primary">
      <a class="nb-07__link" href="#nb-07" aria-current="page">Product</a>
      <a class="nb-07__link" href="#nb-07">Docs</a>
      <a class="nb-07__link" href="#nb-07">Pricing</a>
      <a class="nb-07__link" href="#nb-07">Blog</a>
    </nav>
    <button class="nb-07__cta" type="button">Sign up</button>
  </header>
</section>
```
## CSS
```css
.nb-07,
.nb-07 *,
.nb-07 *::before,
.nb-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-07 {
  --accent: oklch(0.62 0.21 300);
  display: grid;
  place-items: start center;
  width: 100%;
  min-height: 100vh;
  padding: 26px 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(120deg,#3a1c71,#d76d77 50%,#ffaf7b);
  background-size: 180% 180%;
  animation: nb-07-bg 16s ease-in-out infinite;
}

@keyframes nb-07-bg {
  50% {
    background-position: 100% 100%;
  }
}

.nb-07__bar {
  display: flex;
  align-items: center;
  gap: 20px;
  width: min(820px,100%);
  padding: 12px 16px 12px 22px;
  border-radius: 9999px;
  color: #fff;
  background: rgba(255,255,255,.1);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.2),0 18px 40px -22px rgba(0,0,0,.6);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
}

.nb-07__brand {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.01em;
  text-decoration: none;
  color: #fff;
}

.nb-07__nav {
  display: flex;
  gap: 4px;
  margin-inline-start: auto;
}

.nb-07__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 15px;
  border-radius: 9999px;
  text-decoration: none;
  color: rgba(255,255,255,.85);
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,color .2s;
}

.nb-07__link:hover {
  color: #fff;
  background: rgba(255,255,255,.14);
}

.nb-07__link[aria-current] {
  color: #fff;
  background: rgba(255,255,255,.2);
}

.nb-07__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-07__cta {
  min-height: 40px;
  padding: 0 20px;
  border-radius: 9999px;
  border: 0;
  background: #fff;
  color: #3a1c71;
  font-size: 14.5px;
  font-weight: 700;
  cursor: pointer;
  transition: transform .18s;
}

.nb-07__cta:hover {
  transform: translateY(-2px);
}

.nb-07__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}
```

## JavaScript
```js
/* No JavaScript — every property maps to a Tailwind utility: backdrop-blur-xl, bg-white/10, ring-1 ring-white/20, rounded-full. See the Tailwind tab for the utility-class version. */
```
