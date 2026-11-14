---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/brutalist-stamp/"
title: "Brutalist Stamp Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "Neo-brutalism's signature move on a close button: thick 3px black border, flat acid-yellow fill, zero border-radius apology, and a hard offset shadow the…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Stamp Close Button
Source: https://codefronts.com/components/css-close-buttons/brutalist-stamp/

Neo-brutalism's signature move on a close button: thick 3px black border, flat acid-yellow fill, zero border-radius apology, and a hard offset shadow the button physically travels into — hover lifts it to -4px,-4px with the shadow growing to match; press SLAMS it flush with the surface. No blur anywhere; blur is fear.
## HTML
```html
<section class="ccb-27" aria-label="Brutalist close button demo">
  <div class="ccb-27__card">
    <div class="ccb-27__head">
      <span class="ccb-27__tag">NOTICE №4</span>
      <button class="ccb-27__close" type="button" aria-label="Close notice">
        <span class="ccb-27__x" aria-hidden="true"></span>
      </button>
    </div>
    <p class="ccb-27__text">Your free trial ends in 3 days.</p>
  </div>
</section>
```
## CSS
```css
.ccb-27,
.ccb-27 *,
.ccb-27 *::before,
.ccb-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-27 {
  --paper: oklch(0.9 0.18 100);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.93 0.005 90);
}

.ccb-27 .ccb-27__card {
  width: min(340px,100%);
  background: #fff;
  border: 3px solid #000;
  box-shadow: 8px 8px 0 #000;
  padding: 20px;
}

.ccb-27 .ccb-27__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 14px;
}

.ccb-27 .ccb-27__tag {
  font: 700 12px/1.2 ui-monospace,Menlo,monospace;
  letter-spacing: .08em;
  background: #000;
  color: var(--paper);
  padding: 6px 8px;
}

.ccb-27 .ccb-27__text {
  font-size: 14px;
  line-height: 1.5;
  color: #000;
}

.ccb-27 .ccb-27__close {
  position: relative;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  flex-shrink: 0;
  border: 3px solid #000;
  background: var(--paper);
  cursor: pointer;
  box-shadow: 4px 4px 0 #000;
  transition: transform .1s ease-out,box-shadow .1s ease-out;
}

.ccb-27 .ccb-27__close:hover {
  transform: translate(-4px,-4px);
  box-shadow: 8px 8px 0 #000;
}

.ccb-27 .ccb-27__close:active {
  transform: translate(4px,4px);
  box-shadow: 0 0 0 #000;
}

.ccb-27 .ccb-27__close:focus-visible {
  outline: 3px solid #000;
  outline-offset: 3px;
}

.ccb-27 .ccb-27__x {
  position: relative;
  width: 18px;
  height: 18px;
}

.ccb-27 .ccb-27__x::before,
.ccb-27 .ccb-27__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 4px;
  background: #000;
}

.ccb-27 .ccb-27__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-27 .ccb-27__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

@media (prefers-reduced-motion: reduce) {
  .ccb-27 .ccb-27__close {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — transform and a zero-blur shadow move in opposition: lift grows the shadow, press slams both flat. */
```
