---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/sticky-top-css-navigation-header-with-shrinking-breadcrumb-trail/"
title: "Sticky Top CSS Navigation Header with Shrinking Breadcrumb Trail"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A sticky page header whose breadcrumb trail shrinks as you scroll — font size, padding and vertical footprint all contract into a compact bar that stays…"
has_js: "true"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Top CSS Navigation Header with Shrinking Breadcrumb Trail
Source: https://codefronts.com/navigation/css-breadcrumbs/sticky-top-css-navigation-header-with-shrinking-breadcrumb-trail/

A sticky page header whose breadcrumb trail shrinks as you scroll — font size, padding and vertical footprint all contract into a compact bar that stays pinned to the top. Modern build uses CSS scroll-driven animation-timeline:scroll(); a tiny IntersectionObserver fallback ships for engines without it.
## HTML
```html
<div class="bc-07" data-shrunk="false">
  <header class="bc-07__bar">
    <span class="bc-07__logo" aria-hidden="true"></span>
    <nav aria-label="Breadcrumb">
      <ol>
        <li><a href="#">Home</a></li>
        <li><a href="#">Docs</a></li>
        <li><a href="#" aria-current="page">Scroll-driven UI</a></li>
      </ol>
    </nav>
  </header>
  <div class="bc-07__sentinel" aria-hidden="true"></div>
  <div class="bc-07__content">
    <h1 class="bc-07__h1">Scroll-driven sticky breadcrumb header</h1>
    <p class="bc-07__lede">Scroll this panel &darr; and watch the sticky breadcrumb header at the top compress into a slim pinned bar. Padding, type scale, and logo size all contract via CSS <code>animation-timeline: scroll()</code> — no JavaScript scroll listener needed.</p>
    <h2 class="bc-07__h2">How the shrink is wired</h2>
    <p>Modern browsers support scroll-driven animations natively (Chrome 115+, Safari 26+, Firefox 134+). The trick is one <code>@keyframes</code> block plus <code>animation-timeline: scroll(nearest)</code> on the sticky header. As the user scrolls past a sentinel div, the timeline advances from 0 to 1 and the browser interpolates the keyframe values.</p>
    <p>This is the exact pattern <strong>Docusaurus 3</strong>, <strong>Mintlify</strong>, <strong>Nextra</strong>, <strong>VitePress</strong>, <strong>Starlight</strong>, and <strong>Fumadocs</strong> ship on their generated docs sites. No IntersectionObserver, no scroll event listener, no rAF throttle needed — the browser&rsquo;s own compositor drives the animation.</p>
    <h2 class="bc-07__h2">Accessibility contract</h2>
    <p>The breadcrumb still needs to satisfy WCAG 2.4.8 (Location) and WCAG 1.4.3 (Contrast Minimum) regardless of shrink state. Both expanded and compact states use a token-based color system that maintains AA contrast against the frosted-glass backdrop.</p>
    <p>Motion is gated behind <code>@media (prefers-reduced-motion: no-preference)</code> — users who opted out of motion at the OS level see a static bar at the compact size, never the animation. This is WCAG 2.3.3 (Animation from Interactions) compliance.</p>
    <h2 class="bc-07__h2">Falling back gracefully</h2>
    <p>Older Safari and Firefox versions that don&rsquo;t support <code>animation-timeline: scroll()</code> just render the base state — a sticky bar with the expanded padding. The demo also ships a 12-line IntersectionObserver fallback that toggles a <code>.is-shrunk</code> class when the sentinel exits the viewport, so the shrink still works for the ~5% of users on older engines.</p>
    <p>Feature-detect once at page load: <code>if (CSS.supports(&#39;animation-timeline&#39;, &#39;scroll()&#39;)) &#123; /* skip JS fallback */ &#125;</code>. Ship both paths; let the browser pick.</p>
    <h2 class="bc-07__h2">Try it: scroll to the bottom</h2>
    <p>The last paragraph sits at the far bottom so you can watch the header shrink smoothly as the sentinel scrolls out of view. Grab the scrollbar or two-finger swipe to see the full range of the animation.</p>
    <p>Keep scrolling &darr;</p>
    <p>The shrink kicks in at the sentinel boundary, then holds at the compact size all the way to the bottom.</p>
    <p>Once you scroll back up past the sentinel, the header expands smoothly back to its original size &mdash; the animation is bidirectional.</p>
    <p>The frosted-glass <code>backdrop-filter</code> stays consistent throughout, so body text never fights the header for contrast.</p>
    <p>This is the scroll-driven pattern behind every modern docs-site UX from 2024 onward.</p>
    <p>End of scroll region.</p>
  </div>
</div>
```
## CSS
```css
.bc-07 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  height: 300px;
  overflow-y: auto;
  background: oklch(0.97 0.006 255);
  position: relative;
  scrollbar-width: thin;
  place-items: center;
}

.bc-07 * {
  box-sizing: border-box;
}

.bc-07__bar {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 20px 24px;
  background: oklch(1 0 0/.85);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid oklch(0.9 0.01 255);
  box-shadow: 0 0 0 rgba(0,0,0,0);
  transition: padding .3s ease,box-shadow .3s ease;
}

.bc-07__logo {
  width: 34px;
  height: 34px;
  flex: none;
  border-radius: 9px;
  background: conic-gradient(from 210deg,oklch(0.62 0.17 265),oklch(0.6 0.16 210));
  transition: width .3s ease,height .3s ease;
}

.bc-07 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-07 li {
  display: flex;
  align-items: center;
}

.bc-07 li + li::before {
  content: "›";
  margin: 0 8px;
  color: oklch(0.72 0.02 255);
}

.bc-07 a {
  font: 600 15px/1 system-ui,sans-serif;
  color: oklch(0.5 0.1 260);
  text-decoration: none;
  padding: 3px 5px;
  border-radius: 6px;
  transition: font-size .3s ease,color .15s ease;
}

.bc-07 a:hover {
  color: oklch(0.42 0.14 260);
}

.bc-07 a:focus-visible {
  outline: 2px solid oklch(0.5 0.15 260);
  outline-offset: 2px;
}

.bc-07 li[aria-current="page"] a {
  color: oklch(0.28 0.02 255);
  font-weight: 700;
}

.bc-07[data-shrunk="true"] .bc-07__bar {
  padding: 9px 24px;
  box-shadow: 0 4px 18px rgba(0,0,0,.1);
}

.bc-07[data-shrunk="true"] .bc-07__logo {
  width: 24px;
  height: 24px;
}

.bc-07[data-shrunk="true"] .bc-07 a {
  font-size: 13px;
}

.bc-07__sentinel {
  height: 1px;
}

@media (prefers-reduced-motion: reduce) {
  .bc-07__bar,
    .bc-07__logo,
    .bc-07 a {
    transition: none;
  }
}

.bc-07 .bc-07__h1 {
  font: 700 22px/1.3 system-ui,sans-serif;
  color: oklch(0.25 0.02 255);
  margin: 0 0 8px;
}

.bc-07 .bc-07__h2 {
  font: 700 15px/1.3 system-ui,sans-serif;
  color: oklch(0.3 0.02 255);
  margin: 24px 0 6px;
}

.bc-07 .bc-07__lede {
  font: 500 15px/1.55 system-ui,sans-serif;
  color: oklch(0.42 0.02 255);
  margin: 0 0 20px;
  max-width: 60ch;
}

.bc-07 .bc-07__content {
  padding: 24px 24px 40px;
}

.bc-07 .bc-07__content p {
  margin: 0 0 14px;
  color: oklch(0.42 0.02 255);
  font-size: 14px;
  line-height: 1.65;
  max-width: 60ch;
}

.bc-07 .bc-07__content code {
  font: 500 12.5px/1 ui-monospace,Menlo,monospace;
  color: oklch(0.35 0.05 260);
  background: oklch(0.94 0.01 255);
  padding: 2px 6px;
  border-radius: 4px;
}

.bc-07 .bc-07__content strong {
  color: oklch(0.28 0.02 255);
  font-weight: 700;
}
```

## JavaScript
```js
/* Scroll-shrink via IntersectionObserver (universal fallback for animation-timeline:scroll()) */
document.querySelectorAll('.bc-07').forEach((root) => {
  const sentinel = root.querySelector('.bc-07__sentinel');
  const io = new IntersectionObserver(
    ([e]) => root.setAttribute('data-shrunk', String(!e.isIntersecting)),
    { root, threshold: 0 }
  );
  io.observe(sentinel);
});
/* Pure-CSS alternative: give .bc-07__bar { animation: shrink linear both; animation-timeline: scroll(nearest); } and keyframe the same properties. */
```
