---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/docs-sidebar-vertical-tabs-category-groups/"
title: "Docs Sidebar Vertical Tabs (Category Groups)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "A documentation sidebar that scales past four items: labelled category groups, a sticky header per group, a scroll-contained rail, and typographic hierarchy…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Docs Sidebar Vertical Tabs (Category Groups)
Source: https://codefronts.com/navigation/css-vertical-tabs/docs-sidebar-vertical-tabs-category-groups/

A documentation sidebar that scales past four items: labelled category groups, a sticky header per group, a scroll-contained rail, and typographic hierarchy tight enough that thirty links still scan in one glance. The panel renders real docs content — prose measure, inline code, a callout — because a nav is only as good as what it frames.
## HTML
```html
<section class="vt-10" aria-label="Docs sidebar vertical tabs demo">
  <div class="vt-10__stage">
    <div class="vt-10__card" role="radiogroup" aria-label="Documentation pages">
      <nav class="vt-10__rail">
        <p class="vt-10__brand"><span class="vt-10__dot" aria-hidden="true"></span>Docs <span class="vt-10__ver">v4.2</span></p>
        <p class="vt-10__group">Getting started</p>
        <div class="vt-10__tree">
          <input class="vt-10__radio" type="radio" name="vt-10" id="vt-10-t1" checked>
          <label class="vt-10__link" for="vt-10-t1">Introduction</label>
          <input class="vt-10__radio" type="radio" name="vt-10" id="vt-10-t2">
          <label class="vt-10__link" for="vt-10-t2">Installation</label>
          <input class="vt-10__radio" type="radio" name="vt-10" id="vt-10-t3">
          <label class="vt-10__link" for="vt-10-t3">Project structure</label>
        </div>
        <p class="vt-10__group">Core concepts</p>
        <div class="vt-10__tree">
          <input class="vt-10__radio" type="radio" name="vt-10" id="vt-10-t4">
          <label class="vt-10__link" for="vt-10-t4">Routing</label>
          <input class="vt-10__radio" type="radio" name="vt-10" id="vt-10-t5">
          <label class="vt-10__link" for="vt-10-t5">Data fetching</label>
        </div>
        <p class="vt-10__group">Reference</p>
        <div class="vt-10__tree">
          <input class="vt-10__radio" type="radio" name="vt-10" id="vt-10-t6">
          <label class="vt-10__link" for="vt-10-t6">CLI commands</label>
        </div>
      </nav>
      <div class="vt-10__panels">
        <article class="vt-10__panel" id="vt-10-p1">
          <div class="vt-10__body">
            <p class="vt-10__crumb">Getting started <span aria-hidden="true">›</span> Introduction</p>
            <h3 class="vt-10__h">Hierarchy without indentation<a class="vt-10__anchor" aria-label="Anchor link" href="#">#</a></h3>
            <p class="vt-10__p">Three levers carry the structure: a 10px mono heading, a 14px link, and a hairline between groups. Indentation would spend horizontal space the link text needs.</p>
            <div class="vt-10__call">Sticky group headings need an opaque background, or link text scrolls straight through them.</div>
          </div>
          <aside class="vt-10__toc" aria-label="On this page">
            <p class="vt-10__toc-h">On this page</p>
            <ul><li class="vt-10__toc-active">Hierarchy</li><li>Group headings</li><li>Link scale</li></ul>
          </aside>
        </article>
        <article class="vt-10__panel" id="vt-10-p2">
          <div class="vt-10__body">
            <p class="vt-10__crumb">Getting started <span aria-hidden="true">›</span> Installation</p>
            <h3 class="vt-10__h">Contain the scroll<a class="vt-10__anchor" aria-label="Anchor link" href="#">#</a></h3>
            <p class="vt-10__p"><code>overscroll-behavior:contain</code> stops the page lurching when the rail hits its end — the most common complaint about docs sidebars.</p>
            <div class="vt-10__call">Pair it with <code>scroll-padding-block</code> so focused links never hide under the sticky heading.</div>
          </div>
          <aside class="vt-10__toc" aria-label="On this page">
            <p class="vt-10__toc-h">On this page</p>
            <ul><li class="vt-10__toc-active">Scroll behavior</li><li>Scroll padding</li><li>Sticky headers</li></ul>
          </aside>
        </article>
        <article class="vt-10__panel" id="vt-10-p3">
          <div class="vt-10__body">
            <p class="vt-10__crumb">Getting started <span aria-hidden="true">›</span> Project structure</p>
            <h3 class="vt-10__h">Inset bar, not border<a class="vt-10__anchor" aria-label="Anchor link" href="#">#</a></h3>
            <p class="vt-10__p">The active rail is a positioned pseudo-element. A real border would add 2px of layout width and shift every label sideways on selection.</p>
            <div class="vt-10__call">Same trick works for hover states without any reflow at all.</div>
          </div>
          <aside class="vt-10__toc" aria-label="On this page">
            <p class="vt-10__toc-h">On this page</p>
            <ul><li class="vt-10__toc-active">Active indicator</li><li>Reflow-free hover</li></ul>
          </aside>
        </article>
        <article class="vt-10__panel" id="vt-10-p4">
          <div class="vt-10__body">
            <p class="vt-10__crumb">Core concepts <span aria-hidden="true">›</span> Routing</p>
            <h3 class="vt-10__h">Swap radios for links<a class="vt-10__anchor" aria-label="Anchor link" href="#">#</a></h3>
            <p class="vt-10__p">Every active style also matches <code>[aria-current="page"]</code>, so moving from this demo to a real routed docs site is a markup change only.</p>
            <div class="vt-10__call">Use <code>aria-current</code>, not <code>aria-selected</code> — the latter belongs to tablists.</div>
          </div>
          <aside class="vt-10__toc" aria-label="On this page">
            <p class="vt-10__toc-h">On this page</p>
            <ul><li class="vt-10__toc-active">aria-current</li><li>Radios vs links</li><li>Semantics</li></ul>
          </aside>
        </article>
        <article class="vt-10__panel" id="vt-10-p5">
          <div class="vt-10__body">
            <p class="vt-10__crumb">Core concepts <span aria-hidden="true">›</span> Data fetching</p>
            <h3 class="vt-10__h">Prose that stays readable<a class="vt-10__anchor" aria-label="Anchor link" href="#">#</a></h3>
            <p class="vt-10__p">The panel caps its measure at 62 characters and uses <code>text-wrap:pretty</code>, so long paragraphs never end on an orphaned word.</p>
            <div class="vt-10__call">65ch is the classic upper bound for comfortable reading.</div>
          </div>
          <aside class="vt-10__toc" aria-label="On this page">
            <p class="vt-10__toc-h">On this page</p>
            <ul><li class="vt-10__toc-active">Measure</li><li>text-wrap</li><li>Widow control</li></ul>
          </aside>
        </article>
        <article class="vt-10__panel" id="vt-10-p6">
          <div class="vt-10__body">
            <p class="vt-10__crumb">Reference <span aria-hidden="true">›</span> CLI commands</p>
            <h3 class="vt-10__h">Thirty links still scan<a class="vt-10__anchor" aria-label="Anchor link" href="#">#</a></h3>
            <p class="vt-10__p">Groups cap at five or six items. Past that, split the category — a rail is a map, and a map with no landmarks is a list.</p>
            <div class="vt-10__call">Collapsible groups: wrap each in <code>&lt;details open&gt;</code>, still zero JavaScript.</div>
          </div>
          <aside class="vt-10__toc" aria-label="On this page">
            <p class="vt-10__toc-h">On this page</p>
            <ul><li class="vt-10__toc-active">Group size</li><li>Category split</li></ul>
          </aside>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-10-bg);
  --vt-10-bg: oklch(0.16 0.014 258);
  --vt-10-card: oklch(0.205 0.016 258);
  --vt-10-rail: oklch(0.185 0.014 258);
  --vt-10-ink: oklch(0.97 0.006 258);
  --vt-10-mut: oklch(0.64 0.014 258);
  --vt-10-dim: oklch(0.52 0.014 258);
  --vt-10-acc: oklch(0.82 0.16 152);
  --vt-10-line: oklch(1 0 0/.08);
  --vt-10-tree: oklch(1 0 0/.11);
  font-family: 'Inter',ui-sans-serif,system-ui,-apple-system,sans-serif;
  color: var(--vt-10-ink);
}

.vt-10 *,
.vt-10 *::before,
.vt-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-10__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(16px,4vw,56px);
  background: radial-gradient(60% 45% at 15% 0%,oklch(0.28 0.06 165/.42),transparent),radial-gradient(50% 40% at 85% 100%,oklch(0.24 0.05 258/.4),transparent);
}

.vt-10__card {
  width: min(96vw,960px);
  display: grid;
  grid-template-columns: minmax(190px,246px) minmax(0,1fr);
  background: var(--vt-10-card);
  border: 1px solid var(--vt-10-line);
  border-radius: 16px;
  box-shadow: 0 32px 82px -40px oklch(0 0 0/.85);
  overflow: hidden;
}

.vt-10__rail {
  display: flex;
  flex-direction: column;
  padding: 0 12px 18px;
  background: var(--vt-10-rail);
  border-right: 1px solid var(--vt-10-line);
  max-height: 66svh;
  overflow: auto;
  overscroll-behavior: contain;
  scrollbar-width: thin;
  scrollbar-color: oklch(1 0 0/.14) transparent;
  scroll-padding-block: 44px;
}

.vt-10__brand {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 9px;
  margin-inline: -12px;
  padding: 16px 18px 14px;
  background: var(--vt-10-rail);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: -.015em;
  border-bottom: 1px solid var(--vt-10-line);
}

.vt-10__dot {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: var(--vt-10-acc);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--vt-10-acc) 22%,transparent);
}

.vt-10__ver {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  font-weight: 600;
  color: var(--vt-10-acc);
  padding: 2px 7px;
  border-radius: 5px;
  background: color-mix(in oklch,var(--vt-10-acc) 12%,transparent);
  border: 1px solid color-mix(in oklch,var(--vt-10-acc) 26%,transparent);
}

.vt-10__group {
  padding: 16px 6px 6px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--vt-10-dim);
}

.vt-10__tree {
  display: flex;
  flex-direction: column;
  position: relative;
  padding-inline-start: 14px;
}

.vt-10__tree::before {
  content: "";
  position: absolute;
  inset-block: 4px;
  inset-inline-start: 4px;
  inline-size: 1px;
  background: var(--vt-10-tree);
}

.vt-10__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-10__link {
  position: relative;
  display: flex;
  align-items: center;
  min-height: 32px;
  padding: 0 10px;
  font-size: 13.6px;
  font-weight: 500;
  color: var(--vt-10-mut);
  cursor: pointer;
  border-radius: 6px;
  transition: color .16s ease,background .16s ease;
}

.vt-10__link::before {
  content: "";
  position: absolute;
  inset-inline-start: -14px;
  inset-block: 5px;
  inline-size: 2px;
  border-radius: 2px;
  background: transparent;
  transition: background .16s ease;
}

.vt-10__link:hover {
  color: var(--vt-10-ink);
  background: oklch(1 0 0/.03);
}

.vt-10__radio:checked+.vt-10__link,
.vt-10__link[aria-current="page"] {
  color: var(--vt-10-acc);
  background: transparent;
  font-weight: 600;
}

.vt-10__radio:checked+.vt-10__link::before,
.vt-10__link[aria-current="page"]::before {
  background: var(--vt-10-acc);
}

.vt-10__radio:focus-visible+.vt-10__link {
  outline: 2px solid var(--vt-10-acc);
  outline-offset: 1px;
}

.vt-10__panels {
  display: grid;
  min-height: clamp(300px,38vw,352px);
  padding: clamp(26px,3.6vw,40px) clamp(24px,3.4vw,36px);
}

.vt-10__panel {
  grid-area: 1/1;
  display: grid;
  grid-template-columns: minmax(0,1fr) 160px;
  gap: clamp(20px,3vw,36px);
  align-content: start;
  opacity: 0;
  visibility: hidden;
  transform: translateY(6px);
  transition: opacity .26s ease,transform .32s cubic-bezier(.32,.72,.3,1),visibility 0s .32s;
}

.vt-10__card:has(#vt-10-t1:checked) #vt-10-p1,
.vt-10__card:has(#vt-10-t2:checked) #vt-10-p2,
.vt-10__card:has(#vt-10-t3:checked) #vt-10-p3,
.vt-10__card:has(#vt-10-t4:checked) #vt-10-p4,
.vt-10__card:has(#vt-10-t5:checked) #vt-10-p5,
.vt-10__card:has(#vt-10-t6:checked) #vt-10-p6 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-10__body {
  display: grid;
  gap: 14px;
  align-content: start;
  min-inline-size: 0;
}

.vt-10__crumb {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .06em;
  text-transform: none;
  color: var(--vt-10-dim);
}

.vt-10__crumb span {
  color: oklch(1 0 0/.24);
}

.vt-10__h {
  position: relative;
  font-size: clamp(20px,2.4vw,27px);
  line-height: 1.18;
  letter-spacing: -.026em;
  font-weight: 700;
  text-wrap: balance;
  display: inline-flex;
  align-items: baseline;
  gap: 10px;
}

.vt-10__anchor {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .6em;
  font-weight: 600;
  color: var(--vt-10-dim);
  text-decoration: none;
  opacity: .5;
  transition: opacity .16s ease,color .16s ease;
}

.vt-10__h:hover .vt-10__anchor {
  opacity: 1;
  color: var(--vt-10-acc);
}

.vt-10__p {
  max-width: 60ch;
  font-size: 14.6px;
  line-height: 1.66;
  color: var(--vt-10-mut);
  text-wrap: pretty;
}

.vt-10__call {
  max-width: 60ch;
  padding: 12px 15px;
  border-radius: 10px;
  background: color-mix(in oklch,var(--vt-10-acc) 8%,transparent);
  border: 1px solid color-mix(in oklch,var(--vt-10-acc) 22%,transparent);
  border-inline-start: 2px solid var(--vt-10-acc);
  font-size: 13.4px;
  line-height: 1.55;
  color: color-mix(in oklch,var(--vt-10-acc) 55%,var(--vt-10-ink));
}

.vt-10 code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .86em;
  background: oklch(1 0 0/.08);
  padding: 2px 6px;
  border-radius: 4px;
  overflow-wrap: anywhere;
}

.vt-10__toc {
  position: sticky;
  inset-block-start: 0;
  align-self: start;
  display: grid;
  gap: 10px;
  padding-inline-start: 16px;
  border-inline-start: 1px solid var(--vt-10-line);
}

.vt-10__toc-h {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--vt-10-dim);
}

.vt-10__toc ul {
  list-style: none;
  display: grid;
  gap: 6px;
}

.vt-10__toc li {
  position: relative;
  font-size: 12.6px;
  line-height: 1.5;
  color: var(--vt-10-mut);
  padding-inline-start: 12px;
}

.vt-10__toc li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: .55em;
  inline-size: 6px;
  block-size: 1px;
  background: var(--vt-10-tree);
}

.vt-10__toc-active {
  color: var(--vt-10-acc) !important;
  font-weight: 600;
}

.vt-10__toc-active::before {
  background: var(--vt-10-acc) !important;
  inline-size: 8px !important;
}

@media (max-width: 760px) {
  .vt-10__panel {
    grid-template-columns: 1fr;
  }

  .vt-10__toc {
    display: none;
  }
}

@media (max-width: 680px) {
  .vt-10__card {
    grid-template-columns: 1fr;
  }

  .vt-10__rail {
    border-right: 0;
    border-bottom: 1px solid var(--vt-10-line);
    max-height: 220px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-10 * {
    transition-duration: .01ms !important;
  }
}
```
