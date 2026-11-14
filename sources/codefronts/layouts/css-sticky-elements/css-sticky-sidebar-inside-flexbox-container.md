---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-sidebar-inside-flexbox-container/"
title: "CSS Sticky Sidebar Inside Flexbox Container"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The most-asked sticky question on Stack Overflow, answered in one property: a sidebar inside a flex row won't stick because flexbox stretches it to the…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Sidebar Inside Flexbox Container
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-sidebar-inside-flexbox-container/

The most-asked sticky question on Stack Overflow, answered in one property: a sidebar inside a flex row won't stick because flexbox stretches it to the container's full height — and an element with no room to travel has nothing to stick against. align-self: flex-start restores its natural height and the sidebar immediately pins, rides alongside the article, then parks at the container's bottom edge. The demo continues past the article so you can watch it park.
## HTML
```html
<section class="cst-05" aria-label="Sticky sidebar inside flexbox demo">
  <div class="cst-05__stage" id="cst05-top">
    <header class="cst-05__mast">
      <a class="cst-05__brand" href="#cst05-top">The Grid Paper</a>
      <p>A journal about building calmer interfaces</p>
    </header>
    <div class="cst-05__layout">
      <article class="cst-05__article">
        <p class="cst-05__kicker">CSS Architecture · 9 min read</p>
        <h1>The sidebar that finally stayed put</h1>
        <p class="cst-05__lede">Every layout system gives you a way to pin a rail beside long content. Flexbox gives you that way, then quietly sabotages it with a default you'd never suspect: <code>align-items: stretch</code>.</p>
        <p>Here is the setup you have written a hundred times: a flex row, an article that grows, an aside fixed at 300px. You add <code>position: sticky; top: 24px</code> to the aside, reload, and… nothing. It scrolls away with the page like an ordinary block. The property is right there in DevTools — computed, valid, ignored.</p>
        <p>Nothing is ignored. Sticky is working perfectly on an element that has been stretched to the exact height of its container. An element that already spans its parent's full height has zero pixels of travel: it is simultaneously at the top of its range and at the bottom. The browser pins it — across a range of nothing.</p>
        <h3>One property restores the physics</h3>
        <p>Tell the sidebar to keep its natural height and the whole mechanism springs to life. As you scroll this very page, the rail on the right pinned at 24px the moment its top edge got there — and if you keep going past the end of the article, it parks at the flex container's bottom edge and lets the footer through.</p>
        <blockquote>A sticky element slides in the gap between its own height and its parent's. No gap, no slide. That single sentence resolves 90% of “sticky not working” tickets.</blockquote>
        <p>The remaining 10% is ancestry: some wrapper between the rail and the scroller declaring <code>overflow: hidden</code>, usually added months earlier to clip a decorative blob. Demo 16 in this collection is the drill for finding it in under a minute.</p>
        <h3>Cap the rail, always</h3>
        <p>A rail taller than the viewport can technically pin, but you will only ever see its middle — the top links and the bottom CTA both live off-screen. The demo caps the aside at <code>max-height: calc(100svh - 48px)</code> with <code>overflow: auto</code>, so a long rail scrolls internally while staying pinned. Watch for double scrollbars though: if your rail is a six-link nav, it should never need to scroll. The cap is a seatbelt, not a feature.</p>
        <p>That's the whole pattern. No JavaScript, no resize observers, no cloned spacer divs — two declarations on the child, one seatbelt, and a layout that behaves the way every reader expects.</p>
      </article>
      <aside class="cst-05__rail">
        <div class="cst-05__author">
          <i aria-hidden="true">RK</i>
          <div><strong>Rosa Kim</strong><span>CSS columnist</span></div>
        </div>
        <nav class="cst-05__series" aria-label="In this series">
          <h3>In this series</h3>
          <a href="#cst05-p1" aria-current="true">The sidebar that stayed put</a>
          <a href="#cst05-p2">Grid areas are a love language</a>
          <a href="#cst05-p3">Container queries in anger</a>
          <a href="#cst05-p4">:has() is a state machine</a>
        </nav>
        <form class="cst-05__news" onsubmit="return false">
          <h3>The Grid Paper, weekly</h3>
          <p>One layout trick every Thursday. No tracking pixels.</p>
          <label class="cst-05__vh" for="cst05-email">Email address</label>
          <input id="cst05-email" type="email" placeholder="[email protected]" autocomplete="off">
          <button type="submit">Subscribe</button>
        </form>
        <p class="cst-05__note">← this rail is <code>position: sticky</code> + <code>align-self: flex-start</code></p>
      </aside>
    </div>
    <section class="cst-05__more">
      <h2>More from the journal <span>· the sidebar parked above, exactly at its container's edge</span></h2>
      <div class="cst-05__grid">
        <a href="#cst05-m1"><h3>Grid areas are a love language</h3><p>Name your regions and your future self names you kindly.</p></a>
        <a href="#cst05-m2"><h3>Scroll-snap without the rage</h3><p>Proximity vs mandatory, and when each one bites.</p></a>
        <a href="#cst05-m3"><h3>The 44px rule is not negotiable</h3><p>Hit targets, thumbs, and the physics of fingertips.</p></a>
      </div>
    </section>
    <footer class="cst-05__footer"><p><strong>The Grid Paper</strong> — a demo from the CodeFronts sticky-elements collection.</p><a href="#cst05-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-05,
.cst-05 *,
.cst-05 *::before,
.cst-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-05 {
  --bg: oklch(0.98 0.005 90);
  --ink: oklch(0.24 0.02 75);
  --mut: oklch(0.51 0.018 75);
  --line: oklch(0.89 0.012 85);
  --acc: oklch(0.55 0.14 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-05__stage {
  width: 100%;
  container: cst05/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cst-05__mast {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 8px 18px;
  padding: 22px clamp(18px,4cqi,44px) 20px;
  border-bottom: 1px solid var(--line);
}

.cst-05__brand {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.cst-05__brand:hover,
.cst-05__brand:focus-visible {
  color: var(--acc);
}

.cst-05__brand:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.cst-05__mast p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-05__layout {
  display: flex;
  gap: clamp(24px,4cqi,52px);
  align-items: flex-start;
  padding: clamp(26px,5cqi,54px) clamp(18px,4cqi,44px);
}

.cst-05__article {
  flex: 1;
  min-width: 0;
  max-width: 70ch;
}

.cst-05__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 12px;
}

.cst-05__article h1 {
  font-size: clamp(30px,5cqi,50px);
  line-height: 1.04;
  letter-spacing: -.03em;
  font-weight: 800;
  margin-bottom: 18px;
  text-wrap: balance;
}

.cst-05__lede {
  font-size: 17px;
  line-height: 1.6;
  color: var(--ink);
  margin-bottom: 18px;
}

.cst-05__article>p:not(.cst-05__kicker):not(.cst-05__lede) {
  font-size: 15px;
  line-height: 1.75;
  color: oklch(0.38 0.02 75);
  margin-bottom: 16px;
}

.cst-05__article h3 {
  font-size: 20px;
  letter-spacing: -.015em;
  font-weight: 750;
  margin: 26px 0 12px;
}

.cst-05__article code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .86em;
  background: oklch(0.92 0.015 90);
  padding: 2px 6px;
  border-radius: 5px;
}

.cst-05__article blockquote {
  margin: 22px 0;
  padding: 18px 22px;
  border-radius: 14px;
  background: oklch(0.94 0.02 155/.5);
  font-size: 15.5px;
  line-height: 1.6;
  font-weight: 600;
  letter-spacing: -.005em;
}

.cst-05__rail {
  flex: 0 0 288px;
  position: sticky;
  top: 24px;
  align-self: flex-start;
  max-height: calc(100vh - 48px);
  max-height: calc(100svh - 48px);
  overflow: auto;
  display: grid;
  gap: 14px;
  scrollbar-width: thin;
}

.cst-05__author {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  border-radius: 16px;
  background: oklch(1 0 0/.7);
  border: 1px solid var(--line);
}

.cst-05__author i {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-style: normal;
  font-size: 14px;
  font-weight: 800;
  color: oklch(0.99 0 0);
  background: linear-gradient(140deg,var(--acc),oklch(0.45 0.12 200));
}

.cst-05__author strong {
  display: block;
  font-size: 14px;
}

.cst-05__author span {
  font-size: 12px;
  color: var(--mut);
}

.cst-05__series,
.cst-05__news {
  padding: 16px;
  border-radius: 16px;
  background: oklch(1 0 0/.7);
  border: 1px solid var(--line);
}

.cst-05__series h3,
.cst-05__news h3 {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 10px;
}

.cst-05__series {
  display: grid;
}

.cst-05__series a {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 10px;
  margin: 0 -6px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  border-left: 2px solid transparent;
  transition: color .2s,background .2s;
}

.cst-05__series a:hover,
.cst-05__series a:focus-visible {
  color: var(--ink);
  background: oklch(0.94 0.015 90);
}

.cst-05__series a[aria-current] {
  color: var(--ink);
  border-left-color: var(--acc);
  background: oklch(0.94 0.02 155/.55);
}

.cst-05__series a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-05__news p {
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--mut);
  margin-bottom: 12px;
}

.cst-05__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.cst-05__news input {
  width: 100%;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 10px;
  border: 1.5px solid var(--line);
  background: oklch(1 0 0);
  font: inherit;
  font-size: 13.5px;
  color: var(--ink);
  transition: border-color .2s;
}

.cst-05__news input::placeholder {
  color: oklch(0.65 0.015 75);
}

.cst-05__news input:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 3px oklch(0.55 0.14 155/.18);
}

.cst-05__news button {
  width: 100%;
  min-height: 44px;
  margin-top: 8px;
  border: none;
  border-radius: 10px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  color: oklch(0.99 0 0);
  background: var(--ink);
  cursor: pointer;
  transition: background .2s,translate .2s;
}

.cst-05__news button:hover,
.cst-05__news button:focus-visible {
  background: var(--acc);
  translate: 0 -1px;
}

.cst-05__news button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-05__note {
  font-size: 11.5px;
  line-height: 1.5;
  color: var(--mut);
  padding: 0 4px;
}

.cst-05__note code {
  font-size: .9em;
  background: oklch(0.92 0.015 90);
  padding: 1px 5px;
  border-radius: 4px;
}

.cst-05__more {
  padding: clamp(34px,6cqi,60px) clamp(18px,4cqi,44px);
  background: oklch(0.945 0.012 90);
}

.cst-05__more h2 {
  font-size: clamp(20px,3.2cqi,28px);
  letter-spacing: -.02em;
  font-weight: 800;
  margin-bottom: 18px;
}

.cst-05__more h2 span {
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: 0;
  color: var(--mut);
}

.cst-05__grid {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit,minmax(min(220px,100%),1fr));
}

.cst-05__grid a {
  display: grid;
  gap: 6px;
  align-content: start;
  padding: 20px;
  border-radius: 16px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
  transition: translate .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s;
}

.cst-05__grid a:hover,
.cst-05__grid a:focus-visible {
  translate: 0 -3px;
  box-shadow: 0 12px 28px oklch(0.35 0.03 90/.1);
}

.cst-05__grid a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-05__grid h3 {
  font-size: 15.5px;
  letter-spacing: -.01em;
}

.cst-05__grid p {
  font-size: 13px;
  line-height: 1.55;
  color: var(--mut);
}

.cst-05__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 28px clamp(18px,4cqi,44px) 38px;
  border-top: 1px solid var(--line);
}

.cst-05__footer p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-05__footer a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  border: 1.5px solid var(--line);
  transition: border-color .2s;
}

.cst-05__footer a:hover,
.cst-05__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-05__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst05 (width < 680px) {
  .cst-05__layout {
    flex-direction: column;
  }

  .cst-05__rail {
    position: static;
    max-height: none;
    flex-basis: auto;
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-05 * {
    transition-duration: .01ms !important;
  }
}
```
