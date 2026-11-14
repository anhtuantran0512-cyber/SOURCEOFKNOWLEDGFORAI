---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/modal-corner/"
title: "Overlay Lightbox Media Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The fullscreen photo-viewer dismiss: a frosted dark circle floating at the safe-area corner of a lightbox, backdrop-filter blurring whatever chaos the media…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Overlay Lightbox Media Close Button
Source: https://codefronts.com/components/css-close-buttons/modal-corner/

The fullscreen photo-viewer dismiss: a frosted dark circle floating at the safe-area corner of a lightbox, backdrop-filter blurring whatever chaos the media puts behind it, with a hairline border for definition against both bright skies and black bars. The Instagram/Facebook media-overlay pattern, extracted.
## HTML
```html
<section class="ccb-26" aria-label="Lightbox media close button demo">
  <div class="ccb-26__lightbox" role="dialog" aria-label="Photo viewer">
    <div class="ccb-26__photo" aria-hidden="true"></div>
    <button class="ccb-26__close" type="button" aria-label="Close photo viewer">
      <span class="ccb-26__x" aria-hidden="true"></span>
    </button>
    <span class="ccb-26__caption">Golden hour, Big Sur</span>
  </div>
</section>
```
## CSS
```css
.ccb-26,
.ccb-26 *,
.ccb-26 *::before,
.ccb-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-26 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.12 0.01 280);
}

.ccb-26 .ccb-26__lightbox {
  position: relative;
  width: min(420px,100%);
  aspect-ratio: 16/10;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 30px 70px -30px rgba(0,0,0,.9);
}

.ccb-26 .ccb-26__photo {
  position: absolute;
  inset: 0;
  background: radial-gradient(70% 60% at 78% 18%,oklch(0.98 0.03 90),oklch(0.85 0.12 70) 30%,transparent 60%),linear-gradient(190deg,oklch(0.75 0.13 60) 0%,oklch(0.55 0.14 40) 38%,oklch(0.3 0.08 290) 70%,oklch(0.16 0.03 280) 100%);
}

.ccb-26 .ccb-26__close {
  position: absolute;
  top: max(14px,env(safe-area-inset-top));
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border: 1px solid rgba(255,255,255,.18);
  border-radius: 50%;
  background: rgba(20,20,24,.55);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  cursor: pointer;
  transition: background-color .18s ease,transform .18s ease;
}

.ccb-26 .ccb-26__close:hover {
  background: rgba(20,20,24,.75);
}

.ccb-26 .ccb-26__close:active {
  transform: scale(.92);
}

.ccb-26 .ccb-26__close:focus-visible {
  outline: 2.5px solid #fff;
  outline-offset: 2px;
}

.ccb-26 .ccb-26__x {
  position: relative;
  width: 16px;
  height: 16px;
}

.ccb-26 .ccb-26__x::before,
.ccb-26 .ccb-26__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 16px;
  height: 1.8px;
  border-radius: 2px;
  background: rgba(255,255,255,.95);
}

.ccb-26 .ccb-26__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-26 .ccb-26__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-26 .ccb-26__caption {
  position: absolute;
  bottom: 14px;
  left: 16px;
  font-size: 12px;
  color: rgba(255,255,255,.85);
  text-shadow: 0 1px 8px rgba(0,0,0,.6);
}

@media (prefers-reduced-motion: reduce) {
  .ccb-26 .ccb-26__close {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — dark fill + backdrop blur + hairline border: three layers that stay legible over any photo; env() clears the notch. */
```
