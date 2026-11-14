---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/developer-documentation-sidebar-with-scroll-synced-nesting/"
title: "Developer Documentation Sidebar with Scroll-Synced Nesting"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The Stripe-style docs tree: three levels of nested navigation with depth-driven indentation from a single --depth custom property, a vertical guide rail…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Developer Documentation Sidebar with Scroll-Synced Nesting
Source: https://codefronts.com/layouts/css-sidebar-layouts/developer-documentation-sidebar-with-scroll-synced-nesting/

The Stripe-style docs tree: three levels of nested navigation with depth-driven indentation from a single --depth custom property, a vertical guide rail connecting each level, and the current section lit up automatically via :target as readers jump between anchors — no scroll-spy JavaScript.
## HTML
```html
<section class="sbl-04">
  <aside class="sbl-04__rail">
    <nav aria-label="Documentation">
      <ul class="sbl-04__tree">
        <li><a href="#sbl04-start">Getting started</a>
          <ul>
            <li><a href="#sbl04-install">Installation</a></li>
            <li><a href="#sbl04-auth">Authentication</a>
              <ul><li><a href="#sbl04-keys">API keys</a></li><li><a href="#sbl04-oauth">OAuth 2.0</a></li></ul>
            </li>
          </ul>
        </li>
        <li><a href="#sbl04-core">Core concepts</a>
          <ul><li><a href="#sbl04-webhooks">Webhooks</a></li><li><a href="#sbl04-errors">Error handling</a></li></ul>
        </li>
      </ul>
    </nav>
  </aside>
  <main class="sbl-04__doc">
    <section id="sbl04-start"><h1>Getting started</h1><p>Click any sidebar item — the matching link lights via :target, no scroll-spy script.</p></section>
    <section id="sbl04-install"><h2>Installation</h2><p>Install the SDK with your package manager of choice.</p></section>
    <section id="sbl04-auth"><h2>Authentication</h2><p>All requests are authenticated with a bearer token.</p></section>
    <section id="sbl04-keys"><h3>API keys</h3><p>Generate keys from the dashboard. Rotate them quarterly.</p></section>
    <section id="sbl04-oauth"><h3>OAuth 2.0</h3><p>Use the authorization-code flow for user-scoped access.</p></section>
    <section id="sbl04-core"><h2>Core concepts</h2><p>Resources, events and idempotency.</p></section>
    <section id="sbl04-webhooks"><h3>Webhooks</h3><p>Receive events at your endpoint within seconds.</p></section>
    <section id="sbl04-errors"><h3>Error handling</h3><p>Every error returns a typed code and a human message.</p></section>
  </main>
</section>
```
## CSS
```css
.sbl-04,
.sbl-04 *,
.sbl-04 *::before,
.sbl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-04 {
  --ink: oklch(0.27 0.015 265);
  --mut: oklch(0.52 0.012 265);
  --line: oklch(0.9 0.007 265);
  --accent: oklch(0.55 0.17 265);
  display: grid;
  grid-template-columns: 250px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.99 0.002 100);
  color: var(--ink);
}

.sbl-04__rail {
  border-right: 1px solid var(--line);
  padding: 24px 12px;
  overflow-y: auto;
}

.sbl-04__tree {
  --depth: 0;
  list-style: none;
}

.sbl-04__tree ul {
  --depth: 1;
  list-style: none;
  border-inline-start: 1px solid var(--line);
  margin-inline-start: calc(12px + (var(--depth) - 1) * 16px + 7px);
}

.sbl-04__tree ul ul {
  --depth: 2;
  margin-inline-start: 15px;
}

.sbl-04__tree a {
  display: block;
  padding: 7px 10px 7px calc(12px + var(--depth) * 14px);
  margin: 1px 0;
  border-radius: 8px;
  font: 500 13.5px/1.3 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: color .15s ease,background-color .15s ease;
}

.sbl-04__tree ul a {
  padding-inline-start: 12px;
}

.sbl-04__tree a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 5%,transparent);
}

.sbl-04__tree a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-04:has(#sbl04-start:target) a[href="#sbl04-start"],
.sbl-04:has(#sbl04-install:target) a[href="#sbl04-install"],
.sbl-04:has(#sbl04-auth:target) a[href="#sbl04-auth"],
.sbl-04:has(#sbl04-keys:target) a[href="#sbl04-keys"],
.sbl-04:has(#sbl04-oauth:target) a[href="#sbl04-oauth"],
.sbl-04:has(#sbl04-core:target) a[href="#sbl04-core"],
.sbl-04:has(#sbl04-webhooks:target) a[href="#sbl04-webhooks"],
.sbl-04:has(#sbl04-errors:target) a[href="#sbl04-errors"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 10%,transparent);
  font-weight: 600;
}

.sbl-04__doc {
  overflow-y: auto;
  scroll-behavior: smooth;
  padding: 36px 44px;
  display: grid;
  gap: 34px;
  align-content: start;
}

.sbl-04__doc section {
  scroll-margin-top: 24px;
}

.sbl-04__doc h1 {
  font: 700 26px/1.2 system-ui,sans-serif;
}

.sbl-04__doc h2 {
  font: 650 20px/1.25 system-ui,sans-serif;
}

.sbl-04__doc h3 {
  font: 600 16px/1.3 system-ui,sans-serif;
}

.sbl-04__doc p {
  margin-top: 8px;
  color: var(--mut);
  font-size: 14px;
  line-height: 1.65;
  max-width: 58ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-04__doc {
    scroll-behavior: auto;
  }

  .sbl-04__tree a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — indentation derives from one --depth variable per nesting level; the active link lights via .sbl-04:has(#id:target) a[href="#id"]. */
```
