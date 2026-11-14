---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/glitch-grid/"
title: "CSS Filter Button Group with RGB-Split Glitch Active State (Cyberpunk Toggle)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A filter button group with a cyberpunk twist: selecting a filter fires a brief RGB-split glitch — the label tears into cyan and magenta ghosts, jitters…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Filter Button Group with RGB-Split Glitch Active State (Cyberpunk Toggle)
Source: https://codefronts.com/components/css-button-groups/glitch-grid/

A filter button group with a cyberpunk twist: selecting a filter fires a brief RGB-split glitch — the label tears into cyan and magenta ghosts, jitters through clip-path slices, then locks into a neon active state. The head-turning 'CSS RGB-split glitch active state button group' for gaming, music and creative-tool UIs.
## HTML
```html
<section class="btn-22" aria-label="RGB-split glitch filter group demo">
  <div class="btn-22__wrap">
    <p class="btn-22__label">Audio filter</p>
    <div class="btn-22__group" role="radiogroup" aria-label="Audio filter">
      <input type="radio" name="btn-22" id="btn-22-1" class="btn-22__in" checked>
      <label for="btn-22-1" class="btn-22__btn" data-txt="CLEAN">CLEAN</label>
      <input type="radio" name="btn-22" id="btn-22-2" class="btn-22__in">
      <label for="btn-22-2" class="btn-22__btn" data-txt="BASS">BASS</label>
      <input type="radio" name="btn-22" id="btn-22-3" class="btn-22__in">
      <label for="btn-22-3" class="btn-22__btn" data-txt="VOCAL">VOCAL</label>
      <input type="radio" name="btn-22" id="btn-22-4" class="btn-22__in">
      <label for="btn-22-4" class="btn-22__btn" data-txt="LO-FI">LO-FI</label>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-22,
.btn-22 *,
.btn-22 *::before,
.btn-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-22 {
  --accent: oklch(0.78 0.2 155);
  font-family: ui-monospace,'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #050506;
  padding: 44px 20px;
}

.btn-22__wrap {
  width: min(520px,100%);
}

.btn-22__label {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: #5a5a62;
  margin: 0 0 16px 2px;
}

.btn-22__group {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 10px;
}

.btn-22__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-22__btn {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 52px;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: .1em;
  color: #7d7d86;
  background: #101014;
  border: 1.5px solid #22222a;
  border-radius: 10px;
  cursor: pointer;
  transition: color .2s,border-color .2s,background .2s;
}

.btn-22__btn::before,
.btn-22__btn::after {
  content: attr(data-txt);
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
}

.btn-22__btn::before {
  color: #00f6ff;
}

.btn-22__btn::after {
  color: #ff2bd0;
}

.btn-22__btn:hover {
  color: #c7c7d0;
  border-color: #33333f;
}

.btn-22__in:checked + .btn-22__btn {
  color: var(--accent);
  border-color: var(--accent);
  background: #0c1410;
  text-shadow: 0 0 10px color-mix(in oklab,var(--accent) 70%,transparent);
  box-shadow: 0 0 20px -8px var(--accent),inset 0 0 12px -8px var(--accent);
  animation: btn-22-glitch .45s steps(2,end);
}

.btn-22__in:checked + .btn-22__btn::before {
  animation: btn-22-c .45s steps(2,end);
}

.btn-22__in:checked + .btn-22__btn::after {
  animation: btn-22-m .45s steps(2,end);
}

@keyframes btn-22-glitch {
  0% {
    clip-path: inset(0 0 0 0);
  }

  20% {
    clip-path: inset(20% 0 55% 0);
  }

  40% {
    clip-path: inset(65% 0 12% 0);
  }

  60% {
    clip-path: inset(35% 0 40% 0);
  }

  80% {
    clip-path: inset(10% 0 75% 0);
  }

  100% {
    clip-path: inset(0 0 0 0);
  }
}

@keyframes btn-22-c {
  0%,
    100% {
    opacity: 0;
    translate: 0 0;
  }

  15% {
    opacity: .9;
    translate: -4px -2px;
  }

  45% {
    opacity: .9;
    translate: 3px 1px;
  }

  70% {
    opacity: .6;
    translate: -2px 2px;
  }
}

@keyframes btn-22-m {
  0%,
    100% {
    opacity: 0;
    translate: 0 0;
  }

  15% {
    opacity: .9;
    translate: 4px 2px;
  }

  45% {
    opacity: .9;
    translate: -3px -1px;
  }

  70% {
    opacity: .6;
    translate: 2px -2px;
  }
}

.btn-22__in:focus-visible + .btn-22__btn {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-22__in:checked + .btn-22__btn,
    .btn-22__in:checked + .btn-22__btn::before,
    .btn-22__in:checked + .btn-22__btn::after {
    animation: none;
  }

  .btn-22__btn::before,
    .btn-22__btn::after {
    display: none;
  }
}
```
