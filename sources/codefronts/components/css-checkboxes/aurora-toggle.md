---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/aurora-toggle/"
title: "Aurora Toggle"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A premium switch that, when flipped on, fills its track with a slow, shifting northern-lights gradient mesh."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Toggle
Source: https://codefronts.com/components/css-checkboxes/aurora-toggle/

A premium switch that, when flipped on, fills its track with a slow, shifting northern-lights gradient mesh. The kind of detail that makes a SaaS settings page or landing hero feel expensive — and it's entirely CSS.
## HTML
```html
<section class="cb-29" aria-label="Aurora toggle switches">
  <div class="cb-29__stack">
    <label class="cb-29__row"><span class="cb-29__name">Aurora theme</span>
      <input type="checkbox" class="cb-29__input" checked>
      <span class="cb-29__track"><span class="cb-29__mesh" aria-hidden="true"></span><span class="cb-29__thumb"></span></span>
    </label>
    <label class="cb-29__row"><span class="cb-29__name">Cinematic mode</span>
      <input type="checkbox" class="cb-29__input">
      <span class="cb-29__track"><span class="cb-29__mesh" aria-hidden="true"></span><span class="cb-29__thumb"></span></span>
    </label>
    <label class="cb-29__row"><span class="cb-29__name">Ambient glow</span>
      <input type="checkbox" class="cb-29__input" checked>
      <span class="cb-29__track"><span class="cb-29__mesh" aria-hidden="true"></span><span class="cb-29__thumb"></span></span>
    </label>
  </div>
</section>
```
## CSS
```css
.cb-29,
.cb-29 *,
.cb-29 *::before,
.cb-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-29 ::selection {
  background: #5effd0;
  color: #04150f;
}

.cb-29 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0c1018;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-29__stack {
  width: min(400px,100%);
  display: flex;
  flex-direction: column;
  gap: 6px;
  background: #141a26;
  border: 1px solid #232b3d;
  border-radius: 16px;
  padding: 12px 18px;
}

.cb-29__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  cursor: pointer;
  padding: 15px 4px;
}

.cb-29__name {
  font-size: 14.5px;
  font-weight: 500;
  color: #c3cad9;
}

.cb-29__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.cb-29__track {
  --w: 64px;
  --h: 32px;
  position: relative;
  flex: none;
  width: var(--w);
  height: var(--h);
  border-radius: 999px;
  background: #232a3a;
  overflow: hidden;
  transition: background .4s;
}

.cb-29__mesh {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity .5s;
  background: radial-gradient(60% 120% at 15% 40%,#4d7fff 0%,transparent 60%), radial-gradient(60% 120% at 50% 60%,#5effd0 0%,transparent 55%), radial-gradient(70% 130% at 85% 35%,#c04cff 0%,transparent 60%), linear-gradient(90deg,#0b1f3a,#0a2b33);
  background-size: 220% 220%,220% 220%,220% 220%,100% 100%;
  background-position: 0% 50%;
}

.cb-29__thumb {
  position: absolute;
  top: 3px;
  left: 3px;
  z-index: 1;
  width: calc(var(--h) - 6px);
  height: calc(var(--h) - 6px);
  border-radius: 50%;
  background: #eef3ff;
  box-shadow: 0 2px 6px rgba(0,0,0,.5);
  transition: transform .4s cubic-bezier(.4,.8,.3,1);
}

.cb-29__input:checked ~ .cb-29__track {
  background: #0a1526;
}

.cb-29__input:checked ~ .cb-29__track .cb-29__mesh {
  opacity: 1;
  animation: cb-29-drift 8s ease-in-out infinite;
}

.cb-29__input:checked ~ .cb-29__track .cb-29__thumb {
  transform: translateX(calc(var(--w) - var(--h)));
}

.cb-29__input:focus-visible ~ .cb-29__track {
  outline: 3px solid #5effd0;
  outline-offset: 3px;
}

@keyframes cb-29-drift {
  0%,
    100% {
    background-position: 0% 50%,100% 50%,50% 0%,0 0;
  }

  50% {
    background-position: 100% 50%,0% 50%,50% 100%,0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-29__track,
    .cb-29__thumb,
    .cb-29__mesh {
    transition: none;
  }

  .cb-29__input:checked ~ .cb-29__track .cb-29__mesh {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a layered radial-gradient mesh drifts via background-position when ON. */
```
