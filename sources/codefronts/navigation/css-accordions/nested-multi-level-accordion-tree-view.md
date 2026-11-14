---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/nested-multi-level-accordion-tree-view/"
title: "Nested Multi-Level Accordion (CSS Tree View for Docs & File Explorers)"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Three levels of <details> nested like a file explorer: folder chevrons, connector tree-lines drawn with borders, per-level indentation and file-type dots —…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nested Multi-Level Accordion (CSS Tree View for Docs & File Explorers)
Source: https://codefronts.com/navigation/css-accordions/nested-multi-level-accordion-tree-view/

Three levels of <details> nested like a file explorer: folder chevrons, connector tree-lines drawn with borders, per-level indentation and file-type dots — the recursive structure devs need for documentation sidebars, org charts and directory browsers, with hierarchy you can read at a glance.
## HTML
```html
<section class="acc-04" aria-label="Nested multi-level accordion tree demo">
  <div class="acc-04__panel">
    <p class="acc-04__crumb">docs / <b>design-system</b></p>
    <details class="acc-04__branch" open>
      <summary class="acc-04__folder">Foundations</summary>
      <div class="acc-04__kids">
        <details class="acc-04__branch" open>
          <summary class="acc-04__folder">Color</summary>
          <div class="acc-04__kids">
            <a href="#" class="acc-04__leaf" style="--dot:#5b8def">palette.md</a>
            <a href="#" class="acc-04__leaf" style="--dot:#5b8def">semantic-tokens.md</a>
            <a href="#" class="acc-04__leaf" style="--dot:#e0a63c">contrast-audit.xlsx</a>
          </div>
        </details>
        <details class="acc-04__branch">
          <summary class="acc-04__folder">Typography</summary>
          <div class="acc-04__kids">
            <a href="#" class="acc-04__leaf" style="--dot:#5b8def">type-scale.md</a>
            <a href="#" class="acc-04__leaf" style="--dot:#c95ddb">specimens.fig</a>
          </div>
        </details>
        <a href="#" class="acc-04__leaf" style="--dot:#5b8def">spacing.md</a>
      </div>
    </details>
    <details class="acc-04__branch">
      <summary class="acc-04__folder">Components</summary>
      <div class="acc-04__kids">
        <details class="acc-04__branch">
          <summary class="acc-04__folder">Forms</summary>
          <div class="acc-04__kids">
            <a href="#" class="acc-04__leaf" style="--dot:#5b8def">inputs.md</a>
            <a href="#" class="acc-04__leaf" style="--dot:#5b8def">validation.md</a>
          </div>
        </details>
        <a href="#" class="acc-04__leaf" style="--dot:#5b8def">accordion.md</a>
        <a href="#" class="acc-04__leaf" style="--dot:#5b8def">navigation.md</a>
      </div>
    </details>
    <details class="acc-04__branch">
      <summary class="acc-04__folder">Release notes</summary>
      <div class="acc-04__kids">
        <a href="#" class="acc-04__leaf" style="--dot:#54b06d">v3.2.0.md</a>
        <a href="#" class="acc-04__leaf" style="--dot:#54b06d">v3.1.4.md</a>
      </div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-04,
.acc-04 *,
.acc-04 *::before,
.acc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-04 {
  --accent: oklch(0.55 0.15 265);
  --line: #dcdfeb;
  --indent: 22px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eef0f6;
  padding: 40px 20px;
}

.acc-04__panel {
  width: min(380px,100%);
  background: #fff;
  border-radius: 16px;
  padding: 22px 20px 26px;
  box-shadow: 0 24px 60px -34px rgba(30,35,80,.35);
}

.acc-04__crumb {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: #8a90a8;
  margin-bottom: 12px;
}

.acc-04__crumb b {
  color: #2a3050;
}

.acc-04__folder {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 9px;
  min-height: 40px;
  padding: 0 8px;
  font-size: 14.5px;
  font-weight: 600;
  color: #2a3050;
  cursor: pointer;
  border-radius: 8px;
  transition: background .15s;
}

.acc-04__folder::-webkit-details-marker {
  display: none;
}

.acc-04__folder::marker {
  content: "";
}

.acc-04__folder:hover {
  background: #f3f5fa;
}

.acc-04__folder::before {
  content: "";
  width: 7px;
  height: 7px;
  border-right: 2px solid #9aa1bd;
  border-bottom: 2px solid #9aa1bd;
  transform: rotate(-45deg);
  transition: transform .2s;
  flex: none;
  margin-left: 2px;
}

.acc-04__branch[open] > .acc-04__folder::before {
  transform: rotate(45deg);
}

.acc-04__branch[open] > .acc-04__folder {
  font-weight: 750;
  color: var(--accent);
}

.acc-04__kids {
  margin-left: var(--indent);
  border-left: 1.5px solid var(--line);
  padding-left: 6px;
  display: flex;
  flex-direction: column;
}

.acc-04__leaf {
  display: flex;
  align-items: center;
  gap: 9px;
  min-height: 38px;
  padding: 0 8px;
  font-size: 13.5px;
  color: #4b5270;
  text-decoration: none;
  border-radius: 8px;
  transition: background .15s;
}

.acc-04__leaf:hover {
  background: #f3f5fa;
  color: var(--accent);
}

.acc-04__leaf::before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--dot,#9aa1bd);
  flex: none;
  margin-left: 1px;
}

.acc-04__folder:focus-visible,
.acc-04__leaf:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 1px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-04__folder::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — details elements nest recursively; indentation + border-left connector lines make depth legible, and the same classes work at every level. */
```
