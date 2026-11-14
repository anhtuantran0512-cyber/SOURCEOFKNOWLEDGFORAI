---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-footer-to-bottom-of-screen/"
title: "CSS Sticky Footer to Bottom of Screen"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The OTHER sticky footer — the one that predates position: sticky and still fills support forums: on a short page the footer floats awkwardly mid-screen; you…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Footer to Bottom of Screen
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-footer-to-bottom-of-screen/

The OTHER sticky footer — the one that predates position: sticky and still fills support forums: on a short page the footer floats awkwardly mid-screen; you want it pinned to the viewport bottom, but pushed down naturally once content grows. The 2026 answer is three lines of grid. This demo has a Short page / Long page toggle (a checkbox and :has(), no JS) so you can watch the same three lines handle both cases.
## HTML
```html
<section class="cst-14" aria-label="Sticky footer at bottom of screen demo">
  <div class="cst-14__stage" id="cst14-top">
    <div class="cst-14__page">
      <header class="cst-14__head">
        <a class="cst-14__brand" href="#cst14-top">Ledger <span>release notes</span></a>
        <fieldset class="cst-14__toggle">
          <legend class="cst-14__vh">Demo page length</legend>
          <input type="radio" name="cst14len" id="cst14-short" checked><label for="cst14-short">Short page</label>
          <input type="radio" name="cst14len" id="cst14-long"><label for="cst14-long">Long page</label>
        </fieldset>
      </header>
      <main class="cst-14__main">
        <p class="cst-14__explain">Toggle above. <strong>Short:</strong> content ends mid-screen, yet the footer holds the bottom edge — the <code>1fr</code> row absorbs the slack. <strong>Long:</strong> the same three lines of grid let the footer flow naturally after the content. No <code>position: fixed</code>, no JavaScript.</p>
        <article class="cst-14__note">
          <header><span class="cst-14__chip">v4.2.0</span><time>Jul 30, 2026</time></header>
          <h2>Saved views, shareable</h2>
          <ul><li>Any filtered ledger view now mints a URL — send it, bookmark it, embed it.</li><li>Export respects the active view, including hidden columns.</li><li>Fixed: month-end close banner no longer overlaps the totals row on 13-inch screens.</li></ul>
        </article>
        <div class="cst-14__extra">
          <article class="cst-14__note">
            <header><span class="cst-14__chip">v4.1.2</span><time>Jul 18, 2026</time></header>
            <h2>Quieter reconciliation</h2>
            <ul><li>Auto-match confidence now shown inline instead of a modal per match.</li><li>Keyboard: <kbd>J</kbd>/<kbd>K</kbd> walk unmatched entries; <kbd>A</kbd> accepts.</li></ul>
          </article>
          <article class="cst-14__note">
            <header><span class="cst-14__chip">v4.1.1</span><time>Jul 09, 2026</time></header>
            <h2>Patch: timezone sanity</h2>
            <ul><li>Statements imported from AU/NZ banks no longer time-travel a day.</li><li>Fixed a sticky table header (yes, we read demo 09) losing its shadow in Safari.</li></ul>
          </article>
          <article class="cst-14__note">
            <header><span class="cst-14__chip">v4.1.0</span><time>Jun 27, 2026</time></header>
            <h2>Rules engine, rebuilt</h2>
            <ul><li>Rules compose now — 'coffee AND &gt; $8' finally files as “regret”.</li><li>Dry-run mode previews the next import against your rule set.</li><li>14 new merchant normalizers for UK and Canadian banks.</li></ul>
          </article>
          <article class="cst-14__note">
            <header><span class="cst-14__chip">v4.0.2</span><time>Jun 14, 2026</time></header>
            <h2>Small sharp fixes</h2>
            <ul><li>CSV import handles files with BOM markers from Excel.</li><li>Dark mode: charts no longer glow radioactive green on P3 displays.</li></ul>
          </article>
          <article class="cst-14__note">
            <header><span class="cst-14__chip">v4.0.0</span><time>May 30, 2026</time></header>
            <h2>Ledger 4</h2>
            <ul><li>Multi-entity books, one login.</li><li>Realtime collaboration with per-cell presence.</li><li>New keyboard-first navigation across every screen.</li></ul>
          </article>
        </div>
      </main>
      <footer class="cst-14__footer">
        <div class="cst-14__cols">
          <div><strong>Product</strong><a href="#cst14-top">Pricing</a><a href="#cst14-top">Changelog</a><a href="#cst14-top">Roadmap</a></div>
          <div><strong>Company</strong><a href="#cst14-top">About</a><a href="#cst14-top">Blog</a><a href="#cst14-top">Careers</a></div>
          <div><strong>Support</strong><a href="#cst14-top">Docs</a><a href="#cst14-top">Status</a><a href="#cst14-top">Contact</a></div>
        </div>
        <div class="cst-14__legal"><span><i aria-hidden="true"></i>All systems normal</span><p>© 2026 Ledger — a CodeFronts sticky-elements demo. This footer is pinned by a 1fr grid row, not position: sticky.</p></div>
      </footer>
    </div>
  </div>
</section>
```
## CSS
```css
.cst-14,
.cst-14 *,
.cst-14 *::before,
.cst-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-14 {
  --bg: oklch(0.975 0.004 230);
  --ink: oklch(0.23 0.015 240);
  --mut: oklch(0.51 0.012 240);
  --line: oklch(0.9 0.007 235);
  --acc: oklch(0.55 0.15 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-14__stage {
  width: 100%;
  container: cst14/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cst-14__page {
  min-height: 100%;
  display: grid;
  grid-template-rows: auto 1fr auto;
}

.cst-14__head {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px 20px;
  padding: 16px clamp(16px,4cqi,40px);
  border-bottom: 1px solid var(--line);
}

.cst-14__brand {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.cst-14__brand span {
  font-weight: 500;
  color: var(--mut);
}

.cst-14__brand:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-14__toggle {
  display: flex;
  border: 1.5px solid var(--line);
  border-radius: 12px;
  padding: 3px;
  background: oklch(1 0 0);
  gap: 2px;
}

.cst-14__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.cst-14__toggle input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.cst-14__toggle label {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 15px;
  border-radius: 9px;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--mut);
  cursor: pointer;
  transition: background .2s,color .2s;
}

.cst-14__toggle label:hover {
  color: var(--ink);
}

.cst-14__toggle input:checked+label {
  background: var(--ink);
  color: oklch(0.98 0 0);
}

.cst-14__toggle input:focus-visible+label {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cst-14__main {
  padding: clamp(22px,4cqi,40px) clamp(16px,4cqi,40px);
  display: grid;
  gap: 16px;
  align-content: start;
  max-width: 820px;
}

.cst-14__explain {
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--mut);
  padding: 14px 16px;
  border-radius: 14px;
  background: oklch(0.93 0.015 225/.6);
  border: 1px solid color-mix(in oklch,var(--acc) 22%,var(--line));
}

.cst-14__explain strong {
  color: var(--ink);
}

.cst-14__explain code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(1 0 0/.7);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.cst-14__note {
  padding: 20px 22px;
  border-radius: 16px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
}

.cst-14__note header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}

.cst-14__chip {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  font-weight: 700;
  color: var(--acc);
  background: oklch(0.93 0.03 220/.7);
  padding: 3px 9px;
  border-radius: 99px;
}

.cst-14__note time {
  font-size: 12px;
  color: var(--mut);
}

.cst-14__note h2 {
  font-size: 17px;
  letter-spacing: -.015em;
  font-weight: 750;
  margin-bottom: 10px;
}

.cst-14__note ul {
  list-style: none;
  display: grid;
  gap: 7px;
}

.cst-14__note li {
  position: relative;
  padding-left: 18px;
  font-size: 13.5px;
  line-height: 1.6;
  color: oklch(0.38 0.015 240);
}

.cst-14__note li::before {
  content: "";
  position: absolute;
  left: 2px;
  top: 9px;
  width: 6px;
  height: 6px;
  border-radius: 2px;
  background: var(--acc);
}

.cst-14__note kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .85em;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 1px 5px;
  background: oklch(0.97 0.004 230);
}

.cst-14__extra {
  display: none;
}

.cst-14__stage:has(#cst14-long:checked) .cst-14__extra {
  display: grid;
  gap: 16px;
}

.cst-14__footer {
  background: oklch(0.24 0.02 245);
  color: oklch(0.9 0.008 235);
}

.cst-14__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(150px,100%),1fr));
  gap: 20px;
  padding: 28px clamp(16px,4cqi,40px) 20px;
  max-width: 820px;
}

.cst-14__cols strong {
  display: block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: oklch(0.66 0.015 235);
  margin-bottom: 6px;
}

.cst-14__cols a {
  display: flex;
  align-items: center;
  min-height: 34px;
  font-size: 13px;
  font-weight: 600;
  color: oklch(0.88 0.01 235);
  text-decoration: none;
  width: fit-content;
}

.cst-14__cols a:hover,
.cst-14__cols a:focus-visible {
  color: oklch(0.99 0 0);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cst-14__cols a:focus-visible {
  outline: 2px solid oklch(0.7 0.12 220);
  outline-offset: 2px;
  border-radius: 4px;
}

.cst-14__legal {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding: 14px clamp(16px,4cqi,40px) 20px;
  border-top: 1px solid oklch(0.34 0.02 245);
}

.cst-14__legal span {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.8 0.09 155);
}

.cst-14__legal i {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: oklch(0.75 0.16 155);
  box-shadow: 0 0 0 3px oklch(0.75 0.16 155/.25);
}

.cst-14__legal p {
  font-size: 11.5px;
  color: oklch(0.66 0.015 235);
}

@media (prefers-reduced-motion: reduce) {
  .cst-14 * {
    transition-duration: .01ms !important;
  }
}
```
