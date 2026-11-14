---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/cyberpunk-holographic-glitch-grid/"
title: "Cyberpunk Holographic Glitch Grid"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A neon, sci-fi CTA for gaming, web3 and dev-tool pages: a holographic grid sits behind the label and, on hover, tears with a hard stepped glitch while a…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Holographic Glitch Grid
Source: https://codefronts.com/motion/css-button-hover-effects/cyberpunk-holographic-glitch-grid/

A neon, sci-fi CTA for gaming, web3 and dev-tool pages: a holographic grid sits behind the label and, on hover, tears with a hard stepped glitch while a magenta/cyan chromatic split flickers over the text.
## HTML
```html
<div class="bhe-02-group">
<section class="bhe-02a" aria-label="Cyberpunk glitch grid button">
  <button class="bhe-02a__btn" type="button" data-text="Enter grid"><span class="bhe-02a__grid" aria-hidden="true"></span><span class="bhe-02a__label">Enter grid</span></button>
</section>
<section class="bhe-02b" aria-label="Cyberpunk scanline button">
  <button class="bhe-02b__btn" type="button"><span class="bhe-02b__scan" aria-hidden="true"></span><span class="bhe-02b__label">Jack in</span></button>
</section>
</div>
```
## CSS
```css
.bhe-02-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-02-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-02a,
.bhe-02a *,
.bhe-02a *::before,
.bhe-02a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-02a {
  --cyan: #22e3ff;
  --mag: #ff2bd6;
  font-family: 'Chakra Petch',ui-monospace,'Segoe UI',monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #07060f;
}

.bhe-02a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: #eafcff;
  padding: 18px 40px;
  border: 1px solid var(--cyan);
  border-radius: 4px;
  cursor: pointer;
  background: #0d0b1f;
  box-shadow: 0 0 0 1px rgba(34,227,255,.2),0 0 24px -8px var(--cyan);
}

.bhe-02a__grid {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(90deg,rgba(34,227,255,.16) 0 1px,transparent 1px 22px),repeating-linear-gradient(0deg,rgba(255,43,214,.14) 0 1px,transparent 1px 22px);
  opacity: .5;
  z-index: -1;
}

.bhe-02a__label {
  position: relative;
  z-index: 1;
}

.bhe-02a__btn::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font: inherit;
  letter-spacing: .22em;
  color: #eafcff;
  text-shadow: 2px 0 var(--mag),-2px 0 var(--cyan);
  opacity: 0;
  clip-path: inset(0 0 55% 0);
  z-index: 2;
  pointer-events: none;
}

.bhe-02a__btn:hover {
  box-shadow: 0 0 0 1px var(--cyan),0 0 34px -6px var(--cyan),0 0 34px -6px var(--mag);
}

.bhe-02a__btn:hover .bhe-02a__grid {
  opacity: .95;
  animation: bhe-02a-tear .5s steps(5) infinite;
}

.bhe-02a__btn:hover::after {
  opacity: .9;
  animation: bhe-02a-glitch .45s steps(4) infinite;
}

.bhe-02a__btn:focus-visible {
  outline: 3px solid var(--cyan);
  outline-offset: 3px;
}

@keyframes bhe-02a-tear {
  0% {
    background-position: 0 0,0 0;
  }

  40% {
    background-position: 6px -4px,-5px 3px;
  }

  70% {
    background-position: -4px 5px,7px -6px;
  }

  100% {
    background-position: 0 0,0 0;
  }
}

@keyframes bhe-02a-glitch {
  0% {
    transform: translate(0);
    clip-path: inset(0 0 60% 0);
  }

  30% {
    transform: translate(-3px,1px);
    clip-path: inset(50% 0 10% 0);
  }

  60% {
    transform: translate(3px,-1px);
    clip-path: inset(20% 0 40% 0);
  }

  100% {
    transform: translate(0);
    clip-path: inset(0 0 60% 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-02a__btn:hover .bhe-02a__grid,
    .bhe-02a__btn:hover::after {
    animation: none;
  }

  .bhe-02a__btn:hover::after {
    opacity: 0;
  }
}

.bhe-02b,
.bhe-02b *,
.bhe-02b *::before,
.bhe-02b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-02b {
  --grn: #39ff88;
  font-family: ui-monospace,'Segoe UI',monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #04100a;
}

.bhe-02b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--grn);
  padding: 18px 40px;
  border: 1px solid var(--grn);
  border-radius: 4px;
  cursor: pointer;
  background: #07160e;
  box-shadow: 0 0 20px -8px var(--grn);
}

.bhe-02b__label {
  position: relative;
  z-index: 1;
}

.bhe-02b__scan {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg,rgba(57,255,136,.14) 0 2px,transparent 2px 4px);
  opacity: .4;
  z-index: 0;
}

.bhe-02b__btn:hover {
  box-shadow: 0 0 30px -4px var(--grn),inset 0 0 20px -6px var(--grn);
}

.bhe-02b__btn:hover .bhe-02b__scan {
  opacity: .9;
  animation: bhe-02b-roll .6s steps(6) infinite;
}

.bhe-02b__btn:hover .bhe-02b__label {
  animation: bhe-02b-jit .3s steps(3) infinite;
}

.bhe-02b__btn:focus-visible {
  outline: 3px solid var(--grn);
  outline-offset: 3px;
}

@keyframes bhe-02b-roll {
  to {
    background-position: 0 8px;
  }
}

@keyframes bhe-02b-jit {
  0%,
    100% {
    transform: translateX(0);
  }

  50% {
    transform: translateX(1.5px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-02b__btn:hover .bhe-02b__scan,
    .bhe-02b__btn:hover .bhe-02b__label {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
