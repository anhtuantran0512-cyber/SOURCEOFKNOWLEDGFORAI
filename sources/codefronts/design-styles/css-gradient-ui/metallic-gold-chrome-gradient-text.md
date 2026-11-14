---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/metallic-gold-chrome-gradient-text/"
title: "Metallic / Gold / Chrome Gradient Text"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "An awards-invitation screen with three metal finishes — brushed gold with a passing shine, liquid chrome with hard specular bands, and rose gold — each an…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Metallic / Gold / Chrome Gradient Text
Source: https://codefronts.com/design-styles/css-gradient-ui/metallic-gold-chrome-gradient-text/

An awards-invitation screen with three metal finishes — brushed gold with a passing shine, liquid chrome with hard specular bands, and rose gold — each an exact multi-stop recipe you can lift, plus the stop math that makes metal read as metal.
## HTML
```html
<div class="cgu-15-group">
<section class="cgu-15" aria-label="Metallic gold and chrome gradient text demos">
  <div class="cgu-15__inner">
    <p class="cgu-15__eyebrow">15 · Metallic text</p>
    <p class="cgu-15__kicker">The Annual</p>
    <h2 class="cgu-15__gold">GOLDEN CURSOR<br>AWARDS</h2>
    <p class="cgu-15__invite">You are cordially invited to the ceremony</p>
    <div class="cgu-15__metals">
      <div class="cgu-15__metal"><span class="cgu-15__chrome">CHROME</span><span class="cgu-15__cap">cool greys · hard specular bands</span></div>
      <div class="cgu-15__metal"><span class="cgu-15__rose">ROSE&nbsp;GOLD</span><span class="cgu-15__cap">hue ~345° · same stop rhythm</span></div>
    </div>
    <p class="cgu-15__foot">Metal = hard lightness banding. Bright and dark stops sit close together — 6-to-8 stops, never 3.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-15-group {
  display: block;
  width: 100%;
}

.cgu-15,
.cgu-15 *,
.cgu-15 *::before,
.cgu-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-15 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: Georgia,'Times New Roman',serif;
  color: #efe9dc;
  background: radial-gradient(90% 70% at 50% 20%,#1a1510 0%,#0c0a07 60%);
}

.cgu-15__inner {
  width: min(760px,100%);
  text-align: center;
  display: grid;
  gap: 18px;
  justify-items: center;
}

.cgu-15__eyebrow {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #a08c62;
}

.cgu-15__kicker {
  font-size: clamp(16px,2.4vw,22px);
  font-style: italic;
  letter-spacing: .34em;
  text-transform: uppercase;
  color: #cbb684;
}

.cgu-15__gold {
  font-size: clamp(42px,8vw,96px);
  font-weight: 800;
  letter-spacing: .02em;
  line-height: 1.04;
  color: #d4a437;
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .cgu-15__gold {
    background: linear-gradient(105deg,transparent 0%,transparent 42%,rgba(255,255,255,.85) 50%,transparent 58%,transparent 100%) no-repeat -200% 0 / 200% 100%,linear-gradient(105deg,#8a5a08 0%,#f9d77e 22%,#fdf0c2 34%,#d4a437 48%,#7a4d05 62%,#f3ce6f 82%,#b8860b 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: cgu15-shine 4.6s ease-in-out infinite;
  }
}

.cgu-15__invite {
  font-size: 15px;
  font-style: italic;
  color: #b8a87f;
  letter-spacing: .06em;
}

.cgu-15__metals {
  display: flex;
  gap: 56px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 26px;
}

.cgu-15__metal {
  display: grid;
  gap: 8px;
  justify-items: center;
}

.cgu-15__chrome {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: clamp(30px,5vw,52px);
  font-weight: 900;
  letter-spacing: .04em;
  color: #c8cdd6;
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .cgu-15__chrome {
    background: linear-gradient(180deg,#f8fafc 0%,#e2e8f0 28%,#64748b 42%,#0f172a 50%,#94a3b8 58%,#f1f5f9 78%,#475569 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

.cgu-15__rose {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: clamp(30px,5vw,52px);
  font-weight: 900;
  letter-spacing: .04em;
  color: #d99a8f;
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .cgu-15__rose {
    background: linear-gradient(105deg,#8c4a3a 0%,#f4b8a6 24%,#fde4d8 36%,#d98a72 50%,#7d3f30 64%,#f0ad93 84%,#a85a44 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

.cgu-15__cap {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12px;
  color: #8d7f60;
  letter-spacing: .04em;
}

.cgu-15__foot {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 13px;
  color: #8d7f60;
  margin-top: 16px;
  max-width: 56ch;
}

@keyframes cgu15-shine {
  0%,
    55% {
    background-position: -200% 0,0 0;
  }

  90%,
    100% {
    background-position: 200% 0,0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-15__gold {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — 7-stop banded ramps clipped to the glyphs; the travelling shine is a transparent white-streak layer panned in the same background stack. */
```
