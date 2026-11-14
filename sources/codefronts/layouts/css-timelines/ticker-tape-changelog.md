---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/ticker-tape-changelog/"
title: "SaaS Changelog Timeline — Version Badges with Sticky Month Rail"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The docs-site staple: releases on a left rail with semver badges, category chips (New / Improved / Fixed) double-coded with glyphs, and month labels that…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Changelog Timeline — Version Badges with Sticky Month Rail
Source: https://codefronts.com/layouts/css-timelines/ticker-tape-changelog/

The docs-site staple: releases on a left rail with semver badges, category chips (New / Improved / Fixed) double-coded with glyphs, and month labels that stick in the gutter as their releases scroll by — the layout Linear, Stripe and every serious devtool converged on for 'What's new' pages.
## HTML
```html
<section class="tls-27" aria-label="Changelog timeline demo">
  <div class="tls-27__inner">
    <h3 class="tls-27__title">What's new</h3>
    <div class="tls-27__month">
      <p class="tls-27__mlabel">Jul<br>2026</p>
      <div class="tls-27__entries">
        <article class="tls-27__rel tls-27__rel--major">
          <header class="tls-27__rhead"><code class="tls-27__ver">v3.0.0</code><time datetime="2026-07-14">Jul 14</time></header>
          <h4 class="tls-27__rtitle">The big one: workspaces</h4>
          <ul class="tls-27__list" role="list">
            <li><span class="tls-27__kind" data-kind="new">New</span>Multi-workspace accounts with per-workspace billing</li>
            <li><span class="tls-27__kind" data-kind="new">New</span>Granular roles: admin, editor, commenter, guest</li>
            <li><span class="tls-27__kind" data-kind="improved">Improved</span>Search is 6× faster on large orgs</li>
          </ul>
        </article>
        <article class="tls-27__rel">
          <header class="tls-27__rhead"><code class="tls-27__ver">v2.14.1</code><time datetime="2026-07-03">Jul 3</time></header>
          <ul class="tls-27__list" role="list">
            <li><span class="tls-27__kind" data-kind="fixed">Fixed</span>Exported CSVs no longer double-escape quotes</li>
            <li><span class="tls-27__kind" data-kind="fixed">Fixed</span>Safari: date picker closes on first tap again</li>
          </ul>
        </article>
      </div>
    </div>
    <div class="tls-27__month">
      <p class="tls-27__mlabel">Jun<br>2026</p>
      <div class="tls-27__entries">
        <article class="tls-27__rel">
          <header class="tls-27__rhead"><code class="tls-27__ver">v2.14.0</code><time datetime="2026-06-19">Jun 19</time></header>
          <h4 class="tls-27__rtitle">Automations, round two</h4>
          <ul class="tls-27__list" role="list">
            <li><span class="tls-27__kind" data-kind="new">New</span>Scheduled triggers (cron syntax supported)</li>
            <li><span class="tls-27__kind" data-kind="improved">Improved</span>Run history keeps 90 days on all plans</li>
            <li><span class="tls-27__kind" data-kind="fixed">Fixed</span>Webhook retries respect Retry-After headers</li>
          </ul>
        </article>
        <article class="tls-27__rel">
          <header class="tls-27__rhead"><code class="tls-27__ver">v2.13.2</code><time datetime="2026-06-05">Jun 5</time></header>
          <ul class="tls-27__list" role="list">
            <li><span class="tls-27__kind" data-kind="improved">Improved</span>Keyboard nav: J/K move between rows everywhere</li>
          </ul>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-27,
.tls-27 *,
.tls-27 *::before,
.tls-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-27 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #4f46e5;
  --tl-line: #e5e7eb;
  --tl-bg: #ffffff;
  --tl-ink: #111827;
  --tl-mut: #6b7280;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--tl-bg);
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-27__inner {
  width: min(620px,100%);
}

.tls-27__title {
  font-size: clamp(22px,3.5vw,28px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
  margin-bottom: 32px;
}

.tls-27__month {
  display: grid;
  grid-template-columns: 64px 1fr;
  gap: 20px;
}

.tls-27__mlabel {
  position: sticky;
  top: 24px;
  align-self: start;
  font-size: 13px;
  font-weight: 800;
  line-height: 1.3;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--tl-mut);
  text-align: right;
  padding-top: 2px;
}

.tls-27__entries {
  position: relative;
  padding: 0 0 36px 26px;
  border-left: 2px solid var(--tl-line);
}

.tls-27__rel {
  position: relative;
  padding-bottom: 28px;
}

.tls-27__rel:last-child {
  padding-bottom: 0;
}

.tls-27__rel::before {
  content: '';
  position: absolute;
  left: -33px;
  top: 5px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--tl-bg);
  border: 3px solid var(--tl-accent);
  box-shadow: 0 0 0 4px var(--tl-bg);
}

.tls-27__rel--major::before {
  left: -35px;
  width: 14px;
  height: 14px;
  background: var(--tl-accent);
}

.tls-27__rhead {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 8px;
}

.tls-27__ver {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  font-weight: 700;
  color: var(--tl-accent);
  background: #eef2ff;
  border-radius: 6px;
  padding: 2px 8px;
}

.tls-27__rel--major .tls-27__ver {
  color: #fff;
  background: var(--tl-accent);
}

.tls-27__rhead time {
  font-size: 12.5px;
  color: var(--tl-mut);
}

.tls-27__rtitle {
  font-size: 16.5px;
  font-weight: 750;
  color: var(--tl-ink);
  letter-spacing: -.01em;
  margin-bottom: 10px;
}

.tls-27__list {
  list-style: none;
  display: grid;
  gap: 8px;
}

.tls-27__list li {
  display: flex;
  align-items: baseline;
  gap: 10px;
  font-size: 14px;
  line-height: 1.55;
  color: #374151;
  text-wrap: pretty;
}

.tls-27__kind {
  flex: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .04em;
  border-radius: 999px;
  padding: 2px 9px;
  min-width: 64px;
  justify-content: center;
}

.tls-27__kind::before {
  font-weight: 800;
}

.tls-27__kind[data-kind="new"] {
  color: #166534;
  background: #f0fdf4;
}

.tls-27__kind[data-kind="new"]::before {
  content: '+';
}

.tls-27__kind[data-kind="improved"] {
  color: #1d4ed8;
  background: #eff6ff;
}

.tls-27__kind[data-kind="improved"]::before {
  content: '↑';
}

.tls-27__kind[data-kind="fixed"] {
  color: #9a3412;
  background: #fff7ed;
}

.tls-27__kind[data-kind="fixed"]::before {
  content: '✓';
}

@media (max-width: 520px) {
  .tls-27__month {
    grid-template-columns: 1fr;
  }

  .tls-27__mlabel {
    position: static;
    text-align: left;
    padding-bottom: 10px;
  }

  .tls-27__mlabel br {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — month labels are position:sticky inside their month group; category chips are data-kind attributes rendering glyph + text (never color alone). */
```
