---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/dynamic-scroll-container-shadows/"
title: "Dynamic Scroll Container Shadows"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The utility every dashboard needs: a scrollable panel grows a soft top shadow the instant content is hidden above, and a bottom shadow while content remains…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dynamic Scroll Container Shadows
Source: https://codefronts.com/motion/css-animation-timeline/dynamic-scroll-container-shadows/

The utility every dashboard needs: a scrollable panel grows a soft top shadow the instant content is hidden above, and a bottom shadow while content remains below — each fading out exactly at the boundary — using animation-timeline: scroll(self), the timeline that tracks the container's OWN scrollbar.
## HTML
```html
<section class="sda-07" aria-label="Scrollable pricing table with dynamic edge shadows">
  <div class="sda-07__frame">
    <header class="sda-07__head"><h2>Plan comparison</h2><p>Scroll the table — edge shadows appear only where content hides.</p></header>
    <div class="sda-07__scroller" role="region" aria-label="Pricing rows, scrollable" tabindex="0">
      <div class="sda-07__shadow sda-07__shadow--top" aria-hidden="true"></div>
      <table class="sda-07__table">
        <thead><tr><th scope="col">Feature</th><th scope="col">Free</th><th scope="col">Pro</th><th scope="col">Team</th></tr></thead>
        <tbody>
          <tr><th scope="row">Projects</th><td>3</td><td>Unlimited</td><td>Unlimited</td></tr>
          <tr><th scope="row">Collaborators</th><td>1</td><td>5</td><td>Unlimited</td></tr>
          <tr><th scope="row">Version history</th><td>7 days</td><td>90 days</td><td>Forever</td></tr>
          <tr><th scope="row">Custom domains</th><td>—</td><td>1</td><td>10</td></tr>
          <tr><th scope="row">Analytics</th><td>Basic</td><td>Full</td><td>Full + export</td></tr>
          <tr><th scope="row">SSO / SAML</th><td>—</td><td>—</td><td>✓</td></tr>
          <tr><th scope="row">Audit log</th><td>—</td><td>30 days</td><td>1 year</td></tr>
          <tr><th scope="row">Priority support</th><td>—</td><td>✓</td><td>✓ dedicated</td></tr>
          <tr><th scope="row">API rate limit</th><td>100/h</td><td>5k/h</td><td>50k/h</td></tr>
          <tr><th scope="row">Sandbox envs</th><td>—</td><td>1</td><td>5</td></tr>
          <tr><th scope="row">Price</th><td>$0</td><td>$16/mo</td><td>$49/mo</td></tr>
        </tbody>
      </table>
      <div class="sda-07__shadow sda-07__shadow--btm" aria-hidden="true"></div>
    </div>
    <p class="sda-07__note">Powered by <code>animation-timeline: scroll(self)</code> — the container watches its own scrollbar.</p>
  </div>
</section>
```
## CSS
```css
.sda-07,
.sda-07 *,
.sda-07 *::before,
.sda-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-07 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: oklch(0.95 0.008 260);
  color: oklch(0.25 0.02 260);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  padding: 40px 20px;
}

.sda-07__frame {
  width: min(560px,92vw);
}

.sda-07__head {
  margin-bottom: 18px;
}

.sda-07__head h2 {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -.015em;
}

.sda-07__head p {
  font-size: 14px;
  color: oklch(0.5 0.02 260);
  margin-top: 6px;
}

.sda-07__scroller {
  position: relative;
  height: 320px;
  overflow-y: auto;
  background: #fff;
  border: 1px solid oklch(0.88 0.01 260);
  border-radius: 16px;
  overscroll-behavior: contain;
}

.sda-07__scroller:focus-visible {
  outline: 3px solid oklch(0.55 0.18 264);
  outline-offset: 2px;
}

.sda-07__shadow {
  position: sticky;
  left: 0;
  height: 26px;
  pointer-events: none;
  z-index: 2;
  opacity: 1;
}

.sda-07__shadow--top {
  top: 0;
  margin-bottom: -26px;
  background: linear-gradient(rgba(20,25,45,.16),transparent);
}

.sda-07__shadow--btm {
  bottom: 0;
  margin-top: -26px;
  background: linear-gradient(transparent,rgba(20,25,45,.16));
}

.sda-07__table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.sda-07__table th,
.sda-07__table td {
  padding: 13px 16px;
  text-align: left;
  border-bottom: 1px solid oklch(0.92 0.008 260);
}

.sda-07__table thead th {
  position: sticky;
  top: 0;
  background: #fff;
  z-index: 1;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.45 0.02 260);
}

.sda-07__table tbody th {
  font-weight: 600;
}

.sda-07__table td {
  color: oklch(0.38 0.02 260);
}

.sda-07__note {
  margin-top: 14px;
  font-size: 12.5px;
  color: oklch(0.52 0.02 260);
}

.sda-07__note code {
  font: 600 12px ui-monospace,Menlo,monospace;
  background: oklch(0.9 0.01 260);
  padding: 2px 6px;
  border-radius: 5px;
}

@supports (animation-timeline: scroll(self)) {
  .sda-07__shadow--top {
    opacity: 0;
    animation: sda-07-in linear both;
    animation-timeline: scroll(self);
    animation-range: 0 48px;
  }

  .sda-07__shadow--btm {
    animation: sda-07-out linear both;
    animation-timeline: scroll(self);
    animation-range: calc(100% - 48px) 100%;
  }
}

@keyframes sda-07-in {
  to {
    opacity: 1;
  }
}

@keyframes sda-07-out {
  from {
    opacity: 1;
  }

  to {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-07__shadow {
    animation-timing-function: steps(2);
  }
}
```

## JavaScript
```js
/* No JavaScript — scroll(self) binds each sticky shadow strip's opacity to the container's OWN scroll position; ranges 0–48px and (100% − 48px)–100% make the fade exact at both edges. */
```
