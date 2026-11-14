---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/inner-glow-hover-links/"
title: "Inner-Glow Hover Links"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "Nav links that illuminate from within on hover — a soft light blooms inside the glass capsule and a specular rim brightens — so the bar guides the eye with…"
has_js: "false"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inner-Glow Hover Links
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/inner-glow-hover-links/

Nav links that illuminate from within on hover — a soft light blooms inside the glass capsule and a specular rim brightens — so the bar guides the eye with light instead of hard borders or fills. Pure CSS, driven by a cursor-anchored radial glow.
## HTML
```html
<section class="nb-14" aria-label="Inner glow hover links demo">
  <nav class="nb-14__bar" aria-label="Primary">
    <span class="nb-14__brand">✺ Lumina</span>
    <div class="nb-14__links">
      <a class="nb-14__link" href="#nb-14" aria-current="page"><span>Home</span></a>
      <a class="nb-14__link" href="#nb-14"><span>Explore</span></a>
      <a class="nb-14__link" href="#nb-14"><span>Studio</span></a>
      <a class="nb-14__link" href="#nb-14"><span>About</span></a>
    </div>
  </nav>
</section>
```
## CSS
```css
.nb-14,
.nb-14 *,
.nb-14 *::before,
.nb-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-14 {
  --glow: oklch(0.82 0.16 200);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(circle at 25% 25%,#132b4d,#060912 70%),url('https://picsum.photos/seed/nb14/1000/700') center/cover;
  background-blend-mode: overlay;
}

.nb-14__bar {
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 12px 18px;
  border-radius: 9999px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 20px 44px -24px rgba(0,0,0,.7);
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
}

.nb-14__brand {
  font-size: 16px;
  font-weight: 800;
}

.nb-14__links {
  display: flex;
  gap: 6px;
}

.nb-14__link {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  min-height: 42px;
  display: flex;
  align-items: center;
  padding: 0 18px;
  border-radius: 9999px;
  text-decoration: none;
  color: rgba(255,255,255,.85);
  font-size: 14.5px;
  font-weight: 600;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0);
  transition: color .25s,box-shadow .3s;
}

.nb-14__link span {
  position: relative;
  z-index: 2;
}

.nb-14__link::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  border-radius: inherit;
  background: radial-gradient(60px 60px at var(--mx,50%) var(--my,50%),color-mix(in oklab,var(--glow) 85%,white),transparent 70%);
  opacity: 0;
  transform: scale(.4);
  transition: opacity .3s,transform .4s;
  pointer-events: none;
}

.nb-14__link:hover,
.nb-14__link:focus-visible,
.nb-14__link[aria-current] {
  color: #04141c;
}

.nb-14__link:hover::before,
.nb-14__link:focus-visible::before,
.nb-14__link[aria-current]::before {
  opacity: .95;
  transform: scale(1);
}

.nb-14__link:hover,
.nb-14__link:focus-visible {
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.6),0 0 22px -4px var(--glow);
}

.nb-14__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-14__link,
    .nb-14__link::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each link's ::before radial glow blooms from 0 on :hover/:focus-visible and an inset rim-light brightens, so the bar guides the eye with light instead of hard fills. */
```
