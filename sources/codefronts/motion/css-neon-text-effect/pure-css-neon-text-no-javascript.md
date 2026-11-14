---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/pure-css-neon-text-no-javascript/"
title: "Pure-CSS Neon Text (No JavaScript)"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "The canonical build-it-from-scratch reference: a clean, dependency-free neon headline that layers text-shadow from a tight white core out to a wide coloured…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure-CSS Neon Text (No JavaScript)
Source: https://codefronts.com/motion/css-neon-text-effect/pure-css-neon-text-no-javascript/

The canonical build-it-from-scratch reference: a clean, dependency-free neon headline that layers text-shadow from a tight white core out to a wide coloured bloom — the exact 'no libraries' answer performance-minded devs want.
## HTML
```html
<div class="cnt-13">
  <h2 class="cnt-13__h">no libraries<br><em>just css</em></h2>
</div>
```
## CSS
```css
.cnt-13,
.cnt-13 *,
.cnt-13 *::before,
.cnt-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-13 ::selection {
  background: oklch(0.82 0.15 320);
  color: #12041a;
}

.cnt-13 {
  --accent: oklch(0.82 0.17 320);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #050505;
}

.cnt-13__h {
  font-size: clamp(42px,11vw,104px);
  font-weight: 800;
  line-height: .98;
  text-align: center;
  letter-spacing: .01em;
  color: #fff;
  text-shadow: 0 0 2px #fff, 0 0 10px var(--accent), 0 0 22px var(--accent), 0 0 44px color-mix(in oklch,var(--accent) 70%,transparent), 0 0 90px color-mix(in oklch,var(--accent) 40%,transparent);
}

.cnt-13__h em {
  font-style: italic;
  color: #ffe9fb;
}

@media (prefers-reduced-motion: reduce) {
}
```

## JavaScript
```js
/* No JavaScript — a single five-layer text-shadow, tight core to wide bloom. */
```
