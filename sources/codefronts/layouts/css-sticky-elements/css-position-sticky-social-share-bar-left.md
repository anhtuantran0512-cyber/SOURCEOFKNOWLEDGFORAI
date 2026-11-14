---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-position-sticky-social-share-bar-left/"
title: "CSS Position Sticky Social Share Bar Left"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The editorial share rail: a slim column of share actions pinned at the article's left margin, riding alongside as you read and retiring exactly where the…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Position Sticky Social Share Bar Left
Source: https://codefronts.com/layouts/css-sticky-elements/css-position-sticky-social-share-bar-left/

The editorial share rail: a slim column of share actions pinned at the article's left margin, riding alongside as you read and retiring exactly where the article ends — because sticky is caged by its container, the rail can never haunt the comments section. On narrow screens the same element becomes a floating glass pill pinned above the viewport's bottom edge. One DOM node, two sticky physics, zero JavaScript.
## HTML
```html
<section class="cst-15" aria-label="Sticky social share bar demo">
  <div class="cst-15__stage" id="cst15-top">
    <header class="cst-15__mast">
      <a class="cst-15__brand" href="#cst15-top">Wireframe <span>— essays on the craft</span></a>
      <a class="cst-15__sub" href="#cst15-subscribe">Subscribe</a>
    </header>
    <div class="cst-15__layout">
      <article class="cst-15__article">
        <p class="cst-15__kicker">Essay · Interface history · 11 min</p>
        <h1>The scrollbar is the most honest UI we ever shipped</h1>
        <p class="cst-15__byline">By Imogen Hale · August 2026</p>
        <p class="cst-15__lede">It tells you where you are, how much is left, and what it costs to get there — no dark patterns, no persuasion, just proportion. Everything since has been negotiation.</p>
        <p>Consider what the humble scrollbar communicates in a glance: position, proportion, affordance. The thumb's size IS the document's length, inverted. No progress ring, no percent-complete counter, no gamified streak has ever matched that density of honest information in nine pixels of width.</p>
        <p>The share rail floating to the left of this text is the scrollbar's polite cousin. It stays while you read — <code>position: sticky</code> against the article's own container — and it leaves when the article does. It cannot follow you into the comments. It physically cannot: sticky elements are caged by their parents, and the cage here is the essay itself.</p>
        <blockquote>An interface element that knows when to leave is rarer than one that knows when to appear.</blockquote>
        <p>We spent the 2010s bolting <code>position: fixed</code> onto everything that marketing wanted permanent. Fixed elements are squatters: they take viewport and never give it back, they overlap footers, they need JavaScript to evict. The sticky rail is a different social contract — it borrows space from a column that was reserved for it, rides exactly as long as it is relevant, and settles back into flow at the article's final paragraph.</p>
        <h3>Try it</h3>
        <p>Scroll to the end of this essay and watch the rail arrive at its natural position — right where the article hands over to the footer. Then, if you're on a narrow screen (or shrink this panel), watch the same DOM node reincarnate as a floating pill pinned above the bottom edge: block flow instead of grid, <code>bottom: 12px</code> instead of <code>top: 96px</code>, demo 11's physics instead of demo 05's.</p>
        <p>One element. Two lives. No script tag. The scrollbar would approve.</p>
        <figure class="cst-15__fig" style="--img:url('https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=1400&auto=format&fit=crop')"><figcaption>The reading column, the margin, and the rail: a page anatomy older than the web.</figcaption></figure>
        <p>Interfaces age the way typography ages: the fashionable parts first. Position sticky — content-aware, self-evicting, JS-free — has the bones of something that lasts. Use it where your UI should behave like a good margin note: present, quiet, gone when the text ends.</p>
      </article>
      <aside class="cst-15__rail" aria-label="Share this essay">
        <span class="cst-15__count">1.4k</span>
        <a href="#cst15-share-x" aria-label="Share on X" data-tip="Share on X"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path d="M3 3h3.6l5 6.7L17.4 3H21l-7.6 8.7L21.4 21h-3.6l-5.4-7.2L6.2 21H2.6l8-9.1L3 3Z" fill="currentColor"/></svg></a>
        <a href="#cst15-share-li" aria-label="Share on LinkedIn" data-tip="LinkedIn"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><circle cx="5.5" cy="5.5" r="2.1" fill="currentColor"/><rect x="3.6" y="9.4" width="3.8" height="11" rx="0.6" fill="currentColor"/><path d="M10.2 9.4H14v1.7c.6-1 1.9-2 3.9-2 3 0 4.5 1.9 4.5 5.4v5.9h-3.8v-5.4c0-1.7-.7-2.6-2-2.6-1.4 0-2.4 1-2.4 2.8v5.2h-4V9.4Z" fill="currentColor"/></svg></a>
        <a href="#cst15-share-mail" aria-label="Share by email" data-tip="Email"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a href="#cst15-share-copy" aria-label="Copy link" data-tip="Copy link"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path d="M10.5 13.5a4.2 4.2 0 0 0 6 .3l2.8-2.8a4.2 4.2 0 1 0-6-6l-1.4 1.4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M13.5 10.5a4.2 4.2 0 0 0-6-.3l-2.8 2.8a4.2 4.2 0 1 0 6 6l1.4-1.4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
        <a href="#cst15-share-save" aria-label="Save for later" data-tip="Save"><svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path d="M18 21l-6-4.6L6 21V5.4C6 4.1 7 3 8.3 3h7.4C17 3 18 4.1 18 5.4V21Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg></a>
      </aside>
    </div>
    <footer class="cst-15__footer" id="cst15-subscribe"><p><strong>Wireframe</strong> — a demo from the CodeFronts sticky-elements collection. The rail parked at the article's edge, right on schedule.</p><a href="#cst15-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-15,
.cst-15 *,
.cst-15 *::before,
.cst-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-15 {
  --bg: oklch(0.977 0.005 75);
  --ink: oklch(0.24 0.02 60);
  --mut: oklch(0.5 0.018 60);
  --line: oklch(0.89 0.012 75);
  --acc: oklch(0.55 0.16 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-15__stage {
  width: 100%;
  container: cst15/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cst-15__mast {
  position: sticky;
  top: 0;
  z-index: 6;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  height: 56px;
  padding: 0 clamp(16px,4cqi,44px);
  background: color-mix(in oklch,var(--bg) 84%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.cst-15__brand {
  font-size: 15.5px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: inherit;
  text-decoration: none;
}

.cst-15__brand span {
  font-weight: 400;
  font-size: 12.5px;
  color: var(--mut);
}

.cst-15__brand:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-15__sub {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 16px;
  border-radius: 99px;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.98 0 0);
  background: var(--ink);
  text-decoration: none;
  transition: background .2s,translate .2s;
}

.cst-15__sub:hover,
.cst-15__sub:focus-visible {
  background: var(--acc);
  translate: 0 -1px;
}

.cst-15__sub:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-15__layout {
  display: grid;
  grid-template-columns: 64px minmax(0,1fr);
  gap: clamp(10px,2cqi,26px);
  max-width: 860px;
  margin-inline: auto;
  padding: clamp(26px,5cqi,56px) clamp(16px,4cqi,44px);
}

.cst-15__article {
  grid-column: 2;
  grid-row: 1;
  max-width: 66ch;
}

.cst-15__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 14px;
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cst-15__article h1 {
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(30px,5.2cqi,52px);
  line-height: 1.08;
  letter-spacing: -.015em;
  font-weight: 700;
  margin-bottom: 14px;
  text-wrap: balance;
}

.cst-15__byline {
  font-size: 12.5px;
  color: var(--mut);
  margin-bottom: 22px;
}

.cst-15__lede {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 19px;
  line-height: 1.55;
  font-style: italic;
  color: oklch(0.36 0.02 60);
  margin-bottom: 20px;
}

.cst-15__article>p:not(.cst-15__kicker):not(.cst-15__byline):not(.cst-15__lede) {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 16px;
  line-height: 1.8;
  color: oklch(0.3 0.018 60);
  margin-bottom: 18px;
}

.cst-15__article h3 {
  font-family: Georgia,serif;
  font-size: 22px;
  font-weight: 700;
  margin: 28px 0 12px;
}

.cst-15__article code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .82em;
  background: oklch(0.92 0.012 75);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-15__article blockquote {
  margin: 24px 0;
  padding: 4px 0 4px 22px;
  border-left: 3px solid var(--acc);
  font-family: Georgia,serif;
  font-size: 20px;
  line-height: 1.5;
  font-style: italic;
  color: var(--ink);
}

.cst-15__fig {
  margin: 24px 0;
  aspect-ratio: 16/9;
  border-radius: 14px;
  background-image: var(--img,none),linear-gradient(150deg,oklch(0.8 0.05 75),oklch(0.55 0.08 50));
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: flex-end;
}

.cst-15__fig figcaption {
  width: 100%;
  padding: 26px 16px 12px;
  font-size: 12px;
  color: oklch(0.97 0.005 75);
  background: linear-gradient(to top,oklch(0.15 0.02 60/.75),transparent);
}

.cst-15__rail {
  grid-column: 1;
  grid-row: 1;
  position: sticky;
  top: 96px;
  align-self: start;
  height: fit-content;
  display: grid;
  gap: 8px;
  justify-items: center;
  padding: 12px 0;
  border-radius: 99px;
  background: oklch(1 0 0/.8);
  border: 1px solid var(--line);
  box-shadow: 0 6px 20px oklch(0.35 0.03 60/.08);
  width: 52px;
}

.cst-15__count {
  font-size: 11px;
  font-weight: 800;
  color: var(--mut);
  padding-bottom: 2px;
}

.cst-15__rail a {
  position: relative;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  color: var(--mut);
  transition: color .2s,background .2s,translate .2s;
}

.cst-15__rail a:hover,
.cst-15__rail a:focus-visible {
  color: var(--acc);
  background: oklch(0.94 0.02 25/.7);
  translate: 0 -1px;
}

.cst-15__rail a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cst-15__rail a::after {
  content: attr(data-tip);
  position: absolute;
  left: calc(100% + 12px);
  top: 50%;
  translate: -4px -50%;
  white-space: nowrap;
  font-size: 11px;
  font-weight: 700;
  color: oklch(0.98 0 0);
  background: var(--ink);
  padding: 5px 9px;
  border-radius: 7px;
  opacity: 0;
  pointer-events: none;
  transition: opacity .18s,translate .18s;
}

.cst-15__rail a:hover::after,
.cst-15__rail a:focus-visible::after {
  opacity: 1;
  translate: 0 -50%;
}

@media (pointer: coarse) {
  .cst-15__rail a::after {
    display: none;
  }
}

.cst-15__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 26px clamp(16px,4cqi,44px) 38px;
  border-top: 1px solid var(--line);
}

.cst-15__footer p {
  font-size: 12.5px;
  color: var(--mut);
  max-width: 60ch;
}

.cst-15__footer a {
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

.cst-15__footer a:hover,
.cst-15__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-15__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst15 (width < 640px) {
  .cst-15__layout {
    display: block;
  }

  .cst-15__rail {
    position: sticky;
    top: auto;
    bottom: 12px;
    z-index: 5;
    display: flex;
    align-items: center;
    gap: 4px;
    width: fit-content;
    margin: 20px auto 0;
    padding: 6px 14px;
    background: color-mix(in oklch,oklch(1 0 0) 82%,transparent);
    -webkit-backdrop-filter: blur(12px);
    backdrop-filter: blur(12px);
  }

  .cst-15__count {
    padding: 0 6px 0 0;
  }

  .cst-15__rail a::after {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-15 * {
    transition-duration: .01ms !important;
  }
}
```
