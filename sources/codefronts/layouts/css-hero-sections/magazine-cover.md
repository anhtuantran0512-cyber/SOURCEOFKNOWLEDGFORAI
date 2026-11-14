---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/magazine-cover/"
title: "Magazine Cover"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Print-magazine cover treatment — issue stamp, oversized italic serif headline, vertical spine label, foil-stamped corner number. Plum and champagne on linen."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magazine Cover
Source: https://codefronts.com/layouts/css-hero-sections/magazine-cover/

Print-magazine cover treatment — issue stamp, oversized italic serif headline, vertical spine label, foil-stamped corner number. Plum and champagne on linen.
## HTML
```html
<section class="hs-11" aria-label="Hero">
  <div class="hs-11__frame">
    <span class="hs-11__spine">Vol. XII · No. 47 · Spring</span>
    <span class="hs-11__num">04</span>
    <header>
      <span class="hs-11__issue">SPRING 2026 · INDEX NO. 04</span>
    </header>
    <h2>
      The Quiet
      <em>Revolution</em>
      of slow type.
    </h2>
    <p>
      Why every serious editorial brand is going back to serifs, italics, and a single column wide
      enough to think in.
    </p>
    <a class="hs-11__cta" href="#read">Read the issue →</a>
  </div>
</section>
```
## CSS
```css
.hs-11 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(20px, 4vw, 40px);
  background: repeating-linear-gradient(0deg, transparent 0 47px, rgba(60,40,80,0.04) 47px 48px), #ede4d3;
  font-family: 'Playfair Display', Georgia, serif;
  color: #2a1f3a;
  box-sizing: border-box;
}

.hs-11__frame {
  position: relative;
  width: 100%;
  max-width: 720px;
  background: #f7f1e1;
  border: 1px solid #2a1f3a;
  padding: clamp(28px, 4vw, 56px) clamp(28px, 4vw, 56px) clamp(28px, 4vw, 56px) clamp(48px, 6vw, 72px);
  box-shadow: 12px 12px 0 #c69e5a, 12px 12px 0 1px #2a1f3a;
}

.hs-11__spine {
  position: absolute;
  top: 50%;
  left: 18px;
  transform: translateY(-50%);
  writing-mode: vertical-rl;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10.5px;
  letter-spacing: 0.32em;
  color: #6b1f4a;
  white-space: nowrap;
  padding: 14px 4px;
  border-block: 1px solid #6b1f4a;
}

.hs-11__num {
  position: absolute;
  top: 16px;
  right: 22px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 48px;
  font-weight: 800;
  font-style: italic;
  color: #c69e5a;
  text-shadow: 1px 1px 0 #2a1f3a;
}

.hs-11 header {
  padding-bottom: 18px;
  border-bottom: 1px solid #2a1f3a;
  margin-bottom: 22px;
}

.hs-11__issue {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.24em;
  color: #2a1f3a;
}

.hs-11 h2 {
  margin: 0 0 22px;
  font-size: clamp(40px, 7vw, 78px);
  font-weight: 600;
  line-height: 0.95;
  letter-spacing: -0.02em;
}

.hs-11 h2 em {
  font-style: italic;
  font-weight: 700;
  color: #6b1f4a;
  display: block;
  font-size: 1.2em;
}

.hs-11 p {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  font-size: 18px;
  line-height: 1.45;
  color: #4a3858;
  margin: 0 0 24px;
  max-width: 460px;
}

.hs-11__cta {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #2a1f3a;
  text-decoration: none;
  border-bottom: 2px solid #2a1f3a;
  padding-bottom: 3px;
  transition: color 0.15s, border-color 0.15s;
}

.hs-11__cta:hover {
  color: #6b1f4a;
  border-color: #6b1f4a;
}
```
