---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/css-masonry-blog-post-cards-layout/"
title: "CSS Masonry Blog Post Cards Layout"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "A magazine archive where the content decides the heights: cover-image cards, text-only pull quotes and a full-width editor's pick banner all pack into one…"
has_js: "false"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Blog Post Cards Layout
Source: https://codefronts.com/layouts/css-masonry-layouts/css-masonry-blog-post-cards-layout/

A magazine archive where the content decides the heights: cover-image cards, text-only pull quotes and a full-width editor's pick banner all pack into one multicol wall. :has() styles cards differently when they contain a figure, column-span: all lets the featured banner interrupt the flow edge-to-edge (the trick almost nobody knows multicol can do), and a staggered fade-up entrance costs eleven lines of keyframes.
## HTML
```html
<section class="msn-04" aria-label="CSS masonry blog post cards demo">
  <div class="msn-04__stage" tabindex="0">
    <header class="msn-04__head">
      <div><h2>The Grid Journal</h2><p>Essays on building for the web · 48 posts</p></div>
      <nav class="msn-04__nav" aria-label="Sections"><a href="#latest" aria-current="true">Latest</a><a href="#css">CSS</a><a href="#perf">Performance</a><a href="#culture">Culture</a></nav>
    </header>
    <div class="msn-04__wall">
      <article class="msn-04__card" style="--i:0"><figure style="--img:url('https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.06 70);--b:oklch(0.55 0.09 50)"></figure><div class="msn-04__body"><span class="msn-04__cat">CSS</span><h3><a href="#post-1">The year masonry went native</a></h3><p>Grid learned to pack. We spent a decade shipping JavaScript to do what one property now describes — here is the migration path.</p><a class="msn-04__author" href="#by-anya" data-min="7"><i style="--a:oklch(0.75 0.1 300);--b:oklch(0.5 0.13 320)"></i><span><strong>Anya Roth</strong><em>Jun 18, 2026</em></span></a></div></article>
      <article class="msn-04__card" style="--i:1"><div class="msn-04__body"><span class="msn-04__cat">Opinion</span><h3><a href="#post-2">Your layout shift budget is zero</a></h3><p>CLS is not a metric, it is a promise you make to readers: nothing you have started reading will move. Reserve space or don't ship.</p><a class="msn-04__author" href="#by-marc" data-min="4"><i style="--a:oklch(0.8 0.09 150);--b:oklch(0.55 0.11 170)"></i><span><strong>Marc Diaz</strong><em>Jun 14, 2026</em></span></a></div></article>
      <article class="msn-04__card" style="--i:2"><figure style="--img:url('https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=800&auto=format&fit=crop');--a:oklch(0.6 0.08 280);--b:oklch(0.38 0.09 300)"></figure><div class="msn-04__body"><span class="msn-04__cat">Performance</span><h3><a href="#post-3">INP: the case for zero-JS layout</a></h3><p>Every resize listener you delete is interaction budget returned to the user.</p><a class="msn-04__author" href="#by-priya" data-min="6"><i style="--a:oklch(0.78 0.1 40);--b:oklch(0.55 0.14 20)"></i><span><strong>Priya Shah</strong><em>Jun 11, 2026</em></span></a></div></article>
      <article class="msn-04__pick" style="--i:3"><div><span class="msn-04__cat msn-04__cat--pick">Editor's pick</span><h3><a href="#post-4">Stop measuring, start declaring</a></h3><p>The whole history of front-end layout is a slow migration from imperative measurement to declarative intent. Masonry is simply the latest room in that house.</p></div><span class="msn-04__pickArrow" aria-hidden="true">→</span></article>
      <article class="msn-04__card" style="--i:4"><div class="msn-04__body"><span class="msn-04__cat">Quote</span><blockquote>“Multi-column is the only layout engine on the web that has never once asked me how tall my content is.”</blockquote><a class="msn-04__author" href="#by-jules" data-min="2"><i style="--a:oklch(0.75 0.08 220);--b:oklch(0.5 0.1 240)"></i><span><strong>Jules Kim</strong><em>Jun 8, 2026</em></span></a></div></article>
      <article class="msn-04__card" style="--i:5"><figure style="--img:url('https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=800&auto=format&fit=crop');--a:oklch(0.82 0.05 250);--b:oklch(0.6 0.07 270)"></figure><div class="msn-04__body"><span class="msn-04__cat">Tooling</span><h3><a href="#post-5">A build step you can delete this week</a></h3><p>We removed the masonry package, the resize observer, and 41KB of hydration. The layout got faster and the diff got red.</p><a class="msn-04__author" href="#by-tom" data-min="5"><i style="--a:oklch(0.8 0.07 100);--b:oklch(0.58 0.1 80)"></i><span><strong>Tom Hale</strong><em>Jun 3, 2026</em></span></a></div></article>
      <article class="msn-04__card" style="--i:6"><div class="msn-04__body"><span class="msn-04__cat">CSS</span><h3><a href="#post-6">:has() is a card component API</a></h3><p>Presence of a figure, a badge, a footnote — the markup itself becomes the variant prop. No modifier classes, no CMS flags, no drift between content and style. The selector reads the truth.</p><a class="msn-04__author" href="#by-sofia" data-min="8"><i style="--a:oklch(0.72 0.11 330);--b:oklch(0.48 0.13 350)"></i><span><strong>Sofia Lund</strong><em>May 29, 2026</em></span></a></div></article>
      <article class="msn-04__card" style="--i:7"><figure style="--img:url('https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?q=80&w=800&auto=format&fit=crop');--a:oklch(0.78 0.06 60);--b:oklch(0.55 0.08 40)"></figure><div class="msn-04__body"><span class="msn-04__cat">Culture</span><h3><a href="#post-7">Writing docs your grid deserves</a></h3><p>Layout code outlives frameworks. Document the intent, not the syntax.</p><a class="msn-04__author" href="#by-ken" data-min="3"><i style="--a:oklch(0.7 0.09 190);--b:oklch(0.48 0.1 210)"></i><span><strong>Ken Watanabe</strong><em>May 24, 2026</em></span></a></div></article>
    </div>
  </div>
</section>
```
## CSS
```css
.msn-04,
.msn-04 *,
.msn-04 *::before,
.msn-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-04 {
  --bg: oklch(0.975 0.006 90);
  --card: oklch(0.995 0.002 90);
  --tint: oklch(0.95 0.02 90);
  --ink: oklch(0.24 0.02 70);
  --mut: oklch(0.53 0.02 70);
  --line: oklch(0.89 0.01 90);
  --acc: oklch(0.55 0.15 45);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-04__stage {
  width: 100%;
  container: msn04/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-04__head {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px 18px;
  padding: 16px clamp(16px,3cqi,30px);
  background: color-mix(in oklch,var(--bg) 84%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.msn-04__head h2 {
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(19px,2.8cqi,26px);
  letter-spacing: -.01em;
}

.msn-04__head p {
  font-size: 12px;
  color: var(--mut);
  margin-top: 2px;
}

.msn-04__nav {
  display: flex;
  gap: 2px;
}

.msn-04__nav a {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  color: var(--mut);
  transition: color .2s,background .2s;
}

.msn-04__nav a:hover,
.msn-04__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.93 0.012 90);
}

.msn-04__nav a[aria-current] {
  color: var(--ink);
  background: oklch(0.91 0.02 90);
}

.msn-04__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.msn-04__wall {
  columns: 290px;
  column-gap: 16px;
  padding: clamp(16px,3cqi,30px);
}

.msn-04__card,
.msn-04__pick {
  break-inside: avoid;
  margin-bottom: 16px;
  border-radius: 16px;
  border: 1px solid var(--line);
  background: var(--card);
  overflow: clip;
  position: relative;
  transition: translate .25s,box-shadow .25s;
}

.msn-04__card:hover,
.msn-04__card:focus-within {
  translate: 0 -3px;
  box-shadow: 0 12px 28px -14px oklch(0.4 0.04 70/.35);
}

.msn-04__card figure {
  aspect-ratio: 16/9;
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
}

.msn-04__body {
  padding: 18px 18px 16px;
  display: grid;
  gap: 10px;
  justify-items: start;
}

.msn-04__card:not(:has(figure)) {
  background: var(--tint);
}

.msn-04__card:not(:has(figure)) .msn-04__body {
  padding: 22px 20px 18px;
}

.msn-04__cat {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--acc);
}

.msn-04__card h3 {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 19px;
  line-height: 1.25;
  letter-spacing: -.01em;
  text-wrap: pretty;
}

.msn-04__card h3 a {
  color: inherit;
  text-decoration: none;
}

.msn-04__card h3 a::after {
  content: "";
  position: absolute;
  inset: 0;
}

.msn-04__card h3 a:focus-visible {
  outline: none;
}

.msn-04__card:has(h3 a:focus-visible) {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.msn-04__card p,
.msn-04__card blockquote {
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--mut);
  text-wrap: pretty;
}

.msn-04__card blockquote {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 17px;
  line-height: 1.5;
  color: var(--ink);
}

.msn-04__author {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  text-decoration: none;
  color: inherit;
  border-radius: 10px;
}

.msn-04__author i {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: linear-gradient(140deg,var(--a),var(--b));
  flex: none;
}

.msn-04__author strong {
  display: block;
  font-size: 12.5px;
}

.msn-04__author em {
  display: block;
  font-style: normal;
  font-size: 11.5px;
  color: var(--mut);
}

.msn-04__author::after {
  content: attr(data-min) " min read";
  margin-left: auto;
  font-size: 11px;
  font-weight: 600;
  color: var(--mut);
  border: 1px solid var(--line);
  border-radius: 99px;
  padding: 4px 9px;
}

.msn-04__author:hover strong,
.msn-04__author:focus-visible strong {
  color: var(--acc);
}

.msn-04__author:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.msn-04__pick {
  column-span: all;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  padding: 24px clamp(18px,3cqi,30px);
  background: var(--ink);
  color: oklch(0.97 0.005 90);
  border-color: var(--ink);
}

.msn-04__pick h3 {
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(19px,2.6cqi,25px);
  letter-spacing: -.01em;
  margin: 8px 0 6px;
}

.msn-04__pick h3 a {
  color: inherit;
  text-decoration: none;
}

.msn-04__pick h3 a::after {
  content: "";
  position: absolute;
  inset: 0;
}

.msn-04__pick h3 a:focus-visible {
  outline: none;
}

.msn-04__pick:has(a:focus-visible) {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.msn-04__pick p {
  font-size: 13.5px;
  line-height: 1.6;
  color: oklch(0.8 0.015 90);
  max-width: 56ch;
  text-wrap: pretty;
}

.msn-04__cat--pick {
  color: oklch(0.8 0.12 60);
}

.msn-04__pickArrow {
  font-size: 26px;
  flex: none;
  transition: translate .25s;
}

.msn-04__pick:hover .msn-04__pickArrow {
  translate: 6px 0;
}

@media (prefers-reduced-motion: no-preference) {
  @keyframes msn04-up {
    from {
      opacity: 0;
      translate: 0 14px;
    }

    to {
      opacity: 1;
      translate: 0 0;
    }
  }

  .msn-04__card,
    .msn-04__pick {
    animation: msn04-up .55s cubic-bezier(.2,.7,.2,1) both;
    animation-delay: min(calc(var(--i)*60ms),720ms);
  }
}

@container msn04 (width < 480px) {
  .msn-04__wall {
    columns: 1;
  }

  .msn-04__pick {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-04 * {
    transition-duration: .01ms !important;
  }
}
```
