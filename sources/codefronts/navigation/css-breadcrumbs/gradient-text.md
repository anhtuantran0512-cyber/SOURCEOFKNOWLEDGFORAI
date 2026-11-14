---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/gradient-text/"
title: "SaaS Marketing Site Gradient Text Breadcrumb Bar"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The breadcrumb SaaS marketing sites like Linear and Vercel reach for when a single line of text needs to feel alive."
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Marketing Site Gradient Text Breadcrumb Bar
Source: https://codefronts.com/navigation/css-breadcrumbs/gradient-text/

The breadcrumb SaaS marketing sites like Linear and Vercel reach for when a single line of text needs to feel alive. Crumbs are painted with a slow-drifting conic gradient clipped to text via @property, so the hue cycles through vivid oklch stops without ever touching the layout.
## HTML
```html
<section class="bc-19" aria-label="SaaS marketing site gradient text breadcrumb demo">
      <nav aria-label="Breadcrumb">
        <ol class="bc-19__list">
          <li class="bc-19__item"><a class="bc-19__link" href="#">Docs</a></li>
          <li class="bc-19__item"><a class="bc-19__link" href="#">Guides</a></li>
          <li class="bc-19__item"><a class="bc-19__link" href="#">Authentication</a></li>
          <li class="bc-19__item"><a class="bc-19__link" aria-current="page" href="#">Magic Links</a></li>
        </ol>
      </nav>
    </section>
```
## CSS
```css
@property --grad-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.bc-19 {
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(24px, 6vw, 64px) clamp(16px, 5vw, 48px);
  font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  background: radial-gradient(1200px 600px at 50% -10%, oklch(0.96 0.02 270 / 0.9), transparent 60%), linear-gradient(180deg, oklch(0.99 0.005 260), oklch(0.97 0.01 265));
  color: oklch(0.28 0.02 260);
  -webkit-font-smoothing: antialiased;
}

.bc-19 nav {
  width: 100%;
  max-width: 880px;
  padding: 14px 22px;
  border-radius: 14px;
  background: oklch(1 0 0 / 0.72);
  backdrop-filter: blur(14px) saturate(1.1);
  -webkit-backdrop-filter: blur(14px) saturate(1.1);
  border: 1px solid oklch(0.9 0.01 260 / 0.7);
  box-shadow: 0 1px 0 oklch(1 0 0 / 0.9) inset, 0 12px 40px -18px oklch(0.3 0.05 270 / 0.35);
}

.bc-19__list {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 2px 4px;
  margin: 0;
  padding: 0;
  list-style: none;
  font-size: clamp(14px, 1.6vw, 16px);
  font-weight: 500;
  letter-spacing: -0.005em;
}

.bc-19__item {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
}

.bc-19__item + .bc-19__item::before {
  content: '';
  display: inline-block;
  width: 6px;
  height: 6px;
  margin: 0 10px;
  border-right: 1.5px solid oklch(0.75 0.02 260);
  border-bottom: 1.5px solid oklch(0.75 0.02 260);
  transform: rotate(-45deg);
  opacity: 0.7;
}

.bc-19__link {
  --grad-stops: oklch(0.62 0.2 285), oklch(0.68 0.22 320), oklch(0.72 0.2 25), oklch(0.7 0.2 190), oklch(0.62 0.2 285);
  position: relative;
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 6px 8px;
  border-radius: 8px;
  text-decoration: none;
  color: oklch(0.42 0.03 265);
  background: conic-gradient(from var(--grad-angle), var(--grad-stops));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: bc31-drift 18s linear infinite;
  transition: transform 0.25s ease, filter 0.25s ease;
}

.bc-19__link::after {
  content: '';
  position: absolute;
  left: 8px;
  right: 8px;
  bottom: 4px;
  height: 1.5px;
  border-radius: 2px;
  background: conic-gradient(from var(--grad-angle), var(--grad-stops));
  opacity: 0;
  transform: scaleX(0.4);
  transform-origin: left center;
  transition: opacity 0.25s ease, transform 0.35s ease;
}

.bc-19__link:hover,
.bc-19__link:focus-visible {
  animation-duration: 6s;
  filter: saturate(1.15);
}

.bc-19__link:hover::after,
.bc-19__link:focus-visible::after {
  opacity: 0.85;
  transform: scaleX(1);
}

.bc-19__link:focus-visible {
  outline: 2px solid oklch(0.62 0.2 285);
  outline-offset: 3px;
}

.bc-19__link[aria-current='page'] {
  --grad-stops: oklch(0.6 0.24 300), oklch(0.68 0.24 340), oklch(0.72 0.22 20), oklch(0.66 0.24 275), oklch(0.6 0.24 300);
  font-weight: 650;
  animation-duration: 7s;
}

@keyframes bc31-drift {
  to {
    --grad-angle: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bc-19__link,
    .bc-19__link[aria-current='page'] {
    animation: none;
    background: linear-gradient(90deg, oklch(0.62 0.2 285), oklch(0.68 0.22 320), oklch(0.66 0.24 20));
    -webkit-background-clip: text;
    background-clip: text;
  }

  .bc-19__link::after {
    transition: none;
  }
}

@supports not (background: paint(something)) {
  /* Older engines without @property still get a static clipped gradient. */

  .bc-19__link {
    background: linear-gradient(90deg, oklch(0.62 0.2 285), oklch(0.68 0.22 320), oklch(0.66 0.24 20));
    -webkit-background-clip: text;
    background-clip: text;
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — @property + conic-gradient + background-clip:text drives the animated gradient text. */
```
