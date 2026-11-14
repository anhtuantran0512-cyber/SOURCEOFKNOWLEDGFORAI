---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/bouncy-pebble-organic-toggle/"
title: "Bouncy Pebble Organic Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A soft river pebble instead of a circle: the asymmetric blob thumb squashes flat as it launches, stretches mid-flight and wobbles back into shape on landing…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncy Pebble Organic Toggle
Source: https://codefronts.com/components/css-toggles-switches/bouncy-pebble-organic-toggle/

A soft river pebble instead of a circle: the asymmetric blob thumb squashes flat as it launches, stretches mid-flight and wobbles back into shape on landing — squash-and-stretch cartoon physics from one keyframe block, in a warm organic palette.
## HTML
```html
<section class="tgl-25" aria-label="Bouncy pebble organic toggle">
  <label class="tgl-25__row" for="tgl-25-sw">
    <span class="tgl-25__lbl">Rain sounds</span>
    <input type="checkbox" id="tgl-25-sw" class="tgl-25__sw" role="switch">
  </label>
  <p class="tgl-25__cap">Squash · stretch · wobble</p>
</section>
```
## CSS
```css
.tgl-25,
.tgl-25 *,
.tgl-25 *::before,
.tgl-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-25 {
  --on: oklch(0.62 0.1 155);
  --pebble: #f6f2e8;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 26px;
  padding: 60px 20px;
  background: #e9e4d6;
}

.tgl-25__row {
  display: flex;
  align-items: center;
  gap: 32px;
  cursor: pointer;
  background: #f3efe3;
  border-radius: 22px;
  padding: 20px 28px;
  box-shadow: 0 12px 30px -20px rgba(90,80,50,.55);
}

.tgl-25__lbl {
  font-size: 16px;
  font-weight: 600;
  color: #4c4a3c;
}

.tgl-25__sw {
  appearance: none;
  -webkit-appearance: none;
  flex: none;
  width: 82px;
  height: 44px;
  border-radius: 26px;
  background: #d8d2bf;
  position: relative;
  cursor: pointer;
  transition: background-color .5s;
}

.tgl-25__sw:checked {
  background: var(--on);
}

.tgl-25__sw::before {
  content: "";
  position: absolute;
  top: 5px;
  left: 5px;
  width: 34px;
  height: 34px;
  border-radius: 40% 60% 55% 45% / 55% 45% 60% 40%;
  background: var(--pebble);
  box-shadow: 0 3px 7px rgba(90,80,50,.4);
  animation: tgl-25-back .55s cubic-bezier(.3,.7,.4,1) forwards;
}

.tgl-25__sw:checked::before {
  animation: tgl-25-go .55s cubic-bezier(.3,.7,.4,1) forwards;
  border-radius: 60% 40% 45% 55% / 45% 55% 40% 60%;
}

@keyframes tgl-25-go {
  0% {
    transform: translateX(0) scale(1,1);
  }

  15% {
    transform: translateX(-3px) scale(.85,1.12);
  }

  45% {
    transform: translateX(20px) scale(1.28,.76);
  }

  70% {
    transform: translateX(38px) scale(.9,1.08);
  }

  85% {
    transform: translateX(38px) scale(1.06,.95);
  }

  100% {
    transform: translateX(38px) scale(1,1);
  }
}

@keyframes tgl-25-back {
  0% {
    transform: translateX(38px) scale(1,1);
  }

  15% {
    transform: translateX(41px) scale(.85,1.12);
  }

  45% {
    transform: translateX(18px) scale(1.28,.76);
  }

  70% {
    transform: translateX(0) scale(.9,1.08);
  }

  85% {
    transform: translateX(0) scale(1.06,.95);
  }

  100% {
    transform: translateX(0) scale(1,1);
  }
}

.tgl-25__sw:focus-visible {
  outline: 3px solid var(--on);
  outline-offset: 4px;
}

.tgl-25__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #a29a80;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-25__sw::before {
    animation: none;
    transition: transform .2s;
  }

  .tgl-25__sw:checked::before {
    transform: translateX(38px);
  }
}
```

## JavaScript
```js
/* No JavaScript — paired check/uncheck keyframes choreograph anticipate, mid-flight stretch and landing wobble on the blob thumb's transform. */
```
