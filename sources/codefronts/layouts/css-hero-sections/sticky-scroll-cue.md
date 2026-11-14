---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/sticky-scroll-cue/"
title: "Sticky Scroll Cue"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Tall full-bleed hero with a bouncing scroll indicator at the bottom. Forest emerald on birch with a soft yellow CTA — the cabin / retreat brand aesthetic."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Scroll Cue
Source: https://codefronts.com/layouts/css-hero-sections/sticky-scroll-cue/

Tall full-bleed hero with a bouncing scroll indicator at the bottom. Forest emerald on birch with a soft yellow CTA — the cabin / retreat brand aesthetic.
## HTML
```html
<section class="hs-10" aria-label="Hero">
  <div class="hs-10__inner">
    <span class="hs-10__eye">— A small place upstate</span>
    <h2>Slow Sundays, <em>warm wood,</em> not a single notification.</h2>
    <p>Three cabins, two acres, no Wi-Fi, one shared kitchen. Book yourself a real weekend.</p>
    <a class="hs-10__cta" href="#book">Check availability</a>
  </div>
  <div class="hs-10__cue" aria-hidden="true">
    <span>scroll</span>
    <div class="hs-10__mouse"><span></span></div>
  </div>
</section>
```
## CSS
```css
.hs-10 {
  position: relative;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px) 90px;
  background: radial-gradient(80% 60% at 50% 0%, rgba(38,82,52,0.16), transparent 70%), #f3eadb;
  font-family: 'Inter', system-ui, sans-serif;
  color: #1e3a26;
  box-sizing: border-box;
}

.hs-10__inner {
  max-width: 720px;
  text-align: center;
}

.hs-10__eye {
  display: inline-block;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  font-size: 16px;
  color: #6b8a6f;
  margin-bottom: 18px;
}

.hs-10 h2 {
  margin: 0 0 18px;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: clamp(34px, 5vw, 56px);
  font-weight: 600;
  letter-spacing: -0.015em;
  line-height: 1.05;
}

.hs-10 h2 em {
  color: #b8893a;
  font-style: italic;
}

.hs-10 p {
  margin: 0 auto 26px;
  font-size: 16px;
  line-height: 1.55;
  color: #5a6b58;
  max-width: 480px;
}

.hs-10__cta {
  display: inline-block;
  padding: 13px 26px;
  background: #f4d35e;
  color: #1e3a26;
  border: 2px solid #1e3a26;
  border-radius: 0;
  text-decoration: none;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 0.04em;
  box-shadow: 4px 4px 0 #1e3a26;
  transition: transform 0.15s, box-shadow 0.15s;
}

.hs-10__cta:hover {
  transform: translate(2px,2px);
  box-shadow: 2px 2px 0 #1e3a26;
}

.hs-10__cue {
  position: absolute;
  bottom: 18px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.18em;
  color: #6b8a6f;
  text-transform: uppercase;
}

.hs-10__mouse {
  width: 22px;
  height: 36px;
  border: 2px solid #1e3a26;
  border-radius: 12px;
  position: relative;
}

.hs-10__mouse span {
  position: absolute;
  top: 6px;
  left: 50%;
  transform: translateX(-50%);
  width: 3px;
  height: 7px;
  background: #1e3a26;
  border-radius: 2px;
  animation: hs-10-bounce 1.4s ease-in-out infinite;
}

@keyframes hs-10-bounce {
  0%,
    100% {
    transform: translate(-50%, 0);
    opacity: 1;
  }

  50% {
    transform: translate(-50%, 10px);
    opacity: 0.4;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-10__mouse span {
    animation: none;
  }

  .hs-10__cta {
    transition: none;
  }
}
```
