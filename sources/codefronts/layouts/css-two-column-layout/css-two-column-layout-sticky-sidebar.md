---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-sticky-sidebar/"
title: "CSS Two Column Layout Sticky Sidebar"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "A long-form article with a sticky table-of-contents sidebar: the content column scrolls while the sidebar pins itself with position: sticky; top: 24px — plus…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Layout Sticky Sidebar
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-sticky-sidebar/

A long-form article with a sticky table-of-contents sidebar: the content column scrolls while the sidebar pins itself with position: sticky; top: 24px — plus a scroll-driven reading-progress bar (animation-timeline: scroll()) that needs zero JavaScript. The pattern behind every docs site and blog you admire.
## HTML
```html
<section class="tcl-07" aria-label="Sticky sidebar two column layout demo">
  <div class="tcl-07__page">
    <article class="tcl-07__article">
      <span class="tcl-07__kicker">Guide · 12 min read</span>
      <h1 id="tcl-07-intro">Designing calmer onboarding flows</h1>
      <p>Scroll this column — the table of contents on the right stays pinned with <code>position: sticky</code>, and the progress bar fills using a scroll-driven animation. Long-form pages earn their sidebar when readers can always see where they are.</p>
      <h2 id="tcl-07-friction">1. Remove friction before adding delight</h2>
      <p>Every field you delete from a signup form outperforms any animation you could add to it. Audit each step and ask what the product genuinely cannot work without — everything else moves to later, contextual moments.</p>
      <p>Teams that defer optional profile questions until after the first success moment see measurably higher completion. The order of asks matters more than their number.</p>
      <h2 id="tcl-07-defaults">2. Defaults are decisions you make for the user</h2>
      <p>A good default is invisible; a bad one is a support ticket. Choose defaults that match the 80% case, and make changing them feel like adjusting, not configuring.</p>
      <p>When users must choose, show the consequence of each option inline — never send them to documentation mid-flow.</p>
      <h2 id="tcl-07-progress">3. Show progress honestly</h2>
      <p>Progress indicators only calm people when they’re truthful. Four real steps beat a vague spinner; a bar that leaps from 10% to 90% teaches users to distrust it.</p>
      <p>The same principle applies to this page: the reading bar in the sidebar maps linearly to scroll position — no easing tricks, no fake momentum.</p>
      <h2 id="tcl-07-end">4. End on capability, not confetti</h2>
      <p>The last onboarding screen should hand the user a verb: import, invite, publish. Celebration is fine, but capability is what brings people back tomorrow.</p>
    </article>
    <aside class="tcl-07__rail" aria-label="Table of contents">
      <div class="tcl-07__sticky">
        <span class="tcl-07__pin">position: sticky · top: 24px</span>
        <div class="tcl-07__progress" aria-hidden="true"><i></i></div>
        <nav class="tcl-07__toc">
          <b>On this page</b>
          <a href="#tcl-07-friction">Remove friction first</a>
          <a href="#tcl-07-defaults">Defaults are decisions</a>
          <a href="#tcl-07-progress">Show progress honestly</a>
          <a href="#tcl-07-end">End on capability</a>
        </nav>
      </div>
    </aside>
  </div>
</section>
```
## CSS
```css
.tcl-07,
.tcl-07 *,
.tcl-07 *::before,
.tcl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-07 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.55 0.2 300);
  --ink: oklch(0.24 0.02 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  background: oklch(0.975 0.006 300);
  padding: clamp(20px,3.5vw,48px);
}

.tcl-07__page {
  display: grid;
  grid-template-columns: minmax(0,1fr) 260px;
  gap: clamp(24px,4vw,56px);
  max-width: 1000px;
  margin-inline: auto;
}

.tcl-07__article {
  display: grid;
  gap: 16px;
  min-width: 0;
}

.tcl-07__kicker {
  font: 700 11px/1 inherit;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.tcl-07__article h1 {
  font-size: clamp(26px,3.6vw,38px);
  line-height: 1.12;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.tcl-07__article h2 {
  font-size: clamp(18px,2.2vw,22px);
  letter-spacing: -.015em;
  margin-top: 14px;
  scroll-margin-top: 24px;
}

.tcl-07__article p {
  font-size: 15px;
  line-height: 1.75;
  color: color-mix(in oklab,var(--ink) 80%,transparent);
  text-wrap: pretty;
}

.tcl-07__article code {
  font: 600 13px ui-monospace,monospace;
  background: color-mix(in oklab,var(--accent) 10%,transparent);
  border-radius: 5px;
  padding: 2px 6px;
}

.tcl-07__rail {
  min-width: 0;
}

.tcl-07__sticky {
  position: sticky;
  top: 24px;
  display: grid;
  gap: 14px;
}

.tcl-07__pin {
  justify-self: start;
  font: 600 10.5px/1 ui-monospace,monospace;
  color: var(--accent);
  border: 1px dashed color-mix(in oklab,var(--accent) 50%,transparent);
  border-radius: 99px;
  padding: 5px 9px;
}

.tcl-07__progress {
  height: 5px;
  border-radius: 99px;
  background: color-mix(in oklab,var(--accent) 14%,transparent);
  overflow: hidden;
}

.tcl-07__progress i {
  display: block;
  height: 100%;
  border-radius: inherit;
  background: var(--accent);
  transform-origin: left;
  transform: scaleX(1);
}

@supports (animation-timeline: scroll()) {
  .tcl-07__progress i {
    transform: scaleX(0);
    animation: tcl-07-read linear both;
    animation-timeline: scroll();
  }
}

@keyframes tcl-07-read {
  to {
    transform: scaleX(1);
  }
}

.tcl-07__toc {
  display: grid;
  gap: 2px;
  background: #fff;
  border: 1px solid oklch(0.9 0.015 300);
  border-radius: 14px;
  padding: 14px;
}

.tcl-07__toc b {
  font-size: 12px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
  padding: 4px 10px 8px;
}

.tcl-07__toc a {
  font-size: 13.5px;
  color: var(--ink);
  text-decoration: none;
  padding: 8px 10px;
  border-radius: 8px;
  border-left: 2px solid transparent;
  transition: background .15s,border-color .15s;
}

.tcl-07__toc a:hover {
  background: color-mix(in oklab,var(--accent) 8%,transparent);
  border-left-color: var(--accent);
}

.tcl-07__toc a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

@media (max-width: 720px) {
  .tcl-07__page {
    grid-template-columns: 1fr;
  }

  .tcl-07__rail {
    order: -1;
  }

  .tcl-07__sticky {
    position: static;
  }
}
```

## JavaScript
```js
/* No JavaScript — position:sticky pins the rail (its grid parent stretches to the article's height), and animation-timeline:scroll() drives the reading-progress bar natively. */
```
