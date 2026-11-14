---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-morphing-text-animation/"
title: "CSS Variable Font Weight Animation on Hover"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Variable-font choreography with Recursive: a headline whose letters swell toward the cursor like type under a magnet (proximity-mapped 'wght'), and a zero-JS…"
has_js: "true"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Variable Font Weight Animation on Hover
Source: https://codefronts.com/motion/css-text-animations/css-morphing-text-animation/

Variable-font choreography with Recursive: a headline whose letters swell toward the cursor like type under a magnet (proximity-mapped 'wght'), and a zero-JS menu where each row transitions weight, slant and the CASL casual axis on hover.
## HTML
```html
<div class="cat-16-group">
<link href="https://fonts.googleapis.com/css2?family=Recursive:slnt,wght,[email protected],300..1000,0..1&display=swap" rel="stylesheet">
<section class="cat-16a" aria-label="Variable font weight follows the cursor">
  <div class="cat-16a__stage" id="cat-16a">
    <h1 class="cat-16a__word" aria-label="come closer">
      <span aria-hidden="true"><i>c</i><i>o</i><i>m</i><i>e</i><i>&nbsp;</i><i>c</i><i>l</i><i>o</i><i>s</i><i>e</i><i>r</i></span>
    </h1>
    <p class="cat-16a__sub" aria-hidden="true">'wght' 320 → 900 mapped to pointer distance</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Recursive:slnt,wght,[email protected],300..1000,0..1&display=swap" rel="stylesheet">
<section class="cat-16b" aria-label="Variable font menu hover">
  <nav class="cat-16b__menu" aria-label="Cafe menu">
    <p class="cat-16b__label" aria-hidden="true">— the counter —</p>
    <a class="cat-16b__item" href="#">Espresso<em>2.80</em></a>
    <a class="cat-16b__item" href="#">Cortado<em>3.60</em></a>
    <a class="cat-16b__item" href="#">Filter<em>3.20</em></a>
    <a class="cat-16b__item" href="#">Cold brew<em>4.40</em></a>
  </nav>
</section>
</div>
```
## CSS
```css
.cat-16-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-16-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-16a,
.cat-16a *,
.cat-16a *::before,
.cat-16a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-16a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f4f2ec;
  font-family: 'Recursive','Segoe UI',system-ui,sans-serif;
}

.cat-16a__stage {
  text-align: center;
  padding: 60px clamp(20px,6vw,90px);
  cursor: crosshair;
}

.cat-16a__word {
  font-size: clamp(40px,8vw,104px);
  color: #191714;
  letter-spacing: -.01em;
}

.cat-16a__word i {
  display: inline-block;
  font-style: normal;
  font-variation-settings: 'wght' 380,'CASL' 0,'slnt' 0;
  transition: font-variation-settings .22s ease-out;
}

.cat-16a__sub {
  margin-top: 22px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  color: rgba(25,23,20,.42);
}

@media (prefers-reduced-motion: reduce) {
  .cat-16a__word i {
    transition: none;
  }
}

.cat-16b,
.cat-16b *,
.cat-16b *::before,
.cat-16b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-16b {
  --paper: #181512;
  --cream: #efe6d8;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: var(--paper);
  font-family: 'Recursive','Segoe UI',system-ui,sans-serif;
}

.cat-16b__menu {
  display: grid;
  gap: 6px;
  width: min(460px,100%);
}

.cat-16b__label {
  font-size: 11px;
  letter-spacing: .34em;
  text-transform: uppercase;
  color: rgba(239,230,216,.4);
  text-align: center;
  margin-bottom: 18px;
  font-variation-settings: 'wght' 400,'CASL' 1,'slnt' 0;
}

.cat-16b__item {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 24px;
  padding: 14px 10px;
  font-size: clamp(24px,3.6vw,34px);
  color: var(--cream);
  text-decoration: none;
  border-bottom: 1px solid rgba(239,230,216,.12);
  font-variation-settings: 'wght' 350,'CASL' 0,'slnt' 0;
  transition: font-variation-settings .35s ease,color .3s;
}

.cat-16b__item em {
  font-style: normal;
  font-size: .55em;
  color: rgba(239,230,216,.5);
  font-variation-settings: 'wght' 400,'CASL' 0,'slnt' 0;
}

.cat-16b__item:hover,
.cat-16b__item:focus-visible {
  color: #fff;
  font-variation-settings: 'wght' 920,'CASL' 1,'slnt' -6;
}

.cat-16b__item:focus-visible {
  outline: 2px solid var(--cream);
  outline-offset: 4px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cat-16b__item {
    transition: color .2s;
  }
}
```

## JavaScript
```js
(() => {
  const wrap = document.querySelector('#cat-16a'); if (!wrap) return;
  const els = Array.from(wrap.querySelectorAll('i'));
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let raf = 0;
  const set = (x, y) => els.forEach((el) => {
    const r = el.getBoundingClientRect();
    const d = Math.hypot(x - (r.left + r.width / 2), y - (r.top + r.height / 2));
    const w = Math.max(320, 900 - d * 2.6);
    el.style.fontVariationSettings = "'wght' " + Math.round(w) + ",'CASL' 0,'slnt' 0";
  });
  wrap.addEventListener('pointermove', (e) => {
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => set(e.clientX, e.clientY));
  });
  wrap.addEventListener('pointerleave', () => els.forEach((el) => {
    el.style.fontVariationSettings = "'wght' 380,'CASL' 0,'slnt' 0";
  }));
})();

/* No JavaScript — font-variation-settings tweens 'wght' 350→920, 'CASL' 0→1 and 'slnt' 0→-6 on hover; identical axis lists in both states make it interpolate. */
```
