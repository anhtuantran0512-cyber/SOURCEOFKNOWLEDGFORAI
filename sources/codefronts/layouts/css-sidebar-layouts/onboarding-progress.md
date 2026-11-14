---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/onboarding-progress/"
title: "Onboarding Wizard Sidebar Layout with Step Progress Tracking"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The setup-wizard rail: an ordered list of steps with completed/current/upcoming states, checkmark badges, a connecting line that FILLS with accent color up…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Onboarding Wizard Sidebar Layout with Step Progress Tracking
Source: https://codefronts.com/layouts/css-sidebar-layouts/onboarding-progress/

The setup-wizard rail: an ordered list of steps with completed/current/upcoming states, checkmark badges, a connecting line that FILLS with accent color up to the current step, and CSS counters numbering the pending steps automatically — add or remove a step and the numbering, line and states all recompute.
## HTML
```html
<section class="sbl-26">
  <aside class="sbl-26__rail" aria-label="Setup progress">
    <h2 class="sbl-26__title">Workspace setup</h2>
    <ol class="sbl-26__steps">
      <li data-state="done"><span class="sbl-26__badge" aria-hidden="true"></span><div><strong>Create account</strong><small>[email protected] verified</small></div></li>
      <li data-state="done"><span class="sbl-26__badge" aria-hidden="true"></span><div><strong>Invite your team</strong><small>4 teammates joined</small></div></li>
      <li data-state="current" aria-current="step"><span class="sbl-26__badge" aria-hidden="true"></span><div><strong>Connect data source</strong><small>Postgres, BigQuery or CSV</small></div></li>
      <li data-state="todo"><span class="sbl-26__badge" aria-hidden="true"></span><div><strong>Build first dashboard</strong><small>From a template or scratch</small></div></li>
      <li data-state="todo"><span class="sbl-26__badge" aria-hidden="true"></span><div><strong>Set up alerts</strong><small>Slack or email digests</small></div></li>
    </ol>
  </aside>
  <main class="sbl-26__main"><h1>Connect data source</h1><p>The rail is an &lt;ol&gt; with three data-states — counters number the todos, checkmarks replace done numbers, and the connector fills behind you.</p><button class="sbl-26__btn" type="button">Connect Postgres</button></main>
</section>
```
## CSS
```css
.sbl-26,
.sbl-26 *,
.sbl-26 *::before,
.sbl-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-26 {
  --panel: oklch(0.965 0.006 275);
  --ink: oklch(0.26 0.02 275);
  --mut: oklch(0.5 0.015 275);
  --line: oklch(0.88 0.008 275);
  --accent: oklch(0.55 0.18 285);
  display: grid;
  grid-template-columns: 300px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.99 0.002 275);
  color: var(--ink);
}

.sbl-26__rail {
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 26px 22px;
  overflow-y: auto;
}

.sbl-26__title {
  font: 700 15px/1 system-ui,sans-serif;
  margin-bottom: 24px;
}

.sbl-26__steps {
  list-style: none;
  counter-reset: sbl26;
  display: flex;
  flex-direction: column;
}

.sbl-26__steps li {
  counter-increment: sbl26;
  position: relative;
  display: grid;
  grid-template-columns: 28px 1fr;
  gap: 14px;
  padding-bottom: 28px;
}

.sbl-26__steps li:last-child {
  padding-bottom: 0;
}

.sbl-26__steps li::after {
  content: "";
  position: absolute;
  left: 13.5px;
  top: 32px;
  bottom: 4px;
  width: 2px;
  border-radius: 2px;
  background: var(--line);
  z-index: 0;
}

.sbl-26__steps li:last-child::after {
  display: none;
}

.sbl-26__steps li[data-state="done"]::after {
  background: var(--accent);
}

.sbl-26__badge {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 2px solid var(--line);
  background: #fff;
  font: 700 12px/1 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-26__badge::before {
  content: counter(sbl26);
}

li[data-state="done"] .sbl-26__badge {
  border-color: var(--accent);
  background: var(--accent);
}

li[data-state="done"] .sbl-26__badge::before {
  content: "";
  width: 12px;
  height: 12px;
  background: #fff;
  -webkit-mask: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12.5 5.5 5.5L20 6.5"/></svg>') center/contain no-repeat;
  mask: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12.5 5.5 5.5L20 6.5"/></svg>') center/contain no-repeat;
}

li[data-state="current"] .sbl-26__badge {
  border-color: var(--accent);
  color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 18%,transparent);
}

.sbl-26__steps strong {
  display: block;
  font: 600 13.5px/1.3 system-ui,sans-serif;
}

.sbl-26__steps small {
  font: 400 12px/1.45 system-ui,sans-serif;
  color: var(--mut);
}

li[data-state="todo"] strong {
  color: var(--mut);
}

li[data-state="current"] strong {
  color: var(--accent);
}

.sbl-26__main {
  padding: 36px;
  overflow-y: auto;
}

.sbl-26__main h1 {
  font: 650 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-26__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.65;
  max-width: 52ch;
  margin-bottom: 22px;
  text-wrap: pretty;
}

.sbl-26__btn {
  padding: 12px 22px;
  border: none;
  border-radius: 11px;
  background: var(--accent);
  color: #fff;
  font: 600 14px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: filter .2s ease;
}

.sbl-26__btn:hover {
  filter: brightness(1.1);
}

.sbl-26__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-26__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS counters number the steps, data-state drives badge/connector styling, aria-current="step" marks the live step for AT. */
```
