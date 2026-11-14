---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/visionos-glass-navbar/"
title: "visionOS Glass Navbar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A heavy, high-contrast visionOS-style navigation panel designed for dark, media-rich layouts."
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: visionOS Glass Navbar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/visionos-glass-navbar/

A heavy, high-contrast visionOS-style navigation panel designed for dark, media-rich layouts. The bar floats as a deeply frosted dark-glass slab with a bright specular top rim and a soft ambient shadow beneath — the spatial-computing look, tuned so links stay perfectly legible over video and photography.
## HTML
```html
<section class="nb-04" aria-label="visionOS style glass navbar demo">
  <nav class="nb-04__bar" aria-label="Primary">
    <span class="nb-04__brand"><span class="nb-04__dot" aria-hidden="true"></span>Horizon</span>
    <div class="nb-04__links">
      <a class="nb-04__link" href="#nb-04" aria-current="page">Spaces</a>
      <a class="nb-04__link" href="#nb-04">Immersive</a>
      <a class="nb-04__link" href="#nb-04">Library</a>
      <a class="nb-04__link" href="#nb-04">Shared</a>
    </div>
    <button class="nb-04__cta" type="button">Enter</button>
  </nav>
</section>
```
## CSS
```css
.nb-04,
.nb-04 *,
.nb-04 *::before,
.nb-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-04 {
  --accent: oklch(0.72 0.16 210);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(90% 120% at 70% 10%,#1b2b4d,#070a14 70%),url('https://picsum.photos/seed/nb04dark/1000/700') center/cover;
  background-blend-mode: soft-light;
}

.nb-04__bar {
  display: flex;
  align-items: center;
  gap: 22px;
  width: min(760px,94%);
  padding: 14px 18px;
  border-radius: 22px;
  isolation: isolate;
  contain: layout paint;
  color: #fff;
  background: color-mix(in oklab,black 34%,transparent);
  border: 1px solid rgba(255,255,255,.16);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 34px 70px -26px rgba(0,0,0,.85);
  backdrop-filter: blur(40px) saturate(140%) brightness(1.05);
  -webkit-backdrop-filter: blur(40px) saturate(140%) brightness(1.05);
}

.nb-04__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.nb-04__dot {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%,#fff,var(--accent));
  box-shadow: 0 0 14px var(--accent);
}

.nb-04__links {
  display: flex;
  gap: 6px;
  margin-inline-start: auto;
}

.nb-04__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 15px;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255,255,255,.86);
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,color .2s;
}

.nb-04__link:hover {
  background: rgba(255,255,255,.14);
  color: #fff;
}

.nb-04__link[aria-current] {
  background: rgba(255,255,255,.2);
  color: #fff;
}

.nb-04__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.nb-04__cta {
  min-height: 40px;
  padding: 0 20px;
  border-radius: 12px;
  border: 1px solid color-mix(in oklab,var(--accent) 50%,white);
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 80%,white),var(--accent));
  color: #04121a;
  font-size: 14.5px;
  font-weight: 700;
  cursor: pointer;
  transition: transform .18s;
}

.nb-04__cta:hover {
  transform: translateY(-2px);
}

.nb-04__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}
```

## JavaScript
```js
/* No JavaScript — a dark tint under a heavy backdrop-filter blur/saturate/brightness reads as thick smoked glass; contain:layout paint isolates the expensive blur so it never repaints the page. */
```
