---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-segmented-control-with-sliding-thumb-indicator-ios-style-pure-css/"
title: "CSS Segmented Control with Sliding Thumb Indicator (iOS-Style, Pure CSS)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "The iOS/macOS segmented control, rebuilt in pure CSS: three or four options with one animated thumb that glides beneath the selected label."
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Segmented Control with Sliding Thumb Indicator (iOS-Style, Pure CSS)
Source: https://codefronts.com/components/css-button-groups/css-segmented-control-with-sliding-thumb-indicator-ios-style-pure-css/

The iOS/macOS segmented control, rebuilt in pure CSS: three or four options with one animated thumb that glides beneath the selected label. The go-to 'CSS segmented control sliding thumb indicator' component for view switchers, filters and settings — accessible radio semantics, arrow-key support, and a thumb that never breaks alignment because it's sized by the grid itself.
## HTML
```html
<section class="btn-05" aria-label="Segmented control sliding thumb demo">
  <div class="btn-05__wrap">
    <p class="btn-05__label">Timeframe</p>
    <div class="btn-05__seg" role="group" aria-label="Chart timeframe">
      <input type="radio" name="btn-05" id="btn-05-1" class="btn-05__in" checked>
      <label for="btn-05-1" class="btn-05__opt">Day</label>
      <input type="radio" name="btn-05" id="btn-05-2" class="btn-05__in">
      <label for="btn-05-2" class="btn-05__opt">Week</label>
      <input type="radio" name="btn-05" id="btn-05-3" class="btn-05__in">
      <label for="btn-05-3" class="btn-05__opt">Month</label>
      <input type="radio" name="btn-05" id="btn-05-4" class="btn-05__in">
      <label for="btn-05-4" class="btn-05__opt">Year</label>
      <span class="btn-05__thumb" aria-hidden="true"></span>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-05,
.btn-05 *,
.btn-05 *::before,
.btn-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-05 {
  --accent: oklch(0.55 0.2 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#f5f2ff,#efeaff 60%,#e7dfff);
  padding: 44px 20px;
}

.btn-05__wrap {
  width: min(520px,100%);
}

.btn-05__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 12px 4px;
}

.btn-05__seg {
  position: relative;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  padding: 5px;
  background: #fff;
  border: 1px solid #e6def9;
  border-radius: 16px;
  box-shadow: 0 18px 44px -30px rgba(60,20,120,.6);
}

.btn-05__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-05__opt {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  font-size: 15px;
  font-weight: 650;
  color: #5b4b86;
  cursor: pointer;
  transition: color .25s;
  border-radius: 11px;
}

.btn-05__thumb {
  position: absolute;
  z-index: 0;
  top: 5px;
  left: 5px;
  width: calc((100% - 10px)/4);
  height: calc(100% - 10px);
  background: var(--accent);
  border-radius: 11px;
  box-shadow: 0 6px 16px -6px var(--accent);
  transition: translate .4s cubic-bezier(.34,1.4,.5,1);
}

.btn-05__seg:has(#btn-05-2:checked) .btn-05__thumb {
  translate: 100% 0;
}

.btn-05__seg:has(#btn-05-3:checked) .btn-05__thumb {
  translate: 200% 0;
}

.btn-05__seg:has(#btn-05-4:checked) .btn-05__thumb {
  translate: 300% 0;
}

.btn-05__in:checked + .btn-05__opt {
  color: #fff;
}

.btn-05__in:focus-visible + .btn-05__opt {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-05__thumb,
    .btn-05__opt {
    transition: none;
  }
}
```
