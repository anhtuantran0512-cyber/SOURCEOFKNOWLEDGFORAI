---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/fantasy-dividers/"
title: "Medieval Fantasy Star Crest Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "A heraldic divider for lore pages, RPG wikis and game sites: a four-point star sitting on tapered blades that narrow toward the ornament, with small…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Medieval Fantasy Star Crest Divider CSS
Source: https://codefronts.com/snippets/css-dividers/fantasy-dividers/

A heraldic divider for lore pages, RPG wikis and game sites: a four-point star sitting on tapered blades that narrow toward the ornament, with small counter-notches carved by clip-path. Everything is CSS shapes on a parchment surface, so it re-colours instantly between a dark grimoire theme and an aged-vellum one — no sprite sheet, no icon font.
## HTML
```html
<section class="div-18" aria-label="Medieval fantasy star crest divider demo">
  <div class="div-18__stage">
    <div class="div-18__halo" aria-hidden="true"></div>
    <p class="div-18__eyebrow">CHAPTER THE THIRD</p>
    <h2 class="div-18__title">Of Rules &amp; Ruin</h2>
    <div class="div-18__crest" role="separator" aria-label="Chapter divider">
      <span class="div-18__blade" aria-hidden="true"></span>
      <span class="div-18__starwrap" aria-hidden="true">
        <span class="div-18__star div-18__star--back"></span>
        <span class="div-18__star"></span>
      </span>
      <span class="div-18__blade div-18__blade--r" aria-hidden="true"></span>
    </div>
    <p class="div-18__body">And it was written that no section should end without its mark, lest the reader wander from one thought into the next and never notice the crossing.</p>
    <div class="div-18__crest div-18__crest--sm" role="separator" aria-label="Divider">
      <span class="div-18__blade" aria-hidden="true"></span>
      <span class="div-18__lozenge" aria-hidden="true"></span>
      <span class="div-18__blade div-18__blade--r" aria-hidden="true"></span>
    </div>
    <p class="div-18__chip">clip-path blades · 4-point star polygon · 40s halo drift</p>
  </div>
</section>
```
## CSS
```css
.div-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-18-bg);
  --div-18-bg: oklch(0.19 0.018 60);
  --div-18-ink: oklch(0.92 0.02 80);
  --div-18-mut: oklch(0.68 0.03 78);
  --div-18-gold: oklch(0.78 0.12 82);
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  color: var(--div-18-ink);
  position: relative;
  overflow: hidden;
}

.div-18 *,
.div-18 *::before,
.div-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-18__stage {
  position: relative;
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(16px,3vw,26px);
  text-align: center;
  padding: clamp(30px,6vw,72px) clamp(20px,5vw,56px);
}

.div-18__halo {
  position: absolute;
  width: min(120vw,900px);
  aspect-ratio: 1;
  background: conic-gradient(from 0deg,oklch(0.78 0.12 82/.13),transparent 22%,oklch(0.78 0.12 82/.1) 50%,transparent 74%,oklch(0.78 0.12 82/.13));
  border-radius: 50%;
  filter: blur(28px);
  animation: div-18-drift 40s linear infinite;
  pointer-events: none;
}

@keyframes div-18-drift {
  to {
    rotate: 360deg;
  }
}

.div-18__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .36em;
  text-indent: .36em;
  color: var(--div-18-gold);
}

.div-18__title {
  font-size: clamp(32px,6.6vw,64px);
  line-height: 1.04;
  font-weight: 400;
  letter-spacing: .01em;
}

.div-18__crest {
  width: min(90vw,460px);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

.div-18__crest--sm {
  width: min(70vw,280px);
  opacity: .72;
}

.div-18__blade {
  flex: 1 1 0;
  height: 11px;
  background: linear-gradient(90deg,oklch(0.6 0.09 78),var(--div-18-gold));
  clip-path: polygon(0 42%,86% 0,100% 50%,86% 100%,0 58%);
}

.div-18__blade--r {
  scale: -1 1;
}

.div-18__crest--sm .div-18__blade {
  height: 7px;
}

.div-18__starwrap {
  position: relative;
  width: 30px;
  height: 30px;
  flex: none;
  filter: drop-shadow(0 0 12px oklch(0.78 0.12 82/.5));
}

.div-18__star {
  position: absolute;
  inset: 0;
  background: var(--div-18-gold);
  clip-path: polygon(50% 0,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0 50%,40% 40%);
}

.div-18__star--back {
  rotate: 45deg;
  scale: .62;
  opacity: .85;
}

.div-18__lozenge {
  width: 11px;
  height: 11px;
  flex: none;
  background: var(--div-18-gold);
  clip-path: polygon(50% 0,100% 50%,50% 100%,0 50%);
}

.div-18__body {
  max-width: 50ch;
  font-size: clamp(15px,1.95vw,18.5px);
  line-height: 1.68;
  color: var(--div-18-mut);
  font-style: italic;
  text-wrap: pretty;
}

.div-18__chip {
  margin-top: 6px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-18-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.78 0.12 82/.3);
  border-radius: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .div-18__halo {
    animation: none;
  }
}
```
