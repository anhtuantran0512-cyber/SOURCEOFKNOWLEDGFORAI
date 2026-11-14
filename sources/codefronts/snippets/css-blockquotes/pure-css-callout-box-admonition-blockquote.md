---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/pure-css-callout-box-admonition-blockquote/"
title: "Pure CSS Callout Box / Admonition Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The docs-site trinity — Note, Tip, Warning — as one CSS system instead of three hand-made boxes."
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Callout Box / Admonition Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/pure-css-callout-box-admonition-blockquote/

The docs-site trinity — Note, Tip, Warning — as one CSS system instead of three hand-made boxes. Each callout is a real <blockquote> carrying a data-kind attribute; a single rule reads the kind and derives the tint, border and icon color from one hue token with color-mix(), so adding a fourth kind (Danger, Deprecated) is two custom properties, not twenty lines. This is the exact pattern GitHub Markdown alerts, Docusaurus and MkDocs admonitions compile down to — shown raw so you can theme it.
## HTML
```html
<section class="bq-03" aria-label="Callout box admonition blockquote demo">
  <div class="bq-03__stage">
    <div class="bq-03__doc">
      <p class="bq-03__crumb" aria-hidden="true">docs / deploying / <b>zero-downtime.md</b></p>
      <blockquote class="bq-03__callout" data-kind="note">
        <p class="bq-03__label"><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 7.2v4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="8" cy="4.9" r=".9" fill="currentColor"/></svg><strong>Note</strong></p>
        <p>Deploys are atomic. The new release only receives traffic after every health check passes — a failed boot never reaches users.</p>
      </blockquote>
      <blockquote class="bq-03__callout" data-kind="tip">
        <p class="bq-03__label"><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M8 1.6a4.6 4.6 0 0 0-2.6 8.4c.5.4.8.9.8 1.5h3.6c0-.6.3-1.1.8-1.5A4.6 4.6 0 0 0 8 1.6z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M6.4 13.6h3.2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg><strong>Tip</strong></p>
        <p>Set <code>--grace-period=30s</code> so in-flight requests drain before the old release is retired. Your p99 will thank you.</p>
      </blockquote>
      <blockquote class="bq-03__callout" data-kind="warn">
        <p class="bq-03__label"><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M8 2 14.6 13.4H1.4z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M8 6.4v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="8" cy="11.4" r=".85" fill="currentColor"/></svg><strong>Warning</strong></p>
        <p>Skipping migrations with <code>--no-migrate</code> leaves the schema behind the code. Only do this when the release is verified backwards-compatible.</p>
      </blockquote>
    </div>
    <p class="bq-03__chip" aria-hidden="true">one --tone token · color-mix() wash · data-kind variants</p>
  </div>
</section>
```
## CSS
```css
.bq-03,
.bq-03 *,
.bq-03 *::before,
.bq-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.975 0.004 250);
  --card: oklch(1 0 0);
  --ink: oklch(0.27 0.015 260);
  --mut: oklch(0.54 0.015 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-03__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(20px,5vw,56px);
  background: var(--bg);
  overflow-y: auto;
}

.bq-03__doc {
  width: min(100%,600px);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.bq-03__crumb {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--mut);
  margin-bottom: 2px;
}

.bq-03__crumb b {
  color: var(--ink);
  font-weight: 600;
}

.bq-03__callout {
  --tone: oklch(0.62 0.14 250);
  border-left: 4px solid var(--tone);
  background: color-mix(in oklch,var(--tone) 9%,var(--card));
  border-radius: 0 12px 12px 0;
  padding: 15px 18px 16px;
  box-shadow: 0 1px 3px oklch(0 0 0/.05);
}

.bq-03__callout[data-kind="tip"] {
  --tone: oklch(0.64 0.14 155);
}

.bq-03__callout[data-kind="warn"] {
  --tone: oklch(0.72 0.15 75);
}

.bq-03__label {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--tone);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .02em;
  margin-bottom: 6px;
}

.bq-03__callout>p:not(.bq-03__label) {
  font-size: 14.5px;
  line-height: 1.62;
  color: color-mix(in oklch,var(--ink) 88%,var(--tone));
  text-wrap: pretty;
}

.bq-03__callout code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: color-mix(in oklch,var(--tone) 14%,var(--card));
  padding: 1.5px 6px;
  border-radius: 5px;
}

.bq-03__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: var(--card);
}

@media (prefers-reduced-motion: reduce) {
  .bq-03 * {
    transition-duration: .01ms !important;
  }
}
```
