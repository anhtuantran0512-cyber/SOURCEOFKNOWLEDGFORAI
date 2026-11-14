---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/thread-timeline/"
title: "Conversation Thread Timeline — Nested Replies with Curved Connectors"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The social-thread structure: a chronological root post with nested replies hanging off curved elbow connectors (border-radius corners, no SVG),…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Conversation Thread Timeline — Nested Replies with Curved Connectors
Source: https://codefronts.com/layouts/css-timelines/thread-timeline/

The social-thread structure: a chronological root post with nested replies hanging off curved elbow connectors (border-radius corners, no SVG), avatar-anchored rails that stop exactly at the last child, and collapse toggles built from <details> — the hierarchy-plus-time layout of comment systems, support threads and design-review trails.
## HTML
```html
<section class="tls-15" aria-label="Thread timeline demo">
  <div class="tls-15__thread">
    <article class="tls-15__post">
      <span class="tls-15__av" style="--a:#0e7490" aria-hidden="true">SL</span>
      <div class="tls-15__bubble">
        <p class="tls-15__meta"><b>sam.lowe</b> · <time datetime="2026-07-18T10:02">10:02</time></p>
        <p class="tls-15__txt">Proposal: we drop the modal and inline the whole review flow. Thread below with the tradeoffs.</p>
      </div>
    </article>
    <details class="tls-15__replies" open>
      <summary class="tls-15__toggle">3 replies</summary>
      <div class="tls-15__reveal"><div class="tls-15__inner">
        <article class="tls-15__post tls-15__post--child" style="--depth:1">
          <span class="tls-15__av" style="--a:#a21caf" aria-hidden="true">RK</span>
          <div class="tls-15__bubble">
            <p class="tls-15__meta"><b>rhea.k</b> · <time datetime="2026-07-18T10:11">10:11</time></p>
            <p class="tls-15__txt">Strong yes. The modal hides the diff context people need mid-review.</p>
          </div>
        </article>
        <article class="tls-15__post tls-15__post--child" style="--depth:1">
          <span class="tls-15__av" style="--a:#b45309" aria-hidden="true">JT</span>
          <div class="tls-15__bubble">
            <p class="tls-15__meta"><b>jtan</b> · <time datetime="2026-07-18T10:26">10:26</time></p>
            <p class="tls-15__txt">Only worry is keyboard focus order when the flow inlines mid-list.</p>
          </div>
        </article>
        <article class="tls-15__post tls-15__post--child" style="--depth:2">
          <span class="tls-15__av" style="--a:#0e7490" aria-hidden="true">SL</span>
          <div class="tls-15__bubble">
            <p class="tls-15__meta"><b>sam.lowe</b> · <time datetime="2026-07-18T10:31">10:31</time></p>
            <p class="tls-15__txt">Good catch — focus moves into the inline panel and returns on close. Prototype Friday.</p>
            <a class="tls-15__more" href="#thread">Continue thread →</a>
          </div>
        </article>
      </div></div>
    </details>
  </div>
</section>
```
## CSS
```css
.tls-15,
.tls-15 *,
.tls-15 *::before,
.tls-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-15 {
  min-height: 100vh;
  width: 100%;
  --tl-rail: 19px;
  --tl-line: #dce3ea;
  --tl-ink: #1b2733;
  --tl-mut: #697b8c;
  --tl-accent: #0e7490;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f2f5f8;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-15__thread {
  width: min(560px,100%);
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 16px;
  padding: 22px 24px;
  position: relative;
}

.tls-15__post {
  display: flex;
  gap: 12px;
  position: relative;
}

.tls-15__post--child {
  margin-top: 14px;
  padding-left: calc(var(--depth) * 30px);
}

.tls-15__post--child::before {
  content: '';
  position: absolute;
  left: calc(var(--tl-rail) + (var(--depth) - 1) * 30px);
  top: -14px;
  width: 14px;
  height: 32px;
  border-left: 2px solid var(--tl-line);
  border-bottom: 2px solid var(--tl-line);
  border-bottom-left-radius: 12px;
}

.tls-15__av {
  flex: none;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 12px;
  font-weight: 800;
  color: #fff;
  background: var(--a);
  position: relative;
  z-index: 1;
}

.tls-15__bubble {
  flex: 1;
  min-width: 0;
}

.tls-15__meta {
  font-size: 12px;
  color: var(--tl-mut);
}

.tls-15__meta b {
  color: var(--tl-ink);
  font-weight: 700;
}

.tls-15__txt {
  font-size: 14px;
  line-height: 1.55;
  color: #33414f;
  margin-top: 3px;
  text-wrap: pretty;
}

.tls-15__more {
  display: inline-block;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--tl-accent);
  text-decoration: none;
  margin-top: 8px;
}

.tls-15__more:hover {
  text-decoration: underline;
}

.tls-15__replies {
  position: relative;
  margin-top: 4px;
}

.tls-15__replies::before {
  content: '';
  position: absolute;
  left: var(--tl-rail);
  top: -8px;
  height: 22px;
  border-left: 2px solid var(--tl-line);
}

.tls-15__toggle {
  list-style: none;
  display: inline-block;
  cursor: pointer;
  font-size: 12px;
  font-weight: 700;
  color: var(--tl-accent);
  background: #e8f4f7;
  border-radius: 999px;
  padding: 4px 12px;
  margin-left: calc(var(--tl-rail) + 18px);
  user-select: none;
}

.tls-15__toggle::-webkit-details-marker {
  display: none;
}

.tls-15__toggle:hover {
  background: #d8ecf1;
}

.tls-15__replies[open] .tls-15__toggle {
  margin-bottom: 2px;
}

.tls-15__reveal {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .3s ease;
}

.tls-15__replies[open] .tls-15__reveal {
  grid-template-rows: 1fr;
}

.tls-15__inner {
  min-height: 0;
  overflow: hidden;
}

@media (prefers-reduced-motion: reduce) {
  .tls-15__reveal {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — collapse is native details/summary (keyboard + ARIA free); elbows are two borders with a corner radius; expansion animates grid-template-rows 0fr→1fr. */
```
