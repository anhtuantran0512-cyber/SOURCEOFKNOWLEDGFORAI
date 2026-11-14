---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/tailwind-css-text-gradient-utility-classes/"
title: "Tailwind CSS Text Gradient Utility Classes"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A mapping table and live recreation of Tailwind's bg-clip-text, bg-gradient-to-*, from-*, and text-transparent utility patterns using native CSS."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Text Gradient Utility Classes
Source: https://codefronts.com/motion/css-text-gradient-effect/tailwind-css-text-gradient-utility-classes/

A mapping table and live recreation of Tailwind's bg-clip-text, bg-gradient-to-*, from-*, and text-transparent utility patterns using native CSS.
## HTML
```html
<div class="tg-18">
  <div class="tg-18__doc">
    <h2 class="tg-18__heading">Tailwind CSS Text Gradient<br><span class="tg-18__grad">Utility Classes</span></h2>
    <p class="tg-18__sub">Tailwind achieves gradient text by composing three utility classes. Here's how the framework classes map to raw CSS properties.</p>

    <div class="tg-18__table-wrap">
      <table class="tg-18__table">
        <thead><tr><th>Tailwind Class</th><th>CSS Property</th></tr></thead>
        <tbody>
          <tr><td><code>bg-gradient-to-r</code></td><td><code>background-image: linear-gradient(to right, …)</code></td></tr>
          <tr><td><code>from-indigo-500</code></td><td><code>--tw-gradient-from: #6366f1</code></td></tr>
          <tr><td><code>to-purple-600</code></td><td><code>--tw-gradient-to: #9333ea</code></td></tr>
          <tr><td><code>bg-clip-text</code></td><td><code>-webkit-background-clip: text; background-clip: text</code></td></tr>
          <tr><td><code>text-transparent</code></td><td><code>color: transparent; -webkit-text-fill-color: transparent</code></td></tr>
        </tbody>
      </table>
    </div>

    <div class="tg-18__preview">
      <p class="tg-18__prev-lbl">Result — native CSS recreation of the Tailwind output:</p>
      <h3 class="tg-18__demo-a">bg-gradient-to-r from-cyan-400 to-blue-600</h3>
      <h3 class="tg-18__demo-b">bg-gradient-to-br from-rose-400 via-fuchsia-500 to-indigo-500</h3>
      <h3 class="tg-18__demo-c">bg-gradient-to-r from-emerald-400 to-teal-600</h3>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-18,
.tg-18 *,
.tg-18 *::before,
.tg-18 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-18 ::selection {
  background: #6366f1;
  color: #fff;
}

.tg-18 {
  --g-a: #6366f1;
  --g-b: #9333ea;
  --bg: #ffffff;
  --surface: #f8fafc;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  --head-bg: #f1f5f9;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 40px 24px;
  display: flex;
  justify-content: center;
}

.tg-18__doc {
  max-width: 660px;
  width: 100%;
}

.tg-18__heading {
  font-size: clamp(1.4rem, 4vw, 2rem);
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.03em;
  line-height: 1.15;
  margin-bottom: 12px;
}

.tg-18__grad {
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-18__sub {
  font-size: .9rem;
  color: var(--muted);
  line-height: 1.65;
  margin-bottom: 24px;
  max-width: 520px;
}

.tg-18__table-wrap {
  overflow-x: auto;
  border: 1px solid var(--border);
  border-radius: 10px;
  margin-bottom: 24px;
}

.tg-18__table {
  width: 100%;
  border-collapse: collapse;
  font-size: .825rem;
}

.tg-18__table thead {
  background: var(--head-bg);
}

.tg-18__table th {
  text-align: left;
  padding: 10px 16px;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .07em;
  color: var(--muted);
  border-bottom: 1px solid var(--border);
}

.tg-18__table td {
  padding: 10px 16px;
  border-bottom: 1px solid var(--border);
  color: var(--text);
}

.tg-18__table tr:last-child td {
  border-bottom: none;
}

.tg-18__table code {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 2px 6px;
  font-size: .775em;
  color: var(--g-a);
  white-space: nowrap;
}

.tg-18__preview {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 20px;
}

.tg-18__prev-lbl {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .09em;
  color: var(--muted);
  margin-bottom: 12px;
}
/* Native CSS recreating Tailwind gradient-text utilities */

.tg-18__demo-a {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -.02em;
  background: linear-gradient(to right, #22d3ee, #2563eb);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  margin-bottom: 4px;
}

.tg-18__demo-b {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -.02em;
  background: linear-gradient(to bottom right, #fb7185, #d946ef, #6366f1);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  margin-bottom: 4px;
}

.tg-18__demo-c {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -.02em;
  background: linear-gradient(to right, #34d399, #0d9488);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

@media (prefers-reduced-motion: reduce) {
}
```
