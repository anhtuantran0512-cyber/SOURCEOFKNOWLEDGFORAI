---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-vintage-typewriter-key-button/"
title: "CSS Vintage Typewriter Key Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A 1930s typewriter keycap on its chrome stem: a concave dished face, a nickel collar, and a full 6px of mechanical travel that collapses the stem's stacked…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Vintage Typewriter Key Button
Source: https://codefronts.com/components/css-buttons/css-vintage-typewriter-key-button/

A 1930s typewriter keycap on its chrome stem: a concave dished face, a nickel collar, and a full 6px of mechanical travel that collapses the stem's stacked shadows on press so the key genuinely descends rather than sliding.
## HTML
```html
<div class="cb-24">
  <div class="cb-24__stage">
    <button class="cb-24__btn" type="button">
      <span class="cb-24__key">
        <span class="cb-24__glyph">Type</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');

.cb-24 {
  --bg: #1d1a16;
  --cap: #efe9dc;
  --cap-lo: #cfc7b6;
  --ink: #211d18;
  --collar: #c8c3ba;
  --travel: 5px;
  --slab: "Special Elite",ui-monospace,"Courier New",Courier,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(36rem 22rem at 50% 38%, color-mix(in oklab,#f0e6cf 12%,transparent), transparent 70%), var(--bg);
  font-family: var(--slab);
}

@supports (color: oklch(50% 0 0)) {
  .cb-24 {
    --cap: oklch(93% .016 88);
    --cap-lo: oklch(82% .02 88);
    --ink: oklch(22% .012 70);
  }
}

@media (prefers-color-scheme: light) {
  .cb-24:not([data-theme="dark"]) {
    --bg: #332c24;
  }
}

.cb-24[data-theme="light"] {
  --bg: #332c24;
}

.cb-24,
.cb-24 *,
.cb-24 *::before,
.cb-24 *::after {
  box-sizing: border-box;
}

.cb-24__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-24__btn {
  position: relative;
  cursor: pointer;
  border: 0;
  background: transparent;
  padding: 0 0 var(--travel);
  font: inherit;
  color: var(--ink);
  -webkit-tap-highlight-color: transparent;
}

.cb-24__key {
  display: grid;
  place-items: center;
  min-width: 6.5rem;
  min-height: 3.5rem;
  padding: .5rem 1.35rem;
  border-radius: 1.6rem;
  background: radial-gradient(120% 90% at 50% 118%, rgba(0,0,0,.16), transparent 58%), radial-gradient(120% 80% at 50% -14%, rgba(255,255,255,.75), transparent 60%), linear-gradient(180deg, var(--cap), var(--cap-lo));
  box-shadow: inset 0 0 0 2px var(--collar), inset 0 -2px 3px rgba(0,0,0,.18), 0 1px 0 #b9b2a6, 0 2px 0 #a79f93, 0 3px 0 #948c81, 0 4px 0 #7f776d, 0 5px 0 #6a635b, 0 12px 18px -8px rgba(0,0,0,.65);
  transition: translate .1s ease, box-shadow .1s ease;
}

.cb-24__glyph {
  font-size: 1.0625rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink);
  text-shadow: 0 1px 0 rgba(255,255,255,.65);
}

.cb-24__btn:hover .cb-24__key {
  translate: 0 -1px;
}

.cb-24__btn:active .cb-24__key {
  translate: 0 var(--travel);
  box-shadow: inset 0 0 0 2px var(--collar), inset 0 3px 6px rgba(0,0,0,.3), 0 1px 0 #948c81, 0 3px 6px -3px rgba(0,0,0,.6);
}

.cb-24__btn:focus-visible {
  outline: none;
}

.cb-24__btn:focus-visible .cb-24__key {
  outline: 2px solid #d9b061;
  outline-offset: 4px;
}

.cb-24__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.5) brightness(.9);
  opacity: .7;
}

@media (prefers-reduced-motion: reduce) {
  .cb-24__key {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-24__key {
    background: ButtonFace;
    box-shadow: none;
    border: 1px solid ButtonText;
  }

  .cb-24__glyph {
    color: ButtonText;
    text-shadow: none;
  }
}
```
