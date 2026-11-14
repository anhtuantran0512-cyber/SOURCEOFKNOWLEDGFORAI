---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/neon-left-rail/"
title: "Anchor-Nav Timeline — :target Deep-Linkable Milestones"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "Every milestone is a URL: a year-chip navigation jumps to events down the page, and the :target pseudo-class lights up whichever milestone the hash points at…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Anchor-Nav Timeline — :target Deep-Linkable Milestones
Source: https://codefronts.com/layouts/css-timelines/neon-left-rail/

Every milestone is a URL: a year-chip navigation jumps to events down the page, and the :target pseudo-class lights up whichever milestone the hash points at — spotlight ring, tinted card, raised marker. Share #tls24-2024 and the recipient lands on that exact event, highlighted, with scroll-margin keeping it clear of any sticky header. Zero JavaScript, fully back-button friendly.
## HTML
```html
<section class="tls-23" aria-label="Anchor navigation timeline demo">
  <div class="tls-23__inner">
    <h3 class="tls-23__title">Five years, five links</h3>
    <nav class="tls-23__nav" aria-label="Jump to year">
      <a class="tls-23__chip" href="#tls24-2022">2022</a>
      <a class="tls-23__chip" href="#tls24-2023">2023</a>
      <a class="tls-23__chip" href="#tls24-2024">2024</a>
      <a class="tls-23__chip" href="#tls24-2025">2025</a>
      <a class="tls-23__chip" href="#tls24-2026">2026</a>
    </nav>
    <ol class="tls-23__list" role="list">
      <li class="tls-23__item" id="tls24-2022">
        <div class="tls-23__card"><span class="tls-23__linked">linked</span><time datetime="2022">2022</time><h4>Open-sourced the core engine</h4><p>14k stars in the first year and a community we still can't believe.</p></div>
      </li>
      <li class="tls-23__item" id="tls24-2023">
        <div class="tls-23__card"><span class="tls-23__linked">linked</span><time datetime="2023">2023</time><h4>First conference talk</h4><p>Forty minutes on rendering pipelines; the demo failed live, twice, charmingly.</p></div>
      </li>
      <li class="tls-23__item" id="tls24-2024">
        <div class="tls-23__card"><span class="tls-23__linked">linked</span><time datetime="2024">2024</time><h4>The v1.0 release</h4><p>Two years of nights and weekends compressed into one git tag.</p></div>
      </li>
      <li class="tls-23__item" id="tls24-2025">
        <div class="tls-23__card"><span class="tls-23__linked">linked</span><time datetime="2025">2025</time><h4>Full-time on the project</h4><p>Sponsorships crossed the salary line. The resignation letter was one sentence.</p></div>
      </li>
      <li class="tls-23__item" id="tls24-2026">
        <div class="tls-23__card"><span class="tls-23__linked">linked</span><time datetime="2026">2026</time><h4>The team becomes plural</h4><p>Two maintainers, three time zones, one very long CONTRIBUTING.md.</p></div>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-23,
.tls-23 *,
.tls-23 *::before,
.tls-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-23 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #0d9488;
  --tl-line: #d8ebe8;
  --tl-ink: #134e4a;
  --tl-mut: #6b8f8a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f4faf9;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

@media (prefers-reduced-motion: no-preference) {
  .tls-23 {
    scroll-behavior: smooth;
  }
}

.tls-23__inner {
  width: min(600px,100%);
}

.tls-23__title {
  font-size: clamp(22px,3.5vw,28px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
  margin-bottom: 20px;
}

.tls-23__nav {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 34px;
}

.tls-23__chip {
  font-size: 13px;
  font-weight: 700;
  color: var(--tl-ink);
  text-decoration: none;
  border: 1.5px solid var(--tl-line);
  border-radius: 999px;
  padding: 7px 16px;
  background: #fff;
  transition: border-color .15s,background .15s;
}

.tls-23__chip:hover {
  border-color: var(--tl-accent);
}

.tls-23__chip:focus-visible {
  outline: 2px solid var(--tl-accent);
  outline-offset: 2px;
}

.tls-23__list {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.tls-23__item {
  position: relative;
  padding: 0 0 26px 34px;
  scroll-margin-top: 84px;
}

.tls-23__item::before {
  content: '';
  position: absolute;
  left: 6px;
  top: 24px;
  bottom: -6px;
  width: 2px;
  background: var(--tl-line);
}

.tls-23__item:last-child::before {
  display: none;
}

.tls-23__item::after {
  content: '';
  position: absolute;
  left: 0;
  top: 18px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #fff;
  border: 3.5px solid var(--tl-mut);
  transition: border-color .2s,scale .2s;
}

.tls-23__card {
  position: relative;
  background: #fff;
  border: 1.5px solid var(--tl-line);
  border-radius: 14px;
  padding: 18px 20px;
  transition: border-color .25s,background .25s,box-shadow .25s;
}

.tls-23__card time {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .1em;
  color: var(--tl-mut);
}

.tls-23__card h4 {
  font-size: 16.5px;
  font-weight: 750;
  color: var(--tl-ink);
  margin: 5px 0 5px;
  letter-spacing: -.01em;
}

.tls-23__card p {
  font-size: 14px;
  line-height: 1.6;
  color: var(--tl-mut);
  text-wrap: pretty;
}

.tls-23__linked {
  position: absolute;
  top: 14px;
  right: 16px;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--tl-accent);
  opacity: 0;
  transition: opacity .25s;
}

.tls-23__item:target::after {
  border-color: var(--tl-accent);
  scale: 1.25;
}

.tls-23__item:target .tls-23__card {
  border-color: var(--tl-accent);
  background: #f0fbf9;
  box-shadow: 0 8px 26px -14px rgb(13 148 136 / .45);
}

.tls-23__item:target .tls-23__linked {
  opacity: 1;
}

@media (prefers-reduced-motion: no-preference) {
  .tls-23__item:target .tls-23__card {
    animation: tls-23-pulse 1.2s ease 1;
  }

  @keyframes tls-23-pulse {
    30% {
      box-shadow: 0 0 0 6px rgb(13 148 136 / .18);
    }
  }
}
```

## JavaScript
```js
/* No JavaScript — highlighting is the :target pseudo-class (the URL hash IS the state: shareable, bookmarkable, back-button friendly); scroll-margin-top keeps anchored cards clear of sticky headers. */
```
