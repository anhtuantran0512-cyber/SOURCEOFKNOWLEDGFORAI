---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/holographic-dial/"
title: "CSS Icon Segmented Control with Holographic Sheen (Iridescent View Switcher)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "An icon segmented control whose active thumb shimmers like a holographic foil card — an iridescent sheen that shifts hue as it catches the light."
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Icon Segmented Control with Holographic Sheen (Iridescent View Switcher)
Source: https://codefronts.com/components/css-button-groups/holographic-dial/

An icon segmented control whose active thumb shimmers like a holographic foil card — an iridescent sheen that shifts hue as it catches the light. A premium 'CSS icon segmented control holographic sheen' view switcher (grid / list / gallery / map) built on real radios, with an @property hue drift so the foil never sits still.
## HTML
```html
<section class="btn-19" aria-label="Holographic icon segmented control demo">
  <div class="btn-19__wrap">
    <p class="btn-19__label">View</p>
    <div class="btn-19__seg" role="radiogroup" aria-label="View mode">
      <input type="radio" name="btn-19" id="btn-19-1" class="btn-19__in" checked>
      <label for="btn-19-1" class="btn-19__opt" aria-label="Grid view"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.1"><rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/></svg></label>
      <input type="radio" name="btn-19" id="btn-19-2" class="btn-19__in">
      <label for="btn-19-2" class="btn-19__opt" aria-label="List view"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01"/></svg></label>
      <input type="radio" name="btn-19" id="btn-19-3" class="btn-19__in">
      <label for="btn-19-3" class="btn-19__opt" aria-label="Gallery view"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.1"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 15l5-4 4 3 3-2 6 5"/><circle cx="9" cy="9" r="1.4"/></svg></label>
      <input type="radio" name="btn-19" id="btn-19-4" class="btn-19__in">
      <label for="btn-19-4" class="btn-19__opt" aria-label="Map view"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2-6-2zM9 4v14M15 6v14"/></svg></label>
      <span class="btn-19__thumb" aria-hidden="true"></span>
    </div>
  </div>
</section>
```
## CSS
```css
@property --btn-19-h {
  syntax: "<angle>";
  inherits: true;
  initial-value: 0deg;
}

.btn-19,
.btn-19 *,
.btn-19 *::before,
.btn-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-19 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 50% 0%,#191426,#0a0710);
  padding: 44px 20px;
}

.btn-19__wrap {
  width: min(420px,100%);
}

.btn-19__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #c9b8ff;
  margin: 0 0 14px 4px;
}

.btn-19__seg {
  position: relative;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  padding: 6px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 16px;
  backdrop-filter: blur(6px);
}

.btn-19__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-19__opt {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 48px;
  color: rgba(230,224,255,.55);
  cursor: pointer;
  transition: color .3s;
}

.btn-19__thumb {
  position: absolute;
  z-index: 1;
  top: 6px;
  left: 6px;
  width: calc((100% - 12px)/4);
  height: calc(100% - 12px);
  border-radius: 11px;
  overflow: hidden;
  background: repeating-linear-gradient(68deg,hsl(var(--btn-19-h) 92% 66%) 0 14px,hsl(calc(var(--btn-19-h) + 60) 92% 66%) 14px 28px,hsl(calc(var(--btn-19-h) + 130) 92% 66%) 28px 42px,hsl(calc(var(--btn-19-h) + 200) 92% 66%) 42px 56px);
  animation: btn-19-drift 6s linear infinite;
  transition: translate .42s cubic-bezier(.34,1.35,.5,1);
  box-shadow: 0 6px 20px -6px hsl(var(--btn-19-h) 90% 60% / .8);
}

.btn-19__thumb::before {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(-58deg,rgba(255,255,255,.5) 0 4px,transparent 4px 16px);
  mix-blend-mode: color-dodge;
  opacity: .55;
}

.btn-19__thumb::after {
  content: "";
  position: absolute;
  inset: -40%;
  background: linear-gradient(110deg,transparent 40%,rgba(255,255,255,.9) 50%,transparent 60%);
  translate: -60% 0;
  animation: btn-19-glare 6s ease-in-out infinite;
}

@keyframes btn-19-drift {
  to {
    --btn-19-h: 360deg;
  }
}

@keyframes btn-19-glare {
  0%,
    55% {
    translate: -80% 0;
  }

  80%,
    100% {
    translate: 80% 0;
  }
}

.btn-19__seg:has(#btn-19-2:checked) .btn-19__thumb {
  translate: 100% 0;
}

.btn-19__seg:has(#btn-19-3:checked) .btn-19__thumb {
  translate: 200% 0;
}

.btn-19__seg:has(#btn-19-4:checked) .btn-19__thumb {
  translate: 300% 0;
}

.btn-19__in:checked + .btn-19__opt {
  color: #1a0d2e;
  mix-blend-mode: hard-light;
}

.btn-19__in:focus-visible + .btn-19__opt {
  outline: 3px solid #fff;
  outline-offset: 3px;
  border-radius: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-19__thumb,
    .btn-19__thumb::after {
    animation: none;
  }

  .btn-19__thumb {
    transition: translate .3s;
  }
}
```
