---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/minimal-rail/"
title: "Minimal Rail Accordion — Timeline Dot Spine for Changelogs & Roadmaps"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The quietest accordion in the set: a single hairline rail down the left with a dot per item — closed dots are hollow, the open dot fills and emits a soft…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Rail Accordion — Timeline Dot Spine for Changelogs & Roadmaps
Source: https://codefronts.com/navigation/css-accordions/minimal-rail/

The quietest accordion in the set: a single hairline rail down the left with a dot per item — closed dots are hollow, the open dot fills and emits a soft ring pulse. Reads like a vertical timeline, which is exactly its use case: roadmaps, changelogs, order tracking and career pages.
## HTML
```html
<section class="acc-13" aria-label="Minimal rail timeline accordion demo">
  <div class="acc-13__wrap">
    <h3 class="acc-13__title">Roadmap</h3>
    <div class="acc-13__rail">
      <details class="acc-13__item" open>
        <summary class="acc-13__sum"><span class="acc-13__meta">Shipped · Q2 2026</span>Offline-first sync engine</summary>
        <div class="acc-13__body"><p>Every document now resolves conflicts with CRDTs locally — edits made on a plane merge cleanly when you land.</p></div>
      </details>
      <details class="acc-13__item">
        <summary class="acc-13__sum"><span class="acc-13__meta">In progress · Q3 2026</span>Shared workspaces</summary>
        <div class="acc-13__body"><p>Real-time cursors, granular roles and workspace-level templates. In beta with 40 design teams now.</p></div>
      </details>
      <details class="acc-13__item">
        <summary class="acc-13__sum"><span class="acc-13__meta">Planned · Q4 2026</span>Plugin API</summary>
        <div class="acc-13__body"><p>A sandboxed runtime with typed manifests. The first-party plugins (linear sync, figma import) will be open source.</p></div>
      </details>
      <details class="acc-13__item">
        <summary class="acc-13__sum"><span class="acc-13__meta">Exploring</span>On-prem deployment</summary>
        <div class="acc-13__body"><p>Single-tenant images with your KMS keys. Talk to us if your compliance team needs this sooner.</p></div>
      </details>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-13,
.acc-13 *,
.acc-13 *::before,
.acc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-13 {
  --accent: oklch(0.58 0.16 250);
  --dot: 12px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fafbfd;
  padding: 48px 24px;
}

.acc-13__wrap {
  width: min(520px,100%);
}

.acc-13__title {
  font-size: 24px;
  font-weight: 800;
  color: #1a2030;
  letter-spacing: -.02em;
  margin-bottom: 22px;
}

.acc-13__rail {
  border-left: 1.5px solid #e2e6ef;
  padding-left: 28px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.acc-13__sum {
  list-style: none;
  position: relative;
  padding: 10px 0;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 3px;
  font-size: 16.5px;
  font-weight: 700;
  color: #232b40;
}

.acc-13__sum::-webkit-details-marker {
  display: none;
}

.acc-13__sum::marker {
  content: "";
}

.acc-13__sum::before {
  content: "";
  position: absolute;
  left: calc(-28px - var(--dot)/2 - .75px);
  top: 34px;
  width: var(--dot);
  height: var(--dot);
  border-radius: 50%;
  background: #fafbfd;
  border: 2px solid #c6cdda;
  transition: background .25s,border-color .25s;
}

.acc-13__sum::after {
  content: "";
  position: absolute;
  left: calc(-28px - var(--dot)/2 - .75px);
  top: 34px;
  width: var(--dot);
  height: var(--dot);
  border-radius: 50%;
  border: 2px solid var(--accent);
  opacity: 0;
  pointer-events: none;
}

.acc-13__item[open] > .acc-13__sum::before {
  background: var(--accent);
  border-color: var(--accent);
}

.acc-13__item[open] > .acc-13__sum::after {
  animation: acc-13-pulse .7s ease-out;
}

@keyframes acc-13-pulse {
  from {
    opacity: .8;
    scale: 1;
  }

  to {
    opacity: 0;
    scale: 2.4;
  }
}

.acc-13__sum:hover {
  color: var(--accent);
}

.acc-13__meta {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: #98a1b6;
}

.acc-13__item[open] .acc-13__meta {
  color: var(--accent);
}

.acc-13__body {
  padding: 2px 12px 16px 0;
  font-size: 14.5px;
  line-height: 1.65;
  color: #4d5670;
}

.acc-13__item[open] .acc-13__body {
  animation: acc-13-in .35s ease-out;
}

@keyframes acc-13-in {
  from {
    opacity: 0;
    translate: 0 -5px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-13__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-13__item[open] > .acc-13__sum::after {
    animation: none;
  }

  .acc-13__item[open] .acc-13__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the rail is one border-left; each row's dot is its own ::before pulled onto the line, and details[open] fills the dot plus fires a single ring-pulse keyframe. */
```
