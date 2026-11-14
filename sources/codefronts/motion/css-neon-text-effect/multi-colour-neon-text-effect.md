---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/multi-colour-neon-text-effect/"
title: "Multi-Colour Neon Text Effect"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A single headline split into independently-glowing colours — a cyan word beside a pink word beside an amber word — the 'how do I make each word a different…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Colour Neon Text Effect
Source: https://codefronts.com/motion/css-neon-text-effect/multi-colour-neon-text-effect/

A single headline split into independently-glowing colours — a cyan word beside a pink word beside an amber word — the 'how do I make each word a different neon' answer, with each tube keeping its own matching bloom.
## HTML
```html
<div class="cnt-12">
  <h2 class="cnt-12__line">
    <span class="cnt-12__w" style="--c:oklch(0.85 0.15 200);--i:0">STAY</span>
    <span class="cnt-12__w" style="--c:oklch(0.72 0.24 340);--i:1">WEIRD</span>
    <span class="cnt-12__w" style="--c:oklch(0.85 0.18 90);--i:2">TONIGHT</span>
  </h2>
</div>
```
## CSS
```css
.cnt-12,
.cnt-12 *,
.cnt-12 *::before,
.cnt-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-12 ::selection {
  background: oklch(0.72 0.24 340);
  color: #fff;
}

.cnt-12 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(120% 120% at 50% 25%,#100b12,#050406);
}

.cnt-12__line {
  display: flex;
  flex-wrap: wrap;
  gap: .28em;
  justify-content: center;
  font-size: clamp(44px,11vw,104px);
  font-weight: 900;
  line-height: 1;
  letter-spacing: .03em;
}

.cnt-12__w {
  color: var(--c);
  text-shadow: 0 0 5px #fff,0 0 14px var(--c),0 0 32px var(--c),0 0 66px color-mix(in oklch,var(--c) 60%,transparent);
  animation: cnt-12-on 1.4s ease both;
  animation-delay: calc(var(--i) * .28s);
}

@keyframes cnt-12-on {
  0% {
    opacity: .2;
    text-shadow: 0 0 4px color-mix(in oklch,var(--c) 40%,transparent);
  }

  60% {
    opacity: 1;
    text-shadow: 0 0 6px #fff,0 0 18px var(--c),0 0 42px var(--c);
  }

  100% {
    opacity: 1;
    text-shadow: 0 0 5px #fff,0 0 14px var(--c),0 0 32px var(--c),0 0 66px color-mix(in oklch,var(--c) 60%,transparent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-12__w {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — one shared rule reads each word's --c to build its matching glow. */
```
