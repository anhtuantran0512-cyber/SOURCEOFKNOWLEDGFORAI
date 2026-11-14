---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/github-style-commit-history-timeline/"
title: "GitHub-Style Commit History Timeline"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The developer-native vertical log: circular commit markers on a continuous rail, monospace hashes, relative timestamps and merge badges — the exact pattern…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: GitHub-Style Commit History Timeline
Source: https://codefronts.com/layouts/css-timelines/github-style-commit-history-timeline/

The developer-native vertical log: circular commit markers on a continuous rail, monospace hashes, relative timestamps and merge badges — the exact pattern for changelogs, release notes and activity feeds, built on a semantic <ol> so screen readers announce it as the numbered sequence it is.
## HTML
```html
<section class="tls-01" aria-label="Commit history timeline demo">
  <div class="tls-01__panel">
    <header class="tls-01__head"><span class="tls-01__branch">main</span><span class="tls-01__count">128 commits</span></header>
    <ol class="tls-01__list" role="list" aria-label="Recent commits">
      <li class="tls-01__item tls-01__item--merge">
        <div class="tls-01__row">
          <p class="tls-01__msg">Merge pull request <a class="tls-01__link" href="#pr">#482</a> — container query layout engine</p>
          <p class="tls-01__meta"><b>mara-k</b> merged <code class="tls-01__hash">9f3ae12</code> · <time datetime="2026-07-18T14:02">2 hours ago</time></p>
        </div>
      </li>
      <li class="tls-01__item">
        <div class="tls-01__row">
          <p class="tls-01__msg">Fix seam flicker on Safari during marker transition</p>
          <p class="tls-01__meta"><b>dev-anand</b> committed <code class="tls-01__hash">c71b04d</code> · <time datetime="2026-07-18T09:41">7 hours ago</time></p>
        </div>
      </li>
      <li class="tls-01__item">
        <div class="tls-01__row">
          <p class="tls-01__msg">Add prefers-reduced-motion fallbacks to all entrance effects</p>
          <p class="tls-01__meta"><b>jwhit</b> committed <code class="tls-01__hash">4e98f2a</code> · <time datetime="2026-07-17T18:20">yesterday</time></p>
        </div>
      </li>
      <li class="tls-01__item tls-01__item--tag">
        <div class="tls-01__row">
          <p class="tls-01__msg">Release v2.4.0 <span class="tls-01__badge">tag</span></p>
          <p class="tls-01__meta"><b>release-bot</b> tagged <code class="tls-01__hash">b02cd91</code> · <time datetime="2026-07-16T11:00">2 days ago</time></p>
        </div>
      </li>
      <li class="tls-01__item">
        <div class="tls-01__row">
          <p class="tls-01__msg">Refactor rail drawing to per-item pseudo-elements</p>
          <p class="tls-01__meta"><b>tokafor</b> committed <code class="tls-01__hash">77aa310</code> · <time datetime="2026-07-15T16:44">3 days ago</time></p>
        </div>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-01,
.tls-01 *,
.tls-01 *::before,
.tls-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-01 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #1f883d;
  --tl-merge: #8250df;
  --tl-line: #d1d9e0;
  --tl-bg: #ffffff;
  --tl-ink: #1f2328;
  --tl-mut: #59636e;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f6f8fa;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-01__panel {
  width: min(640px,100%);
  background: var(--tl-bg);
  border: 1px solid var(--tl-line);
  border-radius: 12px;
  overflow: hidden;
}

.tls-01__head {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 20px;
  border-bottom: 1px solid var(--tl-line);
  background: #f6f8fa;
}

.tls-01__branch {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  font-weight: 600;
  color: var(--tl-ink);
  background: #eff2f5;
  border: 1px solid var(--tl-line);
  border-radius: 6px;
  padding: 2px 8px;
}

.tls-01__count {
  font-size: 12px;
  color: var(--tl-mut);
}

.tls-01__list {
  list-style: none;
  padding: 8px 20px 12px;
}

.tls-01__item {
  position: relative;
  padding-left: 32px;
}

.tls-01__item::before {
  content: '';
  position: absolute;
  left: 8px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: var(--tl-line);
}

.tls-01__item:first-child::before {
  top: 22px;
}

.tls-01__item:last-child::before {
  bottom: calc(100% - 22px);
}

.tls-01__item::after {
  content: '';
  position: absolute;
  left: 3px;
  top: 16px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--tl-bg);
  border: 3px solid var(--tl-accent);
  box-shadow: 0 0 0 4px var(--tl-bg);
}

.tls-01__item--merge::after {
  border-color: var(--tl-merge);
}

.tls-01__item--tag::after {
  border-radius: 3px;
  rotate: 45deg;
}

.tls-01__row {
  padding: 12px 12px 12px 4px;
  border-radius: 8px;
  transition: background .15s;
}

.tls-01__row:hover {
  background: #f6f8fa;
}

.tls-01__msg {
  font-size: 14px;
  font-weight: 600;
  color: var(--tl-ink);
  line-height: 1.45;
  text-wrap: pretty;
}

.tls-01__link {
  color: var(--tl-accent);
  text-decoration: none;
}

.tls-01__link:hover {
  text-decoration: underline;
}

.tls-01__badge {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--tl-merge);
  border: 1px solid currentColor;
  border-radius: 999px;
  padding: 1px 8px;
  margin-left: 6px;
  vertical-align: 2px;
}

.tls-01__meta {
  font-size: 12px;
  color: var(--tl-mut);
  margin-top: 4px;
}

.tls-01__meta b {
  font-weight: 600;
  color: var(--tl-ink);
}

.tls-01__hash {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tl-accent);
  background: #eff2f5;
  border-radius: 4px;
  padding: 1px 5px;
}
```

## JavaScript
```js
/* No JavaScript — the rail is a per-item ::before trimmed at :first/:last-child; markers are ::after circles ring-punched with a box-shadow of the background token. */
```
