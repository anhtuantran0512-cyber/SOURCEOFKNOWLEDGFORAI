---
source: "codefronts"
url: "https://codefronts.com/snippets/css-custom-cursor/svg-brand-pointer/"
title: "Custom SVG Brand Pointer with the CSS cursor url() Property and a Keyword Fallback"
section: "snippets"
category: "css-custom-cursor"
category_name: "CSS Custom Cursor Styles"
description: "The lightest possible custom cursor: no script, no image file, no request."
has_js: "false"
---

Here's a working CSS Custom Cursor Style from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom SVG Brand Pointer with the CSS cursor url() Property and a Keyword Fallback
Source: https://codefronts.com/snippets/css-custom-cursor/svg-brand-pointer/

The lightest possible custom cursor: no script, no image file, no request. A single inline SVG data-URI replaces the default arrow through cursor: url(...) with a hotspot offset, and a native keyword (auto / pointer) always follows the comma as a guaranteed fallback. Clickable links get their own distinct pointer, so affordance stays obvious. This is the performance-friendly baseline every brand site should reach for first.
## HTML
```html
<section class="ccs-01">
  <div class="ccs-01__stage">
    <span class="ccs-01__hint" aria-hidden="true">Move your pointer across this panel</span>
    <article class="ccs-01__card">
      <span class="ccs-01__avatar" aria-hidden="true">CF</span>
      <h2>Custom brand pointer</h2>
      <p>The default arrow is replaced by an inline SVG through <code>cursor: url()</code> — no image file, no request, always with a keyword fallback.</p>
      <div class="ccs-01__actions">
        <a class="ccs-01__btn" href="#">Links get their own cursor</a>
        <a class="ccs-01__btn ccs-01__btn--ghost" href="#">Secondary</a>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
.ccs-01,
.ccs-01 *,
.ccs-01 *::before,
.ccs-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccs-01 {
  --bg: oklch(0.16 0.02 265);
  --surface: oklch(0.21 0.02 265);
  --text: oklch(0.95 0.005 265);
  --border: oklch(0.32 0.02 265);
  --accent: oklch(0.72 0.17 264);
  --muted: color-mix(in oklab,var(--text) 58%,var(--bg));
  --hover: color-mix(in oklab,var(--text) 8%,transparent);
  color-scheme: dark;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 28px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
}

.ccs-01__stage {
  position: relative;
  width: min(460px,100%);
  display: grid;
  place-items: center;
  padding: 40px 24px;
  border-radius: 22px;
  background: radial-gradient(120% 120% at 50% 0%,var(--surface),var(--bg));
  border: 1px solid var(--border);
}

.ccs-01__hint {
  position: absolute;
  top: 14px;
  left: 16px;
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .02em;
  color: var(--muted);
}

.ccs-01__card {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 26px;
  border-radius: 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  box-shadow: 0 20px 50px -28px oklch(0 0 0/.7);
}

.ccs-01__avatar {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 14px;
  font: 700 15px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(140deg,var(--accent),oklch(from var(--accent) l calc(c*0.85) calc(h + 45)));
}

.ccs-01__card h2 {
  font: 700 20px/1.15 system-ui,sans-serif;
  letter-spacing: -.01em;
}

.ccs-01__card p {
  font: 400 14px/1.6 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.ccs-01__card code {
  font: 600 12px/1 ui-monospace,Menlo,monospace;
  padding: 2px 5px;
  border-radius: 5px;
  background: var(--hover);
  color: var(--text);
}

.ccs-01__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 4px;
}

.ccs-01__btn {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 11px;
  font: 600 13.5px/1 system-ui,sans-serif;
  text-decoration: none;
  color: #fff;
  background: var(--accent);
}

.ccs-01__btn--ghost {
  color: var(--text);
  background: transparent;
  border: 1px solid var(--border);
}

.ccs-01__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}
/* ── the custom cursors: pointer-only so touch users are untouched ── */

@media (hover: hover) and (pointer: fine) {
  .ccs-01__stage {
    cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'%3E%3Cpath d='M4 3 12 24l3.1-8.6L24 12z' fill='%230b0b12' stroke='%23ffffff' stroke-width='2' stroke-linejoin='round'/%3E%3C/svg%3E") 4 3, auto;
  }

  .ccs-01__btn,
    .ccs-01__hint {
    cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3E%3Ccircle cx='15' cy='15' r='9' fill='none' stroke='%23ffffff' stroke-width='2'/%3E%3Ccircle cx='15' cy='15' r='3' fill='%237c9cff'/%3E%3C/svg%3E") 15 15, pointer;
  }
}
```

## JavaScript
```js
/* No JavaScript by design — cursor: url() is a pure-CSS property. */
```
