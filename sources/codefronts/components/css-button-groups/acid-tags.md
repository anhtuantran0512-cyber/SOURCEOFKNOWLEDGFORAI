---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/acid-tags/"
title: "CSS Multi-Select Chip Buttons with Acid Glow (Toggleable Tag Filters)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "Multi-select filter chips with an electric acid-green glow: tap to toggle any number on, each active chip lights up with a neon halo, a text glow and a check."
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Multi-Select Chip Buttons with Acid Glow (Toggleable Tag Filters)
Source: https://codefronts.com/components/css-button-groups/acid-tags/

Multi-select filter chips with an electric acid-green glow: tap to toggle any number on, each active chip lights up with a neon halo, a text glow and a check. The high-energy 'CSS multi-select chip buttons acid glow' pattern for tag filters, skill pickers and faceted search — built on real checkboxes so state is genuine and accessible.
## HTML
```html
<section class="btn-14" aria-label="Acid glow multi-select chips demo">
  <div class="btn-14__wrap">
    <p class="btn-14__label">Stack — select all that apply</p>
    <div class="btn-14__chips" role="group" aria-label="Tech stack filters">
      <input type="checkbox" id="btn-14-1" class="btn-14__in" checked>
      <label for="btn-14-1" class="btn-14__chip">TypeScript</label>
      <input type="checkbox" id="btn-14-2" class="btn-14__in">
      <label for="btn-14-2" class="btn-14__chip">Rust</label>
      <input type="checkbox" id="btn-14-3" class="btn-14__in" checked>
      <label for="btn-14-3" class="btn-14__chip">WebGPU</label>
      <input type="checkbox" id="btn-14-4" class="btn-14__in">
      <label for="btn-14-4" class="btn-14__chip">Edge Functions</label>
      <input type="checkbox" id="btn-14-5" class="btn-14__in">
      <label for="btn-14-5" class="btn-14__chip">Vector DB</label>
      <input type="checkbox" id="btn-14-6" class="btn-14__in" checked>
      <label for="btn-14-6" class="btn-14__chip">WASM</label>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-14,
.btn-14 *,
.btn-14 *::before,
.btn-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-14 {
  --acid: oklch(0.87 0.24 130);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 50% 0%,#0c1108,#050703);
  padding: 44px 20px;
}

.btn-14__wrap {
  width: min(560px,100%);
}

.btn-14__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--acid);
  margin: 0 0 16px 2px;
}

.btn-14__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.btn-14__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-14__chip {
  position: relative;
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 18px;
  font-size: 14.5px;
  font-weight: 700;
  color: #8a9a7e;
  background: rgba(255,255,255,.03);
  border: 1.5px solid #253019;
  border-radius: 999px;
  cursor: pointer;
  transition: color .2s,border-color .2s,filter .2s,background .2s;
}

.btn-14__chip::before {
  content: "";
  width: 15px;
  height: 15px;
  border-radius: 50%;
  border: 2px solid #3a4a2a;
  transition: all .2s;
  flex: none;
}

.btn-14__chip:hover {
  filter: saturate(1.4);
  color: #c7dab3;
  border-color: #3f5228;
}

.btn-14__in:checked + .btn-14__chip {
  color: #0a1204;
  background: var(--acid);
  border-color: var(--acid);
  text-shadow: 0 0 8px rgba(255,255,255,.5);
  box-shadow: 0 0 0 1px var(--acid),0 0 22px -2px var(--acid),0 0 46px 2px color-mix(in oklab,var(--acid) 45%,transparent);
}

.btn-14__in:checked + .btn-14__chip::before {
  background: #0a1204;
  border-color: #0a1204;
  box-shadow: inset 0 0 0 2px var(--acid);
}

.btn-14__in:focus-visible + .btn-14__chip {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-14__chip,
    .btn-14__chip::before {
    transition: none;
  }
}
```
