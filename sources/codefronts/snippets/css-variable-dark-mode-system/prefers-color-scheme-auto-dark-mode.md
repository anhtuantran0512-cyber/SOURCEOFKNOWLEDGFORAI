---
source: "codefronts"
url: "https://codefronts.com/snippets/css-variable-dark-mode-system/prefers-color-scheme-auto-dark-mode/"
title: "Pure CSS Automatic Dark Mode with prefers-color-scheme and Custom Properties (Zero JavaScript)"
section: "snippets"
category: "css-variable-dark-mode-system"
category_name: "CSS Variable Dark Mode Systems"
description: "The lightest possible dark mode: no toggle, no script, no localStorage."
has_js: "false"
---

Here's a working CSS Variable Dark Mode System from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Automatic Dark Mode with prefers-color-scheme and Custom Properties (Zero JavaScript)
Source: https://codefronts.com/snippets/css-variable-dark-mode-system/prefers-color-scheme-auto-dark-mode/

The lightest possible dark mode: no toggle, no script, no localStorage. A single set of five CSS custom properties is redefined inside @media (prefers-color-scheme: dark), so the whole card re-skins itself the instant the visitor's operating system (macOS, iOS, Windows, Android) is in dark mode — and back again. This is the zero-maintenance baseline every site should ship before it adds a manual toggle.
## HTML
```html
<section class="cdm-01">
  <article class="cdm-01__card">
    <span class="cdm-01__badge"><span class="cdm-01__dot" aria-hidden="true"></span>Auto · follows your OS appearance</span>
    <header class="cdm-01__head">
      <span class="cdm-01__avatar" aria-hidden="true">CF</span>
      <div><strong>CodeFronts Studio</strong><small>[email protected]</small></div>
    </header>
    <p class="cdm-01__copy">No toggle, no JavaScript. This card reads your system appearance with <code>prefers-color-scheme</code> and re-skins itself from five CSS variables.</p>
    <dl class="cdm-01__stats">
      <div><dt>Plan</dt><dd>Studio</dd></div>
      <div><dt>Seats</dt><dd>8 / 10</dd></div>
      <div><dt>Renews</dt><dd>Aug 1</dd></div>
    </dl>
    <a class="cdm-01__btn" href="#">Manage subscription</a>
  </article>
</section>
```
## CSS
```css
.cdm-01,
.cdm-01 *,
.cdm-01 *::before,
.cdm-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdm-01 {
  /* ── the 5-variable system: light defaults ── */
  --bg: oklch(0.98 0.004 250);
  --surface: oklch(1 0 0);
  --text: oklch(0.24 0.02 265);
  --border: oklch(0.9 0.008 265);
  --accent: oklch(0.55 0.18 264);
  /* ── everything below is DERIVED from the five above ── */
  --muted: color-mix(in oklab,var(--text) 60%,var(--bg));
  --hover: color-mix(in oklab,var(--text) 7%,transparent);
  --ring: color-mix(in oklab,var(--accent) 45%,transparent);
  color-scheme: light dark;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 32px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
  transition: background-color .3s ease,color .3s ease;
}

@media (prefers-color-scheme: dark) {
  .cdm-01 {
    --bg: oklch(0.16 0.02 265);
    --surface: oklch(0.21 0.02 265);
    --text: oklch(0.95 0.005 265);
    --border: oklch(0.32 0.02 265);
    --accent: oklch(0.72 0.16 264);
  }
}

.cdm-01__card {
  width: min(400px,100%);
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding: 26px;
  border-radius: 20px;
  background: var(--surface);
  border: 1px solid var(--border);
  box-shadow: 0 18px 50px -24px oklch(0 0 0 / .4);
  transition: background-color .3s ease,border-color .3s ease;
}

.cdm-01__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  align-self: flex-start;
  padding: 6px 12px;
  border-radius: 999px;
  font: 600 11.5px/1 system-ui,sans-serif;
  letter-spacing: .02em;
  color: var(--muted);
  background: var(--hover);
}

.cdm-01__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 4px var(--ring);
}

.cdm-01__head {
  display: flex;
  align-items: center;
  gap: 13px;
  font: 500 14px/1.35 system-ui,sans-serif;
}

.cdm-01__head small {
  display: block;
  color: var(--muted);
  font-size: 12.5px;
}

.cdm-01__avatar {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  font: 700 14px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(140deg,var(--accent),oklch(from var(--accent) l calc(c*0.8) calc(h + 40)));
}

.cdm-01__copy {
  font: 400 14px/1.6 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.cdm-01__copy code {
  font: 600 12.5px/1 ui-monospace,Menlo,monospace;
  padding: 2px 5px;
  border-radius: 5px;
  background: var(--hover);
  color: var(--text);
}

.cdm-01__stats {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 8px;
  padding: 14px 0;
  border-block: 1px solid var(--border);
}

.cdm-01__stats dt {
  font: 600 10.5px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--muted);
  margin-bottom: 6px;
}

.cdm-01__stats dd {
  font: 600 16px/1 system-ui,sans-serif;
}

.cdm-01__btn {
  display: block;
  text-align: center;
  padding: 12px;
  border-radius: 11px;
  font: 600 14px/1 system-ui,sans-serif;
  text-decoration: none;
  color: #fff;
  background: var(--accent);
  transition: filter .2s ease;
}

.cdm-01__btn:hover {
  filter: brightness(1.08);
}

.cdm-01__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cdm-01,
    .cdm-01 * {
    transition: none!important;
  }
}
```
