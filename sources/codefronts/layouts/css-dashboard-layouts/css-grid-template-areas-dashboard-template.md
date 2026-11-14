---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/css-grid-template-areas-dashboard-template/"
title: "CSS Grid template-areas Dashboard Template"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The most readable layout API in CSS, demonstrated on itself: a header/sidebar/main/aside/footer shell whose entire structure is an ASCII picture in…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid template-areas Dashboard Template
Source: https://codefronts.com/layouts/css-dashboard-layouts/css-grid-template-areas-dashboard-template/

The most readable layout API in CSS, demonstrated on itself: a header/sidebar/main/aside/footer shell whose entire structure is an ASCII picture in grid-template-areas — and the demo prints that live picture in its corner. Drag the resize handle: below 660px a second template string rearranges every region (sidebar → icon rail, aside → stacked row) and the printed CSS updates to match. No other layout method lets you *read* the page like this.
## HTML
```html
<section class="cdl-06" aria-label="grid-template-areas boilerplate demo">
  <div class="cdl-06__stage">
    <div class="cdl-06__shell">
      <header class="cdl-06__header"><b>header</b><span class="cdl-06__hint">grid-area: header</span><span class="cdl-06__drag">⤡ drag stage corner</span></header>
      <nav class="cdl-06__sidebar" aria-label="Demo sidebar"><b>sidebar</b>
        <a href="#dash" aria-current="page" class="cdl-06__on"><i aria-hidden="true"></i><span>Dashboard</span></a>
        <a href="#reports"><i aria-hidden="true"></i><span>Reports</span></a>
        <a href="#team"><i aria-hidden="true"></i><span>Team</span></a>
        <a href="#settings"><i aria-hidden="true"></i><span>Settings</span></a>
      </nav>
      <main class="cdl-06__main"><b>main</b>
        <div class="cdl-06__blocks"><span style="--w:72%"></span><span style="--w:94%"></span><span style="--w:58%"></span><span style="--w:86%"></span><span style="--w:66%"></span></div>
      </main>
      <aside class="cdl-06__aside"><b>aside</b>
        <p class="cdl-06__widget">Quota <span class="cdl-06__meter"><i style="--w:64%"></i></span></p>
        <p class="cdl-06__widget">Storage <span class="cdl-06__meter"><i style="--w:38%"></i></span></p>
      </aside>
      <footer class="cdl-06__footer"><b>footer</b>
        <code class="cdl-06__code cdl-06__code--wide">"header header header" · "sidebar main aside" · "footer footer footer"</code>
        <code class="cdl-06__code cdl-06__code--narrow">"header header" · "sidebar main" · "aside aside" · "footer footer"</code>
      </footer>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-06,
.cdl-06 *,
.cdl-06 *::before,
.cdl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-06 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --paper: oklch(0.98 0.006 240);
  --ink: oklch(0.3 0.03 250);
  --mut: oklch(0.56 0.03 250);
  --line: oklch(0.62 0.11 250);
  --fill: oklch(0.95 0.02 250);
  --acc: oklch(0.55 0.17 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cdl-06__stage {
  width: 100%;
  height: 100vh;
  container-type: inline-size;
  resize: horizontal;
  overflow: auto;
  min-width: 340px;
  max-width: 100%;
  border: 1px solid oklch(0.89 0.015 250);
  background: var(--paper);
  padding: 14px;
  box-shadow: inset 0 0 0 1px transparent;
}

.cdl-06__shell {
  height: 100vh;
  display: grid;
  gap: 12px;
  grid-template-columns: 200px minmax(0,1fr) 230px;
  grid-template-rows: 54px minmax(0,1fr) 44px;
  grid-template-areas: "header header header" "sidebar main aside" "footer footer footer";
}

.cdl-06__header {
  grid-area: header;
}

.cdl-06__sidebar {
  grid-area: sidebar;
}

.cdl-06__main {
  grid-area: main;
}

.cdl-06__aside {
  grid-area: aside;
}

.cdl-06__footer {
  grid-area: footer;
}

.cdl-06__shell>* {
  position: relative;
  border: 1.5px dashed color-mix(in oklch,var(--line) 55%,transparent);
  border-radius: 12px;
  background: linear-gradient(150deg,color-mix(in oklch,var(--fill) 70%,white),var(--fill));
  padding: 12px 14px;
  transition: border-color .2s,background .2s;
}

.cdl-06__shell>*:hover {
  border-color: var(--acc);
  background: color-mix(in oklch,var(--acc) 6%,white);
}

.cdl-06__shell>* > b {
  position: absolute;
  top: -1px;
  left: -1px;
  font: 700 10px ui-monospace,Menlo,Consolas,monospace;
  letter-spacing: .06em;
  color: oklch(1 0 0);
  background: var(--line);
  border-radius: 10px 0 10px 0;
  padding: 4px 10px;
}

.cdl-06__shell>*:hover > b {
  background: var(--acc);
}

.cdl-06__header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}

.cdl-06__hint {
  font: 600 11px ui-monospace,Menlo,Consolas,monospace;
  color: var(--mut);
}

.cdl-06__drag {
  margin-left: auto;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 9%,transparent);
  border-radius: 999px;
  padding: 4px 10px;
}

.cdl-06__sidebar {
  display: flex;
  flex-direction: column;
  gap: 5px;
  padding-top: 30px;
}

.cdl-06__sidebar a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 10px;
  border-radius: 9px;
  text-decoration: none;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
  white-space: nowrap;
  transition: background .15s,color .15s;
}

.cdl-06__sidebar a i {
  flex: none;
  width: 16px;
  height: 16px;
  border-radius: 5px;
  background: color-mix(in oklch,var(--line) 45%,white);
}

.cdl-06__sidebar a:hover {
  background: color-mix(in oklch,var(--acc) 8%,white);
  color: var(--ink);
}

.cdl-06__sidebar a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cdl-06__sidebar a.cdl-06__on {
  background: color-mix(in oklch,var(--acc) 12%,white);
  color: var(--acc);
}

.cdl-06__sidebar a.cdl-06__on i {
  background: var(--acc);
}

.cdl-06__main {
  padding-top: 32px;
}

.cdl-06__blocks {
  display: grid;
  gap: 12px;
}

.cdl-06__blocks span {
  display: block;
  height: 15px;
  width: var(--w);
  border-radius: 999px;
  background: color-mix(in oklch,var(--line) 26%,white);
}

.cdl-06__aside {
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding-top: 32px;
}

.cdl-06__widget {
  display: grid;
  gap: 7px;
  font-size: 12px;
  font-weight: 600;
  color: var(--mut);
}

.cdl-06__meter {
  height: 8px;
  border-radius: 999px;
  background: color-mix(in oklch,var(--line) 22%,white);
  overflow: hidden;
}

.cdl-06__meter i {
  display: block;
  height: 100%;
  width: var(--w);
  border-radius: inherit;
  background: linear-gradient(90deg,var(--acc),var(--line));
}

.cdl-06__footer {
  display: flex;
  align-items: center;
  gap: 12px;
  overflow: hidden;
}

.cdl-06__code {
  font: 600 10.5px ui-monospace,Menlo,Consolas,monospace;
  color: var(--mut);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cdl-06__code--narrow {
  display: none;
}

@container (max-width: 660px) {
  .cdl-06__shell {
    grid-template-columns: 64px minmax(0,1fr);
    grid-template-rows: 54px minmax(0,1fr) auto 44px;
    grid-template-areas: "header header" "sidebar main" "aside aside" "footer footer";
  }

  .cdl-06__sidebar a span {
    display: none;
  }

  .cdl-06__aside {
    flex-direction: row;
    padding-top: 30px;
  }

  .cdl-06__aside .cdl-06__widget {
    flex: 1;
  }

  .cdl-06__code--wide {
    display: none;
  }

  .cdl-06__code--narrow {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-06 * {
    transition: none !important;
  }
}
```
