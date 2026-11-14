---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/liquid-mercury/"
title: "CSS Segmented Control with Liquid Mercury Thumb (Metallic Stretch Animation)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A segmented control whose thumb behaves like a bead of liquid mercury — a chromed, specular-highlit pill that stretches and squashes as it travels between…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Segmented Control with Liquid Mercury Thumb (Metallic Stretch Animation)
Source: https://codefronts.com/components/css-button-groups/liquid-mercury/

A segmented control whose thumb behaves like a bead of liquid mercury — a chromed, specular-highlit pill that stretches and squashes as it travels between options, then settles with a metallic shimmer. A show-stopping 'CSS liquid mercury segmented control' with real radios underneath, so it stays keyboard-operable while looking impossibly fluid.
## HTML
```html
<section class="btn-12" aria-label="Liquid mercury segmented control demo">
  <div class="btn-12__wrap">
    <p class="btn-12__label">Rendering mode</p>
    <div class="btn-12__seg" role="group" aria-label="Rendering mode">
      <input type="radio" name="btn-12" id="btn-12-1" class="btn-12__in" checked>
      <label for="btn-12-1" class="btn-12__opt">Auto</label>
      <input type="radio" name="btn-12" id="btn-12-2" class="btn-12__in">
      <label for="btn-12-2" class="btn-12__opt">Metal</label>
      <input type="radio" name="btn-12" id="btn-12-3" class="btn-12__in">
      <label for="btn-12-3" class="btn-12__opt">Glass</label>
      <span class="btn-12__thumb" aria-hidden="true"></span>
    </div>
  </div>
</section>
```
## CSS
```css
@property --btn-12-sheen {
  syntax: "<angle>";
  inherits: true;
  initial-value: 0deg;
}

.btn-12,
.btn-12 *,
.btn-12 *::before,
.btn-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-12 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 50% 0%,#20242e,#0c0e14);
  padding: 44px 20px;
}

.btn-12__wrap {
  width: min(460px,100%);
}

.btn-12__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #aeb6c9;
  margin: 0 0 14px 4px;
}

.btn-12__seg {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  padding: 6px;
  background: #171a22;
  border: 1px solid #2a2f3c;
  border-radius: 16px;
  box-shadow: inset 0 2px 8px rgba(0,0,0,.6);
}

.btn-12__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-12__opt {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  font-size: 15px;
  font-weight: 700;
  color: #8b93a7;
  cursor: pointer;
  transition: color .3s;
}

.btn-12__thumb {
  position: absolute;
  z-index: 1;
  top: 6px;
  left: 6px;
  width: calc((100% - 12px)/3);
  height: calc(100% - 12px);
  border-radius: 11px;
  background: linear-gradient(var(--btn-12-sheen),#f4f6fb 0%,#c3cad9 30%,#7a8398 55%,#dfe4ee 80%,#f4f6fb 100%);
  box-shadow: 0 4px 14px -4px rgba(0,0,0,.8),inset 0 1px 1px rgba(255,255,255,.9),inset 0 -2px 4px rgba(0,0,0,.3);
  animation: btn-12-sheen 5s linear infinite;
  overflow: hidden;
  transition: translate .5s cubic-bezier(.5,-0.2,.3,1.3);
}

.btn-12__thumb::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(105deg,transparent 35%,rgba(255,255,255,.85) 50%,transparent 65%);
  translate: -120% 0;
  animation: btn-12-glint 5s ease-in-out infinite;
}

@keyframes btn-12-sheen {
  to {
    --btn-12-sheen: 360deg;
  }
}

@keyframes btn-12-glint {
  0%,
    60% {
    translate: -120% 0;
  }

  80%,
    100% {
    translate: 120% 0;
  }
}

.btn-12__seg:has(#btn-12-2:checked) .btn-12__thumb {
  translate: 100% 0;
  animation: btn-12-sheen 5s linear infinite,btn-12-squash .5s ease;
}

.btn-12__seg:has(#btn-12-3:checked) .btn-12__thumb {
  translate: 200% 0;
  animation: btn-12-sheen 5s linear infinite,btn-12-squash .5s ease;
}

@keyframes btn-12-squash {
  40% {
    scale: 1.16 .82;
  }

  70% {
    scale: .94 1.08;
  }

  100% {
    scale: 1 1;
  }
}

.btn-12__in:checked + .btn-12__opt {
  color: #11141c;
  text-shadow: 0 1px 0 rgba(255,255,255,.4);
}

.btn-12__in:focus-visible + .btn-12__opt {
  outline: 3px solid #9fb0ff;
  outline-offset: 3px;
  border-radius: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-12__thumb,
    .btn-12__thumb::after {
    animation: none;
    transition: translate .3s;
  }

  .btn-12__seg:has(.btn-12__in:checked) .btn-12__thumb {
    animation: none;
  }
}
```
