---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-sticky-footer-layout/"
title: "CSS Flexbox Sticky Footer Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "The definitive flexbox sticky footer pattern — a column flex wrapper with min-height: 100% and flex: 1 on the main content pushes the footer to the bottom on…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Sticky Footer Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-sticky-footer-layout/

The definitive flexbox sticky footer pattern — a column flex wrapper with min-height: 100% and flex: 1 on the main content pushes the footer to the bottom on any page length.
## HTML
```html
<div class="fl-09">
  <div class="fl-09__page">

    <!-- Header -->
    <header class="fl-09__header">
      <div class="fl-09__logo">
        <div class="fl-09__logo-icon">↕</div>
        StickyFoot
      </div>
      <ul class="fl-09__header-nav">
        <li class="fl-09__header-link is-active">Home</li>
        <li class="fl-09__header-link">Docs</li>
        <li class="fl-09__header-link">Examples</li>
        <li class="fl-09__header-link">Blog</li>
      </ul>
    </header>

    <!-- Main — flex: 1 gives it all remaining height -->
    <main class="fl-09__main">

      <!-- Diagram -->
      <div class="fl-09__diagram">
        <div class="fl-09__zone fl-09__zone--header">
          Header <span class="fl-09__zone-code">flex-shrink: 0</span>
        </div>
        <div class="fl-09__zone fl-09__zone--main">
          Main Content <span class="fl-09__zone-code">flex: 1</span>
        </div>
        <div class="fl-09__zone fl-09__zone--footer">
          Footer <span class="fl-09__zone-code">flex-shrink: 0</span>
        </div>
      </div>

      <!-- Explainer -->
      <div class="fl-09__explainer">
        <div class="fl-09__explainer-header">
          <div class="fl-09__explainer-tag">CSS Technique</div>
          <div class="fl-09__explainer-title">Sticky Footer with Flexbox</div>
        </div>
        <div class="fl-09__explainer-body">
          <div class="fl-09__code-block">
<span class="fl-09__code-selector">.page</span> {<br>
  <span class="fl-09__code-prop">  display</span>: <span class="fl-09__code-val">flex</span>;<br>
  <span class="fl-09__code-prop">  flex-direction</span>: <span class="fl-09__code-val">column</span>;<br>
  <span class="fl-09__code-prop">  min-height</span>: <span class="fl-09__code-val">100vh</span>;<br>
}<br>
<span class="fl-09__code-selector">.main</span> { <span class="fl-09__code-prop">flex</span>: <span class="fl-09__code-val">1</span>; } <span class="fl-09__code-comment">/* grows */</span><br>
<span class="fl-09__code-selector">.footer</span> { <span class="fl-09__code-prop">flex-shrink</span>: <span class="fl-09__code-val">0</span>; } <span class="fl-09__code-comment">/* fixed */</span>
          </div>
          <div class="fl-09__explainer-check">
            <div class="fl-09__check-icon">✓</div>
            Footer sticks to the bottom even when content is short — no JS or absolute positioning needed.
          </div>
          <div class="fl-09__explainer-check">
            <div class="fl-09__check-icon">✓</div>
            <code>flex: 1</code> on main is shorthand for <code>flex-grow: 1; flex-shrink: 1; flex-basis: 0</code>, making it absorb all remaining vertical space.
          </div>
        </div>
      </div>

    </main>

    <!-- Footer — flex-shrink: 0 keeps it pinned -->
    <footer class="fl-09__footer">
      <div class="fl-09__footer-top">
        <div>
          <div class="fl-09__footer-brand">StickyFoot</div>
          <div class="fl-09__footer-tagline">Pure CSS sticky footer<br>with flexbox column layout.</div>
        </div>
        <div>
          <div class="fl-09__footer-col-title">Product</div>
          <ul class="fl-09__footer-links">
            <li>Features</li><li>Pricing</li><li>Changelog</li>
          </ul>
        </div>
        <div>
          <div class="fl-09__footer-col-title">Company</div>
          <ul class="fl-09__footer-links">
            <li>About</li><li>Blog</li><li>Careers</li>
          </ul>
        </div>
      </div>
      <div class="fl-09__footer-bottom">
        <span>© 2025 StickyFoot. MIT License.</span>
        <div class="fl-09__footer-socials">
          <div class="fl-09__social-btn">𝕏</div>
          <div class="fl-09__social-btn">in</div>
          <div class="fl-09__social-btn">gh</div>
        </div>
      </div>
    </footer>

  </div>
</div>
```
## CSS
```css
.fl-09,
.fl-09 *,
.fl-09 *::before,
.fl-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-09 ::selection {
  background: #0891b2;
  color: #fff;
}

.fl-09 {
  --bg: #f0f4f8;
  --surface: #fff;
  --ink: #0f2139;
  --muted: #64748b;
  --accent: #0891b2;
  --accent2: #0e7490;
  --footer-bg: #0f2139;
  --border: #dde4ec;
  --green: #059669;
  font-family: 'Manrope', sans-serif;
  background: var(--bg);
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--border);
}
/*
  STICKY FOOTER TECHNIQUE:
  Outer wrapper = flex column, min-height set.
  Main content = flex: 1 (grows to fill space).
  Footer = flex-shrink: 0 (never collapses).
  This pushes the footer to the bottom even when content is short.
*/

.fl-09__page {
  display: flex;
  flex-direction: column;
  min-height: 500px;
}
/* ── Header ── */

.fl-09__header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 28px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;
}

.fl-09__logo {
  font-size: 1rem;
  font-weight: 800;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 8px;
}

.fl-09__logo-icon {
  width: 28px;
  height: 28px;
  background: var(--accent);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  color: #fff;
}

.fl-09__header-nav {
  display: flex;
  gap: 4px;
  list-style: none;
}

.fl-09__header-link {
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: all 0.15s;
}

.fl-09__header-link:hover {
  color: var(--ink);
  background: var(--bg);
}

.fl-09__header-link.is-active {
  color: var(--accent);
}
/* ── Main content (grows with flex: 1) ── */

.fl-09__main {
  flex: 1;
  /* ← this is the sticky footer magic */
  padding: 36px 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
}
/* Technique explainer card */

.fl-09__explainer {
  max-width: 560px;
  width: 100%;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
}

.fl-09__explainer-header {
  background: linear-gradient(135deg, #0e4f6e, #0891b2);
  padding: 20px 24px;
}

.fl-09__explainer-tag {
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.6);
  margin-bottom: 6px;
}

.fl-09__explainer-title {
  font-size: 1.1rem;
  font-weight: 800;
  color: #fff;
}

.fl-09__explainer-body {
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.fl-09__code-block {
  background: #0f2139;
  border-radius: 8px;
  padding: 14px 16px;
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
  line-height: 1.8;
  color: #94a3b8;
}

.fl-09__code-comment {
  color: #475569;
}

.fl-09__code-prop {
  color: #7dd3fc;
}

.fl-09__code-val {
  color: #86efac;
}

.fl-09__code-selector {
  color: #c084fc;
}

.fl-09__explainer-desc {
  font-size: 0.8rem;
  color: var(--muted);
  line-height: 1.7;
}

.fl-09__explainer-check {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 0.78rem;
  color: var(--ink);
  font-weight: 500;
}

.fl-09__check-icon {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: rgba(5,150,105,0.12);
  color: var(--green);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.62rem;
  font-weight: 800;
  flex-shrink: 0;
  margin-top: 1px;
}
/* Diagram showing layout zones */

.fl-09__diagram {
  max-width: 560px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.fl-09__zone {
  border-radius: 8px;
  padding: 10px 14px;
  font-size: 0.72rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.fl-09__zone-code {
  font-family: 'Courier New', monospace;
  font-size: 0.68rem;
  opacity: 0.7;
}

.fl-09__zone--header {
  background: rgba(8,145,178,0.15);
  color: var(--accent2);
}

.fl-09__zone--main {
  background: rgba(8,145,178,0.06);
  color: var(--muted);
  border: 1px dashed rgba(8,145,178,0.2);
  flex: 1;
  min-height: 36px;
}

.fl-09__zone--footer {
  background: rgba(15,33,57,0.08);
  color: var(--ink);
}
/* ── Footer (flex-shrink: 0) ── */

.fl-09__footer {
  background: var(--footer-bg);
  padding: 24px 28px;
  flex-shrink: 0;
  /* ← never shrinks; stays at bottom */
}

.fl-09__footer-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 20px;
}

.fl-09__footer-brand {
  font-size: 0.92rem;
  font-weight: 800;
  color: #fff;
  margin-bottom: 6px;
}

.fl-09__footer-tagline {
  font-size: 0.72rem;
  color: rgba(255,255,255,0.35);
  line-height: 1.5;
}

.fl-09__footer-col-title {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.35);
  margin-bottom: 8px;
}

.fl-09__footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.fl-09__footer-links li {
  font-size: 0.76rem;
  color: rgba(255,255,255,0.5);
  cursor: pointer;
  transition: color 0.15s;
}

.fl-09__footer-links li:hover {
  color: #fff;
}

.fl-09__footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,0.08);
  font-size: 0.7rem;
  color: rgba(255,255,255,0.3);
}

.fl-09__footer-socials {
  display: flex;
  gap: 8px;
}

.fl-09__social-btn {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  background: rgba(255,255,255,0.06);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  cursor: pointer;
  transition: background 0.15s;
}

.fl-09__social-btn:hover {
  background: rgba(255,255,255,0.12);
}

@media (prefers-reduced-motion: reduce) {
  .fl-09__header-link,
    .fl-09__footer-links li,
    .fl-09__social-btn {
    transition: none;
  }
}
```
