---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/google-fonts-neon-pairing/"
title: "Google-Fonts Neon Pairing"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A side-by-side reference showing which Google font actually looks like real neon — a rounded monoline display face (Monoton) glowing beside a geometric tech…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Google-Fonts Neon Pairing
Source: https://codefronts.com/motion/css-neon-text-effect/google-fonts-neon-pairing/

A side-by-side reference showing which Google font actually looks like real neon — a rounded monoline display face (Monoton) glowing beside a geometric tech face (Orbitron) — so designers can copy the exact @import + shadow recipe.
## HTML
```html
<div class="cnt-07">
  <div class="cnt-07__grid">
    <figure class="cnt-07__cell">
      <span class="cnt-07__mono">Diner</span>
      <figcaption class="cnt-07__cap"><b>Monoton</b> · inline monoline — reads as bent glass tube</figcaption>
    </figure>
    <figure class="cnt-07__cell">
      <span class="cnt-07__orb">ARCADE</span>
      <figcaption class="cnt-07__cap"><b>Orbitron</b> · geometric — reads as sci-fi HUD sign</figcaption>
    </figure>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Monoton&family=Orbitron:wght@700;900&display=swap');

.cnt-07,
.cnt-07 *,
.cnt-07 *::before,
.cnt-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-07 ::selection {
  background: oklch(0.83 0.16 300);
  color: #0d0416;
}

.cnt-07 {
  --accent: oklch(0.82 0.17 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: radial-gradient(120% 120% at 50% 20%,#0d0b12,#050408);
}

.cnt-07__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(260px,1fr));
  gap: 28px;
  width: min(760px,94vw);
}

.cnt-07__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 44px 24px;
  border-radius: 16px;
  background: #0a0810;
  border: 1px solid #1c1726;
  text-align: center;
}

.cnt-07__mono {
  font-family: 'Monoton',cursive;
  font-size: clamp(40px,9vw,68px);
  color: var(--accent);
  text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 30px var(--accent),0 0 64px var(--accent);
}

.cnt-07__orb {
  font-family: 'Orbitron',sans-serif;
  font-weight: 900;
  font-size: clamp(34px,7vw,54px);
  letter-spacing: .08em;
  color: var(--accent);
  text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 30px var(--accent),0 0 64px var(--accent);
}

.cnt-07__cap {
  font-size: 13px;
  line-height: 1.5;
  color: #8b8399;
  max-width: 26ch;
}

.cnt-07__cap b {
  color: #d9d2e6;
}

@media (prefers-reduced-motion: reduce) {
}
```

## JavaScript
```js
/* No JavaScript — a font legibility reference; the glow is a shared text-shadow. */
```
